"""Comprobaciones de los ejemplos resueltos de las lecciones de la Unidad 1 (Funciones).

Cada función recalcula el ejemplo desde sus datos y verifica los pasos intermedios publicados.
"""
import sympy as sp
from sympy import Interval, Union, S, oo, Rational as R, FiniteSet, Complement
from sympy.calculus.util import continuous_domain, function_range
from content_pipeline.mathcheck import check, require, same

x, t = sp.symbols("x t", real=True)
BASE = "/analisis-matematico-i/unidad-1/teoria/"
P1, P2, P3, P4, P5 = (BASE + s + "/" for s in
                      ("funciones-y-modelos", "caracteristicas", "funciones-elementales",
                       "algebra-y-transformaciones", "inversa"))


def dom(e, var=None):
    return continuous_domain(e, var or x, S.Reals)


def rng(e, domain, var=None):
    return function_range(e, var or x, domain)


def sign_sets(f, domain=S.Reals):
    pos = sp.solve_univariate_inequality(f > 0, x, relational=False, domain=domain)
    neg = sp.solve_univariate_inequality(f < 0, x, relational=False, domain=domain)
    return pos, neg


def rcm(f, v, a, b):
    return (f.subs(v, b) - f.subs(v, a)) / (b - a)


# ---------------------------------------------------------------------------
# Funciones y modelos
# ---------------------------------------------------------------------------
@check("U1.T.FUN.1", "Imagen de x^2-4x+7 en [0,5]", page=P1)
def _():
    g = x ** 2 - 4 * x + 7
    same(-R(-4, 2), 2, "x vértice")
    same(g.subs(x, 2), 3, "g(2)")
    same(g.subs(x, 0), 7, "g(0)")
    same(g.subs(x, 5), 12, "g(5)")
    require(rng(g, Interval(0, 5)) == Interval(3, 12), "imagen en [0,5]")
    require(rng(g, S.Reals) == Interval(3, oo), "imagen en R")


@check("U1.T.FUN.2", "Tabla (0,5),(1,11),(3,23): T=6t+5; sensor hasta 41 grados en t=6", page=P1)
def _():
    same(R(11 - 5, 1 - 0), 6, "incremento 1")
    same(R(23 - 11, 3 - 1), 6, "incremento 2")
    T = 6 * t + 5
    same(T.subs(t, 0), 5, "T(0)")
    same(T.subs(t, 1), 11, "T(1)")
    same(T.subs(t, 3), 23, "T(3)")
    same(sp.solve(sp.Eq(T, 41), t)[0], 6, "t para 41")


@check("U1.T.FUN.3", "Pelota h=20t-5t^2: dominio [0,4], imagen [0,20]", page=P1)
def _():
    h = 20 * t - 5 * t ** 2
    same(h, 5 * t * (4 - t), "factorización")
    require(sp.solve_univariate_inequality(h >= 0, t, relational=False) == Interval(0, 4), "h>=0")
    same(h.subs(t, 2), 20, "h(2)")
    same(h.subs(t, 0), 0, "h(0)")
    same(h.subs(t, 4), 0, "h(4)")
    require(rng(h, Interval(0, 4), t) == Interval(0, 20), "imagen")


@check("U1.T.MOD.1", "Tanque V=80+12t, se llena a los 130/3 min; razón media 12", page=P1)
def _():
    V = 80 + 12 * t
    same(sp.solve(sp.Eq(V, 600), t)[0], R(130, 3), "t llenado")
    require(abs(float(R(130, 3)) - 43.3) < 0.05, "≈43,3")
    same(V.subs(t, 5), 140, "V(5)")
    same(V.subs(t, 7), 164, "V(7)")
    same(rcm(V, t, 5, 7), 12, "razón media")


