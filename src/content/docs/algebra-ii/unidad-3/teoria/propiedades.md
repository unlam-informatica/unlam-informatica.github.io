---
title: Propiedades de los autovalores
description: Independencia lineal de autovectores de autovalores distintos, autovalores de potencias, inversa, transpuesta y polinomios de una matriz, filas de suma constante, y traza y determinante como suma y producto de autovalores.
slug: algebra-ii/unidad-3/teoria/propiedades
sidebar:
  order: 3
  label: 3.3 Propiedades
---

## Para qué sirve

Calcular el polinomio característico de una matriz grande es costoso. Las propiedades de esta
lección permiten **deducir autovalores sin recalcular**: los de $A^3$, $A^{-1}$, $A^2-3A$ o $A+5I$
salen de los de $A$; los de $A^t$ son los mismos que los de $A$; una matriz cuyas filas suman lo
mismo tiene ese número como autovalor; y la traza y el determinante dan dos controles baratos de
cualquier cuenta. Además, el primer resultado (autovectores de autovalores distintos son
linealmente independientes) es el cimiento de la [diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/).

En toda la lección, $A\in\mathbb{R}^{n\times n}$ y "autovalor" significa autovalor real.

## Autovectores de autovalores distintos son independientes

:::note[Teorema]
Sean $\lambda_1,\dots,\lambda_k$ autovalores de $A$ **distintos entre sí** y $v_1,\dots,v_k$
autovectores asociados ($Av_i=\lambda_iv_i$, $v_i\neq0$). Entonces $\{v_1,\dots,v_k\}$ es
linealmente independiente.
:::

**Demostración.** Por inducción completa en $k$.

*Caso $k=1$.* Un único vector no nulo es linealmente independiente.

*Paso inductivo.* Supongamos que el enunciado vale para $k-1$ autovectores (con $k\ge2$) y
sean $v_1,\dots,v_k$ como en el enunciado. Consideremos una combinación lineal nula

$$
\alpha_1v_1+\alpha_2v_2+\dots+\alpha_kv_k=0 .\tag{1}
$$

Aplicamos $A$ a ambos miembros y usamos $Av_i=\lambda_iv_i$:

$$
\alpha_1\lambda_1v_1+\alpha_2\lambda_2v_2+\dots+\alpha_k\lambda_kv_k=0 .\tag{2}
$$

Multiplicamos (1) por $\lambda_k$ y restamos de (2); el último término desaparece:

$$
\alpha_1(\lambda_1-\lambda_k)v_1+\dots+\alpha_{k-1}(\lambda_{k-1}-\lambda_k)v_{k-1}=0 .
$$

Por hipótesis inductiva, $\{v_1,\dots,v_{k-1}\}$ es independiente; entonces cada coeficiente se
anula: $\alpha_i(\lambda_i-\lambda_k)=0$ para $i=1,\dots,k-1$. Como los autovalores son distintos,
$\lambda_i-\lambda_k\neq0$, y por lo tanto $\alpha_1=\dots=\alpha_{k-1}=0$. Reemplazando en (1)
queda $\alpha_kv_k=0$; como $v_k\neq0$, también $\alpha_k=0$. Todos los coeficientes son nulos.
$\blacksquare$

:::note[Corolario]
Si $A\in\mathbb{R}^{n\times n}$ tiene $n$ autovalores reales distintos, los autovectores
correspondientes (uno por autovalor) forman una **base de $\mathbb{R}^n$**: son $n$ vectores
independientes en un espacio de dimensión $n$.
:::

## Potencias, inversa y polinomios en $A$

:::note[Propiedad]
Sea $v$ un autovector de $A$ con autovalor $\lambda$ y sea $k\ge 1$ entero. Entonces:

1. $v$ es autovector de $A^k$ con autovalor $\lambda^k$.
2. Si $A$ es inversible, $\lambda\neq0$ y $v$ es autovector de $A^{-1}$ con autovalor
   $\lambda^{-1}$.
3. Para todo polinomio $p(x)=c_mx^m+\dots+c_1x+c_0$, el vector $v$ es autovector de
   $p(A)=c_mA^m+\dots+c_1A+c_0I$ con autovalor $p(\lambda)$. En particular, $A+cI$ tiene autovalor
   $\lambda+c$ con el mismo $v$.
