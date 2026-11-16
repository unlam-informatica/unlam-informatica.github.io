---
title: Autovalores y autovectores
description: Definición de autovalor, autovector y autoespacio para matrices reales y endomorfismos, interpretación geométrica, ejemplos y relación entre el autovalor 0 y la inversibilidad.
slug: algebra-ii/unidad-3/teoria/autovalores-y-autovectores
sidebar:
  order: 1
  label: 3.1 Autovalores y autovectores
---

## Para qué sirve

Una matriz $A\in\mathbb{R}^{n\times n}$ define la transformación $x\mapsto Ax$ de $\mathbb{R}^n$ en sí
mismo. En general, $Ax$ apunta en una dirección distinta de la de $x$. Pero a veces hay vectores
que la transformación **no gira**: los manda a un múltiplo de sí mismos. Sobre la recta que
generan, $A$ se comporta como un número.

Encontrar esas direcciones simplifica cualquier cálculo que repita la transformación. Si
$Av=\lambda v$, entonces $A^2v=\lambda^2v$, $A^3v=\lambda^3v$ y, en general, $A^kv=\lambda^kv$:
aplicar $A$ mil veces a $v$ cuesta lo mismo que elevar un número a la mil. Esta observación es
la base del análisis de algoritmos recursivos, de los modelos de Markov y del algoritmo PageRank,
que se desarrollan al final de la unidad.

## Intuición: vectores que solo se estiran

Tomemos

$$
A=\begin{pmatrix}2&1\\1&2\end{pmatrix}
$$

y miremos qué les hace a tres vectores:

- $v=(1,1)$: $Av=(3,3)=3v$. El vector se estira al triple sin cambiar de dirección.
- $u=(-1,1)$: $Au=(-2+1,\,-1+2)=(-1,1)=u$. El vector queda fijo.
- $w=(1,0)$: $Aw=(2,1)$, que no es múltiplo de $(1,0)$. La transformación cambió su dirección.

<!-- check: U3.T01.F1 -->

<figure class="math-figure">
<svg viewBox="-80 -115 240 165" role="img" aria-labelledby="u3t1-t u3t1-d" xmlns="http://www.w3.org/2000/svg">
<title id="u3t1-t">Direcciones invariantes de una transformación lineal</title>
<desc id="u3t1-d">Para la matriz A de filas (2,1) y (1,2), con una unidad cada 30 píxeles: el vector v=(1,1) se transforma en Av=(3,3), sobre la misma recta punteada y=x; el vector u=(-1,1) queda fijo, sobre la recta punteada y=-x; en cambio, w=(1,0) se transforma en Aw=(2,1), que apunta en otra dirección.</desc>
<defs>
<marker id="u3t1-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker>
<marker id="u3t1-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker>
<marker id="u3t1-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker>
<marker id="u3t1-arrow-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-d" d="M0 0 10 5 0 10z"/></marker>
</defs>
<g transform="scale(1,-1)">
<line class="grid" x1="-60" y1="-45" x2="-60" y2="110"/>
<line class="grid" x1="-30" y1="-45" x2="-30" y2="110"/>
<line class="grid" x1="30" y1="-45" x2="30" y2="110"/>
<line class="grid" x1="60" y1="-45" x2="60" y2="110"/>
<line class="grid" x1="90" y1="-45" x2="90" y2="110"/>
<line class="grid" x1="120" y1="-45" x2="120" y2="110"/>
<line class="grid" x1="-75" y1="-30" x2="135" y2="-30"/>
<line class="grid" x1="-75" y1="30" x2="135" y2="30"/>
<line class="grid" x1="-75" y1="60" x2="135" y2="60"/>
<line class="grid" x1="-75" y1="90" x2="135" y2="90"/>
<line class="axis" x1="-75" y1="0" x2="135" y2="0"/>
<line class="axis" x1="0" y1="-45" x2="0" y2="110"/>
<line class="guide" x1="-45" y1="-45" x2="110" y2="110"/>
<line class="guide" x1="-70" y1="70" x2="45" y2="-45"/>
<line class="vec-b" x1="0" y1="0" x2="90" y2="90" marker-end="url(#u3t1-arrow-b)"/>
<line class="vec-a" x1="0" y1="0" x2="30" y2="30" marker-end="url(#u3t1-arrow-a)"/>
<line class="vec-a" x1="0" y1="0" x2="-30" y2="30" marker-end="url(#u3t1-arrow-a)"/>
<line class="vec-c" x1="0" y1="0" x2="30" y2="0" marker-end="url(#u3t1-arrow-c)"/>
<line class="vec-d" x1="0" y1="0" x2="60" y2="30" marker-end="url(#u3t1-arrow-d)"/>
</g>
<text class="math" x="36" y="-20">v</text>
<text class="math" x="97" y="-92">Av = 3v</text>
<text class="math" x="-76" y="-36">u = Au</text>
<text class="math" x="24" y="15">w</text>
<text class="math" x="66" y="-28">Aw</text>
</svg>
<figcaption>Las rectas punteadas son direcciones invariantes de A: sobre y = x, A multiplica por 3; sobre y = −x, multiplica por 1. El vector w = (1, 0) no está en ninguna de ellas y su imagen Aw = (2, 1) apunta en otra dirección.</figcaption>
</figure>

