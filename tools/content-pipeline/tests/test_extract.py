import json

from conftest import FakeEngine

from content_pipeline.extract import load_manifest, resolve_profile, run_extract
from content_pipeline.ingest import load_catalog, run_inventory


def doc(subject, path):
    return next(d for d in load_catalog(subject)["documents"] if d["path"] == path)


def test_extrae_markdown_y_json_con_paginas(subject):
    run_inventory(subject)
    counts = run_extract(subject, FakeEngine())
    assert counts["converted"] == 2 and counts["skipped"] == 1 and counts["failed"] == 0
    guide = doc(subject, "practicas/guia.pdf")
    markdown = (subject.markdown / f"{guide['id']}.md").read_text(encoding="utf-8")
    assert markdown.startswith(f"<!-- source: {guide['id']} | sha256: {guide['sha256']} -->")
    assert "<!-- page: 1 -->" in markdown and "<!-- page: 2 -->" in markdown
    payload = json.loads((subject.json / f"{guide['id']}.json").read_text(encoding="utf-8"))
    assert payload["source_path"] == "practicas/guia.pdf"
    assert [p["page_no"] for p in payload["pages"]] == [1, 2]
    assert (subject.images / guide["id"] / "p001-fig001.png").exists()
    assert guide["status"] == "extraido"


def test_cache_por_hash_y_force(subject):
    run_inventory(subject)
    engine = FakeEngine()
    run_extract(subject, engine)
    assert len(engine.calls) == 2
    again = run_extract(subject, engine)
    assert again["cached"] == 2 and len(engine.calls) == 2
    run_extract(subject, engine, force=True)
    assert len(engine.calls) == 4


def test_cambio_del_original_invalida_la_cache(subject):
    run_inventory(subject)
    engine = FakeEngine()
    run_extract(subject, engine)
    (subject.raw / "teoria/espacios.md").write_text("# Otro contenido\n", encoding="utf-8")
    (subject.raw / "otros/copias/espacios (copia).md").unlink()
    run_inventory(subject)
    counts = run_extract(subject, engine)
    assert counts["converted"] == 1 and counts["cached"] == 1


def test_un_error_no_detiene_el_lote(subject):
    run_inventory(subject)
    counts = run_extract(subject, FakeEngine(fail_on={"guia.pdf"}))
    assert counts["failed"] == 1 and counts["converted"] == 1
    guide = doc(subject, "practicas/guia.pdf")
    record = load_manifest(subject)["documents"][guide["id"]]
    assert record["status"] == "failure"
    assert "RuntimeError: documento corrupto" in record["errors"][0]
    assert guide["status"] == "error"
    # Un nuevo intento reprocesa solo el documento fallido.
    retry = run_extract(subject, FakeEngine())
    assert retry["converted"] == 1 and retry["cached"] == 1


def test_perfiles(subject):
    assert resolve_profile({"format": "pdf", "extraction": "front-matter"})[1]["max_pages"] == 30
    assert resolve_profile({"format": "video", "extraction": "full"})[0] == "asr"
    assert resolve_profile({"format": "video", "extraction": "skip"})[0] == "skip"
    name, options = resolve_profile({"format": "pdf", "extraction": {"profile": "text", "max_pages": 5}})
    assert name == "text" and options["max_pages"] == 5 and options["formulas"] is False


def test_limite_y_seleccion_por_id(subject):
    run_inventory(subject)
    engine = FakeEngine()
    assert run_extract(subject, engine, limit=1)["converted"] == 1
    guide = doc(subject, "practicas/guia.pdf")
    other = FakeEngine()
    run_extract(subject, other, ids=[guide["id"]], force=True)
    assert other.calls == ["guia.pdf"]