:::

**Demostración.**

1. Por inducción en $k$. Para $k=1$ es la hipótesis. Si $A^kv=\lambda^kv$, entonces
   $A^{k+1}v=A(A^kv)=A(\lambda^kv)=\lambda^kAv=\lambda^{k+1}v$.
2. Si $A$ es inversible, $0$ no es autovalor (ver la
   [lección 3.1](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/)), así que
   $\lambda\neq0$. Multiplicamos $Av=\lambda v$ por $A^{-1}$ a izquierda:
   $v=\lambda A^{-1}v$, y dividimos por $\lambda$: $A^{-1}v=\lambda^{-1}v$.
3. Por el punto 1, $A^jv=\lambda^jv$ para $j\ge1$, y $A^0v=Iv=\lambda^0v$. Por linealidad,

   $$
   p(A)v=\sum_{j=0}^m c_jA^jv=\sum_{j=0}^m c_j\lambda^jv=p(\lambda)v.\ \blacksquare
   $$


El mismo argumento da $A^{-k}v=\lambda^{-k}v$ para $A$ inversible.

## $A$ y $A^t$ tienen el mismo polinomio característico

:::note[Propiedad]
Para toda $A\in\mathbb{R}^{n\times n}$, $p_{A^t}(\lambda)=p_A(\lambda)$. En consecuencia, $A$ y $A^t$
tienen los mismos autovalores con las mismas multiplicidades algebraicas.
:::

**Demostración.** Como $(\lambda I-A)^t=\lambda I-A^t$ y una matriz tiene el mismo determinante que
su transpuesta,

$$
p_{A^t}(\lambda)=\det(\lambda I-A^t)=\det\big((\lambda I-A)^t\big)=\det(\lambda I-A)=p_A(\lambda).\ \blacksquare
$$

Que los autovalores coincidan **no** significa que los autovectores coincidan: los autoespacios de
$A$ y de $A^t$ suelen ser distintos (ejemplo 3). Sí coinciden sus dimensiones, porque
$\operatorname{rango}(\lambda I-A)=\operatorname{rango}\big((\lambda I-A)^t\big)$.

## Filas o columnas de suma constante

:::note[Propiedad]
Sea $\mathbf 1=(1,1,\dots,1)$ el vector de unos.

- Si **todas las filas** de $A$ suman el mismo número $s$, entonces $s$ es autovalor de $A$ con
  autovector $\mathbf 1$.
- Si **todas las columnas** de $A$ suman el mismo número $s$, entonces $s$ es autovalor de $A$,
  aunque $\mathbf 1$ no sea necesariamente su autovector.
:::

**Demostración.** La componente $i$ de $A\mathbf 1$ es la suma de la fila $i$ de $A$, es decir $s$:
$A\mathbf 1=s\mathbf 1$ y $\mathbf 1\neq0$. Si las columnas suman $s$, las filas de $A^t$ suman $s$,
y por lo anterior $s$ es autovalor de $A^t$; como $A^t$ y $A$ tienen el mismo polinomio
característico, $s$ es autovalor de $A$. $\blacksquare$

Este resultado es el que, en la [lección 3.8](/algebra-ii/unidad-3/teoria/cadenas-de-markov/),
asegura que toda matriz de transición de una cadena de Markov tiene el autovalor $1$.

## Traza y determinante

Recordemos de la [lección 3.2](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/) que
$p_A(\lambda)=\lambda^n-\operatorname{tr}(A)\lambda^{n-1}+\dots+(-1)^n\det(A)$.

:::note[Propiedad]
Si $p_A$ se factoriza en $\mathbb{R}$ como $p_A(\lambda)=(\lambda-\lambda_1)\cdots(\lambda-\lambda_n)$
(autovalores repetidos tantas veces como su multiplicidad algebraica), entonces

$$
\operatorname{tr}(A)=\lambda_1+\dots+\lambda_n,\qquad \det(A)=\lambda_1\lambda_2\cdots\lambda_n .
$$

En particular, $A$ es inversible si y solo si ningún $\lambda_i$ es nulo.
:::

