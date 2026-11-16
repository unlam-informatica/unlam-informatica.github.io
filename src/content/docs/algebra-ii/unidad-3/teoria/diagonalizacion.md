---
title: Diagonalización
description: Matrices diagonalizables, criterio de la base de autovectores y de las multiplicidades, procedimiento completo, ejemplos con autovalor doble, sin diagonalización y con parámetro, y matrices simétricas 2×2.
slug: algebra-ii/unidad-3/teoria/diagonalizacion
sidebar:
  order: 5
  label: 3.5 Diagonalización
---

## Para qué sirve

Una matriz diagonal es la más simple de manejar: sus potencias son las potencias de las entradas,
su determinante es el producto de la diagonal y el sistema $Dx=b$ se resuelve ecuación por
ecuación. Diagonalizar $A$ es **encontrar una base en la que $A$ se vea diagonal**. Si lo
logramos, un problema acoplado de $n$ variables se descompone en $n$ problemas de una variable, y
cuentas que parecen imposibles ($A^{1000}$, el comportamiento de una recurrencia, el estado a
largo plazo de una cadena de Markov) pasan a ser directas.

No toda matriz se puede diagonalizar. Esta lección da un criterio exacto para decidirlo, un
procedimiento para hacerlo y ejemplos de cada situación.

## Definición y primer criterio

:::note[Definición]
Una matriz $A\in\mathbb{R}^{n\times n}$ es **diagonalizable** (sobre $\mathbb{R}$) si es semejante
a una matriz diagonal: existen $C\in\mathbb{R}^{n\times n}$ inversible y
$D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ tales que

$$
A=CDC^{-1}.
$$
:::

:::note[Teorema]
$A\in\mathbb{R}^{n\times n}$ es diagonalizable si y solo si existe una **base de $\mathbb{R}^n$
formada por autovectores de $A$**. En ese caso, si $v_1,\dots,v_n$ es tal base con
$Av_j=\lambda_jv_j$, entonces $A=CDC^{-1}$ con

$$
C=(v_1\mid v_2\mid\cdots\mid v_n),\qquad D=\operatorname{diag}(\lambda_1,\lambda_2,\dots,\lambda_n).
$$
:::

**Demostración.** ($\Leftarrow$) Sean $v_1,\dots,v_n$ una base de autovectores, con
$Av_j=\lambda_jv_j$, y $C=(v_1\mid\cdots\mid v_n)$. Las columnas de $AC$ son $Av_j=\lambda_jv_j$, y
las de $CD$ también: la columna $j$ de $CD$ es $C(\lambda_je_j)=\lambda_jv_j$. Entonces $AC=CD$.
Como las columnas de $C$ son una base, $C$ es inversible, y $A=CDC^{-1}$.

($\Rightarrow$) Si $A=CDC^{-1}$ con $D$ diagonal, entonces $AC=CD$. Mirando la columna $j$ de ambos
miembros, $Ac_j=d_{jj}c_j$, donde $c_j$ es la columna $j$ de $C$. Como $C$ es inversible, sus
columnas son una base de $\mathbb{R}^n$, y ninguna es nula: son autovectores de $A$. $\blacksquare$

La demostración muestra además **cómo se arma $C$ y $D$**: las columnas de $C$ son autovectores y la
entrada $d_{jj}$ es el autovalor del autovector $j$-ésimo. Cualquier cambio del orden de las
columnas de $C$ obliga a cambiar el mismo orden en $D$.

### Visión como cambio de base

Sea $B=\{v_1,\dots,v_n\}$ la base de autovectores. La matriz $C=C_{BE}$ pasa coordenadas de $B$ a
la canónica y $C^{-1}=C_{EB}$ hace lo contrario; $D=M(T)_B$ es la matriz de $T(x)=Ax$ en la base
$B$ (ver [matrices semejantes](/algebra-ii/unidad-3/teoria/matrices-semejantes/)). El siguiente
diagrama resume $A=CDC^{-1}$: ir "por arriba" con $A$ equivale a bajar con $C^{-1}$, multiplicar
por $D$ y subir con $C$.

