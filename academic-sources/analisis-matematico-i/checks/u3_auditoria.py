"""Auditoría de la Práctica 3 (Unidad 3, Derivada): recalcula los resultados publicados.

Cada comprobación rehace el cálculo desde el enunciado y lo contrasta con el resultado de la página
(y, cuando se indica, con la respuesta oficial de la guía). Convenciones: ``U3.A.E<kk><ítem>`` para el
ejercicio kk de la práctica y ``U3.A.AD<k>`` para los ejercicios adicionales.
"""
import sympy as sp
from content_pipeline.mathcheck import check, require, same

P = "/analisis-matematico-i/unidad-3/practica/practica-3/"
x, h, t, z, s, r, a, b, m, y = sp.symbols("x h t z s r a b m y", real=True)
pos = sp.symbols("p", positive=True)


def d(f, v=x):
    return sp.diff(f, v)


def quotient_limit(f, v, point, direction=None):
    """Límite del cociente incremental de f en v = point (por ambos lados si direction es None)."""
    expr = (f.subs(v, point + h) - f.subs(v, point)) / h
    if direction is None:
        lm = sp.limit(expr, h, 0, "-")
        lp = sp.limit(expr, h, 0, "+")
        require(lm == lp, f"laterales distintos: {lm} y {lp}")
        return lp
    return sp.limit(expr, h, 0, direction)


def tangent(f, v, point):
    return sp.simplify(f.subs(v, point) + d(f, v).subs(v, point) * (v - point))


# ---------------------------------------------------------------- Ejercicios 1 a 4
@check("U3.A.E01", "Secantes de x^2 en (1,1): tabla, pendiente genérica, límite y tangente", page=P)
def _():
    f = x ** 2
    for xv, ms in [(2, 3), (sp.Rational(3, 2), sp.Rational(5, 2)), (sp.Rational(11, 10), sp.Rational(21, 10)),
                   (sp.Rational(101, 100), sp.Rational(201, 100)), (sp.Rational(1001, 1000), sp.Rational(2001, 1000)),
                   (0, 1), (sp.Rational(1, 2), sp.Rational(3, 2)), (sp.Rational(9, 10), sp.Rational(19, 10)),
                   (sp.Rational(99, 100), sp.Rational(199, 100)), (sp.Rational(999, 1000), sp.Rational(1999, 1000))]:
        same((f.subs(x, xv) - 1) / (xv - 1), ms, f"secante x={xv}")
    same(sp.cancel((x ** 2 - 1) / (x - 1)), x + 1, "pendiente genérica")
    same(sp.limit(x + 1, x, 1), 2, "límite")
    same(tangent(f, x, 1), 2 * x - 1, "tangente")


@check("U3.A.E02", "Velocidades medias de s=5t^2 en t=2 y velocidad instantánea", page=P)
def _():
    s_ = 5 * t ** 2
    vm = lambda a_, b_: (s_.subs(t, b_) - s_.subs(t, a_)) / (b_ - a_)
    R = sp.Rational
    for (i, j), v in {(2, R(5, 2)): R(45, 2), (2, R(21, 10)): R(41, 2), (2, R(41, 20)): R(81, 4),
                      (2, R(2001, 1000)): R(20005, 1000), (R(3, 2), 2): R(35, 2), (R(19, 10), 2): R(39, 2),
                      (R(39, 20), 2): R(79, 4), (R(1999, 1000), 2): R(19995, 1000)}.items():
        same(vm(i, j), v, f"vm[{i},{j}]")
    same(sp.limit((s_.subs(t, 2 + h) - 20) / h, h, 0), 20, "v(2)")


@check("U3.A.E03", "Derivadas por definición del ejercicio 3 (a a i) y dominios", page=P)
def _():
    k, c = sp.symbols("k c", real=True)
    cases = {"a": (x ** 2 + 2 * x, 2 * x + 2), "b": (1 / x, -1 / x ** 2), "c": (sp.sqrt(x), 1 / (2 * sp.sqrt(x))),
             "d": (1 / sp.sqrt(x), -1 / (2 * sp.sqrt(x ** 3))), "e": (sp.sin(x), sp.cos(x)),
             "f": (sp.log(x), 1 / x), "g": (sp.exp(x), sp.exp(x)), "h": (c + 0 * x, sp.Integer(0)), "i": (k * x, k)}
    for name, (f, fp) in cases.items():
        xv = pos if name in "cdf" else x
        lim = sp.limit(((f.subs(x, xv + h) - f.subs(x, xv)) / h), h, 0, "+")
        same(lim, fp.subs(x, xv), f"3{name} por definición")
        same(d(f.subs(x, xv), xv), fp.subs(x, xv), f"3{name} por reglas")
    # dominio de f' en 0 para sqrt: derivada lateral derecha infinita
    require(sp.limit(sp.sqrt(h) / h, h, 0, "+") == sp.oo, "tangente vertical de sqrt en 0")


@check("U3.A.E04", "Rectas tangentes del ejercicio 4", page=P)
def _():
    same(tangent(5 - 3 * x, x, 3), 5 - 3 * x, "4a")
    same(tangent(x ** 3, x, 1), 3 * x - 2, "4b")
    same(tangent(2 * sp.sqrt(x), x, 9), x / 3 + 3, "4c")


