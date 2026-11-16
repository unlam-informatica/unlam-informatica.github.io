"""Comprobaciones de los ejemplos resueltos de la teoría de la Unidad 3 (autovalores y autovectores).

Cada función recalcula desde los datos del ejemplo publicado: polinomio característico,
raíces con multiplicidad, autoespacios (vía ``nullspace``), factorizaciones ``C^{-1} A C = D``,
potencias, términos de recurrencias contra la fórmula cerrada y vectores estacionarios.
Convención de la cátedra: ``p_A(λ) = det(λI − A)`` y ``A = C D C^{-1}`` con autovectores en las
columnas de ``C``. Las matrices de transición son estocásticas por columnas (``x_{k+1} = P x_k``).
"""
import itertools

import sympy as sp

from content_pipeline.mathcheck import check, require, same

lam = sp.symbols("lambda")
n_sym = sp.symbols("n", integer=True, nonnegative=True)

T01 = "/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/"
T02 = "/algebra-ii/unidad-3/teoria/polinomio-caracteristico/"
T03 = "/algebra-ii/unidad-3/teoria/propiedades/"
T04 = "/algebra-ii/unidad-3/teoria/matrices-semejantes/"
T05 = "/algebra-ii/unidad-3/teoria/diagonalizacion/"
T06 = "/algebra-ii/unidad-3/teoria/potencias/"
T07 = "/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/"
T08 = "/algebra-ii/unidad-3/teoria/cadenas-de-markov/"


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def cp(A):
    """Polinomio característico p_A(λ) = det(λI − A), expandido."""
    return sp.expand((lam * sp.eye(A.rows) - A).det())


def raices(A):
    """Raíces reales o complejas de p_A con su multiplicidad algebraica."""
    return sp.roots(sp.Poly(cp(A), lam))


def autoespacio(A, valor):
    """Base de E_λ(A) = nul(λI − A)."""
    return (valor * sp.eye(A.rows) - A).nullspace()


def es_autovector(A, v, valor):
    v = sp.Matrix(v)
    return any(x != 0 for x in v) and (A * v - valor * v).applyfunc(sp.simplify) == sp.zeros(*v.shape)


def mismo_subespacio(base, esperado):
    """Dos familias generan el mismo subespacio (comparación por rangos)."""
    X = sp.Matrix.hstack(*[sp.Matrix(b) for b in base])
    Y = sp.Matrix.hstack(*[sp.Matrix(e) for e in esperado])
    return X.rank() == Y.rank() == sp.Matrix.hstack(X, Y).rank()


def columna(*valores):
    return sp.Matrix(valores)


# ---------------------------------------------------------------------------
# 3.1 Autovalores y autovectores
# ---------------------------------------------------------------------------
@check("U3.T01.F1", "Figura: direcciones invariantes de A=[[2,1],[1,2]]", page=T01)
def _():
    A = sp.Matrix([[2, 1], [1, 2]])
    same(A * columna(1, 1), columna(3, 3), "Av")
    same(A * columna(-1, 1), columna(-1, 1), "Au")
    Aw = A * columna(1, 0)
    same(Aw, columna(2, 1), "Aw")
    require(sp.Matrix.hstack(Aw, columna(1, 0)).det() != 0, "Aw no es paralelo a w")


@check("U3.T01.E1", "Verificar autovectores y autovalores de una 2x2", page=T01)
def _():
    A = sp.Matrix([[4, -2], [1, 1]])
    same(A * columna(2, 1), columna(6, 3), "Au")
    require(es_autovector(A, (2, 1), 3), "u=(2,1) autovector de 3")
    Aw = A * columna(1, 2)
    same(Aw, columna(0, 3), "Aw")
    require(sp.Matrix.hstack(Aw, columna(1, 2)).det() != 0, "w=(1,2) no es autovector")
    E2 = autoespacio(A, 2)
    require(len(E2) == 1 and mismo_subespacio(E2, [(1, 1)]), "E_2 = gen{(1,1)}")
    same((5 * sp.eye(2) - A).det(), 6, "det(5I-A)")


@check("U3.T01.E2", "Transposición en R^{2x2}: autovalores 1 y -1", page=T01)
def _():
    # Base canónica ordenada E = {E11, E12, E21, E22}; T(X) = X^t.
    base = [sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 1], [0, 0]]),
            sp.Matrix([[0, 0], [1, 0]]), sp.Matrix([[0, 0], [0, 1]])]

    def coords(X):
        return sp.Matrix([X[0, 0], X[0, 1], X[1, 0], X[1, 1]])

    M = sp.Matrix.hstack(*[coords(X.T) for X in base])
    same(M, sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]), "M(T)_E")
    same(cp(M), sp.expand((lam - 1) ** 3 * (lam + 1)), "p(λ)")
    E1, Em1 = autoespacio(M, 1), autoespacio(M, -1)
    require(len(E1) == 3 and mismo_subespacio(E1, [(1, 0, 0, 0), (0, 1, 1, 0), (0, 0, 0, 1)]), "E_1 = simétricas")
    require(len(Em1) == 1 and mismo_subespacio(Em1, [(0, 1, -1, 0)]), "E_-1 = antisimétricas")


@check("U3.T01.E3", "Autovalor 0 de una matriz no inversible", page=T01)
def _():
    A = sp.Matrix([[1, 2, -1], [2, 1, 1], [3, 3, 0]])
    same(A.det(), 0, "det A")
    E0 = autoespacio(A, 0)
    require(len(E0) == 1 and mismo_subespacio(E0, [(1, -1, -1)]), "E_0 = gen{(1,-1,-1)}")
    same(A * columna(1, -1, -1), columna(0, 0, 0), "A v = 0")


