---
title: Producto interno
description: Definición de producto interno real y de espacio euclídeo, productos usuales y no usuales en ℝⁿ, matrices y polinomios, contraejemplos y matriz de Gram.
slug: algebra-ii/unidad-4/teoria/producto-interno
sidebar:
  order: 1
  label: 4.1 Producto interno
---

En $\mathbb{R}^2$ y $\mathbb{R}^3$ el producto punto $u\cdot v=u_1v_1+\dots+u_nv_n$ permite medir: la longitud de $v$ es $\sqrt{v\cdot v}$ y dos vectores son perpendiculares cuando $u\cdot v=0$. Las Unidades 1 a 3 trabajaron con espacios vectoriales sin ninguna noción de longitud ni de ángulo. En esta unidad agregamos esa estructura, pero no la atamos a una fórmula: la definimos por sus propiedades. Así podemos medir en espacios de polinomios o de matrices, y también medir $\mathbb{R}^n$ "de otra manera", por ejemplo dando más peso a unas coordenadas que a otras.

En informática esto aparece seguido: una distancia ponderada entre registros con atributos de distinta escala, la similitud entre documentos representados como vectores, el ajuste de un modelo a mediciones (que es una proyección) y, con una advertencia importante, los códigos detectores de errores sobre $\mathbb{Z}_2^n$ ([lección 4.8](/algebra-ii/unidad-4/teoria/codigos-y-z2/)).

## Definición

:::note[Definición (producto interno y espacio euclídeo)]
Sea $V$ un espacio vectorial **real**. Un **producto interno** en $V$ es una función $\langle\,,\rangle:V\times V\to\mathbb{R}$ que a cada par $(u,v)$ le asigna un número $\langle u,v\rangle$ y cumple, para todos $u,v,w\in V$ y todo $k\in\mathbb{R}$:

1. **Simetría:** $\langle u,v\rangle=\langle v,u\rangle$.
2. **Linealidad respecto de la suma:** $\langle u+v,w\rangle=\langle u,w\rangle+\langle v,w\rangle$.
3. **Linealidad respecto del producto por escalar:** $\langle ku,v\rangle=k\langle u,v\rangle$.
4. **Positividad:** $\langle v,v\rangle\ge 0$, y $\langle v,v\rangle=0$ solo si $v=0_V$.

El par $(V,\langle\,,\rangle)$ se llama **espacio euclídeo**. Cuando no hay ambigüedad decimos simplemente "el espacio euclídeo $V$".
:::

Observemos tres cosas:

- El resultado es un **número real**, no un vector. Por eso a veces se lo llama "producto escalar".
- El mismo espacio vectorial admite **muchos** productos internos distintos. Cada uno da otro espacio euclídeo: otras longitudes, otros ángulos, otros vectores perpendiculares. Cuando un ejercicio dice "con el producto interno $\langle x,y\rangle=\dots$", **todas** las cuentas de la unidad se hacen con ese producto.
- Solo trabajamos con espacios reales. Sobre $\mathbb{Z}_2$ la positividad ni siquiera tiene sentido (en $\mathbb{Z}_2$ no hay orden), y veremos en la lección 4.8 que el "producto punto" de $\mathbb{Z}_2^n$ no es un producto interno.

### El producto interno usual de ℝⁿ

En $\mathbb{R}^n$ el **producto interno usual** (o canónico) es

$$
\langle x,y\rangle=x\cdot y=x_1y_1+x_2y_2+\dots+x_ny_n=x^ty,
$$

donde en la última expresión $x$ e $y$ se escriben como columnas. Cumple los cuatro axiomas: la simetría y la linealidad salen de las propiedades de la suma y el producto de números reales, y $\langle x,x\rangle=x_1^2+\dots+x_n^2$ es una suma de cuadrados, que es mayor o igual que cero y vale cero solo si todas las componentes son nulas.

## Propiedades que se deducen de los axiomas

Los axiomas piden linealidad solo en el **primer** lugar; la simetría la traslada al segundo.

:::note[Propiedad]
En todo espacio euclídeo $V$, para $u,v,w\in V$ y $k,k_1,\dots,k_m\in\mathbb{R}$:

