"""Comprobaciones de los ejercicios originales de la Unidad 1 (Funciones): U1.01, U1.02, ..."""
import sympy as sp
from sympy import Interval, Union, S, oo, Rational as R, FiniteSet, Complement
from sympy.calculus.util import continuous_domain, function_range
from content_pipeline.mathcheck import check, require, same

x, t = sp.symbols("x t", real=True)
LP = "/analisis-matematico-i/unidad-1/teoria/"
L1, L2, L3, L4, L5 = (LP + s + "/" for s in
                      ("funciones-y-modelos", "caracteristicas", "funciones-elementales",
                       "algebra-y-transformaciones", "inversa"))
INTEG = "/analisis-matematico-i/unidad-1/practica/integradores/"


def dom(e, var=None):
    return continuous_domain(e, var or x, S.Reals)


def rng(e, domain, var=None):
    return function_range(e, var or x, domain)


def rcm(f, v, a, b):
    return (f.subs(v, b) - f.subs(v, a)) / (b - a)


# ---------------------------------------------------------------------------
# Funciones y modelos
# ---------------------------------------------------------------------------
@check("U1.01", "Tarifa de alquiler C=150+40h en [0,8]", page=L1)
def _():
    h = sp.Symbol("h")
    C = 150 + 40 * h
    same(C.subs(h, 0), 150, "C(0)")
    same(C.subs(h, 8), 470, "C(8)")
    same(sp.solve(sp.Eq(C, 350), h)[0], 5, "h para 350")
    same(rcm(C, h, 2, 6), 40, "razón media")
    same([C.subs(h, 6), C.subs(h, 2)], [390, 230], "valores")


@check("U1.03", "Corral dividido: A=60x-3/2 x^2, máximo 600", page=L1)
def _():
    y = sp.Symbol("y")
    yv = sp.solve(sp.Eq(3 * x + 2 * y, 120), y)[0]
    same(yv, 60 - R(3, 2) * x, "y(x)")
    A = x * yv
    same(A, 60 * x - R(3, 2) * x ** 2, "A")
    same(sp.solve(sp.diff(A, x), x)[0], 20, "x*")
    same(yv.subs(x, 20), 30, "y*")
    same(A.subs(x, 20), 600, "Amax")
    same(sp.solve(sp.Eq(yv, 0), x)[0], 40, "x máximo")
    same(A.subs(x, 10), 450, "A(10)")
    same(A.subs(x, 30), 450, "A(30)")
    same(rcm(A, x, 10, 30), 0, "razón media")


@check("U1.04", "Usuarios N=C a^t por (2,90),(5,720)", page=L1)
def _():
    a, C = sp.symbols("a C", positive=True)
    sol = sp.solve([sp.Eq(C * a ** 2, 90), sp.Eq(C * a ** 5, 720)], [a, C], dict=True)
    require(sol == [{a: 2, C: R(45, 2)}], f"{sol}")
    N = R(45, 2) * 2 ** t
    same(sp.solve(sp.Eq(N, 5760), t)[0], 8, "t")
    same(N.subs(t, 8), 5760, "N(8)")
    same(rcm(N, t, 2, 5), 210, "[2,5]")
    same(rcm(N, t, 5, 8), 1680, "[5,8]")
    same(R(1680, 210), 8, "cociente")


@check("U1.05", "Noria h=14-12cos(pi t/15)", page=L1)
def _():
    h = 14 - 12 * sp.cos(sp.pi * t / 15)
    same(sp.periodicity(h, t), 30, "período")
    require(rng(h, Interval(0, 30), t) == Interval(2, 26), "imagen")
    sols = sp.solveset(sp.Eq(h, 20), t, Interval(0, 30))
    require(sols == FiniteSet(10, 20), f"h=20: {sols}")
    same([h.subs(t, k) for k in (0, 5, 10, 15)], [2, 8, 20, 26], "valores")
    same([rcm(h, t, a, a + 5) for a in (0, 5, 10)], [R(6, 5), R(12, 5), R(6, 5)], "razones medias")


# ---------------------------------------------------------------------------
# Ceros, signo, paridad y acotación
# ---------------------------------------------------------------------------
def parity(f):
    fm = f.subs(x, -x)
    if sp.simplify(fm - f) == 0:
        return "par"
    if sp.simplify(fm + f) == 0:
        return "impar"
    return "ninguna"


