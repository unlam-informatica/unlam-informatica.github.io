---
title: Práctica — Guía integradora
description: Cinco problemas de varios ítems sobre toda la Unidad 1, con puntaje orientativo y resolución completa, para ensayar un examen de espacios vectoriales, coordenadas y códigos.
slug: algebra-ii/unidad-1/practica/guia-integradora
sidebar:
  order: 4
  label: Guía integradora
---

## Cómo usar esta página

Esta guía reúne cinco problemas de varios ítems, pensados como práctica de examen sobre toda la Unidad 1.
Cada problema vale **2 puntos** (total orientativo: 10) y cada ítem indica su puntaje entre paréntesis. Los
enunciados son **originales** de este manual; el puntaje es solo una referencia para administrar el tiempo.
Sugerencia: resolver los cinco problemas en una sola sesión de dos horas, sin apuntes, y recién después abrir
las resoluciones. Todas las respuestas deben justificarse.

Lecciones que se presuponen: todas las de la unidad, en particular
[1.3 Subespacios](/algebra-ii/unidad-1/teoria/subespacios/),
[1.5 Independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/),
[1.6 Subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/),
[1.7 Base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/),
[1.9 Cambio de coordenadas](/algebra-ii/unidad-1/teoria/cambio-de-coordenadas/) y
[1.10 Códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/). Conviene haber pasado antes por los
niveles [inicial](/algebra-ii/unidad-1/practica/nivel-inicial/),
[intermedio](/algebra-ii/unidad-1/practica/nivel-intermedio/) y
[avanzado](/algebra-ii/unidad-1/practica/nivel-avanzado/).

### Problema 1 · Un subespacio de polinomios y sus bases
<!-- ejercicio: U1.26 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $S=\{p\in P_2[\mathbb{R}]:\ p(2)=p(0)\}$.

a) **(0,5)** Probar que $S$ es un subespacio de $P_2[\mathbb{R}]$.

b) **(0,5)** Hallar una base $B$ de $S$ y $\dim S$.

c) **(0,5)** Verificar que $B'=\{1-2x+x^2,\ 1-4x+2x^2\}$ es base de $S$ y hallar $C_{BB'}$.

d) **(0,5)** Calcular $[q]_{B'}$ para $q=5-6x+3x^2$ y extender $B$ a una base de $P_2[\mathbb{R}]$.
:::

<details>
<summary>Resolución</summary>

**a)** Para $p=a+bx+cx^2$: $p(2)=a+2b+4c$ y $p(0)=a$, de modo que $p\in S\iff 2b+4c=0\iff b=-2c$. Verificamos
las tres condiciones sobre la definición original: el polinomio nulo cumple $0=0$; si $p,q\in S$,
$(p+q)(2)=p(2)+q(2)=p(0)+q(0)=(p+q)(0)$; si $\lambda\in\mathbb{R}$, $(\lambda p)(2)=\lambda p(2)=\lambda p(0)=(\lambda p)(0)$.

**b)** Con $b=-2c$: $p=a+c(x^2-2x)$. Entonces $S=\operatorname{gen}\{1,\ x^2-2x\}$; los dos son
independientes (grados distintos). $B=\{1,\ x^2-2x\}$ y $\dim S=2$.

**c)** Ambos polinomios de $B'$ están en $S$: $1-2x+x^2$ tiene $b=-2$, $c=1$ y $1-4x+2x^2$ tiene $b=-4$, $c=2$
(en los dos $b=-2c$). Sus coordenadas en $B$ son $[1-2x+x^2]_B=(1,1)^t$ y $[1-4x+2x^2]_B=(1,2)^t$:

$$
C_{B'B}=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad \det=1\neq0,
$$

así que son independientes y, al ser $2=\dim S$, forman una base. Entonces

$$
C_{BB'}=C_{B'B}^{-1}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}.
$$

