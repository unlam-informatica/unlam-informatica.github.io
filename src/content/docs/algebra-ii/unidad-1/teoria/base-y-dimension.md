---
title: Base y dimensión
description: Bases como generadores independientes, invariancia de la cantidad de vectores, dimensión, extensión y extracción de bases, y conteo de elementos en espacios sobre ℤ₂.
slug: algebra-ii/unidad-1/teoria/base-y-dimension
sidebar:
  order: 7
  label: 1.7 Base y dimensión
---

## Para qué sirve

Un generador permite escribir todos los vectores de un subespacio, pero puede tener vectores de más.
Un conjunto linealmente independiente no tiene redundancias, pero puede quedarse corto. Una
**base** es el punto justo entre las dos cosas: alcanza para generar y no sobra nada. La cantidad
de vectores de una base mide el "tamaño" del espacio, su **dimensión**, y ese número resulta ser
el mismo para cualquier base.

La dimensión tiene una lectura muy concreta sobre $\mathbb{Z}_2$: un subespacio de dimensión $k$
tiene exactamente $2^k$ elementos. En un código lineal eso es la cantidad de mensajes distintos que
se pueden transmitir con $k$ bits de información
(ver [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/)).

Usamos lo visto en [combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/),
[independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/) y
[subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/). Todos los
espacios de la materia son **finitamente generados**: tienen un generador con una cantidad finita
de vectores.

## Base

:::note[Definición]
Sea $V$ un espacio vectorial sobre $K$. Un conjunto **ordenado** $B=\{v_1,\dots,v_n\}\subseteq V$ es
una **base** de $V$ si

1. $B$ genera $V$: $\operatorname{gen}\{v_1,\dots,v_n\}=V$, y
2. $B$ es linealmente independiente.

La misma definición vale para un subespacio $S$, que es un espacio vectorial en sí mismo.
:::

Pedimos bases ordenadas porque en la lección de
[coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/) el orden determina qué número va en cada
posición. Como conjuntos, $\{v_1,v_2\}$ y $\{v_2,v_1\}$ son iguales; como bases, son distintas.

Bases canónicas que usamos todo el tiempo:

- $E=\{e_1,\dots,e_n\}$ en $K^n$, con $e_i$ el vector con un $1$ en la posición $i$ y ceros en las
  demás.
- $E=\{1,x,x^2\}$ en $P_2[\mathbb{R}]$, en ese orden; en general, $\{1,x,\dots,x^n\}$ en
  $P_n[\mathbb{R}]$.
- $E=\{E_{11},E_{12},E_{21},E_{22}\}$ en $\mathbb{R}^{2\times2}$, donde $E_{ij}$ tiene un $1$ en la
  posición $(i,j)$ y ceros en el resto.

En cada caso, generar es inmediato (por ejemplo,
$\begin{pmatrix}a&b\\c&d\end{pmatrix}=aE_{11}+bE_{12}+cE_{21}+dE_{22}$) y la independencia también:
una combinación nula obliga a que cada entrada, coeficiente o componente sea cero.

**El espacio nulo.** El espacio $\{0\}$ no tiene ningún conjunto linealmente independiente no vacío
(el conjunto $\{0\}$ es dependiente). Por convención, su base es el conjunto vacío $\varnothing$ y
$\operatorname{gen}\varnothing=\{0\}$.

## Todas las bases tienen la misma cantidad de vectores

El resultado clave es un lema sobre cantidades: en un espacio generado por $m$ vectores no caben más
de $m$ vectores independientes.

:::note[Lema]
Si $V=\operatorname{gen}\{w_1,\dots,w_m\}$ y $u_1,\dots,u_p\in V$ con $p>m$, entonces
$\{u_1,\dots,u_p\}$ es linealmente dependiente.
:::

**Demostración.** Como cada $u_j$ está en $V$, existen escalares $a_{ij}$ con

$$
u_j=a_{1j}w_1+a_{2j}w_2+\dots+a_{mj}w_m\qquad(j=1,\dots,p).
$$

Buscamos $c_1,\dots,c_p$ no todos nulos con $c_1u_1+\dots+c_pu_p=0$. Reemplazando y agrupando según
los $w_i$,

