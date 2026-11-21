"""Comprobaciones de los ejemplos resueltos de la teoría de la Unidad 2 (límite funcional y continuidad).

Cada función recalcula el ejemplo desde sus datos y verifica los pasos publicados. En los límites se
comprueban ambos laterales y, en los delicados, una evaluación numérica con racionales cerca del punto.
Nota: sp.limit con bases distintas de e y exponente 1/x devuelve resultados laterales incorrectos; las
potencias se reescriben como exp(exponente * log(base)).
"""
import sympy as sp
from content_pipeline.mathcheck import check, require, same

x, u, t, k = sp.symbols("x u t k", real=True)
oo = sp.oo
R = sp.Rational
T = "/analisis-matematico-i/unidad-2/teoria/"
P_ENT, P_LAT, P_INF = T + "entornos-y-limite/", T + "limites-laterales-y-propiedades/", T + "infinitesimos/"
P_LIN, P_CAL, P_ASI, P_CONT = T + "limites-infinitos/", T + "calculo-de-limites/", T + "asintotas/", T + "continuidad/"


def igual(a, b, what="valor"):
    require(a == b, f"{what}: {a} ≠ {b}")


def ambos(f, v, a):
    return sp.limit(f, v, a, dir="-"), sp.limit(f, v, a, dir="+")


def bilat(f, v, a):
    i, d = ambos(f, v, a)
    require(i == d, f"laterales distintos en {a}: {i} vs {d}")
    return i


def cerca(f, v, a, esperado, lados=(-1, 1), tol=1e-2):
    for s in lados:
        for n in (4, 6):
            val = sp.N(f.subs(v, a + s * R(1, 10**n)), 30)
            require(abs(val - sp.N(esperado)) < tol, f"{f} en {a}, lado {s}: {val} vs {esperado}")


def pot(base, e):
    return sp.exp(sp.log(base) * e)


# --------------------------------------------------------------- entornos y límite
@check("U2.T.ENT.1", "Entornos y desigualdades con módulo", page=P_ENT)
def _():
    I = sp.Interval.open
    igual(sp.solve_univariate_inequality(sp.Abs(x - 3) < 2, x, relational=False), I(1, 5), "E(3,2)")
    c = sp.Union(I(R(-3, 2), -1), I(-1, R(-1, 2)))
    s = sp.solve_univariate_inequality(sp.Abs(x + 1) < R(1, 2), x, relational=False) - sp.FiniteSet(-1)
    igual(s, c, "E*(-1,1/2)")
    igual(sp.solve_univariate_inequality(sp.Abs(2 * x - 3) < 1, x, relational=False), I(1, 2), "|2x-3|<1")
    igual(sp.solve_univariate_inequality(sp.Abs(x - R(3, 2)) < R(1, 2), x, relational=False), I(1, 2), "E(3/2,1/2)")


@check("U2.T.ENT.2", "Centro y radio de intervalos abiertos", page=P_ENT)
def _():
    for (p, q), (c, r) in {(-4, 6): (1, 5), (R(-5, 2), R(7, 2)): (R(1, 2), 3)}.items():
        same((p + q) / 2, c, "centro"); same((q - p) / 2, r, "radio")


@check("U2.T.LIM.1", "Tabla de (x^2-9)/(x-3) cerca de 3", page=P_ENT)
def _():
    f = lambda v: (v**2 - 9) / (v - 3)
    for v, esp in ((R(29, 10), R(59, 10)), (R(299, 100), R(599, 100)), (R(2999, 1000), R(5999, 1000)),
                   (R(3001, 1000), R(6001, 1000)), (R(301, 100), R(601, 100)), (R(31, 10), R(61, 10))):
        same(f(v), esp, f"f({v})")
    same(bilat((x**2 - 9) / (x - 3), x, 3), 6, "límite")


@check("U2.T.LIM.2", "lim (3x-2)=7 con delta = eps/3", page=P_ENT)
def _():
    e = sp.symbols("e", positive=True)
    same(sp.simplify(sp.Abs((3 * x - 2) - 7) - 3 * sp.Abs(x - 3)), 0, "|f-L| = 3|x-3|")
    d = R(1, 300)
    same(3 * (3 + d) - 2, 7 + R(1, 100), "borde derecho"); same(3 * (3 - d) - 2, 7 - R(1, 100), "borde izquierdo")
    same(sp.limit(3 * x - 2, x, 3), 7, "límite")


