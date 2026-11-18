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


def test_formulas_dentro_de_html():
    assert any("summary" in i for i in math_syntax_issues("<details>\n<summary>¿Es $x$ cero?</summary>\n\nSí.\n\n</details>"))
    assert any("figcaption" in i for i in math_syntax_issues("<figcaption>El vector $v$.</figcaption>"))
    assert math_syntax_issues("<summary>Resolución</summary>\n\nSea $x$.") == []


# --- operadores MongoDB y montos ---------------------------------------------------------------

def _mongo_codes(body, title="Pipeline"):
    from content_pipeline.qa import dollar_findings
    return dollar_findings(body)


def test_operadores_mongodb_sin_codigo_en_parrafos_y_titulos(tmp_path):
    body = ("## Etapa $match y $group\n\nCalcula con $$NOW la fecha y suma \"$a.b\" por grupo.\n\n"
            "Esto está bien: `$match` y `$$ROOT`.\n\n```js\n{ $group: { _id: \"$x\" } }\n```\n")
    operators, _ = _mongo_codes(body)
    assert set(operators) == {"$match", "$group", "$$NOW", '"$a.b"'}
    assert _mongo_codes("Solo `$lookup` y `$$ROOT` en código.\n") == ([], [])
    docs = tmp_path / "src" / "content" / "docs"
    (docs / "demo").mkdir(parents=True)
    (docs / "demo" / "a.md").write_text(
        f"---\ntitle: Agregación con $sum\nslug: demo/a\n---\n{LONG}\n\nUsa $project y $unwind juntos.\n", encoding="utf-8")
    report = run_qa(docs, "demo")
    found = [f for f in report["findings"] if f["code"] == "operador-mongodb-sin-codigo"]
    assert len(found) == 1 and found[0]["severity"] == "error"
    assert "$project" in found[0]["message"] and "$sum" in found[0]["message"]
    assert "formula-mal-delimitada" not in codes(report)


def test_montos_con_signo_pesos(tmp_path):
    operators, amounts = _mongo_codes("Cuesta $500 y luego $ 1.000,50 más.\n")
    assert operators == [] and amounts == ["$500", "$ 1.000,50"]
    assert math_syntax_issues("Cuesta $500 y $ 1.000,50.") == []
    docs = tmp_path / "src" / "content" / "docs"
    (docs / "demo").mkdir(parents=True)
    (docs / "demo" / "a.md").write_text(
        f"---\ntitle: Precios\nslug: demo/a\n---\n{LONG}\n\nEl total es $500.\n", encoding="utf-8")
    report = run_qa(docs, "demo")
    assert [f["severity"] for f in report["findings"] if f["code"] == "monto-con-signo-pesos"] == ["warning"]
    assert "formula-mal-delimitada" not in codes(report)


def test_formulas_reales_siguen_controlandose():
    for ok in ("Sea $x$ y $\\alpha$ con $a_1$ y $x+y=2$.", "Valen $2x+1$ y $1,1,2$ y $2$.", "Uso $match y $x$."):
        assert math_syntax_issues(ok) == [], ok
    assert any("desbalanceado" in i for i in math_syntax_issues("Sea $x suelto."))
    assert any("desbalanceado" in i for i in math_syntax_issues("Con $$NOW y $x suelto."))
    assert math_syntax_issues("Con `$x` en línea y $$ROOT.") == []
    assert _mongo_codes("Sea $x$ y $a_1$.") == ([], [])


# --- mínimos por unidad, motor, revisado, resoluciones completas --------------------------------

def _exercise(ex_id, level="inicial", verification="razonamiento", solution=None, check=True):
    if solution is None:
        solution = "Resolver.\n\n```python\nprint(1)\n```\n\nResultado esperado: 1\n"
    marker = f"<!-- check: {ex_id} -->\n" if check else ""
    return (f"### Ejercicio {ex_id}\n<!-- ejercicio: {ex_id} | nivel: {level} | tipo: calculo | "
            f"verificacion: {verification} -->\n{marker}\n:::note[Enunciado]\nHacer.\n:::\n\n"
            f"<details>\n<summary>Resolución</summary>\n\n{solution}\n</details>\n\n")


