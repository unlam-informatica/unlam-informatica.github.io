"""Comprobaciones de los ejercicios originales de la Unidad 4 (Polinomios de Taylor).

Cada función recalcula el resultado publicado y los pasos intermedios de la resolución. Las cotas de error se
verifican con aritmética racional exacta y desigualdades explícitas; los decimales publicados se contrastan con
precisión explícita (sp.N con 30 dígitos). Los ejercicios U4.04 y U4.13 son demostraciones (razonamiento).
"""
import sympy as sp
from content_pipeline.mathcheck import check, require, same

T = "/analisis-matematico-i/unidad-4/teoria/"
P1 = T + "orden-de-contacto/"
P2 = T + "polinomio-de-taylor/"
P3 = T + "termino-complementario/"
PI = "/analisis-matematico-i/unidad-4/practica/integradores/"

x, t = sp.symbols("x t", real=True)
R = sp.Rational


def d(f, k=1):
    return sp.diff(f, x, k)


def taylor(f, point, n):
    return sum(d(f, k).subs(x, point) / sp.factorial(k) * (x - point) ** k for k in range(n + 1))


def contact_order(f, g, point, kmax=12):
    n = -1
    for k in range(kmax):
        if sp.simplify(d(f, k).subs(x, point) - d(g, k).subs(x, point)) == 0:
            n = k
        else:
            return n
    raise AssertionError("coinciden todas las derivadas hasta kmax")


def num(v, digits=30):
    return sp.N(v, digits)


def lagrange_bound(f, point, n, xv):
    g = d(f, n + 1)
    lo, hi = sorted([sp.nsimplify(point), sp.nsimplify(xv)])
    crit = [s for s in sp.solve(d(g), x) if s.is_real and lo <= s <= hi]
    M = max(abs(g.subs(x, p)) for p in [lo, hi, *crit])
    return M, M / sp.factorial(n + 1) * abs(xv - point) ** (n + 1)


# ---------------------------------------------------------------------------
# Orden de contacto
# ---------------------------------------------------------------------------
@check("U4.01", "Orden de contacto: ln(1+x) con su P3; cos x con 1-x^2/2; e^x con 1+x+x^2", page=P1)
def _():
    f = sp.log(1 + x)
    g = x - x ** 2 / 2 + x ** 3 / 3
    same([d(f, k).subs(x, 0) for k in range(5)], [0, 1, -1, 2, -6], "derivadas de ln(1+x)")
    same([d(g, k).subs(x, 0) for k in range(5)], [0, 1, -1, 2, 0], "derivadas de g")
    same(contact_order(f, g, 0), 3, "a")
    same([d(sp.cos(x), k).subs(x, 0) for k in range(5)], [1, 0, -1, 0, 1], "derivadas de cos")
    same(contact_order(sp.cos(x), 1 - x ** 2 / 2, 0), 3, "b")
    same(contact_order(sp.exp(x), 1 + x + x ** 2, 0), 1, "c")


@check("U4.02", "sqrt(1+x) con 1+ax+bx^2 (a=1/2, b=-1/8) y con el término cúbico k=1/16", page=P1)
def _():
    f = sp.sqrt(1 + x)
    same([d(f, k).subs(x, 0) for k in range(5)], [1, R(1, 2), -R(1, 4), R(3, 8), -R(15, 16)], "derivadas")
    A, B, K = sp.symbols("A B K")
    g = 1 + A * x + B * x ** 2
    sol = sp.solve([d(f, k).subs(x, 0) - d(g, k).subs(x, 0) for k in (1, 2)], [A, B], dict=True)[0]
    same([sol[A], sol[B]], [R(1, 2), -R(1, 8)], "a, b")
    gg = g.subs(sol)
    same(contact_order(f, gg, 0), 2, "orden exacto de g")
    hh = gg + K * x ** 3
    ks = sp.solve(d(f, 3).subs(x, 0) - d(hh, 3).subs(x, 0), K)
    same(ks, [R(1, 16)], "k")
    same(contact_order(f, hh.subs(K, ks[0]), 0), 3, "orden exacto de h")


