---
title: Práctica — Guía integradora
description: Cinco problemas de varios ítems sobre transformaciones lineales, con puntaje orientativo y resolución completa, en el formato de un parcial.
slug: algebra-ii/unidad-2/practica/guia-integradora
sidebar:
  order: 4
  label: Guía integradora
---

Esta guía integra toda la unidad en problemas de varios ítems, con el formato de una evaluación escrita: cada problema vale **2,5 puntos** orientativos repartidos entre sus ítems, de modo que cuatro problemas cualesquiera suman un parcial de 10 puntos. Presupone las ocho lecciones de la unidad: [definición y ejemplos](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/), [núcleo e imagen](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/), [teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/), [clasificación](/algebra-ii/unidad-2/teoria/clasificacion/), [teorema fundamental](/algebra-ii/unidad-2/teoria/teorema-fundamental/), [matriz asociada](/algebra-ii/unidad-2/teoria/matriz-asociada/), [cambio de base](/algebra-ii/unidad-2/teoria/cambio-de-base/) y [composición e inversa](/algebra-ii/unidad-2/teoria/composicion-e-inversa/).

Cómo usarla: elegí uno o varios problemas y resolvelos con tiempo limitado (unos 25 minutos por problema), explicitando y justificando cada paso, como se pide en una evaluación. Después abrí la resolución y comparala ítem por ítem. Los enunciados son originales de este manual y no corresponden a ninguna evaluación de la cátedra. Antes de esta página conviene haber hecho el [nivel avanzado](/algebra-ii/unidad-2/practica/nivel-avanzado/).

### Ejercicio 28 · Problema 1: una transformación de $\mathbb{R}^3$ en $P_2[\mathbb{R}]$
<!-- ejercicio: U2.28 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $B=\{(1,0,0),(1,1,0),(1,1,1)\}$, base de $\mathbb{R}^3$, y sea $T:\mathbb{R}^3\to P_2[\mathbb{R}]$ la transformación lineal con
$$
T(1,0,0)=1+x,\qquad T(1,1,0)=x-x^2,\qquad T(1,1,1)=1+x^2.
$$

a) **(0,75)** Hallar $T(a,b,c)$.

b) **(0,75)** Hallar bases de $\operatorname{Nu}(T)$ y de $\operatorname{Im}(T)$ y clasificar $T$.

c) **(0,5)** Decidir si $q=2+x+x^2\in\operatorname{Im}(T)$ y hallar todos los vectores $v$ con $T(v)=q$.

d) **(0,5)** ¿Existe una transformación lineal $S:P_2[\mathbb{R}]\to\mathbb{R}^3$ con $S\circ T=\operatorname{id}_{\mathbb{R}^3}$? ¿Y una $S$ con $T\circ S=\operatorname{id}_{P_2[\mathbb{R}]}$?
:::

<details>
<summary>Resolución</summary>

**a)** Escribimos $(a,b,c)=\alpha(1,0,0)+\beta(1,1,0)+\gamma(1,1,1)$, que da $\gamma=c$, $\beta=b-c$, $\alpha=a-b$. Por linealidad,
$$
T(a,b,c)=(a-b)(1+x)+(b-c)(x-x^2)+c(1+x^2)=(a-b+c)+(a-c)x+(2c-b)x^2.
$$

**b)** Las imágenes de la base canónica son $T(e_1)=1+x$, $T(e_2)=-1-x^2$ y $T(e_3)=1-x+2x^2$, con coordenadas en $\{1,x,x^2\}$:
$$
M(T)_{EE'}=\begin{pmatrix}1&-1&1\\1&0&-1\\0&-1&2\end{pmatrix}\sim\begin{pmatrix}1&0&-1\\0&1&-2\\0&0&0\end{pmatrix}.
$$
*Núcleo:* $a=c$, $b=2c$, es decir $\operatorname{Nu}(T)=\operatorname{gen}\{(1,2,1)\}$, base $\{(1,2,1)\}$. *Imagen:* columnas pivote 1 y 2, que generan $\operatorname{gen}\{1+x,\ 1+x^2\}$ (la segunda columna es $-(1+x^2)$); base $\{1+x,\ 1+x^2\}$. Dimensiones: $1+2=3$. $T$ no es mono (núcleo no nulo) ni epi ($\dim\operatorname{Im}(T)=2<3=\dim P_2[\mathbb{R}]$).

**c)** Un polinomio $\alpha(1+x)+\beta(1+x^2)$ tiene coeficiente de $x$ igual a $\alpha$, de $x^2$ igual a $\beta$ y término independiente $\alpha+\beta$. Para $q=2+x+x^2$: $\alpha=1$, $\beta=1$, $\alpha+\beta=2$ ✓. Entonces $q\in\operatorname{Im}(T)$; de hecho $T(1,-1,0)=(1+1+0)+(1-0)x+(0+1)x^2=2+x+x^2=q$. Luego
$$
T^{-1}(\{q\})=\{(1,-1,0)+t(1,2,1):\ t\in\mathbb{R}\}.
$$