def sgn_sets(f, domain=S.Reals):
    pos = sp.solve_univariate_inequality(f > 0, x, relational=False, domain=domain)
    neg = sp.solve_univariate_inequality(f < 0, x, relational=False, domain=domain)
    return pos, neg


@check("U1.06", "x^3-x^2-6x: ceros y signo", page=L2)
def _():
    p = x ** 3 - x ** 2 - 6 * x
    same(sp.factor(p), x * (x - 3) * (x + 2), "factorización")
    require(set(sp.solve(p, x)) == {-2, 0, 3}, "ceros")
    pos, neg = sgn_sets(p)
    require(pos == Union(Interval.open(-2, 0), Interval.open(3, oo)), "C+")
    require(neg == Union(Interval.open(-oo, -2), Interval.open(0, 3)), "C-")


@check("U1.07", "(x^3-9x)/(x^2-x-6): dominio, ceros, signo", page=L2)
def _():
    f = (x ** 3 - 9 * x) / (x ** 2 - x - 6)
    same(sp.factor(x ** 3 - 9 * x), x * (x - 3) * (x + 3), "numerador")
    same(sp.factor(x ** 2 - x - 6), (x - 3) * (x + 2), "denominador")
    D = dom(f)
    require(D == sp.Complement(S.Reals, FiniteSet(-2, 3)), "dominio")
    same(sp.cancel(f), x * (x + 3) / (x + 2), "simplificación")
    zeros = [z for z in sp.solve(x ** 3 - 9 * x, x) if D.contains(z) == S.true]
    require(set(zeros) == {-3, 0}, "ceros")
    pos, neg = sgn_sets(f, D)
    require(pos == Union(Interval.open(-3, -2), Interval.open(0, 3), Interval.open(3, oo)), f"C+ {pos}")
    require(neg == Union(Interval.open(-oo, -3), Interval.open(-2, 0)), f"C- {neg}")


@check("U1.08", "Paridad de las cuatro funciones del ejercicio 8", page=L2)
def _():
    require(parity((x ** 5 - x) / (x ** 2 + 1)) == "impar", "a")
    g = sp.log((2 + x) / (2 - x))
    require(sp.solve_univariate_inequality((2 + x) / (2 - x) > 0, x, relational=False) == Interval.open(-2, 2), "dominio b")
    same(sp.simplify(sp.expand_log(g.subs(x, -x) + g, force=True)), 0, "g(-x)+g(x)=0")
    require(parity(sp.exp(x ** 2) + sp.cos(x)) == "par", "c")
    k = sp.sin(x) + sp.cos(x)
    require(parity(k) == "ninguna", "d")
    same(k.subs(x, sp.pi / 4), sp.sqrt(2), "k(pi/4)")
    same(k.subs(x, -sp.pi / 4), 0, "k(-pi/4)")
    same([k.subs(x, sp.pi / 2), k.subs(x, -sp.pi / 2)], [1, -1], "k(±pi/2)")


@check("U1.09", "2x/(x^2+4): |f|<=1/2, imagen, impar", page=L2)
def _():
    f = 2 * x / (x ** 2 + 4)
    require(rng(f, S.Reals) == Interval(-R(1, 2), R(1, 2)), "imagen")
    require(parity(f) == "impar", "impar")
    same([f.subs(x, 2), f.subs(x, -2)], [R(1, 2), -R(1, 2)], "extremos")
    same(sp.expand((x - 2) ** 2), x ** 2 - 4 * x + 4, "(|x|-2)^2 con x>=0")
    y = sp.Symbol("y")
    same(sp.discriminant(y * x ** 2 - 2 * x + 4 * y, x), 4 - 16 * y ** 2, "discriminante")
    require(sp.solve_univariate_inequality(f >= 0, x, relational=False, domain=Interval(0, oo)) == Interval(0, oo), "f>=0 en [0,oo)")
    require(sp.solve_univariate_inequality(f <= 0, x, relational=False, domain=Interval(-oo, 0)) == Interval(-oo, 0), "f<=0 en (-oo,0]")