@check("U3.T01.E4", "Parámetro para que v=(1,1,-1) sea autovector", page=T01)
def _():
    a, l = sp.symbols("a l")
    A = sp.Matrix([[1, a, 0], [2, 1, a], [0, 1, 3]])
    v = columna(1, 1, -1)
    same(A * v, columna(1 + a, 3 - a, -2), "Av")
    sol = sp.solve(list(A * v - l * v), [a, l], dict=True)
    require(sol == [{a: 1, l: 2}], f"única solución a=1, λ=2: {sol}")
    require(es_autovector(A.subs(a, 1), v, 2), "con a=1, Av=2v")


# ---------------------------------------------------------------------------
# 3.2 Polinomio característico
# ---------------------------------------------------------------------------
@check("U3.T02.E1", "Autovalores y autoespacios de una 2x2", page=T02)
def _():
    A = sp.Matrix([[5, -2], [6, -2]])
    same(cp(A), lam**2 - 3 * lam + 2, "p(λ)")
    require(raices(A) == {1: 1, 2: 1}, "raíces 1 y 2")
    require(mismo_subespacio(autoespacio(A, 1), [(1, 2)]), "E_1")
    require(mismo_subespacio(autoespacio(A, 2), [(2, 3)]), "E_2")


@check("U3.T02.E2", "3x3 con Ruffini: autovalores -1, 1, 3", page=T02)
def _():
    A = sp.Matrix([[1, 2, -2], [-2, 1, 2], [-2, 2, 1]])
    p = cp(A)
    same(p, lam**3 - 3 * lam**2 - lam + 3, "p(λ)")
    q, r = sp.div(sp.Poly(p, lam), sp.Poly(lam - 1, lam))
    same(r.as_expr(), 0, "resto de Ruffini en 1")
    same(q.as_expr(), lam**2 - 2 * lam - 3, "cociente de Ruffini")
    require(raices(A) == {-1: 1, 1: 1, 3: 1}, "raíces")
    require(mismo_subespacio(autoespacio(A, -1), [(1, 0, 1)]), "E_-1")
    require(mismo_subespacio(autoespacio(A, 1), [(1, 1, 1)]), "E_1")
    require(mismo_subespacio(autoespacio(A, 3), [(0, 1, 1)]), "E_3")
    # coeficientes: λ^3 − tr(A) λ^2 + ... + (−1)^3 det(A)
    same(A.trace(), 3, "traza")
    same(A.det(), -3, "determinante")
    same(p.subs(lam, 0), (-1) ** 3 * A.det(), "término independiente")


@check("U3.T02.E3", "Autovalor doble con m_g = 1", page=T02)
def _():
    A = sp.Matrix([[3, 0, 1], [1, -1, -2], [-1, 0, 1]])
    same(sp.factor(cp(A)), sp.factor((lam + 1) * (lam - 2) ** 2), "p(λ)")
    # desarrollo por la segunda columna: (λ+1)·[(λ−3)(λ−1)+1]
    same(cp(A), sp.expand((lam + 1) * ((lam - 3) * (lam - 1) + 1)), "desarrollo por columna 2")
    require(raices(A) == {-1: 1, 2: 2}, "m_a")
    E2 = autoespacio(A, 2)
    require(len(E2) == 1 and mismo_subespacio(E2, [(1, 1, -1)]), "E_2, m_g = 1")
    require(mismo_subespacio(autoespacio(A, -1), [(0, 1, 0)]), "E_-1")
    same((2 * sp.eye(3) - A).rank(), 2, "rango(2I-A)")


@check("U3.T02.E4", "2x2 sin autovalores reales", page=T02)
def _():
    A = sp.Matrix([[1, -2], [1, 3]])
    same(cp(A), lam**2 - 4 * lam + 5, "p(λ)")
    same(sp.discriminant(cp(A), lam), -4, "discriminante")
    require(raices(A) == {2 + sp.I: 1, 2 - sp.I: 1}, "raíces complejas 2±i")


@check("U3.T02.E5", "Triangular: autovalores en la diagonal y m_g < m_a", page=T02)
def _():
    A = sp.Matrix([[2, 5, -1], [0, -3, 4], [0, 0, 2]])
    same(sp.factor(cp(A)), sp.factor((lam - 2) ** 2 * (lam + 3)), "p(λ)")
    E2 = autoespacio(A, 2)
    require(len(E2) == 1 and mismo_subespacio(E2, [(1, 0, 0)]), "E_2")
    require(mismo_subespacio(autoespacio(A, -3), [(1, -1, 0)]), "E_-3")


# ---------------------------------------------------------------------------
# 3.3 Propiedades
# ---------------------------------------------------------------------------
A_T03 = sp.Matrix([[2, 1, 1], [0, 3, 1], [1, 1, 2]])


@check("U3.T03.E1", "Filas de suma constante, traza y determinante", page=T03)
def _():
    A = A_T03
    require(all(sum(A.row(i)) == 4 for i in range(3)), "filas de suma 4")
    require(es_autovector(A, (1, 1, 1), 4), "(1,1,1) autovector de 4")
    same(A.trace(), 7, "traza")
    same(A.det(), 8, "det")
    # los otros dos: suma 7 − 4 = 3, producto 8/4 = 2
    same(sp.expand(cp(A)), sp.expand((lam - 4) * (lam**2 - 3 * lam + 2)), "p(λ) = (λ−4)(λ²−3λ+2)")
    require(raices(A) == {1: 1, 2: 1, 4: 1}, "autovalores 1, 2, 4")
    require(es_autovector(A, (1, -1, 1), 2), "v2")
    require(es_autovector(A, (1, 1, -2), 1), "v1")
    C = sp.Matrix([[1, 1, 1], [1, -1, 1], [1, 1, -2]])
    same(C.det(), 6, "det C ≠ 0: autovectores LI")


