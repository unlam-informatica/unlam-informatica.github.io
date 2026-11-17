---
title: Práctica — Nivel intermedio
description: Doce ejercicios resueltos de espacios con producto interno con productos no usuales. Parámetros, verdadero o falso, Gram-Schmidt en R³ y P₂, complementos, proyección por tres métodos, cuadrados mínimos, similitud coseno y códigos en Z₂ⁿ.
slug: algebra-ii/unidad-4/practica/nivel-intermedio
sidebar:
  order: 2
  label: Nivel intermedio
---

Esta página sigue al [nivel inicial](/algebra-ii/unidad-4/practica/nivel-inicial/) con ejercicios que combinan varias ideas y usan los productos no usuales de la cátedra (matricial, de la traza, por evaluación y ponderado). Presupone las ocho lecciones de la unidad: [4.1 Producto interno](/algebra-ii/unidad-4/teoria/producto-interno/), [4.2 Norma, distancia y ángulo](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/), [4.3 Ortogonalidad](/algebra-ii/unidad-4/teoria/ortogonalidad/), [4.4 Gram-Schmidt](/algebra-ii/unidad-4/teoria/gram-schmidt/), [4.5 Complemento ortogonal](/algebra-ii/unidad-4/teoria/complemento-ortogonal/), [4.6 Proyección y distancia](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/), [4.7 Cuadrados mínimos](/algebra-ii/unidad-4/teoria/cuadrados-minimos/) y [4.8 Códigos y $\mathbb{Z}_2^n$](/algebra-ii/unidad-4/teoria/codigos-y-z2/).

Cómo usarla: intentá cada ejercicio sin mirar la resolución; si te trabás, leé solo la **Estrategia** y volvé a intentar. La **Comprobación** de cada resolución es parte del ejercicio: hacela siempre en tu propia resolución. Los enunciados son originales de este manual. Los ejercicios siguen en el [nivel avanzado](/algebra-ii/unidad-4/practica/nivel-avanzado/).

Convenciones: en $P_2[\mathbb{R}]$ la base canónica es $E=\{1,x,x^2\}$; en $\mathbb{R}^{2\times2}$ el producto es $\langle A,B\rangle=\operatorname{tr}(B^tA)$ salvo que se indique otro; $\mathcal C$ es un código lineal y $\mathcal C^\perp$ su dual.

### Ejercicio 9 · Un producto interno con parámetro
<!-- ejercicio: U4.09 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $k\in\mathbb{R}$ se define en $\mathbb{R}^2$ la función $\langle x,y\rangle_k=x_1y_1+k\,x_1y_2+k\,x_2y_1+4x_2y_2$.

a) Hallar todos los valores de $k$ para los cuales $\langle\ ,\ \rangle_k$ es un producto interno.

b) Para $k=1$, calcular $\lVert(2,-1)\rVert$ y el ángulo entre $e_1=(1,0)$ y $e_2=(0,1)$.

c) Verificar que para $k=2$ la función no es un producto interno, exhibiendo un vector no nulo de norma cero.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La función es $x^tM_ky$ con $M_k=\begin{pmatrix}1&k\\k&4\end{pmatrix}$, simétrica para todo $k$. Entonces es producto interno si y solo si $M_k$ es definida positiva: $m_{11}>0$ y $\det M_k>0$.

**a)** $m_{11}=1>0$ siempre y $\det M_k=4-k^2$. Se pide $4-k^2>0$, es decir $-2<k<2$. Para esos $k$, $\langle x,x\rangle=x_1^2+2kx_1x_2+4x_2^2=(x_1+kx_2)^2+(4-k^2)x_2^2$ es positivo salvo en $x=0$, lo que confirma el criterio.

**b)** Para $k=1$: $\langle(2,-1),(2,-1)\rangle=4+2\cdot1\cdot(2)(-1)+4=4-4+4=4$, luego $\lVert(2,-1)\rVert=2$. Para el ángulo: $\langle e_1,e_2\rangle=k=1$, $\lVert e_1\rVert=1$ y $\lVert e_2\rVert=\sqrt4=2$. Entonces $\cos\angle(e_1,e_2)=\dfrac{1}{1\cdot2}=\dfrac12$ y el ángulo es $\dfrac\pi3$.

**c)** Para $k=2$, $\det M_2=0$. El vector $(2,-1)$ cumple $\langle(2,-1),(2,-1)\rangle_2=4+2\cdot2\cdot(2)(-1)+4\cdot1=4-8+4=0$ con $(2,-1)\neq0$: falla la positividad definida.

**Comprobación.** Para $k=1$, $(x_1+x_2)^2+3x_2^2$ evaluado en $(2,-1)$ da $1+3=4$, igual que arriba. Para $k=3$ (fuera del intervalo), $\langle(3,-1),(3,-1)\rangle_3=9-18+4=-5<0$.