Las rectas $y=x$ e $y=-x$ son **direcciones invariantes** de $A$: cada vector de esas rectas se
transforma en un vector de la misma recta. Los factores $3$ y $1$ son los autovalores; los
vectores no nulos de esas rectas, los autovectores. Cualquier otro vector, como $w$, se puede
escribir como combinación de un vector de cada recta; $A$ estira cada componente por su factor
y por eso $Aw$ "se inclina" hacia la recta de factor mayor.

## Definición para matrices

:::note[Definición]
Sea $A\in\mathbb{R}^{n\times n}$. Un número $\lambda\in\mathbb{R}$ es un **autovalor** de $A$ si
existe un vector $v\in\mathbb{R}^n$, $v\neq0$, tal que

$$
Av=\lambda v .
$$

Todo vector $v\neq0$ que cumple esa igualdad es un **autovector de $A$ asociado a $\lambda$**.
:::

Observaciones que conviene fijar desde el principio:

- **El vector nulo nunca es autovector.** Como $A0=\lambda 0$ para cualquier $\lambda$, si lo
  admitiéramos todo número sería autovalor y la definición no diría nada.
- **El autovalor $0$ sí está permitido.** $\lambda=0$ es autovalor cuando existe $v\neq0$ con
  $Av=0$. Volvemos sobre esto al final de la lección.
- **Cada autovector tiene un único autovalor.** Si $Av=\lambda v$ y $Av=\mu v$ con $v\neq0$,
  entonces $(\lambda-\mu)v=0$ y, como $v\neq0$, $\lambda=\mu$.
- **Los múltiplos no nulos de un autovector son autovectores** del mismo autovalor:
  $A(cv)=cAv=c\lambda v=\lambda(cv)$. Por eso hablamos de *direcciones* invariantes.
- En esta asignatura trabajamos con matrices de coeficientes reales y **autovalores reales**.
  Hay matrices reales sin autovalores reales (por ejemplo, una rotación); en ese caso la respuesta
  correcta es "no tiene autovalores reales".

Sinónimos que vas a encontrar en los libros: *valor propio* y *vector propio*; Poole, en su
traducción, escribe *eigenvalor* y *eigenvector*.

## Definición para endomorfismos

La misma idea vale para cualquier transformación lineal de un espacio en sí mismo, sin necesidad
de matrices.

:::note[Definición]
Sea $V$ un espacio vectorial real de dimensión finita y $T:V\to V$ un endomorfismo. Un número
$\lambda\in\mathbb{R}$ es un **autovalor** de $T$ si existe $v\in V$, $v\neq0_V$, tal que
$T(v)=\lambda v$; ese $v$ es un **autovector** de $T$ asociado a $\lambda$.
:::

