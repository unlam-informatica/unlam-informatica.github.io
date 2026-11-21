"""Figuras de la Unidad 2 (Límite funcional y continuidad), calculadas desde la fórmula.

Ejecutar desde la raíz del repositorio:

    python3 academic-sources/analisis-matematico-i/figures/u2_figuras.py

Escribe en public/analisis-matematico-i/figuras/u2-*.svg.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svgplot import Figure  # noqa: E402

OUT = Path("public/analisis-matematico-i/figuras")


def band(fig: Figure, x0: float, x1: float, y0: float, y1: float, color: str = "--c1", opacity: float = 0.13) -> None:
    """Rectángulo translúcido en coordenadas del plano (se dibuja dentro del área, recortado)."""
    fig.layers.append(
        f'<rect x="{fig.X(x0):.2f}" y="{fig.Y(y1):.2f}" width="{fig.X(x1) - fig.X(x0):.2f}" '
        f'height="{fig.Y(y0) - fig.Y(y1):.2f}" style="fill:var({color});fill-opacity:{opacity};stroke:none"/>')


def grid(figs: list[Figure], cols: int, title: str, path: Path) -> None:
    """Compone varias figuras del mismo tamaño en una grilla (un solo SVG)."""
    w, h = figs[0].w, figs[0].h
    rows = math.ceil(len(figs) / cols)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w * cols} {h * rows}" role="img" '
             f'aria-label="{escape(title)}">', f"<title>{escape(title)}</title>"]
    for i, fig in enumerate(figs):
        inner = fig.svg().replace('id="area"', f'id="area{i}"').replace("url(#area)", f"url(#area{i})")
        inner = inner.replace("<svg ", f'<svg x="{(i % cols) * w}" y="{(i // cols) * h}" width="{w}" height="{h}" ', 1)
        parts.append(inner.rstrip())
    parts.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def banda_epsilon_delta() -> None:
    f = lambda x: x * x / 2
    fig = Figure(0, 4, 0, 4.5, title="Definición de límite: banda de radio epsilon alrededor de L y entorno reducido de radio delta alrededor de a",
                 xstep=1, ystep=1)
    eps, delta = 0.8, 0.36
    band(fig, 0, 4, 2 - eps, 2 + eps, "--c2")
    band(fig, 2 - delta, 2 + delta, 0, 4.5, "--c1")
    fig.function(f, label="y = f(x)")
    fig.hline(2, label="y = L")
    fig.vline(2, label="x = a")
    fig.point(2, 2, hollow=True, color="--c3")
    fig.text(0.05, 2 + eps, "L + ε", dx=4, dy=-5)
    fig.text(0.05, 2 - eps, "L − ε", dx=4, dy=14)
    fig.text(2 - delta, 0.05, "a − δ", dx=-4, dy=-6, anchor="end")
    fig.text(2 + delta, 0.05, "a + δ", dx=4, dy=-6)
    fig.save(OUT / "u2-banda-epsilon-delta.svg")


def laterales_distintos() -> None:
    fig = Figure(-1, 3, -1, 4, title="Límites laterales distintos en x = 1: por izquierda tiende a 2 y por derecha tiende a 3", xstep=1, ystep=1)
    fig.function(lambda x: x + 1, domain=(-1, 1), color="--c1")
    fig.function(lambda x: 4 - x, domain=(1, 3), color="--c2")
    fig.point(1, 2, hollow=True, color="--c1")
    fig.point(1, 3, hollow=True, color="--c2")
    fig.point(1, 1, color="--c3")
    fig.vline(1)
    fig.text(1, 2, "lím por izq. = 2", dx=-10, dy=22, anchor="end")
    fig.text(1, 3, "lím por der. = 3", dx=10, dy=-8)
    fig.text(1, 1, "f(1) = 1", dx=10, dy=18)
    fig.save(OUT / "u2-laterales-distintos.svg")


def intercalacion() -> None:
    fig = Figure(-0.6, 0.6, -0.45, 0.45, title="Teorema de intercalación: x al cuadrado por seno de 1 sobre x queda entre menos x al cuadrado y x al cuadrado",
                 xstep=0.2, ystep=0.2)
    fig.function(lambda x: x * x * math.sin(1 / x), breaks=[0], samples=6000, label="x² sen(1/x)", color="--c1")
    fig.function(lambda x: x * x, label="x²", color="--c2", dashed=True)
    fig.function(lambda x: -x * x, label="−x²", color="--c3", dashed=True)
    fig.save(OUT / "u2-intercalacion.svg")


def infinitesimos() -> None:
    fig = Figure(-2, 2, 0, 2.5, title="Infinitésimos equivalentes en 0: 1 − cos x y x²/2 casi coinciden cerca del origen; x², del mismo orden, queda por encima",
                 xstep=0.5, ystep=0.5)
    fig.function(lambda x: x * x, label="x²", color="--c3", dashed=True)
    fig.function(lambda x: 1 - math.cos(x), label="1 − cos x", color="--c1")
    fig.function(lambda x: x * x / 2, label="x²/2", color="--c2", dashed=True)
    fig.save(OUT / "u2-infinitesimos.svg")


def limite_infinito() -> None:
    fig = Figure(-1, 3, 0, 16, title="Límite infinito: para cada M existe un delta tal que f(x) supera a M si x está a menos de delta de 1",
                 xstep=1, ystep=4)
    band(fig, 1 - 1 / 3, 1 + 1 / 3, 0, 16, "--c1")
    band(fig, -1, 3, 9, 16, "--c2", 0.10)
    fig.function(lambda x: 1 / (x - 1) ** 2, breaks=[1], label="1/(x−1)²")
    fig.hline(9, label="y = M = 9")
    fig.vline(1, label="x = 1")
    fig.text(1 + 1 / 3, 0.2, "1 + δ", dx=4, dy=-4)
    fig.text(1 - 1 / 3, 0.2, "1 − δ", dx=-4, dy=-4, anchor="end")
    fig.save(OUT / "u2-limite-infinito.svg")


def asintotas_vh() -> None:
    fig = Figure(-5, 7, -6, 10, title="Asíntota vertical x = 1 y asíntota horizontal y = 2 de f(x) = (2x + 1)/(x − 1)", xstep=2, ystep=2)
    fig.function(lambda x: (2 * x + 1) / (x - 1), breaks=[1], label="f", samples=2000)
    fig.vline(1, label="x = 1 (AV)", color="--c2")
    fig.hline(2, label="y = 2 (AH)", color="--c3")
    fig.save(OUT / "u2-asintotas-vh.svg")


def asintota_oblicua() -> None:
    fig = Figure(-9, 5, -1, 9, title="Asíntotas oblicuas distintas: la curva y = raíz de (x + 2)² + 1 se acerca a y = x + 2 en más infinito y a y = −x − 2 en menos infinito",
                 xstep=2, ystep=2)
    fig.function(lambda x: math.sqrt((x + 2) ** 2 + 1), label="f", color="--c1")
    fig.function(lambda x: x + 2, label="y = x + 2 (x → +∞)", color="--c2", dashed=True)
    fig.function(lambda x: -x - 2, label="y = −x − 2 (x → −∞)", color="--c3", dashed=True)
    fig.save(OUT / "u2-asintota-oblicua.svg")


def discontinuidades() -> None:
    kw = dict(width=300, height=230)
    a = Figure(-1, 3, -1, 4, title="Evitable", xstep=1, ystep=1, **kw)
    a.function(lambda x: x + 1, breaks=[1])
    a.point(1, 2, hollow=True)
    a.point(1, 3, color="--c2")
    a.text(-1, -1, "Evitable: límite 2, f(1) = 3", dy=26)
    b = Figure(-1, 3, -1, 4, title="Salto finito", xstep=1, ystep=1, **kw)
    b.function(lambda x: x + 1, domain=(-1, 1), color="--c1")
    b.function(lambda x: 4 - x, domain=(1, 3), color="--c1")
    b.point(1, 2, hollow=True)
    b.point(1, 3, color="--c2")
    b.text(-1, -1, "Esencial de salto finito: 2 y 3", dy=26)
    c = Figure(-1, 3, -4, 4, title="Salto infinito", xstep=1, ystep=2, **kw)
    c.function(lambda x: 1 / (x - 1), breaks=[1])
    c.vline(1)
    c.text(-1, -4, "Esencial de salto infinito", dy=26)
    d = Figure(-0.5, 0.5, -1.5, 1.5, title="Oscilante", xstep=0.25, ystep=0.5, **kw)
    d.function(lambda x: math.sin(1 / x), breaks=[0], samples=5000)
    d.text(-0.5, -1.5, "Esencial: sen(1/x) oscila", dy=26)
    grid([a, b, c, d], 2, "Cuatro tipos de discontinuidad en x = 1 (o en x = 0 la última): evitable, esencial de salto finito, esencial de salto infinito y esencial oscilante",
         OUT / "u2-discontinuidades.svg")


def bolzano() -> None:
    f = lambda x: x ** 3 + x - 1
    fig = Figure(-0.5, 1.5, -2, 3, title="Teorema de Bolzano: f(x) = x³ + x − 1 es continua en [0, 1] con f(0) < 0 y f(1) > 0, por lo que se anula en algún punto del intervalo",
                 xstep=0.5, ystep=1)
    band(fig, 0, 1, -2, 3, "--c1", 0.08)
    fig.function(f, label="f")
    fig.point(0, -1, color="--c2", label="f(0) = −1", dx=8, dy=16)
    fig.point(1, 1, color="--c2", label="f(1) = 1", dx=-70, dy=-8)
    c = 0.6823278038280193
    fig.point(c, 0, color="--c3", label="c ≈ 0,68", dx=6, dy=18)
    fig.save(OUT / "u2-bolzano.svg")


if __name__ == "__main__":
    for fn in (banda_epsilon_delta, laterales_distintos, intercalacion, infinitesimos, limite_infinito, asintotas_vh,
               asintota_oblicua, discontinuidades, bolzano):
        fn()
    print("Figuras escritas en", OUT)
