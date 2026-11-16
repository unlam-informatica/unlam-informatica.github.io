---
title: Práctica — Guía integradora
description: Cinco problemas de varios ítems, al estilo de un parcial, que integran autovalores, diagonalización con parámetros, endomorfismos, recurrencias y cadenas de Markov, con puntaje orientativo y resolución completa.
slug: algebra-ii/unidad-3/practica/guia-integradora
sidebar:
  order: 4
  label: Guía integradora
---

:::note[Cómo usar esta página]
Cinco problemas **originales** de varios ítems, con el formato y el nivel de un parcial de la unidad. Cada
problema vale **10 puntos orientativos**, repartidos por ítem (entre paréntesis); no son los de ningún examen
tomado por la cátedra. Sugerencia: resolvé uno en unos 25 minutos, con todas las respuestas justificadas y sin mirar la
resolución, y recién después corregite con ella.

**Presupone:** toda la teoría de la unidad,
[3.1 Autovalores y autovectores](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/),
[3.2 Polinomio característico](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/),
[3.3 Propiedades](/algebra-ii/unidad-3/teoria/propiedades/),
[3.4 Matrices semejantes](/algebra-ii/unidad-3/teoria/matrices-semejantes/),
[3.5 Diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/),
[3.6 Potencias](/algebra-ii/unidad-3/teoria/potencias/),
[3.7 Relaciones de recurrencia](/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/) y
[3.8 Cadenas de Markov](/algebra-ii/unidad-3/teoria/cadenas-de-markov/). Para el cambio de base de un
endomorfismo, ver [2.7 Cambio de base](/algebra-ii/unidad-2/teoria/cambio-de-base/).
:::

### Ejercicio 27 · Matriz con un parámetro
<!-- ejercicio: U3.27 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A_k=\begin{pmatrix}k&0&1\\0&2&0\\0&0&2\end{pmatrix}$ con $k\in\mathbb{R}$.

a) **(1)** Hallar el polinomio característico y los autovalores con sus multiplicidades algebraicas.

b) **(3)** Determinar para qué valores de $k$ es $A_k$ diagonalizable.

c) **(3)** Para $k=3$ hallar $C$ y $D$ tales que $A_3=CDC^{-1}$.

d) **(2)** Para $k=3$ hallar una fórmula para $A_3^n$, $n\in\mathbb{N}$.

e) **(1)** Para $k=3$, decidir para qué $n\in\mathbb{N}$ la matriz $A_3^n-4I$ es inversible.
:::

<details>
<summary>Resolución</summary>

**a)** $A_k$ es triangular superior: $p_{A_k}(\lambda)=(\lambda-k)(\lambda-2)^2$. Si $k\neq2$: autovalores $k$ (simple) y $2$ (doble). Si $k=2$: $2$ con $m_a=3$.

**b)** Para $k\neq2$ el autovalor $k$ es simple y solo hay que mirar $\lambda=2$:
$$
2I-A_k=\begin{pmatrix}2-k&0&-1\\0&0&0\\0&0&0\end{pmatrix}
$$
tiene rango $1$ (la primera fila no es nula por el $-1$), de modo que $m_g(2)=2=m_a(2)$: diagonalizable. Para $k=2$ la matriz $2I-A_2=\begin{pmatrix}0&0&-1\\0&0&0\\0&0&0\end{pmatrix}$ tiene rango $1$, $m_g(2)=2<3=m_a(2)$: no diagonalizable. **Respuesta: $k\neq2$.**

**c)** Con $k=3$: $3I-A_3=\begin{pmatrix}0&0&-1\\0&1&0\\0&0&1\end{pmatrix}$ da $z=0$, $y=0$: $E_3=\operatorname{gen}\{(1,0,0)\}$. $2I-A_3=\begin{pmatrix}-1&0&-1\\0&0&0\\0&0&0\end{pmatrix}$ da $x+z=0$: $E_2=\operatorname{gen}\{(0,1,0),(1,0,-1)\}$. Entonces
$$
C=\begin{pmatrix}1&0&1\\0&1&0\\0&0&-1\end{pmatrix},\qquad D=\operatorname{diag}(3,2,2),\qquad C^{-1}=\begin{pmatrix}1&0&1\\0&1&0\\0&0&-1\end{pmatrix}.
$$

