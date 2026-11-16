---
title: Sistemas lineales
description: Forma matricial, eliminación gaussiana, forma escalonada reducida, teorema de Rouché-Frobenius, sistemas homogéneos, parámetros, matriz ampliada múltiple y sistemas en ℤ₂.
slug: algebra-ii/repaso/sistemas-lineales
sidebar:
  order: 3
  label: R.3 Sistemas lineales
---

## Para qué sirve

Resolver sistemas lineales es la herramienta de cálculo de toda la materia. Decidir si un vector pertenece a un subespacio generado, si un conjunto es linealmente independiente, hallar coordenadas, el núcleo de una transformación lineal, los autovectores de un autovalor o la solución de cuadrados mínimos: cada una de esas preguntas se traduce en un sistema $Ax=b$ o $Ax=0$ que se resuelve por eliminación gaussiana. Esta lección repasa el método, la clasificación de los sistemas por el rango y tres situaciones que en Álgebra II aparecen todo el tiempo: sistemas homogéneos, sistemas con parámetros y varios sistemas con la misma matriz. Al final resolvemos un sistema sobre $\mathbb{Z}_2$.

## Forma matricial y matriz ampliada

Un sistema de $m$ ecuaciones lineales con $n$ incógnitas

$$
\begin{cases}a_{11}x_1+a_{12}x_2+\dots+a_{1n}x_n=b_1\\ \quad\vdots\\ a_{m1}x_1+a_{m2}x_2+\dots+a_{mn}x_n=b_m\end{cases}
$$

se escribe $Ax=b$, con $A=(a_{ij})\in\mathbb{R}^{m\times n}$ la **matriz de coeficientes**, $x=(x_1,\dots,x_n)$ y $b=(b_1,\dots,b_m)$ como columnas. Toda la información está en la **matriz ampliada** $(A\mid b)\in\mathbb{R}^{m\times(n+1)}$. Una **solución** es un $x\in\mathbb{R}^n$ que verifica las $m$ ecuaciones. Si $b=0$ el sistema es **homogéneo**.

Por la lectura del producto de [R.1](/algebra-ii/repaso/vectores-y-matrices/), $Ax=x_1c_1+\dots+x_nc_n$ donde $c_j$ son las columnas de $A$. Resolver $Ax=b$ es, entonces, buscar los coeficientes con los que $b$ se escribe como combinación lineal de las columnas de $A$.

## Operaciones elementales y forma escalonada

Las **operaciones elementales de fila** son:

1. intercambiar dos filas, $F_i\leftrightarrow F_j$;
2. multiplicar una fila por un escalar no nulo, $cF_i\to F_i$ con $c\neq0$;
3. sumar a una fila un múltiplo de otra, $F_i+cF_j\to F_i$ con $i\neq j$.

Cada operación se puede deshacer con otra del mismo tipo, así que **no cambia el conjunto de soluciones**. Dos matrices son **equivalentes por filas** ($A\sim B$) si una se obtiene de la otra con una sucesión de operaciones elementales.

:::note[Definición]
Una matriz está en **forma escalonada** si las filas nulas (si las hay) están abajo y el primer elemento no nulo de cada fila no nula (su **pivote**) está a la derecha del pivote de la fila anterior. Está en **forma escalonada reducida** si además cada pivote es $1$ y es el único elemento no nulo de su columna.

El **rango** de $A$, $\operatorname{rango}(A)$, es la cantidad de filas no nulas de cualquier forma escalonada de $A$ (no depende de la forma escalonada elegida).
:::

Toda matriz es equivalente por filas a una forma escalonada (**eliminación gaussiana**: se hacen ceros debajo de cada pivote, de izquierda a derecha) y a una **única** forma escalonada reducida (**Gauss-Jordan**: además se normalizan los pivotes y se hacen ceros encima de ellos).

En el sistema escalonado, las incógnitas que corresponden a columnas con pivote son **variables principales**; las demás son **variables libres** y pueden tomar cualquier valor. Despejando las principales en función de las libres se obtiene la **solución general**.

### Ejemplo 1 · Eliminación gaussiana con variables libres
<!-- check: R.T03.E1 -->

