"""Comprobaciones de los ejemplos resueltos de la teoría de la Unidad 1 (espacios vectoriales).

Cada función recalcula el ejemplo desde sus datos y verifica los pasos intermedios publicados
(escalonamientos, bases, coordenadas, matrices de cambio, palabras de un código). Convenciones:
base canónica de P_n[R] ordenada {1, x, ..., x^n}; base canónica de R^{2x2} ordenada
{E11, E12, E21, E22}; [v]_B como columna; C_{BB'} con columnas [b_j]_{B'}; en los códigos,
G de k x n con filas = base y H de (n-k) x n con C = nul(H). Los polinomios se manejan por su vector
de coeficientes (c0, c1, c2) y las operaciones de fila se aplican paso a paso, como en el texto.
"""
from itertools import combinations, product

import sympy as sp
from content_pipeline.mathcheck import (
    check, gf_dot, gf_matmul, gf_nullspace, gf_rank, gf_rref, gf_span, hamming, min_distance, require, same, weight,
)

T = "/algebra-ii/unidad-1/teoria/"
P1 = T + "cuerpos-y-z2/"
P2 = T + "espacios-vectoriales/"
P3 = T + "subespacios/"
P4 = T + "combinaciones-lineales/"
P5 = T + "independencia-lineal/"
P6 = T + "subespacios-de-una-matriz/"
P7 = T + "base-y-dimension/"
P8 = T + "coordenadas/"
P9 = T + "cambio-de-coordenadas/"
P10 = T + "codigos-lineales/"

R = sp.Rational


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def col(*entries):
    """Vector columna."""
    return sp.Matrix(list(entries))


def cols(*vectors):
    """Matriz cuyas columnas son los vectores dados (tuplas o columnas)."""
    return sp.Matrix.hstack(*[v if isinstance(v, sp.MatrixBase) else sp.Matrix(list(v)) for v in vectors])


def rows_of(*vectors):
    """Matriz cuyas filas son los vectores dados."""
    return sp.Matrix([list(v) for v in vectors])


def swap(A, i, j):
    """F_i <-> F_j (índices desde 1)."""
    r = A.tolist()
    r[i - 1], r[j - 1] = r[j - 1], r[i - 1]
    return sp.Matrix(r)


def rop(A, i, j, c):
    """F_i - c F_j -> F_i (índices desde 1)."""
    r = A.tolist()
    r[i - 1] = [a - c * b for a, b in zip(r[i - 1], r[j - 1])]
    return sp.Matrix(r)


def comb(A, i, a, j, b):
    """a F_i + b F_j -> F_i (índices desde 1)."""
    r = A.tolist()
    r[i - 1] = [a * p + b * q for p, q in zip(r[i - 1], r[j - 1])]
    return sp.Matrix(r)


def scale(A, i, c):
    """c F_i -> F_i (índices desde 1)."""
    r = A.tolist()
    r[i - 1] = [c * a for a in r[i - 1]]
    return sp.Matrix(r)


def lin(coefs, vectors):
    """Combinación lineal sum(c_i v_i) de tuplas."""
    n = len(vectors[0])
    return tuple(sum(c * v[k] for c, v in zip(coefs, vectors)) for k in range(n))


def solve(A, b):
    """Solución única de A x = b (A inversible)."""
    return A.inv() * b


def pivots(A):
    return list(A.rref()[1])


def peval(p, a):
    """Evalúa el polinomio de coeficientes p = (c0, c1, ...) en a."""
    return sum(c * a ** k for k, c in enumerate(p))


def gf_vec(A, v):
    """A v^t en Z2 como tupla."""
    return tuple(row[0] for row in gf_matmul(A, [[x] for x in v]))


def gf_vecadd(*vs):
    return tuple(sum(c) % 2 for c in zip(*vs))


def gf_rowmul(a, G):
    """a G en Z2 (a fila)."""
    return tuple(gf_matmul([list(a)], G)[0])


def gf_transpose(A):
    return [list(r) for r in zip(*A)]


def bits(n):
    return list(product((0, 1), repeat=n))


def gf_solutions(A, b):
    """Todos los x de Z2^n con A x = b."""
    n = len(A[0])
    return sorted(x for x in bits(n) if gf_vec(A, x) == tuple(b))


def is_subspace_z2(S):
    """S (conjunto de tuplas de Z2^n) contiene al nulo y es cerrado para la suma."""
    n = len(next(iter(S)))
    return tuple([0] * n) in S and all(gf_vecadd(a, b) in S for a in S for b in S)


# ---------------------------------------------------------------------------
# 1.1 Cuerpos y Z2
# ---------------------------------------------------------------------------
@check("U1.T01.E1", "Sistema 3x3 resuelto en Z2 y en R; sistema 2x2 incompatible en Z2", page=P1)
def _():
    A = [[1, 1, 0], [0, 1, 1], [1, 1, 1]]
    b = [1, 1, 0]
    require(gf_rank(A, 2) == 3, "rango 3 en Z2")
    require(gf_solutions(A, b) == [(1, 0, 1)], "solución única (1,0,1) en Z2")
    xr = solve(sp.Matrix(A), col(*b))
    same(xr, col(-1, 2, -1), "solución real")
    require(tuple(int(t) % 2 for t in xr) == (1, 0, 1), "la solución real reducida módulo 2")
    # Segundo sistema: x+y=1, x-y=0.
    same(solve(sp.Matrix([[1, 1], [1, -1]]), col(1, 0)), col(R(1, 2), R(1, 2)), "solución real (1/2,1/2)")
    require(gf_solutions([[1, 1], [1, -1]], [1, 0]) == [], "incompatible en Z2")
    require(gf_rank([[1, 1], [1, 1]]) == 1 and gf_rank([[1, 1, 1], [1, 1, 0]]) == 2, "rango A=1, rango ampliada=2")
    # Aritmética de bits del texto.
    require(gf_vecadd((1, 0, 1, 1), (0, 1, 1, 0)) == (1, 1, 0, 1), "XOR bit a bit")
    require(sum((1, 0, 1, 1)) % 2 == 1, "bit de paridad de 1011")


@check("U1.T01.E2", "Inversos en Z5 y la ecuación 3x+4=1; Z3 y Z7 de la autoevaluación", page=P1)
def _():
    inv5 = {a: next(x for x in range(1, 5) if (a * x) % 5 == 1) for a in range(1, 5)}
    require(inv5 == {1: 1, 2: 3, 3: 2, 4: 4}, "inversos en Z5")
    require(-4 % 5 == 1, "opuesto de 4 en Z5")
    require([x for x in range(5) if (3 * x + 4) % 5 == 1] == [4], "única solución x=4")
    require((3 * 4 + 4) % 5 == 1 and (2 * 2) % 5 == 4, "comprobaciones")
    require((2 * 2) % 3 == 1, "2^{-1}=2 en Z3")
    require([x for x in range(7) if (3 * x) % 7 == 5] == [4], "3x=5 en Z7")
    require((1 + 1 + 1) % 2 == 1 and ((1 + 1) * 1) % 2 == 0, "autoevaluación 2")
    require((2 * 3) % 6 == 0 and {(2 * x) % 6 for x in range(6)} == {0, 2, 4}, "Z6 no es cuerpo")


@check("U1.T01.E3", "Tabla del producto de Z4 y los axiomas que fallan; Z_n es cuerpo sii n primo", page=P1)
def _():
    tabla = [[(a * b) % 4 for b in range(4)] for a in range(4)]
    require(tabla == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 0, 2], [0, 3, 2, 1]], "tabla de Z4")
    require(tabla[2][2] == 0, "2*2=0")
    require(1 not in tabla[2], "2 no tiene inverso")
    require([a for a in range(1, 4) if 1 in tabla[a]] == [1, 3], "invertibles de Z4")
    require([x for x in range(4) if (2 * x) % 4 == 1] == [], "2x=1 sin solución")
    require([x for x in range(4) if (2 * x) % 4 == 0] == [0, 2], "2x=0 con dos soluciones")

    def es_cuerpo(n):
        return all(any((a * x) % n == 1 for x in range(1, n)) for a in range(1, n))

    primos = [n for n in range(2, 30) if all(n % d for d in range(2, n))]
    require([n for n in range(2, 30) if es_cuerpo(n)] == primos, "Z_n es cuerpo exactamente para n primo")


# ---------------------------------------------------------------------------
# 1.2 Espacios vectoriales
# ---------------------------------------------------------------------------
@check("U1.T02.E1", "Bloque de paridad en Z2^4 y recuperación de d2", page=P2)
def _():
    d1, d2, d3 = (1, 0, 1, 1), (0, 1, 1, 0), (1, 1, 0, 0)
    p = gf_vecadd(d1, d2, d3)
    require(p == (0, 0, 0, 1), "p = d1+d2+d3")
    require(gf_vecadd(p, d1, d3) == d2, "recupera d2")
    require(gf_vecadd(p, d2, d3) == d1 and gf_vecadd(p, d1, d2) == d3, "recupera cualquier bloque")
    require(all(gf_vecadd(v, v) == (0, 0, 0, 0) for v in bits(4)), "v+v=0 en Z2^4")


@check("U1.T02.E2", "R con x⊕y=x+y-1 y λ⊙x=λx-λ+1 es espacio vectorial; (3⊙5)⊕((-2)⊙4)=7", page=P2)
def _():
    def add(a, b):
        return a + b - 1

    def mul(lam, a):
        return lam * a - lam + 1

    xs = [R(k, 3) for k in (-7, -2, 0, 1, 4, 9)]
    ls = [R(k, 2) for k in (-5, -1, 0, 1, 3, 7)]
    require(all(add(a, 1) == a for a in xs), "el nulo es el número 1")
    require(all(add(a, 2 - a) == 1 for a in xs), "el opuesto de x es 2-x")
    require(all(add(a, b) == add(b, a) for a in xs for b in xs), "conmutativa")
    require(all(add(add(a, b), c) == add(a, add(b, c)) for a in xs for b in xs for c in xs), "asociativa")
    require(all(mul(1, a) == a for a in xs), "1⊙x=x")
    require(all(mul(l * m, a) == mul(l, mul(m, a)) for l in ls for m in ls for a in xs), "(λμ)⊙x=λ⊙(μ⊙x)")
    require(all(mul(l, add(a, b)) == add(mul(l, a), mul(l, b)) for l in ls for a in xs for b in xs), "distributiva 1")
    require(all(mul(l + m, a) == add(mul(l, a), mul(m, a)) for l in ls for m in ls for a in xs), "distributiva 2")
    require(all(mul(0, a) == 1 for a in xs), "0⊙x es el nulo (propiedad 4)")
    require(mul(3, 5) == 13 and mul(-2, 4) == -5 and add(13, -5) == 7, "cálculo pedido")
    phi = lambda a: a - 1  # noqa: E731
    require(all(phi(add(a, b)) == phi(a) + phi(b) for a in xs for b in xs), "φ(x⊕y)=φ(x)+φ(y)")
    require(all(phi(mul(l, a)) == l * phi(a) for l in ls for a in xs), "φ(λ⊙x)=λφ(x)")
    require(3 * phi(5) + (-2) * phi(4) == 6 and 6 + 1 == 7, "comprobación por φ")