**d)** $A_3^n=CD^nC^{-1}=\begin{pmatrix}3^n&0&2^n\\0&2^n&0\\0&0&-2^n\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&0\\0&0&-1\end{pmatrix}$, es decir
$$
A_3^n=\begin{pmatrix}3^n&0&3^n-2^n\\0&2^n&0\\0&0&2^n\end{pmatrix}.
$$

**e)** Los autovalores de $A_3^n-4I$ son $3^n-4$ y $2^n-4$. El primero nunca es $0$ ($3^n=4$ no tiene solución natural); el segundo se anula si y solo si $n=2$. Por lo tanto es inversible si y solo si $n\neq2$.

**Comprobación.** $AC=CD$: $A_3(1,0,0)=3(1,0,0)$, $A_3(0,1,0)=2(0,1,0)$, $A_3(1,0,-1)=(3-1,0,-2)=2(1,0,-1)$. La fórmula de d) da $A_3$ para $n=1$ y $A_3^2$ con entrada $(1,3)=9-4=5$, que coincide con $3\cdot1+1\cdot2=5$.

:::tip[Resultado]
$p=(\lambda-k)(\lambda-2)^2$; diagonalizable si y solo si $k\neq2$; $D=\operatorname{diag}(3,2,2)$; $A_3^n=\begin{pmatrix}3^n&0&3^n-2^n\\0&2^n&0\\0&0&2^n\end{pmatrix}$; $A_3^n-4I$ es inversible si y solo si $n\neq2$.
:::

</details>

### Ejercicio 28 · Un operador sobre polinomios
<!-- ejercicio: U3.28 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:P_2[\mathbb{R}]\toP_2[\mathbb{R}]$ la transformación lineal $T(p)=(x+1)\,p'(x)$, donde $p'$ es la derivada, y sea $B=\{1,x,x^2\}$.

a) **(2)** Hallar $M(T)_B$.

b) **(3)** Hallar los autovalores de $T$ y los autovectores correspondientes (como polinomios).

c) **(2)** Probar que $T$ es diagonalizable, dar una base $B'$ de $P_2[\mathbb{R}]$ y la matriz $M(T)_{B'}$.

d) **(3)** Calcular $T^n(x^2)$ para $n\in\mathbb{N}$ usando $B'$.
:::

<details>
<summary>Resolución</summary>

**a)** $T(1)=0$, $T(x)=x+1$, $T(x^2)=(x+1)2x=2x^2+2x$. Las columnas son las coordenadas respecto de $B$:
$$
M(T)_B=\begin{pmatrix}0&1&0\\0&1&2\\0&0&2\end{pmatrix}.
$$

**b)** La matriz es triangular: $p(\lambda)=\lambda(\lambda-1)(\lambda-2)$, con autovalores $0,1,2$.
- $\lambda=0$: $(0,0,0)$ ya muestra $E_0=\operatorname{gen}\{(1,0,0)\}$, es decir el polinomio $1$.
- $\lambda=1$: $(M-I)v=0$ da $z=0$, $x=y$: $v=(1,1,0)\leftrightarrow 1+x$.
- $\lambda=2$: $(M-2I)v=0$ da $-y+2z=0$ y $-2x+y=0$: $v=(1,2,1)\leftrightarrow1+2x+x^2=(1+x)^2$.

