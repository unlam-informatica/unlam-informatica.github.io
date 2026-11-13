---
title: Ejercicio 21 — Bacterias $P(t)=\dfrac{4}{2+8e^{-2t}}$ (millones)
slug: analisis-matematico-i/unidad-2/practica/ejercicio-21
sidebar:
  order: 21
---


## 21a
Población inicial ($t=0$)



$$
P(0)=\dfrac{4}{2+8e^{0}}=\dfrac{4}{2+8}=\dfrac{4}{10}=0{,}4\ \text{millones}=\mathbf{400\,000\ \text{bacterias}}
$$



✓ Coincide con la respuesta oficial.

## 21b
Razón de cambio media entre día 1 y día 3



$$
P(1)=\dfrac{4}{2+8e^{-2}}=\dfrac{4}{2+8\cdot 0{,}135335}=\dfrac{4}{3{,}082685}\approx 1{,}29761\ \text{millones}
$$





$$
P(3)=\dfrac{4}{2+8e^{-6}}=\dfrac{4}{2+8\cdot 0{,}00247875}=\dfrac{4}{2{,}019830}\approx 1{,}98036\ \text{millones}
$$





$$
\dfrac{P(3)-P(1)}{3-1}=\dfrac{1{,}98036-1{,}29761}{2}\approx \dfrac{0{,}68275}{2}\approx 0{,}3414\ \text{millones/día}
$$



Es decir, un crecimiento medio de aproximadamente $\mathbf{341\,396\ \text{bacterias por día}}$.

✓ Coincide con la respuesta oficial.

## 21c
¿Se estabiliza?



$$
\lim_{t\to\infty}P(t)=\dfrac{4}{2+8e^{-2t}}\to\dfrac{4}{2+0}=2\ \text{millones}
$$



**Sí, la población se estabiliza en $2$ millones** (asíntota horizontal de la curva logística).

✓ Coincide con la respuesta oficial.

