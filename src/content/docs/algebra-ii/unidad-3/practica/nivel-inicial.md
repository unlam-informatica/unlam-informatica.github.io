---
title: Práctica — Nivel inicial
description: Ocho ejercicios iniciales de autovalores y autovectores con resolución completa, desde la definición y la interpretación geométrica hasta las propiedades básicas.
slug: algebra-ii/unidad-3/practica/nivel-inicial
sidebar:
  order: 1
  label: Nivel inicial
---

:::note[Cómo usar esta página]
Ejercicios **originales** para fijar las ideas básicas de la unidad. Resolvé cada uno por tu cuenta antes de abrir la
resolución; después compará el método, no solo el resultado. Cada resolución termina con una
**comprobación** que podés repetir con tus propios resultados (por ejemplo, $Av=\lambda v$ o $AC=CD$).

**Presupone:** [3.1 Autovalores y autovectores](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/),
[3.2 Polinomio característico](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/) y los comienzos de
[3.3 Propiedades](/algebra-ii/unidad-3/teoria/propiedades/). Convención: $p_A(\lambda)=\det(\lambda I-A)$ y
$E_\lambda(A)=\operatorname{nul}(\lambda I-A)$.

Siguiente: [nivel intermedio](/algebra-ii/unidad-3/practica/nivel-intermedio/).
:::

### Ejercicio 1 · ¿Quién es autovector?
<!-- ejercicio: U3.01 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}1&2\\3&0\end{pmatrix}$ y sean $u=(1,1)$, $v=(2,-3)$, $w=(1,0)$.

a) Decidir, usando la definición, cuáles de $u,v,w$ son autovectores de $A$ y, en ese caso, hallar el autovalor.

b) ¿Es $\lambda=1$ un autovalor de $A$? Justificar con un determinante.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $x$ es autovector si $x\neq0$ y $Ax$ es múltiplo de $x$.

**a)** $Au=(1+2,\ 3)=(3,3)=3u$: autovector de autovalor $3$.
$Av=(2-6,\ 6)=(-4,6)=-2v$: autovector de autovalor $-2$.
$Aw=(1,3)$ no es múltiplo de $(1,0)$ (la segunda coordenada es $3\neq0$ y la primera no se anula): $w$ no es autovector.

**b)** $1$ es autovalor si y solo si $\det(I-A)=0$. Pero
$$
\det(I-A)=\det\begin{pmatrix}0&-2\\-3&1\end{pmatrix}=0\cdot1-(-2)(-3)=-6\neq0,
$$
así que $1$ no es autovalor.

**Comprobación.** $p_A(\lambda)=\lambda^2-\lambda-6=(\lambda-3)(\lambda+2)$ y la traza es $1=3+(-2)$: los autovalores son
exactamente $3$ y $-2$, coherente con a) y con b).

:::tip[Resultado]
$u$ (autovalor $3$) y $v$ (autovalor $-2$) son autovectores; $w$ no. El número $1$ no es autovalor ($\det(I-A)=-6$).
:::

</details>

### Ejercicio 2 · Proyección sobre una recta
<!-- ejercicio: U3.02 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:\mathbb{R}^2\to\mathbb{R}^2$ la proyección ortogonal sobre la recta $L=\operatorname{gen}\{(1,2)\}$.

a) Sin hacer cuentas, hallar los autovalores de $T$ y sus autoespacios.

b) Hallar la matriz $A$ de $T$ en la base canónica a partir de a).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Geométricamente: los vectores de $L$ no se mueven y los perpendiculares a $L$ van al origen.

**a)** Si $x\in L$, $T(x)=x$: autovalor $1$ con $E_1=L=\operatorname{gen}\{(1,2)\}$. Si $x\perp L$, es decir $x\in\operatorname{gen}\{(2,-1)\}$ (porque $(1,2)\cdot(2,-1)=0$), $T(x)=0=0\cdot x$: autovalor $0$ con $E_0=\operatorname{gen}\{(2,-1)\}$. Como $\dim E_1+\dim E_0=2$, no hay otros autovalores.

