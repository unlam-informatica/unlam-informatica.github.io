---
title: Práctica — Nivel inicial
description: Ocho ejercicios resueltos de transformaciones lineales para empezar. Linealidad, núcleo e imagen, teorema de la dimensión, matriz canónica y una aplicación a gráficos 2D.
slug: algebra-ii/unidad-2/practica/nivel-inicial
sidebar:
  order: 1
  label: Nivel inicial
---

Esta página reúne los ejercicios básicos de la unidad: reconocer si una función es lineal, calcular núcleo e imagen con sus bases, usar el teorema de la dimensión, pasar de la fórmula a la matriz canónica y viceversa. Presupone las lecciones [definición y ejemplos](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/), [núcleo e imagen](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/), [teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/) y [clasificación](/algebra-ii/unidad-2/teoria/clasificacion/), y de la [matriz asociada](/algebra-ii/unidad-2/teoria/matriz-asociada/) solo el caso de las bases canónicas.

Cómo usarla: resolvé cada ejercicio por tu cuenta antes de abrir la resolución, y usá la resolución para comparar el método y, sobre todo, la comprobación final, que conviene hacer siempre. Todos los enunciados son originales de este manual. Los ejercicios siguen en el [nivel intermedio](/algebra-ii/unidad-2/practica/nivel-intermedio/).

Convenciones: en $P_2[\mathbb{R}]$ la base canónica es $E=\{1,x,x^2\}$ y en $\mathbb{R}^{2\times 2}$ es $E=\{E_{11},E_{12},E_{21},E_{22}\}$, ambas en ese orden.

### Ejercicio 1 · Linealidad y no linealidad
<!-- ejercicio: U2.01 | nivel: inicial | tipo: conceptual | verificacion: sympy -->

:::note[Enunciado]
Decidir si cada función es una transformación lineal. Si lo es, justificarlo; si no, dar un contraejemplo concreto.

a) $T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(x-2y+z,\ 3y-z)$.

b) $S:\mathbb{R}^2\to\mathbb{R}^2$, $S(x,y)=(x+y,\ 2)$.

c) $F:\mathbb{R}^2\to\mathbb{R}$, $F(x,y)=xy$.

d) $D:P_2[\mathbb{R}]\to P_2[\mathbb{R}]$, $D(p)=p'+p(1)$, donde $p(1)$ se interpreta como polinomio constante.

e) $E:\mathbb{R}^{2\times 2}\to\mathbb{R}$, $E(A)=\det(A)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para probar que una función es lineal se verifican la aditividad $T(u+v)=T(u)+T(v)$ y la homogeneidad $T(\lambda u)=\lambda T(u)$, o bien se reconoce que es de la forma $u\mapsto Au$. Para refutarla alcanza un contraejemplo: el test del vector nulo ($T(0)=0$) o un cálculo concreto que rompa alguna de las dos propiedades.

**a)** Cada componente es una combinación lineal de $x,y,z$ sin términos constantes, de modo que

$$
T(x,y,z)=\begin{pmatrix}1&-2&1\\0&3&-1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=Au.
$$

Entonces $T(u+v)=A(u+v)=Au+Av=T(u)+T(v)$ y $T(\lambda u)=A(\lambda u)=\lambda Au=\lambda T(u)$. **$T$ es lineal.**

**b)** $S(0,0)=(0,2)\neq(0,0)$. Toda transformación lineal manda el vector nulo al vector nulo, así que **$S$ no es lineal.**

**c)** Acá $F(0,0)=0$, de modo que el test del nulo no alcanza. Probamos la homogeneidad con $\lambda=2$ y $u=(1,1)$: $F(2u)=F(2,2)=4$, mientras que $2F(u)=2F(1,1)=2$. Como $4\neq 2$, **$F$ no es lineal.**

**d)** Para $p=a+bx+cx^2$ tenemos $p'=b+2cx$ y $p(1)=a+b+c$, luego $D(p)=(a+2b+c)+2cx$. Verificamos las dos propiedades con la definición. Para $p,q\in P_2[\mathbb{R}]$:

$$
D(p+q)=(p+q)'+(p+q)(1)=p'+q'+p(1)+q(1)=D(p)+D(q),
$$

y para $\lambda\in\mathbb{R}$, $D(\lambda p)=\lambda p'+\lambda p(1)=\lambda D(p)$. **$D$ es lineal.** Su matriz en $E$ tiene por columnas las coordenadas de $D(1)=1$, $D(x)=1+1=2$ y $D(x^2)=2x+1$:

$$
M(D)_E=\begin{pmatrix}1&2&1\\0&0&2\\0&0&0\end{pmatrix}.
$$

**e)** Tomemos la identidad $I$. Entonces $E(2I)=\det(2I)=4$, pero $2E(I)=2\cdot 1=2$. **$E$ no es lineal** (el determinante es multilineal en las filas, no lineal en la matriz).

**Comprobación.** En a), $T(1,1,1)=(1-2+1,\ 3-1)=(0,2)$ coincide con $A(1,1,1)^t$. En d), $D(1+x+x^2)=(1+2x)+3=4+2x$, que es $M(D)_E(1,1,1)^t=(4,2,0)^t$.

:::tip[Resultado]
Son lineales a) y d). No lo son b) (porque $S(0,0)\neq 0$), c) (porque $F(2,2)\neq 2F(1,1)$) y e) (porque $\det(2I)\neq 2\det I$).
:::

</details>

### Ejercicio 2 · Núcleo, imagen y preimagen
<!-- ejercicio: U2.02 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:\mathbb{R}^3\to\mathbb{R}^3$, $T(x,y,z)=(x-y+2z,\ 2x-y+3z,\ x+z)$.

a) Hallar una base de $\operatorname{Nu}(T)$ y su dimensión.

b) Hallar una base de $\operatorname{Im}(T)$, su dimensión y una ecuación que la describa.

c) Clasificar $T$ (monomorfismo, epimorfismo, isomorfismo).

d) Decidir si $(3,4,1)\in\operatorname{Im}(T)$ y, en ese caso, describir todos los vectores $v$ con $T(v)=(3,4,1)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escribimos la matriz $A$ de $T$ en las bases canónicas y la escalonamos: las variables libres dan el núcleo, las columnas pivote dan una base de la imagen.

$$
A=\begin{pmatrix}1&-1&2\\2&-1&3\\1&0&1\end{pmatrix}\xrightarrow{\ F_2-2F_1,\ F_3-F_1\ }\begin{pmatrix}1&-1&2\\0&1&-1\\0&1&-1\end{pmatrix}\xrightarrow{\ F_3-F_2,\ F_1+F_2\ }\begin{pmatrix}1&0&1\\0&1&-1\\0&0&0\end{pmatrix}.
$$

**a)** El sistema $Av=0$ queda $x=-z$, $y=z$ con $z$ libre: $v=z(-1,1,1)$. Entonces $\operatorname{Nu}(T)=\operatorname{gen}\{(-1,1,1)\}$, base $\{(-1,1,1)\}$ y $\dim\operatorname{Nu}(T)=1$.

**b)** Las columnas pivote son la 1 y la 2 de $A$ (no de la forma escalonada), así que $\{(1,2,1),(-1,-1,0)\}$ es base de $\operatorname{Im}(T)$ y $\dim\operatorname{Im}(T)=2$. La tercera columna depende de ellas: $(2,3,1)=(1,2,1)-(-1,-1,0)$. Para una ecuación, buscamos la relación entre las coordenadas $(a,b,c)$ de un vector de la imagen: en ambos generadores vale $c=b-a$ ($1=2-1$ y $0=-1+1$), y como la ecuación es lineal vale en todo el generado. Entonces $\operatorname{Im}(T)=\{(a,b,c):\ c=b-a\}$. Verificamos la dimensión: $1+2=3=\dim\mathbb{R}^3$.

