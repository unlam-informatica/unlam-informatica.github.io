"""Control de calidad del material publicado de una materia (``src/content/docs/<materia>``).

No mide calidad por cantidad de palabras: verifica condiciones objetivas.

- Cada página tiene ``title`` y ``slug`` con el prefijo de la materia, y contenido real.
- No hay texto provisional (TODO, "en construcción", "lorem ipsum", etc.).
- Cada ejercicio declarado con ``<!-- ejercicio: ID | nivel: … | tipo: … | verificacion: … -->``
  tiene enunciado y resolución, y su identificador es único.
- Los ejercicios con ``verificacion: sympy`` tienen una comprobación aprobada en el
  reporte de ``verify-math``; los de ``verificacion: razonamiento`` se cuentan aparte.
- Mínimos por unidad (cantidad y niveles) declarados en la matriz curricular.
- Los enlaces internos de la materia apuntan a páginas existentes.
- Los temas de la matriz tienen página y sus ejercicios existen.
- Los ejercicios ``motor`` tienen un check aprobado en ``reports/code-verification.json`` y los
  ``revisado`` figuran en ``checks/reviewed.yaml``; una resolución incompleta (bloque de código vacío,
  falta de "Resultado esperado" o del marcador ``<!-- check: ID -->``) no cuenta para los mínimos.
- Operadores MongoDB (``$match``, ``$$NOW``, ``"$campo"``) sin formato de código y montos con ``$``.
- Las fórmulas siguen la convención del portal (``$$`` en líneas propias, ``$`` balanceados).
- Patrones de notación prohibidos declarados en ``subject.yaml`` (``qa.forbidden``).
- Párrafos largos repetidos entre páginas.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .io_utils import atomic_write, read_json, read_yaml, write_json
from .textscan import clean_dollars, strip_inline_code, strip_mongo

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
EXERCISE_RE = re.compile(r"<!--\s*ejercicio:\s*([^|>]+?)\s*((?:\|[^>]*)?)-->")
CHECK_MARKER_RE = re.compile(r"<!--\s*check:\s*([^\s>]+)\s*-->")
LINK_RE = re.compile(r"\]\((/[^)\s#]*)(#[^)\s]*)?\)|href=\"(/[^\"#]*)(#[^\"]*)?\"")
# Los marcadores se buscan solo en mayúsculas: "todo" es una palabra común en español.
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|TBD|FIXME|XXX)\b|(?i:lorem ipsum|en construcci[oó]n|pr[oó]ximamente|"
    r"pendiente de (?:redactar|completar|escribir)|contenido provisional)|\[\s*\.\.\.\s*\]"
)
STATEMENT_RE = re.compile(r"^:::note\[Enunciado\]", re.M)
HTML_MATH_RE = re.compile(r"<(summary|figcaption|text|title|desc)\b[^>]*>(?:(?!</\1>).)*?(?<!\\)\$(?:(?!</\1>).)*?</\1>", re.S)
SOLUTION_RE = re.compile(r"^<summary>\s*Resoluci[oó]n|^:::tip\[Resoluci[oó]n", re.M)
LEVELS = ("inicial", "intermedio", "avanzado")
VERIFICATIONS = ("sympy", "razonamiento", "motor", "revisado")
CODE_FENCE_RE = re.compile(r"^(```|~~~)[^\n]*\n(.*?)^\1[ \t]*$", re.S | re.M)
EXPECTED_RESULT_RE = re.compile(r"resultado\s+esperado", re.I)
_PLACEHOLDER_CODE_LINE_RE = re.compile(r"^(?:…|\.\.\.|#.*|//.*|--.*|/\*.*|\*.*|<!--.*|%%.*)$")


def _strip_code(text: str) -> str:
    return re.sub(r"^(```|~~~).*?^\1", "", text, flags=re.S | re.M)


def _prose(body: str) -> str:
    text = _strip_code(body)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"^\s*(#{1,6}|:::|import |<).*$", "", text, flags=re.M)
    return re.sub(r"\s+", " ", text).strip()


def parse_page(path: Path) -> dict[str, Any]:
    import yaml

    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    front = yaml.safe_load(match.group(1)) if match else None
    body = text[match.end():] if match else text
    return {"path": path, "front": front or {}, "body": body}


def _placeholder_code(code: str) -> bool:
    lines = [line.strip() for line in code.splitlines() if line.strip()]
    return all(_PLACEHOLDER_CODE_LINE_RE.match(line) for line in lines)


def incomplete_reasons(exercise_id: str, verification: str | None, segment: str) -> list[str]:
    """Motivos por los que la resolución de un ejercicio no está completa (lista vacía si lo está)."""
    reasons = []
    blocks = [m.group(2) for m in CODE_FENCE_RE.finditer(segment)]
    if any(_placeholder_code(block) for block in blocks):
        reasons.append("hay un bloque de código vacío o con solo «…» o comentarios")
    if verification in ("motor", "revisado"):
        solution = SOLUTION_RE.search(segment)
        resolution = segment[solution.start():] if solution else ""
        if not (CODE_FENCE_RE.search(resolution) and EXPECTED_RESULT_RE.search(resolution)):
            reasons.append("la resolución no tiene un bloque de código y «Resultado esperado»")
    if verification == "motor":
        ids = {m.group(1) for m in CHECK_MARKER_RE.finditer(segment)}
        if exercise_id not in ids:
            reasons.append(f"falta el marcador <!-- check: {exercise_id} -->")
    return reasons


def parse_exercises(page: dict[str, Any]) -> list[dict[str, Any]]:
    body = page["body"]
    markers = list(EXERCISE_RE.finditer(body))
    exercises = []
    for position, marker in enumerate(markers):
        end = markers[position + 1].start() if position + 1 < len(markers) else len(body)
        segment = body[marker.end():end]
        attributes = {}
        for part in marker.group(2).split("|"):
            if ":" in part:
                key, value = part.split(":", 1)
                attributes[key.strip()] = value.strip()
        exercises.append({
            "id": marker.group(1).strip(),
            "level": attributes.get("nivel"),
            "type": attributes.get("tipo"),
            "verification": attributes.get("verificacion"),
            "has_statement": bool(STATEMENT_RE.search(segment)),
            "has_solution": bool(SOLUTION_RE.search(segment)),
            "incomplete": incomplete_reasons(marker.group(1).strip(), attributes.get("verificacion"), segment),
            "slug": page["front"].get("slug"),
        })
    return exercises


def math_syntax_issues(body: str) -> list[str]:
    issues = []
    text = _strip_code(body)
    in_block = False
    for number, line in enumerate(strip_mongo(text).splitlines(), start=1):
        stripped = line.strip()
        if stripped == "$$":
            in_block = not in_block
            continue
        if "$$" in stripped:
            issues.append(f"línea {number}: '$$' debe ir en una línea propia")
    if in_block:
        issues.append("bloque '$$' sin cerrar")
    for match in HTML_MATH_RE.finditer(text):
        issues.append(f"fórmula dentro de <{match.group(1)}> (KaTeX no la procesa)")
    for paragraph in re.split(r"\n\s*\n", text):
        if paragraph.strip() == "$$" or paragraph.strip().startswith("$$"):
            continue
        clean = clean_dollars(strip_inline_code(paragraph))[0]
        if len(re.findall(r"(?<!\\)\$", clean)) % 2:
            issues.append(f"'$' desbalanceado cerca de: {paragraph.strip()[:60]!r}")
    return issues


def dollar_findings(body: str) -> tuple[list[str], list[str]]:
    """(operadores MongoDB, montos) fuera de código y de código en línea, sin repetir."""
    operators: list[str] = []
    amounts: list[str] = []
    for paragraph in re.split(r"\n\s*\n", _strip_code(body)):
        if paragraph.strip().startswith("$$"):
            continue
        _, ops, amts = clean_dollars(strip_inline_code(paragraph))
        operators += [o for o in ops if o not in operators]
        amounts += [a for a in amts if a not in amounts]
    return operators, amounts


def _load_reviewed(path: Path) -> set[str]:
    data = read_yaml(path) if path.exists() else None
    if isinstance(data, dict):
        data = data.get("reviewed") or data.get("items") or []
    return {str(item["id"]) for item in data or [] if isinstance(item, dict) and "id" in item}


def run_qa(docs_root: Path, subject: str, curriculum_path: Path | None = None, math_report: Path | None = None,
           subject_config: Path | None = None, report_path: Path | None = None) -> dict[str, Any]:
    base = docs_root / subject
    findings: list[dict[str, Any]] = []

    def add(severity: str, code: str, message: str, where: str = "") -> None:
        findings.append({"severity": severity, "code": code, "message": message, "where": where})

    pages = [parse_page(p) for p in sorted(base.rglob("*.md*")) if p.suffix in (".md", ".mdx")]
    if not pages:
        add("error", "sin-paginas", f"No hay páginas en {base}")
    slugs: dict[str, Path] = {}
    exercises: list[dict[str, Any]] = []
    example_checks: list[tuple[str, str]] = []
    paragraphs: dict[str, list[str]] = defaultdict(list)
    forbidden = []
    if subject_config and subject_config.exists():
        forbidden = ((read_yaml(subject_config) or {}).get("qa") or {}).get("forbidden") or []

    for page in pages:
        where = str(page["path"].relative_to(docs_root))
        front, body = page["front"], page["body"]
        slug = front.get("slug")
        if not front.get("title"):
            add("error", "sin-titulo", "Falta 'title' en el frontmatter", where)
        if not slug or not (slug == subject or slug.startswith(subject + "/")):
            add("error", "slug-invalido", f"slug={slug!r}", where)
        elif slug in slugs:
            add("error", "slug-repetido", f"{slug} también en {slugs[slug]}", where)
        else:
            slugs[slug] = page["path"]
        prose = _prose(body)
        if len(prose) < 300:
            add("error", "pagina-vacia", f"Solo {len(prose)} caracteres de texto", where)
        for match in PLACEHOLDER_RE.finditer(_strip_code(body)):
            add("error", "contenido-provisional", f"«{match.group(0)}»", where)
        operators, amounts = dollar_findings(body)
        title_ops = dollar_findings(str(front.get("title") or ""))[0]
        operators += [o for o in title_ops if o not in operators]
        if operators:
            add("error", "operador-mongodb-sin-codigo",
                "Operadores sin formato de código (KaTeX los toma como fórmula): " + ", ".join(operators), where)
        if amounts:
            add("warning", "monto-con-signo-pesos",
                "Montos con '$' fuera de código: " + ", ".join(amounts), where)
        for issue in math_syntax_issues(body):
            add("error", "formula-mal-delimitada", issue, where)
        for rule in forbidden:
            if re.search(rule["pattern"], body):
                add("warning", "notacion", rule.get("message", rule["pattern"]), where)
        for paragraph in re.split(r"\n\s*\n", _strip_code(body)):
            clean = paragraph.strip()
            if len(clean) >= 200 and not clean.startswith(("<!--", "|", "import ")):
                paragraphs[clean].append(where)
        exercises.extend(parse_exercises(page))
        for marker in CHECK_MARKER_RE.finditer(body):
            example_checks.append((marker.group(1), where))

    for text, places in paragraphs.items():
        if len(places) > 1:
            add("warning", "parrafo-duplicado", f"{text[:70]!r}…", ", ".join(sorted(set(places))))

    known = {"/" + s.strip("/") + "/" for s in slugs}
    for page in pages:
        where = str(page["path"].relative_to(docs_root))
        for match in LINK_RE.finditer(page["body"]):
            target = match.group(1) or match.group(3)
            if not target.startswith(f"/{subject}/") and target != f"/{subject}":
                continue
            normalized = target.removesuffix("index.html")
            normalized = normalized if normalized.endswith("/") else normalized + "/"
            if normalized not in known and not (docs_root.parent.parent.parent / "public" / target.lstrip("/")).exists():
                add("error", "enlace-roto", target, where)

    ids = Counter(ex["id"] for ex in exercises)
    for exercise_id, count in ids.items():
        if count > 1:
            add("error", "ejercicio-repetido", f"{exercise_id} aparece {count} veces")
    # Reporte de código (verify-code) y revisiones sin ejecución: se cargan primero porque también
    # respaldan los marcadores <!-- check: ID --> de ejemplos de código.
    code_report_path = curriculum_path.parent / "reports" / "code-verification.json" if curriculum_path else None
    code_status: dict[str, str] = {}
    has_code_report = bool(code_report_path and code_report_path.exists())
    if has_code_report:
        for check in read_json(code_report_path).get("checks") or []:
            # un id con varios checks: el peor estado manda
            current = code_status.get(check["id"])
            if current is None or current == "aprobado":
                code_status[check["id"]] = check["status"]
    reviewed_path = curriculum_path.parent / "checks" / "reviewed.yaml" if curriculum_path else None
    reviewed = _load_reviewed(reviewed_path) if reviewed_path else set()

    engine_ids = {ex["id"] for ex in exercises if ex["verification"] == "motor"}
    example_checks = [(cid, where) for cid, where in example_checks if cid not in engine_ids]
    math_examples = []
    for check_id, where in example_checks:
        if check_id in code_status:
            if code_status[check_id] != "aprobado":
                add("error", "verificacion-fallida", f"La comprobación de código {check_id} no aprueba", where)
        elif check_id not in reviewed:
            math_examples.append((check_id, where))

    passed: set[str] = set()
    failed: set[str] = set()
    if math_report and math_report.exists():
        report = read_json(math_report)
        passed = {r["id"] for r in report["results"] if r["status"] == "passed"}
        failed = {r["id"] for r in report["results"] if r["status"] == "failed"}
    elif any(ex["verification"] == "sympy" for ex in exercises) or math_examples:
        add("error", "sin-reporte-matematico", "No existe el reporte de verify-math")
    for check_id, where in math_examples:
        if check_id in failed:
            add("error", "verificacion-fallida", f"La comprobación {check_id} falla", where)
        elif math_report and math_report.exists() and check_id not in passed:
            add("error", "sin-comprobacion", f"El ejemplo marca {check_id} pero no hay comprobación aprobada", where)
    if engine_ids and not has_code_report:
        add("error", "sin-reporte-de-codigo", "No existe reports/code-verification.json")
    for ex in exercises:
        where = f"/{ex['slug']}/ {ex['id']}"
        if ex["verification"] == "motor" and has_code_report:
            status = code_status.get(ex["id"])
            if status is None:
                add("error", "sin-verificacion-motor", "No hay check de código aprobado con ese identificador", where)
            elif status != "aprobado":
                add("error", "verificacion-motor-fallida", f"El check de código está en estado {status}", where)
        if ex["verification"] == "revisado" and ex["id"] not in reviewed:
            add("error", "sin-revision", "El ejercicio no figura en checks/reviewed.yaml", where)
        for reason in ex["incomplete"]:
            add("error", "resolucion-incompleta", reason, where)
        if not ex["has_statement"]:
            add("error", "sin-enunciado", "Falta :::note[Enunciado]", where)
        if not ex["has_solution"]:
            add("error", "sin-resolucion", "Falta la resolución", where)
        if ex["level"] not in LEVELS:
            add("error", "nivel-invalido", f"nivel={ex['level']!r}", where)
        if ex["verification"] not in VERIFICATIONS:
            add("error", "verificacion-invalida", f"verificacion={ex['verification']!r}", where)
        if ex["verification"] == "sympy" and ex["id"] in failed:
            add("error", "verificacion-fallida", "La comprobación simbólica falla", where)
        elif ex["verification"] == "sympy" and math_report and ex["id"] not in passed:
            add("error", "sin-comprobacion", "No hay comprobación registrada con ese identificador", where)

    units: dict[str, Any] = {}
    if curriculum_path and curriculum_path.exists():
        curriculum = read_yaml(curriculum_path) or {}
        minimum = curriculum.get("minimums") or {}
        by_id = {ex["id"]: ex for ex in exercises}
        for unit in curriculum.get("units") or []:
            prefix = unit.get("exercise_prefix")
            unit_exercises = [ex for ex in exercises if prefix and ex["id"].startswith(prefix)]
            complete = [ex for ex in unit_exercises
                        if ex["has_statement"] and ex["has_solution"] and not ex["incomplete"]]
            levels = Counter(ex["level"] for ex in unit_exercises)
            complete_levels = Counter(ex["level"] for ex in complete)
            units[unit["id"]] = {
                "exercises": len(unit_exercises),
                "levels": dict(levels),
                "sympy": sum(1 for ex in unit_exercises if ex["verification"] == "sympy"),
                "razonamiento": sum(1 for ex in unit_exercises if ex["verification"] == "razonamiento"),
                "motor": sum(1 for ex in unit_exercises if ex["verification"] == "motor"),
                "revisado": sum(1 for ex in unit_exercises if ex["verification"] == "revisado"),
                "complete": len(complete),
                "incomplete": len(unit_exercises) - len(complete),
                "complete_levels": dict(complete_levels),
                "complete_by_verification": dict(Counter(ex["verification"] for ex in complete)),
            }
            min_exercises = unit.get("minimum_exercises", minimum.get("exercises_per_unit", 0))
            min_level = unit.get("minimum_per_level", minimum.get("levels_per_unit"))
            enforce = prefix and unit.get("minimum", True)
            if enforce and len(complete) < min_exercises:
                add("error", "ejercicios-insuficientes", f"{len(complete)} < {min_exercises}", unit["id"])
            if enforce and min_level:
                for level in LEVELS:
                    if complete_levels[level] < min_level:
                        add("error", "nivel-insuficiente", f"{level}: {complete_levels[level]} < {min_level}", unit["id"])
            for topic in unit.get("topics") or []:
                page = topic.get("page")
                if not page:
                    add("error", "tema-sin-pagina", topic["id"], unit["id"])
                elif "/" + page.split("#")[0].strip("/") + "/" not in known:
                    add("error", "tema-sin-pagina", f"{topic['id']} → {page}", unit["id"])
                for exercise_id in topic.get("exercises") or []:
                    if exercise_id not in by_id:
                        add("error", "ejercicio-inexistente", f"{topic['id']} → {exercise_id}", unit["id"])
                if topic.get("production") not in ("redactado", "revisado"):
                    add("error", "tema-no-redactado", f"{topic['id']}: {topic.get('production')}", unit["id"])

    report = {
        "subject": subject,
        "pages": len(pages),
        "exercises": len(exercises),
        "exercises_sympy": sum(1 for ex in exercises if ex["verification"] == "sympy"),
        "exercises_reasoning": sum(1 for ex in exercises if ex["verification"] == "razonamiento"),
        "exercises_engine": sum(1 for ex in exercises if ex["verification"] == "motor"),
        "exercises_reviewed": sum(1 for ex in exercises if ex["verification"] == "revisado"),
        "exercises_complete": sum(1 for ex in exercises if ex["has_statement"] and ex["has_solution"] and not ex["incomplete"]),
        "example_checks": len(example_checks),
        "units": units,
        "errors": sum(1 for f in findings if f["severity"] == "error"),
        "warnings": sum(1 for f in findings if f["severity"] == "warning"),
        "findings": findings,
    }
    if report_path is not None:
        write_json(report_path, report)
        lines = [f"# Control de calidad — {subject}", "",
                 f"- Páginas: {report['pages']} · Ejercicios: {report['exercises']} "
                 f"(SymPy: {report['exercises_sympy']}, razonamiento: {report['exercises_reasoning']}, "
                 f"motor: {report['exercises_engine']}, revisado: {report['exercises_reviewed']}; "
                 f"completos: {report['exercises_complete']})",
                 f"- Errores: **{report['errors']}** · Advertencias: {report['warnings']}", ""]
        if units:
            lines += ["| Unidad | Ejercicios | Inicial | Intermedio | Avanzado | SymPy | Razonamiento | Motor | Revisado | Completos |",
                      "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
            for unit_id, data in units.items():
                lv = data["levels"]
                lines.append(f"| {unit_id} | {data['exercises']} | {lv.get('inicial', 0)} | "
                             f"{lv.get('intermedio', 0)} | {lv.get('avanzado', 0)} | {data['sympy']} | "
                             f"{data['razonamiento']} | {data['motor']} | {data['revisado']} | {data['complete']} |")
            lines.append("")
        for finding in findings:
            lines.append(f"- **{finding['severity']}** `{finding['code']}` {finding['where']} — {finding['message']}")
        atomic_write(report_path.with_suffix(".md"), "\n".join(lines).rstrip() + "\n")
    return report
