---
title: Ejercicio 14 — Límites trigonométricos
slug: analisis-matematico-i/unidad-2/practica/ejercicio-14
sidebar:
  order: 14
  label: Ejercicio 14
---


Idea de trabajo: cuando el ángulo tiende a $0$, usamos las equivalencias
$\operatorname{sen}u\sim u$, $1-\cos u\sim \tfrac{u^2}{2}$ y $\tan u\sim u$.
Así convertimos cada expresión en una forma más simple para evaluar el límite.

## 14a
$\lim_{x\to0}\dfrac{\operatorname{sen}4x}{3x}$

Primero reescribimos la expresión para que aparezca el límite notable $\dfrac{\operatorname{sen}u}{u}$:



$$
\dfrac{\operatorname{sen}4x}{3x}=\dfrac{4}{3}\cdot\dfrac{\operatorname{sen}4x}{4x}
$$



Ahora usamos que, cuando $x\to0$, también $4x\to0$ y entonces
$\dfrac{\operatorname{sen}4x}{4x}\to1$:



$$
\dfrac{4}{3}\cdot\dfrac{\operatorname{sen}4x}{4x}\to\dfrac{4}{3}\cdot1=\mathbf{\dfrac{4}{3}}
$$



**Verificación:** coincide con la respuesta oficial.

## 14b
$\lim_{x\to0}\dfrac{\operatorname{sen}4x}{\operatorname{sen}5x}$

Usamos las equivalencias cerca de $0$:



$$
\operatorname{sen}4x\sim4x \qquad \operatorname{sen}5x\sim5x
$$



Entonces el cociente se comporta como



$$
\dfrac{\operatorname{sen}4x}{\operatorname{sen}5x}\sim\dfrac{4x}{5x}
$$



Simplificamos $x$ y obtenemos:



$$
\dfrac{4x}{5x}=\dfrac{4}{5}=\mathbf{\dfrac{4}{5}}
$$



**Verificación:** coincide con la respuesta oficial.

## 14c
$\lim_{x\to0}\dfrac{\operatorname{sen}^2 3x}{4x^2}$

Primero reemplazamos $\operatorname{sen}3x$ por su equivalencia:



$$
\operatorname{sen}3x\sim3x
$$



Como la expresión está al cuadrado, también podemos escribir:



$$
\operatorname{sen}^2 3x\sim(3x)^2=9x^2
$$



Entonces:



$$
\dfrac{\operatorname{sen}^2 3x}{4x^2}\sim\dfrac{9x^2}{4x^2}=\dfrac{9}{4}=\mathbf{\dfrac{9}{4}}
$$



**Verificación:** coincide con la respuesta oficial.

## 14d
$\lim_{x\to0}\dfrac{x\operatorname{sen}x}{1-\cos x}$

Analizamos numerador y denominador por separado.

Para el numerador, usamos $\operatorname{sen}x\sim x$:



$$
x\operatorname{sen}x\sim x\cdot x=x^2
$$



Para el denominador, usamos la equivalencia conocida:



$$
1-\cos x\sim \frac{x^2}{2}
$$



Entonces el cociente queda:



$$
\dfrac{x^2}{x^2/2}=2=\mathbf{2}
$$



**Verificación:** coincide con la respuesta oficial.

## 14e
$\lim_{z\to0}\dfrac{1-\cos 3z}{z^2}$

Usamos la equivalencia $1-\cos u\sim \tfrac{u^2}{2}$ con $u=3z$:



$$
1-\cos 3z\sim \frac{(3z)^2}{2}=\frac{9z^2}{2}
$$



Ahora dividimos por $z^2$ y simplificamos:



$$
\dfrac{1-\cos 3z}{z^2}\sim\dfrac{9z^2/2}{z^2}=\dfrac{9}{2}=\mathbf{\dfrac{9}{2}}
$$



**Verificación:** coincide con la respuesta oficial.

## 14f
$\lim_{x\to a}\dfrac{\operatorname{sen}(x-a)}{x-a}$

Hacemos el cambio de variable



$$
u=x-a
$$



Entonces, cuando $x\to a$, se cumple $u\to0$ y el límite queda:



$$
\lim_{u\to0}\frac{\operatorname{sen}u}{u}=\mathbf{1}
$$



**Verificación:** coincide con la respuesta oficial.

## 14g
$\lim_{x\to0^+}\left(\dfrac{\operatorname{sen}2x}{x}\right)^{\tan 3x/x}$

Estudiamos base y exponente por separado.

La base es



$$
\dfrac{\operatorname{sen}2x}{x}=\frac{\operatorname{sen}2x}{2x}\cdot2
$$



como $\dfrac{\operatorname{sen}2x}{2x}\to1$, entonces la base tiende a $2$.

Para el exponente:



$$
\dfrac{\tan 3x}{x}=\frac{\tan 3x}{3x}\cdot3
$$



y como $\dfrac{\tan 3x}{3x}\to1$, el exponente tiende a $3$.

Como la base tiende a un número distinto de $1$, no aparece la indeterminación $1^\infty$:



$$
\left(\dfrac{\operatorname{sen}2x}{x}\right)^{\tan 3x/x}\to2^3=\mathbf{8}
$$



**Verificación:** coincide con la respuesta oficial.

## 14h
$\lim_{x\to0}\dfrac{2\operatorname{sen}x+3x\cos x}{3\operatorname{sen}x-x\cos x}$

El numerador y el denominador tienen factor $x$ en todos los términos, así que dividimos todo por $x$:



$$
\dfrac{2\operatorname{sen}x+3x\cos x}{3\operatorname{sen}x-x\cos x}
=
\dfrac{2\frac{\operatorname{sen}x}{x}+3\cos x}{3\frac{\operatorname{sen}x}{x}-\cos x}
$$



Ahora usamos los límites notables:



$$
\frac{\operatorname{sen}x}{x}\to1 \qquad \cos x\to1
$$



Entonces:



$$
\dfrac{2\frac{\operatorname{sen}x}{x}+3\cos x}{3\frac{\operatorname{sen}x}{x}-\cos x}\to\dfrac{2\cdot1+3\cdot1}{3\cdot1-1}=\dfrac{5}{2}=\mathbf{\dfrac{5}{2}}
$$



**Verificación:** coincide con la respuesta oficial.

## 14i
$\lim_{x\to3}\dfrac{\operatorname{sen}(x^2-10x+21)}{x-3}$

Primero factorizamos el polinomio del argumento:



$$
x^2-10x+21=(x-3)(x-7)
$$



Como estamos tomando $x\to3$, el producto $(x-3)(x-7)\to0$. Entonces el seno del argumento se puede tratar con el límite notable $\dfrac{\operatorname{sen}u}{u}$.

Reescribimos el cociente multiplicando y dividiendo por $(x-7)$:



$$
\dfrac{\operatorname{sen}\big((x-3)(x-7)\big)}{x-3}=\dfrac{\operatorname{sen}\big((x-3)(x-7)\big)}{(x-3)(x-7)}\cdot(x-7)
$$



Ahora vemos cada factor por separado:

- $\dfrac{\operatorname{sen}\big((x-3)(x-7)\big)}{(x-3)(x-7)}\to1$
- $x-7\to3-7=-4$

Por lo tanto:



$$
1\cdot(-4)=\mathbf{-4}
$$



**Verificación:** coincide con la respuesta oficial.
