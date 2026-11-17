"""Comprobaciones de los ejemplos resueltos de la Unidad 4 (teoría): espacios con producto interno.

Cada función recalcula el ejemplo desde sus datos. Las cantidades irracionales (normas, cosenos)
se comprueban a través de sus cuadrados y su signo, para que la verificación sea exacta.
Las cuentas sobre Z_2 usan exclusivamente las funciones ``gf_*`` (aritmética módulo 2).
"""
import itertools

import sympy as sp

from content_pipeline.mathcheck import (
    check,
    gf_dot,
    gf_matmul,
    gf_nullspace,
    gf_rank,
    gf_span,
    hamming,
    min_distance,
    require,
    same,
    weight,
)

R = sp.Rational
BASE = "/algebra-ii/unidad-4/teoria/"


# ---------------------------------------------------------------------------
# Auxiliares sobre R^n con producto <u, v> = u^t M v (M simétrica).
# ---------------------------------------------------------------------------
def _col(*entries):
    return sp.Matrix(list(entries))


def _ip(M, u, v):
    return (u.T * M * v)[0, 0]


def _minors(M):
    return [M[:k, :k].det() for k in range(1, M.shape[0] + 1)]


def _require_inner_product(M, what):
    """Simétrica con menores principales positivos (criterio de Sylvester)."""
    require(M == M.T, f"{what}: la matriz de Gram no es simétrica")
    require(all(m > 0 for m in _minors(M)), f"{what}: algún menor principal no es positivo")


def _gram_schmidt(vectors, M):
    ws = []
    for v in vectors:
        w = v
        for u in ws:
            w = w - (_ip(M, v, u) / _ip(M, u, u)) * u
        ws.append(w)
    return ws


def _parallel(u, v):
    return sp.Matrix.hstack(u, v).rank() == 1


def _same_span(first, second):
    a, b = sp.Matrix.hstack(*first), sp.Matrix.hstack(*second)
    return a.rank() == b.rank() == sp.Matrix.hstack(a, b).rank()


def _same_list(actual, expected, what):
    """Compara listas de escalares entrada por entrada (como vectores columna)."""
    require(len(actual) == len(expected), f"{what}: longitudes distintas")
    same(sp.Matrix(list(actual)), sp.Matrix(list(expected)), what)


def _proj(v, orthogonal_basis, M):
    p = sp.zeros(v.shape[0], 1)
    for u in orthogonal_basis:
        p = p + (_ip(M, v, u) / _ip(M, u, u)) * u
    return p


# Producto por evaluación en P_2[R] (coordenadas en E = {1, x, x^2}).
_NODES = (-1, 0, 1)
_EV = sp.Matrix([[1, t, t * t] for t in _NODES])
_G_EVAL = _EV.T * _EV


def _least_squares(columns, y):
    A = sp.Matrix.hstack(*columns)
    AtA, Aty = A.T * A, A.T * y
    x = AtA.inv() * Aty
    residual = y - A * x
    return A, AtA, Aty, x, residual


# ---------------------------------------------------------------------------
# 4.1 Producto interno
# ---------------------------------------------------------------------------
PAGE = BASE + "producto-interno/"


@check("U4.T01.E1", "Producto u^t M v en R^2: criterio 2x2 y completar cuadrados", page=PAGE)
def _():
    M = sp.Matrix([[3, -1], [-1, 2]])
    same(M[0, 0], 3, "m11")
    same(M.det(), 5, "det M")
    _require_inner_product(M, "M")
    # 3 x1^2 - 2 x1 x2 + 2 x2^2 = 3 (x1 - x2/3)^2 + (5/3) x2^2  <=>  M = U^t D U
    U = sp.Matrix([[1, R(-1, 3)], [0, 1]])
    D = sp.diag(3, R(5, 3))
    same(U.T * D * U, M, "completar cuadrados")
    same(_ip(M, _col(1, 2), _col(2, -1)), -1, "<(1,2),(2,-1)>")
    # No ejemplo: matriz con determinante negativo.
    N = sp.Matrix([[1, 4], [4, 1]])
    same(N.det(), -15, "det N")
    same(_ip(N, _col(1, -1), _col(1, -1)), -6, "<(1,-1),(1,-1)>_N")


@check("U4.T01.E2", "Suma de productos de formas lineales en R^2", page=PAGE)
def _():
    L = sp.Matrix([[1, 0], [1, 1]])  # formas x1 y x1 + x2
    M = L.T * L
    same(M, sp.Matrix([[2, 1], [1, 1]]), "matriz de Gram")
    require(L.det() != 0, "las formas lineales deben ser LI")
    _require_inner_product(M, "x1y1+(x1+x2)(y1+y2)")
    for x in itertools.product(range(-2, 3), repeat=2):
        for y in itertools.product(range(-2, 3), repeat=2):
            explicit = x[0] * y[0] + (x[0] + x[1]) * (y[0] + y[1])
            same(_ip(M, _col(*x), _col(*y)), explicit, "fórmula vs. Gram")
    same(_ip(M, _col(1, 0), _col(0, 1)), 1, "<e1,e2>")