$$
\sum_{j=1}^{p}c_ju_j=\sum_{i=1}^{m}\Big(\sum_{j=1}^{p}a_{ij}c_j\Big)w_i .
$$

Basta entonces que $c=(c_1,\dots,c_p)$ resuelva el sistema homogéneo $\sum_{j}a_{ij}c_j=0$,
$i=1,\dots,m$, cuya matriz $(a_{ij})$ es de $m\times p$. Su rango es a lo sumo $m$ (no hay más
pivotes que filas), así que por el teorema rango–nulidad su espacio nulo tiene dimensión al menos
$p-m>0$: existe una solución $c\neq0$. Con ella, $\sum_jc_ju_j=0$ y los $u_j$ son dependientes.
$\blacksquare$

:::note[Teorema (igual cardinal de las bases)]
Si $B=\{v_1,\dots,v_n\}$ y $B'=\{v_1',\dots,v_{n'}'\}$ son bases de $V$, entonces $n=n'$.
:::

**Demostración.** $B$ genera $V$ y $B'$ es independiente: por el lema, $n'\leq n$ (si fuera
$n'>n$, $B'$ sería dependiente). Intercambiando los papeles, $B'$ genera y $B$ es independiente, así
que $n\leq n'$. $\blacksquare$

:::note[Definición]
La **dimensión** de un espacio vectorial $V\neq\{0\}$ finitamente generado es la cantidad de
vectores de cualquiera de sus bases; se nota $\dim(V)$. Además, $\dim(\{0\})=0$.
:::

| Espacio | Dimensión |
|---|---|
| $K^n$ (incluye $\mathbb{R}^n$ y $\mathbb{Z}_2^n$) | $n$ |
| $\mathbb{R}^{m\times n}$ | $mn$ |
| $P_n[\mathbb{R}]$ | $n+1$ |
| $\operatorname{fil}(A)$, $\operatorname{col}(A)$ | $\operatorname{rango}(A)$ |
| $\operatorname{nul}(A)$, con $A$ de $n$ columnas | $n-\operatorname{rango}(A)$ |

## Propiedades de la dimensión

Recordemos un hecho de [independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/)
que usamos varias veces.

:::note[Lema]
Si $\{v_1,\dots,v_k\}$ es linealmente independiente y $v\notin\operatorname{gen}\{v_1,\dots,v_k\}$,
entonces $\{v_1,\dots,v_k,v\}$ es linealmente independiente.
:::

**Demostración.** Sea $c\,v+c_1v_1+\dots+c_kv_k=0$. Si fuera $c\neq0$, despejando
$v=-c^{-1}(c_1v_1+\dots+c_kv_k)\in\operatorname{gen}\{v_1,\dots,v_k\}$, absurdo. Luego $c=0$, queda
$c_1v_1+\dots+c_kv_k=0$ y, por independencia, todos los $c_i$ son nulos. $\blacksquare$

:::note[Teorema]
Sea $V$ con $\dim(V)=n\geq1$.

1. Todo conjunto linealmente independiente de $V$ tiene a lo sumo $n$ vectores, y todo generador
   de $V$ tiene al menos $n$.
2. Si $v_1,\dots,v_n$ son $n$ vectores linealmente independientes de $V$, forman una base.
3. Si $v_1,\dots,v_n$ son $n$ vectores que generan $V$, forman una base.
4. Si $S$ es un subespacio de $V$, entonces $\dim(S)\leq n$. Si además $S\subseteq W$ son subespacios
   con $\dim(S)=\dim(W)$, entonces $S=W$.
:::

**Demostración.**

1. Una base de $V$ tiene $n$ vectores y genera; por el lema de las cantidades, más de $n$ vectores
   son dependientes. Si un generador tuviera $m<n$ vectores, la base (independiente, con $n>m$
   vectores) sería dependiente por el mismo lema, absurdo.
2. Si no generaran $V$, habría $v\in V$ fuera de $\operatorname{gen}\{v_1,\dots,v_n\}$ y, por el
   lema anterior, $\{v_1,\dots,v_n,v\}$ sería independiente con $n+1$ vectores, contra el punto 1.
