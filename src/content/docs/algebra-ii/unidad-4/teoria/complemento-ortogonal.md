---
title: Complemento ortogonal
description: El complemento ortogonal de un subespacio, sus propiedades (dimensión y doble complemento) y su cálculo en Rⁿ con producto usual y no usual, en matrices y en polinomios.
slug: algebra-ii/unidad-4/teoria/complemento-ortogonal
sidebar:
  order: 5
  label: 4.5 Complemento ortogonal
---

En el plano, la perpendicular a una recta por el origen es otra recta; en el espacio, la perpendicular a un plano por el origen es una recta, y la perpendicular a una recta es un plano. En todos los casos, el conjunto de todos los vectores perpendiculares a un subespacio es otro subespacio, de dimensión complementaria. Ese es el **complemento ortogonal**: la herramienta que permite descomponer cualquier vector en una parte que está en $S$ y una parte "perpendicular" a $S$ (lección [4.6](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/)), y que reaparece en los cuadrados mínimos y en los códigos duales.

En toda la lección, $(V,\langle\,,\rangle)$ es un espacio euclídeo de dimensión $n$.

## Definición

:::note[Definición (complemento ortogonal)]
Sea $S\subseteq V$ un subespacio. El **complemento ortogonal** de $S$ es

$$
S^{\perp}=\{v\in V:\ \langle v,s\rangle=0\ \text{ para todo } s\in S\}.
$$
:::

Dicho en palabras: $S^\perp$ está formado por los vectores ortogonales a **todos** los vectores de $S$. Dos casos extremos: $\{0_V\}^\perp=V$ (todo vector es ortogonal al nulo) y $V^\perp=\{0_V\}$ (un vector ortogonal a todo $V$ lo es a sí mismo, y es nulo).

## Propiedades

:::note[Propiedad 1]
$S^\perp$ es un subespacio de $V$.
:::

**Demostración.** $0_V\in S^\perp$, pues $\langle0_V,s\rangle=0$. Si $u,w\in S^\perp$ y $a\in\mathbb{R}$, para cada $s\in S$ vale $\langle u+aw,s\rangle=\langle u,s\rangle+a\langle w,s\rangle=0+0$; luego $u+aw\in S^\perp$. $\blacksquare$

:::note[Propiedad 2 (basta un generador)]
Si $S=\operatorname{gen}\{g_1,\dots,g_m\}$, entonces $v\in S^\perp$ si y solo si $\langle v,g_i\rangle=0$ para todo $i=1,\dots,m$.
:::

**Demostración.** Si $v\in S^\perp$, en particular es ortogonal a cada $g_i\in S$. Recíprocamente, si $v\perp g_i$ para todo $i$ y $s=a_1g_1+\dots+a_mg_m$ es un vector cualquiera de $S$, entonces $\langle v,s\rangle=\sum a_i\langle v,g_i\rangle=0$. $\blacksquare$

Esta propiedad reduce "ortogonal a infinitos vectores" a "ortogonal a unos pocos", y es el punto de partida del cálculo: se imponen las ecuaciones $\langle v,g_i\rangle=0$ solo para los generadores (o para una base).

:::note[Propiedad 3]
$S\cap S^\perp=\{0_V\}$.
:::

**Demostración.** Si $v\in S\cap S^\perp$, es ortogonal a todos los vectores de $S$, en particular a $v\in S$: $\langle v,v\rangle=0$, y por positividad $v=0_V$. $\blacksquare$

:::note[Propiedad 4 (dimensión)]
Si $\dim V=n$ y $S$ es un subespacio, entonces $\dim S+\dim S^\perp=n$.
:::

**Demostración.** Sea $k=\dim S$. Por Gram-Schmidt (lección [4.4](/algebra-ii/unidad-4/teoria/gram-schmidt/)) existe una base ortogonal $\{u_1,\dots,u_k\}$ de $S$, que se extiende a una base ortogonal $\{u_1,\dots,u_n\}$ de $V$. Afirmamos que $S^\perp=\operatorname{gen}\{u_{k+1},\dots,u_n\}$.

