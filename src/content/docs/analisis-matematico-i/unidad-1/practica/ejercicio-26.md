---
title: Ejercicio 26 — Función inversa
slug: analisis-matematico-i/unidad-1/practica/ejercicio-26
sidebar:
  order: 26
  label: Ejercicio 26
---


Recordatorio: para invertir, $f$ debe ser **biyectiva** (inyectiva + sobreyectiva) en el dominio/codominio dados; se intercambian dominio e imagen.

## 26a - $f(x)=(x-1)^3+8$

Cúbica trasladada: biyectiva en $\mathbb{R}$. Despejamos:



$$
y-8=(x-1)^3\Rightarrow x-1=\sqrt[3]{y-8}\Rightarrow x=\sqrt[3]{y-8}+1
$$



**Resultado: $f^{-1}(x)=\sqrt[3]{x-8}+1$, $\mathbb{R}\to\mathbb{R}$.** ✓ Coincide.

## 26b - $f(x)=e^{2x}+1$

Inyectiva; imagen $(1,+\infty)$.



$$
y-1=e^{2x}\Rightarrow 2x=\ln(y-1)\Rightarrow x=\tfrac12\ln(y-1)
$$



**Resultado: $f:\mathbb{R}\to(1,+\infty)$, $f^{-1}(x)=\tfrac12\ln(x-1)$.** ✓ Coincide.

## 26c - $f(x)=3-\sqrt{x+5}$

$D=[-5,+\infty)$; como $\sqrt{x+5}\ge0$, $f(x)\le3$, imagen $(-\infty,3]$. Inyectiva (decreciente).



$$
y-3=-\sqrt{x+5}\Rightarrow\sqrt{x+5}=3-y\Rightarrow x+5=(3-y)^2\Rightarrow x=(3-y)^2-5
$$



**Resultado: $f:[-5,+\infty)\to(-\infty,3]$, $f^{-1}(x)=(3-x)^2-5$.** ✓ Coincide.

## 26d - $f(x)=\log_3(2x-4)$

$D:2x-4>0\Rightarrow x>2$, es decir $(2,+\infty)$; imagen $\mathbb{R}$.



$$
y=\log_3(2x-4)\Rightarrow 3^y=2x-4\Rightarrow x=\dfrac{3^y+4}{2}
$$



**Resultado: $f:(2,+\infty)\to\mathbb{R}$, $f^{-1}(x)=\dfrac{3^x+4}{2}$.** ✓ Coincide.

## 26e - $f(x)=2x^2-1$

No es inyectiva en $\mathbb{R}$ (parábola). Restringimos a $[0,+\infty)$ (rama derecha): imagen $[-1,+\infty)$.



$$
y+1=2x^2\Rightarrow x^2=\dfrac{y+1}{2}\Rightarrow x=\sqrt{\dfrac{y+1}{2}}\ (x\ge0)
$$



**Resultado: $f:[0,+\infty)\to[-1,+\infty)$, $f^{-1}(x)=\sqrt{\dfrac{x+1}{2}}$** (la rama $(-\infty,0]$ da $-\sqrt{\tfrac{x+1}{2}}$). ✓ Coincide.

## 26f - $f(x)=2\operatorname{sen}(3x)$

Se restringe a un intervalo donde $3x\in\left[-\tfrac\pi2,\tfrac\pi2\right]$, es decir $x\in\left[-\tfrac\pi6,\tfrac\pi6\right]$; imagen $[-2,2]$.



$$
y=2\operatorname{sen}(3x)\Rightarrow\operatorname{sen}(3x)=\dfrac y2\Rightarrow 3x=\arcsin\!\left(\dfrac y2\right)\Rightarrow x=\dfrac13\arcsin\!\left(\dfrac y2\right)
$$



**Resultado: $f:\left[-\tfrac\pi6,\tfrac\pi6\right]\to[-2,2]$, $f^{-1}(x)=\tfrac13\arcsin\!\left(\tfrac x2\right)$.** ✓ Coincide.

## 26g - $f(x)=\dfrac{-x+3}{x-1}$

$D=\mathbb{R}-\lbrace 1\rbrace $; AH $y=-1$, imagen $\mathbb{R}-\lbrace -1\rbrace $. Despejamos:



$$
y(x-1)=-x+3\Rightarrow yx-y=-x+3\Rightarrow x(y+1)=y+3\Rightarrow x=\dfrac{y+3}{y+1}
$$



**Resultado: $f:\mathbb{R}-\lbrace 1\rbrace \to\mathbb{R}-\lbrace -1\rbrace $, $f^{-1}(x)=\dfrac{x+3}{x+1}$.** ✓ Coincide.