@check("U1.T02.E3", "λ⊙(x,y)=(λx,y) rompe solo el axioma 10; con (λx,0) falla el 7", page=P2)
def _():
    def mul(l, v):
        return (l * v[0], v[1])

    def add(u, v):
        return (u[0] + v[0], u[1] + v[1])

    vs = [(1, 2), (-3, 5), (0, 4), (2, -1)]
    ls = [-2, 0, 1, 3]
    require(all(mul(1, v) == v for v in vs), "axioma 7")
    require(all(mul(l * m, v) == mul(l, mul(m, v)) for l in ls for m in ls for v in vs), "axioma 8")
    require(all(mul(l, add(u, v)) == add(mul(l, u), mul(l, v)) for l in ls for u in vs for v in vs), "axioma 9")
    require(mul(2, (1, 2)) == (2, 2) and add(mul(1, (1, 2)), mul(1, (1, 2))) == (2, 4), "contraejemplo del axioma 10")
    require(all(mul(l + m, (x0, 0)) == add(mul(l, (x0, 0)), mul(m, (x0, 0))) for l in ls for m in ls for x0 in (1, 2)),
            "con y=0 el axioma 10 parece valer")
    require((1 * 1, 0) == (1, 0) and (1, 0) != (1, 2), "con (λx,0): 1⊙(1,2)=(1,0)≠(1,2)")


@check("U1.T02.E4", "2p-q en P_2[R] y el conjunto de polinomios de grado exactamente 2", page=P2)
def _():
    p, q = (1, 2, -1), (3, -1, 2)
    d = tuple(2 * a - b for a, b in zip(p, q))
    require(d == (-1, 5, -4), "2p-q")
    require(all(peval(d, t) == 2 * peval(p, t) - peval(q, t) for t in (1, 2, -3, R(1, 2))), "evaluaciones")
    require(2 * peval(p, 1) - peval(q, 1) == 0 and 2 * peval(p, 2) - peval(q, 2) == -7, "valores del texto")
    a, b = (0, 1, 1), (1, 0, -1)  # x+x^2 y 1-x^2
    s = tuple(i + j for i, j in zip(a, b))
    require(s == (1, 1, 0), "la suma (x+x^2)+(1-x^2)=1+x tiene grado 1")
    require(sp.Matrix([0, 0, 0]) != sp.Matrix(list(s)), "no es nulo")
    # Autoevaluación: I y -I son inversibles, su suma no.
    require(sp.eye(2).det() != 0 and (-sp.eye(2)).det() != 0 and (sp.eye(2) + (-sp.eye(2))).det() == 0, "I + (-I)")


# ---------------------------------------------------------------------------
# 1.3 Subespacios
# ---------------------------------------------------------------------------
@check("U1.T03.E1", "S: x-2y=0 es subespacio y L: x-2y=-4 no lo es", page=P3)
def _():
    f = lambda v: v[0] - 2 * v[1]  # noqa: E731
    p, q = (0, 2), (2, 3)
    require(f(p) == -4 and f(q) == -4 and f((0, 0)) == 0, "p, q en L; el origen no")
    s = (p[0] + q[0], p[1] + q[1])
    require(s == (2, 5) and f(s) == -8, "p+q sobre x-2y=-8")
    require(f((2 * p[0], 2 * p[1])) == -8 and (2 * p[0], 2 * p[1]) == (0, 4), "2p fuera de L")
    # Puntos de S y de L en el rango de la figura, y cierre de S.
    ptsS = [(2 * t, t) for t in range(-6, 7)]
    require(all(f(v) == 0 for v in ptsS), "puntos de S")
    require(all(f((u[0] + v[0], u[1] + v[1])) == 0 for u in ptsS for v in ptsS), "S cerrado para la suma")
    require(all(f((l * u[0], l * u[1])) == 0 for u in ptsS for l in (-3, R(1, 2), 5)), "S cerrado por escalares")
    ptsL = [(2 * t - 4, t) for t in range(-6, 7)]
    require(all(f(v) == -4 for v in ptsL) and all(f((u[0] + v[0], u[1] + v[1])) == -8 for u in ptsL for v in ptsL),
            "la suma de dos puntos de L cae siempre en x-2y=-8")


@check("U1.T03.E2", "Plano 2x-y+3z=0 de R^3: cierre y pertenencias", page=P3)
def _():
    f = lambda v: 2 * v[0] - v[1] + 3 * v[2]  # noqa: E731
    require(f((1, 5, 1)) == 0 and f((2, 1, -1)) == 0 and f((1, 1, 1)) == 4, "pertenencias")
    require(lin((1, 1), [(1, 5, 1), (2, 1, -1)]) == (3, 6, 0) and f((3, 6, 0)) == 0, "suma")
    require(lin((-2,), [(1, 5, 1)]) == (-2, -10, -2) and f((-2, -10, -2)) == 0, "múltiplo")
    A = sp.Matrix([[2, -1, 3]])
    require(len(A.nullspace()) == 2, "el sistema homogéneo de una ecuación tiene nulidad 2")
    for v in A.nullspace():
        same(A * v, sp.zeros(1, 1), "base del plano")


@check("U1.T03.E3", "Matrices simétricas y de traza nula en R^{2x2}", page=P3)
def _():
    # Coordenadas (a,b,c,d) en {E11,E12,E21,E22}: simétrica <=> b-c=0, traza nula <=> a+d=0.
    S = sp.Matrix([[0, 1, -1, 0]])
    Tn = sp.Matrix([[1, 0, 0, 1]])
    require(len(S.nullspace()) == 3 and len(Tn.nullspace()) == 3, "dim S = dim T = 3")
    ST = sp.Matrix.vstack(S, Tn)
    require(len(ST.nullspace()) == 2, "dim de la intersección = 2")
    A, B = sp.Matrix([[1, 2], [2, -1]]), sp.Matrix([[0, 3], [3, 0]])
    C = A + B
    same(C, sp.Matrix([[1, 5], [5, -1]]), "A+B")
    require(C == C.T and C[0, 0] + C[1, 1] == 0, "A+B simétrica y de traza nula")
    require(A == A.T and B == B.T and A[0, 0] + A[1, 1] == 0 and B[0, 0] + B[1, 1] == 0, "A y B en la intersección")
    for t in [A, B, A + B, 3 * A - 2 * B]:
        v = sp.Matrix([t[0, 0], t[0, 1], t[1, 0], t[1, 1]])
        same(ST * v, sp.zeros(2, 1), "pertenece a la intersección")


@check("U1.T03.E4", "S={p en P2: p(-1)=p(2)}: forma genérica, base {1, x^2-x}, pertenencias", page=P3)
def _():
    # p = a + b x + c x^2: p(-1)-p(2) = -3b - 3c.
    for a, b, c in [(1, 2, 3), (0, 1, 0), (5, -1, 4), (2, 2, -2)]:
        p = (a, b, c)
        require(peval(p, -1) - peval(p, 2) == -3 * b - 3 * c, "diferencia de evaluaciones")
    base = [(1, 0, 0), (0, -1, 1)]  # 1 y x^2-x
    require(all(peval(p, -1) == peval(p, 2) for p in base), "la base está en S")
    require(peval((0, -1, 1), -1) == 2 and peval((0, -1, 1), 2) == 2, "valores de x^2-x")
    q = (3, 2, -2)
    require(peval(q, -1) == -1 and peval(q, 2) == -1, "q en S")
    require(lin((3, -2), base) == q, "q = 3·1 - 2(x^2-x)")
    r = (0, 1, 0)
    require(peval(r, -1) == -1 and peval(r, 2) == 2, "r no está en S")
    require(sp.Matrix([[1, 0, 0], [0, -1, 1]]).rank() == 2, "independientes")
    # Para todo (a,c): a + c(x^2-x) está en S.
    require(all(peval(lin((a, c), base), -1) == peval(lin((a, c), base), 2) for a in range(-3, 4) for c in range(-3, 4)),
            "forma genérica")
    # Simetría respecto de x=1/2.
    require(all(peval(lin((a, c), base), R(1, 2) + t) == peval(lin((a, c), base), R(1, 2) - t)
                for a in (1, 3) for c in (-2, 1) for t in (R(1, 3), 2)), "simetría respecto de x=1/2")


@check("U1.T03.E5", "S={a+b+c=0} en Z2^3: elementos, subespacio; T={a+b+c=1} no lo es", page=P3)
def _():
    S = {v for v in bits(3) if sum(v) % 2 == 0}
    Tt = {v for v in bits(3) if sum(v) % 2 == 1}
    require(S == {(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)}, "elementos de S")
    require(is_subspace_z2(S), "S es subespacio")
    require(not is_subspace_z2(Tt) and (0, 0, 0) not in Tt, "T no es subespacio")
    require(gf_vecadd((1, 0, 0), (0, 1, 0)) == (1, 1, 0) and (1, 1, 0) not in Tt, "suma fuera de T")
    require(len(S) == len(Tt) == 4 and S | Tt == set(bits(3)) and not (S & Tt), "particiones")
    require(all(v[2] == (v[0] + v[1]) % 2 for v in S), "código de paridad: c = a+b")
    tabla = [[gf_vecadd(a, b) for b in sorted(S)] for a in sorted(S)]
    require(all(x in S for fila in tabla for x in fila), "tabla de sumas cerrada")


@check("U1.T03.E6", "Subespacios de Z2^2 (5) y de Z2^3 (16 = 1+7+7+1)", page=P3)
def _():
    def subespacios(n):
        todos = bits(n)
        cero = tuple([0] * n)
        out = []
        for mask in range(1 << len(todos)):
            S = {todos[i] for i in range(len(todos)) if mask >> i & 1}
            if S and cero in S and is_subspace_z2(S):
                out.append(S)
        return out

    s2 = subespacios(2)
    require(len(s2) == 5 and sorted(len(S) for S in s2) == [1, 2, 2, 2, 4], "Z2^2")
    s3 = subespacios(3)
    require(len(s3) == 16, "Z2^3 tiene 16 subespacios")
    require(sorted(len(S) for S in s3) == [1] + [2] * 7 + [4] * 7 + [8], "tamaños 1,2,4,8")
    # Los 7 de cuatro elementos son los núcleos de las 7 ecuaciones a·x=0.
    nucleos = {frozenset(v for v in bits(3) if gf_dot(a, v) == 0) for a in bits(3) if any(a)}
    require(nucleos == {frozenset(S) for S in s3 if len(S) == 4}, "subespacios de 4 elementos")


