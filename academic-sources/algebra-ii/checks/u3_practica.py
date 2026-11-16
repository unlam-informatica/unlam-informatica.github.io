"""Comprobaciones de los ejercicios de la práctica de la Unidad 3 (autovalores y autovectores).

Cada función recalcula desde los datos del enunciado: polinomios característicos, raíces con
multiplicidad, autoespacios (``nullspace``), factorizaciones ``A C = C D``, potencias contra la
fórmula cerrada, términos de recurrencias y vectores estacionarios.
Convención: ``p_A(λ) = det(λI − A)``, ``A = C D C^{-1}`` con autovectores en las columnas de ``C`` y
matrices de transición estocásticas por columnas (``x_{k+1} = P x_k``).
Los ejercicios U3.19, U3.20 y U3.25 son demostraciones (``verificacion: razonamiento``) y no se registran.
"""
import sympy as sp

from content_pipeline.mathcheck import check, require, same

lam = sp.symbols("lambda")

INI = "/algebra-ii/unidad-3/practica/nivel-inicial/"
INT = "/algebra-ii/unidad-3/practica/nivel-intermedio/"
AVZ = "/algebra-ii/unidad-3/practica/nivel-avanzado/"
GUI = "/algebra-ii/unidad-3/practica/guia-integradora/"

R = sp.Rational


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def cp(A):
    """Polinomio característico p_A(λ) = det(λI − A), expandido."""
    return sp.expand((lam * sp.eye(A.rows) - A).det())


def raices(A):
    """Raíces de p_A con su multiplicidad algebraica."""
    return sp.roots(sp.Poly(cp(A), lam))


def autoespacio(A, valor):
    """Base de E_λ(A) = nul(λI − A)."""
    return (valor * sp.eye(A.rows) - A).nullspace()


def mismo_subespacio(base, esperado):
    """Dos familias generan el mismo subespacio (comparación por rangos)."""
    X = sp.Matrix.hstack(*[sp.Matrix(b) for b in base])
    Y = sp.Matrix.hstack(*[sp.Matrix(e) for e in esperado])
    return X.rank() == Y.rank() == sp.Matrix.hstack(X, Y).rank()


def col(*valores):
    return sp.Matrix(valores)


def diag(*valores):
    n = len(valores)
    D = sp.zeros(n, n)
    for i, v in enumerate(valores):
        D[i, i] = v
    return D


def es_autovector(A, v, valor):
    v = sp.Matrix(v)
    return any(x != 0 for x in v) and A * v == valor * v


def mg(A, valor):
    return len(autoespacio(A, valor))


def diagonaliza(A, C, D):
    """A C = C D con C inversible."""
    return A * C == C * D and C.det() != 0


def estocastica(P):
    n = P.rows
    return all(x >= 0 for x in P) and all(sum(P[i, j] for i in range(n)) == 1 for j in range(n))


def estacionario(P):
    v = autoespacio(P, 1)
    require(len(v) == 1, "autoespacio de 1 de dimensión 1")
    s = sum(v[0])
    return v[0] / s


# ---------------------------------------------------------------------------
# Nivel inicial
# ---------------------------------------------------------------------------
@check("U3.01", "Autovectores por definición y determinante de I-A", page=INI)
def _():
    A = sp.Matrix([[1, 2], [3, 0]])
    require(es_autovector(A, (1, 1), 3), "u autovector de 3")
    require(es_autovector(A, (2, -3), -2), "v autovector de -2")
    Aw = A * col(1, 0)
    same(Aw, col(1, 3), "Aw")
    require(sp.Matrix.hstack(Aw, col(1, 0)).det() != 0, "w no es autovector")
    same((sp.eye(2) - A).det(), -6, "det(I-A)")
    same(cp(A), lam**2 - lam - 6, "p_A")


@check("U3.02", "Proyección ortogonal sobre una recta", page=INI)
def _():
    u = col(1, 2)
    P = (u * u.T) / (u.T * u)[0, 0]
    same(P, sp.Matrix([[R(1, 5), R(2, 5)], [R(2, 5), R(4, 5)]]), "matriz de la proyección")
    require(es_autovector(P, (1, 2), 1), "E_1")
    same(P * col(2, -1), col(0, 0), "E_0")
    C = sp.Matrix([[1, 2], [2, -1]])
    same(C * diag(1, 0) * C.inv(), P, "A = C D C^-1")
    same(cp(P), lam**2 - lam, "p_A")


