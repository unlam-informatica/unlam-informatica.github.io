---
title: Práctica — Nivel avanzado
description: Nueve ejercicios resueltos de transformaciones lineales con demostraciones, contraejemplos, verdadero o falso, una familia con parámetro, bases abstractas y una reflexión del plano en una base adaptada.
slug: algebra-ii/unidad-2/practica/nivel-avanzado
sidebar:
  order: 3
  label: Nivel avanzado
---

Esta página presupone el [nivel intermedio](/algebra-ii/unidad-2/practica/nivel-intermedio/) y toda la teoría de la unidad: [clasificación](/algebra-ii/unidad-2/teoria/clasificacion/), [teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/), [teorema fundamental](/algebra-ii/unidad-2/teoria/teorema-fundamental/), [matriz asociada](/algebra-ii/unidad-2/teoria/matriz-asociada/), [cambio de base](/algebra-ii/unidad-2/teoria/cambio-de-base/) y [composición e inversa](/algebra-ii/unidad-2/teoria/composicion-e-inversa/). Combina argumentos teóricos (ejercicios 19 a 24) con cálculos más largos (25 a 27).

Cómo usarla: en las demostraciones, escribí primero qué hay que probar y con qué hipótesis; en los contraejemplos, verificá siempre que el ejemplo cumple las hipótesis antes de mostrar que falla la conclusión. Todos los enunciados son originales de este manual. La numeración continúa la del nivel intermedio.

### Ejercicio 19 · Inyectividad y conjuntos independientes
<!-- ejercicio: U2.19 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $T:V\to W$ una transformación lineal entre espacios sobre el mismo cuerpo.

a) Probar que $T$ es inyectiva si y solo si transforma todo conjunto linealmente independiente $\{v_1,\dots,v_k\}$ de $V$ en un conjunto linealmente independiente $\{T(v_1),\dots,T(v_k)\}$ de $W$.

b) Deducir que si $\dim V>\dim W$ (finitas), ninguna transformación lineal $T:V\to W$ es inyectiva.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Usamos que $T$ es inyectiva si y solo si $\operatorname{Nu}(T)=\{0_V\}$ y la definición de independencia lineal.

**a)** ($\Rightarrow$) Supongamos $T$ inyectiva y sea $\{v_1,\dots,v_k\}$ linealmente independiente. Si $\lambda_1T(v_1)+\dots+\lambda_kT(v_k)=0_W$, por linealidad $T(\lambda_1v_1+\dots+\lambda_kv_k)=0_W$, así que $\lambda_1v_1+\dots+\lambda_kv_k\in\operatorname{Nu}(T)=\{0_V\}$. Entonces $\lambda_1v_1+\dots+\lambda_kv_k=0_V$ y, por la independencia de los $v_i$, $\lambda_1=\dots=\lambda_k=0$. Luego $\{T(v_1),\dots,T(v_k)\}$ es linealmente independiente.

($\Leftarrow$) Supongamos que $T$ transforma conjuntos LI en conjuntos LI y que $T$ no es inyectiva. Entonces existe $v\in\operatorname{Nu}(T)$ con $v\neq 0_V$. El conjunto $\{v\}$ es LI (un vector no nulo es LI), pero $\{T(v)\}=\{0_W\}$ es LD. Esto contradice la hipótesis. Entonces $T$ es inyectiva. $\blacksquare$

**b)** Sea $n=\dim V>\dim W=m$ y una base $\{v_1,\dots,v_n\}$ de $V$, que es LI. Si $T$ fuera inyectiva, por a) $\{T(v_1),\dots,T(v_n)\}$ sería un conjunto LI de $n$ vectores de $W$, pero $W$ tiene dimensión $m<n$ y no admite más de $m$ vectores LI. Contradicción. $\blacksquare$

**Comprobación (casos borde).** El enunciado vale también para $k=1$ (un vector no nulo va a un vector no nulo) y no exige que el conjunto genere. Si $V=\{0\}$ la afirmación es trivial. En b) el resultado es consistente con el teorema de la dimensión: $\dim\operatorname{Nu}(T)\ge n-m>0$.