Resolvemos

$$
\begin{cases}x_1+2x_2-x_3+x_4=3\\ 2x_1+4x_2-x_3+3x_4=7\\ -x_1-2x_2+2x_3=-2\end{cases}
$$

Con $F_2-2F_1\to F_2$ y $F_3+F_1\to F_3$, y luego $F_3-F_2\to F_3$:

$$
\left(\begin{array}{cccc|c}1&2&-1&1&3\\2&4&-1&3&7\\-1&-2&2&0&-2\end{array}\right)\sim\left(\begin{array}{cccc|c}1&2&-1&1&3\\0&0&1&1&1\\0&0&1&1&1\end{array}\right)\sim\left(\begin{array}{cccc|c}1&2&-1&1&3\\0&0&1&1&1\\0&0&0&0&0\end{array}\right).
$$

Para la forma reducida, $F_1+F_2\to F_1$:

$$
\left(\begin{array}{cccc|c}1&2&0&2&4\\0&0&1&1&1\\0&0&0&0&0\end{array}\right).
$$

Los pivotes están en las columnas 1 y 3: $x_1$ y $x_3$ son principales; $x_2$ y $x_4$ son libres. Despejando, $x_1=4-2x_2-2x_4$ y $x_3=1-x_4$. La solución general, escrita como vector,

$$
x=\begin{pmatrix}4-2x_2-2x_4\\x_2\\1-x_4\\x_4\end{pmatrix}=\begin{pmatrix}4\\0\\1\\0\end{pmatrix}+x_2\begin{pmatrix}-2\\1\\0\\0\end{pmatrix}+x_4\begin{pmatrix}-2\\0\\-1\\1\end{pmatrix},\qquad x_2,x_4\in\mathbb{R}.
$$

El sistema tiene infinitas soluciones: $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)=2<4$.

**Comprobación.** $x=(4,0,1,0)$ (con $x_2=x_4=0$) cumple $4+0-1+0=3$, $8+0-1+0=7$ y $-4-0+2+0=-2$. El vector $(-2,1,0,0)$ cumple las ecuaciones con lado derecho nulo: $-2+2=0$, $-4+4=0$, $2-2=0$; lo mismo $(-2,0,-1,1)$: $-2+1+1=0$, $-4+1+3=0$, $2-2+0=0$.

## Clasificación: el teorema de Rouché-Frobenius

Un sistema es **compatible** si tiene al menos una solución e **incompatible** si no tiene ninguna. Un sistema compatible es **determinado** si la solución es única e **indeterminado** si tiene infinitas (sobre $\mathbb{R}$ no hay término medio).

:::note[Teorema de Rouché-Frobenius]
Sea $Ax=b$ con $A\in\mathbb{R}^{m\times n}$.

1. El sistema es compatible si y solo si $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)$.
2. Si es compatible y $\operatorname{rango}(A)=n$, es compatible determinado.
3. Si es compatible y $\operatorname{rango}(A)<n$, es compatible indeterminado, con $n-\operatorname{rango}(A)$ variables libres.
:::

**Demostración.** Escalonamos $(A\mid b)$. Si $\operatorname{rango}(A\mid b)>\operatorname{rango}(A)$, alguna fila queda de la forma $(0\ \cdots\ 0\mid c)$ con $c\neq0$, es decir la ecuación $0=c$, y no hay solución. Si los rangos coinciden, no aparece esa fila y la sustitución hacia atrás produce soluciones: hay tantas variables principales como pivotes, $\operatorname{rango}(A)$, y las $n-\operatorname{rango}(A)$ restantes son libres. Si no hay variables libres la solución es única; si hay al menos una, cada valor de ella da una solución distinta. $\blacksquare$

| Situación | Rangos | Soluciones |
|---|---|---|
| Compatible determinado (SCD) | $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)=n$ | una |
| Compatible indeterminado (SCI) | $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)<n$ | infinitas, con $n-\operatorname{rango}(A)$ parámetros |
| Incompatible (SI) | $\operatorname{rango}(A)<\operatorname{rango}(A\mid b)$ | ninguna |

