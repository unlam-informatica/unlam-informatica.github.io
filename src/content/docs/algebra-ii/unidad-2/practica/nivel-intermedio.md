---
title: Práctica — Nivel intermedio
description: Diez ejercicios resueltos de transformaciones lineales. Teorema fundamental, núcleo e imagen prescritos, matrices en bases no canónicas, cambio de base, composición, inversa y códigos sobre Z2.
slug: algebra-ii/unidad-2/practica/nivel-intermedio
sidebar:
  order: 2
  label: Nivel intermedio
---

Esta página sigue el [nivel inicial](/algebra-ii/unidad-2/practica/nivel-inicial/) y presupone todas las lecciones de la unidad. Los ejercicios 9 a 11 usan el [teorema fundamental](/algebra-ii/unidad-2/teoria/teorema-fundamental/); el 12 y el 13, la [matriz asociada](/algebra-ii/unidad-2/teoria/matriz-asociada/) con bases no canónicas; el 14, el [cambio de base](/algebra-ii/unidad-2/teoria/cambio-de-base/) con tres factores; el 15 y el 16, la [composición y la inversa](/algebra-ii/unidad-2/teoria/composicion-e-inversa/); el 17 recupera la [definición](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/) sobre $\mathbb{Z}_2$, y el 18 combina el [núcleo y la imagen](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/) con la matriz en $\mathbb{R}^{2\times 2}$.

Cómo usarla: conviene hacerlos en orden, escribiendo en cada uno la estrategia antes de calcular, y revisar siempre la comprobación final. Todos los enunciados son originales de este manual. La numeración continúa la del nivel inicial.

Recordatorio de notación: $M(T)_{BB'}$ tiene por columnas $[T(b_j)]_{B'}$, de modo que $M(T)_{BB'}[v]_B=[T(v)]_{B'}$, y $C_{BB'}[v]_B=[v]_{B'}$.

### Ejercicio 9 · Una transformación definida sobre una base
<!-- ejercicio: U2.09 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $B=\{(1,0,0),(1,1,0),(1,1,1)\}$, que es base de $\mathbb{R}^3$.

a) Probar que existe una única transformación lineal $T:\mathbb{R}^3\to\mathbb{R}^3$ con $T(1,0,0)=(1,0,2)$, $T(1,1,0)=(2,1,0)$ y $T(1,1,1)=(3,1,2)$, y hallar $T(x,y,z)$.

b) Calcular $T(1,2,3)$.

c) Hallar bases de $\operatorname{Nu}(T)$ y de $\operatorname{Im}(T)$, una ecuación de la imagen, y clasificar $T$.

d) Hallar todos los $v$ con $T(v)=(3,1,2)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Como $B$ es base, el teorema fundamental asegura existencia y unicidad. Para obtener la fórmula escribimos un vector genérico en la base $B$ y usamos la linealidad.

**a)** $B$ es base (tres vectores LI, pues la matriz con esas columnas es triangular con unos en la diagonal) y los datos asignan una imagen a cada vector de $B$. Por el teorema fundamental, existe una única $T$. Para el vector $(x,y,z)=\alpha(1,0,0)+\beta(1,1,0)+\gamma(1,1,1)$ queda $\alpha+\beta+\gamma=x$, $\beta+\gamma=y$, $\gamma=z$, es decir

$$
\gamma=z,\qquad \beta=y-z,\qquad \alpha=x-y.
$$

Por linealidad,

$$
T(x,y,z)=(x-y)(1,0,2)+(y-z)(2,1,0)+z(3,1,2)=(x+y+z,\ y,\ 2x-2y+2z).
$$

**b)** $T(1,2,3)=(1+2+3,\ 2,\ 2-4+6)=(6,2,4)$. Con las coordenadas: $[(1,2,3)]_B=(-1,-1,3)$ y $-(1,0,2)-(2,1,0)+3(3,1,2)=(6,2,4)$.

**c)** La matriz canónica y su forma escalonada son

$$
A=\begin{pmatrix}1&1&1\\0&1&0\\2&-2&2\end{pmatrix}\sim\begin{pmatrix}1&0&1\\0&1&0\\0&0&0\end{pmatrix}.
$$

*Núcleo:* $y=0$, $x=-z$, es decir $\operatorname{Nu}(T)=\operatorname{gen}\{(-1,0,1)\}$, dimensión 1. Esto es coherente con los datos: $(-1,0,1)=(1,1,1)-(1,0,0)-(1,1,0)$ y $(3,1,2)-(1,0,2)-(2,1,0)=(0,0,0)$.

*Imagen:* las columnas pivote son la 1 y la 2: base $\{(1,0,2),(1,1,-2)\}$, dimensión 2. Para la ecuación buscamos $n=(n_1,n_2,n_3)$ ortogonal a los dos generadores: $n_1+2n_3=0$ y $n_1+n_2-2n_3=0$, que se resuelve con $n=(-2,4,1)$. Entonces $\operatorname{Im}(T)=\{(p,q,r):\ -2p+4q+r=0\}$.

Como $\operatorname{Nu}(T)\neq\{0\}$ y $\dim\operatorname{Im}(T)=2<3$, $T$ no es mono ni epi.

