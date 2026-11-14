---
title: Ejercicio 30 — Construcción de ejemplos
slug: analisis-matematico-i/unidad-2/practica/ejercicio-30
sidebar:
  order: 30
  label: Ejercicio 30
---


## 30a
Evitable en $2$ y esencial de salto infinito en $-1$

Un ejemplo simple:



$$
f(x)=\dfrac{(x-2)}{(x-2)(x+1)}=\dfrac{1}{x+1}\ \text{(con hueco en }x=2)
$$



- En $x=2$: el factor $(x-2)$ se cancela, $\lim_{x\to2}f=\dfrac{1}{3}$ finito, pero $f(2)$ no existe $\Rightarrow$ **evitable**.
- En $x=-1$: denominador $\to0$, $\to\pm\infty$ $\Rightarrow$ **esencial salto infinito**.

## 30b
Esencial de salto finito en $1$ y evitable en $0$ con $0\in$ dominio



$$
f(x)=\begin{cases}\dfrac{\operatorname{sen}x}{x} & x\neq0,\ x<1\\ 5 & x=0\\ x+10 & x\ge1\end{cases}
$$



- En $x=0$: $\lim=\dfrac{\operatorname{sen}x}{x}\to1$ pero $f(0)=5\neq1$, con $0$ en el dominio $\Rightarrow$ **evitable**.
- En $x=1$: $\lim_{x\to1^-}\dfrac{\operatorname{sen}x}{x}=\operatorname{sen}1\approx0{,}84$; $\lim_{x\to1^+}(x+10)=11$. Laterales finitos distintos $\Rightarrow$ **esencial salto finito**.

(Cualquier ejemplo que cumpla las condiciones es válido.)