@check("U1.T.MOD.2", "Corral junto a la pared: A=40x-2x^2, máximo 200 en x=10", page=P1)
def _():
    A = x * (40 - 2 * x)
    same(A, 40 * x - 2 * x ** 2, "A")
    same(sp.solve(sp.diff(A, x), x)[0], 10, "x vértice")
    same(A.subs(x, 10), 200, "A(10)")
    require(rng(A, Interval.open(0, 20)) == Interval.Lopen(0, 200), "imagen (0,200]")


@check("U1.T.MOD.3", "Bacterias: N=200*2^t por (0,200),(4,3200); N=10000 en log2(50)", page=P1)
def _():
    a, C = sp.symbols("a C", positive=True)
    sol = sp.solve([sp.Eq(C, 200), sp.Eq(C * a ** 4, 3200)], [a, C], dict=True)
    require(sol == [{a: 2, C: 200}], f"{sol}")
    N = 200 * 2 ** t
    same(N.subs(t, 4), 3200, "N(4)")
    tt = sp.log(50, 2)
    same(N.subs(t, tt), 10000, "N=10000")
    require(abs(float(tt) - 5.64) < 0.005, "≈5,64")


@check("U1.T.MOD.4", "Razones medias de N=200*2^t en [0,1],[1,2],[2,3]; cociente N(t+1)/N(t)=2", page=P1)
def _():
    N = 200 * 2 ** t
    same([rcm(N, t, k, k + 1) for k in (0, 1, 2)], [200, 400, 800], "razones")
    same([N.subs(t, k) for k in (0, 1, 2, 3)], [200, 400, 800, 1600], "valores")
    same(sp.simplify(N.subs(t, t + 1) / N), 2, "cociente")


@check("U1.T.MOD.5", "Razón media de h=20t-5t^2 en [1,4], [0,2], [2,4], [1,3]", page=P1)
def _():
    h = 20 * t - 5 * t ** 2
    same(rcm(h, t, 1, 4), -5, "[1,4]")
    same(h.subs(t, 1), 15, "h(1)")
    same(rcm(h, t, 0, 2), 10, "[0,2]")
    same(rcm(h, t, 2, 4), -10, "[2,4]")
    same(rcm(h, t, 1, 3), 0, "[1,3]")


@check("U1.T.MOD.6", "Rueda: h=10-8cos(pi t/12), imagen [2,18]", page=P1)
def _():
    h = 10 - 8 * sp.cos(sp.pi * t / 12)
    same(h.subs(t, 0), 2, "h(0)")
    same(h.subs(t, 12), 18, "h(12)")
    same(h.subs(t, 6), 10, "h(6)")
    same(sp.periodicity(h, t), 24, "período")
    require(rng(h, Interval(0, 24), t) == Interval(2, 18), "imagen")


# ---------------------------------------------------------------------------
# Ceros, signo, paridad y acotación
# ---------------------------------------------------------------------------
def parity(f, var=None):
    v = var or x
    fm = f.subs(v, -v)
    if sp.simplify(fm - f) == 0:
        return "par"
    if sp.simplify(fm + f) == 0:
        return "impar"
    return "ninguna"


def U(*a):
    return Union(*a)


@check("U1.T.ZER.1", "p=(x+2)(x-1)^2(x-3): ceros y signo", page=P2)
def _():
    p = (x + 2) * (x - 1) ** 2 * (x - 3)
    require(set(sp.solve(p, x)) == {-2, 1, 3}, "ceros")
    pos, neg = sign_sets(p)
    require(pos == U(Interval.open(-oo, -2), Interval.open(3, oo)), f"C+ {pos}")
    require(neg == U(Interval.open(-2, 1), Interval.open(1, 3)), f"C- {neg}")
    for pt, sg in [(-3, 1), (0, -1), (2, -1), (4, 1)]:
        require(sp.sign(p.subs(x, pt)) == sg, f"signo en {pt}")


