"""Comprobaciones de los simulacros (integradores/simulacro-1 y simulacro-2)."""
import itertools

import sympy as sp

from content_pipeline.mathcheck import (check, gf_matmul, gf_nullspace, gf_rank, gf_span, hamming,
                                        min_distance, require, same, weight)

x = sp.symbols("x")
S1 = "/algebra-ii/integradores/simulacro-1/"
S2 = "/algebra-ii/integradores/simulacro-2/"


def _coeffs(p):
    """Coeficientes (a, b, c) de a + b x + c x^2."""
    poly = sp.Poly(sp.expand(p), x)
    return sp.Matrix([poly.coeff_monomial(x**k) for k in range(3)])


@check("S1.1", "Subespacio p(1)=2p(0), base y cambio de coordenadas", page=S1)
def _():
    a, b, c = sp.symbols("a b c")
    p = a + b * x + c * x**2
    solution = sp.solve(sp.Eq(p.subs(x, 1), 2 * p.subs(x, 0)), a, dict=True)[0]
    same(solution[a], b + c, "condición a = b + c")
    B = [1 + x, 1 + x**2]
    Bp = [2 + x + x**2, x - x**2]
    for q in B + Bp + [3 + x + 2 * x**2]:
        require(q.subs(x, 1) == 2 * q.subs(x, 0), f"{q} pertenece a S")
    require(sp.Matrix.hstack(*[_coeffs(q) for q in B]).rank() == 2, "B es LI")
    require(sp.Matrix.hstack(*[_coeffs(q) for q in Bp]).rank() == 2, "B' es LI")
    Mbp = sp.Matrix.hstack(*[_coeffs(q) for q in Bp])

    def coords(q):
        sol = sp.Matrix(sp.symbols("s t"))
        system = Mbp * sol - _coeffs(q)
        values = sp.solve(list(system), list(sol), dict=True)
        require(len(values) == 1, f"coordenadas únicas de {q}")
        return sol.subs(values[0])

    C = sp.Matrix.hstack(*[coords(q) for q in B])
    same(C, sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [sp.Rational(1, 2), -sp.Rational(1, 2)]]), "C_BB'")
    qB = sp.Matrix([1, 2])
    same(sum((qB[i] * B[i] for i in range(2)), sp.Integer(0)).expand(), 3 + x + 2 * x**2, "[q]_B")
    same(C * qB, sp.Matrix([sp.Rational(3, 2), -sp.Rational(1, 2)]), "[q]_B'")
    same(coords(3 + x + 2 * x**2), C * qB, "[q]_B' directo")


H1 = [[1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1]]
G1 = [[1, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1]]


@check("S1.2", "Código (6,3): generadora, codificación, síndrome y error doble", page=S1)
def _():
    require(gf_rank(H1, 2) == 3, "rango de H")
    require(len(gf_nullspace(H1, 2)) == 3, "dim C = 3")
    require(gf_matmul(G1, sp.Matrix(H1).T, 2) == [[0] * 3] * 3, "G H^t = 0")
    require(gf_rank(G1, 2) == 3, "filas de G LI")
    code = gf_span(G1, 2)
    require(len(code) == 8, "8 palabras")
    require(code == set(gf_span(gf_nullspace(H1, 2), 2)), "C = nul(H)")
    encoded = tuple((G1[0][i] + G1[2][i]) % 2 for i in range(6))
    require(encoded == (1, 0, 1, 0, 1, 1), "codificación de (1,0,1)")
    v = [1, 1, 0, 0, 0, 1]
    syndrome = [row[0] for row in gf_matmul(H1, [[t] for t in v], 2)]
    columns = [[row[j] for row in H1] for j in range(6)]
    require(syndrome == [1, 0, 0] and columns.index(syndrome) == 3, "síndrome = h_4")
    corrected = v[:]
    corrected[3] ^= 1
    require(tuple(corrected) == (1, 1, 0, 1, 0, 1) in code, "corrección")
    require(min_distance(code) == 3, "distancia mínima 3")
    double = [1, 1, 0, 0, 0, 0]
    s = [row[0] for row in gf_matmul(H1, [[t] for t in double], 2)]
    require(s == columns[2], "error doble con síndrome h_3")
    wrong = double[:]
    wrong[2] ^= 1
    require(tuple(wrong) in code and any(wrong), "corrección errónea a otra palabra")
    require(hamming(wrong, [0] * 6) == weight(wrong) == 3, "peso de la palabra errónea")


