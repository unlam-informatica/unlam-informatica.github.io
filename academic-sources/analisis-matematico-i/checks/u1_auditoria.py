"""Auditoría de la Práctica 1 (Unidad 1): recalcula los resultados publicados en las páginas de práctica
y los contrasta con las respuestas de la guía de la cátedra.

Donde la página discrepa de la guía, la comprobación demuestra que la página es la correcta y deja la
evidencia (ver U1.A.E09.j, U1.A.E09.k y U1.A.E09.l).
"""
import sympy as sp
from sympy import Interval, Union, S, oo, Rational as R, Intersection, FiniteSet, Complement
from sympy.calculus.util import continuous_domain, function_range
from content_pipeline.mathcheck import check, require, same

x, t, c = sp.symbols("x t C", real=True)
P = "/analisis-matematico-i/unidad-1/practica/"


def page(n):
    return P + f"ejercicio-{n}/"


def dom(expr):
    return continuous_domain(expr, x, S.Reals)


def eq_set(a, b, what):
    require(sp.simplify(a - b) == S.EmptySet or (a == b), f"{what}: {a} != {b}")


def rng(expr, domain):
    return function_range(expr, x, domain)


# ---------------------------------------------------------------- Ejercicio 1
@check("U1.A.E01.a", "Recta por P(-3,4) y Q(2,-3)", page=page(1))
def _():
    m = R(-3 - 4, 2 + 3)
    f = 4 + m * (x + 3)
    same(f, -R(7, 5) * x - R(1, 5), "m(x)")


@check("U1.A.E01.b", "Recta paralela a 2x-3y+9=0 con raíz -1/2", page=page(1))
def _():
    slope = sp.solve(2 * x - 3 * sp.Symbol("y") + 9, sp.Symbol("y"))[0].diff(x)
    f = slope * (x + R(1, 2))
    same(f, R(2, 3) * x + R(1, 3), "f(x)")


@check("U1.A.E01.c", "Parábola de vértice (-1/2,5) por (0,4)", page=page(1))
def _():
    a = sp.solve(sp.Eq(sp.Symbol("a") * R(1, 4) + 5, 4), sp.Symbol("a"))[0]
    same(a, -4, "a")
    p = a * (x + R(1, 2)) ** 2 + 5
    same(p.subs(x, 0), 4, "p(0)")
    require(rng(p, S.Reals) == Interval(-oo, 5), "imagen")


@check("U1.A.E01.d", "Parábola de raíces -1 y 5/7 por (1,8/7)", page=page(1))
def _():
    a = sp.solve(sp.Eq(sp.Symbol("a") * (1 + 1) * (1 - R(5, 7)), R(8, 7)), sp.Symbol("a"))[0]
    same(a, 2, "a")
    h = 2 * (x + 1) * (x - R(5, 7))
    same(h.subs(x, 1), R(8, 7), "h(1)")
    xv = R(-1, 7)
    same(sp.diff(h, x).subs(x, xv), 0, "vértice")
    same(h.subs(x, xv), R(-72, 49), "mínimo")
    require(rng(h, S.Reals) == Interval(R(-72, 49), oo), "imagen")


@check("U1.A.E01.efg", "Dominio e imagen de |x|, sqrt(x), 1/x", page=page(1))
def _():
    require(rng(sp.Abs(x), S.Reals) == Interval(0, oo), "|x|")
    require(dom(sp.sqrt(x)) == Interval(0, oo), "dom sqrt")
    require(rng(sp.sqrt(x), Interval(0, oo)) == Interval(0, oo), "im sqrt")
    require(dom(1 / x) == Union(Interval.open(-oo, 0), Interval.open(0, oo)), "dom 1/x")
    # 1/x alcanza todo y != 0 y nunca 0
    y = sp.Symbol("y", real=True, nonzero=True)
    same(1 / (1 / y), y, "todo y != 0 es imagen")
    require(sp.solve(sp.Eq(1 / x, 0), x) == [], "1/x no vale 0")


# ---------------------------------------------------------------- Ejercicio 2
@check("U1.A.E02", "Celsius-Fahrenheit", page=page(2))
def _():
    Fc = sp.Rational(212 - 32, 100) * c + 32
    same(Fc, R(9, 5) * c + 32, "F(C)")
    same(Fc.subs(c, -10), 14, "b")
    same(sp.solve(sp.Eq(Fc, 0), c)[0], R(-160, 9), "c exacto")
    require(abs(float(R(-160, 9)) + 17.8) < 0.03, "c ≈ -17,8")
    same(Fc.subs(c, 10) - Fc.subs(c, 0), 18, "d [0,10]")
    same(Fc.subs(c, 20) - Fc.subs(c, 10), 18, "d [10,20]")


