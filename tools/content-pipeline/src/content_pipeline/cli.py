"""Interfaz de línea de comandos: ``content-pipeline <comando> --subject <materia>``."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from . import __version__
from .config import PipelineError, find_repo_root, subject_paths
from .logging_utils import configure, get_logger


def _split(value: str | None) -> list[str] | None:
    return [item.strip() for item in value.split(",") if item.strip()] if value else None


def _print(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2, default=str))


def _engine(args: argparse.Namespace):
    from .extract import DoclingEngine

    return DoclingEngine(device=args.device, artifacts_path=args.artifacts_path)


def cmd_inventory(args, paths):
    from .ingest import run_inventory

    summary = run_inventory(paths, reclassify=args.reclassify)
    _print({k: v for k, v in summary.items() if k != "skipped_files"} | {"skipped_files": len(summary["skipped_files"])})
    return 0


def cmd_extract(args, paths):
    from .extract import run_extract

    _print(run_extract(paths, _engine(args), ids=_split(args.ids), force=args.force, profile=args.profile,
                       limit=args.limit))
    return 0


def cmd_normalize(args, paths):
    from .normalize import run_normalize

    _print(run_normalize(paths, ids=_split(args.ids), force=args.force))
    return 0


def cmd_package(args, paths):
    from .package import run_package

    result = run_package(paths, unit_id=args.unit, topic_id=args.topic, budget=args.budget)
    _print({"packages": result["packages"], "topics_without_sources": result["topics_without_sources"]})
    return 0


def cmd_validate(args, paths):
    from .validate import run_validate

    docs_root = Path(args.docs_root) if args.docs_root else find_repo_root(paths.root) / "src/content/docs"
    report = run_validate(paths, docs_root=docs_root)
    _print({k: report[k] for k in ("errors", "warnings", "info", "documents", "curriculum")})
    return 1 if report["errors"] and args.strict else 0


def cmd_run(args, paths):
    from .extract import run_extract
    from .ingest import run_inventory
    from .normalize import run_normalize
    from .package import run_package
    from .validate import run_validate

    log = get_logger()
    summary: dict[str, Any] = {}
    inventory = run_inventory(paths)
    summary["inventory"] = {"unique_documents": inventory["unique_documents"],
                            "duplicate_files": inventory["duplicate_files"]}
    summary["extract"] = run_extract(paths, _engine(args), force=args.force, limit=args.limit)
    summary["normalize"] = run_normalize(paths, force=args.force)
    if paths.curriculum.exists():
        summary["package"] = {"packages": run_package(paths)["packages"]}
    else:
        log.warning("sin curriculum-map.yaml: se omiten los paquetes de contexto")
    report = run_validate(paths, docs_root=find_repo_root(paths.root) / "src/content/docs")
    summary["validate"] = {k: report[k] for k in ("errors", "warnings", "info")}
    _print(summary)
    return 1 if report["errors"] and args.strict else 0


def cmd_status(args, paths):
    from .extract import load_manifest
    from .ingest import load_catalog

    catalog = load_catalog(paths)
    manifest = load_manifest(paths)["documents"]
    documents = catalog["documents"]
    status: dict[str, Any] = {
        "subject": paths.subject,
        "documents": len(documents),
        "by_status": dict(Counter(d.get("status") for d in documents)),
        "by_type": dict(Counter(d.get("doc_type") for d in documents)),
        "needs_review": sum(1 for d in documents if d.get("needs_review")),
        "extraction": dict(Counter(r.get("status") for r in manifest.values())),
        "normalized": len(list(paths.index.glob("*.json"))) if paths.index.exists() else 0,
        "context_packages": len(list(paths.context.rglob("*.md"))) if paths.context.exists() else 0,
    }
    if paths.curriculum.exists():
        from .package import iter_topics, load_curriculum

        topics = [topic for _, topic in iter_topics(load_curriculum(paths))]
        status["curriculum"] = {
            "topics": len(topics),
            "production": dict(Counter(t.get("production", "pendiente") for t in topics)),
            "validation": dict(Counter(t.get("validation", "pendiente") for t in topics)),
        }
    report = paths.reports / "validation.json"
    if report.exists():
        data = json.loads(report.read_text(encoding="utf-8"))
        status["last_validation"] = {k: data[k] for k in ("errors", "warnings", "info")}
    _print(status)
    return 0


def cmd_verify_math(args, paths):
    from .mathcheck import run_checks

    directory = Path(args.checks) if args.checks else paths.root / "checks"
    report_path = Path(args.report) if args.report else paths.root / "reports" / "math-verification.json"
    report = run_checks(directory, ids=_split(args.ids), report_path=report_path)
    _print({k: report[k] for k in ("total", "passed", "failed")})
    for result in report["results"]:
        if result["status"] == "failed":
            print(f"FALLA {result['id']} ({result['module']}): {result['detail']}", file=sys.stderr)
    return 1 if report["failed"] else 0


def cmd_qa(args, paths):
    from .qa import run_qa

    repo = find_repo_root(paths.root)
    docs_root = Path(args.docs_root) if args.docs_root else repo / "src/content/docs"
    report_path = Path(args.report) if args.report else paths.root / "reports" / "content-qa.json"
    math_report = paths.root / "reports" / "math-verification.json"
    report = run_qa(docs_root, paths.subject, curriculum_path=paths.curriculum, math_report=math_report,
                    subject_config=paths.subject_config, report_path=report_path)
    _print({k: report[k] for k in ("pages", "exercises", "exercises_sympy", "exercises_reasoning", "units",
                                   "errors", "warnings")})
    for finding in report["findings"]:
        if finding["severity"] == "error":
            print(f"ERROR {finding['code']} {finding['where']}: {finding['message']}", file=sys.stderr)
    return 1 if report["errors"] else 0


COMMANDS = {
    "inventory": (cmd_inventory, "Inventaria raw/, calcula hashes, detecta duplicados y actualiza catalog.yaml"),
    "extract": (cmd_extract, "Convierte con Docling a Markdown y JSON (con caché por hash)"),
    "normalize": (cmd_normalize, "Normaliza el Markdown extraído e indexa secciones y páginas"),
    "package": (cmd_package, "Prepara paquetes de contexto por unidad o tema"),
    "validate": (cmd_validate, "Valida documentos y matriz curricular; genera reportes"),
    "run": (cmd_run, "Ejecuta inventory → extract → normalize → package → validate"),
    "status": (cmd_status, "Muestra el estado de procesamiento de una materia"),
    "verify-math": (cmd_verify_math, "Ejecuta las comprobaciones simbólicas (SymPy) de checks/"),
    "qa": (cmd_qa, "Controla calidad y cobertura del material publicado"),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="content-pipeline", description=__doc__)
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--subject", required=True, help="Identificador de la materia (carpeta en academic-sources/)")
    common.add_argument("--sources-root", help="Carpeta academic-sources/ (por defecto, la del repositorio)")
    common.add_argument("--log-level", default="info", choices=["debug", "info", "warning", "error"])
    common.add_argument("--log-format", default="text", choices=["text", "json"])
    common.add_argument("--log-file", help="Además, registrar eventos JSON en este archivo")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name, (_, help_text) in COMMANDS.items():
        sub = subparsers.add_parser(name, parents=[common], help=help_text, description=help_text)
        if name == "inventory":
            sub.add_argument("--reclassify", action="store_true",
                             help="Reaplicar subject.yaml aunque el catálogo tenga correcciones manuales")
        if name in ("extract", "run"):
            sub.add_argument("--device", default="auto", help="auto | cpu | mps | cuda")
            sub.add_argument("--artifacts-path", help="Modelos de Docling descargados para uso sin red")
            sub.add_argument("--limit", type=int, help="Procesar como máximo N documentos nuevos")
        if name == "extract":
            sub.add_argument("--profile", help="Forzar perfil: full | text | front-matter | asr | skip")
        if name in ("extract", "normalize", "verify-math"):
            sub.add_argument("--ids", help="Lista de identificadores separados por comas")
        if name in ("extract", "normalize", "run"):
            sub.add_argument("--force", action="store_true", help="Ignorar la caché")
        if name == "package":
            sub.add_argument("--unit", help="Solo esta unidad (id de curriculum-map.yaml)")
            sub.add_argument("--topic", help="Solo este tema")
            sub.add_argument("--budget", type=int, default=24_000, help="Caracteres de fragmentos por paquete")
        if name in ("validate", "run"):
            sub.add_argument("--strict", action="store_true", help="Salir con código 1 si hay errores")
        if name in ("validate", "qa"):
            sub.add_argument("--docs-root", help="Carpeta src/content/docs del portal")
        if name == "verify-math":
            sub.add_argument("--checks", help="Carpeta de comprobaciones (por defecto <materia>/checks)")
        if name in ("verify-math", "qa"):
            sub.add_argument("--report", help="Ruta del reporte JSON")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    configure(args.log_level, args.log_format, Path(args.log_file) if args.log_file else None)
    try:
        paths = subject_paths(args.subject, Path(args.sources_root).resolve() if args.sources_root else None)
        handler = COMMANDS[args.command][0]
        return handler(args, paths)
    except PipelineError as error:
        get_logger().error(str(error))
        return 2
    except KeyboardInterrupt:
        get_logger().error("interrumpido")
        return 130


if __name__ == "__main__":
    sys.exit(main())