Una matriz $A$ es un caso particular: sus autovalores son los del endomorfismo $x\mapsto Ax$ de
$\mathbb{R}^n$. En el otro sentido, si fijamos una base $B$ de $V$ y llamamos $M(T)_B$ a la matriz
de $T$ en esa base, sabemos que $M(T)_B[v]_B=[T(v)]_B$. Entonces

$$
T(v)=\lambda v\iff [T(v)]_B=\lambda[v]_B\iff M(T)_B\,[v]_B=\lambda\,[v]_B ,
$$

porque tomar coordenadas es lineal e inyectivo, y $v\neq0_V$ si y solo si $[v]_B\neq0$.

:::tip[Independencia de la base]
Para cualquier base $B$ de $V$: $\lambda$ es autovalor de $T$ si y solo si es autovalor de la
matriz $M(T)_B$, y $v$ es autovector de $T$ si y solo si $[v]_B$ es autovector de $M(T)_B$. En
particular, **los autovalores de $T$ no dependen de la base elegida**; lo que cambia con la base
son las coordenadas de los autovectores.
:::

Este hecho reaparece en la lección de [matrices semejantes](/algebra-ii/unidad-3/teoria/matrices-semejantes/):
las matrices de un mismo endomorfismo en bases distintas tienen los mismos autovalores.

:::caution[Notación de los libros]
Escribimos $M(T)_B$ para la matriz de $T$ en la base $B$ (salida y llegada en $B$). Poole y Lay
la escriben $[T]_B$ y, para bases distintas, invierten el orden de los subíndices. La tabla de
equivalencias está en [notación](/algebra-ii/notacion/).
:::

## Interpretación geométrica

Si $v$ es autovector de $A$ con autovalor $\lambda$, la recta $\operatorname{gen}\{v\}$ se
transforma dentro de sí misma: $A(tv)=(\lambda t)v$. Sobre esa recta, $A$ actúa así:

- $\lambda>1$: estira; $0<\lambda<1$: encoge; $\lambda=1$: deja fijo cada vector;
- $\lambda<0$: invierte el sentido (y estira o encoge según $\lvert\lambda\rvert$);
- $\lambda=0$: aplasta la recta entera en el origen.

### Tres ejemplos sin cuentas

Muchas transformaciones geométricas del plano tienen autovalores y autovectores que se leen
directamente de su definición, sin calcular nada.

**Proyección ortogonal sobre una recta $L$ por el origen.** Un vector de $L$ se proyecta en sí
mismo: autovalor $1$, con todos los vectores no nulos de $L$ como autovectores. Un vector
perpendicular a $L$ se proyecta en el origen: autovalor $0$. Cualquier otro vector cambia de
dirección. Autovalores: $1$ y $0$.

**Simetría respecto de una recta $L$ por el origen.** Los vectores de $L$ quedan fijos (autovalor
$1$) y los perpendiculares a $L$ se invierten (autovalor $-1$). Autovalores: $1$ y $-1$.

**Rotación de ángulo $\theta$ alrededor del origen, con $0<\theta<\pi$.** Ningún vector no nulo
conserva su dirección: todos giran. Por lo tanto **no hay autovalores reales**. Los casos
extremos son distintos: la rotación de ángulo $\pi$ es $v\mapsto-v$ (todo vector no nulo es
autovector de $-1$) y la de ángulo $0$ es la identidad (todo vector no nulo es autovector de $1$).

Más en general, la homotecia $v\mapsto kv$ tiene un único autovalor, $k$, y todo vector no nulo es
autovector suyo. En la [lección siguiente](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/)
confirmamos estas conclusiones con cuentas.

## El autoespacio

Juntemos todos los autovectores de un autovalor y agreguemos el vector nulo.

:::note[Definición]
Si $\lambda$ es autovalor de $A\in\mathbb{R}^{n\times n}$, el **autoespacio** de $A$ asociado a
$\lambda$ es

