import json

from conftest import FakeEngine

from content_pipeline.extract import run_extract
from content_pipeline.ingest import run_inventory
from content_pipeline.normalize import classify_title, detect_flags, normalize_markdown, run_normalize


def pages(*bodies):
    return "\n".join(f"<!-- page: {i} -->\n\n{body}\n" for i, body in enumerate(bodies, start=1))


def test_quita_encabezados_repetidos_pero_no_formulas():
    words = ["uno", "dos", "tres", "cuatro"]
    md = pages(*[f"UNLaM — Álgebra II\nPág. {i} de 4\n\n$$\nx+y=0\n$$\n\nTexto {w}" for i, w in enumerate(words, 1)])
    text, _, report = normalize_markdown(md)
    assert "UNLaM — Álgebra II" not in text and "Pág." not in text
    assert text.count("x+y=0") == 4
    assert report["removed_repeated_lines"] == 8


def test_no_borra_titulos_repetidos_en_el_cuerpo():
    body = "Encabezado\n\nA\n\nB\n\nC\n\nEjercicio {i}\n\nD\n\nE\n\nF\n\nPie"
    text, _, _ = normalize_markdown(pages(*[body.format(i=i) for i in range(1, 5)]))
    assert "Encabezado" not in text and "Pie" not in text
    assert text.count("### Ejercicio") == 4


def test_jerarquia_de_titulos_sin_saltos():
    text, sections, _ = normalize_markdown(pages("### Unidad 1\n\nA\n\n##### Subespacios\n\nB\n\n### Bases\n\nC"))
    assert [s.level for s in sections if s.level] == [1, 2, 1]
    assert "# Unidad 1" in text and "## Subespacios" in text


def test_titulos_implicitos_y_tipos():
    text, sections, report = normalize_markdown(pages("**Ejercicio 3.** Hallar una base.", "Resolución\n\nTexto"))
    assert report["pseudo_headings"] == 1
    assert "### Ejercicio 3" in text
    assert sections[1].kind == "enunciado"
    assert classify_title("2. Resolución del ejercicio") == "resolucion"
    assert classify_title("Teorema de la dimensión") == "teoria"


def test_paginas_y_secciones_trazables():
    _, sections, report = normalize_markdown(pages("# A\n\nuno", "dos", "# B\n\ntres"))
    a, b = [s for s in sections if s.level]
    assert (a.page_start, a.page_end) == (1, 2)
    assert (b.page_start, b.page_end) == (3, 3)
    assert report["pages"] == 3


def test_marcas_de_formulas_dudosas():
    assert "delimitadores-desbalanceados" in detect_flags("Sea $x \\in V un vector")
    assert "formula-no-decodificada" in detect_flags("<!-- formula-not-decoded -->")
    assert "glifos-cid" in detect_flags("(cid:42)")
    assert detect_flags("Sea $x \\in V$ y `a$b`") == []


def test_no_modifica_el_interior_de_las_formulas():
    body = "$$\n\\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}\n$$"
    text, _, _ = normalize_markdown(pages(body))
    assert body in text


def test_paginas_vacias_y_secciones_vacias():
    _, sections, report = normalize_markdown(pages("# Título\n\n# Otro\n\ntexto", "   "))
    assert report["empty_pages"] == [2]
    assert any("seccion-vacia" in s.flags for s in sections)


def test_parrafos_repetidos_se_informan():
    paragraph = "Un párrafo largo " * 10
    _, _, report = normalize_markdown(pages(paragraph, paragraph))
    assert report["repeated_paragraphs"] == 1


def test_run_normalize_idempotente(subject):
    run_inventory(subject)
    run_extract(subject, FakeEngine())
    first = run_normalize(subject)
    assert first["normalized"] == 2 and first["pending_extraction"] == 0
    second = run_normalize(subject)
    assert second["cached"] == 2 and second["normalized"] == 0
    index = json.loads(next(subject.index.glob("*.json")).read_text(encoding="utf-8"))
    assert index["sections"] and "report" in index
