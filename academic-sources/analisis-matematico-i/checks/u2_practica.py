"""Comprobaciones de los ejercicios originales de la Unidad 2 (límite funcional y continuidad).

Cada función recalcula el resultado publicado y los pasos intermedios (factorizaciones, laterales,
valores de parámetros). Límites: ambos laterales y contraste numérico con racionales cerca del punto.
Las potencias con base distinta de e se reescriben como exp(exponente * log(base)) porque sp.limit
devuelve laterales incorrectos para 3**(1/x).
"""
import sympy as sp
from content_pipeline.mathcheck import check, require, same

x, a, b, k, m, t = sp.symbols("x a b k m t", real=True)
oo = sp.oo
R = sp.Rational
T = "/analisis-matematico-i/unidad-2/teoria/"
PG = "/analisis-matematico-i/unidad-2/practica/"
ENT, LAT, INF, LIN, CAL, ASI, CONT = (T + s + "/" for s in (
    "entornos-y-limite", "limites-laterales-y-propiedades", "infinitesimos", "limites-infinitos",
    "calculo-de-limites", "asintotas", "continuidad"))
INTEG = PG + "integradores/"


def igual(p, q, what="valor"):
    require(p == q, f"{what}: {p} ≠ {q}")


def ambos(f, v, p):
    return sp.limit(f, v, p, dir="-"), sp.limit(f, v, p, dir="+")


def bilat(f, v, p):
    i, d = ambos(f, v, p)
    require(i == d, f"laterales distintos en {p}: {i} vs {d}")
    return i


def cerca(f, v, p, esperado, lados=(-1, 1), tol=1e-2):
    for s in lados:
        for n in (4, 6):
            val = sp.N(f.subs(v, p + s * R(1, 10**n)), 30)
            require(abs(val - sp.N(esperado)) < tol, f"{f} en {p}, lado {s}: {val} vs {esperado}")


def pot(base, e):
    return sp.exp(sp.log(base) * e)


def oblicua(f, v, p):
    mm = sp.limit(f / v, v, p)
    if not mm.is_finite:
        return None
    n = sp.limit(f - mm * v, v, p)
    return (mm, n) if n.is_finite else None


@check("U2.01", "Entornos: intervalos, centro y radio, desigualdad con módulo", page=ENT)
def _():
    I = sp.Interval.open
    igual(I(-2 - R(3, 2), -2 + R(3, 2)), I(R(-7, 2), R(-1, 2)), "a")
    same(((R(-5, 2) + R(7, 2)) / 2, (R(7, 2) + R(5, 2)) / 2), (R(1, 2), 3), "b1") if False else None
    same((R(-5, 2) + R(7, 2)) / 2, R(1, 2), "centro b1"); same((R(7, 2) + R(5, 2)) / 2, 3, "radio b1")
    same((-5 + 3) / 2, -1, "centro b2"); same((3 + 5) / 2, 4, "radio b2")
    igual(sp.solve_univariate_inequality(sp.Abs(3 * x + 1) < 5, x, relational=False), I(-2, R(4, 3)), "c")
    same((-2 + R(4, 3)) / 2, R(-1, 3), "centro c"); same((R(4, 3) + 2) / 2, R(5, 3), "radio c")
    igual((4 - R(1, 5), 4 + R(1, 5)), (R(19, 5), R(21, 5)), "d")


@check("U2.02", "delta = eps/2 para lim (5-2x) = -1 en 3", page=ENT)
def _():
    same(sp.simplify(sp.Abs((5 - 2 * x) + 1) - 2 * sp.Abs(x - 3)), 0, "|f-L| = 2|x-3|")
    d = R(2, 100) / 2
    same(d, R(1, 100), "delta")
    same((5 - 2 * (3 + d), 5 - 2 * (3 - d)), (R(-102, 100), R(-98, 100)), "valores en 3±delta")
    same(sp.limit(5 - 2 * x, x, 3), -1, "límite")


@check("U2.05", "Laterales con valor absoluto", page=LAT)
def _():
    f = (x**2 - x - 6) / sp.Abs(x - 3)
    same(sp.factor(x**2 - x - 6), (x - 3) * (x + 2), "factor")
    igual(ambos(f, x, 3), (-5, 5), "a")
    g = sp.Abs(x + 1) / (x**2 - 1)
    igual(ambos(g, x, -1), (R(1, 2), R(-1, 2)), "b")