# ---------------------------------------------------------------- Ejercicio 5
@check("U3.A.E05", "Continuidad y derivabilidad del ejercicio 5 (a a e) con laterales", page=P)
def _():
    # a) en x=2 y en x=-1
    same(sp.limit(x + 3, x, -1, "-"), 2, "5a lim -1-")
    same(sp.limit(x ** 2, x, -1, "+"), 1, "5a lim -1+")
    same(sp.limit(x ** 2, x, 2), 4, "5a continua en 2")
    same(sp.limit(x + 2, x, 2), 4, "5a continua en 2 (der)")
    same(d(x ** 2).subs(x, 2), 4, "5a f'_-(2)")
    same(d(x + 2), 1, "5a f'_+(2)")
    # b) |x-3|
    g = sp.Abs(x - 3)
    same(sp.limit((g.subs(x, 3 + h) - 0) / h, h, 0, "-"), -1, "5b g'_-")
    same(sp.limit((g.subs(x, 3 + h) - 0) / h, h, 0, "+"), 1, "5b g'_+")
    # c) x^(2/3): laterales infinitos de signo opuesto (cúspide)
    require(sp.limit(h ** sp.Rational(-1, 3), h, 0, "+") == sp.oo, "5c lateral derecha infinita")
    same(sp.Rational(2, 3) * x ** sp.Rational(-1, 3), d(x ** sp.Rational(2, 3)), "5c derivada para x>0")
    require(sp.limit(sp.Rational(2, 3) * x ** sp.Rational(-1, 3), x, 0, "+") == sp.oo, "5c lim n' en 0+")
    # por la izquierda n(x) = (-x)^(2/3) y n'(x) = -(2/3)(-x)^(-1/3) -> -oo: cúspide (tangente vertical x = 0, laterales de signo opuesto)
    xn = sp.symbols("xn", negative=True)
    require(sp.limit(d((-xn) ** sp.Rational(2, 3), xn), xn, 0, "-") == -sp.oo, "5c lim n' en 0- (cúspide)")
    # d) x|x|
    f = x * sp.Abs(x)
    same(sp.limit(f.subs(x, h) / h, h, 0, "+"), 0, "5d f'_+")
    same(sp.limit(f.subs(x, h) / h, h, 0, "-"), 0, "5d f'_-")
    # e) h(x)=x+2|1-2x|
    hh = x + 2 * (2 * x - 1)
    hl = x + 2 * (1 - 2 * x)
    same(hh.subs(x, sp.Rational(1, 2)), hl.subs(x, sp.Rational(1, 2)), "5e continua")
    same([d(hl), d(hh)], [-3, 5], "5e laterales")


# ---------------------------------------------------------------- Ejercicio 6
@check("U3.A.E06", "Derivadas del ejercicio 6 (a a s)", page=P)
def _():
    R = sp.Rational
    mm, bb, nn = sp.symbols("m b n", positive=True)
    aa = sp.symbols("a", positive=True)
    xp = pos
    cases = [
        ("a", x ** 5 - 2 * x ** 4 + sp.sqrt(3), 5 * x ** 4 - 8 * x ** 3),
        ("b", sp.sqrt(xp) + R(3, 2) * xp ** R(2, 3) - xp ** R(3, 4) + R(34, 100) / xp ** 5,
         1 / (2 * sp.sqrt(xp)) + 1 / xp ** R(1, 3) - 3 / (4 * xp ** R(1, 4)) - R(17, 10) / xp ** 6),
        ("c", (z ** 3 - z ** 2 + 1) / 5, (3 * z ** 2 - 2 * z) / 5),
        ("d", x / mm - mm / bb + x ** 2 / nn ** 2, 1 / mm + 2 * x / nn ** 2),
        ("e", sp.exp(xp) - 2 * sp.log(xp) + sp.sqrt(5 * xp ** 3),
         sp.exp(xp) - 2 / xp + 3 * sp.sqrt(5) / 2 * sp.sqrt(xp)),
        ("f", sp.sin(t) / 3 - 4 * sp.cos(t), sp.cos(t) / 3 + 4 * sp.sin(t)),
        ("g", sp.sin(t) * sp.cos(t), sp.cos(t) ** 2 - sp.sin(t) ** 2),
        ("h", (-x ** 2 + x / 4) * sp.exp(x), sp.exp(x) * (-x ** 2 - R(7, 4) * x + R(1, 4))),
        ("i", 3 * xp * (sp.sqrt(xp) + sp.sin(xp)), R(9, 2) * sp.sqrt(xp) + 3 * sp.sin(xp) + 3 * xp * sp.cos(xp)),
        ("j", 2 * t * sp.sin(t) - (t ** 2 - 2) * sp.cos(t), t ** 2 * sp.sin(t)),
        ("k", xp ** 3 * sp.log(xp) - xp ** 3 / 3, 3 * xp ** 2 * sp.log(xp)),
        ("l", sp.log(xp) / xp, (1 - sp.log(xp)) / xp ** 2),
        ("ll", t / (t + aa / t), 2 * aa * t / (t ** 2 + aa) ** 2),
        ("m", (sp.sqrt(s) - 1) / (sp.sqrt(s) + 1), 1 / (sp.sqrt(s) * (sp.sqrt(s) + 1) ** 2)),
        ("n", sp.cot(x) * (3 * x + 2), -(3 * x + 2) / sp.sin(x) ** 2 + 3 * sp.cot(x)),
        ("o", xp ** 2 / sp.log(xp), xp * (2 * sp.log(xp) - 1) / sp.log(xp) ** 2),
        ("p", (sp.sin(x) + sp.cos(x)) / sp.cos(x), 1 / sp.cos(x) ** 2),
        ("q", z ** 2 * sp.sin(z) + 2 * z * sp.cos(z) - 2 * sp.sin(z), z ** 2 * sp.cos(z)),
        ("r", sp.exp(x) / x, sp.exp(x) * (x - 1) / x ** 2),
        ("s", sp.cos(t) / (1 + sp.sin(t)), -1 / (1 + sp.sin(t))),
    ]
    for name, f, fp in cases:
        v = next(iter(f.free_symbols - {mm, bb, nn, aa}))
        same(d(f, v), fp, f"6{name}")


@check("U3.A.E06e.discrepancia", "6e: la respuesta oficial 3*sqrt(5)*x^2 no es la derivada de sqrt(5x^3)", page=P)
def _():
    f = sp.sqrt(5 * pos ** 3)
    pagina = 3 * sp.sqrt(5) / 2 * sp.sqrt(pos)
    oficial = 3 * sp.sqrt(5) * pos ** 2
    same(d(f, pos), pagina, "derivada correcta")
    require(sp.simplify(d(f, pos) - oficial) != 0, "la oficial no coincide")
    # evidencia numérica en x = 4: correcta 3*sqrt(5), oficial 48*sqrt(5)
    same(d(f, pos).subs(pos, 4), 3 * sp.sqrt(5), "valor en 4")
    same(oficial.subs(pos, 4), 48 * sp.sqrt(5), "valor oficial en 4")


