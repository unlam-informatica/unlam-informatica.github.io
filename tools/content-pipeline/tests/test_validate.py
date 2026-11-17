from conftest import FakeEngine, minimal_pdf

from content_pipeline.extract import run_extract
from content_pipeline.ingest import load_catalog, run_inventory
from content_pipeline.normalize import run_normalize
from content_pipeline.validate import pdf_page_count, run_validate


def codes(report, severity=None):
    return {f["code"] for f in report["findings"] if severity in (None, f["severity"])}


def test_reporta_pendientes_duplicados_y_metadatos(subject):
    run_inventory(subject)
    report = run_validate(subject)
    assert "sin-extraer" in codes(report, "warning")
    assert "duplicado" in codes(report, "info")
    assert "sin-matriz" in codes(report)
    assert (subject.reports / "validation.md").exists()


def test_reporta_errores_de_conversion_y_paginas_perdidas(subject):
    run_inventory(subject)
    run_extract(subject, FakeEngine(fail_on={"espacios.md"}))
    run_normalize(subject)
    report = run_validate(subject)
    assert "error-de-conversion" in codes(report, "error")
    assert report["errors"] >= 1
    # Simular una extracción que perdió una página del PDF.
    import json
    manifest = json.loads(subject.manifest.read_text(encoding="utf-8"))
    guide = next(d for d in load_catalog(subject)["documents"] if d["path"] == "practicas/guia.pdf")
    manifest["documents"][guide["id"]]["stats"]["pages"] = 1
    subject.manifest.write_text(json.dumps(manifest), encoding="utf-8")
    assert "paginas-perdidas" in codes(run_validate(subject), "error")


def test_documento_modificado_despues_de_extraer(subject):
    run_inventory(subject)
    run_extract(subject, FakeEngine())
    (subject.raw / "practicas/guia.pdf").write_bytes(minimal_pdf(["Otra version"]))
    run_inventory(subject)
    assert "sin-extraer" in codes(run_validate(subject))


def test_referencias_invalidas_en_la_matriz(subject, tmp_path):
    run_inventory(subject)
    subject.curriculum.write_text(
        "units:\n  - id: u1\n    title: U\n    topics:\n"
        "      - id: t1\n        title: T\n        production: redactado\n"
        "        page: /demo/t1/\n        sources: [demo-000000000000]\n        bibliography: [nadie]\n",
        encoding="utf-8")
    docs = tmp_path / "docs"
    docs.mkdir()
    report = run_validate(subject, docs_root=docs)
    found = codes(report, "error")
    assert {"referencia-invalida", "pagina-inexistente"} <= found
    assert "sin-objetivos" in codes(report, "warning")


def test_conteo_de_paginas_pdf(tmp_path):
    path = tmp_path / "a.pdf"
    path.write_bytes(minimal_pdf(["a", "b", "c"]))
    assert pdf_page_count(path) == 3