:::tip[Resultado]
$T$ es inyectiva $\iff$ lleva conjuntos LI en conjuntos LI. En particular, no hay inyectivas de un espacio en otro de menor dimensión.
:::

</details>

### Ejercicio 20 · Qué se hereda de una composición
<!-- ejercicio: U2.20 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sean $T:V\to W$ y $S:W\to U$ transformaciones lineales entre espacios de dimensión finita.

a) Probar que si $S\circ T$ es inyectiva, entonces $T$ es inyectiva.

b) Probar que si $S\circ T$ es sobreyectiva, entonces $S$ es sobreyectiva.

c) Probar que si $S\circ T$ es un isomorfismo y $\dim V=\dim W$, entonces $T$ y $S$ son isomorfismos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En a) se trabaja con el núcleo y en b) con la imagen; en c) se combinan con el teorema de la dimensión.

**a)** Sea $v\in\operatorname{Nu}(T)$. Entonces $(S\circ T)(v)=S(T(v))=S(0_W)=0_U$, así que $v\in\operatorname{Nu}(S\circ T)=\{0_V\}$ (por la inyectividad de $S\circ T$). Luego $\operatorname{Nu}(T)=\{0_V\}$ y $T$ es inyectiva. $\blacksquare$

**b)** Como $S\circ T$ es sobreyectiva, todo $u\in U$ es de la forma $u=S(T(v))$ con $v\in V$; entonces $u=S(w)$ con $w=T(v)\in W$. Es decir, $\operatorname{Im}(S)=U$ y $S$ es sobreyectiva. $\blacksquare$

**c)** Un isomorfismo es inyectivo y sobreyectivo. Por a), $T$ es inyectiva; como $\dim V=\dim W$, el teorema de la dimensión da $\dim\operatorname{Im}(T)=\dim V=\dim W$, así que $\operatorname{Im}(T)=W$ y $T$ es isomorfismo. Por b), $S$ es sobreyectiva. Además $V\cong U$ (por el isomorfismo $S\circ T$), de modo que $\dim U=\dim V=\dim W$; entonces $\dim\operatorname{Nu}(S)=\dim W-\dim U=0$ y $S$ es inyectiva. Luego $S$ es isomorfismo. $\blacksquare$

**Comprobación.** Sin la hipótesis $\dim V=\dim W$ la conclusión de c) falla: es el contenido del ejercicio siguiente.

:::tip[Resultado]
$S\circ T$ inyectiva $\Rightarrow$ $T$ inyectiva; $S\circ T$ sobreyectiva $\Rightarrow$ $S$ sobreyectiva; con $\dim V=\dim W$, $S\circ T$ iso $\Rightarrow$ $T$ y $S$ isos.
:::

</details>

### Ejercicio 21 · Una composición biyectiva por un espacio más grande
<!-- ejercicio: U2.21 | nivel: avanzado | tipo: contraejemplo | verificacion: sympy -->

:::note[Enunciado]
Un estudiante afirma: "si $S\circ T$ es un isomorfismo, entonces $S$ es inyectiva y $T$ es sobreyectiva". Dar un contraejemplo con transformaciones lineales $T:\mathbb{R}\to\mathbb{R}^2$ y $S:\mathbb{R}^2\to\mathbb{R}$, verificando todas las hipótesis y mostrando por qué falla la conclusión.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Por el ejercicio anterior, de $S\circ T$ iso se deduce que $T$ es *inyectiva* y que $S$ es *sobreyectiva*, que son las propiedades opuestas a las afirmadas. Buscamos entonces un caso donde el espacio intermedio $\mathbb{R}^2$ sea "demasiado grande".

Tomamos
$$
T(x)=(x,0),\qquad S(x,y)=x.
$$
Ambas son lineales: $M(T)=\begin{pmatrix}1\\0\end{pmatrix}$ y $M(S)=\begin{pmatrix}1&0\end{pmatrix}$.

*Hipótesis.* $M(S\circ T)=M(S)M(T)=(1)$, es decir $(S\circ T)(x)=S(x,0)=x$: la identidad de $\mathbb{R}$, que es un isomorfismo.