@check("U1.T.ZER.2", "r=(x^2-4)/(x^2-x-6): dominio, ceros y signo", page=P2)
def _():
    r = (x ** 2 - 4) / (x ** 2 - x - 6)
    same(sp.factor(x ** 2 - x - 6), (x - 3) * (x + 2), "denominador")
    require(dom(r) == Complement(S.Reals, FiniteSet(-2, 3)), "dominio")
    cand = sp.solve(x ** 2 - 4, x)
    require(set(cand) == {-2, 2}, "candidatos")
    zeros = [c for c in cand if dom(r).contains(c) == S.true]
    require(zeros == [2], "ceros")
    same(sp.cancel(r), (x - 2) / (x - 3), "simplificación")
    pos, neg = sign_sets(r, dom(r))
    require(pos == U(Interval.open(-oo, -2), Interval.open(-2, 2), Interval.open(3, oo)), f"C+ {pos}")
    require(neg == Interval.open(2, 3), f"C- {neg}")


@check("U1.T.ZER.3", "Función por tramos: ceros {1,4}, signo y salto en x=2", page=P2)
def _():
    f1, f2 = x ** 2 - 4 * x + 3, 8 - 2 * x
    z1 = [z for z in sp.solve(f1, x) if z < 2]
    z2 = [z for z in sp.solve(f2, x) if z >= 2]
    require(z1 == [1] and z2 == [4], "ceros por tramo")
    require(set(sp.solve(f1, x)) == {1, 3}, "candidatos del tramo 1")
    p1 = sp.solve_univariate_inequality(f1 > 0, x, relational=False, domain=Interval.open(-oo, 2))
    n1 = sp.solve_univariate_inequality(f1 < 0, x, relational=False, domain=Interval.open(-oo, 2))
    p2 = sp.solve_univariate_inequality(f2 > 0, x, relational=False, domain=Interval(2, oo))
    n2 = sp.solve_univariate_inequality(f2 < 0, x, relational=False, domain=Interval(2, oo))
    require(U(p1, p2) == U(Interval.open(-oo, 1), Interval.Ropen(2, 4)), "C+")
    require(U(n1, n2) == U(Interval.open(1, 2), Interval.open(4, oo)), "C-")
    same(f2.subs(x, 2), 4, "f(2)")
    same(sp.limit(f1, x, 2, "-"), -1, "límite por izquierda")


@check("U1.T.PAR.1", "Paridad de x^4-3x^2+1, x^3-4x, x^2+x, 1/(x-1)", page=P2)
def _():
    require(parity(x ** 4 - 3 * x ** 2 + 1) == "par", "a")
    require(parity(x ** 3 - 4 * x) == "impar", "b")
    h = x ** 2 + x
    require(parity(h) == "ninguna", "c")
    same([h.subs(x, 1), h.subs(x, -1)], [2, 0], "valores")
    k = 1 / (x - 1)
    require(dom(k).contains(-1) == S.true and dom(k).contains(1) == S.false, "dominio no simétrico")


@check("U1.T.PAR.2", "Paridad de (x^2+1)x^3 y sen(x)/x", page=P2)
def _():
    m = (x ** 2 + 1) * x ** 3
    require(parity(m) == "impar", "m")
    n = sp.sin(x) / x
    require(parity(n) == "par", "n")
    require(dom(n).contains(0) == S.false, "0 fuera del dominio")


@check("U1.T.PAR.3", "Descomposición par/impar de x^3+2x^2-x+5", page=P2)
def _():
    f = x ** 3 + 2 * x ** 2 - x + 5
    same(f.subs(x, -x), -x ** 3 + 2 * x ** 2 + x + 5, "f(-x)")
    fp = (f + f.subs(x, -x)) / 2
    fi = (f - f.subs(x, -x)) / 2
    same(fp, 2 * x ** 2 + 5, "parte par")
    same(fi, x ** 3 - x, "parte impar")
    require(parity(fp) == "par" and parity(fi) == "impar", "paridades")
    same(fp + fi, f, "suma")
    same((f + f.subs(x, -x)), 4 * x ** 2 + 10, "numerador")
    same((f - f.subs(x, -x)), 2 * x ** 3 - 2 * x, "numerador impar")


