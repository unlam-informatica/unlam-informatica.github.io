"""Auditoría de la práctica de la Unidad 2 (Límite funcional y continuidad).

Cada comprobación recalcula con SymPy el resultado publicado en la página de la práctica y lo contrasta con la
respuesta oficial de la Guía de TP 2026. En los límites se comprueban ambos laterales (dir="+" y dir="-")
y, en los delicados, una evaluación numérica con racionales cerca del punto.
Convención de IDs: U2.A.<página>.<k>.
"""
import sympy as sp
from content_pipeline.mathcheck import check, require, same

x, t, h, z = sp.symbols("x t h z", real=True)
oo = sp.oo
R = sp.Rational
P = "/analisis-matematico-i/unidad-2/practica/"


def ambos(f, v, a):
    """Límites laterales (izquierdo, derecho) de f en a."""
    return sp.limit(f, v, a, dir="-"), sp.limit(f, v, a, dir="+")


def lim_bilat(f, v, a):
    """Límite bilateral: exige que ambos laterales existan, sean iguales y devuelve el valor."""
    izq, der = ambos(f, v, a)
    require(izq == der, f"laterales distintos en {a}: {izq} vs {der}")
    return izq


def igual(actual, expected, what="valor"):
    """Igualdad estructural exacta (para infinitos, tuplas y diccionarios, donde simplify no sirve)."""
    require(actual == expected, f"{what}: {actual} ≠ {expected}")


def numerico(f, v, a, esperado, lado=0, tol=1e-2):
    """Contraste numérico con racionales cerca de a (lado: -1, 0 o +1)."""
    lados = [lado] if lado else [-1, 1]
    for s in lados:
        for k in (4, 6):
            val = sp.N(f.subs(v, a + s * R(1, 10 ** k)), 30)
            require(abs(val - sp.N(esperado)) < tol, f"{f} en {a}{'+' if s > 0 else '-'}: {val} vs {esperado}")


def asintotas_oblicuas(f, v):
    """Pendiente y ordenada de la asíntota oblicua o horizontal en +oo y -oo (None si no hay)."""
    res = {}
    for nombre, p in (("+", oo), ("-", -oo)):
        m = sp.limit(f / v, v, p)
        if m.is_finite:
            b = sp.limit(f - m * v, v, p)
            res[nombre] = (m, b) if b.is_finite else None
        else:
            res[nombre] = None
    return res


# ---------------------------------------------------------------------------
@check("U2.A.E02.a", "Ejercicio 2: límites inmediatos", page=P + "ejercicio-2/")
def _():
    same(lim_bilat(x**2 - 3 * x + 1, x, 2), -1, "2a")
    same(lim_bilat(sp.sqrt((x + 1) / (2 * x + 1)), x, 1), sp.sqrt(6) / 3, "2b")
    same(lim_bilat(((x**2 + 1) / x) ** (2 * x + 1), x, 3), R(10, 3) ** 7, "2c")
    same(lim_bilat(sp.log(sp.Abs(x**2 - 4 * x - 1)), x, 3), 2 * sp.log(2), "2d")
    same(lim_bilat(x * sp.sin(x) + sp.cos(x), x, sp.pi / 2), sp.pi / 2, "2e")


@check("U2.A.E03.a", "Ejercicio 3: funciones por tramos (laterales)", page=P + "ejercicio-3/")
def _():
    g1, g2, g3 = -x + 1, x - 1, 6 - x**2
    same(g1.subs(x, 1), 0, "g izq en 1"); same(g2.subs(x, 1), 0, "g der en 1")
    same(g2.subs(x, 2), 1, "g izq en 2"); same(g3.subs(x, 2), 2, "g der en 2")
    require(g2.subs(x, 2) != g3.subs(x, 2), "salto en 2")
    same(g1.subs(x, R(1, 4)), R(3, 4), "g(1/4)")
    h1, h2, h3 = x**2 - 5, 3 * x + 2, 4 * x**2 + 2 * x
    same(h1.subs(x, -1), -4, "h izq en -1"); same(h2.subs(x, -1), -1, "h der en -1")
    same(h2.subs(x, 1), 5, "h izq en 1"); same(h3.subs(x, 1), 6, "h der en 1")
    same(h3.subs(x, 2), 20, "h(2)")


@check("U2.A.E05.a", "Ejercicio 5: coeficientes a, b", page=P + "ejercicio-5/")
def _():
    a, b = sp.symbols("a b")
    sol = sp.solve([sp.Eq(b * -2, 4 + a * -2), sp.Eq(1 + a, a - b)], [a, b], dict=True)
    require(sol == [{a: 1, b: -1}], f"solución {sol}")


@check("U2.A.E06.a", "Ejercicio 6: f+g=2, f-g=1 => fg=3/4", page=P + "ejercicio-6/")
def _():
    F, G = sp.symbols("F G")
    s = sp.solve([sp.Eq(F + G, 2), sp.Eq(F - G, 1)], [F, G], dict=True)[0]
    same(s[F] * s[G], R(3, 4), "producto")


