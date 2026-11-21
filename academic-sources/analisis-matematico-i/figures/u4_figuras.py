"""Figuras de la Unidad 4 (Polinomios de Taylor). Se ejecuta desde la raíz del repositorio:

    python3 academic-sources/analisis-matematico-i/figures/u4_figuras.py
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svgplot import Figure  # noqa: E402

OUT = Path("public/analisis-matematico-i/figuras")


def taylor_poly(derivs, a, n):
    """Polinomio de Taylor como función, dados los valores f^(k)(a) para k = 0..n."""
    return lambda x: sum(derivs[k] / math.factorial(k) * (x - a) ** k for k in range(n + 1))


def orden_contacto() -> None:
    """e^x con tres polinomios que tienen contacto de orden exactamente 0, 1 y 2 en x = 0."""
    fig = Figure(-1.6, 1.6, -0.5, 5, title="La exponencial y tres polinomios con contacto de orden 0, 1 y 2 en el origen",
                 xstep=0.5, ystep=1)
    fig.function(math.exp, label="f(x) = eˣ", color="--c1")
    fig.function(lambda x: 1.0, label="g₀ (orden 0)", color="--c2", dashed=True)
    fig.function(lambda x: 1 + x, label="g₁ (orden 1)", color="--c3", dashed=True)
    fig.function(lambda x: 1 + x + x * x / 2, label="g₂ (orden 2)", color="--c4", dashed=True)
    fig.point(0, 1)
    fig.save(OUT / "u4-orden-contacto.svg")


def seno_taylor() -> None:
    """sen x con los polinomios de Mac Laurin de orden 1, 3 y 5."""
    fig = Figure(-2 * math.pi, 2 * math.pi, -3, 3, title="sen x y sus polinomios de Mac Laurin de orden 1, 3 y 5",
                 xstep=math.pi, ystep=1,
                 tick_labels={round(-2 * math.pi, 10): "-2π", round(-math.pi, 10): "-π", round(math.pi, 10): "π", round(2 * math.pi, 10): "2π"})
    fig.function(math.sin, label="sen x", color="--c1")
    fig.function(lambda x: x, label="P₁(x) = x", color="--c2", dashed=True)
    fig.function(lambda x: x - x ** 3 / 6, label="P₃(x)", color="--c3", dashed=True)
    fig.function(lambda x: x - x ** 3 / 6 + x ** 5 / 120, label="P₅(x)", color="--c4", dashed=True)
    fig.save(OUT / "u4-seno-taylor.svg")


def ln_taylor() -> None:
    """ln x con los polinomios de Taylor de orden 1, 2 y 3 en a = 1."""
    p1 = taylor_poly([0, 1, -1, 2], 1, 1)
    p2 = taylor_poly([0, 1, -1, 2], 1, 2)
    p3 = taylor_poly([0, 1, -1, 2], 1, 3)
    fig = Figure(0.1, 3.1, -2.5, 2.5, title="ln x y sus polinomios de Taylor de orden 1, 2 y 3 centrados en a = 1",
                 xstep=0.5, ystep=0.5)
    fig.function(math.log, label="ln x", color="--c1")
    fig.function(p1, label="P₁", color="--c2", dashed=True)
    fig.function(p2, label="P₂", color="--c3", dashed=True)
    fig.function(p3, label="P₃", color="--c4", dashed=True)
    fig.point(1, 0, label="a = 1", dx=8, dy=16)
    fig.save(OUT / "u4-ln-taylor.svg")


def aprox_lineal() -> None:
    """raíz cuarta de x y su recta tangente en x = 16: la tangente queda por encima (f'' < 0)."""
    fig = Figure(8, 24, 1.6, 2.3, title="Raíz cuarta de x y su recta tangente en x = 16: la tangente queda por encima de la curva",
                 xstep=2, ystep=0.1)
    fig.function(lambda x: x ** 0.25, label="f(x) = ⁴√x", color="--c1")
    fig.function(lambda x: 2 + (x - 16) / 32, label="tangente L(x)", color="--c2")
    fig.point(16, 2, label="(16, 2)", dx=-8, dy=-12)
    fig.point(20, 20 ** 0.25, color="--c1", hollow=True)
    fig.point(20, 2 + 4 / 32, color="--c2", hollow=True)
    fig.save(OUT / "u4-aprox-lineal.svg")


def error_taylor() -> None:
    """|e^x - P_n(x)| para n = 1, 2, 3: crece al alejarse de 0 y baja al subir el orden."""
    def err(n):
        return lambda x: abs(math.exp(x) - sum(x ** k / math.factorial(k) for k in range(n + 1)))

    fig = Figure(-1.5, 1.5, 0, 1.5, title="Error absoluto de eˣ con los polinomios de Mac Laurin de orden 1, 2 y 3",
                 xstep=0.5, ystep=0.25)
    fig.function(err(1), label="|R₁(x)|", color="--c2")
    fig.function(err(2), label="|R₂(x)|", color="--c3")
    fig.function(err(3), label="|R₃(x)|", color="--c4")
    fig.save(OUT / "u4-error-taylor.svg")


if __name__ == "__main__":
    orden_contacto()
    seno_taylor()
    ln_taylor()
    aprox_lineal()
    error_taylor()
    print("Figuras de la Unidad 4 generadas en", OUT)
