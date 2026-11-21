"""Comprobaciones de los ejemplos resueltos de la teoría de la Unidad 3 (Derivada).

Cada función recalcula el ejemplo desde sus datos y verifica los pasos intermedios publicados
(cocientes incrementales, límites laterales, derivadas, rectas y puntos).
"""
import sympy as sp
from content_pipeline.mathcheck import check, require, same

T = "/analisis-matematico-i/unidad-3/teoria/"
P1 = T + "razon-de-cambio-y-derivada/"
P2 = T + "derivada-como-funcion/"
P3 = T + "reglas-de-derivacion/"
P4 = T + "regla-de-la-cadena-e-inversa/"
P5 = T + "implicita-y-logaritmica/"

x, h, t, a, b = sp.symbols("x h t a b", real=True)
xp = sp.symbols("xp", positive=True)
R = sp.Rational


def d(f, v=x):
    return sp.diff(f, v)


def quotient(f, v, point):
    return sp.simplify((f.subs(v, point + h) - f.subs(v, point)) / h)


def tangent(f, v, point):
    return sp.expand(f.subs(v, point) + d(f, v).subs(v, point) * (v - point))


def numeric(expr_a, expr_b, points, tol=1e-12):
    for p in points:
        require(abs(float(expr_a.subs(x, p)) - float(expr_b.subs(x, p))) < tol, f"difieren en {p}")


# ---------------------------------------------------------------------------
# 3.1 Razón de cambio y derivada
# ---------------------------------------------------------------------------
@check("U3.T.RAZ.1", "Razón media de s=2t^2+t en [1,3] y cociente en [1,1+h]", page=P1)
def _():
    s = 2 * t ** 2 + t
    same(s.subs(t, 1), 3, "s(1)")
    same(s.subs(t, 3), 21, "s(3)")
    same((s.subs(t, 3) - s.subs(t, 1)) / 2, 9, "media en [1,3]")
    same(sp.expand(s.subs(t, 1 + h)), 3 + 5 * h + 2 * h ** 2, "s(1+h)")
    same(sp.simplify((s.subs(t, 1 + h) - 3) / h), 5 + 2 * h, "cociente")
    same([5 + 2 * v for v in (2, 1, R(1, 10), R(1, 100))], [9, 7, R(26, 5), R(251, 50)], "valores con h")


@check("U3.T.RAZ.2", "Velocidad instantánea s'(1)=5", page=P1)
def _():
    s = 2 * t ** 2 + t
    same(sp.limit((s.subs(t, 1 + h) - 3) / h, h, 0, "+"), 5, "por derecha")
    same(sp.limit((s.subs(t, 1 + h) - 3) / h, h, 0, "-"), 5, "por izquierda")


@check("U3.T.DER.1", "f'(1)=1/4 para sqrt(x+3), con la racionalización publicada", page=P1)
def _():
    f = sp.sqrt(x + 3)
    same(f.subs(x, 1), 2, "f(1)")
    q = (sp.sqrt(4 + h) - 2) / h
    same(q, 1 / (sp.sqrt(4 + h) + 2), "racionalización")
    same(sp.limit(q, h, 0, "+"), R(1, 4), "lateral +")
    same(sp.limit(q, h, 0, "-"), R(1, 4), "lateral -")
    same(d(f).subs(x, 1), R(1, 4), "por reglas")


@check("U3.T.DER.2", "Tangente y normal a sqrt(x+3) en x=1", page=P1)
def _():
    f = sp.sqrt(x + 3)
    same(tangent(f, x, 1), x / 4 + R(7, 4), "tangente")
    same(2 - (x - 1) / d(f).subs(x, 1), -4 * x + 6, "normal")
    same(R(1, 4) * (-4), -1, "producto de pendientes")


