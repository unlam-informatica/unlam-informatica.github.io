---
title: Coordenadas
description: Teorema de existencia y unicidad de coordenadas, vector de coordenadas en una base ordenada, linealidad de las coordenadas y su uso en polinomios, matrices y ℤ₂ⁿ.
slug: algebra-ii/unidad-1/teoria/coordenadas
sidebar:
  order: 8
  label: 1.8 Coordenadas
---

## Para qué sirve

Una base permite describir cada vector con una lista de números: cuánto de cada vector de la base
hace falta para construirlo. Esa lista, las **coordenadas**, convierte cualquier espacio de
dimensión $n$ (polinomios, matrices, subespacios de $\mathbb{R}^5$) en $K^n$, donde sabemos
calcular con matrices y escalonamiento.

En un código lineal la idea aparece de forma literal: si $g_1,\dots,g_k$ es una base del código, la
palabra transmitida $u=a_1g_1+\dots+a_kg_k$ tiene $n$ bits, pero sus coordenadas
$(a_1,\dots,a_k)$ son los $k$ bits del mensaje
(ver [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/)). Codificar es pasar de
coordenadas a vector; decodificar es volver.

Partimos de [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/).

## Intuición: medir con otra grilla

En $\mathbb{R}^2$, las coordenadas usuales de $v=(3,4)$ dicen "3 pasos en dirección $e_1$ y 4 en
dirección $e_2$". Si en lugar de $e_1,e_2$ usamos $b_1=(2,1)$ y $b_2=(-1,2)$, la grilla se inclina y
el mismo $v$ se alcanza con 2 pasos de $b_1$ y 1 de $b_2$, porque $2(2,1)+1(-1,2)=(3,4)$. El vector
es el mismo; cambian los números con que lo describimos.