@check("U2.T.LIM.3", "lim x^2 = 4 en 2 con delta = min(1, eps/5)", page=P_ENT)
def _():
    for e in (R(1, 2), R(1, 10), R(5), R(100)):
        d = min(1, e / 5)
        # sup de |x^2-4| en (2-d, 2+d) se alcanza (como cota) en los extremos
        sup = max(abs((2 + d) ** 2 - 4), abs((2 - d) ** 2 - 4))
        require(sup <= e, f"eps={e}: sup {sup}")
    same((R(21, 10)) ** 2, R(441, 100), "f(2,1)"); same((R(19, 10)) ** 2, R(361, 100), "f(1,9)")
    same(sp.limit(x**2, x, 2), 4, "límite")


@check("U2.T.LIM.4", "lim (x^2-9)/(x-3) = 6 con delta = eps", page=P_ENT)
def _():
    same(sp.simplify((x**2 - 9) / (x - 3) - (x + 3)), 0, "simplificación")
    same(bilat((x**2 - 9) / (x - 3), x, 3), 6, "límite")


@check("U2.T.LIM.5", "lim sqrt(x)=2 en 4 con delta = min(4, 2 eps)", page=P_ENT)
def _():
    same(sp.simplify(sp.sqrt(x) - 2 - (x - 4) / (sp.sqrt(x) + 2)), 0, "conjugado")
    for e in (R(1, 100), R(1), R(10)):
        d = min(4, 2 * e)
        sup = max(abs(sp.sqrt(4 + d) - 2), abs(sp.sqrt(4 - d) - 2))
        require(sp.N(sup - e) <= 0, f"eps={e}: {sup}")
    same(sp.limit(sp.sqrt(x), x, 4, dir="+"), 2, "límite")


@check("U2.T.LIM.6", "|x|/x no tiene límite en 0", page=P_ENT)
def _():
    igual(ambos(sp.Abs(x) / x, x, 0), (-1, 1), "laterales")
    require(abs(1 - (-1)) == 2, "distancia 2")


# ------------------------------------------------------- laterales y propiedades
@check("U2.T.LAT.1", "(x^2-4)/|x-2| en 2: laterales 4 y -4", page=P_LAT)
def _():
    igual(ambos((x**2 - 4) / sp.Abs(x - 2), x, 2), (-4, 4), "laterales")
    same(sp.simplify((x**2 - 4) / (x - 2) - (x + 2)), 0, "x>2")


@check("U2.T.LAT.2", "Parámetro k para que exista el límite en 2", page=P_LAT)
def _():
    sol = sp.solve(sp.Eq(2 * k + 1, 4 - k), k)
    igual(sol, [1], "k")
    same((2 * k + 1).subs(k, 1), 3, "valor del límite")


@check("U2.T.LAT.3", "lim (3x^2-x)/(sqrt(x)+1) en 4 = 44/3", page=P_LAT)
def _():
    same((3 * x**2 - x).subs(x, 4), 44, "numerador"); same((sp.sqrt(x) + 1).subs(x, 4), 3, "denominador")
    same(bilat((3 * x**2 - x) / (sp.sqrt(x) + 1), x, 4), R(44, 3), "límite")


@check("U2.T.LAT.4", "lim x^2 sen(1/x) = 0 por intercalación", page=P_LAT)
def _():
    f = x**2 * sp.sin(1 / x)
    same(sp.limit(f, x, 0, dir="+"), 0, "derecha"); same(sp.limit(f, x, 0, dir="-"), 0, "izquierda")
    for n in (3, 6):
        v = R(1, 10**n)
        require(abs(sp.N(f.subs(x, v))) <= v**2, "cota")
        require(abs(sp.N(f.subs(x, -v))) <= v**2, "cota")


@check("U2.T.LAT.5", "sen(5x)/x -> 5 y tan(x)/x -> 1", page=P_LAT)
def _():
    same(bilat(sp.sin(5 * x) / x, x, 0), 5, "sen 5x / x")
    same(bilat(sp.tan(x) / x, x, 0), 1, "tan x / x")
    same(bilat(sp.sin(x) / x, x, 0), 1, "sen x / x")
    same(bilat((x - 1) / (x**2 - 1), x, 1), R(1, 2), "(x-1)/(x^2-1) (errores frecuentes)")