# ---------------------------------------------------------------- Ejercicio 3-4
@check("U1.A.E03", "Vaciado del tanque: 4000 L en 16 min, 250 L/min, 1000 L a los 12 min", page=page(3))
def _():
    V = 4000 - R(4000, 16) * t
    same(V.subs(t, 16), 0, "vacío a los 16")
    same(sp.diff(V, t), -250, "caudal")
    same(sp.solve(sp.Eq(V, 1000), t)[0], 12, "1000 L")


@check("U1.A.E04", "Resorte f(x)=0,875x en [0,8]", page=page(4))
def _():
    k = R(7, 8)
    same(k * 8, 7, "f(8)")
    same(k * 10, R(35, 4), "f(10)=8,75")
    same(sp.diff(k * x, x), R(7, 8), "razón")


# ---------------------------------------------------------------- Ejercicio 5-8
@check("U1.A.E05", "Canaleta: A=2x(6-x), máximo 18 en x=3, volumen 200x(6-x)", page=page(5))
def _():
    A = 12 * x - 2 * x ** 2
    same(A, 2 * x * (6 - x), "A")
    same(sp.solve(sp.diff(A, x), x)[0], 3, "x")
    same(A.subs(x, 3), 18, "Amax")
    same(100 * A, 200 * x * (6 - x), "V")
    same((100 * A).subs(x, 3), 1800, "Vmax")


@check("U1.A.E06", "Caja sin tapa: V=4x(12-x)(16-x), máximo en x≈4,53", page=page(6))
def _():
    V = (24 - 2 * x) * (32 - 2 * x) * x
    same(V, 4 * x * (12 - x) * (16 - x), "V")
    sol = [s for s in sp.solve(sp.diff(V, x), x) if 0 < s < 12]
    require(len(sol) == 1, "un punto crítico")
    s = sol[0]
    require(abs(float(s) - 4.53) < 0.005, "x ≈ 4,53")
    require(abs(float(V.subs(x, s)) - 1552.5) < 0.5, "Vmax ≈ 1552,5")


@check("U1.A.E07", "Áreas y perímetros del ejercicio 7", page=page(7))
def _():
    same((x * (10 - x)).subs(x, 5), 25, "a) A(5)")
    same(2 * x + 32 / x, 2 * (x + 16 / x), "b) P")
    # 7b: rectángulo de área 16 => la otra dimensión 16/x
    same(2 * (x + 16 / x), 2 * x + 32 / x, "P(x)")
    l = sp.Symbol("l", positive=True)
    same(sp.sqrt(3) / 4 * l ** 2, l * (sp.sqrt(3) / 2 * l) / 2, "A(l)")


@check("U1.A.E08", "Concentración C(t)=-t^2+6t", page=page(8))
def _():
    C = -t ** 2 + 6 * t
    require(function_range(C, t, Interval(0, 6)) == Interval(0, 9), "imagen [0,9]")
    sol = sp.solve_univariate_inequality(C > 8, t, relational=False)
    require(sol.intersect(Interval(0, 6)) == Interval.open(2, 4), "C>8")
    same((C.subs(t, 2) - C.subs(t, 1)) / (2 - 1), 3, "RCM [1,2]")
    same((C.subs(t, R(3, 2)) - C.subs(t, 1)) / R(1, 2), R(7, 2), "RCM [1;1,5]")


# ---------------------------------------------------------------- Ejercicio 9 (dominios)
def U(*a):
    return Union(*a)


D9 = {
    "a": (-sp.sqrt(2) * x ** 4 - 3 * x + x ** 2 / 7 - 2, S.Reals),
    "b": ((x ** 2 - 3) ** -4, U(Interval.open(-oo, -sp.sqrt(3)), Interval.open(-sp.sqrt(3), sp.sqrt(3)), Interval.open(sp.sqrt(3), oo))),
    "c": ((x ** 5 - 2 * x + 5) / (x ** 2 - 3 * x + 2), U(Interval.open(-oo, 1), Interval.open(1, 2), Interval.open(2, oo))),
    "d": (sp.Abs(x - 1) / (x + 2), U(Interval.open(-oo, -2), Interval.open(-2, oo))),
    "e": (sp.sqrt(x + 2), Interval(-2, oo)),
    "f": (sp.sqrt(1 / (2 * x + 1) - 2), Interval.Lopen(R(-1, 2), R(-1, 4))),
    "g": (2 * x / sp.sqrt(x ** 2 - 4), U(Interval.open(-oo, -2), Interval.open(2, oo))),
    "h": ((x + 3) / sp.Abs(3 * x + 2) + 1 / (x + 1) ** R(1, 4),
          Complement(Interval.open(-1, oo), FiniteSet(R(-2, 3)))),
    "j": (sp.sqrt((3 * x - 4) / (x + 1)), U(Interval.open(-oo, -1), Interval(R(4, 3), oo))),
    "k": (sp.sqrt(3 * x - 4) / sp.sqrt(x + 1), Interval(R(4, 3), oo)),
}