**c)** Tres autovalores distintos en un espacio de dimensión $3$: es diagonalizable, y $B'=\{1,\ 1+x,\ (1+x)^2\}$ es una base de autovectores, con
$$
M(T)_{B'}=\operatorname{diag}(0,1,2).
$$

**d)** Escribimos $x^2$ en $B'$: $x^2=1-2(1+x)+(1+x)^2$. Aplicando $T^n$, que multiplica cada autovector por $\lambda^n$,
$$
T^n(x^2)=0^n\cdot1-2\cdot1^n(1+x)+2^n(1+x)^2=-2(1+x)+2^n(1+x)^2\qquad(n\ge1).
$$

**Comprobación.** $T(1+x)=(x+1)\cdot1$ y $T((1+x)^2)=(x+1)\cdot2(1+x)=2(1+x)^2$. Para $n=1$: $-2-2x+2(1+2x+x^2)=2x+2x^2=T(x^2)$. Y la traza $3=0+1+2$.

:::tip[Resultado]
$M(T)_B=\begin{pmatrix}0&1&0\\0&1&2\\0&0&2\end{pmatrix}$; autovalores $0,1,2$ con autovectores $1$, $1+x$, $(1+x)^2$; $T^n(x^2)=-2(1+x)+2^n(1+x)^2$ para $n\ge1$.
:::

</details>

### Ejercicio 29 · Recurrencia, matriz compañera e inversibilidad
<!-- ejercicio: U3.29 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
El costo $a_n$ de un algoritmo recursivo cumple $a_{n+1}=2a_n+3a_{n-1}$ para $n\ge1$, con $a_0=2$ y $a_1=2$.

a) **(2)** Escribir la forma matricial, con $x_n=(a_{n+1},a_n)$ y la matriz compañera $A$, y hallar los autovalores de $A$.

b) **(3)** Hallar una fórmula cerrada para $a_n$ y calcular $a_{10}$.

c) **(2)** Calcular $\lim_{n\to\infty}a_{n+1}/a_n$ e interpretarlo.

d) **(3)** Decidir si $A-2I$ es inversible y para qué $k\in\mathbb{N}$ es inversible $A^k-I$.
:::

<details>
<summary>Resolución</summary>

**a)** $x_n=Ax_{n-1}$ con $A=\begin{pmatrix}2&3\\1&0\end{pmatrix}$ y $x_0=(2,2)$. $p_A=\lambda^2-2\lambda-3=(\lambda-3)(\lambda+1)$: autovalores $3$ y $-1$, con $E_3=\operatorname{gen}\{(3,1)\}$ y $E_{-1}=\operatorname{gen}\{(-1,1)\}$.

**b)** $x_0=\alpha(3,1)+\beta(-1,1)$ da $3\alpha-\beta=2$ y $\alpha+\beta=2$, luego $\alpha=\beta=1$. Entonces $x_n=3^n(3,1)+(-1)^n(-1,1)$ y la segunda coordenada es
$$
a_n=3^n+(-1)^n,\qquad a_{10}=59049+1=59050.
$$

**c)** $\dfrac{a_{n+1}}{a_n}=\dfrac{3^{n+1}+(-1)^{n+1}}{3^n+(-1)^n}=\dfrac{3-(-1/3)^n}{1+(-1/3)^n}\longrightarrow3$. El autovalor dominante $3$ gobierna el crecimiento: el costo se multiplica casi por $3$ al pasar de $n$ a $n+1$.

**d)** Los autovalores de $A-2I$ son $3-2=1$ y $-1-2=-3$: no hay $0$, es inversible. Los de $A^k-I$ son $3^k-1\neq0$ (para $k\ge1$) y $(-1)^k-1$, que es $0$ si y solo si $k$ es par. Entonces $A^k-I$ es inversible si y solo si $k$ es impar.

**Comprobación.** Por la recurrencia: $2,2,10,26,82,242,\ldots$; la fórmula da $a_2=9+1=10$, $a_3=27-1=26$, $a_4=82$. $\det(A-2I)=\det\begin{pmatrix}0&3\\1&-2\end{pmatrix}=-3=1\cdot(-3)$.

