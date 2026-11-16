---
title: Práctica — Nivel intermedio
description: Diez ejercicios de la Unidad 1 sobre subespacios de matrices y polinomios, generadores y ecuaciones, contraejemplos, parámetros, bases, cambio de coordenadas y códigos sobre ℤ₂, con resolución completa.
slug: algebra-ii/unidad-1/practica/nivel-intermedio
sidebar:
  order: 2
  label: Nivel intermedio
---

## Cómo usar esta página

Los ejercicios 9 a 18 combinan varias herramientas en un mismo problema: subespacios de $\mathbb{R}^{2\times2}$
y $P_2[\mathbb{R}]$, pasaje entre generadores y ecuaciones, contraejemplos, un parámetro, cambio de
coordenadas y códigos. Los enunciados son **originales** de este manual. Intentá cada ejercicio por tu
cuenta, abrí la resolución para contrastar el método y repetí la comprobación final.

Lecciones que se presuponen (la numeración continúa la de la página
[Nivel inicial](/algebra-ii/unidad-1/practica/nivel-inicial/)):

- [1.3 Subespacios](/algebra-ii/unidad-1/teoria/subespacios/) y
  [1.4 Combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/) (ejercicios 9, 10, 11 y 17).
- [1.5 Independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/) (ejercicio 12).
- [1.7 Base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/) (ejercicios 13 y 16).
- [1.8 Coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/) y
  [1.9 Cambio de coordenadas](/algebra-ii/unidad-1/teoria/cambio-de-coordenadas/) (ejercicios 14 y 15).
- [1.10 Códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/) (ejercicios 16 y 18).

Seguí con el [Nivel avanzado](/algebra-ii/unidad-1/practica/nivel-avanzado/).

### Ejercicio 9 · Un subespacio de matrices $2\times2$
<!-- ejercicio: U1.09 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $S=\{A\in\mathbb{R}^{2\times2}:\ a_{11}+a_{22}=0\ \text{ y }\ a_{12}=2a_{21}\}$.

a) Probar que $S$ es un subespacio de $\mathbb{R}^{2\times2}$.

b) Hallar una base de $S$ y su dimensión.

c) Decidir si $M=\begin{pmatrix}3&4\\2&-3\end{pmatrix}$ y $N=\begin{pmatrix}1&2\\1&1\end{pmatrix}$ pertenecen a
$S$ y, si corresponde, dar sus coordenadas en la base hallada.
:::

<details>
<summary>Resolución</summary>

**a)** Criterio de las tres condiciones.

- La matriz nula cumple $0+0=0$ y $0=2\cdot0$: $0\in S$.
- Si $A,A'\in S$: $(a_{11}+a'_{11})+(a_{22}+a'_{22})=0+0=0$ y $a_{12}+a'_{12}=2a_{21}+2a'_{21}=2(a_{21}+a'_{21})$:
  $A+A'\in S$.
- Si $A\in S$ y $\lambda\in\mathbb{R}$: $\lambda a_{11}+\lambda a_{22}=0$ y $\lambda a_{12}=2(\lambda a_{21})$:
  $\lambda A\in S$.

**b)** Escribimos $a_{11}=a$, $a_{21}=c$; entonces $a_{22}=-a$ y $a_{12}=2c$:

$$
A=\begin{pmatrix}a&2c\\c&-a\end{pmatrix}=a\begin{pmatrix}1&0\\0&-1\end{pmatrix}+c\begin{pmatrix}0&2\\1&0\end{pmatrix}.
$$

Los dos generadores son linealmente independientes (uno tiene $a_{12}=0$ y el otro no es nulo allí; ninguno es
múltiplo del otro). Base $B=\{\begin{pmatrix}1&0\\0&-1\end{pmatrix},\begin{pmatrix}0&2\\1&0\end{pmatrix}\}$,
$\dim S=2$.