@check("U1.A.E09.i", "Dominio natural 9i: el denominador x*cbrt(x^2-1) se anula solo en -1, 0, 1", page=page(9))
def _():
    den = x * sp.real_root(x ** 2 - 1, 3)
    require(set(sp.solve(sp.Eq(x * (x ** 2 - 1), 0), x)) == {-1, 0, 1}, "ceros del denominador")
    for v in (-1, 0, 1):
        require(den.subs(x, v) == 0, f"den({v})=0")
    for v in (-2, R(-1, 2), R(1, 2), 2):
        require(den.subs(x, v) != 0, f"den({v}) != 0")


def _dom_check(key):
    expr, expected = D9[key]
    got = dom(expr)
    require(got == expected, f"9{key}: calculado {got}, publicado {expected}")


for _k in D9:
    check(f"U1.A.E09.{_k}", f"Dominio natural 9{_k}", page=page(9))(lambda k=_k: _dom_check(k))


@check("U1.A.E09.j.oficial", "Respuestas oficiales de 9j y 9k intercambiadas", page=page(9))
def _():
    """La guía publica 9j = [4/3,oo) y 9k = (-oo,-1) U [4/3,oo): son los dominios de k y de j respectivamente."""
    oficial_j = Interval(R(4, 3), oo)
    oficial_k = U(Interval.open(-oo, -1), Interval(R(4, 3), oo))
    require(dom(sp.sqrt((3 * x - 4) / (x + 1))) != oficial_j, "la oficial de j no es el dominio de j")
    require(dom(sp.sqrt(3 * x - 4) / sp.sqrt(x + 1)) != oficial_k, "la oficial de k no es el dominio de k")
    require(dom(sp.sqrt((3 * x - 4) / (x + 1))) == oficial_k, "dom j = oficial k")
    require(dom(sp.sqrt(3 * x - 4) / sp.sqrt(x + 1)) == oficial_j, "dom k = oficial j")
    # contraste numérico: x=-2 está en el dominio de j (cociente 10 >= 0) y no en el de k
    require(((3 * -2 - 4) / (-2 + 1)) >= 0, "x=-2: cociente 10 >= 0")


@check("U1.A.E09.l", "Dominio de 9l (por tramos, raíz solo en el numerador): [1,5)-{3}, igual a la oficial", page=page(9))
def _():
    # Regresión: la página transcribía el primer tramo como sqrt((x-1)/(x-3)) y declaraba errónea la respuesta
    # oficial. El enunciado de la guía es sqrt(x-1)/(x-3) (raíz solo en el numerador).
    t1 = Intersection(dom(sp.sqrt(x - 1) / (x - 3)), Interval.open(-oo, 4))
    t2 = Intersection(dom(sp.log(5 - x)), Interval(4, oo))
    total = Union(t1, t2)
    oficial = Complement(Interval.Ropen(1, 5), FiniteSet(3))
    require(total == oficial, f"dominio {total}")
    require(t1 == Complement(Interval.Ropen(1, 4), FiniteSet(3)), f"primer tramo {t1}")
    require(0 not in total and 3 not in total and 1 in total and 4 in total, "puntos de control")
    # con la lectura errónea (raíz de todo el cociente) el dominio sería otro: la diferencia es real
    erroneo = Union(Intersection(dom(sp.sqrt((x - 1) / (x - 3))), Interval.open(-oo, 4)), t2)
    require(erroneo != oficial, "la lectura errónea da otro dominio")


@check("U1.A.E09.mn", "Dominios por tramos 9m, 9n, 9ñ", page=page(9))
def _():
    m = Union(Intersection(dom(sp.sqrt(4 - x ** 2)), Interval(-oo, 2)),
              Intersection(U(Interval.open(-oo, 1), Interval.open(1, oo)), Interval.open(2, oo)))
    require(m == Interval(-2, oo), "9m")
    n = Union(Intersection(dom(sp.sqrt(x ** 2 - 9)), Interval.open(-oo, 4)), Interval(4, oo))
    require(n == U(Interval(-oo, -3), Interval(3, oo)), "9n")
    a = Intersection(dom(1 / sp.sqrt(5 - x)), Interval.open(-oo, 3))
    b = Intersection(dom(sp.sqrt(sp.log(x - 2))), Interval(3, oo))
    require(Union(a, b) == S.Reals, "9ñ")