**d)** El vector $(3,1,2)$ es $T(1,1,1)$ (dato del enunciado), así que una solución particular es $(1,1,1)$ y

$$
T^{-1}(\{(3,1,2)\})=\{(1,1,1)+t(-1,0,1):\ t\in\mathbb{R}\}.
$$

**Comprobación.** $T(1,0,0)=(1,0,2)$, $T(1,1,0)=(2,1,0)$, $T(1,1,1)=(3,1,2)$ reproducen los datos. Además $(3,1,2)$ cumple la ecuación de la imagen: $-6+4+2=0$.

:::tip[Resultado]
$T(x,y,z)=(x+y+z,\ y,\ 2x-2y+2z)$; $T(1,2,3)=(6,2,4)$; $\operatorname{Nu}(T)=\operatorname{gen}\{(-1,0,1)\}$; $\operatorname{Im}(T)=\operatorname{gen}\{(1,0,2),(1,1,-2)\}=\{-2p+4q+r=0\}$; $T$ no es mono ni epi; $T^{-1}(\{(3,1,2)\})=(1,1,1)+\operatorname{Nu}(T)$.
:::

</details>

### Ejercicio 10 · Datos dependientes y un parámetro
<!-- ejercicio: U2.10 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $k\in\mathbb{R}$. Se buscan transformaciones lineales $T:\mathbb{R}^3\to\mathbb{R}^2$ con
$$
T(1,0,1)=(1,2),\qquad T(0,1,1)=(0,1),\qquad T(1,1,2)=(k,\ k+2).
$$

a) Para cada valor de $k$, decidir si existe tal $T$ y, cuando existe, si es única.

b) Para el valor de $k$ que corresponda, dar dos transformaciones distintas y hallar $\operatorname{Nu}$ e $\operatorname{Im}$ de una de ellas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los tres vectores del dominio son linealmente dependientes: $(1,1,2)=(1,0,1)+(0,1,1)$. La linealidad impone entonces una condición sobre las imágenes.

**a)** Si $T$ existe, debe cumplir
$$
T(1,1,2)=T(1,0,1)+T(0,1,1)=(1,2)+(0,1)=(1,3).
$$
Como el dato es $T(1,1,2)=(k,k+2)$, hace falta $(k,k+2)=(1,3)$, es decir $k=1$ (y entonces $k+2=3$ también se cumple).

- Si $k\neq 1$: no existe ninguna $T$. Por ejemplo, con $k=0$ el dato pide $T(1,1,2)=(0,2)$, pero la linealidad fuerza $(1,3)$.
- Si $k=1$: los datos son compatibles. Los vectores $(1,0,1)$ y $(0,1,1)$ son LI pero no forman una base de $\mathbb{R}^3$; sobre ellos solo hay datos de un subespacio de dimensión 2, y la imagen de un tercer vector independiente queda libre. Por lo tanto existen infinitas, **no hay unicidad**.

**b)** Para $k=1$ completamos a una base con $e_3=(0,0,1)$: el conjunto $\{(1,0,1),(0,1,1),(0,0,1)\}$ es base (matriz triangular tras reordenar, de determinante 1). Escribimos
$$
(x,y,z)=x(1,0,1)+y(0,1,1)+(z-x-y)(0,0,1),
$$
y para una imagen libre $T(0,0,1)=(p,q)$:
$$
T(x,y,z)=x(1,2)+y(0,1)+(z-x-y)(p,q).
$$

- Con $(p,q)=(0,0)$: $T_0(x,y,z)=(x,\ 2x+y)$.
- Con $(p,q)=(1,0)$: $T_1(x,y,z)=(x+z-x-y,\ 2x+y)=(z-y,\ 2x+y)$.

Son distintas, porque $T_0(0,0,1)=(0,0)$ y $T_1(0,0,1)=(1,0)$.

Para $T_0$: $\operatorname{Nu}(T_0)$ cumple $x=0$ y $2x+y=0$, o sea $x=y=0$: $\operatorname{Nu}(T_0)=\operatorname{gen}\{(0,0,1)\}$. Como $\dim\operatorname{Im}(T_0)=3-1=2$, $\operatorname{Im}(T_0)=\mathbb{R}^2$ y $T_0$ es epimorfismo.

**Comprobación.** $T_1(1,0,1)=(1,2)$, $T_1(0,1,1)=(0,1)$ y $T_1(1,1,2)=(2-1,\ 3)=(1,3)=(k,k+2)$ con $k=1$. Lo mismo vale para $T_0$: $T_0(1,1,2)=(1,3)$.

:::tip[Resultado]
Existe si y solo si $k=1$, y entonces hay infinitas (no es única). Por ejemplo $T_0(x,y,z)=(x,2x+y)$ y $T_1(x,y,z)=(z-y,2x+y)$; $\operatorname{Nu}(T_0)=\operatorname{gen}\{(0,0,1)\}$ e $\operatorname{Im}(T_0)=\mathbb{R}^2$.
:::

</details>