@check("U1.T03.E7", "Tres conjuntos que no son subespacios: xy=0, det=0, x>=0", page=P3)
def _():
    # (a) xy=0
    A = lambda v: v[0] * v[1] == 0  # noqa: E731
    require(A((0, 0)) and A((1, 0)) and A((0, 1)) and not A((1, 1)), "unión de ejes")
    require(all(A((l * 3, l * 0)) and A((l * 0, l * 2)) for l in (-2, R(1, 3), 5)), "cerrado por escalares")
    # (b) det=0
    E1, E2 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]])
    require(E1.det() == 0 and E2.det() == 0 and (E1 + E2).det() == 1, "suma de singulares inversible")
    require(all((l * E1).det() == l ** 2 * E1.det() for l in (-2, 3)), "det(λM)=λ²det M")
    # (c) x>=0
    H = lambda v: v[0] >= 0  # noqa: E731
    require(H((1, 0)) and H((0, 0)) and not H((-1, 0)), "semiplano")
    require(all(H((a + b, 0)) for a in range(5) for b in range(5)), "cerrado para la suma")
    # Autoevaluación: M^2=0.
    M, N = sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]])
    require(M * M == sp.zeros(2, 2) and N * N == sp.zeros(2, 2) and (M + N) * (M + N) == sp.eye(2), "M+N")
    require(gf_vecadd((1, 1, 0), (0, 1, 1)) == (1, 0, 1), "autoevaluación 4")


# ---------------------------------------------------------------------------
# 1.4 Combinaciones lineales (esta lección)
# ---------------------------------------------------------------------------
@check("U1.T04.E1", "Pertenencia a gen{v1,v2,v3} en R^3 por escalonamiento y ecuación del plano", page=P4)
def _():
    v1, v2, v3 = (1, 2, -1), (2, 1, 3), (0, 3, -5)
    require(lin((2, -1), [v1, v2]) == v3, "v3 = 2v1 - v2")
    w, z = (4, 5, 1), (1, 1, 1)
    A = cols(v1, v2, v3)
    aug = sp.Matrix.hstack(A, col(*w), col(*z))
    same(aug, sp.Matrix([[1, 2, 0, 4, 1], [2, 1, 3, 5, 1], [-1, 3, -5, 1, 1]]), "matriz ampliada")
    e1 = rop(rop(aug, 2, 1, 2), 3, 1, -1)
    same(e1, sp.Matrix([[1, 2, 0, 4, 1], [0, -3, 3, -3, -1], [0, 5, -5, 5, 2]]), "primer paso")
    e2 = scale(e1, 2, R(-1, 3))
    e3 = rop(e2, 3, 2, 5)
    same(e3, sp.Matrix([[1, 2, 0, 4, 1], [0, 1, -1, 1, R(1, 3)], [0, 0, 0, 0, R(1, 3)]]), "escalonada")
    require(A.rank() == 2 and sp.Matrix.hstack(A, col(*w)).rank() == 2 and sp.Matrix.hstack(A, col(*z)).rank() == 3,
            "w compatible, z incompatible")
    require(lin((2, 1), [v1, v2]) == w, "w = 2v1 + v2")
    sol = lambda t: (2 - 2 * t, 1 + t, t)  # noqa: E731
    require(all(lin(sol(t), [v1, v2, v3]) == w for t in range(-3, 4)), "soluciones generales")
    # Ecuación del plano: 7x - 5y - 3z = 0.
    n = (7, -5, -3)
    require(all(sum(a * b for a, b in zip(n, v)) == 0 for v in (v1, v2, v3, w)), "los generadores y w cumplen la ecuación")
    require(sum(a * b for a, b in zip(n, z)) == -1, "z no")
    cruz = (v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0])
    require(cruz == n, "v1 x v2 es normal")
    require(sp.Matrix([list(n)]).nullspace() and len(sp.Matrix([list(n)]).nullspace()) == 2, "plano de dimensión 2")


@check("U1.T04.E2", "De generadores a ecuaciones implícitas (dos métodos) y de ecuaciones a generadores, en R^4", page=P4)
def _():
    g1, g2, g3, g4 = (1, 1, 0, 2), (0, 1, 1, -1), (1, 2, 1, 1), (2, 1, -1, 5)
    require(lin((1, 1), [g1, g2]) == g3 and lin((2, -1), [g1, g2]) == g4, "g3 = g1+g2 y g4 = 2g1-g2")
    G = cols(g1, g2, g3, g4)
    require(G.rank() == 2 and pivots(G) == [0, 1], "dim 2, columnas pivote 1 y 2")
    # Método 1: columnas (g1 g2) | x con x genérico, se anulan las filas de abajo.
    x1, x2, x3, x4 = (R(3), R(-5), R(7), R(2))  # un punto cualquiera
    aug = sp.Matrix([[1, 0, x1], [1, 1, x2], [0, 1, x3], [2, -1, x4]])
    a1 = rop(rop(aug, 2, 1, 1), 4, 1, 2)
    same(a1, sp.Matrix([[1, 0, x1], [0, 1, x2 - x1], [0, 1, x3], [0, -1, x4 - 2 * x1]]), "primer paso")
    a2 = rop(a1, 3, 2, 1)
    a2 = comb(a2, 4, 1, 2, 1)
    require(a2[2, 2] == x3 - x2 + x1 and a2[3, 2] == x4 + x2 - 3 * x1, "condiciones: x1-x2+x3 y -3x1+x2+x4")
    eqs1 = [(1, -1, 1, 0), (-3, 1, 0, 1)]
    # Método 2: coeficientes c con c·g_i=0 (núcleo de la matriz con los generadores como filas).
    N = rows_of(g1, g2, g3, g4).nullspace()
    require(len(N) == 2, "dos ecuaciones independientes")
    cnull = rows_of(g1, g2).nullspace()
    same(cnull[0].T, sp.Matrix([[1, -1, 1, 0]]), "primer vector de coeficientes")
    same(cnull[1].T, sp.Matrix([[-3, 1, 0, 1]]), "segundo vector de coeficientes")
    require(sp.Matrix([list(e) for e in eqs1]).rank() == 2, "ecuaciones independientes")
    for e in eqs1:
        require(all(sum(a * b for a, b in zip(e, g)) == 0 for g in (g1, g2, g3, g4)), "los generadores cumplen las ecuaciones")
    # El otro sistema equivalente (2x1 - x3 - x4 = 0) tiene el mismo conjunto solución.
    otra = (2, 0, -1, -1)
    require(sp.Matrix([list(e) for e in eqs1] + [list(otra)]).rank() == 2, "equivalente al anterior")
    require(all(sum(a * b for a, b in zip(otra, g)) == 0 for g in (g1, g2)), "2x1-x3-x4=0 también la cumplen")
    # De ecuaciones a generadores: x1-x2+x3=0, -3x1+x2+x4=0 -> libres x1, x3.
    Sys = sp.Matrix([[1, -1, 1, 0], [-3, 1, 0, 1]])
    ns = Sys.nullspace()
    require(len(ns) == 2 and Sys.rank() == 2, "rango-nulidad: 4 = 2 + 2")
    for v in ns:
        same(Sys * v, sp.zeros(2, 1), "solución general")
    same(cols(g1, g2).rank(), 2, "g1, g2 independientes")
    for g in (g1, g2):
        same(Sys * col(*g), sp.zeros(2, 1), "g en nul")
    # x = a g1 + b g2 = (a, a+b, b, 2a-b).
    require(all(lin((a, b), [g1, g2]) == (a, a + b, b, 2 * a - b) for a in range(-2, 3) for b in range(-2, 3)), "forma genérica")
    # Un vector que no está: (1,0,0,0).
    require(sp.Matrix.hstack(cols(g1, g2), col(1, 0, 0, 0)).rank() == 3, "(1,0,0,0) no pertenece")


@check("U1.T04.E3", "Igualdad de generados en P2: gen{1+x, x+x^2} = gen{1+2x+x^2, 1-x^2}; 1+x^2 no pertenece", page=P4)
def _():
    p1, p2 = (1, 1, 0), (0, 1, 1)
    q1, q2 = (1, 2, 1), (1, 0, -1)
    require(lin((1, 1), [p1, p2]) == q1 and lin((1, -1), [p1, p2]) == q2, "q1=p1+p2, q2=p1-p2")
    require(lin((R(1, 2), R(1, 2)), [q1, q2]) == p1 and lin((R(1, 2), R(-1, 2)), [q1, q2]) == p2, "p1, p2 en gen{q1,q2}")
    P, Q = cols(p1, p2), cols(q1, q2)
    require(P.rank() == Q.rank() == sp.Matrix.hstack(P, Q).rank() == 2, "mismo generado por rangos")
    r = (1, 0, 1)
    require(sp.Matrix.hstack(P, col(*r)).rank() == 3, "1+x^2 no pertenece")
    # Con el coeficiente: a(1+x)+b(x+x^2) = 1+x^2 exige a=1, b=1 y a+b=0.
    require((1, 1) != (1, 0) and 1 + 1 != 0, "incompatible")
    # Ecuación de gen{p1,p2} en coordenadas: c0 - c1 + c2 = 0.
    n = (1, -1, 1)
    require(all(sum(a * b for a, b in zip(n, v)) == 0 for v in (p1, p2, q1, q2)) and sum(a * b for a, b in zip(n, r)) == 2,
            "ecuación c0-c1+c2=0")


@check("U1.T04.E4", "Z2^4: gen{g1,g2,g3} tiene 4 elementos aunque haya 8 combinaciones; ecuaciones", page=P4)
def _():
    g1, g2, g3 = (1, 1, 0, 1), (0, 1, 1, 1), (1, 0, 1, 0)
    require(gf_vecadd(g1, g2) == g3, "g3 = g1+g2")
    combos = {c: gf_vecadd(*[tuple(a * x for x in g) for a, g in zip(c, (g1, g2, g3))]) for c in bits(3)}
    require(len(set(combos.values())) == 4, "ocho combinaciones, cuatro vectores")
    S = gf_span([g1, g2, g3])
    require(S == {(0, 0, 0, 0), (1, 1, 0, 1), (0, 1, 1, 1), (1, 0, 1, 0)}, "elementos del generado")
    require(S == gf_span([g1, g2]) and gf_rank([g1, g2, g3]) == 2, "dimensión 2")
    require((1, 1, 1, 1) not in S, "(1,1,1,1) no pertenece")
    eq = [[1, 1, 1, 0], [0, 1, 0, 1]]
    require(all(gf_vec(eq, g) == (0, 0) for g in (g1, g2, g3)), "ecuaciones x1+x2+x3=0, x2+x4=0")
    require({x for x in bits(4) if gf_vec(eq, x) == (0, 0)} == S, "las ecuaciones definen el mismo conjunto")
    require(gf_nullspace(eq) and len(gf_nullspace(eq)) == 2, "nulidad 2")
    require(all(gf_vecadd(a, b) in S for a in S for b in S), "cerrado para la suma")
    require(len(gf_span([(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)])) == 8, "tres independientes dan 2^3 vectores")


