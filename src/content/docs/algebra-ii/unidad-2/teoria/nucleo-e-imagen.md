---
title: Núcleo e imagen
description: Núcleo e imagen de una transformación lineal, por qué son subespacios, cómo calcular sus bases y cómo se describen las preimágenes de un vector.
slug: algebra-ii/unidad-2/teoria/nucleo-e-imagen
sidebar:
  order: 2
  label: 2.2 Núcleo e imagen
---

## Para qué sirve

Toda TL $T:V\to W$ tiene asociados dos subespacios que la describen casi por completo:

- el **núcleo**, que reúne los vectores que $T$ "aplasta" contra el nulo: mide cuánta información pierde $T$;
- la **imagen**, que reúne los vectores a los que $T$ llega: mide qué puede producir $T$.

Con ellos se responden las preguntas básicas sobre una TL. ¿La ecuación $T(v)=w$ tiene solución? (¿$w$ está en la imagen?) ¿Cuántas? (Tantas como vectores tiene el núcleo, trasladado.) ¿$T$ distingue vectores distintos? (Sí, exactamente cuando el núcleo es trivial.) Para una matriz $A$, son los subespacios $\operatorname{nul}(A)$ y $\operatorname{col}(A)$ que estudiamos en [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/).

## Definiciones

:::note[Definición]
Sea $T:V\to W$ una TL.

- El **núcleo** de $T$ es $\operatorname{Nu}(T)=\{v\in V:\ T(v)=0_W\}$. Es un subconjunto de $V$.
- La **imagen** de $T$ es $\operatorname{Im}(T)=\{w\in W:\ w=T(v)\text{ para algún } v\in V\}=\{T(v):\ v\in V\}$. Es un subconjunto de $W$.
:::

Siempre $0_V\in\operatorname{Nu}(T)$ y $0_W\in\operatorname{Im}(T)$, porque $T(0_V)=0_W$. Los casos extremos son la TL nula ($T(v)=0_W$ para todo $v$), con $\operatorname{Nu}(T)=V$ e $\operatorname{Im}(T)=\{0_W\}$, y la identidad de $V$, con $\operatorname{Nu}=\{0_V\}$ e $\operatorname{Im}=V$.

Primeros ejemplos, del catálogo de [2.1](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/):

- Proyección $P(x,y)=(x,0)$: $\operatorname{Nu}(P)$ es el eje $y$ e $\operatorname{Im}(P)$ es el eje $x$.
- Derivación $D:P_2[\mathbb{R}]\to P_2[\mathbb{R}]$: $\operatorname{Nu}(D)$ son los polinomios constantes (incluido el nulo) e $\operatorname{Im}(D)=P_1[\mathbb{R}]$, porque todo polinomio de grado $\le 1$ es derivada de uno de grado $\le 2$: $(a+bx)=\big(ax+\tfrac b2x^2\big)'$.
- Traza $\operatorname{tr}:\mathbb{R}^{2\times 2}\to\mathbb{R}$: $\operatorname{Nu}$ son las matrices de traza nula e $\operatorname{Im}=\mathbb{R}$ (la traza de $\begin{pmatrix}t&0\\0&0\end{pmatrix}$ es $t$).
- $T_A(x)=Ax$ con $A\in K^{m\times n}$: $\operatorname{Nu}(T_A)=\operatorname{nul}(A)$ y, como $Ax$ es la combinación lineal de las columnas de $A$ con los escalares de $x$, $\operatorname{Im}(T_A)=\operatorname{col}(A)$.

## Núcleo e imagen son subespacios

:::note[Teorema]
Si $T:V\to W$ es lineal, $\operatorname{Nu}(T)$ es un subespacio de $V$ e $\operatorname{Im}(T)$ es un subespacio de $W$.
:::

**Demostración.** Usamos el criterio de las tres condiciones de [subespacios](/algebra-ii/unidad-1/teoria/subespacios/).

*Núcleo.*

1. $0_V\in\operatorname{Nu}(T)$ porque $T(0_V)=0_W$.
2. Si $u,v\in\operatorname{Nu}(T)$, entonces $T(u+v)=T(u)+T(v)=0_W+0_W=0_W$; luego $u+v\in\operatorname{Nu}(T)$.
3. Si $v\in\operatorname{Nu}(T)$ y $\lambda\in K$, entonces $T(\lambda v)=\lambda T(v)=\lambda\,0_W=0_W$; luego $\lambda v\in\operatorname{Nu}(T)$.

*Imagen.*