:::tip[Resultado]
$\langle\ ,\ \rangle_k$ es producto interno si y solo si $-2<k<2$. Para $k=1$: $\lVert(2,-1)\rVert=2$ y $\angle(e_1,e_2)=\pi/3$. Para $k=2$, $\lVert(2,-1)\rVert=0$.
:::

</details>

### Ejercicio 10 · Verdadero o falso con justificación
<!-- ejercicio: U4.10 | nivel: intermedio | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
En un espacio euclídeo $(V,\langle\ ,\ \rangle)$, decidir si cada afirmación es verdadera o falsa y justificar con una demostración o un contraejemplo.

a) Si $u\perp v$ y $u\perp w$, entonces $u\perp(\alpha v+\beta w)$ para todo $\alpha,\beta\in\mathbb{R}$.

b) Si $u\neq0$ y $\langle u,v\rangle=\langle u,w\rangle$, entonces $v=w$.

c) En $\mathbb{R}^3$ con el producto usual existen cuatro vectores no nulos, ortogonales de a pares.

d) Si $\lVert u\rVert=\lVert v\rVert$, entonces $(u+v)\perp(u-v)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las afirmaciones verdaderas se prueban con las propiedades del producto (linealidad, simetría) y las falsas con un ejemplo concreto verificado.

**a) Verdadera.** Por linealidad, $\langle u,\alpha v+\beta w\rangle=\alpha\langle u,v\rangle+\beta\langle u,w\rangle=\alpha\cdot0+\beta\cdot0=0$. (Es lo mismo que decir que $\{u\}^\perp$ es un subespacio.)

**b) Falsa.** Alcanza con ver que la igualdad solo dice $\langle u,v-w\rangle=0$, es decir $v-w\perp u$, no $v=w$. Contraejemplo en $\mathbb{R}^2$ con el producto usual: $u=(1,1)$, $v=(1,0)$, $w=(0,1)$. Entonces $\langle u,v\rangle=1=\langle u,w\rangle$ con $v\neq w$.

**c) Falsa.** Un conjunto de vectores no nulos ortogonales de a pares es linealmente independiente. Cuatro vectores LI en $\mathbb{R}^3$ es imposible, pues $\dim\mathbb{R}^3=3$. (Se pueden hallar tres, como $(1,0,0),(0,1,0),(0,0,1)$, pero no cuatro.)

**d) Verdadera.** $\langle u+v,u-v\rangle=\langle u,u\rangle-\langle u,v\rangle+\langle v,u\rangle-\langle v,v\rangle=\lVert u\rVert^2-\lVert v\rVert^2=0$, usando la simetría para cancelar los términos cruzados. (Geométricamente: las diagonales de un rombo son perpendiculares.)

**Comprobación.** En b), $v-w=(1,-1)$ y $u\cdot(v-w)=1-1=0$, como se esperaba. En d) con $u=(1,2)$ y $v=(2,1)$ (misma norma $\sqrt5$): $u+v=(3,3)$, $u-v=(-1,1)$ y $(3,3)\cdot(-1,1)=0$.

:::tip[Resultado]
a) V, d) V (demostraciones). b) F (contraejemplo $u=(1,1)$, $v=(1,0)$, $w=(0,1)$). c) F (cuatro ortogonales no nulos serían LI en $\mathbb{R}^3$).
:::

</details>

### Ejercicio 11 · Gram-Schmidt en $\mathbb{R}^3$
<!-- ejercicio: U4.11 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^3$ con el producto usual sea $B=\{(1,2,2),(1,1,0),(0,1,1)\}$, que es una base.

a) Aplicar Gram-Schmidt a $B$, en ese orden, para obtener una base ortogonal $B'$ (escalar los vectores para evitar fracciones) y una base ortonormal.

b) Hallar $[v]_{B'}$ para $v=(3,0,3)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con $v_1,v_2,v_3$ los vectores de $B$, se define $w_1=v_1$ y $w_k=v_k-\sum_{j<k}\dfrac{\langle v_k,w_j\rangle}{\langle w_j,w_j\rangle}w_j$. Cada $w_k$ queda ortogonal a los anteriores y genera con ellos el mismo subespacio que $v_1,\dots,v_k$. Un múltiplo no nulo de un $w_k$ sigue siendo ortogonal a los demás, y se puede usar en los pasos siguientes.

**a)** $w_1=(1,2,2)$, con $\langle w_1,w_1\rangle=9$.

Paso 2: $\langle v_2,w_1\rangle=1+2+0=3$, entonces
$w_2=(1,1,0)-\frac39(1,2,2)=\left(\frac23,\frac13,-\frac23\right)$. Lo reescalamos por $3$: $w_2'=(2,1,-2)$, con $\langle w_2',w_2'\rangle=9$.

