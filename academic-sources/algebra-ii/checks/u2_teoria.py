"""Comprobaciones de los ejemplos resueltos de la teoría de la Unidad 2 (transformaciones lineales).

Cada función recalcula el ejemplo desde sus datos y verifica los pasos intermedios publicados
(escalonamientos, bases, coordenadas, matrices asociadas, inversas y productos).
Convenciones: base canónica de P_n[R] ordenada {1, x, ..., x^n}; base canónica de R^{2x2}
ordenada {E11, E12, E21, E22}; [v]_B como columna; M(T)_{BB'} con columnas [T(b_j)]_{B'};
C_{BB'}[v]_B = [v]_{B'}.
"""
import sympy as sp
from content_pipeline.mathcheck import check, gf_matmul, gf_nullspace, gf_rank, gf_span, require, same

T = "/algebra-ii/unidad-2/teoria/"
P1 = T + "definicion-y-ejemplos/"
P2 = T + "nucleo-e-imagen/"
P3 = T + "teorema-de-la-dimension/"
P4 = T + "clasificacion/"
P5 = T + "teorema-fundamental/"
P6 = T + "matriz-asociada/"
P7 = T + "cambio-de-base/"
P8 = T + "composicion-e-inversa/"

x = sp.symbols("x")


def ev(p, a):
    """Evalúa el polinomio p (en x) en a."""
    return sp.expand(p).subs(x, a)


def der(p):
    return sp.expand(sp.diff(p, x))


def cp(p, n=2):
    """Coordenadas de p en la base canónica {1, x, ..., x^n} de P_n[R]."""
    q = sp.expand(p)
    return sp.Matrix([q.coeff(x, k) for k in range(n + 1)])


def poly(c):
    """Polinomio cuyas coordenadas en {1, x, ..., x^n} son c."""
    return sp.expand(sum(c[k] * x ** k for k in range(len(c))))


def vec(A):
    """Coordenadas de una matriz 2x2 en la base canónica {E11, E12, E21, E22}."""
    return sp.Matrix([A[0, 0], A[0, 1], A[1, 0], A[1, 1]])


def col(*entries):
    return sp.Matrix(list(entries))


def cols(*vectors):
    """Matriz cuyas columnas son los vectores dados (tuplas o columnas)."""
    return sp.Matrix.hstack(*[v if isinstance(v, sp.MatrixBase) else sp.Matrix(list(v)) for v in vectors])


def in_kernel_basis(A, basis, what):
    """Los vectores están en nul(A), son LI y su cantidad es n - rango(A)."""
    for v in basis:
        same(A * v, sp.zeros(A.shape[0], 1), f"{what}: {list(v)} en el núcleo")
    require(cols(*basis).rank() == len(basis), f"{what}: base LI")
    require(len(basis) == A.shape[1] - A.rank(), f"{what}: dimensión del núcleo")


def same_span(gens, basis, what):
    """gen(gens) = gen(basis) y basis es LI."""
    G, Bm = cols(*gens), cols(*basis)
    require(Bm.rank() == len(basis), f"{what}: base LI")
    require(G.rank() == Bm.rank() == sp.Matrix.hstack(G, Bm).rank(), f"{what}: mismo subespacio generado")


# ---------------------------------------------------------------------------
# 2.1 Definición y ejemplos
# ---------------------------------------------------------------------------
@check("U2.T01.E1", "Linealidad de T(x,y,z)=(x-2y+z, 3y-z) y su forma matricial", page=P1)
def _():
    x1, y1, z1, x2, y2, z2, lam = sp.symbols("x1 y1 z1 x2 y2 z2 lam")

    def Tf(v):
        a, b, c = v
        return sp.Matrix([a - 2 * b + c, 3 * b - c])

    u, v = (x1, y1, z1), (x2, y2, z2)
    same(Tf(tuple(p + q for p, q in zip(u, v))), Tf(u) + Tf(v), "aditividad")
    same(Tf(tuple(lam * p for p in u)), lam * Tf(u), "homogeneidad")
    A = sp.Matrix([[1, -2, 1], [0, 3, -1]])
    same(A * sp.Matrix(list(u)), Tf(u), "T(v) = Av")
    same(Tf((2, 1, -1)), col(-1, 4), "T(2,1,-1)")


@check("U2.T01.E2", "F(x,y)=(x+y, xy) fija el origen y no es lineal", page=P1)
def _():
    def F(a, b):
        return sp.Matrix([a + b, a * b])

    same(F(0, 0), sp.zeros(2, 1), "F(0,0)")
    same(F(1, 1), col(2, 1), "F(1,1)")
    same(F(2, 2), col(4, 4), "F(2,2)")
    require(F(2, 2) != 2 * F(1, 1), "falla la homogeneidad")
    same(F(1, 0) + F(0, 1), col(2, 0), "F(1,0)+F(0,1)")
    require(F(1, 1) != F(1, 0) + F(0, 1), "falla la aditividad")


@check("U2.T01.E3", "Rotación con cos=4/5, sen=3/5: imagen del cuadrado unidad", page=P1)
def _():
    c, s = sp.Rational(4, 5), sp.Rational(3, 5)
    R = sp.Matrix([[c, -s], [s, c]])
    same(R * col(1, 0), col(sp.Rational(4, 5), sp.Rational(3, 5)), "R(e1)")
    same(R * col(0, 1), col(sp.Rational(-3, 5), sp.Rational(4, 5)), "R(e2)")
    same(R * col(1, 1), col(sp.Rational(1, 5), sp.Rational(7, 5)), "R(e1+e2)")
    same(c ** 2 + s ** 2, 1, "cos^2+sen^2")
    same(R.det(), 1, "el área se conserva")
    # Coordenadas de la figura (escala 100 px por unidad).
    same(100 * R * col(1, 1), col(20, 140), "vértice dibujado")


