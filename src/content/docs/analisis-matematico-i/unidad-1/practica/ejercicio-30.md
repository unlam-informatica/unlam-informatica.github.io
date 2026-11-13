---
title: Ejercicio 30 — Masa de sustancia
slug: analisis-matematico-i/unidad-1/practica/ejercicio-30
sidebar:
  order: 30
---


$t=0,1,2,5\to$ masa $25,75,225,6075$. Cada paso multiplica por $3$ ($75/25=3$, $225/75=3$, y $6075/225=27=3^3$ ✓). Crecimiento exponencial $M(t)=25\cdot3^t$.

## 30a - Masa inicial

$M(0)=25$ g. ✓ Coincide.

## 30b - $M(t)$ (experimento $8$ h)

$M(8)=25\cdot3^8=25\cdot6561=164025$.

**Resultado: $M:[0,8]\to[25,\,164025]$, $M(t)=25\cdot3^t$.** ✓ Coincide.

## 30c - Inversa y significado



$$
M=25\cdot3^t\Rightarrow 3^t=\dfrac{M}{25}\Rightarrow t=\log_3\!\left(\dfrac{M}{25}\right)
$$



$M^{-1}$ da el **tiempo** necesario para alcanzar una masa dada. **Resultado: $t=\log_3\!\left(\tfrac{M}{25}\right)$.** ✓ Coincide.