1. $\langle u,v+w\rangle=\langle u,v\rangle+\langle u,w\rangle$ y $\langle u,kv\rangle=k\langle u,v\rangle$.
2. $\langle 0_V,v\rangle=\langle v,0_V\rangle=0$.
3. Si $\langle u,v\rangle=0$ para todo $v\in V$, entonces $u=0_V$.
4. $\left\langle \sum_{i}k_iv_i,\,w\right\rangle=\sum_i k_i\langle v_i,w\rangle$ (bilinealidad).
5. $\langle u+v,u+v\rangle=\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle$.
:::

**Demostración.** (1) $\langle u,v+w\rangle=\langle v+w,u\rangle=\langle v,u\rangle+\langle w,u\rangle=\langle u,v\rangle+\langle u,w\rangle$, usando simetría, linealidad en el primer lugar y simetría otra vez; lo mismo con $kv$. (2) $\langle 0_V,v\rangle=\langle 0\cdot 0_V,v\rangle=0\cdot\langle 0_V,v\rangle=0$. (3) Tomando $v=u$ queda $\langle u,u\rangle=0$, y por positividad $u=0_V$. (4) Se aplica la linealidad repetidas veces. (5) Se desarrolla con (1) y la linealidad: $\langle u+v,u+v\rangle=\langle u,u\rangle+\langle u,v\rangle+\langle v,u\rangle+\langle v,v\rangle$ y se usa la simetría. $\blacksquare$

La propiedad 3 es la que se usa para probar que un vector es nulo "porque es ortogonal a todo": aparece en complemento ortogonal y en proyecciones.

## Productos internos no usuales en ℝⁿ

Esta es la parte que más se ejercita en la materia: dada una fórmula, decidir si es un producto interno y, si lo es, trabajar con ella.

### Producto ponderado

Si $c_1,\dots,c_n$ son números reales,

$$
\langle x,y\rangle=c_1x_1y_1+c_2x_2y_2+\dots+c_nx_ny_n
$$

es simétrico y lineal para cualquier elección de los $c_i$. La positividad pide **todos los $c_i>0$**: en ese caso $\langle x,x\rangle=\sum c_ix_i^2$ es una suma de términos no negativos que se anula solo si cada $x_i=0$. Si algún $c_j\le 0$, el canónico $e_j$ cumple $\langle e_j,e_j\rangle=c_j\le 0$ con $e_j\neq 0$, y falla la positividad.

Interpretación: si los atributos de un registro están medidos en escalas muy distintas (por ejemplo, edad en años e ingreso en miles de pesos), un producto ponderado corrige la influencia de cada coordenada en las longitudes y distancias.

### Productos de la forma $u^tMv$

Si $M\in\mathbb{R}^{n\times n}$, la fórmula $\langle u,v\rangle=u^tMv=\sum_{i,j}m_{ij}u_iv_j$ es siempre lineal en cada lugar (propiedades del producto de matrices). Además:

- es **simétrica** si y solo si $M$ es simétrica ($M^t=M$): si lo es, $u^tMv$ es un número, igual a su transpuesta $v^tM^tu=v^tMu$; y si $m_{ij}\neq m_{ji}$ para algún par, entonces $\langle e_i,e_j\rangle=m_{ij}\neq m_{ji}=\langle e_j,e_i\rangle$;
- es **positiva** si y solo si $v^tMv>0$ para todo $v\neq 0$. Las matrices simétricas con esa propiedad se llaman **definidas positivas**.

Toda fórmula bilineal en $\mathbb{R}^n$ se escribe así: $m_{ij}$ es el coeficiente del término $u_iv_j$. Por ejemplo, $3x_1y_1-x_1y_2-x_2y_1+2x_2y_2$ corresponde a $M=\begin{pmatrix}3&-1\\-1&2\end{pmatrix}$.

Para matrices $2\times 2$ hay un criterio práctico.

:::note[Teorema (criterio para matrices 2×2)]
Sea $M=\begin{pmatrix}a&b\\b&c\end{pmatrix}$ simétrica. Entonces $\langle u,v\rangle=u^tMv$ es un producto interno en $\mathbb{R}^2$ si y solo si