*Falla la conclusión.*

- $S$ no es inyectiva: $S(0,1)=0$ con $(0,1)\neq(0,0)$, o sea $\operatorname{Nu}(S)=\operatorname{gen}\{(0,1)\}\neq\{0\}$.
- $T$ no es sobreyectiva: $\operatorname{Im}(T)=\operatorname{gen}\{(1,0)\}$ tiene dimensión $1<2$; por ejemplo, $(0,1)\notin\operatorname{Im}(T)$.

**Comprobación.** $(S\circ T)(7)=S(7,0)=7$ y $\dim\operatorname{Nu}(S)+\dim\operatorname{Im}(S)=1+1=2=\dim\mathbb{R}^2$, consistente con el teorema de la dimensión.

:::tip[Resultado]
$T(x)=(x,0)$ y $S(x,y)=x$ cumplen $S\circ T=\operatorname{id}_{\mathbb{R}}$, pero $S$ no es inyectiva y $T$ no es sobreyectiva. La afirmación es falsa.
:::

</details>

### Ejercicio 22 · Núcleo e imagen de una suma
<!-- ejercicio: U2.22 | nivel: avanzado | tipo: contraejemplo | verificacion: sympy -->

:::note[Enunciado]
Sean $S,T:V\to W$ transformaciones lineales. Se afirma:

a) $\operatorname{Nu}(S+T)=\operatorname{Nu}(S)\cap\operatorname{Nu}(T)$.

b) $\operatorname{Im}(S+T)=\operatorname{Im}(S)+\operatorname{Im}(T)$.

Probar que en ambos casos vale una inclusión y dar un contraejemplo para la otra, con $V=W=\mathbb{R}^2$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se prueba la inclusión que sí vale con la definición, y para la que falla alcanza un ejemplo; sirve el par más simple, $S=I$ y $T=-I$, cuya suma es nula.

**Inclusiones que valen.**

- $\operatorname{Nu}(S)\cap\operatorname{Nu}(T)\subseteq\operatorname{Nu}(S+T)$: si $S(v)=0$ y $T(v)=0$, entonces $(S+T)(v)=S(v)+T(v)=0$.
- $\operatorname{Im}(S+T)\subseteq\operatorname{Im}(S)+\operatorname{Im}(T)$: un elemento de $\operatorname{Im}(S+T)$ es $(S+T)(v)=S(v)+T(v)$, suma de un elemento de $\operatorname{Im}(S)$ y uno de $\operatorname{Im}(T)$.

**Contraejemplo.** Sea $S=I$ y $T=-I$ en $\mathbb{R}^2$ (ambas son lineales), de modo que $S+T$ es la transformación nula.

a) $\operatorname{Nu}(S+T)=\mathbb{R}^2$ (todo vector va a cero), pero $\operatorname{Nu}(S)=\operatorname{Nu}(T)=\{0\}$ (son isomorfismos), con lo cual $\operatorname{Nu}(S)\cap\operatorname{Nu}(T)=\{0\}\neq\mathbb{R}^2$. La inclusión recíproca es falsa.

b) $\operatorname{Im}(S+T)=\{0\}$, pero $\operatorname{Im}(S)+\operatorname{Im}(T)=\mathbb{R}^2+\mathbb{R}^2=\mathbb{R}^2\neq\{0\}$. La inclusión recíproca es falsa.

**Comprobación.** Dimensiones: en a) $\dim\operatorname{Nu}(S+T)=2>0=\dim(\operatorname{Nu}(S)\cap\operatorname{Nu}(T))$ y en b) $\dim\operatorname{Im}(S+T)=0<2$, coherentes con $\dim\operatorname{Nu}+\dim\operatorname{Im}=2$ para la transformación nula. Un caso en que valen las inclusiones: $S(x,y)=(x+y,0)$ y $T(x,y)=(2x+2y,0)$ tienen el vector $(1,-1)$ en ambos núcleos y también en el de $S+T$.