Paso 3: $\langle v_3,w_1\rangle=0+2+2=4$ y $\langle v_3,w_2'\rangle=0+1-2=-1$. Entonces
$$
w_3=(0,1,1)-\frac49(1,2,2)+\frac19(2,1,-2)=\left(-\frac29,\frac29,-\frac19\right)=-\frac19(2,-2,1).
$$
Tomamos $w_3'=(2,-2,1)$, con norma al cuadrado $9$.

La base ortogonal es $B'=\{(1,2,2),(2,1,-2),(2,-2,1)\}$. Como las tres normas valen $3$, la base ortonormal es
$$
\left\{\tfrac13(1,2,2),\ \tfrac13(2,1,-2),\ \tfrac13(2,-2,1)\right\}.
$$

**b)** $\langle v,w_1\rangle=3+0+6=9$, $\langle v,w_2'\rangle=6+0-6=0$ y $\langle v,w_3'\rangle=6+0+3=9$. Las coordenadas son $c_i=\langle v,w_i\rangle/9$: $[v]_{B'}=(1,0,1)^t$.

**Comprobación.** $1\cdot(1,2,2)+0\cdot(2,1,-2)+1\cdot(2,-2,1)=(3,0,3)=v$. Además $w_1\cdot w_2'=2+2-4=0$, $w_1\cdot w_3'=2-4+2=0$ y $w_2'\cdot w_3'=4-2-2=0$.

:::tip[Resultado]
$B'=\{(1,2,2),(2,1,-2),(2,-2,1)\}$ es ortogonal (y $\tfrac13B'$, ortonormal). $[v]_{B'}=(1,0,1)^t$.
:::

</details>

### Ejercicio 12 · Gram-Schmidt en $P_2[\mathbb{R}]$
<!-- ejercicio: U4.12 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $P_2[\mathbb{R}]$ se considera el producto interno $\langle p,q\rangle=p(0)q(0)+p(1)q(1)+p(2)q(2)$.

a) Aplicar Gram-Schmidt a la base $\{1,x,x^2\}$ y obtener una base ortogonal de polinomios de coeficientes enteros.

b) Calcular la norma de cada polinomio de esa base.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El producto es el producto punto de las ternas de valores en $0,1,2$. Gram-Schmidt se aplica igual que siempre, calculando los productos con esas ternas: $1\leftrightarrow(1,1,1)$, $x\leftrightarrow(0,1,2)$, $x^2\leftrightarrow(0,1,4)$.

**a)** $w_1=1$, con $\langle1,1\rangle=3$.

Paso 2: $\langle x,1\rangle=0+1+2=3$, luego $w_2=x-\frac33\cdot1=x-1$, con valores $(-1,0,1)$ y $\langle w_2,w_2\rangle=2$.

Paso 3: $\langle x^2,1\rangle=0+1+4=5$ y $\langle x^2,x-1\rangle=0\cdot(-1)+1\cdot0+4\cdot1=4$. Entonces
$$
w_3=x^2-\frac53\cdot1-\frac42(x-1)=x^2-2x+\frac13.
$$
Los valores de $w_3$ en $0,1,2$ son $(\frac13,-\frac23,\frac13)$. Multiplicando por $3$ se obtiene $3x^2-6x+1$, con valores $(1,-2,1)$.

Una base ortogonal con coeficientes enteros es $\{1,\ x-1,\ 3x^2-6x+1\}$.

**b)** $\lVert1\rVert^2=3$, $\lVert x-1\rVert^2=(-1)^2+0+1^2=2$ y $\lVert3x^2-6x+1\rVert^2=1+4+1=6$. Las normas son $\sqrt3$, $\sqrt2$ y $\sqrt6$.

**Comprobación.** $\langle1,3x^2-6x+1\rangle=1-2+1=0$, $\langle x-1,3x^2-6x+1\rangle=(-1)(1)+0\cdot(-2)+1\cdot1=0$ y $\langle1,x-1\rangle=-1+0+1=0$.

:::tip[Resultado]
Base ortogonal $\{1,\ x-1,\ 3x^2-6x+1\}$ con normas $\sqrt3$, $\sqrt2$ y $\sqrt6$.
:::

</details>

### Ejercicio 13 · Complemento ortogonal en matrices
<!-- ejercicio: U4.13 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^{2\times2}$ con $\langle A,B\rangle=\operatorname{tr}(B^tA)$ sea
$S=\operatorname{gen}\left\{\begin{pmatrix}1&1\\0&1\end{pmatrix},\begin{pmatrix}0&1\\1&0\end{pmatrix}\right\}$.

a) Hallar una base de $S^\perp$ y verificar la relación entre las dimensiones.

