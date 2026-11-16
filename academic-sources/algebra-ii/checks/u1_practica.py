"""Comprobaciones de los ejercicios de la práctica de la Unidad 1 (espacios vectoriales).

Cada función recalcula los resultados publicados desde los datos del enunciado: independencia,
rangos, bases de fil/col/nul, coordenadas y matrices de cambio sobre R (aritmética racional exacta) y
cuentas sobre Z_2 con aritmética modular exacta (gf_*). Convenciones: base canónica de P_n[R]
ordenada {1, x, ..., x^n} (un polinomio es su vector de coeficientes (c0, c1, ...)); base canónica de
R^{2x2} ordenada {E11, E12, E21, E22}; [v]_B como columna; C_{BB'} con columnas [b_j]_{B'}.
Los ejercicios con verificacion "razonamiento" (U1.17, U1.22, U1.25) no tienen función aquí.
"""
from itertools import product

import sympy as sp
from content_pipeline.mathcheck import (
    check, gf_dot, gf_matmul, gf_nullspace, gf_rank, gf_rref, gf_span, hamming, min_distance, require, same, weight,
)

PG = "/algebra-ii/unidad-1/practica/"
INI = PG + "nivel-inicial/"
INT = PG + "nivel-intermedio/"
AVA = PG + "nivel-avanzado/"
GUIA = PG + "guia-integradora/"

R = sp.Rational


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def col(*entries):
    """Vector columna."""
    return sp.Matrix(list(entries))


def cols(*vectors):
    """Matriz cuyas columnas son los vectores dados (tuplas)."""
    return sp.Matrix.hstack(*[col(*v) for v in vectors])


def rows_of(*vectors):
    """Matriz cuyas filas son los vectores dados."""
    return sp.Matrix([list(v) for v in vectors])


def lista(M):
    """Entradas de una matriz columna como lista."""
    return [M[i, 0] for i in range(M.shape[0])]


def gen_igual(X, Y):
    """Dos matrices (columnas = generadores) generan el mismo subespacio de R^n."""
    return X.rank() == Y.rank() == sp.Matrix.hstack(X, Y).rank()


def en_gen(base, v):
    """v (columna) pertenece al generado por las columnas de base."""
    return sp.Matrix.hstack(base, v).rank() == base.rank()


def gf_mat_t(H):
    """Traspuesta de una lista de listas."""
    return [list(r) for r in zip(*H)]


def sindrome(H, v):
    """s = H v^t sobre Z_2, como lista."""
    return [gf_dot(row, v) for row in H]


def palabras(G):
    """Todas las palabras del código generado por las filas de G."""
    return sorted(gf_span(G))


def suma2(u, v):
    return tuple((a + b) % 2 for a, b in zip(u, v))


# ---------------------------------------------------------------------------
# Nivel inicial
# ---------------------------------------------------------------------------
@check("U1.01", "Aritmética en Z2 y Z5; Z4 no es cuerpo", page=INI)
def _():
    require((1 + 1 + 1) % 2 == 1 and (1 * 1 + 1) % 2 == 0, "cuentas en Z2")
    require([[(a + b) % 2 for b in (0, 1)] for a in (0, 1)] == [[0, 1], [1, 0]], "tabla de la suma en Z2")
    require([[(a * b) % 2 for b in (0, 1)] for a in (0, 1)] == [[0, 0], [0, 1]], "tabla del producto en Z2")
    require((3 * 2) % 5 == 1, "inverso de 3 en Z5")
    require([x for x in range(5) if (3 * x) % 5 == 4] == [3], "3x=4 en Z5 tiene la única solución x=3")
    tabla4 = [[(a * b) % 4 for b in range(4)] for a in range(4)]
    require(tabla4 == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 0, 2], [0, 3, 2, 1]], "tabla del producto en Z4")
    require(tabla4[2][2] == 0, "2*2=0 en Z4")
    require(1 not in tabla4[2], "2 no tiene inverso en Z4")
    require([a for a in range(1, 4) if 1 in tabla4[a]] == [1, 3], "solo 1 y 3 son inversibles en Z4")


@check("U1.02", "Subespacios de R^3: plano, plano afín y unión de planos", page=INI)
def _():
    n = sp.Matrix([[1, 2, -1]])
    ns = n.nullspace()
    require(len(ns) == 2, "S es un plano")
    base = [(1, 0, 1), (0, 1, 2)]
    for b in base:
        require(sum(a * c for a, c in zip((1, 2, -1), b)) == 0, "generadores en S")
    require(gen_igual(cols(*base), sp.Matrix.hstack(*ns)), "la base dada genera S")
    require(cols(*base).rank() == 2, "base LI")
    # cerradura de S sobre combinaciones enteras
    for a, b in product(range(-2, 3), repeat=2):
        v = tuple(a * x + b * y for x, y in zip(base[0], base[1]))
        require(v[0] + 2 * v[1] - v[2] == 0, "S cerrado")
    require(0 + 0 + 0 != 1, "0 no está en T")
    u, v = (1, 0, 0), (0, 1, 0)
    s = tuple(a + b for a, b in zip(u, v))
    require(u[0] * u[1] == 0 and v[0] * v[1] == 0 and s[0] * s[1] == 1, "U no es cerrado por la suma")


