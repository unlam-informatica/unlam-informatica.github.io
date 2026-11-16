---
title: Práctica — Nivel avanzado
description: Ocho ejercicios avanzados de autovalores y diagonalización con demostraciones, contraejemplos, parámetros, recurrencias de raíz doble y cadenas de Markov, con resolución completa.
slug: algebra-ii/unidad-3/practica/nivel-avanzado
sidebar:
  order: 3
  label: Nivel avanzado
---

:::note[Cómo usar esta página]
Ejercicios **originales** que exigen argumentar con rigor: demostraciones, contraejemplos, dos parámetros,
una recurrencia con raíz doble y modelos de Markov. En las demostraciones, fijá primero las hipótesis y
qué se quiere probar. Los ejercicios continúan los del [nivel intermedio](/algebra-ii/unidad-3/practica/nivel-intermedio/).

**Presupone:** todas las lecciones de la unidad, en especial
[3.3 Propiedades](/algebra-ii/unidad-3/teoria/propiedades/),
[3.5 Diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/),
[3.7 Relaciones de recurrencia](/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/) y
[3.8 Cadenas de Markov](/algebra-ii/unidad-3/teoria/cadenas-de-markov/).

Siguiente: [guía integradora](/algebra-ii/unidad-3/practica/guia-integradora/).
:::

### Ejercicio 19 · Matrices idempotentes
<!-- ejercicio: U3.19 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $A\in\mathbb{R}^{n\times n}$ tal que $A^2=A$.

a) Probar que todo autovalor de $A$ es $0$ o $1$.

b) Probar que $\mathbb{R}^n=\operatorname{nul}(A)\oplus\operatorname{nul}(A-I)$ y deducir que $A$ es diagonalizable.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para a), aplicar la definición y $A^2=A$. Para b), descomponer cada vector en una parte que $A$ anula y una que $A$ deja fija.

**a)** Si $Av=\lambda v$ con $v\neq0$, entonces $\lambda v=Av=A^2v=A(\lambda v)=\lambda^2v$. Luego $(\lambda^2-\lambda)v=0$ y, como $v\neq0$, $\lambda(\lambda-1)=0$.

**b)** *Suma.* Para $v\in\mathbb{R}^n$, $v=(v-Av)+Av$. Se cumple $A(v-Av)=Av-A^2v=0$, así que $v-Av\in\operatorname{nul}(A)$, y $(A-I)(Av)=A^2v-Av=0$, así que $Av\in\operatorname{nul}(A-I)$. *Intersección.* Si $x\in\operatorname{nul}(A)\cap\operatorname{nul}(A-I)$, entonces $Ax=0$ y $Ax=x$, de modo que $x=0$. Por lo tanto la suma es directa y $\mathbb{R}^n=E_0\oplus E_1$ (cuando algún subespacio es $\{0\}$, el correspondiente número no es autovalor y el argumento sigue valiendo). Uniendo una base de $E_0$ con una de $E_1$ se obtiene una base de $\mathbb{R}^n$ formada por autovectores: $A$ es diagonalizable, con $D$ diagonal con entradas $0$ y $1$.

**Comprobación de las hipótesis.** No se usó nada más que $A^2=A$. Ejemplo: la proyección $A=\tfrac15\begin{pmatrix}1&2\\2&4\end{pmatrix}$ del Ejercicio 2 cumple $A^2=A$ y tiene autovalores $1$ y $0$.

:::tip[Resultado]
Los autovalores de una idempotente están en $\{0,1\}$ y $\mathbb{R}^n=\operatorname{nul}(A)\oplus\operatorname{nul}(A-I)$: es diagonalizable. $\blacksquare$
:::

</details>

### Ejercicio 20 · Matrices nilpotentes
<!-- ejercicio: U3.20 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Una matriz $N\in\mathbb{R}^{n\times n}$ es **nilpotente** si $N^k=0$ para algún $k\ge1$.

a) Probar que el único autovalor real posible de $N$ es $0$.

b) Probar que si $N$ es nilpotente y diagonalizable, entonces $N=0$.

c) Dar una matriz nilpotente no nula de $2\times2$ y concluir que no es diagonalizable.
:::