@check("U4.T01.E3", "Producto tr(A^t B) en R^{2x2}", page=PAGE)
def _():
    S = sp.Matrix([[1, 2], [2, 3]])
    K = sp.Matrix([[0, 1], [-1, 0]])
    same((S.T * K).trace(), 0, "<S,K>")
    A = sp.Matrix([[1, 2], [0, -1]])
    B = sp.Matrix([[3, -1], [4, 2]])
    entrywise = sum(A[i, j] * B[i, j] for i in range(2) for j in range(2))
    same((A.T * B).trace(), entrywise, "traza = suma de productos de entradas")
    same(entrywise, -1, "<A,B>")


@check("U4.T01.E4", "Producto por evaluación en P_2: tres nodos sí, dos no", page=PAGE)
def _():
    require(_EV.det() != 0, "Vandermonde con tres nodos distintos")
    same(_EV.det(), 2, "det Vandermonde")
    p, q = _col(1, 1, 0), _col(0, 0, 1)  # 1 + x, x^2
    same((_EV * p).dot(_EV * q), 2, "<1+x, x^2>")
    two = sp.Matrix([[1, 0, 0], [1, 1, 1]])  # nodos 0 y 1
    r = _col(0, -1, 1)  # x^2 - x
    same(two * r, sp.zeros(2, 1), "x^2 - x se anula en 0 y 1")
    same((two * r).dot(two * r), 0, "<x^2-x, x^2-x> con dos nodos")


@check("U4.T01.E5", "Matriz de Gram del producto por evaluación en P_2", page=PAGE)
def _():
    same(_G_EVAL, sp.Matrix([[3, 0, 2], [0, 2, 0], [2, 0, 2]]), "G_E")
    _same_list(_minors(_G_EVAL), [3, 6, 4], "menores principales")
    _require_inner_product(_G_EVAL, "evaluación en -1, 0, 1")
    p, q = _col(2, -1, 1), _col(1, 3, -1)  # 2 - x + x^2, 1 + 3x - x^2
    same(_EV * p, _col(4, 2, 2), "valores de p")
    same(_EV * q, _col(-3, 1, 3), "valores de q")
    same((_EV * p).dot(_EV * q), -4, "<p,q> por evaluación")
    same(_ip(_G_EVAL, p, q), -4, "<p,q> con la matriz de Gram")


# ---------------------------------------------------------------------------
# 4.2 Norma, distancia y ángulo
# ---------------------------------------------------------------------------
PAGE = BASE + "norma-distancia-angulo/"


@check("U4.T02.E1", "Norma, distancia y ángulo con el producto usual en R^3", page=PAGE)
def _():
    u, v = _col(2, 1, -2), _col(1, 1, 0)
    same(u.dot(u), 9, "||u||^2")
    same(v.dot(v), 2, "||v||^2")
    same(u.dot(v), 3, "u.v")
    same((u - v).dot(u - v), 5, "d(u,v)^2")
    same(u.dot(v) ** 2 / (u.dot(u) * v.dot(v)), R(1, 2), "cos^2")
    require(u.dot(v) > 0, "coseno positivo: ángulo pi/4")
    require(u.dot(v) ** 2 <= u.dot(u) * v.dot(v), "Cauchy-Schwarz")


@check("U4.T02.E2", "Los canónicos con un producto no usual", page=PAGE)
def _():
    M = sp.Matrix([[2, 1], [1, 1]])
    e1, e2 = _col(1, 0), _col(0, 1)
    same(_ip(M, e1, e1), 2, "||e1||^2")
    same(_ip(M, e2, e2), 1, "||e2||^2")
    same(_ip(M, e1, e2), 1, "<e1,e2>")
    same(_ip(M, e1, e2) ** 2 / (_ip(M, e1, e1) * _ip(M, e2, e2)), R(1, 2), "cos^2")
    same(_ip(M, e1 - e2, e1 - e2), 1, "d(e1,e2)^2")
    # ley del coseno: ||e1-e2||^2 = ||e1||^2 + ||e2||^2 - 2<e1,e2>
    same(_ip(M, e1, e1) + _ip(M, e2, e2) - 2 * _ip(M, e1, e2), 1, "ley del coseno")
    same(_ip(M, e1, _col(1, -2)), 0, "(1,-2) ortogonal a e1")


@check("U4.T02.E3", "Ángulo y Pitágoras en P_2 con producto por evaluación", page=PAGE)
def _():
    p, q = _col(0, 1, 0), _col(0, 1, 1)  # x, x + x^2
    same(_ip(_G_EVAL, p, q), 2, "<x, x+x^2>")
    same(_ip(_G_EVAL, p, p), 2, "||x||^2")
    same(_ip(_G_EVAL, q, q), 4, "||x+x^2||^2")
    same(_ip(_G_EVAL, p, q) ** 2 / (_ip(_G_EVAL, p, p) * _ip(_G_EVAL, q, q)), R(1, 2), "cos^2")
    one = _col(1, 0, 0)
    same(_ip(_G_EVAL, one, p), 0, "1 ortogonal a x")
    same(_ip(_G_EVAL, one + p, one + p), _ip(_G_EVAL, one, one) + _ip(_G_EVAL, p, p), "Pitágoras")
    same(_ip(_G_EVAL, one + p, one + p), 5, "||1+x||^2")