**Comprobación:** $\begin{pmatrix}1&1\\1&2\end{pmatrix}\begin{pmatrix}2&-1\\-1&1\end{pmatrix}=I$; además
$2\cdot b'_1-b'_2=2(1-2x+x^2)-(1-4x+2x^2)=1$, la primera columna de $C_{BB'}$.

**d)** $q=5-6x+3x^2$ cumple $b=-6=-2\cdot3$: $q\in S$ y $[q]_B=(5,3)^t$. Entonces
$[q]_{B'}=C_{BB'}[q]_B=(10-3,\ -5+3)^t=(7,-2)^t$.

**Comprobación:** $7(1-2x+x^2)-2(1-4x+2x^2)=5-6x+3x^2$.

Para extender, agregamos $x$: la matriz de coordenadas de $\{1,\ x^2-2x,\ x\}$ en $E$ es
$\begin{pmatrix}1&0&0\\0&-2&1\\0&1&0\end{pmatrix}$, con determinante $-1\neq0$. Entonces
$\{1,\ x^2-2x,\ x\}$ es base de $P_2[\mathbb{R}]$.

:::tip[Resultado]
$B=\{1,x^2-2x\}$, $\dim S=2$, $C_{BB'}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$, $[q]_{B'}=(7,-2)^t$ y
$\{1,x^2-2x,x\}$ base de $P_2[\mathbb{R}]$.
:::

</details>

### Problema 2 · Subespacios de una matriz con un parámetro
<!-- ejercicio: U1.27 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $k\in\mathbb{R}$ sea
$$
A_k=\begin{pmatrix}1&1&0&1\\0&1&1&k\\1&2&1&3\end{pmatrix}.
$$

a) **(0,5)** Hallar $\operatorname{rango}(A_k)$ según $k$.

b) **(0,5)** Para $k=2$, hallar bases de $\operatorname{fil}(A_2)$, $\operatorname{col}(A_2)$ y $\operatorname{nul}(A_2)$.

c) **(0,5)** Para $k=2$, hallar una ecuación implícita de $\operatorname{col}(A_2)$ y decidir si $(2,1,3)$ y
$(1,1,1)$ pertenecen a él.

d) **(0,5)** Para $k\neq2$, hallar $\dim\operatorname{nul}(A_k)$ y decidir si $A_kx=b$ tiene solución para todo
$b\in\mathbb{R}^3$.
:::

<details>
<summary>Resolución</summary>

**a)** Restamos: $F_3-F_1\to F_3$ da $(0,1,1,2)$ y luego $F_3-F_2\to F_3$ da $(0,0,0,2-k)$:

$$
A_k\sim\begin{pmatrix}1&1&0&1\\0&1&1&k\\0&0&0&2-k\end{pmatrix}.
$$

Si $k\neq2$ hay tres filas no nulas (pivotes en las columnas $1$, $2$ y $4$): $\operatorname{rango}=3$. Si
$k=2$ la tercera fila es nula: $\operatorname{rango}=2$.

**b)** Para $k=2$ la reducida es $\begin{pmatrix}1&0&-1&-1\\0&1&1&2\\0&0&0&0\end{pmatrix}$. Entonces
$\operatorname{fil}(A_2)$ tiene base $\{(1,0,-1,-1),(0,1,1,2)\}$ y $\operatorname{col}(A_2)$, con pivotes en las
columnas $1$ y $2$, tiene base $\{(1,0,1),(1,1,2)\}$. Con $x_3=s$, $x_4=t$ libres: $x_1=s+t$ y $x_2=-s-2t$:

$$
\operatorname{nul}(A_2)=\operatorname{gen}\{(1,-1,1,0),\ (1,-2,0,1)\}.
$$

**Comprobación:** $A_2(1,-1,1,0)^t=(0,\ -1+1,\ 1-2+1)=0$ y $A_2(1,-2,0,1)^t=(1-2+1,\ -2+2,\ 1-4+3)=0$. Rango–nulidad:
$2+2=4$.

**c)** $\operatorname{col}(A_2)=\operatorname{gen}\{(1,0,1),(1,1,2)\}$: un vector genérico es
$(a+b,\ b,\ a+2b)$ y cumple $x+y-z=(a+b)+b-(a+2b)=0$. Ecuación: $x+y-z=0$. Para $(2,1,3)$:
$2+1-3=0$, pertenece. Para $(1,1,1)$: $1+1-1=1\neq0$, no pertenece.