### Ejercicio 11 · Núcleo e imagen prescritos
<!-- ejercicio: U2.11 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) Definir explícitamente una transformación lineal $T:\mathbb{R}^3\to\mathbb{R}^3$ tal que $\operatorname{Nu}(T)=\operatorname{gen}\{(1,1,1)\}$ e $\operatorname{Im}(T)=\operatorname{gen}\{(1,0,1),(0,1,1)\}$.

b) ¿Es única? Justificar.

c) ¿Existe una transformación lineal $S:\mathbb{R}^3\to\mathbb{R}^3$ con $\operatorname{Nu}(S)=\operatorname{gen}\{(1,1,1)\}$ e $\operatorname{Im}(S)=\mathbb{R}^3$?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se extiende el generador del núcleo a una base del dominio; el vector del núcleo va al nulo y los otros dos se mandan a una base de la imagen deseada. Las dimensiones deben cerrar: $1+2=3$.

**a)** Completamos $(1,1,1)$ con $e_1,e_2$: el conjunto $B=\{(1,1,1),e_1,e_2\}$ es base de $\mathbb{R}^3$ (el determinante de la matriz con esas columnas vale 1). Definimos, por el teorema fundamental,

$$
T(1,1,1)=(0,0,0),\qquad T(e_1)=(1,0,1),\qquad T(e_2)=(0,1,1).
$$

Como $e_3=(1,1,1)-e_1-e_2$, resulta $T(e_3)=-(1,0,1)-(0,1,1)=(-1,-1,-2)$ y

$$
T(x,y,z)=x(1,0,1)+y(0,1,1)+z(-1,-1,-2)=(x-z,\ y-z,\ x+y-2z).
$$

*Verificación de las condiciones.* $T(x,y,z)=0$ si y solo si $x=z$, $y=z$, o sea $\operatorname{Nu}(T)=\operatorname{gen}\{(1,1,1)\}$. La imagen está generada por $T(e_1),T(e_2),T(e_3)$ y el tercero es $-(T(e_1)+T(e_2))$, así que $\operatorname{Im}(T)=\operatorname{gen}\{(1,0,1),(0,1,1)\}$.

**b)** No es única. Si intercambiamos las imágenes, $T'(1,1,1)=0$, $T'(e_1)=(0,1,1)$, $T'(e_2)=(1,0,1)$, se obtiene $T'(x,y,z)=(y-z,\ x-z,\ x+y-2z)$, con el mismo núcleo y la misma imagen, pero $T'(e_1)=(0,1,1)\neq(1,0,1)=T(e_1)$.

**c)** No existe. Por el teorema de la dimensión, $\dim\operatorname{Im}(S)=3-\dim\operatorname{Nu}(S)=3-1=2<3$.

**Comprobación.** $T(1,1,1)=(0,0,0)$; $T(1,0,0)=(1,0,1)$; $T(0,1,0)=(0,1,1)$; y $\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)=1+2=3$.

:::tip[Resultado]
a) $T(x,y,z)=(x-z,\ y-z,\ x+y-2z)$. b) No es única (otra: $T'(x,y,z)=(y-z,x-z,x+y-2z)$). c) No existe.
:::

</details>

### Ejercicio 12 · Matriz asociada en bases no canónicas
<!-- ejercicio: U2.12 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(x+y-z,\ 2x-z)$, y sean
$$
B=\{(1,0,1),(0,1,1),(1,1,0)\},\qquad B'=\{(1,0),(1,1)\}.
$$

a) Verificar que $B$ y $B'$ son bases y hallar $M(T)_{BB'}$.