**c)** Como $\operatorname{Nu}(T)\neq\{0\}$, $T$ no es monomorfismo; como $\dim\operatorname{Im}(T)=2<3$, no es epimorfismo. Por lo tanto no es isomorfismo.

**d)** Para $(3,4,1)$: $c=1$ y $b-a=4-3=1$, así que pertenece a la imagen. Resolvemos $Av=(3,4,1)$ con la matriz ampliada:

$$
\left(\begin{array}{ccc|c}1&-1&2&3\\2&-1&3&4\\1&0&1&1\end{array}\right)\sim\left(\begin{array}{ccc|c}1&0&1&1\\0&1&-1&-2\\0&0&0&0\end{array}\right),
$$

de donde $x=1-z$, $y=-2+z$. Con $z=t$ queda $v=(1,-2,0)+t(-1,1,1)$, es decir, una solución particular más el núcleo.

**Comprobación.** $T(1,-2,0)=(1+2,\ 2+2,\ 1)=(3,4,1)$ y $T(-1,1,1)=(-1-1+2,\ -2-1+3,\ -1+1)=(0,0,0)$. Además $(1,1,1)$ no está en la imagen porque $1\neq 1-1$.

:::tip[Resultado]
$\operatorname{Nu}(T)=\operatorname{gen}\{(-1,1,1)\}$; $\operatorname{Im}(T)=\operatorname{gen}\{(1,2,1),(-1,-1,0)\}=\{c=b-a\}$; ni mono ni epi. $T^{-1}(\{(3,4,1)\})=\{(1,-2,0)+t(-1,1,1):\ t\in\mathbb{R}\}$.
:::

</details>

### Ejercicio 3 · De polinomios a vectores
<!-- ejercicio: U2.03 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:P_2[\mathbb{R}]\to\mathbb{R}^2$ definida por $T(p)=\big(p(0),\ p(1)-p'(1)\big)$.

a) Calcular $T(a+bx+cx^2)$.

b) Hallar bases de $\operatorname{Nu}(T)$ y de $\operatorname{Im}(T)$ y verificar el teorema de la dimensión.

c) Clasificar $T$ y calcular $T(2+3x+x^2)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Evaluamos la fórmula sobre un polinomio genérico y trabajamos con las coordenadas $(a,b,c)$ respecto de la base canónica.

**a)** Para $p=a+bx+cx^2$: $p(0)=a$, $p(1)=a+b+c$, $p'(x)=b+2cx$ y $p'(1)=b+2c$. Luego $p(1)-p'(1)=a-c$ y

$$
T(a+bx+cx^2)=(a,\ a-c).
$$

**b)** *Núcleo.* $T(p)=0$ si y solo si $a=0$ y $a-c=0$, es decir $a=c=0$ con $b$ libre: $p=bx$. Entonces $\operatorname{Nu}(T)=\operatorname{gen}\{x\}$, base $\{x\}$, dimensión 1.

*Imagen.* Los generadores $1,x,x^2$ van a $T(1)=(1,1)$, $T(x)=(0,0)$, $T(x^2)=(0,-1)$. Entonces $\operatorname{Im}(T)=\operatorname{gen}\{(1,1),(0,-1)\}$ y como estos dos vectores no son proporcionales, son una base y $\dim\operatorname{Im}(T)=2$, por lo que $\operatorname{Im}(T)=\mathbb{R}^2$.

*Teorema de la dimensión:* $\dim P_2[\mathbb{R}]=3=1+2=\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)$.

**c)** $T$ es epimorfismo ($\operatorname{Im}(T)=\mathbb{R}^2$) pero no monomorfismo ($x\in\operatorname{Nu}(T)$). Con $a=2$, $b=3$, $c=1$: $T(2+3x+x^2)=(2,\ 2-1)=(2,1)$.

**Comprobación.** Directamente: $p=2+3x+x^2$ tiene $p(0)=2$, $p(1)=6$, $p'(1)=3+2=5$, y $T(p)=(2,\ 6-5)=(2,1)$.

