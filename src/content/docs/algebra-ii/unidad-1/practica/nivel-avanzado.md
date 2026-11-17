---
title: Práctica — Nivel avanzado
description: Siete ejercicios exigentes de la Unidad 1 con bases abstractas sobre ℝ y ℤ₂, recuperación de una base desde una matriz de cambio, cadenas de tres bases, demostraciones, un código acortado de Hamming y un parámetro en el rango.
slug: algebra-ii/unidad-1/practica/nivel-avanzado
sidebar:
  order: 3
  label: Nivel avanzado
---

## Cómo usar esta página

Los ejercicios 19 a 25 piden más autonomía: elegir el método, mirar el cuerpo $K$ como una variable,
trabajar con bases abstractas y demostrar. Los enunciados son **originales** de este manual. Se recomienda
haber resuelto antes las páginas [Nivel inicial](/algebra-ii/unidad-1/practica/nivel-inicial/) e
[intermedio](/algebra-ii/unidad-1/practica/nivel-intermedio/). Escribí tu solución completa antes de abrir la
resolución: en este nivel la justificación vale tanto como el resultado.

Lecciones que se presuponen:

- [1.5 Independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/) y
  [1.6 Subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/) (ejercicios 19 y 24).
- [1.8 Coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/) (ejercicio 22).
- [1.9 Cambio de coordenadas](/algebra-ii/unidad-1/teoria/cambio-de-coordenadas/) (ejercicios 19, 20 y 21).
- [1.10 Códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/) (ejercicios 23 y 25).

Cierra la unidad la [Guía integradora](/algebra-ii/unidad-1/practica/guia-integradora/).

### Ejercicio 19 · Una base abstracta que deja de serlo en ℤ₂
<!-- ejercicio: U1.19 | nivel: avanzado | tipo: contraejemplo | verificacion: sympy -->

:::note[Enunciado]
Sea $V$ un espacio vectorial sobre $K$ con base $B=\{u,v,w\}$ y sea $B'=\{u+v,\ v+w,\ w+u\}$.

a) Si $K=\mathbb{R}$, probar que $B'$ es base de $V$, hallar $C_{B'B}$ y $C_{BB'}$, y calcular $[x]_{B'}$ para el
vector $x$ con $[x]_B=(4,2,-2)^t$.

b) Si $K=\mathbb{Z}_2$, probar que $B'$ **no** es base y calcular cuántos elementos tiene $\operatorname{gen}B'$.

c) Concluir: ¿para qué cuerpos $K$ vale que $B'$ es base?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con la base $B$ se reduce todo a matrices: las columnas de $C_{B'B}$ son las coordenadas en $B$
de los vectores de $B'$.

**a)** Los vectores de $B'$ tienen coordenadas $(1,1,0)^t$, $(0,1,1)^t$ y $(1,0,1)^t$ en $B$, entonces

$$
C_{B'B}=\begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},\qquad \det C_{B'B}=1\cdot(1-0)-0+1\cdot(1-0)=2.
$$

Como $\det=2\neq0$ en $\mathbb{R}$, las coordenadas de los vectores de $B'$ son independientes y, por la
unicidad de coordenadas, los vectores de $B'$ son independientes; son $3=\dim V$: base. La inversa es

$$
C_{BB'}=C_{B'B}^{-1}=\frac12\begin{pmatrix}1&1&-1\\-1&1&1\\1&-1&1\end{pmatrix}.
$$

**Comprobación:** la fila $(1,0,1)$ de $C_{B'B}$ por las columnas de la inversa da $\tfrac12(1+1)=1$, $\tfrac12(1-1)=0$ y $\tfrac12(-1+1)=0$, la primera fila de $I$; las otras dos filas se verifican igual. Para $x$:

$$
[x]_{B'}=C_{BB'}[x]_B=\frac12\begin{pmatrix}1&1&-1\\-1&1&1\\1&-1&1\end{pmatrix}\begin{pmatrix}4\\2\\-2\end{pmatrix}
=\frac12\begin{pmatrix}8\\-4\\0\end{pmatrix}=\begin{pmatrix}4\\-2\\0\end{pmatrix}.
$$

Con $x=4u+2v-2w$: $4(u+v)-2(v+w)=4u+2v-2w$.

**b)** En $\mathbb{Z}_2$: $(u+v)+(v+w)+(w+u)=2u+2v+2w=0$, una combinación no trivial nula. $B'$ es
dependiente: no es base (coincide con $\det=2\equiv0$). Además $u+v$ y $v+w$ son independientes (sus
coordenadas $(1,1,0)$ y $(0,1,1)$ son distintas y no nulas), de modo que $\dim\operatorname{gen}B'=2$ y hay
$2^2=4$ elementos: $0$, $u+v$, $v+w$ y $u+w$.

