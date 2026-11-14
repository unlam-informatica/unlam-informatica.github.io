---
title: Ejercicio 28 — Resorte lineal $L(P)$
slug: analisis-matematico-i/unidad-1/practica/ejercicio-28
sidebar:
  order: 28
  label: Ejercicio 28
---


$7$ cm con $10$ g, $13$ cm con $80$ g.

Pendiente:



$$
m=\dfrac{13-7}{80-10}=\dfrac{6}{70}=\dfrac{3}{35}
$$



Ordenada (longitud sin peso): usando $(10,7)$,



$$
7=\dfrac{3}{35}\cdot10+b=\dfrac{30}{35}+b=\dfrac67+b\Rightarrow b=7-\dfrac67=\dfrac{49-6}{7}=\dfrac{43}{7}
$$



**Resultado: $L(P)=\dfrac{3}{35}P+\dfrac{43}{7}$.** ✓ Coincide.

## 28a - Longitud sin peso

$L(0)=\dfrac{43}{7}\approx6{,}14$ cm. ✓ Coincide.

## 28b - Variación cada $10$ g

$\Delta L=m\cdot10=\dfrac{3}{35}\cdot10=\dfrac{30}{35}=\dfrac67$ cm. ✓ Coincide.

## 28c - Dominio (se deforma al alargarse $5$ veces la longitud inicial)

Longitud inicial $\dfrac{43}{7}$; el límite es $5\cdot\dfrac{43}{7}=\dfrac{215}{7}$. El peso máximo $P_{\max}$ cumple $L(P_{\max})=\dfrac{215}{7}$:



$$
\dfrac{3}{35}P+\dfrac{43}{7}=\dfrac{215}{7}\Rightarrow\dfrac{3}{35}P=\dfrac{172}{7}\Rightarrow P=\dfrac{172}{7}\cdot\dfrac{35}{3}=\dfrac{172\cdot5}{3}=\dfrac{860}{3}
$$



**Resultado: $D=\left[0,\dfrac{860}{3}\right]$, $I=\left[\dfrac{43}{7},\dfrac{215}{7}\right]$.** ✓ Coincide.

## 28d - Inversa y significado



$$
L=\dfrac{3}{35}P+\dfrac{43}{7}\Rightarrow P=\dfrac{35}{3}\left(L-\dfrac{43}{7}\right)
$$



$L^{-1}$ da el **peso** necesario para una longitud dada.