@check("U3.03", "Autovalores y autoespacios 2x2", page=INI)
def _():
    A = sp.Matrix([[1, 4], [2, 3]])
    same(cp(A), lam**2 - 4 * lam - 5, "p_A")
    require(raices(A) == {5: 1, -1: 1}, "raíces 5 y -1")
    require(mismo_subespacio(autoespacio(A, 5), [(1, 1)]), "E_5")
    require(mismo_subespacio(autoespacio(A, -1), [(2, -1)]), "E_-1")
    same(A.trace(), 4, "traza")
    same(A.det(), -5, "determinante")


@check("U3.04", "Multiplicidades en una 3x3 no diagonalizable", page=INI)
def _():
    A = sp.Matrix([[2, 1, -1], [-1, 3, 0], [-1, 1, 2]])
    same(cp(A), sp.expand((lam - 2) ** 2 * (lam - 3)), "p_A")
    require(raices(A) == {2: 2, 3: 1}, "multiplicidades algebraicas")
    require(mismo_subespacio(autoespacio(A, 2), [(1, 1, 1)]) and mg(A, 2) == 1, "E_2")
    require(mismo_subespacio(autoespacio(A, 3), [(0, 1, 1)]) and mg(A, 3) == 1, "E_3")
    same(A * col(1, 1, 1), col(2, 2, 2), "A(1,1,1)")
    same(A * col(0, 1, 1), col(0, 3, 3), "A(0,1,1)")
    require(mg(A, 2) < 2, "no diagonalizable")


@check("U3.05", "Matrices sin autovalores reales", page=INI)
def _():
    Rg = sp.Matrix([[0, -1], [1, 0]])
    B = sp.Matrix([[2, -1], [1, 2]])
    same(cp(Rg), lam**2 + 1, "p_R")
    same(cp(B), lam**2 - 4 * lam + 5, "p_B")
    require(B.trace() ** 2 - 4 * B.det() < 0, "discriminante negativo")
    A3 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 2]])
    same(cp(A3), sp.expand((lam**2 + 1) * (lam - 2)), "p de la 3x3")
    require(es_autovector(A3, (0, 0, 1), 2), "autovector real de la 3x3")
    require(mg(A3, 2) == 1 and mg(A3, 0) == 0, "único autovalor real 2")


@check("U3.06", "V/F: autovectores y suma de matrices", page=INI)
def _():
    A = sp.Matrix([[1, 0], [0, 0]])
    B = sp.Matrix([[0, 0], [0, 1]])
    require(es_autovector(A, (1, 0), 1) and es_autovector(B, (0, 1), 1), "autovalores 1 de A y de B")
    same(A + B, sp.eye(2), "A+B = I")
    same(cp(A + B), (lam - 1) ** 2, "p_{A+B}")
    require((2 * sp.eye(2) - (A + B)).det() != 0, "2 no es autovalor de A+B")
    # b) A v = a v y B v = b v implican (A+B) v = (a+b) v
    A2 = sp.Matrix([[2, 1], [0, 3]])
    B2 = sp.Matrix([[5, 1], [0, -1]])
    v = col(1, 0)
    require(es_autovector(A2, v, 2) and es_autovector(B2, v, 5) and es_autovector(A2 + B2, v, 7), "(A+B)v=(a+b)v")


@check("U3.07", "Propiedades en una matriz triangular", page=INI)
def _():
    A = sp.Matrix([[2, 5, -1], [0, 3, 4], [0, 0, -1]])
    require(raices(A) == {2: 1, 3: 1, -1: 1}, "autovalores 2, 3, -1")
    same(A.trace(), 4, "traza")
    same(A.det(), -6, "determinante")
    require(raices(A.inv()) == {R(1, 2): 1, R(1, 3): 1, -1: 1}, "autovalores de A^-1")
    require(raices(A**3 + 2 * sp.eye(3)) == {10: 1, 29: 1, 1: 1}, "autovalores de A^3+2I")
    q = A**2 - 3 * A
    same(q, sp.Matrix([[-2, 10, 22], [0, 0, -4], [0, 0, 4]]), "q(A)")
    same(q.det(), 0, "q(A) no inversible")
    require(raices(q) == {-2: 1, 0: 1, 4: 1}, "autovalores de q(A)")


