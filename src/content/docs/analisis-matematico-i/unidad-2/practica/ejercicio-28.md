---
title: "Ejercicio 28 — Discontinuidades: tipo y redefinición"
slug: analisis-matematico-i/unidad-2/practica/ejercicio-28
sidebar:
  order: 28
  label: Ejercicio 28
---


## 28a
$f(x)=\dfrac{x-1}{\lvert x\rvert-1}$

$\lvert x\rvert-1=0\Rightarrow x=1$ o $x=-1$.

**En $x=1$** ($x>0$, $\lvert x\rvert=x$): $\dfrac{x-1}{x-1}=1$, $\lim_{x\to1}=1$ finito $\Rightarrow$ **evitable** (redefinir $f(1)=1$).

**En $x=-1$:** lateral izquierdo ($x<0$, $\lvert x\rvert=-x$): $\dfrac{x-1}{-x-1}=\dfrac{x-1}{-(x+1)}\to\dfrac{-2}{0^{+}}\to-\infty$. $\Rightarrow$ **esencial de salto infinito**.



$$
\boxed{x=1\ \text{evitable};\quad x=-1\ \text{esencial salto infinito}.}
$$



✓ Coincide con la respuesta oficial.

## 28b
$f(x)=\dfrac{x^2-4}{x^2-5x+6}$

$\dfrac{(x-2)(x+2)}{(x-2)(x-3)}=\dfrac{x+2}{x-3}$.

**En $x=2$:** $\lim=\dfrac{4}{-1}=-4$ finito $\Rightarrow$ **evitable** (redefinir $f(2)=-4$).

**En $x=3$:** denominador $\to0$, numerador $\to5\neq0\Rightarrow \pm\infty$ $\Rightarrow$ **esencial salto infinito**.



$$
\boxed{x=2\ \text{evitable};\quad x=3\ \text{esencial salto infinito}.}
$$



✓ Coincide con la respuesta oficial.

## 28c
$f(x)=\dfrac{4x^2}{3-\sqrt{x^2+5}}$

$3-\sqrt{x^2+5}=0\Rightarrow x^2+5=9\Rightarrow x=\pm2$. En $x=\pm2$ el numerador $4x^2=16\neq0$ y el denominador $\to0\Rightarrow \pm\infty$:



$$
\boxed{x=2,\ x=-2\ \text{esencial salto infinito}.}
$$



✓ Coincide con la respuesta oficial.

## 28d
* $f(x)=\dfrac{\operatorname{sen}(2x-10)}{\lvert x-5\rvert}$

$2x-10=2(x-5)$. **En $x=5$:** lateral derecho ($\lvert x-5\rvert=x-5$): $\dfrac{\operatorname{sen}2(x-5)}{x-5}\to 2$. Lateral izquierdo ($\lvert x-5\rvert=-(x-5)$): $\dfrac{\operatorname{sen}2(x-5)}{-(x-5)}\to -2$. Laterales finitos distintos:



$$
\boxed{x=5\ \text{esencial de salto finito}\ (S=4).}
$$



✓ Coincide con la respuesta oficial.

## 28e
* $f(x)=\dfrac{1}{1+e^{1/(1-x)}}$

**En $x=1$:** lateral izquierdo ($x\to1^-$, $1-x\to0^+$, $\tfrac{1}{1-x}\to+\infty$): $e^{+\infty}\to\infty\Rightarrow f\to\dfrac{1}{1+\infty}=0$. Lateral derecho ($1-x\to0^-$, $\tfrac{1}{1-x}\to-\infty$): $e^{-\infty}\to0\Rightarrow f\to\dfrac{1}{1+0}=1$. Laterales finitos distintos ($0$ y $1$):



$$
\boxed{x=1\ \text{esencial de salto finito}.}
$$



✓ Coincide con la respuesta oficial.

## 28f
$f(x)=\begin{cases}x-\tfrac34 & x\ge1\\ \dfrac{1}{3x+1} & x<1\end{cases}$