@check("U2.T01.E4", "T(p)=(p(1), p'(0)) en P_2[R] es lineal; T(2-x+3x^2)=(4,-1)", page=P1)
def _():
    a0, a1, a2, b0, b1, b2, lam = sp.symbols("a0 a1 a2 b0 b1 b2 lam")

    def Tf(p):
        return sp.Matrix([ev(p, 1), ev(der(p), 0)])

    p = a0 + a1 * x + a2 * x ** 2
    q = b0 + b1 * x + b2 * x ** 2
    same(Tf(p + q), Tf(p) + Tf(q), "aditividad")
    same(Tf(lam * p), lam * Tf(p), "homogeneidad")
    same(Tf(p), col(a0 + a1 + a2, a1), "fórmula general")
    same(Tf(2 - x + 3 * x ** 2), col(4, -1), "T(2-x+3x^2)")


@check("U2.T01.E5", "Codificación a -> aG en Z2 con G de 2x5", page=P1)
def _():
    G = [[1, 0, 1, 1, 0], [0, 1, 0, 1, 1]]
    words = {
        (0, 0): (0, 0, 0, 0, 0),
        (1, 0): (1, 0, 1, 1, 0),
        (0, 1): (0, 1, 0, 1, 1),
        (1, 1): (1, 1, 1, 0, 1),
    }
    for a, w in words.items():
        require(tuple(gf_matmul([list(a)], G)[0]) == w, f"codificación de {a}")
    for a in words:
        for b in words:
            s = tuple((p + q) % 2 for p, q in zip(a, b))
            ws = tuple((p + q) % 2 for p, q in zip(words[a], words[b]))
            require(words[s] == ws, f"aditividad en {a}, {b}")


@check("U2.T01.E6", "Contraejemplos: traslación, norma, determinante y x^2", page=P1)
def _():
    same(col(0 + 1, 0 - 2), col(1, -2), "la traslación no fija el origen")
    same(sp.sqrt(3 ** 2 + 4 ** 2), 5, "norma de (3,4)")
    same(sp.sqrt((-3) ** 2 + (-4) ** 2), 5, "norma de (-3,-4)")
    require(sp.sqrt((-3) ** 2 + (-4) ** 2) != -5, "N(-v) != -N(v)")
    I2 = sp.eye(2)
    same((I2 + I2).det(), 4, "det(I+I)")
    same(I2.det() + I2.det(), 2, "det(I)+det(I)")
    same((1 + 1) ** 2, 4, "(1+1)^2")
    same(1 ** 2 + 1 ** 2, 2, "1^2+1^2")


@check("U2.T01.E7", "Cizalla de la grilla y traslación en coordenadas homogéneas", page=P1)
def _():
    S = sp.Matrix([[1, 1], [0, 1]])
    for i in range(3):
        for j in range(3):
            same(S * col(i, j), col(i + j, j), f"cizalla de ({i},{j})")
    Hm = sp.Matrix([[1, 0, 2], [0, 1, -1], [0, 0, 1]])
    same(Hm * col(3, 1, 1), col(5, 0, 1), "traslación homogénea")
    Rh = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    same(Rh * col(3, 1, 1), col(-1, 3, 1), "rotación de 90° homogénea")
    same(Hm * Rh * col(3, 1, 1), col(1, 2, 1), "rotar y después trasladar")
    same(Hm * Rh, sp.Matrix([[0, -1, 2], [1, 0, -1], [0, 0, 1]]), "matriz de la composición")


# ---------------------------------------------------------------------------
# 2.2 Núcleo e imagen
# ---------------------------------------------------------------------------
A22 = sp.Matrix([[1, 1, 0, -1], [1, 2, 1, 0], [2, 3, 1, -1]])


@check("U2.T02.E1", "Núcleo e imagen de una TL de R^4 en R^3", page=P2)
def _():
    A = A22
    step1 = sp.Matrix([[1, 1, 0, -1], [0, 1, 1, 1], [0, 1, 1, 1]])
    same(sp.Matrix([list(A.row(0)), list(A.row(1) - A.row(0)), list(A.row(2) - 2 * A.row(0))]), step1, "F2-F1, F3-2F1")
    R, piv = A.rref()
    same(R, sp.Matrix([[1, 0, -1, -2], [0, 1, 1, 1], [0, 0, 0, 0]]), "forma escalonada reducida")
    require(piv == (0, 1), "pivotes")
    in_kernel_basis(A, [col(1, -1, 1, 0), col(2, -1, 0, 1)], "Nu(T)")
    imgs = [A.col(j) for j in range(4)]
    same_span(imgs, [col(1, 1, 2), col(0, 1, 1)], "Im(T)")
    for w in imgs:
        same(w[2], w[0] + w[1], "ecuación z = x + y")
    require(A.rank() == 2, "dim Im = 2")
    same(A.shape[1], A.rank() + len(A.nullspace()), "teorema de la dimensión: 4 = 2 + 2")