1. $0_W=T(0_V)$, así que $0_W\in\operatorname{Im}(T)$.
2. Si $w_1,w_2\in\operatorname{Im}(T)$, existen $v_1,v_2\in V$ con $T(v_1)=w_1$ y $T(v_2)=w_2$. Entonces $w_1+w_2=T(v_1)+T(v_2)=T(v_1+v_2)$, que es imagen de $v_1+v_2\in V$.
3. Si $w\in\operatorname{Im}(T)$, $w=T(v)$, y $\lambda\in K$, entonces $\lambda w=\lambda T(v)=T(\lambda v)\in\operatorname{Im}(T)$. $\blacksquare$

En la prueba de la imagen se usó la linealidad "de derecha a izquierda": $T(v_1)+T(v_2)=T(v_1+v_2)$. Es el paso que falla para funciones no lineales: la imagen de $f(x)=x^2$ es $[0,+\infty)$, que no es subespacio de $\mathbb{R}$.

## Cómo se calculan

### El núcleo: un sistema homogéneo

Plantear $T(v)=0_W$ con un vector genérico de $V$ da un sistema lineal homogéneo. Su solución general, escrita en forma paramétrica, se factoriza por parámetros y da un conjunto generador; los vectores que acompañan a parámetros independientes son LI, así que forman una base.

### La imagen: transformar un generador

:::note[Propiedad · La imagen de un generador genera la imagen]
Si $V=\operatorname{gen}\{v_1,\dots,v_n\}$, entonces $\operatorname{Im}(T)=\operatorname{gen}\{T(v_1),\dots,T(v_n)\}$.
:::

**Demostración.** ($\supseteq$) Cada $T(v_i)$ está en $\operatorname{Im}(T)$, y como $\operatorname{Im}(T)$ es subespacio contiene todas sus combinaciones lineales.
($\subseteq$) Si $w\in\operatorname{Im}(T)$, existe $v\in V$ con $T(v)=w$. Como los $v_i$ generan $V$, $v=\lambda_1v_1+\cdots+\lambda_nv_n$ para ciertos escalares, y por linealidad $w=T(v)=\lambda_1T(v_1)+\cdots+\lambda_nT(v_n)\in\operatorname{gen}\{T(v_1),\dots,T(v_n)\}$. $\blacksquare$

Lo práctico es transformar una base de $V$ (la canónica, si la hay). Los transformados **generan** la imagen pero pueden ser LD: hay que **depurarlos**. Dos maneras equivalentes:

- ponerlos como **filas** de una matriz y escalonar: las filas no nulas que quedan son una base de la imagen (escalonar por filas no cambia el subespacio generado por las filas);
- ponerlos como **columnas** de una matriz, escalonar y quedarse con los vectores **originales** que ocupan las columnas con pivote.

### Ejemplo 1 · Núcleo e imagen de una TL de ℝ⁴ en ℝ³
<!-- check: U2.T02.E1 -->

Hallar bases de $\operatorname{Nu}(T)$ y de $\operatorname{Im}(T)$ para

$$
T(x_1,x_2,x_3,x_4)=(x_1+x_2-x_4,\ \ x_1+2x_2+x_3,\ \ 2x_1+3x_2+x_3-x_4).
$$

**Núcleo.** $T(x)=0$ es el sistema homogéneo de matriz

$$
A=\begin{pmatrix}1&1&0&-1\\1&2&1&0\\2&3&1&-1\end{pmatrix}.
$$

Como hay 4 incógnitas y a lo sumo 3 ecuaciones independientes, ya sabemos que el sistema es compatible indeterminado. Escalonamos:

$$
A\xrightarrow[F_3-2F_1\to F_3]{F_2-F_1\to F_2}\begin{pmatrix}1&1&0&-1\\0&1&1&1\\0&1&1&1\end{pmatrix}\xrightarrow[F_1-F_2\to F_1]{F_3-F_2\to F_3}\begin{pmatrix}1&0&-1&-2\\0&1&1&1\\0&0&0&0\end{pmatrix}.
$$

Las variables libres son $x_3$ y $x_4$: $x_1=x_3+2x_4$ y $x_2=-x_3-x_4$. Entonces

$$
(x_1,x_2,x_3,x_4)=(x_3+2x_4,\ -x_3-x_4,\ x_3,\ x_4)=x_3\,(1,-1,1,0)+x_4\,(2,-1,0,1),
$$

y una base del núcleo es $B_{\operatorname{Nu}}=\{(1,-1,1,0),\ (2,-1,0,1)\}$, con $\dim\operatorname{Nu}(T)=2$.

