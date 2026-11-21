---
title: Ejercicio 4 — Lectura de gráficos
slug: analisis-matematico-i/unidad-2/practica/ejercicio-4
sidebar:
  order: 4
  label: Ejercicio 4
---


:::note[Enunciado]
Dados los siguientes gráficos, determinar los valores que se indican o indicar que no existen.

**a)** En el gráfico de $y=g(x)$ se piden:

![Gráfico de y = g(x) del ejercicio 4 a): rama que sube hasta un hueco en (−2, −1); rama desde un hueco en (−2, 1) que baja hasta el eje; rama que sube del eje hasta un hueco en (2, 1); punto lleno en (2, 2) y segmento horizontal hasta un hueco en (4, 2); desde allí una curva que oscila entre 0 y 4](/analisis-matematico-i/figuras/u2-p2-4a.svg)


$\lim\limits_{x\to -2^-} g(x)$, $\lim\limits_{x\to -2^+} g(x)$, $\lim\limits_{x\to -2} g(x)$, $\lim\limits_{x\to 2^-} g(x)$, $\lim\limits_{x\to 2^+} g(x)$, $\lim\limits_{x\to 2} g(x)$, $g(-2)$, $g(2)$, $\lim\limits_{x\to 4} g(x)$, $g(4)$, $\lim\limits_{x\to 5} g(x)$.

**b)** En el gráfico de $y=f(x)$ se piden:

![Gráfico de y = f(x) del ejercicio 4 b): punto lleno en (−3, −1/2) y rama que baja sin cota antes de x = −1; parábola desde un hueco en (−1, 1) hasta un punto lleno en (1, 1); segmento desde un hueco en (1, 2) hasta un hueco en (3, 4); semirrecta horizontal y = 4 hacia la derecha](/analisis-matematico-i/figuras/u2-p2-4b.svg)


$\lim\limits_{x\to -3^+} f(x)$, $\lim\limits_{x\to -3^-} f(x)$, $\lim\limits_{x\to -3} f(x)$, $\lim\limits_{x\to -1^+} f(x)$, $\lim\limits_{x\to -1^-} f(x)$, $\lim\limits_{x\to -1} f(x)$, $\lim\limits_{x\to 1^+} f(x)$, $\lim\limits_{x\to 1^-} f(x)$, $\lim\limits_{x\to 1} f(x)$, $\lim\limits_{x\to 3^+} f(x)$, $\lim\limits_{x\to 3^-} f(x)$, $\lim\limits_{x\to 3} f(x)$, $\lim\limits_{x\to +\infty} f(x)$.
:::


:::note[Sobre los gráficos]
Los gráficos de la guía son capturas de GeoGebra sin fórmula. Aquí se redibujan a partir de la imagen original: las curvas se digitalizaron desde los píxeles de la página, con la escala calibrada sobre la cuadrícula o las marcas de los ejes. No hay fórmulas inventadas. Los puntos marcados y las rectas punteadas son los del original. Los valores que no caen sobre la cuadrícula se informan como lecturas aproximadas.
:::

:::tip[Resolución]
**Cómo se lee.** El límite por izquierda sigue la curva desde valores menores que $a$, y el límite por derecha, desde valores mayores. El límite bilateral existe solo si los dos laterales existen, son finitos y coinciden. La imagen $f(a)$ es el punto **lleno** sobre $x=a$; si en $x=a$ solo hay huecos, $f(a)$ no existe.

**a)**

| Pedido | Lectura | Por qué |
|---|---|---|
| $\lim\limits_{x\to-2^-}g(x)$ | $-1$ | la rama izquierda llega al hueco $(-2,-1)$ |
| $\lim\limits_{x\to-2^+}g(x)$ | $1$ | la rama derecha sale del hueco $(-2,1)$ |
| $\lim\limits_{x\to-2}g(x)$ | no existe | laterales distintos |
| $g(-2)$ | no existe | en $x=-2$ solo hay huecos |
| $\lim\limits_{x\to2^-}g(x)$ | $1$ | la curva llega al hueco $(2,1)$ |
| $\lim\limits_{x\to2^+}g(x)$ | $2$ | el segmento horizontal empieza en $(2,2)$ |
| $\lim\limits_{x\to2}g(x)$ | no existe | laterales distintos |
| $g(2)$ | $2$ | punto lleno $(2,2)$ |
| $\lim\limits_{x\to4}g(x)$ | $2$ | el segmento llega a altura $2$ y la oscilación sale de altura $2$ |
| $g(4)$ | no existe | en $(4,2)$ hay un hueco |
| $\lim\limits_{x\to5}g(x)$ | $g(5)\approx2{,}4$ | la curva es continua en $x=5$: el límite es la imagen, que no cae sobre la cuadrícula (lectura aproximada) |

**b)**

| Pedido | Lectura | Por qué |
|---|---|---|
| $\lim\limits_{x\to-3^+}f(x)$ | $-\tfrac12$ | la rama sale del punto lleno $\left(-3,-\tfrac12\right)$ |
| $\lim\limits_{x\to-3^-}f(x)$ | no existe | a la izquierda de $-3$ la función no está definida |
| $\lim\limits_{x\to-3}f(x)$ | no existe como límite bilateral | $f$ no está definida en un entorno reducido de $-3$; solo tiene sentido el lateral derecho |
| $\lim\limits_{x\to-1^-}f(x)$ | $-\infty$ | la rama baja sin cota al acercarse a $x=-1$ (sale de la ventana en $x\approx-1{,}25$, así que la lectura supone que sigue bajando hasta la recta $x=-1$) |
| $\lim\limits_{x\to-1^+}f(x)$ | $1$ | la parábola sale del hueco $(-1,1)$ |
| $\lim\limits_{x\to-1}f(x)$ | no existe | laterales distintos (uno infinito) |
| $\lim\limits_{x\to1^-}f(x)$ | $1$ | la parábola llega al punto lleno $(1,1)$ |
| $\lim\limits_{x\to1^+}f(x)$ | $2$ | el segmento sale del hueco $(1,2)$ |
| $\lim\limits_{x\to1}f(x)$ | no existe | laterales distintos |
| $\lim\limits_{x\to3^-}f(x)$ | $4$ | el segmento llega al hueco $(3,4)$ |
| $\lim\limits_{x\to3^+}f(x)$ | $4$ | la semirrecta $y=4$ empieza en ese hueco |
| $\lim\limits_{x\to3}f(x)$ | $4$ | laterales iguales, aunque $f(3)$ no exista |
| $\lim\limits_{x\to+\infty}f(x)$ | $4$ | a la derecha de $3$ la función vale $4$ |

**Verificación.** La guía no da respuestas para este ejercicio. Cada lectura se apoya en un punto marcado del gráfico original o en el comportamiento de una rama, y el «por qué» indica cuál.
:::
