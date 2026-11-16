---
title: Composición e inversa
description: La composición de TL y su matriz como producto, núcleo e imagen de una composición, transformación inversa y su matriz como inversa de la matriz, preimágenes y el error de declarar isomorfismo a una composición que pasa por menor dimensión.
slug: algebra-ii/unidad-2/teoria/composicion-e-inversa
sidebar:
  order: 8
  label: 2.8 Composición e inversa
---

## Para qué sirve

Encadenar transformaciones es la operación natural de la informática gráfica: para dibujar un objeto se lo escala, luego se lo gira y luego se lo traslada, y cada paso es una TL (o casi). Aplicar los tres pasos seguidos es una sola TL, la **composición**, y su matriz es el **producto** de las matrices de los pasos. Del mismo modo, deshacer un paso es aplicar la TL **inversa**, cuya matriz es la matriz inversa. Esta lección hace precisas esas dos afirmaciones, decide qué propiedades heredan las composiciones (¿es mono? ¿es epi?) y cierra la Unidad 2.

## La composición de TL es una TL

Sean $T:V\to W$ y $S:W\to U$. La composición $S\circ T:V\to U$ se define por $(S\circ T)(v)=S(T(v))$: primero actúa $T$, después $S$. Solo se puede componer cuando el espacio de llegada de $T$ es el de salida de $S$.

:::note[Propiedad]
Si $T:V\to W$ y $S:W\to U$ son lineales, $S\circ T:V\to U$ es lineal.
:::

**Demostración.** Para $u,v\in V$ y $\lambda\in K$, usando primero la linealidad de $T$ y luego la de $S$:

$$
(S\circ T)(u+v)=S\big(T(u)+T(v)\big)=S(T(u))+S(T(v))=(S\circ T)(u)+(S\circ T)(v),
$$

$$
(S\circ T)(\lambda v)=S\big(\lambda T(v)\big)=\lambda\,S(T(v))=\lambda\,(S\circ T)(v).\ \blacksquare
$$

## La matriz de la composición

:::note[Teorema · Matriz de la composición]
Sean $B$, $B'$ y $B''$ bases de $V$, $W$ y $U$. Entonces

$$
M(S\circ T)_{BB''}=M(S)_{B'B''}\ M(T)_{BB'}.
$$
:::

**Demostración.** Para todo $v\in V$, aplicando dos veces la identidad fundamental de [2.6](/algebra-ii/unidad-2/teoria/matriz-asociada/):

$$
M(S)_{B'B''}\,M(T)_{BB'}\,[v]_B=M(S)_{B'B''}\,[T(v)]_{B'}=[S(T(v))]_{B''}=[(S\circ T)(v)]_{B''}.
$$

Como $M(S\circ T)_{BB''}$ es la única matriz con $M[v]_B=[(S\circ T)(v)]_{B''}$, coincide con el producto. $\blacksquare$

Dos precisiones. La base $B'$ **del medio debe ser la misma** en los dos factores: la llegada de $T$ y la salida de $S$ se miden en $B'$. Y el orden es el de las funciones: el primero en actuar, $T$, queda a la **derecha**. Los tamaños lo confirman: $M(S)$ es $\dim U\times\dim W$ y $M(T)$ es $\dim W\times\dim V$.

:::caution[Notación de los libros]
En la notación de Poole y Lay, $[S\circ T]_{B''\leftarrow B}=[S]_{B''\leftarrow B'}\,[T]_{B'\leftarrow B}$: la misma regla, con los subíndices en orden inverso al nuestro. Ver [notación](/algebra-ii/notacion/).
:::

### Ejemplo 1 · Composición de rotaciones
<!-- check: U2.T08.E1 -->

Sea $R:\mathbb{R}^2\to\mathbb{R}^2$ la rotación de ángulo $\theta$ con $\cos\theta=\tfrac45$ y $\operatorname{sen}\theta=\tfrac35$, de matriz canónica $R=\begin{pmatrix}\tfrac45&-\tfrac35\\\tfrac35&\tfrac45\end{pmatrix}$. Calcular $R\circ R$ y $R^{-1}$.

**Composición.** Es el producto de la matriz por sí misma:

$$
R\cdot R=\frac1{25}\begin{pmatrix}16-9&-12-12\\12+12&-9+16\end{pmatrix}=\frac1{25}\begin{pmatrix}7&-24\\24&7\end{pmatrix}.
$$

