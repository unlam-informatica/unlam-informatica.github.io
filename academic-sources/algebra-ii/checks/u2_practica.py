"""Comprobaciones de los ejercicios de la práctica de la Unidad 2 (transformaciones lineales).

Cada función recalcula los resultados publicados desde los datos del enunciado: linealidad con
símbolos, núcleos e imágenes (``nullspace`` / ``columnspace``), matrices asociadas, cambios de base,
composiciones e inversas, y las cuentas sobre Z_2 con aritmética modular exacta.
Convenciones: base canónica de P_2[R] ordenada {1, x, x^2}; de R^{2x2} ordenada {E11, E12, E21, E22};
[v]_B como columna; M(T)_{BB'} con columnas [T(b_j)]_{B'}; C_{BB'}[v]_B = [v]_{B'}.
"""
import sympy as sp
from content_pipeline.mathcheck import check, gf_matmul, gf_nullspace, gf_rank, gf_span, require, same

PG = "/algebra-ii/unidad-2/practica/"
INI = PG + "nivel-inicial/"
INT = PG + "nivel-intermedio/"
AVA = PG + "nivel-avanzado/"
GUIA = PG + "guia-integradora/"

x = sp.symbols("x")


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def col(*v):
    """Vector columna."""
    return sp.Matrix(list(v))


def cols(*vs):
    """Matriz cuyas columnas son los vectores dados (tuplas)."""
    return sp.Matrix.hstack(*[col(*v) for v in vs])


def mat(f, n):
    """Matriz de f respecto de las bases canónicas (columnas f(e_j))."""
    I = sp.eye(n)
    return sp.Matrix.hstack(*[f(I.col(j)) for j in range(n)])


def pol(c):
    """Polinomio c0 + c1 x + c2 x^2 a partir de sus coordenadas canónicas."""
    return sum(c[k] * x**k for k in range(len(c)))


def cp(q, n=2):
    """Coordenadas canónicas de q en {1, x, ..., x^n}."""
    q = sp.expand(q)
    return sp.Matrix([q.coeff(x, k) for k in range(n + 1)])


def mismo_sub(base, esperado):
    """Dos familias de vectores columna generan el mismo subespacio (comparación de rangos)."""
    X = sp.Matrix.hstack(*base)
    Y = sp.Matrix.hstack(*esperado)
    return X.rank() == Y.rank() == sp.Matrix.hstack(X, Y).rank()


def es_lineal(f, n):
    """f: columna de R^n -> columna; comprueba aditividad y homogeneidad con símbolos."""
    u = sp.Matrix(list(sp.symbols(" ".join(f"u{i}" for i in range(n)))))
    v = sp.Matrix(list(sp.symbols(" ".join(f"v{i}" for i in range(n)))))
    lam = sp.symbols("lam")
    d1 = (f(u + v) - f(u) - f(v)).applyfunc(sp.expand)
    d2 = (f(lam * u) - lam * f(u)).applyfunc(sp.expand)
    return d1 == sp.zeros(*d1.shape) and d2 == sp.zeros(*d2.shape)


def gf_vec_mat(a, G):
    """Producto fila-matriz a*G sobre Z_2, devuelve lista."""
    return gf_matmul([list(a)], G, 2)[0]


# ---------------------------------------------------------------------------
# Nivel inicial
# ---------------------------------------------------------------------------
@check("U2.01", "Linealidad y no linealidad de cinco funciones", page=INI)
def _():
    T = lambda v: col(v[0] - 2 * v[1] + v[2], 3 * v[1] - v[2])
    require(es_lineal(T, 3), "a) T es lineal")
    same(mat(T, 3), sp.Matrix([[1, -2, 1], [0, 3, -1]]), "matriz de T")
    S = lambda v: col(v[0] + v[1], 2)
    same(S(col(0, 0)), col(0, 2), "b) S(0,0) != 0")
    require(not es_lineal(S, 2), "S no lineal")
    F = lambda v: v[0] * v[1]
    same(F(col(1, 1)), 1, "F(1,1)")
    same(F(col(2, 2)), 4, "F(2,2)")
    require(F(col(2, 2)) != 2 * F(col(1, 1)), "c) F no homogénea")

    def D(v):
        p = pol([v[0], v[1], v[2]])
        q = sp.diff(p, x) + p.subs(x, 1)
        return cp(q)

    require(es_lineal(D, 3), "d) D es lineal")
    same(mat(D, 3), sp.Matrix([[1, 2, 1], [0, 0, 2], [0, 0, 0]]), "matriz de D en {1,x,x^2}")
    same(D(col(1, 1, 1)), col(4, 2, 0), "D(1+x+x^2) = 4+2x")
    det = lambda v: sp.Matrix([[v[0], v[1]], [v[2], v[3]]]).det()
    I2 = col(1, 0, 0, 1)
    same(det(2 * I2), 4, "e) det(2I)")
    same(2 * det(I2), 2, "e) 2 det(I)")
    require(det(2 * I2) != 2 * det(I2), "e) det no homogénea")


@check("U2.02", "Núcleo, imagen y preimagen de una TL de R^3 en R^3", page=INI)
def _():
    A = sp.Matrix([[1, -1, 2], [2, -1, 3], [1, 0, 1]])
    T = lambda v: A * v
    same(T(col(1, 1, 1)), col(2, 4, 2), "T(1,1,1)")
    N = A.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(-1, 1, 1)]), "Nu(T) = gen{(-1,1,1)}")
    same(A * col(-1, 1, 1), col(0, 0, 0), "T(-1,1,1)=0")
    C = A.columnspace()
    require(len(C) == 2, "dim Im = 2")
    require(mismo_sub(C, [col(1, 2, 1), col(-1, -1, 0)]), "Im(T) = gen{(1,2,1),(-1,-1,0)}")
    same(A.col(2), A.col(0) - A.col(1), "columna 3 = col1 - col2")
    for w in (col(1, 2, 1), col(-1, -1, 0)):
        same(w[2], w[1] - w[0], "ecuación de la imagen c = b - a")
    require(3 == len(N) + len(C), "teorema de la dimensión")
    p = col(1, -2, 0)
    same(A * p, col(3, 4, 1), "T(1,-2,0) = (3,4,1)")
    same(col(3, 4, 1)[2], col(3, 4, 1)[1] - col(3, 4, 1)[0], "(3,4,1) está en la imagen")
    t = sp.symbols("t")
    same(A * (p + t * col(-1, 1, 1)), col(3, 4, 1), "preimagen completa")
    w = col(1, 1, 1)
    require(w[2] != w[1] - w[0], "(1,1,1) no está en la imagen")