# ---------------------------------------------------------------------------
# 1.5 Independencia lineal (esta lección)
# ---------------------------------------------------------------------------
@check("U1.T05.E1", "El mismo conjunto {(1,1,0),(0,1,1),(1,0,1)}: LI en R^3 y LD en Z2^3", page=P5)
def _():
    v1, v2, v3 = (1, 1, 0), (0, 1, 1), (1, 0, 1)
    A = cols(v1, v2, v3)
    same(A.det(), 2, "determinante real")
    require(A.rank() == 3 and A.nullspace() == [], "sobre R: solo la solución trivial")
    # Escalonamiento real publicado.
    e = rop(A, 2, 1, 1)
    same(e, sp.Matrix([[1, 0, 1], [0, 1, -1], [0, 1, 1]]), "F2-F1")
    e = rop(e, 3, 2, 1)
    same(e, sp.Matrix([[1, 0, 1], [0, 1, -1], [0, 0, 2]]), "F3-F2")
    # Sobre Z2.
    M = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    require(gf_rank(M) == 2 and gf_nullspace(M) == [[1, 1, 1]], "sobre Z2: rango 2, relación (1,1,1)")
    require(gf_vecadd(v1, v2, v3) == (0, 0, 0) and gf_vecadd(v1, v2) == v3, "v1+v2+v3=0 en Z2")
    require(round(A.det()) % 2 == 0, "det=2 ≡ 0 mod 2")
    require(len(gf_span([v1, v2, v3])) == 4, "el generado sobre Z2 tiene 4 elementos")
    # Sobre R los tres generan R^3; los cuatro vectores de Z2^3 que no están son los de peso impar.
    require({v for v in bits(3)} - gf_span([v1, v2, v3]) == {(0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)}, "complemento")


@check("U1.T05.E2", "Vandermonde: {(1,1,1),(1,2,4),(1,k,k^2)} es LD sii k=1 o k=2", page=P5)
def _():
    for k in range(-4, 8):
        A = cols((1, 1, 1), (1, 2, 4), (1, k, k * k))
        same(A.det(), (k - 1) * (k - 2), f"det con k={k}")
        require((A.rank() < 3) == (k in (1, 2)), f"dependencia con k={k}")
    require((1, 1, 1) == (1, 1, 1 ** 2) and (1, 2, 4) == (1, 2, 2 ** 2), "k=1 repite v1, k=2 repite v2")
    A = cols((1, 1, 1), (1, 2, 4), (1, 3, 9))
    same(A.det(), 2, "k=3")
    # Escalonamiento con k genérico evaluado en k=3: F2-F1, F3-F1.
    e = rop(rop(A.T, 2, 1, 1), 3, 1, 1)
    same(e, sp.Matrix([[1, 1, 1], [0, 1, 3], [0, 2, 8]]), "filas = vectores")
    e = rop(e, 3, 2, 2)
    same(e, sp.Matrix([[1, 1, 1], [0, 1, 3], [0, 0, 2]]), "F3-2F2")
    # Relación de dependencia para k=1 y k=2.
    require(sp.Matrix.hstack(*[col(*v) for v in ((1, 1, 1), (1, 2, 4), (1, 1, 1))]).nullspace()[0].T == sp.Matrix([[-1, 0, 1]]),
            "relación v1 - v3 = 0 para k=1")


@check("U1.T05.E3", "{u,v,w} LI implica {u+v,u-v,w} LI sobre R y LD sobre Z2", page=P5)
def _():
    # Coordenadas respecto de (u,v,w): columnas de u+v, u-v, w.
    A = cols((1, 1, 0), (1, -1, 0), (0, 0, 1))
    same(A.det(), -2, "determinante")
    require(A.rank() == 3, "LI sobre R")
    # a(u+v)+b(u-v)+cw=0 -> a+b=0, a-b=0, c=0.
    require(A.nullspace() == [], "solo la trivial")
    B = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]  # -1 = 1 en Z2
    require(gf_rank(B) == 2 and gf_nullspace(B) == [[1, 1, 0]], "sobre Z2: (u+v)+(u-v)=0")
    require(gf_vecadd((1, 1, 0), (1, 1, 0)) == (0, 0, 0), "u+v = u-v en Z2")
    # Otro conjunto: {u+v, v+w, u+w} es LI sobre R (det 2) y LD sobre Z2 (suma nula).
    C = cols((1, 1, 0), (0, 1, 1), (1, 0, 1))
    same(C.det(), 2, "det {u+v,v+w,u+w}")
    require(gf_vecadd((1, 1, 0), (0, 1, 1), (1, 0, 1)) == (0, 0, 0), "suma nula en Z2")
    # {u+v, v+w, w-u} es LD sobre cualquier cuerpo.
    D = cols((1, 1, 0), (0, 1, 1), (-1, 0, 1))
    same(D.det(), 0, "det {u+v,v+w,w-u}")
    require(D.nullspace()[0].T == sp.Matrix([[1, -1, 1]]), "relación (u+v)-(v+w)+(w-u)=0")


@check("U1.T05.E4", "Independencia de matrices 2x2 por coordenadas y relación A3=2A1+A2", page=P5)
def _():
    A1, A2, A3, A4 = (sp.Matrix(m) for m in ([[1, 0], [1, 1]], [[0, 1], [1, 0]], [[2, 1], [3, 2]], [[1, 1], [0, 0]]))
    same(2 * A1 + A2, A3, "A3 = 2A1 + A2")
    vec = lambda M: col(M[0, 0], M[0, 1], M[1, 0], M[1, 1])  # noqa: E731
    same(vec(A1), col(1, 0, 1, 1), "coordenadas de A1")
    same(vec(A2), col(0, 1, 1, 0), "coordenadas de A2")
    same(vec(A3), col(2, 1, 3, 2), "coordenadas de A3")
    same(vec(A4), col(1, 1, 0, 0), "coordenadas de A4")
    D = cols(vec(A1), vec(A2), vec(A3))
    require(D.rank() == 2 and D.nullspace()[0].T == sp.Matrix([[-2, -1, 1]]), "A1,A2,A3 dependientes")
    L = cols(vec(A1), vec(A2), vec(A4))
    require(L.rank() == 3 and L.nullspace() == [], "A1,A2,A4 independientes")
    # Escalonamiento de las coordenadas de (A1 A2 A4).
    e = rop(L, 3, 1, 1)
    e = rop(e, 4, 1, 1)
    same(e, sp.Matrix([[1, 0, 1], [0, 1, 1], [0, 1, -1], [0, 0, -1]]), "paso 1")
    e = rop(e, 3, 2, 1)
    same(e, sp.Matrix([[1, 0, 1], [0, 1, 1], [0, 0, -2], [0, 0, -1]]), "paso 2")
    require(e.rank() == 3, "tres pivotes")


# ---------------------------------------------------------------------------
# 1.6 Subespacios de una matriz
# ---------------------------------------------------------------------------
@check("U1.T06.E1", "fil, col y nul de una matriz real 3x4; compatibilidad de Ax=b", page=P6)
def _():
    A = sp.Matrix([[1, 2, 0, 3], [2, 4, 1, 8], [1, 2, 2, 7]])
    e1 = rop(rop(A, 2, 1, 2), 3, 1, 1)
    same(e1, sp.Matrix([[1, 2, 0, 3], [0, 0, 1, 2], [0, 0, 2, 4]]), "primer escalonamiento")
    e2 = rop(e1, 3, 2, 2)
    Ap = sp.Matrix([[1, 2, 0, 3], [0, 0, 1, 2], [0, 0, 0, 0]])
    same(e2, Ap, "escalonada A'")
    same(A.rref()[0], Ap, "A' es la reducida")
    require(pivots(A) == [0, 2] and A.rank() == 2, "pivotes en columnas 1 y 3")
    # Espacio nulo.
    n1, n2 = col(-2, 1, 0, 0), col(-3, 0, -2, 1)
    same(A * n1, sp.zeros(3, 1), "A n1 = 0")
    same(A * n2, sp.zeros(3, 1), "A n2 = 0")
    require(len(A.nullspace()) == 2 and cols(n1, n2).rank() == 2, "dim nul = 2")
    require(A.rank() + len(A.nullspace()) == 4, "rango-nulidad")
    # Espacio columna.
    c1, c2, c3, c4 = (col(*[A[i, j] for i in range(3)]) for j in range(4))
    same(c2, 2 * c1, "c2 = 2c1")
    same(c4, 3 * c1 + 2 * c3, "c4 = 3c1 + 2c3")
    same(3 * c1 + 2 * c3, col(3, 8, 7), "(3,8,7)")
    # Ecuación de col(A): 3y1 - 2y2 + y3 = 0.
    eq = sp.Matrix([[3, -2, 1]])
    for c in (c1, c2, c3, c4):
        same(eq * c, sp.zeros(1, 1), "columna en el plano")
    b1, b2 = col(1, 1, -1), col(1, 0, 0)
    same(eq * b1, sp.zeros(1, 1), "b=(1,1,-1) cumple")
    require((eq * b2)[0, 0] == 3, "b=(1,0,0) no cumple")
    require(sp.Matrix.hstack(A, b1).rank() == 2 and sp.Matrix.hstack(A, b2).rank() == 3, "compatibilidad por rangos")
    same(A * col(1, 0, -1, 0), b1, "solución particular")
    same(c1 - c3, b1, "b = c1 - c3")
    # col(A') es el plano y3 = 0 y (1,2,1) no está.
    cA = [col(*[Ap[i, j] for i in range(3)]) for j in range(4)]
    require(all(v[2] == 0 for v in cA), "col(A') ⊆ {y3=0}")
    require(sp.Matrix.hstack(*cA).rank() == 2 and sp.Matrix.hstack(sp.Matrix.hstack(*cA), c1).rank() == 3, "(1,2,1) no está en col(A')")
    # Ecuación del texto: beta = y2 - 2y1.
    for al, be in [(1, 0), (0, 1), (2, -3), (-1, 4)]:
        y = lin((al, be), [(1, 2, 1), (0, 1, 2)])
        require(be == y[1] - 2 * y[0] and 3 * y[0] - 2 * y[1] + y[2] == 0, "parametrización")
    # Producto del texto Ax como combinación de columnas.
    P = sp.Matrix([[1, 3], [2, -1]])
    same(P * col(2, -1), col(-1, 5), "ejemplo de A x")
    same(2 * col(1, 2) - col(3, -1), col(-1, 5), "combinación de columnas")
    # El espacio columna cambia al escalonar.
    Q, Qp = sp.Matrix([[1, 1], [1, 1]]), sp.Matrix([[1, 1], [0, 0]])
    same(rop(Q, 2, 1, 1), Qp, "F2-F1")
    require(sp.Matrix.hstack(Q, col(1, 0)).rank() == 2, "(1,0) no está en col(Q)")
    # Autoevaluación: A 5x7 rango 5 tiene nul de dim 2.
    require(7 - 5 == 2, "autoevaluación 1")