Es la rotación de ángulo $2\theta$: las identidades $\cos2\theta=\cos^2\theta-\operatorname{sen}^2\theta=\tfrac{16}{25}-\tfrac9{25}=\tfrac7{25}$ y $\operatorname{sen}2\theta=2\operatorname{sen}\theta\cos\theta=2\cdot\tfrac35\cdot\tfrac45=\tfrac{24}{25}$ dan exactamente las entradas de la matriz. Por ejemplo, $(R\circ R)(5,0)=\tfrac1{25}(35,\ 120)=\big(\tfrac75,\ \tfrac{24}5\big)$, de norma $\sqrt{\tfrac{49+576}{25}}=5$: la composición de rotaciones conserva las longitudes.

**Inversa.** Deshacer una rotación de $\theta$ es rotar $-\theta$, cuya matriz es $\begin{pmatrix}\tfrac45&\tfrac35\\-\tfrac35&\tfrac45\end{pmatrix}=R^t$. Comprobamos que es la inversa: $R^tR=\tfrac1{25}\begin{pmatrix}16+9&-12+12\\-12+12&9+16\end{pmatrix}=I$. Luego $R$ es un automorfismo y $R^{-1}=R^t$. (La igualdad $R^{-1}=R^t$ vale para toda rotación, porque $\cos^2\theta+\operatorname{sen}^2\theta=1$.)

## Núcleo, imagen y rango de una composición

:::note[Propiedad · Núcleo e imagen de $S\circ T$]
Sean $T:V\to W$ y $S:W\to U$ lineales.

1. $\operatorname{Nu}(T)\subseteq\operatorname{Nu}(S\circ T)$. Si además $S$ es monomorfismo, $\operatorname{Nu}(S\circ T)=\operatorname{Nu}(T)$.
2. $\operatorname{Im}(S\circ T)\subseteq\operatorname{Im}(S)$. Si además $T$ es epimorfismo, $\operatorname{Im}(S\circ T)=\operatorname{Im}(S)$.
3. $\dim\operatorname{Im}(S\circ T)\le\min\{\dim\operatorname{Im}(T),\ \dim\operatorname{Im}(S)\}$. En términos de matrices, $\operatorname{rango}(AB)\le\min\{\operatorname{rango}(A),\operatorname{rango}(B)\}$.
:::

**Demostración.**

1. Si $T(v)=0_W$, entonces $(S\circ T)(v)=S(0_W)=0_U$. Si $S$ es mono y $S(T(v))=0_U$, entonces $T(v)\in\operatorname{Nu}(S)=\{0_W\}$, así que $v\in\operatorname{Nu}(T)$.
2. Todo elemento de $\operatorname{Im}(S\circ T)$ es $S(T(v))=S(w)$ con $w=T(v)\in W$, que está en $\operatorname{Im}(S)$. Si $T$ es epi, $w$ recorre todo $W$ y se obtiene toda la imagen de $S$.
3. De 2, $\dim\operatorname{Im}(S\circ T)\le\dim\operatorname{Im}(S)$. Por otra parte, $\operatorname{Im}(S\circ T)=\{S(w):\ w\in\operatorname{Im}(T)\}$ es la imagen por $S$ del subespacio $\operatorname{Im}(T)$; si $\{w_1,\dots,w_r\}$ es una base de $\operatorname{Im}(T)$, los vectores $S(w_1),\dots,S(w_r)$ generan $\operatorname{Im}(S\circ T)$, que entonces tiene dimensión a lo sumo $r=\dim\operatorname{Im}(T)$. $\blacksquare$

De 1 y 2 salen dos reglas útiles para clasificar una composición: **si $S\circ T$ es monomorfismo, $T$ es monomorfismo** (porque $\operatorname{Nu}(T)\subseteq\operatorname{Nu}(S\circ T)=\{0\}$); y **si $S\circ T$ es epimorfismo, $S$ es epimorfismo** ($U=\operatorname{Im}(S\circ T)\subseteq\operatorname{Im}(S)$). La recíproca no vale en general: $T(t)=(t,0)$ es mono y $S(x,y)=y$ es epi, y la composición $S\circ T=0$ no es ni mono ni epi.

### Ejemplo 2 · Una composición que no es isomorfismo y otra que sí
<!-- check: U2.T08.E2 -->

Sean $T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(x+y,\ y-z)$ y $S:\mathbb{R}^2\to\mathbb{R}^3$, $S(u,v)=(u,\ u+v,\ v)$. Estudiar $S\circ T:\mathbb{R}^3\to\mathbb{R}^3$ y $T\circ S:\mathbb{R}^2\to\mathbb{R}^2$.

