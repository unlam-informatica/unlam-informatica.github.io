---
title: Ejercicio 10 — Existencia de $a$ para que el límite sea finito
slug: analisis-matematico-i/unidad-2/practica/ejercicio-10
sidebar:
  order: 10
  label: Ejercicio 10
---


:::note[Enunciado]
¿Existe un número $a$ para el cual el $\lim\limits_{x\to -2}\dfrac{3x^2+ax+a+3}{x^2+x-2}$ sea finito? Si es así encontrar los valores de $a$ y del límite.
:::

:::tip[Resolución]
El denominador $x^2+x-2$ se anula en $x=-2$ (raíces: $x=-2$ y $x=1$). Por lo tanto, para que el límite sea finito, el numerador también debe anularse en $x=-2$ (cancelando un factor común $(x+2)$).

**Condición sobre el numerador.** Imponemos que $3x^2+ax+a+3$ se anule en $x=-2$:



$$
3(-2)^2+a(-2)+a+3=0
$$





$$
12-2a+a+3=0
$$





$$
15-a=0\implies a=15
$$



**Verificación de que la indeterminación se cancela.** Con $a=15$, el numerador es:



$$
3x^2+15x+18=3(x^2+5x+6)=3(x+2)(x+3)
$$



Factorizamos también el denominador:



$$
x^2+x-2=(x+2)(x-1)
$$



Sustituimos y simplificamos:



$$
\dfrac{3(x+2)(x+3)}{(x+2)(x-1)}=\dfrac{3(x+3)}{x-1}\quad (x\neq -2)
$$



**Cálculo del límite.** Evaluamos en $x=-2$:



$$
\lim_{x\to -2}\dfrac{3(x+3)}{x-1}=\dfrac{3(1)}{-3}=-1
$$



**Resultado:** $a=15$ y el límite vale $-1$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