@check("U3.T03.E2", "Autovalores de A^-1, A^3 y A^2 - 3A", page=T03)
def _():
    A = A_T03
    Ainv = A.inv()
    require(raices(Ainv) == {1: 1, sp.Rational(1, 2): 1, sp.Rational(1, 4): 1}, "A^{-1}")
    require(raices(A**3) == {1: 1, 8: 1, 64: 1}, "A^3")
    X = A**2 - 3 * A
    same(X, sp.Matrix([[-1, 3, 2], [1, 1, 2], [1, 3, 0]]), "A^2 − 3A")
    require(raices(X) == {-2: 2, 4: 1}, "autovalores de A^2 − 3A")
    same(X.det(), 16, "det(A^2−3A)")
    same(X.trace(), 0, "tr(A^2−3A)")
    for v, valor in (((1, 1, 1), 4), ((1, -1, 1), 2), ((1, 1, -2), 1)):
        require(es_autovector(X, v, valor**2 - 3 * valor), f"p(A)v = p(λ)v para λ={valor}")
        require(es_autovector(A + 5 * sp.eye(3), v, valor + 5), "A + 5I")


@check("U3.T03.E3", "A y A^t: mismo polinomio, distintos autoespacios", page=T03)
def _():
    A = sp.Matrix([[1, 1], [0, 2]])
    same(cp(A), cp(A.T), "p_A = p_{A^t}")
    require(mismo_subespacio(autoespacio(A, 1), [(1, 0)]), "E_1(A)")
    require(mismo_subespacio(autoespacio(A, 2), [(1, 1)]), "E_2(A)")
    require(mismo_subespacio(autoespacio(A.T, 1), [(1, -1)]), "E_1(A^t)")
    require(mismo_subespacio(autoespacio(A.T, 2), [(0, 1)]), "E_2(A^t)")


@check("U3.T03.E4", "Columnas de suma constante", page=T03)
def _():
    B = sp.Matrix([[1, 4], [2, -1]])
    require(all(sum(B.col(j)) == 3 for j in range(2)), "columnas de suma 3")
    require(raices(B) == {3: 1, -3: 1}, "autovalores ±3")
    require(mismo_subespacio(autoespacio(B, 3), [(2, 1)]), "E_3(B)")
    require(not es_autovector(B, (1, 1), 3), "(1,1) no es autovector de B")
    require(es_autovector(B.T, (1, 1), 3), "(1,1) sí es autovector de B^t")


@check("U3.T03.E5", "Los autovalores no son aditivos", page=T03)
def _():
    A = sp.Matrix([[0, 1], [0, 0]])
    B = sp.Matrix([[0, 0], [1, 0]])
    require(raices(A) == {0: 2} and raices(B) == {0: 2}, "autovalor 0 en ambas")
    same(cp(A + B), lam**2 - 1, "p_{A+B}")
    require(raices(A * B) == {1: 1, 0: 1}, "autovalores de AB")
    R = sp.Matrix([[0, -1], [1, 0]])
    same(R**2, -sp.eye(2), "R^2 = -I tiene autovalor real -1")
    require(not [r for r in raices(R) if r.is_real], "R sin autovalores reales")
    # Autoevaluación: autovalores 1, 2, 5 -> det(A^2+I) = 2*5*26; A=[[2,1],[0,3]] filas de suma 3, traza 5
    same(2 * 5 * 26, 260, "det(A^2+I)")
    M = sp.Matrix([[2, 1], [0, 3]])
    require(all(sum(M.row(i)) == 3 for i in range(2)) and M.trace() == 5, "autoevaluación 2")


# ---------------------------------------------------------------------------
# 3.4 Matrices semejantes
# ---------------------------------------------------------------------------
@check("U3.T04.E1", "Construir A = CBC^{-1} y comparar invariantes", page=T04)
def _():
    B = sp.Matrix([[2, 1], [0, 3]])
    C = sp.Matrix([[1, 1], [1, 2]])
    same(C.inv(), sp.Matrix([[2, -1], [-1, 1]]), "C^{-1}")
    A = C * B * C.inv()
    same(A, sp.Matrix([[0, 2], [-3, 5]]), "A")
    same(cp(A), cp(B), "polinomio característico")
    same(A.trace(), B.trace(), "traza")
    same(A.det(), B.det(), "det")
    same(A.rank(), B.rank(), "rango")
    require(es_autovector(B, (1, 0), 2) and es_autovector(A, C * columna(1, 0), 2), "Cv autovector de A")
    require(not es_autovector(A, (1, 0), 2), "los autovectores no son invariantes")


@check("U3.T04.E2", "Decidir semejanza", page=T04)
def _():
    # (a) determinantes distintos
    same(sp.Matrix([[1, 2], [3, 4]]).det(), -2, "det (a) A")
    same(sp.Matrix([[2, 1], [1, 3]]).det(), 5, "det (a) B")
    # (b) 2I y J tienen el mismo polinomio pero C(2I)C^{-1} = 2I ≠ J
    J = sp.Matrix([[2, 1], [0, 2]])
    same(cp(J), cp(2 * sp.eye(2)), "mismo polinomio (b)")
    c = sp.symbols("c0:4")
    Cg = sp.Matrix(2, 2, c)
    same(Cg * (2 * sp.eye(2)) - 2 * sp.eye(2) * Cg, sp.zeros(2, 2), "C(2I) = (2I)C")
    # (c) C explícita con A1 C = C B1
    A1 = sp.Matrix([[3, 1], [0, 2]])
    B1 = sp.Matrix([[2, 0], [5, 3]])
    C = sp.Matrix([[6, 1], [-1, 0]])
    same(C.det(), 1, "det C")
    same(A1 * C, C * B1, "A1 C = C B1")
    same(C * B1 * C.inv(), A1, "A1 = C B1 C^{-1}")


