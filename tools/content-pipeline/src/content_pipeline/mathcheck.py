"""Verificación matemática reproducible de los ejercicios y ejemplos publicados.

Cada materia guarda sus comprobaciones en ``academic-sources/<materia>/checks/*.py``.
Cada archivo registra funciones con el decorador :func:`check`; el identificador
coincide con el marcador ``<!-- ejercicio: ID ... -->`` de la página (o con el de un
ejemplo resuelto). Una comprobación falla si lanza una excepción.

Las cuentas sobre cuerpos finitos usan aritmética modular exacta (funciones
``gf_*``), nunca aritmética real seguida de un redondeo.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

from .io_utils import write_json


@dataclass
class Check:
    check_id: str
    function: Callable[[], Any]
    description: str
    page: str | None
    module: str


_REGISTRY: dict[str, Check] = {}
_CURRENT_MODULE = "<desconocido>"


class CheckFailure(AssertionError):
    pass


def check(check_id: str, description: str = "", page: str | None = None):
    """Registra una comprobación. El identificador debe ser único en la materia."""

    def decorator(function: Callable[[], Any]) -> Callable[[], Any]:
        if check_id in _REGISTRY:
            raise ValueError(f"Comprobación repetida: {check_id} ({_REGISTRY[check_id].module})")
        _REGISTRY[check_id] = Check(check_id, function, description or (function.__doc__ or "").strip(),
                                    page, _CURRENT_MODULE)
        return function

    return decorator


def require(condition: Any, message: str) -> None:
    """Como ``assert``, pero no desaparece con ``python -O``."""
    if not condition:
        raise CheckFailure(message)


def same(actual: Any, expected: Any, what: str = "valor") -> None:
    """Igualdad simbólica exacta para escalares, expresiones o matrices de SymPy."""
    import sympy

    if isinstance(actual, sympy.MatrixBase) or isinstance(expected, sympy.MatrixBase):
        actual_m, expected_m = sympy.Matrix(actual), sympy.Matrix(expected)
        require(actual_m.shape == expected_m.shape, f"{what}: forma {actual_m.shape} ≠ {expected_m.shape}")
        difference = (actual_m - expected_m).applyfunc(sympy.simplify)
        require(difference == sympy.zeros(*actual_m.shape), f"{what}: {actual_m.tolist()} ≠ {expected_m.tolist()}")
        return
    require(sympy.simplify(sympy.sympify(actual) - sympy.sympify(expected)) == 0, f"{what}: {actual} ≠ {expected}")


# ---------------------------------------------------------------------------
# Álgebra lineal sobre Z_p (p primo) con enteros exactos.
# ---------------------------------------------------------------------------
Rows = list[list[int]]


def _rows(matrix: Any) -> Rows:
    if hasattr(matrix, "tolist"):
        matrix = matrix.tolist()
    return [[int(x) for x in row] for row in matrix]


def gf_reduce(matrix: Any, p: int = 2) -> Rows:
    return [[x % p for x in row] for row in _rows(matrix)]


def gf_rref(matrix: Any, p: int = 2) -> tuple[Rows, list[int]]:
    """Forma escalonada reducida por filas en Z_p y columnas pivote."""
    rows = gf_reduce(matrix, p)
    if not rows:
        return rows, []
    pivots: list[int] = []
    r = 0
    for c in range(len(rows[0])):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c] % p), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inverse = pow(rows[r][c], -1, p)
        rows[r] = [(x * inverse) % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                factor = rows[i][c]
                rows[i] = [(a - factor * b) % p for a, b in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    return rows, pivots


def gf_rank(matrix: Any, p: int = 2) -> int:
    return len(gf_rref(matrix, p)[1])


def gf_matmul(a: Any, b: Any, p: int = 2) -> Rows:
    a_rows, b_rows = _rows(a), _rows(b)
    require(len(a_rows[0]) == len(b_rows), "gf_matmul: dimensiones incompatibles")
    return [[sum(x * y for x, y in zip(row, column)) % p for column in zip(*b_rows)] for row in a_rows]


def gf_nullspace(matrix: Any, p: int = 2) -> Rows:
    """Base del espacio nulo {x : A x = 0} en Z_p, como lista de vectores."""
    rref, pivots = gf_rref(matrix, p)
    n = len(_rows(matrix)[0])
    free = [c for c in range(n) if c not in pivots]
    basis: Rows = []
    for f in free:
        vector = [0] * n
        vector[f] = 1
        for row, pc in zip(rref, pivots):
            vector[pc] = (-row[f]) % p
        basis.append(vector)
    return basis


def gf_span(generators: Iterable[Sequence[int]], p: int = 2) -> set[tuple[int, ...]]:
    """Todos los vectores del subespacio generado (solo para dimensiones chicas)."""
    gens = [tuple(int(x) % p for x in g) for g in generators]
    require(gens, "gf_span: sin generadores")
    require(len(gens) <= 12, "gf_span: demasiados generadores para enumerar")
    n = len(gens[0])
    words = set()
    for coefficients in itertools.product(range(p), repeat=len(gens)):
        words.add(tuple(sum(c * g[i] for c, g in zip(coefficients, gens)) % p for i in range(n)))
    return words


def weight(vector: Sequence[int]) -> int:
    return sum(1 for x in vector if x)


def hamming(u: Sequence[int], v: Sequence[int]) -> int:
    require(len(u) == len(v), "hamming: longitudes distintas")
    return sum(1 for a, b in zip(u, v) if a != b)


def min_distance(words: Iterable[Sequence[int]]) -> int:
    """Distancia mínima de un código lineal = peso mínimo de una palabra no nula."""
    weights = [weight(w) for w in words if any(w)]
    require(weights, "min_distance: el código solo tiene la palabra nula")
    return min(weights)


def gf_dot(u: Sequence[int], v: Sequence[int], p: int = 2) -> int:
    return sum(a * b for a, b in zip(u, v)) % p


# ---------------------------------------------------------------------------
# Carga y ejecución.
# ---------------------------------------------------------------------------
def load_checks(directory: Path) -> dict[str, Check]:
    """Importa cada ``*.py`` del directorio (en orden) y devuelve el registro."""
    global _CURRENT_MODULE
    _REGISTRY.clear()
    files = sorted(p for p in directory.glob("*.py") if not p.name.startswith("_"))
    for path in files:
        _CURRENT_MODULE = path.name
        name = f"_checks_{path.stem.replace('-', '_')}"
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"No se pudo cargar {path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    _CURRENT_MODULE = "<desconocido>"
    return dict(_REGISTRY)


def run_checks(directory: Path, ids: list[str] | None = None, report_path: Path | None = None) -> dict[str, Any]:
    import sympy

    registry = load_checks(directory)
    selected = [c for c in registry.values() if not ids or c.check_id in ids]
    results = []
    for item in sorted(selected, key=lambda c: c.check_id):
        try:
            detail = item.function()
            results.append({"id": item.check_id, "status": "passed", "module": item.module, "page": item.page,
                            "description": item.description, "detail": None if detail is None else str(detail)})
        except Exception as error:  # noqa: BLE001 - toda excepción es una comprobación fallida
            frame = traceback.extract_tb(error.__traceback__)[-1]
            results.append({"id": item.check_id, "status": "failed", "module": item.module, "page": item.page,
                            "description": item.description,
                            "detail": f"{type(error).__name__}: {error} (línea {frame.lineno})"})
    sources = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
               for p in sorted(directory.glob("*.py")) if not p.name.startswith("_")}
    report = {
        "sympy_version": sympy.__version__,
        "python_version": sys.version.split()[0],
        "sources": sources,
        "total": len(results),
        "passed": sum(1 for r in results if r["status"] == "passed"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "results": results,
    }
    if report_path is not None:
        write_json(report_path, report)
    return report