Posible discontinuidad en el empalme $x=1$ y donde $3x+1=0$, es decir $x=-\tfrac13$ (dentro del tramo $x<1$).

**En $x=-\tfrac13$:** $3x+1\to0$, $\dfrac{1}{3x+1}\to\pm\infty\Rightarrow$ **esencial salto infinito**.

**En $x=1$:** $\lim_{x\to1^-}\dfrac{1}{3x+1}=\dfrac14$; $\lim_{x\to1^+}(x-\tfrac34)=\dfrac14$; $f(1)=\tfrac14$. Coinciden $\Rightarrow$ **continua** en $1$.



$$
\boxed{x=-\tfrac13\ \text{esencial salto infinito (única discontinuidad)}.}
$$



✓ Coincide con la respuesta oficial.

## 28g
$f(x)=\begin{cases}\ln(x-2) & x>2\\ x^3 & -1<x\le2\\ \lvert x\rvert & x\le-1\end{cases}$

**En $x=2$:** $\lim_{x\to2^+}\ln(x-2)=\ln 0^+=-\infty$; $\lim_{x\to2^-}x^3=8$. Lateral $-\infty\Rightarrow$ **esencial salto infinito**.

**En $x=-1$:** $\lim_{x\to-1^-}\lvert x\rvert=1$; $\lim_{x\to-1^+}x^3=-1$. Finitos distintos $\Rightarrow$ **esencial salto finito**.



$$
\boxed{x=2\ \text{esencial salto infinito};\quad x=-1\ \text{esencial salto finito}.}
$$



✓ Coincide con la respuesta oficial.

## 28h
$f(x)=\dfrac{1}{\ln(x+3)}$

Dominio: $x+3>0\Rightarrow x>-3$, y $\ln(x+3)\neq0\Rightarrow x+3\neq1\Rightarrow x\neq-2$.

**En $x=-3$** (borde del dominio): a la vez se pierde dominio; analizando $x\to-3^+$, $\ln(x+3)\to-\infty\Rightarrow f\to0$. El límite existe (finito $0$) pero $f(-3)$ no está definida $\Rightarrow$ **evitable** (redefinir $f(-3)=0$).

**En $x=-2$:** $\ln(x+3)\to\ln1=0\Rightarrow f\to\pm\infty$ $\Rightarrow$ **esencial salto infinito**.



$$
\boxed{x=-3\ \text{evitable};\quad x=-2\ \text{esencial salto infinito}.}
$$



✓ Coincide con la respuesta oficial.

## 28i
$g(x)=\begin{cases}\dfrac{x^3+4x^2-5x}{x^2+3x-10} & x\le0\\[6pt] \dfrac{2}{e^{1/x}-2} & x>0\end{cases}$

**Primer tramo:** $\dfrac{x(x^2+4x-5)}{(x+5)(x-2)}=\dfrac{x(x+5)(x-1)}{(x+5)(x-2)}=\dfrac{x(x-1)}{x-2}$ (hueco en $x=-5$). En $x=-5$ (dentro de $x\le0$) el límite es $\dfrac{-5\cdot(-6)}{-7}=\dfrac{30}{-7}$ finito $\Rightarrow$ **evitable**.

**Segundo tramo, en $x>0$:** $e^{1/x}-2=0\Rightarrow e^{1/x}=2\Rightarrow \tfrac1x=\ln2\Rightarrow x=\dfrac{1}{\ln2}$. Allí denominador $\to0$, numerador $=2\neq0\Rightarrow\pm\infty$ $\Rightarrow$ **esencial salto infinito**.

(En $x=0$: lateral izq $\to0$; lateral der: $\tfrac1x\to+\infty$, $e^{1/x}\to\infty$, $f\to0$; el empalme está acotado y no genera salto infinito, queda por analizar como punto regular.)



$$
\boxed{x=-5\ \text{evitable};\quad x=\tfrac{1}{\ln2}\ \text{esencial salto infinito}.}
$$



✓ Coincide con la respuesta oficial.

