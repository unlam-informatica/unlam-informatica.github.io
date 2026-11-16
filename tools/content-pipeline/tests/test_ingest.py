import hashlib

import pytest

from content_pipeline.config import PipelineError, subject_paths
from content_pipeline.ingest import classify, load_catalog, run_inventory
from content_pipeline.io_utils import read_yaml, write_yaml
from content_pipeline.config import load_subject_config


def by_path(catalog, path):
    return next(d for d in catalog["documents"] if d["path"] == path)


def test_inventario_hashes_y_formatos(subject):
    summary = run_inventory(subject)
    catalog = load_catalog(subject)
    guide = by_path(catalog, "practicas/guia.pdf")
    expected = hashlib.sha256((subject.raw / "practicas/guia.pdf").read_bytes()).hexdigest()
    assert guide["sha256"] == expected
    assert guide["id"] == f"demo-{expected[:12]}"
    assert guide["format"] == "pdf"
    assert summary["files_scanned"] == 4  # .txt omitido y .DS_Store ignorado
    assert [s["path"] for s in summary["skipped_files"]] == ["practicas/notas.txt"]
    assert not any(".DS_Store" in d["path"] for d in catalog["documents"])


def test_duplicados_por_hash(subject):
    summary = run_inventory(subject)
    catalog = load_catalog(subject)
    assert summary["unique_documents"] == 3
    assert summary["duplicate_files"] == 1
    entry = by_path(catalog, "teoria/espacios.md")
    assert entry["duplicate_paths"] == ["otros/espacios (copia).md"]
    assert catalog["summary"]["duplicate_files"] == 1


def test_clasificacion_por_reglas(subject):
    config = load_subject_config(subject)
    result = classify("Practicas/Guía.pdf", config)  # sin distinguir mayúsculas ni acentos
    assert result["doc_type"] == "guia-practica"
    assert result["units"] == ["u1"]
    assert result["license"] == "privado-catedra"
    other = classify("otros/sin regla.pdf", config)
    assert other["doc_type"] == "otro" and other["_matched"] is False


def test_documentos_que_requieren_intervencion(subject):
    run_inventory(subject)
    catalog = load_catalog(subject)
    video = by_path(catalog, "clase.mp4")
    assert video["status"] == "omitido"
    assert "sin-unidad" in video["needs_review"]
    assert "sin-fuente" in video["needs_review"]


def test_idempotencia(subject):
    run_inventory(subject)
    before = subject.catalog.read_bytes()
    second = run_inventory(subject)
    assert second["catalog_changed"] is False
    assert subject.catalog.read_bytes() == before


def test_correcciones_manuales_se_conservan(subject):
    run_inventory(subject)
    catalog = read_yaml(subject.catalog)
    entry = by_path(catalog, "practicas/guia.pdf")
    entry["units"] = ["u1", "u2"]
    entry["notes"] = "Revisado a mano"
    write_yaml(subject.catalog, catalog)
    run_inventory(subject)
    entry = by_path(load_catalog(subject), "practicas/guia.pdf")
    assert entry["units"] == ["u1", "u2"] and entry["notes"] == "Revisado a mano"
    run_inventory(subject, reclassify=True)
    entry = by_path(load_catalog(subject), "practicas/guia.pdf")
    assert entry["units"] == ["u1"]


def test_documento_eliminado_queda_registrado(subject):
    run_inventory(subject)
    (subject.raw / "practicas/guia.pdf").unlink()
    summary = run_inventory(subject)
    entry = by_path(load_catalog(subject), "practicas/guia.pdf")
    assert summary["missing_documents"] == 1
    assert entry["status"] == "ausente" and "archivo-ausente" in entry["needs_review"]


def test_catalogo_sin_rutas_absolutas(subject):
    run_inventory(subject)
    text = subject.catalog.read_text(encoding="utf-8")
    assert str(subject.root.parent) not in text


def test_nombres_unicode_normalizados(subject):
    nfd = "teoría.md"  # "teoría" en NFD, como lo guarda macOS
    (subject.raw / "teoria" / nfd).write_text("hola", encoding="utf-8")
    run_inventory(subject)
    paths = [d["path"] for d in load_catalog(subject)["documents"]]
    assert "teoria/teoría.md" in paths


def test_errores_de_configuracion(tmp_path):
    with pytest.raises(PipelineError):
        subject_paths("../fuera", tmp_path)
    with pytest.raises(PipelineError):
        subject_paths("inexistente", tmp_path)
    (tmp_path / "x" / "raw").mkdir(parents=True)
    (tmp_path / "x" / "subject.yaml").write_text("rules:\n  - doc_type: apunte\n", encoding="utf-8")
    with pytest.raises(PipelineError, match="match"):
        run_inventory(subject_paths("x", tmp_path))
