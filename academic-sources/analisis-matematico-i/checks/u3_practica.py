"""Comprobaciones de los ejercicios originales de la Unidad 3 (Derivada).

Cada función recalcula el resultado publicado y los pasos intermedios de la resolución.
"""
import sympy as sp
from content_pipeline.mathcheck import check, require, same

T = "/analisis-matematico-i/unidad-3/teoria/"
P1 = T + "razon-de-cambio-y-derivada/"
P2 = T + "derivada-como-funcion/"
P3 = T + "reglas-de-derivacion/"
P4 = T + "regla-de-la-cadena-e-inversa/"
P5 = T + "implicita-y-logaritmica/"
PI = "/analisis-matematico-i/unidad-3/practica/integradores/"

x, h, t, a, b, y = sp.symbols("x h t a b y", real=True)
xp = sp.symbols("xp", positive=True)
R = sp.Rational


def d(f, v=x):
    return sp.diff(f, v)


def tangent(f, v, p):
    return sp.expand(f.subs(v, p) + d(f, v).subs(v, p) * (v - p))


@check("U3.01", "Enfriamiento T=300-12t+t^2/10", page=P1)
def _():
    T_ = 300 - 12 * t + t ** 2 / 10
    same((T_.subs(t, 10) - T_.subs(t, 0)) / 10, -11, "media")
    same(sp.expand(T_.subs(t, 10 + h)), 190 - 10 * h + h ** 2 / 10, "T(10+h)")
    same(sp.limit((T_.subs(t, 10 + h) - 190) / h, h, 0), -10, "T'(10)")
    same(d(T_, t), -12 + t / 5, "T'")
    # Regresión de la auditoría pedagógica: el dominio era [0, 40] y T(40) = -20 °C (irreal); ahora [0, 30].
    same(sp.solve(sp.Eq(d(T_, t), -8), t), [20], "t con T' = -8")
    same(T_.subs(t, 20), 100, "T(20)")
    same(T_.subs(t, 30), 30, "T(30), fin del modelo")
    require(sp.solve(sp.Eq(d(T_, t), 0), t) == [60], "T' se anula recién en t = 60, fuera de [0, 30]")
    same((d(T_, t).subs(t, 0), d(T_, t).subs(t, 30)), (-12, -6), "T' entre -12 y -6")


@check("U3.02", "f=3x^2-x: f'(2)=11, tangente y normal", page=P1)
def _():
    f = 3 * x ** 2 - x
    same(f.subs(x, 2), 10, "f(2)")
    same(sp.expand(f.subs(x, 2 + h)), 10 + 11 * h + 3 * h ** 2, "f(2+h)")
    same(sp.limit((f.subs(x, 2 + h) - 10) / h, h, 0), 11, "f'(2)")
    same(tangent(f, x, 2), 11 * x - 12, "tangente")
    same(10 - (x - 2) / 11, 10 - (x - 2) / d(f).subs(x, 2), "normal")


@check("U3.03", "Tangentes a x^2-6x+10 por (2,-2)", page=P1)
def _():
    f = x ** 2 - 6 * x + 10
    cond = f.subs(x, a) + d(f).subs(x, a) * (2 - a) + 2
    same(sp.expand(cond), sp.expand(-a ** 2 + 4 * a), "ecuación")
    same(sorted(sp.solve(cond, a)), [0, 4], "a")
    same(f.subs(x, 2), 2, "(2,-2) exterior")
    same(tangent(f, x, 0), 10 - 6 * x, "t0")
    same(tangent(f, x, 4), 2 * x - 6, "t4")
    same([(10 - 6 * x).subs(x, 2), (2 * x - 6).subs(x, 2)], [-2, -2], "pasan por el punto")


@check("U3.04", "a, b con y=4x-3 tangente a ax^3+bx en x=1", page=P1)
def _():
    f = a * x ** 3 + b * x
    sol = sp.solve([sp.Eq(f.subs(x, 1), 1), sp.Eq(d(f).subs(x, 1), 4)], [a, b])
    same([sol[a], sol[b]], [R(3, 2), -R(1, 2)], "a, b")
    same(1 - (x - 1) / 4, 1 - (x - 1) / d(f.subs({a: R(3, 2), b: -R(1, 2)})).subs(x, 1), "normal")