@check("U3.T04.E3", "Matriz de un endomorfismo en dos bases", page=T04)
def _():
    AE = sp.Matrix([[3, -1], [2, 0]])  # T(x,y) = (3x − y, 2x)
    CBE = sp.Matrix([[1, 1], [0, 1]])  # B = {(1,0),(1,1)}
    MB = CBE.inv() * AE * CBE
    same(MB, sp.Matrix([[1, 0], [2, 2]]), "M(T)_B")
    same(cp(MB), cp(AE), "polinomio")
    same(cp(AE), lam**2 - 3 * lam + 2, "p(λ)")
    CB2 = sp.Matrix([[1, 1], [1, 2]])  # B' = {(1,1),(1,2)}
    same(CB2.inv() * AE * CB2, sp.diag(2, 1), "M(T)_{B'} diagonal")


@check("U3.T04.E4", "Potencias vía semejanza con B = [[1,1],[0,1]]", page=T04)
def _():
    B = sp.Matrix([[1, 1], [0, 1]])
    C = sp.Matrix([[1, 1], [1, 2]])
    A = C * B * C.inv()
    same(A, sp.Matrix([[0, 1], [-1, 2]]), "A")
    for k in range(-3, 13):
        Bk = sp.Matrix([[1, k], [0, 1]])
        same(B**k, Bk, f"B^{k}")
        same(A**k, sp.Matrix([[1 - k, k], [-k, 1 + k]]), f"A^{k}")
        same(C * Bk * C.inv(), A**k, f"A^{k} = C B^{k} C^-1")


@check("U3.T04.E5", "I y N no son semejantes", page=T04)
def _():
    N = sp.Matrix([[1, 1], [0, 1]])
    same(cp(N), cp(sp.eye(2)), "mismo polinomio")
    same(N.trace(), 2, "traza")
    same(N.det(), 1, "det")
    same((sp.eye(2) - N).rank(), 1, "m_g(1) de N es 1")
    a, b, c, d = sp.symbols("a b c d")
    Cg = sp.Matrix([[a, b], [c, d]])
    ecuaciones = list(sp.eye(2) * Cg - Cg * N)
    sol = sp.solve(ecuaciones, [a, c], dict=True)
    require(sol == [{a: 0, c: 0}], f"IC = CN fuerza a=c=0: {sol}")
    same(Cg.subs({a: 0, c: 0}).det(), 0, "C no inversible")
    # Autoevaluación: tr y det de semejantes
    same((sp.Integer(6)) ** 2, 36, "det(B^2)")


# ---------------------------------------------------------------------------
# 3.5 Diagonalización
# ---------------------------------------------------------------------------
@check("U3.T05.E1", "Diagonalizar una 2x2", page=T05)
def _():
    A = sp.Matrix([[4, -2], [1, 1]])
    C = sp.Matrix([[1, 2], [1, 1]])
    D = sp.diag(2, 3)
    same(C.inv(), sp.Matrix([[-1, 2], [1, -1]]), "C^{-1}")
    same(C.inv() * A * C, D, "C^{-1}AC = D")
    same(C * D * C.inv(), A, "A = CDC^{-1}")
    C2 = sp.Matrix([[2, 1], [1, 1]])
    same(C2.inv() * A * C2, sp.diag(3, 2), "otro orden de columnas")
    C3 = sp.Matrix([[-3, 4], [-3, 2]])
    same(C3.inv() * A * C3, D, "C no es única (múltiplos)")


@check("U3.T05.E2", "3x3 diagonalizable con autovalor doble", page=T05)
def _():
    A = sp.Matrix([[2, 0, 1], [1, 1, 1], [2, 0, 3]])
    same(cp(A), sp.expand((lam - 1) * (lam**2 - 5 * lam + 4)), "desarrollo por columna 2")
    require(raices(A) == {1: 2, 4: 1}, "m_a")
    E1 = autoespacio(A, 1)
    require(len(E1) == 2 and mismo_subespacio(E1, [(0, 1, 0), (1, 0, -1)]), "E_1, m_g = 2")
    require(mismo_subespacio(autoespacio(A, 4), [(1, 1, 2)]), "E_4")
    C = sp.Matrix([[0, 1, 1], [1, 0, 1], [0, -1, 2]])
    same(C.det(), -3, "det C")
    same(C.inv() * A * C, sp.diag(1, 1, 4), "C^{-1}AC")
    Cp = sp.Matrix([[1, 0, 1], [1, 1, 0], [2, 0, -1]])
    same(Cp.inv() * A * Cp, sp.diag(4, 1, 1), "orden alternativo")


@check("U3.T05.E3", "3x3 no diagonalizable", page=T05)
def _():
    A = sp.Matrix([[0, -1, 1], [3, 1, -3], [2, -1, -1]])
    same(cp(A), lam**3 - 3 * lam + 2, "p(λ)")
    q, r = sp.div(sp.Poly(cp(A), lam), sp.Poly(lam - 1, lam))
    same(r.as_expr(), 0, "Ruffini en 1")
    same(q.as_expr(), lam**2 + lam - 2, "cociente")
    require(raices(A) == {1: 2, -2: 1}, "m_a")
    E1 = autoespacio(A, 1)
    require(len(E1) == 1 and mismo_subespacio(E1, [(1, 0, 1)]), "E_1, m_g = 1")
    require(mismo_subespacio(autoespacio(A, -2), [(0, 1, 1)]), "E_-2")
    require(not A.is_diagonalizable(), "no diagonalizable")


@check("U3.T05.E4", "Diagonalizabilidad según un parámetro", page=T05)
def _():
    k = sp.symbols("k")
    A = sp.Matrix([[2, 1, 0], [0, k, 0], [1, -1, 3]])
    same(sp.factor(cp(A)), sp.factor((lam - 2) * (lam - k) * (lam - 3)), "p(λ)")
    A2, A3 = A.subs(k, 2), A.subs(k, 3)
    require(len(autoespacio(A2, 2)) == 1, "k=2: m_g(2)=1")
    require(mismo_subespacio(autoespacio(A2, 2), [(1, 0, -1)]), "k=2: E_2")
    require(not A2.is_diagonalizable(), "k=2 no diagonalizable")
    E3 = autoespacio(A3, 3)
    require(len(E3) == 2 and mismo_subespacio(E3, [(1, 1, 0), (0, 0, 1)]), "k=3: E_3 de dim 2")
    require(A3.is_diagonalizable(), "k=3 diagonalizable")
    for valor in (-1, 0, 1, 4, sp.Rational(5, 2)):
        require(A.subs(k, valor).is_diagonalizable(), f"k={valor} diagonalizable")


