"""Comprobaciones de los ejemplos resueltos de la teoría de la Unidad 4 (Polinomios de Taylor).

Cada función recalcula el ejemplo desde sus datos y verifica los pasos intermedios publicados (derivadas en el
punto, coeficientes, valores aproximados y cotas de error). Las cotas se comprueban con aritmética racional
exacta y desigualdades explícitas; los valores decimales publicados se contrastan con precisión explícita.
"""
import sympy as sp
from content_pipeline.mathcheck import check, require, same

T = "/analisis-matematico-i/unidad-4/teoria/"
P1 = T + "orden-de-contacto/"
P2 = T + "polinomio-de-taylor/"
P3 = T + "termino-complementario/"

x, a, h, t, c = sp.symbols("x a h t c", real=True)
R = sp.Rational


def d(f, k=1, v=x):
    return sp.diff(f, v, k)


def taylor(f, point, n):
    return sum(d(f, k).subs(x, point) / sp.factorial(k) * (x - point) ** k for k in range(n + 1))


def contact_order(f, g, point, kmax=12):
    """Mayor n tal que f^(k)(point) = g^(k)(point) para k = 0..n (−1 si ni siquiera coinciden los valores)."""
    n = -1
    for k in range(kmax):
        if sp.simplify(d(f, k).subs(x, point) - d(g, k).subs(x, point)) == 0:
            n = k
        else:
            return n
    raise AssertionError("las derivadas coinciden hasta kmax")


def dec(value, places=6):
    return float(sp.N(value, 30)) if places is None else round(float(sp.N(value, 30)), places)


def lagrange_bound(f, point, n, xv):
    """M/(n+1)! |x-a|^(n+1) con M = máximo exacto de |f^(n+1)| en el intervalo entre a y xv."""
    g = d(f, n + 1)
    lo, hi = sorted([sp.nsimplify(point), sp.nsimplify(xv)])
    crit = [s for s in sp.solve(d(g), x) if s.is_real and lo <= s <= hi]
    M = max(abs(g.subs(x, p)) for p in [lo, hi, *crit])
    return M, M / sp.factorial(n + 1) * abs(xv - point) ** (n + 1)


# ---------------------------------------------------------------------------
# 4.1 Orden de contacto y polinomio por sus derivadas
# ---------------------------------------------------------------------------
@check("U4.T.CON.1", "sen x y x tienen contacto de orden 2 en 0", page=P1)
def _():
    f, g = sp.sin(x), x
    same([d(f, k).subs(x, 0) for k in range(4)], [0, 1, 0, -1], "derivadas de sen x")
    same([d(g, k).subs(x, 0) for k in range(4)], [0, 1, 0, 0], "derivadas de x")
    same(contact_order(f, g, 0), 2, "orden de contacto")


@check("U4.T.CON.2", "cos x y 1-x^2/2+x^4/24: contacto de orden 5 en 0", page=P1)
def _():
    f, g = sp.cos(x), 1 - x ** 2 / 2 + x ** 4 / 24
    same([d(f, k).subs(x, 0) for k in range(7)], [1, 0, -1, 0, 1, 0, -1], "cos")
    same([d(g, k).subs(x, 0) for k in range(7)], [1, 0, -1, 0, 1, 0, 0], "g")
    same(contact_order(f, g, 0), 5, "orden de contacto")


@check("U4.T.CON.3", "x^3 y 3x-2: contacto de orden 1 en a=1 y de orden 0 en a=-2", page=P1)
def _():
    f, g = x ** 3, 3 * x - 2
    same(sp.factor(f - g), (x - 1) ** 2 * (x + 2), "factorización de f-g")
    same([d(f, k).subs(x, 1) for k in range(3)], [1, 3, 6], "f en 1")
    same([d(g, k).subs(x, 1) for k in range(3)], [1, 3, 0], "g en 1")
    same(contact_order(f, g, 1), 1, "orden en 1")
    same(f.subs(x, -2), -8, "f(-2)")
    same(g.subs(x, -2), -8, "g(-2)")
    same([d(f, 1).subs(x, -2), d(g, 1).subs(x, -2)], [12, 3], "pendientes en -2")
    same(contact_order(f, g, -2), 0, "orden en -2")
    same(f.subs(x, 1) + d(f).subs(x, 1) * (x - 1), g, "g es la tangente en 1")


