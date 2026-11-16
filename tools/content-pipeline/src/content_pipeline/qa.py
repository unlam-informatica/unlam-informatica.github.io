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

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
EXERCISE_RE = re.compile(r"<!--\s*ejercicio:\s*([^|>]+?)\s*((?:\|[^>]*)?)-->")
CHECK_MARKER_RE = re.compile(r"<!--\s*check:\s*([^\s>]+)\s*-->")
LINK_RE = re.compile(r"\]\((/[^)\s#]*)(#[^)\s]*)?\)|href=\"(/[^\"#]*)(#[^\"]*)?\"")
PLACEHOLDER_RE = re.compile(
    r"\b(TODO|TBD|FIXME|XXX)\b|lorem ipsum|en construcci[oó]n|pr[oó]ximamente|"
    r"pendiente de (redactar|completar|escribir)|contenido provisional|\[\s*\.\.\.\s*\]",
    re.IGNORECASE,
)
STATEMENT_RE = re.compile(r"^:::note\[Enunciado\]", re.M)
SOLUTION_RE = re.compile(r"^<summary>\s*Resoluci[oó]n|^:::tip\[Resoluci[oó]n", re.M)
LEVELS = ("inicial", "intermedio", "avanzado")
VERIFICATIONS = ("sympy", "razonamiento")


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
            "slug": page["front"].get("slug"),
        })
    return exercises


def math_syntax_issues(body: str) -> list[str]:
    issues = []
    text = _strip_code(body)
    in_block = False
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped == "$$":
            in_block = not in_block
            continue
        if "$$" in stripped:
            issues.append(f"línea {number}: '$$' debe ir en una línea propia")
    if in_block:
        issues.append("bloque '$$' sin cerrar")
    for paragraph in re.split(r"\n\s*\n", text):
        if paragraph.strip() == "$$" or paragraph.strip().startswith("$$"):
            continue
        clean = re.sub(r"`[^`]*`", "", paragraph)
        if len(re.findall(r"(?<!\\)\$", clean)) % 2:
            issues.append(f"'$' desbalanceado cerca de: {paragraph.strip()[:60]!r}")
    return issues


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
    passed: set[str] = set()
    failed: set[str] = set()
    if math_report and math_report.exists():
        report = read_json(math_report)
        passed = {r["id"] for r in report["results"] if r["status"] == "passed"}
        failed = {r["id"] for r in report["results"] if r["status"] == "failed"}
    elif any(ex["verification"] == "sympy" for ex in exercises) or example_checks:
        add("error", "sin-reporte-matematico", "No existe el reporte de verify-math")
    for check_id, where in example_checks:
        if check_id in failed:
            add("error", "verificacion-fallida", f"La comprobación {check_id} falla", where)
        elif math_report and check_id not in passed:
            add("error", "sin-comprobacion", f"El ejemplo marca {check_id} pero no hay comprobación aprobada", where)
    for ex in exercises:
        where = f"/{ex['slug']}/ {ex['id']}"
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
            levels = Counter(ex["level"] for ex in unit_exercises)
            units[unit["id"]] = {
                "exercises": len(unit_exercises),
                "levels": dict(levels),
                "sympy": sum(1 for ex in unit_exercises if ex["verification"] == "sympy"),
                "razonamiento": sum(1 for ex in unit_exercises if ex["verification"] == "razonamiento"),
            }
            enforce = prefix and unit.get("minimum", True)
            if enforce and len(unit_exercises) < minimum.get("exercises_per_unit", 0):
                add("error", "ejercicios-insuficientes",
                    f"{len(unit_exercises)} < {minimum['exercises_per_unit']}", unit["id"])
            if enforce and minimum.get("levels_per_unit"):
                for level in LEVELS:
                    if levels[level] < minimum["levels_per_unit"]:
                        add("error", "nivel-insuficiente", f"{level}: {levels[level]}", unit["id"])
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
                 f"(SymPy: {report['exercises_sympy']}, razonamiento: {report['exercises_reasoning']})",
                 f"- Errores: **{report['errors']}** · Advertencias: {report['warnings']}", ""]
        if units:
            lines += ["| Unidad | Ejercicios | Inicial | Intermedio | Avanzado | SymPy | Razonamiento |",
                      "|---|---:|---:|---:|---:|---:|---:|"]
            for unit_id, data in units.items():
                lv = data["levels"]
                lines.append(f"| {unit_id} | {data['exercises']} | {lv.get('inicial', 0)} | "
                             f"{lv.get('intermedio', 0)} | {lv.get('avanzado', 0)} | {data['sympy']} | "
                             f"{data['razonamiento']} |")
            lines.append("")
        for finding in findings:
            lines.append(f"- **{finding['severity']}** `{finding['code']}` {finding['where']} — {finding['message']}")
        atomic_write(report_path.with_suffix(".md"), "\n".join(lines).rstrip() + "\n")
    return report
