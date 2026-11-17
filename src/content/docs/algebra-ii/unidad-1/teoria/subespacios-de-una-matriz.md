---
title: Subespacios de una matriz
description: Espacio fila, espacio columna y espacio nulo de una matriz, cómo obtener sus bases por escalonamiento, rango y teorema rango–nulidad sobre ℝ y sobre ℤ₂.
slug: algebra-ii/unidad-1/teoria/subespacios-de-una-matriz
sidebar:
  order: 6
  label: 1.6 Subespacios de una matriz
---

## Para qué sirve

Toda matriz $A\in K^{m\times n}$ trae consigo tres subespacios: el generado por sus filas, el
generado por sus columnas y el conjunto de soluciones de $Ax=0$. Casi todas las preguntas de la
unidad se reducen a ellos: decidir si un vector es combinación lineal de otros es preguntar si
pertenece a un espacio columna; hallar generadores de un subespacio dado por ecuaciones es calcular
un espacio nulo; extraer un conjunto linealmente independiente de un generador es elegir columnas
pivote. Y el mismo cálculo (escalonar) resuelve las tres cosas a la vez.

En informática estos subespacios aparecen sin disfraz: un código corrector de errores es el espacio
fila de una matriz generadora y, al mismo tiempo, el espacio nulo de una matriz de control
(lo vemos en [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/)).

En esta lección usamos las nociones de **base** (conjunto linealmente independiente que genera) y
**dimensión** (cantidad de vectores de una base). Que todas las bases de un subespacio tengan la
misma cantidad de vectores se demuestra en la lección siguiente,
[base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/). Escalonar matrices y resolver
sistemas se repasa en [sistemas lineales](/algebra-ii/repaso/sistemas-lineales/).

## Los tres subespacios

:::note[Definición]
Sea $A\in K^{m\times n}$, con $K=\mathbb{R}$ o $K=\mathbb{Z}_2$. Notamos $f_1,\dots,f_m$ sus filas y
$c_1,\dots,c_n$ sus columnas.

- **Espacio fila**: $\operatorname{fil}(A)=\operatorname{gen}\{f_1,\dots,f_m\}\subseteq K^n$.
- **Espacio columna**: $\operatorname{col}(A)=\operatorname{gen}\{c_1,\dots,c_n\}\subseteq K^m$.
- **Espacio nulo**: $\operatorname{nul}(A)=\{x\in K^n:\ Ax=0\}\subseteq K^n$.
:::

Los dos primeros son subespacios porque todo generado lo es (ver
[combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/)). Para el tercero
aplicamos el criterio de subespacio de [subespacios](/algebra-ii/unidad-1/teoria/subespacios/):
$A0=0$, así que $0\in\operatorname{nul}(A)$; si $Ax=0$ y $Ay=0$, entonces $A(x+y)=Ax+Ay=0$; y si
$\lambda\in K$, $A(\lambda x)=\lambda Ax=0$.

Observemos dónde vive cada uno: $\operatorname{fil}(A)$ y $\operatorname{nul}(A)$ están en $K^n$
(tantas componentes como columnas tiene $A$), mientras que $\operatorname{col}(A)$ está en $K^m$
(tantas componentes como filas). Cuando $m\neq n$ no tiene sentido preguntar si un vector de
$\operatorname{col}(A)$ está en $\operatorname{fil}(A)$.

## El producto $Ax$ como combinación de columnas

:::note[Propiedad]
Si $A\in K^{m\times n}$ tiene columnas $c_1,\dots,c_n$ y $x=(x_1,\dots,x_n)$, entonces

$$
Ax=x_1c_1+x_2c_2+\dots+x_nc_n .
$$
:::

**Demostración.** La componente $i$ de $Ax$ es $a_{i1}x_1+a_{i2}x_2+\dots+a_{in}x_n$. La componente
$i$ de $x_1c_1+\dots+x_nc_n$ es $x_1a_{i1}+\dots+x_na_{in}$, porque la componente $i$ de la columna
$c_j$ es $a_{ij}$. Son iguales para cada $i$. $\blacksquare$

Por ejemplo,