@check("U2.06", "a=3, b=0: existencia de los límites en -1 y 3", page=LAT)
def _():
    sol = sp.solve([sp.Eq(-a + 4, 1 + b), sp.Eq(9 + b, 12 - 3)], [a, b], dict=True)
    igual(sol, [{a: 3, b: 0}], "parámetros")
    f1, f2, f3 = 3 * x + 4, x**2, 12 - x
    same((sp.limit(f1, x, -1, dir="-"), sp.limit(f2, x, -1, dir="+")), (1, 1), "empalme -1")
    same((sp.limit(f2, x, 3, dir="-"), sp.limit(f3, x, 3, dir="+")), (9, 9), "empalme 3")


@check("U2.07", "Intercalación: infinitésimo por acotada", page=LAT)
def _():
    f = (x - 2) ** 2 * sp.sin(5 / (x - 2))
    same(sp.limit(f, x, 2, dir="+"), 0, "a derecha"); same(sp.limit(f, x, 2, dir="-"), 0, "a izquierda")
    g = sp.sqrt(x) * (3 + sp.cos(1 / x))
    for n in (2, 4, 6):
        v = R(1, 10**n)
        val = sp.N(g.subs(x, v))
        require(2 * sp.sqrt(v) <= val + 1e-12 and val <= 4 * sp.sqrt(v) + 1e-12, "cotas 2√x ≤ g ≤ 4√x")
    same(sp.limit(2 * sp.sqrt(x), x, 0, dir="+"), 0, "cota inferior"); same(sp.limit(4 * sp.sqrt(x), x, 0, dir="+"), 0, "cota superior")


@check("U2.09", "Orden respecto de x de varios infinitésimos", page=INF)
def _():
    same(bilat(3 * x / x, x, 0), 3, "φ1/x")
    same(bilat((x**2 - x**3) / x**2, x, 0), 1, "φ2/x²")
    same(bilat(sp.sin(x**2) / x**2, x, 0), 1, "φ3/x²")
    same(bilat((1 - sp.cos(x)) / x**2, x, 0), R(1, 2), "φ4/x²")
    same(bilat((x**2 - x**3) / sp.sin(x**2), x, 0), 1, "φ2 ~ φ3")
    same(bilat((1 - sp.cos(x)) / (x**2 - x**3), x, 0), R(1, 2), "φ4/φ2")
    same(bilat((x**2 - x**3) / (3 * x), x, 0), 0, "φ2/φ1")


@check("U2.10", "Límites con infinitésimos equivalentes", page=INF)
def _():
    fa = sp.sin(6 * x) / sp.log(1 + 2 * x)
    fb = (1 - sp.cos(4 * x)) / (x * sp.sin(2 * x))
    fc = sp.sin(x**2 - 1) / sp.log(x)
    for f, v, esp in ((fa, 0, 3), (fb, 0, 4), (fc, 1, 2)):
        same(sp.limit(f, x, v, dir="+"), esp, f"{f} derecha"); same(sp.limit(f, x, v, dir="-"), esp, f"{f} izquierda")
        cerca(f, x, v, esp)


@check("U2.11", "lim (tan 2x - sen 2x)/x^3 = 4 (no 0)", page=INF)
def _():
    f = (sp.tan(2 * x) - sp.sin(2 * x)) / x**3
    same(bilat(f, x, 0), 4, "límite"); cerca(f, x, 0, 4)
    same(sp.simplify(sp.tan(2 * x) - sp.sin(2 * x) - sp.sin(2 * x) * (1 - sp.cos(2 * x)) / sp.cos(2 * x)), 0, "factorización")
    same(bilat(sp.tan(2 * x) / x - sp.sin(2 * x) / x, x, 0), 0, "la diferencia de equivalentes sí da 0 pero a orden 1")


@check("U2.12", "Límites infinitos con signo", page=LIN)
def _():
    f = (2 * x + 1) / (x - 3)
    igual((sp.limit(f, x, 3, dir="+"), sp.limit(f, x, 3, dir="-")), (oo, -oo), "a y b")
    same((2 * x + 1).subs(x, 3), 7, "numerador")
    g = (x - 2) / (x - 1) ** 2
    igual(ambos(g, x, 1), (-oo, -oo), "c")


