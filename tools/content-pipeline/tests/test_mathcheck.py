import sympy as sp
import pytest

from content_pipeline.mathcheck import (CheckFailure, gf_matmul, gf_nullspace, gf_rank, gf_rref, gf_span,
                                        hamming, min_distance, run_checks, same, weight)

HAMMING_H = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]]


def test_rref_y_rango_en_z2():
    rref, pivots = gf_rref([[1, 1, 0], [1, 1, 1], [0, 0, 1]], 2)
    assert pivots == [0, 2]
    assert rref == [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
    # En R la matriz [[1,1],[1,-1]] tiene rango 2; en Z_2 sus filas coinciden.
    assert gf_rank([[1, 1], [1, -1]], 2) == 1
    assert sp.Matrix([[1, 1], [1, -1]]).rank() == 2


def test_codigo_de_hamming_7_4():
    code = gf_nullspace(HAMMING_H, 2)
    assert len(code) == 4
    assert all(row == [0, 0, 0] for row in gf_matmul(HAMMING_H, sp.Matrix(code).T, 2))
    words = gf_span(code, 2)
    assert len(words) == 16
    assert min_distance(words) == 3
    assert hamming([1, 0, 1], [0, 0, 1]) == 1 and weight([1, 0, 1, 1]) == 3


def test_aritmetica_en_z3():
    assert gf_rank([[1, 2], [2, 1]], 3) == 1  # (2,1) = 2·(1,2) mod 3
    assert gf_rank([[1, 2], [2, 1]], 5) == 2


def test_same_simbolico():
    x = sp.symbols("x")
    same(sp.Matrix([[sp.sin(x) ** 2 + sp.cos(x) ** 2]]), sp.Matrix([[1]]))
    same(sp.Rational(1, 2), 0.5)
    with pytest.raises(CheckFailure):
        same(sp.Matrix([1, 2]), sp.Matrix([1, 3]), "vector")


def test_ejecutor_y_reporte(tmp_path):
    checks = tmp_path / "checks"
    checks.mkdir()
    (checks / "u1.py").write_text(
        "from content_pipeline.mathcheck import check, require\n"
        "@check('u1-01', 'suma')\n"
        "def _():\n    require(1 + 1 == 2, 'aritmética')\n"
        "@check('u1-02')\n"
        "def _():\n    require(False, 'resultado incorrecto')\n", encoding="utf-8")
    report = run_checks(checks, report_path=tmp_path / "report.json")
    assert (report["total"], report["passed"], report["failed"]) == (2, 1, 1)
    failed = next(r for r in report["results"] if r["status"] == "failed")
    assert "resultado incorrecto" in failed["detail"]
    assert (tmp_path / "report.json").exists() and "u1.py" in report["sources"]
    assert run_checks(checks, ids=["u1-01"])["total"] == 1


def test_identificadores_repetidos(tmp_path):
    checks = tmp_path / "checks"
    checks.mkdir()
    body = "from content_pipeline.mathcheck import check\n@check('x')\ndef _():\n    pass\n"
    (checks / "a.py").write_text(body, encoding="utf-8")
    (checks / "b.py").write_text(body, encoding="utf-8")
    with pytest.raises(ValueError, match="repetida"):
        run_checks(checks)
