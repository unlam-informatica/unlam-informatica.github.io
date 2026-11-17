---
title: Simulacro del segundo parcial
description: Simulacro original e integrador de tres horas sobre cambio de base, diagonalización, recurrencias, producto interno no usual y códigos duales, con resolución completa.
slug: algebra-ii/integradores/simulacro-2
sidebar:
  order: 2
  label: Simulacro 2
---

:::note[Sobre este simulacro]
Simulacro **original** preparado para este manual con los temas del segundo parcial del programa
2023, que es integrador. No es un examen tomado por la cátedra. Duración sugerida: **3 horas**.
Puntaje total: 10 puntos (2 por ejercicio). Todas las respuestas deben estar justificadas.
:::

Temas: transformaciones lineales y cambio de base
([2.7](/algebra-ii/unidad-2/teoria/cambio-de-base/)); autovalores, diagonalización y potencias
([Unidad 3](/algebra-ii/unidad-3/)); relaciones de recurrencia
([3.7](/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/)); producto interno, Gram-Schmidt,
complemento y proyección ([Unidad 4](/algebra-ii/unidad-4/)); códigos sobre $\mathbb{Z}_2$
([4.8](/algebra-ii/unidad-4/teoria/codigos-y-z2/)).

### Ejercicio 1 · Una simetría en una base adaptada
<!-- ejercicio: S2.1 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:\mathbb{R}^2\to\mathbb{R}^2$ la simetría (reflexión) respecto de la recta $L: y=2x$.

a) **(0,75)** Elegir una base $B$ de $\mathbb{R}^2$ en la que $M(T)_B$ sea diagonal y escribirla.

b) **(1)** Hallar $M(T)_E$ en la base canónica usando un cambio de base.

c) **(0,25)** Sin hacer cuentas, hallar los autovalores de $M(T)_E$ y decidir si es diagonalizable.
:::

<details>
<summary>Resolución</summary>

**a)** La simetría deja fijos los vectores de la recta y cambia de signo los perpendiculares a ella.
Tomamos $b_1=(1,2)\in L$ y $b_2=(-2,1)$, perpendicular a $L$ (producto escalar $-2+2=0$). Entonces
$T(b_1)=b_1$ y $T(b_2)=-b_2$, y en $B=\{b_1,b_2\}$:

$$
M(T)_B=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

**b)** Por la fórmula de cambio de base para un endomorfismo,
$M(T)_E=C_{BE}\,M(T)_B\,C_{EB}$, con $C_{BE}$ formada por los vectores de $B$ en columnas y
$C_{EB}=C_{BE}^{-1}$:

$$
C_{BE}=\begin{pmatrix}1&-2\\2&1\end{pmatrix},\qquad C_{EB}=\frac15\begin{pmatrix}1&2\\-2&1\end{pmatrix}.
$$

$$
M(T)_E=\begin{pmatrix}1&-2\\2&1\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\frac15\begin{pmatrix}1&2\\-2&1\end{pmatrix}
=\begin{pmatrix}1&2\\2&-1\end{pmatrix}\frac15\begin{pmatrix}1&2\\-2&1\end{pmatrix}
=\frac15\begin{pmatrix}-3&4\\4&3\end{pmatrix}.
$$

**Comprobación.** $\tfrac15(-3+8,\ 4+6)=(1,2)$ y $\tfrac15(6+4,\ -8+3)=(2,-1)$: la matriz fija $b_1$ y
cambia de signo a $b_2$.

**c)** $M(T)_E$ y $M(T)_B$ son semejantes, así que tienen los mismos autovalores: $1$ y $-1$. Es
diagonalizable porque $B$ es una base de autovectores (de hecho, $M(T)_E=C_{BE}\,D\,C_{BE}^{-1}$ es su
diagonalización).

:::tip[Resultado]
$B=\{(1,2),(-2,1)\}$, $M(T)_B=\operatorname{diag}(1,-1)$, $M(T)_E=\tfrac15\begin{pmatrix}-3&4\\4&3\end{pmatrix}$,
autovalores $\pm1$, diagonalizable.
:::

</details>

### Ejercicio 2 · Diagonalización con un parámetro
<!-- ejercicio: S2.2 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A_a=\begin{pmatrix}3&1&1\\0&2&a\\0&0&2\end{pmatrix}$, con $a\in\mathbb{R}$.

a) **(0,75)** Hallar los autovalores y decidir, según el valor de $a$, si $A_a$ es diagonalizable.

b) **(0,75)** Para $a=0$, hallar $C$ inversible y $D$ diagonal tales que $A_0=CDC^{-1}$.

c) **(0,5)** Decidir si $A_a^2-5A_a+6I=0$. Justificar para cada valor de $a$.
:::

<details>
<summary>Resolución</summary>