@check("U3.T.DER.3", "Tangentes de x^3-3x perpendiculares a y=-x/6+1", page=P1)
def _():
    f = x ** 3 - 3 * x
    sols = sp.solve(sp.Eq(d(f), 6), x)
    same(sorted(sols, key=float), [-sp.sqrt(3), sp.sqrt(3)], "abscisas")
    same([f.subs(x, v) for v in sols], [0, 0], "ordenadas")
    same(-R(1, 6) * 6, -1, "perpendicularidad")
    same(tangent(f, x, sp.sqrt(3)), sp.expand(6 * (x - sp.sqrt(3))), "tangente 1")
    same(tangent(f, x, -sp.sqrt(3)), sp.expand(6 * (x + sp.sqrt(3))), "tangente 2")


@check("U3.T.DER.4", "Tangentes a x^2 por (1,-3)", page=P1)
def _():
    f = x ** 2
    cond = sp.Eq(-3, f.subs(x, a) + d(f).subs(x, a) * (1 - a))
    same(sp.expand(2 * a - a ** 2 - (-3)), sp.expand(-(a ** 2 - 2 * a - 3)), "ecuación")
    sols = sp.solve(cond, a)
    same(sorted(sols), [-1, 3], "a")
    same(f.subs(x, 1), 1, "(1,-3) no está en la parábola")
    same(tangent(f, x, 3), 6 * x - 9, "tangente a=3")
    same(tangent(f, x, -1), -2 * x - 1, "tangente a=-1")
    same([(6 * x - 9).subs(x, 1), (-2 * x - 1).subs(x, 1)], [-3, -3], "pasan por (1,-3)")


@check("U3.T.DER.5", "a, b para que y=5x-4 sea tangente a ax^2+bx en x=1", page=P1)
def _():
    f = a * x ** 2 + b * x
    sol = sp.solve([sp.Eq(f.subs(x, 1), 1), sp.Eq(d(f).subs(x, 1), 5)], [a, b])
    same([sol[a], sol[b]], [4, -3], "a, b")


@check("U3.T.DER.6", "sqrt(4,1) ≈ 2,025 por la recta tangente (numérico, aritmética exacta)", page=P1)
def _():
    f = sp.sqrt(x)
    same(d(f).subs(x, 4), R(1, 4), "f'(4)")
    approx = 2 + R(1, 4) * R(1, 10)
    same(approx, R(81, 40), "2,025")
    exact = sp.sqrt(R(41, 10))
    require(abs(float(exact) - 2.02484) < 1e-5, "valor exacto 2,02484")
    require(abs(exact - approx) < R(1, 1000), "error menor que 0,001")


# ---------------------------------------------------------------------------
# 3.2 La derivada como función
# ---------------------------------------------------------------------------
@check("U3.T.FUN.1", "f'(x) por definición para 1/(x+2)", page=P2)
def _():
    f = 1 / (x + 2)
    q = (f.subs(x, x + h) - f) / h
    same(sp.simplify(q), -1 / ((x + h + 2) * (x + 2)), "cociente simplificado")
    same(sp.limit(sp.simplify(q), h, 0), -1 / (x + 2) ** 2, "límite")
    same(d(f), -1 / (x + 2) ** 2, "por reglas")


@check("U3.T.FUN.2", "g'(x)=1/sqrt(2x-1) y comportamiento en x=1/2", page=P2)
def _():
    g = sp.sqrt(2 * xp - 1)
    q = (g.subs(xp, xp + h) - g) / h
    same(sp.simplify(q), 2 / (sp.sqrt(2 * xp - 1 + 2 * h) + sp.sqrt(2 * xp - 1)), "racionalización")
    same(sp.limit(2 / (sp.sqrt(2 * xp - 1 + 2 * h) + sp.sqrt(2 * xp - 1)), h, 0), 1 / sp.sqrt(2 * xp - 1), "límite")
    # en x = 1/2: cociente sqrt(2h)/h
    hp = sp.symbols("hp", positive=True)
    same(sp.simplify(sp.sqrt(2 * hp) / hp - sp.sqrt(2 / hp)), 0, "sqrt(2h)/h = sqrt(2/h)")
    require(sp.limit(sp.sqrt(2 / hp), hp, 0, "+") == sp.oo, "tangente vertical")