**c)** Para $M$: $3+(-3)=0$ y $4=2\cdot2$: $M\in S$, con $a=3$, $c=2$, o sea $[M]_B=(3,2)^t$.
**Comprobación:** $3\begin{pmatrix}1&0\\0&-1\end{pmatrix}+2\begin{pmatrix}0&2\\1&0\end{pmatrix}=\begin{pmatrix}3&4\\2&-3\end{pmatrix}$.
Para $N$: $1+1=2\neq0$, luego $N\notin S$.

:::tip[Resultado]
$S$ es subespacio de dimensión $2$ con la base $B$ indicada; $M\in S$ con $[M]_B=(3,2)^t$ y $N\notin S$.
:::

</details>

### Ejercicio 10 · De generadores a ecuaciones y viceversa en ℝ⁴
<!-- ejercicio: U1.10 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^4$ sea $S=\operatorname{gen}\{(1,0,1,2),\ (0,1,-1,1),\ (1,1,0,3)\}$ y
$T=\{(x,y,z,w):\ x+y-z=0,\ y-2w=0\}$.

a) Hallar una base de $S$ y ecuaciones implícitas de $S$.

b) Hallar una base de $T$.

c) Hallar $S\cap T$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para pasar de generadores a ecuaciones se escribe el vector genérico y se eliminan los
parámetros; de ecuaciones a generadores se resuelve el sistema homogéneo.

**a)** Los generadores son $v_1,v_2,v_3$ con $v_3=(1,1,0,3)=v_1+v_2$, de modo que $v_3$ sobra:
$S=\operatorname{gen}\{v_1,v_2\}$, y $v_1,v_2$ son independientes (no proporcionales). Base
$\{(1,0,1,2),(0,1,-1,1)\}$, $\dim S=2$.

Un vector genérico es $a v_1+b v_2=(a,\ b,\ a-b,\ 2a+b)$. Con $x=a$ e $y=b$ resulta $z=x-y$ y $w=2x+y$:

$$
S:\ \begin{cases}x-y-z=0\\ 2x+y-w=0.\end{cases}
$$

**Comprobación:** $v_1$: $1-0-1=0$ y $2+0-2=0$; $v_2$: $0-1+1=0$ y $0+1-1=0$.

**b)** En $T$, $y=2w$ y $x=z-y=z-2w$, con $z,w$ libres:

$$
(x,y,z,w)=z(1,0,1,0)+w(-2,2,0,1).
$$

Base de $T$: $\{(1,0,1,0),(-2,2,0,1)\}$, $\dim T=2$. **Comprobación:** $(-2,2,0,1)$: $-2+2-0=0$ y $2-2=0$.

**c)** Un elemento de $S$ es $(a,b,a-b,2a+b)$. Imponemos las ecuaciones de $T$: la primera da
$a+b-(a-b)=2b=0$, o sea $b=0$; la segunda da $b-2(2a+b)=-4a-b=0$ y con $b=0$, $a=0$. Luego
$S\cap T=\{0\}$.

**Comprobación:** los cuatro vectores $(1,0,1,2),(0,1,-1,1),(1,0,1,0),(-2,2,0,1)$ tienen rango $4$, de modo que
$S$ y $T$ juntos generan $\mathbb{R}^4$.

:::tip[Resultado]
$S:\ x-y-z=0,\ 2x+y-w=0$, $\dim S=2$; $\dim T=2$ con base $\{(1,0,1,0),(-2,2,0,1)\}$; $S\cap T=\{0\}$.
:::

</details>

### Ejercicio 11 · Tres contraejemplos
<!-- ejercicio: U1.11 | nivel: intermedio | tipo: contraejemplo | verificacion: sympy -->

:::note[Enunciado]
Mostrar con un contraejemplo explícito que cada afirmación es falsa.

a) Si $\{u,v,w\}$ es linealmente dependiente, entonces $w\in\operatorname{gen}\{u,v\}$.