@check("U2.03", "Núcleo e imagen de T: P2 -> R^2, T(p) = (p(0), p(1) - p'(1))", page=INI)
def _():
    a, b, c = sp.symbols("a b c")
    p = a + b * x + c * x**2
    img = sp.Matrix([p.subs(x, 0), sp.expand(p.subs(x, 1) - sp.diff(p, x).subs(x, 1))])
    same(img, col(a, a - c), "T(a+bx+cx^2) = (a, a-c)")

    def T(v):
        q = pol([v[0], v[1], v[2]])
        return col(q.subs(x, 0), sp.expand(q.subs(x, 1) - sp.diff(q, x).subs(x, 1)))

    M = mat(T, 3)
    same(M, sp.Matrix([[1, 0, 0], [1, 0, -1]]), "matriz en las bases canónicas")
    N = M.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(0, 1, 0)]), "Nu(T) = gen{x}")
    require(M.rank() == 2, "T es sobreyectiva")
    require(mismo_sub(M.columnspace(), [col(1, 0), col(0, 1)]), "Im(T) = R^2")
    same(T(col(2, 3, 1)), col(2, 1), "T(2+3x+x^2) = (2,1)")
    require(len(N) + M.rank() == 3, "teorema de la dimensión")


@check("U2.04", "Núcleo e imagen de T(A) = A - A^t en R^{2x2}", page=INI)
def _():
    def T(v):
        A = sp.Matrix([[v[0], v[1]], [v[2], v[3]]])
        B = A - A.T
        return col(B[0, 0], B[0, 1], B[1, 0], B[1, 1])

    M = mat(T, 4)
    same(M, sp.Matrix([[0, 0, 0, 0], [0, 1, -1, 0], [0, -1, 1, 0], [0, 0, 0, 0]]), "matriz en {E11,E12,E21,E22}")
    N = M.nullspace()
    require(len(N) == 3, "dim Nu = 3")
    require(mismo_sub(N, [col(1, 0, 0, 0), col(0, 0, 0, 1), col(0, 1, 1, 0)]), "Nu = simétricas")
    C = M.columnspace()
    require(len(C) == 1 and mismo_sub(C, [col(0, 1, -1, 0)]), "Im = gen{E12 - E21}")
    require(len(N) + len(C) == 4, "teorema de la dimensión")
    # las simétricas son exactamente las que cumplen A = A^t
    for w in (col(1, 0, 0, 0), col(0, 0, 0, 1), col(0, 1, 1, 0)):
        same(T(w), col(0, 0, 0, 0), "T(simétrica) = 0")
    same(T(col(0, 1, 0, 0)), col(0, 1, -1, 0), "T(E12) = E12 - E21")
    # toda imagen es antisimétrica
    B = T(col(3, 5, -2, 7))
    same(B[0] , 0, "diagonal nula")
    same(B[1], -B[2], "antisimétrica")


@check("U2.05", "De la fórmula a la matriz y preimágenes de T(x,y,z) = (2x - y + z, x + 3z)", page=INI)
def _():
    T = lambda v: col(2 * v[0] - v[1] + v[2], v[0] + 3 * v[2])
    M = mat(T, 3)
    same(M, sp.Matrix([[2, -1, 1], [1, 0, 3]]), "M(T) en bases canónicas")
    N = M.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(-3, -5, 1)]), "Nu(T) = gen{(-3,-5,1)}")
    same(T(col(-3, -5, 1)), col(0, 0), "T(-3,-5,1) = 0")
    require(M.rank() == 2, "T sobreyectiva")
    same(T(col(5, 6, 0)), col(4, 5), "T(5,6,0) = (4,5)")
    t = sp.symbols("t")
    same(T(col(5, 6, 0) + t * col(-3, -5, 1)), col(4, 5), "preimagen de (4,5)")
    # M(T)_{EE'} inversa del problema: de la matriz a la fórmula
    A = sp.Matrix([[1, 2], [0, -1], [3, 1]])
    S = lambda v: A * v
    same(S(col(2, -3)), col(-4, 3, 3), "S(2,-3)")
    require(A.rank() == 2 and A.nullspace() == [], "S es monomorfismo")
    require(not mismo_sub(A.columnspace(), [col(1, 0, 0), col(0, 1, 0), col(0, 0, 1)]), "S no es epi")
    same(sp.Matrix.hstack(A, col(1, 1, 1)).rank(), 3, "(1,1,1) no está en la imagen de S")
    same(sp.Matrix.hstack(A, col(3, -1, 4)).rank(), 2, "(3,-1,4) = S(1,1)")
    same(S(col(1, 1)), col(3, -1, 4), "S(1,1)")


@check("U2.06", "Existencia de TL según dimensiones; ejemplo con núcleo gen{I}", page=INI)
def _():
    require(4 - 3 != 2, "a) epi con dim Nu = 2 en R^4 -> R^3 es imposible")
    Tb = lambda v: col(v[0], v[1], v[2], 0, 0)
    Mb = mat(Tb, 3)
    require(Mb.rank() == 3 and Mb.nullspace() == [], "b) inyectiva")
    require(3 < 4, "c) dim P2 = 3 < 4 = dim R^{2x2}")
    Td = lambda v: col(v[0] - v[3], v[1], v[2])
    Md = mat(Td, 4)
    same(Md, sp.Matrix([[1, 0, 0, -1], [0, 1, 0, 0], [0, 0, 1, 0]]), "d) matriz")
    N = Md.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(1, 0, 0, 1)]), "d) Nu = gen{I}")
    require(Md.rank() == 3, "d) epimorfismo")
    require(es_lineal(Td, 4), "d) lineal")
    same(Td(col(1, 0, 0, 1)), col(0, 0, 0), "T(I) = 0")


@check("U2.08", "Gráficos 2D: reflexión y cizalladura", page=INI)
def _():
    R = sp.Matrix([[-1, 0], [0, 1]])
    S = sp.Matrix([[1, 2], [0, 1]])
    SR = S * R
    RS = R * S
    same(SR, sp.Matrix([[-1, 2], [0, 1]]), "M(S o R)")
    same(RS, sp.Matrix([[-1, -2], [0, 1]]), "M(R o S)")
    require(SR != RS, "no conmutan")
    for v, w in ((col(0, 0), col(0, 0)), (col(1, 0), col(-1, 0)), (col(1, 1), col(1, 1)), (col(0, 1), col(2, 1))):
        same(SR * v, w, "imagen del vértice")
    same(RS * col(1, 1), col(-3, 1), "R o S (1,1)")
    same(SR.det(), -1, "det de S o R")
    same(SR.inv(), SR, "S o R es involución")
    same(SR * SR, sp.eye(2), "(S o R)^2 = I")
    same(S.inv(), sp.Matrix([[1, -2], [0, 1]]), "inversa de la cizalladura")
    same(R.inv() * S.inv(), SR, "(S o R)^{-1} = R^{-1} S^{-1}")


