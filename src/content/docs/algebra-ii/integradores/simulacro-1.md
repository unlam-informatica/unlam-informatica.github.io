---
title: Simulacro del primer parcial
description: Simulacro original de dos horas sobre espacios vectoriales, cambio de coordenadas, códigos en Z2 y transformaciones lineales, con resolución completa.
slug: algebra-ii/integradores/simulacro-1
sidebar:
  order: 1
  label: Simulacro 1
---

:::note[Sobre este simulacro]
Simulacro **original** preparado para este manual con los temas del primer parcial del programa
2023. No es un examen tomado por la cátedra. Duración sugerida: **2 horas**. Puntaje total: 10
puntos. Todas las respuestas deben estar justificadas.
:::

Temas: subespacios, base y dimensión, coordenadas y cambio de coordenadas
([1.3](/algebra-ii/unidad-1/teoria/subespacios/) a
[1.9](/algebra-ii/unidad-1/teoria/cambio-de-coordenadas/)); espacios sobre $\mathbb{Z}_2$ y códigos
([1.10](/algebra-ii/unidad-1/teoria/codigos-lineales/)); subespacios de una matriz
([1.6](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/)); transformaciones lineales
([Unidad 2](/algebra-ii/unidad-2/)).

## Enunciados

1. **(2,5 puntos)** Subespacio de polinomios y cambio de coordenadas.
2. **(2,5 puntos)** Un código lineal sobre $\mathbb{Z}_2$.
3. **(2,5 puntos)** Una transformación lineal con núcleo e imagen prescritos.
4. **(2,5 puntos)** Bases abstractas, el mismo cálculo en $\mathbb{R}$ y en $\mathbb{Z}_2$, y rango.

Los enunciados completos están a continuación, cada uno seguido de su resolución plegada.

### Ejercicio 1 · Subespacio de polinomios y cambio de coordenadas
<!-- ejercicio: S1.1 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $S=\{p\in P_2[\mathbb{R}]:\ p(1)=2\,p(0)\}$.

a) **(0,75)** Probar que $S$ es un subespacio de $P_2[\mathbb{R}]$.

b) **(0,75)** Hallar una base $B$ de $S$ y su dimensión.

c) **(1)** Sea $B'=\{2+x+x^2,\ x-x^2\}$. Verificar que $B'$ es base de $S$, hallar la matriz de cambio
de coordenadas $C_{BB'}$ y usarla para calcular $[q]_{B'}$, donde $q=3+x+2x^2$.
:::

<details>
<summary>Resolución</summary>

**a)** Usamos el criterio de subespacio con sus tres condiciones.

- El polinomio nulo cumple $0(1)=0=2\cdot 0(0)$, así que $0\in S$.
- Si $p,q\in S$, entonces $(p+q)(1)=p(1)+q(1)=2p(0)+2q(0)=2(p+q)(0)$; luego $p+q\in S$.
- Si $p\in S$ y $\lambda\in\mathbb{R}$, entonces $(\lambda p)(1)=\lambda p(1)=\lambda\,2p(0)=2(\lambda p)(0)$;
  luego $\lambda p\in S$.

Como $S\subseteq P_2[\mathbb{R}]$ cumple las tres condiciones, es subespacio.

**b)** Escribimos un elemento genérico $p=a+bx+cx^2$. Como $p(1)=a+b+c$ y $p(0)=a$, la condición es
$a+b+c=2a$, es decir, $a=b+c$. Entonces

$$
p=(b+c)+bx+cx^2=b\,(1+x)+c\,(1+x^2),\qquad b,c\in\mathbb{R}.
$$

Luego $S=\operatorname{gen}\{1+x,\ 1+x^2\}$. Los dos polinomios son linealmente independientes (ninguno
es múltiplo del otro: uno tiene término en $x$ y el otro no). Por lo tanto
$B=\{1+x,\ 1+x^2\}$ es base de $S$ y $\dim S=2$.

**c)** *$B'$ es base de $S$.* Ambos polinomios están en $S$: para $2+x+x^2$, $p(1)=4=2\cdot 2=2p(0)$;
para $x-x^2$, $p(1)=0=2p(0)$. No son proporcionales, así que son linealmente independientes. Dos
vectores LI en un subespacio de dimensión 2 forman una base.

