---
title: Ejercicio 11 * — $a$ para cociente de infinitésimos
slug: analisis-matematico-i/unidad-2/practica/ejercicio-11
sidebar:
  order: 11
---


Buscamos los valores de $a$ tales que, en $x=a$, numerador y denominador se anulen simultáneamente (forma $\tfrac00$).

## 11a
$\lim_{x\to a}\dfrac{(x^2-1)(x+2)}{x^3-x}$

$x^3-x=x(x-1)(x+1)$ se anula en $x=0,1,-1$. El numerador $(x-1)(x+1)(x+2)$ se anula en $x=1,-1,-2$. Coinciden en $x=1$ y $x=-1$.

- **$a=1$:** $\dfrac{(x-1)(x+1)(x+2)}{x(x-1)(x+1)}=\dfrac{x+2}{x}\Big|_{x=1}=\dfrac{3}{1}=3.$
- **$a=-1$:** $\dfrac{x+2}{x}\Big|_{x=-1}=\dfrac{1}{-1}=-1.$



$$
\boxed{a=1\Rightarrow 3;\quad a=-1\Rightarrow -1.}
$$



✓ Coincide con la respuesta oficial.

## 11b
$\lim_{x\to a}\dfrac{x^3+x^2-6x}{6+x^3-7x}$

Numerador: $x(x^2+x-6)=x(x+3)(x-2)$, raíces $0,-3,2$.

Denominador: $x^3-7x+6$. Probando raíces: $x=1\Rightarrow 1-7+6=0$; $x=2\Rightarrow 8-14+6=0$; $x=-3\Rightarrow -27+21+6=0$. Así $x^3-7x+6=(x-1)(x-2)(x+3)$.

Raíces comunes: $x=2$ y $x=-3$.

- **$a=2$:** $\dfrac{x(x+3)(x-2)}{(x-1)(x-2)(x+3)}=\dfrac{x}{x-1}\Big|_{x=2}=\dfrac{2}{1}=2.$
- **$a=-3$:** $\dfrac{x}{x-1}\Big|_{x=-3}=\dfrac{-3}{-4}=\dfrac{3}{4}.$



$$
\boxed{a=2\Rightarrow 2;\quad a=-3\Rightarrow \dfrac{3}{4}.}
$$



✓ Coincide con la respuesta oficial.

