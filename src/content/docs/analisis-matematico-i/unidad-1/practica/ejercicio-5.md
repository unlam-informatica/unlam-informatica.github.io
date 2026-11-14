---
title: Ejercicio 5* — Canaleta de desagüe
slug: analisis-matematico-i/unidad-1/practica/ejercicio-5
sidebar:
  order: 5
  label: Ejercicio 5
---


Se desea construir una canaleta de desagüe a partir de una hoja rectangular de metal de $12$ cm de ancho y $1$ metro de largo. Se dobla la hoja hacia arriba $x$ cm en los dos bordes de $1$ metro de largo.

## 5a

:::note[Enunciado]
Expresar el área de la sección transversal de la canaleta como una función de $x$.
:::

:::tip[Resolución]
La **sección transversal** es la figura plana que se obtiene al cortar la canaleta perpendicularmente a su largo. Como los dos bordes se doblaron hacia arriba $x$ cm, ese corte tiene forma de "U": un fondo horizontal y dos paredes verticales. El área de la sección transversal es el área que ocupa el agua cuando la canaleta está llena hasta el borde, es decir, la del rectángulo encerrado entre el fondo y las paredes.

Las dimensiones de ese rectángulo son:

- Base: $12-2x$ cm (lo que queda del ancho original después de descontar los dos pliegues).
- Altura: $x$ cm (cuánto se levantaron las paredes al doblarlas).

El área es base por altura:



$$
A(x)=(12-2x)\cdot x
$$



Distribuyendo:



$$
A(x)=12x-2x^2
$$



Se puede también factorizar como:



$$
A(x)=2x\,(6-x)
$$



**Resultado:** $A(x)=12x-2x^2=2x(6-x)$, expresada en cm².

**Verificación:** El [documento de respuestas oficiales](https://drive.google.com/file/d/1nJsGgi-k5Zgey-RVAF49SmP-BSGfFFGe/view) publica como respuesta del ejercicio la fórmula del **volumen** $V(x)=200x(6-x)$ (en cm³, ya incluyendo el largo de $100$ cm), mientras que aquí respondemos lo que el enunciado pide literalmente: el **área** de la sección transversal. Ambas expresiones son consistentes entre sí, ya que $V(x)=100\cdot A(x)=100\cdot 2x(6-x)=200x(6-x)$, y se usa más abajo en `5d`.
:::

:::note[Enunciado]
¿Cuál es el dominio de esta función de acuerdo al contexto?
:::

:::tip[Resolución]
Para que la canaleta exista físicamente, deben cumplirse simultáneamente dos condiciones de contexto.

**Condición 1.** El pliegue debe tener altura positiva (si no se dobla, no hay canaleta):



$$
x>0
$$



**Condición 2.** El fondo debe tener ancho positivo (si se doblara más de la mitad por cada lado, no quedaría base):



$$
12-2x>0
$$





$$
2x<12
$$





$$
x<6
$$



La intersección de ambas condiciones es:



$$
0<x<6
$$



**Resultado:** $D_A=(0,6)$, con $x$ medido en cm.

**Verificación:** Coincide con la respuesta indicada en el [documento de respuestas oficiales](https://drive.google.com/file/d/1nJsGgi-k5Zgey-RVAF49SmP-BSGfFFGe/view). El dominio es el mismo para la función área $A(x)$ usada acá y para la función volumen $V(x)=100\cdot A(x)$ con la que trabaja el solucionario, ya que ambas se anulan en los mismos extremos.
:::

## 5c

:::note[Enunciado]
Graficar la función y estimar para qué valor de $x$ el área de la sección transversal de la canaleta es máxima.
:::

:::tip[Resolución]
La función $A(x)=-2x^2+12x$ es cuadrática con coeficiente principal $a=-2<0$, por lo que su gráfica es una parábola que abre hacia abajo. Esto garantiza que el vértice corresponde a un **máximo absoluto**.

Buscamos la abscisa del vértice. Como $A$ está factorizada como $A(x)=2x(6-x)$, sus raíces son $x_1=0$ y $x_2=6$. El vértice está en el punto medio entre ambas:



$$
x_v=\dfrac{x_1+x_2}{2}=\dfrac{0+6}{2}=3
$$



Evaluamos $A$ en $x_v=3$ para obtener el valor máximo:



$$
A(3)=2\cdot 3\cdot(6-3)
$$





$$
A(3)=2\cdot 3\cdot 3
$$





$$
A(3)=18
$$



En el gráfico, la parábola corta al eje $x$ en $x=0$ y $x=6$, sube hasta el vértice $(3,18)$ y luego baja simétricamente.

**Resultado:** el área de la sección transversal es máxima cuando $x=3$ cm, y vale $A_{\max}=18$ cm².

**Verificación:** El valor $x=3$ cm donde se alcanza el máximo coincide con el indicado en el [documento de respuestas oficiales](https://drive.google.com/file/d/1nJsGgi-k5Zgey-RVAF49SmP-BSGfFFGe/view) ("se obtiene mayor volumen cuando se cortan $3$ cm de cada lado"). Como $V(x)=100\cdot A(x)$, los máximos de área y volumen ocurren en el mismo $x$. El valor $A_{\max}=18$ cm² no figura explícito en el solucionario (que reporta el máximo del volumen), pero es consistente con él: $V_{\max}=100\cdot 18=1800$ cm³ $=200\cdot 3\cdot(6-3)$.
:::

## 5d

:::note[Enunciado]
¿Cuántos cm se deben doblar para que la canaleta tenga la capacidad máxima de transporte de agua?
:::

:::tip[Resolución]
La capacidad de transporte de agua de la canaleta es el **volumen** que puede contener. Como la canaleta tiene sección transversal constante a lo largo de toda su longitud, el volumen es el producto del área de la sección por el largo:



$$
V(x)=A(x)\cdot L
$$



El largo es $L=1$ m $=100$ cm, por lo que:



$$
V(x)=100\cdot A(x)=100\cdot(12x-2x^2)=200x(6-x)
$$



Como $100$ es una constante positiva, $V(x)$ alcanza su máximo en el mismo valor de $x$ que $A(x)$. De `5c` ya sabemos que el área es máxima en $x=3$, por lo que también lo es el volumen.

El volumen máximo es:



$$
V(3)=100\cdot 18=1800
$$



**Resultado:** se deben doblar $x=3$ cm en cada borde para que la canaleta tenga capacidad máxima, que vale $1800$ cm³.

**Verificación:** Coincide con el [documento de respuestas oficiales](https://drive.google.com/file/d/1nJsGgi-k5Zgey-RVAF49SmP-BSGfFFGe/view): "se obtiene mayor volumen cuando se cortan $3$ cm de cada lado", a partir de la fórmula $V(x)=200x(6-x)$ que coincide con la $V(x)=100\cdot A(x)$ deducida aquí. Evaluando la oficial en $x=3$ se obtiene $V(3)=200\cdot 3\cdot(6-3)=1800$ cm³, igual al valor calculado.
:::