@check("U4.T02.E4", "Similitud coseno entre documentos", page=PAGE)
def _():
    d1 = _col(2, 1, 2, 0, 0)
    d2, d3, d4 = _col(4, 2, 4, 0, 0), _col(1, 0, 0, 2, 2), _col(2, 2, 1, 0, 0)
    same(d1.dot(d1), 9, "||d1||^2")
    expected = {"d2": (d2, 18, 36, 1, 9), "d3": (d3, 2, 9, R(2, 9), 14), "d4": (d4, 8, 9, R(8, 9), 2)}
    for name, (d, dot_value, norm2, cosine, dist2) in expected.items():
        same(d1.dot(d), dot_value, f"d1.{name}")
        same(d.dot(d), norm2, f"||{name}||^2")
        same(d1.dot(d) ** 2 / (d1.dot(d1) * d.dot(d)), cosine ** 2, f"cos^2(d1,{name})")
        require(d1.dot(d) > 0, f"coseno positivo con {name}")
        same((d1 - d).dot(d1 - d), dist2, f"d(d1,{name})^2")
    # Con vectores normalizados: ||a/|a| - b/|b|||^2 = 2 - 2 cos.  Para d1 y d2 (mismo sentido) da 0.
    same(d1 / 3 - d2 / 6, sp.zeros(5, 1), "d1 y d2 normalizados coinciden")


# ---------------------------------------------------------------------------
# 4.3 Ortogonalidad
# ---------------------------------------------------------------------------
PAGE = BASE + "ortogonalidad/"


@check("U4.T03.E1", "Coordenadas en una base ortogonal de R^2", page=PAGE)
def _():
    u1, u2, v = _col(2, 1), _col(-1, 2), _col(4, 7)
    same(u1.dot(u2), 0, "u1 . u2")
    c1, c2 = v.dot(u1) / u1.dot(u1), v.dot(u2) / u2.dot(u2)
    same(c1, 3, "c1")
    same(c2, 2, "c2")
    same(c1 * u1 + c2 * u2, v, "reconstrucción")
    same(sp.Matrix.hstack(u1, u2).inv() * v, _col(3, 2), "coordenadas por sistema")


@check("U4.T03.E2", "Base ortogonal y ortonormal de R^3, coordenadas y Q^tQ = I", page=PAGE)
def _():
    U = sp.Matrix([[1, 1, 1], [1, -2, 0], [1, 1, -1]])  # columnas u1, u2, u3
    same(U.T * U, sp.diag(3, 6, 2), "U^t U")
    v = _col(2, -3, 4)
    cs = [v.dot(U[:, i]) / U[:, i].dot(U[:, i]) for i in range(3)]
    same(sp.Matrix(cs), _col(1, 2, -1), "coordenadas")
    same(U * sp.Matrix(cs), v, "reconstrucción")
    # Coordenadas en la base ortonormal: <v, u_i>/||u_i||; se comprueban cuadrados y signos.
    squares = [v.dot(U[:, i]) ** 2 / U[:, i].dot(U[:, i]) for i in range(3)]
    same(sp.Matrix(squares), _col(3, 24, 2), "cuadrados de las coordenadas ortonormales")
    require([sp.sign(v.dot(U[:, i])) for i in range(3)] == [1, 1, -1], "signos")
    same(sum(squares), v.dot(v), "Parseval: ||v||^2 = 29")
    # Q = U D^{-1/2}  =>  Q^t Q = D^{-1/2} (U^t U) D^{-1/2} = I.
    Dinv = sp.diag(R(1, 3), R(1, 6), R(1, 2))
    same(Dinv * (U.T * U), sp.eye(3), "Q^tQ = I (en forma racional)")


@check("U4.T03.E3", "Base ortogonal para un producto no usual en R^2", page=PAGE)
def _():
    M = sp.Matrix([[2, 1], [1, 1]])
    b1, b2, v = _col(1, 0), _col(1, -2), _col(3, 1)
    same(_ip(M, b1, b2), 0, "<b1,b2>")
    same(b1.dot(b2), 1, "con el producto usual no son ortogonales")
    same(_ip(M, b1, b1), 2, "||b1||^2")
    same(_ip(M, b2, b2), 2, "||b2||^2")
    same(_ip(M, v, b1), 7, "<v,b1>")
    same(_ip(M, v, b2), -1, "<v,b2>")
    c1, c2 = _ip(M, v, b1) / _ip(M, b1, b1), _ip(M, v, b2) / _ip(M, b2, b2)
    same(c1, R(7, 2), "c1")
    same(c2, R(-1, 2), "c2")
    same(c1 * b1 + c2 * b2, v, "reconstrucción")


# ---------------------------------------------------------------------------
# 4.4 Gram-Schmidt
# ---------------------------------------------------------------------------
PAGE = BASE + "gram-schmidt/"


@check("U4.T04.E1", "Gram-Schmidt de tres vectores de R^4 (producto usual)", page=PAGE)
def _():
    I4 = sp.eye(4)
    v1, v2, v3 = _col(1, 1, 1, 1), _col(1, 2, 0, 1), _col(2, 0, 1, 3)
    w1, w2, w3 = _gram_schmidt([v1, v2, v3], I4)
    same(w2, _col(0, 1, -1, 0), "w2")
    same(v3.dot(w1) / w1.dot(w1), R(3, 2), "coeficiente de w1 en el paso 3")
    same(v3.dot(w2) / w2.dot(w2), R(-1, 2), "coeficiente de w2 en el paso 3")
    same(w3, _col(R(1, 2), -1, -1, R(3, 2)), "w3")
    w3s = 2 * w3
    same(w3s, _col(1, -2, -2, 3), "w3 reescalado")
    for a, b in [(w1, w2), (w1, w3s), (w2, w3s)]:
        same(a.dot(b), 0, "ortogonalidad")
    _same_list([w1.dot(w1), w2.dot(w2), w3s.dot(w3s)], [4, 2, 18], "normas al cuadrado")
    require(_same_span([v1, v2, v3], [w1, w2, w3s]), "mismo subespacio generado")


