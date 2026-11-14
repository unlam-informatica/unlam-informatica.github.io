---
title: Ejercicio 16 — Indeterminados en el infinito
slug: analisis-matematico-i/unidad-2/practica/ejercicio-16
sidebar:
  order: 16
  label: Ejercicio 16
---


Comparación de grados y técnicas para $x\to\infty$.

## 16a
$\lim_{x\to\infty}\dfrac{2x^2+x^4-\sqrt3}{3x^4-x+1/2}$

Mismo grado ($4$), cociente de coeficientes principales:



$$
\dfrac{1}{3}=\mathbf{\dfrac{1}{3}}
$$



✓ Coincide con la respuesta oficial.

## 16b
$\lim_{x\to\infty}\dfrac{x^3+4x^2-x+5}{2x^2-8x+1}$

Grado mayor arriba ($3>2$): $\to\infty=\mathbf{\infty}.$

✓ Coincide con la respuesta oficial.

## 16c
$\lim_{x\to\infty}\dfrac{2x^3-5x^2+1}{-3x^5-2x^3+3}$

Grado mayor abajo ($3<5$): $\to 0=\mathbf{0}.$

✓ Coincide con la respuesta oficial.

## 16d
$\lim_{x\to\infty}\left(\dfrac{2x^5-3x^4+1}{3x^5-2x^3-3}\right)^{\frac{6x^2+x-1}{3x^2-2x}}$

Base: cociente de grado $5$, tiende a $\dfrac{2}{3}$. Exponente: cociente de grado $2$, tiende a $\dfrac{6}{3}=2$. Como la base $\to\tfrac23\neq 1$:



$$
\to\left(\dfrac{2}{3}\right)^{2}=\dfrac{4}{9}=\mathbf{\dfrac{4}{9}}
$$



✓ Coincide con la respuesta oficial.

## 16e
$\lim_{x\to\infty}\left(\sqrt{\dfrac{1-x}{1-64x}}\cdot\dfrac{1+2x}{3x-1}\right)$

Primer factor: dentro de la raíz, cociente de grado $1$ con coeficientes $\dfrac{-1}{-64}=\dfrac{1}{64}$, luego $\sqrt{\tfrac{1}{64}}=\dfrac{1}{8}$. Segundo factor: $\dfrac{1+2x}{3x-1}\to\dfrac{2}{3}$.



$$
\to\dfrac{1}{8}\cdot\dfrac{2}{3}=\dfrac{2}{24}=\dfrac{1}{12}
$$



> ⚠️ **Discrepancia:** Resultado calculado: $\dfrac{1}{12}$. Respuesta del documento: $\dfrac{1}{4}$.
>
> Recalculo cuidadoso: $\sqrt{\tfrac{1-x}{1-64x}}\to\sqrt{\tfrac{1}{64}}=\tfrac18$ y $\tfrac{1+2x}{3x-1}\to\tfrac23$, cuyo producto es $\tfrac{1}{12}$. Para obtener $\tfrac14$ el segundo factor debería tender a $2$ (p. ej. $\tfrac{1+2x}{x-1}$) o el radicando a $\tfrac{1}{16}$. Con el enunciado tal como está escrito, el valor correcto es $\dfrac{1}{12}$. Posible errata en el enunciado/respuesta oficial.

## 16f
* $\lim_{x\to\infty}\dfrac{\sqrt{9x^2+6}}{5x-2}$ (lateral $\pm\infty$)

Para $x\to+\infty$, $\sqrt{9x^2+6}\sim \sqrt{9x^2}=3\lvert x\rvert=3x$:



$$
\dfrac{3x}{5x}\to\dfrac{3}{5}
$$



Para $x\to-\infty$, $\sqrt{9x^2+6}=3\lvert x\rvert=-3x$ y $5x-2<0$:



$$
\dfrac{-3x}{5x}\to-\dfrac{3}{5}
$$





$$
\boxed{x\to+\infty:\ \dfrac{3}{5};\qquad x\to-\infty:\ -\dfrac{3}{5}.}
$$



✓ Coincide con la respuesta oficial.

## 16g
$\lim_{x\to\infty}\dfrac{x+\operatorname{sen}x}{x-\cos x}$

Dividimos por $x$: $\dfrac{1+\frac{\operatorname{sen}x}{x}}{1-\frac{\cos x}{x}}$. Los términos acotados sobre $x$ tienden a $0$:



$$
\to\dfrac{1+0}{1-0}=1=\mathbf{1}
$$



✓ Coincide con la respuesta oficial.