# ---------------------------------------------------------------------------
# Nivel intermedio
# ---------------------------------------------------------------------------
@check("U2.09", "Teorema fundamental: construcción de T con tres imágenes dadas", page=INT)
def _():
    B = cols((1, 0, 0), (1, 1, 0), (1, 1, 1))
    Im = cols((1, 0, 2), (2, 1, 0), (3, 1, 2))
    require(B.det() != 0, "B es base")
    A = Im * B.inv()
    same(A, sp.Matrix([[1, 1, 1], [0, 1, 0], [2, -2, 2]]), "matriz de T en canónicas")
    T = lambda v: A * v
    for b, w in zip(((1, 0, 0), (1, 1, 0), (1, 1, 1)), ((1, 0, 2), (2, 1, 0), (3, 1, 2))):
        same(T(col(*b)), col(*w), "T(b_i)")
    X, Y, Z = sp.symbols("X Y Z")
    same(T(col(X, Y, Z)), col(X + Y + Z, Y, 2 * X - 2 * Y + 2 * Z), "fórmula de T")
    same(B.inv() * col(1, 2, 3), col(-1, -1, 3), "coordenadas de (1,2,3) en B")
    same(T(col(1, 2, 3)), col(6, 2, 4), "T(1,2,3)")
    N = A.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(-1, 0, 1)]), "Nu(T) = gen{(-1,0,1)}")
    C = A.columnspace()
    require(len(C) == 2 and mismo_sub(C, [col(1, 0, 2), col(1, 1, -2)]), "Im(T) = gen{(1,0,2),(1,1,-2)}")
    n = col(-2, 4, 1)
    same((n.T * col(1, 0, 2))[0], 0, "ecuación de Im, 1")
    same((n.T * col(1, 1, -2))[0], 0, "ecuación de Im, 2")
    for c in A.columnspace():
        same((n.T * c)[0], 0, "la imagen cumple -2p+4q+r=0")
    same(sp.Matrix.hstack(A, col(3, 1, 2)).rank(), 2, "(3,1,2) está en Im")
    t = sp.symbols("t")
    same(T(col(1, 1, 1) + t * col(-1, 0, 1)), col(3, 1, 2), "preimagen de (3,1,2)")
    require(len(N) + len(C) == 3, "dimensión")


@check("U2.10", "Teorema fundamental con datos linealmente dependientes y un parámetro", page=INT)
def _():
    k = sp.symbols("k")
    v1, v2, v3 = col(1, 0, 1), col(0, 1, 1), col(1, 1, 2)
    same(v1 + v2, v3, "v3 = v1 + v2")
    require(sp.Matrix.hstack(v1, v2, v3).rank() == 2, "los datos son LD")
    w1, w2 = col(1, 2), col(0, 1)
    w3 = col(k, k + 2)
    cond = (w1 + w2 - w3).applyfunc(sp.expand)
    same(cond, col(1 - k, 3 - k - 2), "compatibilidad: (1-k, 1-k)")
    require(cond.subs(k, 1) == col(0, 0), "k = 1 compatible")
    require(cond.subs(k, 0) != col(0, 0), "k = 0 incompatible")
    same(w3.subs(k, 0), col(0, 2), "T(1,1,2) para k=0")
    same(w1 + w2, col(1, 3), "T(1,1,2) forzado")
    # completar con v4 = (0,0,1)
    B = cols((1, 0, 1), (0, 1, 1), (0, 0, 1))
    require(B.det() != 0, "{v1,v2,e3} es base")
    p, q = sp.symbols("p q")
    Im = sp.Matrix.hstack(w1, w2, col(p, q))
    A = Im * B.inv()
    X, Y, Z = sp.symbols("X Y Z")
    gen = (A * col(X, Y, Z)).applyfunc(sp.expand)
    same(gen, col(X + (Z - X - Y) * p, 2 * X + Y + (Z - X - Y) * q), "familia de TL")
    A0 = A.subs({p: 0, q: 0})
    same(A0, sp.Matrix([[1, 0, 0], [2, 1, 0]]), "T0(x,y,z) = (x, 2x+y)")
    A1 = A.subs({p: 1, q: 0})
    same(A1, sp.Matrix([[0, -1, 1], [2, 1, 0]]), "T1(x,y,z) = (z-y, 2x+y)")
    for AA in (A0, A1):
        same(AA * v1, w1, "T(v1)")
        same(AA * v2, w2, "T(v2)")
        same(AA * v3, col(1, 3), "T(v3)")
    require(A0 != A1, "dos TL distintas")
    N = A0.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(0, 0, 1)]), "Nu(T0) = gen{(0,0,1)}")
    require(A0.rank() == 2, "T0 sobreyectiva")


@check("U2.11", "TL con núcleo e imagen prescritos", page=INT)
def _():
    B = cols((1, 1, 1), (1, 0, 0), (0, 1, 0))
    require(B.det() != 0, "{(1,1,1),e1,e2} es base")
    Im = cols((0, 0, 0), (1, 0, 1), (0, 1, 1))
    A = Im * B.inv()
    same(A, sp.Matrix([[1, 0, -1], [0, 1, -1], [1, 1, -2]]), "matriz de T")
    X, Y, Z = sp.symbols("X Y Z")
    same(A * col(X, Y, Z), col(X - Z, Y - Z, X + Y - 2 * Z), "fórmula de T")
    same(A * col(0, 0, 1), col(-1, -1, -2), "T(e3) = -T(e1) - T(e2)")
    N = A.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(1, 1, 1)]), "Nu(T) = gen{(1,1,1)}")
    require(mismo_sub(A.columnspace(), [col(1, 0, 1), col(0, 1, 1)]), "Im(T) = gen{(1,0,1),(0,1,1)}")
    # otra TL distinta con los mismos núcleo e imagen
    Im2 = cols((0, 0, 0), (0, 1, 1), (1, 0, 1))
    A2 = Im2 * B.inv()
    require(A2 != A, "T' distinta")
    require(len(A2.nullspace()) == 1 and mismo_sub(A2.nullspace(), [col(1, 1, 1)]), "Nu(T')")
    require(mismo_sub(A2.columnspace(), [col(1, 0, 1), col(0, 1, 1)]), "Im(T')")
    same(A2, sp.Matrix([[0, 1, -1], [1, 0, -1], [1, 1, -2]]), "matriz de T'")
    # no existe con Nu = gen{(1,1,1)} y T epi: dim Im = 3 - 1 = 2 < 3
    require(3 - 1 == 2 and 2 < 3, "dim Im = 2 < 3")


@check("U2.12", "Matriz asociada en bases no canónicas, de R^3 en R^2", page=INT)
def _():
    A = sp.Matrix([[1, 1, -1], [2, 0, -1]])
    T = lambda v: A * v
    b = [(1, 0, 1), (0, 1, 1), (1, 1, 0)]
    bp = [(1, 0), (1, 1)]
    Bm, Bpm = cols(*b), cols(*bp)
    require(Bm.det() != 0 and Bpm.det() != 0, "B y B' son bases")
    imgs = [T(col(*v)) for v in b]
    same(imgs[0], col(0, 1), "T(b1)")
    same(imgs[1], col(0, -1), "T(b2)")
    same(imgs[2], col(2, 2), "T(b3)")
    coords = [Bpm.inv() * w for w in imgs]
    same(coords[0], col(-1, 1), "[T(b1)]_B'")
    same(coords[1], col(1, -1), "[T(b2)]_B'")
    same(coords[2], col(0, 2), "[T(b3)]_B'")
    M = sp.Matrix.hstack(*coords)
    same(M, sp.Matrix([[-1, 1, 0], [1, -1, 2]]), "M(T)_{BB'}")
    same(Bpm.inv() * A * Bm, M, "M = C_{E'B'} A C_{BE}")
    cb = col(1, 2, -1)
    v = Bm * cb
    same(v, col(0, 1, 3), "v = b1 + 2 b2 - b3")
    same(M * cb, col(1, -3), "[T(v)]_B'")
    same(Bpm * (M * cb), col(-2, -3), "T(v) en canónicas")
    same(T(v), col(-2, -3), "T(v) directo")
    N = M.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(1, 1, 0)]), "nul(M) = gen{(1,1,0)}")
    same(Bm * col(1, 1, 0), col(1, 1, 2), "núcleo en canónicas")
    same(T(col(1, 1, 2)), col(0, 0), "T(1,1,2) = 0")
    require(M.rank() == 2, "T epi")