*Matriz de cambio.* Las columnas de $C_{BB'}$ son las coordenadas de los vectores de $B$ en $B'$.
Para un polinomio $r=\alpha(2+x+x^2)+\beta(x-x^2)=2\alpha+(\alpha+\beta)x+(\alpha-\beta)x^2$:

- $1+x$: $2\alpha=1$, $\alpha+\beta=1$, $\alpha-\beta=0$, de donde $\alpha=\beta=\tfrac12$.
- $1+x^2$: $2\alpha=1$, $\alpha+\beta=0$, $\alpha-\beta=1$, de donde $\alpha=\tfrac12$, $\beta=-\tfrac12$.

$$
C_{BB'}=\begin{pmatrix}\tfrac12 & \tfrac12\\[2pt] \tfrac12 & -\tfrac12\end{pmatrix}.
$$

*Coordenadas de $q$.* Primero $q\in S$: $q(1)=6=2q(0)$. En la base $B$, $q=b(1+x)+c(1+x^2)$ con
$b=1$ (coeficiente de $x$) y $c=2$ (coeficiente de $x^2$); la constante da $b+c=3$, que coincide. Así
$[q]_B=\begin{pmatrix}1\\2\end{pmatrix}$ y

$$
[q]_{B'}=C_{BB'}[q]_B=\begin{pmatrix}\tfrac12 & \tfrac12\\[2pt] \tfrac12 & -\tfrac12\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=\begin{pmatrix}\tfrac32\\[2pt]-\tfrac12\end{pmatrix}.
$$

**Comprobación.** $\tfrac32(2+x+x^2)-\tfrac12(x-x^2)=3+x+2x^2=q$.

:::tip[Resultado]
$B=\{1+x,1+x^2\}$, $\dim S=2$; $C_{BB'}=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ y
$[q]_{B'}=\left(\tfrac32,-\tfrac12\right)^t$.
:::

</details>

### Ejercicio 2 · Un código lineal sobre $\mathbb{Z}_2$
<!-- ejercicio: S1.2 | nivel: intermedio | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C=\operatorname{nul}(H)\subseteq\mathbb{Z}_2^6$, con

$$
H=\begin{pmatrix}1&0&1&1&0&0\\1&1&0&0&1&0\\0&1&1&0&0&1\end{pmatrix}\in\mathbb{Z}_2^{3\times 6}.
$$

a) **(0,75)** Hallar $\dim\mathcal C$, la cantidad de palabras del código, una base y una matriz
generadora $G$ con forma sistemática $G=(I_3\mid A)$.

b) **(0,5)** Codificar el mensaje $a=(1,0,1)$.

c) **(0,75)** Se recibe $v=(1,1,0,0,0,1)$. Sabiendo que hubo a lo sumo un error, decidir si hubo
error, corregirlo y recuperar el mensaje.

d) **(0,5)** Decidir si es verdadera o falsa: "Si el receptor corrige con el síndrome, todo error en dos
posiciones se detecta". Justificar.
:::

<details>
<summary>Resolución</summary>

**a)** Las tres últimas columnas de $H$ forman $I_3$, así que $\operatorname{rango}(H)=3$. Por el teorema
rango–nulidad, $\dim\mathcal C=\dim\operatorname{nul}(H)=6-3=3$: es un código $(6,3)$ con $2^3=8$ palabras.

Como $H=(A^t\mid I_3)$ con $A^t=\begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix}$, la matriz
$G=(I_3\mid A)$ con $A=(A^t)^t$ cumple $GH^t=A+A=0$. Explícitamente,

$$
G=\begin{pmatrix}1&0&0&1&1&0\\0&1&0&0&1&1\\0&0&1&1&0&1\end{pmatrix}.
$$

Sus filas $g_1,g_2,g_3$ están en $\mathcal C$ (por ejemplo, $Hg_1^t=(1+1,\,1+1,\,0)^t=0$) y son LI por el
bloque $I_3$; tres vectores LI en un espacio de dimensión 3 forman base.

**b)** La palabra codificada es $aG=g_1+g_3=(1,0,1,0,1,1)$. Como $G$ es sistemática, las tres primeras
componentes repiten el mensaje.

**c)** Calculamos el síndrome:

$$
Hv^t=\begin{pmatrix}1+0+0+0+0+0\\1+1+0+0+0+0\\0+1+0+0+0+1\end{pmatrix}=\begin{pmatrix}1\\0\\0\end{pmatrix}.
$$

No es nulo, así que $v\notin\mathcal C$: hubo error. El síndrome coincide con la cuarta columna de $H$
(y con ninguna otra), lo que indica un error en la posición 4. Corregimos: $c=(1,1,0,1,0,1)$.

*Comprobación:* $c=g_1+g_2\in\mathcal C$. El mensaje es $(1,1,0)$, las tres primeras componentes.

