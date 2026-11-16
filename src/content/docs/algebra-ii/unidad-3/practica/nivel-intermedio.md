---
title: Práctica — Nivel intermedio
description: Diez ejercicios intermedios de diagonalización, semejanza, potencias, recurrencias lineales y cadenas de Markov, con resolución completa.
slug: algebra-ii/unidad-3/practica/nivel-intermedio
sidebar:
  order: 2
  label: Nivel intermedio
---

:::note[Cómo usar esta página]
Ejercicios **originales** que combinan varias ideas: diagonalizar, justificar afirmaciones, calcular potencias y
modelar situaciones de informática. Intentá primero plantear la estrategia en una línea y recién después
calcular. Los ejercicios numerados continúan los del [nivel inicial](/algebra-ii/unidad-3/practica/nivel-inicial/).

**Presupone:** [3.3 Propiedades](/algebra-ii/unidad-3/teoria/propiedades/),
[3.4 Matrices semejantes](/algebra-ii/unidad-3/teoria/matrices-semejantes/),
[3.5 Diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/),
[3.6 Potencias](/algebra-ii/unidad-3/teoria/potencias/),
[3.7 Relaciones de recurrencia](/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/) y
[3.8 Cadenas de Markov](/algebra-ii/unidad-3/teoria/cadenas-de-markov/).
Convención: $A=CDC^{-1}$ con los autovectores en las columnas de $C$; las matrices de transición son
estocásticas por columnas ($x_{k+1}=Px_k$).

Siguiente: [nivel avanzado](/algebra-ii/unidad-3/practica/nivel-avanzado/).
:::

### Ejercicio 9 · Diagonalizar con tres autovalores distintos
<!-- ejercicio: U3.09 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}2&-1&1\\5&-4&1\\5&-5&2\end{pmatrix}$. Hallar $C$ inversible y $D$ diagonal tales que $A=CDC^{-1}$ y verificar que $AC=CD$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Polinomio característico, raíces por Ruffini, un autovector por cada autovalor. Tres autovalores distintos aseguran tres autovectores independientes.

$\operatorname{tr}(A)=0$ y desarrollando el determinante, $p_A(\lambda)=\lambda^3-7\lambda+6$. Como $p_A(1)=0$, Ruffini da $p_A=(\lambda-1)(\lambda^2+\lambda-6)=(\lambda-1)(\lambda-2)(\lambda+3)$.

- $\lambda=1$: $I-A=\begin{pmatrix}-1&1&-1\\-5&5&-1\\-5&5&-1\end{pmatrix}$. Restando $5$ veces la primera fila a la segunda: $4z=0$, y $x=y$. $E_1=\operatorname{gen}\{(1,1,0)\}$.
- $\lambda=2$: $2I-A=\begin{pmatrix}0&1&-1\\-5&6&-1\\-5&5&0\end{pmatrix}$ da $y=z$, $x=y$. $E_2=\operatorname{gen}\{(1,1,1)\}$.
- $\lambda=-3$: $-3I-A=\begin{pmatrix}-5&1&-1\\-5&1&-1\\-5&5&-5\end{pmatrix}$ da $y=z$ y $x=0$. $E_{-3}=\operatorname{gen}\{(0,1,1)\}$.

Entonces
$$
C=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix},\qquad D=\begin{pmatrix}1&0&0\\0&2&0\\0&0&-3\end{pmatrix}.
$$

**Comprobación.** $AC$ tiene por columnas $A(1,1,0)=(1,1,0)$, $A(1,1,1)=(2,2,2)$ y $A(0,1,1)=(0,-3,-3)$; son las columnas de $CD$ ($1\cdot c_1$, $2\cdot c_2$, $-3\cdot c_3$). Además $\det C=-1\neq0$.

:::tip[Resultado]
$A=CDC^{-1}$ con $C=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}$ y $D=\operatorname{diag}(1,2,-3)$.
:::

</details>

### Ejercicio 10 · Autovalor doble que sí diagonaliza
<!-- ejercicio: U3.10 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}5&-3&3\\3&-1&3\\3&-3&5\end{pmatrix}$.

a) Hallar autovalores, $m_a$ y $m_g$.

b) Si es posible, diagonalizar $A$ y comprobar con $AC=CD$.
:::

<details>
<summary>Resolución</summary>