@check("U2.13", "Diferencia finita en P2 con una base no canónica", page=INT)
def _():
    def T(v):
        p = pol([v[0], v[1], v[2]])
        return cp(p.subs(x, x + 1) - p)

    ME = mat(T, 3)
    same(ME, sp.Matrix([[0, 1, 1], [0, 0, 2], [0, 0, 0]]), "M(T)_E")
    require(es_lineal(T, 3), "T lineal")
    b = [(1, 0, 0), (1, 1, 0), (1, 1, 1)]
    Bm = cols(*b)
    imgs = [T(col(*v)) for v in b]
    same(imgs[0], col(0, 0, 0), "T(1) = 0")
    same(imgs[1], col(1, 0, 0), "T(1+x) = 1")
    same(imgs[2], col(2, 2, 0), "T(1+x+x^2) = 2+2x")
    M = Bm.inv() * ME * Bm
    same(M, sp.Matrix([[0, 1, 0], [0, 0, 2], [0, 0, 0]]), "M(T)_B")
    N = M.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(1, 0, 0)]), "nul(M) = gen{(1,0,0)}")
    same(Bm * col(1, 0, 0), col(1, 0, 0), "Nu(T) = gen{1}")
    require(mismo_sub(M.columnspace(), [col(1, 0, 0), col(0, 1, 0)]), "col(M) = gen{e1,e2}")
    same(Bm * col(1, 0, 0), col(1, 0, 0), "1 = [1]_B -> 1")
    same(Bm * col(0, 1, 0), col(1, 1, 0), "[e2]_B -> 1 + x")
    same(M * M, sp.Matrix([[0, 0, 2], [0, 0, 0], [0, 0, 0]]), "M(T o T)_B")
    same(M * M * M, sp.zeros(3, 3), "T^3 = 0")
    same(ME * ME, sp.Matrix([[0, 0, 2], [0, 0, 0], [0, 0, 0]]), "M(T o T)_E")
    # T(T(x^2)) = T(2x + 1) = 2
    same(T(col(0, 0, 1)), col(1, 2, 0), "T(x^2) = 1 + 2x")
    same(T(T(col(0, 0, 1))), col(2, 0, 0), "T(T(x^2)) = 2")


@check("U2.14", "Cambio de base con tres factores de R^2 en R^3", page=INT)
def _():
    A = sp.Matrix([[1, 2], [0, 1], [1, -1]])
    b1 = [(1, 1), (1, 2)]
    b1p = [(1, 0, 0), (1, 1, 0), (1, 1, 1)]
    B1, B1p = cols(*b1), cols(*b1p)
    same(B1.det(), 1, "B1 base")
    same(B1p.det(), 1, "B1' base")
    CB1E = B1
    CEB1p = B1p.inv()
    same(CEB1p, sp.Matrix([[1, -1, 0], [0, 1, -1], [0, 0, 1]]), "C_{E'B1'}")
    same(A * B1, sp.Matrix([[3, 5], [1, 2], [0, -1]]), "A C_{B1E}")
    M = CEB1p * A * CB1E
    same(M, sp.Matrix([[2, 3], [1, 3], [0, -1]]), "M(T)_{B1B1'}")
    # directo: columnas [T(b_j)]_{B1'}
    directo = sp.Matrix.hstack(*[B1p.inv() * (A * col(*v)) for v in b1])
    same(directo, M, "cálculo directo")
    same(B1p * M * col(1, 0), A * col(1, 1), "reconstrucción de T(b1)")
    same(A * col(1, 1), col(3, 1, 0), "T(1,1)")
    same(A * col(1, 2), col(5, 2, -1), "T(1,2)")
    require(M.rank() == 2, "T inyectiva")
    X, Y = sp.symbols("X Y")
    same(A * col(X, Y), col(X + 2 * Y, Y, X - Y), "T(x,y)")


@check("U2.15", "Composición de S: R^2 -> R^3 y U: R^3 -> R^2", page=INT)
def _():
    MS = sp.Matrix([[1, 1], [0, 1], [1, -1]])
    MU = sp.Matrix([[1, 0, 1], [0, 1, -1]])
    X, Y, Z = sp.symbols("X Y Z")
    same(MS * col(X, Y), col(X + Y, Y, X - Y), "S(x,y)")
    same(MU * col(X, Y, Z), col(X + Z, Y - Z), "U(x,y,z)")
    US = MU * MS
    same(US, sp.Matrix([[2, 0], [-1, 2]]), "M(U o S)")
    same(US * col(X, Y), col(2 * X, 2 * Y - X), "(U o S)(x,y)")
    same(MU * (MS * col(X, Y)), US * col(X, Y), "U(S(v))")
    same(US.det(), 4, "det(U o S)")
    inv = US.inv()
    same(inv, sp.Matrix([[sp.Rational(1, 2), 0], [sp.Rational(1, 4), sp.Rational(1, 2)]]), "inversa")
    same(US * inv, sp.eye(2), "(U o S)(U o S)^{-1} = I")
    SU = MS * MU
    same(SU, sp.Matrix([[1, 1, 0], [0, 1, -1], [1, -1, 2]]), "M(S o U)")
    same(SU.det(), 0, "det(S o U)")
    require(SU.rank() == 2, "rango de S o U")
    N = SU.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(1, -1, -1)]), "Nu(S o U) = gen{(1,-1,-1)}")
    same(SU * col(1, -1, -1), col(0, 0, 0), "(S o U)(1,-1,-1) = 0")
    same(MU * col(1, -1, -1), col(0, 0), "(1,-1,-1) en Nu(U)")
    require(MS.rank() == 2 and MU.rank() == 2, "S mono, U epi")
    require(MS.nullspace() == [], "S inyectiva")


