"""Comprobaciones de la sección de repaso (repaso/*: vectores y matrices, determinantes,
sistemas lineales, polinomios, rectas y planos)."""
import itertools
import math

import sympy as sp

from content_pipeline.mathcheck import check, gf_matmul, gf_nullspace, gf_rank, gf_rref, require, same

INDEX = "/algebra-ii/repaso/"
VM = "/algebra-ii/repaso/vectores-y-matrices/"
DET = "/algebra-ii/repaso/determinantes/"
SIS = "/algebra-ii/repaso/sistemas-lineales/"
POL = "/algebra-ii/repaso/polinomios/"
RP = "/algebra-ii/repaso/rectas-y-planos/"

x, k, a, b, t, s, y, z, lam = sp.symbols("x k a b t s y z lambda")


# ---------------------------------------------------------------------------
# Auxiliares
# ---------------------------------------------------------------------------
def M(rows):
    return sp.Matrix(rows)


def op(A, kind, i, j=None, c=1):
    """Operación elemental de fila con índices desde 1: 'add' = F_i + c F_j -> F_i,
    'swap' = F_i <-> F_j, 'scale' = c F_i -> F_i."""
    rows = [list(r) for r in A.tolist()]
    i -= 1
    if kind == "swap":
        j -= 1
        rows[i], rows[j] = rows[j], rows[i]
    elif kind == "scale":
        rows[i] = [c * v for v in rows[i]]
    else:
        j -= 1
        rows[i] = [p + c * q for p, q in zip(rows[i], rows[j])]
    return sp.Matrix(rows).applyfunc(sp.expand)


def dot(u, v):
    return sum(p * q for p, q in zip(u, v))


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def trace(A):
    return sum(A[i, i] for i in range(A.shape[0]))


def minor(A, i, j):
    rows = [[A[r, c] for c in range(A.shape[1]) if c != j] for r in range(A.shape[0]) if r != i]
    return sp.Matrix(rows).det()


def col(*entries):
    return sp.Matrix(list(entries))


def ruffini(coeffs, root):
    """Regla de Ruffini: (coeficientes del cociente, resto)."""
    row = [coeffs[0]]
    for c in coeffs[1:]:
        row.append(c + root * row[-1])
    return row[:-1], row[-1]


def poly(coeffs, var=x):
    n = len(coeffs) - 1
    return sum(c * var ** (n - i) for i, c in enumerate(coeffs))


def divisors(n):
    n = abs(n)
    return [d for d in range(1, n + 1) if n % d == 0]


def rational_candidates(coeffs):
    """Candidatas r/s del criterio de Gauss (r | a0, s | an), con ambos signos."""
    out = set()
    for r in divisors(coeffs[-1]):
        for q in divisors(coeffs[0]):
            out.add(sp.Rational(r, q))
            out.add(-sp.Rational(r, q))
    return out


def roots_of(p, var=x, **kw):
    return {sp.sympify(r): m for r, m in sp.roots(sp.Poly(p, var), **kw).items()}


def gf2_solutions(A, bvec):
    n = len(A[0])
    return {v for v in itertools.product((0, 1), repeat=n)
            if all(sum(r[j] * v[j] for j in range(n)) % 2 == bv for r, bv in zip(A, bvec))}


def comb2(basis, offset=None):
    """Todas las combinaciones lineales sobre Z2 de la base, trasladadas por offset."""
    n = len(basis[0]) if basis else len(offset)
    base = tuple(offset) if offset is not None else (0,) * n
    out = set()
    for coeffs in itertools.product((0, 1), repeat=len(basis)):
        out.add(tuple((base[i] + sum(c * v[i] for c, v in zip(coeffs, basis))) % 2 for i in range(n)))
    return out


# ---------------------------------------------------------------------------
# Presentación: autodiagnóstico
# ---------------------------------------------------------------------------
@check("R.T00.E1", "Autodiagnóstico 1: AB y BA no coinciden", page=INDEX)
def _():
    A, B = M([[1, 2], [0, 1]]), M([[0, 1], [1, 0]])
    same(A * B, M([[2, 1], [1, 0]]), "AB")
    same(B * A, M([[0, 1], [1, 2]]), "BA")
    require(A * B != B * A, "AB ≠ BA")
    # a derecha por B intercambia columnas; a izquierda, filas
    same(A * B, sp.Matrix.hstack(A[:, 1], A[:, 0]), "AB = columnas de A intercambiadas")
    same(B * A, sp.Matrix.vstack(A[1, :], A[0, :]), "BA = filas de A intercambiadas")


@check("R.T00.E2", "Autodiagnóstico 2: inversa de una 2x2", page=INDEX)
def _():
    Mm = M([[2, 1], [5, 3]])
    same(Mm.det(), 1, "det M")
    Mi = M([[3, -1], [-5, 2]])
    same(Mm.inv(), Mi, "M^-1")
    same(Mm * Mi, sp.eye(2), "M M^-1")
    same(Mm[0, :] * Mi[:, 0], M([[1]]), "6-5")
    same(Mm[0, :] * Mi[:, 1], M([[0]]), "-2+2")
    same(Mm[1, :] * Mi[:, 0], M([[0]]), "15-15")
    same(Mm[1, :] * Mi[:, 1], M([[1]]), "-5+6")


@check("R.T00.E3", "Autodiagnóstico 3: det A y det(2A)", page=INDEX)
def _():
    A = M([[1, 2, 3], [0, 4, 5], [0, 0, 6]])
    same(A.det(), 24, "det A")
    same(A.det(), 1 * 4 * 6, "producto de la diagonal")
    same((2 * A).det(), 192, "det 2A")
    same((2 * A).det(), 2 ** 3 * A.det(), "2^3 det A")
    require((2 * A).det() != 48, "no es 2 det A")


@check("R.T00.E4", "Autodiagnóstico 4: inversibilidad con parámetro", page=INDEX)
def _():
    A = M([[k, 2], [2, k]])
    same(A.det(), k ** 2 - 4, "det")
    same(sp.factor(A.det()), (k - 2) * (k + 2), "factorización")
    require(set(sp.solve(A.det(), k)) == {2, -2}, "valores críticos")
    for v in (2, -2):
        require(A.subs(k, v).det() == 0, f"k={v} no inversible")
    for v in (0, 1, 3, -1):
        require(A.subs(k, v).det() != 0, f"k={v} inversible")


@check("R.T00.E5", "Autodiagnóstico 5: clasificación de x+y=2, 2x+2y=k", page=INDEX)
def _():
    A = M([[1, 1], [2, 2]])
    aug = M([[1, 1, 2], [2, 2, k]])
    same(op(aug, "add", 2, 1, -2), M([[1, 1, 2], [0, 0, k - 4]]), "F2-2F1")
    require(A.rank() == 1, "rango A = 1")
    require(aug.subs(k, 4).rank() == 1, "k=4: rango ampliada 1 (SCI)")
    for v in (0, 3, 5, -7):
        require(aug.subs(k, v).rank() == 2, f"k={v}: incompatible")
    # soluciones (2-y, y) cuando k = 4
    same(A * col(2 - y, y), col(2, 4), "(2-y, y) resuelve con k=4")
    require(A.rank() < 2, "nunca compatible determinado")


@check("R.T00.E6", "Autodiagnóstico 6: sistema cíclico en Z2 y en R", page=INDEX)
def _():
    A = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
    bvec = [1, 1, 1]
    require(gf_rank(A, 2) == 2, "rango de A en Z2")
    require(gf_rank([r + [bv] for r, bv in zip(A, bvec)], 2) == 3, "rango ampliada en Z2: incompatible")
    require(gf2_solutions(A, bvec) == set(), "sin soluciones en Z2")
    require([sum(r[j] for r in A) % 2 for j in range(3)] == [0, 0, 0], "suma de filas = 0 en Z2")
    require(sum(bvec) % 2 == 1, "0 = 1")
    AR = M(A)
    same(AR.det(), 2, "det en R")
    same(AR.inv() * col(1, 1, 1), col(sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)), "solución en R")
    same(AR * col(sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)), col(1, 1, 1), "verificación")