Corroboramos: $T(1,-1,1,0)=(1-1-0,\ 1-2+1,\ 2-3+1-0)=(0,0,0)$ y $T(2,-1,0,1)=(2-1-1,\ 2-2+0,\ 4-3+0-1)=(0,0,0)$.

**Imagen.** Transformamos la base canónica: $T(e_1)=(1,1,2)$, $T(e_2)=(1,2,3)$, $T(e_3)=(0,1,1)$, $T(e_4)=(-1,0,-1)$ (son las columnas de $A$). Los ponemos como filas y escalonamos:

$$
\begin{pmatrix}1&1&2\\1&2&3\\0&1&1\\-1&0&-1\end{pmatrix}\xrightarrow[F_4+F_1\to F_4]{F_2-F_1\to F_2}\begin{pmatrix}1&1&2\\0&1&1\\0&1&1\\0&1&1\end{pmatrix}\xrightarrow[F_4-F_2\to F_4]{F_3-F_2\to F_3}\begin{pmatrix}1&1&2\\0&1&1\\0&0&0\\0&0&0\end{pmatrix}.
$$

Una base de la imagen es $B_{\operatorname{Im}}=\{(1,1,2),\ (0,1,1)\}$ y $\dim\operatorname{Im}(T)=2$.

**Ecuación de la imagen.** $(a,b,c)\in\operatorname{Im}(T)$ si y solo si $(a,b,c)=\alpha(1,1,2)+\beta(0,1,1)=(\alpha,\ \alpha+\beta,\ 2\alpha+\beta)$, es decir, si y solo si $c=a+b$. La imagen es el plano $z=x+y$ de $\mathbb{R}^3$; los cuatro transformados de la base canónica lo cumplen.

**Comprobación.** $\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)=2+2=4=\dim\mathbb{R}^4$, como anticipa el [teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/).

### Ejemplo 2 · Llegada en matrices
<!-- check: U2.T02.E2 -->

Sea $T:P_2[\mathbb{R}]\to\mathbb{R}^{2\times 2}$, $T(p)=\begin{pmatrix}p(0)&p(1)\\p(1)&p(2)\end{pmatrix}$. (Es lineal porque cada entrada es una evaluación.) Hallar $\operatorname{Nu}(T)$ e $\operatorname{Im}(T)$.

**Núcleo.** $T(p)=0$ significa $p(0)=p(1)=p(2)=0$. Con $p=a+bx+cx^2$:

$$
\begin{cases}a=0\\a+b+c=0\\a+2b+4c=0\end{cases}\ \Longrightarrow\ a=0,\ b+c=0,\ 2b+4c=0\ \Longrightarrow\ c=0,\ b=0.
$$

$\operatorname{Nu}(T)=\{0\}$. (También se ve sin cuentas: un polinomio no nulo de grado $\le 2$ tiene a lo sumo 2 raíces, y $p$ tendría tres.)

**Imagen.** Transformamos la base canónica $\{1,x,x^2\}$:

$$
T(1)=\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad T(x)=\begin{pmatrix}0&1\\1&2\end{pmatrix},\quad T(x^2)=\begin{pmatrix}0&1\\1&4\end{pmatrix}.
$$

Para ver si son LI pasamos a coordenadas en la base canónica $\{E_{11},E_{12},E_{21},E_{22}\}$ de $\mathbb{R}^{2\times 2}$ y escalonamos por filas:

$$
\begin{pmatrix}1&1&1&1\\0&1&1&2\\0&1&1&4\end{pmatrix}\xrightarrow{F_3-F_2\to F_3}\begin{pmatrix}1&1&1&1\\0&1&1&2\\0&0&0&2\end{pmatrix}.
$$

Tres filas no nulas: las tres matrices son LI y $\dim\operatorname{Im}(T)=3$.

**Interpretación.** Las tres imágenes son simétricas, y el conjunto $\mathcal S$ de matrices simétricas de $2\times 2$ es un subespacio de dimensión 3 (base $\{E_{11},\ E_{12}+E_{21},\ E_{22}\}$). Como $\operatorname{Im}(T)\subseteq\mathcal S$ y ambos tienen dimensión 3, **$\operatorname{Im}(T)=\mathcal S$**. Este argumento, "inclusión más igualdad de dimensiones", evita resolver sistemas.

### Ejemplo 3 · Salida en matrices, llegada en polinomios
<!-- check: U2.T02.E3 -->