@check("U2.A.E07.a", "Ejercicio 7: límites con módulo (laterales y valores)", page=P + "ejercicio-7/")
def _():
    f = sp.Abs(x - 1) / (x - 1)
    same(ambos(f, x, 1), (-1, 1), "7a laterales")
    same(sp.limit(f, x, 1, dir="-"), -1, "7b")
    same(sp.limit((x**2 - sp.Abs(x - 1) - 1) / (x - 1), x, 1, dir="-"), 3, "7c")
    same(sp.limit(1 / (x - 1) - 1 / sp.Abs(x - 1), x, 1, dir="+"), 0, "7d")
    same(lim_bilat((sp.Abs(x) - x) / (x - 1), x, 1), 0, "7e")
    same(lim_bilat((x + x**2) / sp.Abs(x), x, -1), 0, "7f")
    same(sp.limit((x + x**2) / sp.Abs(x), x, 0, dir="+"), 1, "7g")


@check("U2.A.E08.a", "Ejercicio 8: indeterminaciones 0/0", page=P + "ejercicio-8/")
def _():
    casos = [
        ((x - 3) / (x**2 - 9), x, 3, R(1, 6)),
        ((x**2 - 5 * x + 6) / (x**2 - 9 * x + 14), x, 2, R(1, 5)),
        ((1 / (3 + h) - R(1, 3)) / h, h, 0, R(-1, 9)),
        ((x - sp.sqrt(3 * x - 2)) / (x**2 - 4), x, 2, R(1, 16)),
        ((t**3 - 8) / (t**5 - 32), t, 2, R(3, 20)),
        ((sp.sqrt(2 * x) - 4) / (64 - x**2), x, 8, R(-1, 64)),
        ((4 * x**2 - x - R(1, 2)) / (1 - 16 * x**4), x, R(1, 2), R(-3, 8)),
        ((2 * x - sp.sqrt(x + 3)) / (sp.sqrt(x) - 1), x, 1, R(7, 2)),
    ]
    for i, (f, v, a, esp) in enumerate(casos):
        same(lim_bilat(f, v, a), esp, f"8{'abcdefgh'[i]}")
        numerico(f, v, a, esp)
    # pasos publicados
    same(sp.factor(x**2 - 5 * x + 6), (x - 2) * (x - 3), "factor num 8b")
    same(sp.factor(x**2 - 9 * x + 14), (x - 2) * (x - 7), "factor den 8b")
    same(sp.simplify(((x - 1) * (x - 2)) / ((x - 2) * (x + 2) * (x + sp.sqrt(3 * x - 2))) -
                     (x - sp.sqrt(3 * x - 2)) / (x**2 - 4)), 0, "racionalización 8d")
    same(sp.simplify((t**3 - 8) / (t**5 - 32) - (t**2 + 2 * t + 4) / (t**4 + 2 * t**3 + 4 * t**2 + 8 * t + 16)), 0, "8e")
    same(sp.simplify((4 * x**2 - x - R(1, 2)) / (1 - 16 * x**4) + R(1, 2) * (4 * x + 1) / ((1 + 2 * x) * (1 + 4 * x**2))), 0, "8g")
    same(sp.simplify((2 * x - sp.sqrt(x + 3)) / (sp.sqrt(x) - 1) -
                     (4 * x + 3) * (sp.sqrt(x) + 1) / (2 * x + sp.sqrt(x + 3))), 0, "8h")


@check("U2.A.E09.a", "Ejercicio 9: caída libre, velocidades medias e instantánea", page=P + "ejercicio-9/")
def _():
    s = lambda tt: R(49, 10) * tt**2
    for I, v in ((R(4), R(343, 10)), (R(31, 10), R(2989, 100)), (R(305, 100), R(29645, 1000)),
                 (R(301, 100), R(29449, 1000)), (R(3001, 1000), R(294049, 10000))):
        same((s(I) - s(3)) / (I - 3), v, f"vm en [3,{I}]")
    same(lim_bilat((R(49, 10) * t**2 - R(441, 10)) / (t - 3), t, 3), R(294, 10), "v(3)")
    same(sp.solve(sp.Eq(R(49, 10) * t**2, 150), t)[1], sp.sqrt(R(1500, 49)), "dominio")
    require(abs(sp.sqrt(R(1500, 49)) - R(553, 100)) < R(1, 100), "5,53 s")


@check("U2.A.E10.a", "Ejercicio 10: a=15, límite -1", page=P + "ejercicio-10/")
def _():
    a = sp.symbols("a")
    sol = sp.solve((3 * x**2 + a * x + a + 3).subs(x, -2), a)
    same(sol, [15], "a")
    f = (3 * x**2 + 15 * x + 18) / (x**2 + x - 2)
    same(lim_bilat(f, x, -2), -1, "límite")
    # para a != 15 el límite es infinito (laterales de signo opuesto)
    g = (3 * x**2 + 14 * x + 17) / (x**2 + x - 2)
    require(sp.limit(g, x, -2, dir="+") in (oo, -oo), "a=14 diverge")


