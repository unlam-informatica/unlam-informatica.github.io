---
title: Ortogonalidad
description: Conjuntos ortogonales y ortonormales, independencia lineal, coordenadas en una base ortogonal y matrices con columnas ortonormales.
slug: algebra-ii/unidad-4/teoria/ortogonalidad
sidebar:
  order: 3
  label: 4.3 Ortogonalidad
---

Calcular las coordenadas de un vector en una base cualquiera exige resolver un sistema lineal. Si la base es **ortogonal**, cada coordenada se obtiene con un solo producto interno y un cociente, sin resolver nada. Esa simplificación es la razón por la que las bases ortogonales son la herramienta central de la unidad: las proyecciones de la [lección 4.6](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/), los cuadrados mínimos de la [4.7](/algebra-ii/unidad-4/teoria/cuadrados-minimos/) y el método de Gram-Schmidt de la [4.4](/algebra-ii/unidad-4/teoria/gram-schmidt/) se apoyan en ellas.

En toda la lección, $(V,\langle\,,\rangle)$ es un espacio euclídeo (ver [4.1](/algebra-ii/unidad-4/teoria/producto-interno/) y [4.2](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/)).

## Vectores y conjuntos ortogonales

Recordemos que $u\perp v$ significa $\langle u,v\rangle=0$. El vector nulo es ortogonal a todos los vectores, incluso a sí mismo, y es el único vector ortogonal a sí mismo: $\langle u,u\rangle=0$ implica $u=0_V$ por positividad.

:::note[Definición (conjunto ortogonal y ortonormal)]
Un conjunto $\{u_1,\dots,u_k\}\subset V$ de vectores **no nulos** es:

- **ortogonal** si $\langle u_i,u_j\rangle=0$ para todo $i\neq j$;
- **ortonormal** si es ortogonal y además $\lVert u_i\rVert=1$ para todo $i$, es decir, $\langle u_i,u_j\rangle=\delta_{ij}$ (vale $1$ si $i=j$ y $0$ si $i\neq j$).

Una **base ortogonal** (respectivamente **ortonormal**) es una base que es un conjunto ortogonal (respectivamente ortonormal).
:::

Para pasar de un conjunto ortogonal a uno ortonormal alcanza con **normalizar** cada vector: si $\{u_1,\dots,u_k\}$ es ortogonal, entonces $\left\{\dfrac{u_1}{\lVert u_1\rVert},\dots,\dfrac{u_k}{\lVert u_k\rVert}\right\}$ es ortonormal. En efecto, multiplicar por un escalar no altera la ortogonalidad, porque $\langle au_i,bu_j\rangle=ab\langle u_i,u_j\rangle$, y cada vector dividido por su norma tiene norma $1$.

Todo depende del producto interno elegido. En $\mathbb{R}^2$ con el producto usual, $\{(1,0),(0,1)\}$ es ortonormal. Con el producto $\langle x,y\rangle=x_1y_1+(x_1+x_2)(y_1+y_2)$ de la lección 4.1 no lo es: $\langle e_1,e_2\rangle=1$ y $\lVert e_1\rVert=\sqrt2$.

## Ortogonales no nulos implican independientes

:::note[Teorema]
Todo conjunto ortogonal $\{u_1,\dots,u_k\}$ de vectores no nulos es linealmente independiente.
:::

**Demostración.** Sea $c_1u_1+\dots+c_ku_k=0_V$. Fijamos $j$ y hacemos el producto interno con $u_j$ de ambos lados. Por linealidad en la primera variable y por ortogonalidad,

$$
0=\langle c_1u_1+\dots+c_ku_k,\,u_j\rangle=c_1\langle u_1,u_j\rangle+\dots+c_k\langle u_k,u_j\rangle=c_j\langle u_j,u_j\rangle .
$$

Como $u_j\neq0_V$, es $\langle u_j,u_j\rangle>0$, y entonces $c_j=0$. Esto vale para cada $j$: la única combinación lineal nula es la trivial. $\blacksquare$

:::note[Corolario]
Si $\dim V=n$, todo conjunto ortogonal de $n$ vectores no nulos es una base ortogonal de $V$.
:::

Es el análogo de "$n$ vectores LI en un espacio de dimensión $n$ forman una base" (lección 1.7 de [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/)): para verificar que un conjunto es base ortogonal alcanza con comprobar que hay $n$ vectores no nulos y que son ortogonales dos a dos, sin calcular ningún determinante.