@check("U1.T.ACO.1", "x/(1+x^2): |f|<=1/2, imagen [-1/2,1/2]", page=P2)
def _():
    f = x / (1 + x ** 2)
    same(sp.expand((1 - x) ** 2), 1 - 2 * x + x ** 2, "(1-x)^2")
    require(rng(f, S.Reals) == Interval(-R(1, 2), R(1, 2)), "imagen")
    same([f.subs(x, 1), f.subs(x, -1)], [R(1, 2), -R(1, 2)], "se alcanzan")
    y = sp.Symbol("y")
    disc = sp.discriminant(y * x ** 2 - x + y, x)
    same(disc, 1 - 4 * y ** 2, "discriminante")


@check("U1.T.ACO.2", "x^2+3 acotada inferiormente, no superiormente", page=P2)
def _():
    g = x ** 2 + 3
    M = sp.Symbol("M", positive=True)
    same(g.subs(x, sp.sqrt(M)), M + 3, "g(sqrt M)")
    require(rng(g, S.Reals) == Interval(3, oo), "imagen")
    require(sp.simplify(g.subs(x, sp.sqrt(M)) - M) == 3, "supera a M")


@check("U1.T.ACO.3", "1/x en (0,1]: sin cota superior; en [1,oo) acotada por 1", page=P2)
def _():
    M = sp.Symbol("M", positive=True)
    x0 = 1 / (M + 1)
    same(1 / x0, M + 1, "h(x0)")
    require(0 < x0.subs(M, 5) <= 1, "x0 en (0,1]")
    require(rng(1 / x, Interval(1, oo)) == Interval.Lopen(0, 1), "imagen en [1,oo)")
    require(rng(1 / x, Interval.Lopen(0, 1)) == Interval(1, oo), "imagen en (0,1]")


# ---------------------------------------------------------------------------
# Funciones elementales
# ---------------------------------------------------------------------------
@check("U1.T.ELE.1", "Parábola 2x^2-12x+10: forma canónica, ceros, signo", page=P3)
def _():
    f = 2 * x ** 2 - 12 * x + 10
    same(f, 2 * (x - 3) ** 2 - 8, "canónica")
    same(f, 2 * (x - 1) * (x - 5), "factorizada")
    require(set(sp.solve(f, x)) == {1, 5}, "ceros")
    same(f.subs(x, 3), -8, "vértice")
    require(rng(f, S.Reals) == Interval(-8, oo), "imagen")
    same(f.subs(x, 0), 10, "ordenada")
    pos = sp.solve_univariate_inequality(f > 0, x, relational=False)
    neg = sp.solve_univariate_inequality(f < 0, x, relational=False)
    require(pos == Union(Interval.open(-oo, 1), Interval.open(5, oo)), "C+")
    require(neg == Interval.open(1, 5), "C-")


@check("U1.T.ELE.2", "Homográfica (3x-1)/(x+2) = 3 - 7/(x+2)", page=P3)
def _():
    h = (3 * x - 1) / (x + 2)
    same(h, 3 - 7 / (x + 2), "división")
    a, b, c_, d = 3, -1, 1, 2
    same(R(a, c_) + R(b * c_ - a * d, c_ ** 2) / (x + R(d, c_)), h, "fórmula general")
    require(dom(h) == Complement(S.Reals, FiniteSet(-2)), "dominio")
    same(sp.limit(h, x, oo), 3, "AH en +oo")
    same(sp.limit(h, x, -oo), 3, "AH en -oo")
    require(sp.limit(h, x, -2, "+") == -oo and sp.limit(h, x, -2, "-") == oo, "AV")
    require(sp.solve(sp.Eq(h, 3), x) == [], "y=3 no se alcanza")
    require(rng(h, dom(h)) == Complement(S.Reals, FiniteSet(3)), "imagen")
    require(sp.solve(h, x) == [R(1, 3)], "cero")
    same(h.subs(x, 0), -R(1, 2), "ordenada")
    pos = sp.solve_univariate_inequality(h > 0, x, relational=False)
    require(pos == Union(Interval.open(-oo, -2), Interval.open(R(1, 3), oo)), "C+")


