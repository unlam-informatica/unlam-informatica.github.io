---
title: Ejercicio 22-23
slug: analisis-matematico-i/unidad-2/practica/ejercicio-22
sidebar:
  order: 22
---

## Ejercicios 22 y 23 — Asíntotas a partir de gráficos

**Método.** Para identificar asíntotas en un gráfico:

- **Vertical (AV)** $x=a$: la curva se «dispara» a $\pm\infty$ acercándose a la recta vertical $x=a$, por al menos un lado.
- **Horizontal (AH)** $y=L$: en un extremo ($x\to+\infty$ o $x\to-\infty$) la curva se aplana hacia la altura $L$.
- **Oblicua (AO)** $y=mx+n$: en un extremo la curva se pega a una recta inclinada; analíticamente $m=\lim\frac{f(x)}{x}$ y $n=\lim\,(f(x)-mx)$.

Cada extremo se estudia por separado. Las funciones del **Ejercicio 24** sirven de modelo analítico de cada caso.

:::note[Sobre los gráficos]
Los gráficos de la guía son capturas de GeoGebra sin fórmula. Aquí se redibujan a partir de la imagen original: las curvas se digitalizaron desde los píxeles de la página, con la escala calibrada sobre la cuadrícula. No hay fórmulas inventadas. Las rectas punteadas rojas son las que dibuja el original. Donde el original no marca una asíntota, su posición se informa como lectura aproximada.
:::

### Ejercicio 22

Dados los siguientes gráficos, determinar las ecuaciones de todas las asíntotas a la curva, en cada caso.

![Ejercicio 22 a): rama izquierda que se aplana hacia y = 1 y sube sin cota al acercarse a x = −2; rama derecha que empieza en (2, 0) y se acerca a y = 1 por debajo](/analisis-matematico-i/figuras/u2-p2-22a.svg)

**a)** AV $x=-2$ (por izquierda la curva tiende a $+\infty$) y AH $y=1$ en los dos extremos: por arriba si $x\to-\infty$ y por debajo si $x\to+\infty$. La rama derecha empieza en $(2,0)$: entre $-2$ y $2$ no hay gráfico.

![Ejercicio 22 b): rama izquierda cerca de y = 1 que sube sin cota al acercarse a x = 0; rama derecha que viene desde −∞ junto a x = 0, corta el eje en x = 1 y se acerca a y = 1 por debajo](/analisis-matematico-i/figuras/u2-p2-22b.svg)

**b)** AV $x=0$, con $+\infty$ por izquierda y $-\infty$ por derecha. AH $y=1$ en los dos extremos.

![Ejercicio 22 c): dos ramas que suben sin cota a ambos lados de x = 1 y se aplanan hacia y = 0 en los dos extremos; la rama izquierda queda por debajo del eje antes de subir](/analisis-matematico-i/figuras/u2-p2-22c.svg)

**c)** AV $x=1$, con $+\infty$ por los dos lados. AH $y=0$ en los dos extremos: por debajo si $x\to-\infty$ y por encima si $x\to+\infty$.

![Ejercicio 22 d): rama izquierda junto a y = 2 que baja sin cota cerca de x ≈ −0,7; rama central en forma de U con mínimo cerca de (0, 3) que sube sin cota en x ≈ −0,7 y x ≈ 0,7; rama derecha que viene de −∞ cerca de x ≈ 0,7 y se acerca a y = 2](/analisis-matematico-i/figuras/u2-p2-22d.svg)

**d)** AH $y=2$ en los dos extremos, la única que el original dibuja. Además hay **dos asíntotas verticales** que el gráfico no marca:
- una en $x=a$ con $a\approx-0{,}7$: la rama izquierda llega a $-\infty$ antes de $x=-0{,}72$ y la central viene de $+\infty$ desde $x=-0{,}71$;
- otra en $x=b$ con $b$ entre $0{,}60$ y $0{,}66$: la rama central sube a $+\infty$ y la derecha viene de $-\infty$.

La imagen no permite saber si son simétricas, del tipo $x=\pm k$. Sin la fórmula no se pueden dar valores exactos.