**a)** $A_a$ es triangular superior, así que $p(\lambda)=\det(\lambda I-A_a)=(\lambda-3)(\lambda-2)^2$.
Autovalores: $3$ con $m_a=1$ y $2$ con $m_a=2$. Para $\lambda=3$, $m_g=1=m_a$ siempre. Para $\lambda=2$:

$$
A_a-2I=\begin{pmatrix}1&1&1\\0&0&a\\0&0&0\end{pmatrix}.
$$

Si $a\neq0$, el rango es 2 y $m_g(2)=3-2=1<2$: **no es diagonalizable**. Si $a=0$, el rango es 1 y
$m_g(2)=2=m_a(2)$: **es diagonalizable**.

**b)** Con $a=0$:

- $E_3(A_0)=\operatorname{nul}(3I-A_0)$: $3I-A_0=\begin{pmatrix}0&-1&-1\\0&1&0\\0&0&1\end{pmatrix}$ da $y=z=0$:
  $E_3=\operatorname{gen}\{(1,0,0)\}$.
- $E_2(A_0)$: la ecuación es $x+y+z=0$, así que $E_2=\operatorname{gen}\{(1,-1,0),(1,0,-1)\}$.

$$
C=\begin{pmatrix}1&1&1\\0&-1&0\\0&0&-1\end{pmatrix},\qquad D=\begin{pmatrix}3&0&0\\0&2&0\\0&0&2\end{pmatrix}.
$$

**Comprobación.** $A_0C=\begin{pmatrix}3&2&2\\0&-2&0\\0&0&-2\end{pmatrix}=CD$, y $\det C=1\neq0$.

**c)** Observemos que $A_a^2-5A_a+6I=(A_a-3I)(A_a-2I)$.

- Si $a=0$, $A_0=CDC^{-1}$ y $(A_0-3I)(A_0-2I)=C(D-3I)(D-2I)C^{-1}$. El producto de las matrices
  diagonales $\operatorname{diag}(0,-1,-1)\operatorname{diag}(1,0,0)$ es nulo: **la igualdad vale**.
- Si $a\neq0$, calculando,

$$
(A_a-3I)(A_a-2I)=\begin{pmatrix}0&1&1\\0&-1&a\\0&0&-1\end{pmatrix}\begin{pmatrix}1&1&1\\0&0&a\\0&0&0\end{pmatrix}=\begin{pmatrix}0&0&a\\0&0&-a\\0&0&0\end{pmatrix}\neq0.
$$

  **La igualdad no vale.** Es coherente con a): si se anulara, todo vector se descompondría en
  autovectores de 3 y de 2, y $A_a$ sería diagonalizable.

:::tip[Resultado]
Diagonalizable si y solo si $a=0$; $A_0=CDC^{-1}$ con $C$ y $D$ como arriba; $A_a^2-5A_a+6I=0$ solo
para $a=0$.
:::

</details>

### Ejercicio 3 · Una recurrencia lineal
<!-- ejercicio: S2.3 | nivel: intermedio | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
El costo $a_n$ de un algoritmo recursivo cumple $a_{n+2}=a_{n+1}+6a_n$ para $n\ge0$, con $a_0=1$ y
$a_1=8$.

a) **(0,75)** Escribir la recurrencia en forma matricial $u_{n+1}=Mu_n$ con $u_n=(a_{n+1},a_n)^t$ y
diagonalizar $M$.

b) **(1)** Hallar el término general $a_n$ y comprobarlo para $n=2$ y $n=3$.

c) **(0,25)** Calcular $\displaystyle\lim_{n\to\infty}\frac{a_{n+1}}{a_n}$.
:::

<details>
<summary>Resolución</summary>

**a)** Como $a_{n+2}=a_{n+1}+6a_n$ y $a_{n+1}=a_{n+1}$,

$$
\begin{pmatrix}a_{n+2}\\a_{n+1}\end{pmatrix}=\underbrace{\begin{pmatrix}1&6\\1&0\end{pmatrix}}_{M}\begin{pmatrix}a_{n+1}\\a_n\end{pmatrix}.
$$

$p(\lambda)=\det(\lambda I-M)=\lambda(\lambda-1)-6=\lambda^2-\lambda-6=(\lambda-3)(\lambda+2)$. Dos autovalores
distintos: $M$ es diagonalizable. Autovectores: para $\lambda=3$, $3I-M=\begin{pmatrix}2&-6\\-1&3\end{pmatrix}$
da $x=3y$, vector $(3,1)$; para $\lambda=-2$, $-2I-M=\begin{pmatrix}-3&-6\\-1&-2\end{pmatrix}$ da $x=-2y$,
vector $(-2,1)$. Así $M=CDC^{-1}$ con $C=\begin{pmatrix}3&-2\\1&1\end{pmatrix}$ y $D=\operatorname{diag}(3,-2)$.