@check("U2.A.E11.a", "Ejercicio 11: valores de a y límites", page=P + "ejercicio-11/")
def _():
    f1 = (x**2 - 1) * (x + 2) / (x**3 - x)
    same(lim_bilat(f1, x, 1), 3, "11a a=1"); same(lim_bilat(f1, x, -1), -1, "11a a=-1")
    f2 = (x**3 + x**2 - 6 * x) / (x**3 - 7 * x + 6)
    same(lim_bilat(f2, x, 2), 2, "11b a=2"); same(lim_bilat(f2, x, -3), R(3, 4), "11b a=-3")
    same(sp.factor(x**3 - 7 * x + 6), (x - 1) * (x - 2) * (x + 3), "factor")
    # en a=0 (raíz solo del denominador de 11a) no es 0/0
    require(sp.limit(f1, x, 0, dir="+") in (oo, -oo), "a=0 diverge")


@check("U2.A.E12.a", "Ejercicio 12: costo marginal", page=P + "ejercicio-12/")
def _():
    C = lambda q: 5000 + 10 * q + R(5, 100) * q**2
    same((C(105) - C(100)) / 5, R(2025, 100), "[100,105]")
    same((C(101) - C(100)) / 1, R(2005, 100), "[100,101]")
    same(sp.limit((C(100 + h) - C(100)) / h, h, 0), 20, "instantánea")


@check("U2.A.E13.a", "Ejercicio 13: gas (Boyle)", page=P + "ejercicio-13/")
def _():
    V = lambda p: 30 / p
    for a, b, v in ((R(57, 10), 6, -0.8772), (R(58, 10), 6, -0.8621), (R(59, 10), 6, -0.8475),
                    (6, R(61, 10), -0.8197), (6, R(62, 10), -0.8065), (6, R(63, 10), -0.7937)):
        require(abs(sp.N((V(b) - V(a)) / (b - a)) - v) < 1e-4, f"rcp [{a},{b}]")
    P_ = sp.symbols("P")
    same(sp.diff(30 / P_, P_).subs(P_, 6), R(-5, 6), "rci")
    same(sp.limit((V(6 + h) - 5) / h, h, 0), R(-5, 6), "límite del cociente")


@check("U2.A.E14.a", "Ejercicio 14: límites trigonométricos", page=P + "ejercicio-14/")
def _():
    a = sp.symbols("a", real=True)
    casos = [
        (sp.sin(4 * x) / (3 * x), 0, R(4, 3)),
        (sp.sin(4 * x) / sp.sin(5 * x), 0, R(4, 5)),
        (sp.sin(3 * x) ** 2 / (4 * x**2), 0, R(9, 4)),
        (x * sp.sin(x) / (1 - sp.cos(x)), 0, 2),
        ((1 - sp.cos(3 * z)) / z**2, 0, R(9, 2)),
        ((2 * sp.sin(x) + 3 * x * sp.cos(x)) / (3 * sp.sin(x) - x * sp.cos(x)), 0, R(5, 2)),
        (sp.sin(x**2 - 10 * x + 21) / (x - 3), 3, -4),
    ]
    for i, (f, p, esp) in enumerate(casos):
        v = z if f.has(z) else x
        same(lim_bilat(f, v, p), esp, f"14 caso {i}")
        numerico(f, v, p, esp)
    same(sp.limit(sp.sin(x - a) / (x - a), x, a), 1, "14f")
    g = (sp.sin(2 * x) / x) ** (sp.tan(3 * x) / x)
    same(sp.limit(g, x, 0, dir="+"), 8, "14g"); numerico(g, x, 0, 8, lado=1)


@check("U2.A.E15.a", "Ejercicio 15: límites inmediatos en el infinito", page=P + "ejercicio-15/")
def _():
    same(sp.limit(3 ** (1 / x), x, oo), 1, "15a")
    same(sp.limit(R(1, 3) ** x, x, oo), 0, "15b")
    same(sp.limit((3 + sp.exp(-x**2)) / (1 / x**2 + 1), x, oo), 3, "15c")
    same(sp.limit((2 + 3 / x - 1 / x**2) / (4 + 1 / x), x, oo), R(1, 2), "15d")
    same(sp.limit((sp.exp(1 / x**2) + sp.exp(-x**2)) / (sp.exp(1 / x**2) + sp.log(1 + 1 / x**2)), x, oo), 1, "15e")
    same(sp.limit(sp.atan(1 + sp.exp(t)), t, -oo), sp.pi / 4, "15f")
    same(sp.limit(sp.sin(x) ** 2 / x**2, x, oo), 0, "15g")
    igual(sp.limit(x**2 - 3 * x + 5, x, oo), oo, "15h")


@check("U2.A.E16.a", "Ejercicio 16: indeterminados en el infinito (a-d, f, g)", page=P + "ejercicio-16/")
def _():
    same(sp.limit((2 * x**2 + x**4 - sp.sqrt(3)) / (3 * x**4 - x + R(1, 2)), x, oo), R(1, 3), "16a")
    igual(sp.limit((x**3 + 4 * x**2 - x + 5) / (2 * x**2 - 8 * x + 1), x, oo), oo, "16b")
    same(sp.limit((2 * x**3 - 5 * x**2 + 1) / (-3 * x**5 - 2 * x**3 + 3), x, oo), 0, "16c")
    base = (2 * x**5 - 3 * x**4 + 1) / (3 * x**5 - 2 * x**3 - 3)
    ex = (6 * x**2 + x - 1) / (3 * x**2 - 2 * x)
    same(sp.limit(base, x, oo), R(2, 3), "16d base"); same(sp.limit(ex, x, oo), 2, "16d exponente")
    same(sp.limit(sp.sqrt(9 * x**2 + 6) / (5 * x - 2), x, oo), R(3, 5), "16f +oo")
    same(sp.limit(sp.sqrt(9 * x**2 + 6) / (5 * x - 2), x, -oo), R(-3, 5), "16f -oo")
    same(sp.limit((x + sp.sin(x)) / (x - sp.cos(x)), x, oo), 1, "16g")