<details>
<summary>Resolución</summary>

**a)** Si $Nv=\lambda v$ con $v\neq0$, por inducción $N^jv=\lambda^jv$. Entonces $0=N^kv=\lambda^kv$ y, como $v\neq0$, $\lambda^k=0$, o sea $\lambda=0$.

**b)** Si $N=CDC^{-1}$ con $D$ diagonal, las entradas de $D$ son autovalores de $N$, que por a) son todas $0$. Entonces $D=0$ y $N=C0C^{-1}=0$.

**c)** $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ cumple $N^2=0$ y $N\neq0$. Por b) no es diagonalizable. Directamente: $p_N=\lambda^2$, $m_a(0)=2$ y $\operatorname{nul}(N)=\operatorname{gen}\{(1,0)\}$, de modo que $m_g(0)=1$.

**Comprobación.** En c), $N^2=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}=0$, y $m_g=1<m_a=2$ confirma el resultado de b).

:::tip[Resultado]
Una nilpotente solo tiene el autovalor $0$ y, si es diagonalizable, es la matriz nula. $\blacksquare$
:::

</details>

### Ejercicio 21 · Dos parámetros
<!-- ejercicio: U3.21 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A_{a,b}=\begin{pmatrix}2&a&b\\0&2&0\\0&0&3\end{pmatrix}$ con $a,b\in\mathbb{R}$.

a) Determinar para qué valores de $(a,b)$ la matriz es diagonalizable.

b) Para $a=0$ hallar $C$ y $D$ con $A_{0,b}=CDC^{-1}$ y una fórmula para $A_{0,b}^k$.
:::

<details>
<summary>Resolución</summary>

**a)** $p_A(\lambda)=(\lambda-2)^2(\lambda-3)$. Solo hay que analizar $\lambda=2$:
$$
2I-A=\begin{pmatrix}0&-a&-b\\0&0&0\\0&0&-1\end{pmatrix}.
$$
Las filas no nulas son $(0,-a,-b)$ y $(0,0,-1)$. Son linealmente independientes si y solo si $a\neq0$ (si $a=0$, la primera es múltiplo de la tercera). Entonces: si $a\neq0$, rango $2$ y $m_g(2)=1<2$: no diagonalizable. Si $a=0$, rango $1$ y $m_g(2)=2$: diagonalizable, **para cualquier $b$**. El parámetro $b$ no influye.

**b)** Con $a=0$: $E_2=\{z=0\}=\operatorname{gen}\{(1,0,0),(0,1,0)\}$ y $3I-A=\begin{pmatrix}1&0&-b\\0&1&0\\0&0&0\end{pmatrix}$ da $E_3=\operatorname{gen}\{(b,0,1)\}$. Entonces
$$
C=\begin{pmatrix}1&0&b\\0&1&0\\0&0&1\end{pmatrix},\quad D=\operatorname{diag}(2,2,3),\quad C^{-1}=\begin{pmatrix}1&0&-b\\0&1&0\\0&0&1\end{pmatrix},
$$
$$
A_{0,b}^k=CD^kC^{-1}=\begin{pmatrix}2^k&0&b\,(3^k-2^k)\\0&2^k&0\\0&0&3^k\end{pmatrix}.
$$

**Comprobación.** $\begin{pmatrix}2&0&b\\0&2&0\\0&0&3\end{pmatrix}\begin{pmatrix}b\\0\\1\end{pmatrix}=(3b,0,3)=3(b,0,1)$. Para $k=1$ la fórmula da $b(3-2)=b$, y para $k=2$, $b(9-4)=5b$, que coincide con la entrada $(1,3)$ de $A^2$: $2b+3b=5b$.

:::tip[Resultado]
$A_{a,b}$ es diagonalizable si y solo si $a=0$ (con $b$ cualquiera). Para $a=0$, $A^k=\begin{pmatrix}2^k&0&b(3^k-2^k)\\0&2^k&0\\0&0&3^k\end{pmatrix}$.
:::

</details>

### Ejercicio 22 · Diagonalizables cuya suma y producto no lo son
<!-- ejercicio: U3.22 | nivel: avanzado | tipo: contraejemplo | verificacion: sympy -->