**a)** $p_A(\lambda)=\lambda^3-9\lambda^2+24\lambda-20=(\lambda-2)^2(\lambda-5)$ (la traza es $9=2+2+5$ y $\det A=20$). Entonces $m_a(2)=2$, $m_a(5)=1$.

$2I-A=\begin{pmatrix}-3&3&-3\\-3&3&-3\\-3&3&-3\end{pmatrix}$ tiene rango $1$: $E_2=\{x-y+z=0\}$, con base $\{(1,1,0),(0,1,1)\}$, y $m_g(2)=2$.

$5I-A=\begin{pmatrix}0&3&-3\\-3&6&-3\\-3&3&0\end{pmatrix}$ da $y=z$, $x=y$: $E_5=\operatorname{gen}\{(1,1,1)\}$, $m_g(5)=1$.

**b)** Como $m_g=m_a$ para cada autovalor, $A$ es diagonalizable. Con
$$
C=\begin{pmatrix}1&0&1\\1&1&1\\0&1&1\end{pmatrix},\qquad D=\operatorname{diag}(2,2,5):
$$

**Comprobación.** $A(1,1,0)=(2,2,0)$, $A(0,1,1)=(0,2,2)$, $A(1,1,1)=(5,5,5)$: son $2c_1$, $2c_2$ y $5c_3$, o sea $AC=CD$. Y $\det C=1\neq0$.

:::tip[Resultado]
$m_a(2)=m_g(2)=2$, $m_a(5)=m_g(5)=1$; $A=CDC^{-1}$ con $D=\operatorname{diag}(2,2,5)$.
:::

</details>

### Ejercicio 11 · Diagonalizabilidad según un parámetro
<!-- ejercicio: U3.11 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A_a=\begin{pmatrix}2&0&0\\a&2&0\\1&1&5\end{pmatrix}$ con $a\in\mathbb{R}$.

a) Hallar los autovalores y sus multiplicidades algebraicas.

b) Determinar para qué valores de $a$ la matriz $A_a$ es diagonalizable.

c) Para $a=0$, hallar $C$ y $D$ con $A_0=CDC^{-1}$.
:::

<details>
<summary>Resolución</summary>

**a)** $A_a$ es triangular inferior: $p_{A_a}(\lambda)=(\lambda-2)^2(\lambda-5)$ para todo $a$. $m_a(2)=2$, $m_a(5)=1$.

**b)** El autovalor simple $5$ siempre tiene $m_g=1$. Todo depende de $m_g(2)=3-\operatorname{rango}(2I-A_a)$:
$$
2I-A_a=\begin{pmatrix}0&0&0\\-a&0&0\\-1&-1&-3\end{pmatrix}.
$$
Si $a\neq0$, las filas $(-a,0,0)$ y $(-1,-1,-3)$ son independientes: rango $2$, $m_g(2)=1<2$ y $A_a$ **no** es diagonalizable. Si $a=0$, el rango es $1$ y $m_g(2)=2=m_a(2)$: es diagonalizable.

**c)** Para $a=0$: $E_2=\{x+y+3z=0\}$ con base $\{(1,-1,0),(-3,0,1)\}$. $5I-A_0=\begin{pmatrix}3&0&0\\0&3&0\\-1&-1&0\end{pmatrix}$ da $x=y=0$: $E_5=\operatorname{gen}\{(0,0,1)\}$. Entonces
$$
C=\begin{pmatrix}1&-3&0\\-1&0&0\\0&1&1\end{pmatrix},\qquad D=\operatorname{diag}(2,2,5).
$$

**Comprobación.** $A_0(1,-1,0)=(2,-2,0)$, $A_0(-3,0,1)=(-6,0,-3+0+5)=(-6,0,2)$ y $A_0(0,0,1)=(0,0,5)$: son $2c_1$, $2c_2$, $5c_3$. $\det C=-3\neq0$.

:::tip[Resultado]
$A_a$ es diagonalizable si y solo si $a=0$; en ese caso $D=\operatorname{diag}(2,2,5)$ con $C$ como arriba.
:::

</details>

### Ejercicio 12 · Verdadero o falso sobre diagonalización
<!-- ejercicio: U3.12 | nivel: intermedio | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
Decidir si cada afirmación es verdadera o falsa y justificar ($A\in\mathbb{R}^{n\times n}$).