**La recíproca es falsa.** El conjunto $\{(1,0),(1,1)\}$ es linealmente independiente en $\mathbb{R}^2$, pero con el producto usual $(1,0)\cdot(1,1)=1\neq0$, de modo que no es ortogonal. La independencia lineal es una condición mucho más débil que la ortogonalidad.

## Coordenadas en una base ortogonal

:::note[Teorema (coordenadas respecto de una base ortogonal)]
Sea $B=\{u_1,\dots,u_n\}$ una base ortogonal de $V$. Para todo $v\in V$,

$$
v=\sum_{i=1}^n\frac{\langle v,u_i\rangle}{\langle u_i,u_i\rangle}\,u_i,\qquad\text{es decir,}\qquad[v]_B=\begin{pmatrix}\dfrac{\langle v,u_1\rangle}{\langle u_1,u_1\rangle}\\ \vdots\\ \dfrac{\langle v,u_n\rangle}{\langle u_n,u_n\rangle}\end{pmatrix}.
$$

Si $B$ es ortonormal, los denominadores valen $1$: $v=\sum_i\langle v,u_i\rangle u_i$ y $[v]_B=\big(\langle v,u_1\rangle,\dots,\langle v,u_n\rangle\big)^t$.
:::

**Demostración.** Por ser $B$ una base existen únicos escalares $c_1,\dots,c_n$ con $v=c_1u_1+\dots+c_nu_n$ (unicidad de coordenadas, lección [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/)). Hacemos el producto interno con $u_j$ y usamos que $\langle u_i,u_j\rangle=0$ si $i\neq j$:

$$
\langle v,u_j\rangle=\sum_{i=1}^nc_i\langle u_i,u_j\rangle=c_j\langle u_j,u_j\rangle\quad\Longrightarrow\quad c_j=\frac{\langle v,u_j\rangle}{\langle u_j,u_j\rangle},
$$

donde dividimos por $\langle u_j,u_j\rangle>0$. Si $B$ es ortonormal, $\langle u_j,u_j\rangle=1$. $\blacksquare$

La fórmula tiene una lectura geométrica: el término $\dfrac{\langle v,u_i\rangle}{\langle u_i,u_i\rangle}u_i$ es la proyección ortogonal de $v$ sobre la recta generada por $u_i$ (se formaliza en la lección 4.6), de modo que $v$ es la suma de sus proyecciones sobre los ejes de la base.