b) Comprobar que $M=\begin{pmatrix}-2&1\\-1&1\end{pmatrix}$ pertenece a $S^\perp$ y escribirla en la base hallada.

c) ¿Pertenece la identidad a $S^\perp$?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Identificamos cada matriz $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ con $(a,b,c,d)\in\mathbb{R}^4$ (el producto de la traza es el usual de $\mathbb{R}^4$ con esa identificación) y planteamos ortogonalidad con cada generador.

**a)** Sea $B=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Las condiciones $\langle B,G_1\rangle=0$ y $\langle B,G_2\rangle=0$, con $G_1=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ y $G_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, son
$$
\begin{cases}a+b+d=0\\ b+c=0\end{cases}
$$
Con $b$ y $d$ libres: $c=-b$ y $a=-b-d$. Entonces
$$
B=b\begin{pmatrix}-1&1\\-1&0\end{pmatrix}+d\begin{pmatrix}-1&0\\0&1\end{pmatrix},
$$
y una base de $S^\perp$ es $\left\{\begin{pmatrix}-1&1\\-1&0\end{pmatrix},\begin{pmatrix}-1&0\\0&1\end{pmatrix}\right\}$. Como $G_1$ y $G_2$ son LI, $\dim S=2$ y $\dim S^\perp=2$: se cumple $\dim S+\dim S^\perp=4=\dim\mathbb{R}^{2\times2}$.

**b)** Para $M$: $a+b+d=-2+1+1=0$ y $b+c=1-1=0$, luego $M\in S^\perp$. En la base, $b=1$ y $d=1$: $M=1\cdot\begin{pmatrix}-1&1\\-1&0\end{pmatrix}+1\cdot\begin{pmatrix}-1&0\\0&1\end{pmatrix}$.

**c)** Para $I$: $a+b+d=1+0+1=2\neq0$. **No pertenece** a $S^\perp$ ($\langle I,G_1\rangle=2$).

**Comprobación.** $\begin{pmatrix}-1&1\\-1&0\end{pmatrix}+\begin{pmatrix}-1&0\\0&1\end{pmatrix}=\begin{pmatrix}-2&1\\-1&1\end{pmatrix}=M$. Y $\langle\begin{pmatrix}-1&0\\0&1\end{pmatrix},G_1\rangle=-1+0+0+1=0$, $\langle\begin{pmatrix}-1&0\\0&1\end{pmatrix},G_2\rangle=0$.

:::tip[Resultado]
$S^\perp$ tiene base $\left\{\begin{pmatrix}-1&1\\-1&0\end{pmatrix},\begin{pmatrix}-1&0\\0&1\end{pmatrix}\right\}$ y $\dim S^\perp=2$. $M=B_1+B_2\in S^\perp$ e $I\notin S^\perp$.
:::

</details>

### Ejercicio 14 · Complemento con un producto no usual
<!-- ejercicio: U4.14 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^3$ se define $\langle x,y\rangle=x_1y_1+2x_2y_2+3x_3y_3$ y sea $S=\operatorname{gen}\{(1,0,1),(0,1,1)\}$.

a) Hallar $S^\perp$ respecto de este producto.

b) Hallar el complemento ortogonal de $S$ respecto del producto usual y compararlo con el anterior.

c) Verificar que $\dim S+\dim S^\perp=3$ en ambos casos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $x\in S^\perp$ si y solo si $\langle x,s\rangle=0$ para cada generador $s$ de $S$. Con el producto ponderado, cada condición es una ecuación con los coeficientes ponderados.

**a)** Para $s_1=(1,0,1)$: $\langle x,s_1\rangle=x_1+3x_3=0$. Para $s_2=(0,1,1)$: $\langle x,s_2\rangle=2x_2+3x_3=0$. Con $x_3=t$ libre, $x_1=-3t$ y $x_2=-\frac32t$. Tomando $t=2$:
$$
S^\perp=\operatorname{gen}\{(-6,-3,2)\}.
$$

**b)** Con el producto usual: $x_1+x_3=0$ y $x_2+x_3=0$, o sea $x=t(-1,-1,1)$:
$S^{\perp_{\text{usual}}}=\operatorname{gen}\{(1,1,-1)\}$. Son **rectas distintas**: $(-6,-3,2)$ no es múltiplo de $(1,1,-1)$. El complemento ortogonal depende del producto.

**c)** En ambos casos $\dim S=2$ (los generadores son LI) y el complemento es una recta: $2+1=3=\dim\mathbb{R}^3$.

**Comprobación.** $\langle(-6,-3,2),(1,0,1)\rangle=-6+0+6=0$ y $\langle(-6,-3,2),(0,1,1)\rangle=0+2(-3)(1)+3\cdot2\cdot1=-6+6=0$.

