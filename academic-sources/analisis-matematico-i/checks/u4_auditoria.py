"""Auditoría de la Práctica 4 (Unidad 4): recalcula los resultados publicados en la página de práctica y los
contrasta con las respuestas de la guía de la cátedra.

Las cotas de error se comprueban con aritmética racional exacta y desigualdades explícitas.
"""
import sympy as sp
from sympy import Rational as R
from content_pipeline.mathcheck import check, require, same

PG = "/analisis-matematico-i/unidad-4/practica/practica-4/"
x, u = sp.symbols("x u", real=True)


def taylor(f, a, n):
    return sum(sp.diff(f, x, k).subs(x, a) / sp.factorial(k) * (x - a) ** k for k in range(n + 1))


def lagrange_bound(f, a, n, xv):
    """Cota M/(n+1)! |x-a|^(n+1), con M = máximo exacto de |f^(n+1)| en el intervalo entre a y xv."""
    g = sp.diff(f, x, n + 1)
    lo, hi = sorted([sp.nsimplify(a), sp.nsimplify(xv)])
    crit = [c for c in sp.solve(sp.diff(g, x), x) if c.is_real and lo <= c <= hi]
    cand = [abs(g.subs(x, p)) for p in [lo, hi, *crit]]
    M = max(cand)
    return M, M / sp.factorial(n + 1) * abs(xv - a) ** (n + 1)


@check("U4.A.E01", "Orden de contacto de P, Q, R con e^x en 0", page=PG)
def _():
    f = sp.exp(x)
    for pol, order in ((1 - x + x ** 2, 0), (1 + x - x ** 2, 1), (1 + x + x ** 2 / 2, 2)):
        first = 0
        while sp.diff(f, x, first).subs(x, 0) == sp.diff(pol, x, first).subs(x, 0):
            first += 1
        same(first - 1, order, "orden de contacto")


@check("U4.A.E02.a", "Taylor de 1/x en 1, orden 3, y valor en 1,3", page=PG)
def _():
    P = taylor(1 / x, 1, 3)
    same(P, 1 - (x - 1) + (x - 1) ** 2 - (x - 1) ** 3, "P3")
    same(P.subs(x, R(13, 10)), R(763, 1000), "P3(1,3)")


@check("U4.A.E02.b", "Taylor de cos(x-2) en 2, orden 3, y valor en 2,1", page=PG)
def _():
    P = taylor(sp.cos(x - 2), 2, 3)
    same(P, 1 - (x - 2) ** 2 / 2, "P3")
    same(P.subs(x, R(21, 10)), R(995, 1000), "P3(2,1)")


@check("U4.A.E02.c", "Taylor de sqrt(x+1) en 0, orden 3, y valor en -0,15", page=PG)
def _():
    P = taylor(sp.sqrt(x + 1), 0, 3)
    same(P, 1 + x / 2 - x ** 2 / 8 + x ** 3 / 16, "P3")
    v = P.subs(x, -R(15, 100))
    require(abs(float(v) - 0.92197656) < 1e-8, "valor")


@check("U4.A.E03", "Aproximaciones del ejercicio 3: e^(1/2), ln 0,4 y sen 31°", page=PG)
def _():
    require(taylor(sp.exp(x), 0, 4).subs(x, R(1, 2)) == R(211, 128), "P4(1/2)=211/128")
    require(abs(float(R(211, 128)) - 1.6484375) < 1e-12, "decimal")
    P3 = taylor(sp.log(x), 1, 3)
    same(P3, (x - 1) - (x - 1) ** 2 / 2 + (x - 1) ** 3 / 3, "P3 ln")
    same(P3.subs(x, R(2, 5)), -R(852, 1000), "P3(0,4)")
    require(abs(float(sp.log(R(2, 5))) + 0.91629) < 1e-5, "ln 0,4")
    P2 = taylor(sp.sin(x), sp.pi / 6, 2)
    same(P2, R(1, 2) + sp.sqrt(3) / 2 * (x - sp.pi / 6) - (x - sp.pi / 6) ** 2 / 4, "P2 sen")
    require(abs(float(P2.subs(x, 31 * sp.pi / 180)) - 0.515039) < 1e-6, "sen 31 aprox")
    require(abs(float(sp.sin(31 * sp.pi / 180)) - 0.515038) < 1e-6, "sen 31 exacto")