@check("U2.13", "Límites en +oo y -oo", page=LIN)
def _():
    a_ = (4 * x**2 - x + 1) / (2 - x**2)
    same((sp.limit(a_, x, oo), sp.limit(a_, x, -oo)), (-4, -4), "a")
    b_ = (x**3 - 2 * x) / (5 * x**2 + 1)
    igual((sp.limit(b_, x, oo), sp.limit(b_, x, -oo)), (oo, -oo), "b")
    c_ = (pot(3, x) + pot(2, x)) / (pot(3, x) - pot(2, x))
    same((sp.limit(c_, x, oo), sp.limit(c_, x, -oo)), (1, -1), "c")
    d_ = sp.sqrt(x**2 + x) / (2 * x + 1)
    same((sp.limit(d_, x, oo), sp.limit(d_, x, -oo)), (R(1, 2), R(-1, 2)), "d")


@check("U2.15", "Indeterminaciones 0/0", page=CAL)
def _():
    fa = (x**2 + x - 2) / (x**2 + 5 * x + 6)
    same(sp.factor(x**2 + x - 2), (x + 2) * (x - 1), "factor 1"); same(sp.factor(x**2 + 5 * x + 6), (x + 2) * (x + 3), "factor 2")
    same(bilat(fa, x, -2), -3, "a")
    fb = (sp.sqrt(x + 8) - 3) / (x - 1)
    same(sp.simplify(fb - 1 / (sp.sqrt(x + 8) + 3)), 0, "racionalización")
    same(bilat(fb, x, 1), R(1, 6), "b")
    fc = ((x + 3) ** 2 - 9) / x
    same(sp.simplify(fc - (x + 6)), 0, "c simplificación"); same(bilat(fc, x, 0), 6, "c")


@check("U2.16", "∞-∞ con conjugado y cociente de exponenciales", page=CAL)
def _():
    f = sp.sqrt(x**2 + 6 * x) - x
    same(sp.limit(f, x, oo), 3, "a")
    igual(sp.limit(f, x, -oo), oo, "b")
    same(sp.simplify(f - 6 * x / (sp.sqrt(x**2 + 6 * x) + x)), 0, "conjugado")
    g = (pot(2, x + 1) + pot(3, x)) / (pot(3, x + 1) - pot(2, x))
    same((sp.limit(g, x, oo), sp.limit(g, x, -oo)), (R(1, 3), -2), "c")


@check("U2.17", "Forma 1^∞", page=CAL)
def _():
    fa = (2 * x + 1) / (2 * x - 3)
    same(sp.limit(x * (fa - 1), x, oo), 2, "g(f-1) a")
    same(sp.limit(pot(fa, x), x, oo), sp.exp(2), "a")
    same(sp.limit(pot(1 + 3 * x, 2 / x), x, 0, dir="+"), sp.exp(6), "b +")
    same(sp.limit(pot(1 + 3 * x, 2 / x), x, 0, dir="-"), sp.exp(6), "b -")
    same(bilat((sp.cos(2 * x) - 1) / x**2, x, 0), -2, "g(f-1) c")
    same(sp.limit(pot(sp.cos(2 * x), 1 / x**2), x, 0, dir="+"), sp.exp(-2), "c")
    cerca(pot(sp.cos(2 * x), 1 / x**2), x, 0, sp.exp(-2))


@check("U2.18", "Parámetros: a=1, b=2 y k=2", page=CAL)
def _():
    f = sp.sqrt(x**2 + 4 * x + 7) - x
    same(sp.limit(f, x, oo), 2, "a=1 da límite 2")
    same(sp.limit(f - 2, x, oo), 0, "b=2")
    igual(sp.limit(sp.sqrt(x**2 + 4 * x + 7) - 2 * x, x, oo), -oo, "a=2 no sirve")
    g = (sp.sqrt(1 + k * x) - 1) / sp.sin(3 * x)
    same(sp.limit(g, x, 0, dir="+"), k / 6, "límite en función de k")
    igual(sp.solve(sp.Eq(k / 6, R(1, 3)), k), [2], "k")


@check("U2.19", "Asíntotas de (3x^2-2)/(x^2-x-2)", page=ASI)
def _():
    f = (3 * x**2 - 2) / (x**2 - x - 2)
    same(sp.factor(x**2 - x - 2), (x - 2) * (x + 1), "factor")
    same((3 * 4 - 2, 3 * 1 - 2), (10, 1), "numerador en 2 y -1")
    for p in (2, -1):
        igual(sorted([sp.limit(f, x, p, dir="+"), sp.limit(f, x, p, dir="-")], key=str), sorted([oo, -oo], key=str), f"AV {p}")
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (3, 3), "AH")