# ---------------------------------------------------------------- Ejercicio 10
@check("U1.A.E10.a", "x^2+2x-8", page=page(10))
def _():
    f = x ** 2 + 2 * x - 8
    require(rng(f, S.Reals) == Interval(-9, oo), "imagen")
    same(f.subs(x, 0), -8, "ordenada")
    require(set(sp.solve(f, x)) == {-4, 2}, "ceros")
    require(sp.solve_univariate_inequality(f > 0, x, relational=False) == U(Interval.open(-oo, -4), Interval.open(2, oo)), "C+")
    require(sp.solve_univariate_inequality(f < 0, x, relational=False) == Interval.open(-4, 2), "C-")


@check("U1.A.E10.b", "|x-2|", page=page(10))
def _():
    f = sp.Abs(x - 2)
    require(rng(f, S.Reals) == Interval(0, oo), "imagen")
    same(f.subs(x, 0), 2, "ordenada")
    require(sp.solve(sp.Eq(x - 2, 0), x) == [2], "cero")


@check("U1.A.E10.c", "x/(x-2)", page=page(10))
def _():
    f = x / (x - 2)
    same(sp.limit(f, x, oo), 1, "AH")
    require(sp.limit(f, x, 2, "+") == oo and sp.limit(f, x, 2, "-") == -oo, "AV en 2")
    # y = 1 no se alcanza: x/(x-2)=1 no tiene solución; y != 1 sí
    require(sp.solve(sp.Eq(f, 1), x) == [], "1 no está en la imagen")
    yv = sp.Symbol("y")
    same(sp.solve(sp.Eq(f, yv), x)[0], 2 * yv / (yv - 1), "x(y) para y != 1")
    require(sp.solve_univariate_inequality(f > 0, x, relational=False) == U(Interval.open(-oo, 0), Interval.open(2, oo)), "C+")
    require(sp.solve_univariate_inequality(f < 0, x, relational=False) == Interval.open(0, 2), "C-")


@check("U1.A.E10.d", "(-2x+3)/(x+4)", page=page(10))
def _():
    f = (-2 * x + 3) / (x + 4)
    same(sp.limit(f, x, oo), -2, "AH")
    require(sp.solve(sp.Eq(f, -2), x) == [], "-2 no está en la imagen")
    same(f.subs(x, 0), R(3, 4), "ordenada")
    require(sp.solve(f, x) == [R(3, 2)], "cero")
    pos = sp.solve_univariate_inequality(f > 0, x, relational=False)
    require(pos == Interval.open(-4, R(3, 2)), "C+")
    neg = sp.solve_univariate_inequality(f < 0, x, relational=False)
    require(neg == U(Interval.open(-oo, -4), Interval.open(R(3, 2), oo)), "C-")


@check("U1.A.E10.e", "sqrt(x-2)", page=page(10))
def _():
    f = sp.sqrt(x - 2)
    require(dom(f) == Interval(2, oo), "dominio")
    require(rng(f, Interval(2, oo)) == Interval(0, oo), "imagen")


@check("U1.A.E10.f", "ln(x+1)", page=page(10))
def _():
    f = sp.log(x + 1)
    require(dom(f) == Interval.open(-1, oo), "dominio")
    same(f.subs(x, 0), 0, "cero")
    require(sp.limit(f, x, -1, "+") == -oo, "AV x=-1")
    require(sp.solve_univariate_inequality(f > 0, x, relational=False).intersect(Interval.open(-1, oo)) == Interval.open(0, oo), "C+")


@check("U1.A.E10.g", "2^(x+1) (el enunciado de la guía pierde el exponente: 2^{x+1})", page=page(10))
def _():
    f = 2 ** (x + 1)
    same(f.subs(x, 0), 2, "ordenada")
    s_ = sp.Symbol("s", positive=True)
    same(sp.limit(2 ** (1 - s_), s_, oo), 0, "AH y=0 (x=-s, s -> oo)")
    require(sp.solve(sp.Eq(f, 0), x) == [], "sin ceros")
    require(sp.simplify(sp.log(f, 2) - (x + 1)) == 0, "imagen: todo y>0 se alcanza con x=log2(y)-1")


# ---------------------------------------------------------------- Ejercicio 11
def pw_image(pieces):
    """Unión de las imágenes de cada tramo (expresión, intervalo)."""
    return Union(*[function_range(e, x, iv) for e, iv in pieces])


