---
title: Ejercicio 24* — Profundidad sinusoidal
slug: analisis-matematico-i/unidad-1/practica/ejercicio-24
sidebar:
  order: 24
---


Ciclo cada $4$ h, mínimo $1$ m, máximo $2$ m. Modelo $p(t)=a\operatorname{sen}(bt)+c$.

## 24a - Variables

Independiente: tiempo $t$ (h). Dependiente: profundidad $p$ (m).

## 24b - Parámetros

- **Amplitud:** $a=\dfrac{\max-\min}{2}=\dfrac{2-1}{2}=\dfrac12$.
- **Desplazamiento vertical:** $c=\dfrac{\max+\min}{2}=\dfrac{2+1}{2}=\dfrac32$.
- **Frecuencia:** período $T=4\Rightarrow b=\dfrac{2\pi}{T}=\dfrac{2\pi}{4}=\dfrac\pi2$.

**Resultado: $p(t)=\dfrac12\operatorname{sen}\!\left(\dfrac\pi2 t\right)+\dfrac32$.** ✓ Coincide ($a=\tfrac12,b=\tfrac\pi2,c=\tfrac32$).

## 24c - Dominio e imagen (terna)

**Resultado: $p:[0,+\infty)\to[1,2]$.** ✓ Coincide.

## 24d - Profundidad a $6$ h



$$
p(6)=\dfrac12\operatorname{sen}\!\left(\dfrac\pi2\cdot6\right)+\dfrac32=\dfrac12\operatorname{sen}(3\pi)+\dfrac32=\dfrac12\cdot0+\dfrac32=1{,}5
$$



**Resultado: $1{,}5$ m.** ✓ Coincide.

## 24e - Variación entre $3$ y $4$ h

$p(3)=\dfrac12\operatorname{sen}\!\left(\dfrac{3\pi}{2}\right)+\dfrac32=\dfrac12(-1)+\dfrac32=1$.
$p(4)=\dfrac12\operatorname{sen}(2\pi)+\dfrac32=\dfrac32$.
Variación $=1{,}5-1=0{,}5$.

**Resultado: medio metro ($0{,}5$ m).** ✓ Coincide.