b) La unión de dos subespacios de $V$ es un subespacio de $V$.

c) Si $A,B\in\mathbb{R}^{2\times2}$ tienen rango $1$, entonces $A+B$ tiene rango $1$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un contraejemplo es un caso concreto que cumple la hipótesis y no la conclusión; hay que
verificar **las dos cosas**.

**a)** Sean $u=(1,0)$, $v=(2,0)$, $w=(0,1)$ en $\mathbb{R}^2$. Hipótesis: $v-2u=0$ es una combinación
no trivial nula, luego $\{u,v,w\}$ es dependiente. Conclusión: $\operatorname{gen}\{u,v\}$ es el eje $x$ y
$w=(0,1)$ no está en él. La dependencia no involucra a $w$.

**b)** $S=\operatorname{gen}\{(1,0)\}$ y $T=\operatorname{gen}\{(0,1)\}$ son subespacios de $\mathbb{R}^2$
(los ejes). $(1,0)\in S\cup T$ y $(0,1)\in S\cup T$, pero $(1,0)+(0,1)=(1,1)\notin S\cup T$: no es cerrado
por la suma.

**c)** $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ y $B=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ tienen rango $1$
(una fila no nula), pero $A+B=I$ tiene rango $2$.

**Comprobación.** a) $v=2u$ y $\det\begin{pmatrix}1&0\\2&0\end{pmatrix}=0$ pero
$\operatorname{rango}\begin{pmatrix}1&2&0\\0&0&1\end{pmatrix}=2$; b) $(1,1)$ no tiene una coordenada nula;
c) $\det I=1\neq0$.

:::tip[Resultado]
Los tres contraejemplos: $\{(1,0),(2,0),(0,1)\}$; los ejes coordenados de $\mathbb{R}^2$; $E_{11}$ y $E_{22}$.
:::

</details>

### Ejercicio 12 · Una base de polinomios con parámetro
<!-- ejercicio: U1.12 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $k\in\mathbb{R}$ sean $p_1=1+x$, $p_2=1+kx^2$, $p_3=k+x^2$ en $P_2[\mathbb{R}]$.

a) Hallar los valores de $k$ para los que $\{p_1,p_2,p_3\}$ es una base de $P_2[\mathbb{R}]$.

b) Para cada valor de $k$ que no sirva, hallar la dimensión de $\operatorname{gen}\{p_1,p_2,p_3\}$ y una
relación de dependencia.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Como $\dim P_2[\mathbb{R}]=3$, tres polinomios forman una base si y solo si son
independientes, y eso se decide con el determinante de la matriz de coordenadas en $E=\{1,x,x^2\}$.

**a)** Las coordenadas son $[p_1]_E=(1,1,0)^t$, $[p_2]_E=(1,0,k)^t$, $[p_3]_E=(k,0,1)^t$. Desarrollando por la
segunda fila:

$$
\det\begin{pmatrix}1&1&k\\1&0&0\\0&k&1\end{pmatrix}=-1\cdot\det\begin{pmatrix}1&k\\k&1\end{pmatrix}=-(1-k^2)=k^2-1.
$$

Es base si y solo si $k^2-1\neq0$, es decir $k\neq1$ y $k\neq-1$.

**b)** Si $k=1$: $p_2=p_3=1+x^2$, entonces $p_2-p_3=0$. Los polinomios $p_1$ y $p_2$ son independientes
(no proporcionales), así que la dimensión del generado es $2$.

Si $k=-1$: $p_2=1-x^2$ y $p_3=-1+x^2=-p_2$, entonces $p_2+p_3=0$ y otra vez $\dim=2$.

**Comprobación:** para $k=2$, $\det=3\neq0$ (base); para $k=0$, $\det=-1\neq0$ (base).

:::tip[Resultado]
Base si y solo si $k\neq\pm1$. Para $k=\pm1$ el generado tiene dimensión $2$, con $p_2-p_3=0$ ($k=1$) o
$p_2+p_3=0$ ($k=-1$).
:::