@check("U4.T.CON.4", "f=1/(1+2x) y 1+ax+bx^2: a=-2, b=4, orden exacto 2", page=P1)
def _():
    f = 1 / (1 + 2 * x)
    same([d(f, k).subs(x, 0) for k in range(4)], [1, -2, 8, -48], "derivadas de f")
    A, B = sp.symbols("A B")
    g = 1 + A * x + B * x ** 2
    sol = sp.solve([d(f, k).subs(x, 0) - d(g, k).subs(x, 0) for k in (1, 2)], [A, B], dict=True)[0]
    same([sol[A], sol[B]], [-2, 4], "a y b")
    gg = g.subs(sol)
    same(d(gg, 3), 0, "g''' = 0")
    same(contact_order(f, gg, 0), 2, "orden exacto")


@check("U4.T.CON.5", "Caracterización por límites con sen x - x", page=P1)
def _():
    q = sp.sin(x) - x
    same(sp.limit(q / x ** 2, x, 0, "+"), 0, "q/x^2 por derecha")
    same(sp.limit(q / x ** 2, x, 0, "-"), 0, "q/x^2 por izquierda")
    same(sp.limit(q / x ** 3, x, 0, "+"), R(-1, 6), "q/x^3 por derecha")
    same(sp.limit(q / x ** 3, x, 0, "-"), R(-1, 6), "q/x^3 por izquierda")
    same(R(-1, 6), (d(sp.sin(x), 3).subs(x, 0) - d(x, 3).subs(x, 0)) / sp.factorial(3), "= diferencia de terceras derivadas / 3!")


@check("U4.T.POL.1", "x^4-3x^3+2x-5 en potencias de (x-2)", page=P1)
def _():
    P = x ** 4 - 3 * x ** 3 + 2 * x - 5
    same([d(P, k).subs(x, 2) for k in range(5)], [-9, -2, 12, 30, 24], "derivadas en 2")
    same([d(P, k).subs(x, 2) / sp.factorial(k) for k in range(5)], [-9, -2, 6, 5, 1], "coeficientes")
    same(sp.expand(-9 - 2 * (x - 2) + 6 * (x - 2) ** 2 + 5 * (x - 2) ** 3 + (x - 2) ** 4), P, "reconstrucción")


@check("U4.T.POL.2", "Polinomio de grado <=3 con P(1)=2, P'(1)=-1, P''(1)=4, P'''(1)=12", page=P1)
def _():
    P = 2 - (x - 1) + 2 * (x - 1) ** 2 + 2 * (x - 1) ** 3
    same([d(P, k).subs(x, 1) for k in range(4)], [2, -1, 4, 12], "datos")
    same(sp.expand(P), 2 * x ** 3 - 4 * x ** 2 + x + 3, "desarrollado")


@check("U4.T.POL.3", "Deducción: derivar k veces sum c_j (x-a)^j y evaluar en a da k! c_k", page=P1)
def _():
    cs = sp.symbols("c0:5")
    P = sum(cs[j] * (x - a) ** j for j in range(5))
    for k in range(5):
        same(d(P, k).subs(x, a), sp.factorial(k) * cs[k], f"P^({k})(a)")
    # y el factorial no se pierde: P(x) con coeficientes P^(k)(a)/k! se reconstruye
    Q = sum(d(P, k).subs(x, a) / sp.factorial(k) * (x - a) ** k for k in range(5))
    same(sp.expand(Q - P), 0, "reconstrucción")


# ---------------------------------------------------------------------------
# 4.2 Polinomio de Taylor y de Mac Laurin; aproximación lineal
# ---------------------------------------------------------------------------
@check("U4.T.TAY.1", "Orden y grado: P4 de sen x en 0 es x - x^3/6 (grado 3)", page=P2)
def _():
    f = sp.sin(x)
    same([d(f, k).subs(x, 0) for k in range(5)], [0, 1, 0, -1, 0], "derivadas")
    P4 = taylor(f, 0, 4)
    same(P4, x - x ** 3 / 6, "P4")
    same(sp.degree(P4, x), 3, "grado")
    same(taylor(f, 0, 3), P4, "P3 = P4")