@check("U3.05", "f'(x) de x/(x-1) por definición, f'(3) y tangente", page=P2)
def _():
    f = x / (x - 1)
    same(sp.expand((x + h) * (x - 1) - x * (x + h - 1)), -h, "numerador")
    q = sp.simplify((f.subs(x, x + h) - f) / h)
    same(q, -1 / ((x + h - 1) * (x - 1)), "cociente")
    same(sp.limit(q, h, 0), -1 / (x - 1) ** 2, "f'")
    same(d(f).subs(x, 3), -R(1, 4), "f'(3)")
    same(f.subs(x, 3), R(3, 2), "f(3)")
    same(tangent(f, x, 3), R(3, 2) - (x - 3) / 4, "tangente")


@check("U3.06", "Derivabilidad de ax^2+1 | bx-3 en x=2", page=P2)
def _():
    sol = sp.solve([sp.Eq(4 * a + 1, 2 * b - 3), sp.Eq(4 * a, b)], [a, b])
    same([sol[a], sol[b]], [1, 4], "a, b")
    l, r = x ** 2 + 1, 4 * x - 3
    same([l.subs(x, 2), r.subs(x, 2)], [5, 5], "continuidad")
    same(sp.limit((l.subs(x, 2 + h) - 5) / h, h, 0, "-"), 4, "f'_-")
    same(sp.limit((r.subs(x, 2 + h) - 5) / h, h, 0, "+"), 4, "f'_+")
    same([d(l), d(r)], [2 * x, 4], "f'")
    same([sp.limit(0 * x - 3, x, 2, "+"), (1 * 4 + 1)], [-3, 5], "salto con a=1, b=0")


@check("U3.07", "Ejemplos numéricos de la paridad: f par => f' impar; f impar => f' par", page=P2)
def _():
    fp_ = x ** 4 + 3 * x ** 2 - sp.cos(x)
    fi = x ** 3 - 2 * x + sp.sin(x)
    same(fp_.subs(x, -x) - fp_, 0, "f par")
    same(d(fp_).subs(x, -x) + d(fp_), 0, "f' impar")
    same(fi.subs(x, -x) + fi, 0, "f impar")
    same(d(fi).subs(x, -x) - d(fi), 0, "f' par")
    same(d(fp_).subs(x, 0), 0, "f'(0)=0")


@check("U3.08", "Derivadas de sumas con potencias", page=P3)
def _():
    same(d(6 * x ** 5 - 4 * x ** 3 + 2 * x - 9), 30 * x ** 4 - 12 * x ** 2 + 2, "a")
    g = 3 * sp.cbrt(xp) - 5 / xp ** 2 + 4 * sp.exp(xp)
    same(d(g, xp), 1 / sp.cbrt(xp ** 2) + 10 / xp ** 3 + 4 * sp.exp(xp), "b")
    hh = 7 * sp.sin(t) - t ** 2 / 2 + sp.log(t) - sp.pi ** 2
    tt = sp.symbols("tt", positive=True)
    same(d(hh.subs(t, tt), tt), 7 * sp.cos(tt) - tt + 1 / tt, "c")


@check("U3.09", "Producto y cociente", page=P3)
def _():
    f = (x ** 2 - 2 * x) * sp.exp(x)
    same(d(f), (x ** 2 - 2) * sp.exp(x), "a")
    same(sorted(sp.solve(d(f), x), key=float), [-sp.sqrt(2), sp.sqrt(2)], "tangente horizontal")
    same([f.subs(x, sp.sqrt(2)), f.subs(x, -sp.sqrt(2))],
         [(2 - 2 * sp.sqrt(2)) * sp.exp(sp.sqrt(2)), (2 + 2 * sp.sqrt(2)) * sp.exp(-sp.sqrt(2))], "ordenadas")
    g = sp.sin(x) / (x ** 2 + 1)
    same(d(g), ((x ** 2 + 1) * sp.cos(x) - 2 * x * sp.sin(x)) / (x ** 2 + 1) ** 2, "b")
    same(d(x * sp.tan(x)), sp.tan(x) + x / sp.cos(x) ** 2, "c")