@check("U3.T.FUN.3", "|x| en 0: derivadas laterales -1 y 1", page=P2)
def _():
    same(sp.limit(sp.Abs(h) / h, h, 0, "+"), 1, "f'_+")
    same(sp.limit(sp.Abs(h) / h, h, 0, "-"), -1, "f'_-")


@check("U3.T.FUN.4", "Función por tramos: continua, laterales 2 y 3 en x=1, derivada por tramos", page=P2)
def _():
    left, right = x ** 2 + 1, 3 * x - 1
    same(left.subs(x, 1), 2, "f(1)")
    same(sp.limit(left, x, 1, "-"), 2, "límite izquierdo")
    same(sp.limit(right, x, 1, "+"), 2, "límite derecho")
    same(sp.limit((left.subs(x, 1 + h) - 2) / h, h, 0, "-"), 2, "f'_-")
    same(sp.limit((right.subs(x, 1 + h) - 2) / h, h, 0, "+"), 3, "f'_+")
    same(sp.simplify((left.subs(x, 1 + h) - 2) / h), 2 + h, "cociente izquierdo")
    same([d(left), d(right)], [2 * x, 3], "derivada por tramos")


@check("U3.T.FUN.5", "a, b para derivabilidad de x^3+1 | ax+b en x=1", page=P2)
def _():
    sol = sp.solve([sp.Eq(a + b, 2), sp.Eq(a, 3)], [a, b])
    same([sol[a], sol[b]], [3, -1], "a, b")
    same(d(x ** 3 + 1).subs(x, 1), 3, "f'_-(1)")
    same(sp.limit(((3 * (1 + h) - 1) - 2) / h, h, 0, "+"), 3, "f'_+(1)")


@check("U3.T.FUN.6", "x^(1/3): tangente vertical; x^(2/3): cúspide (laterales infinitos)", page=P2)
def _():
    hp = sp.symbols("hp", positive=True)
    # cbrt(x): para h = -u, cbrt(-u) = -cbrt(u)
    require(sp.limit(hp ** R(-2, 3), hp, 0, "+") == sp.oo, "cbrt: lateral derecha +oo")
    # h<0, h=-u: cbrt(-u)/(-u) = (-u^(1/3))/(-u) = u^(-2/3)
    q_left = (-(hp ** R(1, 3))) / (-hp)
    same(sp.simplify(q_left - hp ** R(-2, 3)), 0, "cociente izquierdo de cbrt")
    require(sp.limit(q_left, hp, 0, "+") == sp.oo, "cbrt: lateral izquierda +oo")
    # x^(2/3): derecha h^(-1/3) -> +oo ; izquierda cbrt(u^2)/(-u) = -u^(-1/3) -> -oo
    q_right = hp ** R(2, 3) / hp
    q_left2 = (hp ** R(2, 3)) / (-hp)
    require(sp.limit(q_right, hp, 0, "+") == sp.oo, "x^(2/3): lateral derecha +oo")
    require(sp.limit(q_left2, hp, 0, "+") == -sp.oo, "x^(2/3): lateral izquierda -oo")


@check("U3.T.FUN.7", "x^2 sen(1/x): f'(0)=0, f'(x)=2x sen(1/x)-cos(1/x), f' toma -1 y 1 cerca de 0", page=P2)
def _():
    f = x ** 2 * sp.sin(1 / x)
    same(sp.limit(h * sp.sin(1 / h), h, 0), 0, "f'(0)")
    fp = d(f)
    same(fp, 2 * x * sp.sin(1 / x) - sp.cos(1 / x), "f' para x != 0")
    for k in (1, 5, 50):
        same(fp.subs(x, 1 / (2 * k * sp.pi)), -1, "f'(x_k)")
        same(fp.subs(x, 1 / ((2 * k + 1) * sp.pi)), 1, "f'(y_k)")