def _setup(tmp_path, exercises, unit_extra="", minimums="{exercises_per_unit: 1, levels_per_unit: 0}",
           code_report=None, reviewed=None):
    docs = tmp_path / "src" / "content" / "docs"
    (docs / "demo").mkdir(parents=True)
    (docs / "demo" / "a.md").write_text(
        f"---\ntitle: A\nslug: demo/a\n---\n{LONG}\n\n" + "".join(exercises), encoding="utf-8")
    root = tmp_path / "academic"
    (root / "reports").mkdir(parents=True)
    (root / "checks").mkdir()
    curriculum = root / "curriculum.yaml"
    curriculum.write_text(f"minimums: {minimums}\nunits:\n  - id: u1\n    title: U1\n    exercise_prefix: \"U1.\"\n"
                          f"{unit_extra}    topics: []\n", encoding="utf-8")
    if code_report is not None:
        (root / "reports" / "code-verification.json").write_text(json.dumps(code_report), encoding="utf-8")
    if reviewed is not None:
        (root / "checks" / "reviewed.yaml").write_text(reviewed, encoding="utf-8")
    return docs, curriculum


def _by_code(report, code):
    return [f for f in report["findings"] if f["code"] == code]


def test_minimos_por_unidad_reemplazan_al_global(tmp_path):
    exercises = [_exercise("U1.01"), _exercise("U1.02", "intermedio")]
    docs, curriculum = _setup(tmp_path, exercises, unit_extra="    minimum_exercises: 3\n    minimum_per_level: 1\n",
                              minimums="{exercises_per_unit: 1, levels_per_unit: 0}")
    report = run_qa(docs, "demo", curriculum_path=curriculum)
    assert _by_code(report, "ejercicios-insuficientes")[0]["message"] == "2 < 3"
    assert {f["message"].split(":")[0] for f in _by_code(report, "nivel-insuficiente")} == {"avanzado"}
    assert report["units"]["u1"]["complete"] == 2
    # sin claves por unidad se usa el global
    docs2, curriculum2 = _setup(tmp_path / "otro", exercises)
    assert not _by_code(run_qa(docs2, "demo", curriculum_path=curriculum2), "ejercicios-insuficientes")


def test_ejercicio_incompleto_no_cuenta_para_minimos(tmp_path):
    exercises = [_exercise("U1.01", solution="Resolver.\n\n```python\n# TODO\n...\n```\n")]
    docs, curriculum = _setup(tmp_path, exercises)
    report = run_qa(docs, "demo", curriculum_path=curriculum)
    assert _by_code(report, "resolucion-incompleta")
    assert _by_code(report, "ejercicios-insuficientes")[0]["message"] == "0 < 1"
    assert report["units"]["u1"]["exercises"] == 1 and report["units"]["u1"]["incomplete"] == 1


def test_motor_con_check_aprobado_fallido_o_ausente(tmp_path):
    exercises = [_exercise("U1.01", verification="motor"), _exercise("U1.02", verification="motor"),
                 _exercise("U1.03", verification="motor")]
    report_json = {"checks": [{"id": "U1.01", "status": "aprobado"}, {"id": "U1.02", "status": "fallido"}], "reviewed": []}
    docs, curriculum = _setup(tmp_path, exercises, code_report=report_json)
    math = tmp_path / "math.json"
    math.write_text(json.dumps({"results": []}), encoding="utf-8")
    report = run_qa(docs, "demo", curriculum_path=curriculum, math_report=math)
    assert [f["where"].split()[-1] for f in _by_code(report, "verificacion-motor-fallida")] == ["U1.02"]
    assert [f["where"].split()[-1] for f in _by_code(report, "sin-verificacion-motor")] == ["U1.03"]
    assert not _by_code(report, "sin-reporte-de-codigo")
    assert not _by_code(report, "sin-comprobacion")  # los marcadores de motor no son ejemplos SymPy
    assert report["units"]["u1"]["motor"] == 3


