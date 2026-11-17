---
title: Vectores y matrices
description: Operaciones con vectores de ℝⁿ, producto escalar y norma, producto de matrices, transpuesta, inversa por Gauss-Jordan, traza y matrices especiales.
slug: algebra-ii/repaso/vectores-y-matrices
sidebar:
  order: 1
  label: R.1 Vectores y matrices
---

## Para qué sirve

Álgebra II generaliza dos objetos de Álgebra I: los vectores de $\mathbb{R}^n$ pasan a ser un caso particular de *espacio vectorial*, y las matrices pasan a representar *transformaciones lineales*. Casi todas las cuentas de la materia terminan siendo productos de matrices, transpuestas o inversas. Esta lección repasa lo mínimo para hacerlas con seguridad: operaciones con vectores, producto escalar y norma, producto de matrices (en sus dos lecturas), transpuesta, inversa, traza y algunas matrices con forma especial.

## Vectores de ℝⁿ

:::note[Definición]
$\mathbb{R}^n$ es el conjunto de las $n$-uplas ordenadas $u=(u_1,u_2,\dots,u_n)$ con $u_i\in\mathbb{R}$. Para $u,v\in\mathbb{R}^n$ y $c\in\mathbb{R}$ se definen la **suma** y el **producto por escalar** componente a componente:

$$
u+v=(u_1+v_1,\dots,u_n+v_n),\qquad c\,u=(c\,u_1,\dots,c\,u_n).
$$

El vector nulo es $0=(0,\dots,0)$ y el opuesto de $u$ es $-u=(-1)\,u$.
:::

Estas dos operaciones cumplen las propiedades conocidas de la aritmética: la suma es asociativa y conmutativa, tiene neutro ($0$) y opuestos; el producto por escalar distribuye respecto de la suma de vectores y de la suma de escalares, $(cd)\,u=c\,(d\,u)$ y $1\,u=u$. Esas diez propiedades son, justamente, los axiomas de [espacio vectorial](/algebra-ii/unidad-1/teoria/espacios-vectoriales/) de la Unidad 1.

En el texto escribimos los vectores como $n$-uplas con comas, $(1,-2,0)$; cuando intervienen en un producto de matrices los escribimos como **columnas**.

### Producto escalar y norma

:::note[Definición]
El **producto escalar usual** de $u,v\in\mathbb{R}^n$ es el número

$$
u\cdot v=u_1v_1+u_2v_2+\dots+u_nv_n .
$$

La **norma** (longitud) de $u$ es $\lVert u\rVert=\sqrt{u\cdot u}=\sqrt{u_1^2+\dots+u_n^2}$. Dos vectores son **ortogonales** ($u\perp v$) si $u\cdot v=0$. Si $u,v\neq 0$, el ángulo $\angle(u,v)\in[0,\pi]$ entre ellos cumple

$$
\cos\angle(u,v)=\frac{u\cdot v}{\lVert u\rVert\,\lVert v\rVert}.
$$
:::

El producto escalar es simétrico ($u\cdot v=v\cdot u$), lineal en cada variable ($(au+bw)\cdot v=a\,u\cdot v+b\,w\cdot v$) y positivo ($u\cdot u>0$ si $u\neq0$). En la Unidad 4 esas tres propiedades se toman como definición de [producto interno](/algebra-ii/unidad-4/teoria/producto-interno/). De la definición de norma se obtiene $\lVert c\,u\rVert=\lvert c\rvert\,\lVert u\rVert$; un vector de norma $1$ se llama **unitario**, y $\frac{1}{\lVert u\rVert}u$ es el unitario con la dirección y el sentido de $u\neq 0$.

### Interpretación geométrica

En $\mathbb{R}^2$ y $\mathbb{R}^3$ identificamos $u$ con la flecha que va del origen al punto de coordenadas $u$. La suma $u+v$ es la diagonal del paralelogramo de lados $u$ y $v$ (regla del paralelogramo); $c\,u$ estira o contrae la flecha por el factor $\lvert c\rvert$ y la invierte si $c<0$; $\lVert u\rVert$ es la longitud de la flecha (teorema de Pitágoras) y $\lVert u-v\rVert$ es la distancia entre los puntos $u$ y $v$.