@check("U2.20", "Asíntotas oblicuas", page=ASI)
def _():
    f = (x**2 + 2 * x - 3) / (x - 2)
    same(sp.apart(f, x), x + 4 + 5 / (x - 2), "división")
    igual((oblicua(f, x, oo), oblicua(f, x, -oo)), ((1, 4), (1, 4)), "AO f")
    g = sp.sqrt(4 * x**2 + 3 * x)
    igual((oblicua(g, x, oo), oblicua(g, x, -oo)), ((2, R(3, 4)), (-2, R(-3, 4))), "AO g")


@check("U2.21", "N(t) = 800/(1+15 e^(-0,4 t))", page=ASI)
def _():
    N = 800 / (1 + 15 * sp.exp(-R(2, 5) * t))
    same(N.subs(t, 0), 50, "N(0)"); same(sp.limit(N, t, oo), 800, "AH")
    sol = sp.solve(sp.Eq(N, 400), t)
    igual(sol, [sp.log(15) / R(2, 5)], "t") if False else same(sol[0], sp.log(15) * R(5, 2), "t")
    require(abs(sp.N(sol[0]) - 6.77) < 0.01, "6,77 meses")


@check("U2.22", "f=(a x^2+3)/(x-b) con AO y=2x+8", page=ASI)
def _():
    f = (a * x**2 + 3) / (x - b)
    same(sp.simplify(f - (a * x + a * b + (a * b**2 + 3) / (x - b))), 0, "división")
    sol = sp.solve([sp.Eq(a, 2), sp.Eq(a * b, 8)], [a, b], dict=True)
    igual(sol, [{a: 2, b: 4}], "parámetros")
    g = f.subs({a: 2, b: 4})
    igual(oblicua(g, x, oo), (2, 8), "AO"); same((2 * 16 + 3), 35, "resto 35")
    igual(sorted([sp.limit(g, x, 4, dir="+"), sp.limit(g, x, 4, dir="-")], key=str), sorted([oo, -oo], key=str), "AV x=4")


@check("U2.23", "Continuidad en 2: evitable, redefinir f(2) = -1", page=CONT)
def _():
    f = (x**2 - 5 * x + 6) / (x - 2)
    same(sp.simplify(f - (x - 3)), 0, "simplificación"); same(bilat(f, x, 2), -1, "límite")
    require(-1 != 3, "f(2)=3 distinto del límite")


@check("U2.24", "Discontinuidades de (x+3)/(x^2+x-6)", page=CONT)
def _():
    f = (x + 3) / (x**2 + x - 6)
    same(sp.factor(x**2 + x - 6), (x + 3) * (x - 2), "factor")
    same(bilat(f, x, -3), R(-1, 5), "evitable en -3")
    igual(ambos(f, x, 2), (-oo, oo), "salto infinito en 2")
    dom = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)
    igual(dom, sp.Union(sp.Interval.open(-oo, -3), sp.Interval.open(-3, 2), sp.Interval.open(2, oo)), "dominio")


@check("U2.25", "k=2, m=1 por continuidad en 0 y en 1", page=CONT)
def _():
    same(sp.limit(sp.sin(4 * x) / (k * x), x, 0, dir="-"), 4 / k, "lateral izquierdo en 0")
    igual(sp.solve(sp.Eq(4 / k, 2), k), [2], "k")
    same(sp.simplify((x**3 - 1) / (x - 1) - (x**2 + x + 1)), 0, "simplificación")
    same(sp.limit((x**3 - 1) / (x - 1), x, 1, dir="+"), 3, "lateral derecho en 1")
    igual(sp.solve(sp.Eq(m + 2, 3), m), [1], "m")


@check("U2.26", "x^3-3x+1: cambios de signo y bisección", page=CONT)
def _():
    f = lambda v: v**3 - 3 * v + 1
    same([f(v) for v in (-2, -1, 0, 1, 2)], [-1, 3, 1, -1, 3], "valores")
    same(f(R(3, 2)), R(-1, 8), "f(1,5)"); same(f(R(7, 4)), R(71, 64), "f(1,75)")
    r = sp.Poly(x**3 - 3 * x + 1).nroots()
    require(sum(1 for z in r if abs(sp.im(z)) < 1e-12) == 3, "tres raíces reales")
    require(any(1.5 < sp.re(z) < 1.75 for z in r), "raíz en (1,5; 1,75)")