a) Si $A\in\mathbb{R}^{3\times3}$ tiene tres autovalores reales distintos, entonces es diagonalizable.

b) Si $A$ es diagonalizable e inversible, entonces $A^{-1}$ es diagonalizable.

c) Si $A$ tiene un autovalor de multiplicidad algebraica mayor que $1$, entonces no es diagonalizable.

d) Si $A$ es diagonalizable, entonces $A^t$ es diagonalizable.
:::

<details>
<summary>Resolución</summary>

**a) Verdadera.** Autovectores de autovalores distintos son linealmente independientes; tres de ellos forman una base de $\mathbb{R}^3$.

**b) Verdadera.** Si $A=CDC^{-1}$, todos los autovalores (entradas de $D$) son no nulos porque $A$ es inversible, así que $A^{-1}=CD^{-1}C^{-1}$ con $D^{-1}$ diagonal.

**c) Falsa.** Contraejemplo: $A=2I_2$ tiene $m_a(2)=2$ y ya es diagonal; $E_2=\mathbb{R}^2$ y $m_g(2)=2$. La condición correcta es $m_g=m_a$ para cada autovalor.

**d) Verdadera.** Si $A=CDC^{-1}$, trasponiendo $A^t=(C^{-1})^tD^tC^t=(C^t)^{-1}D\,C^t$, con $D^t=D$ diagonal.

**Comprobación.** Para el contraejemplo de c), $p_{2I}(\lambda)=(\lambda-2)^2$ y $2I-2I=0$ tiene rango $0$, de modo que $m_g=2$. Para b), con la matriz del Ejercicio 9, $A^{-1}$ tiene los mismos autovectores y autovalores $1,\tfrac12,-\tfrac13$.

:::tip[Resultado]
a) V; b) V; c) F (contraejemplo $A=2I_2$); d) V.
:::

</details>

### Ejercicio 13 · Contraejemplos de semejanza
<!-- ejercicio: U3.13 | nivel: intermedio | tipo: contraejemplo | verificacion: sympy -->

:::note[Enunciado]
Probar con un contraejemplo que las siguientes afirmaciones son falsas.

a) Si $A$ y $B$ tienen el mismo polinomio característico, entonces son semejantes.

b) Si $A$ y $B$ son semejantes, entonces tienen los mismos autovectores.
:::

<details>
<summary>Resolución</summary>

**a)** Sean $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ y $B=I_2$. Ambas tienen $p(\lambda)=(\lambda-1)^2$. Pero $B=I$ es semejante solo a sí misma: $C^{-1}IC=I$ para toda $C$, y $A\neq I$. Por lo tanto no son semejantes. (Otra forma: $\operatorname{rango}(I-A)=1\neq0=\operatorname{rango}(I-B)$, y el rango es invariante por semejanza.)

**b)** Sean $A=\begin{pmatrix}1&0\\0&2\end{pmatrix}$ y $B=\begin{pmatrix}1&1\\0&2\end{pmatrix}$. Ambas tienen autovalores distintos $1$ y $2$, luego son diagonalizables y semejantes a $\operatorname{diag}(1,2)$, por lo que son semejantes entre sí. Sin embargo $v=(0,1)$ es autovector de $A$ ($Av=2v$) y no de $B$: $Bv=(1,2)$ no es múltiplo de $(0,1)$. Los autovectores de $B$ son los múltiplos de $(1,0)$ y de $(1,1)$.

**Comprobación.** $p_A=p_B=\lambda^2-3\lambda+2$ en b); $E_2(B)=\operatorname{gen}\{(1,1)\}\not\ni(0,1)$.

:::tip[Resultado]
a) $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ e $I$ tienen el mismo $p$ y no son semejantes. b) $\operatorname{diag}(1,2)$ y $\begin{pmatrix}1&1\\0&2\end{pmatrix}$ son semejantes pero $(0,1)$ es autovector de la primera y no de la segunda.
:::

</details>

### Ejercicio 14 · Hallar la matriz que realiza la semejanza
<!-- ejercicio: U3.14 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $A=\begin{pmatrix}0&1\\6&1\end{pmatrix}$ y $B=\begin{pmatrix}-2&5\\0&3\end{pmatrix}$.

a) Probar que $A$ y $B$ son semejantes y hallar $S$ inversible con $AS=SB$.