**Demostración.** Al desarrollar el producto, el coeficiente de $\lambda^{n-1}$ es
$-(\lambda_1+\dots+\lambda_n)$; igualándolo con $-\operatorname{tr}(A)$ se obtiene la primera
fórmula. El término independiente del producto es $(-1)^n\lambda_1\cdots\lambda_n$ y debe coincidir
con $p_A(0)=(-1)^n\det(A)$, lo que da la segunda. $\blacksquare$

Si $p_A$ **no** se factoriza en $\mathbb{R}$, las fórmulas valen igual con los autovalores
complejos contados con multiplicidad, pero la suma y el producto de los autovalores *reales* ya no
alcanzan a reconstruir la traza ni el determinante. Por ejemplo, la rotación
$R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ tiene traza $0$ y determinante $1$ y ningún autovalor real.

## Ejemplos resueltos

### Ejemplo 1 · Filas de suma constante, traza y determinante

<!-- check: U3.T03.E1 -->

Hallar los autovalores y una base de autovectores de

$$
A=\begin{pmatrix}2&1&1\\0&3&1\\1&1&2\end{pmatrix}
$$

sin desarrollar el polinomio por cofactores.

**Un autovalor.** Las tres filas suman $4$, así que $4$ es autovalor y $\mathbf 1=(1,1,1)$ es un
autovector: $A\mathbf 1=(4,4,4)^t$.

**Los otros dos.** $\operatorname{tr}(A)=2+3+2=7$ y $\det(A)=2(6-1)-1(0-1)+1(0-3)=10+1-3=8$. Si los
autovalores son $4$, $\mu_1$ y $\mu_2$, entonces
$4+\mu_1+\mu_2=7$ y $4\mu_1\mu_2=8$, es decir
$\mu_1+\mu_2=3$ y $\mu_1\mu_2=2$. Son las raíces de $x^2-3x+2=(x-1)(x-2)$:

$$
p_A(\lambda)=(\lambda-4)(\lambda-1)(\lambda-2),\qquad \lambda\in\{1,2,4\}.
$$

**Autovectores.** Resolvemos $(\lambda I-A)x=0$ para $\lambda=1$ y $\lambda=2$:

$$
I-A=\begin{pmatrix}-1&-1&-1\\0&-2&-1\\-1&-1&-1\end{pmatrix}\ \Rightarrow\ y=-\tfrac12z,\ x=-y-z=-\tfrac12z
\ \Rightarrow\ v_1=(1,1,-2)\ \text{(tomando }z=-2\text{)},
$$

$$
2I-A=\begin{pmatrix}0&-1&-1\\0&-1&-1\\-1&-1&0\end{pmatrix}\ \Rightarrow\ y=-z,\ x=-y=z
\ \Rightarrow\ v_2=(1,-1,1).
$$

**Comprobación.** $Av_1=(2+1-2,\;3-2,\;1+1-4)^t=(1,1,-2)^t=v_1$ y
$Av_2=(2-1+1,\;-3+1,\;1-1+2)^t=(2,-2,2)^t=2v_2$. Como los tres autovalores son distintos, el
teorema asegura que $\{(1,1,-2),(1,-1,1),(1,1,1)\}$ es independiente; en efecto, la matriz que
tiene esos vectores por columnas tiene determinante $6\neq0$.

:::tip[Resultado]
Autovalores $1,2,4$ con autovectores $(1,1,-2)$, $(1,-1,1)$, $(1,1,1)$, base de $\mathbb{R}^3$.
:::

### Ejemplo 2 · Autovalores de $A^{-1}$, $A^3$, $A^2-3A$ y $A+5I$

<!-- check: U3.T03.E2 -->

Con la $A$ del ejemplo anterior, hallar los autovalores de $A^{-1}$, $A^3$, $A+5I$ y
$X=A^2-3A$, y calcular $\det(X)$ y $\operatorname{tr}(X)$.

Los autovectores de $A$ lo son de todas estas matrices (propiedad de potencias, inversa y
polinomios), con autovalores:

| de $A$ | $1$ | $2$ | $4$ |
|---|---|---|---|
| $A^{-1}$: $\lambda^{-1}$ | $1$ | $\tfrac12$ | $\tfrac14$ |
| $A^{3}$: $\lambda^{3}$ | $1$ | $8$ | $64$ |
| $A+5I$: $\lambda+5$ | $6$ | $7$ | $9$ |
| $A^2-3A$: $\lambda^2-3\lambda$ | $-2$ | $-2$ | $4$ |