```mermaid
flowchart LR
  X["x en la base canónica E"] -->|"A"| AX["Ax en la base canónica E"]
  X -->|"C⁻¹ (pasar a B)"| Y["[x] en la base B de autovectores"]
  Y -->|"D (cada coordenada se multiplica por su λ)"| DY["[Ax] en la base B"]
  DY -->|"C (volver a E)"| AX
```

En la base $B$ la transformación solo **estira cada coordenada** por el autovalor correspondiente.
Con el [laboratorio](/algebra-ii/laboratorio/) se pueden ver las dos direcciones invariantes de una
matriz $2\times2$ diagonalizable y cómo la grilla se estira a lo largo de ellas.

## Cuándo es diagonalizable

### Autovalores distintos

:::note[Propiedad]
Si $A\in\mathbb{R}^{n\times n}$ tiene $n$ autovalores reales **distintos**, entonces es
diagonalizable.
:::

**Demostración.** Por el [teorema de independencia](/algebra-ii/unidad-3/teoria/propiedades/), $n$
autovectores de autovalores distintos son linealmente independientes, y $n$ vectores independientes
de $\mathbb{R}^n$ son una base. $\blacksquare$

La **recíproca es falsa**: la matriz identidad $I_n$ es diagonalizable (ya es diagonal) y tiene un
solo autovalor, $1$, con $m_a=n$. El ejemplo 2 de esta lección también tiene un autovalor doble y
es diagonalizable.

### El criterio de las multiplicidades

Para el caso general necesitamos un lema.

:::note[Lema]
Si $\lambda_1,\dots,\lambda_r$ son autovalores distintos de $A$ y, para cada $i$, $\mathcal B_i$ es
una base de $E_{\lambda_i}(A)$, entonces la unión $\mathcal B_1\cup\cdots\cup\mathcal B_r$ es
linealmente independiente.
:::

**Demostración.** Una combinación lineal nula de la unión se agrupa como $w_1+\dots+w_r=0$, con
$w_i\in E_{\lambda_i}(A)$ la combinación de los vectores de $\mathcal B_i$. Si algún $w_i$ fuera no
nulo, los $w_i$ no nulos serían autovectores de autovalores distintos y su suma no podría ser $0$,
porque son linealmente independientes. Entonces todos los $w_i$ son nulos, y como cada $\mathcal B_i$
es independiente, todos los coeficientes son nulos. $\blacksquare$

:::note[Teorema (criterio de diagonalización)]
Sea $A\in\mathbb{R}^{n\times n}$. Son equivalentes:

1. $A$ es diagonalizable.
2. $p_A$ se factoriza en $\mathbb{R}$ en factores lineales, y $m_g(\lambda)=m_a(\lambda)$ para cada
   autovalor $\lambda$.
3. La suma de las dimensiones de los autoespacios es $n$: $\sum_\lambda m_g(\lambda)=n$.
:::

**Demostración.** Sean $\lambda_1,\dots,\lambda_r$ los autovalores reales distintos de $A$. Como
$p_A$ tiene grado $n$, $\sum m_a(\lambda_i)\le n$, con igualdad si y solo si $p_A$ se factoriza en
$\mathbb{R}$. Además, $1\le m_g(\lambda_i)\le m_a(\lambda_i)$.

(1 $\Rightarrow$ 3) Si hay una base de autovectores, cada uno está en algún $E_{\lambda_i}(A)$; los
que caen en un mismo autoespacio son independientes, así que hay a lo sumo $m_g(\lambda_i)$ de ellos
en $E_{\lambda_i}(A)$. Entonces $n\le\sum m_g(\lambda_i)$. Por el lema, la unión de bases de los
autoespacios es un conjunto independiente de $\mathbb{R}^n$, de modo que $\sum m_g(\lambda_i)\le n$.
Luego, $\sum m_g(\lambda_i)=n$.

(3 $\Rightarrow$ 2) Si $\sum m_g=n$, entonces $n=\sum m_g\le\sum m_a\le n$: todas las desigualdades
son igualdades. Por eso $\sum m_a=n$ ($p_A$ se factoriza en $\mathbb{R}$) y, como $m_g\le m_a$ en
cada término, $m_g(\lambda_i)=m_a(\lambda_i)$ para todo $i$.