# ------------------------------------------------------------------ infinitésimos
@check("U2.T.INF.1", "Infinitésimos en puntos concretos", page=P_INF)
def _():
    same(sp.limit(x - 3, x, 3), 0, "x-3"); same(sp.limit(x**2 - 4, x, 2), 0, "x^2-4 en 2")
    same(sp.limit(x**2 - 4, x, -2), 0, "x^2-4 en -2"); same(sp.limit(sp.sin(sp.pi * x), x, 2), 0, "sen(pi x) en 2")
    require(sp.limit(x**2 + 1, x, 2) != 0, "x^2+1 no es infinitésimo")


@check("U2.T.INF.2", "1-cos x tiene orden 2 y es equivalente a x^2/2", page=P_INF)
def _():
    same(bilat((1 - sp.cos(x)) / x**2, x, 0), R(1, 2), "orden 2")
    same(bilat((1 - sp.cos(x)) / x, x, 0), 0, "orden superior a x")
    same(bilat((1 - sp.cos(x)) / (x**2 / 2), x, 0), 1, "equivalente")


@check("U2.T.INF.3", "x^3+2x^2 es del mismo orden que x^2 y equivalente a 2x^2", page=P_INF)
def _():
    same(bilat((x**3 + 2 * x**2) / x**2, x, 0), 2, "cociente con x^2")
    same(bilat((x**3 + 2 * x**2) / (2 * x**2), x, 0), 1, "cociente con 2x^2")


@check("U2.T.INF.4", "Equivalencias fundamentales (u -> 0)", page=P_INF)
def _():
    for nombre, f in (("sen", sp.sin(u) / u), ("tan", sp.tan(u) / u), ("1-cos", (1 - sp.cos(u)) / (u**2 / 2)),
                      ("ln(1+u)", sp.log(1 + u) / u), ("exp", (sp.exp(u) - 1) / u), ("arcsen", sp.asin(u) / u),
                      ("arctan", sp.atan(u) / u), ("raíz", (sp.sqrt(1 + u) - 1) / (u / 2))):
        same(bilat(f, u, 0), 1, nombre)
    same(sp.simplify(sp.sqrt(1 + u) - 1 - u / (sp.sqrt(1 + u) + 1)), 0, "racionalización")


@check("U2.T.INF.5", "lim (1-cos 3x)/(x tan 2x) = 9/4", page=P_INF)
def _():
    f = (1 - sp.cos(3 * x)) / (x * sp.tan(2 * x))
    same(bilat(f, x, 0), R(9, 4), "límite"); cerca(f, x, 0, R(9, 4))


@check("U2.T.INF.6", "lim (e^{2x}-1)/ln(1+5x) = 2/5", page=P_INF)
def _():
    f = (sp.exp(2 * x) - 1) / sp.log(1 + 5 * x)
    same(sp.limit(f, x, 0, dir="+"), R(2, 5), "derecha"); same(sp.limit(f, x, 0, dir="-"), R(2, 5), "izquierda")
    cerca(f, x, 0, R(2, 5))


@check("U2.T.INF.7", "lim sen(x^2-4)/(x-2) = 4 en 2", page=P_INF)
def _():
    f = sp.sin(x**2 - 4) / (x - 2)
    same(bilat(f, x, 2), 4, "límite"); cerca(f, x, 2, 4)


@check("U2.T.INF.8", "lim (tan x - sen x)/x^3 = 1/2 (no 0)", page=P_INF)
def _():
    f = (sp.tan(x) - sp.sin(x)) / x**3
    same(bilat(f, x, 0), R(1, 2), "límite"); cerca(f, x, 0, R(1, 2))
    same(sp.simplify(sp.tan(x) - sp.sin(x) - sp.sin(x) * (1 - sp.cos(x)) / sp.cos(x)), 0, "factorización")
    require(abs(sp.N(f.subs(x, R(1, 100))) - 0.5000125) < 1e-6, "valor en x=0,01")


# ------------------------------------------------------------- límites infinitos
@check("U2.T.LIN.1", "1/(x-1)^2 -> +oo; delta = 1/sqrt(M)", page=P_LIN)
def _():
    f = 1 / (x - 1) ** 2
    igual(ambos(f, x, 1), (oo, oo), "laterales")
    M = 9
    d = 1 / sp.sqrt(M)
    same(d, R(1, 3), "delta")
    for s in (R(1, 4), R(1, 10), R(-1, 4), R(-1, 100)):
        require(abs(s) < d and f.subs(x, 1 + s) > M, f"f(1+{s}) > M")