**b)** Con $C=\begin{pmatrix}1&2\\2&-1\end{pmatrix}$ (autovectores en columnas) y $D=\operatorname{diag}(1,0)$, $A=CDC^{-1}$. Como $\det C=-5$, $C^{-1}=\tfrac15\begin{pmatrix}1&2\\2&-1\end{pmatrix}$ y
$$
A=\begin{pmatrix}1&0\\2&0\end{pmatrix}\tfrac15\begin{pmatrix}1&2\\2&-1\end{pmatrix}=\frac15\begin{pmatrix}1&2\\2&4\end{pmatrix}.
$$

**Comprobación.** $A(1,2)=\tfrac15(1+4,\ 2+8)=(1,2)$ y $A(2,-1)=\tfrac15(2-2,\ 4-4)=(0,0)$. Además $p_A(\lambda)=\lambda^2-\lambda$ (traza $1$, determinante $0$).

:::tip[Resultado]
$E_1=\operatorname{gen}\{(1,2)\}$, $E_0=\operatorname{gen}\{(2,-1)\}$, $A=\tfrac15\begin{pmatrix}1&2\\2&4\end{pmatrix}$.
:::

</details>

### Ejercicio 3 · Autovalores y autoespacios de una matriz 2×2
<!-- ejercicio: U3.03 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $A=\begin{pmatrix}1&4\\2&3\end{pmatrix}$ hallar el polinomio característico, los autovalores y una base de cada autoespacio.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Resolver $\det(\lambda I-A)=0$ y, para cada raíz, el sistema homogéneo $(\lambda I-A)x=0$.

$$
p_A(\lambda)=\det\begin{pmatrix}\lambda-1&-4\\-2&\lambda-3\end{pmatrix}=(\lambda-1)(\lambda-3)-8=\lambda^2-4\lambda-5=(\lambda-5)(\lambda+1).
$$

**$\lambda=5$:** $5I-A=\begin{pmatrix}4&-4\\-2&2\end{pmatrix}$ equivale a $x-y=0$; $E_5=\operatorname{gen}\{(1,1)\}$.

**$\lambda=-1$:** $-I-A=\begin{pmatrix}-2&-4\\-2&-4\end{pmatrix}$ equivale a $x+2y=0$; $E_{-1}=\operatorname{gen}\{(2,-1)\}$.

**Comprobación.** $A(1,1)=(5,5)$ y $A(2,-1)=(2-4,\ 4-3)=(-2,1)=-(2,-1)$. Traza: $4=5+(-1)$; determinante: $-5=5\cdot(-1)$.

:::tip[Resultado]
$p_A=\lambda^2-4\lambda-5$; $E_5=\operatorname{gen}\{(1,1)\}$, $E_{-1}=\operatorname{gen}\{(2,-1)\}$.
:::

</details>

### Ejercicio 4 · Multiplicidades en una matriz 3×3
<!-- ejercicio: U3.04 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}2&1&-1\\-1&3&0\\-1&1&2\end{pmatrix}$.

a) Hallar los autovalores con su multiplicidad algebraica.

b) Hallar los autoespacios y la multiplicidad geométrica de cada autovalor.

c) ¿Es $A$ diagonalizable? Justificar.
:::

<details>
<summary>Resolución</summary>

**a)** Desarrollando $\det(\lambda I-A)$ se obtiene
$$
p_A(\lambda)=\lambda^3-7\lambda^2+16\lambda-12=(\lambda-2)^2(\lambda-3),
$$
(Ruffini con $\lambda=2$: cociente $\lambda^2-5\lambda+6=(\lambda-2)(\lambda-3)$). Entonces $m_a(2)=2$ y $m_a(3)=1$.

**b)** Para $\lambda=2$: $2I-A=\begin{pmatrix}0&-1&1\\1&-1&0\\1&-1&0\end{pmatrix}$. Las dos últimas filas son iguales y las dos primeras independientes: rango $2$. Las ecuaciones $y=z$, $x=y$ dan $E_2=\operatorname{gen}\{(1,1,1)\}$ y $m_g(2)=1$.
Para $\lambda=3$: $3I-A=\begin{pmatrix}1&-1&1\\1&0&0\\1&-1&1\end{pmatrix}$ da $x=0$, $y=z$: $E_3=\operatorname{gen}\{(0,1,1)\}$, $m_g(3)=1$.