@check("U1.T06.E2", "La misma matriz 4x4 sobre R (inversible) y sobre Z2 (rango 3)", page=P6)
def _():
    M = [[1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1]]
    Mr = sp.Matrix(M)
    s1 = rop(Mr, 3, 2, 1)
    same(s1, sp.Matrix([[1, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, -1], [0, 0, 1, 1]]), "F3-F2 (real)")
    s2 = rop(s1, 4, 3, 1)
    same(s2, sp.Matrix([[1, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, -1], [0, 0, 0, 2]]), "F4-F3 (real)")
    same(Mr.det(), 2, "det real")
    require(Mr.rank() == 4 and Mr.nullspace() == [], "rango 4 sobre R")
    x = Mr.inv() * col(1, 0, 0, 1)
    same(x, col(0, R(-1, 2), R(1, 2), R(1, 2)), "solución real para b=(1,0,0,1)")
    same(Mr * x, col(1, 0, 0, 1), "comprobación real")
    # Sobre Z2, con las operaciones del texto.
    t1 = [r[:] for r in M]
    t1[2] = [(a + b) % 2 for a, b in zip(t1[2], t1[1])]
    require(t1 == [[1, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1]], "F3+F2 (Z2)")
    t1[3] = [(a + b) % 2 for a, b in zip(t1[3], t1[2])]
    require(t1 == [[1, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0]], "M' (Z2)")
    require(gf_rank(M) == 3 and det_mod2(M) == 0, "rango 3 y det ≡ 0 sobre Z2")
    require(gf_nullspace(M) == [[0, 1, 1, 1]], "nul(M) = gen{(0,1,1,1)}")
    cols_ = [tuple(M[i][j] for i in range(4)) for j in range(4)]
    require(cols_ == [(1, 0, 0, 0), (0, 1, 1, 0), (1, 0, 1, 1), (1, 1, 0, 1)], "columnas de M")
    require(gf_vecadd(cols_[1], cols_[2], cols_[3]) == (0, 0, 0, 0) and gf_vecadd(cols_[1], cols_[2]) == cols_[3], "c4 = c2 + c3")
    require(tuple(a + b - c for a, b, c in zip(cols_[1], cols_[2], cols_[3])) == (0, 0, 2, 0), "sobre R: c2+c3-c4=(0,0,2,0)")
    colM = gf_span(cols_)
    require(colM == {b for b in bits(4) if (b[1] + b[2] + b[3]) % 2 == 0} and len(colM) == 8, "col(M) = {b2+b3+b4=0}")
    require(gf_solutions(M, (1, 0, 0, 1)) == [], "b=(1,0,0,1) incompatible en Z2")
    require(gf_solutions(M, (1, 1, 0, 1)) == [(0, 0, 0, 1), (0, 1, 1, 0)], "b=(1,1,0,1): dos soluciones")
    require(gf_vec(M, (0, 1, 1, 1)) == (0, 0, 0, 0) and gf_vec(M, (0, 1, 1, 0)) == (1, 1, 0, 1), "comprobaciones")
    require(gf_rank(M) + len(gf_nullspace(M)) == 4, "rango-nulidad en Z2")


def det_mod2(M):
    """Determinante entero reducido módulo 2."""
    return int(sp.Matrix(M).det()) % 2