$$
E_\lambda(A)=\{v\in\mathbb{R}^n: Av=\lambda v\}=\operatorname{nul}(\lambda I-A).
$$

Para un endomorfismo $T:V\to V$, $E_\lambda(T)=\{v\in V: T(v)=\lambda v\}$.
:::

La segunda igualdad es la clave de todos los cálculos: $Av=\lambda v\iff\lambda v-Av=0\iff
(\lambda I-A)v=0$. Observá que $E_\lambda(A)$ contiene al vector nulo, que **no** es autovector;
los autovectores asociados a $\lambda$ son exactamente los vectores no nulos de $E_\lambda(A)$.

:::note[Propiedad]
Para todo autovalor $\lambda$, $E_\lambda(A)$ es un subespacio de $\mathbb{R}^n$ de dimensión al
menos $1$. Lo mismo vale para $E_\lambda(T)\subseteq V$.
:::

**Demostración.** Verificamos las tres condiciones del criterio de subespacio para
$E_\lambda(T)=\{v\in V: T(v)=\lambda v\}$, que incluye el caso matricial con $T(x)=Ax$.

1. $0_V\in E_\lambda(T)$, porque $T(0_V)=0_V=\lambda 0_V$.
2. Si $u,v\in E_\lambda(T)$, entonces $T(u+v)=T(u)+T(v)=\lambda u+\lambda v=\lambda(u+v)$, así
   que $u+v\in E_\lambda(T)$.
3. Si $v\in E_\lambda(T)$ y $c\in\mathbb{R}$, entonces $T(cv)=cT(v)=c\lambda v=\lambda(cv)$, así
   que $cv\in E_\lambda(T)$.

Como $\lambda$ es autovalor, existe al menos un autovector $v\neq0_V$ en $E_\lambda(T)$, de modo
que $\dim E_\lambda(T)\ge1$. En el caso matricial también se puede argumentar en una línea:
$E_\lambda(A)=\operatorname{nul}(\lambda I-A)$ y el espacio nulo de una matriz es siempre un
subespacio. $\blacksquare$

La dimensión de $E_\lambda(A)$ se llama **multiplicidad geométrica** de $\lambda$ y se anota
$m_g(\lambda)$. Por la relación rango–nulidad,

$$
m_g(\lambda)=\dim\operatorname{nul}(\lambda I-A)=n-\operatorname{rango}(\lambda I-A).
$$

Un número $\lambda$ es autovalor si y solo si $E_\lambda(A)=\operatorname{nul}(\lambda I-A)\neq\{0\}$,
es decir, si y solo si $\operatorname{rango}(\lambda I-A)<n$.

## El autovalor 0 y la inversibilidad

:::note[Propiedad]
Sea $A\in\mathbb{R}^{n\times n}$. Entonces $0$ es autovalor de $A$ si y solo si $A$ no es
inversible. En ese caso, $E_0(A)=\operatorname{nul}(A)$.
:::

**Demostración.** $0$ es autovalor $\iff$ existe $v\neq0$ con $Av=0v=0$ $\iff$
$\operatorname{nul}(A)\neq\{0\}$ $\iff$ $\operatorname{rango}(A)<n$ $\iff$ $A$ no es inversible.
La igualdad $E_0(A)=\operatorname{nul}(0I-A)=\operatorname{nul}(-A)=\operatorname{nul}(A)$ es
inmediata. $\blacksquare$

Para un endomorfismo $T:V\to V$ la versión es: $0$ es autovalor de $T$ $\iff$
$\operatorname{Nu}(T)\neq\{0_V\}$ $\iff$ $T$ no es monomorfismo. Como $V$ tiene dimensión
finita, por el teorema de la dimensión eso equivale a que $T$ no sea isomorfismo.

Dicho al revés: **una matriz es inversible si y solo si $0$ no es autovalor suyo.** Es una
caracterización más para la larga lista de condiciones equivalentes a la inversibilidad
($\det A\neq0$, $\operatorname{rango}(A)=n$, $\operatorname{nul}(A)=\{0\}$, columnas LI...).