<figure class="math-figure">
<svg viewBox="-30 -150 230 180" role="img" aria-labelledby="vm-t vm-d" xmlns="http://www.w3.org/2000/svg">
<title id="vm-t">Suma de vectores por la regla del paralelogramo</title>
<desc id="vm-d">En el plano, los vectores u=(3,1) y v=(1,2) dibujados desde el origen, y su suma u+v=(4,3) como diagonal del paralelogramo que forman; los lados opuestos están punteados.</desc>
<defs><marker id="vm-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker><marker id="vm-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker><marker id="vm-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="scale(1,-1)">
<line class="grid" x1="40" y1="-20" x2="40" y2="140"/>
<line class="grid" x1="80" y1="-20" x2="80" y2="140"/>
<line class="grid" x1="120" y1="-20" x2="120" y2="140"/>
<line class="grid" x1="160" y1="-20" x2="160" y2="140"/>
<line class="grid" x1="-20" y1="40" x2="190" y2="40"/>
<line class="grid" x1="-20" y1="80" x2="190" y2="80"/>
<line class="grid" x1="-20" y1="120" x2="190" y2="120"/>
<line class="axis" x1="-20" y1="0" x2="190" y2="0"/>
<line class="axis" x1="0" y1="-20" x2="0" y2="140"/>
<line class="guide" x1="120" y1="40" x2="160" y2="120"/>
<line class="guide" x1="40" y1="80" x2="160" y2="120"/>
<line class="vec-a" x1="0" y1="0" x2="120" y2="40" marker-end="url(#vm-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="40" y2="80" marker-end="url(#vm-arrow-b)"/>
<line class="vec-c" x1="0" y1="0" x2="160" y2="120" marker-end="url(#vm-arrow-c)"/>
</g>
<text class="small" x="37" y="14">1</text>
<text class="small" x="77" y="14">2</text>
<text class="small" x="117" y="14">3</text>
<text class="small" x="157" y="14">4</text>
<text class="small" x="-12" y="-37">1</text>
<text class="small" x="-12" y="-77">2</text>
<text class="small" x="-12" y="-117">3</text>
<text class="math" x="124" y="-28">u</text>
<text class="math" x="24" y="-84">v</text>
<text class="math" x="164" y="-124">u+v</text>
</svg>
<figcaption>Con u=(3,1) y v=(1,2), la suma u+v=(4,3) es la diagonal del paralelogramo: se llega al mismo punto recorriendo u y luego v que recorriendo v y luego u (lados punteados). Esa es la conmutatividad de la suma vista geométricamente.</figcaption>
</figure>

En $\mathbb{R}^3$ la lectura es la misma, con tres ejes perpendiculares. El signo de $u\cdot v$ informa el tipo de ángulo: positivo si es agudo, cero si es recto, negativo si es obtuso. Para $n>3$ ya no hay dibujo, pero las fórmulas siguen funcionando y conservamos el vocabulario geométrico (longitud, ángulo, ortogonalidad).

### Ejemplo 1 · Operaciones, producto escalar y norma en ℝ³
<!-- check: R.T01.E1 -->

Sean $u=(2,-1,2)$ y $v=(1,3,-1)$. Calculamos $u+v$, $2u-v$, $u\cdot v$, las normas y el coseno del ángulo.

Las operaciones son componente a componente:

$$
u+v=(2+1,\,-1+3,\,2-1)=(3,2,1),\qquad 2u-v=(4-1,\,-2-3,\,4+1)=(3,-5,5).
$$

El producto escalar es $u\cdot v=2\cdot1+(-1)\cdot 3+2\cdot(-1)=2-3-2=-3$. Las normas:

$$
\lVert u\rVert=\sqrt{4+1+4}=3,\qquad \lVert v\rVert=\sqrt{1+9+1}=\sqrt{11}.
$$

Entonces $\cos\angle(u,v)=\dfrac{-3}{3\sqrt{11}}=-\dfrac{1}{\sqrt{11}}<0$: el ángulo es obtuso (aproximadamente $107{,}5^\circ$). El vector unitario en la dirección de $u$ es $\frac13(2,-1,2)$.

**Comprobación.** $u\cdot u=9=\lVert u\rVert^2$ y $(u+v)\cdot(u+v)=9+4+1=14=\lVert u\rVert^2+2\,u\cdot v+\lVert v\rVert^2=9-6+11$, como debe ser al desarrollar el cuadrado.

## Matrices y sus operaciones

Una matriz $A\in\mathbb{R}^{m\times n}$ es un arreglo de $m$ filas y $n$ columnas; su elemento de la fila $i$ y la columna $j$ es $a_{ij}$ y escribimos $A=(a_{ij})$. La suma (para matrices del mismo tamaño) y el producto por escalar se hacen elemento a elemento, igual que con vectores. Con esas operaciones $\mathbb{R}^{m\times n}$ también cumple los axiomas de espacio vectorial.

### Producto de matrices

:::note[Definición]
Si $A\in\mathbb{R}^{m\times n}$ y $B\in\mathbb{R}^{n\times p}$ (columnas de $A$ = filas de $B$), el producto $AB\in\mathbb{R}^{m\times p}$ es la matriz cuyo elemento $(i,j)$ es el producto escalar de la **fila** $i$ de $A$ con la **columna** $j$ de $B$:

$$
(AB)_{ij}=\sum_{k=1}^{n}a_{ik}\,b_{kj}=a_{i1}b_{1j}+a_{i2}b_{2j}+\dots+a_{in}b_{nj}.
$$
:::

Hay una segunda lectura, más útil en Álgebra II. Si $c_1,\dots,c_n$ son las columnas de $A$ y $x=(x_1,\dots,x_n)$ es una columna, entonces

$$
Ax=x_1\,c_1+x_2\,c_2+\dots+x_n\,c_n ,
$$

es decir, **$Ax$ es la combinación lineal de las columnas de $A$ con los coeficientes de $x$**. Aplicada a cada columna $b_j$ de $B$: la columna $j$ de $AB$ es $A\,b_j$, una combinación lineal de las columnas de $A$. Esta lectura explica por qué el sistema $Ax=b$ tiene solución exactamente cuando $b$ es combinación de las columnas de $A$ (lo que en la Unidad 1 se escribe $b\in\operatorname{col}(A)$).

:::note[Propiedad]
Siempre que los tamaños permitan las operaciones:

1. $(AB)C=A(BC)$ (asociatividad).
2. $A(B+C)=AB+AC$ y $(A+B)C=AC+BC$ (distributividad).
3. $c\,(AB)=(cA)B=A(cB)$ para todo escalar $c$.
4. $I_mA=A=AI_n$ si $A\in\mathbb{R}^{m\times n}$, donde $I_k$ es la identidad de $k\times k$ (unos en la diagonal, ceros fuera de ella).

En general **$AB\neq BA$**: el producto de matrices no es conmutativo.
:::

### Ejemplo 2 · Producto, combinación de columnas y no conmutatividad
<!-- check: R.T01.E2 -->

Sean

$$
A=\begin{pmatrix}1&2&0\\-1&1&3\end{pmatrix}\in\mathbb{R}^{2\times3},\qquad B=\begin{pmatrix}2&1\\0&-1\\1&2\end{pmatrix}\in\mathbb{R}^{3\times2}.
$$

**Filas por columnas.** $AB$ es de $2\times 2$:

$$
AB=\begin{pmatrix}1\cdot2+2\cdot0+0\cdot1 & 1\cdot1+2\cdot(-1)+0\cdot2\\ (-1)\cdot2+1\cdot0+3\cdot1 & (-1)\cdot1+1\cdot(-1)+3\cdot2\end{pmatrix}=\begin{pmatrix}2&-1\\1&4\end{pmatrix}.
$$

**Como combinación de columnas.** La primera columna de $B$ es $(2,0,1)$, así que la primera columna de $AB$ es

$$
2\begin{pmatrix}1\\-1\end{pmatrix}+0\begin{pmatrix}2\\1\end{pmatrix}+1\begin{pmatrix}0\\3\end{pmatrix}=\begin{pmatrix}2\\1\end{pmatrix},
$$

que coincide con lo anterior. En cambio $BA$ es de $3\times3$:

$$
BA=\begin{pmatrix}1&5&3\\1&-1&-3\\-1&4&6\end{pmatrix},
$$

de modo que $AB$ y $BA$ ni siquiera tienen el mismo tamaño. Aun con matrices cuadradas el orden importa: con

$$
P=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad Q=\begin{pmatrix}1&0\\1&1\end{pmatrix}:\qquad PQ=\begin{pmatrix}2&1\\1&1\end{pmatrix}\neq\begin{pmatrix}1&1\\1&2\end{pmatrix}=QP .
$$

**Comprobación.** Transponiendo, $(AB)^t=\begin{pmatrix}2&1\\-1&4\end{pmatrix}$, y el producto $B^tA^t$ (de $2\times3$ por $3\times2$) da la misma matriz, como anticipa la propiedad de la transpuesta que sigue.

### Transpuesta

:::note[Definición]
La **transpuesta** de $A\in\mathbb{R}^{m\times n}$ es $A^t\in\mathbb{R}^{n\times m}$, con $(A^t)_{ij}=a_{ji}$: las filas de $A$ son las columnas de $A^t$.
:::

Valen $(A^t)^t=A$, $(A+B)^t=A^t+B^t$, $(cA)^t=c\,A^t$ y la regla del producto con el **orden invertido**:

$$
(AB)^t=B^tA^t .
$$

**Demostración.** El elemento $(i,j)$ de $(AB)^t$ es $(AB)_{ji}=\sum_k a_{jk}b_{ki}$. El elemento $(i,j)$ de $B^tA^t$ es $\sum_k (B^t)_{ik}(A^t)_{kj}=\sum_k b_{ki}a_{jk}$. Son la misma suma. $\blacksquare$

Una observación que se usa mucho en la Unidad 4: si $u,v\in\mathbb{R}^n$ son columnas, $u\cdot v=u^tv$ (una matriz de $1\times1$, que identificamos con un número).

### Inversa

:::note[Definición]
Una matriz cuadrada $A\in\mathbb{R}^{n\times n}$ es **inversible** si existe $B\in\mathbb{R}^{n\times n}$ con $AB=BA=I_n$. Esa $B$ es única, se llama **inversa** de $A$ y se escribe $A^{-1}$.
:::

La unicidad sale de la asociatividad: si $B$ y $B'$ cumplen la definición, $B=BI=B(AB')=(BA)B'=IB'=B'$. Para matrices cuadradas alcanza con verificar una de las dos igualdades: si $AB=I$, entonces también $BA=I$.

