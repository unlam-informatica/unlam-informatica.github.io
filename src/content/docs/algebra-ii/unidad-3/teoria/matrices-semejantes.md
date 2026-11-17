---
title: Matrices semejantes
description: Definición de semejanza, relación de equivalencia, invariantes (determinante, polinomio característico, autovalores, traza y rango), interpretación como matrices de un mismo endomorfismo y un contraejemplo con igual polinomio característico.
slug: algebra-ii/unidad-3/teoria/matrices-semejantes
sidebar:
  order: 4
  label: 3.4 Matrices semejantes
---

## Para qué sirve

Un mismo endomorfismo $T:V\to V$ tiene una matriz distinta para cada base elegida. Esas matrices
se ven muy diferentes, pero describen **la misma transformación**; lo que dependa solo de $T$ (y no
de la base) tiene que ser igual en todas ellas. La **semejanza** es la relación que formaliza esta
idea, y sus **invariantes** son las propiedades de $T$ que cualquier matriz de $T$ hereda:
autovalores, traza, determinante, rango. Cuando elegimos la base de modo que la matriz sea
diagonal, estamos diagonalizando; esa es la [lección 3.5](/algebra-ii/unidad-3/teoria/diagonalizacion/).

## Definición y relación de equivalencia

:::note[Definición]
Sean $A,B\in\mathbb{R}^{n\times n}$. Decimos que $A$ es **semejante** a $B$ si existe una matriz
inversible $C\in\mathbb{R}^{n\times n}$ tal que

$$
A=CBC^{-1}\qquad(\text{equivalentemente, } B=C^{-1}AC).
$$
:::

:::note[Propiedad]
La semejanza es una **relación de equivalencia** en $\mathbb{R}^{n\times n}$: es reflexiva,
simétrica y transitiva.
:::

**Demostración.**

- *Reflexiva.* $A=IAI^{-1}$.
- *Simétrica.* Si $A=CBC^{-1}$, multiplicando por $C^{-1}$ a izquierda y por $C$ a derecha,
  $B=C^{-1}AC=(C^{-1})A(C^{-1})^{-1}$, con $C^{-1}$ inversible.
- *Transitiva.* Si $A=CBC^{-1}$ y $B=DED^{-1}$, entonces
  $A=C(DED^{-1})C^{-1}=(CD)E(CD)^{-1}$, y $CD$ es inversible. $\blacksquare$

Por ser de equivalencia, tiene sentido decir "$A$ y $B$ son semejantes" sin ordenarlas, y
$\mathbb{R}^{n\times n}$ se parte en **clases de semejanza**: dos matrices están en la misma clase
si y solo si son matrices del mismo endomorfismo en bases distintas (ver más abajo).

## Invariantes de la semejanza

:::note[Teorema]
Si $A$ y $B$ son semejantes, entonces:

1. $\det(A)=\det(B)$.
2. $p_A(\lambda)=p_B(\lambda)$; en particular, tienen los mismos autovalores con las mismas
   multiplicidades algebraicas.
3. $\operatorname{tr}(A)=\operatorname{tr}(B)$.
4. $\operatorname{rango}(A)=\operatorname{rango}(B)$.
5. Para cada autovalor $\lambda$, $m_g(\lambda)$ es el mismo en $A$ y en $B$. Más precisamente, si
   $A=CBC^{-1}$ y $v$ es un autovector de $B$ con autovalor $\lambda$, entonces $Cv$ es un
   autovector de $A$ con el mismo autovalor.
6. $A^k=CB^kC^{-1}$ para todo $k\ge0$ (y para $k<0$ si son inversibles).
:::

**Demostración.** Sea $A=CBC^{-1}$.

1. $\det(A)=\det(C)\det(B)\det(C^{-1})=\det(B)$, porque $\det(C^{-1})=\det(C)^{-1}$.
2. Como $\lambda I=C(\lambda I)C^{-1}$,

   $$
   \lambda I-A=C(\lambda I)C^{-1}-CBC^{-1}=C(\lambda I-B)C^{-1},
   $$

   y por el punto 1 aplicado a $\lambda I-B$, $p_A(\lambda)=\det(\lambda I-A)=\det(\lambda I-B)=p_B(\lambda)$.
3. La traza es, salvo signo, el coeficiente de $\lambda^{n-1}$ del polinomio característico
   ([lección 3.2](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/)), y por el punto 2 ese
   coeficiente es el mismo.