$$
\begin{pmatrix}1&3\\2&-1\end{pmatrix}\begin{pmatrix}2\\-1\end{pmatrix}
=2\begin{pmatrix}1\\2\end{pmatrix}+(-1)\begin{pmatrix}3\\-1\end{pmatrix}
=\begin{pmatrix}-1\\5\end{pmatrix}.
$$

Esta lectura del producto cambia el sentido de un sistema lineal: resolver $Ax=b$ es buscar los
coeficientes con los que las columnas de $A$ "fabrican" el vector $b$.

:::note[Teorema]
El sistema $Ax=b$ es compatible si y solo si $b\in\operatorname{col}(A)$.
:::

**Demostración.** Si el sistema tiene una solución $x=(x_1,\dots,x_n)$, entonces
$b=Ax=x_1c_1+\dots+x_nc_n$ es combinación lineal de las columnas, es decir,
$b\in\operatorname{col}(A)$. Recíprocamente, si $b\in\operatorname{col}(A)$ existen escalares
$\alpha_1,\dots,\alpha_n$ con $b=\alpha_1c_1+\dots+\alpha_nc_n$, y entonces
$x=(\alpha_1,\dots,\alpha_n)$ cumple $Ax=b$. $\blacksquare$

En particular, $\operatorname{col}(A)=\{Ax: x\in K^n\}$: el espacio columna es el conjunto de todos
los $b$ para los que el sistema tiene solución. Y cuando el sistema es compatible, el conjunto de
soluciones es $x_p+\operatorname{nul}(A)$, con $x_p$ una solución particular: si $Ax_p=b$, entonces
$Ax=b$ equivale a $A(x-x_p)=0$.

## Qué cambia y qué no cuando escalonamos

Para calcular usamos operaciones elementales de fila: intercambiar dos filas, multiplicar una fila
por un escalar no nulo y sumarle a una fila un múltiplo de otra. Cada operación equivale a
multiplicar a izquierda por una matriz elemental inversible; por lo tanto, si $A'$ es una
escalonada de $A$, existe $P\in K^{m\times m}$ inversible con $A'=PA$.

:::note[Teorema]
Si $A'$ se obtiene de $A$ por operaciones elementales de fila, entonces
$\operatorname{fil}(A')=\operatorname{fil}(A)$ y $\operatorname{nul}(A')=\operatorname{nul}(A)$.
:::

**Demostración.** Escribimos $A'=PA$ con $P$ inversible.