@check("R.T00.E7", "Autodiagnóstico 7: raíces de λ³-3λ²+2λ", page=INDEX)
def _():
    p = lam ** 3 - 3 * lam ** 2 + 2 * lam
    same(sp.expand(lam * (lam ** 2 - 3 * lam + 2)), p, "factor común")
    same(sp.expand(lam * (lam - 1) * (lam - 2)), p, "factorización")
    require(roots_of(p, lam) == {0: 1, 1: 1, 2: 1}, "raíces simples 0, 1, 2")
    require(sp.Poly(p, lam).eval(0) == 0, "p(0)=0")


@check("R.T00.E8", "Autodiagnóstico 8: plano gen{(1,0,1),(0,1,1)}", page=INDEX)
def _():
    u, v = (1, 0, 1), (0, 1, 1)
    n = cross(u, v)
    require(n == (-1, -1, 1), "normal u×v")
    require(dot(n, u) == 0 and dot(n, v) == 0, "n ⟂ u, v")
    require(dot((1, 1, -1), u) == 0 and dot((1, 1, -1), v) == 0, "x+y-z=0 contiene u y v")
    require(1 + 0 - 1 == 0 and 0 + 1 - 1 == 0, "comprobación")
    # el plano x+y-z=0 es exactamente gen{u,v}: nulo de [1 1 -1] de dimensión 2 que contiene u y v
    N = M([[1, 1, -1]]).nullspace()
    require(len(N) == 2, "dim del plano 2")
    require(sp.Matrix.hstack(*N, col(*u), col(*v)).rank() == 2, "gen{u,v} = plano")


# ---------------------------------------------------------------------------
# R.1 Vectores y matrices
# ---------------------------------------------------------------------------
@check("R.T01.E1", "Operaciones, producto escalar, norma y ángulo en R^3", page=VM)
def _():
    u, v = col(2, -1, 2), col(1, 3, -1)
    same(u + v, col(3, 2, 1), "u+v")
    same(2 * u - v, col(3, -5, 5), "2u-v")
    d = dot(u, v)
    same(d, -3, "u·v")
    same(dot(u, u), 9, "|u|^2 = 9")
    same(dot(v, v), 11, "|v|^2 = 11")
    require(3 * 3 == dot(u, u), "|u| = 3")
    # cos = -3 / (3 sqrt 11) = -1/sqrt 11
    same(sp.Rational(d ** 2, dot(u, u) * dot(v, v)), sp.Rational(1, 11), "cos^2 = 1/11")
    require(d < 0, "ángulo obtuso")
    require(abs(math.degrees(math.acos(d / math.sqrt(dot(u, u) * dot(v, v)))) - 107.5) < 0.1, "≈ 107,5°")
    same(dot(u + v, u + v), 14, "|u+v|^2")
    same(dot(u, u) + 2 * d + dot(v, v), 14, "desarrollo del cuadrado")
    same(sp.Matrix(u.tolist()) / 3, col(sp.Rational(2, 3), -sp.Rational(1, 3), sp.Rational(2, 3)), "unitario")
    same(dot(sp.Matrix(u.tolist()) / 3, sp.Matrix(u.tolist()) / 3), 1, "norma 1")


@check("R.T01.E2", "Producto de matrices, combinación de columnas y no conmutatividad", page=VM)
def _():
    A = M([[1, 2, 0], [-1, 1, 3]])
    B = M([[2, 1], [0, -1], [1, 2]])
    AB = A * B
    same(AB, M([[2, -1], [1, 4]]), "AB")
    same(AB[0, 0], 1 * 2 + 2 * 0 + 0 * 1, "elemento (1,1)")
    same(AB[0, 1], 1 * 1 + 2 * (-1) + 0 * 2, "elemento (1,2)")
    same(AB[1, 0], (-1) * 2 + 1 * 0 + 3 * 1, "elemento (2,1)")
    same(AB[1, 1], (-1) * 1 + 1 * (-1) + 3 * 2, "elemento (2,2)")
    comb = 2 * A[:, 0] + 0 * A[:, 1] + 1 * A[:, 2]
    same(comb, col(2, 1), "primera columna como combinación")
    same(comb, AB[:, 0], "coincide con AB")
    BA = B * A
    same(BA, M([[1, 5, 3], [1, -1, -3], [-1, 4, 6]]), "BA")
    require(AB.shape == (2, 2) and BA.shape == (3, 3), "tamaños distintos")
    P, Q = M([[1, 1], [0, 1]]), M([[1, 0], [1, 1]])
    same(P * Q, M([[2, 1], [1, 1]]), "PQ")
    same(Q * P, M([[1, 1], [1, 2]]), "QP")
    require(P * Q != Q * P, "PQ ≠ QP")
    same(AB.T, M([[2, 1], [-1, 4]]), "(AB)^t")
    same(B.T * A.T, AB.T, "B^t A^t = (AB)^t")


@check("R.T01.E3", "Inversa por Gauss-Jordan de una 3x3", page=VM)
def _():
    A = M([[1, 2, 1], [0, 1, 1], [1, 2, 2]])
    aug = sp.Matrix.hstack(A, sp.eye(3))
    s1 = op(aug, "add", 3, 1, -1)
    same(s1, M([[1, 2, 1, 1, 0, 0], [0, 1, 1, 0, 1, 0], [0, 0, 1, -1, 0, 1]]), "F3-F1")
    s2 = op(op(s1, "add", 2, 3, -1), "add", 1, 3, -1)
    same(s2, M([[1, 2, 0, 2, 0, -1], [0, 1, 0, 1, 1, -1], [0, 0, 1, -1, 0, 1]]), "F2-F3, F1-F3")
    s3 = op(s2, "add", 1, 2, -2)
    same(s3, M([[1, 0, 0, 0, -2, 1], [0, 1, 0, 1, 1, -1], [0, 0, 1, -1, 0, 1]]), "F1-2F2")
    Ai = M([[0, -2, 1], [1, 1, -1], [-1, 0, 1]])
    same(s3[:, 3:], Ai, "bloque derecho")
    same(A.inv(), Ai, "A^-1")
    same(A * Ai, sp.eye(3), "A A^-1")
    same(Ai * A, sp.eye(3), "A^-1 A")
    same(trace(A), 4, "tr A")


@check("R.01", "Operaciones y ángulo en R^3", page=VM)
def _():
    u, v = col(1, -2, 2), col(3, 0, -4)
    same(3 * u - 2 * v, col(-3, -6, 14), "3u-2v")
    same(3 * u, col(3, -6, 6), "3u")
    same(2 * v, col(6, 0, -8), "2v")
    d = dot(u, v)
    same(d, -5, "u·v")
    same(dot(u, u), 9, "|u|^2")
    same(dot(v, v), 25, "|v|^2")
    require(3 * 3 == dot(u, u) and 5 * 5 == dot(v, v), "normas 3 y 5")
    same(sp.Rational(d, 3 * 5), -sp.Rational(1, 3), "cos")
    require(d < 0, "obtuso")
    require(abs(d) <= 3 * 5, "Cauchy-Schwarz")