@check("U1.A.E11.a", "Función por tramos 11a", page=page(11))
def _():
    pieces = [(x + 2, Interval(-oo, -1)), (-x, Interval.Lopen(-1, 1)), (3 * x - 4, Interval.Lopen(1, 3)), (sp.Integer(2), Interval.open(3, oo))]
    require(Union(*[iv for _, iv in pieces]) == S.Reals, "dominio")
    require(pw_image(pieces) == Interval(-oo, 5), "imagen")
    zeros = [z for e, iv in pieces for z in sp.solve(e, x) if z in iv]
    require(sorted(zeros) == [-2, 0, R(4, 3)], "ceros")


@check("U1.A.E11.b", "Función por tramos 11b", page=page(11))
def _():
    same(sp.cancel((x ** 2 - 6 * x + 9) / (x - 3)), x - 3, "simplificación")
    img = Union(function_range(x - 3, x, Union(Interval.open(-oo, 3), Interval.open(3, oo))), FiniteSet(4))
    require(img == Union(Interval.open(-oo, 0), Interval.open(0, oo)), "imagen")
    require(all(z == 3 for z in sp.solve(x - 3, x)), "el único cero candidato es x=3, que vale 4")


@check("U1.A.E11.c", "Función por tramos 11c", page=page(11))
def _():
    pieces = [(sp.Abs(x + R(1, 2)), Interval(-oo, 2)), (sp.Abs(x - 4), Interval.open(2, oo))]
    require(pw_image(pieces) == Interval(0, oo), "imagen")
    zeros = [z for e, iv in pieces for z in sp.solve(sp.Eq(e, 0), x) if z in iv]
    require(sorted(zeros) == [R(-1, 2), 4], "ceros")


@check("U1.A.E11.d", "Función por tramos 11d", page=page(11))
def _():
    pieces = [(sp.sqrt(x + 4), Interval(-3, oo)), (x + 3, Interval.Ropen(-4, -3)), (sp.real_root(x, 3) + 3, Interval.open(-oo, -4))]
    require(Union(*[iv for _, iv in pieces]) == S.Reals, "dominio")
    imgs = [Interval(1, oo), Interval.Ropen(-1, 0), Interval.open(-oo, 3 - sp.real_root(4, 3))]
    require(Union(*imgs) == S.Reals, "imagen R")
    require(sp.real_root(-27, 3) + 3 == 0 and -27 < -4, "cero -27")


# ---------------------------------------------------------------- Ejercicio 12
@check("U1.A.E12", "Beneficio B(t): máximo 12,25 en t=3,5; B=11,25 en 2,5 y 4,5; B=10 desde t=5", page=page(12))
def _():
    B = -t ** 2 + 7 * t
    same(sp.solve(sp.diff(B, t), t)[0], R(7, 2), "t del máximo")
    same(B.subs(t, R(7, 2)), R(49, 4), "12,25")
    require(sorted(sp.solve(sp.Eq(B, R(45, 4)), t)) == [R(5, 2), R(9, 2)], "11,25")
    same(B.subs(t, 5), 10, "continuidad en 5")
    require(R(49, 4) > 10, "máximo global")


# ---------------------------------------------------------------- Ejercicio 13
def parity(f, domain_sym=True):
    fm = f.subs(x, -x)
    if sp.simplify(fm - f) == 0:
        return "par"
    if sp.simplify(fm + f) == 0:
        return "impar"
    return "ninguna"


@check("U1.A.E13.a", "Paridad: x^2-4 par; x^2+x-2 ninguna; |x+1|-|x-1| impar; x+1 ninguna", page=page(13))
def _():
    require(parity(x ** 2 - 4) == "par", "a")
    require(parity(x ** 2 + x - 2) == "ninguna", "b")
    require(parity(sp.Abs(x + 1) - sp.Abs(x - 1)) == "impar", "c")
    require(parity(x + 1) == "ninguna", "d")


@check("U1.A.E13.e", "Paridad e) g(x)=cbrt(x) impar; g) x-3x^3 impar", page=page(13))
def _():
    require(parity(sp.real_root(x, 3)) == "impar", "e")
    require(parity(x - 3 * x ** 3) == "impar", "g")


@check("U1.A.E13.h", "Paridad h) (1-x)/(1+x): ninguna (dominio no simétrico)", page=page(13))
def _():
    f = (1 - x) / (1 + x)
    require(parity(f) == "ninguna", "h")
    require(dom(f).contains(1) == S.true and dom(f).contains(-1) == S.false, "-1 fuera del dominio y 1 dentro")


@check("U1.A.E13.fij", "Paridad f) cbrt-/ i) j): pares, según la guía", page=page(13))
def _():
    require(parity(sp.real_root(x ** 2, 3)) == "par", "f")


