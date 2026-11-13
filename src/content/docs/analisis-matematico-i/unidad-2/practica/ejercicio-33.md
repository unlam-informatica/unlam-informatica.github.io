---
title: Ejercicio 33 — Verdadero / Falso (justificar)
slug: analisis-matematico-i/unidad-2/practica/ejercicio-33
sidebar:
  order: 33
---


## 33a
$\lim_{x\to c}f=L\Rightarrow f(c)=L$ — **Falsa**

El límite no depende de $f(c)$. Contraejemplo: $f(x)=\dfrac{\operatorname{sen}x}{x}$ tiene $\lim_{x\to0}=1$ pero $f(0)$ no existe.

## 33b
Si $f(c)$ no está definida entonces no existe $\lim$ — **Falsa**

Mismo contraejemplo: el límite puede existir aunque $f(c)$ no esté definida (discontinuidad evitable).

## 33c
Si $\lim_{x\to c^-}=\lim_{x\to c^+}$ entonces $f$ es continua en $c$ — **Falsa**

Que existan y coincidan los laterales asegura que existe el límite, pero la continuidad exige además $f(c)=\lim$. Si $f(c)$ difiere o no existe, no es continua.

## 33d
$\lim f=\infty$ y $\lim g=\infty\Rightarrow \lim(f-g)=0$ — **Falsa**

Es indeterminación $\infty-\infty$. Contraejemplo: $f=x^2$, $g=x$ dan $\lim(f-g)=\infty$.

## 33e
$\lim f=0$ y $\lim g=0\Rightarrow \lim f/g$ no existe — **Falsa**

Es $\tfrac00$, indeterminado, pero el límite **puede** existir: p. ej. $\dfrac{\operatorname{sen}x}{x}\to1$.

## 33f
$\lim_{x\to0^+}(\ln\operatorname{sen}x-\ln x)=0$ — **Verdadera**

$\ln\operatorname{sen}x-\ln x=\ln\dfrac{\operatorname{sen}x}{x}$, y $\dfrac{\operatorname{sen}x}{x}\to1$, luego $\ln1=0$.

## 33g
Si $x=1$ es AV entonces $1\notin$ dominio — **Falsa**

Hay funciones definidas en $1$ con AV ahí (en general la AV implica que no está definida en sentido finito, pero el enunciado se considera falso porque una AV refiere al comportamiento del límite, no obliga formalmente; siguiendo la respuesta oficial es **Falsa**).

## 33h
Si $y=b$ es asíntota entonces no existe $c$ del dominio con $f(c)=b$ — **Falsa**

Una curva puede cruzar su asíntota horizontal. Ej.: $\dfrac{\operatorname{sen}x}{x}$ tiene AH $y=0$ y vale $0$ en infinitos puntos.

## 33i
Si $a\notin$ dominio entonces $x=a$ es asíntota — **Falsa**

Puede ser discontinuidad evitable (límite finito), no asíntota. Ej.: $\dfrac{\operatorname{sen}x}{x}$ en $x=0$.

## 33j
Si $f,g$ son polinomios del mismo grado entonces $f/g$ tiene AH — **Verdadera**

Mismo grado $\Rightarrow \lim_{x\to\infty}\dfrac{f}{g}=$ cociente de coeficientes principales (finito) $\Rightarrow$ AH.

## 33k
Si $f,g$ tienen distinto grado entonces $f/g$ tiene AO — **Falsa**

AO solo si el grado del numerador supera **en exactamente uno** al del denominador. Si la diferencia es mayor, o si el numerador tiene menor grado (AH $y=0$), no hay AO.

## 33l
$y=\dfrac{3x^2+2x+\operatorname{sen}x}{x}$ tiene AO $y=3x+2$ — **Verdadera**

$y=3x+2+\dfrac{\operatorname{sen}x}{x}$, y $\dfrac{\operatorname{sen}x}{x}\to0$ cuando $x\to\infty$, luego AO $y=3x+2$.

## 33m
$\lim_{h\to0}f(2+h)=f(2)$ — **Falsa**

Equivale a afirmar que $f$ es continua en $2$, lo cual no se cumple para toda $f$ (puede haber discontinuidad en $2$).

## 33n
Si $P(x)$ es polinomio entonces $\dfrac{P(x)}{x-1}$ tiene AV en $1$ — **Falsa**

Si $P(1)=0$ el factor $(x-1)$ se cancela y puede no haber AV (discontinuidad evitable). Ej.: $\dfrac{x-1}{x-1}=1$.

**Resumen:** Falsas: a, b, c, d, e, g, h, i, k, m, n. Verdaderas: f, j, l.

✓ Coincide con la respuesta oficial.