@check("U2.T02.E2", "T(p)=[[p(0),p(1)],[p(1),p(2)]]: núcleo nulo e imagen = simétricas", page=P2)
def _():
    def Tf(p):
        return sp.Matrix([[ev(p, 0), ev(p, 1)], [ev(p, 1), ev(p, 2)]])

    imgs = [Tf(1), Tf(x), Tf(x ** 2)]
    same(imgs[0], sp.Matrix([[1, 1], [1, 1]]), "T(1)")
    same(imgs[1], sp.Matrix([[0, 1], [1, 2]]), "T(x)")
    same(imgs[2], sp.Matrix([[0, 1], [1, 4]]), "T(x^2)")
    for M in imgs:
        same(M, M.T, "imagen simétrica")
    rows = sp.Matrix([list(vec(M)) for M in imgs])
    same(rows.row(2) - rows.row(1), sp.Matrix([[0, 0, 0, 2]]), "F3-F2")
    require(rows.rank() == 3, "imágenes LI")
    M = cols(*[vec(Mi) for Mi in imgs])
    require(M.nullspace() == [], "Nu(T) = {0}")
    sym_basis = [vec(sp.Matrix([[1, 0], [0, 0]])), vec(sp.Matrix([[0, 1], [1, 0]])), vec(sp.Matrix([[0, 0], [0, 1]]))]
    same_span([vec(Mi) for Mi in imgs], sym_basis, "Im(T) = matrices simétricas")


@check("U2.T02.E3", "T: R^{2x2} -> P_2[R] con núcleo y imagen de dimensión 2", page=P2)
def _():
    def Tf(A):
        a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
        return sp.expand((a + d) + (b - c) * x + (a + b - c + d) * x ** 2)

    E = [sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]]), sp.Matrix([[0, 0], [0, 1]])]
    imgs = [Tf(Ei) for Ei in E]
    same(imgs[0], 1 + x ** 2, "T(E11)")
    same(imgs[1], x + x ** 2, "T(E12)")
    same(imgs[2], -x - x ** 2, "T(E21)")
    same(imgs[3], 1 + x ** 2, "T(E22)")
    M = cols(*[cp(p) for p in imgs])
    same(M, sp.Matrix([[1, 0, 0, 1], [0, 1, -1, 0], [1, 1, -1, 1]]), "matriz de coeficientes")
    in_kernel_basis(M, [vec(sp.Matrix([[1, 0], [0, -1]])), vec(sp.Matrix([[0, 1], [1, 0]]))], "Nu(T)")
    same(Tf(sp.Matrix([[1, 0], [0, -1]])), 0, "T(N1)")
    same(Tf(sp.Matrix([[0, 1], [1, 0]])), 0, "T(N2)")
    same_span([cp(p) for p in imgs], [cp(1 + x ** 2), cp(x + x ** 2)], "Im(T)")


@check("U2.T02.E4", "Preimágenes por la TL de U2.T02.E1", page=P2)
def _():
    A = A22
    aug = sp.Matrix.hstack(A, col(2, 3, 5))
    R, _ = aug.rref()
    same(R, sp.Matrix([[1, 0, -1, -2, 1], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0]]), "ampliada reducida")
    same(A * col(1, 1, 0, 0), col(2, 3, 5), "solución particular")
    for s, t in [(1, 0), (0, 1), (2, -3)]:
        v = col(1, 1, 0, 0) + s * col(1, -1, 1, 0) + t * col(2, -1, 0, 1)
        same(A * v, col(2, 3, 5), "v_p + Nu(T)")
    aug2 = sp.Matrix.hstack(A, col(1, 0, 0))
    require(aug2.rank() == 3 and A.rank() == 2, "(1,0,0) no está en la imagen")
    same(0 - (1 + 0), -1, "condición z - x - y")


@check("U2.T02.E5", "Proyección P(x,y)=(2x-2y, x-y): núcleo, imagen y figura", page=P2)
def _():
    P = sp.Matrix([[2, -2], [1, -1]])
    same(P * P, P, "P^2 = P")
    in_kernel_basis(P, [col(1, 1)], "Nu(P)")
    same_span([P.col(0), P.col(1)], [col(2, 1)], "Im(P)")
    same(P * col(3, 1), col(4, 2), "P(3,1)")
    same(col(3, 1) - P * col(3, 1), col(-1, -1), "v - P(v)")
    same(P * col(2, 0), col(4, 2), "P(2,0)")
    same(P * col(4, 2), col(4, 2), "P(4,2)")
    # descomposición v = (x-y)(2,1) + (-x+2y)(1,1)
    xx, yy = sp.symbols("xx yy")
    same((xx - yy) * col(2, 1) + (-xx + 2 * yy) * col(1, 1), col(xx, yy), "descomposición")


# ---------------------------------------------------------------------------
# 2.3 Teorema de la dimensión
# ---------------------------------------------------------------------------
@check("U2.T03.E1", "T: P_3 -> R^3, T(p)=(p(1), p(-1), p'(0)): epimorfismo con núcleo gen{x^2-1}", page=P3)
def _():
    def Tf(p):
        return col(ev(p, 1), ev(p, -1), ev(der(p), 0))

    M = cols(*[Tf(x ** k) for k in range(4)])
    same(M, sp.Matrix([[1, 1, 1, 1], [1, -1, 1, -1], [0, 1, 0, 0]]), "matriz de coeficientes")
    step = sp.Matrix([list(M.row(0)), list(M.row(1) - M.row(0)), list(M.row(2))])
    same(step, sp.Matrix([[1, 1, 1, 1], [0, -2, 0, -2], [0, 1, 0, 0]]), "F2-F1")
    step2 = sp.Matrix([list(step.row(0)), list(step.row(1)), list(step.row(2) + sp.Rational(1, 2) * step.row(1))])
    same(step2, sp.Matrix([[1, 1, 1, 1], [0, -2, 0, -2], [0, 0, 0, -1]]), "F3+(1/2)F2")
    require(M.rank() == 3, "rango 3")
    in_kernel_basis(M, [cp(x ** 2 - 1, 3)], "Nu(T)")
    same(Tf(x ** 2 - 1), col(0, 0, 0), "T(x^2-1)")
    same(4 - 1, 3, "dim Im = 4 - 1")