@check("U3.T05.E5", "Simétrica 2x2", page=T05)
def _():
    a, b, c = sp.symbols("a b c", real=True)
    S = sp.Matrix([[a, b], [b, c]])
    same(sp.discriminant(cp(S), lam), (a - c) ** 2 + 4 * b**2, "discriminante")
    N = sp.Matrix([[1, 2], [2, -2]])
    same(cp(N), lam**2 + lam - 6, "p(λ)")
    require(raices(N) == {2: 1, -3: 1}, "autovalores")
    C = sp.Matrix([[2, 1], [1, -2]])
    same(C.inv() * N * C, sp.diag(2, -3), "C^{-1}NC")
    same((C.col(0).T * C.col(1))[0], 0, "autovectores perpendiculares")


# ---------------------------------------------------------------------------
# 3.6 Potencias
# ---------------------------------------------------------------------------
A_T06 = sp.Matrix([[4, -2], [1, 1]])


def potencia_T06(k):
    dos, tres = sp.Integer(2) ** k, sp.Integer(3) ** k
    return sp.Matrix([[-dos + 2 * tres, 2 * dos - 2 * tres],
                      [-dos + tres, 2 * dos - tres]])


@check("U3.T06.E1", "Fórmula de A^k y A^10", page=T06)
def _():
    A = A_T06
    C = sp.Matrix([[1, 2], [1, 1]])
    k = sp.symbols("k", integer=True)
    general = C * sp.diag(2**k, 3**k) * C.inv()
    same(general, potencia_T06(k), "C D^k C^{-1}")
    for j in range(0, 12):
        same(A**j, potencia_T06(j), f"A^{j}")
    same(A**10, sp.Matrix([[117074, -116050], [58025, -57001]]), "A^10")


@check("U3.T06.E2", "Potencias negativas", page=T06)
def _():
    A = A_T06
    same(A.inv(), sp.Matrix([[sp.Rational(1, 6), sp.Rational(1, 3)], [-sp.Rational(1, 6), sp.Rational(2, 3)]]), "A^{-1}")
    for j in range(-4, 0):
        same(A**j, potencia_T06(j), f"A^{j}")
    same(A**-2, sp.Matrix([[-sp.Rational(1, 36), sp.Rational(5, 18)], [-sp.Rational(5, 36), sp.Rational(7, 18)]]), "A^{-2}")


@check("U3.T06.E3", "Inversibilidad de polinomios en A", page=T06)
def _():
    A = sp.Matrix([[0, 1, 1], [1, 0, 1], [3, -3, 2]])
    I3 = sp.eye(3)
    require(raices(A) == {-1: 1, 1: 1, 2: 1}, "autovalores")
    require(es_autovector(A, (1, 0, -1), -1), "v(-1)")
    require(es_autovector(A, (1, 1, 0), 1), "v(1)")
    require(es_autovector(A, (1, 1, 1), 2), "v(2)")
    C = sp.Matrix([[1, 1, 1], [0, 1, 1], [-1, 0, 1]])
    same(C.inv() * A * C, sp.diag(-1, 1, 2), "diagonalización")
    same((A**100 - I3).det(), 0, "A^100 − I singular")
    same((A**2 + A).det(), 0, "A^2 + A singular")
    same((A**2 + I3).det(), 20, "det(A^2 + I)")
    X = A**3 - 3 * A
    same(X, sp.Matrix([[6, -8, 4], [4, -6, 4], [0, 0, 2]]), "A^3 − 3A")
    same(X.det(), -8, "det(A^3 − 3A)")
    same((A**101 + I3).det(), 0, "A^101 + I singular")


@check("U3.T06.E4", "Límite de A^k", page=T06)
def _():
    C = sp.Matrix([[1, 1], [1, 2]])
    A = C * sp.diag(1, sp.Rational(1, 2)) * C.inv()
    same(A, sp.Matrix([[sp.Rational(3, 2), -sp.Rational(1, 2)], [1, 0]]), "A")
    k = sp.symbols("k", integer=True, positive=True)
    Ak = sp.Matrix([[2 - 2**-k, -1 + 2**-k], [2 - 2 * 2**-k, -1 + 2 * 2**-k]])
    same(C * sp.diag(1, sp.Rational(1, 2) ** k) * C.inv(), Ak, "A^k")
    for j in range(1, 8):
        same(A**j, Ak.subs(k, j), f"A^{j}")
    L = sp.Matrix([[2, -1], [2, -1]])
    # A^k − L = 2^{-k} M con M fija: tiende a la matriz nula
    same(Ak - L, 2**-k * sp.Matrix([[-1, 1], [-2, 2]]), "A^k − L")
    same(L * L, L, "L idempotente")


@check("U3.T06.E5", "Rotación: A^2 + I = 0 sin autovalores reales", page=T06)
def _():
    R = sp.Matrix([[0, -1], [1, 0]])
    same(cp(R), lam**2 + 1, "p(λ)")
    same(R**2 + sp.eye(2), sp.zeros(2, 2), "R^2 + I")
    N = sp.Matrix([[1, 1], [0, 1]])
    for k in range(0, 10):
        same(N**k, sp.Matrix([[1, k], [0, 1]]), f"N^{k}")