**c)** No: $m_g(2)=1<2=m_a(2)$, así que no hay una base de $\mathbb{R}^3$ formada por autovectores (en total solo hay $2$ autovectores independientes).

**Comprobación.** $A(1,1,1)=(2,2,2)$ y $A(0,1,1)=(0,3,3)$. Traza $7=2+2+3$, determinante $12=2\cdot2\cdot3$.

:::tip[Resultado]
$m_a(2)=2$, $m_g(2)=1$; $m_a(3)=m_g(3)=1$. $A$ no es diagonalizable.
:::

</details>

### Ejercicio 5 · Matrices sin autovalores reales
<!-- ejercicio: U3.05 | nivel: inicial | tipo: conceptual | verificacion: sympy -->

:::note[Enunciado]
a) Sea $R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ el giro de $90^\circ$ en el plano. Explicar geométricamente por qué no tiene autovectores reales y confirmarlo con $p_R$.

b) Probar que $B=\begin{pmatrix}2&-1\\1&2\end{pmatrix}$ no tiene autovalores reales.

c) ¿Puede una matriz real de $3\times3$ carecer de autovalores reales? Justificar y dar un ejemplo con exactamente un autovalor real.
:::

<details>
<summary>Resolución</summary>

**a)** Un autovector debería quedar sobre su propia recta, pero un giro de $90^\circ$ lleva todo vector no nulo a uno perpendicular a él, que nunca es múltiplo. Algebraicamente, $p_R(\lambda)=\lambda^2+1$, sin raíces reales.

**b)** $p_B(\lambda)=(\lambda-2)^2+1=\lambda^2-4\lambda+5$, con discriminante $16-20=-4<0$: no hay raíces reales.

**c)** No puede: $p_A$ tiene grado $3$, impar, y todo polinomio real de grado impar tiene al menos una raíz real (cambia de signo). Ejemplo: $\begin{pmatrix}0&-1&0\\1&0&0\\0&0&2\end{pmatrix}$ tiene $p(\lambda)=(\lambda^2+1)(\lambda-2)$, y su único autovalor real es $2$ (autovector $(0,0,1)$).

**Comprobación.** $p_R=\lambda^2+1$ (traza $0$, determinante $1$) y $p_B=\lambda^2-4\lambda+5$ (traza $4$, determinante $5$); en el ejemplo, $(\lambda^2+1)(\lambda-2)=\lambda^3-2\lambda^2+\lambda-2$.

:::tip[Resultado]
$p_R=\lambda^2+1$ y $p_B=\lambda^2-4\lambda+5$ no tienen raíces reales; en $\mathbb{R}^{3\times3}$ siempre hay un autovalor real.
:::

</details>

### Ejercicio 6 · Verdadero o falso sobre autovectores
<!-- ejercicio: U3.06 | nivel: inicial | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
Decidir si cada afirmación es verdadera o falsa y justificar ($A,B\in\mathbb{R}^{n\times n}$).

a) El vector nulo es autovector de toda matriz $A$.

b) Si $v$ es autovector de $A$ y de $B$, entonces $v$ es autovector de $A+B$.

c) Si $\lambda$ es autovalor de $A$ y $\mu$ es autovalor de $B$, entonces $\lambda+\mu$ es autovalor de $A+B$.
:::

<details>
<summary>Resolución</summary>

**a) Falsa.** Por definición un autovector es **no nulo**. (Es cierto que $A0=\lambda0$ para todo $\lambda$, pero eso no dice nada del autovalor.)

**b) Verdadera.** Si $Av=\lambda v$ y $Bv=\mu v$, entonces $(A+B)v=Av+Bv=(\lambda+\mu)v$ y $v\neq0$.

**c) Falsa.** Contraejemplo: $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ tiene autovalor $1$ y $B=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ tiene autovalor $1$, pero $A+B=I$ solo tiene el autovalor $1$ y $\lambda+\mu=2$ no lo es. El error de la afirmación es que los autovectores correspondientes ($(1,0)$ para $A$, $(0,1)$ para $B$) son distintos.

**Comprobación.** $p_{A+B}(\lambda)=(\lambda-1)^2$, que no se anula en $2$.

:::tip[Resultado]
a) F; b) V; c) F (contraejemplo $A=\operatorname{diag}(1,0)$, $B=\operatorname{diag}(0,1)$).
:::

