"""Consolida la digitalización de los gráficos de la Práctica 2 (ejercicios 4, 22, 23 y 27).

Los gráficos de la guía son capturas de GeoGebra sin fórmula. No se reconstruye ninguna fórmula: las curvas son
las polilíneas digitalizadas desde los píxeles de la página renderizada (`digitalizar.py`), calibradas con la
cuadrícula o con las marcas de los ejes (`calibracion.json`).

Este paso solo:
- une los tramos que la extracción cortó al cruzar un eje, una etiqueta o la cuadrícula (huecos cortos sin salto
  de altura), salvo en las abscisas declaradas en `cortes`, donde el gráfico original tiene una discontinuidad;
- agrega los puntos marcados (lleno/hueco) leídos sobre la imagen;
- agrega las asíntotas o guías punteadas que el original dibuja. Cada asíntota guarda el valor medido sobre la
  imagen y el valor leído (redondeado a la cuadrícula) que se dibuja; la diferencia queda registrada.

Uso (desde la raíz del repositorio, con la salida de `digitalizar.py` en un directorio de trabajo privado):

    python academic-sources/analisis-matematico-i/figures/digitalizacion/consolidar.py <dig.json>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

FUENTE = {
    "documento": "Practica_AMI_UNLAM_2026-(2)_2.pdf",
    "catalogo": "analisis-matematico-i-20099881563a",
    "paginas": {"e4a": 15, "e4b": 15, "e22a": 19, "e22b": 19, "e22c": 19, "e22d": 19, "e22e": 19, "e22f": 19,
                "e23": 19, "e27a": 20, "e27b": 20, "e27c": 20, "e27d": 20, "e27e": 20, "e27f": 20},
}

# Ventana, pasos de la cuadrícula, cortes (discontinuidades del original), puntos y rectas punteadas.
# Puntos: (x, y, lleno). Rectas: ("v", x) vertical, ("h", y) horizontal, ("o", m, b) oblicua,
# ("s", x0, y0, x1, y1) segmento guía. «medido» es lo que da la imagen; el valor dibujado es la lectura.
META = {
    "e4a": dict(win=(-5, 8.5, -5, 5), step=(1, 1), cortes=[-2, 2, 4],
                puntos=[(-2, 1, False), (-2, -1, False), (2, 2, True), (2, 1, False), (4, 2, False)],
                # Tramos que el original dibuja sobre el eje x (tapados por el eje en la extracción por color):
                # se detectan porque el trazo es más grueso que el eje solo, de x = -1 a -0,45 y de 0,5 a 1.
                extensiones=[(-0.45, 0), (0.5, 0)]),
    "e4b": dict(win=(-3.5, 6.9, -4, 4.8), step=(1, 1), cortes=[-1, 1, 3],
                puntos=[(-3, -0.5, True), (-1, 1, False), (1, 1, True), (1, 2, False), (3, 4, False)]),
    "e22a": dict(win=(-9, 8.5, -6.5, 10.5), step=(2, 2), rectas=[("v", -2), ("h", 1)],
                 medido={"x": -2.023, "y": 0.986}),
    "e22b": dict(win=(-4.3, 4.3, -5.2, 5.2), step=(1, 1), rectas=[("v", 0), ("h", 1)], cortes=[0],
                 medido={"x": -0.01, "y": 0.985}),
    "e22c": dict(win=(-17.5, 17.5, -8.5, 20.5), step=(4, 4), rectas=[("v", 1), ("h", 0)],
                 medido={"x": 1.082, "y": -0.039}),
    # En el original las ramas exteriores siguen bajo la asíntota punteada (y = 2) hasta el borde: la extracción
    # por color las pierde donde se superponen, y se prolongan horizontalmente desde el último valor digitalizado.
    "e22d": dict(win=(-6.4, 6.8, -6.6, 6.8), step=(2, 2), rectas=[("h", 2)], medido={"y": 2.007},
                 prolongar=True),
    "e22e": dict(win=(-8.7, 10.9, -12.7, 10.8), step=(2, 2), rectas=[("v", 1), ("o", -1, -1)],
                 medido={"x": 0.99, "m": -1.0, "b": -0.997}),
    "e22f": dict(win=(-11.3, 11.3, -14.5, 14.8), step=(2, 2), rectas=[("v", -2), ("v", 2), ("o", -1, 0)],
                 medido={"x1": -1.978, "x2": 2.057, "m": -0.99, "b": 0.053}),
    "e23": dict(win=(-7.2, 19.2, -11.2, 4.6), step=(1, 1), cortes=[-1, 4],
                puntos=[(-1, 3, True), (4, 1.652, True), (4, -0.418, False)]),
    "e27a": dict(win=(-3.3, 4.9, -2.8, 5.4), step=(1, 1), cortes=[1], puntos=[(1, 1, False), (1, 3, False)]),
    "e27b": dict(win=(-2.7, 7.2, -2.3, 3.3), step=(1, 1)),
    "e27c": dict(win=(-3.2, 5.2, -5.9, 2.3), step=(1, 1), rectas=[("v", 1)], guia_gris=True),
    "e27d": dict(win=(-3.2, 6.2, -3.4, 5.8), step=(1, 1), cortes=[2],
                 puntos=[(2, 4, True), (2, -2, False)], rectas=[("s", 2, -2, 2, 4)]),
    "e27e": dict(win=(-2.8, 5.5, -0.3, 5.2), step=(1, 1), cortes=[2],
                 puntos=[(2, 3, False), (2, 1, True)], rectas=[("s", 0, 1, 2, 1), ("s", 2, 0, 2, 3)]),
    "e27f": dict(win=(-1.7, 6.2, -2.3, 6.6), step=(1, 1)),
}


def unir(ramas, cortes, win, gap=0.45, dy=0.6, rel=0.06):
    ramas = sorted(ramas, key=lambda r: r[0][0])
    out = [list(ramas[0])] if ramas else []
    for r in ramas[1:]:
        a, b = out[-1][-1], r[0]
        cruza = any(min(a[0], b[0]) - 0.02 <= c <= max(a[0], b[0]) + 0.02 for c in cortes)
        # Une si el hueco es corto en unidades, o si es corto en relación con la ventana (tramos empinados
        # que la extracción partió en dos piezas que se solapan levemente).
        corto = b[0] - a[0] < gap and abs(b[1] - a[1]) < dy
        relativo = abs(b[0] - a[0]) < rel * (win[1] - win[0]) and abs(b[1] - a[1]) < rel * (win[3] - win[2])
        # Dos extremos junto al borde de la ventana son una rama que sale y otra que entra: el criterio relativo
        # no los une.
        borde = lambda p: min(abs(p[1] - win[2]), abs(p[1] - win[3])) < 0.1 * (win[3] - win[2])
        cerca = corto or (relativo and not (borde(a) and borde(b)))
        if cerca and not cruza:
            out[-1] += r
        else:
            out.append(list(r))
    return out


def anclar(ramas, puntos, tx=0.3, ty=0.6):
    """Si un extremo de rama termina junto a un punto marcado, la rama llega exactamente a ese punto."""
    for r in ramas:
        for idx in (0, -1):
            x, y = r[idx]
            for px, py, _ in puntos:
                if abs(x - px) < tx and abs(y - py) < ty:
                    if idx == 0:
                        r.insert(0, [px, py])
                    else:
                        r.append([px, py])
                    break
    return ramas


def extender(ramas, extensiones, tol=0.6):
    for ex, ey in extensiones:
        mejor = min(((abs(r[i][0] - ex) + abs(r[i][1] - ey), j, i) for j, r in enumerate(ramas) for i in (0, -1)))
        if mejor[0] < tol:
            r = ramas[mejor[1]]
            if mejor[2] == 0:
                r.insert(0, [ex, ey])
            else:
                r.append([ex, ey])
    return ramas


def sin_rebotes(rama, dx=0.06):
    """Quita puntos aislados que invierten el sentido en tramos casi verticales (ruido de la extracción)."""
    cambio = True
    while cambio and len(rama) > 2:
        cambio = False
        for i in range(1, len(rama) - 1):
            (x0, y0), (x1, y1), (x2, y2) = rama[i - 1], rama[i], rama[i + 1]
            if abs(x2 - x0) < dx and not (min(y0, y2) <= y1 <= max(y0, y2)):
                del rama[i]
                cambio = True
                break
    return rama


def prolongar(ramas, xmin, xmax):
    ramas[0].insert(0, [xmin, ramas[0][0][1]])
    ramas[-1].append([xmax, ramas[-1][-1][1]])
    return ramas


def main(src: str) -> None:
    dig = json.load(open(src))
    calib = json.load(open(Path(__file__).resolve().parent / "calibracion.json"))
    out = {"fuente": FUENTE, "metodo": __doc__.strip().splitlines()[0], "graficos": {}}
    for k, meta in META.items():
        ramas = unir(dig[k]["branches"], meta.get("cortes", []), meta["win"])
        ramas = anclar(ramas, meta.get("puntos", []))
        ramas = extender(ramas, meta.get("extensiones", []))
        if meta.get("prolongar"):
            ramas = prolongar(ramas, meta["win"][0], meta["win"][1])
        ramas = [sin_rebotes([[round(x, 3), round(y, 3)] for x, y in r]) for r in ramas if len(r) > 1]
        # Relación entre la escala vertical y la horizontal del original (px por unidad), para conservarla.
        out["graficos"][k] = {**meta, "aspecto": round(calib[k]["sy"] / calib[k]["sx"], 3), "ramas": ramas}
    dst = Path(__file__).resolve().parent.parent / "datos" / "practica-2-digitalizado.json"
    dst.parent.mkdir(exist_ok=True)
    dst.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    for k, g in out["graficos"].items():
        print(k, len(g["ramas"]), "ramas")


if __name__ == "__main__":
    main(sys.argv[1])
