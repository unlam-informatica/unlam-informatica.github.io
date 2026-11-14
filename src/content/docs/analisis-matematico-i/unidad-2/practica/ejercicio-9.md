---
title: Ejercicio 9* — Pelota en caída libre
slug: analisis-matematico-i/unidad-2/practica/ejercicio-9
sidebar:
  order: 9
  label: Ejercicio 9
---


Una pelota cae desde una altura de $150$ m. Si la distancia recorrida en $t$ segundos se representa por $s(t)$, y se mide en metros, la ley de Galileo establece que $s(t)=4{,}9\,t^2$ (no se tiene en cuenta la resistencia del aire).

## 9a

:::note[Enunciado]
Encontrar el dominio de la función bajo el contexto del problema y graficar.
:::

:::tip[Resolución]
En contexto, $t$ representa el tiempo desde que cae la pelota hasta que llega al suelo. El tiempo inicial es $t=0$ y el tiempo final es el momento en que la distancia recorrida iguala la altura inicial $150$ m.

Imponemos $s(t)=150$:



$$
4{,}9\,t^2=150
$$





$$
t^2=\dfrac{150}{4{,}9}\approx 30{,}612
$$





$$
t=\sqrt{\dfrac{150}{4{,}9}}\approx 5{,}53\ \text{s}
$$



El dominio en contexto es $[0,\sqrt{150/4{,}9}\,]\approx [0; 5{,}53]$ s.

La gráfica es un arco de parábola que abre hacia arriba, desde $(0,0)$ hasta $(5{,}53;\,150)$ aproximadamente.

**Resultado:** $D_s=[0,\sqrt{150/4{,}9}\,]\approx [0;\,5{,}53]$ segundos.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 9b

:::note[Enunciado]
Calcular la velocidad media de la pelota en los intervalos que se indican. Tener en cuenta que



$$
v_m=\dfrac{\Delta s}{\Delta t}=\dfrac{s(t)-s(3)}{t-3}
$$



Intervalos: $[3,4]$, $[3,\,3{,}1]$, $[3,\,3{,}05]$, $[3,\,3{,}01]$, $[3,\,3{,}001]$.
:::

:::tip[Resolución]
Calculamos $s(t)-s(3)$ y dividimos por $t-3$ para cada intervalo. Usamos $s(3)=4{,}9\cdot 9=44{,}1$ m.

| Intervalo | $t$ | $s(t)$ | $v_m=\dfrac{s(t)-44{,}1}{t-3}$ |
|-----------|-----|--------|--------------------------------|
| $[3,4]$ | $4$ | $4{,}9\cdot 16=78{,}4$ | $\dfrac{78{,}4-44{,}1}{1}=34{,}3$ |
| $[3;\,3{,}1]$ | $3{,}1$ | $4{,}9\cdot 9{,}61=47{,}089$ | $\dfrac{2{,}989}{0{,}1}=29{,}89$ |
| $[3;\,3{,}05]$ | $3{,}05$ | $4{,}9\cdot 9{,}3025=45{,}58225$ | $\dfrac{1{,}48225}{0{,}05}=29{,}645$ |
| $[3;\,3{,}01]$ | $3{,}01$ | $4{,}9\cdot 9{,}0601=44{,}39449$ | $\dfrac{0{,}29449}{0{,}01}=29{,}449$ |
| $[3;\,3{,}001]$ | $3{,}001$ | $4{,}9\cdot 9{,}006001=44{,}1294049$ | $\dfrac{0{,}0294049}{0{,}001}=29{,}4049$ |


Las velocidades medias **tienden a $29{,}4$ m/s** a medida que el intervalo se achica hacia $t=3$.

**Resultado:** las velocidades medias son $34{,}3$; $29{,}89$; $29{,}645$; $29{,}449$; $29{,}4049$ m/s respectivamente.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 9c

:::note[Enunciado]
Se define velocidad instantánea al límite de las velocidades medias cuando $\Delta t\to 0$. Estimar el valor del límite de acuerdo con los datos completados en la tabla y luego hallarlo en forma exacta. Prestar atención a las unidades con las que se trabaja.
:::

:::tip[Resolución]
**Estimación.** De la tabla, las velocidades medias tienden a aproximadamente $29{,}4$ m/s cuando $\Delta t\to 0$.

**Cálculo exacto del límite.** La velocidad instantánea en $t=3$ es:



$$
v(3)=\lim_{t\to 3}\dfrac{s(t)-s(3)}{t-3}=\lim_{t\to 3}\dfrac{4{,}9 t^2-44{,}1}{t-3}
$$



Factorizamos sacando $4{,}9$ y usando diferencia de cuadrados:



$$
=\lim_{t\to 3}\dfrac{4{,}9(t^2-9)}{t-3}=\lim_{t\to 3}\dfrac{4{,}9(t-3)(t+3)}{t-3}
$$



Simplificamos $(t-3)$:



$$
=\lim_{t\to 3}4{,}9(t+3)=4{,}9\cdot 6=29{,}4
$$



**Unidades.** $s$ está en metros y $t$ en segundos, así que $\dfrac{\Delta s}{\Delta t}$ está en metros por segundo (m/s).

**Resultado:** $v(3)=29{,}4$ m/s.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