:::tip[Resultado]
Con el producto ponderado, $S^\perp=\operatorname{gen}\{(-6,-3,2)\}$; con el usual, $\operatorname{gen}\{(1,1,-1)\}$. En ambos $\dim S+\dim S^\perp=3$.
:::

</details>

### Ejercicio 15 · Proyección por tres métodos
<!-- ejercicio: U4.15 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^3$ con el producto usual sea $S=\{(x,y,z):x+y-2z=0\}$ y $v=(4,2,0)$. Calcular $\operatorname{proy}_S(v)$ y $d(v,S)$ de tres maneras:

a) con una base ortogonal de $S$;

b) con la proyección sobre $S^\perp$;

c) con las ecuaciones normales a partir de la base $\{(1,-1,0),(2,0,1)\}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los tres métodos deben dar el mismo vector. El primero necesita una base **ortogonal** de $S$; el segundo aprovecha que $S^\perp$ es una recta y usa $v=\operatorname{proy}_S(v)+\operatorname{proy}_{S^\perp}(v)$; el tercero funciona con cualquier base: si $A$ tiene por columnas esa base, $\operatorname{proy}_S(v)=Ax$ donde $A^tAx=A^tv$.

**a)** Los vectores $b_1=(1,-1,0)$ y $b_2=(1,1,1)$ están en $S$ ($1-1-0=0$ y $1+1-2=0$) y son ortogonales ($1-1+0=0$): base ortogonal de $S$ (como $\dim S=2$). Con $v\cdot b_1=2$, $b_1\cdot b_1=2$, $v\cdot b_2=6$ y $b_2\cdot b_2=3$:
$$
\operatorname{proy}_S(v)=\frac22(1,-1,0)+\frac63(1,1,1)=(1,-1,0)+(2,2,2)=(3,1,2).
$$

**b)** $S^\perp=\operatorname{gen}\{n\}$ con $n=(1,1,-2)$ (los coeficientes de la ecuación). $v\cdot n=4+2-0=6$ y $n\cdot n=6$, entonces $\operatorname{proy}_{S^\perp}(v)=\frac66n=(1,1,-2)$ y
$$
\operatorname{proy}_S(v)=v-\operatorname{proy}_{S^\perp}(v)=(4,2,0)-(1,1,-2)=(3,1,2).
$$
La distancia es $d(v,S)=\lVert\operatorname{proy}_{S^\perp}(v)\rVert=\sqrt6$.

**c)** Sea $A=\begin{pmatrix}1&2\\-1&0\\0&1\end{pmatrix}$. Entonces $A^tA=\begin{pmatrix}2&2\\2&5\end{pmatrix}$ y $A^tv=\begin{pmatrix}2\\8\end{pmatrix}$. Resolvemos $A^tAx=A^tv$: $\det(A^tA)=6$ y
$$
x=\frac16\begin{pmatrix}5&-2\\-2&2\end{pmatrix}\begin{pmatrix}2\\8\end{pmatrix}=\frac16\begin{pmatrix}-6\\12\end{pmatrix}=\begin{pmatrix}-1\\2\end{pmatrix},
$$
y $\operatorname{proy}_S(v)=-1\cdot(1,-1,0)+2\cdot(2,0,1)=(3,1,2)$.

**Comprobación.** Los tres métodos dan $(3,1,2)$, que cumple $3+1-4=0$ (está en $S$). Además $\lVert v-\operatorname{proy}_S(v)\rVert=\lVert(1,1,-2)\rVert=\sqrt6$.

:::tip[Resultado]
$\operatorname{proy}_S(v)=(3,1,2)$ y $d(v,S)=\sqrt6$ por los tres métodos.
:::

</details>

### Ejercicio 16 · Tres contraejemplos
<!-- ejercicio: U4.16 | nivel: intermedio | tipo: contraejemplo | verificacion: sympy -->

:::note[Enunciado]
Refutar cada afirmación con un contraejemplo explícito y verificado.

a) «Si $\{b_1,b_2\}$ es una base cualquiera de un subespacio $S$, entonces $\operatorname{proy}_S(v)=\dfrac{\langle v,b_1\rangle}{\langle b_1,b_1\rangle}b_1+\dfrac{\langle v,b_2\rangle}{\langle b_2,b_2\rangle}b_2$.» (Usar $\mathbb{R}^2$ con el producto usual.)

b) «El complemento ortogonal de un subespacio no depende del producto interno.» (Usar $S=\operatorname{gen}\{(1,0,1),(1,1,0)\}$ en $\mathbb{R}^3$ y el producto $\langle x,y\rangle=x^tMy$ con $M=\begin{pmatrix}2&1&0\\1&2&0\\0&0&3\end{pmatrix}$.)