$A$ es inversible porque $\det(A)=8\neq0$. Para $X=A^2-3A$ tenemos $p(x)=x^2-3x$ y $-2$ aparece con $m_a=2$ y $4$
con $m_a=1$ (los tres autovectores $v_1,v_2,v_3$ del ejemplo 1 son una base formada por
autovectores de $X$, con autovalores $-2,-2,4$), de modo que

$$
\det(X)=(-2)(-2)(4)=16,\qquad \operatorname{tr}(X)=-2-2+4=0 .
$$

**Comprobación directa.** $A^2=\begin{pmatrix}5&6&5\\1&10&5\\4&6&6\end{pmatrix}$ y

$$
X=A^2-3A=\begin{pmatrix}-1&3&2\\1&1&2\\1&3&0\end{pmatrix},
$$

cuya traza es $-1+1+0=0$. Además $X(1,1,1)^t=(4,4,4)^t=4(1,1,1)^t$ y
$X(1,-1,1)^t=(-2,2,-2)^t=-2(1,-1,1)^t$.

:::tip[Resultado]
Los autovalores de $A^2-3A$ son $-2$ (doble) y $4$; $\det(A^2-3A)=16$ y su traza es $0$. No hizo
falta calcular ningún polinomio característico nuevo.
:::

### Ejemplo 3 · $A$ y $A^t$: mismos autovalores, distintos autoespacios

<!-- check: U3.T03.E3 -->

Comparar los autovalores y los autoespacios de $A=\begin{pmatrix}1&1\\0&2\end{pmatrix}$ y de $A^t$.

$A$ es triangular, así que $p_A(\lambda)=(\lambda-1)(\lambda-2)$, y $A^t=\begin{pmatrix}1&0\\1&2\end{pmatrix}$
también es triangular con la misma diagonal: $p_{A^t}=p_A$.

- $E_1(A)$: $I-A=\begin{pmatrix}0&-1\\0&-1\end{pmatrix}$ da $y=0$: $E_1(A)=\operatorname{gen}\{(1,0)\}$.
- $E_2(A)$: $2I-A=\begin{pmatrix}1&-1\\0&0\end{pmatrix}$ da $x=y$: $E_2(A)=\operatorname{gen}\{(1,1)\}$.
- $E_1(A^t)$: $I-A^t=\begin{pmatrix}0&0\\-1&-1\end{pmatrix}$ da $y=-x$: $E_1(A^t)=\operatorname{gen}\{(1,-1)\}$.
- $E_2(A^t)$: $2I-A^t=\begin{pmatrix}1&0\\-1&0\end{pmatrix}$ da $x=0$: $E_2(A^t)=\operatorname{gen}\{(0,1)\}$.

:::tip[Resultado]
Los autovalores coinciden ($1$ y $2$), pero los autovectores no: $(1,0)$ es autovector de $A$ y no
lo es de $A^t$, pues $A^t(1,0)^t=(1,1)^t$.
:::

### Ejemplo 4 · Columnas de suma constante

<!-- check: U3.T03.E4 -->

Hallar los autovalores de $B=\begin{pmatrix}1&4\\2&-1\end{pmatrix}$ y el autovector de cada uno.

Las dos columnas suman $3$ ($1+2$ y $4+(-1)$), mientras que las filas suman $5$ y $1$. Por la
propiedad, $3$ es autovalor de $B$. Como $\operatorname{tr}(B)=0$, el otro autovalor es $-3$
(comprobación con el determinante: $3\cdot(-3)=-9=\det(B)=-1-8$).

Para $\lambda=3$: $3I-B=\begin{pmatrix}2&-4\\-2&4\end{pmatrix}$ da $x=2y$, así que
$E_3(B)=\operatorname{gen}\{(2,1)\}$. Observemos que $(1,1)$ **no** es autovector de $B$:
$B(1,1)^t=(5,1)^t$. En cambio, sí lo es de $B^t$, cuyas filas suman $3$:
$B^t(1,1)^t=(3,3)^t$.

:::tip[Resultado]
Autovalores $3$ y $-3$, con $E_3(B)=\operatorname{gen}\{(2,1)\}$. Con columnas de suma constante, el
autovector de ese autovalor no es $\mathbf 1$ (salvo que también las filas sumen lo mismo).
:::