@check("U4.03", "Q=2x^4-x^3+3x^2+x-4 en potencias de (x+1)", page=P1)
def _():
    Q = 2 * x ** 4 - x ** 3 + 3 * x ** 2 + x - 4
    same([d(Q, k).subs(x, -1) for k in range(5)], [1, -16, 36, -54, 48], "derivadas en -1")
    same([d(Q, k).subs(x, -1) / sp.factorial(k) for k in range(5)], [1, -16, 18, -9, 2], "coeficientes")
    same(sp.expand(1 - 16 * (x + 1) + 18 * (x + 1) ** 2 - 9 * (x + 1) ** 3 + 2 * (x + 1) ** 4), Q, "reconstrucción")
    same(-9 * 6, -54, "Q'''(-1)")
    same(2 * 24, 48, "Q''''(-1)")
    tang = Q.subs(x, -1) + d(Q).subs(x, -1) * (x + 1)
    same(tang, 1 - 16 * (x + 1), "tangente")
    same(contact_order(Q, tang, -1), 1, "orden de contacto con la tangente")


# ---------------------------------------------------------------------------
# Polinomio de Taylor
# ---------------------------------------------------------------------------
@check("U4.05", "Mac Laurin de orden 4 de e^(-2x) y cos 3x; e^(-0,2) con P4 en x=0,1", page=P2)
def _():
    P = taylor(sp.exp(-2 * x), 0, 4)
    same([d(sp.exp(-2 * x), k).subs(x, 0) for k in range(5)], [1, -2, 4, -8, 16], "derivadas")
    same(P, 1 - 2 * x + 2 * x ** 2 - R(4, 3) * x ** 3 + R(2, 3) * x ** 4, "P4 de e^(-2x)")
    Pc = taylor(sp.cos(3 * x), 0, 4)
    same(Pc, 1 - R(9, 2) * x ** 2 + R(27, 8) * x ** 4, "P4 de cos 3x")
    same(sp.cos(3 * x).series(x, 0, 5).removeO(), Pc, "serie de SymPy")
    v = P.subs(x, R(1, 10))
    same(v, 1 - R(1, 5) + R(1, 50) - R(1, 750) + R(1, 15000), "suma")
    same(v, R(12281, 15000), "fracción")
    require(abs(float(v) - 0.818733) < 1e-6, "decimal 0,818733")
    require(abs(float(num(sp.exp(-R(1, 5)))) - 0.818730) < 1e-6, "valor real")


@check("U4.06", "Linealización de sqrt(x) en 36; sqrt(37) y sqrt(35) sobreestimados", page=P2)
def _():
    f = sp.sqrt(x)
    same([f.subs(x, 36), d(f).subs(x, 36)], [6, R(1, 12)], "f(36), f'(36)")
    L = taylor(f, 36, 1)
    same(L, 6 + (x - 36) / 12, "L")
    same([L.subs(x, 37), L.subs(x, 35)], [R(73, 12), R(71, 12)], "estimaciones")
    require(all(d(f, 2).subs(x, v) < 0 for v in (35, 36, 37)), "f'' < 0")
    require(num(sp.sqrt(37)) < R(73, 12) and num(sp.sqrt(35)) < R(71, 12), "sobreestiman")
    require(abs(float(num(sp.sqrt(37))) - 6.08276) < 1e-5 and abs(float(num(sp.sqrt(35))) - 5.91608) < 1e-5, "valores reales")
    require(abs(float(R(73, 12)) - 6.08333) < 1e-5 and abs(float(R(71, 12)) - 5.91667) < 1e-5, "decimales")


@check("U4.07", "sen x = x^2 con Mac Laurin de orden 3", page=P2)
def _():
    P3_ = taylor(sp.sin(x), 0, 3)
    same(P3_, x - x ** 3 / 6, "P3")
    same(sp.factor(P3_ - x ** 2), -x * (x ** 2 + 6 * x - 6) / 6, "factorización")
    sols = sp.solve(sp.Eq(P3_, x ** 2), x)
    same(sorted(sols, key=float), sorted([0, -3 + sp.sqrt(15), -3 - sp.sqrt(15)], key=float), "soluciones")
    require(abs(float(-3 + sp.sqrt(15)) - 0.8730) < 1e-4 and abs(float(-3 - sp.sqrt(15)) + 6.8730) < 1e-4, "decimales")
    require(abs(float(P3_.subs(x, -3 - sp.sqrt(15))) - 47.2) < 0.1, "P3 en la solución espuria ≈ 47")
    g = lambda v: num(sp.sin(v) - v ** 2)
    require(abs(float(g(R(87, 100))) - 0.0074) < 1e-4 and abs(float(g(R(88, 100))) + 0.0037) < 1e-4, "valores de g")
    require(g(R(87, 100)) > 0 > g(R(88, 100)), "cambio de signo")
    require(R(87, 100) < -3 + sp.sqrt(15) < R(88, 100), "aproximación dentro del intervalo")
    # para |x| > 1 no hay soluciones: sen x <= 1 < x^2
    for v in (R(11, 10), 2, 5, -2, -R(69, 10)):
        require(sp.sin(v) < v ** 2, "sen x < x^2 si |x| > 1")


