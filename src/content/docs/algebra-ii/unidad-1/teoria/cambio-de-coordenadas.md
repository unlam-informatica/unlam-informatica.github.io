---
title: Cambio de coordenadas
description: Matriz de cambio de coordenadas C_BB′, sus propiedades (unicidad, inversa, composición), métodos de cálculo y aplicaciones con bases de ℝ³, polinomios y bases abstractas.
slug: algebra-ii/unidad-1/teoria/cambio-de-coordenadas
sidebar:
  order: 9
  label: 1.9 Cambio de coordenadas
---

## Para qué sirve

Un mismo vector tiene coordenadas distintas en bases distintas. A veces el dato viene en una base y
la pregunta conviene responderla en otra: un plano que en la base canónica tiene ecuación
$x-2y+z=0$ puede tener, en una base elegida a medida, la ecuación $y_3=0$. La **matriz de cambio de
coordenadas** hace esa traducción con un solo producto matricial, y no depende del vector: se
calcula una vez y sirve para todos.

En computación gráfica, robótica o procesamiento de señales se cambia de "sistema de referencia"
todo el tiempo; algebraicamente, cada cambio es una matriz de este tipo.

Partimos de [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/). En toda la lección $V$ es un
espacio de dimensión $n$ sobre $K$ y $B=\{b_1,\dots,b_n\}$, $B'=\{b_1',\dots,b_n'\}$,
$B''$ son bases ordenadas de $V$.

## Intuición

En la figura, el vector $v=(2,3)$ se mide con dos grillas. En la base $B$ sus coordenadas son
$(1,2)$; en la base $B'$, $(2,1)$. Para pasar de unas a otras no hace falta volver al vector:
alcanza con saber cómo se escriben los vectores de $B$ en la base $B'$.

<figure class="math-figure">
@@FIG19@@
</figure>

Si $v=x_1b_1+\dots+x_nb_n$, la linealidad de las coordenadas da

$$
[v]_{B'}=x_1[b_1]_{B'}+\dots+x_n[b_n]_{B'}=\big([b_1]_{B'}\mid\cdots\mid[b_n]_{B'}\big)\begin{pmatrix}x_1\\ \vdots\\ x_n\end{pmatrix}.
$$

La matriz que aparece solo depende de las dos bases.

## Definición y propiedades

:::note[Definición]
La **matriz de cambio de coordenadas de $B$ a $B'$** es la matriz $n\times n$ cuyas columnas son
las coordenadas de los vectores de $B$ respecto de $B'$:

$$
C_{BB'}=\big([b_1]_{B'}\mid[b_2]_{B'}\mid\cdots\mid[b_n]_{B'}\big).
$$
:::

:::caution[Notación de los libros]
Poole y Lay escriben $P_{B'\leftarrow B}$ para la matriz que aquí notamos $C_{BB'}$: los subíndices
aparecen en orden inverso ("hacia $B'$ desde $B$"). La matriz es la misma y cumple
$P_{B'\leftarrow B}[v]_B=[v]_{B'}$. Al leer ejercicios de esos libros, traducir antes de calcular.
La tabla completa de equivalencias está en [notación](/algebra-ii/notacion/).
:::

