"""Fixtures distribuibles: todos los documentos de prueba se generan en el momento."""
from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from content_pipeline.config import subject_paths
from content_pipeline.extract import EngineOutput, PageText
from content_pipeline.logging_utils import configure


def minimal_pdf(pages: list[str]) -> bytes:
    """PDF válido de varias páginas con una línea de texto en Helvetica por página."""
    objects: list[bytes] = []
    count = len(pages)
    kids = " ".join(f"{3 + 2 * i} 0 R" for i in range(count))
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {count} >>".encode())
    font_id = 3 + 2 * count
    for index, text in enumerate(pages):
        content_id = 4 + 2 * index
        objects.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents {content_id} 0 R "
                       f"/Resources << /Font << /F1 {font_id} 0 R >> >> >>".encode())
        stream = f"BT /F1 14 Tf 72 760 Td ({text}) Tj ET".encode()
        objects.append(b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for number, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{number} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode()
    out += b"".join(f"{offset:010d} 00000 n \n".encode() for offset in offsets)
    out += f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    return bytes(out)


SUBJECT_YAML = textwrap.dedent("""\
    id: demo
    id_prefix: demo
    defaults:
      license: privado-catedra
      distribution: privado
    rules:
      - match: "teoria/*"
        doc_type: apunte
        source: Cátedra de prueba
        units: [u1]
      - match: "practicas/*"
        doc_type: guia-practica
        source: Cátedra de prueba
        units: [u1]
      - match: "*libro*"
        doc_type: bibliografia
        source: Editorial de prueba
        extraction: front-matter
      - match: "*.mp4"
        doc_type: clase-grabada
        extraction: skip
    qa:
      forbidden:
        - pattern: "operatorname\\\\{Ker\\\\}"
          message: "Usar Nu(T) para el núcleo"
    """)


class FakeEngine:
    """Motor determinista: una página por línea no vacía del archivo (o del texto del PDF)."""

    name = "fake"
    version = "1.0"

    def __init__(self, fail_on: set[str] | None = None) -> None:
        self.calls: list[str] = []
        self.fail_on = fail_on or set()

    def supports(self, fmt: str) -> bool:
        return fmt in {"pdf", "docx", "markdown", "image", "video", "audio"}

    def convert(self, path: Path, fmt: str, options: dict) -> EngineOutput:
        self.calls.append(path.name)
        if path.name in self.fail_on:
            raise RuntimeError("documento corrupto")
        raw = path.read_bytes()
        if raw.startswith(b"%PDF"):
            import re
            lines = [m.decode() for m in re.findall(rb"\((.*?)\) Tj", raw)]
        else:
            lines = [l for l in raw.decode("utf-8", "replace").split("\n---page---\n")]
        pages = [PageText(i, text) for i, text in enumerate(lines, start=1)]
        if options.get("max_pages"):
            pages = pages[: options["max_pages"]]
        return EngineOutput(status="success", pages=pages, document={"pages": len(pages)},
                            images=[("p001-fig001.png", 1, b"\x89PNG fake")] if options.get("images") else [],
                            stats={"pages": len(pages), "formulas": 0, "formulas_undecoded": 0})


@pytest.fixture(autouse=True)
def _quiet_logs():
    configure("error", "text")


@pytest.fixture
def subject(tmp_path: Path):
    root = tmp_path / "academic-sources" / "demo"
    raw = root / "raw"
    (raw / "teoria").mkdir(parents=True)
    (raw / "practicas").mkdir()
    (raw / "otros" / "copias").mkdir(parents=True)
    (root / "subject.yaml").write_text(SUBJECT_YAML, encoding="utf-8")
    (raw / "teoria" / "espacios.md").write_text(
        "# Espacios vectoriales\n\nUn subespacio es cerrado por la suma.\n---page---\n"
        "## Base y dimensión\n\nUna base es un conjunto generador linealmente independiente.\n",
        encoding="utf-8")
    copy = (raw / "teoria" / "espacios.md").read_bytes()
    (raw / "otros" / "copias" / "espacios (copia).md").write_bytes(copy)
    (raw / "practicas" / "guia.pdf").write_bytes(minimal_pdf(["Ejercicio 1 base de R3", "Resolucion del ejercicio 1"]))
    (raw / "practicas" / "notas.txt").write_text("formato no compatible", encoding="utf-8")
    (raw / "clase.mp4").write_bytes(b"\x00\x00\x00\x18ftypmp42")
    (raw / ".DS_Store").write_bytes(b"x")
    return subject_paths("demo", tmp_path / "academic-sources")