:::tip[Resultado]
$T(a+bx+cx^2)=(a,a-c)$; $\operatorname{Nu}(T)=\operatorname{gen}\{x\}$; $\operatorname{Im}(T)=\mathbb{R}^2$ con base $\{(1,1),(0,-1)\}$; $T$ es epimorfismo y no monomorfismo; $T(2+3x+x^2)=(2,1)$.
:::

</details>

### Ejercicio 4 · Simétricas y antisimétricas
<!-- ejercicio: U2.04 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:\mathbb{R}^{2\times 2}\to\mathbb{R}^{2\times 2}$, $T(A)=A-A^t$.

a) Hallar la matriz $M(T)_E$ en la base canónica.

b) Hallar bases de $\operatorname{Nu}(T)$ y de $\operatorname{Im}(T)$ e interpretar ambos subespacios.

c) Decidir si $T$ es mono, epi o iso.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Calculamos $T$ sobre cada matriz de la base canónica y leemos núcleo e imagen de la matriz $4\times 4$ obtenida.

**a)** Con $E=\{E_{11},E_{12},E_{21},E_{22}\}$:

- $T(E_{11})=E_{11}-E_{11}=0$ y $T(E_{22})=0$.
- $T(E_{12})=E_{12}-E_{21}$, con coordenadas $(0,1,-1,0)$.
- $T(E_{21})=E_{21}-E_{12}$, con coordenadas $(0,-1,1,0)$.

$$
M(T)_E=\begin{pmatrix}0&0&0&0\\0&1&-1&0\\0&-1&1&0\\0&0&0&0\end{pmatrix}.
$$

**b)** *Núcleo.* $M(T)_E(a,b,c,d)^t=0$ equivale a $b-c=0$, con $a,d$ libres. Entonces los vectores del núcleo son $(a,b,b,d)$, y una base es $\{E_{11},\ E_{22},\ E_{12}+E_{21}\}$, de dimensión 3. Es el subespacio de las matrices simétricas: $A=A^t\iff A-A^t=0$.

*Imagen.* La matriz tiene rango 1 (todas las columnas no nulas son múltiplos de $(0,1,-1,0)^t$). Una base es $\{E_{12}-E_{21}\}$, de dimensión 1: son las matrices antisimétricas de $2\times 2$, de la forma $\begin{pmatrix}0&s\\-s&0\end{pmatrix}$.

Teorema de la dimensión: $4=3+1$.

**c)** $\operatorname{Nu}(T)\neq\{0\}$ (por ejemplo $I\in\operatorname{Nu}(T)$), así que no es mono; $\dim\operatorname{Im}(T)=1<4$, así que no es epi. No es iso.

**Comprobación.** $T\begin{pmatrix}3&5\\-2&7\end{pmatrix}=\begin{pmatrix}3&5\\-2&7\end{pmatrix}-\begin{pmatrix}3&-2\\5&7\end{pmatrix}=\begin{pmatrix}0&7\\-7&0\end{pmatrix}$, que es $7(E_{12}-E_{21})$, antisimétrica y múltiplo de la base de la imagen.

:::tip[Resultado]
$\operatorname{Nu}(T)$ = simétricas, base $\{E_{11},E_{22},E_{12}+E_{21}\}$; $\operatorname{Im}(T)$ = antisimétricas, base $\{E_{12}-E_{21}\}$; $T$ no es mono ni epi.
:::

</details>

