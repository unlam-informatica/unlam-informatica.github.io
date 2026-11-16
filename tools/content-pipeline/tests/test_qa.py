import json
import textwrap

from content_pipeline.qa import math_syntax_issues, run_qa

LONG = "Texto explicativo suficientemente largo para no considerarse una página vacía. " * 6

PAGE = textwrap.dedent("""\
    ---
    title: Bases
    slug: demo/unidad-1/bases
    ---
    {long}

    Ver [subespacios](/demo/unidad-1/subespacios/) y [otra](/demo/no-existe/).

    ### Ejercicio 1
    <!-- ejercicio: U1.01 | nivel: inicial | tipo: calculo | verificacion: sympy -->

    :::note[Enunciado]
    Hallar una base de $W$.
    :::

    <details>
    <summary>Resolución</summary>

    La base es $\\{{(1,0)\\}}$.

    </details>

    ### Ejercicio 2
    <!-- ejercicio: U1.02 | nivel: experto | tipo: demostracion | verificacion: razonamiento -->

    :::note[Enunciado]
    Demostrar que $\\operatorname{{Ker}} T$ es subespacio.
    :::
    """)


def build(tmp_path, page=PAGE):
    docs = tmp_path / "src" / "content" / "docs"
    (docs / "demo" / "unidad-1").mkdir(parents=True)
    (docs / "demo" / "unidad-1" / "bases.md").write_text(page.format(long=LONG), encoding="utf-8")
    (docs / "demo" / "unidad-1" / "subespacios.md").write_text(
        f"---\ntitle: Subespacios\nslug: demo/unidad-1/subespacios\n---\n{LONG}\n\nTODO: completar.\n",
        encoding="utf-8")
    return docs


def codes(report):
    return {f["code"] for f in report["findings"]}


def test_detecta_problemas_de_contenido(tmp_path):
    docs = build(tmp_path)
    math = tmp_path / "math.json"
    math.write_text(json.dumps({"results": [{"id": "U1.01", "status": "passed"}]}), encoding="utf-8")
    config = tmp_path / "subject.yaml"
    config.write_text('qa:\n  forbidden:\n    - pattern: "operatorname\\\\{Ker\\\\}"\n      message: Usar Nu\n',
                      encoding="utf-8")
    report = run_qa(docs, "demo", math_report=math, subject_config=config, report_path=tmp_path / "qa.json")
    found = codes(report)
    assert {"enlace-roto", "contenido-provisional", "sin-resolucion", "nivel-invalido", "notacion"} <= found
    assert "sin-comprobacion" not in found  # U1.01 tiene comprobación aprobada
    assert report["exercises"] == 2 and report["exercises_sympy"] == 1
    assert (tmp_path / "qa.md").exists()


def test_ejercicio_sin_comprobacion_y_minimos(tmp_path):
    docs = build(tmp_path)
    math = tmp_path / "math.json"
    math.write_text(json.dumps({"results": []}), encoding="utf-8")
    curriculum = tmp_path / "curriculum.yaml"
    curriculum.write_text(textwrap.dedent("""\
        minimums: {exercises_per_unit: 15, levels_per_unit: 1}
        units:
          - id: u1
            title: U1
            exercise_prefix: "U1."
            topics:
              - {id: t1, title: Bases, page: /demo/unidad-1/bases/, exercises: [U1.01, U1.99], production: redactado}
              - {id: t2, title: Otro, page: /demo/unidad-9/x/, production: pendiente}
        """), encoding="utf-8")
    report = run_qa(docs, "demo", curriculum_path=curriculum, math_report=math)
    found = codes(report)
    assert {"sin-comprobacion", "ejercicios-insuficientes", "nivel-insuficiente", "ejercicio-inexistente",
            "tema-sin-pagina", "tema-no-redactado"} <= found
    assert report["units"]["u1"]["exercises"] == 2


def test_delimitadores_de_formulas():
    assert math_syntax_issues("$$\nx\n$$\n\nSea $a$ y $b$.") == []
    assert any("línea propia" in i for i in math_syntax_issues("Texto $$x$$"))
    assert any("desbalanceado" in i for i in math_syntax_issues("Sea $a y b."))
    assert any("sin cerrar" in i for i in math_syntax_issues("$$\nx\n"))


def test_marcadores_de_comprobacion_en_ejemplos(tmp_path):
    docs = build(tmp_path)
    page = docs / "demo" / "unidad-1" / "subespacios.md"
    page.write_text(page.read_text(encoding="utf-8").replace("TODO: completar.", "<!-- check: U1.T01.E1 -->\n<!-- check: U1.T01.E2 -->"),
                    encoding="utf-8")
    math = tmp_path / "math.json"
    math.write_text(json.dumps({"results": [{"id": "U1.T01.E1", "status": "passed"},
                                             {"id": "U1.01", "status": "passed"}]}), encoding="utf-8")
    report = run_qa(docs, "demo", math_report=math)
    missing = [f for f in report["findings"] if f["code"] == "sin-comprobacion"]
    assert [m["message"] for m in missing] == ["El ejemplo marca U1.T01.E2 pero no hay comprobación aprobada"]
    assert report["example_checks"] == 2


def test_la_palabra_todo_no_es_un_marcador_provisional():
    from content_pipeline.qa import PLACEHOLDER_RE
    assert not PLACEHOLDER_RE.search("Todo subespacio contiene al nulo y todos sus elementos.")
    assert PLACEHOLDER_RE.search("TODO: revisar") and PLACEHOLDER_RE.search("Página En Construcción")