:::note[Propiedad]
Si $A$ y $B$ son inversibles de $n\times n$ y $c\neq 0$:

1. $(A^{-1})^{-1}=A$ y $(cA)^{-1}=\frac1c A^{-1}$.
2. $(A^t)^{-1}=(A^{-1})^t$.
3. $AB$ es inversible y $(AB)^{-1}=B^{-1}A^{-1}$ (otra vez, orden invertido).
:::

**Demostración de 3.** $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AIA^{-1}=AA^{-1}=I$. $\blacksquare$

**Caso $2\times 2$.** Si $ad-bc\neq0$,

$$
\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix},
$$

y si $ad-bc=0$ la matriz no es inversible (ese número es el determinante; ver [R.2](/algebra-ii/repaso/determinantes/)).

**Método de Gauss-Jordan.** Para $n\geq3$ se arma la matriz $(A\mid I_n)$ y se aplican operaciones elementales de fila (intercambiar filas, multiplicar una fila por un escalar no nulo, sumar a una fila un múltiplo de otra) hasta llevar el bloque izquierdo a $I_n$. Si se logra, el bloque derecho es $A^{-1}$; si aparece una fila nula en el bloque izquierdo, $A$ no es inversible. Funciona porque cada operación de fila equivale a multiplicar a izquierda por una matriz inversible $E$, y si $E_k\cdots E_1A=I$ entonces $E_k\cdots E_1=A^{-1}$, que es justamente lo que se acumula a la derecha.