4. Multiplicar por una matriz inversible (a izquierda o a derecha) no cambia el rango. Entonces
   $\operatorname{rango}(A)=\operatorname{rango}(CBC^{-1})=\operatorname{rango}(B)$.
5. Si $Bv=\lambda v$, entonces $A(Cv)=CBC^{-1}Cv=CBv=\lambda Cv$, y $Cv\neq0$ porque $C$ es
   inversible. La aplicación $v\mapsto Cv$ lleva $E_\lambda(B)$ en $E_\lambda(A)$, es inyectiva, y
   su inversa $w\mapsto C^{-1}w$ lleva $E_\lambda(A)$ en $E_\lambda(B)$ (misma cuenta con
   $B=C^{-1}AC$). Entonces $\dim E_\lambda(A)=\dim E_\lambda(B)$.
6. Por inducción: $A^{k+1}=A^kA=(CB^kC^{-1})(CBC^{-1})=CB^{k}(C^{-1}C)BC^{-1}=CB^{k+1}C^{-1}$.
   $\blacksquare$

Todo lo que **no** figura en la lista no es invariante. Las entradas de la matriz cambian, y
también los autovectores: el punto 5 dice que $Cv$ es autovector de $A$, pero $v$ en general no lo
es (ejemplo 1).

### Un contraejemplo: el recíproco es falso

Que dos matrices tengan el mismo polinomio característico (y, por lo tanto, la misma traza, el mismo
determinante y los mismos autovalores) **no** alcanza para que sean semejantes. Sean

$$
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad N=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
$$

Ambas tienen $p(\lambda)=(\lambda-1)^2$, determinante $1$, traza $2$ y rango $2$. Sin embargo **no
son semejantes**: para toda $C$ inversible, $CIC^{-1}=CC^{-1}=I\neq N$. La identidad solo es
semejante a sí misma. Desde los autoespacios, la diferencia es visible: $m_g(1)=2$ para $I$ (todo
vector es autovector) y $m_g(1)=1$ para $N$, porque $I-N=\begin{pmatrix}0&-1\\0&0\end{pmatrix}$ tiene
rango $1$. Como $m_g$ es invariante, no pueden ser semejantes.

El mismo razonamiento vale para cualquier matriz escalar $cI$: es la única de su clase de
semejanza. En cambio, si el polinomio característico tiene $n$ raíces reales **distintas**, dos matrices con ese
polinomio **sí** son semejantes: ambas son semejantes a la misma matriz diagonal (ejemplo 2(c) y
lección 3.5).

## Semejanza y cambio de base

Sea $T:\mathbb{R}^n\to\mathbb{R}^n$ un endomorfismo y sea $E$ la base canónica; $A=M(T)_E$ es su
matriz canónica. Para otra base ordenada $B=\{b_1,\dots,b_n\}$, la matriz $M(T)_B$ tiene por
columnas $[T(b_j)]_B$. Con la matriz $C=C_{BE}=(b_1\mid\cdots\mid b_n)$ de cambio de coordenadas
de $B$ a $E$ (sus columnas son las coordenadas canónicas de los $b_j$) y $C_{EB}=C^{-1}$, el
cambio de base de la matriz de $T$ (ver [cambio de base](/algebra-ii/unidad-2/teoria/cambio-de-base/))
es

$$
M(T)_B=C_{EB}\,M(T)_E\,C_{BE}=C^{-1}AC,\qquad\text{es decir,}\qquad A=C\,M(T)_B\,C^{-1}.
$$

Se lee de derecha a izquierda: una coordenada en $B$ se pasa a $E$ con $C$, se aplica $A$ y se
vuelve a $B$ con $C^{-1}$.

:::note[Teorema]
Dos matrices $A,B\in\mathbb{R}^{n\times n}$ son semejantes si y solo si son matrices de un mismo
endomorfismo de $\mathbb{R}^n$ respecto de dos bases.
:::

