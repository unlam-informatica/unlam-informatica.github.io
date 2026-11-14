---
title: Ejercicio 31* — Marea $y=5+4{,}9\cos\!\left(\tfrac\pi6 t\right)$
slug: analisis-matematico-i/unidad-1/practica/ejercicio-31
sidebar:
  order: 31
  label: Ejercicio 31
---


## 31a - Gráfica en $[0,24]$ y terna

Coseno de amplitud $4{,}9$ centrado en $5$; período $\dfrac{2\pi}{\pi/6}=12$ h.

**Resultado: $y:[0,24]\to[0{,}1;\,9{,}9]$** (mín $5-4{,}9=0{,}1$, máx $5+4{,}9=9{,}9$). Verificar en GeoGebra.

## 31b - Nivel en marea alta

Cuando $\cos=1$ (en $t=0,12,24$): $y=5+4{,}9=9{,}9$.

**Resultado: $9{,}9$ pies.** ✓ Coincide.

## 31c - Marea baja

Cuando $\cos=-1$: $\dfrac\pi6 t=\pi\Rightarrow t=6$ (y $t=18$). $y=5-4{,}9=0{,}1$.

**Resultado: a las $6$ h y $18$ h, $0{,}1$ pies.** ✓ Coincide.

## 31d - Período y amplitud

**Resultado: período $12$ h, amplitud $4{,}9$ pies.** ✓ Coincide.

## 31e - Inversa restringida a las primeras $6$ h

En $[0,6]$ el coseno es inyectivo (decreciente). Despejamos:



$$
y-5=4{,}9\cos\!\left(\dfrac\pi6 t\right)\Rightarrow\cos\!\left(\dfrac\pi6 t\right)=\dfrac{y-5}{4{,}9}\Rightarrow\dfrac\pi6 t=\arccos\!\left(\dfrac{y-5}{4{,}9}\right)\Rightarrow t=\dfrac6\pi\arccos\!\left(\dfrac{y-5}{4{,}9}\right)
$$



**Resultado: $t=\dfrac6\pi\arccos\!\left(\dfrac{h-5}{4{,}9}\right)$.** ✓ Coincide.