**d)** Si $S\circ T=\operatorname{id}_{\mathbb{R}^3}$, la composición es inyectiva y entonces $T$ lo sería; pero $\operatorname{Nu}(T)\neq\{0\}$ (por ejemplo, $(S\circ T)(1,2,1)=S(0)=0\neq(1,2,1)$). No existe. Si $T\circ S=\operatorname{id}_{P_2[\mathbb{R}]}$, la composición es sobreyectiva y entonces $T$ lo sería; pero $\dim\operatorname{Im}(T)=2<3$ (el polinomio $x^2$ no está en la imagen: $\alpha=0$, $\beta=1$ da término independiente $1\neq 0$). No existe.

**Comprobación.** $T(1,2,1)=(1-2+1)+(1-1)x+(2-2)x^2=0$ ✓; $T(1,1,1)=1+x^2$ ✓.

:::tip[Resultado]
a) $T(a,b,c)=(a-b+c)+(a-c)x+(2c-b)x^2$. b) $\operatorname{Nu}(T)=\operatorname{gen}\{(1,2,1)\}$, $\operatorname{Im}(T)=\operatorname{gen}\{1+x,1+x^2\}$; ni mono ni epi. c) $q\in\operatorname{Im}(T)$ y $T^{-1}(\{q\})=(1,-1,0)+\operatorname{Nu}(T)$. d) Ninguna de las dos existe.
:::

</details>

### Ejercicio 29 · Problema 2: un endomorfismo del plano con un parámetro
<!-- ejercicio: U2.29 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $B=\{(1,1),(1,2)\}$ y, para $k\in\mathbb{R}$, sea $T_k:\mathbb{R}^2\to\mathbb{R}^2$ la transformación lineal con
$$
M(T_k)_B=\begin{pmatrix}1&-1\\2&k\end{pmatrix}.
$$

a) **(0,75)** Hallar $M(T_k)_E$ en función de $k$.

b) **(0,5)** Determinar para qué valores de $k$ la transformación $T_k$ es un isomorfismo.

c) **(0,75)** Para el valor de $k$ en que no lo es, hallar bases de $\operatorname{Nu}(T_k)$ y de $\operatorname{Im}(T_k)$ (en $\mathbb{R}^2$).

d) **(0,5)** Para ese valor de $k$, calcular $M(T_k\circ T_k)_E$ y expresar $T_k\circ T_k$ en términos de $T_k$.
:::

<details>
<summary>Resolución</summary>

**a)** Usamos $M(T)_E=C_{BE}\,M(T)_B\,C_{EB}$ con $C_{BE}=\begin{pmatrix}1&1\\1&2\end{pmatrix}$ y $C_{EB}=C_{BE}^{-1}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$. Primero
$$
C_{BE}M(T_k)_B=\begin{pmatrix}1&1\\1&2\end{pmatrix}\begin{pmatrix}1&-1\\2&k\end{pmatrix}=\begin{pmatrix}3&k-1\\5&2k-1\end{pmatrix},
$$
y luego
$$
M(T_k)_E=\begin{pmatrix}3&k-1\\5&2k-1\end{pmatrix}\begin{pmatrix}2&-1\\-1&1\end{pmatrix}=\begin{pmatrix}7-k&k-4\\11-2k&2k-6\end{pmatrix}.
$$

**b)** $T_k$ es isomorfismo si y solo si $\det M(T_k)_B\neq 0$ (el determinante no depende de la base, porque las matrices son semejantes). Como $\det M(T_k)_B=k+2$, es isomorfismo si y solo si $k\neq -2$.