@check("U3.10", "tanh x: f'=1-f^2=4/(e^x+e^-x)^2, tangente en 0", page=P3)
def _():
    u, v = sp.exp(x) - sp.exp(-x), sp.exp(x) + sp.exp(-x)
    f = u / v
    same(d(u), v, "u'=v")
    same(d(v), u, "v'=u")
    same(d(f), 1 - f ** 2, "1-f^2")
    same(d(f), 4 / v ** 2, "4/v^2")
    same(sp.expand(v ** 2 - u ** 2), 4, "v^2-u^2")
    same([f.subs(x, 0), d(f).subs(x, 0)], [0, 1], "tangente y=x")


@check("U3.11", "Cadena en cuatro funciones", page=P4)
def _():
    same(d((3 * x ** 2 - 5 * x + 1) ** 4), 4 * (6 * x - 5) * (3 * x ** 2 - 5 * x + 1) ** 3, "a")
    same(d(sp.exp(x ** 2 - 2 * x)), (2 * x - 2) * sp.exp(x ** 2 - 2 * x), "b")
    same(d(sp.log(x ** 3 + 1)), 3 * x ** 2 / (x ** 3 + 1), "c")
    require(sp.solveset(x ** 3 + 1 > 0, x, sp.S.Reals) == sp.Interval.open(-1, sp.oo), "dominio")
    same(d(sp.sin(sp.sqrt(xp)), xp), sp.cos(sp.sqrt(xp)) / (2 * sp.sqrt(xp)), "d")


@check("U3.12", "Cadena con tabla (puntos distintos de los del ejemplo 5)", page=P4)
def _():
    tabla = {1: (2, 3, 3, -2), 2: (1, -1, 1, 4), 3: (3, 5, 2, 1)}
    f, fp, g, gp = [lambda k, i=i: tabla[k][i] for i in range(4)]
    same(gp(f(1)) * fp(1), 12, "a: (g∘f)'(1)")
    same(fp(g(2)) * gp(2), 12, "b: (f∘g)'(2)")
    same(f(g(2)), 2, "(f∘g)(2)")
    require(g(3) != 0, "g(3) ≠ 0")
    same(R(fp(3) * g(3) - f(3) * gp(3), g(3) ** 2), R(7, 4), "c: (f/g)'(3)")
    same(2 * f(3) * fp(3) * g(3) + f(3) ** 2 * gp(3), 69, "d")
    same(sp.expand(2 + 12 * (x - 2)), 12 * x - 22, "tangente")
    # Que no repita el ejemplo 5, que calcula (f∘g)'(1) = -10, (g∘f)'(2) = 2 y (f/g)'(2) = -5.
    require((gp(f(1)) * fp(1), fp(g(2)) * gp(2)) != (2, -10), "datos distintos del ejemplo 5")


@check("U3.13", "Inversa de 2x^3+3x", page=P4)
def _():
    f = 2 * x ** 3 + 3 * x
    same(d(f), 6 * x ** 2 + 3, "f'")
    same([f.subs(x, 1), f.subs(x, 0)], [5, 0], "preimágenes")
    same([1 / d(f).subs(x, 1), 1 / d(f).subs(x, 0)], [R(1, 9), R(1, 3)], "(f^-1)'")
    same(1 + (x - 5) / 9, 1 + R(1, 9) * (x - 5), "tangente")