$$
a>0\qquad\text{y}\qquad \det M=ac-b^2>0 .
$$
:::

**Demostración.** Escribimos $q(x)=x^tMx=ax_1^2+2bx_1x_2+cx_2^2$.

($\Leftarrow$) Como $a>0$, completamos cuadrados en $x_1$:

$$
q(x)=a\left(x_1+\frac{b}{a}x_2\right)^2+\frac{ac-b^2}{a}\,x_2^2 .
$$

Los dos coeficientes $a$ y $\frac{ac-b^2}{a}$ son positivos, así que $q(x)\ge 0$. Si $q(x)=0$, ambos cuadrados son nulos: $x_2=0$ y luego $x_1=-\frac{b}{a}x_2=0$. Vale la positividad.

($\Rightarrow$) Si es producto interno, $a=q(e_1)=\langle e_1,e_1\rangle>0$. Tomamos $x=(-b,a)$, que no es nulo porque $a\neq 0$:

$$
q(-b,a)=ab^2-2ab^2+ca^2=a\,(ac-b^2).
$$

Por positividad $q(-b,a)>0$, y como $a>0$ resulta $ac-b^2>0$. $\blacksquare$

Para $n\times n$ vale el **criterio de Sylvester**: una matriz simétrica es definida positiva si y solo si todos sus menores principales "de la esquina" $\det(m_{ij})_{i,j\le k}$, $k=1,\dots,n$, son positivos. También equivale a que todos sus autovalores sean positivos (ver [autovalores y autovectores](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/)). En esta materia los usamos sin demostración; en los ejemplos siempre podemos verificar la positividad completando cuadrados.

### Ejemplo 1 · Decidir si una fórmula es producto interno
<!-- check: U4.T01.E1 -->

Decidir si $\langle x,y\rangle=3x_1y_1-x_1y_2-x_2y_1+2x_2y_2$ es un producto interno en $\mathbb{R}^2$ y, en ese caso, calcular $\langle (1,2),(2,-1)\rangle$. Hacer lo mismo con $[x,y]=x_1y_1+4x_1y_2+4x_2y_1+x_2y_2$.

**Resolución.** La matriz de la primera fórmula es $M=\begin{pmatrix}3&-1\\-1&2\end{pmatrix}$, simétrica, con $a=3>0$ y $\det M=6-1=5>0$. Por el criterio, es un producto interno. Para verlo sin el teorema, completamos cuadrados:

$$
\langle x,x\rangle=3x_1^2-2x_1x_2+2x_2^2=3\left(x_1-\tfrac13x_2\right)^2+\tfrac53x_2^2\ \ge 0,
$$

y se anula solo si $x_2=0$ y $x_1=\frac13x_2=0$. Además

$$
\langle (1,2),(2,-1)\rangle=3\cdot1\cdot2-1\cdot(-1)-2\cdot2+2\cdot2\cdot(-1)=6+1-4-4=-1 .
$$

Un producto interno puede dar negativo para vectores distintos: lo que no puede ser negativo es $\langle v,v\rangle$.

La segunda fórmula tiene matriz $N=\begin{pmatrix}1&4\\4&1\end{pmatrix}$, simétrica, pero $\det N=1-16=-15<0$. No es producto interno. Un contraejemplo explícito sale de la demostración: con $x=(-b,a)=(-4,1)$, o más simple con $x=(1,-1)$,

$$
[(1,-1),(1,-1)]=1-4-4+1=-6<0 .
$$

**Comprobación.** $3\left(x_1-\frac13x_2\right)^2+\frac53x_2^2=3x_1^2-2x_1x_2+\frac13x_2^2+\frac53x_2^2=3x_1^2-2x_1x_2+2x_2^2$.

### Suma de productos de formas lineales

Una familia muy usada en la cátedra se arma con **formas lineales** (expresiones del tipo $a_1x_1+\dots+a_nx_n$). Por ejemplo, en $\mathbb{R}^2$:

$$
\langle x,y\rangle=x_1y_1+(x_1+x_2)(y_1+y_2).
$$