@check("U1.03", "Pertenencia al generado, ecuación del plano y parámetro", page=INI)
def _():
    v1, v2 = col(1, 0, 1), col(2, 1, 3)
    B = sp.Matrix.hstack(v1, v2)
    w, wp = col(4, 1, 5), col(1, 1, 1)
    same(2 * v1 + v2, w, "w = 2 v1 + v2")
    require(en_gen(B, w), "w en S")
    require(not en_gen(B, wp), "w' no está en S")
    ns = sp.Matrix([[1, 0, 1], [2, 1, 3]]).nullspace()
    require(len(ns) == 1, "S es un plano")
    require(gen_igual(ns[0], col(1, 1, -1)), "la normal es (1,1,-1)")
    for v in (v1, v2, w):
        require(v[0] + v[1] - v[2] == 0, "ecuación x+y-z=0")
    require(wp[0] + wp[1] - wp[2] == 1, "w' no cumple")
    ks = [k for k in range(-6, 7) if en_gen(B, col(3, k, 6))]
    require(ks == [3], "solo k=3")
    same(-3 * v1 + 3 * v2, col(3, 3, 6), "comprobación de k=3")


@check("U1.04", "La misma terna: LI en R^3 y LD en Z2^3", page=INI)
def _():
    U = [(1, 1, 0), (0, 1, 1), (1, 0, 1)]
    same(cols(*U).det(), 2, "det en R")
    require(cols(*U).rank() == 3, "LI en R")
    require(gf_rank(U, 2) == 2, "rango 2 en Z2")
    require(suma2(suma2(U[0], U[1]), U[2]) == (0, 0, 0), "suma nula en Z2")
    require(suma2(U[0], U[1]) == U[2], "u3 = u1+u2")
    require(len(gf_span(U)) == 4, "el generado tiene 4 elementos")
    require(sorted(gf_span(U)) == [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)], "elementos")


@check("U1.05", "Cuatro afirmaciones V/F (subespacios y conteos en Z2)", page=INI)
def _():
    # a) {xy=0} no es cerrado por la suma
    require(1 * 0 == 0 and 0 * 1 == 0 and 1 * 1 != 0, "contraejemplo de a)")
    # b) un conjunto con el nulo es LD (ejemplo y regla)
    require(cols((0, 0), (1, 2)).rank() < 2, "ejemplo de b)")
    # c) 7 subespacios de dimensión 1 en Z2^3 (y 7 de dimensión 2)
    vect = [v for v in product((0, 1), repeat=3) if any(v)]
    rectas = {frozenset(gf_span([v])) for v in vect}
    require(len(rectas) == 7, "7 subespacios de dimensión 1")
    planos = {frozenset(gf_span([u, v])) for u in vect for v in vect if gf_rank([u, v]) == 2}
    require(len(planos) == 7, "7 subespacios de dimensión 2")
    for r in rectas:
        require(all(suma2(a, b) in r for a in r for b in r), "cerrado por la suma")
    # d) dimensión 3 en Z2^5 da 8 elementos
    require(len(gf_span([(1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 1, 1)])) == 8, "2^3 = 8")


@check("U1.06", "fil, col, nul de una matriz 3x4 y rango-nulidad", page=INI)
def _():
    A = sp.Matrix([[1, 2, 0, 1], [2, 4, 1, 5], [1, 2, 1, 4]])
    Rr, piv = A.rref()
    require(tuple(piv) == (0, 2), "pivotes en las columnas 1 y 3")
    require(A.rank() == 2, "rango 2")
    # F2-2F1, F3-F1, F3-F2
    E = sp.Matrix([[1, 2, 0, 1], [0, 0, 1, 3], [0, 0, 0, 0]])
    same(E, Rr, "escalonada (ya reducida)")
    fil = rows_of((1, 2, 0, 1), (0, 0, 1, 3))
    require(gen_igual(fil.T, A.T), "base de fil")
    colb = cols((1, 2, 1), (0, 1, 1))
    require(gen_igual(colb, A), "base de col")
    nb = [col(-2, 1, 0, 0), col(-1, 0, -3, 1)]
    for v in nb:
        same(A * v, sp.zeros(3, 1), "A v = 0")
    require(gen_igual(sp.Matrix.hstack(*nb), sp.Matrix.hstack(*A.nullspace())), "base de nul")
    require(A.rank() + len(A.nullspace()) == 4, "rango-nulidad")
    same(colb * col(1, 1), col(1, 3, 2), "b = c1 + c2")
    require(en_gen(colb, col(1, 3, 2)), "b en col(A)")


@check("U1.07", "Coordenadas, orden de la base y tamaño de [v]_B", page=INI)
def _():
    PB = cols((2, 1), (1, 1))
    PBp = cols((1, 1), (2, 1))
    v = col(5, 3)
    same(PB.inv() * v, col(2, 1), "[v]_B")
    same(PBp.inv() * v, col(1, 2), "[v]_B'")
    same(PB * col(2, 1), v, "reconstrucción en B")
    same(PBp * col(1, 2), v, "reconstrucción en B'")
    p = col(3, -1, 2)
    Bpp = cols((0, 0, 1), (0, 1, 0), (1, 0, 0))
    same(Bpp.inv() * p, col(2, -1, 3), "[p]_B''")
    # matriz 2x2: coordenadas en {E11,E12,E21,E22}
    M = [[1, 2], [0, 3]]
    coords = [M[0][0], M[0][1], M[1][0], M[1][1]]
    require(coords == [1, 2, 0, 3] and len(coords) == 4, "[M] tiene 4 componentes")