@check("U1.T.ELE.3", "sqrt(6-2x)+1: dominio (-oo,3], imagen [1,oo), sin ceros", page=P3)
def _():
    f = sp.sqrt(6 - 2 * x) + 1
    require(dom(f) == Interval(-oo, 3), "dominio")
    require(rng(f, Interval(-oo, 3)) == Interval(1, oo), "imagen")
    same(f.subs(x, 3), 1, "f(3)")
    require(sp.solve(sp.Eq(f, 0), x) == [], "sin ceros")


@check("U1.T.ELE.4", "|2x-6| por tramos, |2x-6|=4 -> x=1,5", page=P3)
def _():
    g = sp.Abs(2 * x - 6)
    same(g.subs(x, 4), 2, "tramo x>=3: 2x-6")
    same(g.subs(x, 0), 6, "tramo x<3: 6-2x")
    same(g, 2 * sp.Abs(x - 3), "2|x-3|")
    require(sp.solve(sp.Eq(2 * x - 6, 4), x) == [5], "rama +")
    require(sp.solve(sp.Eq(6 - 2 * x, 4), x) == [1], "rama -")
    require(set(sp.solve(sp.Eq(g, 4), x)) == {1, 5}, "solve")
    require(rng(g, S.Reals) == Interval(0, oo), "imagen")


@check("U1.T.ELE.5", "2^(x+1)=20 y ln(x-1)+ln(x+1)=ln 8", page=P3)
def _():
    xa = sp.log(20, 2) - 1
    same(2 ** (xa + 1), 20, "a")
    require(abs(float(xa) - 3.3219) < 1e-3, "≈3,32")
    require(set(sp.solve(x ** 2 - 1 - 8, x)) == {-3, 3}, "candidatas")
    same(sp.log(2) + sp.log(4), sp.log(8), "verificación x=3")
    require(sp.solve_univariate_inequality(x - 1 > 0, x, relational=False) == Interval.open(1, oo), "dominio x>1")
    require(not (sp.Integer(-3) - 1 > 0), "x=-3 fuera del dominio")


@check("U1.T.ELE.6", "2cos(pi x/3)+1: período 6, imagen [-1,3], ceros 2 y 4", page=P3)
def _():
    y = 2 * sp.cos(sp.pi * x / 3) + 1
    same(sp.periodicity(y, x), 6, "período")
    require(rng(y, Interval(0, 6)) == Interval(-1, 3), "imagen")
    require(sp.solveset(sp.Eq(y, 0), x, Interval(0, 6)) == FiniteSet(2, 4), "ceros")
    same([y.subs(x, 0), y.subs(x, 3), y.subs(x, 6)], [3, -1, 3], "extremos")


@check("U1.T.ELE.7", "Valores de arcsen, arccos, arctan y arcsen(sen(7pi/6))", page=P3)
def _():
    same(sp.asin(-R(1, 2)), -sp.pi / 6, "a")
    same(sp.acos(-R(1, 2)), 2 * sp.pi / 3, "b")
    same(sp.atan(1), sp.pi / 4, "c")
    same(sp.sin(7 * sp.pi / 6), -R(1, 2), "sen(7pi/6)")
    same(sp.asin(sp.sin(7 * sp.pi / 6)), -sp.pi / 6, "d")
    require(7 * sp.pi / 6 > sp.pi / 2, "7pi/6 fuera de [-pi/2, pi/2]")