<figure class="math-figure">
<svg viewBox="-90 -180 255 235" role="img" aria-labelledby="co-t co-d" xmlns="http://www.w3.org/2000/svg">
<title id="co-t">Coordenadas en una base no canónica de ℝ²</title>
<desc id="co-d">Grilla oblicua formada por rectas paralelas a b1=(2,1) y a b2=(-1,2). El vector v=(3,4) se alcanza avanzando dos veces b1 y una vez b2, por lo que sus coordenadas en B son 2 y 1.</desc>
<defs><marker id="co-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker><marker id="co-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker><marker id="co-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="scale(1,-1)">
<line class="grid" x1="-52.5" y1="-45" x2="-75" y2="0"/>
<line class="grid" x1="60" y1="-45" x2="150" y2="0"/>
<line class="grid" x1="22.5" y1="-45" x2="-75" y2="150"/>
<line class="grid" x1="-75" y1="-37.5" x2="150" y2="75"/>
<line class="grid" x1="97.5" y1="-45" x2="-7.5" y2="165"/>
<line class="grid" x1="-75" y1="37.5" x2="150" y2="150"/>
<line class="grid" x1="150" y1="0" x2="67.5" y2="165"/>
<line class="grid" x1="-75" y1="112.5" x2="30" y2="165"/>
<line class="grid" x1="150" y1="150" x2="142.5" y2="165"/>
<line class="axis" x1="-75" y1="0" x2="150" y2="0"/>
<line class="axis" x1="0" y1="-45" x2="0" y2="165"/>
<line class="guide" x1="0" y1="0" x2="120" y2="60"/>
<line class="guide" x1="120" y1="60" x2="90" y2="120"/>
<line class="vec-a" x1="0" y1="0" x2="60" y2="30" marker-end="url(#co-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="-30" y2="60" marker-end="url(#co-arrow-b)"/>
<line class="vec-c" x1="0" y1="0" x2="90" y2="120" marker-end="url(#co-arrow-c)"/>
<circle class="dot-a" cx="120" cy="60" r="3"/>
</g>
<text class="math" x="57" y="-13.5">b₁</text>
<text class="math" x="-52.5" y="-51">b₂</text>
<text class="math" x="94.5" y="-124.5">v</text>
<text class="math" x="124.5" y="-48">2b₁</text>
<text class="small" x="136.5" y="12">x</text>
<text class="small" x="4.5" y="-156">y</text>
</svg>
<figcaption>La base B={b₁,b₂} con b₁=(2,1) y b₂=(−1,2) define una grilla oblicua. Para llegar a v=(3,4) avanzamos 2 veces b₁ (hasta el punto 2b₁) y 1 vez b₂: por eso [v]<sub>B</sub> tiene componentes 2 y 1, mientras que sus componentes en la base canónica son 3 y 4.</figcaption>
</figure>

## Existencia y unicidad

:::note[Teorema de existencia y unicidad de coordenadas]
Sea $V$ un espacio vectorial sobre $K$ y $B=\{v_1,\dots,v_n\}$ una base de $V$. Para cada $v\in V$
existen escalares $\alpha_1,\dots,\alpha_n\in K$, **únicos**, tales que

$$
v=\alpha_1v_1+\alpha_2v_2+\dots+\alpha_nv_n .
$$
:::

**Demostración.** *Existencia.* $B$ genera $V$, así que $v$ es combinación lineal de
$v_1,\dots,v_n$.

*Unicidad.* Supongamos $v=\alpha_1v_1+\dots+\alpha_nv_n=\beta_1v_1+\dots+\beta_nv_n$. Restando,

$$
(\alpha_1-\beta_1)v_1+\dots+(\alpha_n-\beta_n)v_n=0 .
$$

Como $B$ es linealmente independiente, todos los coeficientes son nulos: $\alpha_i=\beta_i$ para
cada $i$. $\blacksquare$

Cada hipótesis cumple un papel: la generación da la existencia y la independencia da la unicidad.
Con un generador dependiente la escritura existe pero no es única. Por ejemplo,
$\{(1,0),(0,1),(1,1)\}$ genera $\mathbb{R}^2$ y

$$
(2,3)=2(1,0)+3(0,1)+0(1,1)=1(1,0)+2(0,1)+1(1,1),
$$

así que no tiene sentido hablar de "las" coordenadas de $(2,3)$ respecto de ese conjunto. Con un
conjunto independiente que no genera, la escritura es única cuando existe, pero hay vectores que no
se pueden escribir.

:::note[Definición]
Los escalares $\alpha_1,\dots,\alpha_n$ del teorema son las **coordenadas** de $v$ respecto de la
base ordenada $B$. El **vector de coordenadas** de $v$ en $B$ es la matriz columna

$$
[v]_B=\begin{pmatrix}\alpha_1\\ \alpha_2\\ \vdots\\ \alpha_n\end{pmatrix}\in K^{n}.
$$
:::

Tres observaciones que conviene fijar desde el principio:

- **El orden importa.** Si $B=\{b_1,b_2\}$ y $B'=\{b_2,b_1\}$, entonces $[v]_{B'}$ es $[v]_B$ con las
  componentes intercambiadas. En el ejemplo de la figura, $[v]_B=\begin{pmatrix}2\\1\end{pmatrix}$
  y $[v]_{B'}=\begin{pmatrix}1\\2\end{pmatrix}$.
- **El tamaño de $[v]_B$ es la dimensión del espacio de la base**, no la cantidad de componentes de
  $v$. Un vector de un plano de $\mathbb{R}^3$ tiene dos coordenadas respecto de una base del plano;
  un polinomio de $P_2[\mathbb{R}]$ tiene tres; una matriz simétrica $2\times2$ tiene tres respecto
  de una base de las simétricas, aunque tenga cuatro entradas.
- **En la base canónica de $K^n$, coordenadas y componentes coinciden**: $[v]_E$ es $v$ escrito en
  columna. En cualquier otra base hay que calcular.

## Cómo se calculan

Hallar $[v]_B$ es resolver la ecuación $\alpha_1v_1+\dots+\alpha_nv_n=v$. En $K^n$ es el sistema de
matriz ampliada $(v_1\ \cdots\ v_n\mid v)$, con los vectores de la base en columnas; por el teorema,
si $v$ está en el espacio generado por $B$ el sistema tiene solución única. En polinomios o matrices
se igualan coeficientes o entradas y se llega a un sistema del mismo tipo.

El camino inverso no requiere resolver nada: si $[v]_B=(\alpha_1,\dots,\alpha_n)^t$, entonces
$v=\alpha_1v_1+\dots+\alpha_nv_n$.

## Las coordenadas son lineales

:::note[Propiedad]
Para todo $u,v\in V$ y $\lambda\in K$:

$$
[u+v]_B=[u]_B+[v]_B,\qquad [\lambda v]_B=\lambda\,[v]_B .
$$

Además, $[v]_B=0$ si y solo si $v=0_V$.
:::

**Demostración.** Si $u=\sum\alpha_iv_i$ y $v=\sum\beta_iv_i$, entonces
$u+v=\sum(\alpha_i+\beta_i)v_i$ y $\lambda v=\sum(\lambda\beta_i)v_i$. Por la unicidad, esas son las
coordenadas de $u+v$ y de $\lambda v$. Si $[v]_B=0$, $v=0v_1+\dots+0v_n=0_V$; y $0_V=0v_1+\dots+0v_n$
es la única escritura del nulo. $\blacksquare$

Por inducción, $[\lambda_1w_1+\dots+\lambda_kw_k]_B=\lambda_1[w_1]_B+\dots+\lambda_k[w_k]_B$.

:::note[Teorema]
Sea $B$ una base de $V$ y $w_1,\dots,w_k\in V$.

1. $\{w_1,\dots,w_k\}$ es linealmente independiente en $V$ si y solo si
   $\{[w_1]_B,\dots,[w_k]_B\}$ es linealmente independiente en $K^n$.
2. $w\in\operatorname{gen}\{w_1,\dots,w_k\}$ si y solo si
   $[w]_B\in\operatorname{gen}\{[w_1]_B,\dots,[w_k]_B\}$, con los mismos coeficientes.
:::

**Demostración.** Por la linealidad,
$[\lambda_1w_1+\dots+\lambda_kw_k]_B=\lambda_1[w_1]_B+\dots+\lambda_k[w_k]_B$. Como un vector es nulo
si y solo si su vector de coordenadas es nulo,
$\lambda_1w_1+\dots+\lambda_kw_k=0\iff\lambda_1[w_1]_B+\dots+\lambda_k[w_k]_B=0$: las relaciones
lineales entre los $w_j$ y entre sus coordenadas son exactamente las mismas, lo que da 1. Para 2,
$w=\sum\lambda_jw_j$ equivale a $[w]_B=\sum\lambda_j[w_j]_B$ porque dos vectores son iguales si y
solo si tienen las mismas coordenadas. $\blacksquare$

Este teorema justifica un procedimiento que usamos todo el tiempo: para estudiar independencia,
generadores, bases o dimensión en $P_n[\mathbb{R}]$ o en $\mathbb{R}^{m\times n}$, pasamos a
coordenadas en la base canónica y trabajamos con matrices en $K^n$. Al final, volvemos a escribir
los resultados como polinomios o matrices.

## Ejemplos resueltos

### Ejemplo 1 · Coordenadas en una base no canónica de ℝ²

<!-- check: U1.T08.E1 -->

Sea $B=\{b_1,b_2\}$ con $b_1=(2,1)$ y $b_2=(-1,2)$. Probar que $B$ es base de $\mathbb{R}^2$, hallar
$[v]_B$ para $v=(3,4)$ y hallar el vector $w$ con $[w]_B=\begin{pmatrix}-1\\3\end{pmatrix}$.

**Base.** Son dos vectores no proporcionales de $\mathbb{R}^2$, que tiene dimensión 2: forman base.

**Coordenadas de $v$.** Resolvemos $\alpha(2,1)+\beta(-1,2)=(3,4)$:

$$
\left(\begin{array}{cc|c} 2&-1&3\\1&2&4 \end{array}\right)
\xrightarrow{F_1\leftrightarrow F_2}
\left(\begin{array}{cc|c} 1&2&4\\2&-1&3 \end{array}\right)
\xrightarrow{F_2-2F_1\to F_2}
\left(\begin{array}{cc|c} 1&2&4\\0&-5&-5 \end{array}\right).
$$

Entonces $\beta=1$ y $\alpha=4-2\beta=2$: $[v]_B=\begin{pmatrix}2\\1\end{pmatrix}$, como muestra la
figura.

**Vector a partir de sus coordenadas.** $w=-1\,b_1+3\,b_2=(-2,-1)+(-3,6)=(-5,5)$.

**Comprobación.** $2(2,1)+1(-1,2)=(3,4)$. Para $w$, resolviendo $\alpha(2,1)+\beta(-1,2)=(-5,5)$ se
obtiene $\alpha=-1$, $\beta=3$.

:::tip[Resultado]
$[v]_B=\begin{pmatrix}2\\1\end{pmatrix}$ (y $[v]_E=\begin{pmatrix}3\\4\end{pmatrix}$); $w=(-5,5)$.
:::

### Ejemplo 2 · Coordenadas dentro de un plano de ℝ³

<!-- check: U1.T08.E2 -->

Sea $S=\{(x,y,z)\in\mathbb{R}^3: x-y-z=0\}$ y $B_S=\{(1,0,1),(0,1,-1)\}$. Verificar que $B_S$ es
base de $S$, hallar $[v]_{B_S}$ para $v=(2,3,-1)$ y decidir si $w=(1,1,1)$ tiene coordenadas en
$B_S$.

**Base.** $S=\operatorname{nul}\begin{pmatrix}1&-1&-1\end{pmatrix}$ tiene dimensión $3-1=2$. Los dos
vectores están en $S$ ($1-0-1=0$ y $0-1+1=0$) y no son proporcionales: son 2 vectores
independientes en un espacio de dimensión 2, luego forman base.

**Coordenadas de $v$.** Primero, $v\in S$ porque $2-3+1=0$. De
$\alpha(1,0,1)+\beta(0,1,-1)=(2,3,-1)$, las dos primeras componentes dan $\alpha=2$, $\beta=3$, y la
tercera se cumple: $2-3=-1$. Así $[v]_{B_S}=\begin{pmatrix}2\\3\end{pmatrix}$: **dos** coordenadas,
aunque $v$ tenga tres componentes.

**El vector $w$.** $1-1-1=-1\neq0$, así que $w\notin S$. El sistema
$\alpha(1,0,1)+\beta(0,1,-1)=(1,1,1)$ exige $\alpha=1$, $\beta=1$ y $\alpha-\beta=1$, que es
incompatible: $w$ no tiene coordenadas en $B_S$, porque $B_S$ no es base de $\mathbb{R}^3$.

**Comprobación.** $2(1,0,1)+3(0,1,-1)=(2,3,-1)$.

:::tip[Resultado]
$[v]_{B_S}=\begin{pmatrix}2\\3\end{pmatrix}$; $[w]_{B_S}$ no existe porque $w\notin S$.
:::

### Ejemplo 3 · Coordenadas de un polinomio

<!-- check: U1.T08.E3 -->

En $P_2[\mathbb{R}]$ sea $B=\{1,\ 1+x,\ 1+x+x^2\}$ (en ese orden). Hallar $[p]_B$ para
$p=3-x+2x^2$.

Planteamos $p=\alpha\cdot1+\beta(1+x)+\gamma(1+x+x^2)=(\alpha+\beta+\gamma)+(\beta+\gamma)x+\gamma x^2$
e igualamos coeficientes:

$$
\begin{cases}
\alpha+\beta+\gamma=3\\
\beta+\gamma=-1\\
\gamma=2
\end{cases}
$$

De abajo hacia arriba: $\gamma=2$, $\beta=-3$, $\alpha=3-(-3)-2=4$. El sistema tiene solución única
para cualquier $p$ (es triangular con unos en la diagonal), lo que prueba de paso que $B$ es base.

**Comprobación.** $4-3(1+x)+2(1+x+x^2)=(4-3+2)+(-3+2)x+2x^2=3-x+2x^2$.

:::tip[Resultado]
$[p]_B=\begin{pmatrix}4\\-3\\2\end{pmatrix}$, mientras que en la base canónica
$[p]_E=\begin{pmatrix}3\\-1\\2\end{pmatrix}$.
:::

### Ejemplo 4 · Coordenadas de una matriz simétrica

<!-- check: U1.T08.E4 -->

Sea $\mathcal S$ el subespacio de matrices simétricas de $\mathbb{R}^{2\times2}$ y

$$
B=\left\{M_1=\begin{pmatrix}1&1\\1&0\end{pmatrix},\ M_2=\begin{pmatrix}0&1\\1&1\end{pmatrix},\ M_3=\begin{pmatrix}1&0\\0&1\end{pmatrix}\right\}.
$$

Probar que $B$ es base de $\mathcal S$ y hallar $[M]_B$ para $M=\begin{pmatrix}3&1\\1&2\end{pmatrix}$.

**Base.** Las tres matrices son simétricas y $\dim\mathcal S=3$
(ver [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/)), así que basta ver
independencia. En general,

$$
aM_1+bM_2+cM_3=\begin{pmatrix}a+c&a+b\\a+b&b+c\end{pmatrix}.
$$

Si es la matriz nula, $a+c=0$, $a+b=0$, $b+c=0$; sumando las tres, $2(a+b+c)=0$, y restando cada
ecuación de $a+b+c=0$ queda $a=b=c=0$.

**Coordenadas de $M$.** Igualamos entradas: $a+c=3$, $a+b=1$, $b+c=2$. Sumando, $a+b+c=3$; luego
$b=3-3=0$, $c=3-1=2$, $a=3-2=1$.

**Comprobación.** $1\cdot M_1+0\cdot M_2+2\cdot M_3=\begin{pmatrix}1+2&1\\1&0+2\end{pmatrix}=M$.

:::tip[Resultado]
$[M]_B=\begin{pmatrix}1\\0\\2\end{pmatrix}$: tres coordenadas, porque $\dim\mathcal S=3$.
:::

### Ejemplo 5 · Coordenadas en ℤ₂³

<!-- check: U1.T08.E5 -->

En $\mathbb{Z}_2^3$ sea $B=\{(1,1,0),(0,1,1),(1,1,1)\}$. Probar que es base y hallar $[v]_B$ para
$v=(1,0,1)$.

**Base.** Si $a(1,1,0)+b(0,1,1)+c(1,1,1)=(a+c,\ a+b+c,\ b+c)=(0,0,0)$, entonces $a=c$ y $b=c$ (en
$\mathbb{Z}_2$, $a+c=0$ significa $a=c$), y la segunda ecuación queda $c+c+c=c=0$. Así $a=b=c=0$:
son 3 vectores independientes en un espacio de dimensión 3.

**Coordenadas.** Ahora $(a+c,\ a+b+c,\ b+c)=(1,0,1)$. Sumando la primera y la tercera ecuación,
$a+b=0$, es decir, $a=b$; la segunda da entonces $c=0$, y de la primera $a=1$, así que $b=1$.

**Comprobación.** $(1,1,0)+(0,1,1)=(1,0,1)$ en $\mathbb{Z}_2^3$.

:::tip[Resultado]
$[v]_B=\begin{pmatrix}1\\1\\0\end{pmatrix}$.
:::

Sobre $\mathbb{Z}_2$, cada vector de coordenadas es una cadena de bits. La función
$v\mapsto[v]_B$ es una biyección entre $\mathbb{Z}_2^3$ y $\mathbb{Z}_2^3$ que "renombra" los
$8$ vectores; es la misma biyección que usamos para contar elementos en
[base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/).

### Ejemplo 6 · Independencia y pertenencia a través de coordenadas

<!-- check: U1.T08.E6 -->

En $P_2[\mathbb{R}]$ sean $p_1=1+x$, $p_2=x+x^2$, $p_3=1+2x+x^2$. Decidir si $\{p_1,p_2,p_3\}$ es
independiente y si $q=2+3x+x^2$ y $r=1+x^2$ pertenecen a $\operatorname{gen}\{p_1,p_2,p_3\}$.

**Paso a coordenadas.** En $E=\{1,x,x^2\}$:
$[p_1]_E=(1,1,0)^t$, $[p_2]_E=(0,1,1)^t$, $[p_3]_E=(1,2,1)^t$, $[q]_E=(2,3,1)^t$, $[r]_E=(1,0,1)^t$.
Escalonamos con esas columnas (las tres primeras, y las de $q$ y $r$ como columnas ampliadas):

$$
\left(\begin{array}{ccc|c|c} 1&0&1&2&1\\1&1&2&3&0\\0&1&1&1&1 \end{array}\right)
\xrightarrow{F_2-F_1\to F_2}
\left(\begin{array}{ccc|c|c} 1&0&1&2&1\\0&1&1&1&-1\\0&1&1&1&1 \end{array}\right)
\xrightarrow{F_3-F_2\to F_3}
\left(\begin{array}{ccc|c|c} 1&0&1&2&1\\0&1&1&1&-1\\0&0&0&0&2 \end{array}\right).
$$

**Lectura.** Las columnas pivote son la 1 y la 2: las coordenadas tienen rango 2, así que
$\{p_1,p_2,p_3\}$ es **dependiente**, con $[p_3]_E=[p_1]_E+[p_2]_E$, es decir, $p_3=p_1+p_2$. La
columna de $q$ no genera pivote: $q=2p_1+p_2$. La columna de $r$ produce la fila
$(0\ 0\ 0\mid 2)$: el sistema es incompatible y $r\notin\operatorname{gen}\{p_1,p_2,p_3\}$.

**Comprobación.** $p_1+p_2=1+2x+x^2=p_3$ y $2(1+x)+(x+x^2)=2+3x+x^2=q$.

:::tip[Resultado]
$\{p_1,p_2,p_3\}$ es dependiente ($p_3=p_1+p_2$); $q=2p_1+p_2$ pertenece al generado y $r$ no.
:::

## Interpretación

- **Geométrica.** Una base de $\mathbb{R}^2$ o $\mathbb{R}^3$ define una grilla (en general
  oblicua) y las coordenadas son la "dirección postal" del punto en esa grilla.
- **Algebraica.** Fijada una base de $V$ con $n$ vectores, $v\mapsto[v]_B$ es una correspondencia
  biyectiva entre $V$ y $K^n$ que respeta suma y producto por escalar. En la Unidad 2 se dirá que
  es un **isomorfismo**: todo espacio de dimensión $n$ sobre $K$ "es" $K^n$ una vez elegida una base.
- **Computacional.** Un programa que trabaje con polinomios de grado $\le2$ los guarda como arreglos
  de tres números: está usando coordenadas en la base canónica. Cambiar de base es cambiar de
  formato de representación, que es el tema de la lección siguiente.

## Errores frecuentes

:::caution[Errores frecuentes]
- **Confundir el vector con sus coordenadas.** En el ejemplo 1, $v=(3,4)$ y
  $[v]_B=\begin{pmatrix}2\\1\end{pmatrix}$; escribir "$v=(2,1)$" es falso.
- **Olvidar el orden.** Con $B=\{(-1,2),(2,1)\}$, el mismo $v=(3,4)$ tiene
  $[v]_B=\begin{pmatrix}1\\2\end{pmatrix}$.
- **Dar coordenadas respecto de un conjunto que no es base.** Con $\{(1,0),(0,1),(1,1)\}$ el vector
  $(2,3)$ admite infinitas escrituras; "sus coordenadas" no están definidas.
- **Calcular coordenadas de un vector que no está en el subespacio.** En el ejemplo 2, $w=(1,1,1)$
  no tiene coordenadas en $B_S$; un sistema incompatible no es un error de cuentas, es la respuesta.
- **Dar $[v]_{B_S}$ con tantas componentes como el espacio ambiente.** Para un plano de
  $\mathbb{R}^3$ son 2 coordenadas, no 3.
- **Tratar polinomios como ternas al concluir.** Las ternas de coeficientes son una herramienta de
  cálculo; la respuesta "$p_3=p_1+p_2$" se da con polinomios.
:::

## Autoevaluación

1. Si $[v]_B=\begin{pmatrix}0\\1\\0\end{pmatrix}$ con $B=\{v_1,v_2,v_3\}$, ¿quién es $v$?
2. ¿Puede un vector no nulo tener vector de coordenadas nulo?
3. En $\mathbb{R}^{2\times2}$ con la base canónica $E=\{E_{11},E_{12},E_{21},E_{22}\}$, ¿cuál es
   $\left[\begin{pmatrix}5&-1\\0&2\end{pmatrix}\right]_E$?

<details>
<summary>Respuestas</summary>

1. $v=v_2$.
2. No: $[v]_B=0$ implica $v=0v_1+\dots+0v_n=0_V$.
3. $\begin{pmatrix}5\\-1\\0\\2\end{pmatrix}$, leyendo las entradas en el orden de la base.

</details>

## Resumen

:::tip[En resumen]
- Respecto de una base ordenada $B$, cada vector tiene coordenadas únicas: la generación da
  existencia y la independencia, unicidad.
- $[v]_B$ es una columna con $\dim V$ componentes, que depende del orden de la base.
- $[u+v]_B=[u]_B+[v]_B$, $[\lambda v]_B=\lambda[v]_B$, y $[v]_B=0\iff v=0$.
- Independencia, generación y pertenencia se deciden igual en $V$ que en las coordenadas: así se
  trabaja en polinomios y matrices.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 6.2, "Independencia lineal,
  bases y dimensión", p. 461 (coordenadas y su unicidad).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: sistemas de coordenadas.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed., sección 4.2, p. 148.
- Lecciones relacionadas: [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/)
  (anterior), [cambio de coordenadas](/algebra-ii/unidad-1/teoria/cambio-de-coordenadas/)
  (siguiente) y [matriz asociada](/algebra-ii/unidad-2/teoria/matriz-asociada/), donde las
  coordenadas permiten representar transformaciones lineales con matrices.