@check("U4.A.E04", "Tabla de P1 y P2 de ln x en 1", page=PG)
def _():
    P1, P2 = taylor(sp.log(x), 1, 1), taylor(sp.log(x), 1, 2)
    same(P1, x - 1, "P1")
    same(sp.expand(P2), -x ** 2 / 2 + 2 * x - R(3, 2), "P2")
    xs = [1, R(5, 4), R(3, 2), R(7, 4), 2]
    same([P1.subs(x, v) for v in xs], [0, R(1, 4), R(1, 2), R(3, 4), 1], "P1 tabla")
    same([P2.subs(x, v) for v in xs], [0, R(7, 32), R(3, 8), R(15, 32), R(1, 2)], "P2 tabla")
    require(abs(float(1 - sp.log(2)) - 0.307) < 1e-3 and abs(float(sp.log(2) - R(1, 2)) - 0.193) < 1e-3, "errores en 2")
    require(all(P1.subs(x, v) >= sp.log(v) for v in xs), "P1 sobreestima")


@check("U4.A.E05", "Maclaurin de orden 2 de (1-u^2)^(-1/2)", page=PG)
def _():
    h = (1 - u ** 2) ** R(-1, 2)
    same([sp.diff(h, u, k).subs(u, 0) for k in range(3)], [1, 0, 1], "derivadas")
    same(sp.simplify(sp.diff(h, u, 2) - ((1 - u ** 2) ** R(-3, 2) + 3 * u ** 2 * (1 - u ** 2) ** R(-5, 2))), 0, "h''")


@check("U4.A.E06", "Ecuaciones con Maclaurin: a-e", page=PG)
def _():
    same(sorted(sp.solve(sp.Eq(x - x ** 3 / 3, x ** 2), x)), sorted([0, (-3 - sp.sqrt(21)) / 2, (-3 + sp.sqrt(21)) / 2]), "a")
    require(abs(float((-3 + sp.sqrt(21)) / 2) - 0.7913) < 1e-4, "a decimal")
    same(sorted(sp.solve(sp.Eq(1 + x + x ** 2 / 2 + x ** 3 / 6, x ** 3 + 1), x)),
         sorted([0, (3 - sp.sqrt(129)) / 10, (3 + sp.sqrt(129)) / 10]), "b")
    require(abs(float((3 + sp.sqrt(129)) / 10) - 1.43578) < 1e-5 and abs(float((3 - sp.sqrt(129)) / 10) + 0.835782) < 1e-6, "b dec")
    same(sp.solve(sp.Eq(x - x ** 2 / 2, x + x ** 2), x), [0], "c")
    same(sorted(sp.solve(sp.Eq(x - x ** 3 / 6, x / 2), x)), sorted([0, sp.sqrt(3), -sp.sqrt(3)]), "d")
    same(sp.solve(sp.Eq(x ** 3 / 6, x ** 3), x), [0], "e")
    # c) la ecuación original solo tiene x = 0 (ln(1+x) <= x < x + x^2 para x != 0, x > -1)
    for v in (R(-9, 10), R(-1, 2), R(-1, 10), R(1, 10), 1, 10):
        require(sp.log(1 + v) < v + v ** 2, f"ln(1+x) < x+x^2 en {v}")


@check("U4.A.E07", "f=1+3x+sen x: P4, f(1/3) y cota de R4", page=PG)
def _():
    f = 1 + 3 * x + sp.sin(x)
    P = taylor(f, 0, 4)
    same(P, 1 + 4 * x - x ** 3 / 6, "P4")
    same(P.subs(x, R(1, 3)), R(1, 1) + R(4, 3) - R(1, 162), "P4(1/3)")
    require(abs(float(P.subs(x, R(1, 3))) - 2.327160) < 1e-6, "P4(1/3)")
    bound = R(1, 120) * R(1, 3) ** 5
    same(bound, R(1, 29160), "cota")
    require(bound < R(35, 10 ** 6), "cota < 0,000035")
    err = f.subs(x, R(1, 3)) - P.subs(x, R(1, 3))
    require(0 < float(err) <= float(bound), "error real dentro de la cota")
    require(abs(float(f.subs(x, R(1, 3))) - 2.327195) < 1e-6, "f(1/3)")


