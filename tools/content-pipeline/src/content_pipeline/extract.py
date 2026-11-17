"""Extracción con Docling: de cada documento del catálogo a Markdown y JSON trazables.

El motor queda detrás de la interfaz :class:`Engine`. :class:`DoclingEngine` es la
implementación real; los tests unitarios usan un motor falso para ejercitar la caché,
la idempotencia y el manejo de errores sin instalar Docling ni descargar modelos.

Salidas por documento (``<id>`` es el identificador del catálogo):

- ``processed/markdown/<id>.md``: texto por página, con marcas ``<!-- page: N -->``.
- ``processed/json/<id>.json``: sobre con metadatos, páginas y el ``DoclingDocument``.
- ``processed/images/<id>/``: figuras recortadas, cuando el perfil las solicita.
- ``processed/manifest.json``: clave de caché, estado, errores y estadísticas.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

from .config import PipelineError, SubjectPaths
from .ingest import load_catalog, save_catalog
from .io_utils import atomic_write, read_json, write_json
from .logging_utils import get_logger

PAGE_MARK = "<!-- page: {page} -->"
FORMULA_PLACEHOLDER = "<!-- formula-not-decoded -->"

#: Perfiles de extracción declarables en ``subject.yaml`` o en el catálogo.
PROFILES: dict[str, dict[str, Any]] = {
    # Apuntes, guías y parciales: OCR cuando hace falta, fórmulas a LaTeX y tablas.
    "full": {"ocr": True, "formulas": True, "tables": True, "images": True, "max_pages": None},
    # Texto corrido sin reconocimiento de fórmulas (mucho más rápido).
    "text": {"ocr": True, "formulas": False, "tables": True, "images": False, "max_pages": None},
    # Libros: solo portada, créditos e índice, para citar sin convertir la obra completa.
    "front-matter": {"ocr": True, "formulas": False, "tables": False, "images": False, "max_pages": 30},
    # Clases grabadas: transcripción con el pipeline ASR de Docling.
    "asr": {"asr": True},
    "skip": {},
}

FORMAT_PROFILES = {"audio": "asr", "video": "asr"}


class EngineUnavailable(PipelineError):
    """El motor no está instalado o le falta una dependencia del sistema."""


@dataclass
class PageText:
    page_no: int | None
    markdown: str


@dataclass
class EngineOutput:
    status: str  # success | partial | failure
    pages: list[PageText] = field(default_factory=list)
    document: dict[str, Any] | None = None
    images: list[tuple[str, int | None, bytes]] = field(default_factory=list)  # (nombre, página, PNG)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)


class Engine(Protocol):
    name: str
    version: str

    def supports(self, fmt: str) -> bool: ...

    def convert(self, path: Path, fmt: str, options: dict[str, Any]) -> EngineOutput: ...


class DoclingEngine:
    """Adaptador de Docling. Importa la librería recién al convertir el primer documento."""

    name = "docling"
    _FORMATS = {"pdf", "docx", "pptx", "xlsx", "markdown", "html", "image", "audio", "video"}

    def __init__(self, device: str = "auto", ocr_languages: tuple[str, ...] = ("es", "en"),
                 artifacts_path: str | None = None) -> None:
        self.device = device
        self.ocr_languages = ocr_languages
        self.artifacts_path = artifacts_path
        self._converters: dict[str, Any] = {}
        self._version: str | None = None

    @property
    def version(self) -> str:
        if self._version is None:
            try:
                from importlib.metadata import version
                self._version = version("docling")
            except Exception as error:  # pragma: no cover - depende del entorno
                raise EngineUnavailable(
                    "Docling no está instalado. Instalá el extra: pip install -e '.[extract]'"
                ) from error
        return self._version

    def supports(self, fmt: str) -> bool:
        return fmt in self._FORMATS

    # -- construcción de conversores ------------------------------------------------
    def _document_converter(self, options: dict[str, Any]) -> Any:
        key = json.dumps(options, sort_keys=True)
        if key in self._converters:
            return self._converters[key]
        try:
            from docling.datamodel.base_models import InputFormat
            from docling.datamodel.pipeline_options import AcceleratorOptions, PdfPipelineOptions
            from docling.document_converter import DocumentConverter, ImageFormatOption, PdfFormatOption
        except ImportError as error:
            raise EngineUnavailable(
                "Docling no está instalado. Instalá el extra: pip install -e '.[extract]'"
            ) from error
        pipeline = PdfPipelineOptions()
        pipeline.do_ocr = bool(options.get("ocr", True))
        pipeline.do_table_structure = bool(options.get("tables", True))
        pipeline.do_formula_enrichment = bool(options.get("formulas", False))
        pipeline.generate_picture_images = bool(options.get("images", False))
        pipeline.images_scale = 2.0
        pipeline.accelerator_options = AcceleratorOptions(device=self.device)
        if self.artifacts_path:
            pipeline.artifacts_path = self.artifacts_path
        if pipeline.do_ocr and hasattr(pipeline.ocr_options, "lang"):
            try:
                # Cada motor de OCR nombra los idiomas a su manera; si rechaza los
                # nuestros se conservan sus valores por defecto.
                pipeline.ocr_options.lang = list(self.ocr_languages)
            except Exception:
                pass
        converter = DocumentConverter(format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline),
            InputFormat.IMAGE: ImageFormatOption(pipeline_options=pipeline),
        })
        self._converters[key] = converter
        return converter

    def _asr_converter(self) -> Any:
        if "asr" in self._converters:
            return self._converters["asr"]
        if shutil.which("ffmpeg") is None:
            raise EngineUnavailable("La transcripción necesita ffmpeg en el PATH")
        try:
            from docling.datamodel import asr_model_specs
            from docling.datamodel.base_models import InputFormat
            from docling.datamodel.pipeline_options import AsrPipelineOptions
            from docling.document_converter import AudioFormatOption, DocumentConverter
            from docling.pipeline.asr_pipeline import AsrPipeline
        except ImportError as error:
            raise EngineUnavailable(
                "La transcripción necesita el extra: pip install -e '.[asr]'"
            ) from error
        pipeline = AsrPipelineOptions()
        pipeline.asr_options = asr_model_specs.WHISPER_TURBO
        option = AudioFormatOption(pipeline_cls=AsrPipeline, pipeline_options=pipeline)
        formats = {InputFormat.AUDIO: option}
        if hasattr(InputFormat, "VIDEO"):
            formats[InputFormat.VIDEO] = option
        self._converters["asr"] = DocumentConverter(format_options=formats)
        return self._converters["asr"]

    # -- conversión ----------------------------------------------------------------
    def convert(self, path: Path, fmt: str, options: dict[str, Any]) -> EngineOutput:
        converter = self._asr_converter() if options.get("asr") else self._document_converter(options)
        kwargs: dict[str, Any] = {"raises_on_error": False}
        if options.get("max_pages"):
            kwargs["page_range"] = (1, int(options["max_pages"]))
        result = converter.convert(path, **kwargs)
        status_name = getattr(result.status, "name", str(result.status)).upper()
        errors = [getattr(e, "error_message", str(e)) for e in (getattr(result, "errors", None) or [])]
        document = getattr(result, "document", None)
        if status_name == "FAILURE" or document is None:
            return EngineOutput(status="failure", errors=errors or [f"Docling devolvió {status_name}"])

        warnings: list[str] = []
        pages = self._pages(document, warnings)
        output = EngineOutput(
            status="success" if status_name == "SUCCESS" else "partial",
            pages=pages,
            document=document.export_to_dict(),
            errors=errors,
            warnings=warnings,
        )
        if options.get("images"):
            output.images = self._pictures(document, warnings)
        texts = getattr(document, "texts", []) or []
        formulas = [t for t in texts if str(getattr(t, "label", "")).lower().endswith("formula")]
        output.stats = {
            "pages": len(getattr(document, "pages", {}) or {}),
            "pages_requested": options.get("max_pages"),
            "text_items": len(texts),
            "headings": sum(1 for t in texts if "header" in str(getattr(t, "label", "")).lower()
                            or str(getattr(t, "label", "")).lower().endswith("title")),
            "tables": len(getattr(document, "tables", []) or []),
            "pictures": len(getattr(document, "pictures", []) or []),
            "formulas": len(formulas),
            "formulas_undecoded": sum(1 for f in formulas if not (getattr(f, "text", "") or "").strip()),
        }
        return output

    @staticmethod
    def _pages(document: Any, warnings: list[str]) -> list[PageText]:
        page_numbers = sorted((getattr(document, "pages", None) or {}).keys())
        if not page_numbers:
            return [PageText(None, document.export_to_markdown())]
        try:
            return [PageText(number, document.export_to_markdown(page_no=number)) for number in page_numbers]
        except TypeError:
            warnings.append("Esta versión de Docling no exporta por página; se pierde el número de página.")
            return [PageText(None, document.export_to_markdown())]

    @staticmethod
    def _pictures(document: Any, warnings: list[str]) -> list[tuple[str, int | None, bytes]]:
        import io

        images: list[tuple[str, int | None, bytes]] = []
        for index, picture in enumerate(getattr(document, "pictures", []) or [], start=1):
            try:
                image = picture.get_image(document)
                if image is None:
                    continue
                provenance = getattr(picture, "prov", None) or []
                page = provenance[0].page_no if provenance else None
                buffer = io.BytesIO()
                image.save(buffer, format="PNG")
                prefix = f"p{page:03d}-" if page is not None else ""
                images.append((f"{prefix}fig{index:03d}.png", page, buffer.getvalue()))
            except Exception as error:  # una figura rota no invalida el documento
                warnings.append(f"No se pudo exportar la figura {index}: {error}")
        return images


def resolve_profile(document: dict[str, Any], override: str | None = None) -> tuple[str, dict[str, Any]]:
    """Devuelve (nombre, opciones). ``extraction`` puede ser un nombre o un mapa con ``profile``."""
    declared = override or document.get("extraction") or "full"
    extra: dict[str, Any] = {}
    if isinstance(declared, dict):
        extra = {k: v for k, v in declared.items() if k != "profile"}
        declared = declared.get("profile", "full")
    if declared not in PROFILES:
        raise PipelineError(f"Perfil de extracción desconocido: {declared!r} ({document.get('id')})")
    if declared not in ("skip", "asr") and document.get("format") in FORMAT_PROFILES:
        declared = FORMAT_PROFILES[document["format"]]
    return declared, {**PROFILES[declared], **extra}


def cache_key(document: dict[str, Any], engine: Engine, profile: str, options: dict[str, Any]) -> str:
    payload = json.dumps([document["sha256"], engine.name, engine.version, profile, options], sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def load_manifest(paths: SubjectPaths) -> dict[str, Any]:
    return read_json(paths.manifest) if paths.manifest.exists() else {"documents": {}}


def render_markdown(document: dict[str, Any], output: EngineOutput) -> str:
    lines = [f"<!-- source: {document['id']} | sha256: {document['sha256']} -->", ""]
    by_page: dict[int | None, list[str]] = {}
    for name, page, _ in output.images:
        by_page.setdefault(page, []).append(name)
    for page in output.pages:
        if page.page_no is not None:
            lines += [PAGE_MARK.format(page=page.page_no), ""]
        lines += [page.markdown.strip(), ""]
        if by_page.get(page.page_no):
            lines += [f"<!-- images: {', '.join(by_page[page.page_no])} -->", ""]
    return "\n".join(lines).rstrip() + "\n"


def run_extract(paths: SubjectPaths, engine: Engine, ids: list[str] | None = None, force: bool = False,
                profile: str | None = None, limit: int | None = None,
                formulas: bool = True) -> dict[str, Any]:
    """Convierte los documentos pendientes. Un fallo individual nunca detiene el lote."""
    log = get_logger()
    catalog = load_catalog(paths)
    manifest = load_manifest(paths)
    known = {d["id"] for d in catalog["documents"]}
    unknown = sorted(set(ids or []) - known)
    if unknown:
        raise PipelineError(f"Identificadores inexistentes en el catálogo: {unknown}")

    counts = {"converted": 0, "partial": 0, "cached": 0, "skipped": 0, "failed": 0, "missing": 0}
    processed = 0
    for document in catalog["documents"]:
        doc_id = document["id"]
        if ids and doc_id not in ids:
            continue
        name, options = resolve_profile(document, profile)
        if not formulas and options.get("formulas"):
            options = {**options, "formulas": False}  # pasada rápida: sin el modelo de fórmulas
        if name == "skip":
            document["status"] = "omitido"
            counts["skipped"] += 1
            continue
        source = paths.raw / document["path"]
        # Una entrada "ausente" es una versión anterior: su ruta puede tener hoy otro contenido.
        if document.get("status") == "ausente" or not source.is_file():
            counts["missing"] += 1
            log.warning("documento ausente en raw/", extra={"id": doc_id, "path": document["path"]})
            continue
        if not engine.supports(document["format"]):
            manifest["documents"][doc_id] = {"status": "failure", "profile": name,
                                             "errors": [f"Formato no compatible: {document['format']}"]}
            document["status"] = "requiere-intervencion"
            counts["failed"] += 1
            continue
        try:
            key = cache_key(document, engine, name, options)
        except EngineUnavailable:
            raise
        markdown_path = paths.markdown / f"{doc_id}.md"
        json_path = paths.json / f"{doc_id}.json"
        previous = manifest["documents"].get(doc_id, {})
        if (not force and previous.get("cache_key") == key and previous.get("status") in ("success", "partial")
                and markdown_path.exists() and json_path.exists()):
            counts["cached"] += 1
            continue
        if limit is not None and processed >= limit:
            continue
        processed += 1
        started = time.monotonic()
        log.info("extrayendo", extra={"id": doc_id, "path": document["path"], "profile": name})
        try:
            output = engine.convert(source, document["format"], options)
        except EngineUnavailable as error:
            # Falta una dependencia para este tipo de documento; el resto del lote sigue.
            output = EngineOutput(status="failure", errors=[str(error)])
        except Exception as error:  # noqa: BLE001 - se registra y se continúa con el resto
            output = EngineOutput(status="failure", errors=[f"{type(error).__name__}: {error}"])
        elapsed = round(time.monotonic() - started, 2)

        record: dict[str, Any] = {
            "sha256": document["sha256"],
            "engine": engine.name,
            "engine_version": engine.version,
            "profile": name,
            "options": options,
            "status": output.status,
            "errors": output.errors,
            "warnings": output.warnings,
            "stats": output.stats,
            "seconds": elapsed,
        }
        if output.status == "failure":
            document["status"] = "error"
            counts["failed"] += 1
            log.error("extracción fallida", extra={"id": doc_id, "errors": output.errors})
        else:
            image_names = []
            image_dir = paths.images / doc_id
            for image_name, page, payload in output.images:
                atomic_write(image_dir / image_name, payload)
                image_names.append({"file": f"{doc_id}/{image_name}", "page": page})
            atomic_write(markdown_path, render_markdown(document, output))
            write_json(json_path, {
                "id": doc_id,
                "sha256": document["sha256"],
                "source_path": document["path"],
                "engine": engine.name,
                "engine_version": engine.version,
                "profile": name,
                "status": output.status,
                "stats": output.stats,
                "errors": output.errors,
                "warnings": output.warnings,
                "images": image_names,
                "pages": [{"page_no": p.page_no, "markdown": p.markdown} for p in output.pages],
                "docling_document": output.document,
            })
            record["cache_key"] = key
            document["status"] = "extraido" if output.status == "success" else "extraido-parcial"
            counts["converted" if output.status == "success" else "partial"] += 1
        manifest["documents"][doc_id] = record
        # Guardar tras cada documento permite retomar un lote interrumpido.
        write_json(paths.manifest, manifest)

    write_json(paths.manifest, manifest)
    save_catalog(paths, catalog)
    log.info("extracción terminada", extra=counts)
    return counts