# ---------------------------------------------------------------------------
# 1.7 Base y dimensión
# ---------------------------------------------------------------------------
@check("U1.T07.E1", "Extensión de {v1,v2} a una base de R^4 por filas y por columnas", page=P7)
def _():
    v1, v2 = (1, 2, 0, 1), (2, 4, 1, 3)
    F = rows_of(v1, v2)
    same(rop(F, 2, 1, 2), sp.Matrix([[1, 2, 0, 1], [0, 0, 1, 1]]), "F2-2F1")
    require(pivots(F) == [0, 2], "pivotes en las columnas 1 y 3")
    e = lambda i: tuple(int(i == j) for j in range(4))  # noqa: E731
    B1 = rows_of(v1, v2, e(1), e(3))
    B2 = rows_of(v1, v2, e(0), e(1))
    same(B1.det(), -1, "det de la primera base")
    same(B2.det(), -1, "det de la segunda base")
    # Método por columnas.
    M = sp.Matrix([[1, 2, 1, 0, 0, 0], [2, 4, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [1, 3, 0, 0, 0, 1]])
    same(M, sp.Matrix.hstack(cols(v1, v2), sp.eye(4)), "matriz (v1|v2|e1..e4)")
    m1 = rop(rop(M, 2, 1, 2), 4, 1, 1)
    same(m1, sp.Matrix([[1, 2, 1, 0, 0, 0], [0, 0, -2, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, -1, 0, 0, 1]]), "paso 1")
    m2 = swap(m1, 2, 3)
    m3 = rop(m2, 4, 2, 1)
    same(m3, sp.Matrix([[1, 2, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, -2, 1, 0, 0], [0, 0, -1, 0, -1, 1]]), "paso 3")
    m4 = comb(m3, 4, 2, 3, -1)
    same(m4, sp.Matrix([[1, 2, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, -2, 1, 0, 0], [0, 0, 0, -1, -2, 2]]), "escalonada final")
    require(pivots(M) == [0, 1, 2, 3], "columnas pivote 1, 2, 3, 4")
    require(sp.Matrix([list(v1), list(v2)]).rank() == 2, "v1, v2 independientes")


@check("U1.T07.E2", "Base de gen{w1..w5} en R^4 por columnas pivote y ecuación del subespacio", page=P7)
def _():
    w = [(1, -1, 0, 2), (2, -2, 0, 4), (0, 1, 1, 1), (1, 0, 1, 3), (1, 1, 1, 0)]
    A = cols(*w)
    same(A, sp.Matrix([[1, 2, 0, 1, 1], [-1, -2, 1, 0, 1], [0, 0, 1, 1, 1], [2, 4, 1, 3, 0]]), "matriz de columnas")
    a1 = rop(rop(A, 2, 1, -1), 4, 1, 2)
    same(a1, sp.Matrix([[1, 2, 0, 1, 1], [0, 0, 1, 1, 2], [0, 0, 1, 1, 1], [0, 0, 1, 1, -2]]), "paso 1")
    a2 = rop(rop(a1, 3, 2, 1), 4, 2, 1)
    same(a2, sp.Matrix([[1, 2, 0, 1, 1], [0, 0, 1, 1, 2], [0, 0, 0, 0, -1], [0, 0, 0, 0, -4]]), "paso 2")
    a3 = rop(a2, 4, 3, 4)
    same(a3, sp.Matrix([[1, 2, 0, 1, 1], [0, 0, 1, 1, 2], [0, 0, 0, 0, -1], [0, 0, 0, 0, 0]]), "escalonada")
    require(pivots(A) == [0, 2, 4] and A.rank() == 3, "columnas pivote 1, 3, 5")
    require(lin((2,), [w[0]]) == w[1] and lin((1, 1), [w[0], w[2]]) == w[3], "w2 = 2w1 y w4 = w1 + w3")
    require(cols(w[0], w[2], w[4]).rank() == 3, "base {w1,w3,w5}")
    eq = (1, 3, -4, 1)
    require(all(sum(a * b for a, b in zip(eq, v)) == 0 for v in w), "x1+3x2-4x3+x4=0")
    # Incógnitas (a,b,c,d): a-b+2d=0, b+c+d=0, a+b+c=0.
    system = sp.Matrix([[1, -1, 0, 2], [0, 1, 1, 1], [1, 1, 1, 0]])
    ns = system.nullspace()
    require(len(ns) == 1 and ns[0].T == sp.Matrix([[1, 3, -4, 1]]) * (ns[0][0]), "coeficientes de la ecuación")
    require(sp.Matrix([list(eq)]).rank() == 1 and 4 - 1 == 3, "dim = 3 por rango-nulidad")


@check("U1.T07.E3", "Simétricas, traza nula y su intersección en R^{2x2}: bases y extensión", page=P7)
def _():
    E11, E12, E21, E22 = (sp.Matrix(m) for m in ([[1, 0], [0, 0]], [[0, 1], [0, 0]], [[0, 0], [1, 0]], [[0, 0], [0, 1]]))
    vec = lambda M: col(M[0, 0], M[0, 1], M[1, 0], M[1, 1])  # noqa: E731
    BS = [E11, E12 + E21, E22]
    BT = [E11 - E22, E12, E21]
    BI = [E11 - E22, E12 + E21]
    for M in BS:
        require(M == M.T, "simétrica")
    for M in BT + BI:
        require(M[0, 0] + M[1, 1] == 0, "traza nula")
    for M in BI:
        require(M == M.T, "la intersección es simétrica")
    require(cols(*[vec(M) for M in BS]).rank() == 3 and cols(*[vec(M) for M in BT]).rank() == 3, "bases independientes")
    require(cols(*[vec(M) for M in BI]).rank() == 2, "base de la intersección")
    cond = sp.Matrix([[0, 1, -1, 0], [1, 0, 0, 1]])
    require(len(cond.nullspace()) == 2, "dim intersección = 2")
    ext = BI + [E11]
    require(E11[0, 0] + E11[1, 1] == 1, "E11 tiene traza 1")
    same(cols(*[vec(M) for M in ext]), sp.Matrix([[1, 0, 1], [0, 1, 0], [0, 1, 0], [-1, 0, 0]]), "coordenadas (a,b,c,d)")
    require(cols(*[vec(M) for M in ext]).rank() == 3, "extensión independiente")
    for M in ext:
        require(M == M.T, "la extensión está en S")
    # Una matriz genérica simétrica es combinación de BS: (a,b,d) = a E11 + b(E12+E21) + d E22.
    require(all(sp.Matrix([[a, b], [b, d]]) == a * BS[0] + b * BS[1] + d * BS[2] for a in range(3) for b in range(3) for d in range(3)),
            "forma genérica")


@check("U1.T07.E4", "W={p en P2: p(1)=0}: base {x-1, x^2-1}, q=1+x-2x^2 y extensión con 1", page=P7)
def _():
    b1, b2 = (-1, 1, 0), (-1, 0, 1)
    require(peval(b1, 1) == 0 and peval(b2, 1) == 0, "base en W")
    require(sp.Matrix([list(b1), list(b2)]).rank() == 2, "independientes")
    require(all(peval((-b - c, b, c), 1) == 0 for b in range(-2, 3) for c in range(-2, 3)), "forma genérica")
    require(all(lin((b, c), [b1, b2]) == (-b - c, b, c) for b in range(-2, 3) for c in range(-2, 3)), "p = b(x-1)+c(x^2-1)")
    q = (1, 1, -2)
    require(peval(q, 1) == 0 and lin((1, -2), [b1, b2]) == q, "q = (x-1) - 2(x^2-1)")
    require(peval((1, 0, 0), 1) == 1, "1 no está en W")
    B = cols(b1, b2, (1, 0, 0))
    same(B, sp.Matrix([[-1, -1, 1], [1, 0, 0], [0, 1, 0]]), "matriz de coeficientes")
    same(B.det(), 1, "det = 1")
    # Dimensión: una ecuación a+b+c=0 en R^3.
    require(len(sp.Matrix([[1, 1, 1]]).nullspace()) == 2, "dim W = 2")
    # Autoevaluación 1: {1+x, 1-x, x^2} es base de P2.
    same(cols((1, 1, 0), (1, -1, 0), (0, 0, 1)).det(), -2, "autoevaluación 1")


@check("U1.T07.E5", "Subespacio de Z2^5 definido por dos ecuaciones: base y sus 8 elementos", page=P7)
def _():
    H = [[1, 1, 0, 1, 0], [0, 1, 1, 0, 1]]
    require(gf_rank(H) == 2 and 5 - gf_rank(H) == 3, "rango 2, nulidad 3")
    base = [(1, 0, 0, 1, 0), (0, 1, 0, 1, 1), (0, 0, 1, 0, 1)]
    require(all(gf_vec(H, v) == (0, 0) for v in base), "la base está en S")
    require(gf_rank(base) == 3, "independiente")
    S = {x for x in bits(5) if gf_vec(H, x) == (0, 0)}
    require(S == gf_span(base) and len(S) == 8, "S = gen(base), 8 elementos")
    tabla = {
        (0, 0, 0): (0, 0, 0, 0, 0), (1, 0, 0): (1, 0, 0, 1, 0), (0, 1, 0): (0, 1, 0, 1, 1), (0, 0, 1): (0, 0, 1, 0, 1),
        (1, 1, 0): (1, 1, 0, 0, 1), (1, 0, 1): (1, 0, 1, 1, 1), (0, 1, 1): (0, 1, 1, 1, 0), (1, 1, 1): (1, 1, 1, 0, 0),
    }
    for k, v in tabla.items():
        require(gf_vecadd(*[tuple(a * x for x in g) for a, g in zip(k, base)]) == v, f"fila {k}")
        require(v == (k[0], k[1], k[2], (k[0] + k[1]) % 2, (k[1] + k[2]) % 2), "forma (x1,x2,x3,x1+x2,x2+x3)")
    require(len(set(tabla.values())) == 8 and set(tabla.values()) == S, "ocho distintos y todos en S")
    # Autoevaluación 3: A en Z2^{3x6} de rango 3 tiene nul con 2^3 elementos.
    require(2 ** (6 - 3) == 8, "autoevaluación 3")


# ---------------------------------------------------------------------------
# 1.8 Coordenadas
# ---------------------------------------------------------------------------
@check("U1.T08.E1", "Coordenadas en la base {(2,1),(-1,2)} de R^2", page=P8)
def _():
    b1, b2 = (2, 1), (-1, 2)
    Bm = cols(b1, b2)
    same(Bm.det(), 5, "det de la base")
    aug = sp.Matrix([[2, -1, 3], [1, 2, 4]])
    s1 = swap(aug, 1, 2)
    s2 = rop(s1, 2, 1, 2)
    same(s2, sp.Matrix([[1, 2, 4], [0, -5, -5]]), "escalonada")
    cv = solve(Bm, col(3, 4))
    same(cv, col(2, 1), "[v]_B")
    require(lin((2, 1), [b1, b2]) == (3, 4), "2b1 + b2 = (3,4)")
    require(lin((-1, 3), [b1, b2]) == (-5, 5), "w = (-5,5)")
    same(solve(Bm, col(-5, 5)), col(-1, 3), "coordenadas de w")
    # El orden importa: con {(-1,2),(2,1)}, [v] = (1,2).
    same(solve(cols(b2, b1), col(3, 4)), col(1, 2), "base permutada")


@check("U1.T08.E2", "Coordenadas dentro del plano x-y-z=0 de R^3", page=P8)
def _():
    b1, b2 = (1, 0, 1), (0, 1, -1)
    eq = sp.Matrix([[1, -1, -1]])
    require(len(eq.nullspace()) == 2, "dim S = 2")
    same(eq * col(*b1), sp.zeros(1, 1), "b1 en S")
    same(eq * col(*b2), sp.zeros(1, 1), "b2 en S")
    require(cols(b1, b2).rank() == 2, "independientes")
    v = (2, 3, -1)
    same(eq * col(*v), sp.zeros(1, 1), "v en S")
    require(lin((2, 3), [b1, b2]) == v, "[v] = (2,3)")
    w = (1, 1, 1)
    require((eq * col(*w))[0, 0] == -1, "w no está en S")
    require(sp.Matrix.hstack(cols(b1, b2), col(*w)).rank() == 3, "sistema incompatible")


@check("U1.T08.E3", "Coordenadas de 3-x+2x^2 en la base {1, 1+x, 1+x+x^2}", page=P8)
def _():
    B = cols((1, 0, 0), (1, 1, 0), (1, 1, 1))
    same(B.det(), 1, "triangular con unos en la diagonal")
    p = col(3, -1, 2)
    c = solve(B, p)
    same(c, col(4, -3, 2), "[p]_B")
    require(lin((4, -3, 2), [(1, 0, 0), (1, 1, 0), (1, 1, 1)]) == (3, -1, 2), "4 - 3(1+x) + 2(1+x+x^2)")
    # Sistema triangular del texto: gamma=2, beta+gamma=-1, alpha+beta+gamma=3.
    g = 2
    be = -1 - g
    al = 3 - be - g
    require((al, be, g) == (4, -3, 2), "sustitución hacia atrás")


@check("U1.T08.E4", "Coordenadas de [[3,1],[1,2]] en la base de simétricas {M1,M2,M3}", page=P8)
def _():
    M1, M2, M3 = (sp.Matrix(m) for m in ([[1, 1], [1, 0]], [[0, 1], [1, 1]], [[1, 0], [0, 1]]))
    for M in (M1, M2, M3):
        require(M == M.T, "simétrica")
    vec = lambda M: col(M[0, 0], M[0, 1], M[1, 0], M[1, 1])  # noqa: E731
    require(cols(vec(M1), vec(M2), vec(M3)).rank() == 3, "independientes")
    for a, b, c in [(1, 2, 3), (-1, 0, 4)]:
        same(a * M1 + b * M2 + c * M3, sp.Matrix([[a + c, a + b], [a + b, b + c]]), "forma general")
    # Sistema simétrico a+c=3, a+b=1, b+c=2.
    S = sp.Matrix([[1, 0, 1], [1, 1, 0], [0, 1, 1]])
    same(solve(S, col(3, 1, 2)), col(1, 0, 2), "[M]_B")
    same(1 * M1 + 0 * M2 + 2 * M3, sp.Matrix([[3, 1], [1, 2]]), "comprobación")
    same(S.det(), 2, "determinante del sistema")
    # Autoevaluación 3.
    same(vec(sp.Matrix([[5, -1], [0, 2]])), col(5, -1, 0, 2), "coordenadas canónicas")


@check("U1.T08.E5", "Coordenadas de (1,0,1) en la base {(1,1,0),(0,1,1),(1,1,1)} de Z2^3", page=P8)
def _():
    B = [(1, 1, 0), (0, 1, 1), (1, 1, 1)]
    M = [[B[j][i] for j in range(3)] for i in range(3)]
    require(gf_rank(M) == 3 and gf_nullspace(M) == [], "base de Z2^3")
    v = (1, 0, 1)
    sols = gf_solutions(M, v)
    require(sols == [(1, 1, 0)], "[v]_B = (1,1,0)")
    require(gf_vecadd(B[0], B[1]) == v, "(1,1,0)+(0,1,1)=(1,0,1)")
    # La función coordenadas es biyectiva sobre los 8 vectores.
    imagenes = {gf_vec(M, c) for c in bits(3)}
    require(imagenes == set(bits(3)), "las 8 combinaciones dan los 8 vectores")


@check("U1.T08.E6", "Independencia y pertenencia en P2 por coordenadas: p3=p1+p2, q=2p1+p2, r no pertenece", page=P8)
def _():
    p1, p2, p3, q, r = (1, 1, 0), (0, 1, 1), (1, 2, 1), (2, 3, 1), (1, 0, 1)
    aug = sp.Matrix([[1, 0, 1, 2, 1], [1, 1, 2, 3, 0], [0, 1, 1, 1, 1]])
    same(aug, sp.Matrix.hstack(cols(p1, p2, p3), col(*q), col(*r)), "matriz ampliada")
    s1 = rop(aug, 2, 1, 1)
    same(s1, sp.Matrix([[1, 0, 1, 2, 1], [0, 1, 1, 1, -1], [0, 1, 1, 1, 1]]), "F2-F1")
    s2 = rop(s1, 3, 2, 1)
    same(s2, sp.Matrix([[1, 0, 1, 2, 1], [0, 1, 1, 1, -1], [0, 0, 0, 0, 2]]), "F3-F2")
    A = cols(p1, p2, p3)
    require(A.rank() == 2 and pivots(A) == [0, 1], "dependientes, pivotes en 1 y 2")
    require(lin((1, 1), [p1, p2]) == p3, "p3 = p1 + p2")
    require(lin((2, 1), [p1, p2]) == q, "q = 2p1 + p2")
    require(sp.Matrix.hstack(A, col(*r)).rank() == 3, "r no pertenece")


# ---------------------------------------------------------------------------
# 1.9 Cambio de coordenadas
# ---------------------------------------------------------------------------
@check("U1.T09.E1", "C_BB' entre dos bases de R^3 por los dos métodos y [v]_B'", page=P9)
def _():
    B = [(1, 0, 1), (1, 1, 0), (2, 1, 2)]
    Bp = [(1, 1, 1), (0, 1, 1), (0, 0, 1)]
    aug = sp.Matrix.hstack(cols(*Bp), cols(*B))
    same(aug, sp.Matrix([[1, 0, 0, 1, 1, 2], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 2]]), "matriz (B'|B)")
    a1 = rop(rop(aug, 2, 1, 1), 3, 1, 1)
    same(a1, sp.Matrix([[1, 0, 0, 1, 1, 2], [0, 1, 0, -1, 0, -1], [0, 1, 1, 0, -1, 0]]), "paso 1")
    a2 = rop(a1, 3, 2, 1)
    same(a2, sp.Matrix([[1, 0, 0, 1, 1, 2], [0, 1, 0, -1, 0, -1], [0, 0, 1, 1, -1, 1]]), "paso 2")
    C = sp.Matrix([[1, 1, 2], [-1, 0, -1], [1, -1, 1]])
    same(sp.Matrix([r[3:] for r in a2.tolist()]), C, "C_BB' por el método 1")
    CBE, CBpE = cols(*B), cols(*Bp)
    same(CBE, sp.Matrix([[1, 1, 2], [0, 1, 1], [1, 0, 2]]), "C_BE")
    same(CBpE, sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]]), "C_B'E")
    CEBp = sp.Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])
    same(CBpE * CEBp, sp.eye(3), "C_EB' es la inversa")
    same(CEBp * CBE, C, "C_BB' por el método 2")
    vB = col(2, -1, 1)
    same(C * vB, col(3, -3, 4), "[v]_B'")
    require(lin((2, -1, 1), B) == (3, 0, 4), "v = (3,0,4)")
    require(lin((3, -3, 4), Bp) == (3, 0, 4), "3(1,1,1) - 3(0,1,1) + 4(0,0,1)")
    CBpB = sp.Matrix([[-1, -3, -1], [0, -1, -1], [1, 2, 1]])
    same(C.inv(), CBpB, "C_B'B")
    same(C * CBpB, sp.eye(3), "C C^{-1}")
    require(lin((-1, 0, 1), B) == (1, 1, 1), "[b1']_B = (-1,0,1)")


