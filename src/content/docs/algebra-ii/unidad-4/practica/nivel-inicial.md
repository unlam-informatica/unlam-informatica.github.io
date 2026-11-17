---
title: Práctica — Nivel inicial
description: Ocho ejercicios resueltos de espacios con producto interno para empezar. Cómo reconocer un producto interno, norma, distancia y ángulo, coordenadas en bases ortogonales, complemento, proyección y producto punto en Z₂ⁿ.
slug: algebra-ii/unidad-4/practica/nivel-inicial
sidebar:
  order: 1
  label: Nivel inicial
---

Esta página reúne los ejercicios básicos de la unidad: decidir si una fórmula define un producto interno, calcular normas, distancias y ángulos con productos no usuales, usar una base ortogonal para hallar coordenadas y proyecciones, calcular un complemento ortogonal y operar con el producto punto de $\mathbb{Z}_2^n$. Presupone las lecciones [4.1 Producto interno](/algebra-ii/unidad-4/teoria/producto-interno/), [4.2 Norma, distancia y ángulo](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/), [4.3 Ortogonalidad](/algebra-ii/unidad-4/teoria/ortogonalidad/) y [4.5 Complemento ortogonal](/algebra-ii/unidad-4/teoria/complemento-ortogonal/); del ejercicio 7 en adelante conviene haber leído [4.6 Proyección y distancia](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/) (solo la fórmula con base ortogonal) y para el ejercicio 8 la primera sección de [4.8 Códigos y $\mathbb{Z}_2^n$](/algebra-ii/unidad-4/teoria/codigos-y-z2/).

Cómo usarla: resolvé cada ejercicio por tu cuenta antes de abrir la resolución, y usá la resolución para comparar el método y, sobre todo, la comprobación final, que conviene hacer siempre. Todos los enunciados son originales de este manual. Los ejercicios siguen en el [nivel intermedio](/algebra-ii/unidad-4/practica/nivel-intermedio/).

Convenciones: en $\mathbb{R}^{2\times 2}$ el producto es $\langle A,B\rangle=\operatorname{tr}(B^tA)$, o sea la suma de los productos entrada a entrada; en $\mathbb{R}^n$, $u\cdot v$ o $\langle u,v\rangle$ es el producto usual cuando no se indica otro.

### Ejercicio 1 · ¿Es un producto interno?
<!-- ejercicio: U4.01 | nivel: inicial | tipo: conceptual | verificacion: sympy -->

:::note[Enunciado]
Para $x=(x_1,x_2)$ e $y=(y_1,y_2)$ en $\mathbb{R}^2$, decidir si cada fórmula define un producto interno. Si lo define, justificarlo; si no, indicar qué axioma falla y dar un ejemplo concreto.

a) $\langle x,y\rangle=2x_1y_1+3x_2y_2$.

b) $\langle x,y\rangle=x_1y_1-x_2y_2$.

c) $\langle x,y\rangle=(x_1+x_2)(y_1+y_2)$.

d) $\langle x,y\rangle=x_1y_1+x_1y_2+x_2y_1+3x_2y_2$.

e) $\langle x,y\rangle=x_1y_1+x_1y_2+2x_2y_1+x_2y_2$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un producto interno debe ser simétrico, lineal en la primera variable y definido positivo ($\langle x,x\rangle>0$ si $x\neq0$). Cuando la fórmula es $x^tMy$ con $M$ simétrica, la simetría y la linealidad se cumplen solas y todo se reduce a decidir si $M$ es definida positiva; en $2\times2$ alcanza con $m_{11}>0$ y $\det M>0$. Para refutar una fórmula se exhibe un caso concreto que rompa un axioma.

**a)** $M=\begin{pmatrix}2&0\\0&3\end{pmatrix}$ es simétrica, con $m_{11}=2>0$ y $\det M=6>0$. Directamente, $\langle x,x\rangle=2x_1^2+3x_2^2>0$ si $x\neq0$. **Es producto interno** (ponderado).

**b)** $\langle(0,1),(0,1)\rangle=-1<0$. **No es producto interno:** falla la positividad.

**c)** La fórmula es simétrica y bilineal, pero $\langle(1,-1),(1,-1)\rangle=(1-1)(1-1)=0$ con $(1,-1)\neq0$. **No es producto interno:** falla que $\langle x,x\rangle=0$ implique $x=0$.

**d)** $M=\begin{pmatrix}1&1\\1&3\end{pmatrix}$ es simétrica, $m_{11}=1>0$ y $\det M=3-1=2>0$. Se puede ver también completando cuadrados: $\langle x,x\rangle=x_1^2+2x_1x_2+3x_2^2=(x_1+x_2)^2+2x_2^2$, que solo se anula si $x_2=0$ y $x_1=0$. **Es producto interno.**

