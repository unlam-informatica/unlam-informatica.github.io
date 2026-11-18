"""Soporte de texto plano (.txt): decodificación, ingesta, extracción sin Docling y normalización."""
import json
import socket
import unicodedata

import pytest
from conftest import FakeEngine

from content_pipeline.extract import PlainTextEngine, decode_text, load_manifest, run_extract
from content_pipeline.ingest import load_catalog, run_inventory
from content_pipeline.normalize import run_normalize

TEXTO = "Ejercicio 3\n\nCalcular el núcleo de T.\n"


class EngineSinTxt(FakeEngine):
    """Falla si se le pide convertir un .txt, y registra las llamadas."""

    def convert(self, path, fmt, options):
        assert fmt != "plaintext", "el .txt no debe llegar al motor principal"
        return super().convert(path, fmt, options)


def doc_txt(paths, name):
    return next(d for d in load_catalog(paths)["documents"] if d["path"] == name)


# -- decodificación ---------------------------------------------------------------
def test_decodifica_utf8():
    text, encoding, warnings = decode_text("Ñandú — café".encode("utf-8"))
    assert (text, encoding, warnings) == ("Ñandú — café", "utf-8", [])


def test_decodifica_utf8_con_bom():
    text, encoding, warnings = decode_text(b"\xef\xbb\xbf" + "áé".encode("utf-8"))
    assert text == "áé" and encoding == "utf-8-sig" and warnings == []


@pytest.mark.parametrize("codec", ["utf-16-le", "utf-16-be"])
def test_decodifica_utf16_con_bom(codec):
    bom = b"\xff\xfe" if codec.endswith("le") else b"\xfe\xff"
    text, encoding, warnings = decode_text(bom + "Ñandú".encode(codec))
    assert text == "Ñandú" and encoding == "utf-16" and warnings == []


def test_cp1252_con_advertencia():
    text, encoding, warnings = decode_text("Ñandú — “café”".encode("cp1252"))
    assert text == "Ñandú — “café”"
    assert encoding == "cp1252"
    assert "codificacion-heredada: cp1252" in warnings


def test_latin1_si_cp1252_falla():
    text, encoding, warnings = decode_text(b"a\x81b")  # 0x81 no existe en cp1252
    assert encoding == "latin-1" and text == "a\x81b"
    assert "codificacion-heredada: latin-1" in warnings


def test_saltos_nfc_y_nul():
    text, _, _ = decode_text(b"a\r\nb\rc\nd\x00e")
    assert text == "a\nb\nc\nde"
    nfd = unicodedata.normalize("NFD", "canción")
    assert nfd != "canción"
    assert decode_text(nfd.encode("utf-8"))[0] == "canción"


@pytest.mark.parametrize("data", [b"", b"  \n\t\r\n"])
def test_archivo_vacio(data):
    text, _, warnings = decode_text(data)
    assert not text.strip() and "archivo-vacio" in warnings


def test_no_reescribe_markdown_ni_urls():
    original = "# Título\n* item\n[x](http://a.b/c?d=1) $x_1$\n"
    text, _, warnings = decode_text(original.encode())
    assert text == original
    assert warnings == ["enlaces-externos-no-seguidos: 1"]


# -- ingesta ----------------------------------------------------------------------
def test_ingesta_cataloga_txt(subject):
    name = "1. [Final][1C2025][Llamado B][].txt"
    (subject.raw / "practicas" / name).write_text(TEXTO, encoding="utf-8")
    summary = run_inventory(subject)
    assert summary["skipped_files"] == [s for s in summary["skipped_files"] if not s["path"].endswith(".txt")]
    entry = doc_txt(subject, f"practicas/{name}")
    assert entry["format"] == "plaintext"
    assert entry["doc_type"] == "guia-practica"  # regla practicas/* de subject.yaml


# -- extracción -------------------------------------------------------------------
def make_txt(subject, content=TEXTO.encode("utf-8")):
    (subject.raw / "practicas" / "final.txt").write_bytes(content)
    run_inventory(subject)
    return doc_txt(subject, "practicas/final.txt")