:::tip[Resultado]
Valen $\operatorname{Nu}(S)\cap\operatorname{Nu}(T)\subseteq\operatorname{Nu}(S+T)$ e $\operatorname{Im}(S+T)\subseteq\operatorname{Im}(S)+\operatorname{Im}(T)$. Con $S=I$, $T=-I$ ambas inclusiones recíprocas son falsas.
:::

</details>

### Ejercicio 23 · Proyecciones
<!-- ejercicio: U2.23 | nivel: avanzado | tipo: demostracion | verificacion: sympy -->

:::note[Enunciado]
Sea $T:V\to V$ lineal con $T\circ T=T$ (una proyección).

a) Probar que $\operatorname{Im}(T)=\{v\in V:\ T(v)=v\}$.

b) Probar que $V=\operatorname{Nu}(T)\oplus\operatorname{Im}(T)$, es decir, $\operatorname{Nu}(T)\cap\operatorname{Im}(T)=\{0\}$ y $V=\operatorname{Nu}(T)+\operatorname{Im}(T)$.

c) Verificar con $T:\mathbb{R}^2\to\mathbb{R}^2$ de matriz $\begin{pmatrix}1&1\\0&0\end{pmatrix}$ y hallar $\operatorname{Nu}(T)$, $\operatorname{Im}(T)$ y la descomposición de $(3,2)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La condición $T^2=T$ dice que $T$ actúa como la identidad sobre su propia imagen.

**a)** Si $v=T(u)$, entonces $T(v)=T(T(u))=T(u)=v$, así que $v$ está en el conjunto $\{T(v)=v\}$. Recíprocamente, si $T(v)=v$, entonces $v\in\operatorname{Im}(T)$ por definición. $\blacksquare$

**b)** *Intersección.* Si $w\in\operatorname{Nu}(T)\cap\operatorname{Im}(T)$, por a) $T(w)=w$ y por pertenecer al núcleo $T(w)=0$; luego $w=0$.

*Suma.* Dado $v\in V$ escribimos $v=(v-T(v))+T(v)$. El segundo sumando está en $\operatorname{Im}(T)$. Para el primero, $T(v-T(v))=T(v)-T(T(v))=T(v)-T(v)=0$, así que está en $\operatorname{Nu}(T)$. Entonces $V=\operatorname{Nu}(T)+\operatorname{Im}(T)$, y la descomposición es única por la intersección nula. $\blacksquare$

**c)** Con $A=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ se comprueba $A^2=\begin{pmatrix}1&1\\0&0\end{pmatrix}=A$. Entonces $T(x,y)=(x+y,\ 0)$. *Núcleo:* $x+y=0$, es decir $\operatorname{Nu}(T)=\operatorname{gen}\{(1,-1)\}$. *Imagen:* $\operatorname{Im}(T)=\operatorname{gen}\{(1,0)\}$. Para $(3,2)$: $T(3,2)=(5,0)$ y $(3,2)-(5,0)=(-2,2)=-2(1,-1)\in\operatorname{Nu}(T)$:
$$
(3,2)=(-2,2)+(5,0).
$$

**Comprobación.** $T(-2,2)=(0,0)$ ✓ y $T(5,0)=(5,0)$ ✓ (la proyección fija su imagen). Dimensiones: $1+1=2$. Es una proyección sobre la recta $y=0$ a lo largo de la recta generada por $(1,-1)$, que no es perpendicular.

:::tip[Resultado]
Para $T\circ T=T$: $\operatorname{Im}(T)=\{v:\ T(v)=v\}$ y $V=\operatorname{Nu}(T)\oplus\operatorname{Im}(T)$. En el ejemplo, $(3,2)=(-2,2)+(5,0)$.
:::

</details>

### Ejercicio 24 · Cuatro afirmaciones sobre transformaciones de $\mathbb{R}^2$ y $\mathbb{R}^3$
<!-- ejercicio: U2.24 | nivel: avanzado | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
Decidir si cada afirmación es verdadera o falsa. Justificar con una demostración o con un contraejemplo explícito.

a) Existe una transformación lineal $T:\mathbb{R}^2\to\mathbb{R}^2$ con $\operatorname{Nu}(T)=\operatorname{Im}(T)$.