### Ejercicio 5 · De la fórmula a la matriz y de la matriz a la fórmula
<!-- ejercicio: U2.05 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) Sea $T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(2x-y+z,\ x+3z)$. Hallar su matriz $M(T)_{EE'}$ en las bases canónicas, una base de $\operatorname{Nu}(T)$ y todas las preimágenes del vector $(4,5)$.

b) Sea $S:\mathbb{R}^2\to\mathbb{R}^3$ la transformación lineal con
$$
M(S)_{EE'}=\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}.
$$
Hallar la fórmula de $S(x,y)$, calcular $S(2,-3)$ y decidir si $S$ es mono o epi. ¿Pertenece $(1,1,1)$ a $\operatorname{Im}(S)$?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las columnas de la matriz canónica son las imágenes de la base canónica; recíprocamente, $S(v)=M(S)_{EE'}\,v$.

**a)** $T(e_1)=(2,1)$, $T(e_2)=(-1,0)$, $T(e_3)=(1,3)$. Entonces

$$
M(T)_{EE'}=\begin{pmatrix}2&-1&1\\1&0&3\end{pmatrix}.
$$

*Núcleo.* $2x-y+z=0$ y $x+3z=0$ dan $x=-3z$ y luego $y=2x+z=-5z$. Base: $\{(-3,-5,1)\}$. Las filas son independientes, así que el rango es 2 y $T$ es epimorfismo (y $\dim\operatorname{Nu}(T)=3-2=1$).

*Preimágenes de $(4,5)$.* Resolvemos $2x-y+z=4$, $x+3z=5$. Con $z=0$: $x=5$, $y=2x-4=6$. Entonces una solución particular es $v_p=(5,6,0)$, y toda la preimagen es

$$
T^{-1}(\{(4,5)\})=\{(5,6,0)+t(-3,-5,1):\ t\in\mathbb{R}\}.
$$

**b)** Multiplicando la matriz por $(x,y)^t$ obtenemos $S(x,y)=(x+2y,\ -y,\ 3x+y)$. Luego $S(2,-3)=(2-6,\ 3,\ 6-3)=(-4,3,3)$.

Las dos columnas son linealmente independientes, así que el rango es 2 y $\operatorname{Nu}(S)=\{0\}$: $S$ es monomorfismo. Como $\dim\operatorname{Im}(S)=2<3$, no es epimorfismo.

Para $(1,1,1)$: $x+2y=1$ y $-y=1$ dan $y=-1$, $x=3$, pero entonces $3x+y=8\neq 1$. El sistema es incompatible: $(1,1,1)\notin\operatorname{Im}(S)$.

**Comprobación.** $T(5,6,0)=(10-6,\ 5)=(4,5)$ y $T(-3,-5,1)=(-6+5+1,\ -3+3)=(0,0)$. Para $S$: $S(1,1)=(3,-1,4)$ es la suma de las dos columnas, como debe ser.

:::tip[Resultado]
a) $M(T)_{EE'}=\begin{pmatrix}2&-1&1\\1&0&3\end{pmatrix}$, $\operatorname{Nu}(T)=\operatorname{gen}\{(-3,-5,1)\}$, $T^{-1}(\{(4,5)\})=(5,6,0)+\operatorname{Nu}(T)$.
b) $S(x,y)=(x+2y,-y,3x+y)$, $S(2,-3)=(-4,3,3)$; $S$ es mono y no epi; $(1,1,1)\notin\operatorname{Im}(S)$.
:::

</details>

### Ejercicio 6 · ¿Existe una transformación con estas propiedades?
<!-- ejercicio: U2.06 | nivel: inicial | tipo: conceptual | verificacion: sympy -->

:::note[Enunciado]
En cada caso decidir si existe una transformación lineal con las propiedades indicadas. Si existe, dar un ejemplo; si no, explicar por qué.

a) $T:\mathbb{R}^4\to\mathbb{R}^3$ epimorfismo con $\dim\operatorname{Nu}(T)=2$.

b) $T:\mathbb{R}^3\to\mathbb{R}^5$ monomorfismo.

c) $T:P_2[\mathbb{R}]\to\mathbb{R}^{2\times 2}$ epimorfismo.

d) $T:\mathbb{R}^{2\times 2}\to P_2[\mathbb{R}]$ con $\operatorname{Nu}(T)=\operatorname{gen}\{I\}$, donde $I$ es la identidad.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El teorema de la dimensión, $\dim V=\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)$, fija qué combinaciones son posibles; cuando las dimensiones lo permiten, se construye un ejemplo.