**d)** Si $k\neq2$, $\operatorname{rango}=3$ y $\dim\operatorname{nul}(A_k)=4-3=1$. Como $\operatorname{rango}=3=$
cantidad de filas, $\operatorname{col}(A_k)=\mathbb{R}^3$ y $A_kx=b$ tiene solución para todo $b$ (con infinitas,
una recta de soluciones).

:::tip[Resultado]
Rango $3$ si $k\neq2$ y rango $2$ si $k=2$; para $k=2$: $\operatorname{col}(A_2)=\{x+y-z=0\}$; para $k\neq2$:
$\dim\operatorname{nul}(A_k)=1$ y el sistema siempre es compatible.
:::

</details>

### Problema 3 · Un código $(5,2)$ sobre ℤ₂
<!-- ejercicio: U1.28 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C=\operatorname{nul}(H)\subseteq\mathbb{Z}_2^5$ con
$$
H=\begin{pmatrix}1&1&0&1&0\\1&0&1&0&1\\0&1&1&0&0\end{pmatrix}.
$$

a) **(0,6)** Hallar $\dim\mathcal C$, una matriz generadora $G$ y todas las palabras de $\mathcal C$.

b) **(0,4)** Calcular $d(\mathcal C)$ y decir cuántos errores detecta y cuántos corrige.

c) **(0,4)** Se recibe $r=11101$. Decodificar.

d) **(0,3)** Se recibe $r'=01010$. Calcular el síndrome y explicar qué puede afirmarse.

e) **(0,3)** De los $8$ síndromes posibles, ¿cuántos no corresponden a ningún error simple? Nombrarlos.
:::

<details>
<summary>Resolución</summary>

**a)** Las columnas $h_4=(1,0,0)^t$, $h_5=(0,1,0)^t$ y $h_3=(0,1,1)^t$ son independientes: $\operatorname{rango}(H)=3$
y $\dim\mathcal C=5-3=2$. Resolvemos $Hx^t=0$: de la tercera fila $x_3=x_2$; de la primera, $x_4=x_1+x_2$; de la segunda, $x_5=x_1+x_3=x_1+x_2$. Con $x_1,x_2$ libres:

$$
G=\left(\begin{array}{cc|ccc}1&0&0&1&1\\0&1&1&1&1\end{array}\right).
$$

Las filas son $g_1=10011$ y $g_2=01111$. Las cuatro palabras son $00000$, $10011$, $01111$ y $11100$ ($=g_1+g_2$).

**Comprobación:** $Hg_1^t=h_1+h_4+h_5=(1,1,0)+(1,0,0)+(0,1,0)=0$; $Hg_2^t=h_2+h_3+h_4+h_5=(1,0,1)+(0,1,1)+(1,0,0)+(0,1,0)=0$.

**b)** Pesos $3$, $4$ y $3$: $d(\mathcal C)=3$. Las columnas de $H$ son no nulas y distintas. Detecta
$d-1=2$ errores y corrige $1$.

**c)** $r=11101$: $Hr^t=(r_1+r_2+r_4,\ r_1+r_3+r_5,\ r_2+r_3)=(1+1+0,\ 1+1+1,\ 1+1)=(0,1,0)^t=h_5$. Se corrige el bit
$5$: $11100\in\mathcal C$ (mensaje asociado $g_1+g_2$, es decir $a=(1,1)$).

**d)** $r'=01010$: $Hr'^t=(1+1,\ 0+0,\ 1+0)=(0,0,1)^t$, que **no** es columna de $H$ ni es $0$. No hay un único error
que lo explique: hubo al menos dos errores, y se detectan pero no se corrigen. $(0,0,1)=h_2+h_4=h_3+h_5$ (dos pares
de posiciones distintos), así que ni siquiera una hipótesis de dos errores permite decidir.

**e)** Hay $2^3=8$ síndromes: $0$ (sin error detectable), cinco columnas de $H$ ($110$, $101$, $011$, $100$,
$010$) y dos más: $(1,1,1)^t$ y $(0,0,1)^t$. Esos dos solo pueden provenir de dos o más errores.