@check("U2.A.E17.a", "Ejercicio 17: límites laterales (potencias con base distinta de e reescritas con exp)", page=P + "ejercicio-17/")
def _():
    # sp.limit(3**(1/x), x, 0, dir="-") devuelve oo (incorrecto: es 0); se reescribe la base como exp(ln(base) * exponente).
    pot = lambda base, e: sp.exp(sp.log(base) * e)
    same(sp.limit(pot(R(1, 3), x), x, 0, dir="+"), 1, "17a"); same(sp.limit(pot(R(1, 3), x), x, 0, dir="-"), 1, "17b")
    igual(sp.limit(pot(3, 1 / x), x, 0, dir="+"), oo, "17c"); same(sp.limit(pot(3, 1 / x), x, 0, dir="-"), 0, "17d")
    same(sp.limit(pot(R(1, 3), 1 / x), x, 0, dir="+"), 0, "17e"); igual(sp.limit(pot(R(1, 3), 1 / x), x, 0, dir="-"), oo, "17f")
    # Contraste numérico con racionales (3**(-10**6) es ínfimo; se compara el logaritmo).
    for k in (3, 6):
        e = R(1, 10 ** k)
        require(sp.N(sp.log(3) * (-1 / e)) < -1000, "17d numérico: 3^(1/x) -> 0 por la izquierda")
        require(sp.N(sp.log(R(1, 3)) * (-1 / e)) > 1000, "17f numérico: (1/3)^(1/x) -> oo por la izquierda")
    igual(sp.limit(sp.log(x - 1), x, 1, dir="+"), -oo, "17g")
    igual(sp.limit(sp.Abs(sp.log(sp.Abs(x + 2))), x, -2, dir="+"), oo, "17h +")
    igual(sp.limit(sp.Abs(sp.log(sp.Abs(x + 2))), x, -2, dir="-"), oo, "17h -")


@check("U2.A.E18.a", "Ejercicio 18: a=-1, b=1", page=P + "ejercicio-18/")
def _():
    a, b = sp.symbols("a b")
    f = (x**2 - 2 * x + 3) / (x - 1)
    same(sp.apart(f, x), x - 1 + 2 / (x - 1), "división")
    same(sp.limit(f - x + 1, x, oo), 0, "con a=-1, b=1 (+oo)")
    same(sp.limit(f - x + 1, x, -oo), 0, "con a=-1, b=1 (-oo)")


@check("U2.A.E19.a", "Ejercicio 19: a=2, b=3, c=0", page=P + "ejercicio-19/")
def _():
    a, b, c = sp.symbols("a b c")
    der = (a - b * x) / x
    same(sp.limit((der + 3).subs({a: 2, b: 3}), x, oo), 0, "+oo")
    sol = sp.solve([sp.Eq(c - 2, (a - 3 * 2) / 2), sp.Eq(a - 1, c + 1)], [a, c], dict=True)
    require(sol == [{a: 2, c: 0}], f"sol {sol}")
    f_izq, f_med, f_der = (1 + 2 * x) / x, 0 - x, (2 - 3 * x) / x
    same(sp.limit(f_med, x, 2, dir="-"), sp.limit(f_der, x, 2, dir="+"), "empalme 2")
    same(sp.limit(f_izq, x, -1, dir="-"), sp.limit(f_med, x, -1, dir="+"), "empalme -1")


@check("U2.A.E20.a", "Ejercicio 20: repaso de técnicas", page=P + "ejercicio-20/")
def _():
    f = (3 * x + 4 * sp.sin(2 * x)) / (x**2 + 5 * sp.sin(x))
    same(lim_bilat(f, x, 0), R(11, 5), "20a"); numerico(f, x, 0, R(11, 5))
    g = (sp.sqrt(x**2 + 1) - x) / (x + 5)
    same(sp.limit(g, x, oo), 0, "20b +oo"); same(sp.limit(g, x, -oo), -2, "20b -oo")
    same(lim_bilat((sp.sqrt(x + 8) - 3) / (x**2 - x), x, 1), R(1, 6), "20c")
    d = (x**2 - 1) / (x - 2) - (x**2 + x - 2) / (x**2 - 2 * x)
    izq, der = ambos(d, x, 2)
    igual((izq, der), (-oo, oo), "20d laterales: el límite bilateral no existe")
    same(sp.factor(x**3 - x**2 - 2 * x + 2), (x - 1) * (x**2 - 2), "20d factor")
    e = sp.sin(x) / x + x * sp.sin(1 / x)
    same(sp.limit(e, x, 0, dir="+"), 1, "20e +"); same(sp.limit(e, x, 0, dir="-"), 1, "20e -")
    f6 = ((x**2 - 4 * x + 3) / (4 * x - 12)) ** (1 / (x - 3))
    same(sp.limit(f6, x, 3, dir="+"), 0, "20f")