Si $A$ es cuadrada ($m=n$), el sistema es compatible determinado para todo $b$ si y solo si $\det A\neq0$ (ver [R.2](/algebra-ii/repaso/determinantes/)); en ese caso $x=A^{-1}b$.

## Sistemas homogéneos

Un sistema homogéneo $Ax=0$ **siempre es compatible**: $x=0$ es solución (la **solución trivial**). Por Rouché-Frobenius, tiene soluciones no triviales si y solo si $\operatorname{rango}(A)<n$; en particular, siempre que haya más incógnitas que ecuaciones.

Las soluciones de $Ax=0$ son cerradas por suma y por producto por escalar: si $Ax=0$ y $Ay=0$, entonces $A(x+y)=0$ y $A(cx)=0$. La solución general se escribe como **combinación lineal** de vectores fijos, uno por cada variable libre. En el Ejemplo 1, el sistema homogéneo asociado tiene la misma forma escalonada con columna de términos independientes nula, y su solución general es

$$
x_2\,(-2,1,0,0)+x_4\,(-2,0,-1,1),\qquad x_2,x_4\in\mathbb{R}.
$$

:::note[Propiedad]
Si $x_p$ es una solución particular de $Ax=b$, entonces las soluciones de $Ax=b$ son exactamente los vectores $x_p+x_h$ con $x_h$ solución del homogéneo $Ax=0$.
:::

**Demostración.** Si $Ax_h=0$, $A(x_p+x_h)=b+0=b$. Recíprocamente, si $Ax=b$, entonces $A(x-x_p)=b-b=0$, así que $x_h=x-x_p$ resuelve el homogéneo y $x=x_p+x_h$. $\blacksquare$

En el Ejemplo 1 se ve la estructura: $(4,0,1,0)$ es una solución particular y lo que se le suma es la solución general del homogéneo. En la Unidad 1 el conjunto de soluciones de $Ax=0$ recibe un nombre, $\operatorname{nul}(A)$, y la cantidad de variables libres es su dimensión.

## Sistemas con parámetros

Si los coeficientes o los términos independientes dependen de parámetros, se escalona igual, con dos cuidados: **no dividir** por expresiones que puedan anularse y, al final, **separar casos** según se anulen o no los elementos que dependen del parámetro. Si la matriz de coeficientes es cuadrada, conviene calcular primero $\det A$: los valores que lo anulan son los únicos que hay que estudiar aparte.

### Ejemplo 2 · Clasificación según dos parámetros
<!-- check: R.T03.E2 -->

Clasificamos, según $a,b\in\mathbb{R}$, el sistema

$$
\begin{cases}x+y+z=1\\ x+2y+3z=2\\ x+3y+az=b\end{cases}
$$

Con $F_2-F_1\to F_2$ y $F_3-F_1\to F_3$, y luego $F_3-2F_2\to F_3$:

$$
\left(\begin{array}{ccc|c}1&1&1&1\\1&2&3&2\\1&3&a&b\end{array}\right)\sim\left(\begin{array}{ccc|c}1&1&1&1\\0&1&2&1\\0&2&a-1&b-1\end{array}\right)\sim\left(\begin{array}{ccc|c}1&1&1&1\\0&1&2&1\\0&0&a-5&b-3\end{array}\right).
$$

Todo depende del elemento $a-5$ y, si se anula, del término $b-3$:

- **$a\neq5$:** hay tres pivotes, $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)=3$: compatible determinado. Resolviendo hacia atrás, $z=\frac{b-3}{a-5}$, $y=1-2z$ y $x=1-y-z=z$.
- **$a=5$ y $b=3$:** la tercera fila es nula, $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)=2<3$: compatible indeterminado, con solución $(x,y,z)=(0,1,0)+z\,(1,-2,1)$, $z\in\mathbb{R}$.
- **$a=5$ y $b\neq3$:** la tercera fila es $(0\ 0\ 0\mid b-3)$ con $b-3\neq0$; $\operatorname{rango}(A)=2<3=\operatorname{rango}(A\mid b)$: incompatible.

