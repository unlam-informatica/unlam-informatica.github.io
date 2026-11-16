"""Ingesta: inventario de ``raw/``, hashes SHA-256, duplicados, clasificación y catálogo.

El catálogo tiene una entrada por contenido único (hash). Las copias idénticas se
registran en ``duplicate_paths`` y no se procesan dos veces. Los campos de
clasificación de una entrada existente no se pisan: se pueden corregir a mano y
sobreviven a nuevas ejecuciones (salvo ``reclassify=True``).
"""
from __future__ import annotations

import fnmatch
from collections import Counter
from pathlib import Path
from typing import Any

from .config import PipelineError, SubjectPaths, load_subject_config
from .io_utils import fold, nfc, read_yaml, sha256_file, write_json, write_yaml
from .logging_utils import get_logger

SCHEMA_VERSION = 1

FORMATS: dict[str, str] = {
    ".pdf": "pdf",
    ".docx": "docx",
    ".pptx": "pptx",
    ".xlsx": "xlsx",
    ".md": "markdown",
    ".html": "html",
    ".htm": "html",
    ".jpg": "image",
    ".jpeg": "image",
    ".png": "image",
    ".tif": "image",
    ".tiff": "image",
    ".bmp": "image",
    ".webp": "image",
    ".mp3": "audio",
    ".wav": "audio",
    ".m4a": "audio",
    ".flac": "audio",
    ".ogg": "audio",
    ".mp4": "video",
    ".mov": "video",
    ".mkv": "video",
    ".webm": "video",
    ".avi": "video",
}

#: Campos que definen la clasificación y que una persona puede corregir en el catálogo.
CLASSIFICATION_FIELDS = (
    "doc_type",
    "units",
    "topics",
    "source",
    "version",
    "license",
    "distribution",
    "extraction",
    "notes",
)

CATALOG_HEADER = (
    "Catálogo de procedencia generado por `content-pipeline inventory`.\n"
    "Una entrada por contenido único (SHA-256). Las rutas son relativas a raw/.\n"
    "Los campos de clasificación pueden corregirse a mano: la ingesta no los pisa."
)


def _is_ignored(relative: Path) -> bool:
    return any(part.startswith(".") or part.startswith("~$") for part in relative.parts)