# ---------------------------------------------------------------------------
# 3.3 Reglas de derivación
# ---------------------------------------------------------------------------
@check("U3.T.REG.1", "(x^4)' por el binomio", page=P3)
def _():
    q = sp.expand(((x + h) ** 4 - x ** 4) / h)
    same(q, 4 * x ** 3 + 6 * x ** 2 * h + 4 * x * h ** 2 + h ** 3, "cociente")
    same(sp.limit(q, h, 0), 4 * x ** 3, "límite")


@check("U3.T.REG.2", "(sqrt x)' por conjugado", page=P3)
def _():
    q = (sp.sqrt(xp + h) - sp.sqrt(xp)) / h
    same(q, 1 / (sp.sqrt(xp + h) + sp.sqrt(xp)), "racionalización")
    same(sp.limit(q, h, 0, "+"), 1 / (2 * sp.sqrt(xp)), "límite")


@check("U3.T.REG.3", "(sen x)' = cos x con los límites publicados", page=P3)
def _():
    q = sp.sin(x + h) / h - sp.sin(x) / h
    same(sp.simplify(sp.expand_trig(q) - (sp.sin(x) * (sp.cos(h) - 1) / h + sp.cos(x) * sp.sin(h) / h)), 0, "identidad")
    same(sp.limit((sp.cos(h) - 1) / h, h, 0), 0, "límite del coseno")
    same(sp.limit(sp.sin(h) / h, h, 0), 1, "límite notable")
    same(sp.simplify((sp.cos(h) - 1) / h + sp.sin(h) ** 2 / (h * (sp.cos(h) + 1))), 0, "(cos h - 1)/h = -sen^2 h / (h (cos h+1))")
    same(sp.limit(q, h, 0), sp.cos(x), "límite")
    same(d(sp.cos(x)), -sp.sin(x), "(cos x)'")


@check("U3.T.REG.4", "Derivada de 4x^5-7sqrt(x)+3/x^2+pi", page=P3)
def _():
    f = 4 * xp ** 5 - 7 * sp.sqrt(xp) + 3 / xp ** 2 + sp.pi
    same(d(f, xp), 20 * xp ** 4 - 7 / (2 * sp.sqrt(xp)) - 6 / xp ** 3, "f'")


@check("U3.T.REG.5", "Derivada de (3x^2-x) ln x", page=P3)
def _():
    f = (3 * xp ** 2 - xp) * sp.log(xp)
    same(d(f, xp), (6 * xp - 1) * sp.log(xp) + 3 * xp - 1, "f'")


@check("U3.T.REG.6", "Derivada de x^2 e^x sen x", page=P3)
def _():
    f = x ** 2 * sp.exp(x) * sp.sin(x)
    same(d(x ** 2 * sp.exp(x)), 2 * x * sp.exp(x) + x ** 2 * sp.exp(x), "factor")
    same(d(f), x * sp.exp(x) * ((x + 2) * sp.sin(x) + x * sp.cos(x)), "f'")


@check("U3.T.REG.7", "Derivada de (2x+1)/(x^2+4)", page=P3)
def _():
    f = (2 * x + 1) / (x ** 2 + 4)
    same(d(f), 2 * (4 - x - x ** 2) / (x ** 2 + 4) ** 2, "f'")
    same(sp.expand(2 * (x ** 2 + 4) - (2 * x + 1) * 2 * x), -2 * x ** 2 - 2 * x + 8, "numerador")
    require(sp.solve(x ** 2 + 4, x, domain=sp.S.Reals) == [], "denominador sin raíces reales")