b) Si $[v]_B=(1,2,-1)^t$, hallar $[T(v)]_{B'}$, $T(v)$ y $v$ (en base canónica), y comprobar con la fórmula.

c) Usando $M(T)_{BB'}$, hallar una base de $\operatorname{Nu}(T)$ y decidir si $T$ es epimorfismo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las columnas de $M(T)_{BB'}$ son $[T(b_j)]_{B'}$. En $B'$, un vector $(p,q)$ se escribe $a(1,0)+b(1,1)$ con $a+b=p$ y $b=q$, o sea $[(p,q)]_{B'}=(p-q,\ q)$.

**a)** El determinante de la matriz con columnas $B$ es $\det\begin{pmatrix}1&0&1\\0&1&1\\1&1&0\end{pmatrix}=-2\neq 0$, y el de $B'$ es $\det\begin{pmatrix}1&1\\0&1\end{pmatrix}=1\neq 0$: ambas son bases. Calculamos:

- $T(1,0,1)=(0,1)$, $[T(b_1)]_{B'}=(0-1,\ 1)=(-1,1)$.
- $T(0,1,1)=(0,-1)$, $[T(b_2)]_{B'}=(0+1,\ -1)=(1,-1)$.
- $T(1,1,0)=(2,2)$, $[T(b_3)]_{B'}=(0,\ 2)$.

$$
M(T)_{BB'}=\begin{pmatrix}-1&1&0\\1&-1&2\end{pmatrix}.
$$

**b)** $[T(v)]_{B'}=M(T)_{BB'}[v]_B=\begin{pmatrix}-1&1&0\\1&-1&2\end{pmatrix}\begin{pmatrix}1\\2\\-1\end{pmatrix}=\begin{pmatrix}1\\-3\end{pmatrix}$. Entonces
$$
T(v)=1\cdot(1,0)-3\cdot(1,1)=(-2,-3).
$$
Además $v=1\cdot(1,0,1)+2\cdot(0,1,1)-1\cdot(1,1,0)=(0,1,3)$, y con la fórmula: $T(0,1,3)=(0+1-3,\ 0-3)=(-2,-3)$. Coincide.

**c)** Resolvemos $M(T)_{BB'}[v]_B=0$: la primera fila da $-a+b=0$ y la segunda $a-b+2c=0$, de donde $c=0$ y $a=b$. Entonces $\operatorname{nul}(M)=\operatorname{gen}\{(1,1,0)\}$, y el vector correspondiente del dominio es $1\cdot(1,0,1)+1\cdot(0,1,1)+0\cdot(1,1,0)=(1,1,2)$. Así, $\{(1,1,2)\}$ es base de $\operatorname{Nu}(T)$. Las dos filas de $M$ son independientes, el rango es 2 y $T$ es epimorfismo.

**Comprobación.** $T(1,1,2)=(1+1-2,\ 2-2)=(0,0)$. Con el producto de tres factores: $C_{E'B'}\,[T]_E\,C_{BE}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}1&1&-1\\2&0&-1\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\\1&1&0\end{pmatrix}$ reproduce la misma matriz.

:::tip[Resultado]
$M(T)_{BB'}=\begin{pmatrix}-1&1&0\\1&-1&2\end{pmatrix}$; $[T(v)]_{B'}=(1,-3)^t$, $T(v)=(-2,-3)$, $v=(0,1,3)$; $\operatorname{Nu}(T)=\operatorname{gen}\{(1,1,2)\}$ y $T$ es epimorfismo.
:::

</details>

### Ejercicio 13 · Un operador sobre polinomios con una base adaptada
<!-- ejercicio: U2.13 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:P_2[\mathbb{R}]\to P_2[\mathbb{R}]$, $T(p)(x)=p(x+1)-p(x)$, y sea $B=\{1,\ 1+x,\ 1+x+x^2\}$.

a) Hallar $T(a+bx+cx^2)$ y la matriz $M(T)_E$ en la base canónica.

b) Verificar que $B$ es base y hallar $M(T)_B$.

c) Usando $M(T)_B$, hallar bases de $\operatorname{Nu}(T)$ y de $\operatorname{Im}(T)$.

d) Calcular $M(T\circ T)_B$ y probar que $T\circ T\circ T$ es la transformación nula.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con la base $B$ la matriz de $T$ resulta muy simple; la usamos para leer núcleo e imagen y para calcular potencias.

**a)** Para $p=a+bx+cx^2$: $p(x+1)=a+b(x+1)+c(x+1)^2=(a+b+c)+(b+2c)x+cx^2$. Restando $p(x)$:
$$
T(a+bx+cx^2)=(b+c)+2c\,x.
$$
Esto es lineal en $(a,b,c)$. Sus columnas: $T(1)=0$, $T(x)=1$, $T(x^2)=1+2x$:
$$
M(T)_E=\begin{pmatrix}0&1&1\\0&0&2\\0&0&0\end{pmatrix}.
$$

**b)** En coordenadas canónicas $B$ es $\{(1,0,0),(1,1,0),(1,1,1)\}$, tres vectores LI (matriz triangular con diagonal de unos). Calculamos las imágenes y sus coordenadas en $B$:

- $T(1)=0$, con coordenadas $(0,0,0)$.
- $T(1+x)=1$, con coordenadas $(1,0,0)$.
- $T(1+x+x^2)=2+2x=2(1+x)$, con coordenadas $(0,2,0)$.

$$
M(T)_B=\begin{pmatrix}0&1&0\\0&0&2\\0&0&0\end{pmatrix}.
$$

**c)** *Núcleo:* $M(T)_B[p]_B=0$ da $a_2=0$ y $a_3=0$, con $a_1$ libre: $[p]_B=(1,0,0)$, es decir $p=1$. Entonces $\operatorname{Nu}(T)=\operatorname{gen}\{1\}$ (las constantes). *Imagen:* las columnas no nulas son $(1,0,0)$ y $(0,2,0)$ en coordenadas de $B$, o sea los polinomios $1$ y $2(1+x)$. Una base es $\{1,\ 1+x\}$, y $\operatorname{Im}(T)=P_1[\mathbb{R}]$. Se cumple $3=1+2$.

**d)** Como $M(T\circ T)_B=M(T)_B^{\,2}$,
$$
M(T\circ T)_B=\begin{pmatrix}0&0&2\\0&0&0\\0&0&0\end{pmatrix},\qquad M(T\circ T\circ T)_B=M(T\circ T)_B\,M(T)_B=\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}.
$$
Entonces $T^3=0$. Concretamente, $(T\circ T)(x^2)=T(1+2x)=2$, y $T(2)=0$. (Tiene sentido: la diferencia finita baja el grado en uno, y un polinomio de grado $\le 2$ se anula tras tres diferencias.)