# ---------------------------------------------------------------- Ejercicios 7 a 19
@check("U3.A.E07", "Tangente por (4,3) y (0,2): f(4)=3, f'(4)=1/4", page=P)
def _():
    same(sp.Rational(3 - 2, 4 - 0), sp.Rational(1, 4), "pendiente")


@check("U3.A.E08", "Tangentes perpendiculares de y=x e y=1/x", page=P)
def _():
    same(sp.solve(sp.Eq(x, 1 / x), x), [-1, 1], "intersecciones")
    for xv in (-1, 1):
        same(d(x).subs(x, xv) * d(1 / x).subs(x, xv), -1, f"producto de pendientes en {xv}")


@check("U3.A.E09", "Tangente horizontal de x+2 sen x", page=P)
def _():
    same(d(x + 2 * sp.sin(x)), 1 + 2 * sp.cos(x), "derivada")
    for k in range(-2, 3):
        for base in (2 * sp.pi / 3, 4 * sp.pi / 3):
            same(1 + 2 * sp.cos(base + 2 * k * sp.pi), 0, "f'=0")
    sols = sp.solveset(sp.Eq(1 + 2 * sp.cos(x), 0), x, sp.Interval(0, 2 * sp.pi))
    same(sorted(sols, key=float), [2 * sp.pi / 3, 4 * sp.pi / 3], "soluciones en [0,2pi]")


@check("U3.A.E10", "Normal a y=x-x^2 en (1,0) y su otra intersección", page=P)
def _():
    f = x - x ** 2
    same(d(f).subs(x, 1), -1, "f'(1)")
    normal = 0 + (-1 / d(f).subs(x, 1)) * (x - 1)
    same(normal, x - 1, "normal")
    same(sp.solve(sp.Eq(f, normal), x), [-1, 1], "intersecciones")
    same(normal.subs(x, -1), -2, "ordenada")


@check("U3.A.E11", "Ángulo de inclinación de la tangente a sen x en pi", page=P)
def _():
    same(d(sp.sin(x)).subs(x, sp.pi), -1, "pendiente")
    same(sp.tan(sp.Rational(135, 180) * sp.pi), -1, "tan 135°")


@check("U3.A.E12", "Puntos con tangente a 45° en x/(1-x^2)", page=P)
def _():
    f = x / (1 - x ** 2)
    same(d(f), (1 + x ** 2) / (1 - x ** 2) ** 2, "derivada")
    sols = sp.solve(sp.Eq(d(f), 1), x)
    same(sorted(sols, key=float), [-sp.sqrt(3), 0, sp.sqrt(3)], "abscisas")
    same([f.subs(x, v) for v in (0, sp.sqrt(3), -sp.sqrt(3))], [0, -sp.sqrt(3) / 2, sp.sqrt(3) / 2], "ordenadas")
    same(sp.factor(x ** 4 - 3 * x ** 2), x ** 2 * (x - sp.sqrt(3)) * (x + sp.sqrt(3)), "factorización")


@check("U3.A.E13", "Tangentes a 1/x y 1/x^2 y sus intersecciones", page=P)
def _():
    aa = sp.symbols("a", positive=True)
    f = 1 / x
    tg = f.subs(x, aa) + d(f).subs(x, aa) * (x - aa)
    same(sp.simplify(tg), 2 / aa - x / aa ** 2, "tangente a 1/x")
    same(sp.together(f - tg), (x - aa) ** 2 / (aa ** 2 * x), "1/x - tangente = (x-a)^2/(a^2 x)")
    same(sp.expand(aa ** 2 - 2 * aa * x + x ** 2), sp.expand((x - aa) ** 2), "raíz doble")
    g = 1 / x ** 2
    tg2 = g.subs(x, aa) + d(g).subs(x, aa) * (x - aa)
    same(sp.simplify(tg2), 3 / aa ** 2 - 2 * x / aa ** 3, "tangente a 1/x^2")
    same(sp.expand(2 * x ** 3 - 3 * aa * x ** 2 + aa ** 3), sp.expand((x - aa) ** 2 * (2 * x + aa)), "factorización")
    same(g.subs(x, -aa / 2), 4 / aa ** 2, "ordenada del segundo punto")
    same(tg2.subs(x, -aa / 2), 4 / aa ** 2, "pertenece a la tangente")


@check("U3.A.E14", "Normal a 60° en y=(1-x)/(1+x): abscisas y ordenadas (corrige P1 ≈ (-2,861; -2,075))", page=P)
def _():
    f = (1 - x) / (1 + x)
    same(sp.simplify(d(f)), -2 / (1 + x) ** 2, "derivada")
    rr = sp.root(12, 4)
    xs = [-1 - rr, -1 + rr]
    for xv in xs:
        same(d(f).subs(x, xv), -1 / sp.sqrt(3), f"f'({xv})")
    y1, y2 = [f.subs(x, xv) for xv in xs]
    same(y1, (2 + rr) / (-rr), "y1 exacta")
    same(y2, (2 - rr) / rr, "y2 exacta")
    require(abs(float(xs[0]) + 2.861) < 5e-4 and abs(float(y1) + 2.075) < 5e-4, f"P1 ≈ ({float(xs[0])}, {float(y1)})")
    require(abs(float(xs[1]) - 0.861) < 5e-4 and abs(float(y2) - 0.075) < 5e-4, "P2 aproximado")
    require(abs(float(y1) - 3.303) > 1, "el valor 3,303 de la versión anterior era erróneo")


@check("U3.A.E15", "Tangente paralela a 3x-y+6=0 en x*sqrt(x)", page=P)
def _():
    f = x * sp.sqrt(x)
    same(sp.solve(sp.Eq(d(f), 3), x), [4], "abscisa")
    same(f.subs(x, 4), 8, "ordenada")