@check("U3.T.REG.8", "(tan x)' = 1/cos^2 x y (sec x)' = sec x tan x", page=P3)
def _():
    same(d(sp.sin(x) / sp.cos(x)), 1 / sp.cos(x) ** 2, "tan")
    same(d(sp.tan(x)), 1 / sp.cos(x) ** 2, "tan (sympy)")
    same(d(1 / sp.cos(x)), sp.sin(x) / sp.cos(x) ** 2, "sec")
    same(sp.sin(x) / sp.cos(x) ** 2, (1 / sp.cos(x)) * sp.tan(x), "sec tan")


@check("U3.T.REG.9", "(x^2-4)/(x-2): derivada por cociente y por simplificación", page=P3)
def _():
    f = (x ** 2 - 4) / (x - 2)
    same(sp.simplify((2 * x * (x - 2) - (x ** 2 - 4)) / (x - 2) ** 2), 1, "cociente")
    same(sp.expand(2 * x * (x - 2) - (x ** 2 - 4)), x ** 2 - 4 * x + 4, "numerador")
    same(sp.cancel(f), x + 2, "simplificación")
    same(d(f), 1, "derivada")


# ---------------------------------------------------------------------------
# 3.4 Regla de la cadena e inversa
# ---------------------------------------------------------------------------
@check("U3.T.CAD.1", "((5x-2)^7)'", page=P4)
def _():
    same(d((5 * x - 2) ** 7), 35 * (5 * x - 2) ** 6, "f'")


@check("U3.T.CAD.2", "(sqrt(x^2+1))'", page=P4)
def _():
    same(d(sp.sqrt(x ** 2 + 1)), x / sp.sqrt(x ** 2 + 1), "f'")


@check("U3.T.CAD.3", "(sen^2(e^(3x)))'", page=P4)
def _():
    f = sp.sin(sp.exp(3 * x)) ** 2
    paso = 2 * sp.sin(sp.exp(3 * x)) * sp.cos(sp.exp(3 * x)) * sp.exp(3 * x) * 3
    same(d(f), paso, "cadena")
    same(paso, 3 * sp.exp(3 * x) * sp.sin(2 * sp.exp(3 * x)), "forma con sen 2θ")


@check("U3.T.CAD.4", "(x^2 e^(-x^2))'", page=P4)
def _():
    f = x ** 2 * sp.exp(-x ** 2)
    same(d(f), 2 * x * (1 - x ** 2) * sp.exp(-x ** 2), "f'")


# tabla del ejemplo y del ejercicio U3.12
TABLA = {1: (2, 3, 3, -2), 2: (1, -1, 1, 4), 3: (3, 5, 2, 1)}  # x: (f, f', g, g')


@check("U3.T.CAD.5", "Cadena y cociente con la tabla de valores", page=P4)
def _():
    f = lambda k: TABLA[k][0]
    fp = lambda k: TABLA[k][1]
    g = lambda k: TABLA[k][2]
    gp = lambda k: TABLA[k][3]
    same(fp(g(1)) * gp(1), -10, "(f∘g)'(1)")
    same(gp(f(2)) * fp(2), 2, "(g∘f)'(2)")
    same(R(fp(2) * g(2) - f(2) * gp(2), g(2) ** 2), -5, "(f/g)'(2)")
    # (f∘g)'(1) y (g∘f)'(1) son distintos
    same(gp(f(1)) * fp(1), 3 * 1 * 0 + gp(2) * 3, "(g∘f)'(1)")
    require(gp(f(1)) * fp(1) != fp(g(1)) * gp(1), "el orden importa")


@check("U3.T.CAD.6", "Tangente a h(x)=f(2x^2-6) en x=2 con f tangente y=-x+7 en x=2", page=P4)
def _():
    u = 2 * x ** 2 - 6
    same(u.subs(x, 2), 2, "u(2)")
    same(d(u).subs(x, 2), 8, "u'(2)")
    f2, fp2 = (-x + 7).subs(x, 2), d(-x + 7)
    same(f2, 5, "f(2)")
    same(fp2 * 8, -8, "h'(2)")
    same(5 - 8 * (x - 2), -8 * x + 21, "tangente")