@check("U4.T04.E2", "Base ortogonal de un plano con producto ponderado", page=PAGE)
def _():
    M = sp.diag(1, 2, 3)
    v1, v2 = _col(2, 1, 0), _col(1, 1, 1)
    normal = _col(1, -2, 1)
    _same_list([normal.dot(v1), normal.dot(v2)], [0, 0], "v1, v2 en el plano x1 - 2x2 + x3 = 0")
    w1, w2 = _gram_schmidt([v1, v2], M)
    same(_ip(M, v2, w1), 4, "<v2,w1>")
    same(_ip(M, w1, w1), 6, "||w1||^2")
    same(w2, _col(R(-1, 3), R(1, 3), 1), "w2")
    w2s = 3 * w2
    same(normal.dot(w2s), 0, "w2 en el plano")
    same(_ip(M, w1, w2s), 0, "ortogonales con el producto ponderado")
    same(_ip(M, w2s, w2s), 30, "||(-1,1,3)||^2")
    same(w1.dot(w2s), -1, "no ortogonales con el producto usual")


@check("U4.T04.E3", "Gram-Schmidt en P_2 con producto por evaluación", page=PAGE)
def _():
    E = [_col(1, 0, 0), _col(0, 1, 0), _col(0, 0, 1)]
    w1, w2, w3 = _gram_schmidt(E, _G_EVAL)
    same(w1, E[0], "w1 = 1")
    same(w2, E[1], "w2 = x")
    same(w3, _col(R(-2, 3), 0, 1), "w3 = x^2 - 2/3")
    q3 = 3 * w3  # 3x^2 - 2
    _same_list([_ip(_G_EVAL, w, w) for w in (w1, w2, q3)], [3, 2, 6], "normas al cuadrado")
    for a, b in [(w1, w2), (w1, q3), (w2, q3)]:
        same(_ip(_G_EVAL, a, b), 0, "ortogonalidad")
    p = _col(1, 2, 3)  # 1 + 2x + 3x^2
    coords = [_ip(_G_EVAL, p, b) / _ip(_G_EVAL, b, b) for b in (w1, w2, q3)]
    _same_list(coords, [3, 2, 1], "coordenadas de 1 + 2x + 3x^2")
    same(coords[0] * w1 + coords[1] * w2 + coords[2] * q3, p, "reconstrucción")


@check("U4.T04.E4", "Gram-Schmidt detecta dependencia lineal", page=PAGE)
def _():
    v1, v2, v3 = _col(1, 0, 1), _col(1, 1, 0), _col(3, 1, 2)
    same(2 * v1 + v2, v3, "v3 = 2 v1 + v2")
    w1, w2, w3 = _gram_schmidt([v1, v2, v3], sp.eye(3))
    same(2 * w2, _col(1, 2, -1), "w2 reescalado")
    same(w3, sp.zeros(3, 1), "w3 = 0")


@check("U4.T04.E5", "Completar una base ortogonal de R^4", page=PAGE)
def _():
    w1, w2, w3 = _col(1, 1, 1, 1), _col(0, 1, -1, 0), _col(1, -2, -2, 3)
    A = sp.Matrix.hstack(w1, w2, w3).T
    null = A.nullspace()
    require(len(null) == 1, "el complemento tiene dimensión 1")
    w4 = _col(-5, 1, 1, 3)
    require(_parallel(null[0], w4), "w4 genera el espacio nulo")
    same(A * w4, sp.zeros(3, 1), "w4 ortogonal a w1, w2, w3")
    # Segundo método: Gram-Schmidt sobre {w1, w2, w3, e1}.
    u4 = _gram_schmidt([w1, w2, w3, _col(1, 0, 0, 0)], sp.eye(4))[3]
    same(u4, R(5, 36) * _col(5, -1, -1, -3), "cuarto vector por Gram-Schmidt")
    require(_parallel(u4, w4), "ambos métodos dan la misma dirección")


# ---------------------------------------------------------------------------
# 4.5 Complemento ortogonal
# ---------------------------------------------------------------------------
PAGE = BASE + "complemento-ortogonal/"


@check("U4.T05.E1", "Complementos de una recta y de un plano en R^3", page=PAGE)
def _():
    d = _col(1, -1, 2)
    plane_basis = [_col(1, 1, 0), _col(-2, 0, 1)]
    _same_list([d.dot(b) for b in plane_basis], [0, 0], "base del plano ortogonal a d")
    require(sp.Matrix.hstack(*plane_basis).rank() == 2, "base LI")
    require(_same_span(sp.Matrix([[1, -1, 2]]).nullspace(), plane_basis), "L^perp = nul(d^t)")
    n = _col(2, 1, -1)
    pi = sp.Matrix([[2, 1, -1]]).nullspace()
    require(len(pi) == 2, "el plano tiene dimensión 2")
    _same_list([n.dot(b) for b in pi], [0, 0], "la normal es ortogonal al plano")