**c)** Para $k=-2$:
$$
M(T_{-2})_E=\begin{pmatrix}9&-6\\15&-10\end{pmatrix}.
$$
La segunda fila es $\tfrac53$ de la primera, así que el rango es 1. *Núcleo:* $9x-6y=0$, es decir $3x=2y$: $\operatorname{Nu}(T_{-2})=\operatorname{gen}\{(2,3)\}$. *Imagen:* la primera columna $(9,15)=3(3,5)$ genera: $\operatorname{Im}(T_{-2})=\operatorname{gen}\{(3,5)\}$. Se cumple $1+1=2$.

Control con $M(T_{-2})_B=\begin{pmatrix}1&-1\\2&-2\end{pmatrix}$: su núcleo es $\operatorname{gen}\{(1,1)\}$ en coordenadas de $B$, o sea el vector $1\cdot(1,1)+1\cdot(1,2)=(2,3)$ ✓; su primera columna $(1,2)_B$ es el vector $(1,1)+2(1,2)=(3,5)$ ✓.

**d)**
$$
\begin{pmatrix}9&-6\\15&-10\end{pmatrix}^2=\begin{pmatrix}81-90&-54+60\\135-150&-90+100\end{pmatrix}=\begin{pmatrix}-9&6\\-15&10\end{pmatrix}=-M(T_{-2})_E.
$$
Entonces $T_{-2}\circ T_{-2}=-T_{-2}$. En particular, sobre la imagen $T_{-2}(3,5)=-(3,5)$: la transformación invierte el sentido de los vectores de su imagen.

**Comprobación.** $M(T_{-2})_E(2,3)^t=(18-18,\ 30-30)=(0,0)$ ✓ y $M(T_{-2})_E(3,5)^t=(27-30,\ 45-50)=(-3,-5)$ ✓.

:::tip[Resultado]
a) $M(T_k)_E=\begin{pmatrix}7-k&k-4\\11-2k&2k-6\end{pmatrix}$. b) Isomorfismo si y solo si $k\neq-2$. c) Para $k=-2$: $\operatorname{Nu}=\operatorname{gen}\{(2,3)\}$, $\operatorname{Im}=\operatorname{gen}\{(3,5)\}$. d) $T_{-2}\circ T_{-2}=-T_{-2}$.
:::

</details>

### Ejercicio 30 · Problema 3: codificar y detectar errores
<!-- ejercicio: U2.30 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Sea $T:\mathbb{Z}_2^3\to\mathbb{Z}_2^5$, $T(a)=aG$, con
$$
G=\begin{pmatrix}1&0&1&1&0\\0&1&1&0&1\\1&1&0&1&1\end{pmatrix},
$$
y sea $S:\mathbb{Z}_2^5\to\mathbb{Z}_2^2$, $S(x)=(x_1+x_3+x_5,\ x_2+x_3+x_4)$.

a) **(0,75)** Probar que $T$ es lineal, hallar $\operatorname{Nu}(T)$, listar los elementos de $\operatorname{Im}(T)$ y clasificar $T$.

b) **(0,5)** Hallar todos los mensajes $a$ con $T(a)=(1,1,0,1,1)$.

c) **(0,5)** Probar que $S\circ T$ es la transformación nula.

d) **(0,75)** El receptor calcula $S$ sobre la palabra recibida. Para $r=(1,0,0,1,1)$, ¿se puede asegurar que no es una palabra código? ¿Vale que $S(x)=0$ implique $x\in\operatorname{Im}(T)$? Justificar.
:::

<details>
<summary>Resolución</summary>