**e)** $\langle(1,0),(0,1)\rangle=1$ pero $\langle(0,1),(1,0)\rangle=2$. **No es producto interno:** falla la simetría (su matriz $\begin{pmatrix}1&1\\2&1\end{pmatrix}$ no es simétrica).

**Comprobación.** En d), $\langle(1,-1),(1,-1)\rangle=1-1-1+3=2>0$, coherente con $(x_1+x_2)^2+2x_2^2=0+2$. En a), el caso límite $\langle(1,0),(1,0)\rangle=2$ y $\langle(0,1),(0,1)\rangle=3$ son positivos.

:::tip[Resultado]
Son productos internos a) y d). No lo son b) (positividad, $\langle(0,1),(0,1)\rangle=-1$), c) (no definido, $\langle(1,-1),(1,-1)\rangle=0$) y e) (no es simétrico).
:::

</details>

### Ejercicio 2 · Norma, distancia y ángulo con un producto ponderado
<!-- ejercicio: U4.02 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^3$ se considera el producto interno $\langle x,y\rangle=x_1y_1+x_2y_2+2x_3y_3$. Sean $u=(1,1,1)$, $v=(1,-1,1)$ y $w=(2,0,-1)$.

a) Calcular $\langle u,v\rangle$, $\lVert u\rVert$, $\lVert v\rVert$ y el ángulo entre $u$ y $v$.

b) Calcular $d(u,v)$.

c) Decidir si $u\perp w$ con este producto y con el producto usual.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se aplica la definición de cada magnitud con el producto dado: $\lVert x\rVert=\sqrt{\langle x,x\rangle}$, $d(x,y)=\lVert x-y\rVert$ y $\cos\angle(x,y)=\dfrac{\langle x,y\rangle}{\lVert x\rVert\lVert y\rVert}$. El tercer peso $2$ cuenta cada vez que aparece la tercera coordenada.

**a)** $\langle u,v\rangle=1\cdot1+1\cdot(-1)+2\cdot1\cdot1=2$. Además $\langle u,u\rangle=1+1+2=4$ y $\langle v,v\rangle=1+1+2=4$, de modo que $\lVert u\rVert=\lVert v\rVert=2$. Entonces

$$
\cos\angle(u,v)=\frac{2}{2\cdot2}=\frac12,\qquad \angle(u,v)=\frac{\pi}{3}.
$$

**b)** $u-v=(0,2,0)$ y $\langle u-v,u-v\rangle=2^2=4$, luego $d(u,v)=2$.

**c)** Con el producto dado, $\langle u,w\rangle=1\cdot2+1\cdot0+2\cdot1\cdot(-1)=0$: **$u\perp w$**. Con el producto usual, $u\cdot w=2+0-1=1\neq0$: **no son ortogonales.** La ortogonalidad depende del producto elegido.

**Comprobación.** Con el producto usual, $u\cdot v=1-1+1=1$ y $\lVert u\rVert=\lVert v\rVert=\sqrt3$, de modo que el ángulo usual es $\arccos\frac13$, distinto de $\frac{\pi}{3}$: el ángulo también depende del producto.

:::tip[Resultado]
$\langle u,v\rangle=2$, $\lVert u\rVert=\lVert v\rVert=2$, $\angle(u,v)=\pi/3$, $d(u,v)=2$. Con este producto $u\perp w$; con el usual no.
:::

</details>

### Ejercicio 3 · El producto de la traza en matrices
<!-- ejercicio: U4.03 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^{2\times2}$ con $\langle A,B\rangle=\operatorname{tr}(B^tA)$ sean
$A=\begin{pmatrix}1&2\\2&0\end{pmatrix}$, $B=\begin{pmatrix}2&-1\\0&2\end{pmatrix}$ y $C=\begin{pmatrix}1&1\\1&1\end{pmatrix}$.

a) Calcular $\langle A,B\rangle$, $\lVert A\rVert$ y $\lVert B\rVert$. ¿Son $A$ y $B$ ortogonales? Verificar el teorema de Pitágoras con ellas.

b) Calcular el coseno del ángulo entre $A$ y $C$ y comprobar la desigualdad de Cauchy-Schwarz para ese par.

c) Hallar $t\in\mathbb{R}$ tal que $T_t=\begin{pmatrix}t&1\\1&t\end{pmatrix}$ sea ortogonal a $A$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Como $\operatorname{tr}(B^tA)=\sum_{i,j}a_{ij}b_{ij}$, calculamos como en $\mathbb{R}^4$, multiplicando entrada a entrada y sumando.