## Ejemplos resueltos

### Ejemplo 1 · Verificar autovectores y autovalores

<!-- check: U3.T01.E1 -->

Sea

$$
A=\begin{pmatrix}4&-2\\1&1\end{pmatrix}.
$$

Decidir si $u=(2,1)$ y $w=(1,2)$ son autovectores de $A$ y si $2$ y $5$ son autovalores de $A$.

**Autovectores candidatos.** Para decidir si un vector dado es autovector alcanza con
multiplicar:

$$
Au=\begin{pmatrix}4\cdot2-2\cdot1\\1\cdot2+1\cdot1\end{pmatrix}=\begin{pmatrix}6\\3\end{pmatrix}=3\begin{pmatrix}2\\1\end{pmatrix}=3u .
$$

Entonces $u$ es autovector de $A$ asociado al autovalor $3$. En cambio,

$$
Aw=\begin{pmatrix}4-4\\1+2\end{pmatrix}=\begin{pmatrix}0\\3\end{pmatrix}.
$$

Si fuera $Aw=\lambda w$, de la primera componente saldría $\lambda\cdot1=0$, o sea $\lambda=0$, y
de la segunda $\lambda\cdot2=3$: contradicción. Por lo tanto $w$ no es autovector.

**Autovalores candidatos.** Para decidir si un número dado es autovalor hay que ver si el
sistema homogéneo $(\lambda I-A)v=0$ tiene soluciones no nulas. Para $\lambda=2$:

$$
2I-A=\begin{pmatrix}-2&2\\-1&1\end{pmatrix}\sim\begin{pmatrix}-1&1\\0&0\end{pmatrix},
$$

que tiene rango $1<2$. Las soluciones cumplen $-x+y=0$, es decir $y=x$:
$E_2(A)=\operatorname{gen}\{(1,1)\}$. Por lo tanto $2$ es autovalor. Para $\lambda=5$:

$$
5I-A=\begin{pmatrix}1&2\\-1&4\end{pmatrix},\qquad \det(5I-A)=4+2=6\neq0 ,
$$

así que $5I-A$ es inversible, el sistema solo tiene la solución nula y $5$ no es autovalor.

**Comprobación.** $A(1,1)=(4-2,\,1+1)=(2,2)=2\,(1,1)$.

:::tip[Resultado]
$u$ es autovector (autovalor $3$); $w$ no lo es. $2$ es autovalor con
$E_2(A)=\operatorname{gen}\{(1,1)\}$; $5$ no es autovalor.
:::

### Ejemplo 2 · La transposición de matrices

<!-- check: U3.T01.E2 -->

Sea $T:\mathbb{R}^{2\times2}\to\mathbb{R}^{2\times2}$, $T(X)=X^t$. Hallar sus autovalores y
autoespacios.

**Sin matrices.** Si $X$ es simétrica, $T(X)=X$: las simétricas no nulas son autovectores de $1$.
Si $X$ es antisimétrica ($X^t=-X$), $T(X)=-X$: las antisimétricas no nulas son autovectores de
$-1$. ¿Hay otros autovalores? Si $X\neq0$ y $X^t=\lambda X$, transponiendo de nuevo,

$$
X=(X^t)^t=(\lambda X)^t=\lambda X^t=\lambda^2X ,
$$

y como $X\neq0$, $\lambda^2=1$. Entonces los únicos autovalores posibles son $1$ y $-1$, y

$$
E_1(T)=\left\{\begin{pmatrix}a&b\\b&d\end{pmatrix}: a,b,d\in\mathbb{R}\right\},\ \dim=3;\qquad
E_{-1}(T)=\operatorname{gen}\left\{\begin{pmatrix}0&1\\-1&0\end{pmatrix}\right\},\ \dim=1 .
$$