@check("U3.T.INV.1", "(f^-1)'(3) para x^5+x^3+x", page=P4)
def _():
    f = x ** 5 + x ** 3 + x
    same(f.subs(x, 1), 3, "f(1)")
    same(d(f), 5 * x ** 4 + 3 * x ** 2 + 1, "f'")
    same(1 / d(f).subs(x, 1), R(1, 9), "(f^-1)'(3)")
    require(sp.real_roots(sp.Poly(f - 3, x)) == [1], "única preimagen real")


@check("U3.T.INV.2", "Tangente a la inversa de x+e^x en (1,0)", page=P4)
def _():
    f = x + sp.exp(x)
    same(f.subs(x, 0), 1, "f(0)")
    same(d(f).subs(x, 0), 2, "f'(0)")
    same(0 + R(1, 2) * (x - 1), (x - 1) / 2, "tangente a la inversa")
    same(tangent(f, x, 0), 1 + 2 * x, "tangente a f")
    # reflexión: x = 1 + 2y  <=>  y = (x-1)/2
    yy = sp.symbols("yy")
    same(sp.solve(sp.Eq(x, 1 + 2 * yy), yy), [(x - 1) / 2], "reflexión de la tangente")


@check("U3.T.INV.3", "(arctan 3x)' = 3/(1+9x^2)", page=P4)
def _():
    same(d(sp.atan(3 * x)), 3 / (1 + 9 * x ** 2), "f'")
    same(sp.diff(sp.atan(x)), 1 / (1 + x ** 2), "(arctan)'")
    same(sp.diff(sp.asin(x)), 1 / sp.sqrt(1 - x ** 2), "(arcsen)'")
    same(sp.diff(sp.acos(x)), -1 / sp.sqrt(1 - x ** 2), "(arccos)'")


@check("U3.T.INV.4", "(arcsen sqrt x)' en (0,1)", page=P4)
def _():
    same(d(sp.asin(sp.sqrt(xp)), xp), 1 / (2 * sp.sqrt(xp) * sp.sqrt(1 - xp)), "f'")


@check("U3.T.INV.5", "arctan x + arctan(1/x) tiene derivada nula; valores en 1 y -1", page=P4)
def _():
    phi = sp.atan(x) + sp.atan(1 / x)
    same(d(phi), 0, "derivada")
    same(phi.subs(x, 1), sp.pi / 2, "φ(1)")
    same(phi.subs(x, -1), -sp.pi / 2, "φ(-1)")


# ---------------------------------------------------------------------------
# 3.5 Derivación implícita y logarítmica
# ---------------------------------------------------------------------------
y = sp.symbols("y", real=True)


@check("U3.T.IMP.1", "Circunferencia x^2+y^2=25: y'=-x/y, tangente en (3,4)", page=P5)
def _():
    F = x ** 2 + y ** 2 - 25
    same(sp.idiff(F, y, x), -x / y, "y'")
    same(F.subs({x: 3, y: 4}), 0, "(3,4) en la curva")
    same(sp.idiff(F, y, x).subs({x: 3, y: 4}), -R(3, 4), "pendiente en (3,4)")
    same(sp.idiff(F, y, x).subs({x: 3, y: -4}), R(3, 4), "pendiente en (3,-4)")
    same(sp.solve(F.subs(y, 0), x), [-5, 5], "y=0 en x=±5")


@check("U3.T.IMP.2", "x^3+xy+y^3=11 en (1,2): y'=-5/13, tangente y normal", page=P5)
def _():
    F = x ** 3 + x * y + y ** 3 - 11
    same(F.subs({x: 1, y: 2}), 0, "punto")
    yp = sp.idiff(F, y, x)
    same(yp, -(3 * x ** 2 + y) / (x + 3 * y ** 2), "y'")
    same(yp.subs({x: 1, y: 2}), -R(5, 13), "pendiente")
    same(2 - R(5, 13) * (x - 1), -R(5, 13) * x + R(31, 13), "tangente")
    same(2 + R(13, 5) * (x - 1), R(13, 5) * x - R(3, 5), "normal")
    same(-R(5, 13) * R(13, 5), -1, "perpendiculares")