### Ejemplo 3 · Inversa por Gauss-Jordan
<!-- check: R.T01.E3 -->

Hallamos la inversa de

$$
A=\begin{pmatrix}1&2&1\\0&1&1\\1&2&2\end{pmatrix}.
$$

Partimos de $(A\mid I)$ y con $F_3-F_1\to F_3$ anulamos el $1$ de la esquina:

$$
\left(\begin{array}{ccc|ccc}1&2&1&1&0&0\\0&1&1&0&1&0\\1&2&2&0&0&1\end{array}\right)\sim\left(\begin{array}{ccc|ccc}1&2&1&1&0&0\\0&1&1&0&1&0\\0&0&1&-1&0&1\end{array}\right).
$$

El bloque izquierdo ya es triangular con unos en la diagonal. Subimos: $F_2-F_3\to F_2$ y $F_1-F_3\to F_1$, y finalmente $F_1-2F_2\to F_1$:

$$
\sim\left(\begin{array}{ccc|ccc}1&2&0&2&0&-1\\0&1&0&1&1&-1\\0&0&1&-1&0&1\end{array}\right)\sim\left(\begin{array}{ccc|ccc}1&0&0&0&-2&1\\0&1&0&1&1&-1\\0&0&1&-1&0&1\end{array}\right).
$$