@check("U2.T.LIN.2", "(x+3)/(x+1) en -1: laterales -oo y +oo", page=P_LIN)
def _():
    igual(ambos((x + 3) / (x + 1), x, -1), (-oo, oo), "laterales")


@check("U2.T.LIN.3", "lim (2x+1)/(x+3)=2 en el infinito; N = 5/eps", page=P_LIN)
def _():
    f = (2 * x + 1) / (x + 3)
    same(sp.simplify(f - 2 + 5 / (x + 3)), 0, "f-2 = -5/(x+3)")
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (2, 2), "límites")
    require(R(5, 503) < R(1, 100), "N=500")


@check("U2.T.LIN.4", "Cocientes de polinomios en +-oo", page=P_LIN)
def _():
    a = (3 * x**3 - x) / (x**3 + 2)
    b = (x + 1) / (x**2 + 4)
    c = (2 * x**2 + 1) / (x - 3)
    same((sp.limit(a, x, oo), sp.limit(a, x, -oo)), (3, 3), "a")
    same((sp.limit(b, x, oo), sp.limit(b, x, -oo)), (0, 0), "b")
    igual((sp.limit(c, x, oo), sp.limit(c, x, -oo)), (oo, -oo), "c")


@check("U2.T.LIN.5", "sqrt(x^2+1)/x -> 1 en +oo y -1 en -oo", page=P_LIN)
def _():
    f = sp.sqrt(x**2 + 1) / x
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (1, -1), "límites")


@check("U2.T.LIN.6", "(2^x+3)/(3^x-1): 0 en +oo y -3 en -oo", page=P_LIN)
def _():
    f = (pot(2, x) + 3) / (pot(3, x) - 1)
    same(sp.limit(f, x, oo), 0, "+oo"); same(sp.limit(f, x, -oo), -3, "-oo")
    same(sp.limit(((R(2, 3)) ** x + 3 * R(1, 3) ** x) / (1 - R(1, 3) ** x), x, oo), 0, "tras dividir por 3^x")


@check("U2.T.LIN.7", "Jerarquía: ln x/sqrt(x) -> 0 y x e^{-x} -> 0", page=P_LIN)
def _():
    same(sp.limit(sp.log(x) / sp.sqrt(x), x, oo), 0, "ln x / sqrt x")
    same(sp.limit(x * sp.exp(-x), x, oo), 0, "x e^-x")


# ------------------------------------------------------------ cálculo de límites
@check("U2.T.CAL.1", "lim (x^3-27)/(x^2-9) = 9/2 en 3", page=P_CAL)
def _():
    same(sp.factor(x**3 - 27), (x - 3) * (x**2 + 3 * x + 9), "factor num")
    same(sp.simplify((x**3 - 27) / (x**2 - 9) - (x**2 + 3 * x + 9) / (x + 3)), 0, "simplificación")
    same(bilat((x**3 - 27) / (x**2 - 9), x, 3), R(9, 2), "límite")


@check("U2.T.CAL.2", "lim (sqrt(x+5)-3)/(x-4) = 1/6 en 4", page=P_CAL)
def _():
    f = (sp.sqrt(x + 5) - 3) / (x - 4)
    same(sp.simplify(f - 1 / (sp.sqrt(x + 5) + 3)), 0, "racionalización")
    same(bilat(f, x, 4), R(1, 6), "límite"); cerca(f, x, 4, R(1, 6))


@check("U2.T.CAL.3", "sqrt(4x^2+1)/(x+3) -> 2 en +oo y -2 en -oo", page=P_CAL)
def _():
    f = sp.sqrt(4 * x**2 + 1) / (x + 3)
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (2, -2), "límites")


