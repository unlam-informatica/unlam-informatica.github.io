---
title: Ejercicio 5 — Coeficientes para existencia del límite
slug: analisis-matematico-i/unidad-2/practica/ejercicio-5
sidebar:
  order: 5
---


:::note[Enunciado]
Determinar los coeficientes $a, b$ sabiendo que existe el límite cuando $x\to -2$ y $x\to 1$, y luego graficar



$$
f(x)=\begin{cases} bx & x\leq -2 \\ x^2+ax & -2<x<1 \\ a-bx & x\geq 1 \end{cases}
$$


:::

:::tip[Resolución]
Para que el límite exista en $x=-2$ y en $x=1$, los **límites laterales** en cada punto de cambio deben coincidir.

**Condición en $x=-2$.** Igualamos $\lim_{x\to -2^-}$ con $\lim_{x\to -2^+}$.

Por izquierda (regla $bx$):



$$
\lim_{x\to -2^-}f(x)=b\cdot (-2)=-2b
$$



Por derecha (regla $x^2+ax$):



$$
\lim_{x\to -2^+}f(x)=(-2)^2+a(-2)=4-2a
$$



Igualando:



$$
-2b=4-2a
$$





$$
a-b=2 \tag{1}
$$



**Condición en $x=1$.** Igualamos $\lim_{x\to 1^-}$ con $\lim_{x\to 1^+}$.

Por izquierda (regla $x^2+ax$):



$$
\lim_{x\to 1^-}f(x)=(1)^2+a(1)=1+a
$$



Por derecha (regla $a-bx$):



$$
\lim_{x\to 1^+}f(x)=a-b(1)=a-b
$$



Igualando:



$$
1+a=a-b
$$





$$
b=-1 \tag{2}
$$



**Resolución del sistema.** De (2), $b=-1$. Sustituyendo en (1):



$$
a-(-1)=2\implies a=1
$$



**Verificación** de los valores hallados.

En $x=-2$: $-2(-1)=2$ y $4-2(1)=2$. ✓

En $x=1$: $1+1=2$ y $1-(-1)=2$. ✓

Los dos límites valen $2$.

**Función resultante** con $a=1$, $b=-1$:



$$
f(x)=\begin{cases} -x & x\leq -2 \\ x^2+x & -2<x<1 \\ 1+x & x\geq 1 \end{cases}
$$



Para graficar: la primera rama es la recta $y=-x$ restringida a $x\leq -2$ (en $x=-2$ vale $2$). El segundo tramo es una parábola con vértice en $x=-1/2$ y valor mínimo $-1/4$, sobre el intervalo $(-2,1)$. El tercer tramo es la recta $y=1+x$ a partir de $x=1$ (en $x=1$ vale $2$). Los tramos "se conectan" en altura $2$ en ambos puntos de cambio, así que la función es continua.

**Resultado:** $a=1$ y $b=-1$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