:::tip[Resultado]
$a_n=3^n+(-1)^n$, $a_{10}=59050$; el cociente tiende a $3$; $A-2I$ es inversible y $A^k-I$ lo es si y solo si $k$ es impar.
:::

</details>

### Ejercicio 30 · Usuarios de una aplicación
<!-- ejercicio: U3.30 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Cada semana, un usuario de una aplicación está **Inactivo** (I), es **Ocasional** (O) o es **Frecuente** (F). Las probabilidades de cambio semanal son: desde I: $0{,}5$ a I, $0{,}3$ a O, $0{,}2$ a F; desde O: $0{,}1$ a I, $0{,}7$ a O, $0{,}2$ a F; desde F: $0{,}3$ a I, $0{,}3$ a O, $0{,}4$ a F.

a) **(1)** Escribir la matriz $P$ de transición (orden I, O, F) y justificar que la cadena es regular.

b) **(3)** Hallar el vector estacionario.

c) **(2)** Hallar los autovalores de $P$ y justificar la convergencia $P^kx_0\to\pi$.

d) **(2)** Si la aplicación tiene $2000$ usuarios, ¿cuántos se espera en cada estado a largo plazo?

e) **(2)** Verdadero o falso: "si todos los usuarios empiezan Frecuentes, el reparto a largo plazo es distinto que si todos empiezan Inactivos". Justificar.
:::

<details>
<summary>Resolución</summary>

**a)**
$$
P=\frac1{10}\begin{pmatrix}5&1&3\\3&7&3\\2&2&4\end{pmatrix}.
$$
Las columnas suman $1$ y todas las entradas son positivas, así que $P$ ya es regular ($P^1>0$).

**b)** $(I-P)x=0$: $\tfrac1{10}\begin{pmatrix}5&-1&-3\\-3&3&-3\\-2&-2&6\end{pmatrix}x=0$. De la segunda fila, $-3x+3y-3z=0\Rightarrow y=x+z$; de la primera, $5x-y-3z=0\Rightarrow4x-4z=0\Rightarrow x=z$. Entonces $y=2x$ y $x=(1,2,1)$, que normalizado es
$$
\pi=\left(\tfrac14,\ \tfrac12,\ \tfrac14\right).
$$

**c)** $p_P(\lambda)=\lambda^3-\tfrac85\lambda^2+\tfrac{17}{25}\lambda-\tfrac2{25}=(\lambda-1)(\lambda-\tfrac25)(\lambda-\tfrac15)$, con autovectores $(1,2,1)$, $(-1,1,0)$ y $(-1,0,1)$. Con $C=\begin{pmatrix}1&-1&-1\\2&1&0\\1&0&1\end{pmatrix}$ y $D=\operatorname{diag}(1,\tfrac25,\tfrac15)$, $P^k=CD^kC^{-1}\to C\operatorname{diag}(1,0,0)C^{-1}$ porque $(2/5)^k,(1/5)^k\to0$. Para cualquier distribución inicial $x_0$ (suma $1$), $P^kx_0\to\pi$.

**d)** $2000\cdot\left(\tfrac14,\tfrac12,\tfrac14\right)=(500,\ 1000,\ 500)$.

**e)** **Falso.** El límite no depende del estado inicial: $P^kx_0\to\pi$ para $x_0=(0,0,1)$ y para $x_0=(1,0,0)$. Cambia solo el camino (la rapidez con que se acerca), no el destino.

**Comprobación.** $P\pi=\tfrac1{10}\left(\tfrac54+\tfrac12+\tfrac34,\ \tfrac34+\tfrac72+\tfrac34,\ \tfrac12+1+1\right)=\tfrac1{10}\left(\tfrac52,5,\tfrac52\right)=\pi$. También $P(-1,1,0)=\tfrac1{10}(-4,4,0)=\tfrac25(-1,1,0)$ y $P(-1,0,1)=\tfrac1{10}(-2,0,2)=\tfrac15(-1,0,1)$.

