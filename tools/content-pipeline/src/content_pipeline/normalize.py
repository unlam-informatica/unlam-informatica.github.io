"""Normalización: limpia la estructura del Markdown extraído sin tocar su significado.

Reglas de seguridad matemática:

- Nunca se edita el interior de ``$...$``, ``$$...$$`` ni de bloques de código.
- Una expresión dudosa no se "arregla": se marca con una advertencia y su página.
- Solo se eliminan líneas repetidas de encabezado/pie que no contienen fórmulas.

Salidas por documento: ``processed/normalized/<id>.md`` y ``processed/index/<id>.json``
(secciones con título, nivel, páginas, tipo, posición y advertencias).
"""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from dataclasses import asdict, dataclass, field
from typing import Any

from .config import SubjectPaths
from .extract import FORMULA_PLACEHOLDER, load_manifest
from .ingest import load_catalog, save_catalog
from .io_utils import atomic_write, fold, read_json, sha256_text, write_json
from .logging_utils import get_logger

NORMALIZER_VERSION = 1

PAGE_RE = re.compile(r"^<!-- page: (\d+) -->\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# Guías escaneadas suelen traer "Ejercicio 3" como texto plano o en negrita, sin encabezado.
PSEUDO_HEADING_RE = re.compile(
    r"^(?:\*\*)?((?:ejercicio|actividad|problema|consigna)\s+(?:n[°ºo.]?\s*)?\d+[a-z]?)\b[.:)]?(?:\*\*)?",
    re.IGNORECASE,
)
KIND_PATTERNS = (
    ("resolucion", re.compile(r"^(resoluci[oó]n|soluci[oó]n|soluciones|respuestas?|rta)\b")),
    ("enunciado", re.compile(r"^(ejercicios?|actividad(es)?|problemas?|consignas?|pr[aá]ctica|autoevaluaci[oó]n)\b")),
    ("teoria", re.compile(
        r"^(definici[oó]n|teorema|proposici[oó]n|propiedad(es)?|lema|corolario|demostraci[oó]n|"
        r"ejemplos?|observaci[oó]n|nota)\b")),
)
CID_RE = re.compile(r"\(cid:\d+\)")
PAGE_NUMBER_RE = re.compile(r"\d+")


@dataclass
class Section:
    section_id: str
    title: str
    level: int
    kind: str
    page_start: int | None
    page_end: int | None
    start: int = 0
    end: int = 0
    chars: int = 0
    flags: list[str] = field(default_factory=list)


def split_pages(markdown: str) -> list[tuple[int | None, list[str]]]:
    """Separa el Markdown extraído en páginas según las marcas ``<!-- page: N -->``."""
    pages: list[tuple[int | None, list[str]]] = [(None, [])]
    for line in markdown.splitlines():
        match = PAGE_RE.match(line)
        if match:
            pages.append((int(match.group(1)), []))
        elif not line.startswith("<!-- source:"):
            pages[-1][1].append(line)
    return [(number, lines) for number, lines in pages if number is not None or any(l.strip() for l in lines)]


def _signature(line: str) -> str:
    """Firma de una línea para detectar encabezados/pies repetidos ("Pág. 3 de 8")."""
    return PAGE_NUMBER_RE.sub("#", fold(line.strip()))


MARGIN_LINES = 3  # líneas no vacías del principio y del final de cada página


def margin_indices(lines: list[str]) -> set[int]:
    """Posiciones de las líneas que pueden ser encabezado o pie de página."""
    filled = [i for i, line in enumerate(lines) if line.strip()]
    return set(filled[:MARGIN_LINES] + filled[-MARGIN_LINES:])


def repeated_lines(pages: list[tuple[int | None, list[str]]], threshold: float = 0.6) -> set[str]:
    """Firmas de líneas cortas de encabezado/pie que aparecen en la mayoría de las páginas."""
    numbered = [lines for number, lines in pages if number is not None]
    if len(numbered) < 3:
        return set()
    counter: Counter[str] = Counter()
    for lines in numbered:
        seen = {_signature(lines[i]) for i in margin_indices(lines)
                if len(lines[i].strip()) <= 80 and "$" not in lines[i]}
        counter.update(seen)
    minimum = max(3, int(len(numbered) * threshold + 0.999))
    return {signature for signature, count in counter.items()
            if count >= minimum and (signature.strip("# ") or signature == "#")}


def _odd_dollars(paragraph: str) -> bool:
    without_code = re.sub(r"`[^`]*`", "", paragraph)
    return len(re.findall(r"(?<!\\)\$", without_code)) % 2 == 1


def detect_flags(text: str) -> list[str]:
    """Advertencias sobre expresiones posiblemente mal reconocidas en un fragmento."""
    flags: list[str] = []
    if FORMULA_PLACEHOLDER in text:
        flags.append("formula-no-decodificada")
    if "�" in text:
        flags.append("caracter-de-reemplazo")
    if CID_RE.search(text):
        flags.append("glifos-cid")
    if any(unicodedata.category(c) == "Co" for c in text):
        flags.append("glifos-uso-privado")
    if any(_odd_dollars(p) for p in re.split(r"\n\s*\n", text)):
        flags.append("delimitadores-desbalanceados")
    return flags


def classify_title(title: str) -> str:
    plain = fold(re.sub(r"[*_`#]", "", title)).strip()
    plain = re.sub(r"^[\d.\s)\-–]+", "", plain)
    for kind, pattern in KIND_PATTERNS:
        if pattern.match(plain):
            return kind
    return "otro"


def normalize_markdown(markdown: str) -> tuple[str, list[Section], dict[str, Any]]:
    """Devuelve (Markdown normalizado, secciones, informe)."""
    pages = split_pages(markdown)
    repeated = repeated_lines(pages)
    report: dict[str, Any] = {
        "pages": sum(1 for number, _ in pages if number is not None),
        "empty_pages": [],
        "removed_repeated_lines": 0,
        "headings": 0,
        "pseudo_headings": 0,
        "flags": {},
        "repeated_paragraphs": 0,
        "empty_sections": [],
    }

    # 1) Limpieza por líneas, conservando la página de cada una.
    cleaned: list[tuple[int | None, str]] = []
    for number, lines in pages:
        in_fence = in_math = False
        kept = 0
        margins = margin_indices(lines)
        for position, raw in enumerate(lines):
            line = unicodedata.normalize("NFC", raw).rstrip()
            if FENCE_RE.match(line):
                in_fence = not in_fence
            elif not in_fence and line.strip() == "$$":
                in_math = not in_math
            protected = in_fence or in_math
            if (not protected and position in margins and line.strip() and number is not None
                    and _signature(line) in repeated):
                report["removed_repeated_lines"] += 1
                continue
            if not protected:
                pseudo = PSEUDO_HEADING_RE.match(line)
                if pseudo and not HEADING_RE.match(line):
                    rest = line[pseudo.end():].strip()
                    cleaned.append((number, f"### {pseudo.group(1).strip()}"))
                    report["pseudo_headings"] += 1
                    if rest:
                        cleaned += [(number, ""), (number, rest)]
                    kept += 1
                    continue
            cleaned.append((number, line))
            kept += bool(line.strip())
        if number is not None and kept == 0:
            report["empty_pages"].append(number)
        cleaned.append((number, ""))

    # 2) Jerarquía de encabezados sin saltos: el primero queda en nivel 1 y nadie baja más de uno.
    stack: list[tuple[int, int]] = []  # (nivel original, nivel normalizado)
    in_fence = False
    for position, (number, line) in enumerate(cleaned):
        if FENCE_RE.match(line):
            in_fence = not in_fence
        match = None if in_fence else HEADING_RE.match(line)
        if not match:
            continue
        original = len(match.group(1))
        while stack and stack[-1][0] >= original:
            stack.pop()
        level = stack[-1][1] + 1 if stack else 1
        stack.append((original, level))
        cleaned[position] = (number, f"{'#' * level} {match.group(2)}")
        report["headings"] += 1

    # 3) Párrafos repetidos (no se borran: se informan) y colapso de líneas en blanco.
    output: list[tuple[int | None, str]] = []
    blank = 0
    for number, line in cleaned:
        if line.strip():
            blank = 0
            output.append((number, line))
        else:
            blank += 1
            if blank == 1 and output:
                output.append((number, ""))
    while output and not output[-1][1].strip():
        output.pop()

    # 4) Texto final con marcas de página y secciones con posiciones de caracteres.
    parts: list[str] = []
    sections: list[Section] = []
    offset = 0
    current_page: int | None = None
    in_fence = False

    def emit(text: str) -> None:
        nonlocal offset
        parts.append(text + "\n")
        offset += len(text) + 1

    def close(end: int, page: int | None) -> None:
        if sections:
            sections[-1].end = end
            sections[-1].page_end = page if page is not None else sections[-1].page_start

    last_content_page: int | None = None
    for number, line in output:
        if number != current_page and number is not None:
            emit(f"<!-- page: {number} -->")
            emit("")
            current_page = number
        if FENCE_RE.match(line):
            in_fence = not in_fence
        match = None if in_fence else HEADING_RE.match(line)
        if match or not sections:
            close(offset, last_content_page)
            title = match.group(2) if match else "(inicio del documento)"
            sections.append(Section(
                section_id=f"s{len(sections) + 1:03d}",
                title=title,
                level=len(match.group(1)) if match else 0,
                kind=classify_title(title) if match else "otro",
                page_start=number,
                page_end=number,
                start=offset,
            ))
        emit(line)
        if line.strip():
            last_content_page = number
    close(offset, last_content_page)
    text = "".join(parts)

    seen_paragraphs: Counter[str] = Counter()
    for paragraph in re.split(r"\n\s*\n", text):
        stripped = paragraph.strip()
        if len(stripped) >= 120 and not stripped.startswith("<!--"):
            seen_paragraphs[stripped] += 1
    report["repeated_paragraphs"] = sum(count - 1 for count in seen_paragraphs.values() if count > 1)

    all_flags: Counter[str] = Counter()
    for section in sections:
        body = text[section.start:section.end]
        section.chars = len(body)
        section.flags = detect_flags(body)
        all_flags.update(section.flags)
        content = "\n".join(l for l in body.splitlines()[1:] if l.strip() and not PAGE_RE.match(l))
        if section.level and not content.strip():
            # Un encabezado seguido de otro de nivel inferior es un título contenedor, no una pérdida.
            following = sections[sections.index(section) + 1] if section is not sections[-1] else None
            if following is None or following.level <= section.level:
                section.flags.append("seccion-vacia")
                report["empty_sections"].append(section.section_id)
    report["flags"] = dict(sorted(all_flags.items()))
    report["sections"] = len(sections)
    return text, sections, report


def _promote(document: dict[str, Any]) -> None:
    if document.get("status") in ("extraido", "inventariado"):
        document["status"] = "normalizado"
    elif document.get("status") == "extraido-parcial":
        document["status"] = "normalizado-parcial"


def run_normalize(paths: SubjectPaths, ids: list[str] | None = None, force: bool = False) -> dict[str, int]:
    log = get_logger()
    catalog = load_catalog(paths)
    manifest = load_manifest(paths)
    counts = {"normalized": 0, "cached": 0, "pending_extraction": 0}
    for document in catalog["documents"]:
        doc_id = document["id"]
        if ids and doc_id not in ids:
            continue
        source = paths.markdown / f"{doc_id}.md"
        if not source.exists():
            if document.get("status") not in ("omitido", "ausente"):
                counts["pending_extraction"] += 1
            continue
        markdown = source.read_text(encoding="utf-8")
        key = sha256_text(f"{NORMALIZER_VERSION}:{markdown}")
        index_path = paths.index / f"{doc_id}.json"
        target = paths.normalized / f"{doc_id}.md"
        if not force and target.exists() and index_path.exists() and read_json(index_path).get("input_key") == key:
            counts["cached"] += 1
            _promote(document)
            continue
        text, sections, report = normalize_markdown(markdown)
        atomic_write(target, text)
        write_json(index_path, {
            "id": doc_id,
            "sha256": document["sha256"],
            "source_path": document["path"],
            "input_key": key,
            "normalizer_version": NORMALIZER_VERSION,
            "extraction_status": manifest["documents"].get(doc_id, {}).get("status"),
            "report": report,
            "sections": [asdict(section) for section in sections],
        })
        _promote(document)
        counts["normalized"] += 1
        log.info("normalizado", extra={"id": doc_id, "sections": len(sections), "flags": report["flags"]})
    save_catalog(paths, catalog)
    log.info("normalización terminada", extra=counts)
    return counts