- ($\supseteq$) Cada $u_j$ con $j>k$ es ortogonal a $u_1,\dots,u_k$, que generan $S$; por la propiedad 2, $u_j\in S^\perp$, y como $S^\perp$ es subespacio contiene al generado.
- ($\subseteq$) Sea $v\in S^\perp$. Por el teorema de coordenadas en una base ortogonal (lección [4.3](/algebra-ii/unidad-4/teoria/ortogonalidad/)), $v=\sum_{i=1}^nc_iu_i$ con $c_i=\langle v,u_i\rangle/\langle u_i,u_i\rangle$. Para $i\le k$ es $u_i\in S$, así que $\langle v,u_i\rangle=0$ y $c_i=0$. Luego $v\in\operatorname{gen}\{u_{k+1},\dots,u_n\}$.

Los $u_{k+1},\dots,u_n$ son LI (ortogonales no nulos), de modo que $\dim S^\perp=n-k$. $\blacksquare$

:::note[Propiedad 5 (doble complemento)]
$(S^\perp)^\perp=S$.
:::

**Demostración.** Si $s\in S$, es ortogonal a todo vector de $S^\perp$ por definición de $S^\perp$; entonces $s\in(S^\perp)^\perp$, y $S\subseteq(S^\perp)^\perp$. Por la propiedad 4 aplicada dos veces, $\dim(S^\perp)^\perp=n-(n-\dim S)=\dim S$. Un subespacio contenido en otro de igual dimensión es igual a él. $\blacksquare$

Consecuencia: $V=S+S^\perp$, y como $S\cap S^\perp=\{0_V\}$ la suma es directa, $V=S\oplus S^\perp$. Cada vector se descompone de manera única en una parte de $S$ y otra de $S^\perp$ (la descomposición se desarrolla en la lección 4.6).

Dos subespacios $S,T$ son **ortogonales** si $\langle s,t\rangle=0$ para todos $s\in S$, $t\in T$; equivale a $T\subseteq S^\perp$. Alcanza con verificar la condición sobre bases (o generadores) de ambos.

## Cálculo del complemento ortogonal

**En $\mathbb{R}^n$ con el producto usual.** Si $S=\operatorname{gen}\{s_1,\dots,s_m\}$ y $A$ es la matriz cuyas **filas** son $s_1^t,\dots,s_m^t$, entonces $S=\operatorname{fil}(A)$ y, por la propiedad 2,

$$
v\in S^\perp\iff s_i\cdot v=0\ \ \forall i\iff Av=0,\qquad\text{es decir,}\qquad \operatorname{fil}(A)^\perp=\operatorname{nul}(A).
$$

Una base de $S^\perp$ sale de la solución del sistema homogéneo $Av=0$ (lección [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/)). Como $\dim\operatorname{nul}(A)=n-\operatorname{rango}(A)$, recuperamos la propiedad 4: es el teorema de rango y nulidad. Si las filas de $A$ son LI, $S^\perp=\operatorname{nul}(A)$ tiene dimensión $n-m$.

**Con un producto no usual $\langle x,y\rangle=x^tMy$.** La condición $\langle s_i,v\rangle=s_i^tMv=0$ es una ecuación lineal en $v$ con coeficientes $s_i^tM=(Ms_i)^t$ (usamos $M^t=M$). Entonces $S^\perp=\operatorname{nul}(AM)$: **hay que multiplicar cada generador por $M$ antes de plantear el sistema**.

**En otros espacios** ($\mathbb{R}^{2\times2}$, $P_n[\mathbb{R}]$): se eligen coordenadas respecto de una base $B$, se escribe el producto como $\langle u,v\rangle=[u]_B^tG[v]_B$ y se aplica lo anterior a $[S]_B$. Si el producto es el usual en las coordenadas (por ejemplo la traza en la base canónica de matrices), $G=I$.

