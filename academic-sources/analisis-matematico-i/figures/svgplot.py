"""Gráficos cartesianos en SVG, calculados desde la fórmula, sin dependencias externas.

Uso (desde la raíz del repositorio):

    from svgplot import Figure
    fig = Figure(-4, 4, -3, 5, title="Función con asíntota vertical en x = 1")
    fig.function(lambda x: 1 / (x - 1), label="f", breaks=[1])
    fig.vline(1, dashed=True, label="x = 1")
    fig.point(0, -1)
    fig.save("public/analisis-matematico-i/figuras/ejemplo.svg")

Decisiones:
- Las curvas se muestrean con paso fino y se cortan en las discontinuidades declaradas (`breaks`), donde la
  función no está definida o cuando el valor sale muy lejos de la ventana, para no dibujar falsas «paredes».
- Colores mediante variables CSS dentro del SVG, con variante oscura por `prefers-color-scheme`. El fondo es
  transparente para que la figura se integre al tema del sitio.
- Coordenadas con 2 decimales: el archivo queda chico y es estable entre ejecuciones (salida determinista).
"""
from __future__ import annotations

import math
from pathlib import Path
from typing import Callable, Iterable
from xml.sax.saxutils import escape

PALETTE = ["--c1", "--c2", "--c3", "--c4"]

STYLE = """
:root{--bg:#ffffff;--ink:#1f2328;--muted:#6b7280;--grid:#e5e7eb;--axis:#4b5563;--c1:#2563eb;--c2:#dc2626;--c3:#059669;--c4:#9333ea}
@media (prefers-color-scheme: dark){:root{--bg:#1b1f24;--ink:#e5e7eb;--muted:#9ca3af;--grid:#374151;--axis:#9ca3af;--c1:#60a5fa;--c2:#f87171;--c3:#34d399;--c4:#c084fc}}
text{font-family:system-ui,-apple-system,'Segoe UI',sans-serif;font-size:13px;fill:var(--ink)}
.tick{font-size:11px;fill:var(--muted)}
.grid{stroke:var(--grid);stroke-width:1}
.axis{stroke:var(--axis);stroke-width:1.3}
.curve{fill:none;stroke-width:2.4;stroke-linejoin:round;stroke-linecap:round}
.dash{stroke-dasharray:6 5}
"""


def _fmt(v: float) -> str:
    if abs(v) <= 1e-9:
        return "0"
    # Convención del sitio: coma decimal y signo menos tipográfico.
    return f"{v:.2f}".rstrip("0").rstrip(".").replace(".", ",").replace("-", "−")


def _nice_step(span: float, target: int = 8) -> float:
    raw = span / target
    power = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 5, 10):
        if m * power >= raw:
            return m * power
    return 10 * power