:::note[Enunciado]
Probar que son falsas:

a) Si $A$ y $B$ son diagonalizables, entonces $A+B$ es diagonalizable.

b) Si $A$ y $B$ son diagonalizables, entonces $AB$ es diagonalizable.

Usar el mismo par de matrices para ambos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Buscar dos matrices simples que no comparten autovectores, de modo que la suma o el producto sea una matriz tipo $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ o nilpotente.

Sean $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ y $B=\begin{pmatrix}0&1\\0&1\end{pmatrix}$.

- $A$ es diagonal. $p_B=\lambda^2-\lambda$, con autovalores distintos $0$ y $1$, luego $B$ es diagonalizable ($E_1=\operatorname{gen}\{(1,1)\}$, $E_0=\operatorname{gen}\{(1,0)\}$).

**a)** $A+B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, con $p=(\lambda-1)^2$ y $I-(A+B)=\begin{pmatrix}0&-1\\0&0\end{pmatrix}$ de rango $1$: $m_g(1)=1<2$. No es diagonalizable.

**b)** $AB=\begin{pmatrix}1&0\\0&0\end{pmatrix}\begin{pmatrix}0&1\\0&1\end{pmatrix}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, nilpotente no nula: por el Ejercicio 20 no es diagonalizable.

**Comprobación.** $(AB)^2=0$, $AB\neq0$, y $p_{AB}=\lambda^2$ con $\operatorname{nul}(AB)=\operatorname{gen}\{(1,0)\}$. Aquí $AB\neq BA$ ($BA=\begin{pmatrix}0&0\\0&0\end{pmatrix}$): las matrices no conmutan, que es lo que falla.

:::tip[Resultado]
Con $A=\operatorname{diag}(1,0)$ y $B=\begin{pmatrix}0&1\\0&1\end{pmatrix}$, ambas diagonalizables, $A+B$ y $AB$ no lo son.
:::

</details>

### Ejercicio 23 · Un costo recursivo con raíz doble
<!-- ejercicio: U3.23 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
El costo $T(n)$ (en operaciones) de un procedimiento recursivo satisface $T(n+1)=4T(n)-4T(n-1)$ para $n\ge1$, con $T(0)=1$ y $T(1)=3$.

a) Escribir la forma matricial $x_n=A\,x_{n-1}$ con $x_n=(T(n+1),T(n))$ y probar que $A$ no es diagonalizable.

b) Hallar $A^n$ escribiendo $A=2I+N$ con $N^2=0$.

c) Deducir una fórmula cerrada para $T(n)$ y calcular $T(10)$.
:::

<details>
<summary>Resolución</summary>

**a)** $A=\begin{pmatrix}4&-4\\1&0\end{pmatrix}$ y $x_0=(3,1)$. $p_A=\lambda^2-4\lambda+4=(\lambda-2)^2$. $2I-A=\begin{pmatrix}-2&4\\-1&2\end{pmatrix}$ tiene rango $1$, así que $m_g(2)=1<2=m_a(2)$: $A$ no es diagonalizable.

**b)** Sea $N=A-2I=\begin{pmatrix}2&-4\\1&-2\end{pmatrix}$. Se verifica $N^2=\begin{pmatrix}4-4&-8+8\\2-2&-4+4\end{pmatrix}=0$. Como $2I$ conmuta con $N$, la fórmula del binomio tiene solo dos términos:
$$
A^n=(2I+N)^n=2^nI+n\,2^{n-1}N.
$$

**c)** $T(n)$ es la segunda coordenada de $x_n=A^nx_0$. La segunda fila de $A^n$ es $\left(n2^{n-1},\ 2^n-2n2^{n-1}\right)=\left(n2^{n-1},\ (1-n)2^n\right)$. Entonces
$$
T(n)=3n2^{n-1}+(1-n)2^n=2^{n-1}(3n+2-2n)=(n+2)\,2^{n-1}.
$$
$T(10)=12\cdot2^9=6144$.

**Comprobación.** Por la recurrencia: $1,3,8,20,48,112,\ldots$; la fórmula da $T(2)=4\cdot2=8$, $T(3)=5\cdot4=20$ y $T(4)=6\cdot8=48$. El crecimiento es $n2^n$: la raíz doble agrega el factor lineal en $n$.