**Comprobación.** $T(1+x+x^2)=\big(1+(x+1)+(x+1)^2\big)-(1+x+x^2)=2+2x$ y $M(T)_E$ aplicada a $(1,1,1)^t$ da $(2,2,0)^t$. Además $M(T)_E^{\,2}=\begin{pmatrix}0&0&2\\0&0&0\\0&0&0\end{pmatrix}$ es igual a $M(T\circ T)_B$: el polinomio constante $2$ tiene las mismas coordenadas $(2,0,0)$ en $E$ y en $B$, porque $1$ es el primer vector de ambas bases.

:::tip[Resultado]
$T(a+bx+cx^2)=(b+c)+2cx$; $M(T)_B=\begin{pmatrix}0&1&0\\0&0&2\\0&0&0\end{pmatrix}$; $\operatorname{Nu}(T)=\operatorname{gen}\{1\}$, $\operatorname{Im}(T)=\operatorname{gen}\{1,1+x\}$; $T\circ T\neq 0$ pero $T\circ T\circ T=0$.
:::

</details>

### Ejercicio 14 · Cambio de base con tres factores
<!-- ejercicio: U2.14 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:\mathbb{R}^2\to\mathbb{R}^3$ con matriz canónica
$$
M(T)_{EE'}=\begin{pmatrix}1&2\\0&1\\1&-1\end{pmatrix}.
$$
Sean $B_1=\{(1,1),(1,2)\}$ base de $\mathbb{R}^2$ y $B_1'=\{(1,0,0),(1,1,0),(1,1,1)\}$ base de $\mathbb{R}^3$.

a) Hallar la fórmula de $T(x,y)$.

b) Hallar $M(T)_{B_1B_1'}$ con la fórmula de tres factores, indicando cada factor.

c) Comprobar el resultado calculando directamente $[T(b_j)]_{B_1'}$, y decidir si $T$ es inyectiva.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La fórmula $M(T)_{B_1B_1'}=C_{E'B_1'}\,M(T)_{EE'}\,C_{B_1E}$ se lee de derecha a izquierda: pasar de $B_1$ a canónica, aplicar $T$, pasar de canónica a $B_1'$.

**a)** $T(x,y)=(x+2y,\ y,\ x-y)$.

**b)** Los factores:

- $C_{B_1E}$ tiene por columnas los vectores de $B_1$ escritos en la base canónica: $C_{B_1E}=\begin{pmatrix}1&1\\1&2\end{pmatrix}$.
- $C_{E'B_1'}=C_{B_1'E'}^{-1}$, donde $C_{B_1'E'}$ tiene por columnas los vectores de $B_1'$. Como $C_{B_1'E'}=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$ (triangular, determinante 1), su inversa es
$$
C_{E'B_1'}=\begin{pmatrix}1&-1&0\\0&1&-1\\0&0&1\end{pmatrix}.
$$

Multiplicamos primero los dos de la derecha:

$$
M(T)_{EE'}\,C_{B_1E}=\begin{pmatrix}1&2\\0&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&2\end{pmatrix}=\begin{pmatrix}3&5\\1&2\\0&-1\end{pmatrix},
$$

que tiene por columnas $T(b_1)=(3,1,0)$ y $T(b_2)=(5,2,-1)$ en canónicas. Luego

$$
M(T)_{B_1B_1'}=\begin{pmatrix}1&-1&0\\0&1&-1\\0&0&1\end{pmatrix}\begin{pmatrix}3&5\\1&2\\0&-1\end{pmatrix}=\begin{pmatrix}2&3\\1&3\\0&-1\end{pmatrix}.
$$

**c)** Directamente: $T(1,1)=(3,1,0)$ y, para escribirlo en $B_1'$, planteamos $\alpha(1,0,0)+\beta(1,1,0)+\gamma(1,1,1)=(3,1,0)$, que da $\gamma=0$, $\beta=1$, $\alpha=2$; la primera columna es $(2,1,0)$. Análogamente $T(1,2)=(5,2,-1)$ da $\gamma=-1$, $\beta=2-\gamma=3$, $\alpha=5-\beta-\gamma=3$; la segunda columna es $(3,3,-1)$. Ambas coinciden con las columnas de la matriz obtenida con los tres factores.

Las dos columnas de $M(T)_{B_1B_1'}$ son LI (rango 2), así que $\operatorname{Nu}(T)=\{0\}$ y $T$ es inyectiva (no es epimorfismo, pues $\dim\operatorname{Im}(T)=2<3$). El rango es el mismo con cualquier par de bases.

**Comprobación.** Reconstruimos $T(b_1)$ desde la matriz: $2(1,0,0)+1(1,1,0)+0(1,1,1)=(3,1,0)$ ✓, y $T(b_2)$: $3(1,0,0)+3(1,1,0)-1(1,1,1)=(5,2,-1)$ ✓.

:::tip[Resultado]
$M(T)_{B_1B_1'}=\begin{pmatrix}2&3\\1&3\\0&-1\end{pmatrix}$. $T$ es monomorfismo y no epimorfismo.
:::

</details>

### Ejercicio 15 · Composición de transformaciones entre $\mathbb{R}^2$ y $\mathbb{R}^3$
<!-- ejercicio: U2.15 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $S:\mathbb{R}^2\to\mathbb{R}^3$, $S(x,y)=(x+y,\ y,\ x-y)$ y $U:\mathbb{R}^3\to\mathbb{R}^2$, $U(x,y,z)=(x+z,\ y-z)$.

a) Hallar $M(S)$, $M(U)$ y la matriz de $U\circ S$. Dar la fórmula de $(U\circ S)(x,y)$.

b) Decidir si $U\circ S$ es isomorfismo y, en tal caso, hallar $(U\circ S)^{-1}$.

c) Hallar la matriz de $S\circ U$ y su núcleo. Decidir si $S\circ U$ puede ser isomorfismo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $M(U\circ S)=M(U)\,M(S)$ (el producto respeta el orden inverso al de aplicación). Para decidir si una composición es isomorfismo conviene mirar el determinante o el paso por el espacio intermedio.