**a)** $\langle A,B\rangle=1\cdot2+2\cdot(-1)+2\cdot0+0\cdot2=0$: **$A\perp B$.** Las normas: $\lVert A\rVert^2=1+4+4+0=9$ y $\lVert B\rVert^2=4+1+0+4=9$, de modo que $\lVert A\rVert=\lVert B\rVert=3$. Pitágoras pide $\lVert A+B\rVert^2=\lVert A\rVert^2+\lVert B\rVert^2=18$. En efecto $A+B=\begin{pmatrix}3&1\\2&2\end{pmatrix}$ y $\lVert A+B\rVert^2=9+1+4+4=18$.

**b)** $\langle A,C\rangle=1+2+2+0=5$ y $\lVert C\rVert=\sqrt{4}=2$. Entonces $\cos\angle(A,C)=\dfrac{5}{3\cdot2}=\dfrac56$. Cauchy-Schwarz: $\lvert\langle A,C\rangle\rvert=5\le\lVert A\rVert\lVert C\rVert=6$, y es estricta porque $A$ y $C$ no son múltiplos.

**c)** $\langle A,T_t\rangle=1\cdot t+2\cdot1+2\cdot1+0\cdot t=t+4$. Se anula si y solo si $t=-4$.

**Comprobación.** Para $t=-4$: $T_{-4}=\begin{pmatrix}-4&1\\1&-4\end{pmatrix}$ y $\langle A,T_{-4}\rangle=-4+2+2+0=0$.

:::tip[Resultado]
$\langle A,B\rangle=0$ y $\lVert A\rVert=\lVert B\rVert=3$, con $\lVert A+B\rVert^2=18$. $\cos\angle(A,C)=5/6$ y $5\le6$. $T_t\perp A$ si y solo si $t=-4$.
:::

</details>

### Ejercicio 4 · Producto por evaluación en polinomios
<!-- ejercicio: U4.04 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $P_2[\mathbb{R}]$ se define $\langle p,q\rangle=p(-1)q(-1)+p(0)q(0)+p(1)q(1)$.

a) Justificar que es un producto interno.

b) Calcular $\langle 1+x,\,x^2-1\rangle$ y $\lVert 1+x\rVert$.

c) Probar que $x\perp x^2$.

d) Hallar $c\in\mathbb{R}$ tal que $x^2+c\perp1$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Evaluar un polinomio en tres puntos lo convierte en una terna de números, y el producto es el producto punto de esas ternas. Simetría y bilinealidad se heredan de $\mathbb{R}^3$; lo único que hay que revisar es la positividad definida.

**a)** La simetría es evidente, y la linealidad en $p$ sale de $(\alpha p+\beta p')(t)=\alpha p(t)+\beta p'(t)$. Para la positividad, $\langle p,p\rangle=p(-1)^2+p(0)^2+p(1)^2\ge0$ y vale $0$ solo si $p(-1)=p(0)=p(1)=0$. Un polinomio de grado a lo sumo $2$ con tres raíces distintas es el polinomio nulo. **Es producto interno.**

**b)** Los valores en $(-1,0,1)$ son $(0,1,2)$ para $1+x$ y $(0,-1,0)$ para $x^2-1$. Entonces $\langle1+x,x^2-1\rangle=0\cdot0+1\cdot(-1)+2\cdot0=-1$ y $\lVert1+x\rVert^2=0+1+4=5$, o sea $\lVert1+x\rVert=\sqrt5$.

**c)** Los valores de $x$ son $(-1,0,1)$ y los de $x^2$ son $(1,0,1)$: $\langle x,x^2\rangle=-1+0+1=0$.

**d)** Los valores de $x^2+c$ son $(1+c,\,c,\,1+c)$ y los de $1$ son $(1,1,1)$. Luego $\langle x^2+c,1\rangle=(1+c)+c+(1+c)=2+3c=0$ si y solo si $c=-\tfrac23$.

**Comprobación.** Para $c=-\tfrac23$ los valores de $x^2-\tfrac23$ son $(\tfrac13,-\tfrac23,\tfrac13)$, cuya suma es $0$.

:::tip[Resultado]
Es producto interno. $\langle1+x,x^2-1\rangle=-1$, $\lVert1+x\rVert=\sqrt5$, $x\perp x^2$ y $x^2+c\perp1$ si y solo si $c=-\tfrac23$.
:::

</details>

### Ejercicio 5 · Coordenadas en una base ortogonal
<!-- ejercicio: U4.05 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^3$ con el producto usual sea $B=\{b_1,b_2,b_3\}$ con $b_1=(1,1,0)$, $b_2=(1,-1,1)$ y $b_3=(-1,1,2)$.