**Matrices canónicas.**

$$
M(T)=\begin{pmatrix}1&1&0\\0&1&-1\end{pmatrix},\qquad M(S)=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}.
$$

**$S\circ T$.** El producto, con $T$ a la derecha, es

$$
M(S\circ T)=M(S)\,M(T)=\begin{pmatrix}1&1&0\\1&2&-1\\0&1&-1\end{pmatrix}.
$$

Su determinante es $1\cdot(-2+1)-1\cdot(-1-0)+0=-1+1=0$; el rango es 2 (las dos primeras filas son LI y la tercera es la segunda menos la primera). **$S\circ T$ no es mono, ni epi, ni isomorfismo**, aunque va de $\mathbb{R}^3$ en $\mathbb{R}^3$ y cada factor tiene una buena propiedad: $S$ es mono y $T$ es epi. Las dimensiones lo explican: la composición pasa por $\mathbb{R}^2$ y toda la información queda comprimida en un espacio de dimensión 2, de donde ya no se puede recuperar. Precisamente, $\operatorname{Nu}(T)=\operatorname{gen}\{(-1,1,1)\}$ (de $x+y=0$ y $y=z$) y, como $S$ es mono, $\operatorname{Nu}(S\circ T)=\operatorname{Nu}(T)=\operatorname{gen}\{(-1,1,1)\}$: comprobamos con la matriz de la composición, que aplicada a $(-1,1,1)$ da $(-1+1,\ -1+2-1,\ 1-1)=(0,0,0)$.

**$T\circ S$.** Pasa por $\mathbb{R}^3$ y vuelve a $\mathbb{R}^2$:

$$
M(T\circ S)=M(T)\,M(S)=\begin{pmatrix}1&1&0\\0&1&-1\end{pmatrix}\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}=\begin{pmatrix}2&1\\1&0\end{pmatrix}.
$$

Su determinante es $-1\neq0$: **$T\circ S$ es un automorfismo** de $\mathbb{R}^2$, con $M\big((T\circ S)^{-1}\big)=\begin{pmatrix}0&1\\1&-2\end{pmatrix}$ (se verifica multiplicando: $\begin{pmatrix}2&1\\1&0\end{pmatrix}\begin{pmatrix}0&1\\1&-2\end{pmatrix}=I$). Observemos que $T\circ S$ y $S\circ T$ son TL de espacios distintos, que una sea inversible no dice nada sobre la otra y que ni $T$ ni $S$ son isomorfismos (sus espacios tienen dimensiones 3 y 2).

:::caution[Un error muy común]
**Declarar isomorfismo a una composición que pasa por un espacio de menor dimensión.** En el ejemplo 2, $S\circ T$ es de $\mathbb{R}^3$ en $\mathbb{R}^3$ y se "ve" cuadrada, pero la factorización $\mathbb{R}^3\to\mathbb{R}^2\to\mathbb{R}^3$ obliga a $\operatorname{rango}(M(S\circ T))\le\dim\mathbb{R}^2=2<3$. Tener matriz cuadrada no alcanza: hay que **calcular el rango o el determinante del producto**. En general, si $T:V\to W$ y $S:W\to U$ con $\dim W<\dim V$, $S\circ T$ **no es mono**; si $\dim W<\dim U$, **no es epi**.
:::

## Transformación inversa

Si $T:V\to W$ es isomorfismo, es biyectiva y existe la función inversa $T^{-1}:W\to V$, la única con $T^{-1}\circ T=\operatorname{id}_V$ y $T\circ T^{-1}=\operatorname{id}_W$.

:::note[Teorema · La inversa de un isomorfismo es lineal]
Si $T:V\to W$ es un isomorfismo, $T^{-1}:W\to V$ es un isomorfismo.
:::

**Demostración.** Sean $w_1,w_2\in W$ y $\lambda\in K$. Como $T$ es epi, $w_i=T(v_i)$ para ciertos $v_i\in V$, y $v_i=T^{-1}(w_i)$. Por linealidad de $T$,

$$
T(v_1+v_2)=T(v_1)+T(v_2)=w_1+w_2\quad\Longrightarrow\quad T^{-1}(w_1+w_2)=v_1+v_2=T^{-1}(w_1)+T^{-1}(w_2),
$$