@check("U2.16", "TL inversible en P2: T(p) = p + p'", page=INT)
def _():
    def T(v):
        p = pol([v[0], v[1], v[2]])
        return cp(p + sp.diff(p, x))

    M = mat(T, 3)
    same(M, sp.Matrix([[1, 1, 0], [0, 1, 2], [0, 0, 1]]), "M(T)_E")
    require(es_lineal(T, 3), "T lineal")
    same(M.det(), 1, "det")
    Mi = M.inv()
    same(Mi, sp.Matrix([[1, -1, 2], [0, 1, -2], [0, 0, 1]]), "M(T^{-1})")
    q0, q1, q2 = sp.symbols("q0 q1 q2")
    same(Mi * col(q0, q1, q2), col(q0 - q1 + 2 * q2, q1 - 2 * q2, q2), "fórmula de T^{-1}")
    same(Mi * col(3, 1, 1), col(4, -1, 1), "T^{-1}(3+x+x^2) = 4 - x + x^2")
    same(T(col(4, -1, 1)), col(3, 1, 1), "T(4 - x + x^2) = 3 + x + x^2")
    D = sp.Matrix([[0, 1, 0], [0, 0, 2], [0, 0, 0]])
    same(sp.eye(3) - D + D * D, Mi, "T^{-1} = I - D + D^2")
    same(D * D * D, sp.zeros(3, 3), "D^3 = 0")
    same(M, sp.eye(3) + D, "T = I + D")
    same((sp.eye(3) + D) * (sp.eye(3) - D + D * D), sp.eye(3), "(I+D)(I-D+D^2) = I")


@check("U2.17", "Codificación a -> aG sobre Z_2 como TL", page=INT)
def _():
    G = [[1, 0, 0, 1, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1]]
    msgs = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    code = {m: tuple(gf_vec_mat(m, G)) for m in msgs}
    for m in msgs:
        a, b, c = m
        require(code[m] == ((a), b, c, (a + b) % 2, (a + c) % 2), "fórmula (a,b,c,a+b,a+c)")
    for m in msgs:
        for n in msgs:
            s = tuple((i + j) % 2 for i, j in zip(m, n))
            lhs = tuple(gf_vec_mat(s, G))
            rhs = tuple((i + j) % 2 for i, j in zip(code[m], code[n]))
            require(lhs == rhs, "aditividad sobre Z_2")
    require(gf_rank(G, 2) == 3, "rango 3: T inyectiva")
    Gt = [list(c) for c in zip(*G)]
    require(gf_nullspace(Gt, 2) == [], "Nu(T) = {0}")
    words = set(code.values())
    require(len(words) == 8, "ocho palabras distintas")
    require(words == set(gf_span(G, 2)), "Im(T) = gen de las filas de G")
    require(len(words) < 2**5, "T no es epi")
    require((1, 1, 0, 0, 1) in words and code[(1, 1, 0)] == (1, 1, 0, 0, 1), "T(1,1,0) = (1,1,0,0,1)")
    require((1, 0, 1, 1, 1) not in words, "(1,0,1,1,1) no es palabra código")
    for w in words:
        require(w[3] == (w[0] + w[1]) % 2 and w[4] == (w[0] + w[2]) % 2, "ecuaciones de la imagen")
    bad = (1, 0, 1, 1, 1)
    require(bad[3] != (bad[0] + bad[1]) % 2 or bad[4] != (bad[0] + bad[2]) % 2, "incumple una ecuación")
    todos = [(a, b, c, d, e) for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1) for e in (0, 1)]
    ecuaciones = {u for u in todos if u[3] == (u[0] + u[1]) % 2 and u[4] == (u[0] + u[2]) % 2}
    require(words == ecuaciones, "Im = {u: u4 = u1+u2, u5 = u1+u3}")
    # matriz de T en columnas: G^t
    require([list(r) for r in zip(*G)] == [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1]], "G^t")


@check("U2.18", "T(A) = AB - BA en R^{2x2} desde su matriz", page=INT)
def _():
    Bm = sp.Matrix([[0, 1], [0, 0]])

    def T(v):
        A = sp.Matrix([[v[0], v[1]], [v[2], v[3]]])
        C = A * Bm - Bm * A
        return col(C[0, 0], C[0, 1], C[1, 0], C[1, 1])

    M = mat(T, 4)
    same(M, sp.Matrix([[0, 0, -1, 0], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 1, 0]]), "M(T)_E")
    a, b, c, d = sp.symbols("a b c d")
    same(T(col(a, b, c, d)), col(-c, a - d, 0, c), "T([[a,b],[c,d]])")
    require(es_lineal(T, 4), "T lineal")
    N = M.nullspace()
    require(len(N) == 2 and mismo_sub(N, [col(1, 0, 0, 1), col(0, 1, 0, 0)]), "Nu(T) = gen{I, E12}")
    C = M.columnspace()
    require(len(C) == 2 and mismo_sub(C, [col(0, 1, 0, 0), col(-1, 0, 0, 1)]), "Im(T) = gen{E12, -E11+E22}")
    require(len(N) + len(C) == 4, "dim")
    # [[1,0],[0,1]] y E12 conmutan con B
    for w in (col(1, 0, 0, 1), col(0, 1, 0, 0)):
        same(T(w), col(0, 0, 0, 0), "T = 0 sobre el núcleo")
    # preimagen de E12: A con -c = 0, a - d = 1, c = 0 (E12 en Im)
    same(T(col(1, 0, 0, 0)), col(0, 1, 0, 0), "T(E11) = E12")
    same(sp.Matrix.hstack(M, col(0, 1, 0, 0)).rank(), 2, "E12 en Im")
    same(sp.Matrix.hstack(M, col(1, 0, 0, 0)).rank(), 3, "E11 no está en Im")
    same(T(T(col(a, b, c, d))), col(0, -2 * c, 0, 0), "T(T(A)) = -2c E12")


# ---------------------------------------------------------------------------
# Nivel avanzado
# ---------------------------------------------------------------------------
@check("U2.21", "Contraejemplo: S o T biyectiva sin S inyectiva ni T sobreyectiva", page=AVA)
def _():
    MT = sp.Matrix([[1], [0]])
    MS = sp.Matrix([[1, 0]])
    same(MS * MT, sp.Matrix([[1]]), "S o T = id de R")
    require(MT.rank() == 1 and MT.rows == 2, "T no es sobreyectiva (dim Im = 1 < 2)")
    N = MS.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(0, 1)]), "Nu(S) = gen{(0,1)}")
    same(MS * col(0, 1), col(0), "S(0,1) = 0")
    same(MS * MT * col(7), col(7), "(S o T)(7) = 7")
    X = sp.symbols("X")
    same(MT * col(X), col(X, 0), "T(x) = (x,0)")
    require(sp.Matrix.hstack(MT, col(0, 1)).rank() == 2, "(0,1) no está en Im(T)")


@check("U2.22", "Contraejemplos sobre núcleo e imagen de una suma", page=AVA)
def _():
    S = sp.eye(2)
    T = -sp.eye(2)
    Z = S + T
    same(Z, sp.zeros(2, 2), "S + T = 0")
    require(len(Z.nullspace()) == 2, "Nu(S+T) = R^2")
    require(S.nullspace() == [] and T.nullspace() == [], "Nu(S) = Nu(T) = {0}")
    require(Z.columnspace() == [], "Im(S+T) = {0}")
    require(sp.Matrix.hstack(S, T).rank() == 2, "Im(S) + Im(T) = R^2")
    # las inclusiones sí valen: Nu(S) ∩ Nu(T) está en Nu(S+T) e Im(S+T) está en Im(S) + Im(T)
    S3 = sp.Matrix([[1, 1], [0, 0]])
    T3 = sp.Matrix([[2, 2], [0, 0]])
    v = col(1, -1)
    same(S3 * v, col(0, 0), "v en Nu(S3)")
    same(T3 * v, col(0, 0), "v en Nu(T3)")
    same((S3 + T3) * v, col(0, 0), "v en Nu(S3 + T3)")
    w = (S3 + T3) * col(2, 5)
    same(w, S3 * col(2, 5) + T3 * col(2, 5), "(S+T)(u) = S(u) + T(u)")