@check("U4.T.TAY.2", "Polinomios de Mac Laurin de las funciones elementales", page=P2)
def _():
    n = 5
    same(taylor(sp.exp(x), 0, n), sum(x ** k / sp.factorial(k) for k in range(n + 1)), "e^x")
    same(taylor(sp.sin(x), 0, n), x - x ** 3 / 6 + x ** 5 / 120, "sen x")
    same(taylor(sp.cos(x), 0, 4), 1 - x ** 2 / 2 + x ** 4 / 24, "cos x")
    same(taylor(sp.log(1 + x), 0, 5), x - x ** 2 / 2 + x ** 3 / 3 - x ** 4 / 4 + x ** 5 / 5, "ln(1+x)")
    same([d(sp.log(1 + x), k).subs(x, 0) for k in range(1, 6)], [1, -1, 2, -6, 24], "derivadas de ln(1+x)")
    al = sp.symbols("alpha")
    f = (1 + x) ** al
    for k in range(6):
        same(sp.simplify(d(f, k).subs(x, 0) - sp.ff(al, k)), 0, f"derivada {k} de (1+x)^alpha")
    same(taylor(sp.sqrt(1 + x), 0, 3), 1 + x / 2 - x ** 2 / 8 + x ** 3 / 16, "alpha = 1/2")
    same(taylor(1 / (1 + x), 0, 4), 1 - x + x ** 2 - x ** 3 + x ** 4, "alpha = -1")


@check("U4.T.TAY.3", "Raíz cúbica en a=8, orden 2, y valor aproximado en 8,3", page=P2)
def _():
    f = sp.cbrt(x)
    same([d(f, k).subs(x, 8) for k in range(3)], [2, R(1, 12), -R(1, 144)], "derivadas en 8")
    P = taylor(f, 8, 2)
    same(P, 2 + (x - 8) / 12 - (x - 8) ** 2 / 288, "P2")
    v = P.subs(x, R(83, 10))
    same(v, R(6479, 3200), "P2(8,3)")
    require(abs(dec(v, 7) - 2.0246875) < 1e-9, "decimal")
    require(abs(float(f.subs(x, R(83, 10))) - 2.0246939) < 1e-7, "valor exacto aproximado")


@check("U4.T.TAY.4", "x e^x: Mac Laurin de orden 3", page=P2)
def _():
    f = x * sp.exp(x)
    same([d(f, k).subs(x, 0) for k in range(4)], [0, 1, 2, 3], "derivadas")
    same(taylor(f, 0, 3), x + x ** 2 + x ** 3 / 2, "P3")


@check("U4.T.TAY.5", "cos(2x): coeficientes c^k f^(k)(0), orden 4", page=P2)
def _():
    f = sp.cos(2 * x)
    same([d(f, k).subs(x, 0) for k in range(5)], [1, 0, -4, 0, 16], "derivadas")
    same([2 ** k * d(sp.cos(x), k).subs(x, 0) for k in range(5)], [1, 0, -4, 0, 16], "regla del factor c^k")
    same(taylor(f, 0, 4), 1 - 2 * x ** 2 + R(2, 3) * x ** 4, "P4")


@check("U4.T.TAY.6", "sen x en a=pi/4, orden 3", page=P2)
def _():
    f = sp.sin(x)
    r2 = sp.sqrt(2) / 2
    same([d(f, k).subs(x, sp.pi / 4) for k in range(4)], [r2, r2, -r2, -r2], "derivadas en pi/4")
    same(taylor(f, sp.pi / 4, 3),
         r2 * (1 + (x - sp.pi / 4) - (x - sp.pi / 4) ** 2 / 2 - (x - sp.pi / 4) ** 3 / 6), "P3")


