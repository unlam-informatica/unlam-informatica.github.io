---
title: Ejercicio 27 — $A(t)=100(1-0{,}9^t)$, $t\in[0,10]$ (mg)
slug: analisis-matematico-i/unidad-1/practica/ejercicio-27
sidebar:
  order: 27
---


## 27a - Variables, dominio/imagen

Independiente: tiempo $t$. Dependiente: cantidad $A$ (mg). En $t=0$, $A=0$; en $t=10$, $A=100(1-0{,}9^{10})$.

**Resultado: $D=[0,10]$, $I=\left[0,\,100(1-0{,}9^{10})\right]\approx[0;\,65{,}13]$.** ✓ Coincide.

## 27b - ¿Qué es $A^{-1}$? Hallarla

$A^{-1}$ da el **tiempo** en función de la cantidad de mg absorbida.



$$
A=100(1-0{,}9^t)\Rightarrow 1-0{,}9^t=\dfrac{A}{100}\Rightarrow 0{,}9^t=1-\dfrac{A}{100}\Rightarrow t=\dfrac{\ln\!\left(1-\tfrac{A}{100}\right)}{\ln0{,}9}
$$



**Resultado: $t(A)=\dfrac{\ln\!\left(1-\tfrac{A}{100}\right)}{\ln0{,}9}$.** ✓ Coincide.

## 27c - Minutos para $50$ mg



$$
0{,}9^t=1-\dfrac{50}{100}=0{,}5\Rightarrow t=\dfrac{\ln0{,}5}{\ln0{,}9}\approx\dfrac{-0{,}6931}{-0{,}1054}\approx6{,}58
$$



**Resultado: $\approx6{,}58$ min.** ✓ Coincide.