@check("U2.A.E21.a", "Ejercicio 21: bacterias", page=P + "ejercicio-21/")
def _():
    P_ = lambda tt: 4 / (2 + 8 * sp.exp(-2 * tt))
    same(P_(0), R(2, 5), "P(0)")
    same(sp.N((P_(3) - P_(1)) / 2, 8) * 10**6 // 1, 341396, "razón media (bacterias/día)")
    same(sp.limit(P_(t), t, oo), 2, "asíntota horizontal")


@check("U2.A.E24.a", "Ejercicio 24: asíntotas (a-j)", page=P + "ejercicio-24/")
def _():
    def av(f):
        """Abscisas de AV: puntos donde algún lateral diverge (entre ceros del denominador)."""
        den = sp.denom(sp.together(f))
        pts = sp.solve(den, x)
        return sorted([p for p in pts if p.is_real and
                       (sp.limit(f, x, p, dir="+") in (oo, -oo) or sp.limit(f, x, p, dir="-") in (oo, -oo))], key=sp.N)
    a = (2 * x**2 - x) / (x**2 - 1)
    same(av(a), [-1, 1], "24a AV"); same(sp.limit(a, x, oo), 2, "24a AH")
    b = 2 * (x - 1) ** 2 / (x + R(1, 2))
    same(av(b), [R(-1, 2)], "24b AV"); igual(asintotas_oblicuas(b, x)["+"], (2, -5), "24b AO")
    c = sp.sqrt(x**2 + 1)
    igual(asintotas_oblicuas(c, x), {"+": (1, 0), "-": (-1, 0)}, "24c")
    d = 3 * x / (x - 1) + 3 * x
    same(av(d), [1], "24d AV"); igual(asintotas_oblicuas(d, x)["+"], (3, 3), "24d AO +")
    igual(asintotas_oblicuas(d, x)["-"], (3, 3), "24d AO -")
    e = sp.sin(x) / x
    same(sp.limit(e, x, oo), 0, "24e"); same(lim_bilat(e, x, 0), 1, "24e en 0")
    f = (x**3 + 1) / (x**3 + x)
    same(av(f), [0], "24f AV"); same(sp.limit(f, x, oo), 1, "24f AH")
    g = 1 / (sp.exp(x) - 1)
    igual(sp.limit(g, x, 0, dir="+"), oo, "24g"); igual(sp.limit(g, x, 0, dir="-"), -oo, "24g")
    same((sp.limit(g, x, oo), sp.limit(g, x, -oo)), (0, -1), "24g AH")
    hh = sp.exp(1 / x)
    igual(sp.limit(hh, x, 0, dir="+"), oo, "24h +"); same(sp.limit(hh, x, 0, dir="-"), 0, "24h -")
    same((sp.limit(hh, x, oo), sp.limit(hh, x, -oo)), (1, 1), "24h AH")
    i = x / (x**4 + 1) ** R(1, 4)
    same((sp.limit(i, x, oo), sp.limit(i, x, -oo)), (1, -1), "24i")
    j = (x**2 - 4 * x) / (x**3 - 2 * x)
    same(av(j), [-sp.sqrt(2), sp.sqrt(2)], "24j AV"); same(sp.limit(j, x, oo), 0, "24j AH")
    same(lim_bilat(j, x, 0), 2, "24j hueco en 0")


@check("U2.A.E25.a", "Ejercicio 25a: a=2, b=16, k=-8 (k es el punto excluido -b/a)", page=P + "ejercicio-25/")
def _():
    a, b = sp.symbols("a b")
    f = (x**2 - 2) / (2 * x + 16)
    igual(asintotas_oblicuas(f, x), {"+": (R(1, 2), -4), "-": (R(1, 2), -4)}, "AO y = x/2 - 4")
    same(sp.solve(2 * x + 16, x), [-8], "k = -b/a = -8")
    same(sp.apart(f, x), x / 2 - 4 + 31 / (x + 8), "división")


@check("U2.A.E25.b", "Ejercicio 25b: a=-2, b=0, c=-1", page=P + "ejercicio-25/")
def _():
    f = (x**3 + x - 2) / (x**2 - 1)
    g = (x**2 + x - 2) / (x + 1)
    igual(asintotas_oblicuas(f, x)["+"], (1, 0), "AO f"); igual(asintotas_oblicuas(g, x)["+"], (1, 0), "AO g")
    igual(sp.limit(f, x, -1, dir="+"), oo, "AV f en -1 (dcha.)"); igual(sp.limit(f, x, -1, dir="-"), -oo, "AV f en -1 (izq.)")
    igual(sp.limit(g, x, -1, dir="+"), -oo, "AV g en -1 (dcha.)")
    same(lim_bilat(f, x, 1), 2, "x=1: límite 2 (f no está definida en 1): discontinuidad evitable")
    same(sp.factor(x**3 + x - 2), (x - 1) * (x**2 + x + 2), "factor")


@check("U2.A.E25.c", "Ejercicio 25c: se corrige b=0 (parábola, sin asíntotas) y se registra el caso b=a^2 (una sola AV)", page=P + "ejercicio-25/")
def _():
    a = sp.symbols("a", real=True, nonzero=True)
    # b = 0: f(x) = -(a x^2 + x) es una parábola: no tiene AO.
    f0 = (a * x**2 + x) / (0 * x**2 - 1)
    igual(sp.limit(((2 * x**2 + x) / (0 * x**2 - 1)) / x, x, oo), -oo, "pendiente infinita: no hay AO")
    # a != 0, b != 0: AH y = a/b en ambos extremos.
    b = sp.symbols("b", positive=True)
    f = (a * x**2 + x) / (b * x**2 - 1)
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (a / b, a / b), "AH a/b")
    # Caso b = a^2: cancela una raíz y queda una sola AV (la respuesta oficial dice que no existe tal b).
    fc = (a * x**2 + x) / (a**2 * x**2 - 1)
    same(sp.simplify(fc - x / (a * x - 1)), 0, "simplificación para b=a^2")
    # Con valores concretos (a=2, b=4): una sola AV en x=1/2.
    f24 = (2 * x**2 + x) / (4 * x**2 - 1)
    require(sp.limit(f24, x, R(1, 2), dir="+") in (oo, -oo), "AV en x=1/2")
    same(lim_bilat(f24, x, R(-1, 2)), R(1, 4), "x=-1/2 es hueco (límite 1/4)")
    # Con a=0 (no permitido por el enunciado) f(x) = x/(b x^2 - 1) y con b=0 f(x) = -x: AO y = -x.
    igual(asintotas_oblicuas(x / (0 * x**2 - 1), x)["+"], (-1, 0), "a=0, b=0")