b) ¿Es $A$ semejante a $G=\begin{pmatrix}3&1\\0&-3\end{pmatrix}$? Justificar.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Diagonalizar ambas con el mismo orden de autovalores; si $A=C_ADC_A^{-1}$ y $B=C_BDC_B^{-1}$, entonces $S=C_AC_B^{-1}$ cumple $S^{-1}AS=B$.

**a)** $p_A=\lambda^2-\lambda-6=(\lambda-3)(\lambda+2)$ y $p_B=(\lambda+2)(\lambda-3)$ son iguales, con autovalores distintos $3$ y $-2$. Autovectores de $A$: $E_3=\operatorname{gen}\{(1,3)\}$, $E_{-2}=\operatorname{gen}\{(1,-2)\}$. De $B$: $E_3=\operatorname{gen}\{(1,1)\}$, $E_{-2}=\operatorname{gen}\{(1,0)\}$. Con $D=\operatorname{diag}(3,-2)$,
$$
C_A=\begin{pmatrix}1&1\\3&-2\end{pmatrix},\quad C_B=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad C_B^{-1}=\begin{pmatrix}0&1\\1&-1\end{pmatrix},\quad S=C_AC_B^{-1}=\begin{pmatrix}1&0\\-2&5\end{pmatrix}.
$$

**Comprobación.** $AS=\begin{pmatrix}0&1\\6&1\end{pmatrix}\begin{pmatrix}1&0\\-2&5\end{pmatrix}=\begin{pmatrix}-2&5\\4&5\end{pmatrix}$ y $SB=\begin{pmatrix}1&0\\-2&5\end{pmatrix}\begin{pmatrix}-2&5\\0&3\end{pmatrix}=\begin{pmatrix}-2&5\\4&5\end{pmatrix}$. Además $\det S=5\neq0$.

**b)** No: $\det A=-6$ pero $\det G=-9$, y el determinante es un invariante de la semejanza. (También difieren las trazas: $1$ contra $0$.)

:::tip[Resultado]
$A$ y $B$ son semejantes, con $S=\begin{pmatrix}1&0\\-2&5\end{pmatrix}$ (hay otras elecciones). $A$ no es semejante a $G$.
:::

</details>

### Ejercicio 15 · Fórmula de $A^k$ y potencias negativas
<!-- ejercicio: U3.15 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}3&-2\\1&0\end{pmatrix}$.

a) Hallar una fórmula para $A^k$, $k\in\mathbb{N}$.

b) Calcular $A^{10}$ y $A^{-3}$.
:::

<details>
<summary>Resolución</summary>

**a)** $p_A=\lambda^2-3\lambda+2=(\lambda-1)(\lambda-2)$. $E_1=\operatorname{gen}\{(1,1)\}$ y $E_2=\operatorname{gen}\{(2,1)\}$. Con $C=\begin{pmatrix}1&2\\1&1\end{pmatrix}$, $\det C=-1$, $C^{-1}=\begin{pmatrix}-1&2\\1&-1\end{pmatrix}$ y $D=\operatorname{diag}(1,2)$:
$$
A^k=CD^kC^{-1}=\begin{pmatrix}1&2^{k+1}\\1&2^k\end{pmatrix}\begin{pmatrix}-1&2\\1&-1\end{pmatrix}=\begin{pmatrix}2^{k+1}-1&2-2^{k+1}\\2^k-1&2-2^k\end{pmatrix}.
$$

**b)** Para $k=10$: $A^{10}=\begin{pmatrix}2047&-2046\\1023&-1022\end{pmatrix}$. Como $A$ es inversible ($\det=2$), la misma fórmula vale para $k=-3$ (porque $A^{-1}=CD^{-1}C^{-1}$):
$$
A^{-3}=\begin{pmatrix}2^{-2}-1&2-2^{-2}\\2^{-3}-1&2-2^{-3}\end{pmatrix}=\begin{pmatrix}-\tfrac34&\tfrac74\\-\tfrac78&\tfrac{15}{8}\end{pmatrix}.
$$

**Comprobación.** $k=1$ devuelve $A$. Con $A^3=\begin{pmatrix}15&-14\\7&-6\end{pmatrix}$, la primera fila de $A^{-3}$ por las columnas de $A^3$ da $-\tfrac{45}{4}+\tfrac{49}{4}=1$ y $\tfrac{42}{4}-\tfrac{42}{4}=0$, como en $A^{-3}A^3=I$.