@check("U4.T.TAY.7", "cos x = x^2 con Mac Laurin de orden 2 y 4", page=P2)
def _():
    sol2 = sp.solve(sp.Eq(taylor(sp.cos(x), 0, 2), x ** 2), x)
    same(sorted(sol2, key=float), sorted([-sp.sqrt(R(2, 3)), sp.sqrt(R(2, 3))], key=float), "orden 2")
    require(abs(float(sp.sqrt(R(2, 3))) - 0.8165) < 1e-4, "0,8165")
    eq4 = sp.Eq(taylor(sp.cos(x), 0, 4), x ** 2)
    same(sp.expand((eq4.lhs - eq4.rhs) * 24), x ** 4 - 36 * x ** 2 + 24, "ecuación bicuadrada")
    s2 = sp.solve(t ** 2 - 36 * t + 24, t)
    same(sorted(s2, key=float), sorted([18 - 10 * sp.sqrt(3), 18 + 10 * sp.sqrt(3)], key=float), "x^2")
    x4 = sp.sqrt(18 - 10 * sp.sqrt(3))
    require(abs(float(x4) - 0.82431) < 1e-5, "0,8243")
    require(sp.N(18 - 10 * sp.sqrt(3), 30) < 1 < sp.N(18 + 10 * sp.sqrt(3), 30), "solo la menor raíz está en el rango válido")
    # la solución exacta de cos x = x^2 está en (0,8241; 0,8242) por cambio de signo
    g = lambda v: sp.N(sp.cos(v) - v ** 2, 30)
    require(g(R(8241, 10000)) > 0 > g(R(8242, 10000)), "cambio de signo")
    require(sp.sqrt(R(2, 3)) < R(8241, 10000) and x4 > R(8242, 10000), "la de orden 2 queda por debajo y la de orden 4 por encima")
    require(abs(x4 - R(8241, 10000)) < R(3, 1000), "la de orden 4 está a menos de 0,003")


@check("U4.T.TAY.8", "a e^(bx) con P2 = 5 - 10x + 10x^2: a=5, b=-2", page=P2)
def _():
    A, B = sp.symbols("A B")
    f = A * sp.exp(B * x)
    eqs = [d(f, k).subs(x, 0) / sp.factorial(k) - cf for k, cf in ((0, 5), (1, -10), (2, 10))]
    sol = sp.solve(eqs, [A, B], dict=True)
    same([(s[A], s[B]) for s in sol], [(5, -2)], "a y b")
    same(taylor(5 * sp.exp(-2 * x), 0, 2), 5 - 10 * x + 10 * x ** 2, "P2")


@check("U4.T.TAY.9", "Datos de f a partir de P2(x)=4-6(x+1)+5(x+1)^2 en a=-1", page=P2)
def _():
    P = 4 - 6 * (x + 1) + 5 * (x + 1) ** 2
    same([d(P, k).subs(x, -1) for k in range(3)], [4, -6, 10], "f(-1), f'(-1), f''(-1)")
    same(sp.expand(4 - 6 * (x + 1)), -6 * x - 2, "recta tangente")
    same(P.subs(x, R(-9, 10)), R(4) - R(6, 10) + R(5, 100), "P2(-0,9)")
    same(P.subs(x, R(-9, 10)), R(345, 100), "P2(-0,9) = 3,45")


@check("U4.T.LIN.1", "Linealización de la raíz cuarta en 16 y valor en 16,2", page=P2)
def _():
    f = x ** R(1, 4)
    same([f.subs(x, 16), d(f).subs(x, 16)], [2, R(1, 32)], "f(16), f'(16)")
    L = taylor(f, 16, 1)
    same(L, 2 + (x - 16) / 32, "L(x)")
    same(L.subs(x, R(162, 10)), R(2) + R(1, 160), "L(16,2)")
    require(abs(float(R(2) + R(1, 160)) - 2.00625) < 1e-12, "2,00625")
    require(d(f, 2).subs(x, 16) < 0, "f''(16) < 0")
    # sobreestima: L(x) >= f(x) en puntos de prueba
    for v in (R(8), R(12), R(162, 10), R(20), R(24)):
        require(L.subs(x, v) >= f.subs(x, v), f"L >= f en {v}")
    require(abs(float(sp.N(R(162, 10) ** R(1, 4), 30)) - 2.0062209) < 1e-6, "valor 'exacto'")