<figure class="math-figure">
<svg viewBox="-50 -120 170 140" role="img" aria-labelledby="or-t or-d" xmlns="http://www.w3.org/2000/svg">
<title id="or-t">Descomposición de un vector en una base ortogonal de R2</title>
<desc id="or-d">La base ortogonal u1=(2,1) y u2=(-1,2), y el vector v=(4,7), que es igual a 3 u1 más 2 u2. Los sumandos 3 u1 y 2 u2 forman un rectángulo con v como diagonal.</desc>
<defs>
<marker id="or-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker>
<marker id="or-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker>
<marker id="or-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker>
</defs>
<g transform="scale(1,-1)">
<line class="axis" x1="-45" y1="0" x2="110" y2="0"/>
<line class="axis" x1="0" y1="-8" x2="0" y2="108"/>
<line class="guide" x1="0" y1="0" x2="84" y2="42"/>
<line class="guide" x1="84" y1="42" x2="56" y2="98"/>
<line class="guide" x1="0" y1="0" x2="-28" y2="56"/>
<line class="guide" x1="-28" y1="56" x2="56" y2="98"/>
<polyline class="guide" points="7,3.5 3.5,10.5 -3.5,7"/>
<line class="vec-a" x1="0" y1="0" x2="28" y2="14" marker-end="url(#or-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="-14" y2="28" marker-end="url(#or-arrow-b)"/>
<line class="vec-c" x1="0" y1="0" x2="56" y2="98" marker-end="url(#or-arrow-c)"/>
</g>
<text class="math" x="32" y="-6">u₁</text>
<text class="math" x="-26" y="-30">u₂</text>
<text class="math" x="60" y="-100">v</text>
<text class="small" x="88" y="-40">3u₁</text>
<text class="small" x="-48" y="-58">2u₂</text>
</svg>
<figcaption>En la base ortogonal $u_1=(2,1)$, $u_2=(-1,2)$ el vector $v=(4,7)$ se descompone como $3u_1+2u_2$. Los dos sumandos son perpendiculares y forman con $v$ un rectángulo; cada coordenada es el cociente $\langle v,u_i\rangle/\langle u_i,u_i\rangle$.</figcaption>
</figure>

### Consecuencias: producto y norma en coordenadas

Si $B=\{u_1,\dots,u_n\}$ es ortogonal y $v=\sum c_iu_i$, entonces

$$
\lVert v\rVert^2=\sum_{i=1}^nc_i^2\,\lVert u_i\rVert^2 ,
$$

porque $\langle\sum c_iu_i,\sum c_ju_j\rangle=\sum_{i,j}c_ic_j\langle u_i,u_j\rangle$ y solo sobreviven los términos con $i=j$. Es el teorema de Pitágoras con $n$ sumandos. Si $B$ es **ortonormal**, $\lVert v\rVert^2=c_1^2+\dots+c_n^2$ (identidad de Parseval) y, más en general, $\langle v,w\rangle=[v]_B\cdot[w]_B$: el producto interno de dos vectores es el producto punto usual de sus coordenadas. Por eso, en una base ortonormal **todo espacio euclídeo de dimensión $n$ se comporta como $\mathbb{R}^n$ con el producto usual**.

### Matrices con columnas ortonormales

Sea $Q$ una matriz de $n\times n$ cuyas columnas $q_1,\dots,q_n$ son una base de $\mathbb{R}^n$ **ortonormal para el producto usual**. El elemento $(i,j)$ de $Q^tQ$ es $q_i\cdot q_j=\delta_{ij}$, o sea

$$
Q^tQ=I\qquad\Longleftrightarrow\qquad Q^{-1}=Q^t .
$$

Entonces la matriz de cambio de coordenadas desde la base canónica es $C_{EB}=Q^{-1}=Q^t$ y las coordenadas de $v$ en $B$ se obtienen sin invertir nada: $[v]_B=Q^tv$ (cada componente es $q_i\cdot v$, como dice el teorema). Si las columnas solo son ortogonales y no normalizadas, $U^tU=D$ es **diagonal**, con $d_{ii}=\lVert u_i\rVert^2$.

## Ejemplos

### Ejemplo 1 · Coordenadas en una base ortogonal de $\mathbb{R}^2$
<!-- check: U4.T03.E1 -->

Con el producto usual, verificar que $B=\{u_1,u_2\}$, con $u_1=(2,1)$ y $u_2=(-1,2)$, es una base ortogonal de $\mathbb{R}^2$ y hallar $[v]_B$ para $v=(4,7)$.

**Resolución.** $u_1\cdot u_2=-2+2=0$ y ambos son no nulos: por el corolario, $B$ es una base ortogonal. Calculamos $u_1\cdot u_1=5$, $u_2\cdot u_2=5$, $v\cdot u_1=8+7=15$ y $v\cdot u_2=-4+14=10$. Las coordenadas son

$$
c_1=\frac{15}{5}=3,\qquad c_2=\frac{10}{5}=2,\qquad [v]_B=\begin{pmatrix}3\\2\end{pmatrix}.
$$

**Comprobación.** $3(2,1)+2(-1,2)=(6-2,\,3+4)=(4,7)$. También por el camino largo: el sistema $\begin{pmatrix}2&-1\\1&2\end{pmatrix}c=\begin{pmatrix}4\\7\end{pmatrix}$ tiene solución $c=(3,2)$. Con la fórmula no hizo falta resolverlo. La figura de arriba dibuja este ejemplo.

### Ejemplo 2 · Una base ortogonal de $\mathbb{R}^3$, su normalización y $Q^tQ=I$
<!-- check: U4.T03.E2 -->

Con el producto usual, sean $u_1=(1,1,1)$, $u_2=(1,-2,1)$ y $u_3=(1,0,-1)$. Probar que forman una base ortogonal, hallar las coordenadas de $v=(2,-3,4)$, normalizar la base y verificar $Q^tQ=I$.

**Resolución.** Los productos son $u_1\cdot u_2=1-2+1=0$, $u_1\cdot u_3=1-1=0$ y $u_2\cdot u_3=1-1=0$; los tres vectores son no nulos, así que $B=\{u_1,u_2,u_3\}$ es una base ortogonal de $\mathbb{R}^3$. Las normas al cuadrado son $\lVert u_1\rVert^2=3$, $\lVert u_2\rVert^2=6$ y $\lVert u_3\rVert^2=2$. Con $v\cdot u_1=2-3+4=3$, $v\cdot u_2=2+6+4=12$ y $v\cdot u_3=2-4=-2$:

$$
[v]_B=\left(\frac33,\ \frac{12}{6},\ \frac{-2}{2}\right)^t=(1,\,2,\,-1)^t .
$$

Para la base ortonormal dividimos por las normas: $\hat u_1=\frac1{\sqrt3}(1,1,1)$, $\hat u_2=\frac1{\sqrt6}(1,-2,1)$, $\hat u_3=\frac1{\sqrt2}(1,0,-1)$. Sus coordenadas son $\langle v,\hat u_i\rangle$, o sea $\dfrac{3}{\sqrt3}=\sqrt3$, $\dfrac{12}{\sqrt6}=2\sqrt6$ y $\dfrac{-2}{\sqrt2}=-\sqrt2$. Con $Q=(\hat u_1\mid\hat u_2\mid\hat u_3)$, el elemento $(i,j)$ de $Q^tQ$ es $\hat u_i\cdot\hat u_j=\delta_{ij}$, luego $Q^tQ=I_3$ y $Q^{-1}=Q^t$.

**Comprobación.** $u_1+2u_2-u_3=(1+2-1,\,1-4-0,\,1+2+1)=(2,-3,4)=v$. Identidad de Parseval: $(\sqrt3)^2+(2\sqrt6)^2+(-\sqrt2)^2=3+24+2=29=\lVert v\rVert^2=4+9+16$.

### Ejemplo 3 · Una base ortogonal para un producto no usual
<!-- check: U4.T03.E3 -->

En $\mathbb{R}^2$ con $\langle x,y\rangle=x^tMy$, donde $M=\begin{pmatrix}2&1\\1&1\end{pmatrix}$, es decir $\langle x,y\rangle=2x_1y_1+x_1y_2+x_2y_1+x_2y_2$, verificar que $b_1=(1,0)$ y $b_2=(1,-2)$ son ortogonales y hallar las coordenadas de $v=(3,1)$ en $B=\{b_1,b_2\}$.

**Resolución.** Calculamos $My$ para $y=b_2$: $Mb_2=\begin{pmatrix}2-2\\1-2\end{pmatrix}=\begin{pmatrix}0\\-1\end{pmatrix}$. Entonces $\langle b_1,b_2\rangle=b_1\cdot Mb_2=0$: son ortogonales y, al ser dos vectores no nulos en un espacio de dimensión $2$, forman una base ortogonal. Con el producto usual **no** serían ortogonales: $b_1\cdot b_2=1$.

Las normas son $\langle b_1,b_1\rangle=b_1\cdot Mb_1=(1,0)\cdot(2,1)=2$ y $\langle b_2,b_2\rangle=b_2\cdot Mb_2=(1,-2)\cdot(0,-1)=2$. Los productos con $v$ son

$$
\langle v,b_1\rangle=v\cdot Mb_1=(3,1)\cdot(2,1)=7,\qquad\langle v,b_2\rangle=v\cdot Mb_2=(3,1)\cdot(0,-1)=-1 ,
$$

y por el teorema $[v]_B=\left(\tfrac72,\ -\tfrac12\right)^t$.

**Comprobación.** $\tfrac72(1,0)-\tfrac12(1,-2)=\left(\tfrac72-\tfrac12,\ 1\right)=(3,1)$. La base ortonormal correspondiente es $\left\{\tfrac1{\sqrt2}b_1,\tfrac1{\sqrt2}b_2\right\}$ (ambas normas valen $\sqrt2$).

El ejemplo muestra el método general: **primero se decide qué producto interno se usa** y recién después se calculan productos y normas. La misma base puede ser ortogonal para un producto y no serlo para otro.

## Interpretación

- Una base ortogonal es un sistema de ejes perpendiculares "respecto del producto elegido", con escalas que pueden diferir entre ejes (las normas $\lVert u_i\rVert$); una base ortonormal tiene todas las escalas iguales a $1$.
- Computacionalmente, calcular coordenadas en una base ortogonal cuesta $n$ productos internos y $n$ divisiones, en vez de resolver un sistema de $n\times n$. Además, los errores de redondeo se controlan mucho mejor con bases ortonormales, que no amplifican ninguna dirección.
- Un conjunto ortogonal no nulo nunca es linealmente dependiente: si en una cuenta aparece "ortogonal y LD", algún vector es nulo o hay un error.

:::caution[Errores frecuentes]
- **Creer que ortogonal es lo mismo que independiente.** Ortogonal (con vectores no nulos) implica independiente; la recíproca falla: $\{(1,0),(1,1)\}$ es LI y no es ortogonal.
- **Incluir el vector nulo** en un conjunto "ortogonal". El nulo es ortogonal a todo, pero un conjunto que lo contiene es linealmente dependiente; por eso la definición exige vectores no nulos.
- **Usar $\langle v,u_i\rangle$ como coordenada con una base ortogonal que no es unitaria.** Falta dividir por $\langle u_i,u_i\rangle$. En el Ejemplo 1 el producto $\langle v,u_1\rangle=15$ no es la coordenada: lo es $15/5=3$.
- **Verificar ortogonalidad con el producto usual en un espacio con producto no usual**, como en el Ejemplo 3.
- **Aplicar $Q^tQ=I$ a columnas solo ortogonales.** Con columnas ortogonales no normalizadas se obtiene una matriz diagonal, no la identidad. Tampoco vale si la ortonormalidad es respecto de un producto no usual, porque $Q^tQ$ calcula productos usuales entre columnas.
- **Dividir por la norma al cuadrado al normalizar.** Para normalizar se divide por $\lVert u\rVert$, no por $\lVert u\rVert^2$.
:::

## Autoevaluación

<details>
<summary>1. ¿Existe una base ortogonal de R² que contenga a (1, 1) con el producto usual? ¿Y con el de la lección 4.1, x₁y₁ + (x₁ + x₂)(y₁ + y₂)?</summary>

Con el producto usual, $(1,-1)$ completa una base ortogonal. Con el otro producto, $y$ es ortogonal a $(1,1)$ si $y_1+2(y_1+y_2)=3y_1+2y_2=0$: sirve $(2,-3)$. Siempre existe, y es un caso particular de Gram-Schmidt (lección 4.4).

</details>

<details>
<summary>2. Si {u₁, u₂, u₃} es ortogonal en R³ con el producto usual y ‖u₁‖ = 1, ‖u₂‖ = 2, ‖u₃‖ = 3, ¿cuánto vale ‖u₁ + u₂ + u₃‖?</summary>

Por Pitágoras, $\lVert u_1+u_2+u_3\rVert^2=1+4+9=14$, así que la norma es $\sqrt{14}$.

</details>

<details>
<summary>3. Probar que si {u₁, …, uₙ} es una base ortonormal y v = Σ cᵢuᵢ, entonces cᵢ = ⟨v, uᵢ⟩.</summary>

Es el caso $\langle u_i,u_i\rangle=1$ del teorema de coordenadas: $\langle v,u_j\rangle=\sum_ic_i\langle u_i,u_j\rangle=c_j$.

</details>

:::tip[En resumen]
- Un conjunto ortogonal de vectores no nulos es LI; con $n=\dim V$ vectores es una base. La recíproca falla.
- Con una base ortogonal $\{u_i\}$, las coordenadas son $c_i=\dfrac{\langle v,u_i\rangle}{\langle u_i,u_i\rangle}$ sin resolver sistemas; con una ortonormal, $c_i=\langle v,u_i\rangle$.
- Normalizar es dividir cada vector por su norma. En una base ortonormal, $\lVert v\rVert^2=\sum c_i^2$ y $\langle v,w\rangle=[v]_B\cdot[w]_B$.
- Si las columnas de $Q$ son ortonormales para el producto usual, $Q^tQ=I$ y $Q^{-1}=Q^t$.
- Ortogonal siempre es "respecto de un producto interno": la misma base cambia de carácter si cambia el producto.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 5.1, "Ortogonalidad en $\mathbb{R}^n$" (p. 379: conjuntos y bases ortogonales y ortonormales, matrices ortogonales); sección 7.1, "Espacios con producto interno" (p. 554), para el caso general.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ortogonalidad y mínimos cuadrados (conjuntos ortogonales y ortonormales).
- Anterior: [4.2 Norma, distancia y ángulo](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/). Siguiente: [4.4 Gram-Schmidt](/algebra-ii/unidad-4/teoria/gram-schmidt/), que construye bases ortogonales a partir de cualquier base.
- Repaso: [vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/).