**c)** $B'$ es base si y solo si $2\neq0$ en $K$, es decir, si la característica de $K$ no es $2$ (como en
$\mathbb{R}$, $\mathbb{Q}$ o $\mathbb{Z}_3$). El mismo cálculo formal puede ser válido o no según el cuerpo.

:::tip[Resultado]
Sobre $\mathbb{R}$: base, con $\det C_{B'B}=2$ y $[x]_{B'}=(4,-2,0)^t$. Sobre $\mathbb{Z}_2$: dependiente,
$\operatorname{gen}B'$ tiene $4$ elementos.
:::

</details>

### Ejercicio 20 · Recuperar una base a partir de $C_{BB'}$
<!-- ejercicio: U1.20 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^2$ sea $B'=\{(1,2),(1,3)\}$ y sea $B=\{b_1,b_2\}$ una base tal que

$$
C_{BB'}=\begin{pmatrix}1&2\\1&3\end{pmatrix}.
$$

a) Hallar $b_1$ y $b_2$.

b) Hallar $C_{B'B}$.

c) Si $v=(9,23)$, hallar $[v]_B$ y $[v]_{B'}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las columnas de $C_{BB'}$ son $[b_1]_{B'}$ y $[b_2]_{B'}$: dan los coeficientes con que se
arma cada $b_j$ a partir de $B'$.

**a)** $[b_1]_{B'}=(1,1)^t$ y $[b_2]_{B'}=(2,3)^t$, así que

$$
b_1=1\cdot(1,2)+1\cdot(1,3)=(2,5),\qquad b_2=2\cdot(1,2)+3\cdot(1,3)=(5,13).
$$

$B=\{(2,5),(5,13)\}$ es base: $\det\begin{pmatrix}2&5\\5&13\end{pmatrix}=26-25=1\neq0$.