@check("R.02", "Producto, transpuesta y traza", page=VM)
def _():
    A, B = M([[2, -1], [1, 3]]), M([[0, 1], [2, -2]])
    AB, BA = A * B, B * A
    same(AB, M([[-2, 4], [6, -5]]), "AB")
    same(BA, M([[1, 3], [2, -8]]), "BA")
    require(AB != BA, "AB ≠ BA")
    same(AB.T, M([[-2, 6], [4, -5]]), "(AB)^t")
    same(B.T * A.T, M([[-2, 6], [4, -5]]), "B^t A^t")
    same(B.T * A.T, AB.T, "(AB)^t = B^t A^t")
    same(A.T * B.T, M([[1, 2], [3, -8]]), "A^t B^t")
    same(A.T * B.T, BA.T, "A^t B^t = (BA)^t")
    require(A.T * B.T != AB.T, "(AB)^t ≠ A^t B^t")
    same(trace(AB), -7, "tr AB")
    same(trace(BA), -7, "tr BA")


@check("R.03", "Inversa de una 3x3 por Gauss-Jordan", page=VM)
def _():
    Mm = M([[2, 1, 0], [1, 1, 0], [0, 1, 1]])
    aug = sp.Matrix.hstack(Mm, sp.eye(3))
    s1 = op(aug, "swap", 1, 2)
    same(s1, M([[1, 1, 0, 0, 1, 0], [2, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1]]), "F1<->F2")
    s2 = op(s1, "add", 2, 1, -2)
    same(s2, M([[1, 1, 0, 0, 1, 0], [0, -1, 0, 1, -2, 0], [0, 1, 1, 0, 0, 1]]), "F2-2F1")
    s3 = op(s2, "scale", 2, c=-1)
    same(s3, M([[1, 1, 0, 0, 1, 0], [0, 1, 0, -1, 2, 0], [0, 1, 1, 0, 0, 1]]), "-F2")
    s4 = op(op(s3, "add", 1, 2, -1), "add", 3, 2, -1)
    same(s4, M([[1, 0, 0, 1, -1, 0], [0, 1, 0, -1, 2, 0], [0, 0, 1, 1, -2, 1]]), "F1-F2, F3-F2")
    Mi = M([[1, -1, 0], [-1, 2, 0], [1, -2, 1]])
    same(s4[:, 3:], Mi, "bloque derecho")
    same(Mm.inv(), Mi, "M^-1")
    same(Mm * Mi, sp.eye(3), "M M^-1")
    require(Mm.det() != 0, "inversible")


@check("R.04", "Producto de simétricas: contraejemplo y equivalencia", page=VM)
def _():
    A, B = M([[1, 0], [0, 2]]), M([[0, 1], [1, 0]])
    require(A == A.T and B == B.T, "simétricas")
    AB = A * B
    same(AB, M([[0, 1], [2, 0]]), "AB")
    same(AB.T, M([[0, 2], [1, 0]]), "(AB)^t")
    require(AB != AB.T, "AB no es simétrica")
    same(B * A, M([[0, 2], [1, 0]]), "BA")
    same(B * A, AB.T, "BA = (AB)^t")
    # simétricas genéricas de 2x2: (AB)^t = BA siempre
    p, q, r, u, v, w = sp.symbols("p q r u v w")
    As, Bs = M([[p, q], [q, r]]), M([[u, v], [v, w]])
    same((As * Bs).T, Bs * As, "(AB)^t = B^t A^t = BA")
    # caso con AB = BA: AB resulta simétrica
    C, D = M([[1, 2], [2, 1]]), M([[3, 4], [4, 3]])
    require(C * D == D * C, "C y D conmutan")
    require(C * D == (C * D).T, "CD simétrica")


# ---------------------------------------------------------------------------
# R.2 Determinantes
# ---------------------------------------------------------------------------
@check("R.T02.E1", "Determinante 3x3 por cofactores y por Sarrus", page=DET)
def _():
    A = M([[2, -1, 3], [0, 4, 1], [1, 2, -2]])
    c1 = 2 * M([[4, 1], [2, -2]]).det()
    c3 = 1 * M([[-1, 3], [4, 1]]).det()
    same(M([[4, 1], [2, -2]]).det(), -10, "menor (1,1)")
    same(M([[-1, 3], [4, 1]]).det(), -13, "menor (3,1)")
    same(c1 + c3, -33, "cofactores por columna 1")
    p1 = 2 * 4 * (-2) + (-1) * 1 * 1 + 3 * 0 * 2
    p2 = 3 * 4 * 1 + 2 * 1 * 2 + (-1) * 0 * (-2)
    same(p1, -17, "diagonales principales")
    same(p2, 16, "diagonales secundarias")
    same(p1 - p2, -33, "Sarrus")
    same(A.det(), -33, "det A")
    require(A.det() != 0, "inversible")


@check("R.T02.E2", "Determinante 4x4 por triangulación", page=DET)
def _():
    B = M([[0, 1, 2, 1], [1, 2, 1, 0], [2, 3, 0, 1], [1, 1, 1, 2]])
    same(B.det(), 4, "det B")
    B1 = op(B, "swap", 1, 2)
    same(B1, M([[1, 2, 1, 0], [0, 1, 2, 1], [2, 3, 0, 1], [1, 1, 1, 2]]), "F1<->F2")
    same(B1.det(), -4, "signo del intercambio")
    B2 = op(op(B1, "add", 3, 1, -2), "add", 4, 1, -1)
    same(B2, M([[1, 2, 1, 0], [0, 1, 2, 1], [0, -1, -2, 1], [0, -1, 0, 2]]), "F3-2F1, F4-F1")
    same(B2.det(), -4, "no cambia")
    B3 = op(op(B2, "add", 3, 2, 1), "add", 4, 2, 1)
    same(B3, M([[1, 2, 1, 0], [0, 1, 2, 1], [0, 0, 0, 2], [0, 0, 2, 3]]), "F3+F2, F4+F2")
    same(B3.det(), -4, "no cambia")
    B4 = op(B3, "swap", 3, 4)
    same(B4, M([[1, 2, 1, 0], [0, 1, 2, 1], [0, 0, 2, 3], [0, 0, 0, 2]]), "F3<->F4")
    same(B4.det(), 4, "signo vuelve a cambiar")
    same(B4[0, 0] * B4[1, 1] * B4[2, 2] * B4[3, 3], 4, "producto de la diagonal")
    same(minor(B, 0, 1), -4, "M12")
    same(minor(B, 0, 2), -1, "M13")
    same(minor(B, 0, 3), -2, "M14")
    same(-1 * minor(B, 0, 1) + 2 * minor(B, 0, 2) - 1 * minor(B, 0, 3), 4, "desarrollo por la fila 1")


@check("R.T02.E3", "Determinante de A_k = (k-1)^2 (k+2)", page=DET)
def _():
    Ak = M([[k, 1, 1], [1, k, 1], [1, 1, k]])
    d = Ak.det()
    same(d, k ** 3 - 3 * k + 2, "desarrollo directo")
    same(k * (k ** 2 - 1) - 1 * (k - 1) + 1 * (1 - k), k ** 3 - 3 * k + 2, "por la primera fila")
    q, r = ruffini([1, 0, -3, 2], 1)
    require(r == 0 and q == [1, 1, -2], "Ruffini con 1")
    same(sp.expand((k - 1) * (k ** 2 + k - 2)), k ** 3 - 3 * k + 2, "cociente por (k-1)")
    same(sp.factor(d), (k - 1) ** 2 * (k + 2), "factorización")
    require(roots_of(d, k) == {1: 2, -2: 1}, "raíces 1 doble y -2")
    # método 2: C1+C2+C3 -> C1 y factor común k+2
    C = sp.Matrix.hstack(Ak[:, 0] + Ak[:, 1] + Ak[:, 2], Ak[:, 1], Ak[:, 2])
    same(C.det(), d, "C1+C2+C3 no cambia el determinante")
    same(C[:, 0], col(k + 2, k + 2, k + 2), "columna con k+2")
    F = M([[1, 1, 1], [1, k, 1], [1, 1, k]])
    same((k + 2) * F.det(), d, "factor común k+2")
    T = M([[1, 1, 1], [0, k - 1, 0], [0, 0, k - 1]])
    same(op(op(F, "add", 2, 1, -1), "add", 3, 1, -1), T, "restar la primera fila")
    same((k + 2) * T.det(), (k + 2) * (k - 1) ** 2, "método 2")
    same(d.subs(k, 0), 2, "det A_0")
    same(((0 + 2) * (0 - 1) ** 2), 2, "fórmula con k=0")
    same(Ak.subs(k, -2) * col(1, 1, 1), col(0, 0, 0), "filas suman 0 con k=-2")
    same(d.subs(k, -2), 0, "det A_-2")
    same(d.subs(k, 1), 0, "det A_1")