:::tip[Resultado]
$\dim\mathcal C=2$, palabras $\{00000,10011,01111,11100\}$, $d=3$; $r=11101\to11100$; $r'=01010$ tiene síndrome
$(0,0,1)^t$ (no corregible); quedan $2$ síndromes sin error simple asociado.
:::

</details>

### Problema 4 · Bases abstractas con un parámetro
<!-- ejercicio: U1.29 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $V$ un espacio vectorial real con base $B=\{v_1,v_2,v_3\}$ y sea
$B'=\{w_1,w_2,w_3\}$ con $w_1=v_1+v_2+v_3$, $w_2=v_2+v_3$, $w_3=v_3$.

a) **(0,4)** Probar que $B'$ es base de $V$ y hallar $C_{B'B}$ y $C_{BB'}$.

b) **(0,4)** Si $x=2v_1-v_2+3v_3$, hallar $[x]_{B'}$.

c) **(0,4)** Hallar $y$ tal que $[y]_{B'}=(1,2,-1)^t$ y calcular $[y]_B$.

d) **(0,4)** Para $k\in\mathbb{R}$ sea $B_k=\{v_1+kv_2,\ v_2+kv_3,\ v_3+kv_1\}$. Hallar para qué valores de $k$ es base de $V$.

e) **(0,4)** Si $V$ fuera un espacio sobre $\mathbb{Z}_2$, ¿qué valores de $k\in\mathbb{Z}_2$ dan una base en el inciso d)?
:::

<details>
<summary>Resolución</summary>

**a)** Las coordenadas en $B$ de $w_1,w_2,w_3$ son $(1,1,1)^t$, $(0,1,1)^t$ y $(0,0,1)^t$:

$$
C_{B'B}=\begin{pmatrix}1&0&0\\1&1&0\\1&1&1\end{pmatrix},\qquad\det=1\neq0,
$$

así que las coordenadas son independientes y también $w_1,w_2,w_3$; son $3=\dim V$ vectores: base. Despejando,
$v_3=w_3$, $v_2=w_2-w_3$, $v_1=w_1-w_2$:

$$
C_{BB'}=C_{B'B}^{-1}=\begin{pmatrix}1&0&0\\-1&1&0\\0&-1&1\end{pmatrix}.
$$

**Comprobación:** $\begin{pmatrix}1&0&0\\-1&1&0\\0&-1&1\end{pmatrix}\begin{pmatrix}1&0&0\\1&1&0\\1&1&1\end{pmatrix}=I$.

**b)** $[x]_B=(2,-1,3)^t$, entonces
$[x]_{B'}=C_{BB'}[x]_B=(2,\ -2-1,\ 1+3)^t=(2,-3,4)^t$. **Comprobación:**
$2w_1-3w_2+4w_3=2v_1+(2-3)v_2+(2-3+4)v_3=2v_1-v_2+3v_3$.

**c)** $y=w_1+2w_2-w_3=v_1+3v_2+2v_3$ (coeficientes de $v_2$: $1+2$; de $v_3$: $1+2-1$), luego
$[y]_B=(1,3,2)^t=C_{B'B}(1,2,-1)^t$.

**d)** Las coordenadas en $B$ de $B_k$ son $(1,k,0)^t$, $(0,1,k)^t$ y $(k,0,1)^t$:

$$
\det\begin{pmatrix}1&0&k\\k&1&0\\0&k&1\end{pmatrix}=1\cdot(1-0)-0+k\,(k\cdot k-0)=1+k^3.
$$

Es base si y solo si $1+k^3\neq0$, es decir $k\neq-1$ (la única raíz real de $k^3=-1$).

**e)** Sobre $\mathbb{Z}_2$ el mismo determinante vale $1+k^3$: para $k=0$ es $1$ (base) y para $k=1$ es
$1+1=0$ (no base, porque $(v_1+v_2)+(v_2+v_3)+(v_3+v_1)=0$).