@check("U2.A.E26.a", "Ejercicio 26: rumor", page=P + "ejercicio-26/")
def _():
    N = 5000 * (1 - 2 ** (-R(1, 100) * t))
    same(sp.limit(N, t, oo), 5000, "población")
    same(sp.solve(sp.Eq(N, 2500), t), [100], "t para la mitad")


@check("U2.A.E28.a", "Ejercicio 28: tipo de discontinuidad", page=P + "ejercicio-28/")
def _():
    f = (x - 1) / (sp.Abs(x) - 1)
    same(lim_bilat(f, x, 1), 1, "28a x=1 evitable")
    igual(ambos(f, x, -1), (-oo, oo), "28a x=-1")
    f = (x**2 - 4) / (x**2 - 5 * x + 6)
    same(lim_bilat(f, x, 2), -4, "28b x=2"); require(sp.limit(f, x, 3, dir="+") in (oo, -oo), "28b x=3")
    f = 4 * x**2 / (3 - sp.sqrt(x**2 + 5))
    for p in (2, -2):
        require(sp.limit(f, x, p, dir="+") in (oo, -oo) and sp.limit(f, x, p, dir="-") in (oo, -oo), f"28c {p}")
    f = sp.sin(2 * x - 10) / sp.Abs(x - 5)
    same(ambos(f, x, 5), (-2, 2), "28d")
    f = 1 / (1 + sp.exp(1 / (1 - x)))
    same(ambos(f, x, 1), (0, 1), "28e")
    same((sp.limit(1 / (3 * x + 1), x, 1, dir="-"), sp.limit(x - R(3, 4), x, 1, dir="+"), 1 - R(3, 4)),
         (R(1, 4), R(1, 4), R(1, 4)), "28f x=1 continua")
    require(sp.limit(1 / (3 * x + 1), x, R(-1, 3), dir="+") in (oo, -oo), "28f x=-1/3")
    igual((sp.limit(sp.log(x - 2), x, 2, dir="+"), 2**3), (-oo, 8), "28g x=2")
    same((sp.Abs(-1), (-1) ** 3), (1, -1), "28g x=-1")
    f = 1 / sp.log(x + 3)
    same(sp.limit(f, x, -3, dir="+"), 0, "28h x=-3 evitable"); require(sp.limit(f, x, -2, dir="+") in (oo, -oo), "28h x=-2")
    f1 = (x**3 + 4 * x**2 - 5 * x) / (x**2 + 3 * x - 10)
    same(lim_bilat(f1, x, -5), R(-30, 7) * -1 if False else R(30, -7), "28i x=-5")
    f2 = 2 / (sp.exp(1 / x) - 2)
    same(sp.solve(sp.exp(1 / x) - 2, x), [1 / sp.log(2)], "28i x=1/ln2")
    same((sp.limit(f1, x, 0, dir="-"), sp.limit(f2, x, 0, dir="+"), f1.subs(x, 0)), (0, 0, 0), "28i x=0 continua")


@check("U2.A.E29.a", "Ejercicio 29: parámetros para continuidad", page=P + "ejercicio-29/")
def _():
    a, b, c = sp.symbols("a b c")
    sol = sp.solve([sp.Eq(-1 + a, 1 + b), sp.Eq(-2 + b, a / 2 - c), sp.Eq(-c, -3)], [a, b, c], dict=True)
    require(sol == [{a: 2, b: 0, c: 3}], f"29a {sol}")
    g_der = (x**2 + x - 6) / (sp.sqrt(x**2 + 5) - 3)
    same(lim_bilat(g_der.subs(x, x), x, 2) if False else sp.limit(g_der, x, 2, dir="+"), R(15, 2), "29b lateral dcho.")
    g_izq = sp.sin(30 * x - 60) / (x**2 - 4)
    same(sp.limit(g_izq, x, 2, dir="-"), R(15, 2), "29b a=30")
    aa, bb, cc, dd = sp.symbols("aa bb cc dd")
    f = (5 * x**2 - 20) / (-5 * x**2 + 15 * x - 10)
    same(sp.limit(f, x, oo), -1, "29c AH")
    same(lim_bilat(f, x, 2), -4, "29c redefinición f(2)=-4")
    require(sp.limit(f, x, 1, dir="+") in (oo, -oo), "29c AV en 1")