@check("U2.23", "Proyección T o T = T: ejemplo en R^2", page=AVA)
def _():
    A = sp.Matrix([[1, 1], [0, 0]])
    same(A * A, A, "T o T = T")
    N = A.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(1, -1)]), "Nu(T) = gen{(1,-1)}")
    require(mismo_sub(A.columnspace(), [col(1, 0)]), "Im(T) = gen{(1,0)}")
    same(A * col(3, 2), col(5, 0), "T(3,2) = (5,0)")
    same(col(3, 2) - col(5, 0), -2 * col(1, -1), "(3,2) - T(3,2) en el núcleo")
    same(A * col(-2, 2), col(0, 0), "T(-2,2) = 0")
    same(A * col(5, 0), col(5, 0), "T fija su imagen")
    same(col(-2, 2) + col(5, 0), col(3, 2), "descomposición")


@check("U2.24", "Verdadero o falso sobre TL de R^2 y R^3", page=AVA)
def _():
    # a) existe T: R^2 -> R^2 con Nu(T) = Im(T)
    A = sp.Matrix([[0, 1], [0, 0]])
    N, C = A.nullspace(), A.columnspace()
    require(mismo_sub(N, [col(1, 0)]) and mismo_sub(C, [col(1, 0)]), "a) Nu = Im = gen{(1,0)}")
    same(A * A, sp.zeros(2, 2), "a) T o T = 0")
    # b) imposible en R^3: dim Nu = dim Im y suma 3
    require(not any(2 * d == 3 for d in range(0, 4)), "b) 2d = 3 no tiene solución entera")
    # c) T(e1) = (1,1), T(e2) = (0,1), T(1,1,0) = (1,3)
    M = sp.Matrix([[1, 0], [1, 1]])
    same(M * col(1, 1), col(1, 2), "c) T(1,1,0) forzado = (1,2)")
    require(col(1, 2) != col(1, 3), "c) incompatible con (1,3)")
    # d) S o T = 0 pero T o S != 0
    Tm = sp.Matrix([[0, 0], [1, 0]])
    Sm = sp.Matrix([[1, 0], [0, 0]])
    same(Sm * Tm, sp.zeros(2, 2), "d) S o T = 0")
    TS = Tm * Sm
    same(TS, sp.Matrix([[0, 0], [1, 0]]), "d) T o S")
    require(TS != sp.zeros(2, 2), "d) T o S != 0")
    same(Tm * col(1, 0), col(0, 1), "d) T(1,0) = (0,1)")
    same(Sm * col(0, 1), col(0, 0), "d) S(0,1) = 0")
    same(Sm * col(1, 0), col(1, 0), "d) S(1,0) = (1,0)")
    same(Tm * col(1, 0), col(0, 1), "d) (T o S)(1,0) = (0,1)")


@check("U2.25", "Familia T_k de TL de R^3: núcleo, imagen y clasificación según k", page=AVA)
def _():
    k = sp.symbols("k")
    A = sp.Matrix([[1, 1, k], [1, k, 1], [k, 1, 1]])
    same(A.det(), -(k - 1) ** 2 * (k + 2), "det A_k")
    same(A.det(), -k**3 + 3 * k - 2, "det expandido")
    A1 = A.subs(k, 1)
    require(A1.rank() == 1, "rango 1 para k=1")
    N1 = A1.nullspace()
    require(len(N1) == 2 and mismo_sub(N1, [col(-1, 1, 0), col(-1, 0, 1)]), "Nu(T_1) = {x+y+z=0}")
    require(mismo_sub(A1.columnspace(), [col(1, 1, 1)]), "Im(T_1) = gen{(1,1,1)}")
    A2 = A.subs(k, -2)
    require(A2.rank() == 2, "rango 2 para k=-2")
    N2 = A2.nullspace()
    require(len(N2) == 1 and mismo_sub(N2, [col(1, 1, 1)]), "Nu(T_-2) = gen{(1,1,1)}")
    require(mismo_sub(A2.columnspace(), [col(1, 1, -2), col(1, -2, 1)]), "Im(T_-2) = {x+y+z=0}")
    for c in (A2.col(0), A2.col(1), A2.col(2)):
        same(c[0] + c[1] + c[2], 0, "columnas en x+y+z=0")
    same(A2.col(0) + A2.col(1) + A2.col(2), col(0, 0, 0), "suma de columnas nula")
    for kv in (0, 2, -1, 3):
        require(A.subs(k, kv).det() != 0, f"T_{kv} es iso")
    same(A.subs(k, 0).det(), -2, "det A_0")
    inv0 = A.subs(k, 0).inv()
    same(inv0 * A.subs(k, 0), sp.eye(3), "A_0 inversible")
    same(A.subs(k, 2).det(), -4, "det A_2")
    same(A.subs(k, 1) * col(1, 1, 1), col(3, 3, 3), "T_1(1,1,1)")
    same(A.subs(k, -2) * col(1, 1, 1), col(0, 0, 0), "T_-2(1,1,1)")
    # k = 1: T_1 de rango 1; dimensión del núcleo
    require(len(N1) + A1.rank() == 3 and len(N2) + A2.rank() == 3, "teorema de la dimensión")


@check("U2.26", "Matriz asociada con bases abstractas: núcleo, imagen y cambio de bases", page=AVA)
def _():
    # T(v1) = w1 - w2, T(v2) = 2 w1 - 2 w2, T(v3) = w1
    M = cols((1, -1), (2, -2), (1, 0))
    same(M, sp.Matrix([[1, 2, 1], [-1, -2, 0]]), "M(T)_{BB'}")
    require(M.rank() == 2, "T epi")
    N = M.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(-2, 1, 0)]), "nul(M) = gen{(-2,1,0)}")
    same(M * col(-2, 1, 0), col(0, 0), "T(-2 v1 + v2) = 0")
    same(M * col(2, 0, -1), col(1, -2), "T(2 v1 - v3) = w1 - 2 w2")
    same(M * col(1, 1, 0), col(3, -3), "T(v1 + v2) = 3 w1 - 3 w2")
    C = sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]])      # C_{B1 B}: columnas [b1_j]_B
    require(C.det() != 0, "B1 base")
    Cp = sp.Matrix([[1, 0], [1, 1]])                       # columnas de B1' en B'
    require(Cp.det() != 0, "B1' base")
    Cpinv = Cp.inv()
    same(Cpinv, sp.Matrix([[1, 0], [-1, 1]]), "C_{B'B1'}")
    same(M * C, sp.Matrix([[3, 3, 1], [-3, -2, 0]]), "M(T)_{BB'} C_{B1B}")
    M1 = Cpinv * M * C
    same(M1, sp.Matrix([[3, 3, 1], [-6, -5, -1]]), "M(T)_{B1B1'}")
    # directo
    same(Cpinv * col(3, -3), col(3, -6), "[T(v1+v2)]_{B1'}")
    same(Cpinv * col(3, -2), col(3, -5), "[T(v2+v3)]_{B1'}")
    same(Cpinv * col(1, 0), col(1, -1), "[T(v3)]_{B1'}")
    require(M1.rank() == 2, "mismo rango")
    same(C.inv() * col(-2, 1, 0), col(-2, 3, -3), "[-2v1+v2]_{B1}")
    same(M1 * col(-2, 3, -3), col(0, 0), "M1 anula al núcleo en B1")
    same(C * col(-2, 3, -3), col(-2, 1, 0), "-2(v1+v2) + 3(v2+v3) - 3 v3 = -2 v1 + v2")