:::tip[Resultado]
$C_{B'B}$ y $C_{BB'}$ como arriba; $[x]_{B'}=(2,-3,4)^t$; $[y]_B=(1,3,2)^t$; $B_k$ es base si y solo si $k\neq-1$
(sobre $\mathbb{R}$); sobre $\mathbb{Z}_2$, solo $k=0$.
:::

</details>

### Problema 5 · Cuatro vectores sobre ℤ₂ y sobre ℝ
<!-- ejercicio: U1.30 | nivel: avanzado | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
Sean $u_1=1100$, $u_2=0110$, $u_3=0011$, $u_4=1001$ y $W=\operatorname{gen}\{u_1,u_2,u_3,u_4\}\subseteq\mathbb{Z}_2^4$.

a) **(0,4)** Hallar el rango de $\{u_1,u_2,u_3,u_4\}$ en $\mathbb{Z}_2^4$ y en $\mathbb{R}^4$ y una relación de
dependencia en cada cuerpo.

b) **(0,6)** Probar que $W=\{v\in\mathbb{Z}_2^4:\ v_1+v_2+v_3+v_4=0\}$.

c) **(0,4)** Calcular $|W|$ y $d(W)$, y decir qué detecta y qué corrige $W$ como código.

d) **(0,6)** Decidir si es verdadero o falso, justificando: (i) $1111\in W$; (ii) $W\cup\operatorname{gen}\{1000\}$
es un subespacio de $\mathbb{Z}_2^4$; (iii) como los cuatro vectores tienen el mismo rango en $\mathbb{Z}_2^4$ y
en $\mathbb{R}^4$, los generados correspondientes tienen la misma cantidad de elementos.
:::

<details>
<summary>Resolución</summary>

**a)** Sobre $\mathbb{Z}_2$: $u_1+u_2+u_3+u_4=(1+0+0+1,\ 1+1+0+0,\ 0+1+1+0,\ 0+0+1+1)=0$. Sobre $\mathbb{R}$:
$u_1-u_2+u_3-u_4=(1-0+0-1,\ 1-1+0-0,\ 0-1+1-0,\ 0-0+1-1)=0$. En los dos casos $u_1,u_2,u_3$ son
independientes (el sistema $\alpha u_1+\beta u_2+\gamma u_3=0$ da, de la primera coordenada, $\alpha=0$; de la
segunda, $\beta=0$ y de la cuarta, $\gamma=0$), así que el rango es $3$ en $\mathbb{Z}_2^4$ y en $\mathbb{R}^4$.

**b)** Sea $\sigma(v)=v_1+v_2+v_3+v_4$, una función lineal $\mathbb{Z}_2^4\to\mathbb{Z}_2$. Su núcleo
$N=\{\sigma=0\}$ es subespacio (es $\operatorname{nul}(1\ 1\ 1\ 1)$) de dimensión $4-1=3$. *Inclusión
$W\subseteq N$:* cada $u_i$ tiene dos unos, $\sigma(u_i)=0$, y $N$ es subespacio. *Igualdad:* $\dim W=3=\dim N$
y $W\subseteq N$, luego $W=N$. $\blacksquare$

**c)** $|W|=2^3=8$. Los pesos de las palabras son pares ($v\in W$ tiene cantidad par de unos) y hay palabras
de peso $2$ (por ejemplo $u_1$): $d(W)=2$. Es el código de paridad $(4,3)$: detecta $1$ error y no corrige.

**d)** (i) **Verdadero**: $\sigma(1111)=4\equiv0$, y por b) $1111\in W$ (es $u_1+u_3$). (ii) **Falso**: $1100\in W$ y
$1000\in\operatorname{gen}\{1000\}$, pero su suma $0100$ no está en $W$ (peso $1$) ni en $\{0000,1000\}$; no es
cerrado por la suma. (iii) **Falso**: el rango es el mismo ($3$) pero sobre $\mathbb{Z}_2$ el generado tiene $2^3=8$
elementos y sobre $\mathbb{R}$ tiene infinitos. La dimensión no determina la cantidad de elementos: depende del
cuerpo.

:::tip[Resultado]
Rango $3$ en ambos cuerpos; $W=\operatorname{nul}(1\ 1\ 1\ 1)$ con $8$ elementos y $d=2$; (i) V, (ii) F, (iii) F.
:::

</details>