@check("U1.08", "Código de paridad (5,4)", page=INI)
def _():
    H = [[1, 1, 1, 1, 1]]
    require(gf_rank(H) == 1, "rango de H")
    N = gf_nullspace(H)
    require(len(N) == 4, "dim 4")
    words = [v for v in product((0, 1), repeat=5) if gf_dot(H[0], v) == 0]
    require(len(words) == 16 and sorted(words) == palabras(N), "16 palabras")
    G = [[1, 0, 0, 0, 1], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    require(gf_rank(G) == 4, "G de rango 4")
    require(gf_matmul(G, gf_mat_t(H)) == [[0]] * 4, "G H^t = 0")
    require(gf_matmul([[1, 0, 1, 1]], G) == [[1, 0, 1, 1, 1]], "1011 -> 10111")
    require(min_distance(words) == 2, "d = 2")
    require(sindrome(H, (1, 0, 1, 0, 1)) == [1], "10101 se detecta")
    require(sindrome(H, (0, 1, 1, 1, 1)) == [0], "01111 no se detecta")
    for j in range(5):
        e = tuple(int(i == j) for i in range(5))
        require(sindrome(H, e) == [1], "un error siempre se detecta")


# ---------------------------------------------------------------------------
# Nivel intermedio
# ---------------------------------------------------------------------------
@check("U1.09", "Subespacio de R^{2x2} con dos condiciones", page=INT)
def _():
    # coordenadas (a11, a12, a21, a22)
    cond = sp.Matrix([[1, 0, 0, 1], [0, 1, -2, 0]])
    ns = cond.nullspace()
    require(len(ns) == 2, "dim S = 2")
    B1, B2 = col(1, 0, 0, -1), col(0, 2, 1, 0)
    for b in (B1, B2):
        same(cond * b, sp.zeros(2, 1), "base en S")
    require(gen_igual(sp.Matrix.hstack(B1, B2), sp.Matrix.hstack(*ns)), "base de S")
    Mm = col(3, 4, 2, -3)
    same(cond * Mm, sp.zeros(2, 1), "M en S")
    same(3 * B1 + 2 * B2, Mm, "[M]_B = (3,2)")
    Nn = col(1, 2, 1, 1)
    require(cond * Nn != sp.zeros(2, 1), "N no está en S")
    # cerradura con combinaciones enteras
    for a, c, d, e in product(range(-1, 2), repeat=4):
        X = a * B1 + c * B2
        Y = d * B1 + e * B2
        same(cond * (X + Y), sp.zeros(2, 1), "cerrada por suma")


@check("U1.10", "Generadores y ecuaciones en R^4; intersección", page=INT)
def _():
    v1, v2, v3 = col(1, 0, 1, 2), col(0, 1, -1, 1), col(1, 1, 0, 3)
    same(v1 + v2, v3, "v3 = v1 + v2")
    Gm = sp.Matrix.hstack(v1, v2, v3)
    require(Gm.rank() == 2, "dim S = 2")
    E = sp.Matrix([[1, -1, -1, 0], [2, 1, 0, -1]])
    for v in (v1, v2, v3):
        same(E * v, sp.zeros(2, 1), "ecuaciones de S")
    require(len(E.nullspace()) == 2, "las ecuaciones definen un subespacio de dim 2")
    require(gen_igual(sp.Matrix.hstack(*E.nullspace()), Gm), "nul(E) = S")
    Tm = sp.Matrix([[1, 1, -1, 0], [0, 1, 0, -2]])
    nt = Tm.nullspace()
    require(len(nt) == 2, "dim T = 2")
    t1, t2 = col(1, 0, 1, 0), col(-2, 2, 0, 1)
    for t in (t1, t2):
        same(Tm * t, sp.zeros(2, 1), "base de T")
    require(gen_igual(sp.Matrix.hstack(t1, t2), sp.Matrix.hstack(*nt)), "T = gen{t1,t2}")
    require(sp.Matrix.vstack(E, Tm).rank() == 4, "S ∩ T = {0}")
    require(sp.Matrix.hstack(v1, v2, t1, t2).rank() == 4, "S + T = R^4")
    # sustitución simbólica por muestreo: (a,b,a-b,2a+b) en las ecuaciones de T
    for a, b in product(range(-3, 4), repeat=2):
        w = col(a, b, a - b, 2 * a + b)
        same(Tm * w, col(2 * b, -4 * a - b), "ecuaciones de T sobre S")


@check("U1.11", "Tres contraejemplos", page=INT)
def _():
    u, v, w = (1, 0), (2, 0), (0, 1)
    require(cols(u, v, w).rank() < 3, "LD")
    require(not en_gen(cols(u, v), col(*w)), "w no está en gen{u,v}")
    S, T = cols((1, 0)), cols((0, 1))
    s = col(1, 1)
    require(not en_gen(S, s) and not en_gen(T, s), "(1,1) no está en la unión")
    require(en_gen(S, col(1, 0)) and en_gen(T, col(0, 1)), "los sumandos sí")
    A = sp.Matrix([[1, 0], [0, 0]])
    B = sp.Matrix([[0, 0], [0, 1]])
    require(A.rank() == 1 and B.rank() == 1 and (A + B).rank() == 2, "rango de la suma")


@check("U1.12", "Base de P_2[R] con parámetro k", page=INT)
def _():
    def D(k):
        return cols((1, 1, 0), (1, 0, k), (k, 0, 1)).det()

    for k in range(-5, 6):
        same(D(k), k * k - 1, f"det para k={k}")  # polinomio de grado 2 coincide en 11 puntos
    require(cols((1, 1, 0), (1, 0, 1), (1, 0, 1)).rank() == 2, "dim 2 para k=1")
    require(cols((1, 1, 0), (1, 0, -1), (-1, 0, 1)).rank() == 2, "dim 2 para k=-1")
    same(col(1, 0, 1) - col(1, 0, 1), sp.zeros(3, 1), "k=1: p2 - p3 = 0")
    same(col(1, 0, -1) + col(-1, 0, 1), sp.zeros(3, 1), "k=-1: p2 + p3 = 0")
    require([k for k in range(-5, 6) if D(k) == 0] == [-1, 1], "solo k=±1")
    same(D(2), 3, "k=2")
    same(D(0), -1, "k=0")


@check("U1.13", "Extensión a una base en R^4 y en Z2^4", page=INT)
def _():
    v1, v2 = (1, 2, 0, 1), (0, 1, 1, -1)
    require(cols(v1, v2).rank() == 2, "v1, v2 LI")
    M = cols(v1, v2, (0, 0, 1, 0), (0, 0, 0, 1))
    same(M, sp.Matrix([[1, 0, 0, 0], [2, 1, 0, 0], [0, 1, 1, 0], [1, -1, 0, 1]]), "matriz publicada")
    same(M.det(), 1, "det = 1")
    w1, w2 = (1, 1, 0, 0), (0, 1, 1, 0)
    require(gf_rank([w1, w2]) == 2, "w1, w2 LI en Z2")
    base = [w1, w2, (0, 0, 1, 0), (0, 0, 0, 1)]
    require(gf_rank(base) == 4, "base de Z2^4")
    require(sp.Matrix(gf_mat_t(base)).det() == 1, "det 1 (publicado)")
    require(palabras([w1, w2]) == [(0, 0, 0, 0), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 0)], "4 elementos")
    require(suma2(w1, w2) == (1, 0, 1, 0), "w1 + w2")