@check("U4.T05.E2", "Complemento ortogonal en R^4 como espacio nulo", page=PAGE)
def _():
    A = sp.Matrix([[1, 0, 2, -1], [0, 1, 1, 1]])
    perp = [_col(-2, -1, 1, 0), _col(1, -1, 0, 1)]
    same(A * sp.Matrix.hstack(*perp), sp.zeros(2, 2), "ortogonales a las filas")
    require(_same_span(A.nullspace(), perp), "S^perp = nul(A)")
    same(A.rank() + len(A.nullspace()), 4, "dim S + dim S^perp = 4")
    B = sp.Matrix.hstack(*perp).T
    require(_same_span(B.nullspace(), [A[0, :].T, A[1, :].T]), "(S^perp)^perp = S")


@check("U4.T05.E3", "Complemento ortogonal en R^{2x2} con la traza", page=PAGE)
def _():
    A1 = sp.Matrix([[1, 2], [0, 1]])
    A2 = sp.Matrix([[0, 1], [1, -1]])
    X1 = sp.Matrix([[2, -1], [1, 0]])
    X2 = sp.Matrix([[-3, 1], [0, 1]])
    for A in (A1, A2):
        for X in (X1, X2):
            same((A.T * X).trace(), 0, "ortogonalidad con la traza")
    flat = lambda m: sp.Matrix([m[0, 0], m[0, 1], m[1, 0], m[1, 1]])
    rows = sp.Matrix.hstack(flat(A1), flat(A2)).T
    require(_same_span(rows.nullspace(), [flat(X1), flat(X2)]), "S^perp = gen{X1, X2}")
    same(sp.Matrix.hstack(flat(A1), flat(A2), flat(X1), flat(X2)).rank(), 4, "S + S^perp = R^{2x2}")


@check("U4.T05.E4", "Complemento ortogonal con un producto no usual en R^3", page=PAGE)
def _():
    L = sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]])  # formas x1, x1+x2, x2+x3
    M = L.T * L
    same(M, sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 1]]), "matriz de Gram")
    _same_list(_minors(M), [2, 3, 1], "menores principales")
    _require_inner_product(M, "suma de tres cuadrados de formas")
    s1, s2 = _col(1, 0, 1), _col(0, 1, 0)
    same(M * s1, _col(2, 2, 1), "M s1")
    same(M * s2, _col(1, 2, 1), "M s2")
    equations = sp.Matrix.hstack(M * s1, M * s2).T
    perp = equations.nullspace()
    require(len(perp) == 1 and _parallel(perp[0], _col(0, 1, -2)), "S^perp = gen{(0,1,-2)}")
    _same_list([_ip(M, _col(0, 1, -2), s) for s in (s1, s2)], [0, 0], "comprobación")
    usual = sp.Matrix.hstack(s1, s2).T.nullspace()
    require(_parallel(usual[0], _col(1, 0, -1)), "con el producto usual sería gen{(1,0,-1)}")


# ---------------------------------------------------------------------------
# 4.6 Proyección y distancia
# ---------------------------------------------------------------------------
PAGE = BASE + "proyeccion-y-distancia/"


@check("U4.T06.E1", "Proyección sobre una recta de R^2", page=PAGE)
def _():
    u, v = _col(3, 1), _col(1, 3)
    p = _proj(v, [u], sp.eye(2))
    same(p, _col(R(9, 5), R(3, 5)), "proyección")
    r = v - p
    same(r, _col(R(-4, 5), R(12, 5)), "componente ortogonal")
    same(r.dot(u), 0, "residuo ortogonal a la recta")
    same(r.dot(r), R(32, 5), "d(v,L)^2")
    same((R(4, 5) * sp.sqrt(10)) ** 2, R(32, 5), "d = 4 sqrt(10)/5")
    A = u
    P = A * (A.T * A).inv() * A.T
    same(P, R(1, 10) * sp.Matrix([[9, 3], [3, 1]]), "matriz de proyección")
    same(P * v, p, "P v")


@check("U4.T06.E2", "La fórmula con una base no ortogonal falla", page=PAGE)
def _():
    s1, s2, v = _col(1, 0, 0), _col(1, 1, 0), _col(0, 1, 1)
    require(s1.dot(s2) != 0, "la base no es ortogonal")
    wrong = (v.dot(s1) / s1.dot(s1)) * s1 + (v.dot(s2) / s2.dot(s2)) * s2
    same(wrong, _col(R(1, 2), R(1, 2), 0), "resultado erróneo")
    same((v - wrong).dot(s1), R(-1, 2), "el residuo no es ortogonal a s1")
    w1, w2 = _gram_schmidt([s1, s2], sp.eye(3))
    same(_proj(v, [w1, w2], sp.eye(3)), _col(0, 1, 0), "proyección correcta")


@check("U4.T06.E3", "Proyección sobre un plano de R^3 por dos caminos", page=PAGE)
def _():
    n, v = _col(1, 1, 1), _col(5, 1, 0)
    q = (v.dot(n) / n.dot(n)) * n
    same(q, _col(2, 2, 2), "proy sobre S^perp")
    p = v - q
    same(p, _col(3, -1, -2), "proy sobre S")
    same(n.dot(p), 0, "p pertenece al plano")
    a, b = _col(1, -1, 0), _col(1, 1, -2)
    _same_list([a.dot(b), n.dot(a), n.dot(b)], [0, 0, 0], "base ortogonal del plano")
    _same_list([v.dot(a) / a.dot(a), v.dot(b) / b.dot(b)], [2, 1], "coeficientes")
    same(_proj(v, [a, b], sp.eye(3)), p, "mismo resultado con base ortogonal")
    same(q.dot(q), 12, "d(v,S)^2")
    same(p.dot(p), 14, "||p||^2")
    same(p.dot(p) + q.dot(q), v.dot(v), "Pitágoras")