@check("U3.14", "f=x arcsen x + sqrt(1-x^2): f'=arcsen x, tangente en 1/2, F'", page=P4)
def _():
    xx = sp.symbols("xx", real=True)
    f = xx * sp.asin(xx) + sp.sqrt(1 - xx ** 2)
    same(sp.simplify(d(f, xx) - sp.asin(xx)), 0, "f'")
    same(d(xx * sp.asin(xx), xx), sp.asin(xx) + xx / sp.sqrt(1 - xx ** 2), "producto")
    same(d(sp.sqrt(1 - xx ** 2), xx), -xx / sp.sqrt(1 - xx ** 2), "raíz")
    same(f.subs(xx, R(1, 2)), sp.pi / 12 + sp.sqrt(3) / 2, "f(1/2)")
    same(sp.asin(R(1, 2)), sp.pi / 6, "f'(1/2)")
    F = f.subs(xx, x ** 2 - 1)
    same(sp.simplify(d(F).subs(x, R(1, 2)) - 2 * R(1, 2) * sp.asin(R(1, 4) - 1)), 0, "F'(1/2)")
    dom = sp.Intersection(sp.solveset(x ** 2 - 1 > -1, x, sp.S.Reals), sp.solveset(x ** 2 - 1 < 1, x, sp.S.Reals))
    require(dom == sp.Union(sp.Interval.open(-sp.sqrt(2), 0), sp.Interval.open(0, sp.sqrt(2))), "dominio")


@check("U3.15", "2x^2+3y^2=14 en (1,2)", page=P5)
def _():
    F = 2 * x ** 2 + 3 * y ** 2 - 14
    same(F.subs({x: 1, y: 2}), 0, "punto")
    yp = sp.idiff(F, y, x)
    same(yp, -2 * x / (3 * y), "y'")
    same(yp.subs({x: 1, y: 2}), -R(1, 3), "pendiente")
    same(2 + 3 * (x - 1), 2 - (x - 1) / yp.subs({x: 1, y: 2}), "normal")
    sol = sp.solve([F, y - 2 * x], [x, y])
    same(sorted(sol), [(-1, -2), (1, 2)], "otro punto")


@check("U3.16", "x^2-2xy+2y^2=4: tangentes horizontales y verticales", page=P5)
def _():
    F = x ** 2 - 2 * x * y + 2 * y ** 2 - 4
    yp = sp.idiff(F, y, x)
    same(yp, (y - x) / (2 * y - x), "y'")
    sh = sp.solve([F, y - x], [x, y], dict=True)
    sv = sp.solve([F, x - 2 * y], [x, y], dict=True)
    same(sorted((s_[x], s_[y]) for s_ in sh), [(-2, -2), (2, 2)], "horizontales")
    same(sorted((s_[x], s_[y]) for s_ in sv), sorted([(-2 * sp.sqrt(2), -sp.sqrt(2)), (2 * sp.sqrt(2), sp.sqrt(2))], key=lambda p: float(p[0])), "verticales")
    for s_ in sh:
        require((2 * y - x).subs(s_) != 0, "denominador no nulo")
    for s_ in sv:
        require((y - x).subs(s_) != 0, "numerador no nulo")
    # no hay más: se resuelve cada condición completa
    require(len(sh) == 2 and len(sv) == 2, "cantidad de puntos")


@check("U3.17", "Derivación logarítmica a, b, c", page=P5)
def _():
    xx = sp.symbols("xx", positive=True)
    f = sp.log(xx) ** xx
    same(sp.simplify(d(f, xx) - f * (sp.log(sp.log(xx)) + 1 / sp.log(xx))), 0, "a")
    g = (2 * xx + 1) ** sp.sin(xx)
    same(sp.simplify(d(g, xx) - g * (sp.cos(xx) * sp.log(2 * xx + 1) + 2 * sp.sin(xx) / (2 * xx + 1))), 0, "b")
    hh = xx ** xx
    same(sp.simplify(d(hh, xx) - hh * (sp.log(xx) + 1)), 0, "c: h'")
    same([hh.subs(xx, 1), d(hh, xx).subs(xx, 1)], [1, 1], "h(1), h'(1)")


@check("U3.18", "f=(x+1)^2 (x-2)^3/(x^2+1)^4: (ln|f|)', tangente en 0, f'(-2)", page=P5)
def _():
    f = (x + 1) ** 2 * (x - 2) ** 3 / (x ** 2 + 1) ** 4
    form = 2 / (x + 1) + 3 / (x - 2) - 8 * x / (x ** 2 + 1)
    same(sp.simplify(d(f) - f * form), 0, "f'/f")
    same(f.subs(x, 0), -8, "f(0)")
    same(d(f).subs(x, 0), -4, "f'(0)")
    same(tangent(f, x, 0), -4 * x - 8, "tangente")
    same(f.subs(x, -2), -R(64, 625), "f(-2)")
    same(form.subs(x, -2), R(9, 20), "f'/f en -2")
    same(d(f).subs(x, -2), -R(144, 3125), "f'(-2)")
    require(f.subs(x, -2) < 0, "f negativa en -2")