@check("U1.14", "Cambio de coordenadas entre dos bases de R^3", page=INT)
def _():
    PB = cols((1, 1, 0), (0, 1, 0), (1, 1, 1))
    PBp = cols((1, 1, 1), (0, 1, 1), (0, 0, 1))
    C = PBp.inv() * PB
    same(C, sp.Matrix([[1, 0, 1], [0, 1, 0], [-1, -1, 0]]), "C_BB'")
    for j in range(3):
        same(PBp * col(*[C[i, j] for i in range(3)]), col(*[PB[i, j] for i in range(3)]), f"columna {j + 1}")
    vB = col(2, -1, 3)
    same(C * vB, col(5, -1, -1), "[v]_B'")
    same(PB * vB, col(5, 4, 3), "v")
    same(PBp * col(5, -1, -1), col(5, 4, 3), "v desde B'")
    Ci = PB.inv() * PBp
    same(Ci, sp.Matrix([[0, -1, -1], [0, 1, 0], [1, 1, 1]]), "C_B'B")
    same(C * Ci, sp.eye(3), "C C^-1 = I")
    same(C.inv(), Ci, "C_B'B es la inversa")


@check("U1.15", "Cambio de coordenadas en P_2[R]", page=INT)
def _():
    PB = cols((1, 0, 0), (1, 1, 0), (0, 1, 1))      # {1, 1+x, x+x^2}
    PBp = cols((1, 0, 0), (-1, 1, 0), (1, -2, 1))   # {1, x-1, (x-1)^2}
    C = PBp.inv() * PB
    same(C, sp.Matrix([[1, 2, 2], [0, 1, 3], [0, 0, 1]]), "C_BB'")
    p = col(2, 3, 1)
    pB = PB.inv() * p
    same(pB, col(0, 2, 1), "[p]_B")
    pBp = PBp.inv() * p
    same(pBp, col(6, 5, 1), "[p]_B'")
    same(C * pB, pBp, "C [p]_B = [p]_B'")
    same(6 * col(1, 0, 0) + 5 * col(-1, 1, 0) + col(1, -2, 1), p, "reconstrucción")