**b)** Como $u_n=M^nu_0=CD^nC^{-1}u_0$, cada componente es combinación de $3^n$ y $(-2)^n$:
$a_n=c_1\,3^n+c_2(-2)^n$. Con las condiciones iniciales:

$$
\begin{cases} c_1+c_2=1\\ 3c_1-2c_2=8\end{cases}\quad\Longrightarrow\quad c_1=2,\ c_2=-1.
$$

$$
a_n=2\cdot3^n-(-2)^n.
$$

**Comprobación.** Por la recurrencia, $a_2=8+6=14$ y $a_3=14+48=62$. Por la fórmula,
$a_2=18-4=14$ y $a_3=54+8=62$.

**c)** Dividiendo por $3^n$:
$\dfrac{a_{n+1}}{a_n}=\dfrac{6-(-2)\left(-\tfrac23\right)^n}{2-\left(-\tfrac23\right)^n}\to\dfrac{6}{2}=3$,
porque $\left|-\tfrac23\right|<1$. El autovalor dominante determina el crecimiento: $a_n$ crece como $3^n$.

:::tip[Resultado]
$a_n=2\cdot3^n-(-2)^n$ y el cociente tiende a 3.
:::

</details>

### Ejercicio 4 · Producto interno no usual, Gram-Schmidt y proyección
<!-- ejercicio: S2.4 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^3$ se considera $\langle x,y\rangle=x^tGy$ con
$G=\begin{pmatrix}1&0&1\\0&2&0\\1&0&2\end{pmatrix}$, es decir,
$\langle x,y\rangle=x_1y_1+x_1y_3+x_3y_1+2x_2y_2+2x_3y_3$. Sea $S=\operatorname{gen}\{(1,0,0),(0,1,1)\}$.

a) **(0,5)** Justificar que $\langle\,,\rangle$ es un producto interno.

b) **(0,5)** Hallar una base ortogonal de $S$.

c) **(0,5)** Hallar $S^\perp$.

d) **(0,5)** Hallar $\operatorname{proy}_S(v)$ y $d(v,S)$ para $v=(0,0,1)$.
:::

<details>
<summary>Resolución</summary>

**a)** La forma es bilineal (es $x^tGy$) y simétrica porque $G=G^t$. Falta la positividad. Completando
cuadrados,

$$
\langle x,x\rangle=x_1^2+2x_1x_3+2x_2^2+2x_3^2=(x_1+x_3)^2+2x_2^2+x_3^2\ \ge 0,
$$

y vale $0$ solo si $x_3=0$, $x_2=0$ y $x_1+x_3=0$, es decir, $x=0$. Es un producto interno.

**b)** Gram-Schmidt con $u_1=(1,0,0)$ y $u_2=(0,1,1)$: $\langle u_2,u_1\rangle=1$ (solo aporta el término
$x_3y_1$) y $\langle u_1,u_1\rangle=1$. Entonces

$$
w_2=u_2-\frac{\langle u_2,u_1\rangle}{\langle u_1,u_1\rangle}u_1=(0,1,1)-(1,0,0)=(-1,1,1).
$$

**Comprobación.** $\langle w_2,u_1\rangle=x_1y_1+x_3y_1=-1+1=0$. Base ortogonal:
$\{(1,0,0),(-1,1,1)\}$, con $\lVert w_2\rVert^2=\langle w_2,w_2\rangle=1-2+2+2=3$.

**c)** $x\in S^\perp$ si y solo si es ortogonal a los generadores de $S$:

$$
\langle x,(1,0,0)\rangle=x_1+x_3=0,\qquad \langle x,(0,1,1)\rangle=x_1+2x_2+2x_3=0.
$$

De la primera $x_1=-x_3$; reemplazando, $2x_2+x_3=0$. Con $x_2=t$: $x=(2t,\,t,\,-2t)$.
$S^\perp=\operatorname{gen}\{(2,1,-2)\}$, de dimensión $3-2=1$, como debe ser.

**d)** Con la base ortogonal de b):
$\langle v,u_1\rangle=1$ y $\langle v,w_2\rangle=-1+2=1$. Entonces

$$
\operatorname{proy}_S(v)=\frac{1}{1}(1,0,0)+\frac13(-1,1,1)=\left(\tfrac23,\tfrac13,\tfrac13\right).
$$

El residuo es $v-\operatorname{proy}_S(v)=\left(-\tfrac23,-\tfrac13,\tfrac23\right)=-\tfrac13(2,1,-2)\in S^\perp$
(comprobación de la ortogonalidad). Como $\lVert(2,1,-2)\rVert^2=4-8+2+8=6$,

$$
d(v,S)=\tfrac13\sqrt6=\frac{\sqrt6}{3}.
$$