3. Si fueran dependientes, alguno sería combinación de los otros y podríamos quitarlo sin perder la
   generación (ver la extracción más abajo), obteniendo un generador de $n-1$ vectores, contra el
   punto 1.
4. Una base de $S$ es independiente en $V$, así que tiene a lo sumo $n$ vectores. Si $S\subseteq W$ y
   $\dim(S)=\dim(W)=k$, una base de $S$ consta de $k$ vectores independientes de $W$; por el punto 2
   aplicado a $W$, es base de $W$, y entonces $W=\operatorname{gen}(\text{esa base})=S$. (Si $k=0$,
   ambos son $\{0\}$.) $\blacksquare$

El punto 2 es muy práctico: para probar que $n$ vectores forman una base de un espacio de dimensión
$n$ alcanza con probar **una** de las dos condiciones.

## Extraer una base de un generador

:::note[Teorema]
Si $\{w_1,\dots,w_m\}$ genera $V\neq\{0\}$, algún subconjunto suyo es base de $V$. En $K^n$, una
base se obtiene poniendo los $w_j$ como **columnas** de una matriz, escalonando y quedándose con los
$w_j$ que ocupan las columnas pivote.
:::

**Demostración.** Si el generador es independiente, ya es base. Si no, alguno de sus vectores es
combinación lineal de los demás; al quitarlo, el generado no cambia (toda combinación que lo usaba
se reescribe con los restantes). Repetimos mientras haya dependencia; como el conjunto es finito,
el proceso termina en un conjunto independiente que sigue generando $V$. Para el método matricial,
$V=\operatorname{col}(A)$ con $A=(w_1\mid\cdots\mid w_m)$, y las columnas pivote de la matriz
original forman una base de $\operatorname{col}(A)$, como se probó en
[subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/). $\blacksquare$

## Extender un conjunto independiente a una base

:::note[Teorema (extensión a una base)]
Si $\dim(V)=n$ y $\{v_1,\dots,v_k\}\subseteq V$ es linealmente independiente, existen
$v_{k+1},\dots,v_n\in V$ tales que $\{v_1,\dots,v_n\}$ es base de $V$.
:::

**Demostración.** Si $\{v_1,\dots,v_k\}$ genera $V$, es base (y $k=n$). Si no, elegimos
$v_{k+1}\in V$ fuera de su generado; por el lema, $\{v_1,\dots,v_{k+1}\}$ sigue siendo independiente.
Repetimos. Como en $V$ no hay conjuntos independientes de más de $n$ vectores, el proceso se detiene
a lo sumo al llegar a $n$ vectores, y se detiene solo cuando el conjunto genera $V$. $\blacksquare$

La prueba no dice cómo elegir los vectores. En $K^n$ hay un método directo.

:::note[Método por escalonamiento]
Sea $\{v_1,\dots,v_k\}\subseteq K^n$ independiente. Ponemos los $v_i$ como **filas** de una matriz
y la escalonamos; quedan $k$ filas no nulas con pivotes en columnas $j_1<\dots<j_k$. Los vectores
canónicos $e_j$ con $j\notin\{j_1,\dots,j_k\}$ completan una base:
$\{v_1,\dots,v_k\}\cup\{e_j: j\text{ no pivote}\}$.
:::

**Demostración.** Sean $g_1,\dots,g_k$ las filas no nulas de la escalonada. Cada $g_i$ tiene su
primer elemento no nulo en la columna $j_i$, y cada $e_j$ agregado tiene su único elemento no nulo
en la columna $j$. Los $n$ vectores $g_1,\dots,g_k$ y los $e_j$ tienen entonces sus primeros
elementos no nulos en $n$ columnas distintas; ordenados según esa columna, forman una matriz
escalonada $n\times n$ con $n$ pivotes, así que son independientes y, por el punto 2 de las
propiedades, generan $K^n$. Como escalonar no cambia el espacio fila,
$\operatorname{gen}\{g_1,\dots,g_k\}=\operatorname{gen}\{v_1,\dots,v_k\}$, y entonces
$\{v_1,\dots,v_k\}\cup\{e_j\}$ también genera $K^n$. Son $n$ vectores que generan un espacio de
dimensión $n$: forman una base. $\blacksquare$