</details>

### Ejercicio 13 · Extender a una base en ℝ⁴ y en ℤ₂⁴
<!-- ejercicio: U1.13 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) Probar que $v_1=(1,2,0,1)$ y $v_2=(0,1,1,-1)$ son linealmente independientes en $\mathbb{R}^4$ y extender
$\{v_1,v_2\}$ a una base de $\mathbb{R}^4$ agregando vectores canónicos.

b) Hacer lo mismo con $w_1=(1,1,0,0)$ y $w_2=(0,1,1,0)$ en $\mathbb{Z}_2^4$ y decir cuántos elementos tiene
$\operatorname{gen}\{w_1,w_2\}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Agregar vectores canónicos hasta completar $4$ vectores y comprobar la independencia con un
determinante (en $\mathbb{R}$) o por escalonamiento (en $\mathbb{Z}_2$).

**a)** $v_1$ y $v_2$ no son proporcionales (la primera coordenada de $v_2$ es $0$ y la de $v_1$ no), luego son
independientes. Probamos con $e_3=(0,0,1,0)$ y $e_4=(0,0,0,1)$. La matriz con columnas
$v_1,v_2,e_3,e_4$ es

$$
\begin{pmatrix}1&0&0&0\\2&1&0&0\\0&1&1&0\\1&-1&0&1\end{pmatrix},
$$

triangular inferior, con determinante $1\cdot1\cdot1\cdot1=1\neq0$. Los cuatro vectores son independientes y,
como $\dim\mathbb{R}^4=4$, $\{v_1,v_2,e_3,e_4\}$ es una base.

**b)** $w_1,w_2$ son independientes (distintos y no nulos; en $\mathbb{Z}_2$ el único múltiplo no nulo de un
vector es él mismo). Con $e_3,e_4$ la matriz de columnas $w_1,w_2,e_3,e_4$ es

$$
\begin{pmatrix}1&0&0&0\\1&1&0&0\\0&1&1&0\\0&0&0&1\end{pmatrix},
$$

triangular inferior con determinante $1$ (que es no nulo en $\mathbb{Z}_2$): base de $\mathbb{Z}_2^4$.
El generado $\operatorname{gen}\{w_1,w_2\}$ tiene dimensión $2$ y $2^2=4$ elementos:
$0000,\ 1100,\ 0110,\ 1010$.

**Comprobación de b):** $w_1+w_2=(1,0,1,0)$ y $e_3,e_4\notin\operatorname{gen}\{w_1,w_2\}$.

:::tip[Resultado]
$\{v_1,v_2,e_3,e_4\}$ es base de $\mathbb{R}^4$; $\{w_1,w_2,e_3,e_4\}$ es base de $\mathbb{Z}_2^4$ y
$\operatorname{gen}\{w_1,w_2\}$ tiene $4$ elementos.
:::

</details>

### Ejercicio 14 · Cambio de coordenadas entre dos bases de ℝ³
<!-- ejercicio: U1.14 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $B=\{(1,1,0),(0,1,0),(1,1,1)\}$ y $B'=\{(1,1,1),(0,1,1),(0,0,1)\}$, bases de $\mathbb{R}^3$.