@check("U4.08", "a e^(bx)+c con P2 = 5+6x+6x^2; datos de g en a=2", page=P2)
def _():
    A, B, C = sp.symbols("A B C")
    f = A * sp.exp(B * x) + C
    eqs = [d(f, k).subs(x, 0) / sp.factorial(k) - cf for k, cf in ((0, 5), (1, 6), (2, 6))]
    sol = sp.solve(eqs, [A, B, C], dict=True)
    same([(s[A], s[B], s[C]) for s in sol], [(3, 2, 2)], "(a, b, c)")
    ff = f.subs({A: 3, B: 2, C: 2})
    same(taylor(ff, 0, 2), 5 + 6 * x + 6 * x ** 2, "P2")
    same(d(ff, 3).subs(x, 0), 24, "f'''(0)")
    Q = 1 + 3 * (x - 2) - (x - 2) ** 2 + 4 * (x - 2) ** 3
    same([d(Q, k).subs(x, 2) for k in range(4)], [1, 3, -2, 24], "g(2), g'(2), g''(2), g'''(2)")
    same(Q.subs(x, 2) + d(Q).subs(x, 2) * (x - 2), 1 + 3 * (x - 2), "tangente")


@check("U4.09", "h = g e^(2x): derivadas, Mac Laurin de orden 3 y producto de polinomios", page=P2)
def _():
    gd = [2, -1, 4, 6]
    hd = [sum(sp.binomial(k, j) * gd[j] * 2 ** (k - j) for j in range(k + 1)) for k in range(4)]
    same(hd, [2, 3, 8, 34], "Leibniz")
    # derivadas explícitas publicadas
    same([gd[0], gd[1] + 2 * gd[0], gd[2] + 4 * gd[1] + 4 * gd[0], gd[3] + 6 * gd[2] + 12 * gd[1] + 8 * gd[0]], [2, 3, 8, 34], "forma publicada")
    P = sum(R(hd[k], sp.factorial(k)) * x ** k for k in range(4))
    same(P, 2 + 3 * x + 4 * x ** 2 + R(17, 3) * x ** 3, "P3")
    Pg = sum(R(gd[k], sp.factorial(k)) * x ** k for k in range(4))
    same(Pg, 2 - x + 2 * x ** 2 + x ** 3, "P3 de g")
    Pe = taylor(sp.exp(2 * x), 0, 3)
    same(Pe, 1 + 2 * x + 2 * x ** 2 + R(4, 3) * x ** 3, "P3 de e^(2x)")
    prod = sp.expand(Pg * Pe)
    same([prod.coeff(x, k) for k in range(4)], [2, 3, 4, R(17, 3)], "coeficientes del producto")
    # g(x) cualquiera con esos datos: g(x) = 2 - x + 2x^2 + x^3 los cumple
    gg = 2 - x + 2 * x ** 2 + x ** 3
    same([d(gg * sp.exp(2 * x), k).subs(x, 0) for k in range(4)], [2, 3, 8, 34], "ejemplo con g polinómica")


# ---------------------------------------------------------------------------
# Término complementario
# ---------------------------------------------------------------------------
@check("U4.10", "ln 0,9 con el Mac Laurin de orden 3 de ln(1+x) y cota exacta", page=P3)
def _():
    f = sp.log(1 + x)
    P = taylor(f, 0, 3)
    v = P.subs(x, -R(1, 10))
    same(v, -R(79, 750), "P3(-0,1)")
    require(abs(float(v) + 0.105333) < 1e-6, "decimal")
    M, b = lagrange_bound(f, 0, 3, -R(1, 10))
    same(M, 6 * R(10, 9) ** 4, "M")
    same(b, R(1, 26244), "cota")
    require(abs(float(b) - 3.8e-5) < 1e-6, "cota ≈ 3,8e-5")
    err = abs(num(sp.log(R(9, 10)) - v))
    require(0 < err < b, "error real dentro de la cota")
    require(abs(float(err) - 2.7e-5) < 1e-6, "error real ≈ 2,7e-5")
    require(abs(float(num(sp.log(R(9, 10)))) + 0.1053605) < 1e-7, "valor real")