:::tip[Resultado]
$A^k=\begin{pmatrix}2^{k+1}-1&2-2^{k+1}\\2^k-1&2-2^k\end{pmatrix}$, $A^{10}=\begin{pmatrix}2047&-2046\\1023&-1022\end{pmatrix}$, $A^{-3}=\begin{pmatrix}-\frac34&\frac74\\-\frac78&\frac{15}8\end{pmatrix}$.
:::

</details>

### Ejercicio 16 · ¿Es inversible $A^k-I$?
<!-- ejercicio: U3.16 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}6&-4&4\\2&-3&2\\-6&3&-4\end{pmatrix}$, cuyo polinomio característico es $(\lambda-2)(\lambda+1)(\lambda+2)$.

a) Determinar para qué $k\in\mathbb{N}$ la matriz $A^k-I$ es inversible.

b) Decidir si $B=A^2+A-2I$ es inversible.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Una matriz es inversible si y solo si $0$ no es autovalor; los autovalores de $q(A)$ son $q(\lambda)$.

**a)** Los autovalores de $A^k-I$ son $2^k-1$, $(-1)^k-1$ y $(-2)^k-1$. Para $k\ge1$: $2^k-1\neq0$ y $(-2)^k-1\neq0$ (el módulo es $\ge2$). En cambio $(-1)^k-1=0$ si y solo si $k$ es par. Luego $A^k-I$ es inversible si y solo si $k$ es **impar**.

**b)** Con $q(x)=x^2+x-2=(x-1)(x+2)$: $q(2)=4$, $q(-1)=-2$, $q(-2)=0$. Aparece el autovalor $0$, así que $B$ no es inversible.

**Comprobación.** $\det(A^k-I)=(2^k-1)((-1)^k-1)((-2)^k-1)$ da $6$ para $k=1$, $0$ para $k=2$, $126$ para $k=3$ y $0$ para $k=4$. Además $B=\begin{pmatrix}8&-4&4\\-4&2&-4\\-12&6&-8\end{pmatrix}$ tiene $p_B=\lambda(\lambda-4)(\lambda+2)$.

:::tip[Resultado]
$A^k-I$ es inversible si y solo si $k$ es impar; $A^2+A-2I$ no es inversible (autovalor $0$).
:::

</details>

### Ejercicio 17 · Conteo de embaldosados con una recurrencia
<!-- ejercicio: U3.17 | nivel: intermedio | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Sea $a_n$ la cantidad de formas de cubrir un tablero de $2\times n$ con fichas de $2\times1$ (en cualquier orientación) y fichas cuadradas de $2\times2$, sin superposiciones. Se sabe que $a_0=1$, $a_1=1$.

a) Justificar que $a_{n+1}=a_n+2a_{n-1}$ para $n\ge1$.

b) Escribir la recurrencia en forma matricial y diagonalizar la matriz compañera.

c) Hallar una fórmula cerrada para $a_n$ y calcular $a_{10}$.
:::

<details>
<summary>Resolución</summary>

**a)** Miremos la última columna del tablero de $2\times(n+1)$. Si la cubre una ficha vertical de $2\times1$, queda un tablero de $2\times n$: $a_n$ maneras. Si no, la última columna y la anterior se cubren juntas con un cuadrado $2\times2$ o con dos fichas horizontales apiladas: $2$ opciones, y quedan $2\times(n-1)$: $2a_{n-1}$ maneras. Entonces $a_{n+1}=a_n+2a_{n-1}$.

**b)** Con $x_n=\begin{pmatrix}a_{n+1}\\a_n\end{pmatrix}$ se tiene $x_n=Ax_{n-1}$, donde $A=\begin{pmatrix}1&2\\1&0\end{pmatrix}$ y $x_0=(1,1)$. $p_A=\lambda^2-\lambda-2=(\lambda-2)(\lambda+1)$, con $E_2=\operatorname{gen}\{(2,1)\}$ y $E_{-1}=\operatorname{gen}\{(-1,1)\}$.