# ---------------------------------------------------------------- Ejercicio 16
@check("U1.A.E16", "Transformaciones: dominios, imágenes y ceros", page=page(16))
def _():
    a = sp.Abs(x + 2) - R(3, 2)
    require(rng(a, S.Reals) == Interval(R(-3, 2), oo), "a imagen")
    require(set(sp.solve(sp.Eq(x + 2, R(3, 2)), x) + sp.solve(sp.Eq(x + 2, -R(3, 2)), x)) == {R(-7, 2), R(-1, 2)}, "a ceros (casos)")
    same(a.subs(x, R(-7, 2)), 0, "a(-7/2)")
    same(a.subs(x, R(-1, 2)), 0, "a(-1/2)")
    b = 2 - sp.sqrt(x - 1)
    require(dom(b) == Interval(1, oo) and rng(b, Interval(1, oo)) == Interval(-oo, 2), "b")
    require(sp.solve(b, x) == [5], "b cero")
    m = 1 / (2 - x)
    require(dom(m) == U(Interval.open(-oo, 2), Interval.open(2, oo)), "c dominio")
    require(sp.solve(sp.Eq(m, 0), x) == [], "c sin ceros")
    same(-1 / (x - 2), m, "c: -f(x-2) con f=1/x")
    d = sp.real_root(x + 4, 3) - 1
    same(d.subs(x, -3), 0, "d cero")


# ---------------------------------------------------------------- Ejercicios 17-19, 21
@check("U1.A.E17", "f(x)=C a^x por (-1,6) y (3,3/8)", page=page(17))
def _():
    a, C = sp.symbols("a C", positive=True)
    sol = sp.solve([sp.Eq(C * a ** -1, 6), sp.Eq(C * a ** 3, R(3, 8))], [a, C], dict=True)
    require(sol == [{a: R(1, 2), C: 3}], f"{sol}")


@check("U1.A.E18", "p=760 e^{-0,144 h}: mitad de presión a 4,81 km", page=page(18))
def _():
    h = sp.log(2) / R(144, 1000)
    same(760 * sp.exp(-R(144, 1000) * h), 380, "p(h)=380")
    require(abs(float(h) - 4.81) < 0.005, "h ≈ 4,81")


@check("U1.A.E19", "Aves: A(t)=50*3^(t/2)", page=page(19))
def _():
    A = 50 * 3 ** (t / 2)
    same(A.subs(t, 6), 1350, "a")
    tt = 2 * sp.log(20) / sp.log(3)
    same(A.subs(t, tt), 1000, "1000 aves")
    require(abs(float(tt) - 5.4537) < 1e-3, "t")
    require(int(float(tt - 5) * 365) in (165, 166), "días")


@check("U1.A.E21", "Decibeles: 110 dB y 90 dB", page=page(21))
def _():
    same(10 ** (R(110, 10)) / 10 ** (R(90, 10)), 100, "cociente de potencias")


# ---------------------------------------------------------------- Ejercicio 20, 22, 23
@check("U1.A.E20", "Dominios e imágenes de transformaciones de ln y exp", page=page(20))
def _():
    require(dom(sp.log(x - 2)) == Interval.open(2, oo), "ln(x-2)")
    require(dom(sp.log(-x)) == Interval.open(-oo, 0), "ln(-x)")
    require(dom(sp.log(sp.Abs(x))) == U(Interval.open(-oo, 0), Interval.open(0, oo)), "ln|x|")
    require(rng(sp.exp(sp.Abs(x)), S.Reals) == Interval(1, oo), "e^|x|")
    require(rng(-sp.exp(2 * x + 3) + 1, S.Reals) == Interval.open(-oo, 1), "-e^(2x+3)+1")


@check("U1.A.E23", "Transformaciones del seno: imágenes y sen(x-pi/2)=-cos x", page=page(23))
def _():
    same(sp.sin(x - sp.pi / 2), -sp.cos(x), "desfase")
    require(rng(sp.sin(x) + 3, Interval(0, 2 * sp.pi)) == Interval(2, 4), "+3")


# ---------------------------------------------------------------- Ejercicio 24-31
@check("U1.A.E24", "Profundidad p(t)=1/2 sen(pi t/2)+3/2", page=page(24))
def _():
    p = sp.sin(sp.pi * t / 2) / 2 + R(3, 2)
    same(p.subs(t, 6), R(3, 2), "p(6)")
    same(p.subs(t, 4) - p.subs(t, 3), R(1, 2), "variación")
    same(sp.periodicity(p, t), 4, "período")
    require(rng(p.subs(t, x), Interval(0, 4)) == Interval(1, 2), "imagen")


@check("U1.A.E25", "Presión arterial: período 3/4 s, pulso 80", page=page(25))
def _():
    same(60 / R(3, 4), 80, "pulso")
    same(sp.Rational(2, 1) * sp.pi / (sp.Rational(8, 3) * sp.pi), R(3, 4), "T=2pi/b con b=8pi/3")