b) Existe una transformación lineal $T:\mathbb{R}^3\to\mathbb{R}^3$ con $\operatorname{Nu}(T)=\operatorname{Im}(T)$.

c) Existe una transformación lineal $T:\mathbb{R}^3\to\mathbb{R}^2$ con $T(1,0,0)=(1,1)$, $T(0,1,0)=(0,1)$ y $T(1,1,0)=(1,3)$.

d) Si $S,T:\mathbb{R}^2\to\mathbb{R}^2$ son lineales y $S\circ T=0$, entonces $T\circ S=0$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las afirmaciones de existencia se resuelven con el teorema de la dimensión y con la construcción de un ejemplo; las de implicación, con un contraejemplo si fallan.

**a) Verdadera.** Tomamos $T(x,y)=(y,0)$, con matriz $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. Su núcleo es $\{y=0\}=\operatorname{gen}\{(1,0)\}$ y su imagen es $\operatorname{gen}\{(1,0)\}$ (la imagen de $(0,1)$). Son iguales.

**b) Falsa.** Si $\operatorname{Nu}(T)=\operatorname{Im}(T)=:N$, entonces $\dim\operatorname{Nu}(T)=\dim\operatorname{Im}(T)=d$ y el teorema de la dimensión da $3=2d$, que no tiene solución entera. No existe. (En general, una $T:V\to V$ con $\operatorname{Nu}=\operatorname{Im}$ exige $\dim V$ par.)

**c) Falsa.** Como $(1,1,0)=(1,0,0)+(0,1,0)$, la linealidad obliga a
$$
T(1,1,0)=T(1,0,0)+T(0,1,0)=(1,1)+(0,1)=(1,2)\neq(1,3).
$$
Los datos son incompatibles, y no existe tal transformación.

**d) Falsa.** Contraejemplo: $T(x,y)=(0,x)$ y $S(x,y)=(x,0)$. Entonces $(S\circ T)(x,y)=S(0,x)=(0,0)$ para todo $(x,y)$, o sea $S\circ T=0$. Pero $(T\circ S)(1,0)=T(1,0)=(0,1)\neq(0,0)$, así que $T\circ S\neq 0$. (Las matrices $\begin{pmatrix}1&0\\0&0\end{pmatrix}\begin{pmatrix}0&0\\1&0\end{pmatrix}=0$ y $\begin{pmatrix}0&0\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\1&0\end{pmatrix}$ lo confirman: el producto no es conmutativo.)

**Comprobación.** En a), $T\circ T=0$ (la matriz al cuadrado es nula), que es lo que corresponde a $\operatorname{Im}(T)\subseteq\operatorname{Nu}(T)$. En d), $\operatorname{Im}(T)=\operatorname{gen}\{(0,1)\}\subseteq\operatorname{Nu}(S)=\operatorname{gen}\{(0,1)\}$, que es lo que hace $S\circ T=0$, mientras que $\operatorname{Im}(S)=\operatorname{gen}\{(1,0)\}\not\subseteq\operatorname{Nu}(T)=\operatorname{gen}\{(0,1)\}$.

:::tip[Resultado]
a) Verdadera. b) Falsa ($3=2d$ es imposible). c) Falsa (el dato forzado es $(1,2)$). d) Falsa ($S=\begin{pmatrix}1&0\\0&0\end{pmatrix}$, $T=\begin{pmatrix}0&0\\1&0\end{pmatrix}$).
:::

</details>

### Ejercicio 25 · Una familia de transformaciones según un parámetro
<!-- ejercicio: U2.25 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para cada $k\in\mathbb{R}$ sea $T_k:\mathbb{R}^3\to\mathbb{R}^3$,
$$
T_k(x,y,z)=(x+y+kz,\ x+ky+z,\ kx+y+z).
$$

a) Calcular el determinante de la matriz de $T_k$ y hallar los valores de $k$ para los que $T_k$ es isomorfismo.

b) Para $k=1$, hallar bases de $\operatorname{Nu}(T_1)$ y de $\operatorname{Im}(T_1)$.