@check("U4.11", "Orden para e^(-1/2) con error < 10^-3 y aproximación 233/384", page=P3)
def _():
    half = R(1, 2)
    cota = {n: half ** (n + 1) / sp.factorial(n + 1) for n in (3, 4)}
    same(cota[3], R(1, 384), "n=3")
    same(cota[4], R(1, 3840), "n=4")
    require(cota[3] > R(1, 1000) and cota[4] < R(1, 1000), "n=4 es el menor orden")
    P4 = taylor(sp.exp(x), 0, 4)
    same(P4.subs(x, -half), R(233, 384), "P4(-1/2)")
    require(abs(float(R(233, 384)) - 0.606771) < 1e-6, "decimal")
    err4 = abs(num(sp.exp(-half) - R(233, 384)))
    require(err4 < cota[4], "error real de P4 dentro de la cota")
    require(abs(float(err4) - 2.4e-4) < 1e-5, "error real P4 ≈ 2,4e-4")
    P3 = taylor(sp.exp(x), 0, 3)
    same(P3.subs(x, -half), R(29, 48), "P3(-1/2)")
    err3 = abs(num(sp.exp(-half) - R(29, 48)))
    require(err3 > R(1, 1000), "el orden 3 no alcanzaba en la práctica")
    require(abs(float(err3) - 0.00236) < 1e-5, "error real P3 ≈ 0,00236")
    require(abs(float(num(sp.exp(-half))) - 0.606531) < 1e-6, "valor real")


@check("U4.12", "cos x ~ 1-x^2/2: cota x^4/24 y los valores 0,2, 0,22, 0,23", page=P3)
def _():
    f = sp.cos(x)
    same(taylor(f, 0, 2), taylor(f, 0, 3), "P2 = P3")
    same(taylor(f, 0, 2), 1 - x ** 2 / 2, "P2")
    b = lambda r, n: R(1, sp.factorial(n + 1)) * r ** (n + 1)
    same(b(R(1, 5), 3), R(1, 15000), "cota con n=3 en 0,2")
    require(abs(float(b(R(1, 5), 2)) - 1.33e-3) < 1e-5, "cota con n=2 en 0,2 ≈ 1,3e-3")
    require(abs(float(b(R(1, 5), 2) / b(R(1, 5), 3)) - 20) < 1e-9, "veinte veces peor")
    require(b(R(22, 100), 3) < R(1, 10 ** 4), "0,22: cota < 1e-4")
    require(abs(float(b(R(22, 100), 3)) - 9.76e-5) < 1e-7, "9,76e-5")
    require(b(R(23, 100), 3) > R(1, 10 ** 4), "0,23: cota > 1e-4")
    require(abs(float(b(R(23, 100), 3)) - 1.17e-4) < 1e-6, "1,17e-4")
    require(abs(float(R(24, 10 ** 4) ** R(1, 4)) - 0.2213) < 1e-4, "raíz cuarta de 0,0024")
    # el error real es menor que la cota en puntos de prueba
    for v in (R(1, 5), R(22, 100), -R(22, 100)):
        require(abs(num(sp.cos(v) - (1 - v ** 2 / 2))) <= v ** 4 / 24, "error real <= x^4/24")