@check("U2.27", "Reflexión respecto de una recta en una base adaptada", page=AVA)
def _():
    B = cols((1, 2), (-2, 1))
    D = sp.Matrix([[1, 0], [0, -1]])
    same(B.det(), 5, "B base")
    R = B * D * B.inv()
    same(R, sp.Matrix([[-3, 4], [4, 3]]) / 5, "M(T)_E")
    same(R * col(1, 2), col(1, 2), "T(1,2) = (1,2)")
    same(R * col(-2, 1), col(2, -1), "T(-2,1) = (2,-1)")
    same(R * col(3, 1), col(-1, 3), "T(3,1) = (-1,3)")
    same(R * R, sp.eye(2), "T o T = I")
    same(R.inv(), R, "T^{-1} = T")
    same(R.det(), -1, "det = -1")
    same(B.inv() * col(3, 1), col(1, -1), "[(3,1)]_B")
    same(D * col(1, -1), col(1, 1), "M(T)_B [v]_B")
    same(B * col(1, 1), col(-1, 3), "T(3,1) en canónicas")
    same((col(3, 1).T * col(3, 1))[0], (col(-1, 3).T * col(-1, 3))[0], "conserva la longitud")
    X, Y = sp.symbols("X Y")
    same(R * col(X, Y), col((-3 * X + 4 * Y) / 5, (4 * X + 3 * Y) / 5), "fórmula")
    same(sp.Matrix([[-3, 4], [4, 3]]).det(), -25, "det sin factor")
    require(R.nullspace() == [], "T iso")


# ---------------------------------------------------------------------------
# Guía integradora
# ---------------------------------------------------------------------------
@check("U2.28", "Problema 1: TL de R^3 en P2 definida sobre una base", page=GUIA)
def _():
    b = [(1, 0, 0), (1, 1, 0), (1, 1, 1)]
    imgs = [[1, 1, 0], [0, 1, -1], [1, 0, 1]]       # 1+x, x-x^2, 1+x^2
    Bm = cols(*b)
    Im = cols(*imgs)
    require(Bm.det() != 0, "B base")
    A = Im * Bm.inv()
    X, Y, Z = sp.symbols("X Y Z")
    same(Bm.inv() * col(X, Y, Z), col(X - Y, Y - Z, Z), "coordenadas en B")
    same(A * col(X, Y, Z), col(X - Y + Z, X - Z, 2 * Z - Y), "T(a,b,c) = (a-b+c)+(a-c)x+(2c-b)x^2")
    same(A, sp.Matrix([[1, -1, 1], [1, 0, -1], [0, -1, 2]]), "M(T)_{EE'}")
    for v, w in zip(b, imgs):
        same(A * col(*v), col(*w), "T(b_i)")
    N = A.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(1, 2, 1)]), "Nu(T) = gen{(1,2,1)}")
    same(A * col(1, 2, 1), col(0, 0, 0), "T(1,2,1) = 0")
    C = A.columnspace()
    require(len(C) == 2 and mismo_sub(C, [col(1, 1, 0), col(1, 0, 1)]), "Im(T) = gen{1+x, 1+x^2}")
    require(len(N) + len(C) == 3, "dimensión")
    require(A.rank() < 3, "T ni mono ni epi")
    q = col(2, 1, 1)
    same(sp.Matrix.hstack(A, q).rank(), 2, "q en Im")
    same(q, col(1, 1, 0) + col(1, 0, 1), "q = (1+x) + (1+x^2)")
    t = sp.symbols("t")
    same(A * (col(1, -1, 0) + t * col(1, 2, 1)), q, "preimagen de q")
    same(A * col(1, -1, 0), q, "T(1,-1,0) = q")
    same(sp.Matrix.hstack(A, col(0, 0, 1)).rank(), 3, "x^2 no está en Im")


@check("U2.29", "Problema 2: endomorfismo de R^2 con parámetro dado por M(T)_B", page=GUIA)
def _():
    k = sp.symbols("k")
    B = cols((1, 1), (1, 2))
    Mk = sp.Matrix([[1, -1], [2, k]])
    ME = B * Mk * B.inv()
    same(B.inv(), sp.Matrix([[2, -1], [-1, 1]]), "C_{EB}")
    same(ME, sp.Matrix([[7 - k, k - 4], [11 - 2 * k, 2 * k - 6]]), "M(T)_E en función de k")
    same(Mk.det(), k + 2, "det M(T)_B")
    same(ME.det(), k + 2, "det M(T)_E (semejantes)")
    for kv in (0, 1, 3, -1):
        require(Mk.det().subs(k, kv) != 0, "iso")
    M2 = ME.subs(k, -2)
    same(M2, sp.Matrix([[9, -6], [15, -10]]), "M(T)_E para k = -2")
    require(M2.rank() == 1, "rango 1")
    N = M2.nullspace()
    require(len(N) == 1 and mismo_sub(N, [col(2, 3)]), "Nu(T) = gen{(2,3)}")
    require(mismo_sub(M2.columnspace(), [col(3, 5)]), "Im(T) = gen{(3,5)}")
    same(M2 * col(2, 3), col(0, 0), "T(2,3) = 0")
    same(M2.col(0), 3 * col(3, 5), "primera columna")
    same(M2.col(1), -2 * col(3, 5), "segunda columna")
    Mb = Mk.subs(k, -2)
    same(Mb.nullspace()[0], col(1, 1), "nul(M(T)_B) = gen{(1,1)}")
    same(B * col(1, 1), col(2, 3), "núcleo en canónicas")
    same(B * Mb.col(0), col(3, 5), "imagen: columna 1 en canónicas")
    same(M2 * M2, -M2, "T o T = -T")
    require(M2 * M2 != sp.zeros(2, 2), "T o T no es nula")
    same((M2 + sp.eye(2)) * M2, sp.zeros(2, 2), "(T + I) o T = 0")
    same(M2 * col(3, 5), col(-3, -5), "T(3,5) = -(3,5)")