**Comprobación.** $\det A=a-5$ (el producto de la diagonal de la forma escalonada, sin intercambios), de acuerdo con que el caso especial sea $a=5$. Con $a\neq5$, la tercera ecuación da $z+3(1-2z)+az=3+(a-5)z=3+(b-3)=b$.

## Varios sistemas con la misma matriz

Si hay que resolver $Ax=b_1$, $Ax=b_2$, …, $Ax=b_k$ con la **misma** matriz $A$, las operaciones de fila que escalonan $A$ son las mismas para todos. Se arma una **matriz ampliada múltiple** $(A\mid b_1\ b_2\ \cdots\ b_k)$ y se escalona una sola vez; cada columna de la derecha da la solución de su sistema. El cálculo de la inversa por Gauss-Jordan es el caso particular en que los $b_j$ son las columnas de $I$. En la Unidad 1 este recurso se usa para calcular de una vez las coordenadas de varios vectores respecto de una base, que son las columnas de una matriz de cambio de coordenadas.

### Ejemplo 3 · Dos sistemas a la vez
<!-- check: R.T03.E3 -->

Escribimos $b_1=(3,5)$ y $b_2=(2,-1)$ como combinación lineal de $(1,1)$ y $(1,2)$. Hay que resolver $Ax=b_1$ y $Ax=b_2$ con $A=\begin{pmatrix}1&1\\1&2\end{pmatrix}$ (los dos vectores como columnas):

$$
\left(\begin{array}{cc|cc}1&1&3&2\\1&2&5&-1\end{array}\right)\xrightarrow{F_2-F_1\to F_2}\left(\begin{array}{cc|cc}1&1&3&2\\0&1&2&-3\end{array}\right)\xrightarrow{F_1-F_2\to F_1}\left(\begin{array}{cc|cc}1&0&1&5\\0&1&2&-3\end{array}\right).
$$

La tercera columna da la solución del primer sistema, $x=(1,2)$, y la cuarta, la del segundo, $x=(5,-3)$:

$$
(3,5)=1\,(1,1)+2\,(1,2),\qquad (2,-1)=5\,(1,1)-3\,(1,2).
$$

**Comprobación.** $(1,1)+(2,4)=(3,5)$ y $(5,5)+(-3,-6)=(2,-1)$.

## Sistemas sobre ℤ₂

En Álgebra II también trabajamos sobre el cuerpo $\mathbb{Z}_2=\{0,1\}$, con la aritmética módulo 2: $0+0=0$, $0+1=1+0=1$, $1+1=0$, y el producto usual ($1\cdot1=1$, los demás dan $0$). Como $1+1=0$, cada elemento es su propio opuesto: **restar es lo mismo que sumar**. La eliminación gaussiana funciona sin cambios (el único pivote posible es $1$, así que nunca hay que dividir), y un sistema compatible con $r$ variables libres tiene exactamente $2^r$ soluciones, porque cada variable libre toma solo dos valores. La aritmética de $\mathbb{Z}_2$ se desarrolla en [cuerpos y ℤ₂](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/).

### Ejemplo 4 · Un sistema en ℤ₂
<!-- check: R.T03.E4 -->

Resolvemos en $\mathbb{Z}_2$:

$$
\begin{cases}x_1+x_2+x_4=1\\ x_2+x_3+x_4=0\\ x_1+x_3=1\end{cases}
$$

Con $F_3+F_1\to F_3$ (en $\mathbb{Z}_2$ es lo mismo que $F_3-F_1$): la nueva tercera fila es $(1+1,\,0+1,\,1+0,\,0+1\mid1+1)=(0,1,1,1\mid0)$. Luego $F_3+F_2\to F_3$ la anula, y $F_1+F_2\to F_1$ da la forma reducida:

$$
\left(\begin{array}{cccc|c}1&1&0&1&1\\0&1&1&1&0\\1&0&1&0&1\end{array}\right)\sim\left(\begin{array}{cccc|c}1&1&0&1&1\\0&1&1&1&0\\0&0&0&0&0\end{array}\right)\sim\left(\begin{array}{cccc|c}1&0&1&0&1\\0&1&1&1&0\\0&0&0&0&0\end{array}\right).
$$

