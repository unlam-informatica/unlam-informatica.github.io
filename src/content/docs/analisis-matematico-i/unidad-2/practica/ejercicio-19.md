---
title: Ejercicio 19
slug: analisis-matematico-i/unidad-2/practica/ejercicio-19
sidebar:
  order: 19
---


**Enunciado.** Hallar $a,b,c$ para que



$$
f(x)=\begin{cases}\dfrac{a-bx}{x} & x\ge2\\[4pt] c-x & -1<x<2\\[4pt] \dfrac{1+ax}{x} & x\le-1\end{cases}
$$



tenga límite en $x=2$ y $x=-1$, con $\lim_{x\to+\infty}[f(x)+3]=0$.

**Resolución.**

**Condición en $+\infty$:** para $x\ge2$, $f(x)=\dfrac{a-bx}{x}=\dfrac{a}{x}-b\to -b$. Entonces $\lim_{x\to+\infty}[f(x)+3]=-b+3=0\Rightarrow b=3.$

**Límite en $x=2$:** lateral izquierdo $\lim_{x\to2^-}(c-x)=c-2$; lateral derecho $\lim_{x\to2^+}\dfrac{a-3x}{x}=\dfrac{a-6}{2}$. Igualamos:



$$
c-2=\dfrac{a-6}{2}.\qquad (\text{I})
$$



**Límite en $x=-1$:** lateral izquierdo $\lim_{x\to-1^-}\dfrac{1+ax}{x}=\dfrac{1-a}{-1}=a-1$; lateral derecho $\lim_{x\to-1^+}(c-x)=c+1$. Igualamos:



$$
a-1=c+1\Rightarrow c=a-2.\qquad (\text{II})
$$



Sustituimos (II) en (I): $(a-2)-2=\dfrac{a-6}{2}\Rightarrow a-4=\dfrac{a-6}{2}\Rightarrow 2a-8=a-6\Rightarrow a=2.$

Luego $c=a-2=0$.



$$
\boxed{a=2,\quad b=3,\quad c=0.}
$$



✓ Coincide con la respuesta oficial.