c) «Si $u\perp v$ y $v\perp w$, entonces $u\perp w$.» (Usar el producto usual de $\mathbb{R}^3$.)
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada contraejemplo se arma con datos chicos y se verifica con cuentas explícitas. En a) conviene elegir $v\in S$, porque entonces la proyección tiene que ser $v$ mismo.

**a)** Sea $S=\mathbb{R}^2$ con la base $b_1=(1,0)$ y $b_2=(1,1)$ (no ortogonal: $b_1\cdot b_2=1$). Para $v=(0,1)\in S$ la proyección es $v$. Pero la fórmula da
$$
\frac{0}{1}(1,0)+\frac{1}{2}(1,1)=\left(\tfrac12,\tfrac12\right)\neq(0,1).
$$
La fórmula exige una base **ortogonal**.

**b)** $M$ es simétrica con $m_{11}=2>0$, menores principales $2$, $3$ y $9$: es definida positiva. Con el producto usual: $x_1+x_3=0$ y $x_1+x_2=0$ dan $S^\perp=\operatorname{gen}\{(1,-1,-1)\}$. Con $M$: $Ms_1=(2,1,3)$ y $Ms_2=(3,3,0)$ para $s_1=(1,0,1)$ y $s_2=(1,1,0)$, y las condiciones son $2x_1+x_2+3x_3=0$ y $3x_1+3x_2=0$. De la segunda $x_2=-x_1$; de la primera $x_1+3x_3=0$, o sea $x=t(-3,3,1)$. Entonces
$$
S^{\perp_M}=\operatorname{gen}\{(-3,3,1)\}\neq\operatorname{gen}\{(1,-1,-1)\}=S^{\perp_{\text{usual}}}.
$$

**c)** Tomamos $u=(1,0,0)$, $v=(0,1,0)$ y $w=(2,0,1)$. Entonces $u\cdot v=0$ y $v\cdot w=0$, pero $u\cdot w=2\neq0$. La ortogonalidad **no es transitiva**.

**Comprobación.** En b), $(-3,3,1)^tMs_1=-6+3+3=0$ y $(-3,3,1)^tMs_2=-9+9=0$, mientras que $(1,-1,-1)^tMs_1=2-1-3=-2\neq0$: el vector usual no es ortogonal a $s_1$ con $M$.

:::tip[Resultado]
a) $S=\mathbb{R}^2$, $\{(1,0),(1,1)\}$, $v=(0,1)$: la fórmula da $(\frac12,\frac12)$. b) $S^{\perp_M}=\operatorname{gen}\{(-3,3,1)\}$ y $S^{\perp_{\text{usual}}}=\operatorname{gen}\{(1,-1,-1)\}$. c) $u=(1,0,0)$, $v=(0,1,0)$, $w=(2,0,1)$.
:::

</details>

### Ejercicio 17 · Recta de ajuste para tiempos de respuesta
<!-- ejercicio: U4.17 | nivel: intermedio | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Un servicio de consultas respondió, para una base de $n$ millones de registros, en $t$ milisegundos:

| $n$ (millones) | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $t$ (ms) | 3 | 8 | 10 | 14 | 15 |

a) Plantear el sistema $Ax=b$ del modelo $t=a+bn$ y escribir las ecuaciones normales.

b) Hallar la recta de cuadrados mínimos y los residuos.

c) Verificar que el vector de residuos es ortogonal a las columnas de $A$ y calcular el error cuadrático $\lVert b-Ax\rVert^2$.

d) Estimar el tiempo para $n=8$ millones.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con $x=(a,b)^t$, las cinco mediciones dan cinco ecuaciones $a+bn_i=t_i$ en dos incógnitas, en general incompatibles. La solución de cuadrados mínimos es la que cumple $A^tAx=A^tb$, y el vector de residuos $r=b-Ax$ es ortogonal a $\operatorname{col}(A)$.

**a)** Con $A=\begin{pmatrix}1&1\\1&2\\1&3\\1&4\\1&5\end{pmatrix}$ y $b=(3,8,10,14,15)^t$:
$$
A^tA=\begin{pmatrix}5&15\\15&55\end{pmatrix},\qquad A^tb=\begin{pmatrix}50\\180\end{pmatrix}
$$
(pues $\sum t_i=50$ y $\sum n_it_i=3+16+30+56+75=180$). Las ecuaciones normales son $5a+15b=50$ y $15a+55b=180$.

**b)** Dividimos la primera por $5$: $a+3b=10$. De la segunda, $3a+11b=36$. Con $a=10-3b$: $30-9b+11b=36$, o sea $b=3$ y $a=1$. La recta es $t=1+3n$. Los valores ajustados son $4,7,10,13,16$ y los residuos $r=b-Ax=(-1,1,0,1,-1)^t$.