@check("U4.A.E08.a", "sqrt(16,5) con Taylor de orden 2 en 0 y cota", page=PG)
def _():
    f = sp.sqrt(16 + x)
    P = taylor(f, 0, 2)
    same(P, 4 + x / 8 - x ** 2 / 512, "P2")
    same(P.subs(x, R(1, 2)), R(4, 1) + R(1, 16) - R(1, 2048), "P2(1/2)")
    M, b = lagrange_bound(f, 0, 2, R(1, 2))
    same(M, R(3, 8192), "M")
    same(b, R(1, 131072), "cota")
    require(b < R(8, 10 ** 6), "cota < 8e-6")
    require(float(b) > 7.6e-6, "cota ≈ 7,6e-6")
    require(0 < float(f.subs(x, R(1, 2)) - P.subs(x, R(1, 2))) <= float(b), "error real")


@check("U4.A.E08.b", "ln(1,23) con P3 en 1 y cota", page=PG)
def _():
    f = sp.log(x)
    P = taylor(f, 1, 3)
    v = P.subs(x, R(123, 100))
    require(abs(float(v) - 0.207606) < 1e-6, "P3(1,23)")
    M, b = lagrange_bound(f, 1, 3, R(123, 100))
    same(M, 6, "M")
    same(b, R(1, 4) * R(23, 100) ** 4, "cota")
    require(abs(float(b) - 0.0006996) < 1e-7, "cota decimal")
    require(0 < float(v - sp.log(R(123, 100))) <= float(b), "error real")


@check("U4.A.E09", "e^(-1/3) con P5: cota 1/524880 estricta", page=PG)
def _():
    P = taylor(sp.exp(x), 0, 5)
    v = P.subs(x, -R(1, 3))
    require(abs(float(v) - 0.7165294925) < 1e-9, "P5(-1/3)")
    b = R(1, 720) * R(1, 3) ** 6
    same(b, R(1, 524880), "cota")
    err = abs(sp.exp(-R(1, 3)) - v)
    require(float(err) < float(b), "error real menor que la cota")


@check("U4.A.E10", "x ln x: P3 en 1, f(1,5) y cota", page=PG)
def _():
    f = x * sp.log(x)
    P = taylor(f, 1, 3)
    same(P, (x - 1) + (x - 1) ** 2 / 2 - (x - 1) ** 3 / 6, "P3")
    same(P.subs(x, R(3, 2)), R(29, 48), "P3(3/2)")
    M, b = lagrange_bound(f, 1, 3, R(3, 2))
    same(M, 2, "M")
    same(b, R(1, 192), "cota")
    require(abs(float(b) - 0.00520833) < 1e-8, "cota decimal")
    require(0 < float(f.subs(x, R(3, 2)) - P.subs(x, R(3, 2))) <= float(b), "error real")


@check("U4.A.E11.a", "sen(ax+b): a=4, b=pi/4 da P1 = (sqrt2/2)(1+4x)", page=PG)
def _():
    a_, b_ = sp.symbols("a b", real=True)
    f = sp.sin(a_ * x + b_)
    p1 = f.subs(x, 0) + sp.diff(f, x).subs(x, 0) * x
    got = p1.subs({a_: 4, b_: sp.pi / 4})
    same(got, sp.sqrt(2) / 2 * (1 + 4 * x), "P1")


@check("U4.A.E11.b", "a ln(bx+1): a=5, b=-3", page=PG)
def _():
    a_, b_ = sp.symbols("a b")
    f = a_ * sp.log(b_ * x + 1)
    c1, c2 = sp.diff(f, x).subs(x, 0), sp.diff(f, x, 2).subs(x, 0) / 2
    sol = sp.solve([sp.Eq(c1, -15), sp.Eq(c2, -R(45, 2))], [a_, b_], dict=True)
    same([(s[a_], s[b_]) for s in sol], [(5, -3)], "(a,b)")