</details>

### Ejercicio 7 · Propiedades de una matriz triangular
<!-- ejercicio: U3.07 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}2&5&-1\\0&3&4\\0&0&-1\end{pmatrix}$.

a) Hallar los autovalores de $A$ y verificar que su suma es $\operatorname{tr}(A)$ y su producto es $\det(A)$.

b) Hallar los autovalores de $A^{-1}$ y de $A^3+2I$.

c) Sea $q(x)=x^2-3x$. Decidir si $q(A)=A^2-3A$ es inversible.
:::

<details>
<summary>Resolución</summary>

**a)** En una matriz triangular los autovalores son las entradas diagonales: $2,\ 3,\ -1$. Suma: $4=\operatorname{tr}(A)=2+3-1$. Producto: $-6=\det(A)$ (producto de la diagonal).

**b)** Si $Av=\lambda v$ y $A$ es inversible ($\det A=-6\neq0$), entonces $A^{-1}v=\lambda^{-1}v$: autovalores $\tfrac12,\ \tfrac13,\ -1$. Además $(A^3+2I)v=(\lambda^3+2)v$: autovalores $10,\ 29,\ 1$.

**c)** Los autovalores de $q(A)$ son $q(2)=-2$, $q(3)=0$, $q(-1)=4$. Como aparece el autovalor $0$, $\det q(A)=0$ y $q(A)$ **no** es inversible.

**Comprobación.** $\det(A^{-1})=\tfrac12\cdot\tfrac13\cdot(-1)=-\tfrac16=1/\det A$. Calculando directamente, $q(A)=\begin{pmatrix}-2&10&22\\0&0&-4\\0&0&4\end{pmatrix}$ tiene las filas segunda y tercera proporcionales, luego $\det=0$.

:::tip[Resultado]
Autovalores de $A$: $2,3,-1$; de $A^{-1}$: $\tfrac12,\tfrac13,-1$; de $A^3+2I$: $10,29,1$; $q(A)$ no es inversible.
:::

</details>

### Ejercicio 8 · Una matriz de rango 1
<!-- ejercicio: U3.08 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}1&-1&2\\2&-2&4\\-1&1&-2\end{pmatrix}$.

a) Hallar $E_0(A)$ y su dimensión.

b) Hallar el otro autovalor y su autoespacio, usando la traza.

c) Decidir si $A$ es diagonalizable.
:::

<details>
<summary>Resolución</summary>

**a)** Las tres filas son múltiplos de $(1,-1,2)$, así que $\operatorname{rango}(A)=1$. $E_0=\operatorname{nul}(A)=\{x-y+2z=0\}$, con base $\{(1,1,0),(-2,0,1)\}$: $\dim E_0=3-1=2$, o sea $m_g(0)=2$.

**b)** La traza es $1-2-2=-3$. Como $0$ aporta dos veces, el tercer autovalor es $-3$ (y $m_a(0)\ge2$ obliga a $p_A=\lambda^2(\lambda+3)$). Para $\lambda=-3$: $A(1,2,-1)=(1-2-2,\ 2-4-4,\ -1+2+2)$, es decir $(-3,-6,3)=-3(1,2,-1)$, entonces $E_{-3}=\operatorname{gen}\{(1,2,-1)\}$.

**c)** Sí: $m_g(0)=2=m_a(0)$ y $m_g(-3)=1=m_a(-3)$; juntando las bases se obtienen $3$ autovectores independientes. Con $C=\begin{pmatrix}1&-2&1\\1&0&2\\0&1&-1\end{pmatrix}$ y $D=\operatorname{diag}(0,0,-3)$ vale $AC=CD$.

**Comprobación.** $A(1,1,0)=(0,0,0)$, $A(-2,0,1)=(-2+2,\ -4+4,\ 2-2)=0$ y $A(1,2,-1)=-3(1,2,-1)$, es decir $AC=CD$ columna a columna.

:::tip[Resultado]
$p_A=\lambda^2(\lambda+3)$; $E_0=\operatorname{gen}\{(1,1,0),(-2,0,1)\}$, $E_{-3}=\operatorname{gen}\{(1,2,-1)\}$; $A$ es diagonalizable.
:::

</details>