@check("S1.3", "TL con núcleo e imagen prescritos, matriz, composición", page=S1)
def _():
    X, Y, Z = sp.symbols("X Y Z")
    T = lambda v: sp.Matrix([v[0] - v[1], v[0] - v[1] + v[2], v[2]])
    Bv = [sp.Matrix([1, 1, 0]), sp.Matrix([1, 0, 0]), sp.Matrix([0, 0, 1])]
    Bp = [sp.Matrix([1, 1, 0]), sp.Matrix([0, 1, 1]), sp.Matrix([1, 0, 0])]
    same(sp.Matrix.hstack(*Bv).det(), -1, "det B")
    same(sp.Matrix.hstack(*Bp).det(), 1, "det B'")
    same(T(Bv[0]), sp.zeros(3, 1), "T(1,1,0)")
    same(T(Bv[1]), sp.Matrix([1, 1, 0]), "T(1,0,0)")
    same(T(Bv[2]), sp.Matrix([0, 1, 1]), "T(0,0,1)")
    A = sp.Matrix([[1, -1, 0], [1, -1, 1], [0, 0, 1]])
    same(A * sp.Matrix([X, Y, Z]), T([X, Y, Z]), "matriz canónica")
    require(A.rank() == 2, "dim Im = 2")
    same(A.nullspace()[0] / A.nullspace()[0][0], sp.Matrix([1, 1, 0]), "Nu(T)")
    for w in A.columnspace():
        same(w[0] - w[1] + w[2], 0, "Im en el plano")
    M = sp.Matrix.hstack(*Bp).inv() * A * sp.Matrix.hstack(*Bv)
    same(M, sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]]), "M(T)_BB'")
    vB = sp.Matrix.hstack(*Bv).inv() * sp.Matrix([2, -1, 3])
    same(vB, sp.Matrix([-1, 3, 3]), "[v]_B")
    same(M * vB, sp.Matrix([3, 3, 0]), "[T(v)]_B'")
    same(sp.Matrix.hstack(*Bp) * (M * vB), sp.Matrix([3, 6, 3]), "T(2,-1,3)")
    same(A * A, sp.Matrix([[0, 0, -1], [0, 0, 0], [0, 0, 1]]), "T∘T")
    require(len((A * A).nullspace()) == 2, "dim Nu(T∘T) = 2")


@check("S1.4", "Bases abstractas, inversa, Z2 y rango", page=S1)
def _():
    C = sp.Matrix([[1, 0, 1], [1, 1, 0], [0, 1, 1]])
    same(C.det(), 2, "det C_B'B")
    Ci = sp.Rational(1, 2) * sp.Matrix([[1, 1, -1], [-1, 1, 1], [1, -1, 1]])
    same(C.inv(), Ci, "C_BB'")
    wBp = Ci * sp.Matrix([2, -1, 3])
    same(wBp, sp.Matrix([-1, 0, 3]), "[w]_B'")
    same(C * wBp, sp.Matrix([2, -1, 3]), "reconstrucción")
    require(gf_rank(C, 2) == 2, "LD en Z2")
    for A in (sp.Matrix([[1, 0, 0, 2, 1], [0, 1, 0, 1, 1], [0, 0, 1, 3, 0]]),):
        require(A.rank() == 3 and len(A.nullspace()) == 2, "rango–nulidad 3 + 2 = 5")


@check("S2.1", "Simetría respecto de y = 2x", page=S2)
def _():
    Cbe = sp.Matrix([[1, -2], [2, 1]])
    D = sp.diag(1, -1)
    same(Cbe.inv(), sp.Rational(1, 5) * sp.Matrix([[1, 2], [-2, 1]]), "C_EB")
    M = Cbe * D * Cbe.inv()
    same(M, sp.Rational(1, 5) * sp.Matrix([[-3, 4], [4, 3]]), "M(T)_E")
    same(M * sp.Matrix([1, 2]), sp.Matrix([1, 2]), "fija la recta")
    same(M * sp.Matrix([-2, 1]), sp.Matrix([2, -1]), "invierte la normal")
    same(M * M, sp.eye(2), "involución")
    require(set(M.eigenvals()) == {1, -1}, "autovalores ±1")


@check("S2.2", "Diagonalización con parámetro", page=S2)
def _():
    a, lam = sp.symbols("a lambda")
    A = sp.Matrix([[3, 1, 1], [0, 2, a], [0, 0, 2]])
    same(sp.factor((lam * sp.eye(3) - A).det()), (lam - 3) * (lam - 2) ** 2, "polinomio característico")
    require((A - 2 * sp.eye(3)).subs(a, 0).rank() == 1, "m_g(2) = 2 si a = 0")
    for value in (1, -3, sp.Rational(1, 2)):
        require((A - 2 * sp.eye(3)).subs(a, value).rank() == 2, "m_g(2) = 1 si a ≠ 0")
    A0 = A.subs(a, 0)
    C = sp.Matrix([[1, 1, 1], [0, -1, 0], [0, 0, -1]])
    same(C.det(), 1, "det C")
    same(A0 * C, C * sp.diag(3, 2, 2), "A0 C = C D")
    same(C * sp.diag(3, 2, 2) * C.inv(), A0, "A0 = C D C^-1")
    same((A - 3 * sp.eye(3)) * (A - 2 * sp.eye(3)), sp.Matrix([[0, 0, a], [0, 0, -a], [0, 0, 0]]), "producto")
    same((A0**2 - 5 * A0 + 6 * sp.eye(3)), sp.zeros(3), "se anula para a = 0")