**c)** $r\cdot(1,1,1,1,1)=-1+1+0+1-1=0$ y $r\cdot(1,2,3,4,5)=-1+2+0+4-5=0$: $r\perp\operatorname{col}(A)$. El error cuadrático es $\lVert r\rVert^2=1+1+0+1+1=4$.

**d)** Para $n=8$: $t=1+3\cdot8=25$ ms.

**Comprobación.** Las ecuaciones normales se cumplen: $5\cdot1+15\cdot3=50$ y $15\cdot1+55\cdot3=180$.

:::tip[Resultado]
Recta $t=1+3n$, residuos $(-1,1,0,1,-1)$, error cuadrático $4$ y estimación de $25$ ms para $n=8$ (una extrapolación: confiable solo si el crecimiento sigue siendo lineal).
:::

</details>

### Ejercicio 18 · Similitud coseno entre documentos
<!-- ejercicio: U4.18 | nivel: intermedio | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Un buscador representa cada documento por el vector de frecuencias de los términos (algoritmo, dato, red, archivo). La consulta es $q=(2,2,1,0)$ y los documentos son $D_1=(2,1,2,0)$, $D_2=(0,1,2,2)$ y $D_3=(4,4,2,0)$.

a) Calcular la similitud coseno $\cos\angle(q,D_i)$ de la consulta con cada documento.

b) Calcular las distancias euclídeas $d(q,D_i)$.

c) Ordenar los documentos por similitud coseno y por distancia, y explicar la diferencia.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se usa el producto usual de $\mathbb{R}^4$. El coseno depende solo de la dirección del vector (mide el parecido en la proporción de términos) y no de su longitud, que en un documento refleja su extensión.

**a)** $\lVert q\rVert^2=4+4+1+0=9$, $\lVert D_1\rVert^2=4+1+4+0=9$, $\lVert D_2\rVert^2=0+1+4+4=9$ y $\lVert D_3\rVert^2=16+16+4+0=36$. Los productos: $q\cdot D_1=4+2+2+0=8$, $q\cdot D_2=0+2+2+0=4$ y $q\cdot D_3=8+8+2+0=18$. Entonces
$$
\cos\angle(q,D_1)=\frac{8}{3\cdot3}=\frac89,\qquad
\cos\angle(q,D_2)=\frac{4}{3\cdot3}=\frac49,\qquad
\cos\angle(q,D_3)=\frac{18}{3\cdot6}=1.
$$

**b)** $q-D_1=(0,1,-1,0)$, $q-D_2=(2,1,-1,-2)$ y $q-D_3=(-2,-2,-1,0)$, de donde
$$
d(q,D_1)=\sqrt2,\qquad d(q,D_2)=\sqrt{10},\qquad d(q,D_3)=3.
$$

**c)** Por coseno: $D_3$ (1), $D_1$ ($\frac89$), $D_2$ ($\frac49$). Por distancia: $D_1$ ($\sqrt2\approx1{,}41$), $D_3$ ($3$), $D_2$ ($\sqrt{10}\approx3{,}16$). El documento $D_3=2q$ trata exactamente los mismos temas en la misma proporción, pero es más largo, así que queda lejos en distancia y a ángulo $0$ en coseno. Para comparar contenido con documentos de distinta extensión, el coseno es más adecuado.

**Comprobación.** Como $0\le\cos\le1$ para vectores de frecuencias (entradas no negativas), y Cauchy-Schwarz asegura $\lvert q\cdot D_i\rvert\le\lVert q\rVert\lVert D_i\rVert$: $8\le9$, $4\le9$, $18\le18$ (igualdad, porque $D_3$ es múltiplo de $q$).

:::tip[Resultado]
Cosenos $\frac89$, $\frac49$ y $1$; distancias $\sqrt2$, $\sqrt{10}$ y $3$. El orden por coseno es $D_3,D_1,D_2$ y por distancia $D_1,D_3,D_2$.
:::

</details>

### Ejercicio 19 · El código dual de un código $(5,2)$
<!-- ejercicio: U4.19 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C\subseteq\mathbb{Z}_2^5$ el código generado por $g_1=10110$ y $g_2=01011$.

a) Listar las palabras de $\mathcal C$ y hallar la distancia mínima.

b) Hallar una base de $\mathcal C^\perp$ y su dimensión.

c) Decidir si $\mathcal C\subseteq\mathcal C^\perp$ y si $\mathcal C$ es autodual.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $\mathcal C^\perp=\{x:x\cdot g=0\ \forall g\in\mathcal C\}=\operatorname{nul}(G)$, con $G$ la matriz que tiene por filas $g_1$ y $g_2$ (basta ortogonalidad con los generadores). Sale $\dim\mathcal C^\perp=n-k$.