Por lo tanto

$$
A^{-1}=\begin{pmatrix}0&-2&1\\1&1&-1\\-1&0&1\end{pmatrix}.
$$

**Comprobación.** Fila 1 de $A$ por las columnas de $A^{-1}$: $0+2-1=1$, $-2+2+0=0$, $1-2+1=0$; las filas 2 y 3 dan $(0,1,0)$ y $(0,0,1)$. Es decir, $AA^{-1}=I$.

### Traza

:::note[Definición]
La **traza** de $A\in\mathbb{R}^{n\times n}$ es la suma de su diagonal: $\operatorname{tr}(A)=a_{11}+a_{22}+\dots+a_{nn}$.
:::

Es lineal ($\operatorname{tr}(A+B)=\operatorname{tr}(A)+\operatorname{tr}(B)$, $\operatorname{tr}(cA)=c\operatorname{tr}(A)$), cumple $\operatorname{tr}(A^t)=\operatorname{tr}(A)$ y, aunque $AB\neq BA$, siempre $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, porque ambas valen $\sum_i\sum_k a_{ik}b_{ki}$. En el Ejemplo 3, $\operatorname{tr}(A)=1+1+2=4$. En la Unidad 3 la traza reaparece como la suma de los autovalores.

## Matrices especiales

| Tipo | Condición | Ejemplo |
|---|---|---|
| Diagonal | $a_{ij}=0$ si $i\neq j$ | $\operatorname{diag}(2,-1,5)$ |
| Triangular superior | $a_{ij}=0$ si $i>j$ (ceros debajo de la diagonal) | forma escalonada de una matriz cuadrada |
| Triangular inferior | $a_{ij}=0$ si $i<j$ (ceros encima de la diagonal) | transpuesta de una triangular superior |
| Simétrica | $A^t=A$, es decir $a_{ij}=a_{ji}$ | $AA^t$ para cualquier $A$; $A+A^t$ si $A$ es cuadrada |

Notamos $\operatorname{diag}(d_1,\dots,d_n)$ a la matriz diagonal con esos elementos. Las diagonales son las más simples para operar:

$$
\operatorname{diag}(d_1,\dots,d_n)\operatorname{diag}(e_1,\dots,e_n)=\operatorname{diag}(d_1e_1,\dots,d_ne_n),\qquad \operatorname{diag}(d_1,\dots,d_n)^k=\operatorname{diag}(d_1^k,\dots,d_n^k),
$$

y $\operatorname{diag}(d_1,\dots,d_n)$ es inversible si y solo si todos los $d_i\neq0$, con inversa $\operatorname{diag}(1/d_1,\dots,1/d_n)$. Además, multiplicar **a izquierda** por $\operatorname{diag}(d_1,\dots,d_n)$ multiplica la fila $i$ por $d_i$, y multiplicar **a derecha** multiplica la columna $i$ por $d_i$. El producto de triangulares superiores es triangular superior. Que $AA^t$ es simétrica se ve con la regla de la transpuesta: $(AA^t)^t=(A^t)^tA^t=AA^t$.

:::caution[Errores frecuentes]
- **Conmutar factores.** $(A+B)^2=A^2+AB+BA+B^2$, que no es $A^2+2AB+B^2$ salvo que $AB=BA$. Con $P$ y $Q$ del Ejemplo 2, $PQ\neq QP$.
- **Simplificar sin inversa.** De $AB=AC$ no se deduce $B=C$ si $A$ no es inversible: con $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$, $B=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ y $C=0$ se tiene $AB=AC=0$. Por la misma razón, $AB=0$ no implica $A=0$ o $B=0$.
- **Olvidar invertir el orden.** $(AB)^t=B^tA^t$ y $(AB)^{-1}=B^{-1}A^{-1}$; escribir $A^tB^t$ en general ni siquiera tiene el tamaño correcto.
- **Inversa elemento a elemento.** La inversa de $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ no es $\begin{pmatrix}1&1/2\\1/3&1/4\end{pmatrix}$; ese recurso solo vale para matrices diagonales.
- **Norma de una suma.** $\lVert u+v\rVert\neq\lVert u\rVert+\lVert v\rVert$ en general: con $u=(1,0)$ y $v=(0,1)$, $\lVert u+v\rVert=\sqrt2\neq2$.
:::

:::tip[En resumen]
- En $\mathbb{R}^n$: $u\cdot v=\sum u_iv_i$, $\lVert u\rVert=\sqrt{u\cdot u}$, $u\perp v\iff u\cdot v=0$, $\cos\angle(u,v)=\frac{u\cdot v}{\lVert u\rVert\lVert v\rVert}$.
- $(AB)_{ij}$ = fila $i$ de $A$ por columna $j$ de $B$; $Ax$ es la combinación lineal de las columnas de $A$ con coeficientes $x$.
- El producto es asociativo y distributivo pero no conmutativo.
- $(AB)^t=B^tA^t$, $(AB)^{-1}=B^{-1}A^{-1}$, $\operatorname{tr}(AB)=\operatorname{tr}(BA)$.
- La inversa se calcula llevando $(A\mid I)$ a $(I\mid A^{-1})$ con operaciones de fila.
:::

## Ejercicios de repaso

### Ejercicio R.01 · Operaciones y ángulo en ℝ³
<!-- ejercicio: R.01 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Dados $u=(1,-2,2)$ y $v=(3,0,-4)$, calcular $3u-2v$, $u\cdot v$, $\lVert u\rVert$ y $\lVert v\rVert$. Decidir si el ángulo entre $u$ y $v$ es agudo, recto u obtuso y hallar su coseno.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Operar componente a componente y usar $\cos\angle(u,v)=\frac{u\cdot v}{\lVert u\rVert\lVert v\rVert}$.

$3u-2v=(3,-6,6)-(6,0,-8)=(-3,-6,14)$. Además $u\cdot v=3+0-8=-5$, $\lVert u\rVert=\sqrt{1+4+4}=3$ y $\lVert v\rVert=\sqrt{9+0+16}=5$. Entonces