:::tip[Resultado]
$\pi=(\tfrac14,\tfrac12,\tfrac14)$; autovalores $1,\tfrac25,\tfrac15$; $(500,1000,500)$ usuarios; el límite no depende del estado inicial.
:::

</details>

### Ejercicio 31 · Datos de traza, determinante y autovector
<!-- ejercicio: U3.31 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $A=\begin{pmatrix}-2&-2&6\\-1&1&2\\-1&-1&4\end{pmatrix}$.

a) **(1)** Verificar que $(1,1,1)$ es autovector de $A$ y hallar su autovalor.

b) **(2)** Calcular $\operatorname{tr}(A)$ y $\det(A)$ y, con la información de a), hallar todos los autovalores de $A$ sin calcular $p_A$ completo.

c) **(3)** Hallar los autoespacios y decidir si $A$ es diagonalizable.

d) **(2)** Decidir si $A$ es semejante a $\operatorname{diag}(2,2,-1)$ y hallar los autovalores de $A^{-1}$.

e) **(2)** Decidir si $A^2-A-2I$ es inversible y si es la matriz nula.
:::

<details>
<summary>Resolución</summary>

**a)** Las tres filas suman $2$: $A(1,1,1)=(2,2,2)$. El autovalor es $2$.

**b)** $\operatorname{tr}(A)=-2+1+4=3$ y $\det(A)=-4$. Sean $2,\mu,\nu$ los autovalores: $\mu+\nu=3-2=1$ y $2\mu\nu=-4$, es decir $\mu\nu=-2$. Entonces $\mu,\nu$ son raíces de $t^2-t-2=(t-2)(t+1)$: son $2$ y $-1$. Los autovalores son $2$ (con $m_a=2$) y $-1$ (con $m_a=1$): $p_A=(\lambda-2)^2(\lambda+1)$.

**c)** $2I-A=\begin{pmatrix}4&2&-6\\1&1&-2\\1&1&-2\end{pmatrix}$ tiene rango $2$ (dos filas independientes), entonces $E_2=\operatorname{gen}\{(1,1,1)\}$ y $m_g(2)=1<2$. Para $\lambda=-1$: $-I-A=\begin{pmatrix}1&2&-6\\1&-2&-2\\1&1&-5\end{pmatrix}$ da $E_{-1}=\operatorname{gen}\{(4,1,1)\}$. **$A$ no es diagonalizable.**

**d)** No: $\operatorname{diag}(2,2,-1)$ es diagonalizable y $A$ no lo es, y una matriz semejante a una diagonalizable también lo es (equivalentemente, $m_g(2)$ vale $2$ para la diagonal y $1$ para $A$). $A$ es inversible ($\det=-4$) y los autovalores de $A^{-1}$ son $\tfrac12$ (doble) y $-1$.

**e)** Los autovalores de $q(A)=A^2-A-2I$ son $q(2)=0$ y $q(-1)=0$: no es inversible. Sin embargo **no es la matriz nula**: $q(A)=(A-2I)(A+I)=\begin{pmatrix}0&-2&2\\0&-2&2\\0&-2&2\end{pmatrix}\neq0$. (Si $A$ fuera diagonalizable, $q(A)=0$; acá falla porque el autovalor $2$ es defectuoso.)

**Comprobación.** $A(4,1,1)=(-8-2+6,\ -4+1+2,\ -4-1+4)=(-4,-1,-1)=-(4,1,1)$. La traza $3=2+2-1$ y $\det=2\cdot2\cdot(-1)=-4$.

:::tip[Resultado]
Autovalor $2$ (doble, $m_g=1$) y $-1$; $A$ no es diagonalizable ni semejante a $\operatorname{diag}(2,2,-1)$; $A^{-1}$ tiene autovalores $\tfrac12,\tfrac12,-1$; $A^2-A-2I\neq0$ es singular.
:::

</details>
