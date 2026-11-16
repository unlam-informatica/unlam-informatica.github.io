"""Extracción real con Docling. Requiere el extra `extract` y descarga modelos la primera vez."""
import json

import pytest
from conftest import minimal_pdf

pytest.importorskip("docling")
pytestmark = pytest.mark.integration

from content_pipeline.extract import DoclingEngine, run_extract  # noqa: E402
from content_pipeline.ingest import run_inventory  # noqa: E402
from content_pipeline.normalize import run_normalize  # noqa: E402


def test_docling_convierte_pdf_docx_y_conserva_paginas(subject):
    import zipfile

    docx = subject.raw / "teoria" / "nota.docx"
    with zipfile.ZipFile(docx, "w") as archive:
        archive.writestr("[Content_Types].xml",
                         '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/'
                         'content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-'
                         'package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>'
                         '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-'
                         'officedocument.wordprocessingml.document.main+xml"/></Types>')
        archive.writestr("_rels/.rels",
                         '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/'
                         '2006/relationships"><Relationship Id="r1" Type="http://schemas.openxmlformats.org/'
                         'officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
                         '</Relationships>')
        archive.writestr("word/document.xml",
                         '<?xml version="1.0"?><w:document xmlns:w="http://schemas.openxmlformats.org/'
                         'wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Teorema de la dimension</w:t>'
                         '</w:r></w:p></w:body></w:document>')
    (subject.raw / "practicas" / "guia.pdf").write_bytes(minimal_pdf(["Ejercicio 1 base", "Ejercicio 2 rango"]))
    run_inventory(subject)
    engine = DoclingEngine(device="cpu")
    counts = run_extract(subject, engine, profile="text")
    assert counts["failed"] == 0, json.loads(subject.manifest.read_text())
    run_normalize(subject)
    text = "\n".join(p.read_text(encoding="utf-8") for p in subject.markdown.glob("*.md"))
    assert "Ejercicio 2 rango" in text and "<!-- page: 2 -->" in text
    assert "Teorema de la dimension" in text