c) Para $k=-2$, hallar bases de $\operatorname{Nu}(T_{-2})$ y de $\operatorname{Im}(T_{-2})$.

d) Clasificar $T_k$ según $k$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $T_k$ es isomorfismo si y solo si su matriz $A_k$ es inversible, es decir si $\det A_k\neq 0$. Los valores críticos se estudian aparte.

**a)** Desarrollando por la primera fila,
$$
\det A_k=\det\begin{pmatrix}1&1&k\\1&k&1\\k&1&1\end{pmatrix}=(k-1)-(1-k)+k(1-k^2)=(k-1)\big[2-k(1+k)\big].
$$
Como $2-k-k^2=-(k-1)(k+2)$, resulta
$$
\det A_k=-(k-1)^2(k+2).
$$
Es nulo exactamente para $k=1$ y $k=-2$. Entonces $T_k$ es isomorfismo si y solo si $k\notin\{1,-2\}$.

**b)** Para $k=1$ todas las filas de $A_1$ son $(1,1,1)$: el rango es 1. *Núcleo:* $x+y+z=0$, con base $\{(-1,1,0),(-1,0,1)\}$, de dimensión 2. *Imagen:* $\operatorname{Im}(T_1)=\operatorname{gen}\{(1,1,1)\}$, de dimensión 1. Se cumple $2+1=3$.

**c)** Para $k=-2$:
$$
A_{-2}=\begin{pmatrix}1&1&-2\\1&-2&1\\-2&1&1\end{pmatrix}\xrightarrow{\ F_2-F_1,\ F_3+2F_1\ }\begin{pmatrix}1&1&-2\\0&-3&3\\0&3&-3\end{pmatrix},
$$
que tiene rango 2. *Núcleo:* de $-3y+3z=0$ y $x+y-2z=0$ resulta $y=z$, $x=z$: $\operatorname{Nu}(T_{-2})=\operatorname{gen}\{(1,1,1)\}$. *Imagen:* las columnas 1 y 2, $(1,1,-2)$ y $(1,-2,1)$, forman una base. Ambas suman cero en sus coordenadas, y como $\dim\operatorname{Im}=2$, $\operatorname{Im}(T_{-2})=\{x+y+z=0\}$. Se cumple $1+2=3$.

**d)** Si $k\notin\{1,-2\}$, $T_k$ es isomorfismo. Si $k=1$ ($\operatorname{rango}=1$) o $k=-2$ ($\operatorname{rango}=2$), $T_k$ no es mono (núcleo no nulo) ni epi (imagen de dimensión menor que 3).

**Comprobación.** $\det A_0=-(0-1)^2\cdot 2=-2$ y $\det A_2=-(2-1)^2\cdot 4=-4$; directamente, $\det A_0=\det\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix}=1(0-1)-1(1-0)=-2$ ✓. Además $T_1(1,1,1)=(3,3,3)$ y $T_{-2}(1,1,1)=(0,0,0)$.

:::tip[Resultado]
$\det A_k=-(k-1)^2(k+2)$; isomorfismo si y solo si $k\neq 1,-2$. $k=1$: $\operatorname{Nu}=\{x+y+z=0\}$, $\operatorname{Im}=\operatorname{gen}\{(1,1,1)\}$. $k=-2$: $\operatorname{Nu}=\operatorname{gen}\{(1,1,1)\}$, $\operatorname{Im}=\{x+y+z=0\}$.
:::

</details>

### Ejercicio 26 · Bases abstractas
<!-- ejercicio: U2.26 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $V$ y $W$ espacios vectoriales reales con bases $B=\{v_1,v_2,v_3\}$ de $V$ y $B'=\{w_1,w_2\}$ de $W$, y sea $T:V\to W$ la transformación lineal con
$$
T(v_1)=w_1-w_2,\qquad T(v_2)=2w_1-2w_2,\qquad T(v_3)=w_1.
$$

a) Hallar $M(T)_{BB'}$, una base de $\operatorname{Nu}(T)$, una base de $\operatorname{Im}(T)$ y clasificar $T$.

b) Calcular $T(2v_1-v_3)$ y $T(v_1+v_2)$.