La idea general: si $\ell_1,\dots,\ell_m$ son formas lineales en $\mathbb{R}^n$, la fórmula $\langle x,y\rangle=\sum_i \ell_i(x)\,\ell_i(y)$ es simétrica y bilineal, y $\langle x,x\rangle=\sum_i\ell_i(x)^2\ge 0$. Es producto interno exactamente cuando el único $x$ que anula **todas** las formas es $x=0$. Matricialmente, si $L$ es la matriz cuyas filas son los coeficientes de las formas, $\ell(x)=Lx$ y $\langle x,y\rangle=(Lx)\cdot(Ly)=x^t(L^tL)y$: hace falta que $\operatorname{nul}(L)=\{0\}$.

### Ejemplo 2 · Un producto armado con formas lineales
<!-- check: U4.T01.E2 -->

Probar que $\langle x,y\rangle=x_1y_1+(x_1+x_2)(y_1+y_2)$ es un producto interno en $\mathbb{R}^2$, hallar su matriz $M$ (tal que $\langle x,y\rangle=x^tMy$) y calcular $\langle e_1,e_2\rangle$.

**Resolución.** *Simetría:* intercambiar $x$ e $y$ no cambia ninguno de los dos productos. *Linealidad:* para la suma,

$$
\langle x+z,y\rangle=(x_1+z_1)y_1+\big((x_1+z_1)+(x_2+z_2)\big)(y_1+y_2)=\langle x,y\rangle+\langle z,y\rangle,
$$

y análogamente $\langle kx,y\rangle=k\langle x,y\rangle$. *Positividad:* $\langle x,x\rangle=x_1^2+(x_1+x_2)^2\ge0$; si vale cero, $x_1=0$ y $x_1+x_2=0$, así que $x_2=0$.

Desarrollando, $\langle x,y\rangle=2x_1y_1+x_1y_2+x_2y_1+x_2y_2$, de modo que

$$
M=\begin{pmatrix}2&1\\1&1\end{pmatrix}=L^tL,\qquad L=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
$$

El criterio también lo confirma: $2>0$ y $\det M=1>0$. Finalmente $\langle e_1,e_2\rangle=1\cdot0+(1+0)(0+1)=1\neq 0$: **con este producto los canónicos no son perpendiculares**. En la [lección 4.2](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/) calculamos el ángulo que forman.

**Comprobación.** $x^tMy=2x_1y_1+x_1y_2+x_2y_1+x_2y_2=x_1y_1+(x_1y_1+x_1y_2+x_2y_1+x_2y_2)$, que es la fórmula dada.

## Productos internos en espacios de matrices y de polinomios

### En ℝ²ˣ²: el producto de la traza

En $\mathbb{R}^{m\times n}$ se usa

$$
\langle A,B\rangle=\operatorname{tr}(A^tB)=\sum_{i,j}a_{ij}b_{ij}.
$$

La igualdad entre la traza y la suma sale de calcular la diagonal de $A^tB$: su entrada $(j,j)$ es $\sum_i a_{ij}b_{ij}$. Es decir, es el producto usual de $\mathbb{R}^{mn}$ aplicado a las entradas "en fila", y por eso cumple los cuatro axiomas. En los exámenes suele aparecer en $\mathbb{R}^{2\times 2}$, junto con subespacios como las matrices simétricas, las antisimétricas o las de traza nula.

### Ejemplo 3 · Producto de matrices con la traza
<!-- check: U4.T01.E3 -->

En $\mathbb{R}^{2\times2}$ con $\langle A,B\rangle=\operatorname{tr}(A^tB)$, calcular $\langle S,K\rangle$ para $S=\begin{pmatrix}1&2\\2&3\end{pmatrix}$ y $K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, y $\langle A,B\rangle$ para $A=\begin{pmatrix}1&2\\0&-1\end{pmatrix}$, $B=\begin{pmatrix}3&-1\\4&2\end{pmatrix}$.

**Resolución.** Sumando productos de entradas en la misma posición:

$$
\langle S,K\rangle=1\cdot0+2\cdot1+2\cdot(-1)+3\cdot0=0,\qquad
\langle A,B\rangle=3-2+0-2=-1 .
$$

El primer resultado no es casual: toda matriz simétrica es perpendicular a toda antisimétrica con este producto (los términos fuera de la diagonal se cancelan de a pares y la diagonal de una antisimétrica es nula).

**Comprobación.** Con la traza: $A^tB=\begin{pmatrix}1&0\\2&-1\end{pmatrix}\begin{pmatrix}3&-1\\4&2\end{pmatrix}=\begin{pmatrix}3&-1\\2&-4\end{pmatrix}$, cuya traza es $3-4=-1$.

### En P₂[ℝ]: por coeficientes y por evaluación

En $P_2[\mathbb{R}]$, con $p=a_0+a_1x+a_2x^2$ y $q=b_0+b_1x+b_2x^2$, hay dos productos habituales.

- **Por coeficientes:** $\langle p,q\rangle=a_0b_0+a_1b_1+a_2b_2$. Es el producto usual aplicado a las coordenadas en $E=\{1,x,x^2\}$: $\langle p,q\rangle=[p]_E^t[q]_E$.
- **Por evaluación en tres puntos distintos** $t_1,t_2,t_3$:

$$
\langle p,q\rangle=p(t_1)q(t_1)+p(t_2)q(t_2)+p(t_3)q(t_3).
$$

En el segundo, simetría y linealidad son inmediatas (evaluar es lineal: $(p+r)(t)=p(t)+r(t)$). Para la positividad, $\langle p,p\rangle=p(t_1)^2+p(t_2)^2+p(t_3)^2\ge0$, y si vale cero entonces $p$ se anula en tres puntos distintos. Un polinomio no nulo de grado a lo sumo 2 tiene a lo sumo 2 raíces, así que $p$ es el polinomio nulo (ver [polinomios](/algebra-ii/repaso/polinomios/)).

**Por qué dos puntos no alcanzan.** Con $\langle p,q\rangle=p(0)q(0)+p(1)q(1)$ en $P_2[\mathbb{R}]$, el polinomio $p=x^2-x=x(x-1)$ no es nulo y cumple $\langle p,p\rangle=0^2+0^2=0$. Falla la positividad. En general, la evaluación en $m$ puntos distintos es producto interno en $P_n[\mathbb{R}]$ si y solo si $m\ge n+1$.

### Ejemplo 4 · Producto por evaluación
<!-- check: U4.T01.E4 -->

En $P_2[\mathbb{R}]$ con $\langle p,q\rangle=p(-1)q(-1)+p(0)q(0)+p(1)q(1)$, calcular $\langle 1+x,\,x^2\rangle$.

**Resolución.** Conviene tabular los valores en los tres puntos:

| $t$ | $-1$ | $0$ | $1$ |
|---|---|---|---|
| $1+t$ | $0$ | $1$ | $2$ |
| $t^2$ | $1$ | $0$ | $1$ |

y sumar los productos columna por columna: $\langle 1+x,x^2\rangle=0\cdot1+1\cdot0+2\cdot1=2$.

**Comprobación.** El producto es el usual de $\mathbb{R}^3$ entre los vectores de valores $(0,1,2)$ y $(1,0,1)$: $0+0+2=2$. Que sea producto interno se apoya en que la matriz de evaluación $\begin{pmatrix}1&-1&1\\1&0&0\\1&1&1\end{pmatrix}$ (filas: $(1,t,t^2)$ en cada punto) tiene determinante $2\neq0$, es decir, solo el polinomio nulo tiene los tres valores nulos.

## Cuando una fórmula no es producto interno

Para mostrar que una fórmula **no** es producto interno alcanza con **un** contraejemplo concreto de **un** axioma. Algunos casos típicos en $\mathbb{R}^2$:

- **Falla la simetría:** $\langle x,y\rangle=2x_1y_1+x_2y_1+x_2y_2$. Da $\langle e_1,e_2\rangle=0$ pero $\langle e_2,e_1\rangle=1$. (Su "matriz" $\begin{pmatrix}2&0\\1&1\end{pmatrix}$ no es simétrica.)
- **Falla la linealidad:** $\langle x,y\rangle=x_1y_1+x_2y_2+1$. Da $\langle 0,0\rangle=1$, y todo producto interno cumple $\langle 0,v\rangle=0$. Otro caso: $\langle x,y\rangle=x_1^2y_1^2+x_2y_2$, con $\langle 2e_1,e_1\rangle=4\neq 2\langle e_1,e_1\rangle=2$.
- **Falla la positividad porque da negativo:** $\langle x,y\rangle=x_1y_1-x_2y_2$, con $\langle e_2,e_2\rangle=-1$.
- **Falla la positividad porque se anula en un vector no nulo:** $\langle x,y\rangle=x_1y_1$, con $\langle e_2,e_2\rangle=0$ y $e_2\neq 0$. O $\langle x,y\rangle=(x_1+x_2)(y_1+y_2)$, que se anula en $(1,-1)$: una sola forma lineal no alcanza en $\mathbb{R}^2$.

## Matriz de Gram

Fijada una base, todo producto interno se calcula con una matriz.

:::note[Definición (matriz de Gram)]
Sea $B=\{v_1,\dots,v_n\}$ una base del espacio euclídeo $V$. La **matriz de Gram** del producto interno en la base $B$ es la matriz $G_B\in\mathbb{R}^{n\times n}$ con entradas $(G_B)_{ij}=\langle v_i,v_j\rangle$.
:::

:::note[Propiedad]
Para todos $u,v\in V$,

$$
\langle u,v\rangle=[u]_B^t\,G_B\,[v]_B .
$$

$G_B$ es simétrica y sus entradas diagonales $\langle v_i,v_i\rangle$ son positivas.
:::

**Demostración.** Si $[u]_B=(a_1,\dots,a_n)^t$ y $[v]_B=(b_1,\dots,b_n)^t$, por bilinealidad

$$
\langle u,v\rangle=\Big\langle \sum_i a_iv_i,\sum_j b_jv_j\Big\rangle=\sum_{i,j}a_ib_j\langle v_i,v_j\rangle=[u]_B^t\,G_B\,[v]_B .
$$

La simetría de $G_B$ viene de la simetría del producto y la positividad de la diagonal, de que los $v_i$ no son nulos. $\blacksquare$

Para un producto $x^tMy$ en $\mathbb{R}^n$, la matriz de Gram en la base canónica es la propia $M$. Para el producto usual es la identidad. La matriz de Gram permite trasladar cualquier producto interno de un espacio de dimensión $n$ a una cuenta con coordenadas (ver [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/)).

### Ejemplo 5 · Matriz de Gram del producto por evaluación
<!-- check: U4.T01.E5 -->

En $P_2[\mathbb{R}]$ con el producto del Ejemplo 4 y la base $E=\{1,x,x^2\}$ (en ese orden), hallar $G_E$, verificar que es definida positiva y calcular $\langle p,q\rangle$ para $p=2-x+x^2$ y $q=1+3x-x^2$ de dos maneras.

**Resolución.** Cada entrada es $\langle x^i,x^j\rangle=\sum_{t\in\{-1,0,1\}}t^{i+j}$, que vale $3$ si $i+j=0$, $0$ si $i+j$ es impar y $2$ si $i+j$ es par positivo:

$$
G_E=\begin{pmatrix}3&0&2\\0&2&0\\2&0&2\end{pmatrix}.
$$

Sus menores principales son $3$, $3\cdot2-0=6$ y $\det G_E=3\cdot4-0+2\cdot(0-4)=4$, todos positivos (criterio de Sylvester), en concordancia con que ya probamos la positividad.

*Primera manera (con la matriz):* $[p]_E=(2,-1,1)^t$, $[q]_E=(1,3,-1)^t$ y

$$
[p]_E^tG_E=(2,-1,1)\begin{pmatrix}3&0&2\\0&2&0\\2&0&2\end{pmatrix}=(8,-2,6),\qquad (8,-2,6)\begin{pmatrix}1\\3\\-1\end{pmatrix}=8-6-6=-4 .
$$

