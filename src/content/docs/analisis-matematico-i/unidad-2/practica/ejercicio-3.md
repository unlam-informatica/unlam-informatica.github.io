---
title: Ejercicio 3 — Funciones por tramos
slug: analisis-matematico-i/unidad-2/practica/ejercicio-3
sidebar:
  order: 3
  label: Ejercicio 3
---


Graficar cada una de las funciones dadas y hallar los límites pedidos o establecer que no existen.

**Recordatorio.** Para una función por tramos, en un punto interior a un tramo el límite se calcula con la regla de ese tramo. En un punto de cambio de tramo hay que calcular **límites laterales**: el izquierdo con la regla del tramo izquierdo, el derecho con la del tramo derecho. El límite existe si y sólo si ambos laterales coinciden.

## 3a

:::note[Enunciado]
$g:\mathbb{R}-\lbrace 1\rbrace\to\mathbb{R}\,/\,g(x)=\begin{cases} -x+1 & \text{si } x<1 \\ x-1 & \text{si } 1<x<2 \\ 6-x^2 & \text{si } x\geq 2 \end{cases}$

$\lim\limits_{x\to 1}g(x),\quad \lim\limits_{x\to 2}g(x),\quad \lim\limits_{x\to 1/4}g(x)$
:::

:::tip[Resolución]
**Límite en $x=1$.** Es un punto de cambio de tramo (entre $-x+1$ y $x-1$). Calculamos laterales.

Por izquierda ($x\to 1^-$, regla $-x+1$):



$$
\lim_{x\to 1^-}g(x)=-1+1=0
$$



Por derecha ($x\to 1^+$, regla $x-1$):



$$
\lim_{x\to 1^+}g(x)=1-1=0
$$



Ambos coinciden: $\lim_{x\to 1}g(x)=0$.

**Límite en $x=2$.** Es un punto de cambio entre $x-1$ y $6-x^2$. Calculamos laterales.

Por izquierda ($x\to 2^-$, regla $x-1$):



$$
\lim_{x\to 2^-}g(x)=2-1=1
$$



Por derecha ($x\to 2^+$, regla $6-x^2$):



$$
\lim_{x\to 2^+}g(x)=6-4=2
$$



Los laterales **no coinciden** ($1\neq 2$), por lo que $\lim_{x\to 2}g(x)$ **no existe** (salto finito).

**Límite en $x=1/4$.** Es un punto interior al primer tramo ($x<1$), así que usamos la regla $-x+1$:



$$
\lim_{x\to 1/4}g(x)=-\dfrac{1}{4}+1=\dfrac{3}{4}
$$



**Resultado:** $\lim\limits_{x\to 1}g=0$; $\lim\limits_{x\to 2}g$ no existe (salto $1\to 2$); $\lim\limits_{x\to 1/4}g=\dfrac{3}{4}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 3b

:::note[Enunciado]
$h:\mathbb{R}\to\mathbb{R}\,/\,h(x)=\begin{cases} x^2-5 & \text{si } x\leq -1 \\ 3x+2 & \text{si } -1<x<1 \\ 4x^2+2x & \text{si } x\geq 1 \end{cases}$

$\lim\limits_{x\to -1}h(x),\quad \lim\limits_{x\to 1}h(x),\quad \lim\limits_{x\to 2}h(x)$
:::

:::tip[Resolución]
**Límite en $x=-1$.** Punto de cambio entre $x^2-5$ y $3x+2$. Calculamos laterales.

Por izquierda ($x\to -1^-$, regla $x^2-5$):



$$
\lim_{x\to -1^-}h(x)=(-1)^2-5=1-5=-4
$$



Por derecha ($x\to -1^+$, regla $3x+2$):



$$
\lim_{x\to -1^+}h(x)=3(-1)+2=-3+2=-1
$$



Los laterales **no coinciden** ($-4\neq -1$): $\lim_{x\to -1}h(x)$ **no existe**.

**Límite en $x=1$.** Punto de cambio entre $3x+2$ y $4x^2+2x$. Calculamos laterales.

Por izquierda ($x\to 1^-$, regla $3x+2$):



$$
\lim_{x\to 1^-}h(x)=3+2=5
$$



Por derecha ($x\to 1^+$, regla $4x^2+2x$):



$$
\lim_{x\to 1^+}h(x)=4+2=6
$$



Los laterales **no coinciden** ($5\neq 6$): $\lim_{x\to 1}h(x)$ **no existe**.

**Límite en $x=2$.** Punto interior al tercer tramo ($x\geq 1$), regla $4x^2+2x$:



$$
\lim_{x\to 2}h(x)=4(4)+2(2)=16+4=20
$$



**Resultado:** $\lim\limits_{x\to -1}h$ no existe; $\lim\limits_{x\to 1}h$ no existe; $\lim\limits_{x\to 2}h=20$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