:::note[Teorema (propiedades de la matriz de cambio)]
1. $C_{BB'}[v]_B=[v]_{B'}$ para todo $v\in V$.
2. Es la **única** matriz con esa propiedad: si $M\in K^{n\times n}$ cumple $M[v]_B=[v]_{B'}$ para
   todo $v$, entonces $M=C_{BB'}$.
3. $C_{BB}=I_n$.
4. Composición: $C_{BB''}=C_{B'B''}\,C_{BB'}$.
5. $C_{BB'}$ es inversible y $(C_{BB'})^{-1}=C_{B'B}$.
:::

**Demostración.**

1. Es la cuenta de la intuición: si $[v]_B=(x_1,\dots,x_n)^t$, entonces
   $[v]_{B'}=\sum_jx_j[b_j]_{B'}$, que es el producto de $C_{BB'}$ por $[v]_B$ (un producto matriz
   por columna es la combinación de las columnas con esos coeficientes).
2. Tomando $v=b_j$, que tiene $[b_j]_B=e_j$, resulta $Me_j=[b_j]_{B'}$. Pero $Me_j$ es la columna
   $j$ de $M$. Luego $M$ y $C_{BB'}$ tienen las mismas columnas.
3. $[b_j]_B=e_j$, así que las columnas de $C_{BB}$ son $e_1,\dots,e_n$.
4. Para todo $v$, $C_{B'B''}C_{BB'}[v]_B=C_{B'B''}[v]_{B'}=[v]_{B''}$. Por la unicidad (punto 2,
   con $B''$ en lugar de $B'$), $C_{B'B''}C_{BB'}=C_{BB''}$.
5. Por 4 y 3, $C_{B'B}C_{BB'}=C_{BB}=I_n$ y $C_{BB'}C_{B'B}=C_{B'B'}=I_n$. $\blacksquare$

Regla para no equivocarse con la composición: en $C_{B'B''}\,C_{BB'}$, leyendo de derecha a
izquierda, la base de llegada de cada factor es la de partida del siguiente
($B\to B'$, luego $B'\to B''$).

Otras consecuencias directas de la definición:

- **Cuadrada e inversible**: las dos bases tienen $n$ vectores, y las columnas $[b_j]_{B'}$ son
  independientes porque los $b_j$ lo son (independencia se conserva al pasar a coordenadas).
- **Reordenar las bases**: permutar los vectores de $B$ permuta las **columnas** de $C_{BB'}$;
  permutar los de $B'$ permuta sus **filas**.
- **El caso canónico en $K^n$**: como $[w]_E=w$, la matriz $C_{BE}$ tiene como columnas a los
  propios vectores de $B$. Y $C_{EB}=(C_{BE})^{-1}$.

## Métodos de cálculo

**Método 1: sistemas con matriz ampliada múltiple (en $K^n$).** Calcular $[b_j]_{B'}$ es resolver
un sistema con matriz de coeficientes $(b_1'\mid\cdots\mid b_n')$ y columna independiente $b_j$.
Como los $n$ sistemas tienen la misma matriz de coeficientes, se resuelven a la vez:

$$
\big(b_1'\ \cdots\ b_n'\ \big|\ b_1\ \cdots\ b_n\big)\ \longrightarrow\ \big(I_n\ \big|\ C_{BB'}\big).
$$

Se escalona hasta la forma reducida; como las columnas de la izquierda son una base, la reducida
de la izquierda es $I_n$ y a la derecha queda $C_{BB'}$.

**Método 2: a través de la base canónica.** Por la composición,

$$
C_{BB'}=C_{EB'}\,C_{BE}=(C_{B'E})^{-1}\,C_{BE},
$$

donde $C_{BE}$ y $C_{B'E}$ se escriben sin cuentas (columnas = vectores de cada base). Conviene
cuando ya se conoce la inversa de $C_{B'E}$ o cuando hay que pasar por varias bases.

**Método 3: sistema "con incógnitas vectoriales" (bases abstractas).** Si los datos son relaciones
del tipo $b_1'=b_1+b_2$, se despejan los vectores de una base en función de los de la otra usando
solo las operaciones del espacio vectorial, como en un sistema lineal cuyas incógnitas son
vectores. Equivalentemente, se escribe la matriz de cambio en el sentido que dan los datos y se
invierte.

## Ejemplos resueltos

### Ejemplo 1 · Dos bases de ℝ³, por los dos métodos

<!-- check: U1.T09.E1 -->

Sean $B=\{(1,0,1),(1,1,0),(2,1,2)\}$ y $B'=\{(1,1,1),(0,1,1),(0,0,1)\}$, bases de $\mathbb{R}^3$.
Hallar $C_{BB'}$ y, si $[v]_B=(2,-1,1)^t$, hallar $[v]_{B'}$ y $v$.

**Método 1.** Escalonamos $(b_1'\ b_2'\ b_3'\mid b_1\ b_2\ b_3)$:

$$
\left(\begin{array}{ccc|ccc} 1&0&0&1&1&2\\1&1&0&0&1&1\\1&1&1&1&0&2 \end{array}\right)
\xrightarrow[F_3-F_1\to F_3]{F_2-F_1\to F_2}
\left(\begin{array}{ccc|ccc} 1&0&0&1&1&2\\0&1&0&-1&0&-1\\0&1&1&0&-1&0 \end{array}\right)
\xrightarrow{F_3-F_2\to F_3}
\left(\begin{array}{ccc|ccc} 1&0&0&1&1&2\\0&1&0&-1&0&-1\\0&0&1&1&-1&1 \end{array}\right).
$$

**Método 2.** $C_{BE}=\begin{pmatrix}1&1&2\\0&1&1\\1&0&2\end{pmatrix}$ y
$C_{B'E}=\begin{pmatrix}1&0&0\\1&1&0\\1&1&1\end{pmatrix}$, cuya inversa es
$C_{EB'}=\begin{pmatrix}1&0&0\\-1&1&0\\0&-1&1\end{pmatrix}$ (se verifica multiplicando). Entonces

$$
C_{BB'}=C_{EB'}\,C_{BE}=\begin{pmatrix}1&0&0\\-1&1&0\\0&-1&1\end{pmatrix}\begin{pmatrix}1&1&2\\0&1&1\\1&0&2\end{pmatrix}=\begin{pmatrix}1&1&2\\-1&0&-1\\1&-1&1\end{pmatrix}.
$$

Los dos métodos coinciden. Acá el método 1 es más corto, porque $B'$ es "triangular" y el
escalonamiento termina en dos pasos.

**El vector.**

$$
[v]_{B'}=C_{BB'}[v]_B=\begin{pmatrix}1&1&2\\-1&0&-1\\1&-1&1\end{pmatrix}\begin{pmatrix}2\\-1\\1\end{pmatrix}=\begin{pmatrix}3\\-3\\4\end{pmatrix},
\qquad v=2(1,0,1)-(1,1,0)+(2,1,2)=(3,0,4).
$$

**Comprobación.** $3(1,1,1)-3(0,1,1)+4(0,0,1)=(3,0,4)=v$. Además
$C_{B'B}=(C_{BB'})^{-1}=\begin{pmatrix}-1&-3&-1\\0&-1&-1\\1&2&1\end{pmatrix}$; su primera columna,
$[b_1']_B=(-1,0,1)^t$, dice que $(1,1,1)=-(1,0,1)+(2,1,2)$, lo cual es cierto.

:::tip[Resultado]
$C_{BB'}=\begin{pmatrix}1&1&2\\-1&0&-1\\1&-1&1\end{pmatrix}$, $[v]_{B'}=(3,-3,4)^t$, $v=(3,0,4)$.
:::

### Ejemplo 2 · Polinomios: de la base canónica a una base desplazada

<!-- check: U1.T09.E2 -->

En $P_2[\mathbb{R}]$ sean $E=\{1,x,x^2\}$ y $B=\{1,\ 1+x,\ (1+x)^2\}$. Hallar $C_{BE}$ y $C_{EB}$,
y escribir $p=2-3x+x^2$ en la base $B$.

**$C_{BE}$.** Columnas = coeficientes de cada polinomio de $B$ en $E$. Como $(1+x)^2=1+2x+x^2$,

$$
C_{BE}=\begin{pmatrix}1&1&1\\0&1&2\\0&0&1\end{pmatrix}.
$$

**$C_{EB}$.** Es la inversa. Con $(C_{BE}\mid I_3)$:

$$
\left(\begin{array}{ccc|ccc} 1&1&1&1&0&0\\0&1&2&0&1&0\\0&0&1&0&0&1 \end{array}\right)
\xrightarrow[F_1-F_3\to F_1]{F_2-2F_3\to F_2}
\left(\begin{array}{ccc|ccc} 1&1&0&1&0&-1\\0&1&0&0&1&-2\\0&0&1&0&0&1 \end{array}\right)
\xrightarrow{F_1-F_2\to F_1}
\left(\begin{array}{ccc|ccc} 1&0&0&1&-1&1\\0&1&0&0&1&-2\\0&0&1&0&0&1 \end{array}\right).
$$

$C_{EB}=\begin{pmatrix}1&-1&1\\0&1&-2\\0&0&1\end{pmatrix}$. Sus columnas dicen cómo se escriben
$1$, $x$ y $x^2$ en la base $B$: por ejemplo, la tercera dice $x^2=1-2(1+x)+(1+x)^2$.

**El polinomio.**
$[p]_B=C_{EB}[p]_E=C_{EB}\begin{pmatrix}2\\-3\\1\end{pmatrix}=\begin{pmatrix}2+3+1\\-3-2\\1\end{pmatrix}=\begin{pmatrix}6\\-5\\1\end{pmatrix}$.

**Comprobación.** $6-5(1+x)+(1+x)^2=(6-5+1)+(-5+2)x+x^2=2-3x+x^2$. Las coordenadas en $B$ son los
coeficientes del desarrollo de $p$ en potencias de $(x+1)$; en particular, la primera es
$p(-1)=2+3+1=6$.

:::tip[Resultado]
$C_{EB}=\begin{pmatrix}1&-1&1\\0&1&-2\\0&0&1\end{pmatrix}$ y $p=6-5(1+x)+(1+x)^2$, es decir,
$[p]_B=(6,-5,1)^t$.
:::

### Ejemplo 3 · Bases abstractas dadas por combinaciones

<!-- check: U1.T09.E3 -->

Sea $V$ un espacio vectorial con base $B=\{v_1,v_2,v_3\}$ y sean $w_1=v_1+v_2$, $w_2=v_2-v_3$,
$w_3=v_1+2v_3$. Probar que $B'=\{w_1,w_2,w_3\}$ es base de $V$, hallar $C_{BB'}$ y las
coordenadas en $B'$ de $u=2v_1-v_2+v_3$.

Acá no hay componentes: solo sabemos cómo se escriben los $w_j$ en la base $B$.

**$C_{B'B}$ y que $B'$ es base.** Los datos dan directamente $[w_1]_B=(1,1,0)^t$,
$[w_2]_B=(0,1,-1)^t$, $[w_3]_B=(1,0,2)^t$. Si $B'$ es base, entonces

$$
C_{B'B}=\begin{pmatrix}1&0&1\\1&1&0\\0&-1&2\end{pmatrix},\qquad \det C_{B'B}=1\cdot(2-0)-0+1\cdot(-1-0)=1\neq0 .
$$

Las tres columnas son independientes en $K^3$; por el teorema de independencia en coordenadas, los
$w_j$ son independientes en $V$, y como $\dim V=3$, $B'$ es base.

**$C_{BB'}$ por incógnitas vectoriales.** De $w_2=v_2-v_3$ y de
$w_3=v_1+2v_3=(w_1-v_2)+2v_3$ obtenemos $v_2-2v_3=w_1-w_3$. Restando esta igualdad de
$v_2-v_3=w_2$: $v_3=-w_1+w_2+w_3$. Luego $v_2=w_2+v_3=-w_1+2w_2+w_3$ y
$v_1=w_1-v_2=2w_1-2w_2-w_3$. Las columnas de $C_{BB'}$ son esas coordenadas:

$$
C_{BB'}=\begin{pmatrix}2&-1&-1\\-2&2&1\\-1&1&1\end{pmatrix}.
$$

El mismo resultado sale invirtiendo $C_{B'B}$; las dos vías se controlan mutuamente.

**El vector $u$.**
$[u]_{B'}=C_{BB'}\begin{pmatrix}2\\-1\\1\end{pmatrix}=\begin{pmatrix}4+1-1\\-4-2+1\\-2-1+1\end{pmatrix}=\begin{pmatrix}4\\-5\\-2\end{pmatrix}$.

**Comprobación.** $4w_1-5w_2-2w_3=4(v_1+v_2)-5(v_2-v_3)-2(v_1+2v_3)=2v_1-v_2+v_3=u$. Y
$C_{B'B}\,C_{BB'}=I_3$.

:::tip[Resultado]
$C_{BB'}=\begin{pmatrix}2&-1&-1\\-2&2&1\\-1&1&1\end{pmatrix}$ y $[u]_{B'}=(4,-5,-2)^t$.
:::

### Ejemplo 4 · Recuperar una base a partir de la matriz de cambio

<!-- check: U1.T09.E4 -->

En $\mathbb{R}^2$ sea $B=\{b_1,b_2\}$ con $b_1=(2,-1)$, $b_2=(0,2)$, y sea $B'=\{w_1,w_2\}$ una base
desconocida tal que

$$
C_{BB'}=\begin{pmatrix}0&1\\-1&1\end{pmatrix}.
$$

Hallar $B'$ y las coordenadas en $B'$ de $v=(2,3)$.

**Lectura directa por columnas.** La primera columna dice $b_1=0\,w_1-1\,w_2$, así que
$w_2=-b_1=(-2,1)$. La segunda dice $b_2=w_1+w_2$, así que $w_1=b_2-w_2=(0,2)-(-2,1)=(2,1)$.

**Con la inversa.** $C_{B'B}=(C_{BB'})^{-1}=\begin{pmatrix}1&-1\\1&0\end{pmatrix}$ (el determinante de
$C_{BB'}$ es $1$). Sus columnas son $[w_1]_B=(1,1)^t$ y $[w_2]_B=(-1,0)^t$:
$w_1=b_1+b_2=(2,1)$ y $w_2=-b_1=(-2,1)$. Este camino conviene cuando la base es grande, porque
evita despejar a mano.

**Coordenadas de $v$.** $v=(2,3)=1\,b_1+2\,b_2$, porque $(2,-1)+(0,4)=(2,3)$. Entonces

$$
[v]_{B'}=C_{BB'}[v]_B=\begin{pmatrix}0&1\\-1&1\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=\begin{pmatrix}2\\1\end{pmatrix}.
$$

Es la situación de la figura.

**Comprobación.** $2w_1+w_2=(4,2)+(-2,1)=(2,3)$. Y $[b_1]_{B'}=(0,-1)^t$ porque $-w_2=(2,-1)=b_1$.

:::tip[Resultado]
$B'=\{(2,1),(-2,1)\}$ y $[v]_{B'}=(2,1)^t$.
:::

### Ejemplo 5 · Un plano en una base adaptada

<!-- check: U1.T09.E5 -->

Sea $\pi=\{(x,y,z)\in\mathbb{R}^3: x-2y+z=0\}$. Elegir una base $B$ de $\mathbb{R}^3$ cuyos dos
primeros vectores estén en $\pi$ y escribir la ecuación de $\pi$ y de la recta
$L=\operatorname{gen}\{(2,1,0)\}$ en coordenadas respecto de $B$.

**La base.** $u_1=(2,1,0)$ y $u_2=(1,1,1)$ están en $\pi$ ($2-2+0=0$, $1-2+1=0$) y no son
proporcionales; agregamos $u_3=(0,0,1)\notin\pi$ ($0-0+1\neq0$). Por la extensión de un
independiente con un vector fuera de su generado, $B=\{u_1,u_2,u_3\}$ es base de $\mathbb{R}^3$.

**Matriz de cambio.** $C_{BE}=\begin{pmatrix}2&1&0\\1&1&0\\0&1&1\end{pmatrix}$, con determinante
$1$, y

$$
C_{EB}=(C_{BE})^{-1}=\begin{pmatrix}1&-1&0\\-1&2&0\\1&-2&1\end{pmatrix}.
$$

Si $[v]_B=(y_1,y_2,y_3)^t$ y $v=(x,y,z)$, entonces $[v]_B=C_{EB}[v]_E$:

$$
y_1=x-y,\qquad y_2=-x+2y,\qquad y_3=x-2y+z .
$$

**Ecuaciones en la base adaptada.** $v\in\pi$ si y solo si $x-2y+z=0$, es decir,
$\pi=\{v: y_3=0\}$: en la base $B$ el plano es "el plano de las dos primeras coordenadas". Y
$v\in L$ si y solo si $v=tu_1$, es decir, $[v]_B=(t,0,0)^t$: $L=\{v: y_2=0,\ y_3=0\}$. Esto también
se ve sin cuentas: $v=y_1u_1+y_2u_2+y_3u_3$ está en $\pi=\operatorname{gen}\{u_1,u_2\}$ exactamente
cuando $y_3=0$.

**Comprobación.** $v=(3,1,-1)\in\pi$ ($3-2-1=0$) tiene $[v]_B=(2,-1,0)^t$, y
$2u_1-u_2=(4,2,0)-(1,1,1)=(3,1,-1)$. Además $C_{BE}\,C_{EB}=I_3$.

:::tip[Resultado]
En la base $B=\{(2,1,0),(1,1,1),(0,0,1)\}$: $\pi$ es $y_3=0$ y $L$ es $y_2=y_3=0$.
:::

Este es el uso típico de un cambio de base: elegir la base para que el objeto que estudiamos tenga
la descripción más simple posible. En la Unidad 2 la misma idea simplifica la matriz de una
transformación lineal ([cambio de base](/algebra-ii/unidad-2/teoria/cambio-de-base/)) y en la
Unidad 3 lleva a la diagonalización.

## Interpretación

- **Geométrica.** $C_{BB'}$ no mueve vectores: traduce la "dirección" de un vector escrita en la
  grilla de $B$ a la grilla de $B'$.
- **Algebraica.** La columna $j$ de $C_{BB'}$ responde a "¿cómo se escribe $b_j$ con los vectores de
  $B'$?". Toda la información de las dos bases relativa una a la otra está en esa matriz.
- **Computacional.** Pasar por la base canónica es un patrón general: para traducir entre dos
  formatos, se pasa por un formato intermedio común. Con $k$ bases alcanza con conocer $k$ matrices
  $C_{B_iE}$ en lugar de $k(k-1)$ matrices de cambio.

## Errores frecuentes

:::caution[Errores frecuentes]
- **Poner en columnas los vectores de la base equivocada.** $C_{BB'}$ tiene en columnas las
  coordenadas de los vectores de $B$ (la de partida) **en** $B'$. En el ejemplo 4, armar la matriz
  con $[w_j]_B$ produce $C_{B'B}$, que es la inversa.
- **Invertir el orden en la composición.** $C_{BB''}=C_{B'B''}C_{BB'}$, no $C_{BB'}C_{B'B''}$; el
  producto de matrices no es conmutativo.
- **Creer que $C_{BB'}$ actúa sobre vectores.** Multiplica columnas de coordenadas. En el ejemplo 2,
  $C_{EB}$ se multiplica por $(2,-3,1)^t$, no por "el polinomio".
- **Confundir $C_{BE}$ con $C_{EB}$ en $K^n$.** La que se escribe sin cuentas es $C_{BE}$
  (columnas = vectores de $B$). La otra requiere invertir.
- **Mezclar notaciones.** La matriz que Poole llama $P_{B'\leftarrow B}$ es $C_{BB'}$, no $C_{B'B}$.
- **Pensar que $C_{BB}$ depende de $B$.** Para cualquier base, $C_{BB}=I_n$; en particular
  $C_{EE}=C_{BB}$.
:::

## Autoevaluación

1. Si $C_{BB'}=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, ¿cuánto vale $C_{B'B}$?
2. Con $B=\{b_1,b_2\}$, sea $B_1=\{b_2,b_1\}$. ¿Qué relación hay entre $C_{BB'}$ y $C_{B_1B'}$?
3. Si $C_{BE}$ es la matriz de cambio a la canónica de $\mathbb{R}^3$ y $[v]_B=(1,0,0)^t$, ¿qué es
   $v$?

<details>
<summary>Respuestas</summary>

1. $C_{B'B}=\begin{pmatrix}1&-2\\0&1\end{pmatrix}$.
2. $C_{B_1B'}$ es $C_{BB'}$ con las columnas intercambiadas.
3. $v=b_1$, la primera columna de $C_{BE}$.

</details>

## Resumen

:::tip[En resumen]
- $C_{BB'}=([b_1]_{B'}\mid\cdots\mid[b_n]_{B'})$ y $C_{BB'}[v]_B=[v]_{B'}$; es la única matriz con
  esa propiedad.
- $C_{BB}=I$, $C_{BB''}=C_{B'B''}C_{BB'}$ y $(C_{BB'})^{-1}=C_{B'B}$.
- Cálculo: $(b_1'\cdots b_n'\mid b_1\cdots b_n)\to(I\mid C_{BB'})$, o bien
  $C_{BB'}=(C_{B'E})^{-1}C_{BE}$, o despejando vectores en bases abstractas.
- Una base desconocida se recupera leyendo las columnas de $C_{BB'}$ o de su inversa.
- Una base adaptada a un subespacio lo describe con ecuaciones del tipo "últimas coordenadas
  nulas".
- Poole y Lay: $P_{B'\leftarrow B}=C_{BB'}$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 6.3, "Cambio de base", p. 481.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: cambio de base.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed., sección 4.3, "Cambio de base",
  p. 156.
- Lecciones relacionadas: [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/) (anterior),
  [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/) (siguiente),
  [cambio de base](/algebra-ii/unidad-2/teoria/cambio-de-base/) para transformaciones lineales, y
  el repaso de [rectas y planos](/algebra-ii/repaso/rectas-y-planos/).