@check("U4.T06.E4", "Proyección con producto no usual por tres métodos", page=PAGE)
def _():
    M = sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 1]])
    s1, s2, v = _col(1, 0, 1), _col(0, 1, 0), _col(1, 2, 3)
    expected = _col(1, 3, 1)
    # Método 1: base ortogonal de S.
    w1, w2 = _gram_schmidt([s2, s1], M)
    same(w2, _col(1, -1, 1), "segundo vector ortogonal")
    _same_list([_ip(M, w1, w1), _ip(M, w2, w2)], [2, 1], "normas al cuadrado")
    _same_list([_ip(M, v, w1), _ip(M, v, w2)], [8, 1], "productos con v")
    same(_proj(v, [w1, w2], M), expected, "método 1")
    # Método 2: sistema con la matriz de Gram de {s1, s2}.
    Gs = sp.Matrix([[_ip(M, a, b) for b in (s1, s2)] for a in (s1, s2)])
    same(Gs, sp.Matrix([[3, 2], [2, 2]]), "Gram de S")
    rhs = _col(_ip(M, v, s1), _ip(M, v, s2))
    same(rhs, _col(9, 8), "lado derecho")
    ab = Gs.inv() * rhs
    same(ab, _col(1, 3), "coeficientes")
    same(ab[0] * s1 + ab[1] * s2, expected, "método 2")
    # Método 3: base de S unida a base de S^perp.
    t = _col(0, 1, -2)
    coef = sp.Matrix.hstack(s1, s2, t).inv() * v
    same(coef, _col(1, 3, -1), "coordenadas en {s1, s2, t}")
    same(coef[0] * s1 + coef[1] * s2, expected, "método 3")
    residual = v - expected
    same(residual, _col(0, -1, 2), "proy sobre S^perp")
    same(_ip(M, residual, residual), 2, "d(v,S)^2")
    usual = v - (v.dot(_col(1, 0, -1)) / 2) * _col(1, 0, -1)
    same(usual, _col(2, 2, 2), "con el producto usual la proyección es otra")


@check("U4.T06.E5", "Mejor aproximación de x^2 por polinomios de grado <= 1", page=PAGE)
def _():
    q = _col(0, 0, 1)
    one, x = _col(1, 0, 0), _col(0, 1, 0)
    same(_ip(_G_EVAL, one, x), 0, "{1, x} ortogonal")
    _same_list([_ip(_G_EVAL, q, one), _ip(_G_EVAL, q, x)], [2, 0], "productos")
    p = _proj(q, [one, x], _G_EVAL)
    same(p, _col(R(2, 3), 0, 0), "proyección = 2/3")
    r = q - p
    same(_ip(_G_EVAL, r, r), R(2, 3), "d^2")
    same((sp.sqrt(6) / 3) ** 2, R(2, 3), "d = sqrt(6)/3")
    same(_EV * r, _col(R(1, 3), R(-2, 3), R(1, 3)), "valores del error en -1, 0, 1")


# ---------------------------------------------------------------------------
# 4.7 Cuadrados mínimos
# ---------------------------------------------------------------------------
PAGE = BASE + "cuadrados-minimos/"


@check("U4.T07.E1", "Recta de cuadrados mínimos con cinco puntos", page=PAGE)
def _():
    xs, ys = [0, 1, 2, 3, 4], [1, 2, 2, 4, 6]
    ones, xcol, y = sp.ones(5, 1), sp.Matrix(xs), sp.Matrix(ys)
    A, AtA, Aty, sol, r = _least_squares([ones, xcol], y)
    same(AtA, sp.Matrix([[5, 10], [10, 30]]), "A^tA")
    same(Aty, _col(15, 42), "A^t b")
    same(AtA.det(), 50, "det A^tA")
    same(sol, _col(R(3, 5), R(6, 5)), "a = 0.6, b = 1.2")
    same(A * sol, _col(R(3, 5), R(9, 5), 3, R(21, 5), R(27, 5)), "valores ajustados")
    same(r, _col(R(2, 5), R(1, 5), -1, R(-1, 5), R(3, 5)), "residuos")
    same(A.T * r, sp.zeros(2, 1), "residuo ortogonal a col(A)")
    same(r.dot(r), R(8, 5), "error cuadrático")


@check("U4.T07.E2", "Parábola de cuadrados mínimos", page=PAGE)
def _():
    xs = [-1, 0, 1, 2]
    y = _col(R(28, 10), R(16, 10), R(4, 10), R(32, 10))
    cols = [sp.ones(4, 1), sp.Matrix(xs), sp.Matrix([t * t for t in xs])]
    A, AtA, Aty, sol, r = _least_squares(cols, y)
    same(AtA, sp.Matrix([[4, 2, 6], [2, 6, 8], [6, 8, 18]]), "A^tA")
    same(Aty, _col(8, 4, 16), "A^t b")
    same(sol, _col(1, -1, 1), "y = 1 - x + x^2")
    same(r, _col(R(-1, 5), R(3, 5), R(-3, 5), R(1, 5)), "residuos")
    same(r.dot(r), R(4, 5), "error cuadrático")