@check("U2.T.CAL.4", "sqrt(x^2+3x)-x: 3/2 en +oo y +oo en -oo", page=P_CAL)
def _():
    f = sp.sqrt(x**2 + 3 * x) - x
    same(sp.limit(f, x, oo), R(3, 2), "+oo")
    igual(sp.limit(f, x, -oo), oo, "-oo")
    same(sp.simplify(f - 3 * x / (sp.sqrt(x**2 + 3 * x) + x)), 0, "conjugado")
    for n in (3, 6):
        v = -R(10) ** n
        require(sp.N(f.subs(x, v)) > 10**n, "valores grandes para x muy negativo")
        require(abs(sp.N(f.subs(x, -v)) - 1.5) < 1e-2, "valores cercanos a 3/2 para x grande")


@check("U2.T.CAL.5", "lim (1/(x-1) - 2/(x^2-1)) = 1/2 en 1", page=P_CAL)
def _():
    f = 1 / (x - 1) - 2 / (x**2 - 1)
    same(sp.simplify(f - 1 / (x + 1)), 0, "simplificación")
    same(bilat(f, x, 1), R(1, 2), "límite")


@check("U2.T.CAL.6", "x sen(3/x) -> 3 y x ln x -> 0", page=P_CAL)
def _():
    same(sp.limit(x * sp.sin(3 / x), x, oo), 3, "+oo"); same(sp.limit(x * sp.sin(3 / x), x, -oo), 3, "-oo")
    same(sp.limit(x * sp.log(x), x, 0, dir="+"), 0, "x ln x")


@check("U2.T.CAL.7", "(1+1/x)^x -> e", page=P_CAL)
def _():
    f = pot(1 + 1 / x, x)
    same(sp.limit(f, x, oo), sp.E, "+oo"); same(sp.limit(f, x, -oo), sp.E, "-oo")
    v = sp.N((1 + R(1, 10**6)) ** (10**6), 15)
    require(abs(v - sp.N(sp.E)) < 2e-6 and abs(v - 2.7182805) < 1e-6, f"valor {v}")


@check("U2.T.CAL.8", "Límites notables: ln(1+u)/u, (e^u-1)/u, (a^u-1)/u", page=P_CAL)
def _():
    same(bilat(sp.log(1 + u) / u, u, 0), 1, "ln")
    same(bilat((sp.exp(u) - 1) / u, u, 0), 1, "exp")
    same(bilat((pot(5, u) - 1) / u, u, 0), sp.log(5), "a=5")


@check("U2.T.CAL.9", "(1+3/x)^(2x) -> e^6", page=P_CAL)
def _():
    same(sp.limit(2 * x * (3 / x), x, oo), 6, "g(f-1)")
    same(sp.limit(pot(1 + 3 / x, 2 * x), x, oo), sp.exp(6), "límite")


@check("U2.T.CAL.10", "((x+1)/(x-1))^x -> e^2 en +-oo", page=P_CAL)
def _():
    same(sp.simplify((x + 1) / (x - 1) - 1 - 2 / (x - 1)), 0, "f-1")
    same((sp.limit(2 * x / (x - 1), x, oo), sp.limit(2 * x / (x - 1), x, -oo)), (2, 2), "g(f-1)")
    f = pot((x + 1) / (x - 1), x)
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (sp.exp(2), sp.exp(2)), "límites")


@check("U2.T.CAL.11", "(cos x)^(1/x^2) -> e^(-1/2) en 0", page=P_CAL)
def _():
    same(bilat((sp.cos(x) - 1) / x**2, x, 0), R(-1, 2), "g(f-1)")
    f = pot(sp.cos(x), 1 / x**2)
    same(sp.limit(f, x, 0, dir="+"), sp.exp(R(-1, 2)), "derecha"); same(sp.limit(f, x, 0, dir="-"), sp.exp(R(-1, 2)), "izquierda")
    cerca(f, x, 0, sp.exp(R(-1, 2)), tol=1e-2)


@check("U2.T.CAL.12", "(1+1/x)^(x^2) -> +oo", page=P_CAL)
def _():
    igual(sp.limit(x**2 * (1 / x), x, oo), oo, "g(f-1)")
    igual(sp.limit(pot(1 + 1 / x, x**2), x, oo), oo, "límite")


@check("U2.T.CAL.13", "x^(1/x) -> 1 en +oo; x^x -> 1 en 0+", page=P_CAL)
def _():
    same(sp.limit(sp.log(x) / x, x, oo), 0, "ln x / x")
    same(sp.limit(pot(x, 1 / x), x, oo), 1, "x^(1/x)")
    same(sp.limit(pot(x, x), x, 0, dir="+"), 1, "x^x")