Sea $T:\mathbb{R}^{2\times 2}\to P_2[\mathbb{R}]$,

$$
T\begin{pmatrix}a&b\\c&d\end{pmatrix}=(a+d)+(b-c)\,x+(a+b-c+d)\,x^2.
$$

**Núcleo.** Igualamos al polinomio nulo coeficiente a coeficiente:

$$
\begin{cases}a+d=0\\b-c=0\\a+b-c+d=0\end{cases}
$$

La tercera ecuación es la suma de las dos primeras, así que sobra: $d=-a$, $c=b$, con $a,b$ libres.

$$
\begin{pmatrix}a&b\\b&-a\end{pmatrix}=a\begin{pmatrix}1&0\\0&-1\end{pmatrix}+b\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$

y $B_{\operatorname{Nu}}=\left\{\begin{pmatrix}1&0\\0&-1\end{pmatrix},\ \begin{pmatrix}0&1\\1&0\end{pmatrix}\right\}$, $\dim\operatorname{Nu}(T)=2$. Los elementos del núcleo son **matrices**, no cuaternas.

**Imagen.** $T(E_{11})=1+x^2$, $T(E_{12})=x+x^2$, $T(E_{21})=-x-x^2$, $T(E_{22})=1+x^2$. Se repite $1+x^2$ y $T(E_{21})=-T(E_{12})$; los dos restantes, $1+x^2$ y $x+x^2$, no son proporcionales, así que son LI. $B_{\operatorname{Im}}=\{1+x^2,\ x+x^2\}$ y $\dim\operatorname{Im}(T)=2$.

**Comprobación.** $T\begin{pmatrix}1&0\\0&-1\end{pmatrix}=0+0x+0x^2$ y $T\begin{pmatrix}0&1\\1&0\end{pmatrix}=0+0x+0x^2$; además $2+2=4=\dim\mathbb{R}^{2\times 2}$.

## Preimágenes

Dado $w\in W$, el conjunto de sus **preimágenes** es $\{v\in V:\ T(v)=w\}$. Es vacío si $w\notin\operatorname{Im}(T)$. Si no es vacío, tiene una estructura muy precisa.

:::note[Teorema · Estructura de las preimágenes]
Sea $T:V\to W$ lineal y sea $v_p\in V$ con $T(v_p)=w$. Entonces

$$
\{v\in V:\ T(v)=w\}=v_p+\operatorname{Nu}(T)=\{v_p+u:\ u\in\operatorname{Nu}(T)\}.
$$
:::

**Demostración.** Si $u\in\operatorname{Nu}(T)$, $T(v_p+u)=T(v_p)+T(u)=w+0_W=w$. Recíprocamente, si $T(v)=w$, entonces $T(v-v_p)=T(v)-T(v_p)=w-w=0_W$, así que $u=v-v_p\in\operatorname{Nu}(T)$ y $v=v_p+u$. $\blacksquare$

Es la versión abstracta de un hecho conocido: **solución general de $Ax=b$ = una solución particular + solución general del sistema homogéneo $Ax=0$**. Consecuencia inmediata: si $\operatorname{Nu}(T)=\{0_V\}$, cada $w$ tiene a lo sumo una preimagen; si $\operatorname{Nu}(T)\neq\{0_V\}$, cada $w\in\operatorname{Im}(T)$ tiene infinitas (sobre $\mathbb{R}$).

### Ejemplo 4 · Preimágenes en ℝ⁴
<!-- check: U2.T02.E4 -->

Con la TL del ejemplo 1, hallar todas las preimágenes de $(2,3,5)$ y de $(1,0,0)$.

**Preimágenes de $(2,3,5)$.** Como $5=2+3$, el vector está en el plano imagen $z=x+y$: tiene preimágenes. Resolvemos $Ax=(2,3,5)$ con las mismas operaciones de fila del ejemplo 1:

$$
\left(\begin{array}{cccc|c}1&1&0&-1&2\\1&2&1&0&3\\2&3&1&-1&5\end{array}\right)\sim\left(\begin{array}{cccc|c}1&0&-1&-2&1\\0&1&1&1&1\\0&0&0&0&0\end{array}\right).
$$

Con $x_3=x_4=0$ obtenemos la solución particular $v_p=(1,1,0,0)$, y

$$
\{v:\ T(v)=(2,3,5)\}=(1,1,0,0)+\operatorname{gen}\{(1,-1,1,0),\ (2,-1,0,1)\}.
$$

Corroboramos: $T(1,1,0,0)=(1+1,\ 1+2,\ 2+3)=(2,3,5)$.