@check("U2.A.E31.a", "Ejercicio 31: salto", page=P + "ejercicio-31/")
def _():
    f = (1 - 10 ** (1 / x)) / (1 + 10 ** (1 / x))
    s = sp.limit(f, x, 0, dir="+") - sp.limit(f, x, 0, dir="-")
    same(abs(s), 2, "31a")
    f = sp.sin(5 * x) / (3 * x)
    same(abs(sp.limit(sp.sin(x) / x, x, 0, dir="+") - sp.limit(f, x, 0, dir="-")), R(2, 3), "31b")
    same(abs((5 * 0 + 1) - (0 + 12)), 11, "31c")


@check("U2.A.E32.a", "Ejercicio 32: constantes para continuidad en R", page=P + "ejercicio-32/")
def _():
    a, b = sp.symbols("a b")
    f = (x**2 - a**2) / (x - a)
    same(sp.limit(f, x, a), 2 * a, "32a límite"); same(sp.solve(sp.Eq(2 * a, 8), a), [4], "32a")
    l = sp.limit((1 - sp.cos(a * x)) / (4 * x**2), x, 0, dir="-")
    same(l, a**2 / 8, "32b lateral"); same(sp.solve(sp.Eq(l, 2), a), [-4, 4], "32b")
    same(sp.limit((x**2 + x) / (x**2 - 1), x, -1, dir="-"), R(1, 2), "32c x=-1")
    same(sp.limit(sp.sin(x - 1) / sp.log(x + 1), x, 1, dir="+"), 0, "32c x=1")
    sol = sp.solve([sp.Eq(-a + b, R(1, 2)), sp.Eq(a + b, 0)], [a, b], dict=True)
    require(sol == [{a: R(-1, 4), b: R(1, 4)}], f"32c {sol}")


@check("U2.A.E33.a", "Ejercicio 33: contraejemplos y valores de verdad comprobables", page=P + "ejercicio-33/")
def _():
    same(sp.limit(sp.log(sp.sin(x)) - sp.log(x), x, 0, dir="+"), 0, "33f")
    igual(sp.limit(x**2 - x, x, oo), oo, "33d contraejemplo")
    same(sp.limit(sp.sin(x) / x, x, 0), 1, "33e contraejemplo")
    f = (3 * x**2 + 2 * x + sp.sin(x)) / x
    same(sp.limit(f - 3 * x - 2, x, oo), 0, "33l (+oo)"); same(sp.limit(f - 3 * x - 2, x, -oo), 0, "33l (-oo)")
    # 33h: sen x / x tiene AH y=0 y se anula en x = k pi
    same(sp.sin(sp.pi * 5) / (sp.pi * 5), 0, "33h")
    # 33g: existe f con AV en 1 definida en 1.
    fg = sp.Piecewise((1 / sp.Abs(x - 1), sp.Ne(x, 1)), (0, True))
    igual(sp.limit(1 / sp.Abs(x - 1), x, 1), oo, "33g límite infinito"); same(fg.subs(x, 1), 0, "33g f(1) definida")


@check("U2.A.ADI.1", "Adicionales 1 y 6", page=P + "adicionales/")
def _():
    a = sp.symbols("a", positive=True)
    f = (sp.sqrt(x + 7) - 2) / sp.sin(2 * x + 6)
    same(lim_bilat(f, x, -3), R(1, 8), "1a"); numerico(f, x, -3, R(1, 8))
    g = (1 - sp.cos(x - 1)) / (x**2 - 1)
    same(lim_bilat(g, x, 1), 0, "1b")
    hh = sp.sqrt(x**2 + 5) / (3 * x - 2)
    same((sp.limit(hh, x, oo), sp.limit(hh, x, -oo)), (R(1, 3), R(-1, 3)), "1c")
    L = (x * sp.sqrt(x) - a * sp.sqrt(a)) / (sp.sqrt(x) - sp.sqrt(a))
    same(sp.limit(L, x, a), 3 * a, "6")


@check("U2.A.ADI.3", "Adicional 3: |4-x^2|/(x(x-2))", page=P + "adicionales/")
def _():
    f = sp.Abs(4 - x**2) / (x * (x - 2))
    same(ambos(f, x, 2), (-2, 2), "salto en 2 (S=4)")
    izq, der = ambos(f, x, 0)
    igual((izq, der), (oo, -oo), "AV en 0")
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (1, 1), "AH y=1")
    same(lim_bilat(f, x, -2), 0, "continua en -2")