# ---------------------------------------------------------------------------
# Álgebra de funciones y transformaciones
# ---------------------------------------------------------------------------
@check("U1.T.ALG.1", "Igualdad de funciones: dominios y reglas", page=P4)
def _():
    f = (x ** 2 - 9) / (x - 3)
    require(dom(f) == Complement(S.Reals, FiniteSet(3)), "dominio de f")
    same(sp.cancel(f), x + 3, "regla")
    require(dom(x + 3) == S.Reals, "dominio de g")
    same((x + 3).subs(x, 3), 6, "g(3)")
    require(dom(sp.log(x ** 2)) == Complement(S.Reals, FiniteSet(0)), "dominio de ln(x^2)")
    require(dom(2 * sp.log(x)) == Interval.open(0, oo), "dominio de 2 ln x")
    same(sp.log((-1) ** 2), 0, "f(-1)")
    same(sp.simplify(sp.sqrt(x ** 2) - sp.Abs(x)), 0, "sqrt(x^2)=|x|")
    require(sp.sqrt((-2) ** 2) == 2 and sp.Integer(-2) != 2, "h(-2)=-2 != 2")
    require(dom(sp.sqrt(x ** 2)) == S.Reals, "dominio de sqrt(x^2)")


@check("U1.T.ALG.2", "f=sqrt(x+3), g=sqrt(5-x): dominios de f+g, f/g; (f/g)(1)=1", page=P4)
def _():
    f, g = sp.sqrt(x + 3), sp.sqrt(5 - x)
    require(dom(f) == Interval(-3, oo) and dom(g) == Interval(-oo, 5), "dominios")
    require(dom(f + g) == Interval(-3, 5), "f+g")
    require(dom(f * g) == Interval(-3, 5), "f*g")
    require(dom(f / g) == Interval.Ropen(-3, 5), "f/g")
    for v in (-3, -1, 0, 1, 2, 4):
        same((f / g).subs(x, v), sp.sqrt((sp.Integer(v) + 3) / (5 - sp.Integer(v))), f"regla en {v}")
    same((f / g).subs(x, 1), 1, "(f/g)(1)")
    same(g.subs(x, 5), 0, "g(5)=0")


@check("U1.T.ALG.3", "f=sqrt(x), g=x^2-4x: f∘g y g∘f", page=P4)
def _():
    f = sp.sqrt(x)
    g = x ** 2 - 4 * x
    fg, gf = f.subs(x, g), g.subs(x, f)
    require(dom(fg) == Union(Interval(-oo, 0), Interval(4, oo)), "dominio de f∘g")
    require(dom(gf) == Interval(0, oo), "dominio de g∘f")
    same(sp.expand(gf), x - 4 * sp.sqrt(x), "g∘f")
    same(fg.subs(x, 4), 0, "(f∘g)(4)")
    same(gf.subs(x, 4), -4, "(g∘f)(4)")
    require(g.subs(x, 2) < 0, "f∘g no existe en 2")


@check("U1.T.ALG.4", "f=1/(x-1), g=ln x: dominios de f∘g y g∘f", page=P4)
def _():
    f, g = 1 / (x - 1), sp.log(x)
    require(dom(f.subs(x, g)) == Complement(Interval.open(0, oo), FiniteSet(sp.E)), "dominio de f∘g")
    require(dom(g.subs(x, f)) == Interval.open(1, oo), "dominio de g∘f")
    same(sp.log(sp.E) - 1, 0, "ln e = 1")


@check("U1.T.ALG.5", "Tres dominios naturales", page=P4)
def _():
    fa = sp.log(4 - x ** 2) / sp.sqrt(x + 1)
    require(dom(fa) == Interval.open(-1, 2), "a")
    gb = sp.sqrt(x ** 2 - x - 6) + 1 / (x - 4)
    exp_b = Union(Interval(-oo, -2), Interval.Ropen(3, 4), Interval.open(4, oo))
    require(dom(gb) == exp_b, f"b {dom(gb)}")
    hc = sp.asin((2 * x - 1) / 3)
    require(dom(hc) == Interval(-1, 2), "c")
    same(sp.factor(x ** 2 - x - 6), (x - 3) * (x + 2), "factorización de b")


def transform(f, a, b, c, d):
    return a * f.subs(x, b * (x - c)) + d