@check("U2.29", "Integrador: a=-5, b=6; evitable en 3, AV x=-2, AH y=1", page=INTEG)
def _():
    f = (x**2 + a * x + b) / (x**2 - x - 6)
    sol = sp.solve([sp.Eq(9 + 3 * a + b, 0), sp.Eq((3 + 3 * 0) * 0 + R(1, 5), R(1, 5))], [a, b]) if False else None
    g = f.subs({a: -5, b: 6})
    same(sp.factor(x**2 - 5 * x + 6), (x - 3) * (x - 2), "numerador")
    same(sp.simplify(g - (x - 2) / (x + 2)), 0, "simplificación")
    same(bilat(g, x, 3), R(1, 5), "límite en 3")
    require((x**2 - 5 * x + 6).subs(x, -2) == 20, "numerador en -2")
    igual(ambos(g, x, -2), (oo, -oo), "AV en -2")
    same((sp.limit(g, x, oo), sp.limit(g, x, -oo)), (1, 1), "AH")
    # unicidad: 9+3a+b=0 y (3+s)/5=1/5 con numerador (x-3)(x+s)
    s_ = sp.symbols("s")
    igual(sp.solve(sp.Eq((3 + s_) / 5, R(1, 5)), s_), [-2], "s")


@check("U2.30", "Integrador con GeoGebra: lim (sqrt(x^2+9)-3)/x^2 = 1/6, AH y=0", page=INTEG)
def _():
    f = (sp.sqrt(x**2 + 9) - 3) / x**2
    same(sp.simplify(f - 1 / (sp.sqrt(x**2 + 9) + 3)), 0, "racionalización")
    same(bilat(f, x, 0), R(1, 6), "límite"); cerca(f, x, 0, R(1, 6))
    require(abs(sp.N(R(1, 6)) - 0.1667) < 1e-4, "valor para GeoGebra 0,1667")
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (0, 0), "AH")


@check("U2.31", "Integrador opción múltiple: lim (x+sen 3x)/(x^2+2x) = 2", page=INTEG)
def _():
    f = (x + sp.sin(3 * x)) / (x**2 + 2 * x)
    same(sp.simplify(f - (1 + sp.sin(3 * x) / x) / (x + 2)), 0, "dividir por x")
    igual(ambos(f, x, 0), (2, 2), "laterales"); cerca(f, x, 0, 2)
    same((1 + 3) / 2, 2, "opción c"); same((1 + 1) / 2, 1, "opción b (error)"); same((1 + 3) / 1, 4, "opción d (error)")


@check("U2.32", "Integrador de continuidad por partes: a=-3/4, b=3/2; salto infinito en -1, salto 2 en 3", page=INTEG)
def _():
    f1, f2, f4 = 1 / (x + 1), sp.sin(3 * x) / (2 * x), (x**2 - 5 * x + 6) / sp.Abs(x - 3)
    same(sp.limit(f2, x, 0, dir="-"), R(3, 2), "0-: sen(3x)/(2x) -> 3/2")
    same(sp.limit(f4, x, 2, dir="+"), 0, "2+: -(x-2) -> 0")
    sol = sp.solve([sp.Eq(b, R(3, 2)), sp.Eq(2 * a + b, 0)], [a, b], dict=True)
    require(sol == [{a: R(-3, 4), b: R(3, 2)}], f"a, b: {sol}")
    igual(sp.limit(f1, x, -1, dir="-"), -oo, "-1-: salto infinito")
    same(sp.limit(f2, x, -1, dir="+"), f2.subs(x, -1), "continua por derecha en -1")
    same(f2.subs(x, -1), sp.sin(3) / 2, "f(-1) = sen 3 / 2")
    same(ambos(f4, x, 3), (-1, 1), "laterales en 3")
    cerca(f4, x, 3, -1, lados=(-1,)); cerca(f4, x, 3, 1, lados=(1,))
    # d) salto en 2 con b = 3/2 y a cualquiera
    same(sp.Abs((a * 2 + R(3, 2)) - 0), sp.Abs(2 * a + R(3, 2)), "salto |2a+3/2|")
    # e) sen(1/(x+1)) por izquierda de -1 oscila: valores 1 y -1 arbitrariamente cerca.
    xs1 = [-1 - 1 / (sp.pi / 2 + 2 * sp.pi * n) for n in (10, 100, 1000)]
    xs2 = [-1 - 1 / (3 * sp.pi / 2 + 2 * sp.pi * n) for n in (10, 100, 1000)]
    g = sp.sin(1 / (x + 1))
    require(all(sp.simplify(g.subs(x, v) + 1) == 0 for v in xs1), "valores -1 cerca de -1 por izquierda")
    require(all(sp.simplify(g.subs(x, v) - 1) == 0 for v in xs2), "valores 1 cerca de -1 por izquierda")