![Ejercicio 22 e): rama izquierda que se acerca por arriba a la recta y = −x − 1 y sube sin cota al acercarse a x = 1; rama derecha que viene de −∞ junto a x = 1, tiene un máximo cerca de (2,7; −5,5) y se acerca a la misma recta por debajo](/analisis-matematico-i/figuras/u2-p2-22e.svg)

**e)** AV $x=1$, con $+\infty$ por izquierda y $-\infty$ por derecha. AO $y=-x-1$ en los dos extremos, por arriba si $x\to-\infty$ y por debajo si $x\to+\infty$. Sobre la imagen, la recta punteada mide pendiente $-1{,}00$ y ordenada al origen $-1{,}00$.

![Ejercicio 22 f): tres ramas separadas por x = −2 y x = 2; las ramas exteriores se acercan a la recta y = −x; la central pasa cerca del origen (y ≈ −0,3 en x = 0), casi horizontal](/analisis-matematico-i/figuras/u2-p2-22f.svg)

**f)** AV $x=-2$ y $x=2$. En cada una, la curva tiende a $+\infty$ por izquierda y a $-\infty$ por derecha. AO $y=-x$ en los dos extremos.

**Verificación.** La guía no da respuestas para este ejercicio. Las ecuaciones de las rectas punteadas se midieron sobre la imagen, con estos valores:

| Gráfico | Medido | Leído |
|---|---|---|
| a) | $x=-2{,}02$; $y=0{,}99$ | $x=-2$; $y=1$ |
| b) | $x=-0{,}01$; $y=0{,}99$ | $x=0$; $y=1$ |
| c) | $x=1{,}08$; $y=-0{,}04$ | $x=1$; $y=0$ |
| d) | $y=2{,}01$ | $y=2$ |
| e) | $x=0{,}99$; $m=-1{,}00$, $n=-1{,}00$ | $x=1$; $y=-x-1$ |
| f) | $x=-1{,}98$ y $x=2{,}06$; $m=-0{,}99$, $n=0{,}05$ | $x=\pm2$; $y=-x$ |

### Ejercicio 23

Dado el siguiente gráfico, determinar las ecuaciones de las asíntotas a la curva. Justificar adecuadamente.

![Ejercicio 23: y = h(x). Rama izquierda que se aplana cerca de y ≈ −2 hacia la izquierda y baja sin cota cerca de x = −1; desde el punto lleno (−1, 3) una rama que baja sin cota después de x ≈ 1,2; otra rama que viene de −∞ antes de x ≈ 2,75 y llega a un punto lleno en x = 4; desde un hueco en x = 4, una oscilación alrededor de y = 0 cuya amplitud disminuye](/analisis-matematico-i/figuras/u2-p2-23.svg)

**Asíntota horizontal en $+\infty$.** Para $x>4$ la curva oscila alrededor de $y=0$, con amplitud cada vez menor (las crestas bajan de $\approx0{,}6$ cerca de $x=4{,}5$ a menos de $0{,}2$ cerca de $x=17$). Así, $\lim_{x\to+\infty}h(x)=0$ y $y=0$ es AH por derecha. Que la curva cruce la asíntota infinitas veces no impide que lo sea.

**Asíntota horizontal en $-\infty$.** Hacia la izquierda la curva se aplana cerca de $y\approx-2$: vale $\approx-2{,}18$ en $x=-7$ y sube lentamente. El gráfico sugiere una AH $y=L$ con $L\approx-2$, pero la ventana no alcanza para fijar el valor exacto.

**Asíntotas verticales.**
- **$x=-1$:** la rama izquierda baja sin cota al acercarse a $x=-1$ por izquierda, $\lim_{x\to-1^-}h=-\infty$. Del otro lado, $h(-1)=3$ es un punto lleno.
- **Una AV en $x=c$, con $c>1{,}23$:** la rama que sale de $(-1,3)$ baja sin cota.
- **Otra AV en $x=d$, con $d<2{,}75$:** por derecha, la rama que llega a $x=4$ viene de $-\infty$.

Entre esas dos rectas no hay gráfico. El original no marca $c$ ni $d$, y la imagen no permite precisarlos.

**Verificación.** La guía no da respuestas para este ejercicio. Las lecturas aproximadas se indican como tales y no se completan con valores supuestos.