@check("U1.16", "Subespacio de Z2^4 y los mismos vectores en R^4", page=INT)
def _():
    w1, w2, w3 = (1, 1, 0, 1), (0, 1, 1, 1), (1, 0, 1, 0)
    require(suma2(w1, w2) == w3, "w3 = w1 + w2")
    require(gf_rank([w1, w2, w3]) == 2, "dim 2")
    W = palabras([w1, w2])
    require(W == [(0, 0, 0, 0), (0, 1, 1, 1), (1, 0, 1, 0), (1, 1, 0, 1)], "elementos")
    require(sorted(gf_span([w1, w2, w3])) == W, "mismo generado")
    H = [[1, 1, 1, 0], [0, 1, 0, 1]]
    for w in W:
        require(sindrome(H, w) == [0, 0], "ecuaciones de W")
    require(len(gf_nullspace(H)) == 2 and sorted(gf_span(gf_nullspace(H))) == W, "nul(H) = W")
    require(sindrome(H, (1, 0, 0, 1)) != [0, 0], "1001 no está en W")
    require(cols(w1, w2, w3).rank() == 3, "dim 3 sobre R")
    require(cols(w1, w2).rank() == 2 and not en_gen(cols(w1, w2), col(*w3)), "w3 no es CL sobre R")
    require(sum(a + b for a, b in zip(w1, w2)) != sum(w3), "w1 + w2 != w3 en R")


@check("U1.18", "Hamming (7,4): codificar, corregir y fallar con dos errores", page=INT)
def _():
    G = [[1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]]
    H = [[1, 1, 0, 1, 1, 0, 0], [1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 0, 0, 1]]
    require(gf_matmul(G, gf_mat_t(H)) == [[0, 0, 0]] * 4, "G H^t = 0")
    require(gf_rank(G) == 4 and gf_rank(H) == 3, "rangos")
    ws = palabras(G)
    require(len(ws) == 16 and min_distance(ws) == 3, "(7,4) con d=3")
    u = tuple(gf_matmul([[1, 1, 0, 1]], G)[0])
    require(u == (1, 1, 0, 1, 1, 0, 0), "1101 -> 1101100")
    require(sindrome(H, u) == [0, 0, 0], "síndrome nulo")
    r = (1, 1, 0, 1, 0, 0, 0)
    s = sindrome(H, r)
    require(s == [1, 0, 0], "síndrome del recibido")
    pos = [j for j in range(7) if [H[i][j] for i in range(3)] == s]
    require(pos == [4], "posición 5")
    corr = list(r)
    corr[4] ^= 1
    require(tuple(corr) == u and hamming(r, u) == 1, "corrección")
    v = list(u)
    v[0] ^= 1
    v[6] ^= 1
    v = tuple(v)
    require(v == (0, 1, 0, 1, 1, 0, 1), "dos errores")
    s2 = sindrome(H, v)
    require(s2 == [1, 1, 1], "síndrome h4")
    pos2 = [j for j in range(7) if [H[i][j] for i in range(3)] == s2]
    require(pos2 == [3], "el decodificador cree error en 4")
    w = list(v)
    w[3] ^= 1
    w = tuple(w)
    require(w == (0, 1, 0, 0, 1, 0, 1) and w in ws and w != u, "entrega otra palabra código")
    require(w == tuple(G[1]), "es g2 (mensaje 0100)")


# ---------------------------------------------------------------------------
# Nivel avanzado
# ---------------------------------------------------------------------------
@check("U1.19", "Base abstracta {u+v, v+w, w+u}: sobre R sí, sobre Z2 no", page=AVA)
def _():
    C = cols((1, 1, 0), (0, 1, 1), (1, 0, 1))  # C_{B'B}
    same(C.det(), 2, "det")
    Ci = C.inv()
    same(Ci, R(1, 2) * sp.Matrix([[1, 1, -1], [-1, 1, 1], [1, -1, 1]]), "C_BB'")
    same(C * Ci, sp.eye(3), "producto")
    same(Ci * col(4, 2, -2), col(4, -2, 0), "[x]_B'")
    same(C * col(4, -2, 0), col(4, 2, -2), "reconstrucción")
    M = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    require(gf_rank(M) == 2, "rango 2 en Z2")
    require(sp.Matrix(M).det() % 2 == 0, "det par")
    vecs = [(1, 1, 0), (0, 1, 1), (1, 0, 1)]
    require(suma2(suma2(vecs[0], vecs[1]), vecs[2]) == (0, 0, 0), "suma nula")
    require(len(gf_span(vecs)) == 4, "4 elementos")
    require(sorted(gf_span(vecs)) == [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)], "elementos")


@check("U1.20", "Recuperar B desde C_BB' y B'", page=AVA)
def _():
    PBp = cols((1, 2), (1, 3))
    C = sp.Matrix([[1, 2], [1, 3]])
    PB = PBp * C
    same(PB, cols((2, 5), (5, 13)), "B = {(2,5),(5,13)}")
    same(PB.det(), 1, "det B")
    Ci = C.inv()
    same(Ci, sp.Matrix([[3, -2], [-1, 1]]), "C_B'B")
    same(C * sp.Matrix([[3, -2], [-1, 1]]), sp.eye(2), "producto")
    v = col(9, 23)
    vBp = PBp.inv() * v
    same(vBp, col(4, 5), "[v]_B'")
    same(Ci * vBp, col(2, 1), "[v]_B desde C_B'B")
    same(PB.inv() * v, col(2, 1), "[v]_B directo")
    same(2 * col(2, 5) + col(5, 13), v, "reconstrucción")