@check("U3.A.E16", "a para que y=9x+24 sea tangente a ax/(2x+3) en x=-2", page=P)
def _():
    f = a * x / (2 * x + 3)
    sol = sp.solve(sp.Eq(f.subs(x, -2), 6), a)
    same(sol, [3], "a")
    same(f.subs(a, 3).subs(x, -2), 6, "f(-2)")
    same(sp.simplify(d(f)), 3 * a / (2 * x + 3) ** 2, "derivada")
    same(d(f).subs({a: 3, x: -2}), 9, "pendiente")


@check("U3.A.E17", "a, b para tangente y=2x-4 en x=1 de ax^3+bx^2+x", page=P)
def _():
    f = a * x ** 3 + b * x ** 2 + x
    sol = sp.solve([sp.Eq(f.subs(x, 1), -2), sp.Eq(d(f).subs(x, 1), 2)], [a, b])
    same([sol[a], sol[b]], [7, -10], "a, b")


@check("U3.A.E18", "x+ln x tiene tangente por el origen en x=e", page=P)
def _():
    f = x + sp.log(x)
    aa = sp.symbols("a", positive=True)
    tg = f.subs(x, aa) + d(f).subs(x, aa) * (0 - aa)
    same(sp.solve(sp.Eq(tg, 0), aa), [sp.E], "a=e")
    same(f.subs(x, sp.E), sp.E + 1, "f(e)")
    same(tangent(f, x, sp.E), (1 + 1 / sp.E) * x, "tangente")


@check("U3.A.E19", "Tangentes a 4x-x^2 por (2,5)", page=P)
def _():
    f = 4 * x - x ** 2
    sols = sp.solve(sp.Eq(5 - f.subs(x, a), d(f).subs(x, a) * (2 - a)), a)
    same(sorted(sols), [1, 3], "abscisas")
    same(sp.expand(5 - 4 * a + a ** 2 - (8 - 8 * a + 2 * a ** 2)), sp.expand(-(a ** 2 - 4 * a + 3)), "ecuación")
    same(tangent(f, x, 1), 2 * x + 1, "tangente 1")
    same(tangent(f, x, 3), -2 * x + 9, "tangente 2")


# ---------------------------------------------------------------- Ejercicio 20
@check("U3.A.E20", "Derivadas por regla de la cadena del ejercicio 20 (a a r)", page=P)
def _():
    aa = sp.symbols("a", positive=True)
    xp, tp = pos, sp.symbols("tp", positive=True)
    sq = sp.sqrt
    uu = (1 - sq(xp)) / (1 + sq(xp))
    cases = [
        ("a", sp.cbrt(x ** 2 + 2 * x), (2 * x + 2) / (3 * (x ** 2 + 2 * x) ** sp.Rational(2, 3)), x),
        ("b", sp.exp(-x ** 2), -2 * x * sp.exp(-x ** 2), x),
        ("c", sp.sin(t) ** 2, 2 * sp.sin(t) * sp.cos(t), t),
        ("d", sp.cos(sq(xp)), -sp.sin(sq(xp)) / (2 * sq(xp)), xp),
        ("e", sq(x ** 2 + aa ** 2), x / sq(x ** 2 + aa ** 2), x),
        ("f", sp.log(3 * x ** 2 + 5 * x ** 4) ** 4, 4 * (6 * x + 20 * x ** 3) * sp.log(3 * x ** 2 + 5 * x ** 4) ** 3 / (3 * x ** 2 + 5 * x ** 4), x),
        ("g", sq(sp.log(xp ** 2)), 1 / (xp * sq(sp.log(xp ** 2))), xp),
        ("h", sp.sin(tp / sq(tp + 1)), sp.cos(tp / sq(tp + 1)) * (tp + 2) / (2 * (tp + 1) ** sp.Rational(3, 2)), tp),
        ("i", sp.log(xp) ** 2 + sp.log(sp.log(xp)), (2 * sp.log(xp) + 1 / sp.log(xp)) / xp, xp),
        ("j", sp.log(sq((1 + x) / (1 - x))), 1 / (1 - x ** 2), x),
        ("k", sp.log(2 * xp) + sp.log(2) + sp.log(2 * xp, 10), 1 / xp + 1 / (xp * sp.log(10)), xp),
        ("l", 2 ** sp.sin(sq(tp)) * sp.cos(sq(tp)),
         sp.log(2) * 2 ** sp.sin(sq(tp)) * sp.cos(sq(tp)) ** 2 / (2 * sq(tp)) - 2 ** sp.sin(sq(tp)) * sp.sin(sq(tp)) / (2 * sq(tp)), tp),
        ("m", sp.cbrt(sp.tan(2 * r)), sp.Rational(2, 3) * sp.tan(2 * r) ** sp.Rational(-2, 3) / sp.cos(2 * r) ** 2, r),
        ("n", sp.cos(x ** 2 - sp.sin(x)) * sp.tan(2 * x),
         -sp.sin(x ** 2 - sp.sin(x)) * (2 * x - sp.cos(x)) * sp.tan(2 * x) + 2 * sp.cos(x ** 2 - sp.sin(x)) / sp.cos(2 * x) ** 2, x),
        ("o", 10 ** (z * sp.tan(z)), 10 ** (z * sp.tan(z)) * sp.log(10) * (sp.tan(z) + z / sp.cos(z) ** 2), z),
        ("p", sq(1 + xp) - sp.log(1 + sq(1 + xp)), 1 / (2 + 2 * sq(1 + xp)), xp),
        ("q", (2 * x ** 3 + 3) ** 2 / sp.log(x ** 2 + 1),
         (12 * x ** 2 * (2 * x ** 3 + 3) * sp.log(x ** 2 + 1) - (2 * x ** 3 + 3) ** 2 * 2 * x / (x ** 2 + 1)) / sp.log(x ** 2 + 1) ** 2, x),
        ("r", sp.cos(uu) ** 2, sp.sin(2 * uu) / (sq(xp) * (1 + sq(xp)) ** 2), xp),
    ]
    for name, f, fp, v in cases:
        same(d(f, v), fp, f"20{name}")