a) Hallar $C_{BB'}$.

b) Si $[v]_B=(2,-1,3)^t$, hallar $[v]_{B'}$ y $v$.

c) Hallar $C_{B'B}$ y verificar que es la inversa de $C_{BB'}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las columnas de $C_{BB'}$ son las coordenadas en $B'$ de cada vector de $B$. Si $P_B$ y
$P_{B'}$ son las matrices cuyas columnas son los vectores de cada base (coordenadas canónicas), vale
$C_{BB'}=P_{B'}^{-1}P_B$.

**a)** Buscamos $[b_j]_{B'}$ resolviendo $\alpha(1,1,1)+\beta(0,1,1)+\gamma(0,0,1)=b_j$:

- $b_1=(1,1,0)$: $\alpha=1$; $\alpha+\beta=1\Rightarrow\beta=0$; $\alpha+\beta+\gamma=0\Rightarrow\gamma=-1$.
- $b_2=(0,1,0)$: $\alpha=0$, $\beta=1$, $\gamma=-1$.
- $b_3=(1,1,1)$: $\alpha=1$, $\beta=0$, $\gamma=0$.

$$
C_{BB'}=\begin{pmatrix}1&0&1\\0&1&0\\-1&-1&0\end{pmatrix}.
$$

**b)** $[v]_{B'}=C_{BB'}[v]_B=\begin{pmatrix}1&0&1\\0&1&0\\-1&-1&0\end{pmatrix}\begin{pmatrix}2\\-1\\3\end{pmatrix}=\begin{pmatrix}5\\-1\\-1\end{pmatrix}$.

El vector es $v=2(1,1,0)-(0,1,0)+3(1,1,1)=(5,4,3)$. **Comprobación** con $B'$:
$5(1,1,1)-(0,1,1)-(0,0,1)=(5,4,3)$.

**c)** $C_{B'B}=C_{BB'}^{-1}$. Calculando las coordenadas de los vectores de $B'$ en $B$:

$$
C_{B'B}=\begin{pmatrix}0&-1&-1\\0&1&0\\1&1&1\end{pmatrix}.
$$

**Comprobación:**
$C_{BB'}C_{B'B}=\begin{pmatrix}1&0&1\\0&1&0\\-1&-1&0\end{pmatrix}\begin{pmatrix}0&-1&-1\\0&1&0\\1&1&1\end{pmatrix}
=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}$.

:::tip[Resultado]
$C_{BB'}$ como arriba; $[v]_{B'}=(5,-1,-1)^t$, $v=(5,4,3)$; $C_{B'B}=C_{BB'}^{-1}$.
:::

</details>

### Ejercicio 15 · Cambio de coordenadas con polinomios
<!-- ejercicio: U1.15 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $P_2[\mathbb{R}]$ sean $B=\{1,\ 1+x,\ x+x^2\}$ y $B'=\{1,\ x-1,\ (x-1)^2\}$.

a) Hallar $C_{BB'}$.

b) Para $p=2+3x+x^2$, hallar $[p]_B$ y $[p]_{B'}$ y comprobar la relación con $C_{BB'}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Expresar cada polinomio de $B$ como combinación de $1$, $x-1$ y $(x-1)^2=1-2x+x^2$.

**a)** Como $x=(x-1)+1$:

- $1=1\cdot1$: $[1]_{B'}=(1,0,0)^t$.
- $1+x=2+(x-1)$: $[1+x]_{B'}=(2,1,0)^t$.
- $x+x^2$: como $x^2=(x-1)^2+2x-1$ resulta $x+x^2=(x-1)^2+3x-1=(x-1)^2+3(x-1)+2$, luego
  $[x+x^2]_{B'}=(2,3,1)^t$.

$$
C_{BB'}=\begin{pmatrix}1&2&2\\0&1&3\\0&0&1\end{pmatrix}.
$$

**b)** $p=2+3x+x^2=0\cdot1+2(1+x)+1(x+x^2)$ (la suma da $2+2x+x+x^2$), así que $[p]_B=(0,2,1)^t$. Entonces

$$
[p]_{B'}=C_{BB'}[p]_B=\begin{pmatrix}1&2&2\\0&1&3\\0&0&1\end{pmatrix}\begin{pmatrix}0\\2\\1\end{pmatrix}=\begin{pmatrix}6\\5\\1\end{pmatrix}.
$$

**Comprobación directa:** $6+5(x-1)+(x-1)^2=6+5x-5+x^2-2x+1=2+3x+x^2$.

:::tip[Resultado]
$C_{BB'}$ como arriba; $[p]_B=(0,2,1)^t$ y $[p]_{B'}=(6,5,1)^t$.
:::

</details>

### Ejercicio 16 · Un subespacio de ℤ₂⁴ y el mismo conjunto en ℝ⁴
<!-- ejercicio: U1.16 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $W=\operatorname{gen}\{w_1,w_2,w_3\}\subseteq\mathbb{Z}_2^4$ con $w_1=1101$, $w_2=0111$, $w_3=1010$.

a) Hallar una base de $W$, su dimensión y listar todos sus elementos.

b) Hallar ecuaciones implícitas de $W$ y decidir si $1001\in W$.

c) ¿Cuál es la dimensión del generado por los mismos tres vectores, vistos como vectores de $\mathbb{R}^4$?
:::

