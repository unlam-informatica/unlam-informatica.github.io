---
title: Ejercicio 10 — Dominio, imagen, intersecciones, positividad/negatividad
slug: analisis-matematico-i/unidad-1/practica/ejercicio-10
sidebar:
  order: 10
---


Determinar dominio, imagen, intersecciones con los ejes coordenados y los conjuntos de positividad y negatividad de las siguientes funciones. Graficar. Corroborar con GeoGebra.

## 10a

:::note[Enunciado]
$f(x)=x^2+2x-8$.
:::

:::tip[Resolución]
Es una función cuadrática con coeficiente principal $a=1>0$: parábola que abre hacia arriba.

**Dominio.** Por ser polinomio:



$$
D_f=\mathbb{R}
$$



**Raíces e intersecciones con los ejes.** Factorizamos:



$$
x^2+2x-8=(x+4)(x-2)
$$



Las raíces son $x=-4$ y $x=2$, por lo que la gráfica corta al eje $x$ en $(-4,0)$ y $(2,0)$. La intersección con el eje $y$ es $f(0)=-8$, punto $(0,-8)$.

**Vértice e imagen.** La abscisa del vértice es el punto medio entre las raíces:



$$
x_v=\dfrac{-4+2}{2}=-1
$$





$$
f(-1)=(-1)^2+2(-1)-8=1-2-8=-9
$$



Como la parábola abre hacia arriba, el vértice es mínimo absoluto:



$$
I_f=[-9,+\infty)
$$



**Conjuntos de positividad y negatividad.** Una parábola que abre hacia arriba es positiva fuera del intervalo entre sus raíces y negativa entre ellas:



$$
C^+=(-\infty,-4)\cup(2,+\infty),\qquad C^-=(-4,2)
$$



**Resultado:** $D_f=\mathbb{R}$, $I_f=[-9,+\infty)$, intersecciones $(0,-8)$, $(-4,0)$, $(2,0)$; $C^+=(-\infty,-4)\cup(2,+\infty)$, $C^-=(-4,2)$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 10b

:::note[Enunciado]
$f(x)=\lvert x-2\rvert$.
:::

:::tip[Resolución]
Es un valor absoluto: su gráfica tiene forma de "V" con vértice en $(2,0)$, donde el argumento $x-2$ se anula.

**Dominio.** $\lvert x-2\rvert$ está definido para todo real:



$$
D_f=\mathbb{R}
$$



**Imagen.** El valor absoluto nunca es negativo y vale $0$ en $x=2$:



$$
I_f=[0,+\infty)
$$



**Intersecciones con los ejes.** $f(0)=\lvert-2\rvert=2$ → $(0,2)$. $f(x)=0\iff x=2$ → $(2,0)$.

**Conjuntos de positividad y negatividad.** Como $\lvert x-2\rvert\geq 0$ siempre, y solo se anula en $x=2$:



$$
C^+=\mathbb{R}-\lbrace 2\rbrace ,\qquad C^-=\varnothing
$$



**Resultado:** $D_f=\mathbb{R}$, $I_f=[0,+\infty)$, intersecciones $(0,2)$ y $(2,0)$; $C^+=\mathbb{R}-\lbrace 2\rbrace $, $C^-=\varnothing$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 10c

:::note[Enunciado]
$f(x)=\dfrac{x}{x-2}$.
:::

:::tip[Resolución]
Es una función homográfica (cociente de polinomios de grado $1$).

**Dominio.** Denominador no nulo: $x-2\neq 0$, es decir:



$$
D_f=\mathbb{R}-\lbrace 2\rbrace
$$



**Asíntotas e imagen.** La asíntota vertical es $x=2$. La horizontal se obtiene del cociente de coeficientes principales:



$$
y_{AH}=\dfrac{1}{1}=1
$$



Como la función nunca toma el valor de la AH:



$$
I_f=\mathbb{R}-\lbrace 1\rbrace
$$



**Intersecciones con los ejes.** $f(x)=0\iff x=0$ → corta a ambos ejes en $(0,0)$.

**Conjuntos de positividad y negatividad.** Estudio de signos del cociente $\dfrac{x}{x-2}$ con raíz en $x=0$ y restricción en $x=2$:

- $x<0$: numerador $<0$, denominador $<0$ → cociente positivo.
- $0<x<2$: numerador $>0$, denominador $<0$ → cociente negativo.
- $x>2$: ambos positivos → cociente positivo.

Entonces:



$$
C^+=(-\infty,0)\cup(2,+\infty),\qquad C^-=(0,2)
$$



**Resultado:** $D_f=\mathbb{R}-\lbrace 2\rbrace $, $I_f=\mathbb{R}-\lbrace 1\rbrace $, intersección $(0,0)$; $C^+=(-\infty,0)\cup(2,+\infty)$, $C^-=(0,2)$. Asíntotas: $x=2$ (vertical) e $y=1$ (horizontal).

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 10d

:::note[Enunciado]
$g(x)=\dfrac{-2x+3}{x+4}$.
:::

:::tip[Resolución]
Función homográfica.

