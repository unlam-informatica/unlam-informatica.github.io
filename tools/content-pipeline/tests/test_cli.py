import json

import pytest
from conftest import FakeEngine

from content_pipeline import cli


@pytest.fixture
def fake_engine(monkeypatch):
    engine = FakeEngine()
    monkeypatch.setattr(cli, "_engine", lambda args: engine)
    return engine


def run(capsys, *argv):
    code = cli.main(list(argv))
    return code, capsys.readouterr()


def test_flujo_completo_por_cli(subject, fake_engine, capsys):
    root = str(subject.root.parent)
    code, out = run(capsys, "inventory", "--subject", "demo", "--sources-root", root)
    assert code == 0 and json.loads(out.out)["unique_documents"] == 3
    code, out = run(capsys, "extract", "--subject", "demo", "--sources-root", root)
    assert code == 0 and json.loads(out.out)["converted"] == 2
    code, out = run(capsys, "normalize", "--subject", "demo", "--sources-root", root)
    assert json.loads(out.out)["normalized"] == 2
    code, out = run(capsys, "status", "--subject", "demo", "--sources-root", root)
    status = json.loads(out.out)
    assert status["documents"] == 3 and status["normalized"] == 2
    code, out = run(capsys, "validate", "--subject", "demo", "--sources-root", root,
                    "--docs-root", str(subject.root), "--strict")
    assert code == 0


def test_run_es_idempotente(subject, fake_engine, capsys):
    root = str(subject.root.parent)
    assert run(capsys, "run", "--subject", "demo", "--sources-root", root)[0] == 0
    calls = len(fake_engine.calls)
    code, out = run(capsys, "run", "--subject", "demo", "--sources-root", root)
    assert code == 0 and len(fake_engine.calls) == calls
    assert json.loads(out.out)["extract"]["cached"] == 2


def test_errores_controlados(tmp_path, capsys):
    code, _ = run(capsys, "status", "--subject", "nada", "--sources-root", str(tmp_path))
    assert code == 2
    with pytest.raises(SystemExit):
        cli.main(["inventory"])  # falta --subject