@check("U4.T07.E3", "Ajuste exponencial linealizado con log en base 2", page=PAGE)
def _():
    ts, ys = [0, 1, 2, 3], [1, 2, 8, 16]
    zs = [y.bit_length() - 1 for y in ys]
    require(all(2 ** z == y for z, y in zip(zs, ys)), "log2 exactos")
    same(sp.Matrix(zs), _col(0, 1, 3, 4), "z = log2 y")
    A, AtA, Aty, sol, r = _least_squares([sp.ones(4, 1), sp.Matrix(ts)], sp.Matrix(zs))
    same(AtA, sp.Matrix([[4, 6], [6, 14]]), "A^tA")
    same(Aty, _col(8, 19), "A^t z")
    same(sol, _col(R(-1, 10), R(7, 5)), "z = -0.1 + 1.4 t")
    same(r.dot(r), R(1, 5), "error cuadrático en escala logarítmica")


@check("U4.T07.E4", "Tiempo de ejecución: modelo cuadrático vs. lineal", page=PAGE)
def _():
    ns = [1, 2, 3, 4]
    t = _col(R(35, 10), R(82, 10), R(193, 10), 33)
    ones = sp.ones(4, 1)
    A, AtA, Aty, sol, r = _least_squares([ones, sp.Matrix([n * n for n in ns])], t)
    same(AtA, sp.Matrix([[4, 30], [30, 354]]), "A^tA cuadrático")
    same(Aty, _col(64, 738), "A^t t cuadrático")
    same(sol, _col(1, 2), "t = 1 + 2 n^2")
    same(r, _col(R(1, 2), R(-4, 5), R(3, 10), 0), "residuos")
    same(r.dot(r), R(49, 50), "error cuadrático = 0.98")
    same(sol[0] + sol[1] * 25, 51, "predicción en n = 5")
    A2, AtA2, Aty2, sol2, r2 = _least_squares([ones, sp.Matrix(ns)], t)
    same(AtA2, sp.Matrix([[4, 10], [10, 30]]), "A^tA lineal")
    same(Aty2, _col(64, R(1049, 5)), "A^t t lineal")
    same(sol2, _col(R(-89, 10), R(249, 25)), "t = -8.9 + 9.96 n")
    same(r2.dot(r2), R(5243, 250), "error cuadrático lineal = 20.972")


# ---------------------------------------------------------------------------
# 4.8 Códigos y Z_2^n  (aritmética módulo 2 exacta)
# ---------------------------------------------------------------------------
PAGE = BASE + "codigos-y-z2/"


def _bits(word):
    return [int(c) for c in word]


def _words(vectors):
    return {"".join(str(x) for x in v) for v in vectors}


def _dual(words, n):
    return {w for w in itertools.product((0, 1), repeat=n) if all(gf_dot(w, c) == 0 for c in words)}


@check("U4.T08.E1", "Producto punto en Z_2^n y vectores autoortogonales", page=PAGE)
def _():
    u, v = _bits("10110"), _bits("11101")
    require(gf_dot(u, v) == 0, "u . v = 0")
    require(gf_dot(u, u) == 1 and weight(u) == 3, "u . u = 1 (peso impar)")
    require(gf_dot(_bits("11000"), _bits("11000")) == 0, "11000 es ortogonal a sí mismo")
    for x in itertools.product((0, 1), repeat=5):
        require(gf_dot(x, x) == weight(x) % 2, "x . x = w(x) mod 2")
    self_orth = {x for x in itertools.product((0, 1), repeat=3) if gf_dot(x, x) == 0}
    require(_words(self_orth) == {"000", "110", "101", "011"}, "autoortogonales de Z_2^3")


@check("U4.T08.E2", "Código dual de un código (5,2) y su intersección", page=PAGE)
def _():
    G = [_bits("10110"), _bits("01011")]
    H = [_bits("10100"), _bits("11010"), _bits("01001")]
    require(gf_rank(G) == 2 and gf_rank(H) == 3, "rangos de G y H")
    require(gf_matmul(H, [list(c) for c in zip(*G)]) == [[0, 0]] * 3, "H G^t = 0")
    C = gf_span(G)
    require(_words(C) == {"00000", "10110", "01011", "11101"}, "palabras del código")
    dual_basis = gf_nullspace(G)
    require(len(dual_basis) == 3, "dim C^perp = 5 - 2")
    dual = gf_span(dual_basis)
    require(dual == _dual(C, 5), "C^perp = nul(G)")
    require(dual == gf_span(H), "las filas de H generan C^perp")
    require(len(dual) == 8, "C^perp tiene 8 palabras")
    require(_dual(dual, 5) == C, "(C^perp)^perp = C")
    require(_words(C & dual) == {"00000", "11101"}, "C ∩ C^perp = {0, 11101}")


@check("U4.T08.E3", "Código de doble repetición de longitud 4: autodual", page=PAGE)
def _():
    G = [_bits("1100"), _bits("0011")]
    require(gf_matmul(G, [list(c) for c in zip(*G)]) == [[0, 0], [0, 0]], "G G^t = 0")
    require(gf_rank(G) == 2, "k = 2 = n/2")
    C = gf_span(G)
    require(_dual(C, 4) == C, "C^perp = C")
    require(all(weight(c) % 2 == 0 for c in C), "pesos pares")
    require((1, 1, 1, 1) in C, "1111 pertenece al código")