# ----------------------------------------------------------------------- asíntotas
def oblicua(f, v, p):
    m = sp.limit(f / v, v, p)
    if not m.is_finite:
        return None
    n = sp.limit(f - m * v, v, p)
    return (m, n) if n.is_finite else None


@check("U2.T.ASI.1", "(2x+1)/(x-1): AV x=1 y AH y=2", page=P_ASI)
def _():
    f = (2 * x + 1) / (x - 1)
    igual(ambos(f, x, 1), (-oo, oo), "laterales")
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (2, 2), "AH")


@check("U2.T.ASI.2", "(x^2-1)/(x^2-3x+2): hueco en 1, AV x=2, AH y=1", page=P_ASI)
def _():
    f = (x**2 - 1) / (x**2 - 3 * x + 2)
    same(bilat(f, x, 1), -2, "hueco en 1")
    require(sp.limit(f, x, 2, dir="+") in (oo, -oo) and sp.limit(f, x, 2, dir="-") in (oo, -oo), "AV en 2")
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (1, 1), "AH")


@check("U2.T.ASI.3", "(x^3+2x^2-1)/(x^2+1): AO y=x+2", page=P_ASI)
def _():
    f = (x**3 + 2 * x**2 - 1) / (x**2 + 1)
    same(sp.apart(f, x) - (x + 2 + (-x - 3) / (x**2 + 1)), 0, "división")
    igual((oblicua(f, x, oo), oblicua(f, x, -oo)), ((1, 2), (1, 2)), "AO")


@check("U2.T.ASI.4", "sqrt((x+2)^2+1): AO y=x+2 (+oo) e y=-x-2 (-oo)", page=P_ASI)
def _():
    f = sp.sqrt((x + 2) ** 2 + 1)
    igual((oblicua(f, x, oo), oblicua(f, x, -oo)), ((1, 2), (-1, -2)), "AO")


@check("U2.T.ASI.5", "6e^x/(e^x+2): AH 6 en +oo y 0 en -oo", page=P_ASI)
def _():
    f = 6 * sp.exp(x) / (sp.exp(x) + 2)
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (6, 0), "AH")


@check("U2.T.ASI.6", "sen x/x: AH y=0 y se anula en k*pi", page=P_ASI)
def _():
    same((sp.limit(sp.sin(x) / x, x, oo), sp.limit(sp.sin(x) / x, x, -oo)), (0, 0), "AH")
    for j in (1, 2, 7):
        same(sp.sin(j * sp.pi) / (j * sp.pi), 0, "cruce")


@check("U2.T.ASI.7", "x+sen x no tiene AO; x^2 tampoco", page=P_ASI)
def _():
    same(sp.limit((x + sp.sin(x)) / x, x, oo), 1, "m")
    # f - x = sen x oscila: toma 0 en n*pi y 1 en pi/2+2n*pi
    same(sp.sin(100 * sp.pi), 0, "valor 0"); same(sp.sin(sp.pi / 2 + 200 * sp.pi), 1, "valor 1")
    igual(sp.limit(x**2 / x, x, oo), oo, "m infinita para x^2")


@check("U2.T.ASI.8", "C(t)=12t/(t+3): AH 12, C(3)=6, C<12", page=P_ASI)
def _():
    C = 12 * t / (t + 3)
    same(sp.limit(C, t, oo), 12, "AH"); same(C.subs(t, 3), 6, "mitad")
    same(sp.solve(sp.Eq(C, 6), t), [3], "t")
    same(sp.simplify(12 - C - 36 / (t + 3)), 0, "12 - C = 36/(t+3) > 0 para t >= 0")


# ----------------------------------------------------------------------- continuidad
@check("U2.T.CONT.1", "(x^2-4)/(x-2) con f(2)=k: continua si k=4", page=P_CONT)
def _():
    same(bilat((x**2 - 4) / (x - 2), x, 2), 4, "límite")


@check("U2.T.CONT.2", "sen x/x con g(0)=1 continua; (1-cos x)/x^2 con h(0)=1 no", page=P_CONT)
def _():
    same(bilat(sp.sin(x) / x, x, 0), 1, "g")
    same(bilat((1 - sp.cos(x)) / x**2, x, 0), R(1, 2), "h"); require(R(1, 2) != 1, "h(0)=1 distinto del límite")