**b)** $C_{B'B}=C_{BB'}^{-1}$; como $\det C_{BB'}=3-2=1$,

$$
C_{B'B}=\begin{pmatrix}3&-2\\-1&1\end{pmatrix}.
$$

**Comprobación:** $\begin{pmatrix}1&2\\1&3\end{pmatrix}\begin{pmatrix}3&-2\\-1&1\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$.

**c)** Resolvemos $[v]_{B'}$ directamente: $\alpha+\beta=9$ y $2\alpha+3\beta=23$ dan $\beta=5$ y
$\alpha=4$: $[v]_{B'}=(4,5)^t$. Entonces $[v]_B=C_{B'B}[v]_{B'}=(12-10,\ -4+5)^t=(2,1)^t$.

**Comprobación:** $2(2,5)+1(5,13)=(9,23)$.

:::tip[Resultado]
$B=\{(2,5),(5,13)\}$, $C_{B'B}=\begin{pmatrix}3&-2\\-1&1\end{pmatrix}$, $[v]_B=(2,1)^t$, $[v]_{B'}=(4,5)^t$.
:::

</details>

### Ejercicio 21 · Una cadena de tres bases en $P_1[\mathbb{R}]$
<!-- ejercicio: U1.21 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $P_1[\mathbb{R}]$ sean $E=\{1,x\}$, $B'=\{1+x,\ 1-x\}$ y $B$ una base tal que
$C_{BB'}=\begin{pmatrix}1&2\\1&3\end{pmatrix}$.

a) Hallar $C_{B'E}$ y, con la cadena $B\to B'\to E$, calcular $C_{BE}$. Recuperar los polinomios de $B$.

b) Hallar $C_{EB}$.

c) Calcular $[q]_B$ para $q=3+x$. Explicar por qué $C_{BB'}C_{B'E}$ no es $C_{BE}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los cambios de coordenadas componen en orden inverso al de lectura:
$C_{BE}=C_{B'E}\,C_{BB'}$ (primero se pasa de $B$ a $B'$, que es el factor de la derecha).

**a)** $[1+x]_E=(1,1)^t$ y $[1-x]_E=(1,-1)^t$:

$$
C_{B'E}=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
C_{BE}=C_{B'E}C_{BB'}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&2\\1&3\end{pmatrix}=\begin{pmatrix}2&5\\0&-1\end{pmatrix}.
$$

Las columnas son las coordenadas canónicas de los vectores de $B$: $b_1=2$ y $b_2=5-x$, es decir
$B=\{2,\ 5-x\}$.

**Comprobación independiente:** $b_2=2(1+x)+3(1-x)=5-x$ y $b_1=(1+x)+(1-x)=2$.

**b)** $\det C_{BE}=-2$ y

$$
C_{EB}=C_{BE}^{-1}=\frac{1}{-2}\begin{pmatrix}-1&-5\\0&2\end{pmatrix}=\begin{pmatrix}\tfrac12&\tfrac52\\0&-1\end{pmatrix}.
$$

**c)** $[q]_E=(3,1)^t$ y $[q]_B=C_{EB}[q]_E=(\tfrac32+\tfrac52,\ -1)^t=(4,-1)^t$.

**Comprobación:** $4\cdot2-(5-x)=3+x$.

El producto en el otro orden no tiene sentido como cambio de coordenadas: sus dimensiones coinciden, pero
$C_{BB'}C_{B'E}=\begin{pmatrix}3&-1\\4&-2\end{pmatrix}\neq C_{BE}$. Cada factor espera coordenadas en la base
de partida correcta.

:::tip[Resultado]
$C_{BE}=\begin{pmatrix}2&5\\0&-1\end{pmatrix}$, $B=\{2,\ 5-x\}$, $[q]_B=(4,-1)^t$.
:::

</details>

### Ejercicio 22 · Las coordenadas conservan la independencia
<!-- ejercicio: U1.22 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $B=\{b_1,\dots,b_n\}$ una base de un espacio $V$ sobre $K$ y sean $v_1,\dots,v_k\in V$. Probar que
$\{v_1,\dots,v_k\}$ es linealmente independiente en $V$ si y solo si $\{[v_1]_B,\dots,[v_k]_B\}$ es
linealmente independiente en $K^n$. Usarlo para decidir si $1+x,\ x+x^2,\ 1+x^2$ son independientes en
$P_2[\mathbb{R}]$ y en $P_2[\mathbb{Z}_2]$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Mostrar que $v\mapsto[v]_B$ es lineal y que solo anula al vector nulo.

**Hechos previos.** (i) *Linealidad:* $[\alpha u+\beta v]_B=\alpha[u]_B+\beta[v]_B$, porque si
$u=\sum a_jb_j$ y $v=\sum c_jb_j$ entonces $\alpha u+\beta v=\sum(\alpha a_j+\beta c_j)b_j$ y por unicidad
esos son sus coeficientes. (ii) *Inyectividad en el nulo:* $[v]_B=0$ implica $v=\sum 0\,b_j=0$; y $[0]_B=0$.

**Demostración.** Para escalares $\alpha_1,\dots,\alpha_k$:

$$
\alpha_1v_1+\cdots+\alpha_kv_k=0\iff\bigl[\alpha_1v_1+\cdots+\alpha_kv_k\bigr]_B=0\iff
\alpha_1[v_1]_B+\cdots+\alpha_k[v_k]_B=0.
$$

La primera equivalencia es (ii) y la segunda es (i). Entonces las combinaciones lineales nulas de los $v_i$
y las de los $[v_i]_B$ tienen exactamente los mismos coeficientes. Una familia es independiente cuando el
único coeficiente posible es el nulo, así que ambas lo son o ambas no lo son. $\blacksquare$

**Aplicación.** En $E=\{1,x,x^2\}$ las coordenadas son $(1,1,0)^t$, $(0,1,1)^t$ y $(1,0,1)^t$, la misma terna
del ejercicio 4. Sobre $\mathbb{R}$ son independientes ($\det=2$), luego los polinomios también. Sobre
$\mathbb{Z}_2$ son dependientes ($(1,1,0)+(0,1,1)+(1,0,1)=0$), luego $(1+x)+(x+x^2)+(1+x^2)=0$ en
$P_2[\mathbb{Z}_2]$.

:::tip[Resultado]
$\{v_i\}$ es independiente si y solo si lo es $\{[v_i]_B\}$. Los tres polinomios son independientes sobre
$\mathbb{R}$ y dependientes sobre $\mathbb{Z}_2$.
:::

</details>

### Ejercicio 23 · Un código acortado de Hamming: $(6,3)$ con $d=3$
<!-- ejercicio: U1.23 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C=\operatorname{nul}(H)\subseteq\mathbb{Z}_2^6$ con

$$
H=\begin{pmatrix}1&1&0&1&1&0\\1&0&1&1&0&1\\0&1&1&1&0&0\end{pmatrix}.
$$

(Sus columnas son todos los vectores no nulos de $\mathbb{Z}_2^3$ salvo $(0,0,1)^t$.)

a) Hallar una matriz generadora $G$, la dimensión de $\mathcal C$ y todas sus palabras con sus pesos.

b) Calcular $d(\mathcal C)$ y la cantidad de errores que detecta y corrige.