@check("U4.T08.E4", "Decodificación por síndrome de un código (5,2)", page=PAGE)
def _():
    G = [_bits("10110"), _bits("01011")]
    H = [_bits("10100"), _bits("11010"), _bits("01001")]
    C = gf_span(G)
    require(min_distance(C) == 3, "d(C) = 3")
    syndrome = lambda r: tuple(gf_dot(h, r) for h in H)
    # Tabla: líderes de peso mínimo para cada síndrome.
    table = {}
    for e in itertools.product((0, 1), repeat=5):
        table.setdefault(syndrome(e), []).append(e)
    leaders = {s: sorted(es, key=weight) for s, es in table.items()}
    for j in range(5):
        e = tuple(int(i == j) for i in range(5))
        require(weight(leaders[syndrome(e)][0]) == 1, "síndromes de peso 1 distintos")
    columns = {"".join(str(h[j]) for h in H) for j in range(5)}
    require(columns == {"110", "011", "100", "010", "001"}, "columnas de H")
    for s in [(1, 0, 1), (1, 1, 1)]:
        ws = [e for e in table[s] if weight(e) == 2]
        require(len(ws) == 2 and min(weight(e) for e in table[s]) == 2, "síndromes con dos líderes de peso 2")
    # Envío de a = (1, 1): c = aG = 11101; se recibe 11001.
    c = tuple((G[0][i] + G[1][i]) % 2 for i in range(5))
    require(_words([c]) == {"11101"}, "codificación")
    r = _bits("11001")
    require(syndrome(r) == (1, 0, 0), "síndrome = tercera columna")
    corrected = list(r)
    corrected[2] ^= 1
    require(tuple(corrected) == c, "corrección del bit 3")
    require(sorted(hamming(r, w) for w in C) == [1, 2, 3, 4], "vecino más cercano único")
    # 01110: síndrome 101, dos palabras a distancia 2.
    r2 = _bits("01110")
    require(syndrome(r2) == (1, 0, 1), "síndrome de 01110")
    require(sorted(hamming(r2, w) for w in C) == [2, 2, 3, 3], "empate: se detecta, no se corrige")


@check("U4.T08.E5", "El código de Hamming (7,4) tiene distancia mínima 3", page=PAGE)
def _():
    H = [_bits("0001111"), _bits("0110011"), _bits("1010101")]
    for j in range(7):
        column = int("".join(str(h[j]) for h in H), 2)
        require(column == j + 1, "la columna j es j en binario")
    G = [_bits("1110000"), _bits("1001100"), _bits("0101010"), _bits("1101001")]
    require(gf_matmul(H, [list(c) for c in zip(*G)]) == [[0] * 4] * 3, "H G^t = 0")
    require(gf_rank(G) == 4, "G tiene rango 4")
    C = gf_span(G)
    require(C == gf_span(gf_nullspace(H)), "C = nul(H)")
    require(len(C) == 16, "16 palabras")
    require(min_distance(C) == 3, "d = 3")
    require(sorted(weight(c) for c in C) == [0] + [3] * 7 + [4] * 7 + [7], "distribución de pesos")
    require(gf_matmul(H, [[1], [1], [1], [0], [0], [0], [0]]) == [[0], [0], [0]], "h1 + h2 + h3 = 0")


@check("U4.T08.E6", "Hamming extendido (8,4): autodual, d = 4, corrige 1 y detecta 2", page=PAGE)
def _():
    G7 = [_bits("1110000"), _bits("1001100"), _bits("0101010"), _bits("1101001")]
    G8 = [g + [weight(g) % 2] for g in G7]
    require(_words(G8) == {"11100001", "10011001", "01010101", "11010010"}, "G extendida")
    require(gf_matmul(G8, [list(c) for c in zip(*G8)]) == [[0] * 4] * 4, "G G^t = 0")
    require(gf_rank(G8) == 4, "k = 4 = n/2")
    C = gf_span(G8)
    require(_dual(C, 8) == C, "autodual")
    require(min_distance(C) == 4, "d = 4")
    require(sorted(weight(c) for c in C) == [0] + [4] * 14 + [8], "pesos")
    H8 = [_bits("00011110"), _bits("01100110"), _bits("10101010"), _bits("11111111")]
    require(all(tuple(h) in C for h in H8), "las filas de H8 están en el código (autodual)")
    syndrome = lambda r: tuple(gf_dot(h, r) for h in H8)
    a = [1, 0, 1, 1]
    c = [sum(a[i] * G8[i][j] for i in range(4)) % 2 for j in range(8)]
    require(_words([c]) == {"01100110"}, "codificación de 1011")
    require(syndrome(c) == (0, 0, 0, 0), "síndrome nulo")
    cases = {(5,): (1, 0, 1, 1), (2, 6): (1, 0, 0, 0), (8,): (0, 0, 0, 1)}
    for flips, expected in cases.items():
        r = list(c)
        for f in flips:
            r[f - 1] ^= 1
        require(syndrome(r) == expected, f"síndrome con errores en {flips}")
        require(hamming(r, c) == len(flips), "cantidad de errores")