:::tip[Resultado]
$T(n)=(n+2)2^{n-1}$; $T(10)=6144$.
:::

</details>

### Ejercicio 24 · Navegación en un sitio de tres páginas
<!-- ejercicio: U3.24 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Un navegante recorre un sitio de tres páginas $1,2,3$ eligiendo en cada paso, con igual probabilidad, uno de los enlaces de la página en que está. La página $1$ enlaza a $2$ y a $3$; la página $2$ enlaza a $1$ y a $3$; la página $3$ enlaza solo a $1$.

a) Escribir la matriz de transición $P$ (estocástica por columnas).

b) Hallar el vector estacionario $\pi$.

c) Justificar que $P^k$ converge y hallar $\lim P^k$; ¿qué página se visita más a largo plazo?
:::

<details>
<summary>Resolución</summary>

**a)** Desde $1$: $\tfrac12$ a $2$ y $\tfrac12$ a $3$. Desde $2$: $\tfrac12$ a $1$ y $\tfrac12$ a $3$. Desde $3$: $1$ a $1$. Entonces
$$
P=\begin{pmatrix}0&\tfrac12&1\\\tfrac12&0&0\\\tfrac12&\tfrac12&0\end{pmatrix}.
$$

**b)** $P\pi=\pi$ da $\pi_1=\tfrac12\pi_2+\pi_3$, $\pi_2=\tfrac12\pi_1$, $\pi_3=\tfrac12\pi_1+\tfrac12\pi_2$. De la segunda, $\pi_2=\tfrac12\pi_1$; en la tercera, $\pi_3=\tfrac12\pi_1+\tfrac14\pi_1=\tfrac34\pi_1$. Con $\pi_1+\pi_2+\pi_3=\left(1+\tfrac12+\tfrac34\right)\pi_1=\tfrac94\pi_1=1$:
$$
\pi=\left(\tfrac49,\ \tfrac29,\ \tfrac13\right).
$$

**c)** $P^4=\begin{pmatrix}\tfrac9{16}&\tfrac12&\tfrac14\\\tfrac18&\tfrac3{16}&\tfrac38\\\tfrac5{16}&\tfrac5{16}&\tfrac38\end{pmatrix}$ tiene todas las entradas positivas, así que $P$ es regular y $P^k\to(\pi\ \pi\ \pi)$:
$$
\lim_{k\to\infty}P^k=\begin{pmatrix}\tfrac49&\tfrac49&\tfrac49\\\tfrac29&\tfrac29&\tfrac29\\\tfrac13&\tfrac13&\tfrac13\end{pmatrix}.
$$
La página $1$ es la más visitada ($44{,}4\%$ del tiempo).

**Comprobación.** $P\pi=\left(\tfrac12\cdot\tfrac29+\tfrac13,\ \tfrac12\cdot\tfrac49,\ \tfrac12\cdot\tfrac49+\tfrac12\cdot\tfrac29\right)=\left(\tfrac49,\tfrac29,\tfrac13\right)$. El polinomio característico es $\lambda^3-\tfrac34\lambda-\tfrac14=(\lambda-1)(\lambda+\tfrac12)^2$: $P$ **no** es diagonalizable ($E_{-1/2}=\operatorname{gen}\{(-1,1,0)\}$ tiene dimensión $1$), pero la convergencia se garantiza por la regularidad.

:::tip[Resultado]
$\pi=\left(\tfrac49,\tfrac29,\tfrac13\right)$ y $P^k\to(\pi\ \pi\ \pi)$; la página $1$ es la más visitada.
:::

</details>

### Ejercicio 25 · El autovalor $1$ de una matriz estocástica
<!-- ejercicio: U3.25 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $P\in\mathbb{R}^{n\times n}$ con entradas no negativas y cada columna con suma $1$.

a) Probar que $1$ es autovalor de $P$.

b) Probar que todo autovalor real $\lambda$ de $P$ cumple $|\lambda|\le1$.
:::

<details>
<summary>Resolución</summary>