### Ejemplo 5 · Los autovalores no son aditivos

<!-- check: U3.T03.E5 -->

Sean $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ y $B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$. Ambas son
triangulares con diagonal nula, así que su único autovalor es $0$. Pero

$$
A+B=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad p_{A+B}(\lambda)=\lambda^2-1,
$$

con autovalores $\pm1$, y $AB=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ tiene autovalores $1$ y $0$, no
$0\cdot0$. Los autovalores de una suma o de un producto de matrices **no** se obtienen sumando o
multiplicando los de los factores; las propiedades de esta lección valen para una sola matriz y
sus polinomios.

:::caution[Errores frecuentes]
- **Suponer que los autovalores de $A+B$ (o de $AB$) son las sumas (o los productos) de los de $A$
  y $B$.** Falla ya en el ejemplo 5. Con un mismo autovector $v$ de ambas sí vale: $(A+B)v=(\lambda+\mu)v$.
- **Decir que $A$ y $A^t$ tienen los mismos autovectores.** Tienen los mismos autovalores, no los
  mismos autovectores (ejemplo 3).
- **Creer que todo autovalor de $A^k$ es la potencia de un autovalor *real* de $A$.** Para la
  rotación $R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ se tiene $R^2=-I$, con autovalor real $-1$,
  mientras que $R$ no tiene autovalores reales. La implicación válida es "$\lambda$ autovalor de $A$
  $\Rightarrow$ $\lambda^k$ autovalor de $A^k$".
- **Aplicar $A^{-1}$ con autovalor $0$.** Solo se invierte si $A$ es inversible; $0$ no tiene
  inverso.
- **Usar suma y producto de autovalores cuando $p_A$ no se factoriza en $\mathbb{R}$.**
- **Probar independencia de autovectores del *mismo* autovalor.** El teorema pide autovalores
  distintos; dos autovectores de un mismo $\lambda$ pueden ser dependientes (múltiplos) o no.
- **Olvidar que $A+cI$ solo desplaza.** Los autovectores no cambian, pero $A+cI$ no tiene los
  autovalores de $A$ multiplicados por $c$.
:::

## Autoevaluación

<details>
<summary>1. Una matriz 3 × 3 tiene autovalores 1, 2 y 5. ¿Cuánto vale det(A² + I)?</summary>

Los autovalores de $A^2+I$ son $1+1=2$, $4+1=5$ y $25+1=26$. El determinante es $2\cdot5\cdot26=260$.

</details>

<details>
<summary>2. ¿Puede una matriz 2 × 2 con filas de suma 3 tener traza 5?</summary>

Sí: tiene autovalor $3$ y, con traza $5$, el otro es $2$. Por ejemplo, $\begin{pmatrix}2&1\\0&3\end{pmatrix}$ lo cumple.

</details>

<details>
<summary>3. Si A tiene autovalor 2 con autovector v, ¿qué autovalor tiene A³ − 2A + 4I para v?</summary>

$p(2)=8-4+4=8$.

</details>

:::tip[En resumen]
- Autovectores de autovalores distintos son linealmente independientes; con $n$ autovalores
  distintos hay una base de autovectores.
- Si $Av=\lambda v$, entonces $A^kv=\lambda^kv$, $A^{-1}v=\lambda^{-1}v$ y $p(A)v=p(\lambda)v$.
- $A$ y $A^t$ tienen el mismo polinomio característico, pero no los mismos autovectores.
- Filas de suma $s$: $s$ es autovalor con autovector $\mathbf 1$; columnas de suma $s$: $s$ es
  autovalor.
- Si $p_A$ se factoriza en $\mathbb{R}$: $\operatorname{tr}(A)=\sum\lambda_i$ y $\det(A)=\prod\lambda_i$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 4.3 (p. 303) para
  propiedades de los eigenvalores y la independencia de eigenvectores, y 4.4 (p. 312).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: sección sobre valores propios y la
  independencia de vectores propios de valores propios distintos.
- Anterior: [3.2 Polinomio característico](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/).
  Siguiente: [3.4 Matrices semejantes](/algebra-ii/unidad-3/teoria/matrices-semejantes/).
