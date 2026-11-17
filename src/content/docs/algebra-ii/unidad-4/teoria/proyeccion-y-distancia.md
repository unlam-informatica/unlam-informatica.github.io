---
title: Proyección ortogonal y distancia a un subespacio
description: Descomposición ortogonal de un vector, fórmula de la proyección con una base ortogonal, tres métodos de cálculo, teorema de mejor aproximación y distancia a un subespacio.
slug: algebra-ii/unidad-4/teoria/proyeccion-y-distancia
sidebar:
  order: 6
  label: 4.6 Proyección y distancia
---

Dado un subespacio $S$ y un vector $v$ que probablemente no está en $S$, ¿cuál es el vector de $S$ más parecido a $v$? Intuitivamente es el "pie de la perpendicular" bajada desde $v$ a $S$: la sombra de $v$ sobre $S$ cuando la luz llega perpendicular. Esa sombra es la **proyección ortogonal**, y su distancia a $v$ es la **distancia de $v$ a $S$**. En esta lección la definimos, la calculamos de tres maneras y demostramos que, efectivamente, es el vector de $S$ más cercano a $v$.

En toda la lección, $(V,\langle\,,\rangle)$ es un espacio euclídeo de dimensión finita y $S\subseteq V$ es un subespacio.

## Descomposición ortogonal

:::note[Teorema (descomposición ortogonal)]
Para cada $v\in V$ existen únicos $p\in S$ y $r\in S^\perp$ tales que $v=p+r$. Si $\{u_1,\dots,u_k\}$ es una base ortogonal de $S$,

$$
p=\sum_{i=1}^k\frac{\langle v,u_i\rangle}{\langle u_i,u_i\rangle}\,u_i .
$$
:::

**Demostración.** *Existencia.* Sea $p$ el vector definido por la fórmula; claramente $p\in S$. Sea $r=v-p$. Para cada $j=1,\dots,k$, usando $\langle u_i,u_j\rangle=0$ si $i\neq j$,

$$
\langle r,u_j\rangle=\langle v,u_j\rangle-\sum_{i=1}^k\frac{\langle v,u_i\rangle}{\langle u_i,u_i\rangle}\langle u_i,u_j\rangle=\langle v,u_j\rangle-\langle v,u_j\rangle=0 .
$$

Como $r$ es ortogonal a una base de $S$, la propiedad "basta un generador" de la [lección 4.5](/algebra-ii/unidad-4/teoria/complemento-ortogonal/) da $r\in S^\perp$.

*Unicidad.* Si $v=p+r=p'+r'$ con $p,p'\in S$ y $r,r'\in S^\perp$, entonces $p-p'=r'-r$ pertenece a $S\cap S^\perp=\{0_V\}$; luego $p=p'$ y $r=r'$. $\blacksquare$

:::note[Definición (proyección ortogonal)]
El vector $p$ del teorema se llama **proyección ortogonal** de $v$ sobre $S$ y se escribe $p=\operatorname{proy}_S(v)$. El vector $r=v-p=\operatorname{proy}_{S^\perp}(v)$ es la componente de $v$ ortogonal a $S$.
:::

Algunas consecuencias inmediatas:

- $\operatorname{proy}_S(v)+\operatorname{proy}_{S^\perp}(v)=v$ para todo $v$ (es la descomposición misma).
- $v\in S$ si y solo si $\operatorname{proy}_S(v)=v$; $v\in S^\perp$ si y solo si $\operatorname{proy}_S(v)=0_V$.
- **Pitágoras:** como $p\perp r$, $\lVert v\rVert^2=\lVert p\rVert^2+\lVert r\rVert^2$.
- La aplicación $v\mapsto\operatorname{proy}_S(v)$ es una transformación lineal con $\operatorname{Im}=S$ y $\operatorname{Nu}=S^\perp$; aplicarla dos veces es lo mismo que una vez. Sus autovalores son $1$ (en $S$) y $0$ (en $S^\perp$).
- Si la base ortogonal es **ortonormal**, la fórmula se simplifica a $\operatorname{proy}_S(v)=\sum_i\langle v,u_i\rangle u_i$.