def test_extrae_txt_con_motor_propio_y_cache(subject):
    entry = make_txt(subject)
    engine = EngineSinTxt()
    counts = run_extract(subject, engine)
    assert counts["failed"] == 0 and "final.txt" not in engine.calls
    markdown = (subject.markdown / f"{entry['id']}.md").read_text(encoding="utf-8")
    assert "<!-- page: 1 -->" in markdown and "Calcular el núcleo de T." in markdown
    record = load_manifest(subject)["documents"][entry["id"]]
    assert record["engine"] == "plaintext" and record["status"] == "success"
    assert record["stats"]["pages"] == 1 and record["stats"]["text_items"] == 2
    assert record["stats"]["encoding"] == "utf-8" and record["stats"]["headings"] == 0
    payload = json.loads((subject.json / f"{entry['id']}.json").read_text(encoding="utf-8"))
    assert payload["engine"] == "plaintext"
    assert payload["docling_document"] == {"format": "plaintext", "encoding": "utf-8",
                                           "lines": 3, "chars": len(TEXTO)}
    again = run_extract(subject, engine)
    assert again["converted"] == 0 and again["cached"] >= 1
    assert load_manifest(subject)["documents"][entry["id"]]["engine"] == "plaintext"


def test_lote_solo_txt_no_evalua_el_motor_principal(subject):
    class Prohibido:
        name = "docling"

        @property
        def version(self):
            raise AssertionError("no debe evaluarse la versión de Docling")

        def supports(self, fmt):
            return False

    entry = make_txt(subject)
    counts = run_extract(subject, Prohibido(), ids=[entry["id"]])
    assert counts["converted"] == 1 and counts["failed"] == 0


def test_txt_vacio_es_parcial(subject):
    entry = make_txt(subject, b"")
    counts = run_extract(subject, EngineSinTxt(), ids=[entry["id"]])
    assert counts["partial"] == 1
    record = load_manifest(subject)["documents"][entry["id"]]
    assert record["status"] == "partial" and "archivo-vacio" in record["warnings"]


def test_skip_sigue_omitiendo_txt(subject):
    entry = make_txt(subject)
    counts = run_extract(subject, EngineSinTxt(), ids=[entry["id"]], profile="skip")
    assert counts["skipped"] == 1 and counts["converted"] == 0


def test_motor_de_texto_contrato():
    engine = PlainTextEngine()
    assert engine.name == "plaintext" and engine.version
    assert engine.supports("plaintext") and not engine.supports("pdf")


# -- sin red ----------------------------------------------------------------------
def test_urls_no_abren_conexiones(subject, monkeypatch):
    def prohibido(*args, **kwargs):
        raise AssertionError("no se permite acceso a la red")

    monkeypatch.setattr(socket, "socket", prohibido)
    monkeypatch.setattr(socket, "create_connection", prohibido)
    entry = make_txt(subject, b"Ver https://ejemplo.org/a y http://x.y\n")
    run_extract(subject, EngineSinTxt(), ids=[entry["id"]])
    record = load_manifest(subject)["documents"][entry["id"]]
    assert record["status"] == "success"
    assert "enlaces-externos-no-seguidos: 2" in record["warnings"]


# -- normalización ----------------------------------------------------------------
def test_normaliza_txt_e_indice(subject):
    entry = make_txt(subject, b"Ejercicio 3\r\n\r\nCalcular el n\xc3\xbacleo.\r\n\r\nEjercicio 4\r\n\r\nOtro.\r\n")
    run_extract(subject, EngineSinTxt(), ids=[entry["id"]])
    result = run_normalize(subject, ids=[entry["id"]])
    assert sum(result.values()) >= 1
    index = json.loads((subject.index / f"{entry['id']}.json").read_text(encoding="utf-8"))
    titles = [s["title"] for s in index["sections"]]
    assert any("Ejercicio 3" in t for t in titles)
    assert "Calcular el núcleo." in (subject.normalized / f"{entry['id']}.md").read_text(encoding="utf-8")
