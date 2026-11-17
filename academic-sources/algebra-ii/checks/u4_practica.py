"""Comprobaciones de los ejercicios de la práctica de la Unidad 4 (espacios con producto interno).

Cada función recalcula los resultados publicados desde los datos del enunciado: positividad de
productos internos (criterio de los menores principales y contraejemplos), Gram-Schmidt, complementos
ortogonales (``nullspace``), proyecciones por tres métodos, distancias, ecuaciones normales y ajustes,
y las cuentas sobre Z_2 con aritmética modular exacta (``gf_*``, ``hamming``, ``weight``, ``min_distance``).
Las normas irracionales se comprueban a través de sus cuadrados y las medidas de ángulo por el coseno.
Convenciones: base canónica de P_2[R] ordenada {1, x, x^2}; de R^{2x2} ordenada {E11, E12, E21, E22};
el producto de la traza tr(B^t A) coincide con el usual de R^4 en esas coordenadas.
Los ejercicios demostrativos (U4.23, U4.24) tienen verificacion: razonamiento y no figuran acá.
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
PG = "/algebra-ii/unidad-4/practica/"
INI = PG + "nivel-inicial/"
INT = PG + "nivel-intermedio/"
AVA = PG + "nivel-avanzado/"
GUIA = PG + "guia-integradora/"


# ---------------------------------------------------------------------------
# Utilidades sobre R^n con producto <u, v> = u^t M v (M simétrica).
# ---------------------------------------------------------------------------
def col(*entries):
    """Vector columna."""
    return sp.Matrix(list(entries))


def ip(M, u, v):
    return (u.T * M * v)[0, 0]


def minors(M):
    return [M[:k, :k].det() for k in range(1, M.shape[0] + 1)]


def require_ip(M, what):
    """Simétrica con menores principales positivos (criterio de Sylvester)."""
    require(M == M.T, f"{what}: la matriz de Gram no es simétrica")
    require(all(m > 0 for m in minors(M)), f"{what}: algún menor principal no es positivo")


def gram_schmidt(vectors, M):
    ws = []
    for v in vectors:
        w = v
        for u in ws:
            w = w - (ip(M, v, u) / ip(M, u, u)) * u
        ws.append(w)
    return ws


def proj(v, orthogonal_basis, M):
    p = sp.zeros(v.shape[0], 1)
    for u in orthogonal_basis:
        p = p + (ip(M, v, u) / ip(M, u, u)) * u
    return p


def comp(generators, M):
    """Base de S^perp: x tal que (M s)^t x = 0 para cada generador s (M simétrica)."""
    A = sp.Matrix.vstack(*[(M * g).T for g in generators])
    return A.nullspace()


def same_span(first, second):
    a, b = sp.Matrix.hstack(*first), sp.Matrix.hstack(*second)
    return a.rank() == b.rank() == sp.Matrix.hstack(a, b).rank()


def normal_equations(columns, y):
    A = sp.Matrix.hstack(*columns)
    AtA, Aty = A.T * A, A.T * y
    x = AtA.inv() * Aty
    return A, AtA, Aty, x, y - A * x


def mat2(a, b, c, d):
    return sp.Matrix([[a, b], [c, d]])


def tr_ip(A, B):
    return (B.T * A).trace()


def vec4(A):
    """Coordenadas de una matriz 2x2 en {E11, E12, E21, E22}."""
    return col(A[0, 0], A[0, 1], A[1, 0], A[1, 1])


I3 = sp.eye(3)
I4 = sp.eye(4)


def eval_gram(nodes, weights=None):
    """Matriz de Gram en {1, x, x^2} del producto por evaluación en los nodos (con pesos)."""
    weights = weights or [1] * len(nodes)
    EV = sp.Matrix([[1, t, t * t] for t in nodes])
    return EV.T * sp.diag(*weights) * EV


# ---------------------------------------------------------------------------
# Nivel inicial
# ---------------------------------------------------------------------------
@check("U4.01", "Cinco fórmulas en R^2: cuáles son producto interno", page=INI)
def _():
    # a) diag(2,3)
    Ma = sp.diag(2, 3)
    require_ip(Ma, "a)")
    # b) x1 y1 - x2 y2
    Mb = sp.diag(1, -1)
    same(ip(Mb, col(0, 1), col(0, 1)), -1, "b) <(0,1),(0,1)>")
    # c) (x1 + x2)(y1 + y2)
    Mc = sp.Matrix([[1, 1], [1, 1]])
    same(Mc.det(), 0, "c) det")
    same(ip(Mc, col(1, -1), col(1, -1)), 0, "c) <(1,-1),(1,-1)>")
    # d) x1y1 + x1y2 + x2y1 + 3 x2y2 = (x1 + x2)^2 + 2 x2^2
    Md = sp.Matrix([[1, 1], [1, 3]])
    require_ip(Md, "d)")
    same(minors(Md), [1, 2], "d) menores")
    U = sp.Matrix([[1, 1], [0, 1]])
    same(U.T * sp.diag(1, 2) * U, Md, "d) completar cuadrados")
    same(ip(Md, col(1, -1), col(1, -1)), 2, "d) <(1,-1),(1,-1)>")
    # e) no simétrica
    Me = sp.Matrix([[1, 1], [2, 1]])
    require(Me != Me.T, "e) debería ser no simétrica")
    same(ip(Me, col(1, 0), col(0, 1)), 1, "e) <e1,e2>")
    same(ip(Me, col(0, 1), col(1, 0)), 2, "e) <e2,e1>")


@check("U4.02", "Norma, distancia y ángulo con el producto x1y1+x2y2+2x3y3", page=INI)
def _():
    M = sp.diag(1, 1, 2)
    require_ip(M, "M")
    u, v, w = col(1, 1, 1), col(1, -1, 1), col(2, 0, -1)
    same(ip(M, u, v), 2, "<u,v>")
    same(ip(M, u, u), 4, "||u||^2")
    same(ip(M, v, v), 4, "||v||^2")
    same(ip(M, u, v) / (2 * 2), R(1, 2), "cos")
    d = u - v
    same(d, col(0, 2, 0), "u - v")
    same(ip(M, d, d), 4, "d(u,v)^2")
    same(ip(M, u, w), 0, "<u,w> ponderado")
    same(ip(I3, u, w), 1, "u . w usual")
    same(ip(I3, u, v), 1, "u . v usual")
    same(ip(I3, u, u), 3, "||u||^2 usual")


@check("U4.03", "Producto de la traza en R^{2x2}: ortogonalidad, Pitágoras, coseno y parámetro", page=INI)
def _():
    A, B, C = mat2(1, 2, 2, 0), mat2(2, -1, 0, 2), mat2(1, 1, 1, 1)
    entrywise = lambda X, Y: sum(X[i, j] * Y[i, j] for i in range(2) for j in range(2))
    same(tr_ip(A, B), entrywise(A, B), "tr(B^t A) = suma entrada a entrada")
    same(tr_ip(A, B), 0, "<A,B>")
    same(tr_ip(A, A), 9, "||A||^2")
    same(tr_ip(B, B), 9, "||B||^2")
    same(tr_ip(A + B, A + B), 18, "||A+B||^2")
    same(A + B, mat2(3, 1, 2, 2), "A+B")
    same(tr_ip(A, C), 5, "<A,C>")
    same(tr_ip(C, C), 4, "||C||^2")
    same(R(5, 1) / (3 * 2), R(5, 6), "cos(A,C)")
    require(tr_ip(A, C) ** 2 <= tr_ip(A, A) * tr_ip(C, C), "Cauchy-Schwarz")
    t = sp.symbols("t")
    T = mat2(t, 1, 1, t)
    same(sp.expand(tr_ip(A, T)), t + 4, "<A,T_t>")
    same(tr_ip(A, mat2(-4, 1, 1, -4)), 0, "t = -4")


@check("U4.04", "Producto por evaluación en P_2 con nodos -1, 0, 1", page=INI)
def _():
    nodes = (-1, 0, 1)
    EV = sp.Matrix([[1, t, t * t] for t in nodes])
    G = EV.T * EV
    same(G, sp.Matrix([[3, 0, 2], [0, 2, 0], [2, 0, 2]]), "Gram")
    require_ip(G, "evaluación")
    same(EV.det(), 2, "det de evaluación (nodos distintos => inyectiva)")
    p, q = col(1, 1, 0), col(-1, 0, 1)  # 1 + x, x^2 - 1
    same(ip(G, p, q), -1, "<1+x, x^2-1>")
    same(ip(G, p, p), 5, "||1+x||^2")
    same(ip(G, col(0, 1, 0), col(0, 0, 1)), 0, "<x, x^2>")
    c = sp.symbols("c")
    same(sp.expand(ip(G, col(c, 0, 1), col(1, 0, 0))), 3 * c + 2, "<x^2 + c, 1>")
    same(ip(G, col(R(-2, 3), 0, 1), col(1, 0, 0)), 0, "c = -2/3")


@check("U4.05", "Coordenadas en una base ortogonal de R^3", page=INI)
def _():
    b1, b2, b3 = col(1, 1, 0), col(1, -1, 1), col(-1, 1, 2)
    B = sp.Matrix.hstack(b1, b2, b3)
    same(B.T * B, sp.diag(2, 3, 6), "Gram diagonal")
    require(B.det() != 0, "base")
    v = col(3, 1, 4)
    coords = [ip(I3, v, b) / ip(I3, b, b) for b in (b1, b2, b3)]
    same(sp.Matrix(coords), col(2, 2, 1), "coordenadas por la fórmula")
    same(B.inv() * v, col(2, 2, 1), "coordenadas por B^{-1}")
    same(2 * b1 + 2 * b2 + b3, v, "combinación")
    same(4 * 2 + 4 * 3 + 1 * 6, 26, "suma ponderada")
    same(ip(I3, v, v), 26, "||v||^2")


@check("U4.06", "Complemento ortogonal en R^4 y pertenencia de w", page=INI)
def _():
    g1, g2 = col(1, 1, 0, 1), col(0, 1, 1, -1)
    A = sp.Matrix.vstack(g1.T, g2.T)
    ns = A.nullspace()
    same(len(ns), 2, "dim S^perp")
    same(A.rank(), 2, "dim S")
    esperado = [col(1, -1, 1, 0), col(-2, 1, 0, 1)]
    require(same_span(ns, esperado), "S^perp = gen{(1,-1,1,0), (-2,1,0,1)}")
    for e in esperado:
        same(A * e, sp.zeros(2, 1), "ortogonal a los generadores")
    w = col(3, -2, 1, -1)
    same(A * w, sp.zeros(2, 1), "w en S^perp")
    same(esperado[0] - esperado[1], w, "w = b1 - b2")


@check("U4.07", "Proyección sobre un plano de R^3 con base ortogonal", page=INI)
def _():
    b1, b2 = col(1, 1, 0), col(1, -1, 1)
    same(ip(I3, b1, b2), 0, "ortogonales")
    v = col(3, 1, 4)
    p = proj(v, [b1, b2], I3)
    same(p, col(4, 0, 2), "proy_S(v)")
    r = v - p
    same(r, col(-1, 1, 2), "v - proy")
    same(ip(I3, r, b1), 0, "r perp b1")
    same(ip(I3, r, b2), 0, "r perp b2")
    same(ip(I3, r, r), 6, "d(v,S)^2")
    same(ip(I3, v, v), ip(I3, p, p) + ip(I3, r, r), "Pitágoras")
    # por ecuaciones normales con la misma base
    A, AtA, Aty, x, res = normal_equations([b1, b2], v)
    same(A * x, p, "ecuaciones normales")


@check("U4.08", "Producto punto en Z_2^n: ortogonalidad y conteo", page=INI)
def _():
    u, v = [1, 1, 0, 1, 0], [1, 0, 1, 1, 0]
    require(gf_dot(u, v) == 0, "u.v = 0")
    require(gf_dot(u, u) == 1, "u.u = 1")
    require(weight(u) % 2 == 1, "peso de u impar")
    # x . x = peso mod 2 para todo x de Z_2^5
    for x in itertools.product((0, 1), repeat=5):
        require(gf_dot(x, x) == weight(x) % 2, "x.x = w(x) mod 2")
    ortog = [x for x in itertools.product((0, 1), repeat=3) if gf_dot(x, (1, 1, 0)) == 0]
    require(sorted(ortog) == [(0, 0, 0), (0, 0, 1), (1, 1, 0), (1, 1, 1)], "ortogonales a (1,1,0)")
    cuenta = [x for x in itertools.product((0, 1), repeat=5) if gf_dot(x, u) == 0]
    require(len(cuenta) == 16, "16 vectores ortogonales a u")
    require(len(gf_nullspace([u])) == 4, "dim del subespacio ortogonal = 4")
    require(tuple(v) in cuenta, "v está entre ellos")


# ---------------------------------------------------------------------------
# Nivel intermedio
# ---------------------------------------------------------------------------
@check("U4.09", "Producto con parámetro k: positividad solo si |k| < 2", page=INT)
def _():
    k, x1, x2 = sp.symbols("k x1 x2")
    Mk = sp.Matrix([[1, k], [k, 4]])
    same(sp.expand(Mk.det()), 4 - k * k, "det M_k")
    # (x1 + k x2)^2 + (4 - k^2) x2^2 = x^t M_k x
    xk = col(x1, x2)
    lhs = sp.expand((xk.T * Mk * xk)[0, 0])
    rhs = sp.expand((x1 + k * x2) ** 2 + (4 - k * k) * x2 ** 2)
    same(lhs, rhs, "completar cuadrados")
    for kv in (0, 1, R(19, 10), -1, R(-19, 10)):
        require_ip(sp.Matrix([[1, kv], [kv, 4]]), f"k={kv}")
    for kv in (2, -2, 3, -3):
        require(sp.Matrix([[1, kv], [kv, 4]]).det() <= 0, f"k={kv} no es definida positiva")
    M1 = sp.Matrix([[1, 1], [1, 4]])
    same(ip(M1, col(2, -1), col(2, -1)), 4, "||(2,-1)||^2 con k=1")
    same(ip(M1, col(1, 0), col(0, 1)), 1, "<e1,e2>")
    same(ip(M1, col(1, 0), col(1, 0)), 1, "||e1||^2")
    same(ip(M1, col(0, 1), col(0, 1)), 4, "||e2||^2")
    same(R(1, 1) / (1 * 2), R(1, 2), "cos = 1/2")
    M2 = sp.Matrix([[1, 2], [2, 4]])
    same(ip(M2, col(2, -1), col(2, -1)), 0, "k=2: norma cero")
    M3 = sp.Matrix([[1, 3], [3, 4]])
    same(ip(M3, col(3, -1), col(3, -1)), -5, "k=3: negativa")


@check("U4.10", "Verdadero/falso: cuatro afirmaciones sobre ortogonalidad", page=INT)
def _():
    # a) simbólico: <u, alpha v + beta w> = alpha <u,v> + beta <u,w> en R^3
    u = col(*sp.symbols("u1 u2 u3"))
    v = col(*sp.symbols("v1 v2 v3"))
    w = col(*sp.symbols("w1 w2 w3"))
    al, be = sp.symbols("alpha beta")
    same(sp.expand(ip(I3, u, al * v + be * w) - al * ip(I3, u, v) - be * ip(I3, u, w)), 0, "linealidad")
    # b) contraejemplo
    u0, v0, w0 = col(1, 1), col(1, 0), col(0, 1)
    same(ip(sp.eye(2), u0, v0), ip(sp.eye(2), u0, w0), "<u,v> = <u,w>")
    require(v0 != w0, "v != w")
    same(ip(sp.eye(2), u0, v0 - w0), 0, "u perp (v-w)")
    # c) cuatro vectores de R^3 son LD; tres ortogonales no nulos son LI
    cuatro = sp.Matrix.hstack(col(1, 0, 0), col(0, 1, 0), col(0, 0, 1), col(1, 1, 1))
    require(cuatro.rank() <= 3, "cuatro vectores de R^3 son LD")
    cuatro_gen = sp.Matrix(3, 4, list(sp.symbols("a0:12")))
    require(cuatro_gen.rank() <= 3, "rango a lo sumo 3 en general")
    # d) simbólico en R^3: <u+v, u-v> = |u|^2 - |v|^2
    same(sp.expand(ip(I3, u + v, u - v) - (ip(I3, u, u) - ip(I3, v, v))), 0, "identidad")
    p, q = col(1, 2), col(2, 1)
    same(ip(sp.eye(2), p, p), ip(sp.eye(2), q, q), "misma norma")
    same(ip(sp.eye(2), p + q, p - q), 0, "(u+v) perp (u-v)")


@check("U4.11", "Gram-Schmidt en R^3 usual", page=INT)
def _():
    B = [col(1, 2, 2), col(1, 1, 0), col(0, 1, 1)]
    ws = gram_schmidt(B, I3)
    same(ws[0], col(1, 2, 2), "w1")
    same(ws[1], col(R(2, 3), R(1, 3), R(-2, 3)), "w2")
    same(ws[2], col(R(-2, 9), R(2, 9), R(-1, 9)), "w3")
    same(ws[1] * 3, col(2, 1, -2), "w2 escalado")
    same(ws[2] * (-9), col(2, -2, 1), "w3 escalado")
    Bp = [col(1, 2, 2), col(2, 1, -2), col(2, -2, 1)]
    Q = sp.Matrix.hstack(*Bp)
    same(Q.T * Q, 9 * I3, "ortogonal con normas 3")
    same((Q / 3).T * (Q / 3), I3, "ortonormal")
    require(same_span(B[:2], Bp[:2]) and same_span(B, Bp), "mismos subespacios")
    v = col(3, 0, 3)
    same(sp.Matrix([ip(I3, v, b) / 9 for b in Bp]), col(1, 0, 1), "coordenadas")
    same(Q * col(1, 0, 1), v, "reconstrucción")


@check("U4.12", "Gram-Schmidt en P_2 con evaluación en 0, 1, 2", page=INT)
def _():
    G = eval_gram((0, 1, 2))
    same(G, sp.Matrix([[3, 3, 5], [3, 5, 9], [5, 9, 17]]), "Gram")
    require_ip(G, "evaluación en 0,1,2")
    E = [col(1, 0, 0), col(0, 1, 0), col(0, 0, 1)]
    ws = gram_schmidt(E, G)
    same(ws[0], col(1, 0, 0), "w1 = 1")
    same(ws[1], col(-1, 1, 0), "w2 = x - 1")
    same(ws[2], col(R(1, 3), -2, 1), "w3 = x^2 - 2x + 1/3")
    same(ip(G, ws[0], ws[0]), 3, "||1||^2")
    same(ip(G, ws[1], ws[1]), 2, "||x-1||^2")
    same(ip(G, ws[2], ws[2]), R(2, 3), "||w3||^2")
    w3 = col(1, -6, 3)  # 3x^2 - 6x + 1
    same(ip(G, w3, w3), 6, "||3x^2-6x+1||^2")
    same(ip(G, ws[0], w3), 0, "1 perp w3")
    same(ip(G, ws[1], w3), 0, "x-1 perp w3")
    same(ip(G, ws[0], ws[1]), 0, "1 perp x-1")
    same(ip(G, col(0, 1, 0), col(1, 0, 0)), 3, "<x,1>")
    same(ip(G, col(0, 0, 1), col(1, 0, 0)), 5, "<x^2,1>")
    same(ip(G, col(0, 0, 1), ws[1]), 4, "<x^2,x-1>")


@check("U4.13", "Complemento ortogonal en R^{2x2} con la traza", page=INT)
def _():
    G1, G2 = mat2(1, 1, 0, 1), mat2(0, 1, 1, 0)
    A = sp.Matrix.vstack(vec4(G1).T, vec4(G2).T)
    ns = A.nullspace()
    same(A.rank(), 2, "dim S")
    same(len(ns), 2, "dim S^perp")
    B1, B2 = mat2(-1, 1, -1, 0), mat2(-1, 0, 0, 1)
    require(same_span(ns, [vec4(B1), vec4(B2)]), "S^perp = gen{B1, B2}")
    for B in (B1, B2):
        same(tr_ip(B, G1), 0, "perp G1")
        same(tr_ip(B, G2), 0, "perp G2")
    M = mat2(-2, 1, -1, 1)
    same(tr_ip(M, G1), 0, "M perp G1")
    same(tr_ip(M, G2), 0, "M perp G2")
    same(B1 + B2, M, "M = B1 + B2")
    same(tr_ip(sp.eye(2), G1), 2, "<I, G1>")


@check("U4.14", "Complemento con un producto ponderado y con el usual", page=INT)
def _():
    W = sp.diag(1, 2, 3)
    require_ip(W, "ponderado")
    S = [col(1, 0, 1), col(0, 1, 1)]
    ns = comp(S, W)
    same(len(ns), 1, "dim S^perp (ponderado)")
    require(same_span(ns, [col(-6, -3, 2)]), "S^perp = gen{(-6,-3,2)}")
    same(ip(W, col(-6, -3, 2), S[0]), 0, "perp s1")
    same(ip(W, col(-6, -3, 2), S[1]), 0, "perp s2")
    nu = comp(S, I3)
    same(len(nu), 1, "dim S^perp (usual)")
    require(same_span(nu, [col(1, 1, -1)]), "S^perp usual = gen{(1,1,-1)}")
    require(not same_span(ns, nu), "los complementos son distintos")
    same(sp.Matrix.hstack(*S).rank() + len(ns), 3, "dim S + dim S^perp")


@check("U4.15", "Proyección sobre x + y - 2z = 0 por tres métodos", page=INT)
def _():
    n = col(1, 1, -2)
    v = col(4, 2, 0)
    b1, b2 = col(1, -1, 0), col(1, 1, 1)
    for b in (b1, b2):
        same(ip(I3, n, b), 0, "base en S")
    same(ip(I3, b1, b2), 0, "ortogonales")
    # a) base ortogonal
    pa = proj(v, [b1, b2], I3)
    same(pa, col(3, 1, 2), "método a")
    # b) vía S^perp
    pn = proj(v, [n], I3)
    same(pn, col(1, 1, -2), "proy sobre S^perp")
    pb = v - pn
    same(pb, col(3, 1, 2), "método b")
    same(ip(I3, pn, pn), 6, "d(v,S)^2")
    # c) ecuaciones normales con {(1,-1,0), (2,0,1)}
    a1, a2 = col(1, -1, 0), col(2, 0, 1)
    same(ip(I3, n, a2), 0, "(2,0,1) en S")
    A = sp.Matrix.hstack(a1, a2)
    AtA, Aty = A.T * A, A.T * v
    same(AtA, sp.Matrix([[2, 2], [2, 5]]), "A^t A")
    same(Aty, col(2, 8), "A^t v")
    same(AtA.det(), 6, "det A^t A")
    x = AtA.inv() * Aty
    same(x, col(-1, 2), "solución normal")
    same(A * x, col(3, 1, 2), "método c")
    same(ip(I3, col(3, 1, 2), n), 0, "proy en S")


@check("U4.16", "Tres contraejemplos: fórmula sin base ortogonal, complemento y transitividad", page=INT)
def _():
    # a) base {(1,0),(1,1)} de R^2 no ortogonal
    b1, b2 = col(1, 0), col(1, 1)
    I2 = sp.eye(2)
    require(ip(I2, b1, b2) != 0, "base no ortogonal")
    v = col(0, 1)
    falsa = proj(v, [b1, b2], I2)
    same(falsa, col(R(1, 2), R(1, 2)), "la fórmula da (1/2, 1/2)")
    require(falsa != v, "la fórmula no devuelve v, que está en S = R^2")
    # b) complemento depende del producto
    M = sp.Matrix([[2, 1, 0], [1, 2, 0], [0, 0, 3]])
    require_ip(M, "M")
    same(minors(M), [2, 3, 9], "menores")
    S = [col(1, 0, 1), col(1, 1, 0)]
    nM = comp(S, M)
    nU = comp(S, I3)
    require(len(nM) == 1 and len(nU) == 1, "rectas")
    require(same_span(nM, [col(-3, 3, 1)]), "S^perp_M = gen{(-3,3,1)}")
    require(same_span(nU, [col(1, -1, -1)]), "S^perp usual = gen{(1,-1,-1)}")
    same(M * S[0], col(2, 1, 3), "M s1")
    same(M * S[1], col(3, 3, 0), "M s2")
    same(ip(M, col(-3, 3, 1), S[0]), 0, "(-3,3,1) perp s1")
    same(ip(M, col(-3, 3, 1), S[1]), 0, "(-3,3,1) perp s2")
    same(ip(M, col(1, -1, -1), S[0]), -2, "(1,-1,-1) no es perp con M")
    # c) ortogonalidad no transitiva
    u, vv, w = col(1, 0, 0), col(0, 1, 0), col(2, 0, 1)
    same(ip(I3, u, vv), 0, "u perp v")
    same(ip(I3, vv, w), 0, "v perp w")
    same(ip(I3, u, w), 2, "u no perp w")


@check("U4.17", "Recta de cuadrados mínimos con tiempos de respuesta", page=INT)
def _():
    n = [1, 2, 3, 4, 5]
    y = col(3, 8, 10, 14, 15)
    A, AtA, Aty, x, res = normal_equations([col(1, 1, 1, 1, 1), col(*n)], y)
    same(AtA, sp.Matrix([[5, 15], [15, 55]]), "A^t A")
    same(Aty, col(50, 180), "A^t b")
    same(x, col(1, 3), "recta t = 1 + 3n")
    same(A * x, col(4, 7, 10, 13, 16), "valores ajustados")
    same(res, col(-1, 1, 0, 1, -1), "residuos")
    same(A.T * res, sp.zeros(2, 1), "residuo perp col(A)")
    same(ip(I3 if False else sp.eye(5), res, res), 4, "error cuadrático")
    same(x[0] + x[1] * 8, 25, "predicción n = 8")
    same(sp.Matrix([[5, 15], [15, 55]]) * col(1, 3), col(50, 180), "ecuaciones normales")


@check("U4.18", "Similitud coseno entre una consulta y tres documentos", page=INT)
def _():
    I = sp.eye(4)
    q, d1, d2, d3 = col(2, 2, 1, 0), col(2, 1, 2, 0), col(0, 1, 2, 2), col(4, 4, 2, 0)
    same(ip(I, q, q), 9, "|q|^2")
    same(ip(I, d1, d1), 9, "|D1|^2")
    same(ip(I, d2, d2), 9, "|D2|^2")
    same(ip(I, d3, d3), 36, "|D3|^2")
    same(ip(I, q, d1), 8, "q.D1")
    same(ip(I, q, d2), 4, "q.D2")
    same(ip(I, q, d3), 18, "q.D3")
    same(R(8, 1) / (3 * 3), R(8, 9), "cos D1")
    same(R(4, 1) / (3 * 3), R(4, 9), "cos D2")
    same(R(18, 1) / (3 * 6), 1, "cos D3")
    same(d3, 2 * q, "D3 = 2q")
    for dd, cuad in ((d1, 2), (d2, 10), (d3, 9)):
        same(ip(I, q - dd, q - dd), cuad, "distancia al cuadrado")
    require(ip(I, q, d1) ** 2 <= ip(I, q, q) * ip(I, d1, d1), "Cauchy-Schwarz D1")
    require(ip(I, q, d3) ** 2 == ip(I, q, q) * ip(I, d3, d3), "igualdad en C-S para D3")


@check("U4.19", "Dual de un código (5,2) en Z_2^5", page=INT)
def _():
    G = [[1, 0, 1, 1, 0], [0, 1, 0, 1, 1]]
    C = gf_span(G)
    require(C == {(0, 0, 0, 0, 0), (1, 0, 1, 1, 0), (0, 1, 0, 1, 1), (1, 1, 1, 0, 1)}, "palabras")
    require(min_distance(C) == 3, "d(C) = 3")
    require(gf_rank(G) == 2, "dim C = 2")
    dual_basis = gf_nullspace(G)
    require(len(dual_basis) == 3, "dim C^perp = 3")
    publicada = [[1, 0, 1, 0, 0], [1, 1, 0, 1, 0], [0, 1, 0, 0, 1]]
    require(gf_rank(publicada) == 3, "base publicada independiente")
    require(gf_span(publicada) == gf_span(dual_basis), "mismo subespacio que gf_nullspace")
    for b in publicada:
        for g in G:
            require(gf_dot(b, g) == 0, "ortogonal a los generadores")
    dual = gf_span(publicada)
    todos = {x for x in itertools.product((0, 1), repeat=5) if all(gf_dot(x, g) == 0 for g in G)}
    require(dual == todos, "dual = todos los ortogonales")
    require(gf_dot(G[0], G[0]) == 1, "g1.g1 = 1")
    require(not C <= dual, "C no está contenido en su dual")
    require(len(C) != len(dual), "no es autodual")


@check("U4.20", "Código (7,3): distancia mínima, detección y corrección", page=INT)
def _():
    G = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]]
    C = gf_span(G)
    s = lambda t: "".join(map(str, t))
    esperadas = {"0000000", "1010101", "0110011", "0001111", "1100110", "1011010", "0111100", "1101001"}
    require({s(c) for c in C} == esperadas, "las 8 palabras publicadas")
    d = min_distance(C)
    require(d == 4, "d(C) = 4")
    require(all(weight(c) == 4 for c in C if any(c)), "las siete no nulas pesan 4")
    for a in C:
        for b in C:
            if a != b:
                require(hamming(a, b) >= 4, "distancia entre palabras >= 4")
    require(d - 1 == 3 and (d - 1) // 2 == 1, "detecta 3, corrige 1")
    r = (1, 1, 1, 0, 0, 1, 1)
    dist = sorted((hamming(r, c), s(c)) for c in C)
    require(dist[0] == (1, "0110011") and dist[1][0] == 3, "r se decodifica como 0110011")
    r2 = (1, 0, 0, 1, 1, 0, 1)
    require(r2 not in C, "r' no es palabra")
    dist2 = sorted((hamming(r2, c), s(c)) for c in C)
    require([x[0] for x in dist2].count(2) == 3, "tres palabras a distancia 2")
    require(min(x[0] for x in dist2) == 2 and all(x[0] > 2 for x in dist2 if x[1] not in {"0001111", "1010101", "1101001"}), "las otras, mayor")
    require({x[1] for x in dist2 if x[0] == 2} == {"0001111", "1010101", "1101001"}, "las tres palabras más cercanas")


# ---------------------------------------------------------------------------
# Nivel avanzado
# ---------------------------------------------------------------------------
@check("U4.21", "Verdadero/falso: S ∩ S^perp, Z_2, proyección y norma", page=AVA)
def _():
    # a) en R^3 usual: S ∩ S^perp = 0 (rango de la unión de bases)
    S = [col(1, 2, 0), col(0, 1, 1)]
    Sp = comp(S, I3)
    same(len(Sp), 1, "dim S^perp")
    same(sp.Matrix.hstack(*S, *Sp).rank(), 3, "S y S^perp son independientes y suman R^3")
    # b) Z_2^2: S = gen{11} está contenido en su ortogonal
    require(gf_dot((1, 1), (1, 1)) == 0, "11 . 11 = 0")
    perp = {x for x in itertools.product((0, 1), repeat=2) if gf_dot(x, (1, 1)) == 0}
    require(perp == gf_span([[1, 1]]), "S^perp = S")
    # c) misma proyección, vectores distintos
    s = col(1, 0)
    v, w = col(1, 1), col(1, 2)
    same(proj(v, [s], sp.eye(2)), col(1, 0), "proy v")
    same(proj(w, [s], sp.eye(2)), col(1, 0), "proy w")
    require(v != w, "v != w")
    # d) |proy| <= |v|
    p = proj(v, [s], sp.eye(2))
    same(ip(sp.eye(2), p, p), 1, "|proy|^2")
    same(ip(sp.eye(2), v, v), 2, "|v|^2")
    same(ip(sp.eye(2), v, v), ip(sp.eye(2), p, p) + ip(sp.eye(2), v - p, v - p), "Pitágoras")


@check("U4.22", "Contraejemplos: evaluación en dos nodos, diagonal positiva, ortogonalidad", page=AVA)
def _():
    # a) nodos 0 y 1 en P_2
    G2 = eval_gram((0, 1))
    p = col(0, -1, 1)  # x^2 - x
    same(ip(G2, p, p), 0, "|x^2 - x|^2 = 0")
    require(p != sp.zeros(3, 1), "p != 0")
    same(G2.det(), 0, "Gram singular")
    # b) simétrica con diagonal positiva y det < 0
    M = sp.Matrix([[1, 2], [2, 1]])
    same(M.det(), -3, "det M")
    same(ip(M, col(1, -1), col(1, -1)), -2, "x^t M x")
    # c) (1,1) perp (1,-1) usual, no para diag(1,2)
    D = sp.diag(1, 2)
    require_ip(D, "diag(1,2)")
    same(ip(sp.eye(2), col(1, 1), col(1, -1)), 0, "usual")
    same(ip(D, col(1, 1), col(1, -1)), -1, "ponderado")


@check("U4.25", "Mejor aproximación de x^2 en P_1 con evaluación en 0, 1, 2", page=AVA)
def _():
    G = eval_gram((0, 1, 2))
    one, xm1, q = col(1, 0, 0), col(-1, 1, 0), col(0, 0, 1)
    same(ip(G, one, xm1), 0, "base ortogonal de P_1")
    same(ip(G, one, one), 3, "|1|^2")
    same(ip(G, xm1, xm1), 2, "|x-1|^2")
    same(ip(G, q, one), 5, "<x^2,1>")
    same(ip(G, q, xm1), 4, "<x^2,x-1>")
    p = proj(q, [one, xm1], G)
    same(p, col(R(-1, 3), 2, 0), "proy = 2x - 1/3")
    r = q - p
    same(ip(G, r, r), R(2, 3), "d^2 = 2/3")
    same(ip(G, r, one), 0, "resto perp 1")
    same(ip(G, r, xm1), 0, "resto perp x-1")
    # equivalencia con cuadrados mínimos sobre los puntos (0,0), (1,1), (2,4)
    A, AtA, Aty, x, res = normal_equations([col(1, 1, 1), col(0, 1, 2)], col(0, 1, 4))
    same(AtA, sp.Matrix([[3, 3], [3, 5]]), "A^t A")
    same(Aty, col(5, 9), "A^t y")
    same(x, col(R(-1, 3), 2), "recta de cuadrados mínimos")
    same((res.T * res)[0, 0], R(2, 3), "error cuadrático")
    # otro candidato (el polinomio x) tiene error 4
    cand = col(0, 1, 2)
    same(((col(0, 1, 4) - cand).T * (col(0, 1, 4) - cand))[0, 0], 4, "error de x")


@check("U4.26", "Parábola y recta de cuadrados mínimos para el tiempo de un algoritmo", page=AVA)
def _():
    n = [1, 2, 3, 4, 5]
    t = col(3, 10, 14, 20, 33)
    ones = col(1, 1, 1, 1, 1)
    n1 = col(*n)
    n2 = col(*[k * k for k in n])
    A, AtA, Aty, x, res = normal_equations([ones, n1, n2], t)
    same(AtA, sp.Matrix([[5, 15, 55], [15, 55, 225], [55, 225, 979]]), "A^t A")
    same(Aty, col(80, 310, 1314), "A^t t")
    same(x, col(2, 1, 1), "parábola 2 + n + n^2")
    same(A * x, col(4, 8, 14, 22, 32), "valores ajustados")
    same(res, col(-1, 2, 0, -2, 1), "residuos parábola")
    same((res.T * res)[0, 0], 10, "error parábola")
    same(A.T * res, sp.zeros(3, 1), "residuo perp col(A)")
    Al, AtAl, Atl, xl, resl = normal_equations([ones, n1], t)
    same(xl, col(-5, 7), "recta -5 + 7n")
    same(resl, col(1, 1, -2, -3, 3), "residuos recta")
    same((resl.T * resl)[0, 0], 24, "error recta")
    same(x[0] + 6 * x[1] + 36 * x[2], 44, "parábola en n = 6")
    same(xl[0] + 6 * xl[1], 37, "recta en n = 6")


@check("U4.27", "Código (6,3) por matriz de control: G, distancia y síndromes", page=AVA)
def _():
    H = [[1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1]]
    require(gf_rank(H) == 3, "rango de H")
    G = [[1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 1]]
    require(gf_matmul(H, [list(g) for g in zip(*G)]) == [[0] * 3 for _ in range(3)], "H G^t = 0")
    require(gf_rank(G) == 3, "dim C = 3")
    require(gf_span(G) == gf_span(gf_nullspace(H)), "gen(G) = nul(H)")
    C = gf_span(G)
    require(len(C) == 8, "8 palabras")
    require(min_distance(C) == 3, "d(C) = 3")
    require((1, 1, 1, 0, 0, 0) in C, "111000 en C")
    cols = [tuple(H[i][j] for i in range(3)) for j in range(6)]
    require(len(set(cols)) == 6 and all(any(c) for c in cols), "columnas no nulas y distintas")
    suma = tuple(sum(cols[j][i] for j in range(3)) % 2 for i in range(3))
    require(suma == (0, 0, 0), "h1 + h2 + h3 = 0")
    syndrome = lambda r: tuple(row[0] for row in gf_matmul(H, [[x] for x in r]))
    r = (1, 0, 1, 1, 1, 0)
    require(syndrome(r) == (0, 1, 1) == cols[2], "síndrome de r = columna 3")
    corregida = tuple((x + (1 if i == 2 else 0)) % 2 for i, x in enumerate(r))
    require(corregida == (1, 0, 0, 1, 1, 0) and corregida in C, "corrección a 100110")
    require(syndrome(corregida) == (0, 0, 0), "síndrome nulo")
    c = (1, 0, 0, 1, 1, 0)
    r2 = (0, 1, 0, 1, 1, 0)
    require(hamming(c, r2) == 2, "dos errores")
    require(syndrome(r2) == (0, 1, 1) == cols[2], "mismo síndrome (columna 3)")
    mal = tuple((x + (1 if i == 2 else 0)) % 2 for i, x in enumerate(r2))
    require(mal == (0, 1, 1, 1, 1, 0) and mal in C and mal != c, "decodifica otra palabra")
    require(gf_rank([list(h) for h in zip(*[cols[i] for i in range(6)])]) == 3, "rango por columnas")


# ---------------------------------------------------------------------------
# Guía integradora
# ---------------------------------------------------------------------------
@check("U4.28", "Producto x^t M y en R^3: Gram-Schmidt, complemento, proyección", page=GUIA)
def _():
    M = sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
    require_ip(M, "M")
    same(minors(M), [2, 3, 4], "menores principales")
    u, v = col(1, 0, 1), col(0, 1, 0)
    same(M * u, col(2, 2, 2), "M u")
    same(ip(M, u, v), 2, "<u,v>")
    same(ip(M, u, u), 4, "|u|^2")
    same(ip(M, v, v), 2, "|v|^2")
    same(ip(M, u, v) ** 2, R(1, 2) * ip(M, u, u) * ip(M, v, v), "cos^2 = 1/2 (cos > 0, ángulo pi/4)")
    require(ip(M, u, v) > 0, "cos > 0")
    e1, e2, e3 = col(1, 0, 0), col(0, 1, 0), col(0, 0, 1)
    ws = gram_schmidt([e1, e2], M)
    same(ws[1], col(R(-1, 2), 1, 0), "w2")
    w2 = col(-1, 2, 0)
    same(M * w2, col(0, 3, 2), "M w2'")
    same(ip(M, w2, w2), 6, "|w2'|^2")
    same(ip(M, e1, w2), 0, "ortogonales")
    n = col(1, -2, 3)
    ns = comp([e1, e2], M)
    require(len(ns) == 1 and same_span(ns, [n]), "S^perp = gen{(1,-2,3)}")
    same(M * n, col(0, 0, 4), "M n")
    same(ip(M, n, n), 12, "|n|^2")
    w = col(2, 1, 3)
    same(ip(M, w, n), 12, "<w,n>")
    pS = w - proj(w, [n], M)
    same(pS, col(1, 3, 0), "proy_S(w)")
    same(proj(w, [e1, w2], M), col(1, 3, 0), "proy_S(w) con la base ortogonal")
    same(ip(M, w - pS, w - pS), 12, "d(w,S)^2")


@check("U4.29", "Subespacio de matrices con la traza: Gram-Schmidt, complemento, proyección", page=GUIA)
def _():
    B1, B2 = mat2(1, 1, 0, 1), mat2(1, 2, 1, 0)
    A = mat2(1, 3, 2, 2)
    b1, b2 = vec4(B1), vec4(B2)
    ws = gram_schmidt([b1, b2], I4)
    same(ws[0], b1, "w1")
    same(ws[1], vec4(mat2(0, 1, 1, -1)), "w2 = B2 - B1")
    same(ip(I4, ws[0], ws[0]), 3, "|w1|^2")
    same(ip(I4, ws[1], ws[1]), 3, "|w2|^2")
    same(tr_ip(B2, B1), 3, "<B2,B1>")
    ns = comp([b1, b2], I4)
    same(len(ns), 2, "dim S^perp")
    P1, P2 = mat2(-1, 1, -1, 0), mat2(-1, 0, 1, 1)
    require(same_span(ns, [vec4(P1), vec4(P2)]), "base publicada de S^perp")
    for P in (P1, P2):
        same(tr_ip(P, B1), 0, "perp B1")
        same(tr_ip(P, B2), 0, "perp B2")
    a = vec4(A)
    p = proj(a, ws, I4)
    same(p, vec4(mat2(2, 3, 1, 1)), "proy_S(A)")
    same(B1 + B2, mat2(2, 3, 1, 1), "B1 + B2")
    r = a - p
    same(r, vec4(P2), "resto = segundo vector de la base de S^perp")
    same(ip(I4, r, r), 3, "d(A,S)^2")
    same(ip(I4, a, a), 18, "|A|^2")
    same(ip(I4, p, p), 15, "|proy|^2")
    same(ip(I4, a, a), ip(I4, p, p) + ip(I4, r, r), "Pitágoras")


@check("U4.30", "Producto por evaluación con parámetro a: positividad, Gram-Schmidt, aproximación", page=GUIA)
def _():
    a = sp.symbols("a")
    # a) <p,p>_a = p(-1)^2 + 2 p(0)^2 + a p(1)^2; contraejemplo p = x^2 + x (coords 0,1,1)
    Ga = eval_gram((-1, 0, 1), (1, 2, a))
    p = col(0, 1, 1)
    same(sp.expand(ip(Ga, p, p)), 4 * a, "<x^2+x, x^2+x>_a = 4a")
    for av in (R(1, 2), 1, 3):
        require_ip(eval_gram((-1, 0, 1), (1, 2, av)), f"a={av}")
    for av in (0, -1):
        G0 = eval_gram((-1, 0, 1), (1, 2, av))
        require(ip(G0, p, p) <= 0, f"a={av}: <p,p> <= 0")
    # b) a = 1
    G = eval_gram((-1, 0, 1), (1, 2, 1))
    same(G, sp.Matrix([[4, 0, 2], [0, 2, 0], [2, 0, 2]]), "Gram a=1")
    require_ip(G, "a=1")
    E = [col(1, 0, 0), col(0, 1, 0), col(0, 0, 1)]
    ws = gram_schmidt(E, G)
    same(ws[0], col(1, 0, 0), "w1")
    same(ws[1], col(0, 1, 0), "w2")
    same(ws[2], col(R(-1, 2), 0, 1), "w3 = x^2 - 1/2")
    same(sp.Matrix([ip(G, w, w) for w in ws]), col(4, 2, 1), "normas^2")
    # c) q = 2x^2 + x
    q = col(0, 1, 2)
    pq = proj(q, [ws[0], ws[1]], G)
    same(pq, col(1, 1, 0), "proy = 1 + x")
    r = q - pq
    same(r, col(-1, 0, 2), "resto = 2x^2 - 1")
    same(ip(G, r, r), 4, "d^2 = 4")
    same(ip(G, r, ws[0]), 0, "resto perp 1")
    same(ip(G, r, ws[1]), 0, "resto perp x")
    # d) a = 3
    G3 = eval_gram((-1, 0, 1), (1, 2, 3))
    c = sp.symbols("c")
    same(sp.expand(ip(G3, col(c, 0, 1), col(1, 0, 0))), 4 + 6 * c, "<x^2 + c, 1>_3")
    same(ip(G3, col(R(-2, 3), 0, 1), col(1, 0, 0)), 0, "c = -2/3")


@check("U4.31", "Recta y parábola de cuadrados mínimos con variable centrada; A^t A inversible", page=GUIA)
def _():
    x = [-2, -1, 0, 1, 2]
    y = col(10, 4, 7, 14, 20)
    ones, x1, x2 = col(1, 1, 1, 1, 1), col(*x), col(*[k * k for k in x])
    A, AtA, Aty, sol, res = normal_equations([ones, x1], y)
    same(AtA, sp.Matrix([[5, 0], [0, 10]]), "A^t A recta")
    same(Aty, col(55, 30), "A^t y recta")
    same(sol, col(11, 3), "recta 11 + 3x")
    same(res, col(5, -4, -4, 0, 3), "residuos recta")
    same((res.T * res)[0, 0], 66, "error recta")
    Ap, AtAp, Atyp, solp, resp = normal_equations([ones, x1, x2], y)
    same(AtAp, sp.Matrix([[5, 0, 10], [0, 10, 0], [10, 0, 34]]), "A^t A parábola")
    same(Atyp, col(55, 30, 138), "A^t y parábola")
    same(solp, col(7, 3, 2), "parábola 7 + 3x + 2x^2")
    same(resp, col(1, -2, 0, 2, -1), "residuos parábola")
    same((resp.T * resp)[0, 0], 10, "error parábola")
    same(Ap.T * resp, sp.zeros(3, 1), "residuo perp col(A)")
    same(solp[0] + 3 * solp[1] + 9 * solp[2], 34, "parábola en x = 3")
    same(sol[0] + 3 * sol[1], 20, "recta en x = 3")
    # e) columnas LI => A^t A inversible; con columnas LD no lo es
    require(A.rank() == 2 and AtA.det() != 0, "caso LI")
    B = sp.Matrix.hstack(ones, 2 * ones)
    same((B.T * B).det(), 0, "caso LD: A^t A singular")


@check("U4.32", "Código autodual (6,3), subcódigo (6,2), dual y decodificación", page=GUIA)
def _():
    G = [[1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1]]
    C = gf_span(G)
    require(gf_rank(G) == 3, "dim C = 3")
    for a in G:
        for b in G:
            require(gf_dot(a, b) == 0, "generadores mutuamente ortogonales")
    dual = {x for x in itertools.product((0, 1), repeat=6) if all(gf_dot(x, g) == 0 for g in G)}
    require(dual == C, "C autodual")
    require(len(gf_nullspace(G)) == 3, "dim C^perp = 3")
    require(min_distance(C) == 2, "d(C) = 2")
    require((2 - 1, (2 - 1) // 2) == (1, 0), "detecta 1, corrige 0")
    G2 = [[1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1]]
    C2 = gf_span(G2)
    require(C2 <= C, "C2 contenido en C")
    require(C2 == {(0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 0, 0), (0, 0, 1, 1, 1, 1), (1, 1, 0, 0, 1, 1)}, "palabras de C2")
    base = [[1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1]]
    require(gf_rank(base) == 4, "base independiente")
    for b in base:
        for g in G2:
            require(gf_dot(b, g) == 0, "ortogonal a los generadores de C2")
    require(len(gf_nullspace(G2)) == 4, "dim C2^perp = 4")
    require(gf_span(base) == gf_span(gf_nullspace(G2)), "mismo subespacio que gf_nullspace")
    require(C <= gf_span(base), "C contenido en C2^perp")
    require(min_distance(C2) == 4, "d(C2) = 4")
    r1, r2 = (1, 0, 1, 1, 0, 0), (1, 0, 0, 1, 0, 0)
    d1 = sorted((hamming(r1, c), c) for c in C2)
    require([d for d, _ in d1] == [1, 3, 3, 5] and d1[0][1] == (1, 1, 1, 1, 0, 0), "r1 se decodifica a 111100")
    d2 = sorted(hamming(r2, c) for c in C2)
    require(d2 == [2, 2, 4, 4], "r2 empata a distancia 2")