@check("U1.T.TRA.1", "g=-2 sqrt(x-3)+1: dominio, imagen, cero 13/4", page=P4)
def _():
    g = -2 * sp.sqrt(x - 3) + 1
    same(g, transform(sp.sqrt(x), -2, 1, 3, 1), "forma general")
    require(dom(g) == Interval(3, oo), "dominio")
    require(rng(g, Interval(3, oo)) == Interval(-oo, 1), "imagen")
    same(g.subs(x, 3), 1, "(0,0)->(3,1)")
    require(sp.solve(sp.Eq(g, 0), x) == [R(13, 4)], "cero")


@check("U1.T.TRA.2", "(2x-6)^2 = 4(x-3)^2 y g(x)=f(2x-1)", page=P4)
def _():
    same((2 * x - 6) ** 2, 4 * (x - 3) ** 2, "a")
    same(2 * x - 6, 2 * (x - 3), "interior")
    f = (x - 1) * (x - 3)
    g = f.subs(x, 2 * x - 1)
    same(g, (2 * x - 2) * (2 * x - 4), "b expresión")
    same(g, 4 * (x - 1) * (x - 2), "b factorizada")
    d1 = sp.solve_univariate_inequality(2 * x - 1 >= 0, x, relational=False)
    d2 = sp.solve_univariate_inequality(2 * x - 1 <= 4, x, relational=False)
    require(d1.intersect(d2) == Interval(R(1, 2), R(5, 2)), "dominio")
    require(set(sp.solve(g, x)) == {1, 2}, "ceros")
    for z in (1, 3):
        same(R(1, 2) + R(z, 2), {1: 1, 3: 2}[z], f"c+z/b con z={z}")


@check("U1.T.TRA.3", "3 sen(2x-pi/2)+1: amplitud 3, período pi, imagen [-2,4]", page=P4)
def _():
    g = 3 * sp.sin(2 * x - sp.pi / 2) + 1
    same(g, transform(sp.sin(x), 3, 2, sp.pi / 4, 1), "forma general")
    same(sp.periodicity(g, x), sp.pi, "período")
    require(rng(g, Interval(0, sp.pi)) == Interval(-2, 4), "imagen")
    same(g.subs(x, sp.pi / 2), 4, "máximo")
    same(g.subs(x, 0), -2, "mínimo")


@check("U1.T.TRA.4", "-3*2^(x+1)+5: AH y=5, imagen (-oo,5), g(0)=-1, cero", page=P4)
def _():
    g = -3 * 2 ** (x + 1) + 5
    same(g, transform(2 ** x, -3, 1, -1, 5), "forma general")
    s_ = sp.Symbol("s", positive=True)
    same(sp.limit(-3 * 2 ** (1 - s_) + 5, s_, oo), 5, "AH")
    require(rng(g, S.Reals) == Interval.open(-oo, 5), "imagen")
    same(g.subs(x, 0), -1, "ordenada")
    zx = sp.log(R(5, 3), 2) - 1
    same(g.subs(x, zx), 0, "cero")
    require(abs(float(zx) + 0.263) < 1e-3, "≈-0,263")


# ---------------------------------------------------------------------------
# Funciones biyectivas y función inversa
# ---------------------------------------------------------------------------
@check("U1.T.INV.1", "(2x+1)/(x-3) es inyectiva", page=P5)
def _():
    a, b = sp.symbols("a b")
    f = lambda v: (2 * v + 1) / (v - 3)
    same(sp.expand((2 * a + 1) * (b - 3) - (2 * b + 1) * (a - 3)), 7 * b - 7 * a, "diferencia cruzada")
    same(sp.simplify(f(a) - f(b)), sp.simplify(7 * (b - a) / ((a - 3) * (b - 3))), "f(a)-f(b)")