Las variables libres son $x_3$ y $x_4$. Como $-1=1$ en $\mathbb{Z}_2$, despejar es sumar: $x_1=1+x_3$ y $x_2=x_3+x_4$. La solución general es

$$
x=(1,0,0,0)+x_3\,(1,1,1,0)+x_4\,(0,1,0,1),\qquad x_3,x_4\in\mathbb{Z}_2 ,
$$

y como hay dos variables libres hay $2^2=4$ soluciones: $(1,0,0,0)$, $(0,1,1,0)$, $(1,1,0,1)$ y $(0,0,1,1)$.

**Comprobación.** Para $(0,1,1,0)$: $0+1+0=1$, $1+1+0=0$, $0+1=1$. Para $(0,0,1,1)$: $0+0+1=1$, $0+1+1=0$, $0+1=1$. Las otras dos se verifican igual.

:::caution[Errores frecuentes]
- **Leer el sistema sin escalonar del todo.** Una fila $(0\ 0\ 0\mid c)$ con $c\neq0$ indica incompatibilidad, aunque las demás filas "se vean bien".
- **Contar variables libres por ecuación.** El número de parámetros es $n-\operatorname{rango}(A)$, no $n-m$: en el Ejemplo 1 hay tres ecuaciones y cuatro incógnitas, pero dos variables libres, porque una ecuación era redundante.
- **Dividir por el parámetro.** En el Ejemplo 2, despejar $z=\frac{b-3}{a-5}$ sin haber separado el caso $a=5$ pierde los casos SCI y SI.
- **Operar columnas al resolver un sistema.** Las operaciones de columna cambian las incógnitas; para resolver $Ax=b$ solo se usan operaciones de fila sobre $(A\mid b)$.
- **Aritmética real en $\mathbb{Z}_2$.** En $\mathbb{Z}_2$, $x_1+x_1=0$ y no $2x_1$; escribir $-1$ o $2$ en una matriz de $\mathbb{Z}_2$ indica un error.
- **Olvidar la solución trivial.** Un sistema homogéneo nunca es incompatible.
:::

:::tip[En resumen]
- $Ax=b$ se resuelve escalonando $(A\mid b)$ con operaciones de fila, que no cambian las soluciones.
- Rouché-Frobenius: compatible $\iff\operatorname{rango}(A)=\operatorname{rango}(A\mid b)$; determinado si además el rango es $n$; si no, hay $n-\operatorname{rango}(A)$ variables libres.
- $Ax=0$ siempre es compatible; su solución general es una combinación lineal de vectores fijos, y las soluciones de $Ax=b$ son una particular más las del homogéneo.
- Con parámetros: escalonar sin dividir y separar casos.
- Varios sistemas con la misma $A$: $(A\mid b_1\ \cdots\ b_k)$ se escalona una vez.
- En $\mathbb{Z}_2$ restar es sumar y hay $2^r$ soluciones si hay $r$ variables libres.
:::

## Ejercicios de repaso

### Ejercicio R.09 · Sistema compatible determinado
<!-- ejercicio: R.09 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Resolver por eliminación gaussiana y clasificar el sistema $\begin{cases}x+y+z=6\\ 2x-y+z=3\\ x+2y-z=2\end{cases}$
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escalonar la matriz ampliada y resolver hacia atrás.

Con $F_2-2F_1\to F_2$ y $F_3-F_1\to F_3$; luego intercambiamos $F_2\leftrightarrow F_3$ para tener pivote $1$ y hacemos $F_3+3F_2\to F_3$:

$$
\left(\begin{array}{ccc|c}1&1&1&6\\2&-1&1&3\\1&2&-1&2\end{array}\right)\sim\left(\begin{array}{ccc|c}1&1&1&6\\0&-3&-1&-9\\0&1&-2&-4\end{array}\right)\sim\left(\begin{array}{ccc|c}1&1&1&6\\0&1&-2&-4\\0&0&-7&-21\end{array}\right).
$$

Hay tres pivotes: $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)=3$, compatible determinado. De abajo hacia arriba: $z=3$, $y=-4+2z=2$, $x=6-y-z=1$.