@check("U2.T.CONT.3", "sqrt(4-x^2) continua en [-2,2]", page=P_CONT)
def _():
    f = sp.sqrt(4 - x**2)
    same(sp.limit(f, x, 2, dir="-"), f.subs(x, 2), "en 2"); same(sp.limit(f, x, -2, dir="+"), f.subs(x, -2), "en -2")
    same(sp.limit(f, x, 1), f.subs(x, 1), "interior")


@check("U2.T.CONT.4", "Dominio de continuidad de ln(4-x^2)/(x+1)", page=P_CONT)
def _():
    f = sp.log(4 - x**2) / (x + 1)
    dom = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)
    igual(dom, sp.Union(sp.Interval.open(-2, -1), sp.Interval.open(-1, 2)), "dominio")


@check("U2.T.CONT.5", "(x^2-x-2)/(x^2-4): evitable en 2 (3/4), salto infinito en -2", page=P_CONT)
def _():
    f = (x**2 - x - 2) / (x**2 - 4)
    same(bilat(f, x, 2), R(3, 4), "límite en 2")
    igual(ambos(f, x, -2), (oo, -oo), "laterales en -2")
    same(sp.factor(x**2 - x - 2), (x - 2) * (x + 1), "factor")


@check("U2.T.CONT.6", "Salto finito en 3: 7 y 9, salto 2", page=P_CONT)
def _():
    a, b = 2 * x + 1, 12 - x
    same((a.subs(x, 3), b.subs(x, 3)), (7, 9), "laterales")
    same(abs(9 - 7), 2, "salto"); same(b.subs(x, 3), 9, "g(3)")


@check("U2.T.CONT.7", "e^(1/(x-1)) en 1: laterales +oo y 0", page=P_CONT)
def _():
    igual(ambos(sp.exp(1 / (x - 1)), x, 1), (0, oo), "laterales")


@check("U2.T.CONT.8", "Parámetros a=3, b=-1 para continuidad", page=P_CONT)
def _():
    a, b = sp.symbols("a b")
    same(sp.limit((sp.exp(a * x) - 1) / x, x, 0), a, "lateral izquierdo en 0")
    same(sp.limit((x**2 - 1) / (x - 1), x, 1, dir="+"), 2, "lateral derecho en 1")
    sol = sp.solve([sp.Eq(a, 3), sp.Eq(b + 3, 2)], [a, b], dict=True)
    igual(sol, [{a: 3, b: -1}], "solución")


@check("U2.T.CONT.9", "Bolzano para x^3+x-1 en [0,1] y bisección", page=P_CONT)
def _():
    f = lambda v: v**3 + v - 1
    same((f(0), f(1)), (-1, 1), "extremos")
    pasos = [(R(1, 2), R(-3, 8), -1), (R(3, 4), R(11, 64), 1), (R(5, 8), None, -1), (R(11, 16), None, 1)]
    for p, esp, sg in pasos:
        if esp is not None:
            same(f(p), esp, f"f({p})")
        require(sp.sign(f(p)) == sg, f"signo en {p}")
    require(abs(sp.N(f(R(5, 8))) + 0.130859) < 1e-5, "f(0,625)")
    require(abs(sp.N(f(R(11, 16))) - 0.012451) < 1e-5, "f(0,6875)")
    c = sp.nsolve(x**3 + x - 1, x, 0.7)
    require(R(5, 8) < c < R(11, 16), "la raíz está en (0,625; 0,6875)")


@check("U2.T.CONT.10", "cos x = x tiene solución en (0,1)", page=P_CONT)
def _():
    g = sp.cos(x) - x
    same(g.subs(x, 0), 1, "g(0)"); require(g.subs(x, 1) < 0, "g(1)<0")
    require(sp.cos(1) < 1, "cos 1 < 1")


@check("U2.T.CONT.11", "x^2-4x+1 en [0,3]: imagen [-3,1]", page=P_CONT)
def _():
    f = x**2 - 4 * x + 1
    same(sp.expand((x - 2) ** 2 - 3 - f), 0, "completar cuadrados")
    same((f.subs(x, 2), f.subs(x, 0), f.subs(x, 3)), (-3, 1, -2), "valores")
    imagen = sp.calculus.util.function_range(f, x, sp.Interval(0, 3))
    igual(imagen, sp.Interval(-3, 1), "imagen")
