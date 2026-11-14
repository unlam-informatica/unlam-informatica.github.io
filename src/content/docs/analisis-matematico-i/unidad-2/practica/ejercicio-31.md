---
title: Ejercicio 31 — Salto en la discontinuidad
slug: analisis-matematico-i/unidad-2/practica/ejercicio-31
sidebar:
  order: 31
  label: Ejercicio 31
---


El salto es $S=\big\lvert \lim_{x\to a^+}f-\lim_{x\to a^-}f\big\rvert$ (o la diferencia de laterales).

## 31a
$f(x)=\dfrac{1-10^{1/x}}{1+10^{1/x}}$ en $x=0$

**$x\to0^+$:** $\tfrac1x\to+\infty$, $10^{1/x}\to\infty$. Dividiendo por $10^{1/x}$: $\dfrac{10^{-1/x}-1}{10^{-1/x}+1}\to\dfrac{0-1}{0+1}=-1$.

**$x\to0^-$:** $\tfrac1x\to-\infty$, $10^{1/x}\to0$: $\dfrac{1-0}{1+0}=1$.



$$
S=\lvert -1-1\rvert=2=\mathbf{2}
$$



✓ Coincide con la respuesta oficial.

## 31b
$f(x)=\begin{cases}\dfrac{\operatorname{sen}x}{x} & x>0\\ \dfrac{\operatorname{sen}5x}{3x} & x<0\end{cases}$ en $x=0$

**$x\to0^+$:** $\dfrac{\operatorname{sen}x}{x}\to1$.

**$x\to0^-$:** $\dfrac{\operatorname{sen}5x}{3x}\to\dfrac{5}{3}$.



$$
S=\left\lvert 1-\dfrac{5}{3}\right\rvert=\dfrac{2}{3}=\mathbf{\dfrac{2}{3}}
$$



✓ Coincide con la respuesta oficial.

## 31c
$f(x)=\begin{cases}5x+1 & x>0\\ x+12 & x\le0\end{cases}$ en $x=0$

**$x\to0^+$:** $5\cdot0+1=1$. **$x\to0^-$:** $0+12=12$.



$$
S=\lvert 1-12\rvert=11=\mathbf{11}
$$



✓ Coincide con la respuesta oficial.