**a)** Sobre $\mathbb{Z}_2$ alcanza la aditividad: $T(a+b)=(a+b)G=aG+bG=T(a)+T(b)$. Explícitamente,
$$
T(a_1,a_2,a_3)=(a_1+a_3,\ a_2+a_3,\ a_1+a_2,\ a_1+a_3,\ a_2+a_3).
$$
*Núcleo:* $T(a)=0$ exige $a_1=a_3$, $a_2=a_3$ y $a_1=a_2$; con los tres iguales resulta $\operatorname{Nu}(T)=\{(0,0,0),(1,1,1)\}=\operatorname{gen}\{(1,1,1)\}$, de dimensión 1. Entonces $\dim\operatorname{Im}(T)=3-1=2$ y $\operatorname{Im}(T)$ tiene $4$ elementos: la fila 3 de $G$ es la suma de las filas 1 y 2, así que $\operatorname{Im}(T)=\operatorname{gen}\{(1,0,1,1,0),(0,1,1,0,1)\}$, es decir
$$
\operatorname{Im}(T)=\{(0,0,0,0,0),\ (1,0,1,1,0),\ (0,1,1,0,1),\ (1,1,0,1,1)\}.
$$
$T$ no es mono (núcleo no nulo) ni epi ($4<32$).

**b)** $(1,1,0,1,1)=T(0,0,1)$ (tercera fila de $G$). Todos los mensajes son $(0,0,1)+\operatorname{Nu}(T)=\{(0,0,1),\ (1,1,0)\}$. Verificación: $T(1,1,0)=(1,0,1,1,0)+(0,1,1,0,1)=(1,1,0,1,1)$ ✓.

**c)** Basta ver $S(T(e_i))=0$ para la base canónica (las filas de $G$), y la linealidad hace el resto. $S(1,0,1,1,0)=(1+1+0,\ 0+1+1)=(0,0)$; $S(0,1,1,0,1)=(0+1+1,\ 1+1+0)=(0,0)$; $S(1,1,0,1,1)=(1+0+1,\ 1+0+1)=(0,0)$. Entonces $S\circ T=0$, o sea $\operatorname{Im}(T)\subseteq\operatorname{Nu}(S)$.

**d)** $S(r)=(1+0+1,\ 0+0+1)=(0,1)\neq(0,0)$. Si $r$ fuera palabra código estaría en $\operatorname{Im}(T)\subseteq\operatorname{Nu}(S)$ y $S(r)$ sería nulo; como no lo es, **se puede asegurar que $r$ no es palabra código** (se detecta un error).

La recíproca es falsa. $S$ es sobreyectiva ($S(1,0,0,0,0)=(1,0)$ y $S(0,1,0,0,0)=(0,1)$), así que $\dim\operatorname{Nu}(S)=5-2=3>2=\dim\operatorname{Im}(T)$. Un contraejemplo: $z=(1,1,1,0,0)$ cumple $S(z)=(1+1+0,\ 1+1+0)=(0,0)$, pero $z\notin\operatorname{Im}(T)$ (no es ninguna de las cuatro palabras). Entonces $S(x)=0$ no alcanza para asegurar que $x$ es palabra código.

**Comprobación.** Los cuatro elementos de $\operatorname{Im}(T)$ están en $\operatorname{Nu}(S)$ (se verificó en c), y el tamaño $|\operatorname{Nu}(S)|=2^3=8>4$ confirma que hay palabras con síndrome nulo fuera de la imagen.

:::tip[Resultado]
a) $\operatorname{Nu}(T)=\{000,111\}$, $|\operatorname{Im}(T)|=4$, ni mono ni epi. b) $T^{-1}(1,1,0,1,1)=\{(0,0,1),(1,1,0)\}$. c) $S\circ T=0$. d) $r$ no es palabra código ($S(r)=(0,1)$), pero $S(z)=0$ para $z=(1,1,1,0,0)\notin\operatorname{Im}(T)$.
:::

</details>

### Ejercicio 31 · Problema 4: transformaciones de cuadrado nulo
<!-- ejercicio: U2.31 | nivel: avanzado | tipo: demostracion | verificacion: sympy -->

:::note[Enunciado]
Sea $V$ un espacio de dimensión finita y $T:V\to V$ lineal con $T\circ T=0$.

a) **(0,75)** Probar que $\operatorname{Im}(T)\subseteq\operatorname{Nu}(T)$ y que $2\dim\operatorname{Im}(T)\le\dim V$.

b) **(0,5)** Verificar con $T:\mathbb{R}^4\to\mathbb{R}^4$, $T(x,y,z,w)=(z,w,0,0)$: comprobar que $T\circ T=0$ y hallar $\operatorname{Nu}(T)$ e $\operatorname{Im}(T)$.

c) **(0,5)** ¿Existe una transformación lineal $T:\mathbb{R}^3\to\mathbb{R}^3$ con $T\circ T=0$ y $\operatorname{rango}(T)=2$?