**Preimágenes de $(1,0,0)$.** No cumple $z=x+y$ (sería $0=1$), así que no está en la imagen y no tiene preimágenes. En la matriz ampliada se ve como una fila $(0\ 0\ 0\ 0\mid -1)$ al escalonar: el sistema es incompatible.

## Una figura: la proyección sobre una recta

Sean las rectas $L=\operatorname{gen}\{(2,1)\}$ y $N=\operatorname{gen}\{(1,1)\}$ de $\mathbb{R}^2$. Todo vector se escribe de manera única como $v=\ell+n$ con $\ell\in L$ y $n\in N$; la **proyección sobre $L$ en la dirección de $N$** es $P(v)=\ell$.

### Ejemplo 5 · Núcleo e imagen de una proyección
<!-- check: U2.T02.E5 -->

Hallar la fórmula de $P$, su núcleo y su imagen.

Escribimos $(x,y)=\alpha(2,1)+\beta(1,1)$: de $2\alpha+\beta=x$ y $\alpha+\beta=y$ sale $\alpha=x-y$ y $\beta=-x+2y$. Luego

$$
P(x,y)=(x-y)\,(2,1)=(2x-2y,\ x-y),\qquad\text{de matriz}\quad\begin{pmatrix}2&-2\\1&-1\end{pmatrix}.
$$

- $\operatorname{Nu}(P)$: $2x-2y=0$ y $x-y=0$, o sea $x=y$. $\operatorname{Nu}(P)=\operatorname{gen}\{(1,1)\}=N$.
- $\operatorname{Im}(P)$: las columnas $(2,1)$ y $(-2,-1)$ son proporcionales. $\operatorname{Im}(P)=\operatorname{gen}\{(2,1)\}=L$.

Por ejemplo, $P(3,1)=(4,2)$ y $v-P(v)=(-1,-1)\in N$. Todos los puntos de la recta $(3,1)+N$ tienen la misma imagen: $P(2,0)=(4,2)$ y $P(4,2)=(4,2)$. Además, proyectar dos veces es lo mismo que proyectar una: $P\circ P=P$.

<figure class="math-figure">
<svg viewBox="-140 -140 340 250" role="img" aria-labelledby="nei-proy-t nei-proy-d" xmlns="http://www.w3.org/2000/svg">
<title id="nei-proy-t">Núcleo e imagen de una proyección del plano</title>
<desc id="nei-proy-d">La recta imagen L generada por (2,1), la recta núcleo N generada por (1,1), el vector v=(3,1) y su proyección P(v)=(4,2). La recta punteada que pasa por v paralela a N está formada por todas las preimágenes de P(v).</desc>
<defs><marker id="nei-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker><marker id="nei-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="scale(1,-1)">
<line class="grid" x1="-120" y1="30" x2="180" y2="30"/>
<line class="grid" x1="-120" y1="60" x2="180" y2="60"/>
<line class="grid" x1="-120" y1="90" x2="180" y2="90"/>
<line class="grid" x1="-120" y1="-30" x2="180" y2="-30"/>
<line class="grid" x1="-120" y1="-60" x2="180" y2="-60"/>
<line class="grid" x1="30" y1="-90" x2="30" y2="120"/>
<line class="grid" x1="60" y1="-90" x2="60" y2="120"/>
<line class="grid" x1="90" y1="-90" x2="90" y2="120"/>
<line class="grid" x1="120" y1="-90" x2="120" y2="120"/>
<line class="grid" x1="150" y1="-90" x2="150" y2="120"/>
<line class="grid" x1="-30" y1="-90" x2="-30" y2="120"/>
<line class="grid" x1="-60" y1="-90" x2="-60" y2="120"/>
<line class="grid" x1="-90" y1="-90" x2="-90" y2="120"/>
<line class="axis" x1="-120" y1="0" x2="180" y2="0"/>
<line class="axis" x1="0" y1="-90" x2="0" y2="120"/>
<line class="line-a" x1="-120" y1="-60" x2="180" y2="90"/>
<line class="line-b" x1="-90" y1="-90" x2="120" y2="120"/>
<line class="guide" x1="30" y1="-30" x2="150" y2="90"/>
<line class="vec-c" x1="0" y1="0" x2="90" y2="30" marker-end="url(#nei-arrow-c)"/>
<line class="vec-a" x1="0" y1="0" x2="120" y2="60" marker-end="url(#nei-arrow-a)"/>
<circle class="dot-c" cx="60" cy="0" r="3"/>
</g>
<text class="math" x="96" y="-20">v</text>
<text class="math" x="100" y="-68">P(v)</text>
<text x="132" y="-100">L = Im(P)</text>
<text x="30" y="-124">N = Nu(P)</text>
<text class="small" x="64" y="14">(2,0)</text>
</svg>
<figcaption>La imagen es la recta L y el núcleo es la recta N. Cada vector se proyecta sobre L moviéndose en la dirección de N: la recta punteada, paralela a N y que pasa por v=(3,1), está formada por todas las preimágenes de P(v)=(4,2), entre ellas (2,0). Es la estructura v_p + Nu(P) del teorema anterior.</figcaption>
</figure>