@check("R.05", "Cofactores y propiedades del determinante", page=DET)
def _():
    C = M([[3, 0, -1], [2, 1, 4], [-1, 0, 2]])
    same(1 * M([[3, -1], [-1, 2]]).det(), 5, "desarrollo por la columna 2")
    same(C.det(), 5, "det C")
    same(C.T.det(), 5, "det C^t")
    same((2 * C).det(), 40, "det 2C")
    same(2 ** 3 * C.det(), 40, "2^3 det C")
    same(C.inv().det(), sp.Rational(1, 5), "det C^-1")
    same((C * C * C).det(), 125, "det C^3")
    sarrus = 3 * 1 * 2 + 0 * 4 * (-1) + (-1) * 2 * 0 - ((-1) * 1 * (-1) + 3 * 4 * 0 + 0 * 2 * 2)
    same(sarrus, 5, "Sarrus")


@check("R.06", "Determinante 4x4 por triangulación", page=DET)
def _():
    D = M([[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3], [1, 2, 3, 4]])
    s1 = op(op(op(D, "add", 2, 1, -1), "add", 3, 1, -1), "add", 4, 1, -1)
    same(s1, M([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3]]), "primer paso")
    s2 = op(op(s1, "add", 3, 2, -1), "add", 4, 2, -1)
    same(s2, M([[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 1, 2]]), "segundo paso")
    s3 = op(s2, "add", 4, 3, -1)
    same(s3, M([[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1]]), "tercer paso")
    for m_ in (s1, s2, s3):
        same(m_.det(), 1, "el determinante no cambia")
    same(D.det(), 1, "det D")
    require(D.det() != 0, "inversible")


@check("R.07", "Matriz tridiagonal con parámetro", page=DET)
def _():
    Ak = M([[k, 1, 0], [1, k, 1], [0, 1, k]])
    d = Ak.det()
    same(k * M([[k, 1], [1, k]]).det() - 1 * M([[1, 1], [0, k]]).det(), k ** 3 - 2 * k, "fila 1")
    same(d, k ** 3 - 2 * k, "det A_k")
    same(sp.factor(d), k * (k ** 2 - 2), "factorización")
    require(set(sp.solve(d, k)) == {0, sp.sqrt(2), -sp.sqrt(2)}, "raíces 0, ±√2")
    same(Ak.subs(k, 0).det(), 0, "k = 0")
    require(Ak.subs(k, 0)[0, :] == Ak.subs(k, 0)[2, :], "filas 1 y 3 iguales en k=0")
    same(sp.simplify(d.subs(k, sp.sqrt(2))), 0, "k = √2")
    same(sp.simplify(d.subs(k, -sp.sqrt(2))), 0, "k = -√2")
    for v in (1, 2, -1, 3):
        require(d.subs(k, v) != 0, f"k={v} inversible")


@check("R.08", "Verdadero o falso sobre determinantes", page=DET)
def _():
    # 1. det(A+B) ≠ det A + det B
    I2 = sp.eye(2)
    same((I2 + I2).det(), 4, "det(2 I2)")
    same(I2.det() + I2.det(), 2, "det A + det B")
    require((I2 + I2).det() != I2.det() + I2.det(), "1 es falsa")
    # 2. det(-A) = (-1)^3 det A para 3x3
    A = sp.diag(2, 1, 1)
    same(A.det(), 2, "det A")
    same((-A).det(), -2, "det(-A)")
    G = M([[1, 2, 0], [3, -1, 4], [2, 5, 1]])
    same((-G).det(), -G.det(), "det(-A) = -det A (n impar)")
    H = M([[1, 2], [3, 5]])
    same((-H).det(), H.det(), "n par: det(-A) = det A")
    # 3. det(AB) = 0 implica A o B no inversible
    a1, a2, a3, a4, b1, b2, b3, b4 = sp.symbols("a1 a2 a3 a4 b1 b2 b3 b4")
    As, Bs = M([[a1, a2], [a3, a4]]), M([[b1, b2], [b3, b4]])
    same((As * Bs).det(), As.det() * Bs.det(), "det(AB) = det A det B")
    S, T = M([[1, 2], [2, 4]]), M([[1, 1], [0, 1]])
    same((S * T).det(), 0, "det(ST) = 0")
    require(S.det() == 0 or T.det() == 0, "alguna no es inversible")


# ---------------------------------------------------------------------------
# R.3 Sistemas lineales
# ---------------------------------------------------------------------------
@check("R.T03.E1", "Eliminación gaussiana con variables libres", page=SIS)
def _():
    A = M([[1, 2, -1, 1], [2, 4, -1, 3], [-1, -2, 2, 0]])
    bvec = col(3, 7, -2)
    aug = sp.Matrix.hstack(A, bvec)
    s1 = op(op(aug, "add", 2, 1, -2), "add", 3, 1, 1)
    same(s1, M([[1, 2, -1, 1, 3], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]), "F2-2F1, F3+F1")
    s2 = op(s1, "add", 3, 2, -1)
    same(s2, M([[1, 2, -1, 1, 3], [0, 0, 1, 1, 1], [0, 0, 0, 0, 0]]), "F3-F2")
    s3 = op(s2, "add", 1, 2, 1)
    same(s3, M([[1, 2, 0, 2, 4], [0, 0, 1, 1, 1], [0, 0, 0, 0, 0]]), "F1+F2")
    red, piv = aug.rref()
    same(red, s3, "forma reducida")
    require(tuple(piv) == (0, 2), "pivotes en las columnas 1 y 3")
    require(A.rank() == 2 and aug.rank() == 2, "rangos 2 y 2")
    xp = col(4, 0, 1, 0)
    h1, h2 = col(-2, 1, 0, 0), col(-2, 0, -1, 1)
    same(A * xp, bvec, "solución particular")
    same(A * h1, col(0, 0, 0), "homogénea 1")
    same(A * h2, col(0, 0, 0), "homogénea 2")
    require(sp.Matrix.hstack(h1, h2).rank() == 2, "h1 y h2 independientes")
    require(sp.Matrix.hstack(*A.nullspace(), h1, h2).rank() == 2, "generan el núcleo")
    x2, x4 = sp.symbols("x2 x4")
    gen = xp + x2 * h1 + x4 * h2
    same(gen, col(4 - 2 * x2 - 2 * x4, x2, 1 - x4, x4), "forma de la solución general")
    same(A * gen, bvec, "A x = b para todo x2, x4")