(2 $\Rightarrow$ 1) Si $p_A$ se factoriza y $m_g=m_a$, entonces $\sum m_g=\sum m_a=n$. Por el
lema, la unión de bases de los autoespacios tiene $n$ vectores independientes, es decir, una base
de $\mathbb{R}^n$ formada por autovectores. Por el teorema anterior, $A$ es diagonalizable.
$\blacksquare$

En la práctica el criterio se aplica así: los autovalores simples ($m_a=1$) no hay que
controlarlos, porque $m_g=m_a=1$ automáticamente; solo hay que calcular $m_g$ para los
autovalores **repetidos**, con
$m_g(\lambda)=n-\operatorname{rango}(\lambda I-A)$. Y si $p_A$ tiene raíces complejas no reales, $A$
**no** es diagonalizable sobre $\mathbb{R}$ (aunque lo pueda ser sobre $\mathbb{C}$).

## Procedimiento

Para decidir si $A\in\mathbb{R}^{n\times n}$ es diagonalizable y, si lo es, hallar $C$ y $D$:

1. Calcular $p_A(\lambda)=\det(\lambda I-A)$ y factorizarlo. Si tiene raíces no reales, $A$ no es
   diagonalizable sobre $\mathbb{R}$. Anotar $m_a(\lambda_i)$.
2. Para cada autovalor **repetido**, calcular $m_g(\lambda_i)=n-\operatorname{rango}(\lambda_iI-A)$.
   Si algún $m_g(\lambda_i)<m_a(\lambda_i)$, $A$ no es diagonalizable.
3. Si todo coincide, obtener una base de cada autoespacio resolviendo $(\lambda_iI-A)x=0$.
4. Armar $C$ con esos autovectores como columnas, en el orden que se quiera, y $D$ con los
   autovalores correspondientes **en el mismo orden**.
5. Verificar $AC=CD$ (evita calcular $C^{-1}$) o, si se necesita $C^{-1}$, verificar
   $C^{-1}AC=D$.

**Observaciones.** (a) El orden de las columnas de $C$ es libre, y cada orden da una $D$ distinta
(los autovalores en el orden correspondiente). (b) $C$ **no es única**: cada autovector puede
reemplazarse por cualquier múltiplo no nulo y, en un autoespacio de dimensión mayor que $1$, por
cualquier otra base de ese autoespacio. En cambio, $D$ queda determinada salvo el orden. (c) Para
verificar, $AC=CD$ es más barato y menos propenso a errores que invertir $C$.

## Ejemplos resueltos

### Ejemplo 1 · Una matriz 2×2 y las libertades en la elección de $C$

<!-- check: U3.T05.E1 -->

Diagonalizar $A=\begin{pmatrix}4&-2\\1&1\end{pmatrix}$.

**Polinomio.** $\operatorname{tr}(A)=5$ y $\det(A)=4+2=6$, entonces
$p_A(\lambda)=\lambda^2-5\lambda+6=(\lambda-2)(\lambda-3)$. Hay dos autovalores distintos: $A$ es
diagonalizable por la propiedad anterior.

**Autoespacios.**

- $\lambda=2$: $2I-A=\begin{pmatrix}-2&2\\-1&1\end{pmatrix}$ da $x=y$: $E_2(A)=\operatorname{gen}\{(1,1)\}$.
- $\lambda=3$: $3I-A=\begin{pmatrix}-1&2\\-1&2\end{pmatrix}$ da $x=2y$: $E_3(A)=\operatorname{gen}\{(2,1)\}$.

**Factorización.** Con $v_1=(1,1)$ y $v_2=(2,1)$,

$$
C=\begin{pmatrix}1&2\\1&1\end{pmatrix},\qquad D=\begin{pmatrix}2&0\\0&3\end{pmatrix},\qquad
C^{-1}=\begin{pmatrix}-1&2\\1&-1\end{pmatrix}.
$$

**Comprobación.** $AC=\begin{pmatrix}2&6\\2&3\end{pmatrix}=CD$, y por lo tanto
$A=CDC^{-1}$.

**Otras elecciones válidas.**

- *Otro orden.* Con $C'=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ (columnas $v_2,v_1$) corresponde
  $D'=\operatorname{diag}(3,2)$.
- *Otros múltiplos.* Con $C''=\begin{pmatrix}-3&4\\-3&2\end{pmatrix}$, cuyas columnas son
  $-3v_1$ y $2v_2$, se tiene de nuevo $C''^{-1}AC''=\operatorname{diag}(2,3)$.