Otra forma: escalonar la matriz de columnas $(v_1\mid\cdots\mid v_k\mid e_1\mid\cdots\mid e_n)$ y
quedarse con las columnas pivote. Las primeras $k$ siempre son pivote (los $v_i$ son
independientes) y el resto las aportan canónicos. Los dos métodos pueden dar bases distintas; las
dos son correctas, porque la extensión no es única.

En espacios de polinomios o de matrices se aplica lo mismo trabajando con las coordenadas en la base
canónica, como se justifica en [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/).

## Espacios sobre ℤ₂: dimensión y cantidad de elementos

:::note[Teorema]
Si $V$ es un espacio vectorial sobre $\mathbb{Z}_2$ con $\dim(V)=k$, entonces $V$ tiene exactamente
$2^k$ elementos.
:::

**Demostración.** Sea $B=\{v_1,\dots,v_k\}$ una base. Como $B$ genera, todo vector de $V$ es de la
forma $a_1v_1+\dots+a_kv_k$ con cada $a_i\in\{0,1\}$; hay $2^k$ elecciones de $(a_1,\dots,a_k)$. Falta
ver que elecciones distintas dan vectores distintos: si
$a_1v_1+\dots+a_kv_k=b_1v_1+\dots+b_kv_k$, entonces $(a_1-b_1)v_1+\dots+(a_k-b_k)v_k=0$ y, por
independencia, $a_i=b_i$ para todo $i$. Así, la correspondencia
$(a_1,\dots,a_k)\mapsto a_1v_1+\dots+a_kv_k$ entre $\mathbb{Z}_2^k$ y $V$ es biyectiva y
$|V|=|\mathbb{Z}_2^k|=2^k$. (Si $k=0$, $V=\{0\}$ tiene $2^0=1$ elemento.) $\blacksquare$

Consecuencias: un subespacio de $\mathbb{Z}_2^n$ tiene $1,2,4,8,\dots$ elementos (nunca 3, 5 o 6),
y $\mathbb{Z}_2^n$ tiene $2^n$. La correspondencia de la demostración es la función coordenadas, que
estudiamos en la [lección siguiente](/algebra-ii/unidad-1/teoria/coordenadas/).

## Ejemplos resueltos

### Ejemplo 1 · Extender dos vectores a una base de ℝ⁴

<!-- check: U1.T07.E1 -->

Completar $\{v_1,v_2\}$, con $v_1=(1,2,0,1)$ y $v_2=(2,4,1,3)$, a una base de $\mathbb{R}^4$.

**Independencia.** $v_1$ y $v_2$ no son proporcionales (la tercera componente de $v_1$ es $0$ y la
de $v_2$ no), así que $\{v_1,v_2\}$ es independiente.

**Método por filas.**

$$
\begin{pmatrix}1&2&0&1\\2&4&1&3\end{pmatrix}\xrightarrow{F_2-2F_1\to F_2}
\begin{pmatrix}1&2&0&1\\0&0&1&1\end{pmatrix}.
$$

Los pivotes están en las columnas 1 y 3; faltan las columnas 2 y 4. Agregamos $e_2$ y $e_4$:

$$
B=\{(1,2,0,1),\ (2,4,1,3),\ (0,1,0,0),\ (0,0,0,1)\}.
$$

**Método por columnas.** Escalonamos $(v_1\mid v_2\mid e_1\mid e_2\mid e_3\mid e_4)$:

$$
\begin{pmatrix}1&2&1&0&0&0\\2&4&0&1&0&0\\0&1&0&0&1&0\\1&3&0&0&0&1\end{pmatrix}
\xrightarrow[F_4-F_1\to F_4]{F_2-2F_1\to F_2}
\begin{pmatrix}1&2&1&0&0&0\\0&0&-2&1&0&0\\0&1&0&0&1&0\\0&1&-1&0&0&1\end{pmatrix}
\xrightarrow{F_2\leftrightarrow F_3}
\begin{pmatrix}1&2&1&0&0&0\\0&1&0&0&1&0\\0&0&-2&1&0&0\\0&1&-1&0&0&1\end{pmatrix}
$$