<details>
<summary>Resolución</summary>

**a)** $w_1+w_2=(1,1+1,0+1,1+1)=(1,0,1,0)=w_3$, así que $w_3$ sobra. $w_1,w_2$ son distintos y no nulos, luego
independientes. Base $\{w_1,w_2\}$, $\dim W=2$ y $|W|=2^2=4$:

$$
W=\{0000,\ 1101,\ 0111,\ 1010\}.
$$

**b)** Un elemento es $aw_1+bw_2=(a,\ a+b,\ b,\ a+b)$ con $a,b\in\mathbb{Z}_2$. Entonces $x_1=a$, $x_3=b$ y
$x_2=x_4=a+b$:

$$
W:\ \begin{cases}x_1+x_2+x_3=0\\ x_2+x_4=0.\end{cases}
$$

Para $1001$: $x_1+x_2+x_3=1+0+0=1\neq0$, luego $1001\notin W$. **Comprobación:** $1101$ cumple
$1+1+0=0$ y $1+1=0$; $0111$ cumple $0+1+1=0$ y $1+1=0$.

**c)** Sobre $\mathbb{R}$, $w_1+w_2=(1,2,1,2)\neq w_3$, y $w_3$ no es combinación de $w_1,w_2$ (el sistema
$a(1,1,0,1)+b(0,1,1,1)=(1,0,1,0)$ da $a=1$, $b=1$ y $a+b=2\neq0$). Los tres vectores son independientes en
$\mathbb{R}^4$: la dimensión es $3$.

:::tip[Resultado]
$\dim W=2$, $W=\{0000,1101,0111,1010\}$, ecuaciones $x_1+x_2+x_3=0$, $x_2+x_4=0$, $1001\notin W$; sobre
$\mathbb{R}$ los mismos vectores generan un subespacio de dimensión $3$.
:::

</details>

### Ejercicio 17 · Intersección y suma de subespacios
<!-- ejercicio: U1.17 | nivel: intermedio | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sean $S$ y $T$ subespacios de un espacio vectorial $V$ sobre $K$.

a) Probar que $S\cap T$ es un subespacio de $V$.

b) Probar que $S+T=\{s+t:\ s\in S,\ t\in T\}$ es un subespacio de $V$ que contiene a $S$ y a $T$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Verificar las tres condiciones del criterio de subespacio con las hipótesis $S$ y $T$
subespacios.

**a)** *Nulo.* $0_V\in S$ y $0_V\in T$, luego $0_V\in S\cap T$.
*Suma.* Si $u,v\in S\cap T$, entonces $u,v\in S$ y como $S$ es subespacio, $u+v\in S$; análogamente
$u+v\in T$. Luego $u+v\in S\cap T$.
*Escalares.* Si $u\in S\cap T$ y $\lambda\in K$, $\lambda u\in S$ y $\lambda u\in T$ por la misma razón, así
que $\lambda u\in S\cap T$. $\blacksquare$