@check("U4.T.LIN.2", "Linealizaciones en 0 y 1/sqrt(1,04)", page=P2)
def _():
    same([taylor(sp.sin(x), 0, 1), taylor(sp.exp(x), 0, 1), taylor(sp.log(1 + x), 0, 1)], [x, 1 + x, x], "sen, exp, ln")
    f = (1 + x) ** R(-1, 2)
    same(taylor(f, 0, 1), 1 - x / 2, "(1+x)^(-1/2)")
    same(taylor(f, 0, 1).subs(x, R(4, 100)), R(98, 100), "L(0,04)")
    require(abs(float(sp.N(f.subs(x, R(4, 100)), 30)) - 0.98058) < 1e-5, "valor 'exacto'")


@check("U4.T.LIN.3", "Volumen de la esfera: variación lineal frente a exacta", page=P2)
def _():
    r = sp.symbols("r", positive=True)
    V = R(4, 3) * sp.pi * r ** 3
    same(d(V, 1, r).subs(r, 10), 400 * sp.pi, "V'(10)")
    lin = d(V, 1, r).subs(r, 10) * R(2, 10)
    same(lin, 80 * sp.pi, "variación lineal")
    exact = V.subs(r, R(102, 10)) - V.subs(r, 10)
    same(exact, R(4, 3) * sp.pi * R(61208, 1000), "variación exacta")
    require(abs(float(exact / sp.pi) - 81.6107) < 1e-4, "81,6107 pi")
    require(float(lin / sp.pi) < float(exact / sp.pi), "V''>0: la linealización subestima")


# ---------------------------------------------------------------------------
# 4.3 Término complementario
# ---------------------------------------------------------------------------
@check("U4.T.RES.1", "Derivada de F(t) = f(x) - sum f^(k)(t)(x-t)^k/k! - K(x-t)^(n+1)/(n+1)! se telescopia (n=3)", page=P3)
def _():
    f = sp.Function("f")
    K, X = sp.symbols("K X")
    n = 3
    F = f(X) - sum(d(f(t), k, t) * (X - t) ** k / sp.factorial(k) for k in range(n + 1)) - K * (X - t) ** (n + 1) / sp.factorial(n + 1)
    expected = (K - d(f(t), n + 1, t)) * (X - t) ** n / sp.factorial(n)
    same(sp.simplify(d(F, 1, t) - (-d(f(t), n + 1, t) * (X - t) ** n / sp.factorial(n) + K * (X - t) ** n / sp.factorial(n))), 0, "F'(t) forma intermedia")
    same(sp.simplify(sp.diff(F, t) - expected), 0, "F'(t)")


@check("U4.T.RES.2", "e^0,3 con P3 y cota con M=2", page=P3)
def _():
    f = sp.exp(x)
    P = taylor(f, 0, 3)
    v = P.subs(x, R(3, 10))
    same(v, R(13495, 10000), "P3(0,3)")
    require(sp.E ** 3 < 27 < 1024, "e^3 < 27 < 2^10, luego e^0,3 < 2")
    require(sp.N(sp.exp(R(3, 10)), 30) < 2, "e^0,3 < 2")
    bound = R(2, 24) * R(3, 10) ** 4
    same(bound, R(27, 40000), "cota")
    require(abs(float(bound) - 0.000675) < 1e-12, "0,000675")
    err = sp.N(sp.exp(R(3, 10)) - v, 30)
    require(0 < err < bound, "error real dentro de la cota")
    require(abs(float(err) - 0.000358) < 1e-6, "error real ≈ 0,000358")


@check("U4.T.RES.3", "Orden para sen 0,5 con error < 10^-4", page=P3)
def _():
    half = R(1, 2)
    tabla = {n: half ** (n + 1) / sp.factorial(n + 1) for n in range(1, 7)}
    same(tabla[3], R(1, 384), "n=3")
    same(tabla[4], R(1, 3840), "n=4")
    same(tabla[5], R(1, 46080), "n=5")
    require(all(tabla[n] > R(1, 10 ** 4) for n in (1, 2, 3, 4)), "n<=4 no alcanza con la cota")
    require(tabla[5] < R(1, 10 ** 4), "n=5 alcanza")
    P5 = taylor(sp.sin(x), 0, 5)
    same(P5.subs(x, half), half - R(1, 48) + R(1, 3840), "P5(1/2)")
    same(P5.subs(x, half), R(1841, 3840), "P5(1/2) = 1841/3840")
    err = sp.N(sp.sin(half) - P5.subs(x, half), 30)
    require(abs(err) < tabla[5], "error real dentro de la cota")