**d)** **Falsa.** Si se transmite $0$ y se alteran las posiciones 1 y 2, se recibe $(1,1,0,0,0,0)$, con
síndrome $h_1+h_2=(1,1,0)^t+(0,1,1)^t=(1,0,1)^t=h_3$. El receptor "corrige" la posición 3 y obtiene
$(1,1,1,0,0,0)$, que es una palabra del código ($g_1+g_2+g_3$) distinta de la enviada: el error doble
pasa inadvertido. La distancia mínima es 3 (las palabras no nulas tienen pesos 3 y 4), así que el
código puede **corregir** un error **o detectar** hasta dos, pero no ambas cosas a la vez.

:::tip[Resultado]
$\dim\mathcal C=3$, 8 palabras, $G=(I_3\mid A)$ como arriba; $aG=(1,0,1,0,1,1)$; error en la posición 4,
mensaje $(1,1,0)$; d) falsa.
:::

</details>

### Ejercicio 3 · Transformación lineal con núcleo e imagen prescritos
<!-- ejercicio: S1.3 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) **(0,75)** Definir una transformación lineal $T:\mathbb{R}^3\to\mathbb{R}^3$ tal que
$\operatorname{Nu}(T)=\operatorname{gen}\{(1,1,0)\}$ e $\operatorname{Im}(T)=\{(x,y,z):x-y+z=0\}$, con
$T(1,0,0)=(1,1,0)$ y $T(0,0,1)=(0,1,1)$. Justificar que existe y es única, y dar su fórmula.

b) **(0,75)** Hallar $M(T)_{BB'}$ con $B=\{(1,1,0),(1,0,0),(0,0,1)\}$ y $B'=\{(1,1,0),(0,1,1),(1,0,0)\}$.

c) **(0,5)** Usar la matriz del ítem b) para calcular $T(2,-1,3)$.

d) **(0,5)** Clasificar $T$ y hallar $\operatorname{Nu}(T\circ T)$.
:::

<details>
<summary>Resolución</summary>

**a)** Si $T$ cumple lo pedido, $T(1,1,0)=0$. Los vectores $(1,1,0)$, $(1,0,0)$, $(0,0,1)$ forman una base
de $\mathbb{R}^3$ porque

$$
\det\begin{pmatrix}1&1&0\\1&0&0\\0&0&1\end{pmatrix}=-1\neq 0.
$$

Por el teorema fundamental de las transformaciones lineales existe una única $T$ lineal con
$T(1,1,0)=(0,0,0)$, $T(1,0,0)=(1,1,0)$ y $T(0,0,1)=(0,1,1)$. Falta ver que cumple las condiciones.
Su imagen está generada por las imágenes de la base: $\operatorname{Im}(T)=\operatorname{gen}\{(1,1,0),(0,1,1)\}$.
Ambos vectores cumplen $x-y+z=0$ y no son proporcionales; el plano tiene dimensión 2, así que
$\operatorname{Im}(T)$ es exactamente ese plano. Por el teorema de la dimensión,
$\dim\operatorname{Nu}(T)=3-2=1$, y como $(1,1,0)\in\operatorname{Nu}(T)$, resulta
$\operatorname{Nu}(T)=\operatorname{gen}\{(1,1,0)\}$.

*Fórmula.* Escribimos $(x,y,z)=a(1,1,0)+b(1,0,0)+c(0,0,1)$: de la segunda componente $a=y$, de la
primera $b=x-y$ y de la tercera $c=z$. Por linealidad,

$$
T(x,y,z)=(x-y)(1,1,0)+z(0,1,1)=(x-y,\ x-y+z,\ z).
$$

**b)** $B'$ es base: $\det\begin{pmatrix}1&0&1\\1&1&0\\0&1&0\end{pmatrix}=1\neq0$ (vectores en
columnas). Las columnas de $M(T)_{BB'}$ son las coordenadas en $B'$ de las imágenes de los vectores de $B$:

- $T(1,1,0)=(0,0,0)$, coordenadas $(0,0,0)$;
- $T(1,0,0)=(1,1,0)$, que es el primer vector de $B'$: coordenadas $(1,0,0)$;
- $T(0,0,1)=(0,1,1)$, el segundo vector de $B'$: coordenadas $(0,1,0)$.

$$
M(T)_{BB'}=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}.
$$

**c)** Con las fórmulas de a), $[(2,-1,3)]_B=(a,b,c)^t=(-1,\,3,\,3)^t$. Entonces

$$
[T(2,-1,3)]_{B'}=M(T)_{BB'}\begin{pmatrix}-1\\3\\3\end{pmatrix}=\begin{pmatrix}3\\3\\0\end{pmatrix},
$$

y $T(2,-1,3)=3(1,1,0)+3(0,1,1)+0(1,0,0)=(3,6,3)$. **Comprobación** con la fórmula:
$(2+1,\ 2+1+3,\ 3)=(3,6,3)$.