d) **(0,75)** Probar que $I+T$ es un isomorfismo con inversa $I-T$, y calcular $(I+T)(1,2,3,4)$ para la $T$ del ítem b), junto con su imagen por $(I-T)$.
:::

<details>
<summary>Resolución</summary>

**a)** Sea $w\in\operatorname{Im}(T)$, o sea $w=T(v)$. Entonces $T(w)=T(T(v))=0$, así que $w\in\operatorname{Nu}(T)$. Luego $\operatorname{Im}(T)\subseteq\operatorname{Nu}(T)$ y $\dim\operatorname{Im}(T)\le\dim\operatorname{Nu}(T)$. Por el teorema de la dimensión,
$$
\dim V=\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)\ge 2\dim\operatorname{Im}(T).\qquad\blacksquare
$$

**b)** $T(T(x,y,z,w))=T(z,w,0,0)=(0,0,0,0)$. Núcleo: $z=w=0$, es decir $\operatorname{Nu}(T)=\operatorname{gen}\{e_1,e_2\}$. Imagen: $\{(z,w,0,0)\}=\operatorname{gen}\{e_1,e_2\}$. Coinciden, de dimensión 2, y $2\cdot 2\le 4$ se cumple con igualdad.

**c)** No existe. Por a), $2\cdot 2\le 3$ sería falso. Con $\operatorname{rango}\le 1$ sí se puede: $T(x,y,z)=(y,0,0)$ tiene $T\circ T=0$ y rango 1.

**d)** $(I+T)(I-T)=I-T+T-T\circ T=I-T\circ T=I$, y análogamente $(I-T)(I+T)=I$. Entonces $I+T$ es inversible con inversa $I-T$, y por lo tanto isomorfismo. Para el ítem b): $(I+T)(1,2,3,4)=(1,2,3,4)+(3,4,0,0)=(4,6,3,4)$ y
$$
(I-T)(4,6,3,4)=(4,6,3,4)-(3,4,0,0)=(1,2,3,4).
$$

**Comprobación.** La matriz de $T$ en el ítem b) es $\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&0&0&0\\0&0&0&0\end{pmatrix}$, cuyo cuadrado es nulo, y $\det(I+T)=1$ (triangular superior con unos en la diagonal).

:::tip[Resultado]
a) $\operatorname{Im}(T)\subseteq\operatorname{Nu}(T)$ y $2\dim\operatorname{Im}(T)\le\dim V$. b) $\operatorname{Nu}(T)=\operatorname{Im}(T)=\operatorname{gen}\{e_1,e_2\}$. c) No existe. d) $(I+T)^{-1}=I-T$; $(I+T)(1,2,3,4)=(4,6,3,4)$.
:::

</details>

### Ejercicio 32 · Problema 5: trasladar y rotar con coordenadas homogéneas
<!-- ejercicio: U2.32 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
En gráficos 2D, el punto $(x,y)$ se representa por el vector $(x,y,1)$ de $\mathbb{R}^3$. Sea $\operatorname{Tr}:\mathbb{R}^2\to\mathbb{R}^2$ la traslación $\operatorname{Tr}(x,y)=(x+2,\ y-1)$.

a) **(0,5)** Probar que $\operatorname{Tr}$ no es una transformación lineal.

b) **(0,5)** Sea $H:\mathbb{R}^3\to\mathbb{R}^3$ la transformación de matriz
$$
H=\begin{pmatrix}1&0&2\\0&1&-1\\0&0&1\end{pmatrix}.
$$
Probar que $H(x,y,1)=(x+2,y-1,1)$ y que $H$ es un isomorfismo, hallando su inversa.

c) **(0,5)** Sea $R$ la rotación de $90^\circ$ antihoraria alrededor del origen, $R(x,y)=(-y,x)$, representada por $\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}$. Hallar la matriz de "rotar y después trasladar" y la imagen de $(1,0)$ y de $(3,2)$.

d) **(1,0)** Hallar la matriz $Q$ de la rotación de $90^\circ$ antihoraria alrededor del punto $(1,1)$ como composición de tres transformaciones, y verificar que fija $(1,1)$ y calcular la imagen de $(2,1)$.
:::