@check("U3.A.E20.q.oficial", "20q: la respuesta oficial coincide con la página (con la fracción interpretada)", page=P)
def _():
    num = 12 * x ** 2 * (2 * x ** 3 + 3) * sp.log(x ** 2 + 1) - (2 * x ** 3 + 3) ** 2 * 2 * x / (x ** 2 + 1)
    pub = (2 * x ** 3 + 3) ** 2 / sp.log(x ** 2 + 1)
    same(d(pub), num / sp.log(x ** 2 + 1) ** 2, "derivada")
    # forma oficial: 2x(2x^3+3)[6x ln(x^2+1) - (2x^3+3)/(x^2+1)]/ln^2(x^2+1)
    oficial = 2 * x * (2 * x ** 3 + 3) * (6 * x * sp.log(x ** 2 + 1) - (2 * x ** 3 + 3) / (x ** 2 + 1)) / sp.log(x ** 2 + 1) ** 2
    same(d(pub), oficial, "forma oficial")


# ---------------------------------------------------------------- Ejercicios 21 a 23
@check("U3.A.E21", "Tangente a g(x)=f(-x^2+sen(pi x)) en x=1 con f tangente y=-5x+3 en -1", page=P)
def _():
    u = -x ** 2 + sp.sin(sp.pi * x)
    same(u.subs(x, 1), -1, "u(1)")
    same(d(u).subs(x, 1), -2 - sp.pi, "u'(1)")
    same(-5 * (-1) + 3, 8, "f(-1)")
    same((-5) * (-2 - sp.pi), 10 + 5 * sp.pi, "g'(1)")


@check("U3.A.E22", "a, b de a x^2 e^(x^3-1) + b con tangente y=-5x+8 en x=1", page=P)
def _():
    f = a * x ** 2 * sp.exp(x ** 3 - 1) + b
    same(sp.simplify(d(f, x)), a * sp.exp(x ** 3 - 1) * (2 * x + 3 * x ** 4), "derivada")
    sol = sp.solve([sp.Eq(f.subs(x, 1), 3), sp.Eq(d(f).subs(x, 1), -5)], [a, b])
    same([sol[a], sol[b]], [-1, 4], "a, b")


@check("U3.A.E23", "Ejercicio 23: derivadas con datos por tangente (a a d)", page=P)
def _():
    # a) f(0)=0, f'(0)=2, g(1)=4; g'(1) arbitrario: debe no influir
    gp = sp.symbols("gp")
    same(sp.simplify((2 * 1 * 4 - 0 * gp * 1) / 4 ** 2), sp.Rational(1, 2), "23a")
    xa = sp.symbols("xa")
    f0 = sp.Function("F")
    G, Gp = sp.symbols("G Gp")
    same(sp.simplify(((2 * (1 / (xa + 1)) * G - 0 * Gp * sp.exp(xa)) / G ** 2).subs(xa, 0).subs(G, 4)), sp.Rational(1, 2), "23a general")
    # b)
    f = x / (x ** 2 + 1)
    same(d(f).subs(x, -1), 0, "f'(-1)")
    same(d(f).subs(x, -1) * 2, 0, "23b")
    # c)
    gg = sp.exp(x ** 2) / (2 * x - 3)
    same(gg.subs(x, 1), -sp.E, "g(1)")
    same(d(gg).subs(x, 1), -4 * sp.E, "g'(1)")
    same((-3) * (-sp.E) + 2 * (-4 * sp.E), -5 * sp.E, "23c")
    # d)
    hd = (1 / (x - 9)).subs(x, x ** 2 - 16)
    same(sp.simplify(hd), 1 / (x ** 2 - 25), "h")
    same(d(hd).subs(x, 0), 0, "h'(0)")
    same(hd.subs(x, 0), -sp.Rational(1, 25), "h(0)")


# ---------------------------------------------------------------- Ejercicios 24 a 26
@check("U3.A.E24", "x^2 sen(1/x): continua y derivable en 0, f' discontinua en 0", page=P)
def _():
    f = x ** 2 * sp.sin(1 / x)
    same(sp.limit(f, x, 0), 0, "continuidad")
    same(sp.limit(h * sp.sin(1 / h), h, 0), 0, "f'(0)")
    fp = d(f)
    same(fp, 2 * x * sp.sin(1 / x) - sp.cos(1 / x), "f'(x) para x != 0")
    # f' toma los valores -1 y 1 en sucesiones que tienden a 0
    for k in (10, 100, 1000):
        a1, a2 = 1 / (2 * k * sp.pi), 1 / ((2 * k + 1) * sp.pi)
        same(fp.subs(x, a1), -1, "f' en 1/(2k pi)")
        same(fp.subs(x, a2), 1, "f' en 1/((2k+1)pi)")


@check("U3.A.E25", "m, b para derivabilidad en R (a, b, c)", page=P)
def _():
    sol = sp.solve([sp.Eq(4, 2 * m + b), sp.Eq(4, m)], [m, b])
    same([sol[m], sol[b]], [4, -4], "25a")
    f = x * sp.exp(-1 / x)
    same(sp.limit(f, x, 0, "+"), 0, "25b límite")
    same(sp.limit(f / x, x, 0, "+"), 0, "25b derivada lateral derecha")
    sol = sp.solve([sp.Eq(8 * m, 4 + b), sp.Eq(12 * m, 4)], [m, b])
    same([sol[m], sol[b]], [sp.Rational(1, 3), -sp.Rational(4, 3)], "25c")


@check("U3.A.E26", "Tangentes de x|x| paralelas a y=4x-6", page=P)
def _():
    f = lambda v: v * abs(v)
    same(d(x ** 2), 2 * x, "f' para x>0")
    same(d(-x ** 2), -2 * x, "f' para x<0")
    for xv in (2, -2):
        same(2 * abs(xv), 4, "pendiente")
    same([f(2), f(-2)], [4, -4], "ordenadas")
    same(4 + 4 * (x - 2), 4 * x - 4, "tangente en 2")
    same(-4 + 4 * (x + 2), 4 * x + 4, "tangente en -2")