**b)** *Nulo.* $0_V=0_V+0_V$ con $0_V\in S$ y $0_V\in T$.
*Suma.* Sean $x=s_1+t_1$ y $y=s_2+t_2$ con $s_i\in S$, $t_i\in T$. Por conmutatividad y asociatividad
$x+y=(s_1+s_2)+(t_1+t_2)$; $s_1+s_2\in S$ y $t_1+t_2\in T$, de modo que $x+y\in S+T$.
*Escalares.* $\lambda x=\lambda s_1+\lambda t_1$ con $\lambda s_1\in S$ y $\lambda t_1\in T$.
*Contiene a $S$ y $T$.* Si $s\in S$, $s=s+0_V\in S+T$; igual para $t\in T$, $t=0_V+t$. $\blacksquare$

**Observación.** La unión $S\cup T$ en general no es subespacio (ejercicio 11); $S+T$ es el menor
subespacio que contiene a ambos.

:::tip[Resultado]
$S\cap T$ y $S+T$ son subespacios de $V$, y $S,T\subseteq S+T$.
:::

</details>

### Ejercicio 18 · Hamming $(7,4)$: codificar, corregir y fallar
<!-- ejercicio: U1.18 | nivel: intermedio | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C$ el código de Hamming $(7,4)$ con

$$
G=\left(\begin{array}{cccc|ccc}1&0&0&0&1&1&0\\0&1&0&0&1&0&1\\0&0&1&0&0&1&1\\0&0&0&1&1&1&1\end{array}\right),\qquad
H=\left(\begin{array}{cccc|ccc}1&1&0&1&1&0&0\\1&0&1&1&0&1&0\\0&1&1&1&0&0&1\end{array}\right).
$$

a) Codificar el mensaje $1101$ y verificar que la palabra obtenida tiene síndrome nulo.

b) Se recibe $r=1101000$. Calcular el síndrome, corregir el error y recuperar el mensaje.

c) Se envía la palabra del inciso a) y se invierten los bits $1$ y $7$. Decir qué entrega el decodificador y
por qué es un problema.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Codificar es $u=aG$; el síndrome $s=Hr^t$ de un solo error coincide con la columna de $H$ de la
posición errada.

**a)** $u=g_1+g_2+g_4=(1,0,0,0,1,1,0)+(0,1,0,0,1,0,1)+(0,0,0,1,1,1,1)=(1,1,0,1,\ 1,\ 0,\ 0)=1101100$.
(Los bits de paridad: $1+1+1=1$, $1+0+1=0$, $0+1+1=0$.) **Comprobación:** las filas de $H$ dan
$1+1+1+1=0$, $1+0+1+0=0$, $1+0+1+0=0$, o sea $Hu^t=0$.

**b)** Con $r=(1,1,0,1,0,0,0)$:

$$
s=Hr^t=\begin{pmatrix}r_1+r_2+r_4+r_5\\r_1+r_3+r_4+r_6\\r_2+r_3+r_4+r_7\end{pmatrix}
=\begin{pmatrix}1+1+1+0\\1+0+1+0\\1+0+1+0\end{pmatrix}=\begin{pmatrix}1\\0\\0\end{pmatrix}.
$$

Es la columna $5$ de $H$: el error está en la posición $5$. Corregimos: $r+e_5=1101100=u$. El mensaje son los
primeros cuatro bits: $1101$.

**c)** $v=u+e_1+e_7=0101101$. El síndrome es $h_1+h_7=(1,1,0)+(0,0,1)=(1,1,1)=h_4$, la columna $4$. El
decodificador cree que hubo **un** error en la posición $4$ y entrega $v+e_4=0100101$, que es una palabra
código (la del mensaje $0100$, igual a $g_2$) pero **no** la enviada: se corrige mal y sin ningún aviso, porque
con $d=3$ un código solo garantiza corregir un error.

:::tip[Resultado]
$1101\mapsto1101100$; $r=1101000$ tiene síndrome $(1,0,0)^t$, error en la posición $5$ y mensaje $1101$; con
dos errores el decodificador entrega $0100101$, otra palabra código.
:::

</details>
