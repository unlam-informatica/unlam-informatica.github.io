---
title: Ejercicio 1 — Graficar, indicar dominio e imagen
slug: analisis-matematico-i/unidad-1/practica/ejercicio-1
sidebar:
  order: 1
  label: Ejercicio 1
---


## 1a

:::note[Enunciado]
La función lineal que pasa por $P(-3,4)$ y $Q(2,-3)$.
:::

:::tip[Resolución]
La pendiente es



$$
m=\dfrac{y_Q-y_P}{x_Q-x_P}=\dfrac{-3-4}{2-(-3)}=\dfrac{-7}{5}=-\dfrac75
$$



Usando la forma punto-pendiente con $Q(2,-3)$:



$$
y-(-3)=-\dfrac75(x-2)\ \Rightarrow\ y=-\dfrac75 x+\dfrac{14}{5}-3=-\dfrac75 x-\dfrac15
$$



Una recta no constante tiene dominio e imagen $\mathbb{R}$.

**Resultado:** $m(x)=-\dfrac75 x-\dfrac15$, con $D=I=\mathbb{R}$. ✓ Coincide con la respuesta oficial.
:::

## 1b

:::note[Enunciado]
La función lineal que representa una recta paralela a $2x-3y+9=0$ y corta al eje $x$ en el punto de abscisa $x=-\dfrac12$.
:::

:::tip[Resolución]
Dos rectas son paralelas cuando tienen la misma pendiente. Empezamos escribiendo la recta dada en forma explícita para identificar su pendiente.

Partimos de:



$$
2x-3y+9=0
$$



Despejamos $y$:



$$
3y=2x+9
$$





$$
y=\dfrac23 x+3
$$



La pendiente de la recta dada es $\dfrac23$. Por lo tanto, la recta buscada tiene la misma pendiente:



$$
m=\dfrac23
$$



Como corta al eje $x$ en $x=-\dfrac12$, pasa por el punto $\left(-\dfrac12,0\right)$. Planteamos la forma explícita:



$$
f(x)=\dfrac23 x+b
$$



Imponemos $f\left(-\dfrac12\right)=0$:



$$
0=\dfrac23\left(-\dfrac12\right)+b
$$





$$
0=-\dfrac13+b
$$





$$
b=\dfrac13
$$



Entonces:



$$
f(x)=\dfrac23 x+\dfrac13
$$



Por tratarse de una función lineal no constante, su dominio e imagen son todos los reales.

**Resultado:** $f(x)=\dfrac23 x+\dfrac13$, con $D_f=\mathbb{R}$ e $I_f=\mathbb{R}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 1c

:::note[Enunciado]
La función cuadrática cuya representación gráfica es una parábola que tiene vértice en $V\left(-\dfrac12,5\right)$ y corta al eje de ordenadas en $(0,4)$.
:::

:::tip[Resolución]
Toda función cuadrática puede escribirse en forma canónica como



$$
f(x)=a(x-h)^2+k,
$$



donde $(h,k)$ es el vértice de la parábola y $a\neq 0$ determina la orientación y abertura.

Como el vértice es $V\left(-\dfrac12,5\right)$, entonces:



$$
h=-\dfrac12,\qquad k=5
$$



Por lo tanto:



$$
f(x)=a\left(x+\dfrac12\right)^2+5
$$



Como corta al eje de ordenadas en $(0,4)$, se cumple que $f(0)=4$:



$$
4=a\left(0+\dfrac12\right)^2+5
$$





$$
4=\dfrac{a}{4}+5
$$





$$
-1=\dfrac{a}{4}
$$





$$
a=-4
$$



Entonces:



$$
f(x)=-4\left(x+\dfrac12\right)^2+5
$$



Como $a<0$, la parábola abre hacia abajo, por lo que su valor máximo está en el vértice y la imagen es $(-\infty,5]$.

**Resultado:** $p(x)=-4\left(x+\dfrac12\right)^2+5$, con $D=\mathbb{R}$ e $I=(-\infty,5]$.
:::

## 1d

:::note[Enunciado]
La función cuadrática cuya representación gráfica es una parábola que tiene raíces $x_1=-1$, $x_2=\dfrac57$ y pasa por $P\left(1,\dfrac87\right)$.
:::

:::tip[Resolución]
Si una función cuadrática tiene raíces $x_1$ y $x_2$, puede escribirse en forma factorizada como



$$
f(x)=a(x-x_1)(x-x_2),
$$



donde $a\neq 0$ determina la orientación y abertura de la parábola.

Como las raíces son $x_1=-1$ y $x_2=\dfrac57$, resulta:



$$
f(x)=a(x+1)\left(x-\dfrac57\right)
$$



Además, la parábola pasa por $P\left(1,\dfrac87\right)$, por lo tanto:



$$
f(1)=\dfrac87
$$



Reemplazamos:



$$
\dfrac87=a(1+1)\left(1-\dfrac57\right)
$$





$$
\dfrac87=a\cdot 2\cdot \dfrac27
$$





$$
\dfrac87=\dfrac{4a}{7}
$$





$$
8=4a
$$





$$
a=2
$$



Entonces:



$$
f(x)=2(x+1)\left(x-\dfrac57\right)
$$



Como $a>0$, la parábola abre hacia arriba. Para hallar la imagen, usamos que el vértice está en el punto medio entre las raíces:



$$
x_v=\dfrac{x_1+x_2}{2}
$$



Reemplazamos:



$$
x_v=\dfrac{-1+\dfrac57}{2}=\dfrac{-\dfrac27}{2}=-\dfrac17
$$



Evaluamos la función en ese valor:



$$
f\left(-\dfrac17\right)=2\left(-\dfrac17+1\right)\left(-\dfrac17-\dfrac57\right)
$$





$$
f\left(-\dfrac17\right)=2\cdot\dfrac67\cdot\left(-\dfrac67\right)
$$





$$
f\left(-\dfrac17\right)=-\dfrac{72}{49}
$$



Como la parábola abre hacia arriba, ese valor es el mínimo.

**Resultado:** $h(x)=2(x+1)\left(x-\dfrac57\right)$, con $D=\mathbb{R}$ e $I=\left[-\dfrac{72}{49},+\infty\right)$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 1e

:::note[Enunciado]
$f:D_f\to I_f \,/\, f(x)=\lvert x\rvert$.
:::

:::tip[Resolución]
La función valor absoluto se define como



$$
\lvert x\rvert=\begin{cases} x & \text{si } x\geq 0, \\ -x & \text{si } x<0 \end{cases}
$$



Esta función está definida para todo número real, porque se puede calcular el valor absoluto de cualquier $x\in\mathbb{R}$.

Por lo tanto:



$$
D_f=\mathbb{R}
$$



Además, el valor absoluto nunca toma valores negativos:



$$
\lvert x\rvert\geq 0
$$



Su menor valor es $0$, que ocurre cuando $x=0$:



$$
f(0)=\lvert 0\rvert=0
$$



Por eso, su imagen es:



$$
I_f=[0,+\infty)
$$



Gráficamente, es una función con forma de “V”, con vértice en $(0,0)$.

**Resultado:** $D_f=\mathbb{R}$ e $I_f=[0,+\infty)$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 1f

:::note[Enunciado]
$g:D_g\to \mathbb{R} \,/\, g(x)=\sqrt{x}$.
:::

:::tip[Resolución]
La función raíz cuadrada real



$$
g(x)=\sqrt{x}
$$



sólo está definida cuando el radicando es mayor o igual que cero:



$$
x\geq 0
$$



Por lo tanto:



$$
D_g=[0,+\infty)
$$



Además, la raíz cuadrada principal nunca toma valores negativos:



$$
\sqrt{x}\geq 0
$$



Su menor valor es $0$, que ocurre cuando $x=0$:



$$
g(0)=\sqrt{0}=0
$$



Entonces:



$$
I_g=[0,+\infty)
$$



Gráficamente, comienza en $(0,0)$ y crece hacia la derecha.

**Resultado:** $D_g=[0,+\infty)$ e $I_g=[0,+\infty)$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 1g

:::note[Enunciado]
$h:D_h\to I_h \,/\, h(x)=\dfrac1x$.
:::

:::tip[Resolución]
La función racional



$$
h(x)=\dfrac1x
$$



está definida para todos los valores reales excepto aquellos que anulan el denominador.

En general, una fracción no está definida cuando su denominador vale cero. En este caso:



$$
x\neq 0
$$



Por lo tanto:



$$
D_h=\mathbb{R}-\lbrace 0\rbrace
$$



Para hallar la imagen, observamos que



$$
\dfrac1x
$$



nunca puede valer $0$, porque ninguna división de la forma $\dfrac1x$ da como resultado cero.

Entonces:



$$
I_h=\mathbb{R}-\lbrace 0\rbrace
$$



Gráficamente, es una hipérbola con asíntota vertical $x=0$ y asíntota horizontal $y=0$.

**Resultado:** $D_h=\mathbb{R}-\lbrace 0\rbrace $ e $I_h=\mathbb{R}-\lbrace 0\rbrace $.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