@check("U1.21", "Cadena de tres bases en P_1[R]", page=AVA)
def _():
    CBBp = sp.Matrix([[1, 2], [1, 3]])
    CBpE = cols((1, 1), (1, -1))  # coordenadas de 1+x y 1-x en E={1,x}
    CBE = CBpE * CBBp
    same(CBE, sp.Matrix([[2, 5], [0, -1]]), "C_BE = C_B'E C_BB'")
    same(col(1, 1) + col(1, -1), col(2, 0), "b1 = 2")
    same(2 * col(1, 1) + 3 * col(1, -1), col(5, -1), "b2 = 5 - x")
    same(CBE.det(), -2, "det")
    CEB = CBE.inv()
    same(CEB, sp.Matrix([[R(1, 2), R(5, 2)], [0, -1]]), "C_EB")
    q = col(3, 1)
    qB = CEB * q
    same(qB, col(4, -1), "[q]_B")
    same(4 * col(2, 0) - col(5, -1), q, "reconstrucción de q")
    same(CBBp * CBpE, sp.Matrix([[3, -1], [4, -2]]), "producto en el orden equivocado")
    require(CBBp * CBpE != CBE, "no coincide con C_BE")


@check("U1.23", "Código acortado de Hamming (6,3), d=3", page=AVA)
def _():
    H = [[1, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 0]]
    require(gf_rank(H) == 3, "rango 3")
    G = [[1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0]]
    require(gf_matmul(G, gf_mat_t(H)) == [[0, 0, 0]] * 3, "G H^t = 0")
    require(gf_rank(G) == 3 and len(gf_nullspace(H)) == 3, "dim 3")
    ws = palabras(G)
    require(len(ws) == 8, "8 palabras")
    require(sorted(ws) == sorted(v for v in product((0, 1), repeat=6) if sindrome(H, v) == [0, 0, 0]),
            "las 8 palabras son nul(H)")
    pesos = sorted(weight(w) for w in ws)
    require(pesos == [0, 3, 3, 3, 3, 4, 4, 4], "pesos")
    require(min_distance(ws) == 3, "d = 3")
    colsH = gf_mat_t(H)
    require(all(any(c) for c in colsH) and len({tuple(c) for c in colsH}) == 6, "columnas no nulas y distintas")
    require(suma2(suma2(colsH[0], colsH[1]), colsH[2]) == (0, 0, 0), "h1+h2+h3 = 0")
    require((1, 1, 1, 0, 0, 0) in ws, "111000 está en el código")
    require((0, 0, 1) not in [tuple(c) for c in colsH], "(0,0,1) no es columna")
    r = (1, 0, 1, 0, 0, 1)
    s = sindrome(H, r)
    require(s == [1, 1, 1] and tuple(s) == tuple(colsH[3]), "síndrome h4")
    c = list(r)
    c[3] ^= 1
    require(tuple(c) == (1, 0, 1, 1, 0, 1) and tuple(c) in ws, "corregida a 101101")
    r2 = (0, 0, 1, 0, 0, 1)
    s2 = sindrome(H, r2)
    require(s2 == [0, 0, 1] and tuple(s2) not in [tuple(x) for x in colsH], "síndrome 001 no es columna")
    pares = [(i + 1, j + 1) for i in range(6) for j in range(i + 1, 6)
             if suma2(colsH[i], colsH[j]) == (0, 0, 1)]
    require(pares == [(1, 4), (2, 5), (3, 6)], "tres pares de errores con el mismo síndrome")


@check("U1.24", "Rango y subespacios de A_k = [[1,1,k],[1,k,1],[k,1,1]]", page=AVA)
def _():
    def A(k):
        return sp.Matrix([[1, 1, k], [1, k, 1], [k, 1, 1]])

    for k in range(-5, 6):
        same(A(k).det(), -(k + 2) * (k - 1) ** 2, f"det para k={k}")  # grado 3: 11 puntos
    require(A(1).rank() == 1 and A(-2).rank() == 2, "rangos especiales")
    require(all(A(k).rank() == 3 for k in range(-5, 6) if k not in (1, -2)), "rango 3 genérico")
    n1 = A(1).nullspace()
    require(len(n1) == 2 and gen_igual(sp.Matrix.hstack(*n1), cols((-1, 1, 0), (-1, 0, 1))), "nul(A_1)")
    n2 = A(-2).nullspace()
    require(len(n2) == 1 and gen_igual(n2[0], col(1, 1, 1)), "nul(A_-2)")
    same(A(-2) * col(1, 1, 1), sp.zeros(3, 1), "A(-2)(1,1,1) = 0")
    M = A(-2)
    for j in range(3):
        require(sum(M[i, j] for i in range(3)) == 0, "columnas de suma cero")
    plano = cols((1, -1, 0), (0, 1, -1))
    require(gen_igual(plano, M), "col(A_-2) = {y1+y2+y3=0}")
    require(not en_gen(M, col(1, 1, 1)), "(1,1,1) no está")
    require(en_gen(M, col(1, -2, 1)), "(1,-2,1) sí está")