$$
\xrightarrow{F_4-F_2\to F_4}
\begin{pmatrix}1&2&1&0&0&0\\0&1&0&0&1&0\\0&0&-2&1&0&0\\0&0&-1&0&-1&1\end{pmatrix}
\xrightarrow{2F_4-F_3\to F_4}
\begin{pmatrix}1&2&1&0&0&0\\0&1&0&0&1&0\\0&0&-2&1&0&0\\0&0&0&-1&-2&2\end{pmatrix}.
$$

Columnas pivote: 1, 2, 3 y 4, que corresponden a $v_1,v_2,e_1,e_2$. Otra base es
$B_2=\{v_1,v_2,e_1,e_2\}$.

**Comprobación.** Para que cuatro vectores de $\mathbb{R}^4$ sean base basta que sean independientes
(propiedad 2), es decir, que la matriz que forman tenga determinante no nulo:

$$
\det\begin{pmatrix}1&2&0&1\\2&4&1&3\\0&1&0&0\\0&0&0&1\end{pmatrix}=-1,\qquad
\det\begin{pmatrix}1&2&0&1\\2&4&1&3\\1&0&0&0\\0&1&0&0\end{pmatrix}=-1 .
$$

:::tip[Resultado]
$\{v_1,v_2,e_2,e_4\}$ y $\{v_1,v_2,e_1,e_2\}$ son dos extensiones válidas a bases de $\mathbb{R}^4$.
:::

### Ejemplo 2 · Extraer una base de un generador

<!-- check: U1.T07.E2 -->

Sea $S=\operatorname{gen}\{w_1,\dots,w_5\}\subseteq\mathbb{R}^4$ con $w_1=(1,-1,0,2)$,
$w_2=(2,-2,0,4)$, $w_3=(0,1,1,1)$, $w_4=(1,0,1,3)$ y $w_5=(1,1,1,0)$. Hallar una base de $S$
formada por vectores del generador y su dimensión.

**Escalonamiento por columnas.**

$$
\begin{pmatrix}1&2&0&1&1\\-1&-2&1&0&1\\0&0&1&1&1\\2&4&1&3&0\end{pmatrix}
\xrightarrow[F_4-2F_1\to F_4]{F_2+F_1\to F_2}
\begin{pmatrix}1&2&0&1&1\\0&0&1&1&2\\0&0&1&1&1\\0&0&1&1&-2\end{pmatrix}
\xrightarrow[F_4-F_2\to F_4]{F_3-F_2\to F_3}
\begin{pmatrix}1&2&0&1&1\\0&0&1&1&2\\0&0&0&0&-1\\0&0&0&0&-4\end{pmatrix}
\xrightarrow{F_4-4F_3\to F_4}
\begin{pmatrix}1&2&0&1&1\\0&0&1&1&2\\0&0&0&0&-1\\0&0&0&0&0\end{pmatrix}.
$$

Columnas pivote: 1, 3 y 5. Una base es $B_S=\{w_1,w_3,w_5\}$ y $\dim(S)=3$.

**Qué pasó con los otros.** Las columnas no pivote revelan las dependencias: $w_2=2w_1$ y
$w_4=w_1+w_3$ (en efecto, $(1,-1,0,2)+(0,1,1,1)=(1,0,1,3)$).

**Comprobación.** Como $\dim(S)=3$, $S$ debería describirse con una sola ecuación
$ax_1+bx_2+cx_3+dx_4=0$. Imponiendo que la cumplan $w_1$, $w_3$ y $w_5$ queda el sistema
$a-b+2d=0$, $b+c+d=0$, $a+b+c=0$, cuyas soluciones son los múltiplos de $(a,b,c,d)=(1,3,-4,1)$.
Los cinco vectores cumplen $x_1+3x_2-4x_3+x_4=0$; por ejemplo, para $w_4$, $1+0-4+3=0$. Así,
$S=\{x\in\mathbb{R}^4: x_1+3x_2-4x_3+x_4=0\}$, que tiene dimensión $4-1=3$ por rango–nulidad.

