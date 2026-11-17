"""Validación documental y curricular, con reportes interpretables.

Nunca falla por un documento individual: acumula hallazgos con severidad
``error`` (impide usar el resultado), ``warning`` (requiere revisión manual) o
``info``. El código de salida de la CLI depende solo de los errores.

Reportes: ``processed/reports/validation.json`` y ``validation.md``.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Any

from .config import SubjectPaths
from .extract import load_manifest, resolve_profile
from .ingest import load_catalog
from .io_utils import atomic_write, read_json, write_json
from .logging_utils import get_logger
from .package import iter_topics, load_curriculum

PDF_PAGE_RE = re.compile(rb"/Type\s*/Page(?![a-zA-Z])")
REQUIRED_METADATA = ("doc_type", "license", "source")
PRODUCTION_STATES = ("pendiente", "en-redaccion", "redactado", "revisado")
VALIDATION_STATES = ("pendiente", "verificado", "revisado", "con-observaciones")


def pdf_page_count(path: Path) -> int | None:
    """Estimación sin dependencias: cuenta objetos /Type /Page. Devuelve None si no es fiable."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if b"/ObjStm" in data:  # los objetos comprimidos ocultan las páginas al conteo directo
        return None
    count = len(PDF_PAGE_RE.findall(data))
    return count or None


class Findings:
    def __init__(self) -> None:
        self.items: list[dict[str, Any]] = []

    def add(self, severity: str, code: str, message: str, **context: Any) -> None:
        self.items.append({"severity": severity, "code": code, "message": message, **context})

    def count(self, severity: str) -> int:
        return sum(1 for item in self.items if item["severity"] == severity)


def validate_documents(paths: SubjectPaths, findings: Findings) -> dict[str, Any]:
    catalog = load_catalog(paths)
    manifest = load_manifest(paths)["documents"]
    stats: Counter[str] = Counter()
    for document in catalog["documents"]:
        doc_id, path = document["id"], document["path"]
        stats["documents"] += 1
        if document.get("status") == "ausente":
            findings.add("warning", "archivo-ausente", "El documento ya no está en raw/", doc=doc_id, path=path)
            continue
        if document.get("duplicate_paths"):
            stats["with_duplicates"] += 1
            findings.add("info", "duplicado", f"{len(document['duplicate_paths'])} copia(s) idéntica(s)",
                         doc=doc_id, path=path, duplicates=document["duplicate_paths"])
        for field in REQUIRED_METADATA:
            if document.get(field) in (None, "", "otro", "sin-determinar"):
                findings.add("warning", "metadato-faltante", f"Falta '{field}'", doc=doc_id, path=path)
        if document.get("doc_type") == "otro":
            findings.add("warning", "sin-clasificar", "Documento sin clasificar", doc=doc_id, path=path)
        profile, _ = resolve_profile(document)
        if profile == "skip":
            stats["skipped"] += 1
            continue
        record = manifest.get(doc_id)
        if record is None:
            stats["pending"] += 1
            findings.add("warning", "sin-extraer", "Pendiente de extracción", doc=doc_id, path=path)
            continue
        if record.get("sha256") != document["sha256"]:
            findings.add("error", "extraccion-desactualizada", "El original cambió desde la extracción",
                         doc=doc_id, path=path)
        if record["status"] == "failure":
            stats["failed"] += 1
            findings.add("error", "error-de-conversion", "; ".join(record.get("errors") or ["sin detalle"]),
                         doc=doc_id, path=path)
            continue
        stats["extracted"] += 1
        if record["status"] == "partial":
            findings.add("warning", "conversion-parcial", "; ".join(record.get("errors") or ["sin detalle"]),
                         doc=doc_id, path=path)
        for warning in record.get("warnings") or []:
            findings.add("warning", "advertencia-de-extraccion", warning, doc=doc_id, path=path)
        extracted_stats = record.get("stats") or {}
        if extracted_stats.get("formulas_undecoded"):
            findings.add("warning", "formulas-no-decodificadas",
                         f"{extracted_stats['formulas_undecoded']} fórmula(s) sin LaTeX", doc=doc_id, path=path)
        if document["format"] == "pdf" and profile in ("full", "text"):
            expected = pdf_page_count(paths.raw / path)
            got = extracted_stats.get("pages")
            if expected and got is not None and got < expected:
                findings.add("error", "paginas-perdidas", f"Se extrajeron {got} de {expected} páginas",
                             doc=doc_id, path=path)
        index_path = paths.index / f"{doc_id}.json"
        if not index_path.exists():
            findings.add("warning", "sin-normalizar", "Pendiente de normalización", doc=doc_id, path=path)
            continue
        index = read_json(index_path)
        report = index["report"]
        if index.get("sha256") != document["sha256"]:
            findings.add("error", "indice-desactualizado", "El índice no corresponde al original",
                         doc=doc_id, path=path)
        if report.get("pages") and len(report.get("empty_pages") or []) == report["pages"]:
            findings.add("error", "sin-texto", "Ninguna página tiene texto (¿escaneo sin OCR?)",
                         doc=doc_id, path=path)
        elif report.get("empty_pages"):
            findings.add("warning", "paginas-vacias", f"Páginas sin texto: {report['empty_pages']}",
                         doc=doc_id, path=path)
        if not report.get("headings") and not report.get("pseudo_headings") and (report.get("pages") or 0) > 2:
            findings.add("warning", "sin-estructura", "No se detectaron títulos ni secciones",
                         doc=doc_id, path=path)
        if report.get("empty_sections"):
            findings.add("warning", "secciones-vacias", f"Secciones sin contenido: {report['empty_sections']}",
                         doc=doc_id, path=path)
        for section in index["sections"]:
            for flag in section.get("flags") or []:
                if flag == "seccion-vacia":
                    continue
                pages = section.get("page_start")
                findings.add("warning", f"formula-dudosa:{flag}",
                             f"«{section['title']}» ({'p. ' + str(pages) if pages else 's/p'})",
                             doc=doc_id, path=path, section=section["section_id"])
    return dict(stats)