@check("U2.T03.E2", "T(A)=A-A^t en R^{2x2}: núcleo simétricas, imagen antisimétricas", page=P3)
def _():
    E = [sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]]), sp.Matrix([[0, 0], [0, 1]])]
    M = cols(*[vec(Ei - Ei.T) for Ei in E])
    require(M.rank() == 1, "dim Im = 1")
    sym = [vec(sp.Matrix([[1, 0], [0, 0]])), vec(sp.Matrix([[0, 1], [1, 0]])), vec(sp.Matrix([[0, 0], [0, 1]]))]
    in_kernel_basis(M, sym, "Nu(T) = simétricas")
    same_span([M.col(j) for j in range(4)], [vec(sp.Matrix([[0, 1], [-1, 0]]))], "Im(T)")
    a, b, c, d = sp.symbols("a b c d")
    A = sp.Matrix([[a, b], [c, d]])
    same(A - A.T, (b - c) * sp.Matrix([[0, 1], [-1, 0]]), "A - A^t = (b-c)J")


@check("U2.T03.E3", "No existe T: R^3 -> R^4 con T(1,2,0)=2T(0,1,1) e Im de dimensión >= 3", page=P3)
def _():
    v = col(1, 2, 0) - 2 * col(0, 1, 1)
    same(v, col(1, 0, -2), "vector del núcleo")
    require(v != sp.zeros(3, 1), "no nulo")
    require(cols((1, 0, 1, 0), (0, 1, 0, 1), (1, 1, 0, 0)).rank() == 3, "tres matrices LI")
    require(1 + 3 > 3, "contradicción con el teorema de la dimensión")


@check("U2.T03.E4", "Matriz de control del código de Hamming (7,4): rango 3, núcleo de dimensión 4", page=P3)
def _():
    H = [[(j >> (2 - i)) & 1 for j in range(1, 8)] for i in range(3)]
    require(H == [[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]], "columnas = 1..7 en binario")
    require(gf_rank(H, 2) == 3, "rango 3 (epimorfismo sobre Z2^3)")
    basis = gf_nullspace(H, 2)
    require(len(basis) == 7 - 3, "dim Nu = 4")
    words = gf_span(basis, 2)
    require(len(words) == 2 ** 4, "16 palabras código")
    for w in words:
        require(gf_matmul(H, [[b] for b in w]) == [[0], [0], [0]], "H w^t = 0")


# ---------------------------------------------------------------------------
# 2.4 Clasificación
# ---------------------------------------------------------------------------
@check("U2.T04.E1", "T(x,y,z)=(x+y, y+z, x+2y+z): ni mono ni epi", page=P4)
def _():
    A = sp.Matrix([[1, 1, 0], [0, 1, 1], [1, 2, 1]])
    same(A.row(2), A.row(0) + A.row(1), "F3 = F1 + F2")
    R, piv = A.rref()
    same(R, sp.Matrix([[1, 0, -1], [0, 1, 1], [0, 0, 0]]), "escalonada reducida")
    in_kernel_basis(A, [col(1, -1, 1)], "Nu(T)")
    same_span([A.col(j) for j in range(3)], [col(1, 0, 1), col(0, 1, 1)], "Im(T)")
    for j in range(3):
        same(A[2, j], A[0, j] + A[1, j], "Im: z = x + y")
    require(A.rank() == 2, "rango 2")


@check("U2.T04.E2", "T_k(A)=A+kA^t es automorfismo de R^{2x2} si y solo si k != 1, -1", page=P4)
def _():
    k = sp.symbols("k")
    Mk = sp.Matrix([[1 + k, 0, 0, 0], [0, 1, k, 0], [0, k, 1, 0], [0, 0, 0, 1 + k]])
    E = [sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]]), sp.Matrix([[0, 0], [0, 1]])]
    same(cols(*[vec(Ei + k * Ei.T) for Ei in E]), Mk, "matriz de T_k")
    same(sp.expand(Mk.det() - (1 + k) ** 3 * (1 - k)), 0, "det = (1+k)^3 (1-k)")
    M1 = sp.Matrix([[2, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 2]])
    in_kernel_basis(M1, [vec(sp.Matrix([[0, 1], [-1, 0]]))], "k=1: Nu = antisimétricas")
    Mm1 = sp.Matrix([[0, 0, 0, 0], [0, 1, -1, 0], [0, -1, 1, 0], [0, 0, 0, 0]])
    in_kernel_basis(Mm1, [vec(sp.Matrix([[1, 0], [0, 0]])), vec(sp.Matrix([[0, 1], [1, 0]])),
                          vec(sp.Matrix([[0, 0], [0, 1]]))], "k=-1: Nu = simétricas")
    M2 = sp.Matrix([[3, 0, 0, 0], [0, 1, 2, 0], [0, 2, 1, 0], [0, 0, 0, 3]])
    same(M2.det(), -27, "k=2: determinante")


