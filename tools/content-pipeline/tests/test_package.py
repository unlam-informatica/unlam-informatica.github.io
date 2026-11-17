import json
import textwrap

import pytest
from conftest import FakeEngine

from content_pipeline.config import PipelineError
from content_pipeline.extract import run_extract
from content_pipeline.ingest import load_catalog, run_inventory
from content_pipeline.normalize import run_normalize
from content_pipeline.package import load_curriculum, run_package, score_section


def prepare(subject, curriculum: str):
    run_inventory(subject)
    run_extract(subject, FakeEngine())
    run_normalize(subject)
    ids = {d["path"]: d["id"] for d in load_catalog(subject)["documents"]}
    subject.curriculum.write_text(textwrap.dedent(curriculum).format(**{
        "theory": ids["teoria/espacios.md"], "guide": ids["practicas/guia.pdf"]}), encoding="utf-8")
    return ids


CURRICULUM = """\
    subject: demo
    bibliography:
      - id: poole
        citation: "Poole, D. (2017). Álgebra lineal. Una introducción moderna (4.ª ed.). Cengage."
    units:
      - id: u1
        title: Espacios vectoriales
        topics:
          - id: u1-base
            title: Base y dimensión
            keywords: [base, dimensión, linealmente independiente]
            objectives: [Hallar bases de subespacios]
            bibliography: ["poole:§3.5"]
            sources:
              - doc: {guide}
                pages: [1]
          - id: u1-codigos
            title: Códigos de Hamming
            keywords: [hamming]
            auto_sources: false
    """


def test_paquete_con_fragmentos_trazables(subject):
    ids = prepare(subject, CURRICULUM)
    result = run_package(subject)
    assert result["packages"] == 2
    package = json.loads((subject.context / "u1" / "u1-base.json").read_text(encoding="utf-8"))
    docs = {f["doc"] for f in package["fragments"]}
    assert ids["teoria/espacios.md"] in docs  # elegido por palabra clave (unidad u1)
    assert ids["practicas/guia.pdf"] in docs  # asignado por página
    assigned = next(f for f in package["fragments"] if f["doc"] == ids["practicas/guia.pdf"])
    assert assigned["explicit"] and assigned["pages"] == "pp. 1–2"  # la sección sigue en la p. 2
    assert package["bibliography"][0]["locator"] == "§3.5"
    assert package["exercises"]  # la guía tiene "Ejercicio 1"
    markdown = (subject.context / "u1" / "u1-base.md").read_text(encoding="utf-8")
    assert f"[{ids['practicas/guia.pdf']} · pp. 1–2]" in markdown
    assert "## Objetivos" in markdown


def test_temas_sin_material_se_informan(subject):
    prepare(subject, CURRICULUM)
    result = run_package(subject)
    assert result["topics_without_sources"] == ["u1-codigos"]
    index = json.loads((subject.context / "index.json").read_text(encoding="utf-8"))
    assert {"sin-material-fuente", "sin-ejercicios-de-referencia"} <= set(index[1]["gaps"])


def test_filtro_por_tema_y_presupuesto(subject):
    prepare(subject, CURRICULUM)
    result = run_package(subject, topic_id="u1-base", budget=50)
    assert result["packages"] == 1
    package = json.loads((subject.context / "u1" / "u1-base.json").read_text(encoding="utf-8"))
    assert package["budget"]["used"] <= 50 + 4000
    with pytest.raises(PipelineError):
        run_package(subject, topic_id="no-existe")


def test_matriz_invalida(subject):
    subject.curriculum.write_text("units:\n  - id: u1\n    title: X\n    topics:\n      - id: a\n", encoding="utf-8")
    with pytest.raises(PipelineError, match="title"):
        load_curriculum(subject)


def test_puntaje_por_palabras_clave():
    assert score_section("Base de un subespacio", "texto", ["base"]) == 3
    assert score_section("Otro", "dimensión y DIMENSION", ["dimensión"]) == 2
    assert score_section("Otro", "nada", ["base"]) == 0