<details>
<summary>Resolución</summary>

**a)** Toda transformación lineal cumple $T(0)=0$, pero $\operatorname{Tr}(0,0)=(2,-1)\neq(0,0)$. También falla la aditividad: $\operatorname{Tr}(1,0)+\operatorname{Tr}(0,1)=(3,-1)+(2,0)=(5,-1)$, mientras que $\operatorname{Tr}(1,1)=(3,0)$.

**b)** Multiplicando, $H(x,y,1)^t=(x+2,\ y-1,\ 1)^t$: sobre los vectores con tercera coordenada 1, $H$ realiza la traslación. Es lineal por ser matricial, y $\det H=1\neq 0$, por lo que es isomorfismo. Su inversa es la traslación opuesta:
$$
H^{-1}=\begin{pmatrix}1&0&-2\\0&1&1\\0&0&1\end{pmatrix},
$$
pues $H^{-1}(x+2,y-1,1)^t=(x,y,1)^t$. Así, el truco consiste en que la traslación, que no es lineal en $\mathbb{R}^2$, es la restricción de una transformación lineal de $\mathbb{R}^3$.

**c)** La rotación de $90^\circ$ antihoraria es $R(x,y)=(-y,\ x)$. Rotar y después trasladar corresponde al producto, con $R$ a la derecha:
$$
HR=\begin{pmatrix}1&0&2\\0&1&-1\\0&0&1\end{pmatrix}\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}=\begin{pmatrix}0&-1&2\\1&0&-1\\0&0&1\end{pmatrix}.
$$
Para $(1,0)$: $HR(1,0,1)^t=(2,\ 0,\ 1)^t$, el punto $(2,0)$ (rota a $(0,1)$ y traslada a $(2,0)$). Para $(3,2)$: $HR(3,2,1)^t=(-2+2,\ 3-1,\ 1)^t=(0,2,1)^t$, el punto $(0,2)$. Notemos que $RH\neq HR$: por ejemplo $RH=\begin{pmatrix}0&-1&1\\1&0&2\\0&0&1\end{pmatrix}$, de modo que trasladar antes y rotar después es otra transformación.

**d)** Para rotar alrededor de $(1,1)$: trasladar por $(-1,-1)$ (el centro va al origen), rotar, y trasladar por $(1,1)$. Con matrices, aplicando de derecha a izquierda,
$$
Q=H_{(1,1)}\,R\,H_{(-1,-1)}=\begin{pmatrix}1&0&1\\0&1&1\\0&0&1\end{pmatrix}\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&-1\\0&1&-1\\0&0&1\end{pmatrix}.
$$
Primero $R\,H_{(-1,-1)}=\begin{pmatrix}0&-1&1\\1&0&-1\\0&0&1\end{pmatrix}$ y luego
$$
Q=\begin{pmatrix}0&-1&2\\1&0&0\\0&0&1\end{pmatrix}.
$$
*Punto fijo:* $Q(1,1,1)^t=(-1+2,\ 1,\ 1)^t=(1,1,1)^t$ ✓. *Imagen de $(2,1)$:* $Q(2,1,1)^t=(-1+2,\ 2,\ 1)^t=(1,2,1)^t$, el punto $(1,2)$: el vector $(1,0)$ desde el centro pasa a $(0,1)$ ✓.

**Comprobación.** $Q^4=I$ (cuatro giros de $90^\circ$ dan la vuelta completa) y $\det Q=1$, porque la rotación conserva la orientación. Además $Q(0,1,1)^t=(1,0,1)^t$, el punto $(1,0)$: el vector $(-1,0)$ desde el centro pasa a $(0,-1)$ ✓.

:::tip[Resultado]
a) $\operatorname{Tr}(0,0)\neq 0$. b) $H^{-1}=\begin{pmatrix}1&0&-2\\0&1&1\\0&0&1\end{pmatrix}$. c) $HR=\begin{pmatrix}0&-1&2\\1&0&-1\\0&0&1\end{pmatrix}$, $(1,0)\mapsto(2,0)$, $(3,2)\mapsto(0,2)$. d) $Q=\begin{pmatrix}0&-1&2\\1&0&0\\0&0&1\end{pmatrix}$, fija $(1,1)$ y manda $(2,1)$ a $(1,2)$.
:::

</details>
