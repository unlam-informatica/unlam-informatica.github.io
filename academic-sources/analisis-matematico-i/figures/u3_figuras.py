"""Figuras de la Unidad 3 (Derivada). Se ejecuta desde la raíz del repositorio:

    python3 academic-sources/analisis-matematico-i/figures/u3_figuras.py
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svgplot import Figure  # noqa: E402

OUT = Path("public/analisis-matematico-i/figuras")


def cbrt(v: float) -> float:
    return math.copysign(abs(v) ** (1 / 3), v)


def secantes() -> None:
    """Secantes por (1, 1) de f(x) = x^2 que tienden a la tangente y = 2x - 1."""
    fig = Figure(-0.5, 3.5, -1, 10, title="Rectas secantes a y = x^2 por el punto (1, 1) que tienden a la tangente",
                 xstep=0.5, ystep=1)
    fig.function(lambda x: x * x, label="f(x) = x²", color="--c1")
    for b, label in ((3, "secantes"), (2, None), (1.5, None)):
        m = b + 1
        fig.segment(-0.5, 1 + m * (-1.5), 3.5, 1 + m * 2.5, color="--muted", dashed=True, label=label)
    fig.segment(-0.5, -2, 3.5, 6, color="--c2", label="tangente")
    for b in (3, 2, 1.5):
        fig.point(b, b * b, color="--muted")
    fig.point(1, 1, label="P(1, 1)", dx=-50, dy=-10)
    fig.save(OUT / "u3-secantes.svg")


def tangente_normal() -> None:
    """Tangente y normal a f(x) = x^2/2 en (2, 2), con la misma escala en ambos ejes."""
    fig = Figure(-1.5, 4.5, -0.8, 3.2, height=396, title="Tangente y normal a y = x²/2 en el punto (2, 2)", xstep=1, ystep=1)
    fig.function(lambda x: x * x / 2, label="f(x) = x²/2", color="--c1")
    fig.segment(-1.5, 2 + 2 * (-3.5), 4.5, 2 + 2 * 2.5, color="--c2", label="tangente")
    fig.segment(-1.5, 2 - 0.5 * (-3.5), 4.5, 2 - 0.5 * 2.5, color="--c3", dashed=True, label="normal")
    fig.point(2, 2, label="P(2, 2)", dx=8, dy=-10)
    fig.save(OUT / "u3-tangente-normal.svg")


def no_derivable() -> None:
    """Tres funciones continuas en 0 que no son derivables en 0."""
    fig = Figure(-2, 2, -1.5, 2.5, title="Funciones continuas en 0 y no derivables en 0: |x|, raíz cúbica y x elevado a 2/3",
                 xstep=0.5, ystep=0.5)
    fig.function(lambda x: abs(x), label="|x|", color="--c1")
    fig.function(cbrt, label="x^(1/3)", color="--c2")
    fig.function(lambda x: abs(x) ** (2 / 3), label="x^(2/3)", color="--c3")
    fig.point(0, 0)
    fig.save(OUT / "u3-no-derivable.svg")


def f_y_derivada() -> None:
    """f(x) = x^3/3 - x y su derivada f'(x) = x^2 - 1."""
    fig = Figure(-3, 3, -3, 4, title="La función f(x) = x³/3 − x y su derivada f′(x) = x² − 1",
                 xstep=1, ystep=1)
    fig.function(lambda x: x ** 3 / 3 - x, label="f(x) = x³/3 − x", color="--c1")
    fig.function(lambda x: x * x - 1, label="f′(x) = x² − 1", color="--c2")
    fig.point(-1, 2 / 3, color="--c1")
    fig.point(1, -2 / 3, color="--c1")
    fig.point(-1, 0, hollow=True, color="--c2")
    fig.point(1, 0, hollow=True, color="--c2")
    fig.save(OUT / "u3-f-y-derivada.svg")


def implicita() -> None:
    """Curva x^2 + xy + y^2 = 3 con sus tangentes horizontales y verticales."""
    fig = Figure(-3.4, 3.4, -2.8, 2.8, height=473, title="Curva x² + xy + y² = 3 con tangentes horizontales y verticales",
                 xstep=1, ystep=1)
    top = lambda x: (-x + math.sqrt(max(0.0, 12 - 3 * x * x))) / 2
    bottom = lambda x: (-x - math.sqrt(max(0.0, 12 - 3 * x * x))) / 2
    fig.function(top, domain=(-2, 2), color="--c1", label="la curva", samples=2400)
    fig.function(bottom, domain=(-2, 2), color="--c1", samples=2400)
    fig.segment(-2.6, 2, 2.6, 2, color="--c2", dashed=True, label="tg horizontal")
    fig.segment(-2.6, -2, 2.6, -2, color="--c2", dashed=True)
    fig.segment(2, -2.4, 2, 2.4, color="--c3", dashed=True, label="tg vertical")
    fig.segment(-2, -2.4, -2, 2.4, color="--c3", dashed=True)
    for px, py in ((-1, 2), (1, -2)):
        fig.point(px, py, color="--c2")
    for px, py in ((-2, 1), (2, -1)):
        fig.point(px, py, color="--c3")
    fig.save(OUT / "u3-implicita.svg")


if __name__ == "__main__":
    secantes()
    tangente_normal()
    no_derivable()
    f_y_derivada()
    implicita()
    print("Figuras de la Unidad 3 generadas en", OUT)