@check("U2.A.ADI.4", "Adicional 4: a=3/2, b=-9/2 (lectura (x^2+4x-5)/(2x^2-6x+4) para x<1)", page=P + "adicionales/")
def _():
    a, b = sp.symbols("a b")
    izq = sp.limit((x**2 + 4 * x - 5) / (2 * x**2 - 6 * x + 4), x, 1, dir="-")
    same(izq, -3, "límite en 1")
    sol = sp.solve([sp.Eq(a + b, izq), sp.Eq(3 * a + b, 0)], [a, b], dict=True)
    require(sol == [{a: R(3, 2), b: R(-9, 2)}], f"sol {sol}")


@check("U2.A.ADI.2", "Adicional 2: AV según b (dos si b>0 y b!=a^2, una si b=a^2, ninguna si b<=0); a=1, b=4", page=P + "adicionales/")
def _():
    a = sp.symbols("a", real=True, nonzero=True)
    bp = sp.symbols("bp", positive=True)
    num, den = a * x**2 + x, bp * x**2 - 1
    # Las raíces del numerador (0 y -1/a) coinciden con ±1/sqrt(b) solo si b = a^2.
    raices = sp.solve(sp.Eq(den.subs(x, -1 / a), 0), bp)
    same(raices, [a**2], "cancelación solo si b = a^2")
    fc = (a * x**2 + x) / (a**2 * x**2 - 1)
    same(sp.simplify(fc - x / (a * x - 1)), 0, "b = a^2: f = x/(ax-1)")
    same(sp.limit((x**2 + x) / (x**2 - 1), x, -1), R(1, 2), "a=b=1: hueco en -1 con límite 1/(2a)")
    # b < 0: el denominador no se anula.
    bn = sp.symbols("bn", negative=True)
    require(sp.solve(sp.Eq(bn * x**2 - 1, 0), x) == [], "b<0: sin raíces reales")
    f = (x**2 + x) / (4 * x**2 - 1)
    igual(ambos(f, x, R(1, 2)), (-oo, oo), "AV x=1/2")
    igual(ambos(f, x, R(-1, 2)), (-oo, oo), "AV x=-1/2")
    same((sp.limit(f, x, oo), sp.limit(f, x, -oo)), (R(1, 4), R(1, 4)), "AH y=1/4")


@check("U2.A.ADI.5", "Adicional 5: opción b; contraejemplos de a, c y d", page=P + "adicionales/")
def _():
    # a) y d) fallan con L = 0 (f(x) = x, x0 = 0): el cociente no está definido.
    same(sp.limit(x, x, 0, dir="-"), 0, "L = 0")
    # c) falla si f(x0) != L: f(x) = x para x != 0, f(0) = 5.
    f0, L = 5, sp.limit(x, x, 0)
    require(f0 + L != 2 * L, "c) falla")
    # b) L + L = 2L con un ejemplo genérico.
    g = x**2 + 3
    same(sp.limit(g, x, 1, dir="+") + sp.limit(g, x, 1, dir="-"), 2 * sp.limit(g, x, 1), "b)")


@check("U2.A.ADI.7", "Adicional 7: opción d (AH c/3 si a=0; AV en 1/3 salvo c=3; hueco en 0)", page=P + "adicionales/")
def _():
    a, c = sp.symbols("a c", real=True)
    g = (a * x**3 + c * x**2 - x) / (3 * x**2 - x)
    same(sp.simplify(g - (a * x**2 + c * x - 1) / (3 * x - 1)), 0, "simplificación")
    same(sp.limit(g.subs({a: 2, c: 5}), x, 0), 1, "x=0 es hueco (a)")
    g0 = g.subs(a, 0)
    same(sp.limit(g0, x, oo), c / 3, "AH c/3")
    igual(ambos(g0.subs(c, 1), x, R(1, 3)), (oo, -oo), "c=1: AV en 1/3")
    same(sp.limit(g0.subs(c, 3), x, R(1, 3)), 1, "c=3: hueco en 1/3 (e falla)")
    m = sp.limit(g.subs({a: 6, c: 0}) / x, x, oo)
    same(m, 2, "a=6: AO de pendiente a/3 (b falla)")


@check("U2.A.E16.e", "16e es una potencia (base raíz, exponente (1+2x)/(3x-1)): límite 1/4, igual a la oficial",
       page="/analisis-matematico-i/unidad-2/practica/ejercicio-16/")
def _():
    # Regresión: la página transcribía el exponente como un factor y obtenía 1/12, declarando errónea la respuesta
    # oficial. En la guía (PDF) el exponente afecta a toda la raíz.
    xx = sp.symbols("xx", positive=True)
    base = sp.sqrt((1 - xx) / (1 - 64 * xx))
    expo = (1 + 2 * xx) / (3 * xx - 1)
    require(sp.limit(base, xx, sp.oo) == sp.Rational(1, 8), "base -> 1/8")
    require(sp.limit(expo, xx, sp.oo) == sp.Rational(2, 3), "exponente -> 2/3")
    require(sp.simplify(sp.Rational(1, 8) ** sp.Rational(2, 3) - sp.Rational(1, 4)) == 0, "(1/8)^(2/3) = 1/4")
    require(sp.limit(sp.exp(expo * sp.log(base)), xx, sp.oo) == sp.Rational(1, 4), "límite completo 1/4")
    # contraste numérico en x = 10^6
    v = (base ** expo).subs(xx, 10**6)
    require(abs(sp.N(v, 30) - sp.Rational(1, 4)) < sp.Rational(1, 10**4), "numérico cerca de 1/4")