a) Probar que $B$ es una base ortogonal de $\mathbb{R}^3$.

b) Hallar $[v]_B$ para $v=(3,1,4)$ sin resolver ningún sistema.

c) Verificar que $\lVert v\rVert^2=\sum_i c_i^2\lVert b_i\rVert^2$, donde $c_i$ son las coordenadas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un conjunto ortogonal de vectores no nulos es linealmente independiente, y con tantos vectores como la dimensión es base. En una base ortogonal, la coordenada $i$-ésima de $v$ es $c_i=\dfrac{\langle v,b_i\rangle}{\langle b_i,b_i\rangle}$.

**a)** $b_1\cdot b_2=1-1+0=0$, $b_1\cdot b_3=-1+1+0=0$ y $b_2\cdot b_3=-1-1+2=0$. Son tres vectores no nulos y ortogonales de a pares, luego LI, y forman una base de $\mathbb{R}^3$.

**b)** Las normas al cuadrado son $\langle b_1,b_1\rangle=2$, $\langle b_2,b_2\rangle=3$ y $\langle b_3,b_3\rangle=6$. Los productos con $v$ son $v\cdot b_1=4$, $v\cdot b_2=3-1+4=6$ y $v\cdot b_3=-3+1+8=6$. Entonces

$$
c_1=\frac42=2,\qquad c_2=\frac63=2,\qquad c_3=\frac66=1,\qquad [v]_B=\begin{pmatrix}2\\2\\1\end{pmatrix}.
$$

**c)** $\sum c_i^2\lVert b_i\rVert^2=4\cdot2+4\cdot3+1\cdot6=26$ y $\lVert v\rVert^2=9+1+16=26$.

**Comprobación.** $2b_1+2b_2+b_3=(2,2,0)+(2,-2,2)+(-1,1,2)=(3,1,4)=v$.

:::tip[Resultado]
$B$ es base ortogonal, $[v]_B=(2,2,1)^t$ y $\lVert v\rVert^2=26$.
:::

</details>

### Ejercicio 6 · Complemento ortogonal en $\mathbb{R}^4$
<!-- ejercicio: U4.06 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^4$ con el producto usual sea $S=\operatorname{gen}\{(1,1,0,1),(0,1,1,-1)\}$.

a) Hallar una base de $S^\perp$ y su dimensión.

b) Decidir si $w=(3,-2,1,-1)$ pertenece a $S^\perp$ y, de ser así, escribirlo como combinación de la base hallada.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un vector $x$ es ortogonal a $S$ si y solo si es ortogonal a cada generador. Eso da un sistema homogéneo cuya matriz tiene por filas los generadores: $S^\perp=\operatorname{nul}(A)$, donde $A$ es la matriz que tiene por filas los generadores de $S$.

**a)** Con $A=\begin{pmatrix}1&1&0&1\\0&1&1&-1\end{pmatrix}$, el sistema $Ax=0$ es

$$
\begin{cases}x_1+x_2+x_4=0\\ x_2+x_3-x_4=0\end{cases}
$$

Las variables libres son $x_3$ y $x_4$. De la segunda ecuación, $x_2=x_4-x_3$, y de la primera, $x_1=-x_2-x_4=x_3-2x_4$. Entonces
$x=x_3(1,-1,1,0)+x_4(-2,1,0,1)$ y una base es $\{(1,-1,1,0),\,(-2,1,0,1)\}$, con $\dim S^\perp=2$. Es consistente con $\dim S+\dim S^\perp=2+2=4$.

**b)** Comparamos con ambos generadores: $w\cdot(1,1,0,1)=3-2+0-1=0$ y $w\cdot(0,1,1,-1)=-2+1+1=0$, de modo que $w\in S^\perp$. Las coordenadas se leen en las posiciones libres: $x_3=1$ y $x_4=-1$, o sea $w=1\cdot(1,-1,1,0)-1\cdot(-2,1,0,1)$.

**Comprobación.** $(1,-1,1,0)+(2,-1,0,-1)=(3,-2,1,-1)=w$. Además cada vector de la base es ortogonal a los dos generadores: por ejemplo $(-2,1,0,1)\cdot(1,1,0,1)=-2+1+1=0$ y $(-2,1,0,1)\cdot(0,1,1,-1)=1-1=0$.

:::tip[Resultado]
$S^\perp=\operatorname{gen}\{(1,-1,1,0),(-2,1,0,1)\}$, $\dim S^\perp=2$, y $w=(1,-1,1,0)-(-2,1,0,1)\in S^\perp$.
:::