@check("U1.T09.E2", "Polinomios: C_BE, C_EB para B={1,1+x,(1+x)^2} y [p]_B de 2-3x+x^2", page=P9)
def _():
    B = [(1, 0, 0), (1, 1, 0), (1, 2, 1)]
    CBE = cols(*B)
    same(CBE, sp.Matrix([[1, 1, 1], [0, 1, 2], [0, 0, 1]]), "C_BE")
    aug = sp.Matrix.hstack(CBE, sp.eye(3))
    a1 = rop(rop(aug, 1, 3, 1), 2, 3, 2)
    same(a1, sp.Matrix([[1, 1, 0, 1, 0, -1], [0, 1, 0, 0, 1, -2], [0, 0, 1, 0, 0, 1]]), "paso 1")
    a2 = rop(a1, 1, 2, 1)
    same(a2, sp.Matrix([[1, 0, 0, 1, -1, 1], [0, 1, 0, 0, 1, -2], [0, 0, 1, 0, 0, 1]]), "paso 2")
    CEB = sp.Matrix([[1, -1, 1], [0, 1, -2], [0, 0, 1]])
    same(CBE.inv(), CEB, "C_EB")
    same(CEB * col(2, -3, 1), col(6, -5, 1), "[p]_B")
    require(lin((6, -5, 1), B) == (2, -3, 1), "6 - 5(1+x) + (1+x)^2 = 2 - 3x + x^2")
    require(peval((2, -3, 1), -1) == 6, "la primera coordenada es p(-1)")
    require(lin((1, -2, 1), B) == (0, 0, 1), "x^2 = 1 - 2(1+x) + (1+x)^2")


@check("U1.T09.E3", "Base abstracta B'={v1+v2, v2-v3, v1+2v3}: C_B'B, C_BB' y [u]_B'", page=P9)
def _():
    CBpB = cols((1, 1, 0), (0, 1, -1), (1, 0, 2))
    same(CBpB, sp.Matrix([[1, 0, 1], [1, 1, 0], [0, -1, 2]]), "C_B'B")
    same(CBpB.det(), 1, "determinante")
    C = sp.Matrix([[2, -1, -1], [-2, 2, 1], [-1, 1, 1]])
    same(CBpB.inv(), C, "C_BB' por inversión")
    same(C * CBpB, sp.eye(3), "C_BB' C_B'B = I")
    # Por incógnitas vectoriales: v1 = 2w1 - 2w2 - w3, v2 = -w1 + 2w2 + w3, v3 = -w1 + w2 + w3.
    same(C, cols((2, -2, -1), (-1, 2, 1), (-1, 1, 1)), "columnas: [v_j]_B'")
    u = col(2, -1, 1)
    same(C * u, col(4, -5, -2), "[u]_B'")
    # 4w1 - 5w2 - 2w3 = u en coordenadas de B.
    require(lin((4, -5, -2), [(1, 1, 0), (0, 1, -1), (1, 0, 2)]) == (2, -1, 1), "4w1 - 5w2 - 2w3 = u")


@check("U1.T09.E4", "Recuperar B' a partir de C_BB' en R^2 y [v]_B'", page=P9)
def _():
    b1, b2 = (2, -1), (0, 2)
    C = sp.Matrix([[0, 1], [-1, 1]])
    w2 = tuple(-t for t in b1)
    w1 = tuple(p - q for p, q in zip(b2, w2))
    require(w1 == (2, 1) and w2 == (-2, 1), "w1, w2 por lectura de columnas")
    Cinv = C.inv()
    same(Cinv, sp.Matrix([[1, -1], [1, 0]]), "C_B'B")
    same(C.det(), 1, "determinante 1")
    require(lin((1, 1), [b1, b2]) == w1 and lin((-1, 0), [b1, b2]) == w2, "w1 = b1+b2, w2 = -b1")
    v = (2, 3)
    require(lin((1, 2), [b1, b2]) == v, "v = b1 + 2 b2")
    same(C * col(1, 2), col(2, 1), "[v]_B'")
    require(lin((2, 1), [w1, w2]) == v, "2w1 + w2 = v")
    require(lin((0, -1), [w1, w2]) == b1, "[b1]_B' = (0,-1)")
    require(lin((1, 1), [w1, w2]) == b2, "[b2]_B' = (1,1)")


@check("U1.T09.E5", "Base adaptada a un plano de R^3: C_BE, C_EB y ecuaciones en coordenadas", page=P9)
def _():
    u1, u2, u3 = (2, 1, 0), (1, 1, 1), (0, 0, 1)
    f = lambda v: v[0] - 2 * v[1] + v[2]  # noqa: E731
    require(f(u1) == 0 and f(u2) == 0 and f(u3) == 1, "u1, u2 en el plano; u3 no")
    CBE = cols(u1, u2, u3)
    same(CBE, sp.Matrix([[2, 1, 0], [1, 1, 0], [0, 1, 1]]), "C_BE")
    same(CBE.det(), 1, "determinante")
    CEB = sp.Matrix([[1, -1, 0], [-1, 2, 0], [1, -2, 1]])
    same(CBE.inv(), CEB, "C_EB")
    same(CBE * CEB, sp.eye(3), "producto")
    # y3 = x - 2y + z, y2 = -x + 2y, y1 = x - y.
    for v in [(3, 1, -1), (1, 2, 3), (0, 0, 0), (-2, 5, 1)]:
        y = CEB * col(*v)
        require(y[0] == v[0] - v[1] and y[1] == -v[0] + 2 * v[1] and y[2] == f(v), "fórmulas de y1, y2, y3")
    same(CEB * col(3, 1, -1), col(2, -1, 0), "[v]_B para v=(3,1,-1)")
    require(lin((2, -1), [u1, u2]) == (3, 1, -1), "2u1 - u2")
    # La recta L = gen{u1} = {y2 = y3 = 0}.
    for t in (-2, 1, 3):
        y = CEB * col(*lin((t,), [u1]))
        require(y[0] == t and y[1] == 0 and y[2] == 0, "L en coordenadas")


# ---------------------------------------------------------------------------
# 1.10 Códigos lineales (esta lección)
# ---------------------------------------------------------------------------
def systematic(A):
    """G = (I_k | A) y H = (A^t | I_{n-k}) a partir de A de k x (n-k)."""
    k, r = len(A), len(A[0])
    G = [[int(i == j) for j in range(k)] + list(A[i]) for i in range(k)]
    At = gf_transpose(A)
    H = [list(At[i]) + [int(i == j) for j in range(r)] for i in range(r)]
    return G, H


def words_of(G):
    """Todas las palabras aG con a en Z2^k (en el orden de bits(k))."""
    return {a: gf_rowmul(a, G) for a in bits(len(G))}


def decode_syndrome(H, v):
    """Corrige un error: si s=Hv^t es una columna de H, invierte ese bit."""
    s = gf_vec(H, v)
    if not any(s):
        return tuple(v)
    cols_h = [tuple(H[i][j] for i in range(len(H))) for j in range(len(H[0]))]
    if s in cols_h:
        j = cols_h.index(s)
        return tuple(x ^ int(i == j) for i, x in enumerate(v))
    return None


@check("U1.T10.E1", "Código de paridad (4,3): G, H, ocho palabras, d=2, detecta un error", page=P10)
def _():
    A = [[1], [1], [1]]
    G, H = systematic(A)
    require(G == [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]] and H == [[1, 1, 1, 1]], "G = (I3|1^t), H = (1 1 1 1)")
    require(gf_matmul(G, gf_transpose(H)) == [[0], [0], [0]], "G H^t = 0")
    W = set(words_of(G).values())
    require(W == {v for v in bits(4) if gf_vec(H, v) == (0,)} and len(W) == 8, "C = nul(H) con 2^3 palabras")
    require(W == {v for v in bits(4) if sum(v) % 2 == 0}, "palabras de peso par")
    require(min_distance(W) == 2, "d = 2")
    require(gf_rank(H) == 1 and 4 - gf_rank(H) == 3, "rango-nulidad")
    require(gf_vec(H, (1, 0, 1, 1)) == (1,) and gf_vec(H, (1, 0, 1, 0)) == (0,), "síndromes")
    # Un error se detecta, dos no.
    u = (1, 0, 1, 0)
    require(all(gf_vec(H, tuple(x ^ int(i == j) for i, x in enumerate(u))) == (1,) for j in range(4)), "un error: s=1")
    require(gf_vec(H, (0, 1, 1, 0)) == (0,) and (0, 1, 1, 0) in W and hamming(u, (0, 1, 1, 0)) == 2, "dos errores no se detectan")
    # Todas las posiciones del error producen el mismo síndrome: no se puede corregir.
    require(len({tuple(x ^ int(i == j) for i, x in enumerate(u)) for j in range(4)}) == 4, "cuatro candidatos")
    require(gf_rowmul((1, 0, 1), G) == (1, 0, 1, 0), "codificación de 101")
    listadas = {(0, 0, 0): (0, 0, 0, 0), (1, 0, 0): (1, 0, 0, 1), (0, 1, 0): (0, 1, 0, 1), (0, 0, 1): (0, 0, 1, 1),
                (1, 1, 0): (1, 1, 0, 0), (1, 0, 1): (1, 0, 1, 0), (0, 1, 1): (0, 1, 1, 0), (1, 1, 1): (1, 1, 1, 1)}
    require(words_of(G) == listadas, "las ocho palabras del texto")
    require({tuple(x ^ int(i == j) for i, x in enumerate((1, 0, 1, 1))) for j in range(4)} == {(0, 0, 1, 1), (1, 1, 1, 1), (1, 0, 0, 1), (1, 0, 1, 0)}
            and all(c in W for c in {(0, 0, 1, 1), (1, 1, 1, 1), (1, 0, 0, 1), (1, 0, 1, 0)}), "cuatro candidatos, todos palabras código")
    # Cada columna de H es 1 (columnas repetidas): no corrige.
    require(len({tuple(H[i][j] for i in range(1)) for j in range(4)}) == 1, "columnas repetidas")