# ---------------------------------------------------------------------------
# Guía integradora
# ---------------------------------------------------------------------------
@check("U1.26", "Problema 1: S = {p in P_2: p(2) = p(0)}, bases y cambio", page=GUIA)
def _():
    # p = (a, b, c): p(2) - p(0) = 2b + 4c
    cond = sp.Matrix([[0, 2, 4]])
    ns = cond.nullspace()
    require(len(ns) == 2, "dim S = 2")
    b1, b2 = col(1, 0, 0), col(0, -2, 1)  # 1 y x^2 - 2x
    for b in (b1, b2):
        same(cond * b, sp.zeros(1, 1), "B en S")
    require(gen_igual(sp.Matrix.hstack(b1, b2), sp.Matrix.hstack(*ns)), "B base de S")
    c1, c2 = col(1, -2, 1), col(1, -4, 2)
    for c in (c1, c2):
        same(cond * c, sp.zeros(1, 1), "B' en S")
    PB = sp.Matrix.hstack(b1, b2)
    CBpB = sp.Matrix([[1, 1], [1, 2]])
    same(PB * CBpB, sp.Matrix.hstack(c1, c2), "columnas de C_B'B")
    same(CBpB.det(), 1, "det")
    CBBp = CBpB.inv()
    same(CBBp, sp.Matrix([[2, -1], [-1, 1]]), "C_BB'")
    same(2 * c1 - c2, b1, "primera columna de C_BB'")
    q = col(5, -6, 3)
    same(cond * q, sp.zeros(1, 1), "q en S")
    qB = col(5, 3)
    same(PB * qB, q, "[q]_B")
    qBp = CBBp * qB
    same(qBp, col(7, -2), "[q]_B'")
    same(7 * c1 - 2 * c2, q, "reconstrucción")
    ext = cols((1, 0, 0), (0, -2, 1), (0, 1, 0))
    same(ext.det(), -1, "extensión a base de P_2")
    # p(2) = p(0) para q evaluando
    same(5 + 6 * 0 + 0, 5, "q(0) = 5")
    same(5 - 6 * 2 + 3 * 4, 5, "q(2) = 5")


@check("U1.27", "Problema 2: A_k = [[1,1,0,1],[0,1,1,k],[1,2,1,3]]", page=GUIA)
def _():
    def A(k):
        return sp.Matrix([[1, 1, 0, 1], [0, 1, 1, k], [1, 2, 1, 3]])

    for k in range(-4, 6):
        require(A(k).rank() == (2 if k == 2 else 3), f"rango para k={k}")
        E = A(k)
        F = sp.Matrix([[1, 1, 0, 1], [0, 1, 1, k], [0, 0, 0, 2 - k]])
        # F3 - F1, luego F3 - F2
        r3 = [E[2, j] - E[0, j] - E[1, j] for j in range(4)]
        require(r3 == [0, 0, 0, 2 - k], f"fila 3 escalonada para k={k}")
        same(F[2, 3], 2 - k, "entrada")
    A2 = A(2)
    Rr, piv = A2.rref()
    require(tuple(piv) == (0, 1), "pivotes 1 y 2")
    same(Rr, sp.Matrix([[1, 0, -1, -1], [0, 1, 1, 2], [0, 0, 0, 0]]), "reducida")
    fil = cols((1, 0, -1, -1), (0, 1, 1, 2))
    require(gen_igual(fil, A2.T), "base de fil")
    cb = cols((1, 0, 1), (1, 1, 2))
    require(gen_igual(cb, A2), "base de col")
    nb = [col(1, -1, 1, 0), col(1, -2, 0, 1)]
    for v in nb:
        same(A2 * v, sp.zeros(3, 1), "A2 v = 0")
    require(gen_igual(sp.Matrix.hstack(*nb), sp.Matrix.hstack(*A2.nullspace())), "base de nul")
    require(A2.rank() + len(A2.nullspace()) == 4, "rango-nulidad")
    for a, b in product(range(-3, 4), repeat=2):
        v = a * col(1, 0, 1) + b * col(1, 1, 2)
        require(v[0] + v[1] - v[2] == 0, "ecuación x+y-z=0")
    require(en_gen(cb, col(2, 1, 3)) and not en_gen(cb, col(1, 1, 1)), "pertenencias")
    for k in (-1, 0, 1, 3, 4):
        require(len(A(k).nullspace()) == 1 and A(k).rank() == 3, f"nulidad 1 para k={k}")
        require(en_gen(A(k), col(1, 1, 1)) and en_gen(A(k), col(7, -3, 2)), "col = R^3")
    same(A(3) * col(1, -1, 1, 0), sp.zeros(3, 1), "nul(A_3)")