# ---------------------------------------------------------------- Ejercicios 27 a 31
@check("U3.A.E27", "Movimiento s=t^3-6t^2+9t", page=P)
def _():
    s_ = t ** 3 - 6 * t ** 2 + 9 * t
    v = d(s_, t)
    same(v, 3 * t ** 2 - 12 * t + 9, "v")
    same(sp.factor(v), 3 * (t - 1) * (t - 3), "factorización")
    same([v.subs(t, 2), v.subs(t, 4)], [-3, 9], "v(2), v(4)")
    same(sorted(sp.solve(v, t)), [1, 3], "reposo")
    same([s_.subs(t, k) for k in (0, 1, 3, 5)], [0, 4, 0, 20], "posiciones")
    same(abs(4 - 0) + abs(0 - 4) + abs(20 - 0), 28, "distancia")


@check("U3.A.E28", "Dos partículas s1=t^2-4t, s2=3t-t^2", page=P)
def _():
    s1, s2 = t ** 2 - 4 * t, 3 * t - t ** 2
    same([s1.subs(t, 1), s2.subs(t, 1), s1.subs(t, 4), s2.subs(t, 4)], [-3, 2, 0, -4], "posiciones")
    same([s1.subs(t, 6), s2.subs(t, 6)], [12, -18], "finales")
    same([s1.subs(t, 2), s2.subs(t, sp.Rational(3, 2))], [-4, sp.Rational(9, 4)], "vértices")
    sol = sp.solve(sp.Eq(d(s1, t), d(s2, t)), t)
    same(sol, [sp.Rational(7, 4)], "t")
    same(d(s1, t).subs(t, sol[0]), -sp.Rational(1, 2), "velocidad común")


@check("U3.A.E29", "Vaciado V(t)=5000(1-t/40)^2", page=P)
def _():
    V = 5000 * (1 - t / 40) ** 2
    same([V.subs(t, 0), V.subs(t, 40)], [5000, 0], "extremos")
    same(sp.simplify(d(V, t)), -250 * (1 - t / 40), "V'")
    same(d(V, t).subs(t, 20), -125, "V'(20)")
    l = sp.symbols("l", positive=True)
    inv = 40 - 40 * sp.sqrt(l / 5000)
    same(sp.simplify(V.subs(t, inv)), l, "V(V^-1(l)) = l")


@check("U3.A.E30", "Clavadista s=-16t^2+16t+32", page=P)
def _():
    s_ = -16 * t ** 2 + 16 * t + 32
    same(sorted(sp.solve(s_, t)), [-1, 2], "raíces")
    same(sp.factor(t ** 2 - t - 2), (t - 2) * (t + 1), "factorización")
    same(d(s_, t).subs(t, 2), -48, "v(2)")


@check("U3.A.E31", "Enfriamiento C=20+70e^(-0,1t)", page=P)
def _():
    C = 20 + 70 * sp.exp(-sp.Rational(1, 10) * t)
    same(d(C, t), -7 * sp.exp(-t / 10), "C'")
    same(d(C, t) + sp.Rational(1, 10) * (C - 20), 0, "C' = -0,1 (C-20)")
    require(abs(float(d(C, t).subs(t, 5)) + 4.246) < 5e-4, "C'(5) ≈ -4,246")
    same(sp.limit(d(C, t), t, sp.oo), 0, "límite")


# ---------------------------------------------------------------- Ejercicios 32 y 33
@check("U3.A.E32", "Derivada de la inversa: tangente a f^-1 y (f^-1)'(-2)", page=P)
def _():
    same(3 * (x - 4) + 2, 3 * x - 10, "32a")
    f = x ** 3 + x - 2
    sol_real = [v for v in sp.solve(sp.Eq(f, -2), x) if v.is_real]
    same(sol_real, [0], "a real")
    same(1 / d(f).subs(x, 0), 1, "32b")
    require(sp.simplify(d(f) - (3 * x ** 2 + 1)) == 0 and d(f).subs(x, 0) == 1, "f' = 3x^2+1 > 0: f inyectiva")


@check("U3.A.E33", "Derivadas con trigonométricas inversas", page=P)
def _():
    same(d(sp.exp(sp.asin(3 * x))), sp.exp(sp.asin(3 * x)) * 3 / sp.sqrt(1 - 9 * x ** 2), "33a")
    same(d(x * sp.acos(2 * x)), sp.acos(2 * x) - 2 * x / sp.sqrt(1 - 4 * x ** 2), "33b")
    g = sp.Function("g")
    hh = sp.atan(x) / g(x)
    G0 = sp.symbols("G0", positive=True)
    hp = d(hh).subs(sp.Derivative(g(x), x), 0).subs(x, 0).subs(g(0), G0)
    same(sp.simplify(hp), 1 / G0, "33c")


# ---------------------------------------------------------------- Ejercicios 34 a 38
@check("U3.A.E34", "Derivación implícita (a a d) y tangentes de 34b", page=P)
def _():
    A, B = sp.symbols("A B", positive=True)
    same(sp.idiff(x ** 2 / A ** 2 + y ** 2 / B ** 2 - 1, y, x), -B ** 2 * x / (A ** 2 * y), "34a")
    same(sp.idiff(y ** 3 - 3 * y + 2 * x, y, x), -2 / (3 * (y ** 2 - 1)), "34b")
    for pt in ((-1, 2), (-1, -1)):
        same(pt[1] ** 3 - 3 * pt[1] + 2 * pt[0], 0, f"{pt} en la curva")
    same(-sp.Rational(2, 9) * (x + 1) + 2, -sp.Rational(2, 9) * x + sp.Rational(16, 9), "tangente en (-1,2)")
    same(sp.idiff(2 * y - 2 - x * y ** 3, y, x), y ** 3 / (2 - 3 * x * y ** 2), "34c")
    same(sp.idiff(x ** 2 * y - x * y ** 2 + x ** 2 + y ** 2, y, x), (y ** 2 - 2 * x * y - 2 * x) / (x ** 2 + 2 * y - 2 * x * y), "34d")