:::tip[Resultado]
$A=CDC^{-1}$ con $C=\begin{pmatrix}1&2\\1&1\end{pmatrix}$ y $D=\operatorname{diag}(2,3)$. $C$ no es
única; los autovalores en $D$ sí, salvo el orden.
:::

### Ejemplo 2 · Una 3×3 con autovalor doble diagonalizable

<!-- check: U3.T05.E2 -->

Decidir si $A=\begin{pmatrix}2&0&1\\1&1&1\\2&0&3\end{pmatrix}$ es diagonalizable y, de serlo,
diagonalizarla.

**Polinomio.** La segunda columna de $\lambda I-A$ es $(0,\lambda-1,0)^t$; desarrollamos por ella:

$$
p_A(\lambda)=(\lambda-1)\det\begin{pmatrix}\lambda-2&-1\\-2&\lambda-3\end{pmatrix}
=(\lambda-1)\big[(\lambda-2)(\lambda-3)-2\big]=(\lambda-1)(\lambda^2-5\lambda+4)=(\lambda-1)^2(\lambda-4).
$$

Entonces $m_a(1)=2$ y $m_a(4)=1$. Solo hay que calcular $m_g(1)$.

**Autoespacio de $1$.**

$$
I-A=\begin{pmatrix}-1&0&-1\\-1&0&-1\\-2&0&-2\end{pmatrix}\sim\begin{pmatrix}1&0&1\\0&0&0\\0&0&0\end{pmatrix}.
$$

El rango es $1$, así que $m_g(1)=3-1=2=m_a(1)$: **es diagonalizable**. Las soluciones cumplen
$x=-z$ con $y$ y $z$ libres: $E_1(A)=\operatorname{gen}\{(0,1,0),(1,0,-1)\}$.

**Autoespacio de $4$.** $4I-A=\begin{pmatrix}2&0&-1\\-1&3&-1\\-2&0&1\end{pmatrix}\sim
\begin{pmatrix}2&0&-1\\0&3&-\tfrac32\\0&0&0\end{pmatrix}$ da $z=2x$, $y=\tfrac12 z=x$, de donde
$E_4(A)=\operatorname{gen}\{(1,1,2)\}$.

**Factorización.** Con los autovectores en el orden $(0,1,0)$, $(1,0,-1)$, $(1,1,2)$:

$$
C=\begin{pmatrix}0&1&1\\1&0&1\\0&-1&2\end{pmatrix},\qquad D=\begin{pmatrix}1&0&0\\0&1&0\\0&0&4\end{pmatrix}.
$$

**Comprobación.** $\det(C)=-3\neq0$ y $AC=\begin{pmatrix}0&1&4\\1&0&4\\0&-1&8\end{pmatrix}=CD$: las
columnas de $AC$ son $Av_1=v_1$, $Av_2=v_2$ y $Av_3=4v_3$.

:::tip[Resultado]
$A$ es diagonalizable: $C^{-1}AC=\operatorname{diag}(1,1,4)$. Tener un autovalor repetido no impide
diagonalizar; lo que importa es que $m_g=m_a$.
:::

### Ejemplo 3 · Una 3×3 que no es diagonalizable

<!-- check: U3.T05.E3 -->

Decidir si $A=\begin{pmatrix}0&-1&1\\3&1&-3\\2&-1&-1\end{pmatrix}$ es diagonalizable.

**Polinomio.** Se tiene $\operatorname{tr}(A)=0$, $\det(A)=-2$ y la suma de los menores principales de
orden $2$ es $-3$; el desarrollo de $\det(\lambda I-A)$ da
$p_A(\lambda)=\lambda^3-3\lambda+2$. Como $p_A(1)=0$, por Ruffini
$p_A(\lambda)=(\lambda-1)(\lambda^2+\lambda-2)=(\lambda-1)^2(\lambda+2)$:
$m_a(1)=2$ y $m_a(-2)=1$.

**Autoespacio de $1$.**

$$
I-A=\begin{pmatrix}1&1&-1\\-3&0&3\\-2&1&2\end{pmatrix}\sim\begin{pmatrix}1&1&-1\\0&3&0\\0&0&0\end{pmatrix}.
$$