**Comprobación.** $1+2+3=6$, $2-2+3=3$, $1+4-3=2$.

:::tip[Resultado]
Compatible determinado, con única solución $(x,y,z)=(1,2,3)$.
:::

</details>

### Ejercicio R.10 · Solución general de un sistema homogéneo
<!-- ejercicio: R.10 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallar la solución general del sistema homogéneo $Ax=0$ con $A=\begin{pmatrix}1&-1&2&0\\2&-2&3&1\\1&-1&1&1\end{pmatrix}$ y escribirla como combinación lineal de vectores fijos. Indicar $\operatorname{rango}(A)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En un homogéneo basta escalonar $A$ (la columna de ceros no cambia). Llevar a la forma reducida para despejar directamente.

Con $F_2-2F_1\to F_2$ y $F_3-F_1\to F_3$ las dos filas quedan iguales a $(0,0,-1,1)$; $F_3-F_2\to F_3$ anula la tercera. Luego $-F_2\to F_2$ y $F_1-2F_2\to F_1$:

$$
A\sim\begin{pmatrix}1&-1&2&0\\0&0&-1&1\\0&0&0&0\end{pmatrix}\sim\begin{pmatrix}1&-1&0&2\\0&0&1&-1\\0&0&0&0\end{pmatrix}.
$$

Principales $x_1,x_3$; libres $x_2,x_4$. Despejando, $x_1=x_2-2x_4$ y $x_3=x_4$:

$$
x=x_2\,(1,1,0,0)+x_4\,(-2,0,1,1),\qquad x_2,x_4\in\mathbb{R}.
$$

**Comprobación.** $A\,(1,1,0,0)^t=(1-1,\,2-2,\,1-1)=(0,0,0)$ y $A\,(-2,0,1,1)^t=(-2+2,\,-4+3+1,\,-2+1+1)=(0,0,0)$.

:::tip[Resultado]
$\operatorname{rango}(A)=2$; las soluciones son $x_2\,(1,1,0,0)+x_4\,(-2,0,1,1)$ con $x_2,x_4\in\mathbb{R}$.
:::

</details>

### Ejercicio R.11 · Clasificación según un parámetro
<!-- ejercicio: R.11 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Clasificar según $k\in\mathbb{R}$ el sistema $\begin{cases}x+y+kz=1\\ x+ky+z=1\\ kx+y+z=1\end{cases}$ y resolverlo en los casos compatibles.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La matriz de coeficientes es cuadrada: calcular su determinante para aislar los valores críticos de $k$ y estudiar esos casos por separado.

La matriz de coeficientes se obtiene de la matriz $A_k$ del Ejemplo 3 de [R.2](/algebra-ii/repaso/determinantes/) intercambiando las filas 1 y 3, así que su determinante es $-(k-1)^2(k+2)$.

- **$k\neq1$ y $k\neq-2$:** el determinante no es nulo, compatible determinado. Probamos $x=y=z=t$: cada ecuación queda $(k+2)\,t=1$, así que $t=\frac{1}{k+2}$ es solución, y por ser única es **la** solución.
- **$k=1$:** las tres ecuaciones son $x+y+z=1$. $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)=1<3$: compatible indeterminado con dos variables libres, $(x,y,z)=(1,0,0)+y\,(-1,1,0)+z\,(-1,0,1)$.
- **$k=-2$:** escalonamos con $F_2-F_1\to F_2$, $F_3+2F_1\to F_3$ y luego $F_3+F_2\to F_3$:

$$
\left(\begin{array}{ccc|c}1&1&-2&1\\1&-2&1&1\\-2&1&1&1\end{array}\right)\sim\left(\begin{array}{ccc|c}1&1&-2&1\\0&-3&3&0\\0&3&-3&3\end{array}\right)\sim\left(\begin{array}{ccc|c}1&1&-2&1\\0&-3&3&0\\0&0&0&3\end{array}\right).
$$

$\operatorname{rango}(A)=2<3=\operatorname{rango}(A\mid b)$: incompatible.