**a)** No existe. Si $T$ fuera epimorfismo, $\dim\operatorname{Im}(T)=3$ y entonces $\dim\operatorname{Nu}(T)=4-3=1\neq 2$. (Con $\dim\operatorname{Nu}(T)=2$ resultaría $\dim\operatorname{Im}(T)=2<3$.)

**b)** Existe: no hay obstrucción dimensional porque $3\le 5$. Por ejemplo $T(x,y,z)=(x,y,z,0,0)$: su núcleo es $\{0\}$, así que es inyectiva.

**c)** No existe. Para ser epimorfismo se necesita $\dim\operatorname{Im}(T)=4$, pero $\dim\operatorname{Im}(T)\le\dim P_2[\mathbb{R}]=3$ (la imagen está generada por las imágenes de una base del dominio, que son 3 vectores).

**d)** Existe. Las dimensiones cierran: $\dim\operatorname{Im}(T)=4-1=3=\dim P_2[\mathbb{R}]$, así que $T$ tendría que ser epimorfismo. Un ejemplo es

$$
T\begin{pmatrix}a&b\\c&d\end{pmatrix}=(a-d)+bx+cx^2.
$$

Es lineal (cada coeficiente es combinación lineal de $a,b,c,d$). Su núcleo: $a-d=0$, $b=0$, $c=0$, o sea $a=d$, $b=c=0$, que son los múltiplos de $I$. Y es sobreyectiva: $T(\alpha E_{11}+\beta E_{12}+\gamma E_{21})=\alpha+\beta x+\gamma x^2$.

**Comprobación.** En d): $T(I)=(1-1)+0x+0x^2=0$, y $\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)=1+3=4=\dim\mathbb{R}^{2\times 2}$.

:::tip[Resultado]
a) No. b) Sí, $T(x,y,z)=(x,y,z,0,0)$. c) No. d) Sí, $T(A)=(a_{11}-a_{22})+a_{12}x+a_{21}x^2$.
:::

</details>

### Ejercicio 7 · Tres afirmaciones
<!-- ejercicio: U2.07 | nivel: inicial | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Decidir si cada afirmación es verdadera o falsa y justificar (con una demostración o con un contraejemplo explícito).

a) Si $T:\mathbb{R}^3\to\mathbb{R}^3$ es lineal e inyectiva, entonces es sobreyectiva.

b) Toda transformación lineal $T:\mathbb{R}^2\to\mathbb{R}^3$ es inyectiva.

c) Existe una transformación lineal $T:\mathbb{R}^3\to\mathbb{R}^3$ con $T(1,0,0)=(0,0,0)$ y $\operatorname{Im}(T)=\mathbb{R}^3$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En las afirmaciones sobre dimensiones se usa el teorema de la dimensión; para refutar una afirmación general se exhibe un caso concreto que la viole.

**a) Verdadera.** Si $T$ es inyectiva, $\operatorname{Nu}(T)=\{0\}$ y $\dim\operatorname{Nu}(T)=0$. El teorema de la dimensión da $\dim\operatorname{Im}(T)=3-0=3$. Como $\operatorname{Im}(T)$ es un subespacio de $\mathbb{R}^3$ de dimensión 3, coincide con $\mathbb{R}^3$: $T$ es sobreyectiva.

**b) Falsa.** Contraejemplo: la transformación nula $T(v)=(0,0,0)$ es lineal de $\mathbb{R}^2$ en $\mathbb{R}^3$, pero $T(1,0)=T(0,1)=(0,0,0)$ con $(1,0)\neq(0,1)$, así que no es inyectiva. (Un ejemplo no nulo: $T(x,y)=(x,0,0)$, con $T(0,1)=0$.) Lo que sí es cierto es que ninguna $T:\mathbb{R}^2\to\mathbb{R}^3$ puede ser sobreyectiva, porque $\dim\operatorname{Im}(T)\le 2<3$.