@check("U2.T04.E3", "La codificación con G de rango 2 es monomorfismo de Z2^2 en Z2^5", page=P4)
def _():
    G = [[1, 0, 1, 1, 0], [0, 1, 0, 1, 1]]
    require(gf_rank(G, 2) == 2, "rango de G en Z2")
    msgs = [(0, 0), (1, 0), (0, 1), (1, 1)]
    words = {tuple(gf_matmul([list(a)], G)[0]) for a in msgs}
    require(len(words) == 4, "mensajes distintos dan palabras distintas")
    require((0, 0, 0, 0, 0) in words, "contiene la palabra nula")


@check("U2.T04.E4", "Coordenadas en P_2[R] como isomorfismo con R^3", page=P4)
def _():
    B = [sp.Integer(1), 1 + x, 1 + x + x ** 2]
    CBE = cols(*[cp(b) for b in B])
    same(CBE, sp.Matrix([[1, 1, 1], [0, 1, 1], [0, 0, 1]]), "C_BE")
    c = CBE.inv() * cp(3 + 2 * x - x ** 2)
    same(c, col(1, 3, -1), "[3+2x-x^2]_B")
    same(poly(list(cp(sum(ci * b for ci, b in zip(c, B))))), sp.expand(3 + 2 * x - x ** 2), "reconstrucción")
    V = cols(cp(1 + x), cp(x - x ** 2), cp(1 + 3 * x - 2 * x ** 2))
    require(V.rank() == 2, "rango 2: LD")
    same(cp(1 + x) + 2 * cp(x - x ** 2), cp(1 + 3 * x - 2 * x ** 2), "relación de dependencia")


# ---------------------------------------------------------------------------
# 2.5 Teorema fundamental
# ---------------------------------------------------------------------------
@check("U2.T05.E1", "TL de R^2 en R^3 fijada sobre B={(1,2),(1,3)}: dos métodos", page=P5)
def _():
    xx, yy = sp.symbols("xx yy")
    C = sp.Matrix([[1, 1], [2, 3]])
    alpha, beta = 3 * xx - yy, yy - 2 * xx
    same(alpha * col(1, 2) + beta * col(1, 3), col(xx, yy), "coordenadas en B")
    w1, w2 = col(3, 1, 0), col(4, 1, -1)
    Tv = alpha * w1 + beta * w2
    same(Tv, col(xx + yy, xx, 2 * xx - yy), "fórmula por coordenadas")
    same(C.inv(), sp.Matrix([[3, -1], [-2, 1]]), "inversa de la matriz de la base")
    W = cols(w1, w2)
    A = W * C.inv()
    same(A, sp.Matrix([[1, 1], [1, 0], [2, -1]]), "fórmula por matriz")
    same(A * col(1, 2), w1, "T(1,2)")
    same(A * col(1, 3), w2, "T(1,3)")


@check("U2.T05.E2", "Datos LD compatibles: existen infinitas TL", page=P5)
def _():
    v1, v2, v3 = col(1, 0, 1), col(0, 1, 1), col(1, 1, 2)
    w1, w2, w3 = col(1, 2), col(2, -1), col(3, 1)
    same(v1 + v2, v3, "relación v3 = v1 + v2")
    same(w1 + w2, w3, "las imágenes respetan la relación")
    e3 = col(0, 0, 1)
    require(cols(v1, v2, e3).rank() == 3, "{v1, v2, e3} es base")
    xx, yy, zz = sp.symbols("xx yy zz")
    same(xx * v1 + yy * v2 + (zz - xx - yy) * e3, col(xx, yy, zz), "coordenadas en la base completada")
    T0 = sp.Matrix([[1, 2, 0], [2, -1, 0]])
    T1 = sp.Matrix([[0, 1, 1], [1, -2, 1]])
    for Tm, w in [(T0, col(0, 0)), (T1, col(1, 1))]:
        same(Tm * col(xx, yy, zz), xx * w1 + yy * w2 + (zz - xx - yy) * w, "fórmula de la familia")
        same(Tm * v1, w1, "T(v1)")
        same(Tm * v2, w2, "T(v2)")
        same(Tm * v3, w3, "T(v3)")
        same(Tm * e3, w, "T(e3)")
    require(T0 != T1, "no hay unicidad")


@check("U2.T05.E3", "Datos LD incompatibles: no existe la TL", page=P5)
def _():
    w1, w2, w3 = col(1, 2), col(2, -1), col(3, 0)
    same(w1 + w2, col(3, 1), "T(v1)+T(v2)")
    require(w1 + w2 != w3, "la relación no se respeta")


@check("U2.T05.E4", "TL de R^3 en P_2[R] con núcleo e imagen prescritos", page=P5)
def _():
    a, b, c = sp.symbols("a b c")
    base = [col(1, -1, 0), col(0, 1, 0), col(0, 0, 1)]
    require(cols(*base).rank() == 3, "base de R^3")
    same(a * base[0] + (a + b) * base[1] + c * base[2], col(a, b, c), "coordenadas")
    Tp = sp.expand((a + b) * (1 + x) + c * (x - x ** 2))
    same(Tp, sp.expand((a + b) + (a + b + c) * x - c * x ** 2), "fórmula")
    M = sp.Matrix([[1, 1, 0], [1, 1, 1], [0, 0, -1]])
    same(M * col(a, b, c), cp(Tp), "matriz canónica")
    in_kernel_basis(M, [col(1, -1, 0)], "Nu(T)")
    same_span([M.col(j) for j in range(3)], [cp(1 + x), cp(x - x ** 2)], "Im(T)")