@check("U3.08", "Matriz de rango 1: E_0 y diagonalización", page=INI)
def _():
    A = sp.Matrix([[1, -1, 2], [2, -2, 4], [-1, 1, -2]])
    same(A.rank(), 1, "rango")
    same(cp(A), sp.expand(lam**2 * (lam + 3)), "p_A")
    require(mg(A, 0) == 2 and mismo_subespacio(autoespacio(A, 0), [(1, 1, 0), (-2, 0, 1)]), "E_0")
    require(mg(A, -3) == 1 and mismo_subespacio(autoespacio(A, -3), [(1, 2, -1)]), "E_-3")
    C = sp.Matrix([[1, -2, 1], [1, 0, 2], [0, 1, -1]])
    require(diagonaliza(A, C, diag(0, 0, -3)), "AC = CD")


# ---------------------------------------------------------------------------
# Nivel intermedio
# ---------------------------------------------------------------------------
@check("U3.09", "Diagonalización 3x3 con autovalores 1, 2, -3", page=INT)
def _():
    A = sp.Matrix([[2, -1, 1], [5, -4, 1], [5, -5, 2]])
    same(cp(A), lam**3 - 7 * lam + 6, "p_A")
    require(raices(A) == {1: 1, 2: 1, -3: 1}, "raíces")
    require(mismo_subespacio(autoespacio(A, 1), [(1, 1, 0)]), "E_1")
    require(mismo_subespacio(autoespacio(A, 2), [(1, 1, 1)]), "E_2")
    require(mismo_subespacio(autoespacio(A, -3), [(0, 1, 1)]), "E_-3")
    C = sp.Matrix([[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    same(C.det(), -1, "det C")
    require(diagonaliza(A, C, diag(1, 2, -3)), "AC = CD")
    same(C * diag(1, 2, -3) * C.inv(), A, "A = C D C^-1")


@check("U3.10", "Autovalor doble con m_g = m_a", page=INT)
def _():
    A = sp.Matrix([[5, -3, 3], [3, -1, 3], [3, -3, 5]])
    same(cp(A), sp.expand((lam - 2) ** 2 * (lam - 5)), "p_A")
    require(raices(A) == {2: 2, 5: 1}, "multiplicidades")
    require(mg(A, 2) == 2 and mismo_subespacio(autoespacio(A, 2), [(1, 1, 0), (0, 1, 1)]), "E_2")
    require(mg(A, 5) == 1 and mismo_subespacio(autoespacio(A, 5), [(1, 1, 1)]), "E_5")
    C = sp.Matrix([[1, 0, 1], [1, 1, 1], [0, 1, 1]])
    same(C.det(), 1, "det C")
    require(diagonaliza(A, C, diag(2, 2, 5)), "AC = CD")
    same(A.trace(), 9, "traza")
    same(A.det(), 20, "determinante")


@check("U3.11", "Diagonalizabilidad según el parámetro a", page=INT)
def _():
    a = sp.symbols("a")
    Aa = sp.Matrix([[2, 0, 0], [a, 2, 0], [1, 1, 5]])
    same(cp(Aa), sp.expand((lam - 2) ** 2 * (lam - 5)), "p simbólico")
    for valor in (1, -2, 3, R(1, 2)):
        A = Aa.subs(a, valor)
        require(mg(A, 2) == 1 and mg(A, 5) == 1, f"a={valor}: no diagonalizable")
    A0 = Aa.subs(a, 0)
    require(mg(A0, 2) == 2 and mg(A0, 5) == 1, "a=0: m_g = m_a")
    C = sp.Matrix([[1, -3, 0], [-1, 0, 0], [0, 1, 1]])
    same(C.det(), -3, "det C")
    require(diagonaliza(A0, C, diag(2, 2, 5)), "AC = CD para a=0")


@check("U3.12", "V/F sobre diagonalización", page=INT)
def _():
    # a) tres autovalores distintos => diagonalizable (matriz del ejercicio 9)
    A = sp.Matrix([[2, -1, 1], [5, -4, 1], [5, -5, 2]])
    C = sp.Matrix([[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    require(diagonaliza(A, C, diag(1, 2, -3)), "a) diagonalizable")
    # b) A^{-1} = C D^{-1} C^{-1}
    require(diagonaliza(A.inv(), C, diag(1, R(1, 2), -R(1, 3))), "b) A^-1 diagonalizable con D^-1")
    # c) contraejemplo A = 2I
    A2 = 2 * sp.eye(2)
    require(raices(A2) == {2: 2} and mg(A2, 2) == 2, "c) 2I diagonalizable con m_a = 2")
    # d) A^t = (C^t)^{-1} D C^t
    Ct = C.T
    same(Ct.inv() * diag(1, 2, -3) * Ct, A.T, "d) A^t")


@check("U3.13", "Contraejemplos de semejanza", page=INT)
def _():
    A = sp.Matrix([[1, 1], [0, 1]])
    I2 = sp.eye(2)
    same(cp(A), cp(I2), "mismo p")
    require((I2 - A).rank() == 1 and (I2 - I2).rank() == 0, "rangos distintos: no semejantes")
    A2 = sp.Matrix([[1, 0], [0, 2]])
    B2 = sp.Matrix([[1, 1], [0, 2]])
    same(cp(A2), cp(B2), "mismo p en b)")
    require(raices(B2) == {1: 1, 2: 1}, "autovalores distintos: diagonalizable")
    require(es_autovector(A2, (0, 1), 2), "(0,1) autovector de A")
    Bv = B2 * col(0, 1)
    same(Bv, col(1, 2), "B(0,1)")
    require(sp.Matrix.hstack(Bv, col(0, 1)).det() != 0, "(0,1) no es autovector de B")
    require(mismo_subespacio(autoespacio(B2, 2), [(1, 1)]), "E_2(B)")


@check("U3.14", "Semejanza explícita de dos matrices 2x2", page=INT)
def _():
    A = sp.Matrix([[0, 1], [6, 1]])
    B = sp.Matrix([[-2, 5], [0, 3]])
    same(cp(A), lam**2 - lam - 6, "p_A")
    same(cp(B), lam**2 - lam - 6, "p_B")
    require(mismo_subespacio(autoespacio(A, 3), [(1, 3)]) and mismo_subespacio(autoespacio(A, -2), [(1, -2)]), "autoespacios de A")
    require(mismo_subespacio(autoespacio(B, 3), [(1, 1)]) and mismo_subespacio(autoespacio(B, -2), [(1, 0)]), "autoespacios de B")
    CA = sp.Matrix([[1, 1], [3, -2]])
    CB = sp.Matrix([[1, 1], [1, 0]])
    S = CA * CB.inv()
    same(S, sp.Matrix([[1, 0], [-2, 5]]), "S")
    same(S.det(), 5, "det S")
    same(A * S, S * B, "AS = SB")
    same(S.inv() * A * S, B, "S^-1 A S = B")
    G = sp.Matrix([[3, 1], [0, -3]])
    require(A.det() == -6 and G.det() == -9, "determinantes distintos")


@check("U3.15", "Fórmula de A^k y potencias negativas", page=INT)
def _():
    A = sp.Matrix([[3, -2], [1, 0]])
    same(cp(A), sp.expand((lam - 1) * (lam - 2)), "p_A")
    C = sp.Matrix([[1, 2], [1, 1]])
    require(diagonaliza(A, C, diag(1, 2)), "AC = CD")
    same(C.inv(), sp.Matrix([[-1, 2], [1, -1]]), "C^-1")
    for k in range(-4, 9):
        formula = sp.Matrix([[R(2) ** (k + 1) - 1, 2 - R(2) ** (k + 1)], [R(2) ** k - 1, 2 - R(2) ** k]])
        same(A**k, formula, f"A^{k}")
    same(A**10, sp.Matrix([[2047, -2046], [1023, -1022]]), "A^10")
    same(A**-3, sp.Matrix([[-R(3, 4), R(7, 4)], [-R(7, 8), R(15, 8)]]), "A^-3")


@check("U3.16", "Inversibilidad de A^k - I y de A^2 + A - 2I", page=INT)
def _():
    A = sp.Matrix([[6, -4, 4], [2, -3, 2], [-6, 3, -4]])
    same(cp(A), sp.expand((lam - 2) * (lam + 1) * (lam + 2)), "p_A")
    C = sp.Matrix([[-1, 0, 1], [0, 1, 2], [1, 1, 0]])
    require(diagonaliza(A, C, diag(2, -1, -2)), "AC = CD")
    for k in range(1, 9):
        d = (A**k - sp.eye(3)).det()
        esperado = (2**k - 1) * ((-1) ** k - 1) * ((-2) ** k - 1)
        same(d, esperado, f"det(A^{k}-I)")
        require((d != 0) == (k % 2 == 1), f"inversible solo si k impar (k={k})")
    B = A**2 + A - 2 * sp.eye(3)
    same(B, sp.Matrix([[8, -4, 4], [-4, 2, -4], [-12, 6, -8]]), "B")
    same(B.det(), 0, "B no inversible")
    require(raices(B) == {4: 1, -2: 1, 0: 1}, "autovalores de B")


@check("U3.17", "Embaldosado de 2xn: a_{n+1} = a_n + 2 a_{n-1}", page=INT)
def _():
    A = sp.Matrix([[1, 2], [1, 0]])
    same(cp(A), lam**2 - lam - 2, "p_A")
    require(mismo_subespacio(autoespacio(A, 2), [(2, 1)]), "E_2")
    require(mismo_subespacio(autoespacio(A, -1), [(-1, 1)]), "E_-1")
    a = [1, 1]
    for n in range(2, 14):
        a.append(a[-1] + 2 * a[-2])
    x0 = col(1, 1)
    for n in range(0, 12):
        xn = A**n * x0
        same(xn[1], R(2 ** (n + 1) + (-1) ** n, 3), f"fórmula cerrada n={n}")
        same(xn[1], a[n], f"recurrencia n={n}")
        same(xn[0], a[n + 1], f"a_(n+1) n={n}")
    same(a[10], 683, "a_10")
    same(a[2], 3, "a_2")


@check("U3.18", "Cadena de Markov del estado de un hilo", page=INT)
def _():
    P = sp.Matrix([[5, 2, 1], [2, 5, 1], [3, 3, 8]]) / 10
    require(estocastica(P), "estocástica por columnas")
    x1 = P * col(1, 0, 0)
    same(x1, col(R(1, 2), R(1, 5), R(3, 10)), "x1")
    x2 = P * x1
    same(x2, col(R(8, 25), R(23, 100), R(9, 20)), "x2")
    pi = estacionario(P)
    same(pi, col(R(1, 5), R(1, 5), R(3, 5)), "estacionario")
    same(P * pi, pi, "P pi = pi")
    require(all(x > 0 for x in P), "entradas positivas: regular")
    same(cp(P), sp.expand((lam - 1) * (lam - R(1, 2)) * (lam - R(3, 10))), "p_P")
    L = sp.Matrix.hstack(pi, pi, pi)
    P40 = P**40
    require(all(abs(P40[i, j] - L[i, j]) < R(1, 10**9) for i in range(3) for j in range(3)), "P^40 ≈ límite")


# ---------------------------------------------------------------------------
# Nivel avanzado
# ---------------------------------------------------------------------------
@check("U3.21", "Dos parámetros: diagonalizable si y solo si a = 0", page=AVZ)
def _():
    a, b = sp.symbols("a b")
    Ab = sp.Matrix([[2, a, b], [0, 2, 0], [0, 0, 3]])
    same(cp(Ab), sp.expand((lam - 2) ** 2 * (lam - 3)), "p simbólico")
    for va in (1, -3, R(1, 2)):
        for vb in (0, 2, -1):
            require(mg(Ab.subs({a: va, b: vb}), 2) == 1, f"a={va}, b={vb}: no diagonalizable")
    for vb in (0, 2, -1, 5):
        A = Ab.subs({a: 0, b: vb})
        require(mg(A, 2) == 2 and mg(A, 3) == 1, f"a=0, b={vb}: diagonalizable")
        C = sp.Matrix([[1, 0, vb], [0, 1, 0], [0, 0, 1]])
        require(diagonaliza(A, C, diag(2, 2, 3)), f"AC = CD (b={vb})")
        for k in range(0, 7):
            formula = sp.Matrix([[2**k, 0, vb * (3**k - 2**k)], [0, 2**k, 0], [0, 0, 3**k]])
            same(A**k, formula, f"A^{k} (b={vb})")


@check("U3.22", "Contraejemplo: diagonalizables con suma y producto no diagonalizables", page=AVZ)
def _():
    A = sp.Matrix([[1, 0], [0, 0]])
    B = sp.Matrix([[0, 1], [0, 1]])
    same(cp(B), lam**2 - lam, "p_B")
    require(raices(B) == {0: 1, 1: 1}, "B tiene autovalores distintos")
    require(mismo_subespacio(autoespacio(B, 1), [(1, 1)]) and mismo_subespacio(autoespacio(B, 0), [(1, 0)]), "autoespacios de B")
    S = A + B
    same(S, sp.Matrix([[1, 1], [0, 1]]), "A+B")
    require(raices(S) == {1: 2} and mg(S, 1) == 1, "A+B no diagonalizable")
    Pr = A * B
    same(Pr, sp.Matrix([[0, 1], [0, 0]]), "AB")
    same(Pr * Pr, sp.zeros(2, 2), "(AB)^2 = 0")
    require(raices(Pr) == {0: 2} and mg(Pr, 0) == 1, "AB no diagonalizable")
    same(B * A, sp.zeros(2, 2), "BA = 0, distinto de AB")


@check("U3.23", "Recurrencia con raíz doble: T(n) = (n+2) 2^(n-1)", page=AVZ)
def _():
    A = sp.Matrix([[4, -4], [1, 0]])
    same(cp(A), sp.expand((lam - 2) ** 2), "p_A")
    require(raices(A) == {2: 2} and mg(A, 2) == 1, "no diagonalizable")
    N = A - 2 * sp.eye(2)
    same(N, sp.Matrix([[2, -4], [1, -2]]), "N")
    same(N * N, sp.zeros(2, 2), "N^2 = 0")
    T = [1, 3]
    for n in range(2, 13):
        T.append(4 * T[-1] - 4 * T[-2])
    x0 = col(3, 1)
    for n in range(0, 11):
        An = A**n
        same(An, 2**n * sp.eye(2) + n * R(2) ** (n - 1) * N if n > 0 else sp.eye(2), f"A^{n}")
        xn = An * x0
        same(xn[1], R((n + 2) * 2**n, 2), f"fórmula cerrada n={n}")
        same(xn[1], T[n], f"recurrencia n={n}")
    same(T[10], 6144, "T(10)")


@check("U3.24", "Navegación en un sitio de tres páginas", page=AVZ)
def _():
    P = sp.Matrix([[0, R(1, 2), 1], [R(1, 2), 0, 0], [R(1, 2), R(1, 2), 0]])
    require(estocastica(P), "estocástica por columnas")
    pi = estacionario(P)
    same(pi, col(R(4, 9), R(2, 9), R(1, 3)), "estacionario")
    same(P * pi, pi, "P pi = pi")
    same(cp(P), sp.expand((lam - 1) * (lam + R(1, 2)) ** 2), "p_P")
    require(mg(P, -R(1, 2)) == 1, "autovalor -1/2 defectuoso")
    P4 = P**4
    same(P4, sp.Matrix([[R(9, 16), R(1, 2), R(1, 4)], [R(1, 8), R(3, 16), R(3, 8)], [R(5, 16), R(5, 16), R(3, 8)]]), "P^4")
    require(all(x > 0 for x in P4), "P^4 positiva: regular")
    L = sp.Matrix.hstack(pi, pi, pi)
    P80 = P**80
    require(all(abs(P80[i, j] - L[i, j]) < R(1, 10**9) for i in range(3) for j in range(3)), "P^80 ≈ límite")


@check("U3.26", "Cadena de dos estados con parámetro a", page=AVZ)
def _():
    a = sp.symbols("a")
    P = sp.Matrix([[1 - a, R(1, 2)], [a, R(1, 2)]])
    same(sp.expand(cp(P) - (lam - 1) * (lam - (R(1, 2) - a))), 0, "p_P = (λ-1)(λ-(1/2-a))")
    for va in (R(1, 6), R(1, 2), 1, R(1, 3)):
        Pa = P.subs(a, va)
        require(estocastica(Pa), f"estocástica (a={va})")
        pi = estacionario(Pa)
        same(pi, col(1, 2 * va) / (1 + 2 * va), f"estacionario (a={va})")
        L = sp.Matrix.hstack(pi, pi)
        Pk = Pa**60
        require(all(abs(Pk[i, j] - L[i, j]) < R(1, 10**9) for i in range(2) for j in range(2)), f"límite (a={va})")
    same(1 / (1 + 2 * R(1, 6)), R(3, 4), "a = 1/6 da exactamente 75%")
    require(1 / (1 + 2 * R(1, 5)) < R(3, 4) and 1 / (1 + 2 * R(1, 7)) > R(3, 4), "umbral a <= 1/6")
    P0 = P.subs(a, 0)
    same(estacionario(P0), col(1, 0), "a = 0")
    P12 = P.subs(a, R(1, 2))
    same(P12 * P12, P12, "a = 1/2: P^2 = P")


# ---------------------------------------------------------------------------
# Guía integradora
# ---------------------------------------------------------------------------
@check("U3.27", "Problema con parámetro k: A_k y potencias", page=GUI)
def _():
    k = sp.symbols("k")
    Ak = sp.Matrix([[k, 0, 1], [0, 2, 0], [0, 0, 2]])
    same(cp(Ak), sp.expand((lam - k) * (lam - 2) ** 2), "p simbólico")
    for vk in (-1, 0, 1, 3, R(5, 2), 7):
        A = Ak.subs(k, vk)
        require(mg(A, 2) == 2 and mg(A, vk) == 1, f"k={vk} diagonalizable")
    A2 = Ak.subs(k, 2)
    require(mg(A2, 2) == 2 and raices(A2) == {2: 3}, "k=2 no diagonalizable (m_g=2<3)")
    A = Ak.subs(k, 3)
    require(mismo_subespacio(autoespacio(A, 3), [(1, 0, 0)]), "E_3")
    require(mismo_subespacio(autoespacio(A, 2), [(0, 1, 0), (1, 0, -1)]), "E_2")
    C = sp.Matrix([[1, 0, 1], [0, 1, 0], [0, 0, -1]])
    require(diagonaliza(A, C, diag(3, 2, 2)), "AC = CD")
    same(C.inv(), C, "C^-1")
    for n in range(0, 8):
        formula = sp.Matrix([[3**n, 0, 3**n - 2**n], [0, 2**n, 0], [0, 0, 2**n]])
        same(A**n, formula, f"A^{n}")
        singular = (A**n - 4 * sp.eye(3)).det() == 0
        require(singular == (n == 2), f"A^n-4I singular solo para n=2 (n={n})")


@check("U3.28", "Operador T(p) = (x+1) p' en R_2[x]", page=GUI)
def _():
    x = sp.symbols("x")

    def T(p):
        return sp.expand((x + 1) * sp.diff(p, x))

    base = [sp.Integer(1), x, x**2]

    def coords(p):
        p = sp.expand(p)
        return col(p.coeff(x, 0), p.coeff(x, 1), p.coeff(x, 2))

    M = sp.Matrix.hstack(*[coords(T(b)) for b in base])
    same(M, sp.Matrix([[0, 1, 0], [0, 1, 2], [0, 0, 2]]), "M(T)_B")
    same(cp(M), sp.expand(lam * (lam - 1) * (lam - 2)), "p_T")
    for p, v in ((sp.Integer(1), 0), (1 + x, 1), (sp.expand((1 + x) ** 2), 2)):
        same(T(p), sp.expand(v * p), f"T(p) = {v} p")
    Cb = sp.Matrix.hstack(coords(sp.Integer(1)), coords(1 + x), coords(sp.expand((1 + x) ** 2)))
    same(Cb.det(), 1, "det de la base B'")
    same(Cb.inv() * M * Cb, diag(0, 1, 2), "M(T)_B'")
    same(sp.expand(1 - 2 * (1 + x) + (1 + x) ** 2), x**2, "x^2 en B'")
    p = x**2
    for n in range(1, 7):
        p = T(p)
        same(p, sp.expand(-2 * (1 + x) + 2**n * (1 + x) ** 2), f"T^{n}(x^2)")


@check("U3.29", "Recurrencia a_{n+1} = 2a_n + 3a_{n-1}", page=GUI)
def _():
    A = sp.Matrix([[2, 3], [1, 0]])
    same(cp(A), sp.expand((lam - 3) * (lam + 1)), "p_A")
    require(mismo_subespacio(autoespacio(A, 3), [(3, 1)]) and mismo_subespacio(autoespacio(A, -1), [(-1, 1)]), "autoespacios")
    a = [2, 2]
    for n in range(2, 13):
        a.append(2 * a[-1] + 3 * a[-2])
    x0 = col(2, 2)
    for n in range(0, 11):
        xn = A**n * x0
        same(xn[1], 3**n + (-1) ** n, f"fórmula cerrada n={n}")
        same(xn[1], a[n], f"recurrencia n={n}")
    same(a[10], 59050, "a_10")
    for n in (5, 10, 20, 30):
        cociente = R(3 ** (n + 1) + (-1) ** (n + 1), 3**n + (-1) ** n)
        require(abs(cociente - 3) < R(4, 3**n) * 2, f"cociente cerca de 3 (n={n})")
    same((A - 2 * sp.eye(2)).det(), -3, "det(A-2I)")
    require(raices(A - 2 * sp.eye(2)) == {1: 1, -3: 1}, "autovalores de A-2I")
    for k in range(1, 9):
        d = (A**k - sp.eye(2)).det()
        require((d != 0) == (k % 2 == 1), f"A^k-I inversible solo si k impar (k={k})")


@check("U3.30", "Cadena de Markov de usuarios de una aplicación", page=GUI)
def _():
    P = sp.Matrix([[5, 1, 3], [3, 7, 3], [2, 2, 4]]) / 10
    require(estocastica(P), "estocástica por columnas")
    require(all(x > 0 for x in P), "regular")
    pi = estacionario(P)
    same(pi, col(R(1, 4), R(1, 2), R(1, 4)), "estacionario")
    same(P * pi, pi, "P pi = pi")
    same(cp(P), sp.expand((lam - 1) * (lam - R(2, 5)) * (lam - R(1, 5))), "p_P")
    require(mismo_subespacio(autoespacio(P, 1), [(1, 2, 1)]), "E_1")
    require(mismo_subespacio(autoespacio(P, R(2, 5)), [(-1, 1, 0)]), "E_2/5")
    require(mismo_subespacio(autoespacio(P, R(1, 5)), [(-1, 0, 1)]), "E_1/5")
    C = sp.Matrix([[1, -1, -1], [2, 1, 0], [1, 0, 1]])
    require(diagonaliza(P, C, diag(1, R(2, 5), R(1, 5))), "PC = CD")
    same(2000 * pi, col(500, 1000, 500), "2000 usuarios")
    P60 = P**60
    L = sp.Matrix.hstack(pi, pi, pi)
    require(all(abs(P60[i, j] - L[i, j]) < R(1, 10**9) for i in range(3) for j in range(3)), "P^60 ≈ límite")
    for x0 in (col(0, 0, 1), col(1, 0, 0)):
        y = P60 * x0
        require(all(abs(y[i] - pi[i]) < R(1, 10**9) for i in range(3)), "el límite no depende de x0")


@check("U3.31", "Traza, determinante y autovector: matriz 3x3 defectuosa", page=GUI)
def _():
    A = sp.Matrix([[-2, -2, 6], [-1, 1, 2], [-1, -1, 4]])
    require(es_autovector(A, (1, 1, 1), 2), "(1,1,1) autovector de 2")
    same(A.trace(), 3, "traza")
    same(A.det(), -4, "determinante")
    # mu + nu = 1, mu nu = -2  =>  t^2 - t - 2 = (t-2)(t+1)
    same(sp.expand((lam - 2) * (lam + 1)), lam**2 - lam - 2, "t^2 - t - 2")
    same(cp(A), sp.expand((lam - 2) ** 2 * (lam + 1)), "p_A")
    require(raices(A) == {2: 2, -1: 1}, "multiplicidades")
    require(mg(A, 2) == 1 and mismo_subespacio(autoespacio(A, 2), [(1, 1, 1)]), "E_2")
    require(mg(A, -1) == 1 and mismo_subespacio(autoespacio(A, -1), [(4, 1, 1)]), "E_-1")
    require(mg(A, 2) < raices(A)[2], "no diagonalizable")
    require(raices(A.inv()) == {R(1, 2): 2, -1: 1}, "autovalores de A^-1")
    Q = A**2 - A - 2 * sp.eye(3)
    same(Q, sp.Matrix([[0, -2, 2], [0, -2, 2], [0, -2, 2]]), "A^2 - A - 2I")
    same(Q.det(), 0, "no inversible")
    require(Q != sp.zeros(3, 3), "no es la matriz nula")
    same((A - 2 * sp.eye(3)) * (A + sp.eye(3)), Q, "(A-2I)(A+I)")