$$
\cos\angle(u,v)=\frac{-5}{3\cdot5}=-\frac13 ,
$$

y como es negativo el ángulo es obtuso.

**Comprobación.** $\lvert u\cdot v\rvert=5\le\lVert u\rVert\lVert v\rVert=15$, como exige la desigualdad de Cauchy-Schwarz, de modo que el coseno está en $[-1,1]$.

:::tip[Resultado]
$3u-2v=(-3,-6,14)$, $u\cdot v=-5$, $\lVert u\rVert=3$, $\lVert v\rVert=5$, $\cos\angle(u,v)=-\frac13$: ángulo obtuso.
:::

</details>

### Ejercicio R.02 · Producto, transpuesta y traza
<!-- ejercicio: R.02 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $A=\begin{pmatrix}2&-1\\1&3\end{pmatrix}$ y $B=\begin{pmatrix}0&1\\2&-2\end{pmatrix}$. Calcular $AB$ y $BA$. Verificar que $(AB)^t=B^tA^t$ y que $(AB)^t\neq A^tB^t$. Comparar $\operatorname{tr}(AB)$ con $\operatorname{tr}(BA)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Producto filas por columnas y comparación directa.

$$
AB=\begin{pmatrix}0-2&2+2\\0+6&1-6\end{pmatrix}=\begin{pmatrix}-2&4\\6&-5\end{pmatrix},\qquad BA=\begin{pmatrix}0+1&0+3\\4-2&-2-6\end{pmatrix}=\begin{pmatrix}1&3\\2&-8\end{pmatrix}.
$$

Entonces $AB\neq BA$. Por un lado $(AB)^t=\begin{pmatrix}-2&6\\4&-5\end{pmatrix}$; por otro,

$$
B^tA^t=\begin{pmatrix}0&2\\1&-2\end{pmatrix}\begin{pmatrix}2&1\\-1&3\end{pmatrix}=\begin{pmatrix}-2&6\\4&-5\end{pmatrix}=(AB)^t,
$$

mientras que $A^tB^t=(BA)^t=\begin{pmatrix}1&2\\3&-8\end{pmatrix}\neq(AB)^t$.

**Comprobación.** $\operatorname{tr}(AB)=-2-5=-7$ y $\operatorname{tr}(BA)=1-8=-7$: coinciden aunque las matrices sean distintas.

:::tip[Resultado]
$AB=\begin{pmatrix}-2&4\\6&-5\end{pmatrix}$, $BA=\begin{pmatrix}1&3\\2&-8\end{pmatrix}$, $(AB)^t=B^tA^t$, $\operatorname{tr}(AB)=\operatorname{tr}(BA)=-7$.
:::

</details>

### Ejercicio R.03 · Inversa de una matriz de 3×3
<!-- ejercicio: R.03 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallar, si existe, la inversa de $M=\begin{pmatrix}2&1&0\\1&1&0\\0&1&1\end{pmatrix}$ por el método de Gauss-Jordan, y verificar el resultado.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Llevar $(M\mid I)$ a $(I\mid M^{-1})$. Conviene empezar intercambiando las dos primeras filas para tener un pivote $1$ y evitar fracciones.

$$
\left(\begin{array}{ccc|ccc}2&1&0&1&0&0\\1&1&0&0&1&0\\0&1&1&0&0&1\end{array}\right)\xrightarrow{F_1\leftrightarrow F_2}\left(\begin{array}{ccc|ccc}1&1&0&0&1&0\\2&1&0&1&0&0\\0&1&1&0&0&1\end{array}\right)\xrightarrow{F_2-2F_1\to F_2}\left(\begin{array}{ccc|ccc}1&1&0&0&1&0\\0&-1&0&1&-2&0\\0&1&1&0&0&1\end{array}\right).
$$

Con $-F_2\to F_2$ el pivote pasa a ser $1$; luego $F_1-F_2\to F_1$ y $F_3-F_2\to F_3$:

$$
\left(\begin{array}{ccc|ccc}1&1&0&0&1&0\\0&1&0&-1&2&0\\0&1&1&0&0&1\end{array}\right)\sim\left(\begin{array}{ccc|ccc}1&0&0&1&-1&0\\0&1&0&-1&2&0\\0&0&1&1&-2&1\end{array}\right).
$$

El bloque izquierdo llegó a $I$, así que $M$ es inversible.

**Comprobación.** $M M^{-1}$: fila 1 de $M$, $(2,1,0)$, por las columnas de $M^{-1}$ da $2-1=1$, $-2+2=0$, $0$; fila 2, $(1,1,0)$: $0,1,0$; fila 3, $(0,1,1)$: $-1+1=0$, $2-2=0$, $1$. Resulta $I$.

:::tip[Resultado]
$M^{-1}=\begin{pmatrix}1&-1&0\\-1&2&0\\1&-2&1\end{pmatrix}$.
:::

</details>

### Ejercicio R.04 · Producto de matrices simétricas
<!-- ejercicio: R.04 | nivel: intermedio | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
Decidir si la siguiente afirmación es verdadera o falsa. Justificar. "Si $A,B\in\mathbb{R}^{n\times n}$ son simétricas, entonces $AB$ es simétrica." Probar además que, para $A$ y $B$ simétricas, $AB$ es simétrica si y solo si $AB=BA$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Buscar un contraejemplo pequeño y luego usar $(AB)^t=B^tA^t$.

**Falsa.** $A=\begin{pmatrix}1&0\\0&2\end{pmatrix}$ y $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ son simétricas, pero

$$
AB=\begin{pmatrix}0&1\\2&0\end{pmatrix},\qquad (AB)^t=\begin{pmatrix}0&2\\1&0\end{pmatrix}\neq AB .
$$

**Equivalencia.** Si $A^t=A$ y $B^t=B$, entonces $(AB)^t=B^tA^t=BA$. Por lo tanto $(AB)^t=AB$ si y solo si $BA=AB$. $\blacksquare$

**Comprobación.** En el contraejemplo, $BA=\begin{pmatrix}0&2\\1&0\end{pmatrix}=(AB)^t$, que es distinta de $AB$, en acuerdo con la equivalencia.

:::tip[Resultado]
La afirmación es falsa; el producto de dos simétricas es simétrico exactamente cuando conmutan.
:::

</details>

## Dónde se usa en Álgebra II

- Los axiomas de espacio vectorial generalizan las propiedades de $\mathbb{R}^n$ y $\mathbb{R}^{m\times n}$: [espacios vectoriales](/algebra-ii/unidad-1/teoria/espacios-vectoriales/) y [subespacios](/algebra-ii/unidad-1/teoria/subespacios/).
- "$Ax$ es combinación de las columnas de $A$" es la base de [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/).
- La inversa aparece en el [cambio de coordenadas](/algebra-ii/unidad-1/teoria/cambio-de-coordenadas/) ($C_{B'B}=C_{BB'}^{-1}$), en la [composición e inversa](/algebra-ii/unidad-2/teoria/composicion-e-inversa/) de transformaciones lineales y en la [diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/) ($A=CDC^{-1}$).
- Las potencias de matrices diagonales simplifican el cálculo de [potencias](/algebra-ii/unidad-3/teoria/potencias/).
- Producto escalar, norma y transpuesta son el punto de partida de [producto interno](/algebra-ii/unidad-4/teoria/producto-interno/), [norma, distancia y ángulo](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/) y [cuadrados mínimos](/algebra-ii/unidad-4/teoria/cuadrados-minimos/) ($A^tAx=A^tb$).

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: secciones 1.1 (geometría y álgebra de vectores), 1.2 (longitud y ángulo: el producto punto), 3.1 (operaciones con matrices), 3.2 (álgebra matricial) y 3.3 (la inversa).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de álgebra de matrices.
- Siguiente lección del repaso: [R.2 Determinantes](/algebra-ii/repaso/determinantes/).