*Espacio fila.* La fila $i$ de $PA$ es $p_{i1}f_1+\dots+p_{im}f_m$, una combinación lineal de las filas
de $A$; luego cada fila de $A'$ está en $\operatorname{fil}(A)$ y, como este es un subespacio,
$\operatorname{fil}(A')\subseteq\operatorname{fil}(A)$. Como también $A=P^{-1}A'$, el mismo argumento
da $\operatorname{fil}(A)\subseteq\operatorname{fil}(A')$.

*Espacio nulo.* Si $Ax=0$, entonces $A'x=PAx=P0=0$. Si $A'x=0$, entonces
$Ax=P^{-1}A'x=0$. $\blacksquare$

El espacio columna, en cambio, **sí puede cambiar**. Con

$$
A=\begin{pmatrix}1&1\\1&1\end{pmatrix}\xrightarrow{F_2-F_1\to F_2}A'=\begin{pmatrix}1&1\\0&0\end{pmatrix}
$$

resulta $\operatorname{col}(A)=\operatorname{gen}\{(1,1)\}$ y
$\operatorname{col}(A')=\operatorname{gen}\{(1,0)\}$, que son rectas distintas de $\mathbb{R}^2$:
$(1,0)\notin\operatorname{col}(A)$.

Lo que se conserva son las **relaciones lineales entre columnas**. Como
$\operatorname{nul}(A)=\operatorname{nul}(A')$, para cualquier $x$ vale

$$
x_1c_1+\dots+x_nc_n=0 \iff x_1c_1'+\dots+x_nc_n'=0 ,
$$

donde $c_j'$ son las columnas de $A'$. Así, un grupo de columnas de $A$ es linealmente independiente
si y solo si lo es el grupo de columnas de $A'$ con los mismos índices, y $c_k=\sum_j\alpha_jc_j$ si y
solo si $c_k'=\sum_j\alpha_jc_j'$, con los mismos coeficientes.

## Bases de los tres subespacios a partir de la escalonada

Sea $A'$ una forma escalonada de $A$ con $r$ filas no nulas. Llamamos **columnas pivote** a las que
contienen el primer elemento no nulo (pivote) de alguna fila; hay exactamente $r$.

:::note[Teorema]
1. Las $r$ filas no nulas de $A'$ forman una base de $\operatorname{fil}(A)$.
2. Las columnas de $A$ (la matriz **original**) que ocupan las posiciones pivote forman una base de
   $\operatorname{col}(A)$.
3. Resolviendo $A'x=0$ y escribiendo la solución general como combinación de las variables libres,
   los $n-r$ vectores que acompañan a cada variable libre forman una base de $\operatorname{nul}(A)$.
:::

**Demostración.**

1. Las filas no nulas de $A'$ generan $\operatorname{fil}(A')=\operatorname{fil}(A)$ (las filas
   nulas no aportan). Son linealmente independientes: si
   $\lambda_1g_1+\dots+\lambda_rg_r=0$, miramos la columna del pivote de $g_1$; ahí solo $g_1$ tiene
   entrada no nula (las filas siguientes tienen ceros debajo del pivote), así que $\lambda_1=0$.
   Repitiendo con $g_2$, luego $g_3$, etc., todos los $\lambda_i$ son nulos.
2. En $A'$, las columnas pivote son independientes: la submatriz que forman es escalonada con un
   pivote en cada columna, de modo que el sistema homogéneo asociado solo tiene la solución trivial.
   Además cada columna no pivote $c_k'$ es combinación de las columnas pivote: el sistema cuya matriz
   ampliada es (columnas pivote $\mid c_k'$) no tiene pivote en la última columna, luego es
   compatible. Por la conservación de relaciones lineales, lo mismo vale para las columnas de $A$:
   las columnas pivote de $A$ son independientes y generan a todas las demás, es decir, a
   $\operatorname{col}(A)$.
3. En la solución general $x=\sum_{\ell}t_\ell s_\ell$ (una $t_\ell$ por variable libre), los
   $s_\ell$ generan $\operatorname{nul}(A')=\operatorname{nul}(A)$ por construcción. Son
   independientes porque $s_\ell$ tiene un $1$ en la posición de su variable libre y $0$ en las
   posiciones de las otras variables libres: si $\sum t_\ell s_\ell=0$, leyendo esas posiciones
   queda $t_\ell=0$ para cada $\ell$. $\blacksquare$

:::danger[Columnas pivote de la matriz original]
La base de $\operatorname{col}(A)$ se toma de las columnas de $A$, no de las de $A'$. Las columnas
de $A'$ indican **qué posiciones** elegir, pero en general no pertenecen a $\operatorname{col}(A)$.
:::

## Rango y teorema rango–nulidad

Del teorema anterior, $\dim\operatorname{fil}(A)=r$ y $\dim\operatorname{col}(A)=r$: las dos
dimensiones cuentan los pivotes de una misma escalonada.

:::note[Teorema]
Para toda $A\in K^{m\times n}$, $\dim\operatorname{fil}(A)=\dim\operatorname{col}(A)$ (rango fila
igual a rango columna). Ese número común es el **rango** de $A$, $\operatorname{rango}(A)$. En
consecuencia, $\operatorname{rango}(A)=\operatorname{rango}(A^t)$.
:::

La última afirmación sale de que las filas de $A^t$ son las columnas de $A$:
$\dim\operatorname{fil}(A^t)=\dim\operatorname{col}(A)=\dim\operatorname{fil}(A)$.

:::note[Teorema rango–nulidad]
Si $A\in K^{m\times n}$, entonces

$$
\operatorname{rango}(A)+\dim\operatorname{nul}(A)=n .
$$
:::

**Demostración.** Cada una de las $n$ incógnitas de $A'x=0$ es variable pivote o variable libre.
Hay $r=\operatorname{rango}(A)$ pivotes y, por el punto 3 del teorema anterior,
$\dim\operatorname{nul}(A)$ es la cantidad de variables libres, $n-r$. $\blacksquare$

Este teorema es la versión matricial del teorema de la dimensión de la Unidad 2
([teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/)): $n$ es la
cantidad de incógnitas, el rango mide cuántas "sobreviven" como restricciones independientes y la
nulidad cuántos grados de libertad quedan.

## Rango e inversibilidad

:::note[Teorema]
Sea $A\in K^{n\times n}$. Son equivalentes:

1. $A$ es inversible.
2. $\operatorname{nul}(A)=\{0\}$.
3. $\operatorname{rango}(A)=n$.
4. Las columnas de $A$ forman una base de $K^n$ (y lo mismo las filas).
:::

**Demostración.** (1 ⇒ 2) Si $Ax=0$, multiplicando por $A^{-1}$ queda $x=0$. (2 ⇔ 3) Por rango–nulidad,
$\dim\operatorname{nul}(A)=0$ si y solo si $\operatorname{rango}(A)=n$. (3 ⇒ 1) Con $n$ pivotes en
una matriz $n\times n$ hay un pivote en cada fila y en cada columna, así que la escalonada reducida
es $I_n$; aplicando las mismas operaciones a $(A\mid I_n)$ se llega a $(I_n\mid A^{-1})$, como en
el [repaso de matrices](/algebra-ii/repaso/vectores-y-matrices/). (3 ⇔ 4) $\operatorname{rango}(A)=n$
dice que $\operatorname{col}(A)$ es un subespacio de dimensión $n$ de $K^n$, es decir, todo $K^n$,
y que las $n$ columnas son independientes. Lo mismo para las filas. $\blacksquare$

Con [determinantes](/algebra-ii/repaso/determinantes/) se agrega una condición más:
$\det(A)\neq0$.

## El cuerpo importa: la misma matriz sobre ℝ y sobre ℤ₂

Una matriz de ceros y unos puede leerse en $\mathbb{R}^{m\times n}$ o en $\mathbb{Z}_2^{m\times n}$.
Las operaciones de fila son distintas (en $\mathbb{Z}_2$, $1+1=0$ y restar es sumar), y el rango
puede cambiar. Como el determinante es una suma de productos de entradas con coeficientes $\pm1$, el
determinante en $\mathbb{Z}_2$ es el resto módulo 2 del determinante entero: una matriz con
determinante entero par no nulo es inversible sobre $\mathbb{R}$ y no lo es sobre $\mathbb{Z}_2$. El
ejemplo 2 muestra un caso.

## Ejemplos resueltos

### Ejemplo 1 · Los tres subespacios de una matriz real

<!-- check: U1.T06.E1 -->

Hallar bases de $\operatorname{fil}(A)$, $\operatorname{col}(A)$ y $\operatorname{nul}(A)$ para

$$
A=\begin{pmatrix}1&2&0&3\\2&4&1&8\\1&2&2&7\end{pmatrix}\in\mathbb{R}^{3\times4},
$$

verificar el teorema rango–nulidad y decidir si $Ax=b$ es compatible para $b=(1,1,-1)$ y para
$b=(1,0,0)$.

**Escalonamiento.**

$$
A\xrightarrow[F_3-F_1\to F_3]{F_2-2F_1\to F_2}
\begin{pmatrix}1&2&0&3\\0&0&1&2\\0&0&2&4\end{pmatrix}
\xrightarrow{F_3-2F_2\to F_3}
A'=\begin{pmatrix}1&2&0&3\\0&0&1&2\\0&0&0&0\end{pmatrix}.
$$

Hay dos pivotes, en las columnas 1 y 3: $\operatorname{rango}(A)=2$. La matriz $A'$ ya es
escalonada reducida (el pivote de la columna 3 tiene un cero arriba).

**Espacio fila.** $B_{\operatorname{fil}}=\{(1,2,0,3),(0,0,1,2)\}$, $\dim\operatorname{fil}(A)=2$.

**Espacio nulo.** $A'x=0$ es $x_1+2x_2+3x_4=0$, $x_3+2x_4=0$, con variables libres $x_2$ y $x_4$:

$$
x=(-2x_2-3x_4,\ x_2,\ -2x_4,\ x_4)=x_2(-2,1,0,0)+x_4(-3,0,-2,1).
$$

Entonces $B_{\operatorname{nul}}=\{(-2,1,0,0),(-3,0,-2,1)\}$ y $\dim\operatorname{nul}(A)=2$.

**Espacio columna.** Tomamos las columnas 1 y 3 **de $A$**:
$B_{\operatorname{col}}=\{(1,2,1),(0,1,2)\}$, $\dim\operatorname{col}(A)=2$. La escalonada reducida
dice además cómo se escriben las otras columnas: la columna 2 de $A'$ es $2$ veces la primera y la
columna 4 es $3c_1'+2c_3'$; por lo tanto $c_2=2c_1$ y $c_4=3c_1+2c_3$. En efecto,
$3(1,2,1)+2(0,1,2)=(3,8,7)$.

**Rango–nulidad.** $2+2=4$, la cantidad de columnas.

**Compatibilidad.** Buscamos una ecuación para $\operatorname{col}(A)$. Un vector $y$ está en
$\operatorname{col}(A)$ si $y=\alpha(1,2,1)+\beta(0,1,2)$: de $y_1=\alpha$, $y_2=2\alpha+\beta$,
$y_3=\alpha+2\beta$ sale $\beta=y_2-2y_1$ y la condición

$$
\operatorname{col}(A)=\{y\in\mathbb{R}^3:\ 3y_1-2y_2+y_3=0\}.
$$

Para $b=(1,1,-1)$: $3-2-1=0$, compatible. Con $\alpha=1$, $\beta=-1$ resulta $b=c_1-c_3$, así que
$x_p=(1,0,-1,0)$ es una solución y todas son $x_p+\operatorname{nul}(A)$. Para $b=(1,0,0)$:
$3\neq0$, incompatible.

Observemos que $\operatorname{col}(A')=\{y: y_3=0\}$ es otro plano: $(1,2,1)\in\operatorname{col}(A)$
pero $(1,2,1)\notin\operatorname{col}(A')$.

**Comprobación.** $A(-2,1,0,0)=-2c_1+c_2=0$ y $A(-3,0,-2,1)=-3c_1-2c_3+c_4=0$;
$A(1,0,-1,0)=c_1-c_3=(1,1,-1)$. Las dos columnas de $B_{\operatorname{col}}$ cumplen la ecuación
$3y_1-2y_2+y_3=0$ y no son proporcionales.

:::tip[Resultado]
$\operatorname{rango}(A)=2$, $\dim\operatorname{nul}(A)=2$;
$\operatorname{col}(A)=\{y: 3y_1-2y_2+y_3=0\}$; $Ax=(1,1,-1)$ es compatible y $Ax=(1,0,0)$ no.
:::

### Ejemplo 2 · Una matriz inversible sobre ℝ que no lo es sobre ℤ₂

<!-- check: U1.T06.E2 -->

Sea

$$
M=\begin{pmatrix}1&0&1&1\\0&1&0&1\\0&1&1&0\\0&0&1&1\end{pmatrix}.
$$

Calcular el rango de $M$ como matriz real y como matriz de $\mathbb{Z}_2^{4\times4}$; en cada caso
decidir si es inversible, dar bases de $\operatorname{nul}(M)$ y $\operatorname{col}(M)$ y analizar
el sistema $Mx=b$ para $b=(1,0,0,1)$ y $b=(1,1,0,1)$.

**Sobre $\mathbb{R}$.** La primera columna ya tiene su pivote. Seguimos con las filas 2 a 4:

$$
M\xrightarrow{F_3-F_2\to F_3}
\begin{pmatrix}1&0&1&1\\0&1&0&1\\0&0&1&-1\\0&0&1&1\end{pmatrix}
\xrightarrow{F_4-F_3\to F_4}
\begin{pmatrix}1&0&1&1\\0&1&0&1\\0&0&1&-1\\0&0&0&2\end{pmatrix}.
$$

Cuatro pivotes: $\operatorname{rango}(M)=4$, $\operatorname{nul}(M)=\{0\}$, las cuatro columnas son
base de $\mathbb{R}^4$ y $M$ es inversible ($\det M=1\cdot1\cdot1\cdot2=2$). Para cualquier $b$ el
sistema tiene solución única; con $b=(1,0,0,1)$ es $x=\left(0,-\tfrac12,\tfrac12,\tfrac12\right)$.

**Sobre $\mathbb{Z}_2$.** Ahora $-1=1$ y $2=0$:

$$
M\xrightarrow{F_3+F_2\to F_3}
\begin{pmatrix}1&0&1&1\\0&1&0&1\\0&0&1&1\\0&0&1&1\end{pmatrix}
\xrightarrow{F_4+F_3\to F_4}
M'=\begin{pmatrix}1&0&1&1\\0&1&0&1\\0&0&1&1\\0&0&0&0\end{pmatrix}.
$$

Tres pivotes (columnas 1, 2 y 3): $\operatorname{rango}(M)=3$ y $M$ **no** es inversible en
$\mathbb{Z}_2^{4\times4}$, coherente con $\det M=2\equiv0 \pmod 2$.

- $\operatorname{nul}(M)$: de $M'x=0$, con $x_4=t$ libre, sale $x_3=t$, $x_2=t$ y
  $x_1=x_3+x_4=0$. Base $\{(0,1,1,1)\}$; $\operatorname{nul}(M)=\{0,(0,1,1,1)\}$ tiene $2^1=2$
  elementos y $3+1=4$ confirma rango–nulidad.
- $\operatorname{col}(M)$: columnas 1, 2 y 3 de $M$, $\{(1,0,0,0),(0,1,1,0),(1,0,1,1)\}$. El vector
  del núcleo dice que $c_2+c_3+c_4=0$, es decir, $c_4=c_2+c_3$. Sobre $\mathbb{R}$ esa relación
  falla: $c_2+c_3-c_4=(0,0,2,0)$; el "2" es justamente lo que se anula en $\mathbb{Z}_2$.

**El sistema sobre $\mathbb{Z}_2$.** Aplicando las mismas operaciones a la columna ampliada, la
última fila queda $0=b_2+b_3+b_4$. Por eso
$\operatorname{col}(M)=\{b\in\mathbb{Z}_2^4: b_2+b_3+b_4=0\}$, que tiene $2^3=8$ elementos.

- $b=(1,0,0,1)$: $0+0+1=1\neq0$, **incompatible** en $\mathbb{Z}_2$ (aunque en $\mathbb{R}$ tenía
  solución única).
- $b=(1,1,0,1)$: $1+0+1=0$, compatible. Una solución es $x_p=(0,0,0,1)$, pues $Mx_p=c_4=b$, y el
  conjunto solución es $x_p+\operatorname{nul}(M)=\{(0,0,0,1),(0,1,1,0)\}$.

**Comprobación.** En $\mathbb{Z}_2$, $M(0,1,1,1)=c_2+c_3+c_4=(0,1,1,0)+(1,0,1,1)+(1,1,0,1)=(0,0,0,0)$
y $M(0,1,1,0)=c_2+c_3=(1,1,0,1)$. En $\mathbb{R}$,
$M\left(0,-\tfrac12,\tfrac12,\tfrac12\right)=\left(\tfrac12+\tfrac12,\ -\tfrac12+\tfrac12,\ -\tfrac12+\tfrac12,\ \tfrac12+\tfrac12\right)=(1,0,0,1)$.

:::tip[Resultado]
Sobre $\mathbb{R}$: $\operatorname{rango}(M)=4$, inversible. Sobre $\mathbb{Z}_2$:
$\operatorname{rango}(M)=3$, $\operatorname{nul}(M)=\operatorname{gen}\{(0,1,1,1)\}$,
$\operatorname{col}(M)=\{b: b_2+b_3+b_4=0\}$, no inversible.
:::

## Interpretación

- **Geométrica.** En el ejemplo 1, $\operatorname{col}(A)$ es un plano de $\mathbb{R}^3$ y
  $\operatorname{nul}(A)$ un plano de $\mathbb{R}^4$. El sistema $Ax=b$ "apunta" a $b$ con las
  columnas: si $b$ está fuera del plano $\operatorname{col}(A)$, no hay forma de alcanzarlo.
- **Algebraica.** $\operatorname{nul}(A)$ registra todas las relaciones lineales entre las columnas;
  $\operatorname{fil}(A)$ registra todas las ecuaciones que se pueden deducir combinando las
  ecuaciones del sistema homogéneo.
- **Computacional.** Un único escalonamiento entrega rango, una base de cada subespacio y la
  compatibilidad de cualquier sistema con esa matriz de coeficientes. Sobre $\mathbb{Z}_2$ las
  operaciones de fila son XOR de cadenas de bits, que es exactamente lo que hacen los
  decodificadores de códigos lineales.

## Errores frecuentes

:::caution[Errores frecuentes]
- **Tomar las columnas pivote de la escalonada como base de $\operatorname{col}(A)$.** Con
  $A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$, la escalonada tiene columna pivote $(1,0)$, que no está
  en $\operatorname{col}(A)=\operatorname{gen}\{(1,1)\}$.
- **Tomar las filas originales "que tenían pivote" como base de $\operatorname{fil}(A)$ después de
  intercambiar filas.** Lo seguro es usar las filas no nulas de la escalonada. Las filas originales
  sirven solo si se controla que sean independientes.
- **Confundir dónde vive cada subespacio.** En el ejemplo 1, $\operatorname{nul}(A)\subseteq\mathbb{R}^4$
  y $\operatorname{col}(A)\subseteq\mathbb{R}^3$: un vector de tres componentes nunca puede estar
  en $\operatorname{nul}(A)$.
- **Restar la cantidad de filas en rango–nulidad.** La fórmula usa $n$, la cantidad de
  **columnas**: para $A\in K^{3\times4}$ de rango 2, la nulidad es $4-2=2$, no $3-2=1$.
- **Escalonar sobre $\mathbb{Z}_2$ con reglas reales.** En el ejemplo 2, quien opera en
  $\mathbb{R}$ y al final "reduce módulo 2" obtiene un pivote $2$ que en $\mathbb{Z}_2$ es $0$; hay
  que reducir en cada paso y no dividir por números pares.
:::

## Autoevaluación

1. Si $A\in\mathbb{R}^{5\times7}$ tiene rango 5, ¿qué dimensión tiene $\operatorname{nul}(A)$? ¿Es
   $Ax=b$ compatible para todo $b$?
2. ¿Puede una matriz $3\times5$ tener columnas linealmente independientes?
3. Verdadero o falso: si $A'$ es una escalonada de $A$, entonces $\operatorname{col}(A)=\operatorname{col}(A')$.

<details>
<summary>Respuestas</summary>

1. $\dim\operatorname{nul}(A)=7-5=2$. Sí: $\operatorname{col}(A)$ es un subespacio de dimensión 5 de
   $\mathbb{R}^5$, o sea todo $\mathbb{R}^5$.
2. No: el rango es a lo sumo 3 (no puede haber más pivotes que filas), así que entre 5 columnas a
   lo sumo 3 son independientes; por rango–nulidad, $\dim\operatorname{nul}(A)\geq2$.
3. Falso; contraejemplo: $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ y su escalonada
   $\begin{pmatrix}1&1\\0&0\end{pmatrix}$.

</details>

## Resumen

:::tip[En resumen]
- $\operatorname{fil}(A)\subseteq K^n$, $\operatorname{col}(A)\subseteq K^m$,
  $\operatorname{nul}(A)\subseteq K^n$ para $A\in K^{m\times n}$.
- $Ax=x_1c_1+\dots+x_nc_n$; $Ax=b$ es compatible si y solo si $b\in\operatorname{col}(A)$.
- Escalonar conserva $\operatorname{fil}$, $\operatorname{nul}$ y las relaciones entre columnas, pero
  no $\operatorname{col}$.
- Bases: filas no nulas de la escalonada; columnas pivote de la matriz original; un vector por
  variable libre.
- Rango fila = rango columna = cantidad de pivotes; $\operatorname{rango}(A)+\dim\operatorname{nul}(A)=n$.
- $A\in K^{n\times n}$ es inversible si y solo si $\operatorname{rango}(A)=n$. El rango depende del
  cuerpo.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 3.5, "Subespacios, bases,
  dimensión y rank", p. 197 (espacio renglón, espacio columna, espacio nulo y teorema del rango).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: espacios nulos y espacios columna; rango.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed., sección 1.2 (rango de una
  matriz), p. 13.
- Lecciones relacionadas: [independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/)
  (anterior), [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/) (siguiente),
  [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/) (aplicación) y el repaso de
  [sistemas lineales](/algebra-ii/repaso/sistemas-lineales/).