**c) Falsa.** El vector $(1,0,0)$ es no nulo y pertenece a $\operatorname{Nu}(T)$, así que $\dim\operatorname{Nu}(T)\ge 1$. Por el teorema de la dimensión, $\dim\operatorname{Im}(T)=3-\dim\operatorname{Nu}(T)\le 2<3$, y entonces $\operatorname{Im}(T)\neq\mathbb{R}^3$. No existe.

**Comprobación.** En b), con $T(x,y)=(x,0,0)$: $\operatorname{Nu}(T)=\operatorname{gen}\{(0,1)\}$ y $\dim\operatorname{Im}(T)=1$, de modo que $2=1+1$ se cumple. En a), la condición se ve también en las matrices: una matriz cuadrada $3\times 3$ con columnas independientes tiene rango 3.

:::tip[Resultado]
a) Verdadera. b) Falsa (por ejemplo $T=0$). c) Falsa.
:::

</details>

### Ejercicio 8 · Reflejar e inclinar una figura
<!-- ejercicio: U2.08 | nivel: inicial | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
En un programa de gráficos se aplican a las figuras del plano dos transformaciones: la reflexión respecto del eje $y$, $R(x,y)=(-x,y)$, y la cizalladura horizontal $S(x,y)=(x+2y,\ y)$.

a) Hallar las matrices de $R$, de $S$ y de la composición $S\circ R$ (primero $R$, después $S$).

b) Calcular la imagen por $S\circ R$ de los vértices del cuadrado unidad $(0,0),(1,0),(1,1),(0,1)$.

c) Comparar con $R\circ S$: ¿da lo mismo aplicar las transformaciones en otro orden?

d) Decidir si $S\circ R$ es un isomorfismo y, de serlo, hallar su inversa.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La matriz de una composición es el producto de las matrices en el orden inverso al de aplicación: $M(S\circ R)=M(S)\,M(R)$.

**a)** Las columnas son las imágenes de $e_1$ y $e_2$:

$$
M(R)=\begin{pmatrix}-1&0\\0&1\end{pmatrix},\qquad M(S)=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad M(S\circ R)=M(S)M(R)=\begin{pmatrix}-1&2\\0&1\end{pmatrix}.
$$

Es decir, $(S\circ R)(x,y)=(-x+2y,\ y)$.

**b)** Aplicando la fórmula: $(0,0)\mapsto(0,0)$; $(1,0)\mapsto(-1,0)$; $(1,1)\mapsto(-1+2,\ 1)=(1,1)$; $(0,1)\mapsto(2,1)$. El cuadrado se transforma en el paralelogramo de vértices $(0,0),(-1,0),(1,1),(2,1)$.

**c)** $M(R\circ S)=M(R)M(S)=\begin{pmatrix}-1&-2\\0&1\end{pmatrix}\neq M(S\circ R)$. Por ejemplo, $(R\circ S)(1,1)=(-3,1)$, mientras que $(S\circ R)(1,1)=(1,1)$. El orden importa: el producto de matrices no es conmutativo.

**d)** $\det M(S\circ R)=-1\neq 0$, así que es isomorfismo (la reflexión invierte la orientación y la cizalladura conserva el área). Calculamos la inversa de la matriz: como $\begin{pmatrix}-1&2\\0&1\end{pmatrix}^2=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, la inversa es ella misma. Entonces $(S\circ R)^{-1}=S\circ R$, y también $(S\circ R)^{-1}=R^{-1}\circ S^{-1}=R\circ S^{-1}$ con $S^{-1}(x,y)=(x-2y,y)$, que da $(-x+2y,\ y)$.

**Comprobación.** $(S\circ R)(S\circ R)(x,y)=(S\circ R)(-x+2y,y)=(x-2y+2y,\ y)=(x,y)$.

:::tip[Resultado]
$M(S\circ R)=\begin{pmatrix}-1&2\\0&1\end{pmatrix}$; el cuadrado va al paralelogramo $(0,0),(-1,0),(1,1),(2,1)$; $S\circ R\neq R\circ S$; $S\circ R$ es isomorfismo y su propia inversa.
:::

</details>