c) Verificar que $B_1=\{v_1+v_2,\ v_2+v_3,\ v_3\}$ y $B_1'=\{w_1+w_2,\ w_2\}$ son bases y hallar $M(T)_{B_1B_1'}$ con la fórmula de tres factores. Comprobar una columna directamente.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Trabajamos solo con coordenadas: no hace falta saber qué son concretamente $V$ y $W$.

**a)** Las columnas son las coordenadas de las imágenes en $B'$:
$$
M(T)_{BB'}=\begin{pmatrix}1&2&1\\-1&-2&0\end{pmatrix}.
$$
Las filas son independientes, así que el rango es 2: $\dim\operatorname{Im}(T)=2=\dim W$ y $T$ es epimorfismo; entonces $\dim\operatorname{Nu}(T)=3-2=1$. *Núcleo:* $a+2b+c=0$ y $-a-2b=0$ dan $c=0$ y $a=-2b$: $[v]_B=(-2,1,0)$, o sea $\operatorname{Nu}(T)=\operatorname{gen}\{-2v_1+v_2\}$. *Imagen:* $\operatorname{Im}(T)=W$, con base $B'$ (o con las columnas 1 y 3: $\{w_1-w_2,\ w_1\}$). $T$ no es monomorfismo.

**b)** $T(2v_1-v_3)=2(w_1-w_2)-w_1=w_1-2w_2$ y $T(v_1+v_2)=(w_1-w_2)+(2w_1-2w_2)=3w_1-3w_2$. Con la matriz: $M(2,0,-1)^t=(2-1,\ -2)^t=(1,-2)^t$ ✓ y $M(1,1,0)^t=(3,-3)^t$ ✓.

**c)** *Bases.* En coordenadas respecto de $B$, los vectores de $B_1$ son $(1,1,0)$, $(0,1,1)$ y $(0,0,1)$: la matriz $C_{B_1B}$ con esas columnas es triangular con diagonal de unos, de determinante 1. En $B'$, $B_1'$ tiene coordenadas $(1,1)$ y $(0,1)$, con matriz $\begin{pmatrix}1&0\\1&1\end{pmatrix}$ de determinante 1. Ambas son bases.

*Tres factores:* $M(T)_{B_1B_1'}=C_{B'B_1'}\,M(T)_{BB'}\,C_{B_1B}$ con
$$
C_{B_1B}=\begin{pmatrix}1&0&0\\1&1&0\\0&1&1\end{pmatrix},\qquad C_{B'B_1'}=\begin{pmatrix}1&0\\1&1\end{pmatrix}^{-1}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
$$
Primero $M(T)_{BB'}C_{B_1B}=\begin{pmatrix}1&2&1\\-1&-2&0\end{pmatrix}\begin{pmatrix}1&0&0\\1&1&0\\0&1&1\end{pmatrix}=\begin{pmatrix}3&3&1\\-3&-2&0\end{pmatrix}$ y luego
$$
M(T)_{B_1B_1'}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}\begin{pmatrix}3&3&1\\-3&-2&0\end{pmatrix}=\begin{pmatrix}3&3&1\\-6&-5&-1\end{pmatrix}.
$$

*Comprobación directa de la primera columna.* $T(v_1+v_2)=3w_1-3w_2=3(w_1+w_2)-6w_2$, de coordenadas $(3,-6)$ en $B_1'$ ✓. Las otras: $T(v_2+v_3)=3w_1-2w_2=3(w_1+w_2)-5w_2$, coordenadas $(3,-5)$ ✓; $T(v_3)=w_1=(w_1+w_2)-w_2$, coordenadas $(1,-1)$ ✓.

El núcleo en $B_1$: $[-2v_1+v_2]_{B_1}=C_{B_1B}^{-1}(-2,1,0)^t=(-2,3,-3)^t$ y $M(T)_{B_1B_1'}(-2,3,-3)^t=(-6+9-3,\ 12-15+3)=(0,0)$ ✓.

:::tip[Resultado]
$M(T)_{BB'}=\begin{pmatrix}1&2&1\\-1&-2&0\end{pmatrix}$; $\operatorname{Nu}(T)=\operatorname{gen}\{-2v_1+v_2\}$, $\operatorname{Im}(T)=W$, $T$ epimorfismo; $T(2v_1-v_3)=w_1-2w_2$; $M(T)_{B_1B_1'}=\begin{pmatrix}3&3&1\\-6&-5&-1\end{pmatrix}$.
:::

</details>

### Ejercicio 27 · Reflexión respecto de una recta
<!-- ejercicio: U2.27 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
En un editor gráfico se refleja el plano respecto de la recta $r:\ y=2x$. La reflexión $T:\mathbb{R}^2\to\mathbb{R}^2$ deja fijos los puntos de $r$ y manda cada vector perpendicular a $r$ en su opuesto. Sea $B=\{(1,2),(-2,1)\}$, donde el primer vector es director de $r$ y el segundo es perpendicular a $r$.

a) Hallar $M(T)_B$.

b) Hallar la matriz canónica $M(T)_E$ y la fórmula de $T(x,y)$.

c) Calcular la imagen del punto $(3,1)$ y comprobar que conserva su distancia al origen.