# ---------------------------------------------------------------------------
# Integradores
# ---------------------------------------------------------------------------
@check("U4.14", "x e^(-x): P4, f(0,2) = 307/1875, cota 1/75000 y órdenes de contacto", page=PI)
def _():
    f = x * sp.exp(-x)
    same([sp.simplify(d(f, k) - (-1) ** (k + 1) * (x - k) * sp.exp(-x) * (-1) ** (k + 1) * (-1) ** 0) for k in range(1)], [0], "f")
    fd = [(1 - x) * sp.exp(-x), (x - 2) * sp.exp(-x), (3 - x) * sp.exp(-x), (x - 4) * sp.exp(-x), (5 - x) * sp.exp(-x)]
    for k, e in enumerate(fd, start=1):
        same(sp.simplify(d(f, k) - e), 0, f"f^({k})")
    same([d(f, k).subs(x, 0) for k in range(6)], [0, 1, -2, 3, -4, 5], "derivadas en 0")
    P4 = taylor(f, 0, 4)
    same(P4, x - x ** 2 + x ** 3 / 2 - x ** 4 / 6, "P4")
    v = P4.subs(x, R(1, 5))
    same(v, R(1, 5) - R(1, 25) + R(1, 250) - R(1, 3750), "suma")
    same(v, R(307, 1875), "fracción")
    require(abs(float(v) - 0.163733) < 1e-6, "decimal")
    # f^(5) positiva y decreciente en [0; 0,2]: M = 5
    require(sp.simplify(d(fd[4]) + (6 - x) * sp.exp(-x)) == 0, "derivada de f^(5)")
    require(all((6 - R(p, 10)) * sp.exp(-R(p, 10)) > 0 for p in range(0, 3)), "f^(6) < 0")
    M, b = lagrange_bound(f, 0, 4, R(1, 5))
    same(M, 5, "M")
    same(b, R(1, 75000), "cota")
    err = abs(num(f.subs(x, R(1, 5)) - v))
    require(0 < err < b, "error real dentro de la cota")
    require(abs(float(err) - 1.28e-5) < 1e-7, "error real ≈ 1,28e-5")
    require(abs(float(num(f.subs(x, R(1, 5)))) - 0.1637461) < 1e-7, "valor real")
    g = x - x ** 2 + x ** 3 / 2
    same(contact_order(f, g, 0), 3, "contacto con g")
    same(contact_order(f, P4, 0), 4, "contacto con P4")


@check("U4.15", "x cos x: P5, 337/768, derivadas f^(6), f^(7) y cotas con n=5 y n=6", page=PI)
def _():
    f = x * sp.cos(x)
    P5 = taylor(f, 0, 5)
    same(P5, x - x ** 3 / 2 + x ** 5 / 24, "P5")
    same(sp.expand(x * taylor(sp.cos(x), 0, 4)), P5, "producto x * P4 de cos")
    same([d(f, k).subs(x, 0) for k in (1, 3, 5)], [1, -3, 5], "derivadas impares")
    same([d(f, k).subs(x, 0) for k in (0, 2, 4, 6)], [0, 0, 0, 0], "derivadas pares")
    n_ = sp.symbols("n")
    for k in range(1, 8):
        formula = x * sp.cos(x + k * sp.pi / 2) + k * sp.cos(x + (k - 1) * sp.pi / 2)
        same(sp.simplify(d(f, k) - formula), 0, f"fórmula general k={k}")
    same(sp.simplify(d(f, 6) - (-x * sp.cos(x) - 6 * sp.sin(x))), 0, "f^(6)")
    same(sp.simplify(d(f, 7) - (x * sp.sin(x) - 7 * sp.cos(x))), 0, "f^(7)")
    v = P5.subs(x, R(1, 2))
    same(v, R(1, 2) - R(1, 16) + R(1, 768), "suma")
    same(v, R(337, 768), "fracción")
    require(abs(float(v) - 0.438802) < 1e-6, "decimal")
    # cotas
    b5 = R(13, 2) / sp.factorial(6) * R(1, 2) ** 6
    b6 = R(15, 2) / sp.factorial(7) * R(1, 2) ** 7
    same(b5, R(13, 92160), "cota n=5")
    same(b6, R(1, 86016), "cota n=6")
    require(abs(float(b5) - 1.41e-4) < 1e-6, "cota n=5 ≈ 1,41e-4")
    require(abs(float(R(15, 2) / sp.factorial(7) * R(1, 2) ** 7) - 1.16e-5) < 1e-7, "cota n=6 ≈ 1,16e-5")
    for p in range(0, 6):
        tt = R(p, 10)
        require(abs(d(f, 6).subs(x, tt)) <= tt + 6 and abs(d(f, 7).subs(x, tt)) <= tt + 7, "cotas de |f^(6)|, |f^(7)| en puntos de prueba")
    require(abs(num(d(f, 6).subs(x, R(1, 2)))) < R(13, 2) and abs(num(d(f, 7).subs(x, R(1, 2)))) < R(15, 2), "cotas")
    err = num(f.subs(x, R(1, 2)) - v)
    require(abs(err) < R(15, 2) / sp.factorial(7) * R(1, 2) ** 7, "error real dentro de la cota con n=6")
    require(abs(float(err) + 1.08e-5) < 1e-7, "error real ≈ -1,08e-5 (f - P5)")
    require(abs(float(num(f.subs(x, R(1, 2)))) - 0.4387913) < 1e-7, "valor real")
    require(abs(float(b5 / (R(15, 2) / sp.factorial(7) * R(1, 2) ** 7)) - 12.1) < 0.1, "unas doce veces mejor")