c) Se recibe $r=101001$. Calcular el síndrome y corregir.

d) Se recibe $r'=001001$. Calcular el síndrome y explicar por qué no se puede corregir.
:::

<details>
<summary>Resolución</summary>

**a)** Como $H$ tiene rango $3$ (contiene columnas independientes como $h_5,h_6,h_3$), $\dim\mathcal C=6-3=3$
y hay $8$ palabras. Resolviendo $Hx^t=0$ con $x_1,x_2,x_3$ libres:
$x_4=x_2+x_3$, $x_5=x_1+x_4+x_2=x_1+x_3$, $x_6=x_1+x_3+x_4=x_1+x_2$. Con los valores canónicos de
las libres:

$$
G=\left(\begin{array}{ccc|ccc}1&0&0&0&1&1\\0&1&0&1&0&1\\0&0&1&1&1&0\end{array}\right).
$$

Las ocho palabras y sus pesos: $000000$ (0); $100011$, $010101$, $001110$ (3 cada una); $110110$, $101101$,
$011011$ (4 cada una); $111000$ (3).

**Comprobación:** $Hg_1^t=h_1+h_5+h_6=(1,1,0)+(1,0,0)+(0,1,0)=0$; $Hg_2^t=h_2+h_4+h_6=(1,0,1)+(1,1,1)+(0,1,0)=0$; $Hg_3^t=h_3+h_4+h_5=(0,1,1)+(1,1,1)+(1,0,0)=0$.

**b)** El peso mínimo no nulo es $3$: $d(\mathcal C)=3$. Las columnas de $H$ son no nulas y distintas
(así que $d\geq3$) y $h_1+h_2+h_3=(1,1,0)+(1,0,1)+(0,1,1)=0$ da una palabra de peso $3$ ($111000$). Detecta
$d-1=2$ errores y corrige $\lfloor(d-1)/2\rfloor=1$.

**c)** $s=Hr^t$ con $r=(1,0,1,0,0,1)$: primera fila $1+0+0+0=1$; segunda $1+1+0+1=1$; tercera $0+1+0+0=1$:
$s=(1,1,1)^t=h_4$. Se corrige la posición $4$: $r+e_4=101101$, que es palabra código.

**d)** Con $r'=(0,0,1,0,0,1)$: primera fila $r'_1+r'_2+r'_4+r'_5=0$; segunda $r'_1+r'_3+r'_4+r'_6=0+1+0+1=0$; tercera $r'_2+r'_3+r'_4=1$. Entonces $s=(0,0,1)^t$, que **no es columna de $H$**: ningún error simple lo explica, de modo que se detectan al menos dos errores. Pero $(0,0,1)=h_1+h_4=h_2+h_5=h_3+h_6$: tres pares de errores
distintos producen el mismo síndrome, y el decodificador no puede elegir. Se detecta, no se corrige.

:::tip[Resultado]
$\dim\mathcal C=3$, $8$ palabras, $d=3$: corrige $1$ error y detecta $2$. $r=101001$ se corrige a $101101$;
$r'=001001$ tiene síndrome $(0,0,1)^t$ y solo se puede declarar errónea.
:::

</details>

### Ejercicio 24 · Rango y subespacios de una matriz con parámetro
<!-- ejercicio: U1.24 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $k\in\mathbb{R}$ sea
$$
A_k=\begin{pmatrix}1&1&k\\1&k&1\\k&1&1\end{pmatrix}.
$$

a) Calcular $\det A_k$ y hallar $\operatorname{rango}(A_k)$ según $k$.

b) Para $k=1$ y $k=-2$ hallar una base de $\operatorname{nul}(A_k)$.

c) ¿Para qué $k$ vale $\operatorname{col}(A_k)=\mathbb{R}^3$?

d) Para $k=-2$, decidir si $b=(1,1,1)$ y $b'=(1,-2,1)$ pertenecen a $\operatorname{col}(A_{-2})$.
:::

<details>
<summary>Resolución</summary>

**a)** Sumando las columnas $2$ y $3$ a la primera (no cambia el determinante), la primera columna es
$(k+2)(1,1,1)^t$; sacamos el factor y restamos la primera fila a las demás:

$$
\det A_k=(k+2)\det\begin{pmatrix}1&1&k\\1&k&1\\1&1&1\end{pmatrix}
=(k+2)\det\begin{pmatrix}1&1&k\\0&k-1&1-k\\0&0&1-k\end{pmatrix}=(k+2)(k-1)(1-k)=-(k+2)(k-1)^2.
$$

