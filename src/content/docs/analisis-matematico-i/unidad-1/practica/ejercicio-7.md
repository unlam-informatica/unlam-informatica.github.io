---
title: Ejercicio 7 — Fórmula y dominio
slug: analisis-matematico-i/unidad-1/practica/ejercicio-7
sidebar:
  order: 7
---


Encontrar una fórmula para la función descrita y dar su dominio.

## 7a

:::note[Enunciado]
El área de un rectángulo cuyo perímetro es $20$ m en función de uno de sus lados.
:::

:::tip[Resolución]
Llamamos $x$ a uno de los lados del rectángulo (medido en m) e $y$ al lado contiguo. El perímetro es la suma de los cuatro lados, por lo que:



$$
2x+2y=20
$$



Despejamos $y$ en función de $x$:



$$
2y=20-2x
$$





$$
y=10-x
$$



El área del rectángulo es el producto de los lados:



$$
A(x)=x\,(10-x)
$$





$$
A(x)=10x-x^2
$$



Para que el rectángulo exista físicamente, ambos lados deben ser positivos:



$$
x>0,\qquad 10-x>0
$$



La segunda condición da $x<10$. Combinando:



$$
0<x<10
$$



**Resultado:** $A:(0,10)\to\mathbb{R}\,/\,A(x)=x(10-x)$, con $D_A=(0,10)$ y $x$ medido en m.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 7b

:::note[Enunciado]
El perímetro de un rectángulo cuya área es $16\text{ m}^2$ en función de uno de sus lados.
:::

:::tip[Resolución]
Llamamos $x$ a uno de los lados (medido en m) e $y$ al lado contiguo. El área del rectángulo es:



$$
x\cdot y=16
$$



Despejamos $y$ en función de $x$ (con $x\neq 0$):



$$
y=\dfrac{16}{x}
$$



El perímetro es la suma de los cuatro lados:



$$
P(x)=2x+2y
$$





$$
P(x)=2x+2\cdot\dfrac{16}{x}
$$





$$
P(x)=2x+\dfrac{32}{x}
$$



Para que el rectángulo exista físicamente, ambos lados deben ser positivos. Como $y=16/x$, basta con pedir $x>0$ (eso garantiza también $y>0$):



$$
x>0
$$



**Resultado:** $P:(0,+\infty)\to\mathbb{R}\,/\,P(x)=2x+\dfrac{32}{x}$, con $D_P=(0,+\infty)$ y $x$ medido en m.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 7c

:::note[Enunciado]
El área de un triángulo equilátero en función de la longitud de su lado.
:::

:::tip[Resolución]
Llamamos $l$ a la longitud del lado del triángulo equilátero. Para calcular el área necesitamos también la altura.

La altura $h$ se obtiene aplicando el teorema de Pitágoras a uno de los dos triángulos rectángulos en que la altura divide al triángulo equilátero. En ese triángulo rectángulo:

- La hipotenusa es el lado $l$.
- Un cateto es la mitad de la base, $\dfrac{l}{2}$.
- El otro cateto es la altura $h$.

Por Pitágoras:



$$
l^2=h^2+\left(\dfrac{l}{2}\right)^2
$$





$$
h^2=l^2-\dfrac{l^2}{4}=\dfrac{3l^2}{4}
$$





$$
h=\dfrac{\sqrt 3}{2}\,l
$$



El área es base por altura sobre dos:



$$
A(l)=\dfrac{l\cdot h}{2}=\dfrac{l}{2}\cdot\dfrac{\sqrt 3}{2}\,l
$$





$$
A(l)=\dfrac{\sqrt 3}{4}\,l^2
$$



Para que el triángulo exista físicamente, el lado debe ser positivo:



$$
l>0
$$



**Resultado:** $A:(0,+\infty)\to\mathbb{R}\,/\,A(l)=\dfrac{\sqrt 3}{4}\,l^2$, con $D_A=(0,+\infty)$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