*Segunda manera (evaluando):* $p(-1)=4$, $p(0)=2$, $p(1)=2$; $q(-1)=-3$, $q(0)=1$, $q(1)=3$. Entonces $\langle p,q\rangle=4\cdot(-3)+2\cdot1+2\cdot3=-12+2+6=-4$.

**Comprobación.** Las dos maneras dan $-4$.

:::caution[Errores frecuentes]
- **Probar los axiomas con números.** Un ejemplo numérico no prueba simetría ni positividad para todos los vectores. Un ejemplo sí alcanza para **refutar**.
- **Olvidar el "solo si" de la positividad.** $\langle x,y\rangle=x_1y_1$ en $\mathbb{R}^2$ cumple $\langle x,x\rangle\ge0$, pero $\langle e_2,e_2\rangle=0$ con $e_2\neq0$.
- **Mirar solo la diagonal de $M$.** $N=\begin{pmatrix}1&4\\4&1\end{pmatrix}$ tiene diagonal positiva y no es definida positiva ($\det N=-15$).
- **Usar el criterio $2\times2$ con una matriz no simétrica.** Primero se verifica la simetría; el criterio no la reemplaza.
- **Evaluar en dos puntos en $P_2[\mathbb{R}]$.** Con dos nodos, $x^2-x$ (o el producto de los factores que se anulan en esos nodos) es un vector no nulo de "longitud cero".
- **Suponer que $\langle u,v\rangle\ge0$ siempre.** Solo $\langle v,v\rangle$ es no negativo; en el Ejemplo 1, $\langle(1,2),(2,-1)\rangle=-1$.
:::

## Autoevaluación

<details>
<summary>1. ¿Para qué valores de k es ⟨x, y⟩ = x₁y₁ + k·x₂y₂ un producto interno en ℝ²?</summary>

Para $k>0$. Si $k\le0$, $\langle e_2,e_2\rangle=k\le 0$ con $e_2\neq0$.

</details>

<details>
<summary>2. ¿Es producto interno en ℝ³ la fórmula (x₁ + x₂)(y₁ + y₂) + x₃y₃?</summary>

No. Es simétrica y bilineal, pero el vector no nulo $(1,-1,0)$ cumple $\langle v,v\rangle=0+0=0$.

</details>

<details>
<summary>3. En P₂[ℝ], ¿es producto interno ⟨p, q⟩ = p(0)q(0) + p′(0)q′(0) + p″(0)q″(0)?</summary>

Sí. Si $p=a_0+a_1x+a_2x^2$, entonces $\langle p,p\rangle=a_0^2+a_1^2+4a_2^2$, que se anula solo si $p=0$. Es un producto ponderado de los coeficientes con pesos $1,1,4$.

</details>

:::tip[En resumen]
- Un producto interno es una función $V\times V\to\mathbb{R}$ simétrica, lineal en cada lugar y positiva; con él, $V$ es un espacio euclídeo.
- En $\mathbb{R}^n$, $\langle x,y\rangle=x^tMy$ es producto interno si y solo si $M$ es simétrica y definida positiva; en $2\times2$: $m_{11}>0$ y $\det M>0$.
- Productos habituales: ponderado con pesos positivos, suma de productos de formas lineales que solo se anulan juntas en $0$, $\operatorname{tr}(A^tB)$ en matrices, coeficientes o evaluación en $n+1$ puntos distintos en $P_n[\mathbb{R}]$.
- Para refutar, un contraejemplo de un axioma; para probar, un argumento general.
- En una base $B$: $\langle u,v\rangle=[u]_B^t\,G_B\,[v]_B$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 1.2 (producto punto en $\mathbb{R}^n$, p. 18) y sección 7.1, "Espacios con producto interno" (p. 554).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ortogonalidad y mínimos cuadrados (espacios con producto interno).
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed.: capítulo 8, "Espacios euclídeos".
- Repaso: [vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/), [polinomios](/algebra-ii/repaso/polinomios/).
- Siguiente: [4.2 Norma, distancia y ángulo](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/). Presentación de la unidad: [Unidad 4](/algebra-ii/unidad-4/).