$$
T(\lambda v_1)=\lambda w_1\quad\Longrightarrow\quad T^{-1}(\lambda w_1)=\lambda v_1=\lambda\,T^{-1}(w_1).
$$

Entonces $T^{-1}$ es lineal. Es biyectiva (su inversa es $T$), luego es un isomorfismo. $\blacksquare$

Con esto queda justificado lo que quedó pendiente en [2.4](/algebra-ii/unidad-2/teoria/clasificacion/): la relación "ser isomorfos" es simétrica.

:::note[Teorema · Matriz de la inversa]
Si $T:V\to W$ es un isomorfismo, $B$ es base de $V$ y $B'$ es base de $W$, entonces $M(T)_{BB'}$ es cuadrada e inversible y

$$
M(T^{-1})_{B'B}=\big(M(T)_{BB'}\big)^{-1}.
$$

Recíprocamente, si $\dim V=\dim W$ y $M(T)_{BB'}$ es inversible, $T$ es isomorfismo.
:::

**Demostración.** Por ser isomorfismo, $\dim V=\dim W$ y $M(T)_{BB'}$ es cuadrada. Por el teorema de la matriz de la composición, y porque $M(\operatorname{id}_V)_{BB}=I$ (cada $b_j$ tiene coordenadas $e_j$),

$$
M(T^{-1})_{B'B}\,M(T)_{BB'}=M(T^{-1}\circ T)_{BB}=I,\qquad M(T)_{BB'}\,M(T^{-1})_{B'B}=M(T\circ T^{-1})_{B'B'}=I.
$$

Entonces las dos matrices son inversas una de la otra. Recíprocamente, si $M(T)_{BB'}$ es cuadrada e inversible tiene rango $n=\dim W$ y $\dim V=n$: por la síntesis de [2.6](/algebra-ii/unidad-2/teoria/matriz-asociada/), $T$ es mono y epi. $\blacksquare$

En la práctica: **para hallar $T^{-1}$**, (1) se calcula $M(T)_{BB'}$, (2) se invierte por Gauss-Jordan (ampliando con la identidad), (3) se arma la fórmula de $T^{-1}$ con el método de "de la matriz a la fórmula". También vale, para isomorfismos $T$ y $S$ componibles, $(S\circ T)^{-1}=T^{-1}\circ S^{-1}$, con el orden invertido: es como en la inversa de un producto de matrices.

### Preimágenes e inversa

Para $w\in W$, el conjunto $T^{-1}(w)=\{v\in V:\ T(v)=w\}$ (la **preimagen** de $w$) está definido para **cualquier** TL, aunque no sea inversible, y es vacío o es $v_p+\operatorname{Nu}(T)$ (teorema de [2.2](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/)). Si $T$ es isomorfismo, la preimagen de cada $w$ tiene un solo elemento, y la función inversa lo devuelve. Para la composición, la preimagen se calcula por etapas: $(S\circ T)^{-1}(u)=T^{-1}\big(S^{-1}(u)\big)$ como conjuntos (primero las preimágenes por $S$, luego las de esos vectores por $T$). No hay que confundir el **conjunto** $T^{-1}(w)$, que existe siempre, con la **función** $T^{-1}$, que solo existe si $T$ es isomorfismo.

### Ejemplo 3 · Una TL entre polinomios y ternas
<!-- check: U2.T08.E3 -->

Sea $T:P_2[\mathbb{R}]\to\mathbb{R}^3$, $T(p)=(p(0),\ p(1),\ p(-1))$. Probar que es isomorfismo, hallar $T^{-1}$ y la preimagen de $(2,3,5)$.

**Matriz.** Con la base canónica $\{1,x,x^2\}$ en la salida y la canónica de $\mathbb{R}^3$ en la llegada, las columnas son $T(1)=(1,1,1)$, $T(x)=(0,1,-1)$ y $T(x^2)=(0,1,1)$:

$$
M=M(T)_{EE'}=\begin{pmatrix}1&0&0\\1&1&1\\1&-1&1\end{pmatrix},\qquad\det M=1\cdot(1+1)=2\neq0.
$$

Es cuadrada e inversible: **$T$ es isomorfismo**. (Otra justificación: un polinomio de grado $\le2$ que se anula en $0$, $1$ y $-1$ tiene tres raíces y es el nulo; entonces $T$ es mono y, por igualdad de dimensiones, epi.)

**Inversa de la matriz.** Gauss-Jordan sobre $(M\mid I)$:

$$
\left(\begin{array}{ccc|ccc}1&0&0&1&0&0\\1&1&1&0&1&0\\1&-1&1&0&0&1\end{array}\right)\xrightarrow[F_3-F_1\to F_3]{F_2-F_1\to F_2}\left(\begin{array}{ccc|ccc}1&0&0&1&0&0\\0&1&1&-1&1&0\\0&-1&1&-1&0&1\end{array}\right)\xrightarrow{F_3+F_2\to F_3}\left(\begin{array}{ccc|ccc}1&0&0&1&0&0\\0&1&1&-1&1&0\\0&0&2&-2&1&1\end{array}\right)
$$

$$
\xrightarrow[F_3/2\to F_3]{}\left(\begin{array}{ccc|ccc}1&0&0&1&0&0\\0&1&1&-1&1&0\\0&0&1&-1&\tfrac12&\tfrac12\end{array}\right)\xrightarrow{F_2-F_3\to F_2}\left(\begin{array}{ccc|ccc}1&0&0&1&0&0\\0&1&0&0&\tfrac12&-\tfrac12\\0&0&1&-1&\tfrac12&\tfrac12\end{array}\right).
$$

Entonces $M(T^{-1})_{E'E}=M^{-1}=\begin{pmatrix}1&0&0\\0&\tfrac12&-\tfrac12\\-1&\tfrac12&\tfrac12\end{pmatrix}$.

**Fórmula.** Para $(y_0,y_1,y_2)\in\mathbb{R}^3$ las coordenadas del polinomio son $M^{-1}(y_0,y_1,y_2)^t$:

$$
T^{-1}(y_0,y_1,y_2)=y_0+\tfrac{y_1-y_2}{2}\,x+\tfrac{y_1+y_2-2y_0}{2}\,x^2.
$$

**Preimagen de $(2,3,5)$.** Es el único polinomio $T^{-1}(2,3,5)=2+\tfrac{3-5}{2}x+\tfrac{3+5-4}{2}x^2=2-x+2x^2$. Comprobamos: $p(0)=2$, $p(1)=2-1+2=3$ y $p(-1)=2+1+2=5$. El polinomio es el de interpolación que pasa por los puntos $(0,2)$, $(1,3)$ y $(-1,5)$.

### Ejemplo 4 · La matriz de la inversa en bases no canónicas
<!-- check: U2.T08.E4 -->

Sea $T:P_1[\mathbb{R}]\to\mathbb{R}^2$, $T(a_0+a_1x)=(a_0+a_1,\ a_0+2a_1)$, con $B=\{1,\ 1+x\}$ y $B'=\{(1,1),(0,1)\}$. Hallar $M(T)_{BB'}$, $M(T^{-1})_{B'B}$ y $T^{-1}(u,v)$.

**Matriz.** $T(1)=(1,1)=1\,(1,1)+0\,(0,1)$ y $T(1+x)=(2,3)=2\,(1,1)+1\,(0,1)$. Entonces

$$
M(T)_{BB'}=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad\det=1\neq0.
$$

$T$ es isomorfismo y $M(T^{-1})_{B'B}=\begin{pmatrix}1&2\\0&1\end{pmatrix}^{-1}=\begin{pmatrix}1&-2\\0&1\end{pmatrix}$ (se verifica: $\begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}1&-2\\0&1\end{pmatrix}=I$).

**Lectura de la inversa.** Las columnas dan los transformados de la base $B'$ de $\mathbb{R}^2$, escritos en $B$: $T^{-1}(1,1)=1\cdot1=1$ y $T^{-1}(0,1)=-2\cdot1+1\cdot(1+x)=-1+x$. Comprobación: $T(-1+x)=(-1+1,\ -1+2)=(0,1)$.

**Fórmula.** $(u,v)=u\,(1,1)+(v-u)\,(0,1)$, o sea $[(u,v)]_{B'}=(u,\ v-u)$. Entonces

$$
[T^{-1}(u,v)]_B=\begin{pmatrix}1&-2\\0&1\end{pmatrix}\begin{pmatrix}u\\v-u\end{pmatrix}=\begin{pmatrix}3u-2v\\v-u\end{pmatrix},
$$

y el polinomio es $(3u-2v)\cdot1+(v-u)(1+x)=(2u-v)+(v-u)\,x$. **Comprobación:** $T\big((2u-v)+(v-u)x\big)=\big((2u-v)+(v-u),\ (2u-v)+2(v-u)\big)=(u,\ v)$.

:::caution[Errores frecuentes]
- **Invertir el orden.** $M(S\circ T)=M(S)\,M(T)$, no $M(T)\,M(S)$. En el ejemplo 2, $M(T)M(S)$ es de $2\times2$ y $M(S)M(T)$ es de $3\times3$: son composiciones distintas.
- **Mezclar bases en el producto.** La base del medio tiene que ser la misma. Si $M(T)$ está escrita respecto de $B'$ en la llegada y $M(S)$ respecto de otra $B_2'$ en la salida, hay que pasar antes por $C_{B'B_2'}$.
- **Invertir una matriz que no es cuadrada, o una cuadrada de determinante cero.** $T$ solo tiene inversa si es isomorfismo; mono o epi sueltos no alcanzan, y una matriz cuadrada de rango menor que su tamaño no es inversible.
- **Escribir $M(T^{-1})_{BB'}$.** La inversa lleva de $W$ a $V$: sus bases son $B'$ (salida) y $B$ (llegada), $M(T^{-1})_{B'B}$.
- **Confundir $T^{-1}(w)$ conjunto con $T^{-1}$ función.** La preimagen de un vector existe siempre (a veces es vacía); la función inversa solo si $T$ es isomorfismo.
- **Declarar isomorfismo a $S\circ T$ por ser cuadrada.** Ver el recuadro del ejemplo 2: hay que ver el rango de la matriz del producto.
:::

## Autoevaluación

1. Si $T:\mathbb{R}^4\to\mathbb{R}^2$ y $S:\mathbb{R}^2\to\mathbb{R}^4$, ¿puede $S\circ T$ ser automorfismo de $\mathbb{R}^4$?

<details>
<summary>Respuesta</summary>

No: $\operatorname{rango}(M(S\circ T))\le\dim\mathbb{R}^2=2<4$.

</details>

2. $M(T)_B$ tiene determinante 3 y $M(S)_B$ tiene determinante 2 ($T,S$ endomorfismos). ¿Qué vale $\det M(S\circ T)_B$ y cuánto $\det M(T^{-1})_B$?

<details>
<summary>Respuesta</summary>

$\det\big(M(S)_BM(T)_B\big)=2\cdot3=6$; $\det M(T^{-1})_B=\det\big(M(T)_B^{-1}\big)=\tfrac13$.

</details>

3. Si $S\circ T$ es isomorfismo, ¿es $T$ mono? ¿Es $S$ epi?

<details>
<summary>Respuesta</summary>

Sí a las dos: $\operatorname{Nu}(T)\subseteq\operatorname{Nu}(S\circ T)=\{0\}$ y $U=\operatorname{Im}(S\circ T)\subseteq\operatorname{Im}(S)$.

</details>

:::tip[En resumen]
- $S\circ T$ es lineal y $M(S\circ T)_{BB''}=M(S)_{B'B''}\,M(T)_{BB'}$ (el primero en actuar, a la derecha; misma base en el medio).
- $\operatorname{Nu}(T)\subseteq\operatorname{Nu}(S\circ T)$, $\operatorname{Im}(S\circ T)\subseteq\operatorname{Im}(S)$ y $\operatorname{rango}(AB)\le\min\{\operatorname{rango}A,\operatorname{rango}B\}$.
- Si $T$ es isomorfismo, $T^{-1}$ es lineal (e isomorfismo) y $M(T^{-1})_{B'B}=\big(M(T)_{BB'}\big)^{-1}$.
- Una composición que pasa por un espacio de menor dimensión no es mono (en la salida) ni epi (en la llegada) si esa dimensión es menor.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: secciones 6.4 (p. 490), 6.5 (p. 499) y 6.6 (p. 515), sobre composición, inversa e isomorfismos y la matriz de la composición.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: las partes sobre el producto de matrices como composición y sobre la inversa de una matriz.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed.: sección 5.2 (p. 182), matriz de una aplicación lineal y operaciones.
- Antes: [2.7 Cambio de base](/algebra-ii/unidad-2/teoria/cambio-de-base/) y [2.4 Clasificación](/algebra-ii/unidad-2/teoria/clasificacion/).
- Después: la [práctica de la Unidad 2](/algebra-ii/unidad-2/practica/nivel-inicial/) y, en la unidad siguiente, [autovalores y autovectores](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/), donde se busca la base en la que un endomorfismo es diagonal.