@check("U4.T.RES.4", "ln 1,2 con P3 en 1 y cota con M=6 en [1; 1,2]", page=P3)
def _():
    f = sp.log(x)
    P = taylor(f, 1, 3)
    v = P.subs(x, R(6, 5))
    same(v, R(1, 5) - R(1, 50) + R(1, 375), "P3(1,2)")
    same(v, R(137, 750), "P3(1,2) = 137/750")
    M, b = lagrange_bound(f, 1, 3, R(6, 5))
    same(M, 6, "M")
    same(b, R(4, 10 ** 4), "cota = 0,0004")
    err = sp.N(v - sp.log(R(6, 5)), 30)
    require(0 < err < b, "error real dentro de la cota")
    require(abs(float(err) - 0.000345) < 1e-6, "error real ≈ 0,000345")
    # M es el máximo de 6/c^4 en [1, 1,2]: decrece, vale 6 en c = 1
    for cc in (R(1), R(11, 10), R(6, 5)):
        require(6 / cc ** 4 <= 6, "6/c^4 <= 6")


@check("U4.T.RES.5", "Raíz de 0,9 con P2 en 1 (x < a) y M=1/2", page=P3)
def _():
    f = sp.sqrt(x)
    P = taylor(f, 1, 2)
    same(P, 1 + (x - 1) / 2 - (x - 1) ** 2 / 8, "P2")
    same(P.subs(x, R(9, 10)), R(759, 800), "P2(0,9)")
    require(abs(float(R(759, 800)) - 0.94875) < 1e-12, "0,94875")
    g3 = d(f, 3)
    same(g3, R(3, 8) * x ** R(-5, 2), "f'''")
    require((R(10, 9)) ** 5 < R(16, 9), "(10/9)^5 < 16/9, luego 0,9^(-5/2) < 4/3")
    M = R(3, 8) * R(4, 3)
    same(M, R(1, 2), "M = 1/2")
    bound = M / 6 * R(1, 10) ** 3
    same(bound, R(1, 12000), "cota")
    err = sp.N(sp.sqrt(R(9, 10)) - P.subs(x, R(9, 10)), 30)
    require(abs(err) < bound, "error real dentro de la cota")
    require(abs(float(err) + 6.7e-5) < 1e-6, "error real ≈ -6,7e-5")
    # f''' es decreciente: el máximo en [0,9; 1] está en el extremo izquierdo
    require(g3.subs(x, R(9, 10)) > g3.subs(x, R(1)), "f''' decrece")


@check("U4.T.RES.6", "sen x ~ x para |x| <= 0,1: cotas con n=1 y n=2", page=P3)
def _():
    f = sp.sin(x)
    same(taylor(f, 0, 1), taylor(f, 0, 2), "P1 = P2")
    b1 = R(1, 2) * R(1, 10) ** 2
    b2 = R(1, 6) * R(1, 10) ** 3
    same(b1, R(1, 200), "cota con n=1")
    same(b2, R(1, 6000), "cota con n=2")
    require(b2 < b1, "la cota con n=2 es mejor")
    for v in (R(1, 10), R(1, 20), R(1, 100)):
        require(abs(sp.N(sp.sin(v) - v, 30)) <= v ** 3 / 6, "|sen x - x| <= |x|^3/6")


@check("U4.T.RES.7", "El resto es un infinitésimo de orden superior a (x-a)^n", page=P3)
def _():
    for f, n in ((sp.exp(x), 2), (sp.sin(x), 3)):
        Rn = f - taylor(f, 0, n)
        same(sp.limit(Rn / x ** n, x, 0, "+"), 0, f"R_n/x^n por derecha, {f}")
        same(sp.limit(Rn / x ** n, x, 0, "-"), 0, f"R_n/x^n por izquierda, {f}")
