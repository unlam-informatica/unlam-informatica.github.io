---
title: Ejercicio 18 *
slug: analisis-matematico-i/unidad-2/practica/ejercicio-18
sidebar:
  order: 18
---


**Enunciado.** Hallar $a,b$ con $\lim_{x\to\infty}\left(\dfrac{x^2-2x+3}{x-1}+ax+b\right)=0$.

**Resolución.** Hacemos la división: $\dfrac{x^2-2x+3}{x-1}$. Dividiendo, $x^2-2x+3=(x-1)(x-1)+2$, luego



$$
\dfrac{x^2-2x+3}{x-1}=x-1+\dfrac{2}{x-1}
$$



Entonces



$$
\dfrac{x^2-2x+3}{x-1}+ax+b=(1+a)x+(b-1)+\dfrac{2}{x-1}
$$



El término $\dfrac{2}{x-1}\to0$. Para que el límite total sea $0$ deben anularse los coeficientes:



$$
1+a=0\Rightarrow a=-1,\qquad b-1=0\Rightarrow b=1
$$





$$
\boxed{a=-1,\quad b=1.}
$$



✓ Coincide con la respuesta oficial.