**d)** $\operatorname{Nu}(T)\neq\{0\}$, así que $T$ no es monomorfismo; $\dim\operatorname{Im}(T)=2<3$, así
que no es epimorfismo. No es isomorfismo.

Componiendo, $T(T(x,y,z))=T(x-y,\ x-y+z,\ z)=(-z,\ 0,\ z)$. Se anula si y solo si $z=0$:

$$
\operatorname{Nu}(T\circ T)=\{(x,y,0)\}=\operatorname{gen}\{(1,0,0),(0,1,0)\},\qquad \dim=2.
$$

Contiene a $\operatorname{Nu}(T)$, como debe ocurrir siempre: si $T(v)=0$, entonces $T(T(v))=T(0)=0$.

:::tip[Resultado]
$T(x,y,z)=(x-y,\ x-y+z,\ z)$; $M(T)_{BB'}$ como arriba; $T(2,-1,3)=(3,6,3)$; ni mono ni epi;
$\operatorname{Nu}(T\circ T)=\{z=0\}$.
:::

</details>

### Ejercicio 4 · Bases abstractas, $\mathbb{R}$ y $\mathbb{Z}_2$, y rango
<!-- ejercicio: S1.4 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $V$ un espacio vectorial real con base $B=\{v_1,v_2,v_3\}$ y sea
$B'=\{v_1+v_2,\ v_2+v_3,\ v_1+v_3\}$.

a) **(1)** Probar que $B'$ es base de $V$, hallar $C_{B'B}$ y $C_{BB'}$, y calcular las coordenadas de
$w=2v_1-v_2+3v_3$ en la base $B'$.

b) **(0,75)** Si $V$ fuera un espacio vectorial sobre $\mathbb{Z}_2$ con base $B$, ¿$B'$ sería base?
Justificar.

c) **(0,75)** Sea $A\in\mathbb{R}^{3\times 5}$ con $\operatorname{rango}(A)=3$. Hallar
$\dim\operatorname{nul}(A)$ y decidir si el sistema $Ax=b$ es compatible para todo $b\in\mathbb{R}^3$.
:::

<details>
<summary>Resolución</summary>

**a)** Las coordenadas en $B$ de los vectores de $B'$ son $(1,1,0)$, $(0,1,1)$ y $(1,0,1)$; esas
columnas forman $C_{B'B}$:

$$
C_{B'B}=\begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},\qquad \det C_{B'B}=2\neq 0.
$$

Como la función coordenadas es un isomorfismo, tres vectores de $V$ son LI si y solo si sus
coordenadas lo son; el determinante no nulo muestra que $B'$ es LI y, al tener tres vectores en un
espacio de dimensión 3, es base. Además

$$
C_{BB'}=(C_{B'B})^{-1}=\frac12\begin{pmatrix}1&1&-1\\-1&1&1\\1&-1&1\end{pmatrix},
$$

lo que se comprueba multiplicando: $C_{B'B}\,C_{BB'}=I$. Entonces

$$
[w]_{B'}=C_{BB'}[w]_B=\frac12\begin{pmatrix}1&1&-1\\-1&1&1\\1&-1&1\end{pmatrix}\begin{pmatrix}2\\-1\\3\end{pmatrix}=\begin{pmatrix}-1\\0\\3\end{pmatrix}.
$$

**Comprobación.** $-(v_1+v_2)+0\,(v_2+v_3)+3(v_1+v_3)=2v_1-v_2+3v_3=w$.

**b)** **No.** Sobre $\mathbb{Z}_2$ el determinante vale $2=0$. Directamente:
$(v_1+v_2)+(v_2+v_3)=v_1+2v_2+v_3=v_1+v_3$, porque $2v_2=0$ en $\mathbb{Z}_2$. El tercer vector es
combinación de los otros dos: $B'$ es LD. Las mismas expresiones dan una base en un cuerpo y no en el
otro: la independencia depende del cuerpo.

**c)** Por el teorema rango–nulidad, $\dim\operatorname{nul}(A)=5-3=2$. Además
$\dim\operatorname{col}(A)=\operatorname{rango}(A)=3$ y $\operatorname{col}(A)\subseteq\mathbb{R}^3$, así que
$\operatorname{col}(A)=\mathbb{R}^3$. Como $Ax=b$ es compatible si y solo si $b\in\operatorname{col}(A)$,
el sistema es compatible para todo $b$ (y, como la nulidad es 2, indeterminado).

:::tip[Resultado]
$[w]_{B'}=(-1,0,3)^t$; sobre $\mathbb{Z}_2$, $B'$ no es base; $\dim\operatorname{nul}(A)=2$ y $Ax=b$
siempre es compatible indeterminado.
:::

</details>