El rango es $2$, entonces $m_g(1)=1<2=m_a(1)$. Por el criterio, **$A$ no es diagonalizable**.

**Comprobación de los autoespacios.** De $I-A$: $y=0$ y $x=z$, $E_1(A)=\operatorname{gen}\{(1,0,1)\}$; y
$E_{-2}(A)=\operatorname{gen}\{(0,1,1)\}$. Con $A(1,0,1)^t=(1,0,1)^t$ y
$A(0,1,1)^t=(0,-2,-2)^t=-2(0,1,1)^t$ solo hay **dos** direcciones de autovectores independientes en
$\mathbb{R}^3$: no alcanza para una base.

:::tip[Resultado]
$A$ no es diagonalizable: $m_g(1)=1<m_a(1)=2$. No existe $C$ inversible con $C^{-1}AC$ diagonal.
:::

### Ejemplo 4 · Diagonalizabilidad según un parámetro

<!-- check: U3.T05.E4 -->

Determinar para qué valores de $k\in\mathbb{R}$ es diagonalizable
$A_k=\begin{pmatrix}2&1&0\\0&k&0\\1&-1&3\end{pmatrix}$.

**Polinomio.** Desarrollamos por la segunda fila, que tiene una sola entrada no nula:

$$
p_{A_k}(\lambda)=(\lambda-k)\det\begin{pmatrix}\lambda-2&0\\-1&\lambda-3\end{pmatrix}=(\lambda-k)(\lambda-2)(\lambda-3).
$$

Los autovalores son $2$, $3$ y $k$.

**Caso $k\neq2$ y $k\neq3$.** Hay tres autovalores distintos: es diagonalizable.

**Caso $k=2$.** El autovalor $2$ tiene $m_a=2$. Calculamos

$$
2I-A_2=\begin{pmatrix}0&-1&0\\0&0&0\\-1&1&-1\end{pmatrix},
$$

de rango $2$, así que $m_g(2)=1<2$: **no es diagonalizable**.

**Caso $k=3$.** El autovalor $3$ tiene $m_a=2$ y

$$
3I-A_3=\begin{pmatrix}1&-1&0\\0&0&0\\-1&1&0\end{pmatrix}
$$

tiene rango $1$: $m_g(3)=2=m_a(3)$ y **es diagonalizable**. Por ejemplo,
$E_3(A_3)=\operatorname{gen}\{(1,1,0),(0,0,1)\}$.

**Comprobación.** Para $k=3$, $A_3(1,1,0)^t=(3,3,0)^t$ y $A_3(0,0,1)^t=(0,0,3)^t$.

:::tip[Resultado]
$A_k$ es diagonalizable si y solo si $k\neq2$. (Con $k=3$ lo es aunque el autovalor se repita.)
:::

### Ejemplo 5 · Matrices simétricas $2\times2$

<!-- check: U3.T05.E5 -->

Probar que toda matriz simétrica $S=\begin{pmatrix}a&b\\b&c\end{pmatrix}$ real es diagonalizable
sobre $\mathbb{R}$, y diagonalizar $N=\begin{pmatrix}1&2\\2&-2\end{pmatrix}$.

**Discriminante.** $p_S(\lambda)=\lambda^2-(a+c)\lambda+(ac-b^2)$, y su discriminante es

$$
(a+c)^2-4(ac-b^2)=(a-c)^2+4b^2\ \ge0 .
$$

- Si $(a-c)^2+4b^2>0$, hay dos autovalores reales distintos: $S$ es diagonalizable.
- Si es $0$, entonces $a=c$ y $b=0$, y $S=aI$ ya es diagonal.

En ambos casos, $S$ es diagonalizable. (En $3\times3$ y más, vale para toda simétrica real; es un
resultado general (teorema espectral) que queda fuera de este curso.)

**Caso $N$.** $p_N(\lambda)=\lambda^2+\lambda-6=(\lambda-2)(\lambda+3)$, con autovalores $2$ y $-3$.
De $2I-N=\begin{pmatrix}1&-2\\-2&4\end{pmatrix}$, $E_2(N)=\operatorname{gen}\{(2,1)\}$; de
$-3I-N=\begin{pmatrix}-4&-2\\-2&-1\end{pmatrix}$, $E_{-3}(N)=\operatorname{gen}\{(1,-2)\}$. Entonces