@check("U2.T05.E5", "Endomorfismo de R^4 con Nu(T) = Im(T)", page=P5)
def _():
    A = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    in_kernel_basis(A, [col(1, 0, 0, 0), col(0, 1, 0, 0)], "Nu(T) = gen{e1, e2}")
    same_span([A.col(j) for j in range(4)], [col(1, 0, 0, 0), col(0, 1, 0, 0)], "Im(T) = gen{e1, e2}")
    same(A * A, sp.zeros(4, 4), "T∘T = 0")
    same(A * col(5, -1, 2, 3), col(2, 3, 0, 0), "T(5,-1,2,3)")


# ---------------------------------------------------------------------------
# 2.6 Matriz asociada
# ---------------------------------------------------------------------------
A26 = sp.Matrix([[1, 2, -1], [0, 1, 1]])
B26 = [col(1, 0, 1), col(0, 1, 1), col(1, 1, 0)]
Bp26 = [col(1, 1), col(1, 2)]
M26 = sp.Matrix([[-1, 0, 5], [1, 1, -2]])


@check("U2.T06.E1", "Matriz en bases canónicas de T(x,y,z)=(x+2y-z, y+z)", page=P6)
def _():
    same(cols(A26 * col(1, 0, 0), A26 * col(0, 1, 0), A26 * col(0, 0, 1)), A26, "columnas T(e_j)")
    same(A26 * col(2, 1, 3), col(1, 4), "T(2,1,3)")


@check("U2.T06.E2", "M(T)_{BB'} con bases no canónicas y matriz ampliada múltiple", page=P6)
def _():
    imgs = [A26 * b for b in B26]
    same(cols(*imgs), sp.Matrix([[0, 1, 3], [1, 2, 1]]), "transformados de B")
    Cp = cols(*Bp26)
    aug = sp.Matrix.hstack(Cp, cols(*imgs))
    step = sp.Matrix([list(aug.row(0)), list(aug.row(1) - aug.row(0))])
    same(step, sp.Matrix([[1, 1, 0, 1, 3], [0, 1, 1, 1, -2]]), "F2-F1")
    R, _ = aug.rref()
    same(R, sp.Matrix([[1, 0, -1, 0, 5], [0, 1, 1, 1, -2]]), "ampliada reducida")
    same(cols(R.col(2), R.col(3), R.col(4)), M26, "M(T)_{BB'}")
    for j in range(3):
        same(Cp * M26.col(j), imgs[j], f"corroboración columna {j + 1}")
    vB = cols(*B26).inv() * col(2, 1, 3)
    same(vB, col(2, 1, 0), "[v]_B")
    same(M26 * vB, col(-2, 3), "[T(v)]_{B'}")
    same(Cp * col(-2, 3), col(1, 4), "T(v) reconstruido")
    same(A26 * col(2, 1, 3), col(1, 4), "T(v) por la fórmula")


@check("U2.T06.E3", "Núcleo e imagen desde M(T)_{BB'}: coordenadas versus vectores", page=P6)
def _():
    in_kernel_basis(M26, [col(5, -3, 1)], "nul(M)")
    v = 5 * B26[0] - 3 * B26[1] + 1 * B26[2]
    same(v, col(6, -2, 2), "vector del núcleo")
    same(A26 * v, col(0, 0), "T(6,-2,2)")
    same(A26 * col(5, -3, 1), col(-2, -2), "la terna de coordenadas no está en el núcleo")
    require(M26.rank() == 2, "rango 2: epimorfismo")


@check("U2.T06.E4", "Endomorfismo T(p)=(x+1)p'-p de P_2[R] en bases B y B'", page=P6)
def _():
    a, b, c = sp.symbols("a b c")

    def Tf(p):
        return sp.expand((x + 1) * sp.diff(p, x) - p)

    same(Tf(a + b * x + c * x ** 2), sp.expand((b - a) + 2 * c * x + c * x ** 2), "fórmula")
    ME = cols(*[cp(Tf(x ** k)) for k in range(3)])
    same(ME, sp.Matrix([[-1, 1, 0], [0, 0, 2], [0, 0, 1]]), "M(T)_E")
    B = [1 + x, x, x ** 2]
    Bp = [sp.Integer(1), x, 1 + x ** 2]
    same(Tf(1 + x), 0, "T(1+x)")
    same(Tf(x), 1, "T(x)")
    same(Tf(x ** 2), sp.expand(2 * x + x ** 2), "T(x^2)")
    CBpE = cols(*[cp(q) for q in Bp])
    M = cols(*[CBpE.inv() * cp(Tf(q)) for q in B])
    same(M, sp.Matrix([[0, 1, -1], [0, 0, 2], [0, 0, 1]]), "M(T)_{BB'}")
    same(sp.expand(-1 + 2 * x + (1 + x ** 2)), sp.expand(2 * x + x ** 2), "corroboración columna 3")
    in_kernel_basis(M, [col(1, 0, 0)], "nul(M)")
    require(M.rank() == 2, "dim Im = 2")
    same(poly(list(CBpE * col(-1, 2, 1))), sp.expand(2 * x + x ** 2), "columna 3 como polinomio")