## Ejemplos

### Ejemplo 1 · Complementos de una recta y de un plano en $\mathbb{R}^3$
<!-- check: U4.T05.E1 -->

Con el producto usual, hallar $L^\perp$ para $L=\operatorname{gen}\{(1,-1,2)\}$ y $\Pi^\perp$ para el plano $\Pi:\ 2x+y-z=0$.

**Resolución.** Para $L$, $v=(x,y,z)\in L^\perp$ si y solo si $x-y+2z=0$. Despejamos $x=y-2z$ y escribimos $(x,y,z)=y(1,1,0)+z(-2,0,1)$:

$$
L^\perp=\operatorname{gen}\{(1,1,0),(-2,0,1)\},\qquad\dim L+\dim L^\perp=1+2=3 .
$$

Para $\Pi$: es el conjunto de soluciones de $2x+y-z=0$, es decir, $\Pi=\operatorname{nul}(A)$ con $A=\begin{pmatrix}2&1&-1\end{pmatrix}$, y por el doble complemento $\Pi^\perp=\operatorname{fil}(A)^{\perp\perp}=\operatorname{fil}(A)=\operatorname{gen}\{(2,1,-1)\}$: la recta generada por el **vector normal** del plano. Una base de $\Pi$ es $\{(1,-2,0),(0,1,1)\}$ (despejando $y=z-2x$).

**Comprobación.** $(1,-1,2)\cdot(1,1,0)=0$ y $(1,-1,2)\cdot(-2,0,1)=0$. Para el plano: $(2,1,-1)\cdot(1,-2,0)=2-2=0$ y $(2,1,-1)\cdot(0,1,1)=1-1=0$, y las dimensiones suman $2+1=3$.

### Ejemplo 2 · Un complemento ortogonal en $\mathbb{R}^4$ como espacio nulo
<!-- check: U4.T05.E2 -->

Con el producto usual de $\mathbb{R}^4$, hallar una base de $S^\perp$ para $S=\operatorname{gen}\{(1,0,2,-1),(0,1,1,1)\}$ y verificar que $(S^\perp)^\perp=S$.

**Resolución.** Sea $A=\begin{pmatrix}1&0&2&-1\\0&1&1&1\end{pmatrix}$, de rango $2$. Entonces $S^\perp=\operatorname{nul}(A)$: el sistema $y_1+2y_3-y_4=0$, $y_2+y_3+y_4=0$ tiene como variables libres $y_3,y_4$ y

$$
(y_1,y_2,y_3,y_4)=y_3(-2,-1,1,0)+y_4(1,-1,0,1),\qquad S^\perp=\operatorname{gen}\{(-2,-1,1,0),\ (1,-1,0,1)\}.
$$

La dimensión es $2$ y $\dim S+\dim S^\perp=4$. Para el doble complemento, ponemos las filas $(-2,-1,1,0)$ y $(1,-1,0,1)$ en una matriz $B$ y calculamos $\operatorname{nul}(B)$: el sistema $-2z_1-z_2+z_3=0$, $z_1-z_2+z_4=0$ se despeja como $z_3=2z_1+z_2$ y $z_4=z_2-z_1$, con $z_1,z_2$ libres: $z_1(1,0,2,-1)+z_2(0,1,1,1)$, que es $S$.

**Comprobación.** $A\,(-2,-1,1,0)^t=(-2+0+2+0,\ -1+1)^t=(0,0)^t$ y $A\,(1,-1,0,1)^t=(1-1,\ -1+1)^t=(0,0)^t$.

### Ejemplo 3 · Complemento ortogonal en $\mathbb{R}^{2\times2}$ con la traza
<!-- check: U4.T05.E3 -->

En $\mathbb{R}^{2\times2}$ con $\langle A,B\rangle=\operatorname{tr}(A^tB)$, hallar $S^\perp$ para $S=\operatorname{gen}\{A_1,A_2\}$, con $A_1=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ y $A_2=\begin{pmatrix}0&1\\1&-1\end{pmatrix}$.