**Comprobación.** Para $k=-2$, sumar las tres ecuaciones da $0=3$, lo que confirma la incompatibilidad. Para $k=0$, la solución $x=y=z=\frac12$ cumple $\frac12+\frac12+0=1$ en las tres ecuaciones.

:::tip[Resultado]
$k\notin\{1,-2\}$: SCD con $x=y=z=\frac{1}{k+2}$. $k=1$: SCI, $(1,0,0)+y\,(-1,1,0)+z\,(-1,0,1)$. $k=-2$: SI.
:::

</details>

### Ejercicio R.12 · Todas las soluciones en ℤ₂
<!-- ejercicio: R.12 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Resolver en $\mathbb{Z}_2$ el sistema $\begin{cases}x_1+x_3+x_4=1\\ x_2+x_3=1\\ x_1+x_2+x_4=0\end{cases}$ Listar todas sus soluciones e indicar cuántas soluciones tiene el sistema homogéneo asociado.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escalonar con aritmética módulo 2 (restar es sumar) y contar $2^r$ soluciones, con $r$ la cantidad de variables libres.

Con $F_3+F_1\to F_3$ la tercera fila pasa a $(0,1,1,0\mid1)$, igual a la segunda; $F_3+F_2\to F_3$ la anula:

$$
\left(\begin{array}{cccc|c}1&0&1&1&1\\0&1&1&0&1\\1&1&0&1&0\end{array}\right)\sim\left(\begin{array}{cccc|c}1&0&1&1&1\\0&1&1&0&1\\0&0&0&0&0\end{array}\right).
$$

Ya es escalonada reducida. Libres $x_3,x_4$; $x_1=1+x_3+x_4$, $x_2=1+x_3$:

$$
x=(1,1,0,0)+x_3\,(1,1,1,0)+x_4\,(1,0,0,1),\qquad x_3,x_4\in\mathbb{Z}_2 .
$$

Dando a $(x_3,x_4)$ los valores $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$: $(1,1,0,0)$, $(0,0,1,0)$, $(0,1,0,1)$, $(1,0,1,1)$. El homogéneo asociado tiene la misma cantidad de variables libres, así que también tiene $2^2=4$ soluciones: las combinaciones de $(1,1,1,0)$ y $(1,0,0,1)$.

**Comprobación.** Para $(1,0,1,1)$: $1+1+1=1$, $0+1=1$, $1+0+1=0$. Para $(0,1,0,1)$: $0+0+1=1$, $1+0=1$, $0+1+1=0$.

:::tip[Resultado]
Cuatro soluciones: $(1,1,0,0)$, $(0,0,1,0)$, $(0,1,0,1)$, $(1,0,1,1)$. El homogéneo también tiene 4.
:::

</details>

## Dónde se usa en Álgebra II

- Pertenencia a un generado y generadores de un subespacio: [combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/); decidir dependencia: [independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/).
- $\operatorname{nul}(A)$, $\operatorname{rango}(A)$ y la relación $\operatorname{rango}(A)+\dim\operatorname{nul}(A)=n$: [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/).
- Coordenadas y matriz ampliada múltiple: [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/) y [cambio de coordenadas](/algebra-ii/unidad-1/teoria/cambio-de-coordenadas/).
- Sistemas en $\mathbb{Z}_2$: [cuerpos y ℤ₂](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/) y [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/).
- Núcleo de una transformación lineal como sistema homogéneo: [núcleo e imagen](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/).
- Autoespacios $E_\lambda(A)=\operatorname{nul}(\lambda I-A)$: [autovalores y autovectores](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/).
- Ecuaciones normales $A^tAx=A^tb$: [cuadrados mínimos](/algebra-ii/unidad-4/teoria/cuadrados-minimos/).

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 2.2 (métodos directos para resolver sistemas lineales) y, para la aritmética módulo 2, la subsección "Vectores binarios y aritmética modular" de la sección 1.1.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ecuaciones lineales.
- Lección anterior: [R.2 Determinantes](/algebra-ii/repaso/determinantes/). Siguiente: [R.4 Polinomios](/algebra-ii/repaso/polinomios/).
