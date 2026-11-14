---
title: Ejercicio 2 — Límites inmediatos
slug: analisis-matematico-i/unidad-2/practica/ejercicio-2
sidebar:
  order: 2
  label: Ejercicio 2
---


Calcular los siguientes límites inmediatos utilizando las propiedades algebraicas del límite y el límite de funciones elementales.

Por continuidad de las funciones elementales, reemplazamos directamente y verificamos que el resultado esté definido.

## 2a

:::note[Enunciado]
$\lim\limits_{x\to 2}(x^2-3x+1)$
:::

:::tip[Resolución]
El polinomio $x^2-3x+1$ es continuo en todo $\mathbb{R}$, así que evaluamos directamente en $x=2$:



$$
\lim_{x\to 2}(x^2-3x+1)=(2)^2-3(2)+1
$$





$$
=4-6+1=-1
$$



**Resultado:** $\lim\limits_{x\to 2}(x^2-3x+1)=-1$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 2b

:::note[Enunciado]
$\lim\limits_{x\to 1}\sqrt{\dfrac{x+1}{2x+1}}$
:::

:::tip[Resolución]
La función $\sqrt{\dfrac{x+1}{2x+1}}$ es continua en $x=1$ (numerador y denominador no nulos, cociente positivo). Evaluamos directamente:



$$
\lim_{x\to 1}\sqrt{\dfrac{x+1}{2x+1}}=\sqrt{\dfrac{1+1}{2\cdot 1+1}}
$$





$$
=\sqrt{\dfrac{2}{3}}
$$



Racionalizando:



$$
\sqrt{\dfrac{2}{3}}=\dfrac{\sqrt{2}}{\sqrt{3}}=\dfrac{\sqrt{6}}{3}\approx 0{,}816
$$



**Resultado:** $\lim\limits_{x\to 1}\sqrt{\dfrac{x+1}{2x+1}}=\sqrt{\dfrac{2}{3}}=\dfrac{\sqrt{6}}{3}$.

**Verificación:** Discrepa con la guía oficial, que reporta $\sqrt[3]{2/3}$ (raíz cúbica). La función del enunciado tiene raíz **cuadrada** (índice $2$), por lo que el resultado correcto es $\sqrt{2/3}$. La respuesta oficial parece tener un error tipográfico al cambiar el índice de la raíz.
:::

## 2c

:::note[Enunciado]
$\lim\limits_{x\to 3}\left(\dfrac{x^2+1}{x}\right)^{2x+1}$
:::

:::tip[Resolución]
La función base $\dfrac{x^2+1}{x}$ y el exponente $2x+1$ son continuos en $x=3$. Como además la base es positiva, podemos evaluar directamente.

Base en $x=3$:



$$
\dfrac{(3)^2+1}{3}=\dfrac{10}{3}
$$



Exponente en $x=3$:



$$
2\cdot 3+1=7
$$



Por lo tanto:



$$
\lim_{x\to 3}\left(\dfrac{x^2+1}{x}\right)^{2x+1}=\left(\dfrac{10}{3}\right)^{7}
$$



**Resultado:** $\lim\limits_{x\to 3}\left(\dfrac{x^2+1}{x}\right)^{2x+1}=\left(\dfrac{10}{3}\right)^{7}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 2d

:::note[Enunciado]
$\lim\limits_{x\to 3}\ln\lvert x^2-4x-1\rvert$
:::

:::tip[Resolución]
El logaritmo es continuo en su dominio (argumento positivo). El módulo $\lvert\cdot\rvert$ garantiza que el argumento sea no negativo. Verifiquemos que en $x=3$ el argumento no sea $0$.

Evaluamos $x^2-4x-1$ en $x=3$:



$$
(3)^2-4\cdot 3-1=9-12-1=-4
$$



Tomamos módulo:



$$
\lvert -4\rvert=4
$$



Por lo tanto:



$$
\lim_{x\to 3}\ln\lvert x^2-4x-1\rvert=\ln 4
$$



**Resultado:** $\lim\limits_{x\to 3}\ln\lvert x^2-4x-1\rvert=\ln 4=2\ln 2$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 2e

:::note[Enunciado]
$\lim\limits_{x\to \pi/2}(x\operatorname{sen} x+\cos x)$
:::

:::tip[Resolución]
El producto y suma de funciones continuas son continuas. Evaluamos directamente en $x=\pi/2$, usando $\operatorname{sen}(\pi/2)=1$ y $\cos(\pi/2)=0$:



$$
\lim_{x\to \pi/2}(x\operatorname{sen} x+\cos x)=\dfrac{\pi}{2}\cdot \operatorname{sen}\!\left(\dfrac{\pi}{2}\right)+\cos\!\left(\dfrac{\pi}{2}\right)
$$





$$
=\dfrac{\pi}{2}\cdot 1+0=\dfrac{\pi}{2}
$$



**Resultado:** $\lim\limits_{x\to \pi/2}(x\operatorname{sen} x+\cos x)=\dfrac{\pi}{2}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