**c)** Escribimos $x_0=\alpha(2,1)+\beta(-1,1)$: $2\alpha-\beta=1$, $\alpha+\beta=1$, luego $\alpha=\tfrac23$, $\beta=\tfrac13$. Entonces $x_n=A^nx_0=\alpha2^n(2,1)+\beta(-1)^n(-1,1)$, y la segunda coordenada es
$$
a_n=\frac{2^{n+1}+(-1)^n}{3}.
$$
Así $a_{10}=\dfrac{2048+1}{3}=683$.

**Comprobación.** Por la recurrencia: $1,1,3,5,11,21,43,85,171,341,683$. La fórmula da $a_2=(8+1)/3=3$ y $a_3=(16-1)/3=5$.

:::tip[Resultado]
$a_n=\dfrac{2^{n+1}+(-1)^n}{3}$; $a_{10}=683$.
:::

</details>

### Ejercicio 18 · Estado de un hilo de ejecución
<!-- ejercicio: U3.18 | nivel: intermedio | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Un hilo de un servidor está en cada paso de tiempo en uno de tres estados: **Inactivo** (I), **Ejecutando** (E) o **Bloqueado** (B). Las probabilidades de pasar al estado siguiente son: desde I: $0{,}5$ a I, $0{,}2$ a E, $0{,}3$ a B; desde E: $0{,}2$ a I, $0{,}5$ a E, $0{,}3$ a B; desde B: $0{,}1$ a I, $0{,}1$ a E, $0{,}8$ a B.

a) Escribir la matriz de transición $P$ (con el orden I, E, B) y verificar que es estocástica por columnas.

b) Si el hilo empieza Inactivo, hallar la distribución luego de uno y de dos pasos.

c) Hallar el vector de estado estacionario y $\lim_{k\to\infty}P^k$. Interpretar.
:::

<details>
<summary>Resolución</summary>

**a)** La columna $j$ tiene las probabilidades de salir del estado $j$:
$$
P=\frac1{10}\begin{pmatrix}5&2&1\\2&5&1\\3&3&8\end{pmatrix}.
$$
Cada columna suma $10/10=1$ y todas las entradas son no negativas.

**b)** $x_0=(1,0,0)$. $x_1=Px_0=(0{,}5;\ 0{,}2;\ 0{,}3)=\left(\tfrac12,\tfrac15,\tfrac3{10}\right)$ y
$$
x_2=Px_1=\left(\tfrac{8}{25},\ \tfrac{23}{100},\ \tfrac{9}{20}\right)=(0{,}32;\ 0{,}23;\ 0{,}45).
$$

**c)** Resolvemos $(I-P)x=0$ con $I-P=\tfrac1{10}\begin{pmatrix}5&-2&-1\\-2&5&-1\\-3&-3&2\end{pmatrix}$. Restando las dos primeras ecuaciones, $7x_1-7x_2=0$, o sea $x_1=x_2$; de la primera, $3x_1=x_3$. Una solución es $(1,1,3)$, y normalizando a suma $1$:
$$
\pi=\left(\tfrac15,\ \tfrac15,\ \tfrac35\right).
$$
Todas las entradas de $P$ son positivas, así que la cadena es regular y $P^k\to\begin{pmatrix}\pi&\pi&\pi\end{pmatrix}$:
$$
\lim_{k\to\infty}P^k=\begin{pmatrix}\tfrac15&\tfrac15&\tfrac15\\\tfrac15&\tfrac15&\tfrac15\\\tfrac35&\tfrac35&\tfrac35\end{pmatrix},
$$
sin importar el estado inicial. A la larga el hilo pasa $60\%$ del tiempo bloqueado.

**Comprobación.** En $P\pi$, la primera coordenada es $\tfrac1{10}\left(5\cdot\tfrac15+2\cdot\tfrac15+1\cdot\tfrac35\right)=\tfrac15$ y la tercera $\tfrac1{10}\left(\tfrac35+\tfrac35+\tfrac{24}5\right)=\tfrac35$. El polinomio característico es $(\lambda-1)(\lambda-\tfrac12)(\lambda-\tfrac3{10})$: el autovalor $1$ es simple y los otros dos tienen módulo menor que $1$, lo que explica la convergencia.

:::tip[Resultado]
$x_1=(0{,}5;0{,}2;0{,}3)$, $x_2=(0{,}32;0{,}23;0{,}45)$, $\pi=(\tfrac15,\tfrac15,\tfrac35)$ y $P^k\to(\pi\ \pi\ \pi)$.
:::

</details>