@check("U4.A.E12", "ln(ax+b) con Maclaurin 6x: a=6, b=1; ln(1,06)", page=PG)
def _():
    a_, b_ = sp.symbols("a b", positive=True)
    f = a_ * x + b_
    sol = sp.solve([sp.Eq(sp.log(f).subs(x, 0), 0), sp.Eq(sp.diff(sp.log(f), x).subs(x, 0), 6)], [a_, b_], dict=True)
    same([(s[a_], s[b_]) for s in sol], [(6, 1)], "(a,b)")
    g = sp.log(6 * x + 1)
    same(taylor(g, 0, 2), 6 * x - 18 * x ** 2, "P2")
    same(taylor(g, 0, 2).subs(x, R(1, 100)), R(582, 10000), "P2(0,01)")
    M, b = lagrange_bound(g, 0, 1, R(1, 100))
    same(M, 36, "M")
    same(b, R(18, 10000), "cota")
    require(abs(float(6 * R(1, 100) - sp.log(R(106, 100)))) <= float(b), "error real de P1 dentro de la cota")


@check("U4.A.E13", "(5x+1)f'+f=1, f(0)=2: P3 = 2 - x + 3x^2 - 11x^3", page=PG)
def _():
    P = 2 - x + 3 * x ** 2 - 11 * x ** 3
    # la ecuación diferencial se cumple hasta el orden 2 al reemplazar f por P (orden de contacto)
    resid = sp.expand((5 * x + 1) * sp.diff(P, x) + P - 1)
    same([resid.coeff(x, k) for k in range(3)], [0, 0, 0], "residuo hasta x^2")
    c = sp.symbols("c0:4")
    Q = sum(c[k] * x ** k for k in range(4))
    r = sp.expand((5 * x + 1) * sp.diff(Q, x) + Q - 1)
    sol = sp.solve([r.coeff(x, k) for k in range(3)] + [sp.Eq(c[0], 2)], c, dict=True)
    same([sol[0][c[k]] for k in range(4)], [2, -1, 3, -11], "coeficientes de f (de la ecuación, orden <= 3)")


@check("U4.A.E14", "g = 1-3x+sqrt(f) con P2 = 2-x+3x^2: P2 de f = 1+4x+10x^2", page=PG)
def _():
    Pf = 1 + 4 * x + 10 * x ** 2
    g = 1 - 3 * x + sp.sqrt(Pf)
    same(taylor(g, 0, 2), 2 - x + 3 * x ** 2, "g reproduce P2")


@check("U4.A.E15", "Verdadero/falso de la práctica 4", page=PG)
def _():
    same(taylor(sp.exp(x), 0, 4), 1 + x + x ** 2 / 2 + x ** 3 / 6 + x ** 4 / 24, "a: falso")
    # b) como está transcripto en la guía, el coeficiente de x^6 es f^(6)(0)/6!: lo comprobamos con sen^2 x
    f = sp.sin(x) ** 2
    same(taylor(f, 0, 9).coeff(x, 6), sp.diff(f, x, 6).subs(x, 0) / sp.factorial(6), "b: es verdadero como está escrito")
    # c) contraejemplo: el resto no se evalúa en a
    f = sp.exp(x)
    same(f.subs(x, 1) - taylor(f, 0, 1).subs(x, 1), sp.E - 2, "R1(1)")
    require(sp.diff(f, x, 2).subs(x, 0) * R(1, 2) != sp.E - 2, "c: f''(a)/2 != R1(1)")
    # d) polinomio de grado 3
    f = x ** 3 - 2 * x ** 2 + 3 * x + 5
    same(sp.expand(taylor(f, 1, 3)), sp.expand(f), "d")
    # e) impar => solo potencias impares (ejemplo con tan x y comprobación general de simetría)
    g = sp.tan(x)
    same([taylor(g, 0, 9).coeff(x, k) for k in (0, 2, 4, 6, 8)], [0] * 5, "e")
    # g
    P = -8 + 3 * (x - 2) ** 2 + 3 * (x - 2) ** 4 + (x - 2) ** 5
    same(sp.diff(P, x, 4).subs(x, 2), 72, "g: f^(4)(2) = 72")