@check("U2.T06.E5", "De la matriz M(T)_{BB'} a la fórmula explícita", page=P6)
def _():
    xx, yy = sp.symbols("xx yy")
    M = sp.Matrix([[1, 2], [0, -1]])
    CB = cols((1, 1), (1, 2))
    CBp = cols((1, 0), (1, 1))
    vB = col(2 * xx - yy, yy - xx)
    same(CB * vB, col(xx, yy), "[v]_B")
    same(M * vB, col(yy, xx - yy), "[T(v)]_{B'}")
    same(CBp * (M * vB), col(xx, xx - yy), "T(x,y) = (x, x-y)")
    same(CBp * M, sp.Matrix([[1, 1], [0, -1]]), "T(b1), T(b2)")
    same(CBp * M * CB.inv(), sp.Matrix([[1, 0], [1, -1]]), "matriz canónica")


# ---------------------------------------------------------------------------
# 2.7 Cambio de base
# ---------------------------------------------------------------------------
@check("U2.T07.E1", "M(T)_{BB'} = C_{E'B'} M(T)_{EE'} C_{BE} (verificación por dos caminos)", page=P7)
def _():
    CBE = cols(*B26)
    CBpE = cols(*Bp26)
    CEBp = CBpE.inv()
    same(CEBp, sp.Matrix([[2, -1], [-1, 1]]), "C_{E'B'}")
    same(A26 * CBE, sp.Matrix([[0, 1, 3], [1, 2, 1]]), "M(T)_{EE'} C_{BE}")
    same(CEBp * A26 * CBE, M26, "producto de tres matrices")
    same(CBpE * M26 * CBE.inv(), A26, "vuelta a la canónica")


@check("U2.T07.E2", "Simetría respecto de la recta gen{(1,2)}", page=P7)
def _():
    CBE = cols((1, 2), (-2, 1))
    D = sp.diag(1, -1)
    same(CBE.det(), 5, "det C_BE")
    same(CBE.inv(), sp.Rational(1, 5) * sp.Matrix([[1, 2], [-2, 1]]), "C_EB")
    same(CBE * D, sp.Matrix([[1, 2], [2, -1]]), "C_BE D")
    S = CBE * D * CBE.inv()
    same(S, sp.Rational(1, 5) * sp.Matrix([[-3, 4], [4, 3]]), "M(S)_E")
    same(S * col(1, 2), col(1, 2), "S(b1) = b1")
    same(S * col(-2, 1), col(2, -1), "S(b2) = -b2")
    same(S * S, sp.eye(2), "S∘S = id")
    same(S * col(3, 1), col(-1, 3), "S(3,1)")
    same(S * col(5, 0), col(-3, 4), "S(5,0)")
    same(CBE.inv() * col(3, 1), col(1, -1), "[(3,1)]_B")


@check("U2.T07.E3", "Proyección ortogonal sobre el plano x+y-z=0 mediante base adaptada", page=P7)
def _():
    u1, u2, n = col(1, 0, 1), col(0, 1, 1), col(1, 1, -1)
    for v in (u1, u2):
        same(v[0] + v[1] - v[2], 0, "vector del plano")
        same((v.T * n)[0, 0], 0, "perpendicular a la normal")
    C = cols(u1, u2, n)
    same(C.det(), -3, "det C_BE")
    Ci = C.inv()
    same(Ci, sp.Rational(1, 3) * sp.Matrix([[2, -1, 1], [-1, 2, 1], [1, 1, -1]]), "C_EB")
    P = C * sp.diag(1, 1, 0) * Ci
    same(P, sp.Rational(1, 3) * sp.Matrix([[2, -1, 1], [-1, 2, 1], [1, 1, 2]]), "M(P)_E")
    same(P * n, sp.zeros(3, 1), "P(n) = 0")
    same(P * u1, u1, "P(u1) = u1")
    same(P * u2, u2, "P(u2) = u2")
    same(P * P, P, "P^2 = P")
    same(P * col(1, 2, 0), col(0, 1, 1), "P(1,2,0)")
    same(Ci * col(1, 2, 0), col(0, 1, 1), "[(1,2,0)]_B")
    same(col(1, 2, 0) - col(0, 1, 1), n, "v - P(v) = n")


@check("U2.T07.E4", "Endomorfismo de P_2[R]: M(T)_B = C_{EB} M(T)_E C_{BE}", page=P7)
def _():
    ME = sp.Matrix([[-1, 1, 0], [0, 0, 2], [0, 0, 1]])
    CBE = sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 0, 1]])
    CEB = CBE.inv()
    same(CEB, sp.Matrix([[1, 0, 0], [-1, 1, 0], [0, 0, 1]]), "C_EB")
    same(ME * CBE, sp.Matrix([[0, 1, 0], [0, 0, 2], [0, 0, 1]]), "M(T)_E C_BE")
    MB = CEB * ME * CBE
    same(MB, sp.Matrix([[0, 1, 0], [0, -1, 2], [0, 0, 1]]), "M(T)_B")

    def Tf(p):
        return sp.expand((x + 1) * sp.diff(p, x) - p)

    B = [1 + x, x, x ** 2]
    direct = cols(*[CEB * cp(Tf(q)) for q in B])
    same(direct, MB, "columnas [T(b_j)]_B")
    same(MB.det(), ME.det(), "mismo determinante")
    same(MB[0, 0] + MB[1, 1] + MB[2, 2], ME[0, 0] + ME[1, 1] + ME[2, 2], "misma traza")