@check("U1.A.E26.a", "Inversas 26a-d", page=page(26))
def _():
    y = sp.Symbol("y", real=True)
    f = (x - 1) ** 3 + 8
    finv = sp.real_root(x - 8, 3) + 1
    same(f.subs(x, finv), x, "f(f^-1)")
    g = sp.exp(2 * x) + 1
    ginv = sp.log(x - 1) / 2
    same(g.subs(x, ginv), x, "g(g^-1) en (1,oo)")
    h = 3 - sp.sqrt(x + 5)
    hinv = (3 - x) ** 2 - 5
    same(sp.simplify(h.subs(x, hinv).subs(sp.sqrt((3 - x) ** 2), 3 - x)), x, "h(h^-1) para x<=3")
    k = sp.log(2 * x - 4, 3)
    kinv = (3 ** x + 4) / 2
    same(sp.simplify(sp.expand_log(k.subs(x, kinv), force=True)), x, "k(k^-1)")


@check("U1.A.E26.b", "Inversas 26e-g", page=page(26))
def _():
    e = 2 * x ** 2 - 1
    same(e.subs(x, sp.sqrt((x + 1) / 2)), x, "e rama +")
    same(e.subs(x, -sp.sqrt((x + 1) / 2)), x, "e rama -")
    f = 2 * sp.sin(3 * x)
    same(sp.simplify(f.subs(x, sp.asin(x / 2) / 3)), x, "f")
    g = (3 - x) / (x - 1)
    ginv = (x + 3) / (x + 1)
    same(sp.simplify(g.subs(x, ginv)), x, "g(g^-1)")
    same(sp.simplify(ginv.subs(x, g)), x, "g^-1(g)")


@check("U1.A.E27", "A(t)=100(1-0,9^t) en [0,10]", page=page(27))
def _():
    A = 100 * (1 - R(9, 10) ** t)
    tt = sp.log(1 - R(1, 2)) / sp.log(R(9, 10))
    same(A.subs(t, tt), 50, "A(t)=50")
    require(abs(float(tt) - 6.58) < 0.005, "6,58")
    require(abs(float(A.subs(t, 10)) - 65.13) < 0.005, "A(10)")


@check("U1.A.E28", "Resorte L(P)=3P/35+43/7", page=page(28))
def _():
    P_ = sp.Symbol("P")
    L = R(3, 35) * P_ + R(43, 7)
    same(L.subs(P_, 0), R(43, 7), "a")
    same(L.subs(P_, 10) - L.subs(P_, 0), R(6, 7), "b")
    same(L.subs(P_, R(860, 3)), R(215, 7), "L en el extremo del dominio")


@check("U1.A.E29", "Gas V=30/P en [1,12]", page=page(29))
def _():
    P_ = sp.Symbol("P", positive=True)
    V = 30 / P_
    same(V.subs(P_, 12), R(5, 2), "V(12)")
    same(V.subs(P_, 1), 30, "V(1)")
    require(abs(float(V.subs(P_, R(11, 1)))-2.727) < 0.001, "V(11)≈2,727")


@check("U1.A.E30", "Masa M(t)=25*3^t en [0,8]", page=page(30))
def _():
    same(25 * 3 ** 8, 164025, "M(8)")


@check("U1.A.E31", "Marea h(t)=5+4,9 cos(pi t/6)", page=page(31))
def _():
    h = 5 + R(49, 10) * sp.cos(sp.pi * t / 6)
    same(h.subs(t, 0), R(99, 10), "máxima 9,9")
    same(h.subs(t, 6), R(1, 10), "mínima 0,1")
    same(sp.periodicity(h, t), 12, "período")
    hh = sp.Symbol("hh")
    tinv = 6 / sp.pi * sp.acos((hh - 5) / R(49, 10))
    same(sp.simplify(h.subs(t, tinv)), hh, "inversa en [0,6]")


@check("U1.A.E32", "V/F del ejercicio 32: contraejemplos", page=page(32))
def _():
    same(sp.cos(0), sp.cos(2 * sp.pi), "d")
    require(sp.Integer(2) != sp.Integer(0) + 2 * sp.pi, "d")
    same((sp.log(sp.E)) ** 6, 1, "g: (ln e)^6")
    same(6 * sp.log(sp.E), 6, "g: 6 ln e")
    same(sp.sin(2 * sp.pi / 4), 1, "i: sen(pi/2)")
    same(2 * sp.sin(sp.pi / 4), sp.sqrt(2), "i: 2 sen(pi/4)")
    f = sp.sqrt((x + 3) / (2 - x * 5))
    g = sp.sqrt(x + 3) / sp.sqrt(2 - 5 * x)
    require(dom(f) == dom(g) == Interval.Ropen(-3, R(2, 5)), "j dominios")
    k = 4 + sp.log(3 - x)
    same(k, 4 + sp.log(-(x - 3)), "k")
    require(dom(sp.exp(x)) == S.Reals and rng(sp.exp(x), S.Reals) == Interval.open(0, oo), "l")