**Con la matriz en una base.** Tomemos la base canónica ordenada
$E=\{E_{11},E_{12},E_{21},E_{22}\}$, donde $E_{ij}$ tiene un $1$ en la posición $(i,j)$ y ceros en
el resto. Como $T(E_{11})=E_{11}$, $T(E_{12})=E_{21}$, $T(E_{21})=E_{12}$ y $T(E_{22})=E_{22}$,

$$
M(T)_E=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix}.
$$

Las coordenadas de las simétricas, $(a,b,b,d)$, cumplen $M(T)_E(a,b,b,d)^t=(a,b,b,d)^t$, y las de
la antisimétrica básica, $(0,1,-1,0)$, cumplen $M(T)_E(0,1,-1,0)^t=(0,-1,1,0)^t=-(0,1,-1,0)^t$.
Tal como asegura la independencia de la base, la matriz tiene los mismos autovalores que $T$ y sus
autovectores son las coordenadas de los autovectores de $T$.

**Comprobación.** $\dim E_1(T)+\dim E_{-1}(T)=3+1=4=\dim\mathbb{R}^{2\times2}$.

:::tip[Resultado]
Autovalores $1$ y $-1$. $E_1(T)$ son las matrices simétricas ($\dim 3$) y $E_{-1}(T)$, las
antisimétricas ($\dim 1$).
:::

### Ejemplo 3 · Una matriz no inversible

<!-- check: U3.T01.E3 -->

Sea

$$
A=\begin{pmatrix}1&2&-1\\2&1&1\\3&3&0\end{pmatrix}.
$$

Justificar sin calcular el polinomio característico que $0$ es autovalor de $A$ y hallar
$E_0(A)$.

**Por qué $0$ es autovalor.** La tercera fila es la suma de las dos primeras ($F_3=F_1+F_2$), así
que las filas son LD, $\det A=0$ y $A$ no es inversible. Por la propiedad anterior, $0$ es
autovalor.

**Autoespacio.** $E_0(A)=\operatorname{nul}(A)$. Escalonamos:

$$
\begin{pmatrix}1&2&-1\\2&1&1\\3&3&0\end{pmatrix}
\xrightarrow[F_3-3F_1\to F_3]{F_2-2F_1\to F_2}
\begin{pmatrix}1&2&-1\\0&-3&3\\0&-3&3\end{pmatrix}
\xrightarrow{F_3-F_2\to F_3}
\begin{pmatrix}1&2&-1\\0&-3&3\\0&0&0\end{pmatrix}.
$$

De la segunda fila, $y=z$; de la primera, $x=-2y+z=-z$. Con $z=-1$ queda
$v=(1,-1,-1)$ y $E_0(A)=\operatorname{gen}\{(1,-1,-1)\}$, de dimensión $1$.

**Comprobación.** $A(1,-1,-1)^t=(1-2+1,\;2-1-1,\;3-3+0)^t=(0,0,0)^t$.

:::tip[Resultado]
$0$ es autovalor de $A$ y $E_0(A)=\operatorname{gen}\{(1,-1,-1)\}$.
:::

### Ejemplo 4 · Un parámetro determinado por un autovector

<!-- check: U3.T01.E4 -->

Sea

$$
A=\begin{pmatrix}1&a&0\\2&1&a\\0&1&3\end{pmatrix},\qquad a\in\mathbb{R}.
$$

Hallar $a$ para que $v=(1,1,-1)$ sea autovector de $A$ e indicar el autovalor asociado.

**Planteo.** Calculamos $Av$ en función de $a$:

$$
Av=\begin{pmatrix}1+a+0\\2+1-a\\0+1-3\end{pmatrix}=\begin{pmatrix}1+a\\3-a\\-2\end{pmatrix}.
$$

Pedimos $Av=\lambda v$ para algún $\lambda$, que también es incógnita:

$$
\begin{cases}1+a=\lambda\\3-a=\lambda\\-2=-\lambda\end{cases}
$$

**Resolución.** La tercera ecuación da $\lambda=2$; la primera, $a=1$. La segunda tiene que
cumplirse también: $3-1=2$. Se cumple. Son tres ecuaciones con dos incógnitas, así que en
general podrían ser incompatibles; en ese caso la respuesta sería "no existe ningún $a$".