**a)** Las palabras son $0=00000$, $g_1=10110$, $g_2=01011$ y $g_1+g_2=11101$. Los pesos de las no nulas son $3$, $3$ y $4$, de modo que $d(\mathcal C)=3$.

**b)** $G=\begin{pmatrix}1&0&1&1&0\\0&1&0&1&1\end{pmatrix}$ ya está escalonada reducida, con pivotes en las columnas $1$ y $2$ y variables libres $x_3,x_4,x_5$. Las ecuaciones son $x_1=x_3+x_4$ y $x_2=x_4+x_5$ (en $\mathbb{Z}_2$ el signo menos desaparece). Dando valores a las libres:
$x_3=1$: $10100$; $x_4=1$: $11010$; $x_5=1$: $01001$. Una base es $\{10100,\ 11010,\ 01001\}$ y $\dim\mathcal C^\perp=3=5-2$.

**c)** $g_1\cdot g_1=1+0+1+1+0=1\neq0$ (peso $3$ impar), de modo que $g_1\notin\mathcal C^\perp$ y **$\mathcal C\not\subseteq\mathcal C^\perp$**. En particular no es autodual (además, $\dim\mathcal C=2\neq3=\dim\mathcal C^\perp$).

**Comprobación.** $10100\cdot g_1=1+1=0$, $10100\cdot g_2=0$; $11010\cdot g_1=1+1=0$, $11010\cdot g_2=1+1=0$; $01001\cdot g_1=0$, $01001\cdot g_2=1+1=0$.

:::tip[Resultado]
$\mathcal C=\{00000,10110,01011,11101\}$ con $d(\mathcal C)=3$. $\mathcal C^\perp$ tiene base $\{10100,11010,01001\}$ y dimensión $3$. $\mathcal C$ no es autodual.
:::

</details>

### Ejercicio 20 · Distancia mínima, detección y corrección
<!-- ejercicio: U4.20 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C\subseteq\mathbb{Z}_2^7$ el código lineal con matriz generadora
$$
G=\begin{pmatrix}1&0&1&0&1&0&1\\0&1&1&0&0&1&1\\0&0&0&1&1&1&1\end{pmatrix}.
$$

a) Listar las $8$ palabras y calcular $d(\mathcal C)$.

b) ¿Cuántos errores detecta y cuántos corrige?

c) Se recibe $r=1110011$. Decodificarla por mínima distancia.

d) Se recibe $r'=1001101$. ¿Se detecta un error? ¿Se puede corregir de forma única?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En un código lineal $d_H(u,v)=w(u+v)$ y $u+v\in\mathcal C$, de modo que $d(\mathcal C)$ es el peso mínimo de una palabra no nula. Un código de distancia mínima $d$ detecta hasta $d-1$ errores y corrige hasta $\lfloor(d-1)/2\rfloor$.

**a)** Las combinaciones de las filas $g_1,g_2,g_3$ son
$$
\begin{aligned}
&0000000,\ 1010101\ (g_1),\ 0110011\ (g_2),\ 0001111\ (g_3),\\
&1100110\ (g_1+g_2),\ 1011010\ (g_1+g_3),\ 0111100\ (g_2+g_3),\ 1101001\ (g_1+g_2+g_3).
\end{aligned}
$$
Las siete no nulas tienen peso $4$, luego $d(\mathcal C)=4$.

**b)** Detecta hasta $d-1=3$ errores y corrige hasta $\lfloor3/2\rfloor=1$.

**c)** Las distancias de $r=1110011$ a las palabras se obtienen con $w(r+c)$. La menor es a $0110011$: $r+0110011=1000000$, distancia $1$; las demás son $\ge3$. Como hay una única palabra a distancia $1\le1$, se decodifica $\hat c=0110011$ (error en la primera posición).

**d)** $r'=1001101$ no es palabra (no figura en la lista), de modo que se detecta que hubo error. Sus distancias: $2$ a $0001111$, $2$ a $1010101$, $2$ a $1101001$, y las otras cinco palabras están a distancia mayor. Hay **tres palabras a distancia mínima $2$**: no hay corrección única, aunque el error se detecta. Con $d=4$ un patrón de dos errores se puede detectar pero no siempre corregir.

**Comprobación.** $r'+0001111=1000010$ (peso $2$), $r'+1010101=0011000$ (peso $2$) y $r'+1101001=0100100$ (peso $2$). Y $d(r',c)\ge2$ para cada palabra $c$ de la lista.

:::tip[Resultado]
$d(\mathcal C)=4$: detecta $3$ errores y corrige $1$. $r=1110011$ se decodifica como $0110011$. $r'=1001101$ se detecta como errónea pero hay tres palabras a distancia $2$, de modo que no se corrige de forma única.
:::

</details>