**a)**
$$
M(S)=\begin{pmatrix}1&1\\0&1\\1&-1\end{pmatrix},\qquad M(U)=\begin{pmatrix}1&0&1\\0&1&-1\end{pmatrix},\qquad M(U\circ S)=M(U)M(S)=\begin{pmatrix}2&0\\-1&2\end{pmatrix}.
$$
Es decir, $(U\circ S)(x,y)=(2x,\ 2y-x)$. Directamente: $U(S(x,y))=U(x+y,y,x-y)=(x+y+x-y,\ y-x+y)=(2x,2y-x)$.

**b)** $\det M(U\circ S)=4\neq 0$: es isomorfismo. La inversa es
$$
M(U\circ S)^{-1}=\frac14\begin{pmatrix}2&0\\1&2\end{pmatrix}=\begin{pmatrix}\tfrac12&0\\\tfrac14&\tfrac12\end{pmatrix},\qquad (U\circ S)^{-1}(x,y)=\left(\tfrac x2,\ \tfrac x4+\tfrac y2\right).
$$
Verificación: $\begin{pmatrix}2&0\\-1&2\end{pmatrix}\begin{pmatrix}\tfrac12&0\\\tfrac14&\tfrac12\end{pmatrix}=\begin{pmatrix}1&0\\-\tfrac12+\tfrac12&1\end{pmatrix}=I$.

**c)**
$$
M(S\circ U)=M(S)M(U)=\begin{pmatrix}1&1\\0&1\\1&-1\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&-1\end{pmatrix}=\begin{pmatrix}1&1&0\\0&1&-1\\1&-1&2\end{pmatrix}.
$$
Su determinante es $1\cdot(2-1)-1\cdot(0+1)+0=0$, así que no es iso. Esto se sabía de antemano: $S\circ U$ factoriza por $\mathbb{R}^2$, luego $\dim\operatorname{Im}(S\circ U)\le 2<3$ y no puede ser sobreyectiva, cualesquiera sean $S$ y $U$.

*Núcleo.* Como $S$ es inyectiva (sus columnas son LI), $\operatorname{Nu}(S\circ U)=\operatorname{Nu}(U)$. Resolviendo $x+z=0$, $y-z=0$ se obtiene $z=t$, $x=-t$, $y=t$: $\operatorname{Nu}(S\circ U)=\operatorname{gen}\{(-1,1,1)\}$.

**Comprobación.** $M(S\circ U)(-1,1,1)^t=(-1+1,\ 1-1,\ -1-1+2)=(0,0,0)$ ✓.

:::tip[Resultado]
$M(U\circ S)=\begin{pmatrix}2&0\\-1&2\end{pmatrix}$, isomorfismo, con $(U\circ S)^{-1}(x,y)=(x/2,\ x/4+y/2)$. $S\circ U$ tiene determinante $0$, $\operatorname{Nu}(S\circ U)=\operatorname{gen}\{(-1,1,1)\}$ y nunca puede ser isomorfismo.
:::

</details>

### Ejercicio 16 · Inversa de una transformación de $P_2[\mathbb{R}]$
<!-- ejercicio: U2.16 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $T:P_2[\mathbb{R}]\to P_2[\mathbb{R}]$, $T(p)=p+p'$.

a) Hallar $M(T)_E$ y probar que $T$ es un isomorfismo.

b) Hallar la fórmula de $T^{-1}(q_0+q_1x+q_2x^2)$.

c) Calcular $T^{-1}(3+x+x^2)$ y comprobar.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La inversa de un isomorfismo tiene por matriz la inversa de la matriz: $M(T^{-1})_E=M(T)_E^{-1}$.

**a)** Para $p=a+bx+cx^2$: $T(p)=(a+bx+cx^2)+(b+2cx)=(a+b)+(b+2c)x+cx^2$. Las columnas son $T(1)=1$, $T(x)=1+x$ y $T(x^2)=2x+x^2$:
$$
M(T)_E=\begin{pmatrix}1&1&0\\0&1&2\\0&0&1\end{pmatrix}.
$$
Es triangular con unos en la diagonal, así que $\det=1\neq 0$ y $T$ es isomorfismo (un endomorfismo de un espacio de dimensión finita con matriz inversible).