**a)** Sea $u=(1,\ldots,1)$. Que las columnas sumen $1$ equivale a $u^tP=u^t$, es decir $P^tu=u$. Entonces $1$ es autovalor de $P^t$, o sea $\det(I-P^t)=0$. Como $\det(I-P^t)=\det\big((I-P)^t\big)=\det(I-P)$, resulta $\det(I-P)=0$ y $1$ es autovalor de $P$ (con otros autovectores que $u$, en general).

**b)** Sea $Pv=\lambda v$, $v\neq0$. Tomando valor absoluto en cada coordenada y sumando,
$$
|\lambda|\sum_i|v_i|=\sum_i\Big|\sum_jP_{ij}v_j\Big|\le\sum_i\sum_jP_{ij}|v_j|=\sum_j|v_j|\Big(\sum_iP_{ij}\Big)=\sum_j|v_j|,
$$
usando $P_{ij}\ge0$ y que cada columna suma $1$. Como $\sum|v_i|>0$, se concluye $|\lambda|\le1$.

**Comprobación.** En el Ejercicio 18 los autovalores son $1,\tfrac12,\tfrac3{10}$: todos de módulo $\le1$ y entre ellos aparece el $1$.

:::tip[Resultado]
Toda matriz estocástica por columnas tiene el autovalor $1$, y ninguno de sus autovalores tiene módulo mayor que $1$. $\blacksquare$
:::

</details>

### Ejercicio 26 · Conexión estable o inestable según un parámetro
<!-- ejercicio: U3.26 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Una conexión está en estado **Estable** (E) o **Inestable** (I). Desde E pasa a I con probabilidad $a\in[0,1]$ y permanece en E con probabilidad $1-a$; desde I pasa a E con probabilidad $\tfrac12$ y permanece en I con probabilidad $\tfrac12$.

a) Escribir la matriz de transición $P_a$ y hallar sus autovalores.

b) Hallar el vector estacionario en función de $a$ y $\lim_{k\to\infty}P_a^k$.

c) ¿Para qué valores de $a$ la conexión está estable al menos el $75\%$ del tiempo a largo plazo?
:::

<details>
<summary>Resolución</summary>

**a)** Con el orden (E, I):
$$
P_a=\begin{pmatrix}1-a&\tfrac12\\a&\tfrac12\end{pmatrix}.
$$
Traza $=\tfrac32-a$ y determinante $=\tfrac{1-a}2-\tfrac a2=\tfrac12-a$, de modo que $p_{P_a}(\lambda)=\lambda^2-(\tfrac32-a)\lambda+(\tfrac12-a)=(\lambda-1)(\lambda-(\tfrac12-a))$. Autovalores: $1$ y $\tfrac12-a$, con $|\tfrac12-a|\le\tfrac12<1$ para $a\in[0,1]$.

**b)** $(I-P_a)x=0$ equivale a $-ax_1+\tfrac12x_2=0$, o sea $x_2=2a\,x_1$. Autovector $(1,2a)$ y, normalizando,
$$
\pi_a=\frac1{1+2a}\,(1,\ 2a).
$$
Como el otro autovalor tiene módulo menor que $1$ (hay dos autovalores distintos, así que $P_a$ es diagonalizable),
$$
\lim_{k\to\infty}P_a^k=\frac1{1+2a}\begin{pmatrix}1&1\\2a&2a\end{pmatrix}.
$$
Esto vale también para $a=0$: $\pi_0=(1,0)$ y la conexión queda siempre en E.

**c)** La fracción estable es $\dfrac1{1+2a}\ge\dfrac34\iff4\ge3+6a\iff a\le\dfrac16$.

**Comprobación.** Para $a=\tfrac12$: $P=\begin{pmatrix}\tfrac12&\tfrac12\\\tfrac12&\tfrac12\end{pmatrix}$, $\pi=(\tfrac12,\tfrac12)$, autovalores $1$ y $0$, y $P^2=P$ ya es el límite. La fórmula da $\tfrac1{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$.

:::tip[Resultado]
Autovalores $1$ y $\tfrac12-a$; $\pi_a=\tfrac1{1+2a}(1,2a)$; estabilidad $\ge75\%$ si y solo si $0\le a\le\tfrac16$.
:::

</details>