@check("U3.T06.E6", "Exponenciación binaria de matrices", page=T06)
def _():
    def mat_mul(A, B):
        n, m, p = len(A), len(B), len(B[0])
        return [[sum(A[i][t] * B[t][j] for t in range(m)) for j in range(p)] for i in range(n)]

    def mat_pow(A, k):
        resultado = [[int(i == j) for j in range(len(A))] for i in range(len(A))]
        while k > 0:
            if k & 1:
                resultado = mat_mul(resultado, A)
            A = mat_mul(A, A)
            k >>= 1
        return resultado

    A = [[4, -2], [1, 1]]
    require(mat_pow(A, 10) == [[117074, -116050], [58025, -57001]], "A^10")
    for k in range(0, 15):
        same(sp.Matrix(mat_pow(A, k)), sp.Matrix(A) ** k, f"A^{k}")
    require(mat_pow([[1, 1], [1, 0]], 90)[0][1] == 2880067194370816120, "F_90")
    # autoevaluación: A^5 y A^-2 de autovalores 2, -1, 1/2; 1000 en binario
    require([x**5 for x in (2, -1, sp.Rational(1, 2))] == [32, -1, sp.Rational(1, 32)], "A^5")
    require([x**-2 for x in (2, -1, sp.Rational(1, 2))] == [sp.Rational(1, 4), 1, 4], "A^-2")
    require(bin(1000) == "0b1111101000" and bin(1000).count("1") == 6, "1000 en binario")


# ---------------------------------------------------------------------------
# 3.7 Relaciones de recurrencia
# ---------------------------------------------------------------------------
def sucesion(c1, c2, a0, a1, cantidad):
    """a_{n+1} = c1 a_n + c2 a_{n−1}."""
    a = [a0, a1]
    while len(a) < cantidad:
        a.append(c1 * a[-1] + c2 * a[-2])
    return a


@check("U3.T07.E1", "a_{n+1} = a_n + 6 a_{n-1}", page=T07)
def _():
    A = sp.Matrix([[1, 6], [1, 0]])
    same(cp(A), lam**2 - lam - 6, "p(λ)")
    C = sp.Matrix([[3, -2], [1, 1]])
    same(C.inv() * A * C, sp.diag(3, -2), "diagonalización")
    same(C.inv(), sp.Rational(1, 5) * sp.Matrix([[1, 2], [-1, 3]]), "C^{-1}")
    same(C.inv() * columna(5, 0), columna(1, -1), "coeficientes")
    a = sucesion(1, 6, 0, 5, 20)
    require(a[:6] == [0, 5, 5, 35, 65, 275], "primeros términos")
    for n, valor in enumerate(a):
        same(3**n - (-2) ** n, valor, f"a_{n}")
        same((A**n * columna(5, 0))[1], valor, f"A^n x_0, n={n}")


@check("U3.T07.E2", "Fibonacci: fórmula de Binet y número áureo", page=T07)
def _():
    A = sp.Matrix([[1, 1], [1, 0]])
    same(cp(A), lam**2 - lam - 1, "p(λ)")
    phi = (1 + sp.sqrt(5)) / 2
    psi = (1 - sp.sqrt(5)) / 2
    require(es_autovector(A, (phi, 1), phi) and es_autovector(A, (psi, 1), psi), "autovectores (λ,1)")
    C = sp.Matrix([[phi, psi], [1, 1]])
    same(C.inv() * columna(1, 0), columna(1 / sp.sqrt(5), -1 / sp.sqrt(5)), "coeficientes")
    F = sucesion(1, 1, 0, 1, 40)
    require(F[:11] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], "primeros términos")
    for n, valor in enumerate(F):
        same(sp.expand((phi**n - psi**n) / sp.sqrt(5)), valor, f"Binet n={n}")
    require(abs(sp.N(psi)) < 1, "|ψ| < 1")
    # F_{n+1} − φ F_n = ψ^n, de donde F_{n+1}/F_n − φ = ψ^n / F_n → 0
    same(sp.expand(((phi**(n_sym + 1) - psi**(n_sym + 1)) - phi * (phi**n_sym - psi**n_sym)) / sp.sqrt(5)),
         sp.expand(psi**n_sym * (phi - psi) / sp.sqrt(5)), "identidad simbólica")
    for n in range(0, 30):
        same(sp.expand(F[n + 1] - phi * F[n]), sp.expand(psi**n), f"F_{n + 1} − φF_{n} = ψ^{n}")
    same(F[30], 832040, "F_30")
    require(abs(sp.Rational(F[31], F[30]) - phi) < sp.Rational(1, 10**12), "F_31/F_30 ≈ φ")


@check("U3.T07.E3", "Raíz doble: a_{n+1} = 4a_n − 4a_{n−1}", page=T07)
def _():
    A = sp.Matrix([[4, -4], [1, 0]])
    same(cp(A), (lam - 2) ** 2, "p(λ)")
    E2 = autoespacio(A, 2)
    require(len(E2) == 1 and mismo_subespacio(E2, [(2, 1)]), "E_2 de dimensión 1")
    require(not A.is_diagonalizable(), "compañera no diagonalizable")
    a = sucesion(4, -4, 1, 4, 25)
    require(a[:7] == [1, 4, 12, 32, 80, 192, 448], "primeros términos")
    for n, valor in enumerate(a):
        same((1 + n) * 2**n, valor, f"a_{n}")
    # n λ^n es solución cuando λ es raíz doble de λ² − 4λ + 4
    # con X = 2^{m−1}: (m+1)·2^{m+1} − 4·m·2^m + 4·(m−1)·2^{m−1} = X·[4(m+1) − 8m + 4(m−1)] = 0
    m, X = sp.symbols("m X")
    same(sp.expand((m + 1) * 4 * X - 4 * m * 2 * X + 4 * (m - 1) * X), 0, "(n+1)2^n verifica la recurrencia")