**b)** Invertimos $M(T)_E$ por Gauss-Jordan: de $(M\mid I)$, restando $2F_3$ a $F_2$ y luego restando $F_2$ a $F_1$ se llega a
$$
M(T)_E^{-1}=\begin{pmatrix}1&-1&2\\0&1&-2\\0&0&1\end{pmatrix}.
$$
Entonces
$$
T^{-1}(q_0+q_1x+q_2x^2)=(q_0-q_1+2q_2)+(q_1-2q_2)x+q_2x^2.
$$

*Otro camino.* Si $D$ es la derivada, $T=I+D$ y $D^3=0$ en $P_2[\mathbb{R}]$. Como $(I+D)(I-D+D^2)=I+D^3=I$, resulta $T^{-1}=I-D+D^2$, que da la misma fórmula: $q-q'+q''=(q_0+q_1x+q_2x^2)-(q_1+2q_2x)+2q_2$.

**c)** Con $(q_0,q_1,q_2)=(3,1,1)$: $T^{-1}(3+x+x^2)=(3-1+2)+(1-2)x+x^2=4-x+x^2$.

**Comprobación.** $T(4-x+x^2)=(4-x+x^2)+(-1+2x)=3+x+x^2$ ✓.

:::tip[Resultado]
$T$ es isomorfismo; $T^{-1}(q_0+q_1x+q_2x^2)=(q_0-q_1+2q_2)+(q_1-2q_2)x+q_2x^2$; $T^{-1}(3+x+x^2)=4-x+x^2$.
:::

</details>

### Ejercicio 17 · Codificar es una transformación lineal
<!-- ejercicio: U2.17 | nivel: intermedio | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Un código transmite mensajes $a=(a_1,a_2,a_3)\in\mathbb{Z}_2^3$ como palabras $T(a)=aG\in\mathbb{Z}_2^5$, con
$$
G=\begin{pmatrix}1&0&0&1&1\\0&1&0&1&0\\0&0&1&0&1\end{pmatrix}.
$$

a) Probar que $T:\mathbb{Z}_2^3\to\mathbb{Z}_2^5$ es una transformación lineal y dar su fórmula.

b) Hallar $\operatorname{Nu}(T)$, la dimensión y la cantidad de elementos de $\operatorname{Im}(T)$, y clasificar $T$.

c) Probar que $\operatorname{Im}(T)=\{u\in\mathbb{Z}_2^5:\ u_4=u_1+u_2,\ u_5=u_1+u_3\}$.

d) Decidir si $(1,1,0,0,1)$ y $(1,0,1,1,1)$ pertenecen a $\operatorname{Im}(T)$ y, de ser así, hallar su preimagen.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Sobre $\mathbb{Z}_2$ la homogeneidad es automática ($\lambda\in\{0,1\}$), así que alcanza con la aditividad, que sale de la distributividad del producto de matrices. Todas las cuentas son módulo 2.

**a)** $T(a+b)=(a+b)G=aG+bG=T(a)+T(b)$, y $T(\lambda a)=\lambda T(a)$ para $\lambda=0$ ($T(0)=0$) y $\lambda=1$ (trivial). Explícitamente,
$$
T(a_1,a_2,a_3)=(a_1,\ a_2,\ a_3,\ a_1+a_2,\ a_1+a_3).
$$
Con la convención de columnas, su matriz es $G^t\in\mathbb{Z}_2^{5\times 3}$.

**b)** $T(a)=0$ obliga a $a_1=a_2=a_3=0$ (las tres primeras componentes son los datos originales). Entonces $\operatorname{Nu}(T)=\{0\}$, $T$ es monomorfismo, $\dim\operatorname{Im}(T)=3$ y $\operatorname{Im}(T)$ tiene $2^3=8$ elementos (las ocho palabras código). Como $\mathbb{Z}_2^5$ tiene $32$ elementos, $T$ no es epimorfismo. No es isomorfismo. La inyectividad es lo que permite decodificar: cada palabra tiene un único mensaje.

**c)** Si $u=T(a)$, entonces $u_4=a_1+a_2=u_1+u_2$ y $u_5=a_1+a_3=u_1+u_3$, así que $\operatorname{Im}(T)$ está contenida en el conjunto $W$ de la derecha. En $W$, $u_1,u_2,u_3$ se eligen libremente y determinan $u_4$ y $u_5$; entonces $|W|=2^3=8=|\operatorname{Im}(T)|$. Una inclusión entre conjuntos finitos del mismo tamaño es una igualdad.

**d)** Para $(1,1,0,0,1)$: $u_4=0=1+1$ ✓ y $u_5=1=1+0$ ✓, así que está en la imagen, con $a=(1,1,0)$: $T(1,1,0)=(1,1,0,1+1,1+0)=(1,1,0,0,1)$ ✓. Como $T$ es inyectiva, la preimagen es el único mensaje $\{(1,1,0)\}$.

Para $(1,0,1,1,1)$: $u_4=1$, pero $u_1+u_2=1+0=1$ ✓; $u_5=1$, pero $u_1+u_3=1+1=0\neq 1$ ✗. No está en la imagen: no es una palabra código, y la preimagen es vacía. Si se recibiera esa palabra, el receptor detectaría un error.

