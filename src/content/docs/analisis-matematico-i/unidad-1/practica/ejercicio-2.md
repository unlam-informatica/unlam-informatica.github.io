---
title: Ejercicio 2 — Celsius y Fahrenheit
slug: analisis-matematico-i/unidad-1/practica/ejercicio-2
sidebar:
  order: 2
  label: Ejercicio 2
---


Obtener la ecuación de la recta que relaciona la temperatura $C$ en grados Celsius con la temperatura $F$ en grados Fahrenheit, sabiendo que el agua se hiela a $0^\circ C\,(32^\circ F)$ y hierve a $100^\circ C\,(212^\circ F)$.

## 2a

:::note[Enunciado]
Hallar la función (terna) que modela la situación planteada.
:::

:::tip[Resolución]
La relación entre $C$ y $F$ es lineal, por lo que puede escribirse como



$$
F(C)=mC+b
$$



Los datos del enunciado nos dan dos puntos en el plano $(C,F)$:



$$
(0,32)\quad\text{y}\quad(100,212)
$$



Calculamos la pendiente como el cociente de variaciones:



$$
m=\dfrac{F_2-F_1}{C_2-C_1}
$$



Reemplazamos:



$$
m=\dfrac{212-32}{100-0}=\dfrac{180}{100}=\dfrac95
$$



Para la ordenada al origen, usamos el primer punto $(0,32)$:



$$
32=\dfrac95\cdot 0+b
$$





$$
b=32
$$



Entonces:



$$
F(C)=\dfrac95 C+32
$$



La temperatura en Celsius puede tomar cualquier valor real, y la imagen también recorre todos los reales, por lo que la terna es:



$$
F:\mathbb{R}\to\mathbb{R}\,/\,F(C)=\dfrac95 C+32
$$



**Resultado:** $F:\mathbb{R}\to\mathbb{R}\,/\,F(C)=\dfrac95 C+32$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 2b

:::note[Enunciado]
¿Cuántos grados Fahrenheit son $-10^\circ C$?
:::

:::tip[Resolución]
Para convertir una temperatura de Celsius a Fahrenheit, evaluamos la función hallada en `2a`:



$$
F(C)=\dfrac95 C+32
$$



Reemplazamos $C=-10$:



$$
F(-10)=\dfrac95\cdot(-10)+32
$$





$$
F(-10)=-\dfrac{90}{5}+32
$$





$$
F(-10)=-18+32
$$





$$
F(-10)=14
$$



**Resultado:** $-10^\circ C$ equivalen a $14^\circ F$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 2c

:::note[Enunciado]
¿Cuántos grados Celsius se corresponden con $0^\circ F$?
:::

:::tip[Resolución]
Ahora queremos despejar $C$ en función de $F$. Partimos de:



$$
F=\dfrac95 C+32
$$



Restamos $32$ a ambos miembros:



$$
F-32=\dfrac95 C
$$



Multiplicamos ambos miembros por $\dfrac59$:



$$
C=\dfrac59(F-32)
$$



Reemplazamos $F=0$:



$$
C=\dfrac59(0-32)
$$





$$
C=\dfrac59\cdot(-32)
$$





$$
C=-\dfrac{160}{9}
$$



En forma decimal aproximada:



$$
C\approx-17{,}78
$$



**Resultado:** $0^\circ F$ equivalen a $-\dfrac{160}{9}^\circ C\approx-17{,}78^\circ C$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 2d

:::note[Enunciado]
Calcular el cambio de temperatura $\Delta F$ en los intervalos $[0,10]$, $[10,20]$ (en grados Celsius). Interpretar gráficamente.
:::

:::tip[Resolución]
En una función lineal $F(C)=mC+b$, el cambio en $F$ entre dos valores $C_1$ y $C_2$ es:



$$
\Delta F=F(C_2)-F(C_1)=m\,(C_2-C_1)=m\,\Delta C
$$



Es decir, $\Delta F$ depende solo de la pendiente y de la longitud del intervalo, no de dónde está ubicado.

**Intervalo $[0,10]$:** acá $\Delta C=10-0=10$, entonces



$$
\Delta F=\dfrac95\cdot 10=18
$$



**Intervalo $[10,20]$:** acá también $\Delta C=20-10=10$, entonces



$$
\Delta F=\dfrac95\cdot 10=18
$$



En ambos casos se obtiene el mismo cambio porque la pendiente $m=\dfrac95$ es constante: la razón de cambio de una función lineal es la misma en todo el dominio. Gráficamente, a incrementos iguales en el eje $C$ les corresponden incrementos iguales en el eje $F$, y la pendiente representa la inclinación de la recta (por cada $1^\circ C$ que sube la temperatura Celsius, la Fahrenheit sube $\dfrac95^\circ F$).

**Resultado:** $\Delta F=18^\circ F$ en ambos intervalos.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