@check("U1.T10.E3", "Código (6,3) con d=3: de H a G, enumeración, distancia mínima y corrección de un error", page=P10)
def _():
    H = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 0, 1]]
    cols_h = [tuple(H[i][j] for i in range(3)) for j in range(6)]
    require(len(set(cols_h)) == 6 and all(any(c) for c in cols_h), "columnas no nulas y distintas")
    A = [[H[j][i] for j in range(3)] for i in range(3)]
    require(A == [[0, 1, 1], [1, 0, 1], [1, 1, 0]], "A = (parte izquierda de H)^t")
    G, H2 = systematic(A)
    require(H2 == H, "H = (A^t | I3)")
    require(G == [[1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0]], "G = (I3|A)")
    require(gf_matmul(G, gf_transpose(H)) == [[0] * 3] * 3, "G H^t = 0")
    require(gf_rank(H) == 3 and len(gf_nullspace(H)) == 3, "rango 3, nulidad 3")
    W = words_of(G)
    require(set(W.values()) == {x for x in bits(6) if gf_vec(H, x) == (0, 0, 0)} == gf_span(G), "C = nul(H) = fil(G)")
    require(len(set(W.values())) == 8, "2^3 = 8 palabras")
    pesos = sorted(weight(w) for w in W.values())
    require(pesos == [0, 3, 3, 3, 3, 4, 4, 4], "pesos 0,3,3,3,3,4,4,4")
    require(min_distance(W.values()) == 3, "d = 3")
    # Las filas de G pesan 3, pero d se calcula con todas las palabras: gen{1110,0111} tiene d=2.
    require(min_distance(gf_span([(1, 1, 1, 0), (0, 1, 1, 1)])) == 2 and gf_vecadd((1, 1, 1, 0), (0, 1, 1, 1)) == (1, 0, 0, 1),
            "filas de peso 3 con suma de peso 2")
    require(not is_subspace_z2({(0, 0, 0), (1, 1, 0), (0, 1, 1)}), "{000,110,011} no es lineal")
    require(W[(1, 1, 0)] == (1, 1, 0, 1, 1, 0), "codificación de 110")
    v2 = (0, 0, 0, 1, 1, 0)  # 110110 con errores en las posiciones 1 y 2
    require(hamming(v2, W[(1, 1, 0)]) == 2 and gf_vec(H, v2) == gf_vecadd(cols_h[0], cols_h[1]) == cols_h[2],
            "dos errores: síndrome h1+h2 = h3")
    require(decode_syndrome(H, v2) == (0, 0, 1, 1, 1, 0) == W[(0, 0, 1)], "la 'corrección' da la palabra del mensaje 001")
    # Tabla de pesos del texto.
    require([(a, weight(w)) for a, w in sorted(W.items())] == [((0, 0, 0), 0), ((0, 0, 1), 3), ((0, 1, 0), 3), ((0, 1, 1), 4),
                                                                ((1, 0, 0), 3), ((1, 0, 1), 4), ((1, 1, 0), 4), ((1, 1, 1), 3)],
            "tabla de pesos")
    require(W[(1, 0, 1)] == (1, 0, 1, 1, 0, 1) and W[(0, 1, 1)] == (0, 1, 1, 0, 1, 1) and W[(1, 1, 1)] == (1, 1, 1, 0, 0, 0),
            "palabras de la tabla")
    v = (1, 1, 0, 1, 0, 0)
    require(hamming(v, W[(1, 1, 0)]) == 1, "un error en la posición 5")
    require(gf_vec(H, v) == (0, 1, 0) and cols_h[4] == (0, 1, 0), "síndrome = columna 5")
    require(decode_syndrome(H, v) == W[(1, 1, 0)], "corrige")
    # Corrige cualquier error simple en cualquier palabra.
    for w in W.values():
        require(decode_syndrome(H, w) == w, "palabra sin error")
        for j in range(6):
            e = tuple(x ^ int(i == j) for i, x in enumerate(w))
            require(decode_syndrome(H, e) == w, f"error en {j + 1}")
    # Distancia 3: detecta 2 y corrige 1; con dos errores el decodificador se equivoca o no detecta.
    u = W[(1, 1, 0)]
    e2 = tuple(x ^ int(i in (0, 1)) for i, x in enumerate(u))
    require(gf_vec(H, e2) == (1, 1, 1) or gf_vec(H, e2) != (0, 0, 0), "dos errores dan síndrome no nulo (se detectan)")
    require(all(gf_vec(H, tuple(x ^ int(i in p) for i, x in enumerate(u))) != (0, 0, 0)
                for p in combinations(range(6), 2)), "todo par de errores se detecta")


@check("U1.T10.E4", "Hamming (7,4): H, dimensión, base, G, codificación, corrección y falla con dos errores", page=P10)
def _():
    H = [[1, 1, 0, 1, 1, 0, 0], [1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 0, 0, 1]]
    cols_h = [tuple(H[i][j] for i in range(3)) for j in range(7)]
    require(set(cols_h) == {c for c in bits(3) if any(c)}, "las columnas son los 7 vectores no nulos de Z2^3")
    require(len(set(cols_h)) == 7, "distintas")
    require(gf_rank(H) == 3, "rango 3")
    require(7 - gf_rank(H) == 4 and len(gf_nullspace(H)) == 4, "dim nul(H) = 4")
    A = [[H[j][i] for j in range(3)] for i in range(4)]
    require(A == [[1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]], "A")
    G, H2 = systematic(A)
    require(H2 == H, "H = (A^t|I3)")
    require(G == [[1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]], "G = (I4|A)")
    require(gf_matmul(G, gf_transpose(H)) == [[0] * 3] * 4, "G H^t = 0")
    C = {x for x in bits(7) if gf_vec(H, x) == (0, 0, 0)}
    require(C == gf_span(G) and len(C) == 16, "C = nul(H) = fil(G), 16 palabras")
    require(gf_rank(G) == 4, "las filas de G son LI")
    pesos = sorted(weight(c) for c in C)
    require([pesos.count(k) for k in range(8)] == [1, 0, 0, 7, 7, 0, 0, 1], "distribución de pesos")
    require(min_distance(C) == 3, "d = 3")
    require(min(hamming(a, b) for a in C for b in C if a != b) == 3, "distancia mínima entre palabras")
    # Codificación de 1011.
    a = (1, 0, 1, 1)
    u = gf_rowmul(a, G)
    require(u == (1, 0, 1, 1, 0, 1, 0), "u = 1011010")
    require(gf_vecadd(G[0], G[2], G[3]) == u, "g1+g3+g4")
    require(gf_vec(H, u) == (0, 0, 0), "síndrome nulo")
    # Un error en la posición 3.
    v = tuple(x ^ int(i == 2) for i, x in enumerate(u))
    require(v == (1, 0, 0, 1, 0, 1, 0), "v = 1001010")
    require(gf_vec(H, v) == (0, 1, 1) == cols_h[2], "síndrome = columna 3")
    require(decode_syndrome(H, v) == u, "corrección")
    require(decode_syndrome(H, v)[:4] == a, "mensaje recuperado")
    # Corrección de todos los errores simples en todas las palabras.
    for w in C:
        for j in range(7):
            e = tuple(x ^ int(i == j) for i, x in enumerate(w))
            require(gf_vec(H, e) == cols_h[j] and decode_syndrome(H, e) == w, "error simple")
    # Dos errores: el síndrome es h_i + h_j = h_k y el decodificador produce otra palabra del código.
    for i, j in combinations(range(7), 2):
        e = tuple(x ^ int(t in (i, j)) for t, x in enumerate(u))
        s = gf_vec(H, e)
        k = cols_h.index(s)
        require(s == gf_vecadd(cols_h[i], cols_h[j]) and k not in (i, j), "h_i + h_j = h_k con k distinto")
        d = decode_syndrome(H, e)
        require(d in C and d != u and hamming(d, u) == 3, "decodifica otra palabra, a distancia 3")
    # Ejemplo concreto: errores en las posiciones 1 y 2.
    e = tuple(x ^ int(i in (0, 1)) for i, x in enumerate(u))
    require(e == (0, 1, 1, 1, 0, 1, 0), "v = 0111010")
    require(gf_vec(H, e) == (0, 1, 1) == cols_h[2], "síndrome = h1 + h2 = h3")
    d = decode_syndrome(H, e)
    require(d == (0, 1, 0, 1, 0, 1, 0) and d in C and d[:4] == (0, 1, 0, 1), "se obtiene 0101010, mensaje 0101")
    require(gf_vecadd(u, d) == (1, 1, 1, 0, 0, 0, 0) and (1, 1, 1, 0, 0, 0, 0) in C, "la diferencia es una palabra de peso 3")
    # Todas las columnas no nulas y distintas <=> corrige un error: quitar una columna lo rompe.
    H_malo = [r[:] for r in H]
    for r in H_malo:
        r[6] = r[5]
    require(len({tuple(H_malo[i][j] for i in range(3)) for j in range(7)}) == 6, "columna repetida")
    # La forma general de Hamming con r=2 y r=4.
    for r in (2, 3, 4):
        n = 2 ** r - 1
        Hr = [[(j + 1) >> (r - 1 - i) & 1 for j in range(n)] for i in range(r)]
        require(gf_rank(Hr) == r and n - gf_rank(Hr) == n - r, f"Hamming ({n},{n - r})")
    # Hamming (3,1) es el código de repetición.
    H31 = [[0, 1, 1], [1, 0, 1]]
    require(set(x for x in bits(3) if gf_vec(H31, x) == (0, 0)) == {(0, 0, 0), (1, 1, 1)}, "Hamming (3,1)")


@check("U1.T10.E2", "Repetición (5,1): d=5, detecta 4 y corrige 2; con tres errores falla", page=P10)
def _():
    A = [[1, 1, 1, 1]]
    G, H = systematic(A)
    require(G == [[1, 1, 1, 1, 1]], "G = (11111)")
    require(H == [[1, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1]], "H = (A^t | I4)")
    require(gf_matmul(G, gf_transpose(H)) == [[0, 0, 0, 0]], "G H^t = 0")
    C = {x for x in bits(5) if gf_vec(H, x) == (0, 0, 0, 0)}
    require(C == {(0, 0, 0, 0, 0), (1, 1, 1, 1, 1)} == gf_span(G), "C = {00000, 11111}")
    require(min_distance(C) == 5, "d = 5")
    # Corrección por mayoría: hasta 2 errores.
    for w in C:
        for t in (0, 1, 2):
            for p in combinations(range(5), t):
                v = tuple(x ^ int(i in p) for i, x in enumerate(w))
                dec = (1,) * 5 if sum(v) >= 3 else (0,) * 5
                require(dec == w, f"mayoría corrige {t} errores")
    require(sum((1, 0, 1, 1, 0)) == 3 and hamming((1, 0, 1, 1, 0), (1, 1, 1, 1, 1)) == 2, "10110: dos errores, tres unos")
    require(sum((1, 0, 0, 1, 0)) == 2 and hamming((1, 0, 0, 1, 0), (1, 1, 1, 1, 1)) == 3, "10010: tres errores, dos unos")
    require(gf_vec(H, (1, 0, 1, 1, 0)) == (1, 0, 0, 1), "síndrome de 10110")
    # Con 3 errores la mayoría se equivoca.
    v = (1, 1, 1, 0, 0)
    require(sum(v) >= 3 and hamming(v, (1, 1, 1, 1, 1)) == 2 and hamming(v, (0, 0, 0, 0, 0)) == 3, "3 errores sobre 00000")
    # Detecta hasta 4 errores: toda palabra a distancia 1..4 de una palabra del código no está en C.
    for w in C:
        for t in (1, 2, 3, 4):
            for p in combinations(range(5), t):
                require(tuple(x ^ int(i in p) for i, x in enumerate(w)) not in C, f"detecta {t} errores")
    # Fórmulas: detecta d-1 y corrige floor((d-1)/2).
    require((5 - 1, (5 - 1) // 2) == (4, 2), "d=5")
    require((2 - 1, (2 - 1) // 2) == (1, 0) and (3 - 1, (3 - 1) // 2) == (2, 1), "d=2 y d=3")