@check("S2.3", "Recurrencia a_{n+2} = a_{n+1} + 6 a_n", page=S2)
def _():
    n, lam = sp.symbols("n lambda")
    M = sp.Matrix([[1, 6], [1, 0]])
    same(sp.factor(M.charpoly(lam).as_expr()), (lam - 3) * (lam + 2), "polinomio característico")
    C = sp.Matrix([[3, -2], [1, 1]])
    same(C.inv() * M * C, sp.diag(3, -2), "diagonalización")
    seq = [1, 8]
    for _ in range(20):
        seq.append(seq[-1] + 6 * seq[-2])
    formula = 2 * 3**n - (-2) ** n
    require(all(formula.subs(n, k) == seq[k] for k in range(len(seq))), "término general")
    require(seq[2] == 14 and seq[3] == 62, "a2 y a3")
    # Dividiendo por 3^n: a_{n+1}/a_n = (6 + 2 r^n)/(2 - r^n) con r = -2/3, y |r| < 1, así que tiende a 6/2.
    r = sp.Rational(-2, 3)
    for k in range(len(seq) - 1):
        same(sp.Rational(seq[k + 1], seq[k]), (6 + 2 * r**k) / (2 - r**k), f"cociente para n={k}")
    t = sp.symbols("t")
    same(sp.limit((6 + 2 * t) / (2 - t), t, 0), 3, "límite cuando r^n → 0")
    require(abs(r) < 1, "|r| < 1")


@check("S2.4", "Producto interno no usual, Gram-Schmidt, complemento y proyección", page=S2)
def _():
    G = sp.Matrix([[1, 0, 1], [0, 2, 0], [1, 0, 2]])
    ip = lambda u, v: (sp.Matrix(u).T * G * sp.Matrix(v))[0]
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    same(ip([x1, x2, x3], [x1, x2, x3]), (x1 + x3) ** 2 + 2 * x2**2 + x3**2, "completar cuadrados")
    require(G.is_symmetric() and all(v > 0 for v in G.eigenvals()), "definida positiva")
    u1, u2 = [1, 0, 0], [0, 1, 1]
    w2 = sp.Matrix(u2) - ip(u2, u1) / ip(u1, u1) * sp.Matrix(u1)
    same(w2, sp.Matrix([-1, 1, 1]), "Gram-Schmidt")
    same(ip(w2, u1), 0, "ortogonalidad")
    same(ip(w2, w2), 3, "norma de w2")
    normal = sp.Matrix([2, 1, -2])
    same(ip(normal, u1), 0, "S⊥ ⟂ u1")
    same(ip(normal, u2), 0, "S⊥ ⟂ u2")
    system = sp.Matrix([[ip([1, 0, 0], e) for e in sp.eye(3).columnspace()],
                        [ip([0, 1, 1], e) for e in sp.eye(3).columnspace()]])
    require(len(system.nullspace()) == 1, "dim S⊥ = 1")
    v = sp.Matrix([0, 0, 1])
    p = ip(v, u1) / ip(u1, u1) * sp.Matrix(u1) + ip(v, w2) / ip(w2, w2) * w2
    same(p, sp.Matrix([sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(1, 3)]), "proyección")
    r = v - p
    same(r, -sp.Rational(1, 3) * normal, "residuo en S⊥")
    same(sp.sqrt(ip(r, r)), sp.sqrt(6) / 3, "distancia")
    same(ip(v, v), ip(p, p) + ip(r, r), "Pitágoras")


@check("S2.5", "Código (6,3): dual, distancia mínima, intersección y síndrome", page=S2)
def _():
    G = [[1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0]]
    H = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 0, 1]]
    require(gf_matmul(G, sp.Matrix(H).T, 2) == [[0] * 3] * 3, "G H^t = 0")
    require(gf_rank(H, 2) == 3, "rango de H")
    code, dual = gf_span(G, 2), gf_span(H, 2)
    brute = {v for v in itertools.product((0, 1), repeat=6)
             if all(sum(a * b for a, b in zip(v, c)) % 2 == 0 for c in code)}
    require(dual == brute, "C⊥ = gen(filas de H)")
    require(min_distance(code) == 3, "d(C) = 3")
    require((1,) * 6 not in code and code != dual, "no autodual")
    expected = {(0,) * 6, (1, 1, 0, 1, 1, 0), (1, 0, 1, 1, 0, 1), (0, 1, 1, 0, 1, 1)}
    require(code & dual == expected, "C ∩ C⊥")
    v = [1, 0, 1, 1, 0, 0]
    s = [row[0] for row in gf_matmul(H, [[t] for t in v], 2)]
    require(s == [0, 0, 1] and [[row[j] for row in H] for j in range(6)].index(s) == 5, "síndrome = h_6")
    v[5] ^= 1
    require(tuple(v) in code, "palabra corregida")