@check("U3.T07.E4", "Teselados con cuadrados y dominós de dos colores", page=T07)
def _():
    A = sp.Matrix([[1, 2], [1, 0]])
    same(cp(A), lam**2 - lam - 2, "p(λ)")
    require(raices(A) == {2: 1, -1: 1}, "raíces")

    def contar(n):
        # fichas: cuadrado (1), dominó rojo (2), dominó azul (2)
        if n < 0:
            return 0
        if n == 0:
            return 1
        return contar(n - 1) + 2 * contar(n - 2)

    t = sucesion(1, 2, 1, 1, 15)
    for n, valor in enumerate(t):
        same(contar(n), valor, f"conteo directo n={n}")
        same(sp.Rational(2 ** (n + 1) + (-1) ** n, 3), valor, f"fórmula n={n}")
    require(t[:6] == [1, 1, 3, 5, 11, 21], "primeros términos")


@check("U3.T07.E5", "Cadenas binarias sin dos unos consecutivos", page=T07)
def _():
    F = sucesion(1, 1, 0, 1, 20)
    for n in range(1, 15):
        total = sum(1 for s in itertools.product("01", repeat=n) if "11" not in "".join(s))
        same(total, F[n + 2], f"b_{n} = F_{n + 2}")
    same(F[10 + 2], 144, "b_10")


@check("U3.T07.E6", "Llamadas de la recursión ingenua de Fibonacci", page=T07)
def _():
    F = sucesion(1, 1, 0, 1, 30)

    def llamadas(n):
        return 1 if n < 2 else 1 + llamadas(n - 1) + llamadas(n - 2)

    for n in range(0, 20):
        same(llamadas(n), 2 * F[n + 1] - 1, f"L({n})")
    same(llamadas(10), 177, "L(10)")


# ---------------------------------------------------------------------------
# 3.8 Cadenas de Markov
# ---------------------------------------------------------------------------
def estacionario(P):
    base = (sp.eye(P.rows) - P).nullspace()
    require(len(base) == 1, "autoespacio de 1 de dimensión 1")
    v = base[0]
    return v / sum(v)


def es_regular(P, maximo=20):
    Q = P
    for k in range(1, maximo + 1):
        if all(x > 0 for x in Q):
            return k
        Q = Q * P
    return None


@check("U3.T08.E1", "Usuarios gratuitos y suscriptores", page=T08)
def _():
    r = sp.Rational
    P = sp.Matrix([[r(4, 5), r(3, 10)], [r(1, 5), r(7, 10)]])
    require(all(sum(P.col(j)) == 1 for j in range(2)), "estocástica por columnas")
    x0 = columna(1, 0)
    same(P * x0, columna(r(4, 5), r(1, 5)), "x_1")
    same(P**2 * x0, columna(r(7, 10), r(3, 10)), "x_2")
    same(cp(P), lam**2 - r(3, 2) * lam + r(1, 2), "p(λ)")
    require(raices(P) == {1: 1, r(1, 2): 1}, "autovalores")
    same(estacionario(P), columna(r(3, 5), r(2, 5)), "estado estacionario")
    C = sp.Matrix([[3, 1], [2, -1]])
    same(C.inv(), r(1, 5) * sp.Matrix([[1, 1], [2, -3]]), "C^{-1}")
    same(C.inv() * P * C, sp.diag(1, r(1, 2)), "diagonalización")
    k = sp.symbols("k", integer=True, positive=True)
    h = r(1, 2) ** k
    Pk = r(1, 5) * sp.Matrix([[3 + 2 * h, 3 - 3 * h], [2 - 2 * h, 2 + 3 * h]])
    same(C * sp.diag(1, h) * C.inv(), Pk, "P^k")
    for j in range(1, 6):
        same(P**j, Pk.subs(k, j), f"P^{j}")
    L = sp.Matrix([[r(3, 5), r(3, 5)], [r(2, 5), r(2, 5)]])
    same(Pk - L, h * r(1, 5) * sp.Matrix([[2, -3], [-2, 3]]), "P^k − L = (1/2)^k M")


@check("U3.T08.E2", "Servidor activo/saturado/caído", page=T08)
def _():
    r = sp.Rational
    P = r(1, 10) * sp.Matrix([[8, 3, 5], [1, 6, 0], [1, 1, 5]])
    require(all(sum(P.col(j)) == 1 for j in range(3)), "estocástica por columnas")
    same(estacionario(P), columna(r(2, 3), r(1, 6), r(1, 6)), "estado estacionario")
    require(es_regular(P) == 2, "P^2 positiva")
    same(P**2, sp.Matrix([[r(18, 25), r(47, 100), r(13, 20)], [r(7, 50), r(39, 100), r(1, 20)],
                          [r(7, 50), r(7, 50), r(3, 10)]]), "P^2")
    same(sp.factor(cp(P)), sp.factor((lam - 1) * (lam - r(1, 2)) * (lam - r(2, 5))), "p(λ)")
    C = sp.Matrix([[4, -1, -2], [1, 1, 1], [1, 0, 1]])
    same(C.det(), 6, "det C")
    same(C.inv(), sp.Matrix([[r(1, 6), r(1, 6), r(1, 6)], [0, 1, -1], [-r(1, 6), -r(1, 6), r(5, 6)]]), "C^{-1}")
    same(C.inv() * P * C, sp.diag(1, r(1, 2), r(2, 5)), "diagonalización")
    same(C.inv() * columna(1, 0, 0), columna(r(1, 6), 0, -r(1, 6)), "coordenadas de x_0")
    k = sp.symbols("k", integer=True, positive=True)
    t = r(2, 5) ** k
    xk = columna(r(2, 3) + r(1, 3) * t, r(1, 6) - r(1, 6) * t, r(1, 6) - r(1, 6) * t)
    for j in range(0, 8):
        same(P**j * columna(1, 0, 0), xk.subs(k, j), f"x_{j}")
    same(P**3 * columna(1, 0, 0), columna(r(86, 125), r(39, 250), r(39, 250)), "x_3")
    L = C * sp.diag(1, 0, 0) * C.inv()
    same(L, sp.Matrix([[r(2, 3)] * 3, [r(1, 6)] * 3, [r(1, 6)] * 3]), "límite de P^k")