d) Probar que $T\circ T=\operatorname{id}$, hallar $T^{-1}$ y el determinante de $M(T)_E$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En la base $B$ la reflexión es trivial (fija un vector y cambia de signo el otro); la matriz en la base canónica se obtiene con el cambio de base.

**a)** $T(1,2)=(1,2)$ (está en $r$) y $T(-2,1)=(2,-1)=-(-2,1)$. Entonces las columnas son $(1,0)$ y $(0,-1)$:
$$
M(T)_B=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

**b)** Con $C_{BE}=\begin{pmatrix}1&-2\\2&1\end{pmatrix}$ (columnas los vectores de $B$), de determinante 5, y $C_{EB}=C_{BE}^{-1}=\tfrac15\begin{pmatrix}1&2\\-2&1\end{pmatrix}$:
$$
M(T)_E=C_{BE}\,M(T)_B\,C_{EB}=\begin{pmatrix}1&-2\\2&1\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\frac15\begin{pmatrix}1&2\\-2&1\end{pmatrix}=\frac15\begin{pmatrix}1&2\\2&-1\end{pmatrix}\begin{pmatrix}1&2\\-2&1\end{pmatrix}=\frac15\begin{pmatrix}-3&4\\4&3\end{pmatrix}.
$$
Es decir,
$$
T(x,y)=\left(\frac{-3x+4y}{5},\ \frac{4x+3y}{5}\right).
$$

**c)** $T(3,1)=\left(\frac{-9+4}{5},\ \frac{12+3}{5}\right)=(-1,3)$. Distancias al origen: $\sqrt{3^2+1^2}=\sqrt{10}$ y $\sqrt{(-1)^2+3^2}=\sqrt{10}$. Con coordenadas: $[(3,1)]_B=(1,-1)$, que $M(T)_B$ transforma en $(1,1)$, esto es $(1,2)+(-2,1)=(-1,3)$, mismo resultado.

**d)** $M(T)_B^2=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, así que $T\circ T=\operatorname{id}$ (el producto $M(T)_E^2=C_{BE}M(T)_B^2C_{EB}=I$). Entonces $T$ es isomorfismo y $T^{-1}=T$. El determinante es $\det M(T)_E=\det M(T)_B=-1$ (la matriz es semejante a $M(T)_B$): las reflexiones invierten la orientación.

**Comprobación.** $M(T)_E(1,2)^t=\tfrac15(-3+8,\ 4+6)=(1,2)$ ✓ y $M(T)_E(-2,1)^t=\tfrac15(6+4,\ -8+3)=(2,-1)$ ✓.

:::tip[Resultado]
$M(T)_B=\operatorname{diag}(1,-1)$; $M(T)_E=\tfrac15\begin{pmatrix}-3&4\\4&3\end{pmatrix}$; $T(3,1)=(-1,3)$; $T\circ T=\operatorname{id}$, $T^{-1}=T$, $\det=-1$.
:::

</details>