# ---------------------------------------------------------------------------
# 2.8 Composición e inversa
# ---------------------------------------------------------------------------
@check("U2.T08.E1", "Composición de rotaciones con cos=4/5, sen=3/5", page=P8)
def _():
    c, s = sp.Rational(4, 5), sp.Rational(3, 5)
    R = sp.Matrix([[c, -s], [s, c]])
    R2 = sp.Rational(1, 25) * sp.Matrix([[7, -24], [24, 7]])
    same(R * R, R2, "R∘R")
    same(c ** 2 - s ** 2, sp.Rational(7, 25), "cos 2θ")
    same(2 * s * c, sp.Rational(24, 25), "sen 2θ")
    same(R.inv(), R.T, "R^{-1} = R^t")
    same(R.inv(), sp.Matrix([[c, s], [-s, c]]), "rotación de -θ")
    same(R2 * col(5, 0), col(sp.Rational(7, 5), sp.Rational(24, 5)), "imagen de (5,0)")


@check("U2.T08.E2", "S∘T no es isomorfismo y T∘S sí (T: R^3->R^2, S: R^2->R^3)", page=P8)
def _():
    MT = sp.Matrix([[1, 1, 0], [0, 1, -1]])
    MS = sp.Matrix([[1, 0], [1, 1], [0, 1]])
    ST = MS * MT
    same(ST, sp.Matrix([[1, 1, 0], [1, 2, -1], [0, 1, -1]]), "M(S∘T)")
    same(ST.det(), 0, "det M(S∘T)")
    require(ST.rank() == 2, "rango 2")
    in_kernel_basis(MT, [col(-1, 1, 1)], "Nu(T)")
    in_kernel_basis(ST, [col(-1, 1, 1)], "Nu(S∘T)")
    TS = MT * MS
    same(TS, sp.Matrix([[2, 1], [1, 0]]), "M(T∘S)")
    same(TS.det(), -1, "det M(T∘S)")
    same(TS.inv(), sp.Matrix([[0, 1], [1, -2]]), "M((T∘S)^{-1})")


@check("U2.T08.E3", "Inversa de T(p)=(p(0), p(1), p(-1)) y preimagen de (2,3,5)", page=P8)
def _():
    def Tf(p):
        return col(ev(p, 0), ev(p, 1), ev(p, -1))

    M = cols(Tf(1), Tf(x), Tf(x ** 2))
    same(M, sp.Matrix([[1, 0, 0], [1, 1, 1], [1, -1, 1]]), "M(T)_{EE'}")
    same(M.det(), 2, "det")
    Mi = sp.Matrix([[1, 0, 0], [0, sp.Rational(1, 2), sp.Rational(-1, 2)], [-1, sp.Rational(1, 2), sp.Rational(1, 2)]])
    same(M.inv(), Mi, "M(T^{-1})_{E'E}")
    aug = sp.Matrix.hstack(M, sp.eye(3))
    same(aug.rref()[0], sp.Matrix.hstack(sp.eye(3), Mi), "Gauss-Jordan [M | I]")
    p = poly(list(Mi * col(2, 3, 5)))
    same(p, sp.expand(2 - x + 2 * x ** 2), "T^{-1}(2,3,5)")
    same(Tf(p), col(2, 3, 5), "corroboración")
    y0, y1, y2 = sp.symbols("y0 y1 y2")
    q = poly(list(Mi * col(y0, y1, y2)))
    same(q, sp.expand(y0 + (y1 - y2) / 2 * x + (y1 + y2 - 2 * y0) / 2 * x ** 2), "fórmula de T^{-1}")
    same(Tf(q), col(y0, y1, y2), "T(T^{-1}(y)) = y")


@check("U2.T08.E4", "M(T^{-1})_{B'B} = (M(T)_{BB'})^{-1} para T: P_1[R] -> R^2", page=P8)
def _():
    u, v = sp.symbols("u v")

    def Tf(p):
        q = sp.expand(p)
        a0, a1 = q.coeff(x, 0), q.coeff(x, 1)
        return col(a0 + a1, a0 + 2 * a1)

    B = [sp.Integer(1), 1 + x]
    CBp = cols((1, 1), (0, 1))
    same(Tf(1), col(1, 1), "T(1)")
    same(Tf(1 + x), col(2, 3), "T(1+x)")
    M = cols(*[CBp.inv() * Tf(b) for b in B])
    same(M, sp.Matrix([[1, 2], [0, 1]]), "M(T)_{BB'}")
    Mi = M.inv()
    same(Mi, sp.Matrix([[1, -2], [0, 1]]), "M(T^{-1})_{B'B}")
    same(Tf(-1 + x), col(0, 1), "T(-1+x) = (0,1)")
    same(sp.expand(-2 * 1 + 1 * (1 + x)), sp.expand(-1 + x), "segunda columna como polinomio")
    wB = CBp.inv() * col(u, v)
    same(wB, col(u, v - u), "[(u,v)]_{B'}")
    cB = Mi * wB
    same(cB, col(3 * u - 2 * v, v - u), "[T^{-1}(u,v)]_B")
    p = sp.expand(cB[0] * 1 + cB[1] * (1 + x))
    same(p, sp.expand((2 * u - v) + (v - u) * x), "T^{-1}(u,v)")
    same(Tf(p), col(u, v), "T(T^{-1}(u,v))")