@check("U4.A.A1", "Adicional 1: g(x) = 2/f(5x)", page=PG)
def _():
    Pf = 2 - (x - 5) + 3 * (x - 5) ** 2
    g = 2 / Pf.subs(x, 5 * x)
    same([sp.diff(g, x, k).subs(x, 1) for k in range(3)], [1, R(5, 2), -R(125, 2)], "derivadas")
    same(taylor(g, 1, 2), 1 + R(5, 2) * (x - 1) - R(125, 4) * (x - 1) ** 2, "P2")


@check("U4.A.A2", "Adicional 2: sqrt(1+3x)", page=PG)
def _():
    g = sp.sqrt(1 + 3 * x)
    P = taylor(g, 0, 3)
    same(P, 1 + R(3, 2) * x - R(9, 8) * x ** 2 + R(27, 16) * x ** 3, "P3")
    same(P.subs(x, R(1, 10)), R(11404375, 10 ** 7), "P3(0,1)")
    require(abs(float(g.subs(x, R(1, 10)) - P.subs(x, R(1, 10))) - (-0.000262)) < 1e-6, "error ≈ 0,00026")
    require(abs(float(P.subs(x, 2)) - 13) < 1e-12 and abs(float(g.subs(x, 2)) - 2.6458) < 1e-4, "en x=2 no sirve")


@check("U4.A.A3", "Adicional 3: m = cos(pi-2x) en pi/2", page=PG)
def _():
    m = sp.cos(sp.pi - 2 * x)
    P = taylor(m, sp.pi / 2, 3)
    same(sp.simplify(P - (1 - 2 * (x - sp.pi / 2) ** 2)), 0, "P3")
    require(abs(float(P.subs(x, R(13, 10))) - 0.853339) < 1e-6, "P3(1,3)")
    require(abs(float(m.subs(x, R(13, 10))) - 0.856889) < 1e-6, "m(1,3)")


@check("U4.A.A4", "Adicional 4: ln(x-1) = -(x-1)^2+3 con P2 en 2 da x = -1 ± sqrt13 (opción e)", page=PG)
def _():
    P = taylor(sp.log(x - 1), 2, 2)
    same(P, (x - 2) - (x - 2) ** 2 / 2, "P2")
    sol = sp.solve(sp.Eq(P, -(x - 1) ** 2 + 3), x)
    same(sorted(sol, key=float), sorted([-1 - sp.sqrt(13), -1 + sp.sqrt(13)], key=float), "S")
    # la opción d) {1 ± sqrt13} NO es solución de la ecuación aproximada
    for s in (1 + sp.sqrt(13), 1 - sp.sqrt(13)):
        require(sp.simplify(P.subs(x, s) - (-(s - 1) ** 2 + 3)) != 0, "opción d no cumple")


@check("U4.A.A5", "Adicional 5: P6^(5)(a) = f^(5)(a)", page=PG)
def _():
    a_ = sp.symbols("a")
    f = sp.exp(2 * x) * sp.sin(x)
    P = taylor(f, R(1, 3), 6)
    same(sp.diff(P, x, 5).subs(x, R(1, 3)), sp.diff(f, x, 5).subs(x, R(1, 3)), "P^(5)(a) = f^(5)(a)")


@check("U4.A.E15.b", "15b: el coeficiente de x^6 del Mac Laurin de orden 9 es f^(6)(0)/6! (la oficial marca falso: errónea)", page=PG)
def _():
    for f in (sp.sin(x) ** 2, sp.exp(x) * sp.cos(x), sp.log(1 + x ** 2)):
        same(taylor(f, 0, 9).coeff(x, 6), sp.diff(f, x, 6).subs(x, 0) / sp.factorial(6), "coeficiente de x^6")