# ---------------------------------------------------------------------------
# Funciones elementales
# ---------------------------------------------------------------------------
@check("U1.10", "Parábola de vértice (2,-3) por (0,5)", page=L3)
def _():
    a = sp.Symbol("a")
    av = sp.solve(sp.Eq(a * (0 - 2) ** 2 - 3, 5), a)[0]
    same(av, 2, "a")
    f = 2 * (x - 2) ** 2 - 3
    same(f, 2 * x ** 2 - 8 * x + 5, "polinómica")
    require(rng(f, S.Reals) == Interval(-3, oo), "imagen")
    zs = sp.solve(f, x)
    require(set(zs) == {2 + sp.sqrt(R(3, 2)), 2 - sp.sqrt(R(3, 2))}, "ceros")
    same(sp.sqrt(R(3, 2)), sp.sqrt(6) / 2, "forma alternativa")
    same(f.subs(x, 0), 5, "ordenada")


@check("U1.11", "Por tramos 2^x-3 (x<=1), 4-x^2 (x>1)", page=L3)
def _():
    t1 = rng(2 ** x - 3, Interval(-oo, 1))
    t2 = rng(4 - x ** 2, Interval.open(1, oo))
    require(t1 == Interval.Lopen(-3, -1), f"imagen tramo 1 {t1}")
    require(t2 == Interval.open(-oo, 3), f"imagen tramo 2 {t2}")
    require(Union(t1, t2) == Interval.open(-oo, 3), "imagen")
    z1 = sp.log(3, 2)
    require(z1 > 1, "log2(3) no cumple x<=1")
    require(abs(float(z1) - 1.585) < 1e-3, "≈1,58")
    require([z for z in sp.solve(4 - x ** 2, x) if z > 1] == [2], "cero del tramo 2")
    same(sp.limit(4 - x ** 2, x, 1, "+"), 3, "límite en 1+")


@check("U1.12", "log2(x+1)+log2(x-3)=5 -> x=7", page=L3)
def _():
    require(set(sp.solve((x + 1) * (x - 3) - 32, x)) == {-5, 7}, "candidatas")
    same(sp.factor(x ** 2 - 2 * x - 35), (x - 7) * (x + 5), "factorización")
    same(sp.log(8, 2) + sp.log(4, 2), 5, "verificación")
    require(7 > 3 and not (-5 > 3), "dominio x>3")


@check("U1.13", "Inversas trigonométricas", page=L3)
def _():
    same(sp.cos(sp.asin(R(3, 5))), R(4, 5), "a1")
    same(sp.tan(sp.acos(-R(1, 3))), -2 * sp.sqrt(2), "a2")
    same(sp.sin(sp.acos(-R(1, 3))), 2 * sp.sqrt(2) / 3, "sen(phi)")
    same(sp.asin(sp.sin(11 * sp.pi / 6)), -sp.pi / 6, "b")
    same(sp.sin(11 * sp.pi / 6), -R(1, 2), "sen(11pi/6)")
    g = sp.pi / 2 - 2 * sp.atan(x)
    require(dom(g) == S.Reals, "dominio")
    require(rng(g, S.Reals) == Interval.open(-sp.pi / 2, 3 * sp.pi / 2), "imagen")


# ---------------------------------------------------------------------------
# Álgebra de funciones y transformaciones
# ---------------------------------------------------------------------------
@check("U1.14", "Dominio de sqrt(2x-6)+1/(x-5)", page=L4)
def _():
    f = sp.sqrt(2 * x - 6) + 1 / (x - 5)
    require(dom(f) == Union(Interval.Ropen(3, 5), Interval.open(5, oo)), "dominio")


@check("U1.15", "Igualdad de funciones: tres pares", page=L4)
def _():
    fa = (x ** 2 - 1) / (x + 1)
    require(dom(fa) == Complement(S.Reals, FiniteSet(-1)) and dom(x - 1) == S.Reals, "a dominios")
    same(sp.cancel(fa), x - 1, "a regla")
    fb = sp.log((x - 1) * (x + 1))
    gb = sp.log(x - 1) + sp.log(x + 1)
    require(dom(fb) == Union(Interval.open(-oo, -1), Interval.open(1, oo)), "b dominio de f")
    require(dom(gb) == Interval.open(1, oo), "b dominio de g")
    same(fb.subs(x, -2), sp.log(3), "f(-2)")
    require(dom(sp.log(x)) == Interval.open(0, oo), "c: e^(ln x) exige ln x, o sea x>0")
    same(sp.simplify(sp.exp(sp.log(sp.Symbol("u", positive=True))) - sp.Symbol("u", positive=True)), 0, "c regla")


