---
title: Ejercicio 32 — Constantes para continuidad en $\mathbb{R}$
slug: analisis-matematico-i/unidad-2/practica/ejercicio-32
sidebar:
  order: 32
  label: Ejercicio 32
---


## 32a
* $f(x)=\begin{cases}\dfrac{x^2-a^2}{x-a} & x\neq a\\ 8 & x=a\end{cases}$

$\dfrac{x^2-a^2}{x-a}=\dfrac{(x-a)(x+a)}{x-a}=x+a$, $\lim_{x\to a}=2a$. Para continuidad $2a=f(a)=8\Rightarrow a=4.$



$$
\boxed{a=4.}
$$



✓ Coincide con la respuesta oficial.

## 32b
$f(x)=\begin{cases}\dfrac{1-\cos ax}{4x^2} & x<0\\ \dfrac{2+x}{3x+1} & x\ge0\end{cases}$

**$x\to0^-$:** $1-\cos ax\sim \dfrac{(ax)^2}{2}=\dfrac{a^2x^2}{2}$, luego $\dfrac{a^2x^2/2}{4x^2}=\dfrac{a^2}{8}$.

**$x\to0^+$ y $f(0)$:** $\dfrac{2+0}{0+1}=2$.

Igualamos: $\dfrac{a^2}{8}=2\Rightarrow a^2=16\Rightarrow a=4\ \text{o}\ a=-4.$



$$
\boxed{a=4\ \text{o}\ a=-4.}
$$



✓ Coincide con la respuesta oficial.

## 32c
$f(x)=\begin{cases}\dfrac{x^2+x}{x^2-1} & x<-1\\ ax+b & -1\le x\le1\\ \dfrac{\operatorname{sen}(x-1)}{\ln(x+1)} & x>1\end{cases}$

**En $x=-1$:** lateral izquierdo $\dfrac{x^2+x}{x^2-1}=\dfrac{x(x+1)}{(x-1)(x+1)}=\dfrac{x}{x-1}\to\dfrac{-1}{-2}=\dfrac12$. Lateral derecho (tramo lineal): $a(-1)+b=-a+b$. Igualamos: $-a+b=\dfrac12.\ (\text{I})$

**En $x=1$:** lateral izquierdo (lineal): $a+b$. Lateral derecho: $\dfrac{\operatorname{sen}(x-1)}{\ln(x+1)}$. Con $u=x-1\to0$: $\dfrac{\operatorname{sen}u}{\ln(2+u)}\to\dfrac{0}{\ln2}=0$.

> Cuidado: $\ln(x+1)\to\ln2\neq0$, por lo que el cociente $\to\dfrac{\operatorname{sen}0}{\ln2}=0$. Igualamos: $a+b=0.\ (\text{II})$

De (II) $b=-a$; en (I): $-a-a=\dfrac12\Rightarrow -2a=\dfrac12\Rightarrow a=-\dfrac14$, y $b=\dfrac14$.



$$
\boxed{a=-\dfrac14,\quad b=\dfrac14.}
$$



✓ Coincide con la respuesta oficial.