@check("U3.T08.E3", "Mini PageRank con cuatro páginas", page=T08)
def _():
    r = sp.Rational
    h = r(1, 2)
    # enlaces: 1→2, 1→3, 2→3, 2→4, 3→1, 4→1 (columna j = página de origen)
    P = sp.Matrix([[0, 0, 1, 1], [h, 0, 0, 0], [h, h, 0, 0], [0, h, 0, 0]])
    require(all(sum(P.col(j)) == 1 for j in range(4)), "estocástica por columnas")
    q = estacionario(P)
    same(q, columna(r(2, 5), r(1, 5), r(3, 10), r(1, 10)), "PageRank")
    require(es_regular(P) == 6, "P^6 es la primera potencia positiva")
    x0 = columna(*[r(1, 4)] * 4)
    same(P * x0, columna(r(1, 2), r(1, 8), r(1, 4), r(1, 8)), "x_1")
    same(P**2 * x0, columna(r(3, 8), r(1, 4), r(5, 16), r(1, 16)), "x_2")
    same(sp.factor(cp(P)), sp.factor(lam * (lam - 1) * (lam**2 + lam + h)), "p(λ)")
    x30 = P**30 * x0
    require(max(abs(x30[i] - q[i]) for i in range(4)) < r(1, 10**5), "x_30 ≈ q")
    d = r(17, 20)
    G = d * P + (1 - d) / 4 * sp.ones(4, 4)
    require(all(x > 0 for x in G), "G positiva")
    g = estacionario(G)
    aprox = [r(3869, 10000), r(2020, 10000), r(2878, 10000), r(1233, 10000)]
    require(all(abs(g[i] - aprox[i]) < r(1, 20000) for i in range(4)), f"PageRank amortiguado ≈ {list(map(sp.N, g))}")
    require(g[0] > g[2] > g[1] > g[3], "mismo orden 1, 3, 2, 4")


@check("U3.T08.E4", "Cadenas no regulares", page=T08)
def _():
    S = sp.Matrix([[0, 1], [1, 0]])
    require(raices(S) == {1: 1, -1: 1}, "autovalores ±1")
    x0 = columna(1, 0)
    same(S**5 * x0, columna(0, 1), "x impar")
    same(S**6 * x0, columna(1, 0), "x par")
    require(es_regular(S) is None, "S no es regular")
    I2 = sp.eye(2)
    require(len((I2 - I2).nullspace()) == 2, "I: autoespacio de 1 de dimensión 2")


@check("U3.T07.E7", "Fibonacci iterativo con enteros exactos", page=T07)
def _():
    def fib_iterativo(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    same(fib_iterativo(30), 832040, "F_30")
    same(fib_iterativo(90), 2880067194370816120, "F_90")
    same(fib_iterativo(31), 1346269, "F_31")
    require(abs(sp.Rational(1346269, 832040) - (1 + sp.sqrt(5)) / 2) < sp.Rational(1, 10**11), "F_31/F_30 ≈ φ")
    require(abs(sp.N((1 + sp.sqrt(5)) / 2) ** 10 / sp.sqrt(5) - 55) < sp.Rational(1, 100), "φ^10/√5 ≈ 55")
    # L(n) = 2 F_{n+1} − 1 para n = 30, 50
    same(2 * fib_iterativo(31) - 1, 2692537, "L(30)")
    same(2 * fib_iterativo(51) - 1, 40730022147, "L(50)")
    # autoevaluación 1: λ² − 5λ + 6 y λ² − 6λ + 9
    same(sp.factor(lam**2 - 5 * lam + 6), (lam - 2) * (lam - 3), "raíces 2 y 3")
    same(sp.factor(lam**2 - 6 * lam + 9), (lam - 3) ** 2, "raíz doble 3")


@check("U3.T08.E5", "Estado absorbente: converge sin ser regular", page=T08)
def _():
    r = sp.Rational
    P = sp.Matrix([[1, r(1, 2)], [0, r(1, 2)]])
    require(raices(P) == {1: 1, r(1, 2): 1}, "autovalores 1 y 1/2")
    for k in range(1, 10):
        same(P**k, sp.Matrix([[1, 1 - r(1, 2**k)], [0, r(1, 2**k)]]), f"P^{k}")
        require((P**k)[1, 0] == 0, "entrada (2,1) nula: no regular")
    same(estacionario(P), columna(1, 0), "estacionario (1,0)")
    # PageRank: aproximación de x_20 y polinomio característico (texto de 3.8)
    h = r(1, 2)
    PR = sp.Matrix([[0, 0, 1, 1], [h, 0, 0, 0], [h, h, 0, 0], [0, h, 0, 0]])
    x20 = PR**20 * columna(*[r(1, 4)] * 4)
    aprox = [r(4001, 10000), r(2000, 10000), r(2999, 10000), r(1000, 10000)]
    require(all(abs(x20[i] - aprox[i]) < r(1, 5000) for i in range(4)), "x_20 ≈ (0,4001; 0,2000; 0,2999; 0,1000)")
    # Autoevaluación: [[0.5,0.2],[0.5,0.8]] y [[0.9,0.4],[0.1,0.6]]
    for Q in (sp.Matrix([[r(1, 2), r(1, 5)], [r(1, 2), r(4, 5)]]), sp.Matrix([[r(9, 10), r(2, 5)], [r(1, 10), r(3, 5)]])):
        require(all(x >= 0 for x in Q) and all(sum(Q.col(j)) == 1 for j in range(2)), "estocástica")
    same(estacionario(sp.Matrix([[r(9, 10), r(2, 5)], [r(1, 10), r(3, 5)]])), columna(r(4, 5), r(1, 5)), "estacionario 4:1")
    S3 = sp.Matrix([[r(8, 10), r(3, 10), r(5, 10)], [r(1, 10), r(6, 10), 0], [r(1, 10), r(1, 10), r(5, 10)]])
    same((sp.eye(3) - S3).det(), 0, "det(I-P)=0")