Si $k\neq1$ y $k\neq-2$, $\det\neq0$ y $\operatorname{rango}=3$. Si $k=1$, $A_1$ tiene todas las entradas $1$:
rango $1$. Si $k=-2$, $\det=0$ y las dos primeras filas $(1,1,-2)$ y $(1,-2,1)$ no son proporcionales:
rango $2$.

**b)** $k=1$: $Ax=0$ equivale a $x_1+x_2+x_3=0$, con base $\{(-1,1,0),(-1,0,1)\}$ ($\dim=2=3-1$). $k=-2$: las
filas suman $0$ y el escalonamiento da $x_1=x_2=x_3$; base $\{(1,1,1)\}$ ($\dim=1=3-2$).

**Comprobación:** $A_{-2}(1,1,1)^t=(1+1-2,\ 1-2+1,\ -2+1+1)=0$.

**c)** $\operatorname{col}(A_k)=\mathbb{R}^3$ si y solo si $\operatorname{rango}=3$, o sea $k\neq1$ y $k\neq-2$.

**d)** En $A_{-2}$ la suma de cada columna es $0$, así que $\operatorname{col}(A_{-2})\subseteq\{y_1+y_2+y_3=0\}$,
y por tener dimensión $2$ es **igual** a ese plano. $b=(1,1,1)$ suma $3\neq0$: no pertenece. $b'=(1,-2,1)$ suma
$0$: pertenece (es justamente la segunda columna).

:::tip[Resultado]
$\det A_k=-(k+2)(k-1)^2$; rango $3$ si $k\neq1,-2$, rango $2$ si $k=-2$, rango $1$ si $k=1$;
$\operatorname{col}(A_k)=\mathbb{R}^3$ si y solo si $k\neq1,-2$; $b\notin\operatorname{col}(A_{-2})$ y
$b'\in\operatorname{col}(A_{-2})$.
:::

</details>

### Ejercicio 25 · Distancia mínima y columnas de $H$
<!-- ejercicio: U1.25 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $\mathcal C=\operatorname{nul}(H)\subseteq\mathbb{Z}_2^n$ un código lineal, con $H$ de columnas $h_1,\dots,h_n$.

a) Probar que $d_H(u,v)=w(u+v)$ y que $d(\mathcal C)$ es el mínimo peso de una palabra no nula de $\mathcal C$.

b) Probar que $d(\mathcal C)=1$ si y solo si alguna columna de $H$ es nula.

c) Probar que $d(\mathcal C)\geq3$ si y solo si las columnas de $H$ son no nulas y distintas dos a dos.
:::

<details>
<summary>Resolución</summary>

**a)** En $\mathbb{Z}_2$, $u_i+v_i=1$ exactamente cuando $u_i\neq v_i$. Entonces la cantidad de posiciones donde
difieren es el peso de $u+v$: $d_H(u,v)=w(u+v)$. Si $u,v\in\mathcal C$ son distintas, $u+v$ es una palabra no nula
de $\mathcal C$ (subespacio), y toda palabra no nula $c$ cumple $c=c+0$ con $0\in\mathcal C$, de modo que
$w(c)=d_H(c,0)$. Por lo tanto el conjunto de distancias entre palabras distintas es igual al de pesos no
nulos y $d(\mathcal C)=\min\{w(c):\ c\in\mathcal C,\ c\neq0\}$.

**b)** Una palabra de peso $1$ es $e_j$, y $e_j\in\mathcal C\iff He_j^t=0\iff h_j=0$. Como $d$ es el mínimo peso
no nulo y el peso mínimo posible es $1$, $d=1$ si y solo si existe una palabra de peso $1$ en $\mathcal C$, o
sea una columna nula.

**c)** $d\geq3$ equivale a que no haya palabras de peso $1$ ni de peso $2$ en $\mathcal C$ (por a). Ninguna de
peso $1$ equivale a que ninguna columna sea nula (por b). Una palabra de peso $2$ es $e_i+e_j$ con $i\neq j$ y

$$
e_i+e_j\in\mathcal C\iff h_i+h_j=0\iff h_i=h_j,
$$

(en $\mathbb{Z}_2$, $-h_j=h_j$). Luego ninguna de peso $2$ equivale a que las columnas sean distintas dos a
dos. $\blacksquare$

**Verificación en un caso.** En $H$ del ejercicio 23 las columnas son no nulas y distintas, y $d=3$; en el
ejercicio 8, $H=(1\ 1\ 1\ 1\ 1)$ tiene columnas iguales y $d=2$.

:::tip[Resultado]
$d(\mathcal C)$ es el peso mínimo no nulo; $d=1$ si y solo si hay una columna nula; $d\geq3$ si y solo si las
columnas de $H$ son no nulas y distintas.
:::

</details>