:::tip[Resultado]
$B_S=\{(1,-1,0,2),(0,1,1,1),(1,1,1,0)\}$, $\dim(S)=3$.
:::

### Ejemplo 3 · Matrices simétricas y de traza nula

<!-- check: U1.T07.E3 -->

En $\mathbb{R}^{2\times2}$ consideramos
$\mathcal S=\{A: A^t=A\}$ (simétricas), $\mathcal T=\{A: \operatorname{tr}(A)=0\}$ (traza nula) y
$\mathcal S\cap\mathcal T$. Hallar una base y la dimensión de cada uno, y extender la base de
$\mathcal S\cap\mathcal T$ a una base de $\mathcal S$.

**Simétricas.** $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ es simétrica si y solo si $b=c$:

$$
A=\begin{pmatrix}a&b\\b&d\end{pmatrix}=a\begin{pmatrix}1&0\\0&0\end{pmatrix}+b\begin{pmatrix}0&1\\1&0\end{pmatrix}+d\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$

Las tres matrices generan $\mathcal S$ y son independientes (una combinación nula tiene $a=b=d=0$
leyendo las posiciones $(1,1)$, $(1,2)$ y $(2,2)$). $B_{\mathcal S}=\{E_{11},\ E_{12}+E_{21},\ E_{22}\}$,
$\dim\mathcal S=3$.

**Traza nula.** $\operatorname{tr}(A)=a+d=0$ si y solo si $d=-a$:

$$
A=\begin{pmatrix}a&b\\c&-a\end{pmatrix}=a\begin{pmatrix}1&0\\0&-1\end{pmatrix}+b\begin{pmatrix}0&1\\0&0\end{pmatrix}+c\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$

$B_{\mathcal T}=\{E_{11}-E_{22},\ E_{12},\ E_{21}\}$, $\dim\mathcal T=3$.

**Intersección.** $b=c$ y $d=-a$: $A=a(E_{11}-E_{22})+b(E_{12}+E_{21})$, con
$B_{\mathcal S\cap\mathcal T}=\{E_{11}-E_{22},\ E_{12}+E_{21}\}$ y dimensión 2.

**Extensión.** $E_{11}$ es simétrica pero tiene traza $1$, así que
$E_{11}\notin\operatorname{gen}(B_{\mathcal S\cap\mathcal T})\subseteq\mathcal T$. Por el lema,
$\{E_{11}-E_{22},\ E_{12}+E_{21},\ E_{11}\}$ es independiente; son 3 vectores en $\mathcal S$, que
tiene dimensión 3: es base de $\mathcal S$.

**Comprobación.** Leyendo cada matriz como la cuaterna $(a,b,c,d)$ de sus entradas, la base extendida
da $(1,0,0,-1)$, $(0,1,1,0)$, $(1,0,0,0)$, que tienen rango 3. Las tres matrices son simétricas,
y $E_{11}-E_{22}$ y $E_{12}+E_{21}$ tienen traza $0$, como corresponde a la intersección.

:::tip[Resultado]
$\dim\mathcal S=3$, $\dim\mathcal T=3$, $\dim(\mathcal S\cap\mathcal T)=2$; una base de $\mathcal S$
que extiende la de la intersección es $\{E_{11}-E_{22},\ E_{12}+E_{21},\ E_{11}\}$.
:::

### Ejemplo 4 · Un subespacio de polinomios

<!-- check: U1.T07.E4 -->

Sea $W=\{p\in P_2[\mathbb{R}]: p(1)=0\}$. Hallar una base y la dimensión de $W$, escribir
$q=1+x-2x^2$ como combinación de esa base y extenderla a una base de $P_2[\mathbb{R}]$.

**Base.** Con $p=a+bx+cx^2$, la condición es $a+b+c=0$, o sea $a=-b-c$:

$$
p=(-b-c)+bx+cx^2=b(x-1)+c(x^2-1).
$$