@check("U1.16", "Composiciones de ln(x-1) y sqrt(9-x^2)", page=L4)
def _():
    f, g = sp.log(x - 1), sp.sqrt(9 - x ** 2)
    fg, gf = f.subs(x, g), g.subs(x, f)
    require(dom(fg) == Interval.open(-2 * sp.sqrt(2), 2 * sp.sqrt(2)), f"dominio de f∘g {dom(fg)}")
    require(2 * sp.sqrt(2) < 3, "2√2 < 3")
    same(fg.subs(x, 0), sp.log(2), "(f∘g)(0)")
    require(dom(gf) == Interval(1 + sp.exp(-3), 1 + sp.exp(3)), f"dominio de g∘f {dom(gf)}")
    same(gf.subs(x, 2), 3, "(g∘f)(2)")


@check("U1.17", "g=2f(3-x)+1 con f=4x-x^2 en [0,4]", page=L4)
def _():
    f = 4 * x - x ** 2
    g = 2 * f.subs(x, 3 - x) + 1
    same(f.subs(x, 3 - x), (3 - x) * (1 + x), "f(3-x)")
    same(g, -2 * x ** 2 + 4 * x + 7, "fórmula")
    require(rng(f, Interval(0, 4)) == Interval(0, 4), "imagen de f")
    require(rng(g, Interval(-1, 3)) == Interval(1, 9), "imagen de g")
    same([g.subs(x, -1), g.subs(x, 3), g.subs(x, 1)], [1, 1, 9], "valores")
    require(sp.solve_univariate_inequality(g > 0, x, relational=False, domain=Interval(-1, 3)) == Interval(-1, 3), "sin ceros")
    d1 = sp.solve_univariate_inequality(3 - x >= 0, x, relational=False)
    d2 = sp.solve_univariate_inequality(3 - x <= 4, x, relational=False)
    require(d1.intersect(d2) == Interval(-1, 3), "dominio")


# ---------------------------------------------------------------------------
# Biyectividad e inversa
# ---------------------------------------------------------------------------
@check("U1.18", "Taxi T=450+120d en [0,30]", page=L5)
def _():
    d, y = sp.symbols("d y")
    T = 450 + 120 * d
    same([T.subs(d, 0), T.subs(d, 30)], [450, 4050], "extremos")
    same(sp.solve(sp.Eq(T, y), d)[0], (y - 450) / 120, "inversa")
    same(((y - 450) / 120).subs(y, 1350), R(15, 2), "7,5 km")


@check("U1.19", "-x^2+6x-5 restringida a [3,oo)", page=L5)
def _():
    f = -x ** 2 + 6 * x - 5
    same(f, 4 - (x - 3) ** 2, "canónica")
    same([f.subs(x, 2), f.subs(x, 4)], [3, 3], "no inyectiva")
    require(rng(f, Interval(3, oo)) == Interval(-oo, 4), "imagen")
    finv = 3 + sp.sqrt(4 - x)
    same(sp.simplify(f.subs(x, finv)), x, "f(f^-1)")
    require(dom(finv) == Interval(-oo, 4), "dominio de la inversa")


@check("U1.20", "f=(3x-2)/(x-3) es su propia inversa", page=L5)
def _():
    f = (3 * x - 2) / (x - 3)
    same(f, 3 + 7 / (x - 3), "reescritura")
    same(sp.simplify(f.subs(x, f)), x, "f(f(x))=x")
    y = sp.Symbol("y")
    same(sp.solve(sp.Eq(f, y), x)[0], (3 * y - 2) / (y - 3), "despeje")
    require(rng(f, dom(f)) == Complement(S.Reals, FiniteSet(3)), "imagen")
    require(sp.solve(sp.Eq(f, 3), x) == [], "y=3 no se alcanza")


