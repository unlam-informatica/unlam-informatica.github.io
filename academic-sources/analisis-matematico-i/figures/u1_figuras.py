"""Figuras de las lecciones de la Unidad 1 (Funciones).

Desde la raíz del repositorio:  python3 academic-sources/analisis-matematico-i/figures/u1_figuras.py
Salida: public/analisis-matematico-i/figuras/u1-*.svg
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svgplot import Figure  # noqa: E402

OUT = Path("public/analisis-matematico-i/figuras")


def secante():
    h = lambda t: 20 * t - 5 * t * t
    fig = Figure(-0.5, 4.5, -3, 24, title="Altura h(t) = 20t - 5t² y la secante entre t = 1 y t = 4",
                 xstep=1, ystep=5, xlabel="t", ylabel="h")
    fig.function(h, label="h(t)", domain=(0, 4))
    fig.segment(0.2, h(1) - 5 * (0.2 - 1), 4.4, h(1) - 5 * (4.4 - 1), color="--c2", label="secante, pendiente −5")
    fig.point(1, h(1), color="--c2", label="(1, 15)", dx=-6, dy=-10)
    fig.point(4, h(4), color="--c2", label="(4, 0)", dx=-34, dy=-10)
    fig.save(OUT / "u1-secante.svg")


def signo():
    p = lambda x: (x + 2) * (x - 1) ** 2 * (x - 3)
    fig = Figure(-3.5, 4.5, -18, 14, title="p(x) = (x+2)(x−1)²(x−3): ceros en −2, 1 y 3", xstep=1, ystep=4)
    fig.function(p, label="p(x)")
    for z in (-2, 1, 3):
        fig.point(z, 0, color="--c2")
    fig.save(OUT / "u1-signo.svg")


def par():
    f = lambda x: x ** 4 - 3 * x ** 2 + 1
    fig = Figure(-2.5, 2.5, -3, 6, title="Función par: f(x) = x⁴ − 3x² + 1, simétrica respecto del eje y",
                 xstep=1, ystep=1)
    fig.function(f, label="f(x)")
    for a in (0.5, 1.8):
        fig.point(a, f(a), color="--c2")
        fig.point(-a, f(-a), color="--c2")
        fig.segment(-a, f(a), a, f(a), dashed=True, color="--muted")
    fig.save(OUT / "u1-simetria-par.svg")


def impar():
    g = lambda x: x ** 3 - 3 * x
    fig = Figure(-2.5, 2.5, -6, 6, title="Función impar: g(x) = x³ − 3x, simétrica respecto del origen",
                 xstep=1, ystep=2)
    fig.function(g, label="g(x)")
    for a in (0.7, 1.9):
        fig.point(a, g(a), color="--c2")
        fig.point(-a, g(-a), color="--c2")
        fig.segment(-a, g(-a), a, g(a), dashed=True, color="--muted")
    fig.save(OUT / "u1-simetria-impar.svg")


def algebraicas():
    fig = Figure(-3, 4, -3, 6, title="Algunas funciones algebraicas elementales", xstep=1, ystep=1)
    fig.function(lambda x: x * x, label="x²")
    fig.function(lambda x: x ** 3 / 3, label="x³/3")
    fig.function(lambda x: math.sqrt(x), domain=(0, 4), label="√x")
    fig.function(lambda x: 1 / x, breaks=[0], label="1/x")
    fig.save(OUT / "u1-algebraicas.svg")


def exp_log():
    fig = Figure(-3, 6, -3, 6, title="Exponencial y logaritmo de base 2, simétricas respecto de y = x",
                 xstep=1, ystep=1, width=460, height=460)
    fig.function(lambda x: 2 ** x, label="2ˣ")
    fig.function(lambda x: math.log2(x), domain=(0.001, 6), label="log₂ x")
    fig.function(lambda x: x, dashed=True, color="--muted", label="y = x")
    fig.point(0, 1, color="--c1")
    fig.point(1, 0, color="--c2")
    fig.save(OUT / "u1-exp-log.svg")


def trig():
    pi = math.pi
    names = ["−2π", "−3π/2", "−π", "−π/2", "0", "π/2", "π", "3π/2", "2π"]
    labels = {k * pi / 2: n for k, n in zip(range(-4, 5), names)}
    fig = Figure(-2 * pi, 2 * pi, -2.5, 2.5, title="Seno y coseno: período 2π, imagen [−1, 1]", xstep=pi / 2,
                 ystep=1, tick_labels=labels)
    fig.function(math.sin, label="sen x")
    fig.function(math.cos, label="cos x")
    fig.save(OUT / "u1-trigonometricas.svg")


def desplazamientos():
    f = math.sqrt
    fig = Figure(-3, 8, -3, 5, title="Desplazamientos de f(x) = √x", xstep=1, ystep=1)
    fig.function(f, domain=(0, 8), label="f(x) = √x")
    fig.function(lambda x: f(x - 3), domain=(3, 8), label="f(x − 3): 3 a la derecha", color="--c2")
    fig.function(lambda x: f(x + 2), domain=(-2, 8), label="f(x + 2): 2 a la izquierda", color="--c3")
    fig.function(lambda x: f(x) + 1.5, domain=(0, 8), label="f(x) + 1,5: sube", color="--c4")
    fig.save(OUT / "u1-transf-desplazamientos.svg")


def reflexiones():
    f = math.sqrt
    fig = Figure(-5, 5, -3, 3, title="Reflexiones y escalas de f(x) = √x", xstep=1, ystep=1)
    fig.function(f, domain=(0, 5), label="f(x) = √x")
    fig.function(lambda x: -f(x), domain=(0, 5), label="−f(x): eje x", color="--c2")
    fig.function(lambda x: f(-x), domain=(-5, 0), label="f(−x): eje y", color="--c3")
    fig.function(lambda x: 2 * f(x), domain=(0, 5), label="2f(x): estira", color="--c4", dashed=True)
    fig.save(OUT / "u1-transf-reflexiones.svg")


def composicion_transformaciones():
    f = math.sqrt
    g = lambda x: -2 * f(x - 3) + 1
    fig = Figure(-1, 9, -5, 4, title="g(x) = −2√(x−3) + 1 a partir de √x", xstep=1, ystep=1)
    fig.function(f, domain=(0, 9), label="√x")
    fig.function(g, domain=(3, 9), label="−2√(x−3) + 1", color="--c2")
    fig.point(3, 1, color="--c2")
    fig.point(3.25, 0, color="--c2")
    fig.save(OUT / "u1-transf-composicion.svg")


def inversa():
    f = lambda x: x * x - 1
    finv = lambda x: math.sqrt(x + 1)
    fig = Figure(-2, 4, -2, 4, title="f(x) = x² − 1 en [0, ∞) y su inversa √(x+1), reflejadas en y = x",
                 xstep=1, ystep=1, width=460, height=460)
    fig.function(f, domain=(0, 3), label="f(x) = x² − 1")
    fig.function(finv, domain=(-1, 4), label="f⁻¹(x) = √(x+1)", color="--c2")
    fig.function(lambda x: x, dashed=True, color="--muted", label="y = x")
    fig.point(2, 3, color="--c1", label="(2, 3)", dx=8, dy=14)
    fig.point(3, 2, color="--c2", label="(3, 2)", dx=8, dy=14)
    fig.save(OUT / "u1-inversa-reflejo.svg")


def no_inyectiva():
    f = lambda x: x * x - 4 * x
    fig = Figure(-2, 6, -5, 6, title="f(x) = x² − 4x: la recta y = 0 corta dos veces, no es inyectiva",
                 xstep=1, ystep=1)
    fig.function(f, label="f(x) = x² − 4x")
    fig.hline(0, dashed=True, color="--c2", label="y = 0")
    fig.point(0, 0, color="--c2")
    fig.point(4, 0, color="--c2")
    fig.vline(2, dashed=True, color="--c3", label="x = 2 (vértice)")
    fig.save(OUT / "u1-no-inyectiva.svg")


if __name__ == "__main__":
    for fn in (secante, signo, par, impar, algebraicas, exp_log, trig, desplazamientos, reflexiones,
               composicion_transformaciones, inversa, no_inyectiva):
        fn()
    print("ok")