:::caution[Errores frecuentes]
- **Tomar como base de la imagen las filas de la matriz de la TL.** En el ejemplo 1, la fila $(1,0,-1,-2)$ de la forma escalonada está en $\mathbb{R}^4$, que ni siquiera es el espacio de llegada. Las filas de $A$ generan $\operatorname{fil}(A)\subseteq K^n$; la imagen es $\operatorname{col}(A)\subseteq K^m$.
- **Tomar las columnas de la forma escalonada en lugar de las originales.** En el ejemplo 1, la forma escalonada reducida tiene columna $(1,0,0)$, que no está en la imagen ($0\neq 1+0$). Hay que tomar las columnas **de $A$** en las posiciones de los pivotes.
- **Dar el núcleo como lista de números cuando $V$ es de polinomios o de matrices.** En el ejemplo 3 el núcleo está formado por matrices; las cuaternas $(1,0,0,-1)$ y $(0,1,1,0)$ son solo sus coordenadas.
- **Olvidar que los transformados de un generador pueden ser LD.** En el ejemplo 3 son cuatro polinomios pero la imagen tiene dimensión 2.
- **Confundir "$T(v)=0$" con "$v=0$".** Que $T(v)=0_W$ no implica $v=0_V$: es justamente lo que mide el núcleo.
:::

## Autoevaluación

1. Hallar el núcleo y la imagen de $T:P_2[\mathbb{R}]\to\mathbb{R}$, $T(p)=p(1)$.

<details>
<summary>Respuesta</summary>

$\operatorname{Nu}(T)=\{p:\ p(1)=0\}$, que son los múltiplos de $(x-1)$ en $P_2[\mathbb{R}]$: base $\{x-1,\ x^2-1\}$ (se obtiene de $a+b+c=0$, con $a=-b-c$). $\operatorname{Im}(T)=\mathbb{R}$, porque $T(t)=t$ para el polinomio constante $t$.

</details>

2. Si $T(v_1)=w$ y $T(v_2)=w$ con $v_1\neq v_2$, ¿qué se puede decir del núcleo?

<details>
<summary>Respuesta</summary>

Que no es trivial: $T(v_1-v_2)=w-w=0_W$ con $v_1-v_2\neq 0_V$.

</details>

3. ¿Puede la imagen de una TL de $\mathbb{R}^3$ en $\mathbb{R}^3$ ser el plano $x+y+z=1$?

<details>
<summary>Respuesta</summary>

No: ese plano no pasa por el origen, así que no es subespacio, y la imagen siempre lo es.

</details>

:::tip[En resumen]
- $\operatorname{Nu}(T)=\{v:\ T(v)=0_W\}\subseteq V$ e $\operatorname{Im}(T)=\{T(v):\ v\in V\}\subseteq W$ son subespacios.
- El núcleo se calcula resolviendo el sistema homogéneo $T(v)=0_W$.
- La imagen está generada por los transformados de cualquier generador de $V$; se depura escalonando.
- Para $T(x)=Ax$: $\operatorname{Nu}(T)=\operatorname{nul}(A)$ e $\operatorname{Im}(T)=\operatorname{col}(A)$.
- Si $T(v_p)=w$, las preimágenes de $w$ son exactamente $v_p+\operatorname{Nu}(T)$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 6.5, "El kernel y el rango de una transformación lineal" (p. 499). Atención: Poole llama "kernel" al núcleo y "rango" a la imagen; en este curso "rango" se reserva para matrices.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: la sección sobre espacios nulos, espacios columna y transformaciones lineales.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed.: sección 5.4 (p. 195).
- Antes: [2.1 Definición y ejemplos](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/), [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/) y el repaso de [sistemas lineales](/algebra-ii/repaso/sistemas-lineales/).
- Después: [2.3 Teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/).