@check("U1.28", "Problema 3: código (5,2) sobre Z2", page=GUIA)
def _():
    H = [[1, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 1, 0, 0]]
    require(gf_rank(H) == 3 and len(gf_nullspace(H)) == 2, "dim C = 2")
    G = [[1, 0, 0, 1, 1], [0, 1, 1, 1, 1]]
    require(gf_matmul(G, gf_mat_t(H)) == [[0, 0, 0]] * 2, "G H^t = 0")
    require(gf_rank(G) == 2, "G de rango 2")
    ws = palabras(G)
    require(ws == [(0, 0, 0, 0, 0), (0, 1, 1, 1, 1), (1, 0, 0, 1, 1), (1, 1, 1, 0, 0)], "palabras")
    require(ws == sorted(v for v in product((0, 1), repeat=5) if sindrome(H, v) == [0, 0, 0]), "= nul(H)")
    require(suma2(G[0], G[1]) == (1, 1, 1, 0, 0), "g1 + g2")
    require(sorted(weight(w) for w in ws) == [0, 3, 3, 4] and min_distance(ws) == 3, "d = 3")
    colsH = gf_mat_t(H)
    require(len({tuple(c) for c in colsH}) == 5 and all(any(c) for c in colsH), "columnas no nulas y distintas")
    r = (1, 1, 1, 0, 1)
    s = sindrome(H, r)
    require(s == [0, 1, 0] and tuple(s) == tuple(colsH[4]), "síndrome h5")
    c = list(r)
    c[4] ^= 1
    require(tuple(c) == (1, 1, 1, 0, 0) and tuple(c) in ws, "corrección a 11100")
    r2 = (0, 1, 0, 1, 0)
    s2 = sindrome(H, r2)
    require(s2 == [0, 0, 1] and tuple(s2) not in [tuple(x) for x in colsH], "síndrome 001")
    pares = [(i + 1, j + 1) for i in range(5) for j in range(i + 1, 5)
             if suma2(colsH[i], colsH[j]) == (0, 0, 1)]
    require(pares == [(2, 4), (3, 5)], "dos pares con síndrome 001")
    todos = set(product((0, 1), repeat=3))
    usados = {(0, 0, 0)} | {tuple(c) for c in colsH}
    require(sorted(todos - usados) == [(0, 0, 1), (1, 1, 1)], "dos síndromes sin error simple")
    require(len(todos) == 8 and len(usados) == 6, "conteo de síndromes")


@check("U1.29", "Problema 4: bases abstractas w1=v1+v2+v3, w2=v2+v3, w3=v3 y B_k", page=GUIA)
def _():
    CBpB = cols((1, 1, 1), (0, 1, 1), (0, 0, 1))
    same(CBpB.det(), 1, "det")
    CBBp = CBpB.inv()
    same(CBBp, sp.Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]]), "C_BB'")
    same(CBBp * CBpB, sp.eye(3), "producto")
    xB = col(2, -1, 3)
    xBp = CBBp * xB
    same(xBp, col(2, -3, 4), "[x]_B'")
    same(CBpB * xBp, xB, "reconstrucción de x")
    yBp = col(1, 2, -1)
    same(CBpB * yBp, col(1, 3, 2), "[y]_B")
    same(CBBp * col(1, 3, 2), yBp, "ida y vuelta")

    def D(k):
        return cols((1, k, 0), (0, 1, k), (k, 0, 1)).det()

    for k in range(-5, 6):
        same(D(k), 1 + k ** 3, f"det de B_k para k={k}")  # grado 3: 11 puntos
    require([k for k in range(-5, 6) if D(k) == 0] == [-1], "solo k=-1 entre los enteros chicos")
    for k in (0, 1):
        M = [[1, 0, k], [k, 1, 0], [0, k, 1]]
        require(gf_rank(M) == (3 if k == 0 else 2), f"rango en Z2 para k={k}")
    require(suma2(suma2((1, 1, 0), (0, 1, 1)), (1, 0, 1)) == (0, 0, 0), "k=1: suma nula en Z2")


@check("U1.30", "Problema 5: cuatro vectores sobre Z2 y sobre R", page=GUIA)
def _():
    U = [(1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1)]
    require(gf_rank(U) == 3, "rango 3 en Z2")
    require(cols(*U).rank() == 3, "rango 3 en R")
    s = (0, 0, 0, 0)
    for u in U:
        s = suma2(s, u)
    require(s == (0, 0, 0, 0), "relación en Z2")
    same(col(*U[0]) - col(*U[1]) + col(*U[2]) - col(*U[3]), sp.zeros(4, 1), "relación en R")
    require(gf_rank(U[:3]) == 3 and cols(*U[:3]).rank() == 3, "u1,u2,u3 LI en ambos")
    W = palabras(U)
    N = sorted(v for v in product((0, 1), repeat=4) if sum(v) % 2 == 0)
    require(W == N and len(W) == 8, "W = {v: v1+v2+v3+v4 = 0}")
    require(len(gf_nullspace([[1, 1, 1, 1]])) == 3, "dim N = 3")
    require(min_distance(W) == 2 and weight(U[0]) == 2, "d = 2")
    require(all(weight(w) % 2 == 0 for w in W), "pesos pares")
    require((1, 1, 1, 1) in W and suma2(U[0], U[2]) == (1, 1, 1, 1), "1111 = u1 + u3")
    union = set(W) | {(0, 0, 0, 0), (1, 0, 0, 0)}
    require(suma2((1, 1, 0, 0), (1, 0, 0, 0)) == (0, 1, 0, 0) and (0, 1, 0, 0) not in union, "(ii) falsa")
    require(len(gf_span(U)) == 8, "8 elementos en Z2")