@check("U3.A.E35", "Folium de Descartes: normal en (3/2,3/2) pasa por el origen", page=P)
def _():
    F = x ** 3 + y ** 3 - 3 * x * y
    R = sp.Rational
    same(F.subs({x: R(3, 2), y: R(3, 2)}), 0, "punto en la curva")
    yp = sp.idiff(F, y, x)
    same(yp, (y - x ** 2) / (y ** 2 - x), "y'")
    same(yp.subs({x: R(3, 2), y: R(3, 2)}), -1, "pendiente")
    same(R(3, 2) + 1 * (0 - R(3, 2)), 0, "normal pasa por el origen")


@check("U3.A.E36", "x^2-xy+y^2=27: tangentes horizontales y verticales", page=P)
def _():
    F = x ** 2 - x * y + y ** 2 - 27
    same(sp.idiff(F, y, x), (y - 2 * x) / (2 * y - x), "y'")
    for pt in ((3, 6), (-3, -6)):
        same(F.subs({x: pt[0], y: pt[1]}), 0, "horizontal en la curva")
        same((y - 2 * x).subs({x: pt[0], y: pt[1]}), 0, "numerador nulo")
    for pt in ((6, 3), (-6, -3)):
        same(F.subs({x: pt[0], y: pt[1]}), 0, "vertical en la curva")
        same((2 * y - x).subs({x: pt[0], y: pt[1]}), 0, "denominador nulo")
    # son todos los puntos
    sh = sp.solve([F, y - 2 * x], [x, y])
    sv = sp.solve([F, x - 2 * y], [x, y])
    same(sorted(sh), [(-3, -6), (3, 6)], "horizontales")
    same(sorted(sv), [(-6, -3), (6, 3)], "verticales")


@check("U3.A.E37", "a para tangente horizontal de x^2-xy+y^2=a en x=2", page=P)
def _():
    aa = 2 ** 2 - 2 * 4 + 4 ** 2
    same(aa, 12, "a")
    sol = sp.solve([x ** 2 - x * y + y ** 2 - 12, y - 2 * x], [x, y])
    same(sorted(sol), [(-2, -4), (2, 4)], "puntos")


@check("U3.A.E38", "(x-2)^2-y^2=9: tangente en (7,4) paralela a y=5/4 x+9 y otro punto", page=P)
def _():
    F = (x - 2) ** 2 - y ** 2 - 9
    same(F.subs({x: 7, y: 4}), 0, "punto")
    yp = sp.idiff(F, y, x)
    same(yp, (x - 2) / y, "y'")
    same(yp.subs({x: 7, y: 4}), sp.Rational(5, 4), "pendiente")
    sol = sp.solve([F, (x - 2) - sp.Rational(5, 4) * y], [x, y])
    same(sorted(sol), [(-3, -4), (7, 4)], "puntos con esa pendiente")


# ---------------------------------------------------------------- Ejercicios 39 a 41
@check("U3.A.E39", "Derivación logarítmica del ejercicio 39", page=P)
def _():
    xp = pos
    L = sp.log
    cases = [
        (xp ** xp, xp ** xp * (1 + L(xp))),
        (xp ** L(xp), xp ** L(xp) * 2 * L(xp) / xp),
        (sp.sin(xp) ** xp, sp.sin(xp) ** xp * (L(sp.sin(xp)) + xp * sp.cot(xp))),
        (sp.exp(xp ** xp), sp.exp(xp ** xp) * xp ** xp * (1 + L(xp))),
        ((2 + sp.cos(xp)) ** (xp + 1), (2 + sp.cos(xp)) ** (xp + 1) * (L(2 + sp.cos(xp)) - (xp + 1) * sp.sin(xp) / (2 + sp.cos(xp)))),
        ((xp + 1) ** (xp ** 2), (xp + 1) ** (xp ** 2) * (2 * xp * L(xp + 1) + xp ** 2 / (xp + 1))),
    ]
    for i, (f, fp) in enumerate(cases):
        same(d(f, xp), fp, f"39{'abcdef'[i]}")


@check("U3.A.E40", "Derivadas del ejercicio 40", page=P)
def _():
    xp = sp.symbols("xp", positive=True)
    L = sp.log
    sx = sp.sin(xp)
    cases = [
        (3 ** xp, 3 ** xp * L(3)),
        ((sx ** 3) ** L(xp), (sx ** 3) ** L(xp) * 3 * (L(sx) / xp + L(xp) * sp.cot(xp))),
        (sp.cos(xp) ** sp.exp(xp), sp.cos(xp) ** sp.exp(xp) * sp.exp(xp) * (L(sp.cos(xp)) - sp.tan(xp))),
        (xp ** (1 / xp), xp ** (1 / xp) * (1 - L(xp)) / xp ** 2),
        (2 ** sx + sp.sqrt(sp.sin(3 * xp)), 2 ** sx * L(2) * sp.cos(xp) + 3 * sp.cos(3 * xp) / (2 * sp.sqrt(sp.sin(3 * xp)))),
        (sx ** (xp ** 2) + sp.pi * sp.exp(xp), sx ** (xp ** 2) * (2 * xp * L(sx) + xp ** 2 * sp.cot(xp)) + sp.pi * sp.exp(xp)),
    ]
    for i, (f, fp) in enumerate(cases):
        # se comprueba sobre un intervalo donde sen x > 0, cos x > 0 y sen 3x > 0
        for v in (sp.Rational(1, 10), sp.Rational(3, 10), sp.Rational(1, 2)):
            require(abs(float(d(f, xp).subs(xp, v) - fp.subs(xp, v))) < 1e-12, f"40{'abcdef'[i]} en {v}")
        if i in (0, 3):
            same(sp.simplify(d(f, xp) - fp), 0, f"40{'abcdef'[i]} simbólico")


