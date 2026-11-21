---
title: Ejercicio 20 — Repaso
slug: analisis-matematico-i/unidad-2/practica/ejercicio-20
sidebar:
  order: 20
  label: Ejercicio 20
---


## 20a
$\lim_{x\to0}\dfrac{3x+4\operatorname{sen}2x}{x^2+5\operatorname{sen}x}$

Es la forma $\dfrac00$. Los términos $3x$ y $x^2$ no se pueden reemplazar por equivalentes dentro de una suma sin cuidado, así que dividimos numerador y denominador por $x$ y recién ahí usamos $\operatorname{sen}u\sim u$ en cada cociente:



$$
\dfrac{3x+4\operatorname{sen}2x}{x^2+5\operatorname{sen}x}=\dfrac{3+4\cdot 2\cdot\frac{\operatorname{sen}2x}{2x}}{x+5\,\frac{\operatorname{sen}x}{x}}\to\dfrac{3+4\cdot2\cdot1}{0+5\cdot1}=\dfrac{11}{5}=\mathbf{\dfrac{11}{5}}
$$



✓ Coincide con la respuesta oficial.

## 20b
$\lim_{x\to\infty}\dfrac{\sqrt{x^2+1}-x}{x+5}$ (laterales)

**$x\to+\infty$:** racionalizamos el numerador: $\sqrt{x^2+1}-x=\dfrac{1}{\sqrt{x^2+1}+x}\to0$. El denominador $\to+\infty$:



$$
\to\dfrac{0}{\infty}=0
$$



**$x\to-\infty$:** $\sqrt{x^2+1}\to-x$ (positivo), por lo que $\sqrt{x^2+1}-x\to -x-x=-2x\to+\infty$. Comparando grados: $\sqrt{x^2+1}\sim \lvert x\rvert=-x$, numerador $\sim -2x$, denominador $\sim x$:



$$
\dfrac{-2x}{x}\to -2
$$





$$
\boxed{x\to+\infty:\ 0;\qquad x\to-\infty:\ -2.}
$$



✓ Coincide con la respuesta oficial.

## 20c
$\lim_{x\to1}\dfrac{\sqrt{x+8}-3}{x^2-x}$

Racionalizamos por $\sqrt{x+8}+3$:



$$
\dfrac{(x+8)-9}{(x^2-x)(\sqrt{x+8}+3)}=\dfrac{x-1}{x(x-1)(\sqrt{x+8}+3)}=\dfrac{1}{x(\sqrt{x+8}+3)}
$$





$$
\lim_{x\to1}=\dfrac{1}{1\cdot(3+3)}=\dfrac{1}{6}=\mathbf{\dfrac{1}{6}}
$$



✓ Coincide con la respuesta oficial.

## 20d
$\lim_{x\to2}\left(\dfrac{x^2-1}{x-2}-\dfrac{x^2+x-2}{x^2-2x}\right)$

$\dfrac{x^2+x-2}{x^2-2x}=\dfrac{(x+2)(x-1)}{x(x-2)}$. Común denominador $x(x-2)$:



$$
\dfrac{x(x^2-1)-(x+2)(x-1)}{x(x-2)}=\dfrac{x^3-x-(x^2+x-2)}{x(x-2)}=\dfrac{x^3-x^2-2x+2}{x(x-2)}
$$



Numerador: $x^3-x^2-2x+2=x^2(x-1)-2(x-1)=(x-1)(x^2-2)$. En $x=2$ el numerador tiende a $(2-1)(4-2)=2\neq0$ y el denominador $x(x-2)$ tiende a $0$: no es una forma indeterminada, el cociente diverge. El signo depende del lado:

- por izquierda, $x(x-2)\to0^{-}$ (porque $x>0$ y $x-2<0$), así que el cociente tiende a $-\infty$;
- por derecha, $x(x-2)\to0^{+}$, así que tiende a $+\infty$.

Los laterales son distintos: el límite bilateral **no existe**. Lo que sí vale es que el valor absoluto crece sin cota, $\lvert f(x)\rvert\to+\infty$, y que $x=2$ es una asíntota vertical.

✓ Coincide con la respuesta oficial «$\infty$», leída como $\lvert f(x)\rvert\to\infty$ (divergencia sin signo determinado).

## 20e
$\lim_{x\to0}\left(\dfrac{\operatorname{sen}x}{x}+x\operatorname{sen}\tfrac1x\right)$

$\dfrac{\operatorname{sen}x}{x}\to1$. El término $x\operatorname{sen}\tfrac1x\to0$ (infinitésimo $x$ por factor acotado $\operatorname{sen}\tfrac1x\in[-1,1]$):



$$
\to 1+0=1=\mathbf{1}
$$



✓ Coincide con la respuesta oficial.

## 20f
$\lim_{x\to3^+}\left(\dfrac{x^2-4x+3}{4x-12}\right)^{1/(x-3)}$

Base: $\dfrac{x^2-4x+3}{4x-12}=\dfrac{(x-1)(x-3)}{4(x-3)}=\dfrac{x-1}{4}\to\dfrac{2}{4}=\dfrac{1}{2}$. La base $\to\tfrac12\neq1$ y el exponente $\dfrac{1}{x-3}\to+\infty$ (por derecha):



$$
\left(\dfrac{1}{2}\right)^{+\infty}=0
$$



> Nota: la base tiende a $\tfrac12<1$ con exponente $\to+\infty$, por eso el límite es $0$.



$$
\to\mathbf{0}
$$



✓ Coincide con la respuesta oficial.