class Figure:
    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, *, width: int = 560,
                 height: int = 380, title: str, xstep: float | None = None, ystep: float | None = None,
                 xlabel: str = "x", ylabel: str = "y", tick_labels: dict[float, str] | None = None):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.w, self.h = width, height
        self.pad = 34
        self.title = title
        self.xstep = xstep or _nice_step(xmax - xmin)
        self.ystep = ystep or _nice_step(ymax - ymin)
        self.xlabel, self.ylabel = xlabel, ylabel
        self.tick_labels = {round(k, 10): v for k, v in (tick_labels or {}).items()}
        self.layers: list[str] = []
        self.legend: list[tuple[str, str, bool]] = []
        self.color_index = 0

    # Conversión de coordenadas del plano a la pantalla.
    def X(self, x: float) -> float:
        return self.pad + (x - self.xmin) / (self.xmax - self.xmin) * (self.w - 2 * self.pad)

    def Y(self, y: float) -> float:
        return self.h - self.pad - (y - self.ymin) / (self.ymax - self.ymin) * (self.h - 2 * self.pad)

    def _next_color(self, color: str | None) -> str:
        if color:
            return color
        color = PALETTE[self.color_index % len(PALETTE)]
        self.color_index += 1
        return color

    def function(self, f: Callable[[float], float], *, domain: tuple[float, float] | None = None,
                 breaks: Iterable[float] = (), label: str | None = None, color: str | None = None,
                 dashed: bool = False, samples: int = 1200, open_ends: bool = False) -> None:
        a, b = domain or (self.xmin, self.xmax)
        cuts = sorted(c for c in breaks if a < c < b)
        color = self._next_color(color)
        span = self.ymax - self.ymin
        paths: list[list[tuple[float, float]]] = []
        current: list[tuple[float, float]] = []
        edges = [a, *cuts, b]
        for left, right in zip(edges, edges[1:]):
            n = max(2, int(samples * (right - left) / (self.xmax - self.xmin)))
            eps = (right - left) * 1e-6 if (left in cuts or right in cuts or open_ends) else 0.0
            for i in range(n + 1):
                x = left + eps + (right - left - 2 * eps) * i / n
                try:
                    y = f(x)
                except (ValueError, ZeroDivisionError, OverflowError):
                    y = float("nan")
                if isinstance(y, complex) or y != y or abs(y) > 1e6 or y < self.ymin - 3 * span or y > self.ymax + 3 * span:
                    if len(current) > 1:
                        paths.append(current)
                    current = []
                    continue
                current.append((x, y))
            if len(current) > 1:
                paths.append(current)
            current = []
        cls = "curve dash" if dashed else "curve"
        for path in paths:
            d = "M" + " L".join(f"{self.X(x):.2f},{self.Y(y):.2f}" for x, y in path)
            self.layers.append(f'<path class="{cls}" style="stroke:var({color})" d="{d}"/>')
        if label:
            self.legend.append((label, color, dashed))

    def polyline(self, points: list[tuple[float, float]], *, color: str | None = None, dashed: bool = False,
                 label: str | None = None) -> None:
        """Curva dada por puntos ya calculados o digitalizados (no por una fórmula)."""
        color = self._next_color(color)
        cls = "curve dash" if dashed else "curve"
        if len(points) > 1:
            d = "M" + " L".join(f"{self.X(x):.2f},{self.Y(y):.2f}" for x, y in points)
            self.layers.append(f'<path class="{cls}" style="stroke:var({color})" d="{d}"/>')
        if label:
            self.legend.append((label, color, dashed))

    def segment(self, x0: float, y0: float, x1: float, y1: float, *, color: str | None = None,
                dashed: bool = False, label: str | None = None) -> None:
        color = color or "--axis"
        cls = "curve dash" if dashed else "curve"
        self.layers.append(f'<path class="{cls}" style="stroke:var({color});stroke-width:1.8" '
                           f'd="M{self.X(x0):.2f},{self.Y(y0):.2f} L{self.X(x1):.2f},{self.Y(y1):.2f}"/>')
        if label:
            self.legend.append((label, color, dashed))

    def vline(self, x: float, *, dashed: bool = True, color: str = "--muted", label: str | None = None) -> None:
        self.segment(x, self.ymin, x, self.ymax, color=color, dashed=dashed, label=label)

    def hline(self, y: float, *, dashed: bool = True, color: str = "--muted", label: str | None = None) -> None:
        self.segment(self.xmin, y, self.xmax, y, color=color, dashed=dashed, label=label)

    def point(self, x: float, y: float, *, hollow: bool = False, color: str = "--ink", label: str | None = None,
              dx: float = 8, dy: float = -8) -> None:
        # El punto hueco se rellena con el fondo para que la curva no se vea pasar por un punto excluido.
        fill = "var(--bg)" if hollow else f"var({color})"
        self.layers.append(f'<circle cx="{self.X(x):.2f}" cy="{self.Y(y):.2f}" r="4.2" '
                           f'style="fill:{fill};stroke:var({color});stroke-width:1.8"/>')
        if label:
            self.text(x, y, label, dx=dx, dy=dy)

    def text(self, x: float, y: float, content: str, *, dx: float = 0, dy: float = 0, anchor: str = "start") -> None:
        self.layers.append(f'<text x="{self.X(x) + dx:.2f}" y="{self.Y(y) + dy:.2f}" '
                           f'text-anchor="{anchor}">{escape(content)}</text>')

    def _ticks(self, lo: float, hi: float, step: float) -> list[float]:
        start = math.ceil(lo / step) * step
        values = []
        v = start
        while v <= hi + 1e-9:
            values.append(round(v, 10))
            v += step
        return values

    def svg(self) -> str:
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" role="img" '
               f'aria-label="{escape(self.title)}">', f"<title>{escape(self.title)}</title>",
               f"<style>{STYLE}</style>",
               f'<rect width="{self.w}" height="{self.h}" rx="8" style="fill:var(--bg)"/>',
               f'<clipPath id="area"><rect x="{self.pad}" y="{self.pad}" width="{self.w - 2 * self.pad}" '
               f'height="{self.h - 2 * self.pad}"/></clipPath>']
        for x in self._ticks(self.xmin, self.xmax, self.xstep):
            out.append(f'<line class="grid" x1="{self.X(x):.2f}" y1="{self.Y(self.ymin):.2f}" '
                       f'x2="{self.X(x):.2f}" y2="{self.Y(self.ymax):.2f}"/>')
        for y in self._ticks(self.ymin, self.ymax, self.ystep):
            out.append(f'<line class="grid" x1="{self.X(self.xmin):.2f}" y1="{self.Y(y):.2f}" '
                       f'x2="{self.X(self.xmax):.2f}" y2="{self.Y(y):.2f}"/>')
        x0 = min(max(0.0, self.xmin), self.xmax)
        y0 = min(max(0.0, self.ymin), self.ymax)
        out.append(f'<line class="axis" x1="{self.X(self.xmin):.2f}" y1="{self.Y(y0):.2f}" '
                   f'x2="{self.X(self.xmax):.2f}" y2="{self.Y(y0):.2f}"/>')
        out.append(f'<line class="axis" x1="{self.X(x0):.2f}" y1="{self.Y(self.ymin):.2f}" '
                   f'x2="{self.X(x0):.2f}" y2="{self.Y(self.ymax):.2f}"/>')
        for x in self._ticks(self.xmin, self.xmax, self.xstep):
            if abs(x - x0) > 1e-9:
                label = self.tick_labels.get(x, _fmt(x))
                out.append(f'<text class="tick" x="{self.X(x):.2f}" y="{self.Y(y0) + 15:.2f}" '
                           f'text-anchor="middle">{escape(label)}</text>')
        for y in self._ticks(self.ymin, self.ymax, self.ystep):
            if abs(y - y0) > 1e-9:
                out.append(f'<text class="tick" x="{self.X(x0) - 6:.2f}" y="{self.Y(y) + 4:.2f}" '
                           f'text-anchor="end">{_fmt(y)}</text>')
        out.append(f'<text x="{self.X(self.xmax) - 4:.2f}" y="{self.Y(y0) - 6:.2f}" text-anchor="end">'
                   f'{escape(self.xlabel)}</text>')
        out.append(f'<text x="{self.X(x0) + 6:.2f}" y="{self.Y(self.ymax) + 12:.2f}">{escape(self.ylabel)}</text>')
        out.append('<g clip-path="url(#area)">')
        out += [layer for layer in self.layers if not layer.startswith("<text")]
        out.append("</g>")
        out += [layer for layer in self.layers if layer.startswith("<text")]
        # La leyenda se ancla a la derecha con un ancho estimado según la etiqueta más larga,
        # para que ninguna quede cortada por el borde.
        lw = max((len(label) for label, _, _ in self.legend), default=0) * 7 + 34
        lx = self.w - lw - 10
        for i, (label, color, dashed) in enumerate(self.legend):
            ly = 16 + 18 * i
            cls = "curve dash" if dashed else "curve"
            out.append(f'<path class="{cls}" style="stroke:var({color})" d="M{lx},{ly - 4} L{lx + 24},{ly - 4}"/>')
            out.append(f'<text x="{lx + 30}" y="{ly}">{escape(label)}</text>')
        out.append("</svg>")
        return "\n".join(out) + "\n"

    def save(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.svg(), encoding="utf-8")
