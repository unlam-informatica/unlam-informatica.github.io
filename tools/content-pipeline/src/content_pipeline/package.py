"""Paquetes de contexto por unidad o tema, sin RAG ni embeddings.

La selección es determinista y usa metadatos: la matriz curricular
(``curriculum-map.yaml``) dice qué documentos, páginas y palabras clave
corresponden a cada tema; el índice de secciones de la normalización dice dónde
está cada fragmento. Cada paquete incluye solo los fragmentos pertinentes, con
identificador de documento y páginas, para que quien redacta pueda citar y
volver a la fuente sin releer documentos completos.

Salidas (privadas, porque contienen fragmentos de los originales):
``processed/context/<unidad>/<tema>.md`` y ``.json``, y ``processed/context/index.json``.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .config import PipelineError, SubjectPaths
from .ingest import load_catalog
from .io_utils import atomic_write, fold, read_json, read_yaml, write_json
from .logging_utils import get_logger

DEFAULT_BUDGET = 24_000  # caracteres de fragmentos por paquete
FRAGMENT_LIMIT = 4_000  # caracteres por fragmento
EXERCISE_KINDS = ("enunciado", "resolucion")


@dataclass
class Candidate:
    doc_id: str
    section: dict[str, Any]
    score: float
    explicit: bool
    text: str


def load_curriculum(paths: SubjectPaths) -> dict[str, Any]:
    if not paths.curriculum.exists():
        raise PipelineError(f"Falta la matriz curricular {paths.curriculum}")
    data = read_yaml(paths.curriculum) or {}
    units = data.get("units")
    if not isinstance(units, list) or not units:
        raise PipelineError("curriculum-map.yaml debe definir una lista 'units'")
    seen: set[str] = set()
    for unit in units:
        for key in ("id", "title", "topics"):
            if key not in unit:
                raise PipelineError(f"Unidad sin '{key}' en curriculum-map.yaml: {unit.get('id')}")
        for topic in unit["topics"]:
            for key in ("id", "title"):
                if key not in topic:
                    raise PipelineError(f"Tema sin '{key}' en la unidad {unit['id']}")
            if topic["id"] in seen:
                raise PipelineError(f"Tema repetido en curriculum-map.yaml: {topic['id']}")
            seen.add(topic["id"])
    return data


def iter_topics(curriculum: dict[str, Any]):
    for unit in curriculum["units"]:
        for topic in unit["topics"]:
            yield unit, topic


def _pages_overlap(section: dict[str, Any], pages: list[int] | None) -> bool:
    if not pages:
        return False
    start, end = section.get("page_start"), section.get("page_end")
    if start is None:
        return False
    low, high = (pages[0], pages[-1]) if len(pages) > 1 else (pages[0], pages[0])
    return not (end or start) < low and not start > high


def score_section(title: str, body: str, keywords: list[str]) -> float:
    folded_title, folded_body = fold(title), fold(body)
    score = 0.0
    for keyword in keywords:
        needle = fold(keyword)
        if not needle:
            continue
        if needle in folded_title:
            score += 3
        score += min(folded_body.count(needle), 5)
    return score


def _source_specs(topic: dict[str, Any]) -> list[dict[str, Any]]:
    specs = []
    for source in topic.get("sources") or []:
        spec = {"doc": source} if isinstance(source, str) else dict(source)
        if "doc" not in spec:
            raise PipelineError(f"Fuente sin 'doc' en el tema {topic['id']}")
        pages = spec.get("pages")
        if pages is not None and (not isinstance(pages, list) or not all(isinstance(p, int) for p in pages)):
            raise PipelineError(f"'pages' debe ser una lista de enteros en el tema {topic['id']}")
        specs.append(spec)
    return specs


def collect_candidates(paths: SubjectPaths, unit: dict[str, Any], topic: dict[str, Any],
                       catalog: dict[str, Any], cache: dict[str, Any]) -> tuple[list[Candidate], list[str]]:
    """Secciones candidatas y advertencias de fuentes que no se pudieron usar."""
    warnings: list[str] = []
    keywords = list(topic.get("keywords") or []) + [topic["title"]]
    specs = {spec["doc"]: spec for spec in _source_specs(topic)}
    documents = {d["id"]: d for d in catalog["documents"]}
    doc_ids = list(specs)
    if topic.get("auto_sources", True):
        doc_ids += [d["id"] for d in catalog["documents"]
                    if unit["id"] in (d.get("units") or []) and d["id"] not in specs
                    and d.get("doc_type") != "bibliografia"]
    candidates: list[Candidate] = []
    for doc_id in doc_ids:
        if doc_id not in documents:
            warnings.append(f"{doc_id}: no existe en el catálogo")
            continue
        index_path = paths.index / f"{doc_id}.json"
        text_path = paths.normalized / f"{doc_id}.md"
        if not index_path.exists() or not text_path.exists():
            if doc_id in specs:
                warnings.append(f"{doc_id}: todavía no fue extraído ni normalizado")
            continue
        if doc_id not in cache:
            cache[doc_id] = (read_json(index_path), text_path.read_text(encoding="utf-8"))
        index, text = cache[doc_id]
        status = index.get("extraction_status")
        if status == "partial" and doc_id in specs:
            warnings.append(f"{doc_id}: extracción parcial; revisar contra el original")
        spec = specs.get(doc_id, {})
        for section in index["sections"]:
            body = text[section["start"]:section["end"]]
            explicit = _pages_overlap(section, spec.get("pages")) or section["section_id"] in (spec.get("sections") or [])
            score = score_section(section["title"], body, keywords)
            if doc_id in specs and not spec.get("pages") and not spec.get("sections"):
                score += 1  # documento asignado al tema sin páginas: leve preferencia
            if explicit or score >= 2:
                candidates.append(Candidate(doc_id, section, score + (100 if explicit else 0), explicit, body))
    candidates.sort(key=lambda c: (-c.score, c.doc_id, c.section["start"]))
    return candidates, warnings


def _page_label(section: dict[str, Any]) -> str:
    start, end = section.get("page_start"), section.get("page_end")
    if start is None:
        return "s/p"
    return f"p. {start}" if end in (None, start) else f"pp. {start}–{end}"


def _trim(text: str, limit: int) -> tuple[str, bool]:
    if len(text) <= limit:
        return text.strip(), False
    cut = text.rfind("\n\n", 0, limit)
    cut = cut if cut > limit // 2 else limit
    return text[:cut].rstrip(), True


def build_package(paths: SubjectPaths, curriculum: dict[str, Any], unit: dict[str, Any], topic: dict[str, Any],
                  catalog: dict[str, Any], cache: dict[str, Any], budget: int = DEFAULT_BUDGET) -> dict[str, Any]:
    candidates, warnings = collect_candidates(paths, unit, topic, catalog, cache)
    bibliography = {entry["id"]: entry for entry in curriculum.get("bibliography") or []}
    fragments: list[dict[str, Any]] = []
    exercises: list[dict[str, Any]] = []
    used = 0
    for candidate in candidates:
        section = candidate.section
        reference = {
            "doc": candidate.doc_id,
            "section": section["section_id"],
            "title": section["title"],
            "pages": _page_label(section),
            "kind": section["kind"],
            "flags": section.get("flags") or [],
            "explicit": candidate.explicit,
            "score": candidate.score,
        }
        if section["kind"] in EXERCISE_KINDS:
            exercises.append(reference)
        if used >= budget and not candidate.explicit:
            continue
        text, truncated = _trim(candidate.text, min(FRAGMENT_LIMIT, max(budget - used, 600)))
        used += len(text)
        fragments.append({**reference, "truncated": truncated, "text": text})
        for flag in reference["flags"]:
            warnings.append(f"{candidate.doc_id} {reference['pages']} «{section['title']}»: {flag}")

    gaps: list[str] = []
    if not fragments:
        gaps.append("sin-material-fuente")
    if not exercises:
        gaps.append("sin-ejercicios-de-referencia")
    missing_refs = [ref for ref in topic.get("bibliography") or [] if ref.split(":")[0] not in bibliography]
    if missing_refs:
        warnings.append(f"Referencias bibliográficas inexistentes: {missing_refs}")
    return {
        "subject": paths.subject,
        "unit": {"id": unit["id"], "title": unit["title"]},
        "topic": {key: topic.get(key) for key in ("id", "title", "program_text", "objectives", "prerequisites",
                                                   "page", "exercises", "production", "validation")},
        "bibliography": [
            {**bibliography[ref.split(":")[0]], "locator": ref.split(":", 1)[1] if ":" in ref else None}
            for ref in topic.get("bibliography") or [] if ref.split(":")[0] in bibliography
        ],
        "fragments": fragments,
        "exercises": exercises,
        "warnings": sorted(set(warnings)),
        "gaps": gaps,
        "budget": {"chars": budget, "used": used},
    }


def render_package(package: dict[str, Any]) -> str:
    topic, unit = package["topic"], package["unit"]
    lines = [
        f"# Contexto — {topic['title']}",
        "",
        f"- Materia: `{package['subject']}` · Unidad: {unit['title']} (`{unit['id']}`) · Tema: `{topic['id']}`",
        f"- Página prevista: `{topic.get('page') or 'sin asignar'}`",
        "- Uso: material privado de referencia. Redactar con palabras propias y citar `doc` + páginas.",
        "",
    ]
    if topic.get("program_text"):
        lines += ["## Contenido del programa", "", topic["program_text"].strip(), ""]
    if topic.get("objectives"):
        lines += ["## Objetivos", ""] + [f"- {o}" for o in topic["objectives"]] + [""]
    if topic.get("prerequisites"):
        lines += ["## Conocimientos previos", ""] + [f"- {p}" for p in topic["prerequisites"]] + [""]
    if package["bibliography"]:
        lines += ["## Bibliografía", ""]
        for entry in package["bibliography"]:
            locator = f" — {entry['locator']}" if entry.get("locator") else ""
            lines.append(f"- {entry.get('citation', entry['id'])}{locator}")
        lines.append("")
    lines += ["## Advertencias", ""] + ([f"- {w}" for w in package["warnings"]] or ["- Ninguna."]) + [""]
    lines += ["## Faltantes", ""] + ([f"- {g}" for g in package["gaps"]] or ["- Ninguno."]) + [""]
    if package["exercises"]:
        lines += ["## Ejercicios de referencia", ""]
        for ex in package["exercises"]:
            lines.append(f"- `{ex['doc']}` {ex['pages']} — {ex['title']} ({ex['kind']})")
        lines.append("")
    lines += ["## Fragmentos", ""]
    for fragment in package["fragments"]:
        marker = " · asignado" if fragment["explicit"] else ""
        cut = " · recortado" if fragment["truncated"] else ""
        lines += [
            f"### [{fragment['doc']} · {fragment['pages']}] {fragment['title']}",
            "",
            f"<!-- section: {fragment['section']} | kind: {fragment['kind']}{marker}{cut} -->",
            "",
            fragment["text"],
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def run_package(paths: SubjectPaths, unit_id: str | None = None, topic_id: str | None = None,
                budget: int = DEFAULT_BUDGET) -> dict[str, Any]:
    log = get_logger()
    curriculum = load_curriculum(paths)
    catalog = load_catalog(paths)
    cache: dict[str, Any] = {}
    index: list[dict[str, Any]] = []
    matched = False
    for unit, topic in iter_topics(curriculum):
        if unit_id and unit["id"] != unit_id:
            continue
        if topic_id and topic["id"] != topic_id:
            continue
        matched = True
        package = build_package(paths, curriculum, unit, topic, catalog, cache, budget)
        base = paths.context / unit["id"] / topic["id"]
        write_json(base.with_suffix(".json"), package)
        atomic_write(base.with_suffix(".md"), render_package(package))
        index.append({
            "unit": unit["id"],
            "topic": topic["id"],
            "file": f"{unit['id']}/{topic['id']}.md",
            "fragments": len(package["fragments"]),
            "exercises": len(package["exercises"]),
            "warnings": len(package["warnings"]),
            "gaps": package["gaps"],
        })
    if not matched:
        raise PipelineError(f"No hay temas que coincidan con unidad={unit_id!r} tema={topic_id!r}")
    if not unit_id and not topic_id:
        write_json(paths.context / "index.json", index)
    gaps = [entry["topic"] for entry in index if "sin-material-fuente" in entry["gaps"]]
    log.info("paquetes generados", extra={"packages": len(index), "topics_without_sources": len(gaps)})
    return {"packages": len(index), "topics_without_sources": gaps, "index": index}