</details>

### Ejercicio 7 · Proyección sobre un plano con una base ortogonal
<!-- ejercicio: U4.07 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^3$ con el producto usual sea $S=\operatorname{gen}\{(1,1,0),(1,-1,1)\}$ y $v=(3,1,4)$.

a) Verificar que los generadores forman una base ortogonal de $S$.

b) Calcular $\operatorname{proy}_S(v)$.

c) Calcular $d(v,S)$ y comprobar que $v-\operatorname{proy}_S(v)\in S^\perp$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Si $\{b_1,b_2\}$ es base ortogonal de $S$, entonces $\operatorname{proy}_S(v)=\dfrac{\langle v,b_1\rangle}{\langle b_1,b_1\rangle}b_1+\dfrac{\langle v,b_2\rangle}{\langle b_2,b_2\rangle}b_2$, y $d(v,S)=\lVert v-\operatorname{proy}_S(v)\rVert$.

**a)** $b_1=(1,1,0)$ y $b_2=(1,-1,1)$ cumplen $b_1\cdot b_2=1-1+0=0$, así que son ortogonales y no nulos, luego LI y base de $S$.

**b)** $v\cdot b_1=4$, $b_1\cdot b_1=2$, $v\cdot b_2=3-1+4=6$ y $b_2\cdot b_2=3$. Entonces

$$
\operatorname{proy}_S(v)=\frac42(1,1,0)+\frac63(1,-1,1)=(2,2,0)+(2,-2,2)=(4,0,2).
$$

**c)** $v-\operatorname{proy}_S(v)=(3,1,4)-(4,0,2)=(-1,1,2)$. Es ortogonal a $b_1$ ($-1+1+0=0$) y a $b_2$ ($-1-1+2=0$), de modo que está en $S^\perp$. Su norma es $\sqrt{1+1+4}=\sqrt6$.

**Comprobación (Pitágoras).** $\lVert v\rVert^2=9+1+16=26$ y $\lVert\operatorname{proy}_S(v)\rVert^2+\lVert v-\operatorname{proy}_S(v)\rVert^2=(16+0+4)+6=26$.

:::tip[Resultado]
$\operatorname{proy}_S(v)=(4,0,2)$, $v-\operatorname{proy}_S(v)=(-1,1,2)\in S^\perp$ y $d(v,S)=\sqrt6$.
:::

</details>

### Ejercicio 8 · El producto punto en $\mathbb{Z}_2^n$
<!-- ejercicio: U4.08 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{Z}_2^5$ sean $u=11010$ y $v=10110$ (se escriben sin comas), con el producto punto módulo $2$.

a) Calcular $u\cdot v$ y $u\cdot u$. ¿Es $u$ ortogonal a $v$? ¿Y a sí mismo?

b) Hallar todos los vectores de $\mathbb{Z}_2^3$ ortogonales a $(1,1,0)$.

c) ¿Cuántos vectores de $\mathbb{Z}_2^5$ son ortogonales a $u$?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se multiplican coordenada a coordenada y se suma módulo $2$. Como $x_i^2=x_i$ en $\mathbb{Z}_2$, vale $x\cdot x=w(x)\bmod2$, donde $w$ es el peso. Para contar, se observa que la ortogonalidad a $u$ es una única ecuación lineal.

**a)** $u\cdot v=1\cdot1+1\cdot0+0\cdot1+1\cdot1+0\cdot0=1+0+0+1+0=0$: **$u\perp v$.** Además $u\cdot u=1+1+0+1+0=1$ (peso $3$, impar): **$u$ no es ortogonal a sí mismo.**

**b)** Para $x=(x_1,x_2,x_3)$ la condición es $x_1+x_2=0$, o sea $x_1=x_2$, con $x_3$ libre. Los vectores son $000,\ 001,\ 110,\ 111$.

**c)** La condición $u\cdot x=x_1+x_2+x_4=0$ es una ecuación no trivial sobre $\mathbb{Z}_2^5$, de modo que su conjunto solución es un subespacio de dimensión $4$ y tiene $2^4=16$ elementos.

**Comprobación.** En b), el conjunto tiene $2^{3-1}=4$ elementos, como predice el mismo argumento. En c), $v=10110$ está entre los $16$ porque $u\cdot v=0$.

:::tip[Resultado]
$u\cdot v=0$ y $u\cdot u=1$. Los ortogonales a $(1,1,0)$ en $\mathbb{Z}_2^3$ son $000,001,110,111$. Hay $16$ vectores de $\mathbb{Z}_2^5$ ortogonales a $u$.
:::

</details>