**Dominio.** $x+4\neq 0$:



$$
D_g=\mathbb{R}-\lbrace -4\rbrace
$$



**Asíntotas e imagen.** Asíntota vertical $x=-4$. La horizontal es el cociente de coeficientes principales:



$$
y_{AH}=\dfrac{-2}{1}=-2
$$



Imagen:



$$
I_g=\mathbb{R}-\lbrace -2\rbrace
$$



**Intersecciones con los ejes.** $g(x)=0\iff -2x+3=0\iff x=\dfrac32$ → $\left(\dfrac32,0\right)$. $g(0)=\dfrac{3}{4}$ → $\left(0,\dfrac34\right)$.

**Conjuntos de positividad y negatividad.** Numerador $-2x+3$ se anula en $x=\dfrac32$; denominador $x+4$ en $x=-4$.

- $x<-4$: numerador $>0$, denominador $<0$ → cociente negativo.
- $-4<x<\dfrac32$: numerador $>0$, denominador $>0$ → cociente positivo.
- $x>\dfrac32$: numerador $<0$, denominador $>0$ → cociente negativo.

Entonces:



$$
C^+=\left(-4,\dfrac32\right),\qquad C^-=(-\infty,-4)\cup\left(\dfrac32,+\infty\right)
$$



**Resultado:** $D_g=\mathbb{R}-\lbrace -4\rbrace $, $I_g=\mathbb{R}-\lbrace -2\rbrace $, intersecciones $\left(\dfrac32,0\right)$ y $\left(0,\dfrac34\right)$; $C^+=\left(-4,\dfrac32\right)$, $C^-=(-\infty,-4)\cup\left(\dfrac32,+\infty\right)$. Asíntotas: $x=-4$ (vertical) e $y=-2$ (horizontal).

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 10e

:::note[Enunciado]
$f(x)=\sqrt{x-2}$.
:::

:::tip[Resolución]
**Dominio.** Radicando no negativo:



$$
x-2\geq 0\iff x\geq 2
$$





$$
D_f=[2,+\infty)
$$



**Imagen.** La raíz cuadrada principal nunca es negativa, y toma todos los valores no negativos a partir de $0$:



$$
I_f=[0,+\infty)
$$



**Intersecciones con los ejes.** $f(2)=0$ → $(2,0)$. No corta el eje $y$ porque $0\notin D_f$.

**Conjuntos de positividad y negatividad.** $\sqrt{x-2}>0$ para todo $x>2$, y solo se anula en $x=2$:



$$
C^+=(2,+\infty),\qquad C^-=\varnothing
$$



**Resultado:** $D_f=[2,+\infty)$, $I_f=[0,+\infty)$, intersección $(2,0)$; $C^+=(2,+\infty)$, $C^-=\varnothing$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 10f

:::note[Enunciado]
$f(x)=\ln(x+1)$.
:::

:::tip[Resolución]
**Dominio.** El logaritmo natural exige argumento estrictamente positivo:



$$
x+1>0\iff x>-1
$$





$$
D_f=(-1,+\infty)
$$



**Imagen y asíntotas.** La función $\ln$ toma todos los reales, por lo que:



$$
I_f=\mathbb{R}
$$



Asíntota vertical en el borde del dominio: $x=-1$.

**Intersecciones con los ejes.** $f(x)=0\iff \ln(x+1)=0\iff x+1=1\iff x=0$ → $(0,0)$ (cruce con ambos ejes).

**Conjuntos de positividad y negatividad.** $\ln(x+1)>0\iff x+1>1\iff x>0$, y $\ln(x+1)<0\iff 0<x+1<1\iff -1<x<0$. Entonces:



$$
C^+=(0,+\infty),\qquad C^-=(-1,0)
$$



**Resultado:** $D_f=(-1,+\infty)$, $I_f=\mathbb{R}$, intersección $(0,0)$; $C^+=(0,+\infty)$, $C^-=(-1,0)$. Asíntota vertical $x=-1$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 10g

:::note[Enunciado]
$f(x)=2^{x+1}$.
:::

:::tip[Resolución]
**Dominio.** La exponencial está definida para todo real:



$$
D_f=\mathbb{R}
$$



**Imagen y asíntotas.** Toda exponencial con base positiva $\neq 1$ es estrictamente positiva:



$$
I_f=(0,+\infty)
$$



Asíntota horizontal $y=0$ por izquierda (cuando $x\to-\infty$, $2^{x+1}\to 0$).

**Intersecciones con los ejes.** No corta el eje $x$ porque la exponencial nunca se anula. Con el eje $y$: $f(0)=2^{0+1}=2$ → $(0,2)$.

**Conjuntos de positividad y negatividad.** Por la imagen:



$$
C^+=\mathbb{R},\qquad C^-=\varnothing
$$



**Resultado:** $D_f=\mathbb{R}$, $I_f=(0,+\infty)$, intersección $(0,2)$, no corta el eje $x$; $C^+=\mathbb{R}$, $C^-=\varnothing$. Asíntota horizontal $y=0$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