**Comprobación.** Con $a=1$, $Av=(2,2,-2)=2(1,1,-1)$.

:::tip[Resultado]
$a=1$; $v$ es autovector asociado al autovalor $\lambda=2$.
:::

:::caution[Errores frecuentes]
- **Aceptar $v=0$ como autovector.** Decir "$v=0$ cumple $Av=\lambda v$, así que $\lambda$ es
  autovalor" es incorrecto: con ese argumento todo número sería autovalor. Hace falta $v\neq0$.
- **Confundir "$\lambda=0$ no puede ser autovalor" con "$v=0$ no puede ser autovector".** La
  matriz del ejemplo 3 tiene autovalor $0$ y es perfectamente válido.
- **Concluir que un vector es autovector porque $Av$ "se parece" a $v$.** Hay que verificar que
  todas las componentes de $Av$ son el mismo múltiplo de las de $v$, como en el ejemplo 1 con
  $w=(1,2)$: la primera componente pide $\lambda=0$ y la segunda $\lambda=\frac32$.
- **Creer que todo vector de $E_\lambda(A)$ es autovector.** El vector nulo pertenece al
  autoespacio y no es autovector.
- **Suponer que toda matriz real tiene autovalores reales.** La rotación de ángulo
  $\frac{\pi}{2}$, $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, no tiene ninguno.
- **Pensar que el autovalor depende de la longitud del autovector.** $v$ y $5v$ tienen el mismo
  autovalor.
:::

## Autoevaluación

<details>
<summary>1. Si v y w son autovectores de A con autovalor 3, ¿es v − w autovector de A?</summary>

Es autovector de $3$ siempre que $v-w\neq0$, porque $E_3(A)$ es un subespacio. Si $v=w$, la
diferencia es el vector nulo y no es autovector.

</details>

<details>
<summary>2. ¿Qué autovalores tiene la simetría respecto del eje x en el plano?</summary>

$1$ (con autoespacio el eje $x$) y $-1$ (con autoespacio el eje $y$). Su matriz canónica es
$\operatorname{diag}(1,-1)$.

</details>

<details>
<summary>3. Una matriz 3 × 3 tiene dos columnas iguales. ¿Qué podés afirmar?</summary>

Las columnas son LD, $\det A=0$ y entonces $0$ es autovalor de $A$. Si las columnas $i$ y $j$ son
iguales, $e_i-e_j\in\operatorname{nul}(A)=E_0(A)$.

</details>

:::tip[En resumen]
- $\lambda$ es autovalor de $A$ si existe $v\neq0$ con $Av=\lambda v$; para un endomorfismo,
  $T(v)=\lambda v$. Los autovalores de $T$ coinciden con los de $M(T)_B$ en cualquier base $B$.
- Geométricamente, los autovectores marcan direcciones invariantes, sobre las que la
  transformación actúa como multiplicación por $\lambda$.
- $E_\lambda(A)=\operatorname{nul}(\lambda I-A)$ es un subespacio; sus vectores no nulos son los
  autovectores de $\lambda$; su dimensión es $m_g(\lambda)$.
- Para *verificar* un autovector se multiplica; para *verificar* un autovalor se estudia si
  $\lambda I-A$ es singular.
- $0$ es autovalor de $A$ si y solo si $A$ no es inversible, y entonces $E_0(A)=\operatorname{nul}(A)$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 4.1, Introducción
  (p. 265), con la interpretación geométrica en el plano, y sección 4.3 (p. 303) para
  matrices $n\times n$.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de valores propios y vectores
  propios, sección inicial.
- Repaso: [determinantes](/algebra-ii/repaso/determinantes/) y
  [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/).
- Siguiente lección: [3.2 Polinomio característico](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/),
  donde pasamos de *verificar* a *buscar* autovalores.
- Presentación de la unidad: [Unidad 3](/algebra-ii/unidad-3/).