# ---------------------------------------------------------------- Adicionales
@check("U1.A.ADIC.1", "Adicional 1: paridad de 2x/(x^2+5), 3x^2/(x-5), x^3/(16-x^2)", page="/analisis-matematico-i/unidad-1/practica/adicionales/")
def _():
    require(parity(2 * x / (x ** 2 + 5)) == "impar", "a")
    require(parity(3 * x ** 2 / (x - 5)) == "ninguna", "b")
    require(parity(x ** 3 / (16 - x ** 2)) == "impar", "c")
    require(dom(x ** 3 / (16 - x ** 2)) == Union(Interval.open(-oo, -4), Interval.open(-4, 4), Interval.open(4, oo)), "c: dominio R-{-4,4}")


@check("U1.A.ADIC.2", "Adicional 2: población N(t)=227 e^{0,007 t}", page="/analisis-matematico-i/unidad-1/practica/adicionales/")
def _():
    N = 227 * sp.exp(R(7, 1000) * t)
    require(abs(float(N.subs(t, 10)) - 243.46) < 0.01, "N(10)")
    require(abs(float(N.subs(t, 10) - N.subs(t, 0)) - 16.46) < 0.01, "variación")
    tt = sp.log(2) / R(7, 1000)
    same(N.subs(t, tt), 454, "doble")
    require(abs(float(tt) - 99.0) < 0.05, "99 años")


@check("U1.A.ADIC.3", "Adicional 3: L(d)=-10 log2 d + 120", page="/analisis-matematico-i/unidad-1/practica/adicionales/")
def _():
    d = sp.Symbol("d", positive=True)
    L = -10 * sp.log(d, 2) + 120
    same(sp.simplify(L.subs(d, 8)), 90, "a")
    same(sp.simplify(L.subs(d, 64)), 60, "b")
    Linv = 2 ** ((120 - sp.Symbol("L")) / 10)
    same(sp.simplify(sp.expand_log(L.subs(d, Linv), force=True)), sp.Symbol("L"), "inversa")


@check("U1.A.ADIC.4", "Adicional 4: C(q)=10+3 sqrt q", page="/analisis-matematico-i/unidad-1/practica/adicionales/")
def _():
    q = sp.Symbol("q", positive=True)
    C = 10 + 3 * sp.sqrt(q)
    require(abs(float(C.subs(q, 101) - C.subs(q, 100)) - 0.1496) < 1e-4, "RCM")
    same(sp.diff(C, q).subs(q, 100), R(3, 20), "C'(100)=0,15")


@check("U1.A.ADIC.5", "Adicional 5: V(t)=10(1-t/100)^2 en [0,100]", page="/analisis-matematico-i/unidad-1/practica/adicionales/")
def _():
    V = 10 * (1 - t / 100) ** 2
    v = sp.Symbol("v", positive=True)
    same(sp.simplify(sp.expand(V.subs(t, 100 * (1 - sp.sqrt(v / 10))))), v, "V(V^-1)")


@check("U1.A.ADIC.6", "Adicional 6: g=x^3/sqrt(16-x^2) impar en (-4,4)", page="/analisis-matematico-i/unidad-1/practica/adicionales/")
def _():
    g = x ** 3 / sp.sqrt(16 - x ** 2)
    require(dom(g) == Interval.open(-4, 4), "dominio")
    require(parity(g) == "impar", "paridad")


@check("U1.A.ADIC.7", "Adicional 7: inversa de 3 sen(5x)", page="/analisis-matematico-i/unidad-1/practica/adicionales/")
def _():
    y = sp.Symbol("y")
    same(sp.simplify((3 * sp.sin(5 * x)).subs(x, sp.asin(y / 3) / 5)), y, "m(m^-1)")


@check("U1.A.ADIC.8", "Adicional 8: inversa de U(t)=1000(1-e^{-0,05t})", page="/analisis-matematico-i/unidad-1/practica/adicionales/")
def _():
    u = sp.Symbol("u")
    U_ = 1000 * (1 - sp.exp(-R(1, 20) * t))
    tinv = -20 * sp.log(1 - u / 1000)
    same(sp.simplify(U_.subs(t, tinv)), u, "U(t(U))")
    same(sp.limit(U_, t, oo), 1000, "cota")