$$
C=\begin{pmatrix}2&1\\1&-2\end{pmatrix},\qquad C^{-1}NC=\begin{pmatrix}2&0\\0&-3\end{pmatrix}.
$$

**Comprobación.** $NC=\begin{pmatrix}4&-3\\2&6\end{pmatrix}=CD$. Además, los dos autovectores son
perpendiculares: $(2,1)\cdot(1,-2)=0$, algo que ocurre siempre en las simétricas con autovalores
distintos.

:::tip[Resultado]
Toda simétrica real $2\times2$ es diagonalizable; $N=CDC^{-1}$ con $D=\operatorname{diag}(2,-3)$.
:::

:::caution[Errores frecuentes]
- **Creer que autovalor repetido implica no diagonalizable.** El ejemplo 2 lo desmiente: hay que
  comparar $m_g$ con $m_a$.
- **Creer que autovalores distintos son necesarios.** Los distintos son suficientes, no
  necesarios ($I_n$).
- **Armar $D$ en otro orden que $C$.** Si las columnas de $C$ son $v_2,v_1$, entonces
  $D=\operatorname{diag}(\lambda_2,\lambda_1)$.
- **Completar $C$ repitiendo un autovector (o un múltiplo) cuando faltan columnas.** $C$ debe ser
  inversible, $\det(C)\neq0$; si faltan autovectores independientes, $A$ no es diagonalizable.
- **Calcular $m_g$ con el rango de $A$ en lugar del de $\lambda I-A$.**
- **Declarar "no diagonalizable" por tener raíces complejas sin aclarar el cuerpo.** Sobre
  $\mathbb{R}$ lo es; sobre $\mathbb{C}$ una matriz como la rotación de $90^\circ$ sí es
  diagonalizable (queda fuera de este curso).
- **Confundir diagonalizable con inversible.** $\operatorname{diag}(1,0)$ es diagonalizable y
  singular; $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ es inversible y no diagonalizable.
- **Reutilizar $C$ de una matriz para otra.** Dos matrices con los mismos autovalores pero distintos
  autovectores necesitan matrices $C$ distintas.
:::

## Autoevaluación

<details>
<summary>1. Una matriz 3 × 3 tiene polinomio característico (λ − 2)²(λ + 1) y rango(2I − A) = 1. ¿Es diagonalizable?</summary>

$m_g(2)=3-1=2=m_a(2)$ y $m_a(-1)=m_g(-1)=1$: sí, es diagonalizable.

</details>

<details>
<summary>2. ¿Es diagonalizable una matriz triangular con todos los elementos de la diagonal distintos?</summary>

Sí: sus autovalores son las entradas de la diagonal, $n$ autovalores distintos.

</details>

<details>
<summary>3. ¿Es diagonalizable [[3, 1], [0, 3]]?</summary>

No: $m_a(3)=2$ y $3I-A=\begin{pmatrix}0&-1\\0&0\end{pmatrix}$ tiene rango $1$, así que $m_g(3)=1$.

</details>

:::tip[En resumen]
- $A$ es diagonalizable si y solo si existe una base de $\mathbb{R}^n$ de autovectores; entonces
  $A=CDC^{-1}$ con los autovectores como columnas de $C$ y los autovalores correspondientes en $D$.
- $n$ autovalores reales distintos garantizan la diagonalización (la recíproca es falsa).
- Criterio general: $p_A$ se factoriza en $\mathbb{R}$ y $m_g=m_a$ para cada autovalor; solo hay que
  verificar los autovalores repetidos.
- $C$ no es única (orden y múltiplos); $D$ es única salvo el orden.
- Toda simétrica real $2\times2$ es diagonalizable (discriminante $(a-c)^2+4b^2\ge0$).
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 4.4, Semejanza y
  diagonalización (p. 312).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: sección de diagonalización.
- Anterior: [3.4 Matrices semejantes](/algebra-ii/unidad-3/teoria/matrices-semejantes/).
  Siguiente: [3.6 Potencias de una matriz](/algebra-ii/unidad-3/teoria/potencias/). Interactivo:
  [laboratorio](/algebra-ii/laboratorio/).