<figure class="math-figure">
<svg viewBox="-45 -105 165 125" role="img" aria-labelledby="pr-t pr-d" xmlns="http://www.w3.org/2000/svg">
<title id="pr-t">Proyección ortogonal sobre una recta de R2</title>
<desc id="pr-d">La recta L generada por (3,1), el vector v=(1,3), su proyección (9/5,3/5) sobre L y el componente ortogonal (-4/5,12/5), que va de la proyección a v.</desc>
<defs>
<marker id="pr-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker>
<marker id="pr-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker>
<marker id="pr-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker>
</defs>
<g transform="scale(1,-1)">
<line class="axis" x1="-40" y1="0" x2="105" y2="0"/>
<line class="axis" x1="0" y1="-8" x2="0" y2="100"/>
<line class="line-d" x1="-42" y1="-14" x2="105" y2="35"/>
<polyline class="guide" points="46.8,15.6 44.4,22.8 51.6,25.2"/>
<line class="vec-a" x1="0" y1="0" x2="54" y2="18" marker-end="url(#pr-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="30" y2="90" marker-end="url(#pr-arrow-b)"/>
<line class="vec-c" x1="54" y1="18" x2="30" y2="90" marker-end="url(#pr-arrow-c)"/>
</g>
<text class="math" x="96" y="-44">L</text>
<text class="math" x="34" y="-92">v</text>
<text class="math" x="58" y="-4">p</text>
<text class="math" x="48" y="-60">r</text>
</svg>
<figcaption>Proyección de v = (1, 3) sobre la recta L = gen{(3, 1)}. El vector p = proy<sub>L</sub>(v) = (9/5, 3/5) está sobre L y el vector r = v − p = (−4/5, 12/5) es perpendicular a L. La longitud de r es la distancia de v a L.</figcaption>
</figure>

### La fórmula exige una base ortogonal

La fórmula suma las proyecciones sobre los ejes de una base **ortogonal**. Si los vectores $s_1,\dots,s_k$ de la base de $S$ **no** son ortogonales, el resultado de $\sum\frac{\langle v,s_i\rangle}{\langle s_i,s_i\rangle}s_i$ en general no es $\operatorname{proy}_S(v)$: cada término ignora a los demás ejes (Ejemplo 2). Hay que ortogonalizar antes (Gram-Schmidt, lección [4.4](/algebra-ii/unidad-4/teoria/gram-schmidt/)) o usar alguno de los otros dos métodos.

## Tres métodos para calcular $\operatorname{proy}_S(v)$

**Método 1: base ortogonal.** Se ortogonaliza una base de $S$ y se aplica la fórmula. Conviene cuando $\dim S$ es chico o la base ya es ortogonal, y cuando se necesitan varias proyecciones sobre el mismo $S$.

**Método 2: base cualquiera y sistema de Gram.** Sea $\{s_1,\dots,s_k\}$ una base de $S$ y $p=a_1s_1+\dots+a_ks_k$. La condición $v-p\in S^\perp$ equivale a $\langle v-p,s_i\rangle=0$ para $i=1,\dots,k$, es decir,

$$
\sum_{j=1}^ka_j\langle s_j,s_i\rangle=\langle v,s_i\rangle\quad(i=1,\dots,k),\qquad\text{o sea}\qquad \begin{pmatrix}\langle s_1,s_1\rangle&\cdots&\langle s_k,s_1\rangle\\ \vdots&&\vdots\\ \langle s_1,s_k\rangle&\cdots&\langle s_k,s_k\rangle\end{pmatrix}\begin{pmatrix}a_1\\ \vdots\\ a_k\end{pmatrix}=\begin{pmatrix}\langle v,s_1\rangle\\ \vdots\\ \langle v,s_k\rangle\end{pmatrix}.
$$

La matriz $G$ de este sistema (la **matriz de Gram** de la base) es inversible: si $Ga=0$ entonces $a^tGa=\lVert\sum a_js_j\rVert^2=0$, luego $\sum a_js_j=0_V$ y $a=0$. Se resuelve el sistema y se arma $p$. Es el método para una base cualquiera, sin ortogonalizar.

**Método 3: base de $S$ y base de $S^\perp$.** Como $V=S\oplus S^\perp$, la unión de una base de $S$ y una de $S^\perp$ es una base de $V$. Se calculan las coordenadas de $v$ en esa base y se queda con los términos de $S$ para $p$ (y con los de $S^\perp$ para $r$). Si $S^\perp$ es más chico que $S$ (por ejemplo, un plano de $\mathbb{R}^3$ con una recta normal), conviene calcular primero $r=\operatorname{proy}_{S^\perp}(v)$ y luego $p=v-r$.

## Mejor aproximación y distancia a un subespacio

:::note[Teorema (de mejor aproximación)]
Sea $p=\operatorname{proy}_S(v)$. Para todo $s\in S$,

$$
\lVert v-p\rVert\le\lVert v-s\rVert,
$$

con igualdad si y solo si $s=p$. Es decir, $p$ es el único vector de $S$ más cercano a $v$.
:::

**Demostración.** Sea $s\in S$. Escribimos $v-s=(v-p)+(p-s)$. El primer sumando pertenece a $S^\perp$ y el segundo a $S$ (ambos $p,s\in S$), así que son ortogonales y por Pitágoras

$$
\lVert v-s\rVert^2=\lVert v-p\rVert^2+\lVert p-s\rVert^2\ \ge\ \lVert v-p\rVert^2 .
$$

La igualdad vale si y solo si $\lVert p-s\rVert=0$, es decir, $s=p$. $\blacksquare$

:::note[Definición (distancia a un subespacio)]
La **distancia** de $v$ a $S$ es $d(v,S)=\min_{s\in S}\lVert v-s\rVert=\lVert v-\operatorname{proy}_S(v)\rVert=\lVert\operatorname{proy}_{S^\perp}(v)\rVert$.
:::

Por Pitágoras también $d(v,S)^2=\lVert v\rVert^2-\lVert\operatorname{proy}_S(v)\rVert^2$. Y $d(v,S)=0$ si y solo si $v\in S$.

Para $S\subseteq\mathbb{R}^n$ con el producto usual, si $A$ es la matriz cuyas columnas son una base de $S$, la proyección se escribe con una matriz:

$$
\operatorname{proy}_S(v)=Pv,\qquad P=A\,(A^tA)^{-1}A^t .
$$

Esta fórmula es el Método 2 en forma matricial ($A^tA$ es la matriz de Gram de las columnas) y se demuestra en la lección [4.7](/algebra-ii/unidad-4/teoria/cuadrados-minimos/); se cumple $P^2=P$ y $P^t=P$. Para una sola recta $S=\operatorname{gen}\{u\}$ se reduce a $P=\dfrac{uu^t}{u^tu}$.

## Ejemplos

### Ejemplo 1 · Proyección sobre una recta de $\mathbb{R}^2$
<!-- check: U4.T06.E1 -->

Con el producto usual, hallar $\operatorname{proy}_L(v)$ y $d(v,L)$ para $L=\operatorname{gen}\{u\}$, $u=(3,1)$ y $v=(1,3)$.

**Resolución.** Una base ortogonal de $L$ es $\{u\}$. Con $u\cdot u=10$ y $v\cdot u=3+3=6$,

$$
p=\frac{6}{10}(3,1)=\left(\tfrac95,\tfrac35\right),\qquad r=v-p=\left(-\tfrac45,\tfrac{12}5\right).
$$

La distancia es $\lVert r\rVert=\sqrt{\tfrac{16}{25}+\tfrac{144}{25}}=\sqrt{\tfrac{32}{5}}=\dfrac{4\sqrt{10}}5$. Con la matriz de proyección, $P=\dfrac{uu^t}{u^tu}=\dfrac1{10}\begin{pmatrix}9&3\\3&1\end{pmatrix}$ y $Pv=\frac1{10}(9+9,\ 3+3)=\left(\tfrac95,\tfrac35\right)$, el mismo resultado.

**Comprobación.** $r\cdot u=-\tfrac{12}5+\tfrac{12}5=0$, así que $r\perp L$, y $p+r=(1,3)=v$. Pitágoras: $\lVert p\rVert^2=\tfrac{81+9}{25}=\tfrac{18}5$ y $\tfrac{18}5+\tfrac{32}5=10=\lVert v\rVert^2$.

### Ejemplo 2 · La fórmula con una base no ortogonal falla
<!-- check: U4.T06.E2 -->

En $\mathbb{R}^3$ con el producto usual, $S=\operatorname{gen}\{s_1,s_2\}$ con $s_1=(1,0,0)$ y $s_2=(1,1,0)$ (el plano $z=0$). Calcular $\operatorname{proy}_S(v)$ para $v=(0,1,1)$, y ver qué pasa si se aplica la fórmula con $s_1$ y $s_2$.

**Resolución.** $S$ es el plano $xy$, y la proyección de $(0,1,1)$ sobre él es evidentemente $(0,1,0)$. La fórmula aplicada a $s_1,s_2$, que **no** son ortogonales ($s_1\cdot s_2=1$), daría

$$
\frac{v\cdot s_1}{s_1\cdot s_1}s_1+\frac{v\cdot s_2}{s_2\cdot s_2}s_2=0\cdot s_1+\frac12(1,1,0)=\left(\tfrac12,\tfrac12,0\right)\ \neq\ (0,1,0).
$$

El resultado es erróneo: el residuo $v-\left(\tfrac12,\tfrac12,0\right)=\left(-\tfrac12,\tfrac12,1\right)$ no es ortogonal a $s_1$ (su producto con $s_1$ vale $-\tfrac12$). La forma correcta es ortogonalizar: $w_1=s_1$, $w_2=s_2-\frac11s_1=(0,1,0)$, y entonces $\operatorname{proy}_S(v)=\frac01w_1+\frac11w_2=(0,1,0)$.

**Comprobación.** El residuo correcto $v-(0,1,0)=(0,0,1)$ es ortogonal a $s_1$ y a $s_2$.

### Ejemplo 3 · Proyección sobre un plano de $\mathbb{R}^3$ por dos caminos
<!-- check: U4.T06.E3 -->

Con el producto usual, calcular $\operatorname{proy}_S(v)$ y $d(v,S)$ para el plano $S:\ x+y+z=0$ y $v=(5,1,0)$.

**Resolución.** *Camino 1: por la normal.* $S^\perp=\operatorname{gen}\{n\}$ con $n=(1,1,1)$. Con $v\cdot n=6$ y $n\cdot n=3$,

$$
\operatorname{proy}_{S^\perp}(v)=\frac63(1,1,1)=(2,2,2),\qquad\operatorname{proy}_S(v)=v-(2,2,2)=(3,-1,-2).
$$

*Camino 2: base ortogonal del plano.* Los vectores $a=(1,-1,0)$ y $b=(1,1,-2)$ están en $S$ y $a\cdot b=1-1+0=0$: base ortogonal. Los coeficientes son $\frac{v\cdot a}{a\cdot a}=\frac42=2$ y $\frac{v\cdot b}{b\cdot b}=\frac66=1$, y

$$
\operatorname{proy}_S(v)=2a+b=(2+1,\ -2+1,\ 0-2)=(3,-1,-2).
$$

Ambos caminos coinciden. La distancia es $d(v,S)=\lVert(2,2,2)\rVert=\sqrt{12}=2\sqrt3$.

**Comprobación.** $(3,-1,-2)$ está en el plano ($3-1-2=0$) y Pitágoras: $\lVert p\rVert^2+\lVert q\rVert^2=14+12=26=\lVert v\rVert^2=25+1$.

<figure class="math-figure">
<svg viewBox="-90 -90 190 135" role="img" aria-labelledby="pp-t pp-d" xmlns="http://www.w3.org/2000/svg">
<title id="pp-t">Proyección ortogonal sobre un plano de R3, en perspectiva</title>
<desc id="pp-d">Un trozo del plano S, la recta perpendicular S⊥, el vector v, su proyección p sobre el plano y el vector q de p a v, perpendicular al plano.</desc>
<defs>
<marker id="pp-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker>
<marker id="pp-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker>
<marker id="pp-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker>
</defs>
<g transform="scale(1,-1)">
<polygon class="region-a" points="78,-1.5 42,-28.5 -78,1.5 -42,28.5"/>
<line class="guide" x1="0" y1="-30" x2="0" y2="75"/>
<polyline class="guide" points="52.8,-1.2 52.8,7.8 60,6"/>
<line class="vec-a" x1="0" y1="0" x2="60" y2="-3" marker-end="url(#pp-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="60" y2="57" marker-end="url(#pp-arrow-b)"/>
<line class="vec-c" x1="60" y1="-3" x2="60" y2="57" marker-end="url(#pp-arrow-c)"/>
</g>
<text class="math" x="-78" y="-14">S</text>
<text class="math" x="4" y="-78">S⊥</text>
<text class="math" x="64" y="-60">v</text>
<text class="math" x="64" y="2">p</text>
<text class="math" x="64" y="-28">q</text>
</svg>
<figcaption>Dibujo en perspectiva del Ejemplo 3: v = p + q, con p = (3, −1, −2) = 2a + b en el plano S: x + y + z = 0 y q = (2, 2, 2) sobre la recta normal S<sup>⊥</sup>. En una perspectiva los ángulos no se conservan: lo que se ve es la estructura (el plano, su normal y la descomposición), no las medidas.</figcaption>
</figure>

### Ejemplo 4 · Proyección con un producto no usual, por tres métodos
<!-- check: U4.T06.E4 -->

En $\mathbb{R}^3$ con $\langle x,y\rangle=x^tMy$, $M=\begin{pmatrix}2&1&0\\1&2&1\\0&1&1\end{pmatrix}$ (el producto del Ejemplo 4 de la lección 4.5), calcular $\operatorname{proy}_S(v)$ y $d(v,S)$ para $S=\operatorname{gen}\{s_1,s_2\}$, con $s_1=(1,0,1)$, $s_2=(0,1,0)$ y $v=(1,2,3)$.

**Resolución.** Necesitamos $Ms_1=(2,2,1)^t$ y $Ms_2=(1,2,1)^t$.

*Método 1 (base ortogonal).* Empezamos por $w_1=s_2=(0,1,0)$, con $\langle w_1,w_1\rangle=s_2\cdot Ms_2=2$. Como $\langle s_1,w_1\rangle=s_1\cdot Ms_2=2$, el segundo vector es $w_2=s_1-\frac22s_2=(1,-1,1)$, con $\langle w_2,w_2\rangle=1$ (pues $Mw_2=(1,0,0)^t$). Los productos con $v$ son $\langle v,w_1\rangle=v\cdot Ms_2=1+4+3=8$ y $\langle v,w_2\rangle=v\cdot Mw_2=1$, de modo que

$$
\operatorname{proy}_S(v)=\frac82(0,1,0)+\frac11(1,-1,1)=(1,3,1).
$$

*Método 2 (sistema con la base original).* La matriz de Gram de $\{s_1,s_2\}$ tiene $\langle s_1,s_1\rangle=3$, $\langle s_1,s_2\rangle=2$ y $\langle s_2,s_2\rangle=2$, y el lado derecho es $\langle v,s_1\rangle=v\cdot Ms_1=2+4+3=9$ y $\langle v,s_2\rangle=8$:

$$
\begin{pmatrix}3&2\\2&2\end{pmatrix}\begin{pmatrix}a_1\\a_2\end{pmatrix}=\begin{pmatrix}9\\8\end{pmatrix}\ \Longrightarrow\ \begin{pmatrix}a_1\\a_2\end{pmatrix}=\frac12\begin{pmatrix}2&-2\\-2&3\end{pmatrix}\begin{pmatrix}9\\8\end{pmatrix}=\begin{pmatrix}1\\3\end{pmatrix},
$$

y $p=s_1+3s_2=(1,3,1)$.

*Método 3 (base de $S$ y de $S^\perp$).* Por el Ejemplo 4 de la lección 4.5, $S^\perp=\operatorname{gen}\{t\}$ con $t=(0,1,-2)$. Las coordenadas de $v$ en la base $\{s_1,s_2,t\}$ son $(1,3,-1)$: $s_1+3s_2-t=(1,0,1)+(0,3,0)-(0,1,-2)=(1,2,3)$. Entonces $p=s_1+3s_2=(1,3,1)$ y $r=-t=(0,-1,2)$.

Los tres métodos dan $\operatorname{proy}_S(v)=(1,3,1)$. La distancia: $\langle r,r\rangle=r\cdot Mr$, con $Mr=(-1,0,1)^t$, vale $0+0+2=2$, o sea $d(v,S)=\sqrt2$.

**Comprobación.** $\langle r,s_1\rangle=r\cdot Ms_1=(0,-1,2)\cdot(2,2,1)=0$ y $\langle r,s_2\rangle=(0,-1,2)\cdot(1,2,1)=0$. Con el producto usual, la proyección de $v$ sobre el mismo $S$ es otra: $(2,2,2)$.

### Ejemplo 5 · Mejor aproximación de $x^2$ por polinomios de grado a lo sumo $1$
<!-- check: U4.T06.E5 -->

En $P_2[\mathbb{R}]$ con $\langle p,q\rangle=p(-1)q(-1)+p(0)q(0)+p(1)q(1)$, hallar el polinomio de $P_1[\mathbb{R}]$ más cercano a $q=x^2$ y la distancia.

**Resolución.** $P_1[\mathbb{R}]=\operatorname{gen}\{1,x\}$ y $\{1,x\}$ es ortogonal para este producto ($\langle1,x\rangle=-1+0+1=0$), con $\langle1,1\rangle=3$ y $\langle x,x\rangle=2$. Los productos con $q$ son $\langle x^2,1\rangle=1+0+1=2$ y $\langle x^2,x\rangle=-1+0+1=0$. Entonces

$$
\operatorname{proy}_{P_1}(x^2)=\frac23\cdot1+\frac02x=\frac23 .
$$

El error es $x^2-\frac23$, que toma los valores $\left(\tfrac13,-\tfrac23,\tfrac13\right)$ en $-1,0,1$, y $d^2=\frac19+\frac49+\frac19=\frac23$: $d(x^2,P_1[\mathbb{R}])=\sqrt{\tfrac23}=\dfrac{\sqrt6}3$.

**Comprobación.** El error $x^2-\frac23$ es ortogonal a $1$ ($\tfrac13-\tfrac23+\tfrac13=0$) y a $x$ ($-\tfrac13+0+\tfrac13=0$).

El resultado se interpreta así: con estos tres nodos, la mejor recta para aproximar la parábola es la constante $\frac23$. Es el mismo problema que el ajuste por cuadrados mínimos de la lección siguiente.

## Interpretación

- **Geométrica.** $\operatorname{proy}_S(v)$ es el pie de la perpendicular bajada desde $v$ a $S$ y $d(v,S)$ es la longitud de esa perpendicular. Entre todos los segmentos de $v$ a $S$, el perpendicular es el más corto.
- **Algebraica.** $V=S\oplus S^\perp$ y la proyección es la transformación lineal que "se queda con la componente en $S$".
- **Computacional.** Aproximar un vector por combinaciones de pocos vectores base (compresión, ajuste de datos, filtros) es proyectar. La calidad de la aproximación es $d(v,S)$.

:::caution[Errores frecuentes]
- **Aplicar la fórmula con una base no ortogonal** (Ejemplo 2). El síntoma es que el residuo $v-p$ no es ortogonal a $S$: siempre conviene verificarlo.
- **Olvidar el denominador $\langle u_i,u_i\rangle$**, o usar la norma en lugar de su cuadrado.
- **Calcular las proyecciones con el producto usual en un espacio con producto no usual.** En el Ejemplo 4 el resultado depende del producto.
- **Confundir $\operatorname{proy}_S(v)$ con $\operatorname{proy}_{S^\perp}(v)$**, o dar $r$ como si fuera la distancia: la distancia es la **norma** de $r$.
- **Proyectar sobre cada generador y sumar** cuando los generadores no son ortogonales: es lo mismo que el error del Ejemplo 2.
- **Dar $d(v,S)$ sin la raíz.** $\langle r,r\rangle=\lVert r\rVert^2$; la distancia es su raíz cuadrada.
- **Dar $v$ como proyección de un $v\in S^\perp$ sobre $S$.** La proyección sobre $S$ de un vector de $S^\perp$ es el vector nulo.
:::

## Autoevaluación

<details>
<summary>1. Calcular proy_S(v) para S = gen{(1, 1)} y v = (3, 1) con el producto usual.</summary>

$\dfrac{v\cdot(1,1)}{(1,1)\cdot(1,1)}(1,1)=\dfrac42(1,1)=(2,2)$, y $d(v,S)=\lVert(1,-1)\rVert=\sqrt2$.

</details>

<details>
<summary>2. Si P es la matriz de proyección ortogonal sobre S ⊆ Rⁿ, ¿qué matriz es I − P?</summary>

Es la matriz de la proyección sobre $S^\perp$: $(I-P)v=v-\operatorname{proy}_S(v)=\operatorname{proy}_{S^\perp}(v)$.

</details>

<details>
<summary>3. Probar que ‖proy_S(v)‖ ≤ ‖v‖.</summary>

Por Pitágoras, $\lVert v\rVert^2=\lVert\operatorname{proy}_S(v)\rVert^2+\lVert\operatorname{proy}_{S^\perp}(v)\rVert^2\ge\lVert\operatorname{proy}_S(v)\rVert^2$, con igualdad si y solo si $v\in S$.

</details>

:::tip[En resumen]
- Todo $v$ se descompone de manera única como $v=p+r$ con $p\in S$ y $r\in S^\perp$; $p=\operatorname{proy}_S(v)$.
- Con una base **ortogonal** $\{u_i\}$ de $S$: $\operatorname{proy}_S(v)=\sum\dfrac{\langle v,u_i\rangle}{\langle u_i,u_i\rangle}u_i$. Con una base cualquiera, se resuelve el sistema de Gram; también se puede usar la proyección sobre $S^\perp$ y restar.
- Mejor aproximación: $\lVert v-\operatorname{proy}_S(v)\rVert\le\lVert v-s\rVert$ para todo $s\in S$, con igualdad solo en $s=\operatorname{proy}_S(v)$. La distancia es $d(v,S)=\lVert\operatorname{proy}_{S^\perp}(v)\rVert$.
- $\lVert v\rVert^2=\lVert\operatorname{proy}_S(v)\rVert^2+\lVert\operatorname{proy}_{S^\perp}(v)\rVert^2$.
- En $\mathbb{R}^n$ con el producto usual, $P=A(A^tA)^{-1}A^t$ proyecta sobre $\operatorname{col}(A)$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 5.2, "Complementos y proyecciones ortogonales" (p. 389); sección 7.3, "Aproximación por mínimos cuadrados" (p. 591), para el teorema de mejor aproximación.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ortogonalidad y mínimos cuadrados (proyecciones ortogonales y teorema de la mejor aproximación).
- Anterior: [4.5 Complemento ortogonal](/algebra-ii/unidad-4/teoria/complemento-ortogonal/). Siguiente: [4.7 Cuadrados mínimos](/algebra-ii/unidad-4/teoria/cuadrados-minimos/).
- Repaso: [rectas y planos](/algebra-ii/repaso/rectas-y-planos/).
