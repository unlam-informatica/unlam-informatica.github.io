---
title: Ejercicio 27 — Continuidad en $x=a$ a partir de gráficos
slug: analisis-matematico-i/unidad-2/practica/ejercicio-27
sidebar:
  order: 27
  label: Ejercicio 27
---


:::note[Enunciado]
Dados los siguientes gráficos, analizar si la curva es continua en $x=a$. En caso contrario, clasificar la discontinuidad.
:::

:::note[Sobre los gráficos]
Los gráficos de la guía son capturas de GeoGebra sin fórmula. Aquí se redibujan a partir de la imagen original: las curvas se digitalizaron desde los píxeles de la página, con la escala calibrada sobre las marcas de los ejes. Los puntos llenos y huecos y las rectas punteadas son los del original.
:::

**Criterio.** $f$ es continua en $a$ si existe $f(a)$, existe $\lim_{x\to a}f(x)$ (finito) y ambos coinciden. Si falla alguna de las tres condiciones, la discontinuidad se clasifica con los límites laterales.

![f₁ cerca de a = 1: rama que sube hasta un hueco en (1, 1) y otra que sale de un hueco en (1, 3)](/analisis-matematico-i/figuras/u2-p2-27a.svg)

**a)** $f_1$, $a=1$. Por izquierda la curva llega al hueco $(1,1)$ y por derecha sale del hueco $(1,3)$, así que $\lim_{x\to1^-}f_1=1$ y $\lim_{x\to1^+}f_1=3$. Los laterales son finitos y distintos y $f_1(1)$ no existe. Es una **discontinuidad esencial de salto finito**, con salto $\lvert3-1\rvert=2$.

![f₂ cerca de a = 2: curva en forma de V con el vértice en (2, 0), sin cortes](/analisis-matematico-i/figuras/u2-p2-27b.svg)

**b)** $f_2$, $a=2$. La curva pasa por $(2,0)$ sin cortes, así que $\lim_{x\to2}f_2=0=f_2(2)$: $f_2$ es **continua** en $x=2$. La punta en el vértice no afecta la continuidad. Afecta la derivabilidad, que se estudia en la Unidad 3.

![f₃ cerca de a = 1: dos ramas que bajan sin cota a ambos lados de la recta punteada x = 1](/analisis-matematico-i/figuras/u2-p2-27c.svg)

**c)** $f_3$, $a=1$. Las dos ramas bajan sin cota junto a la recta $x=1$: $\lim_{x\to1^-}f_3=\lim_{x\to1^+}f_3=-\infty$. Es una **discontinuidad esencial de salto infinito**, con asíntota vertical $x=1$.

![f₄ cerca de a = 2: parábola que llega a un punto lleno en (2, 4); recta que sale de un hueco en (2, −2)](/analisis-matematico-i/figuras/u2-p2-27d.svg)

**d)** $f_4$, $a=2$. $\lim_{x\to2^-}f_4=4=f_4(2)$, porque el punto lleno está en $(2,4)$, y $\lim_{x\to2^+}f_4=-2$, porque la recta sale del hueco $(2,-2)$. Los laterales son finitos y distintos: es una **discontinuidad esencial de salto finito**, con salto $\lvert-2-4\rvert=6$. Además $f_4$ es continua por izquierda en $2$.

![f₅ cerca de a = 2: curva con un pico en un hueco en (2, 3) y un punto lleno aislado en (2, 1)](/analisis-matematico-i/figuras/u2-p2-27e.svg)

**e)** $f_5$, $a=2$. Las dos ramas llegan al hueco $(2,3)$, así que $\lim_{x\to2}f_5=3$. Pero $f_5(2)=1$, según el punto lleno y las guías punteadas. El límite existe y es finito, pero no coincide con la imagen: es una **discontinuidad evitable**, que se elimina redefiniendo $f_5(2)=3$.

![f₆ cerca de a = 0: curva creciente sin cortes que pasa por el origen](/analisis-matematico-i/figuras/u2-p2-27f.svg)

**f)** $f_6$, $a=0$. La curva pasa por $(0,0)$ sin cortes: $\lim_{x\to0}f_6=0=f_6(0)$. $f_6$ es **continua** en $x=0$.

| Función | Punto | Clasificación |
|---|---|---|
| $f_1$ | $x=1$ | esencial de salto finito (salto $2$) |
| $f_2$ | $x=2$ | continua |
| $f_3$ | $x=1$ | esencial de salto infinito |
| $f_4$ | $x=2$ | esencial de salto finito (salto $6$) |
| $f_5$ | $x=2$ | evitable (redefinir $f_5(2)=3$) |
| $f_6$ | $x=0$ | continua |

✓ Coincide con la respuesta oficial. Los saltos y el valor para redefinir se leen de los puntos marcados del gráfico.