@check("R.T03.E2", "Clasificación según dos parámetros", page=SIS)
def _():
    A = M([[1, 1, 1], [1, 2, 3], [1, 3, a]])
    rhs = col(1, 2, b)
    aug = sp.Matrix.hstack(A, rhs)
    s1 = op(op(aug, "add", 2, 1, -1), "add", 3, 1, -1)
    same(s1, M([[1, 1, 1, 1], [0, 1, 2, 1], [0, 2, a - 1, b - 1]]), "F2-F1, F3-F1")
    s2 = op(s1, "add", 3, 2, -2)
    same(s2, M([[1, 1, 1, 1], [0, 1, 2, 1], [0, 0, a - 5, b - 3]]), "F3-2F2")
    same(A.det(), a - 5, "det A")
    # a != 5: SCD
    zz = (b - 3) / (a - 5)
    sol = col(zz, 1 - 2 * zz, zz)
    same(A * sol, rhs, "solución con a≠5")
    same(1 - (1 - 2 * zz) - zz, zz, "x = z")
    same(3 + (a - 5) * zz, b, "tercera ecuación")
    for av, bv in ((0, 0), (1, 7), (6, 3), (-2, 5)):
        Aa = A.subs({a: av})
        require(Aa.rank() == 3 and Aa.det() != 0, f"a={av}: SCD")
    # a = 5, b = 3: SCI
    A5 = A.subs(a, 5)
    aug53 = aug.subs({a: 5, b: 3})
    require(A5.rank() == 2 and aug53.rank() == 2, "a=5, b=3: rangos 2 y 2")
    same(op(op(aug53, "add", 2, 1, -1), "add", 3, 1, -1).rank(), 2, "rango tras escalonar")
    same(A5 * (col(0, 1, 0) + t * col(1, -2, 1)), col(1, 2, 3), "a=5, b=3: resuelve para todo t")
    # a = 5, b != 3: SI
    for bv in (0, 4, -1):
        require(A5.rank() == 2 and aug.subs({a: 5, b: bv}).rank() == 3, f"a=5, b={bv}: incompatible")


@check("R.T03.E3", "Matriz ampliada múltiple", page=SIS)
def _():
    A = M([[1, 1], [1, 2]])
    B = M([[3, 2], [5, -1]])
    aug = sp.Matrix.hstack(A, B)
    s1 = op(aug, "add", 2, 1, -1)
    same(s1, M([[1, 1, 3, 2], [0, 1, 2, -3]]), "F2-F1")
    s2 = op(s1, "add", 1, 2, -1)
    same(s2, M([[1, 0, 1, 5], [0, 1, 2, -3]]), "F1-F2")
    same(A.inv() * B, s2[:, 2:], "soluciones")
    same(A * col(1, 2), col(3, 5), "primer sistema")
    same(A * col(5, -3), col(2, -1), "segundo sistema")
    same(1 * col(1, 1) + 2 * col(1, 2), col(3, 5), "(3,5) = 1(1,1) + 2(1,2)")
    same(5 * col(1, 1) - 3 * col(1, 2), col(2, -1), "(2,-1) = 5(1,1) - 3(1,2)")


