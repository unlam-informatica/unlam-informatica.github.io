---
title: Unidad 4 — Polinomios de Taylor
description: Orden de contacto, polinomios de Taylor y de Mac Laurin, aproximación lineal y término complementario; ruta de estudio con lecciones y prácticas.
slug: analisis-matematico-i/unidad-4
sidebar:
  label: Presentación y ruta
---

Un polinomio de Taylor es el polinomio que mejor imita a una función cerca de un punto: tiene el mismo valor y las
mismas derivadas hasta cierto orden. Sirve para aproximar valores, simplificar ecuaciones y estimar el error que
se comete. La recta tangente de la Unidad 3 es el caso más simple. Se evalúa en el **segundo parcial**.

## Objetivos de aprendizaje

Al terminar la unidad deberías poder:

- determinar el orden de contacto entre dos curvas en un punto y escribir un polinomio en potencias de $(x - a)$ a partir de sus derivadas;
- construir polinomios de Taylor y de Mac Laurin, usarlos para aproximar valores y resolver ecuaciones, y hallar parámetros a partir de un polinomio dado;
- relacionar la aproximación lineal con la recta tangente;
- escribir el término complementario en la forma de Lagrange, acotar el error y elegir el orden necesario para una precisión dada.

## Antes de comenzar

- **Conviene repasar:** [derivadas sucesivas, reglas y regla de la cadena](/analisis-matematico-i/unidad-3/), la [recta tangente](/analisis-matematico-i/unidad-3/teoria/razon-de-cambio-y-derivada/) y los [infinitésimos](/analisis-matematico-i/unidad-2/teoria/infinitesimos/).
- **Herramientas:** [GeoGebra para el polinomio de Taylor](/analisis-matematico-i/geogebra/taylor/), para comparar una función con polinomios de distinto orden.

## Ruta de aprendizaje

### 1. Orden de contacto y polinomio por sus derivadas

- **Leé:** [Orden de contacto](/analisis-matematico-i/unidad-4/teoria/orden-de-contacto/) (U4.01 a U4.04).
- **Practicá con la guía:** ejercicio 1 de la [Práctica 4](/analisis-matematico-i/unidad-4/practica/practica-4/).
- **Comprobá:** [autoevaluación](/analisis-matematico-i/unidad-4/teoria/orden-de-contacto/#autoevaluación).

### 2. Polinomio de Taylor y de Mac Laurin

Construcción del polinomio, desarrollos de las funciones elementales, aproximación de valores, ecuaciones y aproximación lineal.

- **Leé:** [Polinomio de Taylor y de Mac Laurin](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/) (U4.05 a U4.09).
- **Practicá con la guía:** ejercicios 2 a 8 y 11 a 14 de la [Práctica 4](/analisis-matematico-i/unidad-4/practica/practica-4/).
- **Comprobá:** [autoevaluación](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/#autoevaluación).

### 3. Término complementario

- **Leé:** [Término complementario](/analisis-matematico-i/unidad-4/teoria/termino-complementario/) (U4.10 a U4.13).
- **Practicá con la guía:** ejercicios 9 y 10 de la [Práctica 4](/analisis-matematico-i/unidad-4/practica/practica-4/).
- **Comprobá:** [autoevaluación](/analisis-matematico-i/unidad-4/teoria/termino-complementario/#autoevaluación).

### 4. Integración

- **Resolvé:** los [integradores de la unidad](/analisis-matematico-i/unidad-4/practica/integradores/) (U4.14 a U4.17), el verdadero o falso (ejercicio 15) y los adicionales de la [Práctica 4](/analisis-matematico-i/unidad-4/practica/practica-4/).

## Temas de la unidad

| Tema | Descripción |
|------|-------------|
| Órdenes de contacto | $f^{(k)}(a) = g^{(k)}(a)$ para $k = 0,\ldots,n$ pero no para $k = n+1$ |
| Expresión por derivadas | Relación entre los coeficientes del polinomio y $f^{(k)}(a)$ |
| Polinomio de Taylor | $P_n(x) = \sum_{k=0}^{n} \dfrac{f^{(k)}(a)}{k!}(x-a)^k$ centrado en $x = a$ |
| Polinomio de Mac Laurin | Caso particular con $a = 0$ |
| Aproximación lineal | $P_1(x) = f(a) + f'(a)(x-a)$ — la recta tangente |
| Resto de Lagrange | $R_n(x) = \dfrac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ para algún $c$ entre $a$ y $x$ |

## Autoevaluación y repaso

- Cada lección termina con una autoevaluación con respuestas plegadas.
- El [resumen integrador](/analisis-matematico-i/unidad-4/teoria/unidad-4/) reúne la unidad en una página, con los desarrollos de Mac Laurin más usados.

## Continuar

Con esta unidad se completa el temario de la materia y del segundo parcial. Para el repaso integrador y el final,
seguí [Repasar para un examen](/analisis-matematico-i/como-estudiar/#repasar-para-un-examen).

:::note[Sobre las prácticas]
La resolución de la Práctica 4 corresponde a los enunciados de la Guía de Trabajos Prácticos 2026 de la cátedra
(DIIT-UNLaM). Los ejercicios de las lecciones y los integradores (U4.01 a U4.17) son originales de estos apuntes.
:::