def scan_raw(raw: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Recorre ``raw`` y devuelve (archivos compatibles, archivos omitidos)."""
    if not raw.is_dir():
        raise PipelineError(f"No existe la carpeta de documentos originales: {raw}")
    files: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    for path in sorted(raw.rglob("*"), key=lambda p: nfc(p.relative_to(raw).as_posix())):
        if not path.is_file():
            continue
        relative = path.relative_to(raw)
        if _is_ignored(relative):
            continue
        relative_text = nfc(relative.as_posix())
        size = path.stat().st_size
        fmt = FORMATS.get(path.suffix.lower())
        if fmt is None:
            skipped.append({"path": relative_text, "reason": "formato-no-compatible", "size_bytes": size})
            continue
        files.append({
            "path": relative_text,
            "format": fmt,
            "size_bytes": size,
            "sha256": sha256_file(path),
        })
    return files, skipped


def classify(relative_path: str, config: dict[str, Any]) -> dict[str, Any]:
    """Aplica las reglas de ``subject.yaml`` en orden; las posteriores pisan a las anteriores.

    ``match`` usa comodines de ``fnmatch`` sobre la ruta relativa, sin distinguir
    mayúsculas ni acentos. ``*`` también cruza separadores de carpeta.
    """
    result = {field: config["defaults"].get(field) for field in CLASSIFICATION_FIELDS}
    result["units"] = list(result["units"] or [])
    result["topics"] = list(result["topics"] or [])
    matched = False
    target = fold(relative_path)
    for rule in config["rules"]:
        patterns = rule["match"] if isinstance(rule["match"], list) else [rule["match"]]
        if not any(fnmatch.fnmatchcase(target, fold(nfc(str(pattern)))) for pattern in patterns):
            continue
        matched = True
        for field in CLASSIFICATION_FIELDS:
            if field in rule:
                value = rule[field]
                result[field] = list(value) if isinstance(value, list) else value
    result["_matched"] = matched
    return result


def _review_reasons(entry: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if entry["size_bytes"] == 0:
        reasons.append("archivo-vacio")
    if entry["doc_type"] == "otro":
        reasons.append("sin-clasificar")
    if not entry["units"] and entry["doc_type"] not in ("bibliografia", "fuera-de-programa"):
        reasons.append("sin-unidad")
    if entry["license"] in (None, "sin-determinar"):
        reasons.append("licencia-sin-determinar")
    if not entry["source"]:
        reasons.append("sin-fuente")
    return reasons


def load_catalog(paths: SubjectPaths) -> dict[str, Any]:
    if not paths.catalog.exists():
        return {"schema_version": SCHEMA_VERSION, "subject": paths.subject, "documents": []}
    catalog = read_yaml(paths.catalog) or {}
    if not isinstance(catalog, dict) or not isinstance(catalog.get("documents", []), list):
        raise PipelineError(f"{paths.catalog} no tiene el formato esperado")
    catalog.setdefault("documents", [])
    return catalog


def save_catalog(paths: SubjectPaths, catalog: dict[str, Any]) -> bool:
    documents = catalog["documents"]
    catalog["summary"] = {
        "documents": len(documents),
        "duplicate_files": sum(len(d.get("duplicate_paths") or []) for d in documents),
        "total_bytes": sum(d.get("size_bytes", 0) for d in documents),
        "by_format": dict(sorted(Counter(d["format"] for d in documents).items())),
        "by_type": dict(sorted(Counter(d["doc_type"] for d in documents).items())),
        "by_status": dict(sorted(Counter(d["status"] for d in documents).items())),
        "needs_review": sum(1 for d in documents if d.get("needs_review")),
    }
    ordered = {
        "schema_version": SCHEMA_VERSION,
        "subject": catalog.get("subject", paths.subject),
        "summary": catalog["summary"],
        "documents": documents,
    }
    return write_yaml(paths.catalog, ordered, header=CATALOG_HEADER)


def document_by_id(catalog: dict[str, Any], doc_id: str) -> dict[str, Any]:
    for document in catalog["documents"]:
        if document["id"] == doc_id:
            return document
    raise PipelineError(f"El catálogo no contiene el documento {doc_id}")


def run_inventory(paths: SubjectPaths, reclassify: bool = False) -> dict[str, Any]:
    """Actualiza ``catalog.yaml`` a partir de ``raw/`` y devuelve un resumen."""
    log = get_logger()
    config = load_subject_config(paths)
    prefix = config.get("id_prefix") or paths.subject
    files, skipped = scan_raw(paths.raw)

    by_hash: dict[str, list[dict[str, Any]]] = {}
    for item in files:
        by_hash.setdefault(item["sha256"], []).append(item)

    previous = {d["sha256"]: d for d in load_catalog(paths)["documents"]}
    documents: list[dict[str, Any]] = []
    added = 0
    for sha256, group in by_hash.items():
        group.sort(key=lambda item: (item["path"].count("/"), item["path"]))
        canonical, duplicates = group[0], group[1:]
        old = previous.pop(sha256, None)
        # Conservar la ruta canónica anterior si todavía existe evita cambios espurios.
        if old and old.get("path") in {item["path"] for item in group}:
            canonical = next(item for item in group if item["path"] == old["path"])
            duplicates = [item for item in group if item is not canonical]
        classification = classify(canonical["path"], config)
        matched = classification.pop("_matched")
        entry: dict[str, Any] = {
            "id": f"{prefix}-{sha256[:12]}",
            "original_name": canonical["path"].rsplit("/", 1)[-1],
            "path": canonical["path"],
            "duplicate_paths": sorted(item["path"] for item in duplicates),
            "format": canonical["format"],
            "size_bytes": canonical["size_bytes"],
            "sha256": sha256,
        }
        if old and not reclassify:
            for field in CLASSIFICATION_FIELDS:
                entry[field] = old.get(field, classification[field])
            entry["status"] = old.get("status", "inventariado")
        else:
            entry.update(classification)
            entry["status"] = (old or {}).get("status", "inventariado")
            if old and old.get("notes") and not classification.get("notes"):
                entry["notes"] = old["notes"]
            if not matched:
                log.warning("documento sin regla de clasificación", extra={"path": canonical["path"]})
        if entry["extraction"] == "skip" and entry["status"] == "inventariado":
            entry["status"] = "omitido"
        entry["needs_review"] = _review_reasons(entry)
        if old is None:
            added += 1
        documents.append(entry)

    missing = 0
    for old in previous.values():
        # No se elimina información: el documento ya no está en raw/, pero su registro queda.
        old["status"] = "ausente"
        old.setdefault("duplicate_paths", [])
        old["needs_review"] = sorted(set(old.get("needs_review") or []) | {"archivo-ausente"})
        documents.append(old)
        missing += 1

    documents.sort(key=lambda d: d["path"])
    ids = Counter(d["id"] for d in documents)
    collisions = [doc_id for doc_id, count in ids.items() if count > 1]
    if collisions:
        raise PipelineError(f"Identificadores repetidos en el catálogo: {collisions}")

    catalog = {"subject": paths.subject, "documents": documents}
    changed = save_catalog(paths, catalog)
    summary = {
        "subject": paths.subject,
        "files_scanned": len(files),
        "unique_documents": len(by_hash),
        "duplicate_files": len(files) - len(by_hash),
        "new_documents": added,
        "missing_documents": missing,
        "skipped_files": skipped,
        "needs_review": sum(1 for d in documents if d["needs_review"]),
        "catalog_changed": changed,
    }
    write_json(paths.reports / "inventory.json", summary)
    log.info("inventario actualizado", extra={k: v for k, v in summary.items() if k != "skipped_files"})
    for item in skipped:
        log.warning("archivo omitido", extra=item)
    return summary