def validate_curriculum(paths: SubjectPaths, findings: Findings, docs_root: Path | None) -> dict[str, Any]:
    if not paths.curriculum.exists():
        findings.add("warning", "sin-matriz", "No existe curriculum-map.yaml")
        return {}
    curriculum = load_curriculum(paths)
    catalog = {d["id"]: d for d in load_catalog(paths)["documents"]}
    bibliography = {entry["id"] for entry in curriculum.get("bibliography") or []}
    stats: Counter[str] = Counter()
    for unit, topic in iter_topics(curriculum):
        topic_id = topic["id"]
        stats["topics"] += 1
        production = topic.get("production", "pendiente")
        validation = topic.get("validation", "pendiente")
        stats[f"production:{production}"] += 1
        stats[f"validation:{validation}"] += 1
        if production not in PRODUCTION_STATES:
            findings.add("error", "estado-invalido", f"production={production!r}", topic=topic_id)
        if validation not in VALIDATION_STATES:
            findings.add("error", "estado-invalido", f"validation={validation!r}", topic=topic_id)
        if not topic.get("objectives"):
            findings.add("warning", "sin-objetivos", "Tema sin objetivos de aprendizaje", topic=topic_id)
        for source in topic.get("sources") or []:
            doc_id = source if isinstance(source, str) else source.get("doc")
            if doc_id not in catalog:
                findings.add("error", "referencia-invalida", f"Fuente inexistente {doc_id}", topic=topic_id)
        for ref in topic.get("bibliography") or []:
            if ref.split(":")[0] not in bibliography:
                findings.add("error", "referencia-invalida", f"Bibliografía inexistente {ref}", topic=topic_id)
        page = topic.get("page")
        if not page:
            findings.add("warning", "sin-pagina", "Tema sin página asignada", topic=topic_id)
        elif docs_root is not None:
            relative = page.strip("/").split("#")[0]
            candidates = [docs_root / f"{relative}.md", docs_root / f"{relative}.mdx",
                          docs_root / relative / "index.md", docs_root / relative / "index.mdx"]
            if not any(candidate.exists() for candidate in candidates):
                severity = "error" if production in ("redactado", "revisado") else "warning"
                findings.add(severity, "pagina-inexistente", f"No existe {page}", topic=topic_id)
        if production in ("redactado", "revisado") and not topic.get("exercises"):
            findings.add("warning", "sin-ejercicios", "Tema redactado sin ejercicios asociados", topic=topic_id)
    return dict(stats)


def render_report(report: dict[str, Any]) -> str:
    lines = [
        f"# Validación — {report['subject']}",
        "",
        f"- Errores: **{report['errors']}** · Advertencias: **{report['warnings']}** · Información: {report['info']}",
        f"- Documentos: {report['documents']}",
        f"- Matriz curricular: {report['curriculum']}",
        "",
    ]
    by_code: dict[str, list[dict[str, Any]]] = {}
    for item in report["findings"]:
        by_code.setdefault(f"{item['severity']} · {item['code']}", []).append(item)
    for key in sorted(by_code, key=lambda k: ({"error": 0, "warning": 1, "info": 2}[k.split(" ·")[0]], k)):
        items = by_code[key]
        lines += [f"## {key} ({len(items)})", ""]
        for item in items:
            where = item.get("path") or item.get("topic") or ""
            lines.append(f"- `{item.get('doc') or item.get('topic') or '-'}` {where} — {item['message']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def run_validate(paths: SubjectPaths, docs_root: Path | None = None) -> dict[str, Any]:
    findings = Findings()
    documents = validate_documents(paths, findings)
    curriculum = validate_curriculum(paths, findings, docs_root)
    report = {
        "subject": paths.subject,
        "errors": findings.count("error"),
        "warnings": findings.count("warning"),
        "info": findings.count("info"),
        "documents": documents,
        "curriculum": curriculum,
        "findings": findings.items,
    }
    write_json(paths.reports / "validation.json", report)
    atomic_write(paths.reports / "validation.md", render_report(report))
    get_logger().info("validación terminada", extra={k: report[k] for k in ("errors", "warnings", "info")})
    return report