@check("U3.19", "Función por tramos con logaritmo", page=PI)
def _():
    sol = sp.solve([sp.Eq(a + b, 1), sp.Eq(2 * a, 1)], [a, b])
    same([sol[a], sol[b]], [R(1, 2), R(1, 2)], "a, b")
    l = x ** 2 / 2 + R(1, 2)
    r = 1 + sp.log(x)
    same([l.subs(x, 1), sp.limit(r, x, 1, "+")], [1, 1], "continuidad")
    same(sp.limit((l.subs(x, 1 + h) - 1) / h, h, 0, "-"), 1, "f'_-")
    same(sp.limit((r.subs(x, 1 + h) - 1) / h, h, 0, "+"), 1, "f'_+")
    same(d(l), x, "f' izquierda")
    same(d(r), 1 / x, "f' derecha")
    same(tangent(l, x, 1), x, "tangente en 1")
    same(sp.solve(sp.Eq(1 / x, R(1, 4)), x), [4], "x=4")
    same(tangent(r, x, 4), 1 + sp.log(4) + (x - 4) / 4, "tangente en 4")
    same([sp.limit(d(l), x, 1, "-"), sp.limit(d(r), x, 1, "+")], [1, 1], "f' continua")


@check("U3.20", "Concentración C=20 t e^(-t/2)", page=PI)
def _():
    C = 20 * t * sp.exp(-t / 2)
    same(d(C, t), 10 * (2 - t) * sp.exp(-t / 2), "C'")
    same(sp.solve(d(C, t), t), [2], "punto crítico")
    same(C.subs(t, 2), 40 / sp.E, "máximo")
    require(abs(float(40 / sp.E) - 14.7) < 0.05, "≈ 14,7")
    same(d(C, t).subs(t, 4), -20 * sp.exp(-2), "C'(4)")
    require(abs(float(-20 * sp.exp(-2)) + 2.71) < 0.005, "≈ -2,71")
    same(tangent(C, t, 0), 20 * t, "tangente en 0")
    require(d(C, t).subs(t, 1) > 0, "C'(1)>0")
    require(d(C, t).subs(t, 3) < 0, "C'(3)<0")


@check("U3.21", "Opción múltiple: h=f(g(x))x^2, h'(2)=44; (g^-1)'(5)=1/3", page=PI)
def _():
    g2, gp2 = (3 * x - 1).subs(x, 2), d(3 * x - 1)
    same([g2, gp2], [5, 3], "g(2), g'(2)")
    f5, fp5 = -1, 4
    h2 = fp5 * gp2 * 2 ** 2 + f5 * 2 * 2
    same(h2, 44, "h'(2)")
    same(fp5 * gp2 * 4, 48, "opción 2")
    same(fp5 * gp2, 12, "opción 3")
    same(1 / gp2, R(1, 3), "(g^-1)'(5)")


@check("U3.22", "f=x e^x: inversa, h=(x e^x)^x", page=PI)
def _():
    f = x * sp.exp(x)
    same(d(f), (1 + x) * sp.exp(x), "f'")
    same(f.subs(x, 1), sp.E, "f(1)=e")
    same(1 / d(f).subs(x, 1), 1 / (2 * sp.E), "(f^-1)'(e)")
    xx = sp.symbols("xx", positive=True)
    hh = (xx * sp.exp(xx)) ** xx
    lh = xx * (sp.log(xx) + xx)
    same(sp.expand_log(sp.log(hh), force=True) - lh, 0, "ln h")
    same(d(lh, xx), sp.log(xx) + 1 + 2 * xx, "(ln h)'")
    same(sp.simplify(d(hh, xx) - hh * (sp.log(xx) + 2 * xx + 1)), 0, "h'")
    same([hh.subs(xx, 1), d(hh, xx).subs(xx, 1)], [sp.E, 3 * sp.E], "h(1), h'(1)")