@check("U3.T.IMP.3", "x^2+xy+y^2=3: tangentes horizontales y verticales", page=P5)
def _():
    F = x ** 2 + x * y + y ** 2 - 3
    yp = sp.idiff(F, y, x)
    same(yp, -(2 * x + y) / (x + 2 * y), "y'")
    sh = sp.solve([F, 2 * x + y], [x, y], dict=True)
    sv = sp.solve([F, x + 2 * y], [x, y], dict=True)
    same(sorted((s_[x], s_[y]) for s_ in sh), [(-1, 2), (1, -2)], "horizontales")
    same(sorted((s_[x], s_[y]) for s_ in sv), [(-2, 1), (2, -1)], "verticales")
    for p in ((1, -2), (-1, 2)):
        require((x + 2 * y).subs({x: p[0], y: p[1]}) != 0, "denominador no nulo")
    for p in ((-2, 1), (2, -1)):
        require((2 * x + y).subs({x: p[0], y: p[1]}) != 0, "numerador no nulo")
    # la curva está dentro del cuadrado |x|<=2, |y|<=2: máximos de x e y
    same(sp.solve(sp.discriminant(F, y), x), [-2, 2], "|x| <= 2")


@check("U3.T.LOG.1", "(x^sen x)'", page=P5)
def _():
    f = xp ** sp.sin(xp)
    same(d(f, xp), f * (sp.cos(xp) * sp.log(xp) + sp.sin(xp) / xp), "f'")


@check("U3.T.LOG.2", "(x^α)' = α x^(α-1) para x>0", page=P5)
def _():
    al = sp.symbols("alpha", real=True)
    same(d(xp ** al, xp), al * xp ** (al - 1), "potencia")
    same(d(al * sp.log(xp), xp), al / xp, "(ln y)'")


@check("U3.T.LOG.3", "Derivación logarítmica de (x^2+1)^3 sqrt(x-2)/(x+5)^4 en x>2", page=P5)
def _():
    xx = sp.symbols("xx", positive=True)
    f = (xx ** 2 + 1) ** 3 * sp.sqrt(xx - 2) / (xx + 5) ** 4
    lf = 3 * sp.log(xx ** 2 + 1) + sp.log(xx - 2) / 2 - 4 * sp.log(xx + 5)
    same(sp.expand_log(sp.log(f), force=True) - lf, 0, "ln f desarrollado")
    same(d(lf, xx), 6 * xx / (xx ** 2 + 1) + 1 / (2 * (xx - 2)) - 4 / (xx + 5), "(ln f)'")
    for v in (R(5, 2), 3, 7, 20):
        same((d(f, xx) - f * (6 * xx / (xx ** 2 + 1) + 1 / (2 * (xx - 2)) - 4 / (xx + 5))).subs(xx, v), 0, f"f' en {v}")


@check("U3.T.LOG.4", "ln|f| para (x-1)^3(x+2)/(x-3)^2: vale con f<0", page=P5)
def _():
    f = (x - 1) ** 3 * (x + 2) / (x - 3) ** 2
    form = 3 / (x - 1) + 1 / (x + 2) - 2 / (x - 3)
    same(sp.simplify(d(f) - f * form), 0, "f' = f * (...)")
    for v, signo in ((-3, 1), (-1, -1), (0, -1), (R(1, 2), -1), (2, 1), (4, 1)):
        fv = f.subs(x, v)
        require(fv != 0 and (fv > 0) == (signo > 0), f"signo de f en {v}")
        same(d(f).subs(x, v), fv * form.subs(x, v), f"f'({v})")