@check("U3.A.E41", "Tangente a (1-x)^(3/(x+1)) en x=0", page=P)
def _():
    f = (1 - x) ** (3 / (x + 1))
    same(f.subs(x, 0), 1, "f(0)")
    same(sp.limit(d(f), x, 0), -3, "f'(0)")
    lf = 3 / (x + 1) * sp.log(1 - x)
    same(d(lf).subs(x, 0), -3, "(ln f)'(0)")
    same(sp.limit(sp.simplify(d(f)), x, 0), -3, "f'(0) simplificada")


# ---------------------------------------------------------------- Ejercicio 42
@check("U3.A.E42", "V/F del ejercicio 42: justificaciones comprobables", page=P)
def _():
    # b) tangente a x^2 en (-2,4)
    same(d(x ** 2).subs(x, -2), -4, "pendiente en -2")
    # d) tangente a 1/x^2 corta en otro punto (ver ejercicio 13b); x^3 en 0 no sirve de contraejemplo
    aa = 1
    f = 1 / x ** 2
    tg = f.subs(x, aa) + d(f).subs(x, aa) * (x - aa)
    same(sp.simplify(f.subs(x, -sp.Rational(aa, 2)) - tg.subs(x, -sp.Rational(aa, 2))), 0, "1/x^2 y su tangente en x=1 se cortan en x=-1/2")
    # tangente a x^3 en 0 es y=0 y solo corta en x=0
    same(sp.solve(sp.Eq(x ** 3, 0), x), [0], "x^3 con y=0 solo en 0")
    # g) |x^2+x|
    g = sp.Abs(x ** 2 + x)
    same(d(g).subs(x, -2), -3, "g'(-2) = -3 mientras |2x+1| = 3")
    # i) pi^5 constante
    same(d(sp.pi ** 5 + 0 * x), 0, "i")
    # j)
    same(1 / sp.Integer(4), sp.Rational(1, 4), "j")
    # k) x^2 sen(1/x): derivable con derivada discontinua (ver E24)
    # m) f creciente derivable, Dx>0: Dy>=dy depende de la concavidad: f=sqrt(x) en 1 con dx=3
    f = sp.sqrt(x)
    dy = d(f).subs(x, 1) * 3
    Dy = f.subs(x, 4) - f.subs(x, 1)
    require(Dy < dy, "para sqrt (cóncava) Dy < dy")


# ---------------------------------------------------------------- Adicionales
@check("U3.A.AD1", "H(t)=15 ln(t+1): H'(3) y t con H'=2", page=P)
def _():
    H = 15 * sp.log(t + 1)
    same(d(H, t), 15 / (t + 1), "H'")
    same(d(H, t).subs(t, 3), sp.Rational(15, 4), "H'(3)")
    same(sp.solve(sp.Eq(d(H, t), 2), t), [sp.Rational(13, 2)], "t")


@check("U3.A.AD2", "x^2y+y^2-4x=0: tangentes verticales", page=P)
def _():
    F = x ** 2 * y + y ** 2 - 4 * x
    same(sp.idiff(F, y, x), (4 - 2 * x * y) / (x ** 2 + 2 * y), "y'")
    sol = sp.solve([F, x ** 2 + 2 * y], [x, y], dict=True)
    pts = {(s_[x], s_[y]) for s_ in sol if s_[x].is_real and s_[y].is_real}
    c2 = sp.cbrt(2)
    esperados = {(0, 0), (-2 * c2, -2 * c2 ** 2)}
    for p in esperados:
        require(any(sp.simplify(p[0] - q[0]) == 0 and sp.simplify(p[1] - q[1]) == 0 for q in pts), f"falta {p}")
    require(len(pts) == 2, f"puntos reales: {pts}")
    for p in esperados:
        require(sp.simplify((4 - 2 * x * y).subs({x: p[0], y: p[1]})) != 0, "numerador no nulo")


@check("U3.A.AD3", "h(x)=f(x^3-7) x^2/e^(x-2): h'(2)=-96", page=P)
def _():
    u = lambda fp1: fp1 * 3 * x ** 2
    v = x ** 2 * sp.exp(2 - x)
    same(v.subs(x, 2), 4, "v(2)")
    same(d(v).subs(x, 2), 0, "v'(2)")
    same(u(-2).subs(x, 2) * 4 + 5 * 0, -96, "h'(2)")


@check("U3.A.AD4", "(x+1)^(x^2+x): tangente horizontal en x=0", page=P)
def _():
    hh = (x + 1) ** (x ** 2 + x)
    same(hh.subs(x, 0), 1, "h(0)")
    same(sp.limit(d(hh), x, 0), 0, "h'(0)")
    same(d((x ** 2 + x) * sp.log(x + 1)).subs(x, 0), 0, "(ln h)'(0)")


@check("U3.A.AD5", "h=f∘g^-1: h'(3) = -f'(1)/2", page=P)
def _():
    same(-2 * 1 + 5, 3, "g(1)")
    same(1 / sp.Integer(-2), -sp.Rational(1, 2), "(g^-1)'(3)")


@check("U3.A.AD6", "a para tangente vertical en x=-2 de a x^2-3xy-y^2=21", page=P)
def _():
    F = a * x ** 2 - 3 * x * y - y ** 2 - 21
    same(sp.idiff(F, y, x), (2 * a * x - 3 * y) / (3 * x + 2 * y), "y'")
    same(sp.solve([F.subs({x: -2, y: 3}), 3 * (-2) + 2 * 3], [a], dict=True)[0][a], 3, "a")
    # opciones: a=12 y a=-12 no dan una curva con tangente vertical en x=-2
    for av in (12, -12):
        sols = sp.solve(sp.Eq(F.subs({a: av, x: -2}), 0), y)
        for yv in sols:
            require(sp.simplify((3 * x + 2 * y).subs({x: -2, y: yv})) != 0, f"a={av} no tiene tangente vertical")