**Demostración.** ($\Leftarrow$) Por el cálculo anterior, $M(T)_{B_1}$ y $M(T)_{B_2}$ son semejantes a $M(T)_E$;
como la semejanza es simétrica y transitiva, son semejantes entre sí. ($\Rightarrow$) Si $A=CBC^{-1}$, sea
$T(x)=Ax$ y sea $B'$ la familia formada por las columnas de $C$; es una base porque $C$ es
inversible. Entonces $M(T)_E=A$ y, por el cálculo anterior, $M(T)_{B'}=C^{-1}AC=B$. $\blacksquare$

Esta es la razón por la cual los invariantes lo son: determinante, traza, autovalores y rango se
pueden definir directamente para el endomorfismo $T$, sin elegir ninguna base.

:::caution[Notación de los libros]
Poole y Lay escriben $P_{B'\leftarrow B}$ para lo que acá es $C_{BB'}$, y Poole escribe $[T]_{B'\leftarrow B}$ para
$M(T)_{BB'}$ (subíndices en orden inverso). Poole llama $P$ a la matriz que acá es $C$. La
equivalencia completa está en la página de [notación](/algebra-ii/notacion/).
:::

## Ejemplos resueltos

### Ejemplo 1 · Construir una matriz semejante y comparar invariantes

<!-- check: U3.T04.E1 -->

Sean $B=\begin{pmatrix}2&1\\0&3\end{pmatrix}$ y $C=\begin{pmatrix}1&1\\1&2\end{pmatrix}$. Calcular
$A=CBC^{-1}$ y verificar los invariantes.

**Inversa.** $\det(C)=2-1=1$, así que $C^{-1}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$.

**Producto.**

$$
CB=\begin{pmatrix}1&1\\1&2\end{pmatrix}\begin{pmatrix}2&1\\0&3\end{pmatrix}=\begin{pmatrix}2&4\\2&7\end{pmatrix},\qquad
A=CBC^{-1}=\begin{pmatrix}2&4\\2&7\end{pmatrix}\begin{pmatrix}2&-1\\-1&1\end{pmatrix}=\begin{pmatrix}0&2\\-3&5\end{pmatrix}.
$$

**Invariantes.** $\operatorname{tr}(A)=5=\operatorname{tr}(B)$, $\det(A)=0+6=6=\det(B)$ y
$p_A(\lambda)=\lambda^2-5\lambda+6=(\lambda-2)(\lambda-3)=p_B(\lambda)$. Ambas tienen rango $2$.

**Autovectores.** $B$ es triangular y $Be_1=2e_1$. Entonces $Ce_1=(1,1)$ debe ser autovector de
$A$ con autovalor $2$: $A(1,1)^t=(2,2)^t$. En cambio $e_1=(1,0)$ **no** es autovector de $A$:
$Ae_1=(0,-3)^t$.

:::tip[Resultado]
$A=\begin{pmatrix}0&2\\-3&5\end{pmatrix}$ tiene el mismo polinomio característico, traza,
determinante y rango que $B$; los autovectores de $A$ se obtienen multiplicando por $C$ los de $B$.
:::

### Ejemplo 2 · Decidir si dos matrices son semejantes

<!-- check: U3.T04.E2 -->

Decidir si son semejantes los pares: (a) $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ y
$\begin{pmatrix}2&1\\1&3\end{pmatrix}$; (b) $2I$ y $J=\begin{pmatrix}2&1\\0&2\end{pmatrix}$;
(c) $A_1=\begin{pmatrix}3&1\\0&2\end{pmatrix}$ y $B_1=\begin{pmatrix}2&0\\5&3\end{pmatrix}$.

**Estrategia.** Primero se comparan invariantes baratos; si alguno difiere, no son semejantes. Si
coinciden, se intenta construir $C$ o hallar un invariante más fino.

**(a)** Los determinantes son $4-6=-2$ y $6-1=5$: **no** son semejantes.

**(b)** Ambas tienen $p(\lambda)=(\lambda-2)^2$, pero $C(2I)C^{-1}=2I\neq J$ para toda $C$: **no** son
semejantes (misma situación que $I$ y $N$; $m_g(2)=2$ para $2I$ y $1$ para $J$).

**(c)** Ambas son triangulares con autovalores $3$ y $2$, distintos, de modo que son
diagonalizables y semejantes a $D=\operatorname{diag}(3,2)$. Hallamos los autovectores:

- $A_1$: para $3$, $(1,0)$; para $2$, de $A_1-2I=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, $(1,-1)$.
  Entonces $A_1=C_1DC_1^{-1}$ con $C_1=\begin{pmatrix}1&1\\0&-1\end{pmatrix}$.
- $B_1$: para $3$, de $B_1-3I=\begin{pmatrix}-1&0\\5&0\end{pmatrix}$, $(0,1)$; para $2$, de
  $B_1-2I=\begin{pmatrix}0&0\\5&1\end{pmatrix}$, $(1,-5)$. Entonces $B_1=C_2DC_2^{-1}$ con
  $C_2=\begin{pmatrix}0&1\\1&-5\end{pmatrix}$.

Despejando $D=C_2^{-1}B_1C_2$ y reemplazando, $A_1=(C_1C_2^{-1})\,B_1\,(C_1C_2^{-1})^{-1}$. Como
$C_2^{-1}=\begin{pmatrix}5&1\\1&0\end{pmatrix}$,

$$
C=C_1C_2^{-1}=\begin{pmatrix}1&1\\0&-1\end{pmatrix}\begin{pmatrix}5&1\\1&0\end{pmatrix}=\begin{pmatrix}6&1\\-1&0\end{pmatrix}.
$$

**Comprobación.** $A_1C=\begin{pmatrix}17&3\\-2&0\end{pmatrix}=CB_1$, y $\det(C)=1\neq0$.

:::tip[Resultado]
(a) no; (b) no; (c) sí, con $A_1=CB_1C^{-1}$ y $C=\begin{pmatrix}6&1\\-1&0\end{pmatrix}$. Dos matrices
diagonalizables son semejantes si y solo si tienen los mismos autovalores con las mismas
multiplicidades.
:::

### Ejemplo 3 · Un endomorfismo en tres matrices

<!-- check: U3.T04.E3 -->

Sea $T:\mathbb{R}^2\to\mathbb{R}^2$, $T(x,y)=(3x-y,\,2x)$. Hallar $M(T)_B$ para $B=\{(1,0),(1,1)\}$ y
$M(T)_{B'}$ para $B'=\{(1,1),(1,2)\}$.

La matriz canónica es $A=M(T)_E=\begin{pmatrix}3&-1\\2&0\end{pmatrix}$, con
$p_A(\lambda)=\lambda^2-3\lambda+2=(\lambda-1)(\lambda-2)$.

**Base $B$.** $C=C_{BE}=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ y $C^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}$.

$$
M(T)_B=C^{-1}AC=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}3&2\\2&2\end{pmatrix}=\begin{pmatrix}1&0\\2&2\end{pmatrix},
$$

donde $AC=\begin{pmatrix}3&2\\2&2\end{pmatrix}$. Directamente: $T(1,0)=(3,2)=1\cdot(1,0)+2\cdot(1,1)$ y
$T(1,1)=(2,2)=0\cdot(1,0)+2\cdot(1,1)$, que dan las columnas $(1,2)$ y $(0,2)$.

**Base $B'$.** $T(1,1)=(2,2)=2(1,1)$ y $T(1,2)=(1,2)=1\cdot(1,2)$. Los vectores de $B'$ son
autovectores y

$$
M(T)_{B'}=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
$$

**Comprobación.** Las tres matrices tienen traza $3$, determinante $2$ y polinomio
$\lambda^2-3\lambda+2$. La tercera es diagonal: encontramos una base en la que $T$ es lo más simple
posible.

:::tip[Resultado]
$M(T)_E=\begin{pmatrix}3&-1\\2&0\end{pmatrix}$, $M(T)_B=\begin{pmatrix}1&0\\2&2\end{pmatrix}$,
$M(T)_{B'}=\operatorname{diag}(2,1)$: semejantes entre sí.
:::

### Ejemplo 4 · Potencias vía semejanza

<!-- check: U3.T04.E4 -->

Calcular $A^k$ para $A=CBC^{-1}$ con $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ y
$C=\begin{pmatrix}1&1\\1&2\end{pmatrix}$.

**Potencias de $B$.** Por inducción, $B^k=\begin{pmatrix}1&k\\0&1\end{pmatrix}$: para $k=1$ es $B$ y
$B^{k+1}=B^kB=\begin{pmatrix}1&k\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}1&k+1\\0&1\end{pmatrix}$.

**Matriz $A$.** Con $C^{-1}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$:
$CB=\begin{pmatrix}1&2\\1&3\end{pmatrix}$ y $A=CBC^{-1}=\begin{pmatrix}0&1\\-1&2\end{pmatrix}$.

**Potencias de $A$.** Como $A^k=CB^kC^{-1}$,

$$
A^k=\begin{pmatrix}1&1+k\\1&2+k\end{pmatrix}\begin{pmatrix}2&-1\\-1&1\end{pmatrix}
=\begin{pmatrix}1-k&k\\-k&1+k\end{pmatrix}.
$$

**Comprobación.** Para $k=1$ da $A$; para $k=2$, $A^2=\begin{pmatrix}-1&2\\-2&3\end{pmatrix}$, que
coincide con el producto directo $A\cdot A=\begin{pmatrix}0&1\\-1&2\end{pmatrix}\begin{pmatrix}0&1\\-1&2\end{pmatrix}=\begin{pmatrix}-1&2\\-2&3\end{pmatrix}$.

:::tip[Resultado]
$A^k=\begin{pmatrix}1-k&k\\-k&1+k\end{pmatrix}$. Aunque $A$ no es diagonalizable (su único autovalor
es $1$ y no es la identidad), la semejanza con una matriz de potencias conocidas alcanza.
:::

### Ejemplo 5 · Mismo polinomio, no semejantes

<!-- check: U3.T04.E5 -->

Verificar con una cuenta explícita que $I$ y $N=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ no son
semejantes. Si $C=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ satisface $IC=CN$, entonces
$\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}a&a+b\\c&c+d\end{pmatrix}$, es decir $a=0$ y
$c=0$, y $C$ tiene una columna nula: no es inversible. Por lo tanto ninguna $C$ inversible
cumple $I=CNC^{-1}$.

:::caution[Errores frecuentes]
- **Pensar que mismo polinomio característico implica semejanza.** Falla con $I$ y $N$. Se
  necesita además, por ejemplo, la misma $m_g$ para cada autovalor (y, si hay autovalores
  repetidos, más datos de los que trata este curso).
- **Confundir semejanza con equivalencia por filas.** Escalonar $A$ da una matriz con otros
  autovalores; la semejanza $CBC^{-1}$ multiplica por $C$ y por su **inversa**, a lados opuestos.
- **Invertir el papel de $C$ y $C^{-1}$.** Si las columnas de $C$ son la base nueva escrita en la
  canónica, la matriz de $T$ en la base nueva es $C^{-1}AC$ y no $CAC^{-1}$.
- **Decir que dos matrices semejantes tienen los mismos autovectores.** Tienen los mismos
  autovalores; los autovectores se corresponden por $v\mapsto Cv$.
- **Creer que la semejanza conserva entradas, simetría o ceros.** $B$ es triangular y $A$ no
  (ejemplo 1).
- **Concluir "no semejantes" por tener distintas entradas.** Solo los invariantes sirven para
  descartar.
:::

## Autoevaluación

<details>
<summary>1. A y B son semejantes y det(A) = 6. ¿Cuánto vale det(B²)?</summary>

$\det(B)=\det(A)=6$, así que $\det(B^2)=36$.

</details>

<details>
<summary>2. ¿Puede una matriz inversible ser semejante a una no inversible?</summary>

No: el determinante es invariante, así que ambas tienen $\det\neq0$ o ambas $\det=0$.

</details>

<details>
<summary>3. Si A = CBC⁻¹ y B es diagonal, ¿cómo son las columnas de C?</summary>

Son autovectores de $A$: de $AC=CB$, la columna $j$ cumple $Ac_j=b_{jj}c_j$. Es la idea de la
diagonalización.

</details>

:::tip[En resumen]
- $A$ es semejante a $B$ si $A=CBC^{-1}$ con $C$ inversible; es una relación de equivalencia.
- Invariantes: determinante, polinomio característico, autovalores con $m_a$ y $m_g$, traza y rango.
  Las entradas y los autovectores **no** lo son.
- Matrices semejantes son matrices de un mismo endomorfismo en bases distintas:
  $M(T)_B=C^{-1}\,M(T)_E\,C$ con $C=C_{BE}$.
- Mismo polinomio característico no implica semejanza ($I$ y $N$).
- $A^k=CB^kC^{-1}$: una semejanza con una matriz de potencias fáciles simplifica los cálculos.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 4.4, Semejanza y
  diagonalización (p. 312).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: sección sobre semejanza y diagonalización.
- Anterior: [3.3 Propiedades](/algebra-ii/unidad-3/teoria/propiedades/). Siguiente:
  [3.5 Diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/). Relacionado:
  [cambio de base de la matriz de una TL](/algebra-ii/unidad-2/teoria/cambio-de-base/).