**Comprobación.** Las ocho palabras son $00000$, $10011$, $01010$, $00101$, $11001$, $10110$, $01111$, $11100$ (para $a=000,100,010,001,110,101,011,111$), y todas cumplen $u_4=u_1+u_2$ y $u_5=u_1+u_3$.

:::tip[Resultado]
$T(a)=(a_1,a_2,a_3,a_1+a_2,a_1+a_3)$; $\operatorname{Nu}(T)=\{0\}$, $|\operatorname{Im}(T)|=8$, monomorfismo no epimorfismo; $\operatorname{Im}(T)=\{u_4=u_1+u_2,\ u_5=u_1+u_3\}$; $T^{-1}(1,1,0,0,1)=\{(1,1,0)\}$ y $(1,0,1,1,1)\notin\operatorname{Im}(T)$.
:::

</details>

### Ejercicio 18 · Una transformación de matrices y su matriz
<!-- ejercicio: U2.18 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ y $T:\mathbb{R}^{2\times 2}\to\mathbb{R}^{2\times 2}$, $T(A)=AN-NA$.

a) Hallar $T\begin{pmatrix}a&b\\c&d\end{pmatrix}$ y la matriz $M(T)_E$ en la base canónica.

b) Hallar bases de $\operatorname{Nu}(T)$ y de $\operatorname{Im}(T)$.

c) Decidir si $E_{11}\in\operatorname{Im}(T)$ y describir las preimágenes de $E_{12}$.

d) Calcular $T(T(A))$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Calculamos con $A$ genérica, armamos la matriz $4\times 4$ en $\{E_{11},E_{12},E_{21},E_{22}\}$ y la escalonamos.

**a)** Con $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$: $AN=\begin{pmatrix}0&a\\0&c\end{pmatrix}$ y $NA=\begin{pmatrix}c&d\\0&0\end{pmatrix}$, entonces
$$
T(A)=\begin{pmatrix}-c&a-d\\0&c\end{pmatrix}.
$$
Las columnas de $M(T)_E$ son las coordenadas de $T(E_{11})=E_{12}$, $T(E_{12})=0$, $T(E_{21})=-E_{11}+E_{22}$ y $T(E_{22})=-E_{12}$:
$$
M(T)_E=\begin{pmatrix}0&0&-1&0\\1&0&0&-1\\0&0&0&0\\0&0&1&0\end{pmatrix}.
$$

**b)** El rango es 2 (las columnas 1 y 3 son LI y las demás dependen de ellas). *Núcleo:* $-c=0$, $a-d=0$, con $b$ libre: las matrices $\begin{pmatrix}a&b\\0&a\end{pmatrix}=aI+bE_{12}$. Base: $\{I,\ E_{12}\}$, dimensión 2. *Imagen:* base $\{E_{12},\ -E_{11}+E_{22}\}$ (columnas 1 y 3), dimensión 2. Se cumple $4=2+2$. Es el conjunto de matrices $\begin{pmatrix}-c&s\\0&c\end{pmatrix}$.

**c)** Una matriz de la imagen tiene la forma $\begin{pmatrix}-c&s\\0&c\end{pmatrix}$: la entrada $(1,1)$ es opuesta a la $(2,2)$. Para que la matriz sea $E_{11}$ haría falta $-c=1$ (entrada $(1,1)$) y $c=0$ (entrada $(2,2)$), lo cual es imposible; entonces $E_{11}\notin\operatorname{Im}(T)$. En cambio $E_{12}=T(E_{11})\in\operatorname{Im}(T)$, y la preimagen es
$$
T^{-1}(\{E_{12}\})=E_{11}+\operatorname{Nu}(T)=\left\{\begin{pmatrix}1+\alpha&\beta\\0&\alpha\end{pmatrix}:\ \alpha,\beta\in\mathbb{R}\right\}.
$$

**d)** $T(A)$ tiene $a'=-c$, $b'=a-d$, $c'=0$, $d'=c$, y entonces $T(T(A))=\begin{pmatrix}0&a'-d'\\0&0\end{pmatrix}=\begin{pmatrix}0&-2c\\0&0\end{pmatrix}$. En particular $T\circ T\neq 0$ (por ejemplo, para $A=E_{21}$ da $-2E_{12}$).

**Comprobación.** $T(I)=IN-NI=N-N=0$ y $T(E_{12})=E_{12}N-NE_{12}=0-0=0$ ✓. Además $T(E_{11}+\alpha I+\beta E_{12})=T(E_{11})=E_{12}$ para cualesquiera $\alpha,\beta$.

:::tip[Resultado]
$T(A)=\begin{pmatrix}-c&a-d\\0&c\end{pmatrix}$; $\operatorname{Nu}(T)=\operatorname{gen}\{I,E_{12}\}$; $\operatorname{Im}(T)=\operatorname{gen}\{E_{12},-E_{11}+E_{22}\}$; $E_{11}\notin\operatorname{Im}(T)$; $T^{-1}(\{E_{12}\})=E_{11}+\operatorname{Nu}(T)$; $T(T(A))=-2c\,E_{12}$.
:::

</details>
