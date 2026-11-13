---
title: Ejercicio 13 — Gas $V(P)=\dfrac{30}{P}$, $V:[1,12]\to[2{,}5;30]$
slug: analisis-matematico-i/unidad-2/practica/ejercicio-13
sidebar:
  order: 13
---


## 13a
Cambios promedio $\dfrac{\Delta V}{\Delta P}$

$V(6)=\dfrac{30}{6}=5$. Calculamos $V$ en los extremos:

| Intervalo | $V$ en extremos | $\dfrac{\Delta V}{\Delta P}$ (l/atm) |
|---|---|---|
| $[5{,}7;\,6]$ | $V(5{,}7)=5{,}263158$ | $\dfrac{5-5{,}263158}{0{,}3}\approx -0{,}8772$ |
| $[5{,}8;\,6]$ | $V(5{,}8)=5{,}172414$ | $\dfrac{5-5{,}172414}{0{,}2}\approx -0{,}8621$ |
| $[5{,}9;\,6]$ | $V(5{,}9)=5{,}084746$ | $\dfrac{5-5{,}084746}{0{,}1}\approx -0{,}8475$ |
| $[6;\,6{,}1]$ | $V(6{,}1)=4{,}918033$ | $\dfrac{4{,}918033-5}{0{,}1}\approx -0{,}8197$ |
| $[6;\,6{,}2]$ | $V(6{,}2)=4{,}838710$ | $\dfrac{4{,}838710-5}{0{,}2}\approx -0{,}8065$ |
| $[6;\,6{,}3]$ | $V(6{,}3)=4{,}761905$ | $\dfrac{4{,}761905-5}{0{,}3}\approx -0{,}7937$ |

## 13b
Significado del signo

Todos los cocientes son **negativos**: al aumentar la presión $P$, el volumen $V$ **disminuye** (ley de Boyle, relación inversa).

## 13c
Razón instantánea en $P=6$



$$
\lim_{h\to0}\dfrac{V(6+h)-V(6)}{h}=\lim_{h\to0}\dfrac{\frac{30}{6+h}-5}{h}=\lim_{h\to0}\dfrac{\frac{30-5(6+h)}{6+h}}{h}=\lim_{h\to0}\dfrac{-5h}{(6+h)h}=\lim_{h\to0}\dfrac{-5}{6+h}=-\dfrac{5}{6}
$$





$$
\boxed{\dfrac{dV}{dP}\Big|_{P=6}=-\dfrac{5}{6}\approx -0{,}8333\ \text{l/atm}.}
$$



## 13d
Significado

Indica la **tasa instantánea** a la que cambia el volumen respecto de la presión en $P=6$: alrededor de esa presión, cada aumento de $1$ atm reduce el volumen unos $0{,}83$ litros.

✓ Coincide con la respuesta oficial.