@check("U1.T.INV.2", "x^2-4x restringida a [2,oo): inversa 2+sqrt(x+4)", page=P5)
def _():
    f = x ** 2 - 4 * x
    same(f.subs(x, 0), f.subs(x, 4), "f(0)=f(4)")
    same(f, (x - 2) ** 2 - 4, "canónica")
    require(rng(f, Interval(2, oo)) == Interval(-4, oo), "imagen")
    finv = 2 + sp.sqrt(x + 4)
    same(sp.simplify(f.subs(x, finv)), x, "f(f^-1)")
    u = sp.Symbol("u", positive=True)
    same(sp.simplify((2 + u) ** 2 - 4 * (2 + u)).subs(u, sp.sqrt(x + 4)), x, "f(2+u)")
    same(2 + sp.sqrt(f.subs(x, 3) + 4), 3, "f^-1(f(3))=3")
    same(sp.simplify(f.subs(x, 2 - sp.sqrt(x + 4))), x, "otra rama")


@check("U1.T.INV.3", "2e^(x-1)+3: inversa 1+ln((x-3)/2)", page=P5)
def _():
    f = 2 * sp.exp(x - 1) + 3
    require(rng(f, S.Reals) == Interval.open(3, oo), "imagen")
    finv = 1 + sp.log((x - 3) / 2)
    same(sp.simplify(f.subs(x, finv)), x, "f(f^-1)")
    require(dom(finv) == Interval.open(3, oo), "dominio de la inversa")
    same(sp.simplify(sp.expand_log(finv.subs(x, f), force=True)), x, "f^-1(f)")


@check("U1.T.INV.4", "(2x+1)/(x-3): inversa (3x+1)/(x-2)", page=P5)
def _():
    f = (2 * x + 1) / (x - 3)
    finv = (3 * x + 1) / (x - 2)
    same(sp.simplify(f.subs(x, finv)), x, "f(f^-1)")
    same(sp.simplify(finv.subs(x, f)), x, "f^-1(f)")
    require(sp.solve(sp.Eq(f, 2), x) == [], "y=2 no se alcanza")
    require(rng(f, dom(f)) == Complement(S.Reals, FiniteSet(2)), "imagen")
    y = sp.Symbol("y")
    same(sp.solve(sp.Eq(f, y), x)[0], (3 * y + 1) / (y - 2), "despeje")
    require(dom(finv) == Complement(S.Reals, FiniteSet(2)), "dominio de la inversa")


@check("U1.T.INV.5", "1-2sen x en [-pi/2,pi/2]: inversa arcsen((1-x)/2)", page=P5)
def _():
    f = 1 - 2 * sp.sin(x)
    same([f.subs(x, -sp.pi / 2), f.subs(x, sp.pi / 2)], [3, -1], "extremos")
    require(rng(f, Interval(-sp.pi / 2, sp.pi / 2)) == Interval(-1, 3), "imagen")
    finv = sp.asin((1 - x) / 2)
    same(sp.simplify(f.subs(x, finv)), x, "f(f^-1)")
    require(dom(finv) == Interval(-1, 3), "dominio")
    for v in (-sp.pi / 3, 0, sp.pi / 4):
        same(finv.subs(x, f.subs(x, v)), v, f"f^-1(f({v}))")


@check("U1.T.INV.6", "(g∘f)^-1 = f^-1∘g^-1 con f=2x+1, g=x^3", page=P5)
def _():
    f, g = 2 * x + 1, x ** 3
    gf = g.subs(x, f)
    same(gf, (2 * x + 1) ** 3, "g∘f")
    inv = (sp.real_root(x, 3) - 1) / 2
    same(sp.simplify(gf.subs(x, inv)), x, "(g∘f)((g∘f)^-1)")
    finv = lambda u: (u - 1) / 2
    ginv = sp.real_root(x, 3)
    same(finv(ginv), inv, "f^-1∘g^-1")


@check("U1.T.INV.7", "f=x^3+x: f(2)=10, f(-1)=-2, creciente", page=P5)
def _():
    f = x ** 3 + x
    same([f.subs(x, 2), f.subs(x, -1)], [10, -2], "valores")
    require(sp.solve_univariate_inequality(sp.diff(f, x) > 0, x, relational=False) == S.Reals, "f' > 0")