# ---------------------------------------------------------------------------
# Integradores
# ---------------------------------------------------------------------------
@check("U1.22", "Integrador: f=ln(x+3)-2", page=INTEG)
def _():
    f = sp.log(x + 3) - 2
    require(dom(f) == Interval.open(-3, oo), "dominio")
    require(sp.solve(sp.Eq(f, 0), x) == [sp.exp(2) - 3], "cero")
    require(abs(float(sp.exp(2) - 3) - 4.39) < 0.01, "≈4,39")
    pos = sp.solve_univariate_inequality(f > 0, x, relational=False, domain=dom(f))
    neg = sp.solve_univariate_inequality(f < 0, x, relational=False, domain=dom(f))
    require(pos == Interval.open(sp.exp(2) - 3, oo), "C+")
    require(neg == Interval.open(-3, sp.exp(2) - 3), "C-")
    require(sp.limit(f, x, -3, "+") == -oo, "AV")
    finv = sp.exp(x + 2) - 3
    same(sp.simplify(f.subs(x, finv)), x, "f(f^-1)")
    same(sp.simplify(sp.expand_log(finv.subs(x, f), force=True)), x, "f^-1(f)")
    fg = f.subs(x, x ** 2 - 1)
    same(fg, sp.log(x ** 2 + 2) - 2, "f∘g")
    require(dom(fg) == S.Reals, "dominio de f∘g")
    same(fg.subs(x, -x), fg, "par")


@check("U1.23", "Integrador: T=20+60*(1/2)^(t/10)", page=INTEG)
def _():
    T = 20 + 60 * R(1, 2) ** (t / 10)
    same([T.subs(t, 0), T.subs(t, 60)], [80, R(335, 16)], "extremos")
    same(R(335, 16), R(20.9375).limit_denominator(100), "335/16 = 20,9375")
    same(sp.solve(sp.Eq(T, 50), t)[0], 10, "T=50")
    same([T.subs(t, 10), T.subs(t, 20)], [50, 35], "valores")
    same([(T.subs(t, 10) - T.subs(t, 0)) / 10, (T.subs(t, 20) - T.subs(t, 10)) / 10], [-3, -R(3, 2)], "razones")
    Tv = sp.Symbol("Tv")
    tinv = 10 * sp.log(60 / (Tv - 20), 2)
    same(sp.simplify(sp.expand_log(T.subs(t, tinv), force=True)), Tv, "T(t(T))")
    same(tinv.subs(Tv, 50), 10, "t(50)")
    same(tinv.subs(Tv, 80), 0, "t(80)")
    same(sp.simplify(tinv.subs(Tv, R(335, 16))), 60, "t(335/16)")


@check("U1.24", "Integrador opción múltiple: inversa de (x-1)/(x+2) y dominio de ln(x-1)/sqrt(5-x)", page=INTEG)
def _():
    f = (x - 1) / (x + 2)
    finv = (2 * x + 1) / (1 - x)
    same(sp.simplify(f.subs(x, finv)), x, "f(f^-1)")
    same(sp.simplify(finv.subs(x, f)), x, "f^-1(f)")
    require(sp.solve(sp.Eq(f, 1), x) == [], "y=1 no se alcanza")
    require(rng(f, dom(f)) == Complement(S.Reals, FiniteSet(1)), "imagen")
    require(dom(finv) == Complement(S.Reals, FiniteSet(1)), "dominio de la inversa")
    same(((x + 2) / (x - 1)).subs(x, -R(1, 2)), -1, "opción a en -1/2")
    same(f.subs(x, 0), -R(1, 2), "f(0)")
    h = sp.log(x - 1) / sp.sqrt(5 - x)
    require(dom(h) == Interval.open(1, 5), "dominio de h")


@check("U1.25", "Integrador: |x^2-2x-3|", page=INTEG)
def _():
    q = x ** 2 - 2 * x - 3
    f = sp.Abs(q)
    same(sp.factor(q), (x - 3) * (x + 1), "factorización")
    require(set(sp.solve(q, x)) == {-1, 3}, "ceros")
    require(rng(f, S.Reals) == Interval(0, oo), "imagen")
    same(f.subs(x, 1), 4, "máximo local")
    same([f.subs(x, 1), f.subs(x, -1)], [4, 0], "paridad")

    def nsol(k):
        sols = set()
        for expr in (q - k, -q - k):
            for r in sp.solve(expr, x):
                if r.is_real and sp.simplify(f.subs(x, r) - k) == 0:
                    sols.add(sp.nsimplify(r))
        return len(sols)

    same([nsol(0), nsol(1), nsol(3), nsol(4), nsol(5), nsol(10)], [2, 4, 4, 3, 2, 2], "soluciones por k")
    same(nsol(R(-1)), 0, "k<0")
    require(set(sp.solve(q - 1, x) + sp.solve(-q - 1, x)) == {1 + sp.sqrt(5), 1 - sp.sqrt(5), 1 + sp.sqrt(3), 1 - sp.sqrt(3)}, "k=1")