def test_motor_sin_reporte_de_codigo(tmp_path):
    docs, curriculum = _setup(tmp_path, [_exercise("U1.01", verification="motor")])
    report = run_qa(docs, "demo", curriculum_path=curriculum)
    assert _by_code(report, "sin-reporte-de-codigo")


def test_revisado_con_y_sin_reviewed_yaml(tmp_path):
    exercises = [_exercise("U1.01", verification="revisado"), _exercise("U1.02", verification="revisado")]
    docs, curriculum = _setup(tmp_path, exercises, reviewed="- {id: U1.01, reason: revisado a mano}\n")
    report = run_qa(docs, "demo", curriculum_path=curriculum)
    assert [f["where"].split()[-1] for f in _by_code(report, "sin-revision")] == ["U1.02"]
    docs2, curriculum2 = _setup(tmp_path / "sin", exercises)
    assert len(_by_code(run_qa(docs2, "demo", curriculum_path=curriculum2), "sin-revision")) == 2
    assert not _by_code(report, "resolucion-incompleta")


def test_resoluciones_incompletas(tmp_path):
    exercises = [
        _exercise("U1.01", "inicial", "razonamiento", solution="Algo.\n\n```python\n\n```\n"),
        _exercise("U1.02", "inicial", "revisado", solution="Algo.\n\n```python\nprint(1)\n```\n"),
        _exercise("U1.03", "inicial", "revisado", solution="Algo.\n\nResultado esperado: 1\n"),
        _exercise("U1.04", "inicial", "revisado", solution="Algo.\n\n```python\nprint(1)\n```\n\nRESULTADO ESPERADO: 1\n"),
        _exercise("U1.05", "inicial", "motor", check=False),
        _exercise("U1.06", "inicial", "motor"),
    ]
    docs, curriculum = _setup(tmp_path, exercises, reviewed="- {id: U1.04, reason: x}\n- {id: U1.02, reason: x}\n- {id: U1.03, reason: x}\n",
                              code_report={"checks": [{"id": "U1.05", "status": "aprobado"}, {"id": "U1.06", "status": "aprobado"}]})
    report = run_qa(docs, "demo", curriculum_path=curriculum)
    incomplete = {f["where"].split()[-1]: f["message"] for f in _by_code(report, "resolucion-incompleta")}
    assert set(incomplete) == {"U1.01", "U1.02", "U1.03", "U1.05"}
    assert "vacío" in incomplete["U1.01"] and "check: U1.05" in incomplete["U1.05"]
    assert report["units"]["u1"]["complete"] == 2
    assert report["units"]["u1"]["complete_by_verification"] == {"revisado": 1, "motor": 1}


def test_marcador_de_ejemplo_respaldado_por_reporte_de_codigo(tmp_path):
    import json

    from content_pipeline.qa import run_qa

    docs = tmp_path / "docs" / "demo"
    docs.mkdir(parents=True)
    (docs / "p.md").write_text("---\ntitle: P\nslug: demo/p\n---\n<!-- check: E.1 -->\n```sql\nSELECT 1;\n```\n"
                               "<!-- check: E.2 -->\n```sql\nSELECT 2;\n```\n", encoding="utf-8")
    subject = tmp_path / "subj"
    (subject / "reports").mkdir(parents=True)
    (subject / "curriculum-map.yaml").write_text("units: []\n", encoding="utf-8")
    (subject / "reports" / "code-verification.json").write_text(json.dumps(
        {"checks": [{"id": "E.1", "status": "aprobado"}, {"id": "E.2", "status": "fallido"}]}), encoding="utf-8")
    report = run_qa(tmp_path / "docs", "demo", curriculum_path=subject / "curriculum-map.yaml",
                    math_report=subject / "reports" / "math-verification.json")
    codes = [(f["code"], f["message"]) for f in report["findings"]]
    assert not any(c == "sin-reporte-matematico" for c, _ in codes)
    assert not any(c == "sin-comprobacion" for c, _ in codes)
    assert any(c == "verificacion-fallida" and "E.2" in m for c, m in codes)