**Resolución.** Con este producto, $\operatorname{tr}(A^tB)$ es la suma de los productos de las entradas correspondientes: es el producto usual de $\mathbb{R}^4$ en las coordenadas canónicas. Para $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, las condiciones de la propiedad 2 son

$$
\begin{cases}\langle A_1,X\rangle=a+2b+d=0\\ \langle A_2,X\rangle=b+c-d=0\end{cases}\qquad\Longrightarrow\qquad d=-a-2b,\quad c=d-b=-a-3b .
$$

Los parámetros libres son $a,b$. Tomando $(a,b)=(2,-1)$ resulta $X_1=\begin{pmatrix}2&-1\\1&0\end{pmatrix}$ y con $(a,b)=(-3,1)$, $X_2=\begin{pmatrix}-3&1\\0&1\end{pmatrix}$, que son LI (los pares de parámetros $(2,-1)$ y $(-3,1)$ no son proporcionales). Entonces $S^\perp=\operatorname{gen}\{X_1,X_2\}$ y $\dim S+\dim S^\perp=2+2=4=\dim\mathbb{R}^{2\times2}$.

**Comprobación.** $\operatorname{tr}(A_1^tX_1)=1\cdot2+2\cdot(-1)+0\cdot1+1\cdot0=0$ y $\operatorname{tr}(A_2^tX_1)=0\cdot2+1\cdot(-1)+1\cdot1+(-1)\cdot0=0$; análogamente para $X_2$: $-3+2+0+1=0$ y $1+0-1=0$.

### Ejemplo 4 · Complemento con un producto no usual
<!-- check: U4.T05.E4 -->

En $\mathbb{R}^3$ con $\langle x,y\rangle=x_1y_1+(x_1+x_2)(y_1+y_2)+(x_2+x_3)(y_2+y_3)$, hallar $S^\perp$ para $S=\operatorname{gen}\{s_1,s_2\}$, con $s_1=(1,0,1)$ y $s_2=(0,1,0)$.

**Resolución.** Desarrollando, $\langle x,y\rangle=x^tMy$ con $M=\begin{pmatrix}2&1&0\\1&2&1\\0&1&1\end{pmatrix}$. (Es un producto interno: es suma de cuadrados de las formas lineales $x_1$, $x_1+x_2$, $x_2+x_3$, que son LI.) Calculamos $Ms_1=(2,2,1)^t$ y $Ms_2=(1,2,1)^t$, de modo que $v=(x,y,z)\in S^\perp$ si y solo si

$$
\begin{cases}2x+2y+z=0\\ x+2y+z=0\end{cases}\ \Longrightarrow\ x=0,\quad z=-2y\ \Longrightarrow\ S^\perp=\operatorname{gen}\{(0,1,-2)\}.
$$

**Comprobación.** $\langle(0,1,-2),s_1\rangle=(0,1,-2)\cdot(2,2,1)=0$ y $\langle(0,1,-2),s_2\rangle=(0,1,-2)\cdot(1,2,1)=0$. Con el producto usual el complemento sería otro: $\operatorname{gen}\{(1,0,-1)\}$. Este mismo $S$ y este producto vuelven en el Ejemplo 4 de la lección 4.6.

## Interpretación

- La descomposición $V=S\oplus S^\perp$ hace de $S^\perp$ un "complemento canónico" de $S$: entre todos los subespacios complementarios, es el único cuyos vectores son perpendiculares a $S$. Cualquier otro complemento depende de la elección y no es ortogonal.
- Para una matriz $A$ de $m\times n$ con el producto usual, la relación $\operatorname{fil}(A)^\perp=\operatorname{nul}(A)$ dice que el espacio nulo es exactamente lo perpendicular al espacio fila. Aplicada a $A^t$ da $\operatorname{col}(A)^\perp=\operatorname{nul}(A^t)$, la clave de los cuadrados mínimos (lección [4.7](/algebra-ii/unidad-4/teoria/cuadrados-minimos/)).
- Cuando un subespacio tiene muchos generadores y su complemento pocos, conviene calcular el complemento chico y obtener el grande como su complemento (por ejemplo, un plano de $\mathbb{R}^3$ a partir de su normal).

