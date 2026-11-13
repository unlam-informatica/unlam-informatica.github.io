---
title: Ejercicio 29 — Parámetros para continuidad
slug: analisis-matematico-i/unidad-2/practica/ejercicio-29
sidebar:
  order: 29
---


## 29a



$$
f(x)=\begin{cases}\dfrac1x+a & x\le-1\\ -x+b & -1<x\le2\\ \dfrac{a}{x}-c & x>2\end{cases}
$$



con $f$ continua en $\mathbb{R}$ y $y=-3$ asíntota cuando $x\to+\infty$.

**Asíntota en $+\infty$:** $\lim_{x\to+\infty}\left(\dfrac{a}{x}-c\right)=-c=-3\Rightarrow c=3.$

**Continuidad en $x=-1$:** $\lim_{x\to-1^-}\left(\dfrac1x+a\right)=-1+a$; $\lim_{x\to-1^+}(-x+b)=1+b$. Igualamos: $-1+a=1+b\Rightarrow a-b=2.\ (\text{I})$

**Continuidad en $x=2$:** $\lim_{x\to2^-}(-x+b)=-2+b$; $\lim_{x\to2^+}\left(\dfrac{a}{x}-c\right)=\dfrac{a}{2}-3$. Igualamos: $-2+b=\dfrac{a}{2}-3\Rightarrow b=\dfrac{a}{2}-1.\ (\text{II})$

Sustituyendo (II) en (I): $a-\left(\dfrac{a}{2}-1\right)=2\Rightarrow \dfrac{a}{2}+1=2\Rightarrow a=2.$ Luego $b=\dfrac{2}{2}-1=0$.



$$
\boxed{a=2,\quad b=0,\quad c=3.}
$$



✓ Coincide con la respuesta oficial.

## 29b



$$
g(x)=\begin{cases}\dfrac{\operatorname{sen}(ax-2a)}{x^2-4} & x<2\\[6pt] \dfrac{x^2+x-6}{\sqrt{x^2+5}-3} & x>2\end{cases}
$$



Hallar $a$ para que exista el límite en $2$, y el valor $g(2)$ que la hace continua.

**Lateral derecho:** racionalizamos por $\sqrt{x^2+5}+3$:



$$
\dfrac{(x^2+x-6)(\sqrt{x^2+5}+3)}{(x^2+5)-9}=\dfrac{(x+3)(x-2)(\sqrt{x^2+5}+3)}{x^2-4}=\dfrac{(x+3)(x-2)(\sqrt{x^2+5}+3)}{(x-2)(x+2)}
$$





$$
=\dfrac{(x+3)(\sqrt{x^2+5}+3)}{x+2}\xrightarrow{x\to2^+}\dfrac{5\cdot(3+3)}{4}=\dfrac{30}{4}=\dfrac{15}{2}
$$



**Lateral izquierdo:** $\operatorname{sen}(ax-2a)=\operatorname{sen}\big(a(x-2)\big)$ y $x^2-4=(x-2)(x+2)$:



$$
\dfrac{\operatorname{sen}\big(a(x-2)\big)}{(x-2)(x+2)}=\dfrac{\operatorname{sen}\big(a(x-2)\big)}{a(x-2)}\cdot\dfrac{a}{x+2}\xrightarrow{x\to2^-}1\cdot\dfrac{a}{4}=\dfrac{a}{4}
$$



**Igualamos laterales:** $\dfrac{a}{4}=\dfrac{15}{2}\Rightarrow a=30.$ El valor común es $\dfrac{15}{2}$, así que para continuidad $g(2)=\dfrac{15}{2}$.



$$
\boxed{a=30,\quad g(2)=\dfrac{15}{2}.}
$$



✓ Coincide con la respuesta oficial.

## 29c

$f(x)=\dfrac{5x^2-a}{bx^2+cx+d}$ con $D=\mathbb{R}-\lbrace 1,2\rbrace $: $y=-1$ AH, $x=1$ AV, en $x=2$ evitable. Hallar $a,b,c,d$ y redefinir.

**AH $y=-1$:** grados iguales, coeficientes principales $\dfrac{5}{b}=-1\Rightarrow b=-5.$

**Denominador con raíces $1$ y $2$:** $bx^2+cx+d=-5(x-1)(x-2)=-5(x^2-3x+2)=-5x^2+15x-10\Rightarrow c=15,\ d=-10.$

**En $x=2$ evitable:** el numerador debe anularse en $x=2$: $5\cdot4-a=0\Rightarrow a=20.$

Verificación: $f(x)=\dfrac{5x^2-20}{-5x^2+15x-10}=\dfrac{5(x-2)(x+2)}{-5(x-1)(x-2)}=\dfrac{x+2}{-(x-1)}=\dfrac{x+2}{1-x}$ (con AV en $x=1$ y hueco en $x=2$). Valor en $x=2$: $\dfrac{4}{-1}=-4$, redefinir $f(2)=-4$.



$$
\boxed{a=20,\ b=-5,\ c=15,\ d=-10;\quad f(2):=-4.}
$$



✓ Coincide con la respuesta oficial.

