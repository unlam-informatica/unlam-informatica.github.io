"""Pruebas de codecheck con un runner falso (sin Docker) y una prueba de integración real."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from content_pipeline import codecheck
from content_pipeline.codecheck import RunResult, normalize_output, sanitize_id
from content_pipeline.config import PipelineError, SubjectPaths


class FakeRunner:
    def __init__(self, outputs=None):
        self.outputs = outputs or {}
        self.calls = []
        self.ready = True

    def ensure_ready(self, engines):
        if not self.ready:
            raise PipelineError("motores apagados: engines up")

    def versions(self, engines):
        return {e: f"v-{e}" for e in engines}

    def _run(self, engine, db, script, timeout):
        self.calls.append((engine, db, script))
        return self.outputs.get(db, RunResult(0, ""))

    def run_sql(self, db, script, timeout):
        return self._run("mssql", db, script, timeout)

    def run_mongo(self, db, script, timeout):
        return self._run("mongo", db, script, timeout)


@pytest.fixture
def subj(tmp_path):
    root = tmp_path / "academic-sources" / "demo"
    (root / "checks" / "sql").mkdir(parents=True)
    (root / "checks" / "mongo").mkdir(parents=True)
    (root / "subject.yaml").write_text("engines:\n  mssql: {image: img-sql, container: c1}\n"
                                       "  mongo: {image: img-mongo, container: c2}\n", encoding="utf-8")
    docs = tmp_path / "docs"
    docs.mkdir()
    return SubjectPaths("demo", root), docs


def add(paths, kind, check_id, script="SELECT 1;", expected=None):
    ext = "sql" if kind == "sql" else "js"
    (paths.root / "checks" / kind / f"{check_id}.{ext}").write_text(script, encoding="utf-8")
    if expected is not None:
        (paths.root / "checks" / kind / f"{check_id}.expected").write_text(expected, encoding="utf-8")


def verify(paths, docs, runner, **kw):
    return codecheck.run_verify_code(paths, runner, docs_root=docs, **kw)


def test_normalize_output():
    assert normalize_output("a  \r\n\r\n b\t\n\n") == "a\n b"


def test_sanitize_id_con_puntos():
    assert sanitize_id("U1.T03.E2") == "chk_U1_T03_E2"


def test_aprobado_fallido_error_y_contrato(subj):
    paths, docs = subj
    add(paths, "sql", "U1.01", expected="1|a\n")
    add(paths, "sql", "U1.02", expected="x\n")
    add(paths, "sql", "U1.03")
    add(paths, "mongo", "M.1", script="print(1)")
    runner = FakeRunner({
        "chk_U1_01": RunResult(0, "1|a  \r\n\r\n"),
        "chk_U1_02": RunResult(0, "y\n"),
        "chk_U1_03": RunResult(1, "", "Msg 102\nsintaxis"),
    })
    report = verify(paths, docs, runner)
    by_id = {c["id"]: c for c in report["checks"]}
    assert by_id["U1.01"]["status"] == "aprobado" and by_id["U1.01"]["expected"] is True
    assert by_id["U1.02"]["status"] == "fallido" and "-x" in by_id["U1.02"]["message"]
    assert by_id["U1.03"]["status"] == "error" and "sintaxis" in by_id["U1.03"]["message"]
    assert by_id["M.1"]["status"] == "aprobado" and by_id["M.1"]["engine"] == "mongo"
    assert by_id["U1.01"]["script"] == "checks/sql/U1.01.sql"
    assert report["summary"] == {"executed": 4, "passed": 2, "failed": 1, "errors": 1, "reviewed": 0, "pending": 0,
                                 "syntax_templates": 0}
    assert set(report) == {"subject", "generated", "engines", "checks", "reviewed", "pending", "orphan_markers", "syntax_templates",
                           "summary"}
    assert report["engines"]["mssql"] == {"image": "img-sql", "version": "v-mssql"}
    assert set(by_id["U1.01"]) == {"id", "engine", "status", "script", "expected", "seconds", "message"}
    out = paths.root / "reports"
    assert json.loads((out / "code-verification.json").read_text())["subject"] == "demo"
    md = (out / "code-verification.md").read_text()
    assert "## Ejecutados" in md and "## Pendientes de verificación específica" in md and "## Pendientes" in md


def test_ids_filtra_y_desconocido(subj):
    paths, docs = subj
    add(paths, "sql", "A")
    add(paths, "sql", "B")
    runner = FakeRunner()
    assert [c["id"] for c in verify(paths, docs, runner, ids=["B"])["checks"]] == ["B"]
    with pytest.raises(PipelineError):
        verify(paths, docs, runner, ids=["Z"])


def test_motores_apagados(subj):
    paths, docs = subj
    add(paths, "sql", "A")
    runner = FakeRunner()
    runner.ready = False
    with pytest.raises(PipelineError, match="engines up"):
        verify(paths, docs, runner)


def test_script_recibe_nombre_de_base_saneado(subj):
    paths, docs = subj
    add(paths, "mongo", "U1.T03.E2", script="print(1)")
    runner = FakeRunner()
    verify(paths, docs, runner)
    assert runner.calls[0][:2] == ("mongo", "chk_U1_T03_E2")


def test_reviewed_valido_e_invalido(subj):
    paths, docs = subj
    path = paths.root / "checks" / "reviewed.yaml"
    path.write_text("- {id: R1, reason: motivo, reviewer: yo, date: 2026-11-17, page: a/b.md}\n", encoding="utf-8")
    report = verify(paths, docs, FakeRunner())
    assert report["reviewed"] == [{"id": "R1", "reason": "motivo", "reviewer": "yo", "date": "2026-11-17",
                                   "page": "a/b.md"}]
    assert report["summary"]["reviewed"] == 1
    path.write_text("- {id: R1, reason: motivo}\n", encoding="utf-8")
    with pytest.raises(PipelineError, match="reviewer"):
        verify(paths, docs, FakeRunner())


def test_pendientes_y_huerfanos(subj):
    paths, docs = subj
    add(paths, "sql", "D1")
    (paths.root / "checks" / "reviewed.yaml").write_text(
        "- {id: R1, reason: x, reviewer: y, date: '2026-01-01', page: p.md}\n", encoding="utf-8")
    (docs / "sub").mkdir()
    (docs / "sub" / "p.md").write_text(
        "# T\n\n<!-- check: D1 -->\n```sql\nSELECT 1;\n```\n\n"      # marcado
        "```sql\nSELECT 2;\n```\n\n"                                  # pendiente (línea 8)
        "<!-- check: R1 -->\n\n```js\nx\n```\n\n"                     # revisado
        "<!-- check: FALTA -->\n\ntexto\n\n"                          # huérfano
        "```text\n<!-- check: DENTRO -->\n```\n"                      # dentro de cerco, ignorado
        "```mongodb\ndb.a.find()\n```\n", encoding="utf-8")
    report = verify(paths, docs, FakeRunner())
    assert report["pending"] == [{"page": "sub/p.md", "line": 8, "language": "sql"},
                                 {"page": "sub/p.md", "line": 25, "language": "mongodb"}]
    assert report["orphan_markers"] == [{"id": "FALTA", "page": "sub/p.md", "line": 18}]
    assert "### sub/p.md (2)" in (paths.root / "reports" / "code-verification.md").read_text()


def test_marcador_lejano_no_cuenta(subj):
    paths, docs = subj
    add(paths, "sql", "D1")
    (docs / "p.md").write_text("<!-- check: D1 -->\na\nb\nc\n```sql\nx\n```\n", encoding="utf-8")
    assert len(verify(paths, docs, FakeRunner())["pending"]) == 1


@pytest.mark.integration
def test_docker_real(subj):
    if shutil.which("docker") is None or subprocess.run(["docker", "info"], capture_output=True).returncode != 0:
        pytest.skip("Docker no disponible")
    paths, docs = subj
    repo_yaml = Path(__file__).resolve().parents[3] / "academic-sources" / "bbdd-aplicadas" / "subject.yaml"
    if not repo_yaml.exists():
        pytest.skip("sin subject.yaml de bbdd-aplicadas")
    shutil.copy(repo_yaml, paths.root / "subject.yaml")
    runner = codecheck.DockerRunner(codecheck.load_engines(paths))
    try:
        runner.ensure_ready({"mssql", "mongo"})
    except PipelineError:
        pytest.skip("contenedores apagados (engines up)")
    add(paths, "sql", "I.1", script="SELECT 1 AS x;", expected="1\n")
    add(paths, "mongo", "I.2", script="print(1+1)", expected="2\n")
    add(paths, "sql", "I.3", script="SELEC;")
    report = verify(paths, docs, runner)
    assert {c["id"]: c["status"] for c in report["checks"]} == {"I.1": "aprobado", "I.2": "aprobado", "I.3": "error"}
    assert "SQL Server" in report["engines"]["mssql"]["version"]


def test_archivos_auxiliares_se_copian_y_reemplazan_el_marcador(tmp_path):
    from content_pipeline.codecheck import FIXTURES_TOKEN, RunResult, _run_check

    script = tmp_path / "U2.01.sql"
    script.write_text(f"BULK INSERT dbo.T FROM '{FIXTURES_TOKEN}/datos.csv';", encoding="utf-8")
    (tmp_path / "U2.01.files").mkdir()
    (tmp_path / "U2.01.files" / "datos.csv").write_text("a;b\n", encoding="utf-8")

    class Runner:
        def __init__(self):
            self.script = None

        def stage_files(self, engine, database, directory):
            assert directory.name == "U2.01.files"
            return f"/tmp/checks/{database}"

        def run_sql(self, database, text, timeout):
            self.script = text
            return RunResult(0, "", "")

    runner = Runner()
    entry = _run_check(runner, {"id": "U2.01", "engine": "mssql", "file": script, "script": "checks/sql/U2.01.sql",
                                "expected_file": tmp_path / "U2.01.expected"}, 10)
    assert entry["status"] == "aprobado"
    assert "/tmp/checks/" in runner.script and FIXTURES_TOKEN not in runner.script


def test_marcador_sin_archivos_auxiliares_es_error(tmp_path):
    from content_pipeline.codecheck import FIXTURES_TOKEN, RunResult, _run_check

    script = tmp_path / "U2.02.sql"
    script.write_text(f"SELECT '{FIXTURES_TOKEN}';", encoding="utf-8")

    class Runner:
        def run_sql(self, database, text, timeout):
            return RunResult(0, "", "")

    entry = _run_check(Runner(), {"id": "U2.02", "engine": "mssql", "file": script, "script": "x",
                                  "expected_file": tmp_path / "x.expected"}, 10)
    assert entry["status"] == "error"


def test_plantillas_de_sintaxis_no_son_pendientes(tmp_path):
    from content_pipeline.codecheck import scan_docs

    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "p.md").write_text(
        "<!-- sintaxis -->\n```sql\nSELECT ... FROM <tabla>;\n```\n\n"
        "<!-- sintaxis -->\n```sql\nINSERT INTO dbo.T VALUES (1);\n```\n\n"
        "```sql\nSELECT 1;\n```\n", encoding="utf-8")
    syntax = []
    pending, orphans = scan_docs(docs, set(), syntax)
    assert [p["line"] for p in pending] == [11]
    assert [t["suspicious"] for t in syntax] == [False, True]
    assert not orphans


def test_directiva_ignorar_salida(tmp_path):
    from content_pipeline.codecheck import RunResult, _run_check

    script = tmp_path / "X.1.sql"
    script.write_text("-- verify: ignorar-salida ^Nonqualified transactions\nSELECT 1;", encoding="utf-8")
    (tmp_path / "X.1.expected").write_text("1\n", encoding="utf-8")

    class Runner:
        def run_sql(self, database, text, timeout):
            return RunResult(0, "Nonqualified transactions are being rolled back. 0%.\n1\n", "")

    entry = _run_check(Runner(), {"id": "X.1", "engine": "mssql", "file": script, "script": "x",
                                  "expected_file": tmp_path / "X.1.expected"}, 10)
    assert entry["status"] == "aprobado"