:::caution[Errores frecuentes]
- **Creer que dos planos perpendiculares de $\mathbb{R}^3$ son subespacios ortogonales.** Los planos $z=0$ y $y=0$ forman un diedro de $90^\circ$ y sus normales $e_3$ y $e_2$ son ortogonales, pero $e_1$ pertenece a ambos planos y $\langle e_1,e_1\rangle=1\neq0$. Dos planos de $\mathbb{R}^3$ nunca son subespacios ortogonales: $T\subseteq S^\perp$ obligaría a $2\le\dim S^\perp=1$.
- **Calcular $S^\perp$ con el producto usual cuando el producto no lo es.** Hay que usar $Ms_i$ (Ejemplo 4).
- **Omitir generadores.** $v\perp S$ exige ortogonalidad con una base *completa* de $S$, no con un solo vector.
- **Olvidar las dimensiones.** Si $\dim S=k$ en $\mathbb{R}^n$ y el sistema da un espacio de dimensión distinto de $n-k$, hay un error en el escalonamiento o las filas no eran LI.
- **Confundir el complemento ortogonal con el complemento conjuntista.** $S^\perp$ es un subespacio y contiene al vector nulo; el conjunto $V\setminus S$ no.
:::

## Autoevaluación

<details>
<summary>1. Si S es la recta generada por (1, 2, 2) en R³ con el producto usual, ¿qué dimensión tiene S⊥ y cuál es una ecuación implícita?</summary>

$\dim S^\perp=3-1=2$ y $S^\perp:\ x+2y+2z=0$.

</details>

<details>
<summary>2. Probar que si S ⊆ T entonces T⊥ ⊆ S⊥.</summary>

Si $v\in T^\perp$, es ortogonal a todo vector de $T$, en particular a todo vector de $S\subseteq T$; luego $v\in S^\perp$.

</details>

<details>
<summary>3. ¿Existen subespacios S, T de R⁴ con dim S = dim T = 2, ortogonales entre sí con el producto usual?</summary>

Sí: $S=\operatorname{gen}\{e_1,e_2\}$ y $T=\operatorname{gen}\{e_3,e_4\}$; en este caso $T=S^\perp$. En $\mathbb{R}^3$, en cambio, dos planos nunca son ortogonales.

</details>

:::tip[En resumen]
- $S^\perp=\{v:\langle v,s\rangle=0\ \forall s\in S\}$ es un subespacio; para pertenecer a él basta ser ortogonal a un generador de $S$.
- $S\cap S^\perp=\{0_V\}$, $\dim S+\dim S^\perp=\dim V$, $(S^\perp)^\perp=S$ y $V=S\oplus S^\perp$.
- Con el producto usual, $\operatorname{fil}(A)^\perp=\operatorname{nul}(A)$; con $\langle x,y\rangle=x^tMy$, $S^\perp=\operatorname{nul}(AM)$ con $A$ de filas $s_i^t$.
- En $\mathbb{R}^3$: la perpendicular de una recta es un plano y la de un plano es su recta normal; dos planos nunca son ortogonales.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 5.2, "Complementos y proyecciones ortogonales" (p. 389); sección 7.1 (p. 554) para espacios con producto interno generales.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ortogonalidad y mínimos cuadrados (complemento ortogonal y descomposición ortogonal).
- Anterior: [4.4 Gram-Schmidt](/algebra-ii/unidad-4/teoria/gram-schmidt/). Siguiente: [4.6 Proyección y distancia](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/).
- Repaso: [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/); [rectas y planos](/algebra-ii/repaso/rectas-y-planos/).
