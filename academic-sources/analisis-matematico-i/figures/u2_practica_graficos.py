"""Gráficos de la Práctica 2 (ejercicios 4, 22, 23 y 27) redibujados desde la digitalización de la guía.

Las curvas no salen de una fórmula: son las polilíneas de `datos/practica-2-digitalizado.json`, obtenidas con
`digitalizacion/` a partir de la página renderizada de la guía. Ver la procedencia en ese archivo.
Uso (desde la raíz del repositorio):

    python academic-sources/analisis-matematico-i/figures/u2_practica_graficos.py
"""
import json
from pathlib import Path

from svgplot import Figure

DATOS = Path(__file__).resolve().parent / "datos" / "practica-2-digitalizado.json"
OUT = Path("public/analisis-matematico-i/figuras")

TITULOS = {
    "e4a": ("y = g(x)", "Ejercicio 4 a) de la Práctica 2: gráfico de y = g(x)"),
    "e4b": ("y = f(x)", "Ejercicio 4 b) de la Práctica 2: gráfico de y = f(x)"),
    "e22a": ("a)", "Ejercicio 22 a) de la Práctica 2"),
    "e22b": ("b)", "Ejercicio 22 b) de la Práctica 2"),
    "e22c": ("c)", "Ejercicio 22 c) de la Práctica 2"),
    "e22d": ("d)", "Ejercicio 22 d) de la Práctica 2"),
    "e22e": ("e)", "Ejercicio 22 e) de la Práctica 2"),
    "e22f": ("f)", "Ejercicio 22 f) de la Práctica 2"),
    "e23": ("y = h(x)", "Ejercicio 23 de la Práctica 2: gráfico de y = h(x)"),
    "e27a": ("f₁, a = 1", "Ejercicio 27 a) de la Práctica 2: f₁ cerca de a = 1"),
    "e27b": ("f₂, a = 2", "Ejercicio 27 b) de la Práctica 2: f₂ cerca de a = 2"),
    "e27c": ("f₃, a = 1", "Ejercicio 27 c) de la Práctica 2: f₃ cerca de a = 1"),
    "e27d": ("f₄, a = 2", "Ejercicio 27 d) de la Práctica 2: f₄ cerca de a = 2"),
    "e27e": ("f₅, a = 2", "Ejercicio 27 e) de la Práctica 2: f₅ cerca de a = 2"),
    "e27f": ("f₆, a = 0", "Ejercicio 27 f) de la Práctica 2: f₆ cerca de a = 0"),
}
ARCHIVO = {k: f"u2-p2-{k[1:]}.svg" for k in TITULOS}


def dibujar(clave: str, g: dict) -> None:
    x0, x1, y0, y1 = g["win"]
    sx, sy = g["step"]
    rotulo, titulo = TITULOS[clave]
    # Misma relación de escalas que el original: alto útil = ancho útil · aspecto · (rango y / rango x).
    ancho = 760 if clave == "e23" else 560
    alto = int(round((ancho - 68) * g["aspecto"] * (y1 - y0) / (x1 - x0) + 68))
    alto = max(260, min(alto, 720))
    fig = Figure(x0, x1, y0, y1, title=titulo, xstep=sx, ystep=sy, width=ancho, height=alto)
    for r in g.get("rectas", []):
        tono = "--muted" if g.get("guia_gris") else "--c2"
        if r[0] == "v":
            fig.vline(r[1], color=tono)
        elif r[0] == "h":
            fig.hline(r[1], color="--c2")
        elif r[0] == "o":
            m, b = r[1], r[2]
            fig.segment(x0, m * x0 + b, x1, m * x1 + b, color="--c2", dashed=True)
        elif r[0] == "s":
            fig.segment(r[1], r[2], r[3], r[4], color="--muted", dashed=True)
    for rama in g["ramas"]:
        fig.polyline([tuple(p) for p in rama], color="--c1")
    for x, y, lleno in g.get("puntos", []):
        fig.point(x, y, hollow=not lleno, color="--c1")
    fig.text(x0, y1, rotulo, dx=8, dy=16)
    fig.save(OUT / ARCHIVO[clave])


if __name__ == "__main__":
    datos = json.loads(DATOS.read_text(encoding="utf-8"))
    for clave, g in datos["graficos"].items():
        dibujar(clave, g)
    print(f"{len(datos['graficos'])} gráficos de la Práctica 2 generados en {OUT}")