@check("U4.16", "Opción múltiple con P3 = 3-2(x-1)+6(x-1)^2-4(x-1)^3", page=PI)
def _():
    P = 3 - 2 * (x - 1) + 6 * (x - 1) ** 2 - 4 * (x - 1) ** 3
    same([d(P, k).subs(x, 1) for k in range(4)], [3, -2, 12, -24], "f(1), f'(1), f''(1), f'''(1)")
    same(-4 * 6, -24, "a: opción 2")
    require(-24 not in (-4, -12, -R(2, 3)) and -24 == -4 * 6, "las otras opciones no valen -24")
    same([-4, -4 * 3, -R(4, 6)], [-4, -12, -R(2, 3)], "origen de los distractores")
    same(taylor(P, 1, 1), 3 - 2 * (x - 1), "b: tangente")
    same(taylor(P, 1, 2), 3 - 2 * (x - 1) + 6 * (x - 1) ** 2, "P2 (distractor 4)")
    same((3 - 2 * x).subs(x, 1), 1, "la opción 3 vale 1 y no 3 en x=1")
    c1 = R(10, 24) * R(1, 5) ** 4
    same(c1, R(1, 1500), "c: opción 1")
    require(abs(float(c1) - 6.7e-4) < 1e-5, "6,7e-4")
    same(P.subs(x, R(6, 5)), R(2808, 1000), "d: P3(1,2)")
    same([P.subs(x, R(6, 5)), 3 - R(2, 5), taylor(P, 1, 2).subs(x, R(6, 5)), 3 - R(2, 5) + R(24, 100) + R(32, 1000)],
         [R(2808, 1000), R(26, 10), R(284, 100), R(2872, 1000)], "opciones de d")


@check("U4.17", "Presión p(h)=100 e^(-h/8000): linealización, cotas y orden 2", page=PI)
def _():
    h = sp.symbols("h", real=True)
    p = 100 * sp.exp(-h / 8000)
    same(sp.diff(p, h).subs(h, 0), -R(1, 80), "p'(0)")
    L = 100 - h / 80
    same(p.subs(h, 0) + sp.diff(p, h).subs(h, 0) * h, L, "L")
    same(L.subs(h, 400), 95, "L(400)")
    same(sp.diff(p, h, 2).subs(h, 0), R(1, 640000), "p''(0)")
    same(sp.diff(p, h, 3).subs(h, 0), -R(1, 5120000000), "p'''(0)")
    M = R(1, 640000)
    b1 = M / 2 * 400 ** 2
    same(b1, R(1, 8), "cota de R1(400)")
    require(sp.diff(p, h, 2).subs(h, 400) > 0 and sp.diff(p, h, 2).subs(h, 0) == M, "p'' > 0 y su máximo en [0,400] es M")
    err1 = num(p.subs(h, 400) - 95)
    require(0 < err1 < b1, "p(400) > L(400), dentro de la cota")
    require(abs(float(err1) - 0.1229) < 1e-4 and abs(float(num(p.subs(h, 400))) - 95.1229) < 1e-4, "decimales")
    # c) H = 250 sirve y 253 no
    require(R(250) ** 2 / 1280000 < R(1, 20) < R(253) ** 2 / 1280000, "H=250 sirve; con 253 la cota ya supera 0,05")
    require(R(250) ** 2 / 1280000 == R(625, 12800) and abs(float(R(250) ** 2 / 1280000) - 0.0488) < 1e-4, "0,0488")
    same(sp.solve(sp.Eq(h ** 2 / 1280000, R(1, 20)), h)[1] ** 2, 64000, "H^2 = 64000")
    require(abs(float(sp.sqrt(64000)) - 252.98) < 1e-2, "252,98")
    # d) P2 y su cota
    P2 = 100 - h / 80 + h ** 2 / 1280000
    same(P2.subs(h, 400), R(95125, 1000), "P2(400)")
    M3 = R(1, 5120000000)
    b2 = M3 / 6 * 400 ** 3
    same(b2, R(1, 480), "cota de R2(400)")
    err2 = abs(num(p.subs(h, 400) - P2.subs(h, 400)))
    require(err2 < b2, "error real dentro de la cota")
    require(abs(float(err2) - 0.00206) < 1e-5 and abs(float(b2) - 0.0021) < 1e-4, "decimales")