@check("R.T03.E4", "Sistema en Z2 con variables libres", page=SIS)
def _():
    A = [[1, 1, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    bvec = [1, 0, 1]
    aug = [r + [bv] for r, bv in zip(A, bvec)]
    r3 = [(p + q) % 2 for p, q in zip(aug[2], aug[0])]
    require(r3 == [0, 1, 1, 1, 0], "F3+F1")
    require([(p + q) % 2 for p, q in zip(r3, aug[1])] == [0, 0, 0, 0, 0], "F3+F2 anula")
    r1 = [(p + q) % 2 for p, q in zip(aug[0], aug[1])]
    require(r1 == [1, 0, 1, 0, 1], "F1+F2")
    rref, piv = gf_rref(aug, 2)
    require(rref == [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]] and piv == [0, 1], "forma reducida")
    require(gf_rank(A, 2) == 2 and gf_rank(aug, 2) == 2, "rangos 2 y 2")
    sols = gf2_solutions(A, bvec)
    require(sols == {(1, 0, 0, 0), (0, 1, 1, 0), (1, 1, 0, 1), (0, 0, 1, 1)}, "las 4 soluciones")
    require(len(sols) == 2 ** 2, "2^2 soluciones")
    require(sols == comb2([(1, 1, 1, 0), (0, 1, 0, 1)], (1, 0, 0, 0)), "forma general")
    for v in sols:
        require(v[0] == (1 + v[2]) % 2 and v[1] == (v[2] + v[3]) % 2, "x1 = 1 + x3, x2 = x3 + x4")
    require(all(row[0] % 2 == 0 for row in gf_matmul(A, [[c] for c in (1, 1, 1, 0)], 2)), "(1,1,1,0) homogénea")
    require(all(row[0] % 2 == 0 for row in gf_matmul(A, [[c] for c in (0, 1, 0, 1)], 2)), "(0,1,0,1) homogénea")


@check("R.09", "Sistema compatible determinado 3x3", page=SIS)
def _():
    A = M([[1, 1, 1], [2, -1, 1], [1, 2, -1]])
    bvec = col(6, 3, 2)
    aug = sp.Matrix.hstack(A, bvec)
    s1 = op(op(aug, "add", 2, 1, -2), "add", 3, 1, -1)
    same(s1, M([[1, 1, 1, 6], [0, -3, -1, -9], [0, 1, -2, -4]]), "F2-2F1, F3-F1")
    s2 = op(op(s1, "swap", 2, 3), "add", 3, 2, 3)
    same(s2, M([[1, 1, 1, 6], [0, 1, -2, -4], [0, 0, -7, -21]]), "F2<->F3, F3+3F2")
    require(A.rank() == 3 and aug.rank() == 3, "rangos 3 y 3")
    zz = sp.Rational(-21, -7)
    yy = -4 + 2 * zz
    xx = 6 - yy - zz
    require((xx, yy, zz) == (1, 2, 3), "sustitución hacia atrás")
    same(A.inv() * bvec, col(1, 2, 3), "solución")
    same(A * col(1, 2, 3), bvec, "verificación")


@check("R.10", "Solución general de un homogéneo", page=SIS)
def _():
    A = M([[1, -1, 2, 0], [2, -2, 3, 1], [1, -1, 1, 1]])
    s1 = op(op(A, "add", 2, 1, -2), "add", 3, 1, -1)
    same(s1, M([[1, -1, 2, 0], [0, 0, -1, 1], [0, 0, -1, 1]]), "F2-2F1, F3-F1")
    s2 = op(s1, "add", 3, 2, -1)
    same(s2, M([[1, -1, 2, 0], [0, 0, -1, 1], [0, 0, 0, 0]]), "F3-F2")
    s3 = op(op(s2, "scale", 2, c=-1), "add", 1, 2, -2)
    same(s3, M([[1, -1, 0, 2], [0, 0, 1, -1], [0, 0, 0, 0]]), "-F2, F1-2F2")
    same(A.rref()[0], s3, "forma reducida")
    require(A.rank() == 2, "rango 2")
    v1, v2 = col(1, 1, 0, 0), col(-2, 0, 1, 1)
    same(A * v1, col(0, 0, 0), "A v1")
    same(A * v2, col(0, 0, 0), "A v2")
    x2, x4 = sp.symbols("x2 x4")
    same(col(x2 - 2 * x4, x2, x4, x4), x2 * v1 + x4 * v2, "x1 = x2 - 2x4, x3 = x4")
    same(A * (x2 * v1 + x4 * v2), col(0, 0, 0), "solución general")
    require(sp.Matrix.hstack(*A.nullspace(), v1, v2).rank() == 2, "generan el núcleo")
    require(len(A.nullspace()) == 4 - 2, "dos variables libres")


@check("R.11", "Clasificación de x+y+kz=1, x+ky+z=1, kx+y+z=1", page=SIS)
def _():
    A = M([[1, 1, k], [1, k, 1], [k, 1, 1]])
    Ak = M([[k, 1, 1], [1, k, 1], [1, 1, k]])
    same(op(Ak, "swap", 1, 3), A, "A = A_k con filas 1 y 3 intercambiadas")
    same(A.det(), -(k - 1) ** 2 * (k + 2), "det A")
    same(sp.factor(A.det()), -(k - 1) ** 2 * (k + 2), "factorización")
    ones = col(1, 1, 1)
    # k != 1, -2: x = y = z = 1/(k+2)
    tt = 1 / (k + 2)
    same(A * (tt * ones), ones, "x=y=z=1/(k+2)")
    for v in (0, 2, -1, 3):
        Av = A.subs(k, v)
        require(Av.det() != 0, f"k={v}: SCD")
        same(Av.inv() * ones, sp.Rational(1, v + 2) * ones, f"k={v}: solución única")
    same(A.subs(k, 0) * (sp.Rational(1, 2) * ones), ones, "k=0")
    # k = 1: SCI
    A1 = A.subs(k, 1)
    require(A1.rank() == 1 and sp.Matrix.hstack(A1, ones).rank() == 1, "k=1: rangos 1 y 1")
    same(A1 * (col(1, 0, 0) + y * col(-1, 1, 0) + z * col(-1, 0, 1)), ones, "k=1: solución general")
    require(sp.Matrix.hstack(*A1.nullspace(), col(-1, 1, 0), col(-1, 0, 1)).rank() == 2, "dirección")
    # k = -2: SI
    Am = A.subs(k, -2)
    aug = sp.Matrix.hstack(Am, ones)
    same(aug, M([[1, 1, -2, 1], [1, -2, 1, 1], [-2, 1, 1, 1]]), "matriz ampliada")
    s1 = op(op(aug, "add", 2, 1, -1), "add", 3, 1, 2)
    same(s1, M([[1, 1, -2, 1], [0, -3, 3, 0], [0, 3, -3, 3]]), "F2-F1, F3+2F1")
    s2 = op(s1, "add", 3, 2, 1)
    same(s2, M([[1, 1, -2, 1], [0, -3, 3, 0], [0, 0, 0, 3]]), "F3+F2")
    require(Am.rank() == 2 and aug.rank() == 3, "rangos 2 y 3")
    same(aug[0, :] + aug[1, :] + aug[2, :], M([[0, 0, 0, 3]]), "suma de las ecuaciones: 0 = 3")


@check("R.12", "Sistema en Z2: todas las soluciones", page=SIS)
def _():
    A = [[1, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1]]
    bvec = [1, 1, 0]
    aug = [r + [bv] for r, bv in zip(A, bvec)]
    r3 = [(p + q) % 2 for p, q in zip(aug[2], aug[0])]
    require(r3 == [0, 1, 1, 0, 1] == aug[1], "F3+F1 = F2")
    require([(p + q) % 2 for p, q in zip(r3, aug[1])] == [0] * 5, "F3+F2 anula")
    rref, piv = gf_rref(aug, 2)
    require(rref == [[1, 0, 1, 1, 1], [0, 1, 1, 0, 1], [0, 0, 0, 0, 0]] and piv == [0, 1], "forma reducida")
    sols = gf2_solutions(A, bvec)
    expected = {(1, 1, 0, 0), (0, 0, 1, 0), (0, 1, 0, 1), (1, 0, 1, 1)}
    require(sols == expected, "las cuatro soluciones")
    require(sols == comb2([(1, 1, 1, 0), (1, 0, 0, 1)], (1, 1, 0, 0)), "forma general")
    for x3, x4 in itertools.product((0, 1), repeat=2):
        require((1 + x3 + x4) % 2 == next(v[0] for v in sols if v[2] == x3 and v[3] == x4), "x1 = 1 + x3 + x4")
        require((1 + x3) % 2 == next(v[1] for v in sols if v[2] == x3 and v[3] == x4), "x2 = 1 + x3")
    hom = gf2_solutions(A, [0, 0, 0])
    require(len(hom) == 4, "homogéneo con 4 soluciones")
    require(hom == comb2([(1, 1, 1, 0), (1, 0, 0, 1)]), "combinaciones de (1,1,1,0) y (1,0,0,1)")
    require(hom == comb2([tuple(v) for v in gf_nullspace(A, 2)]), "base del núcleo en Z2")
    require(gf_rank(A, 2) == 2, "rango 2")


# ---------------------------------------------------------------------------
# R.4 Polinomios
# ---------------------------------------------------------------------------
@check("R.T04.E1", "Ruffini, teorema del resto y factorización", page=POL)
def _():
    cf = [1, -2, -5, 6]
    p = poly(cf)
    same(p.subs(x, 2), -4, "p(2)")
    q, r = ruffini(cf, 2)
    require(q == [1, 0, -5] and r == -4, "Ruffini con 2")
    same(sp.expand((x - 2) * (x ** 2 - 5) - 4), p, "p = (x-2)(x²-5) - 4")
    same(p.subs(x, 1), 0, "p(1)")
    for c in (-1, 2, -3, 6, -6):
        require(p.subs(x, c) != 0, f"{c} no es raíz")
    require({1, 3, -2} <= rational_candidates(cf), "las raíces están entre las candidatas")
    q1, r1 = ruffini(cf, 1)
    require(q1 == [1, -1, -6] and r1 == 0, "Ruffini con 1")
    require(roots_of(x ** 2 - x - 6) == {3: 1, -2: 1}, "raíces de x²-x-6")
    same(sp.expand((x - 3) * (x + 2)), x ** 2 - x - 6, "(x-3)(x+2)")
    same(sp.expand((x - 1) * (x ** 2 - x - 6)), p, "(x-1)(x²-x-6)")
    same(sp.factor(p), (x - 1) * (x - 3) * (x + 2), "factorización")
    require(roots_of(p) == {1: 1, 3: 1, -2: 1}, "raíces simples")


@check("R.T04.E2", "Raíz doble y raíces fraccionarias", page=POL)
def _():
    # (a)
    ca = [1, -5, 8, -4]
    pa = poly(ca, lam)
    require(set(map(int, divisors(4))) == {1, 2, 4}, "divisores de 4")
    same(pa.subs(lam, 1), 0, "p(1)")
    q1, r1 = ruffini(ca, 1)
    require(q1 == [1, -4, 4] and r1 == 0, "Ruffini con 1")
    q2, r2 = ruffini(q1, 2)
    require(q2 == [1, -2] and r2 == 0, "Ruffini con 2")
    same(sp.expand((lam - 2) ** 2), lam ** 2 - 4 * lam + 4, "(λ-2)²")
    same(sp.factor(pa), (lam - 1) * (lam - 2) ** 2, "factorización")
    require(roots_of(pa, lam) == {1: 1, 2: 2}, "1 simple y 2 doble")
    same(1 + 2 + 2, 5, "suma de raíces")
    same(1 * 2 * 2, 4, "producto de raíces")
    # (b)
    cb = [2, -3, -3, 2]
    qb = poly(cb)
    cands = rational_candidates(cb)
    require(cands == {1, -1, 2, -2, sp.Rational(1, 2), -sp.Rational(1, 2)}, "candidatas")
    same(qb.subs(x, -1), 0, "q(-1)")
    c1, r1b = ruffini(cb, -1)
    require(c1 == [2, -5, 2] and r1b == 0, "Ruffini con -1")
    require(roots_of(2 * x ** 2 - 5 * x + 2) == {2: 1, sp.Rational(1, 2): 1}, "raíces del cociente")
    same(sp.expand((x + 1) * (2 * x - 1) * (x - 2)), qb, "factorización")
    same(sp.expand(2 * (x + 1) * (x - sp.Rational(1, 2)) * (x - 2)), qb, "forma con 2 delante")
    same(qb.subs(x, sp.Rational(1, 2)), 0, "q(1/2)")
    require(roots_of(qb) == {-1: 1, 2: 1, sp.Rational(1, 2): 1}, "raíces")


@check("R.T04.E3", "Factor irreducible y polinomio característico sin expandir", page=POL)
def _():
    # (a)
    ca = [1, -3, 4, -2]
    pa = poly(ca)
    same(pa.subs(x, 1), 0, "p(1)")
    q, r = ruffini(ca, 1)
    require(q == [1, -2, 2] and r == 0, "Ruffini con 1")
    same((-2) ** 2 - 4 * 1 * 2, -4, "discriminante")
    require(roots_of(x ** 2 - 2 * x + 2) == {1 + sp.I: 1, 1 - sp.I: 1}, "raíces 1 ± i")
    same(sp.expand((x - 1) * (x ** 2 - 2 * x + 2)), pa, "factorización en R")
    require(roots_of(pa, filter="R") == {1: 1}, "única raíz real")
    same(1 + (1 + sp.I) + (1 - sp.I), 3, "suma de raíces")
    same(sp.expand(1 * (1 + sp.I) * (1 - sp.I)), 2, "producto de raíces")
    # (b)
    qq = (lam - 2) * ((lam - 1) * (lam - 3) - 3)
    same(sp.expand((lam - 1) * (lam - 3) - 3), lam ** 2 - 4 * lam, "corchete")
    same(sp.expand((lam - 1) * (lam - 3) - 3), lam * (lam - 4), "λ(λ-4)")
    same(sp.expand(qq), sp.expand(lam * (lam - 2) * (lam - 4)), "q = λ(λ-2)(λ-4)")
    same(sp.expand(qq), lam ** 3 - 6 * lam ** 2 + 8 * lam, "expandido")
    require(roots_of(qq, lam) == {0: 1, 2: 1, 4: 1}, "raíces simples 0, 2, 4")
    same(0 + 2 + 4, 6, "suma de raíces")


@check("R.13", "Factorizar un polinomio de grado 3", page=POL)
def _():
    cf = [1, 2, -5, -6]
    p = poly(cf)
    require(rational_candidates(cf) == {1, -1, 2, -2, 3, -3, 6, -6}, "candidatas")
    same(p.subs(x, 1), -8, "p(1)")
    same(p.subs(x, -1), 0, "p(-1)")
    q, r = ruffini(cf, -1)
    require(q == [1, 1, -6] and r == 0, "Ruffini con -1")
    require(roots_of(x ** 2 + x - 6) == {2: 1, -3: 1}, "raíces del cociente")
    same(sp.expand((x + 1) * (x - 2) * (x + 3)), p, "factorización")
    same(sp.factor(p), (x + 1) * (x - 2) * (x + 3), "sp.factor")
    require(roots_of(p) == {-1: 1, 2: 1, -3: 1}, "raíces simples")
    same(-1 + 2 - 3, -2, "suma")
    same((-1) * 2 * (-3), 6, "producto")


@check("R.14", "Teorema del resto con parámetro", page=POL)
def _():
    p = x ** 3 + k * x ** 2 - x + 2
    same(p.subs(x, 2), 8 + 4 * k, "p(2)")
    require(sp.solve(p.subs(x, 2), k) == [-2], "k = -2")
    pk = p.subs(k, -2)
    same(pk, x ** 3 - 2 * x ** 2 - x + 2, "p con k=-2")
    q, r = ruffini([1, -2, -1, 2], 2)
    require(q == [1, 0, -1] and r == 0, "Ruffini con 2")
    same(sp.expand((x - 2) * (x - 1) * (x + 1)), pk, "factorización")
    same(sp.expand(x ** 2 * (x - 2) - (x - 2)), pk, "por agrupación")
    same(sp.factor(pk), (x - 2) * (x - 1) * (x + 1), "sp.factor")
    require(roots_of(pk) == {2: 1, 1: 1, -1: 1}, "raíces")
    for v in (0, 1, -1, 3):
        require(p.subs({k: v, x: 2}) != 0, f"k={v} no sirve")


@check("R.15", "Raíces y multiplicidades", page=POL)
def _():
    cf = [1, -4, 5, -2]
    p = poly(cf, lam)
    require(rational_candidates(cf) == {1, -1, 2, -2}, "candidatas")
    same(p.subs(lam, 1), 0, "p(1)")
    q, r = ruffini(cf, 1)
    require(q == [1, -3, 2] and r == 0, "Ruffini con 1")
    q2, r2 = ruffini(q, 1)
    require(r2 == 0 and q2 == [1, -2], "1 vuelve a ser raíz")
    same(sp.expand((lam - 1) * (lam - 2)), lam ** 2 - 3 * lam + 2, "cociente")
    same(sp.factor(p), (lam - 1) ** 2 * (lam - 2), "factorización")
    require(roots_of(p, lam) == {1: 2, 2: 1}, "multiplicidades")
    same(1 + 1 + 2, 4, "suma de raíces")
    same(1 * 1 * 2, 2, "producto de raíces")


@check("R.16", "Raíz fraccionaria y factor irreducible", page=POL)
def _():
    cf = [3, -1, 3, -1]
    p = poly(cf)
    require(rational_candidates(cf) == {1, -1, sp.Rational(1, 3), -sp.Rational(1, 3)}, "candidatas")
    same(p.subs(x, 1), 4, "p(1)")
    same(p.subs(x, -1), -8, "p(-1)")
    same(p.subs(x, sp.Rational(1, 3)), 0, "p(1/3)")
    require(p.subs(x, -sp.Rational(1, 3)) != 0, "p(-1/3) ≠ 0")
    same(p.subs(x, -sp.Rational(1, 3)), -sp.Rational(1, 9) - sp.Rational(1, 9) - 1 - 1, "valor de p(-1/3)")
    q, r = ruffini(cf, sp.Rational(1, 3))
    require(q == [3, 0, 3] and r == 0, "Ruffini con 1/3")
    same(0 ** 2 - 4 * 1 * 1, -4, "discriminante de x²+1")
    same(sp.expand((3 * x - 1) * (x ** 2 + 1)), p, "factorización")
    same(sp.expand(x ** 2 * (3 * x - 1) + (3 * x - 1)), p, "por agrupación")
    same(sp.factor(p), (3 * x - 1) * (x ** 2 + 1), "sp.factor")
    require(roots_of(p, filter="R") == {sp.Rational(1, 3): 1}, "única raíz real")


# ---------------------------------------------------------------------------
# R.5 Rectas y planos
# ---------------------------------------------------------------------------
@check("R.T05.E1", "Recta por dos puntos en R^3", page=RP)
def _():
    P, Q = (1, 2, -1), (3, 1, 1)
    d = tuple(q - p for p, q in zip(P, Q))
    require(d == (2, -1, 2), "d = Q - P")
    X = tuple(p + t * di for p, di in zip(P, d))
    same(M(list(X)), M([1 + 2 * t, 2 - t, -1 + 2 * t]), "paramétricas")
    xx, yy, zz = X
    same(xx + 2 * yy, 5, "x + 2y = 5 sobre toda la recta")
    same(2 * yy + zz, 3, "2y + z = 3 sobre toda la recta")
    same(xx - zz, 2, "x - z = 2 sobre toda la recta")
    same((xx + 2 * yy) - (2 * yy + zz), 5 - 3, "resta de las dos ecuaciones: x - z = 2")
    Aimp = M([[1, 2, 0], [1, 0, -1]])
    N = Aimp.nullspace()
    require(len(N) == 1 and sp.Matrix.hstack(N[0], col(*d)).rank() == 1, "el director genera el núcleo")
    require(Aimp.rank() == 2, "dos ecuaciones independientes")
    require(cross((1, 2, 0), (1, 0, -1)) == (-2, 1, -2), "normales: su producto es paralelo a d")
    R = (5, 0, 3)
    require(R[0] + 2 * R[1] == 5 and R[0] - R[2] == 2, "R ∈ r")
    require(tuple(p + 2 * di for p, di in zip(P, d)) == R, "R corresponde a t = 2")
    for pt in (P, Q):
        require(pt[0] + 2 * pt[1] == 5 and pt[0] - pt[2] == 2, "P y Q están en r")
    require(d[0] + 2 * d[1] == 0 and d[0] - d[2] == 0, "d cumple las ecuaciones homogéneas")


@check("R.T05.E2", "Plano por tres puntos", page=RP)
def _():
    A_, B_, C_ = (1, 0, 1), (2, 1, 0), (0, 2, 3)
    u = tuple(q - p for p, q in zip(A_, B_))
    v = tuple(q - p for p, q in zip(A_, C_))
    require(u == (1, 1, -1) and v == (-1, 2, 2), "directores")
    n = cross(u, v)
    require(n == (4, -1, 3), "n = u×v")
    require(cross(u, v) != (0, 0, 0), "no paralelos")
    require(dot(n, u) == 0 and dot(n, v) == 0, "n ⟂ u, v")
    d = dot(n, A_)
    require(d == 7, "d = n·A")
    for pt in (A_, B_, C_):
        require(dot(n, pt) == 7, f"{pt} ∈ π")
    require(dot(n, B_) == 8 - 1 + 0 and dot(n, C_) == 0 - 2 + 9, "valores de B y C")
    same(dot(n, n), 26, "|n|² = 26")
    same(sp.Rational(dot(n, n), 4), sp.Rational(26, 4), "(área del triángulo)² = 26/4")


@check("R.T05.E3", "De generadores a ecuación y de ecuación a generadores", page=RP)
def _():
    # (a)
    u, v = (1, 0, 0), (0, 2, 1)
    n = cross(u, v)
    require(n == (0, -1, 2), "n = u×v")
    require(dot(n, u) == 0 and dot(n, v) == 0, "n ⟂ u, v")
    w = (3, 4, 2)
    require(-w[1] + 2 * w[2] == 0, "w ∈ π0")
    require(tuple(3 * p + 2 * q for p, q in zip(u, v)) == w, "w = 3u + 2v")
    require(-1 + 2 * 1 == 1, "(1,1,1) no está")
    require(len(M([[0, -1, 2]]).nullspace()) == 2, "dim π0 = 2")
    require(sp.Matrix.hstack(*M([[0, -1, 2]]).nullspace(), col(*u), col(*v)).rank() == 2, "π0 = gen{u,v}")
    # (b)
    Sg = M([[1, -1, 2]])
    g1, g2 = col(1, 1, 0), col(-2, 0, 1)
    same(Sg * g1, M([[0]]), "g1 ∈ σ")
    same(Sg * g2, M([[0]]), "g2 ∈ σ")
    yy_, zz_ = sp.symbols("yy zz")
    same(col(yy_ - 2 * zz_, yy_, zz_), yy_ * g1 + zz_ * g2, "x = y - 2z")
    require(len(Sg.nullspace()) == 2, "dos variables libres")
    require(sp.Matrix.hstack(*Sg.nullspace(), g1, g2).rank() == 2, "σ = gen{g1,g2}")
    require(cross((1, 1, 0), (-2, 0, 1)) == (1, -1, 2), "normal de σ")


@check("R.17", "Plano por un punto con normal dado", page=RP)
def _():
    P, n, Q = (2, -1, 3), (1, 2, -2), (0, 0, 3)
    same(dot(n, P), -6, "n·P")
    same(dot(n, Q), -6, "Q ∈ π")
    d1, d2 = (2, -1, 0), (2, 0, 1)
    require(dot(n, d1) == 0 and dot(n, d2) == 0, "directores en π")
    require(cross(d1, d2) == (-1, -2, 2) == tuple(-c for c in n), "d1×d2 = -n")
    require(cross(d1, d2) != (0, 0, 0), "no paralelos")
    X = tuple(p + s * a1 + t * a2 for p, a1, a2 in zip(P, d1, d2))
    same(dot(n, X), -6, "la ecuación vectorial cumple la implícita para todo s, t")


@check("R.18", "Producto vectorial y plano por el origen", page=RP)
def _():
    u, v = (1, 2, 3), (0, 1, -1)
    w = cross(u, v)
    require(w == (-5, 1, 1), "w = u×v")
    require(dot(w, u) == 0 and dot(w, v) == 0, "w ⟂ u, v")
    require(w == tuple(-c for c in cross(v, u)), "v×u = -(u×v)")
    same(dot(w, w), 27, "|w|² = 27")
    same(sp.sqrt(dot(w, w)), 3 * sp.sqrt(3), "área = 3√3")
    require(sp.Matrix.hstack(*M([[-5, 1, 1]]).nullspace(), col(*u), col(*v)).rank() == 2, "plano = gen{u,v}")
    require(len(M([[-5, 1, 1]]).nullspace()) == 2, "dim 2")


@check("R.19", "Posición relativa de rectas y un plano", page=RP)
def _():
    n = (2, -1, 1)
    # recta r
    Pr, dr = (1, 0, 2), (1, 1, -1)
    same(dot(dr, n), 0, "d_r · n")
    same(dot(n, Pr), 4, "P_r no cumple la ecuación")
    require(dot(n, Pr) != 7, "r paralela, no contenida")
    Xr = tuple(p + t * d for p, d in zip(Pr, dr))
    same(dot(n, Xr), 4, "2(1+t) - t + (2-t) = 4 para todo t")
    require(sp.solve(sp.Eq(sp.expand(dot(n, Xr)), 7), t) == [], "nunca vale 7")
    # recta s
    Ps, ds = (1, 1, 0), (1, 2, 1)
    same(dot(ds, n), 1, "d_s · n")
    Xs = tuple(p + t * d for p, d in zip(Ps, ds))
    same(M(list(Xs)), M([1 + t, 1 + 2 * t, t]), "paramétricas de s")
    same(dot(n, Xs), 1 + t, "2(1+t) - (1+2t) + t = 1 + t")
    require(sp.solve(sp.Eq(sp.expand(dot(n, Xs)), 7), t) == [6], "t = 6")
    pt = tuple(c.subs(t, 6) for c in Xs)
    require(pt == (7, 13, 6), "punto de intersección")
    same(dot(n, pt), 7, "pertenece al plano")


@check("R.20", "Subespacio o no: plano por el origen y plano afín", page=RP)
def _():
    g1, g2 = (1, 0, 2), (0, 1, -1)
    w = cross(g1, g2)
    require(w == (-2, 1, 1), "normal")
    require(dot(w, g1) == 0 and dot(w, g2) == 0, "ortogonal a los generadores")
    require(tuple(-c for c in w) == (2, -1, -1), "2x - y - z = 0 equivale a -2x + y + z = 0")
    # (1,1,1) ∈ π
    require(dot((2, -1, -1), (1, 1, 1)) == 0, "(1,1,1) cumple 2x-y-z=0")
    require(tuple(1 * p + 1 * q for p, q in zip(g1, g2)) == (1, 1, 1), "(1,1,1) = 1·g1 + 1·g2")
    require(M([[1, 0, 2], [0, 1, -1], [1, 1, 1]]).rank() == 2, "(1,1,1) ∈ gen{g1,g2}")
    require(dot((2, -1, -1), tuple(c * 5 for c in (1, 1, 1))) == 0, "múltiplos también")
    # π' no es cerrado
    f = lambda pt: dot((2, -1, -1), pt)
    p1, p2 = (1, 1, 0), (1, 0, 1)
    require(f(p1) == 1 and f(p2) == 1, "los puntos están en π'")
    ssum = tuple(p + q for p, q in zip(p1, p2))
    require(ssum == (2, 1, 1) and f(ssum) == 2 and f(ssum) != 1, "su suma no está en π'")
    require(f((0, 0, 0)) == 0 != 1, "el origen no está en π'")
    # en general la suma da 1 + 1 = 2
    a1, a2, a3, c1, c2, c3 = sp.symbols("a1 a2 a3 c1 c2 c3")
    same(f((a1 + c1, a2 + c2, a3 + c3)), f((a1, a2, a3)) + f((c1, c2, c3)), "linealidad: 1 + 1 = 2")