Los polinomios $x-1$ y $x^2-1$ generan $W$. Son independientes: si $\beta(x-1)+\gamma(x^2-1)=0$,
el coeficiente de $x^2$ da $\gamma=0$ y el de $x$ da $\beta=0$. Base $B_W=\{x-1,\ x^2-1\}$,
$\dim W=2$.

**El polinomio $q$.** $q(1)=1+1-2=0$, así que $q\in W$. Con $b=1$ y $c=-2$:
$q=(x-1)-2(x^2-1)$.

**Extensión.** El polinomio constante $1$ no está en $W$ porque vale $1$ en $x=1$. Por el lema,
$\{x-1,\ x^2-1,\ 1\}$ es independiente y, como $\dim P_2[\mathbb{R}]=3$, es una base de
$P_2[\mathbb{R}]$.

**Comprobación.** $(x-1)-2(x^2-1)=x-1-2x^2+2=1+x-2x^2$. En la base canónica $\{1,x,x^2\}$ los tres
polinomios tienen coeficientes $(-1,1,0)$, $(-1,0,1)$ y $(1,0,0)$, que forman una matriz de
determinante $1\neq0$.

:::tip[Resultado]
$B_W=\{x-1,\ x^2-1\}$, $\dim W=2$; $q=(x-1)-2(x^2-1)$; $\{x-1,\ x^2-1,\ 1\}$ es base de
$P_2[\mathbb{R}]$.
:::

### Ejemplo 5 · Un subespacio de ℤ₂⁵ y sus ocho elementos

<!-- check: U1.T07.E5 -->

Sea $S=\{x\in\mathbb{Z}_2^5:\ x_1+x_2+x_4=0,\ x_2+x_3+x_5=0\}$. Hallar una base, la dimensión y la
lista completa de elementos de $S$.

**Base.** En $\mathbb{Z}_2$ restar es sumar, así que las ecuaciones equivalen a $x_4=x_1+x_2$ y
$x_5=x_2+x_3$, con $x_1,x_2,x_3$ libres:

$$
x=(x_1,x_2,x_3,x_1+x_2,x_2+x_3)=x_1(1,0,0,1,0)+x_2(0,1,0,1,1)+x_3(0,0,1,0,1).
$$

Los tres vectores generan $S$ y son independientes (basta mirar las tres primeras componentes). Base
$B_S=\{(1,0,0,1,0),(0,1,0,1,1),(0,0,1,0,1)\}$, $\dim S=3$. Por rango–nulidad: la matriz de
coeficientes $\begin{pmatrix}1&1&0&1&0\\0&1&1&0&1\end{pmatrix}$ tiene rango 2 y $5-2=3$.

**Elementos.** Por el teorema de conteo, $S$ tiene $2^3=8$ elementos, uno por cada
$(x_1,x_2,x_3)\in\mathbb{Z}_2^3$:

| $(x_1,x_2,x_3)$ | elemento de $S$ | $(x_1,x_2,x_3)$ | elemento de $S$ |
|---|---|---|---|
| $(0,0,0)$ | $(0,0,0,0,0)$ | $(1,1,0)$ | $(1,1,0,0,1)$ |
| $(1,0,0)$ | $(1,0,0,1,0)$ | $(1,0,1)$ | $(1,0,1,1,1)$ |
| $(0,1,0)$ | $(0,1,0,1,1)$ | $(0,1,1)$ | $(0,1,1,1,0)$ |
| $(0,0,1)$ | $(0,0,1,0,1)$ | $(1,1,1)$ | $(1,1,1,0,0)$ |

**Comprobación.** Cada fila cumple las dos ecuaciones; por ejemplo, $(1,1,1,0,0)$:
$1+1+0=0$ y $1+1+0=0$. Los ocho vectores son distintos, como predice el teorema de conteo.

:::tip[Resultado]
$\dim S=3$ y $S$ tiene exactamente $8$ elementos, listados en la tabla.
:::

## Interpretación

- **Geométrica.** En $\mathbb{R}^3$, los subespacios de dimensión 0, 1, 2 y 3 son el origen, las
  rectas por el origen, los planos por el origen y todo el espacio. La dimensión cuenta los
  "grados de libertad" para moverse dentro del subespacio.
