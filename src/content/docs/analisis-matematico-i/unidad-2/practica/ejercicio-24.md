---
title: Ejercicio 24 — Asíntotas (AV, AH, AO)
slug: analisis-matematico-i/unidad-2/practica/ejercicio-24
sidebar:
  order: 24
  label: Ejercicio 24
---


## 24a
$f(x)=\dfrac{2x^2-x}{x^2-1}$

**AV:** denominador $x^2-1=(x-1)(x+1)=0\Rightarrow x=1,\ x=-1$ (numerador $\neq0$ allí). 

**AH:** mismo grado, $\lim_{x\to\infty}\dfrac{2x^2-x}{x^2-1}=\dfrac{2}{1}=2\Rightarrow y=2$.



$$
\boxed{\text{AV: }x=1,\ x=-1;\quad \text{AH: }y=2.}
$$



✓ Coincide con la respuesta oficial.

## 24b
$f(x)=\dfrac{2(x-1)^2}{x+1/2}$

**AV:** $x+\tfrac12=0\Rightarrow x=-\tfrac12$.

**AO:** numerador grado $2$, denominador grado $1$ (difieren en uno). $f(x)=\dfrac{2x^2-4x+2}{x+1/2}$. Dividiendo: $2x^2-4x+2=(x+\tfrac12)(2x-5)+\tfrac{9}{2}$, luego



$$
f(x)=2x-5+\dfrac{9/2}{x+1/2}\Rightarrow y=2x-5
$$





$$
\boxed{\text{AV: }x=-\tfrac12;\quad \text{AO: }y=2x-5.}
$$



✓ Coincide con la respuesta oficial.

## 24c
$f(x)=\sqrt{x^2+1}$

**AO:** $m=\lim_{x\to+\infty}\dfrac{\sqrt{x^2+1}}{x}=1$; $b=\lim_{x\to+\infty}(\sqrt{x^2+1}-x)=0$ (racionalizando) $\Rightarrow y=x$.

Para $x\to-\infty$: $m=\lim\dfrac{\sqrt{x^2+1}}{x}=-1$ (pues $\sqrt{x^2+1}\sim -x$); $b=\lim(\sqrt{x^2+1}+x)=0\Rightarrow y=-x$.



$$
\boxed{y=x\ (x\to+\infty);\quad y=-x\ (x\to-\infty).}
$$



✓ Coincide con la respuesta oficial.

## 24d
$f(x)=\dfrac{3x}{x-1}+3x$

**AV:** $x=1$ (por el primer término).

**AO:** $\dfrac{3x}{x-1}=3+\dfrac{3}{x-1}\to3$, luego $f(x)=3x+3+\dfrac{3}{x-1}$, y el término residual $\to0$:



$$
y=3x+3
$$





$$
\boxed{\text{AV: }x=1;\quad \text{AO: }y=3x+3.}
$$



✓ Coincide con la respuesta oficial.

## 24e
$f(x)=\dfrac{\operatorname{sen}x}{x}$

**AH:** $\lim_{x\to\pm\infty}\dfrac{\operatorname{sen}x}{x}=0$ (acotado sobre infinito) $\Rightarrow y=0$. No hay AV (en $x=0$ el límite es $1$, finito: discontinuidad evitable, no asíntota).



$$
\boxed{\text{AH: }y=0.}
$$



✓ Coincide con la respuesta oficial.

## 24f
$f(x)=\dfrac{x^3+1}{x^3+x}$

**AV:** $x^3+x=x(x^2+1)=0\Rightarrow x=0$ (las otras raíces son complejas). En $x=0$ numerador $=1\neq0$, hay AV.

**AH:** mismo grado, $\dfrac{1}{1}=1\Rightarrow y=1$.



$$
\boxed{\text{AV: }x=0;\quad \text{AH: }y=1.}
$$



✓ Coincide con la respuesta oficial.

## 24g
* $f(x)=\dfrac{1}{e^x-1}$

**AV:** $e^x-1=0\Rightarrow x=0$.

**AH ($x\to+\infty$):** $e^x\to\infty\Rightarrow f\to0\Rightarrow y=0$.

**AH ($x\to-\infty$):** $e^x\to0\Rightarrow \dfrac{1}{0-1}=-1\Rightarrow y=-1$.



$$
\boxed{\text{AV: }x=0;\quad y=0\ (x\to+\infty);\quad y=-1\ (x\to-\infty).}
$$



✓ Coincide con la respuesta oficial.

## 24h
$g(x)=e^{1/x}$

**AV:** en $x=0$, $\lim_{x\to0^+}e^{1/x}=e^{+\infty}=+\infty$ (AV por derecha); $\lim_{x\to0^-}e^{1/x}=e^{-\infty}=0$ (sin AV por izquierda).

**AH:** $\lim_{x\to\pm\infty}e^{1/x}=e^{0}=1\Rightarrow y=1$.



$$
\boxed{\text{AV: }x=0\ \text{(por derecha)};\quad \text{AH: }y=1.}
$$



✓ Coincide con la respuesta oficial.

## 24i
$f(x)=\dfrac{x}{\sqrt[4]{x^4+1}}$

**AH ($x\to+\infty$):** $\sqrt[4]{x^4+1}\sim x$, luego $\dfrac{x}{x}\to1\Rightarrow y=1$.

**AH ($x\to-\infty$):** $\sqrt[4]{x^4+1}\sim \lvert x\rvert=-x$, luego $\dfrac{x}{-x}\to-1\Rightarrow y=-1$.



$$
\boxed{y=1\ (x\to+\infty);\quad y=-1\ (x\to-\infty).}
$$



✓ Coincide con la respuesta oficial.

## 24j
$h(x)=\dfrac{x^2-4x}{x^3-2x}$

Factorizamos: $\dfrac{x(x-4)}{x(x^2-2)}=\dfrac{x-4}{x^2-2}$ (con hueco evitable en $x=0$).

**AV:** $x^2-2=0\Rightarrow x=\sqrt2,\ x=-\sqrt2$.

**AH:** grado mayor abajo $\Rightarrow y=0$.



$$
\boxed{\text{AV: }x=\sqrt2,\ x=-\sqrt2;\quad \text{AH: }y=0.}
$$



✓ Coincide con la respuesta oficial.