**Comprobación (Pitágoras).** $\lVert v\rVert^2=2$, $\lVert\operatorname{proy}_S(v)\rVert^2=\tfrac43$ y
$d(v,S)^2=\tfrac23$; efectivamente $\tfrac43+\tfrac23=2$.

:::tip[Resultado]
Base ortogonal $\{(1,0,0),(-1,1,1)\}$; $S^\perp=\operatorname{gen}\{(2,1,-2)\}$;
$\operatorname{proy}_S(v)=\left(\tfrac23,\tfrac13,\tfrac13\right)$ y $d(v,S)=\tfrac{\sqrt6}{3}$.
:::

</details>

### Ejercicio 5 · Código dual y corrección de un error
<!-- ejercicio: S2.5 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C\subseteq\mathbb{Z}_2^6$ el código generado por las filas de

$$
G=\begin{pmatrix}1&0&0&0&1&1\\0&1&0&1&0&1\\0&0&1&1&1&0\end{pmatrix}.
$$

a) **(0,5)** Hallar una matriz $H$ de control de paridad y una base del código dual $\mathcal C^\perp$.

b) **(0,5)** Hallar la distancia mínima de $\mathcal C$ y decidir si $\mathcal C$ es autodual.

c) **(0,5)** Hallar $\mathcal C\cap\mathcal C^\perp$. ¿Puede ocurrir algo así con un subespacio $S$ de
$\mathbb{R}^n$ y su complemento ortogonal?

d) **(0,5)** Se recibe $v=(1,0,1,1,0,0)$. Suponiendo a lo sumo un error, corregirlo.
:::

<details>
<summary>Resolución</summary>

**a)** $G=(I_3\mid A)$ con $A=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$. La matriz
$H=(A^t\mid I_3)$ cumple $GH^t=A+A=0$ y tiene rango 3, así que $\mathcal C=\operatorname{nul}(H)$ (ambos
tienen dimensión 3 y $\mathcal C\subseteq\operatorname{nul}(H)$). Como $A^t=A$:

$$
H=\begin{pmatrix}0&1&1&1&0&0\\1&0&1&0&1&0\\1&1&0&0&0&1\end{pmatrix}.
$$

Las filas de $H$ son ortogonales a todas las filas de $G$ (eso dice $GH^t=0$), y $\mathcal C^\perp$ tiene
dimensión $6-3=3$; las tres filas de $H$, que son LI, forman una base de $\mathcal C^\perp$.

**b)** Las palabras no nulas de $\mathcal C$ son las sumas de filas de $G$:

| Combinación | Palabra | Peso |
|---|---|---|
| $g_1$ | 100011 | 3 |
| $g_2$ | 010101 | 3 |
| $g_3$ | 001110 | 3 |
| $g_1+g_2$ | 110110 | 4 |
| $g_1+g_3$ | 101101 | 4 |
| $g_2+g_3$ | 011011 | 4 |
| $g_1+g_2+g_3$ | 111000 | 3 |

En un código lineal la distancia mínima es el menor peso no nulo: $d(\mathcal C)=3$. Corrige un error.

No es autodual: en un código autodual toda palabra tiene peso par (porque $c\cdot c=w(c)\bmod 2$ debe
ser 0), y $g_1$ tiene peso 3. Equivalentemente, $g_1\cdot g_1=1\neq0$, así que $g_1\notin\mathcal C^\perp$.

**c)** Las palabras de $\mathcal C^\perp$ son las sumas de filas de $H$: 011100, 101010, 110001, 110110,
101101, 011011, 000111 y 000000. Comparando con la tabla:

$$
\mathcal C\cap\mathcal C^\perp=\{000000,\ 110110,\ 101101,\ 011011\},
$$

un subespacio de dimensión 2. Con un producto interno real esto es imposible: si $v\in S\cap S^\perp$,
entonces $\langle v,v\rangle=0$ y la positividad obliga a $v=0$. En $\mathbb{Z}_2^n$ el producto
$u\cdot v$ no es un producto interno (falla la positividad): las palabras de peso par son ortogonales
a sí mismas.

**d)** Síndrome:

$$
Hv^t=\begin{pmatrix}0+0+1+1+0+0\\1+0+1+0+0+0\\1+0+0+0+0+0\end{pmatrix}=\begin{pmatrix}0\\0\\1\end{pmatrix},
$$

que es la sexta columna de $H$. Corregimos la posición 6: $c=(1,0,1,1,0,1)=g_1+g_3\in\mathcal C$. El
mensaje enviado era $(1,0,1)$.

:::tip[Resultado]
$H=(A^t\mid I_3)$ como arriba; $d(\mathcal C)=3$; no es autodual;
$\mathcal C\cap\mathcal C^\perp$ tiene 4 palabras; $v$ se corrige a $(1,0,1,1,0,1)$.
:::

</details>