- **Algebraica.** Si un subespacio se describe con $m$ ecuaciones independientes en $K^n$, su
  dimensión es $n-m$ (rango–nulidad). Si se describe con generadores, su dimensión es el rango de la
  matriz que forman.
- **Computacional.** Sobre $\mathbb{Z}_2$ la dimensión es la cantidad de bits libres: un subespacio
  de dimensión $k$ de $\mathbb{Z}_2^n$ se describe con $k$ bits, aunque sus vectores tengan $n$.

## Errores frecuentes

:::caution[Errores frecuentes]
- **Contar vectores sin verificar independencia.** $\{(1,2),(2,4)\}$ tiene dos vectores pero genera
  una recta: no es base de $\mathbb{R}^2$.
- **Creer que menos vectores "alcanzan" o que más "sobran" siempre.** Dos vectores nunca generan
  $\mathbb{R}^3$ y cuatro vectores de $\mathbb{R}^3$ siempre son dependientes, pero tres vectores
  pueden no ser base: $\{(1,0,0),(0,1,0),(1,1,0)\}$ es dependiente.
- **Confundir la dimensión del subespacio con la del ambiente.** En el ejemplo 4, $W\subseteq P_2[\mathbb{R}]$
  tiene dimensión 2 aunque sus elementos tengan "tres coeficientes".
- **Dar como base de $\{0\}$ el conjunto $\{0\}$.** Es dependiente ($1\cdot0=0$). La base es
  $\varnothing$ y la dimensión, 0.
- **Asumir que la extensión es única.** El ejemplo 1 muestra dos extensiones distintas, ambas
  correctas.
- **Contar mal en $\mathbb{Z}_2$.** Un subespacio de $\mathbb{Z}_2^4$ definido por una ecuación no
  trivial tiene $2^3=8$ elementos, no $2^4-1$ ni $4$.
:::

## Autoevaluación

1. ¿Es $\{1+x,\ 1-x,\ x^2\}$ base de $P_2[\mathbb{R}]$?
2. Si $S\subseteq\mathbb{R}^5$ tiene dimensión 5, ¿qué se puede decir de $S$?
3. ¿Cuántos elementos tiene $\operatorname{nul}(A)$ si $A\in\mathbb{Z}_2^{3\times6}$ tiene rango 3?

<details>
<summary>Respuestas</summary>

1. Sí. Son 3 vectores en un espacio de dimensión 3, así que basta ver independencia:
   $a(1+x)+b(1-x)+cx^2=0$ da $a+b=0$, $a-b=0$, $c=0$, de donde $a=b=c=0$.
2. $S=\mathbb{R}^5$, por la propiedad 4 con $W=\mathbb{R}^5$.
3. $\dim\operatorname{nul}(A)=6-3=3$, así que tiene $2^3=8$ elementos.

</details>

## Resumen

:::tip[En resumen]
- Base: conjunto ordenado, independiente y generador. Base de $\{0\}$: $\varnothing$.
- En un espacio generado por $m$ vectores, más de $m$ vectores son dependientes; por eso todas las
  bases tienen la misma cantidad de vectores, la dimensión.
- $\dim K^n=n$, $\dim\mathbb{R}^{m\times n}=mn$, $\dim P_n[\mathbb{R}]=n+1$.
- En dimensión $n$: $n$ vectores independientes, o $n$ vectores que generan, forman una base.
  $S\subseteq W$ con igual dimensión implica $S=W$.
- Todo generador contiene una base (columnas pivote); todo independiente se extiende a una base
  (agregando canónicos de las columnas sin pivote).
- Sobre $\mathbb{Z}_2$, dimensión $k$ equivale a exactamente $2^k$ elementos.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 6.2, "Independencia lineal,
  bases y dimensión", p. 461; sección 3.5, p. 197, para el caso de $\mathbb{R}^n$.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: conjuntos linealmente independientes y bases;
  la dimensión de un espacio vectorial.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed., sección 4.2, "Base y
  dimensión", p. 148.
- Lecciones relacionadas: [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/)
  (anterior), [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/) (siguiente),
  [cuerpos y ℤ₂](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/) y
  [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/).