@check("U2.30", "Problema 3: codificación y detección de errores con TL sobre Z_2", page=GUIA)
def _():
    G = [[1, 0, 1, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 1]]
    msgs = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    code = {m: tuple(gf_vec_mat(m, G)) for m in msgs}
    for m in msgs:
        a, b, c = m
        require(code[m] == ((a + c) % 2, (b + c) % 2, (a + b) % 2, (a + c) % 2, (b + c) % 2), "fórmula de T")
    require(gf_rank(G, 2) == 2, "rango 2")
    Gt = [list(c) for c in zip(*G)]
    N = gf_nullspace(Gt, 2)
    require(N == [[1, 1, 1]], "Nu(T) = {000, 111}")
    require(code[(1, 1, 1)] == (0, 0, 0, 0, 0), "T(1,1,1) = 0")
    words = set(code.values())
    require(len(words) == 4, "|Im| = 4")
    require(words == set(gf_span([G[0], G[1]], 2)), "Im(T) = gen{filas 1 y 2}")
    require(words == {(0, 0, 0, 0, 0), (1, 0, 1, 1, 0), (0, 1, 1, 0, 1), (1, 1, 0, 1, 1)}, "palabras")
    u = (1, 1, 0, 1, 1)
    pre = sorted(m for m in msgs if code[m] == u)
    require(pre == [(0, 0, 1), (1, 1, 0)], "T^{-1}(u) = {(0,0,1),(1,1,0)}")
    require(tuple((i + j) % 2 for i, j in zip((0, 0, 1), (1, 1, 1))) == (1, 1, 0), "(0,0,1) + (1,1,1)")
    H = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0]]
    HtT = [list(c) for c in zip(*H)]          # 5x2: S(x) = x H^t
    comp = gf_matmul(G, HtT, 2)
    require(comp == [[0, 0]] * 3, "S o T = 0")
    require(gf_rank(H, 2) == 2, "S epi")
    require(len(gf_nullspace(H, 2)) == 3, "dim Nu(S) = 3")
    require(len(gf_nullspace(H, 2)) > 2, "Im(T) estrictamente contenida en Nu(S)")
    r = (1, 0, 0, 1, 1)
    s = gf_matmul([list(r)], HtT, 2)[0]
    require(s == [0, 1], "S(r) = (0,1)")
    require(r not in words, "r no es palabra código")
    for w in words:
        require(gf_matmul([list(w)], HtT, 2)[0] == [0, 0], "S anula la imagen")
    z = (1, 1, 1, 0, 0)
    require(gf_matmul([list(z)], HtT, 2)[0] == [0, 0] and z not in words, "S(z) = 0 pero z no está en Im(T)")


@check("U2.31", "Problema 4: transformaciones con T o T = 0", page=GUIA)
def _():
    T = lambda v: col(v[2], v[3], 0, 0)
    M = mat(T, 4)
    same(M, sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]), "M(T)_E")
    same(M * M, sp.zeros(4, 4), "T o T = 0")
    N = M.nullspace()
    C = M.columnspace()
    require(len(N) == 2 and len(C) == 2, "dim Nu = dim Im = 2")
    require(mismo_sub(N, [col(1, 0, 0, 0), col(0, 1, 0, 0)]), "Nu(T) = gen{e1, e2}")
    require(mismo_sub(C, [col(1, 0, 0, 0), col(0, 1, 0, 0)]), "Im(T) = gen{e1, e2}")
    require(2 * 2 <= 4, "2 dim Im <= 4")
    require(not any(2 * r <= 3 and r == 2 for r in range(4)), "rango 2 no cabe en R^3 con T^2 = 0")
    S = sp.eye(4) + M
    Sinv = sp.eye(4) - M
    same(S * Sinv, sp.eye(4), "(I+T)(I-T) = I")
    same(Sinv * S, sp.eye(4), "(I-T)(I+T) = I")
    same(S.det(), 1, "det(I+T) = 1")
    same(S.inv(), Sinv, "inversa")
    same(S * col(1, 2, 3, 4), col(4, 6, 3, 4), "(I+T)(1,2,3,4)")
    same(Sinv * col(4, 6, 3, 4), col(1, 2, 3, 4), "(I-T)(4,6,3,4)")
    # contraejemplo de la recíproca de rango: un T con T^2 = 0 en R^3 de rango 1
    M3 = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    same(M3 * M3, sp.zeros(3, 3), "T^2 = 0 en R^3, rango 1")
    require(M3.rank() == 1 and 2 * 1 <= 3, "rango 1 cabe")
    require(M.det() == 0, "T no es iso")


@check("U2.32", "Problema 5: gráficos 2D con coordenadas homogéneas", page=GUIA)
def _():
    Tr = lambda v: col(v[0] + 2, v[1] - 1)
    same(Tr(col(0, 0)), col(2, -1), "Tr(0,0) = (2,-1) != 0")
    require(Tr(col(1, 0)) + Tr(col(0, 1)) != Tr(col(1, 1)), "Tr no aditiva")
    same(Tr(col(1, 0)) + Tr(col(0, 1)), col(5, -1), "Tr(e1) + Tr(e2)")
    same(Tr(col(1, 1)), col(3, 0), "Tr(e1 + e2)")
    H = sp.Matrix([[1, 0, 2], [0, 1, -1], [0, 0, 1]])
    X, Y = sp.symbols("X Y")
    same(H * col(X, Y, 1), col(X + 2, Y - 1, 1), "H actúa como la traslación")
    require(es_lineal(lambda v: H * v, 3), "H es lineal")
    same(H.det(), 1, "det H")
    Hi = H.inv()
    same(Hi, sp.Matrix([[1, 0, -2], [0, 1, 1], [0, 0, 1]]), "H^{-1}")
    same(Hi * col(2, -1, 1), col(0, 0, 1), "H^{-1} deshace la traslación")
    R = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    same(R * col(1, 0, 1), col(0, 1, 1), "rotación de (1,0)")
    HR = H * R
    same(HR, sp.Matrix([[0, -1, 2], [1, 0, -1], [0, 0, 1]]), "H R")
    same(HR * col(1, 0, 1), col(2, 0, 1), "imagen de (1,0)")
    same(HR * col(3, 2, 1), col(0, 2, 1), "imagen de (3,2)")
    same(R * H, sp.Matrix([[0, -1, 1], [1, 0, 2], [0, 0, 1]]), "R H (otro orden)")
    require(R * H != HR, "no conmutan")
    Hp = sp.Matrix([[1, 0, 1], [0, 1, 1], [0, 0, 1]])
    Hm = sp.Matrix([[1, 0, -1], [0, 1, -1], [0, 0, 1]])
    same(Hp.inv(), Hm, "H(1,1)^{-1} = H(-1,-1)")
    same(R * Hm, sp.Matrix([[0, -1, 1], [1, 0, -1], [0, 0, 1]]), "R H(-1,-1)")
    Q = Hp * R * Hm
    same(Q, sp.Matrix([[0, -1, 2], [1, 0, 0], [0, 0, 1]]), "rotación alrededor de (1,1)")
    same(Q * col(1, 1, 1), col(1, 1, 1), "(1,1) fijo")
    same(Q * col(2, 1, 1), col(1, 2, 1), "imagen de (2,1)")
    same(Q * col(0, 1, 1), col(1, 0, 1), "imagen de (0,1)")
    same(Q * Q * Q * Q, sp.eye(3), "Q^4 = I")
    same(Q.det(), 1, "det Q")
