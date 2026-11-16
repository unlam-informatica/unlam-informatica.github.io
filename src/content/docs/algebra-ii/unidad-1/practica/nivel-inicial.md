---
title: Práctica — Nivel inicial
description: Ocho ejercicios de la Unidad 1 sobre cuerpos, subespacios, generadores, independencia, subespacios de una matriz, coordenadas y un primer código de paridad, con resolución completa.
slug: algebra-ii/unidad-1/practica/nivel-inicial
sidebar:
  order: 1
  label: Nivel inicial
---

## Cómo usar esta página

Los ejercicios 1 a 8 fijan las herramientas básicas de la Unidad 1: aritmética en $\mathbb{Z}_2$ y $\mathbb{Z}_p$,
el criterio de subespacio, combinaciones lineales, independencia, los subespacios de una matriz,
coordenadas y un código de paridad. Todos los enunciados son **originales** de este manual.

Cada ejercicio trae el enunciado a la vista y la resolución plegada. Conviene intentarlo antes de abrirla
y, después, comparar el **método** (no solo el resultado). Las resoluciones terminan con una
comprobación independiente; hacerla por cuenta propia es parte del ejercicio.

Lecciones que se presuponen:

- [1.1 Cuerpos y ℤ₂](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/) (ejercicio 1).
- [1.3 Subespacios](/algebra-ii/unidad-1/teoria/subespacios/) (ejercicios 2 y 5).
- [1.4 Combinaciones lineales y generadores](/algebra-ii/unidad-1/teoria/combinaciones-lineales/) (ejercicio 3).
- [1.5 Independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/) (ejercicio 4).
- [1.6 Subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/) (ejercicio 6).
- [1.8 Coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/) (ejercicio 7).
- [1.10 Códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/) (ejercicio 8).

Siguen [Nivel intermedio](/algebra-ii/unidad-1/practica/nivel-intermedio/),
[Nivel avanzado](/algebra-ii/unidad-1/practica/nivel-avanzado/) y la
[Guía integradora](/algebra-ii/unidad-1/practica/guia-integradora/).

### Ejercicio 1 · Aritmética en ℤ₂, ℤ₅ y por qué ℤ₄ no es cuerpo
<!-- ejercicio: U1.01 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) Escribir las tablas de la suma y del producto de $\mathbb{Z}_2=\{0,1\}$ y calcular $1+1+1$ y
$1\cdot 1+1$.

b) Resolver en $\mathbb{Z}_5$ la ecuación $3x=4$.

c) Escribir la tabla del producto de $\mathbb{Z}_4$ y explicar qué axioma de cuerpo falla.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Operar módulo $n$ (resto de la división por $n$) y, para dividir, buscar el inverso
multiplicativo.

**a)** Las tablas de $\mathbb{Z}_2$ salen de $1+1=2\equiv 0 \pmod 2$:

| + | 0 | 1 |
|---|---|---|
| **0** | 0 | 1 |
| **1** | 1 | 0 |

| · | 0 | 1 |
|---|---|---|
| **0** | 0 | 0 |
| **1** | 0 | 1 |

Luego $1+1+1=(1+1)+1=0+1=1$ y $1\cdot 1+1=1+1=0$. En general, en $\mathbb{Z}_2$ la suma es el
o exclusivo y el producto es la conjunción.

**b)** En $\mathbb{Z}_5$, $3\cdot 2=6\equiv 1$, así que $3^{-1}=2$. Multiplicamos la ecuación por $2$:

$$
x=2\cdot 3x=2\cdot 4=8\equiv 3 \pmod 5.
$$

**Comprobación:** $3\cdot 3=9\equiv 4$.

**c)** Tabla del producto de $\mathbb{Z}_4=\{0,1,2,3\}$:

| · | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **0** | 0 | 0 | 0 | 0 |
| **1** | 0 | 1 | 2 | 3 |
| **2** | 0 | 2 | 0 | 2 |
| **3** | 0 | 3 | 2 | 1 |

La fila del $2$ no contiene al $1$: $2$ no tiene inverso multiplicativo, y falla el axioma «todo
elemento no nulo tiene inverso». Además $2\cdot 2=0$ con $2\neq 0$: en un cuerpo el producto de no
nulos nunca es cero. Por eso $\mathbb{Z}_4$ no es cuerpo (sí lo es $\mathbb{Z}_p$ con $p$ primo).

:::tip[Resultado]
$1+1+1=1$ y $1\cdot1+1=0$ en $\mathbb{Z}_2$; $x=3$ en $\mathbb{Z}_5$; $\mathbb{Z}_4$ no es cuerpo porque
$2\cdot2=0$ y $2$ no tiene inverso.
:::

</details>

### Ejercicio 2 · ¿Cuáles son subespacios de ℝ³?
<!-- ejercicio: U1.02 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Decidir si cada conjunto es un subespacio de $\mathbb{R}^3$. Si lo es, probarlo con el criterio de las tres
condiciones y dar una base; si no, indicar qué falla.

a) $S=\{(x,y,z):\ x+2y-z=0\}$.

b) $T=\{(x,y,z):\ x+y+z=1\}$.

c) $U=\{(x,y,z):\ xy=0\}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para cada conjunto se prueba primero que el vector nulo pertenece (si no, no es
subespacio) y después la cerradura bajo suma y producto por escalares, o se busca un contraejemplo.

**a)** Se cumplen las tres condiciones:

- $(0,0,0)$ verifica $0+0-0=0$, luego $0\in S$.
- Si $(x,y,z),(x',y',z')\in S$, la suma cumple $(x+x')+2(y+y')-(z+z')=(x+2y-z)+(x'+2y'-z')=0+0=0$.
- Si $(x,y,z)\in S$ y $\lambda\in\mathbb{R}$: $\lambda x+2\lambda y-\lambda z=\lambda\cdot 0=0$.

Es subespacio. Despejando $z=x+2y$ resulta $(x,y,z)=x(1,0,1)+y(0,1,2)$, con $(1,0,1)$ y $(0,1,2)$
linealmente independientes (no son proporcionales). Base $\{(1,0,1),(0,1,2)\}$; $S$ es un plano por el
origen.

**b)** $(0,0,0)$ da $0\neq1$: $0\notin T$. No es subespacio (es un plano que no pasa por el origen).

**c)** $0\in U$ y $U$ es cerrado por múltiplos, pero **no por sumas**: $(1,0,0)$ y $(0,1,0)$ están en $U$
y su suma $(1,1,0)$ cumple $1\cdot1=1\neq0$, o sea $(1,1,0)\notin U$. No es subespacio (es unión de dos
planos).

**Comprobación de a).** $(1,0,1)$: $1+0-1=0$; $(0,1,2)$: $0+2-2=0$.

:::tip[Resultado]
Solo $S$ es subespacio, con base $\{(1,0,1),(0,1,2)\}$. $T$ no contiene al origen y $U$ no es cerrado por
la suma.
:::

</details>

### Ejercicio 3 · Pertenencia al generado y ecuación del plano
<!-- ejercicio: U1.03 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $v_1=(1,0,1)$, $v_2=(2,1,3)$ y $S=\operatorname{gen}\{v_1,v_2\}\subseteq\mathbb{R}^3$.

a) Decidir si $w=(4,1,5)$ pertenece a $S$ y, en caso afirmativo, escribirlo como combinación lineal.

b) Decidir si $w'=(1,1,1)$ pertenece a $S$.

c) Hallar una ecuación implícita de $S$.

d) Hallar $k$ tal que $(3,k,6)\in S$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $w\in S$ si y solo si el sistema $a v_1+b v_2=w$ tiene solución. Una ecuación implícita
se obtiene eliminando $a$ y $b$ del vector genérico.

**a)** $a(1,0,1)+b(2,1,3)=(a+2b,\ b,\ a+3b)=(4,1,5)$. De la segunda componente $b=1$; de la primera,
$a=2$; la tercera da $a+3b=5$, que coincide. Luego $w=2v_1+v_2$.

**Comprobación:** $2(1,0,1)+(2,1,3)=(4,1,5)$.

**b)** $b=1$ y $a+2b=1$ dan $a=-1$, pero entonces $a+3b=2\neq1$. El sistema es incompatible: $w'\notin S$.

**c)** Un vector genérico de $S$ es $(x,y,z)=(a+2b,\ b,\ a+3b)$. Entonces $y=b$ y $z-x=b$, de donde
$z-x=y$:

$$
S=\{(x,y,z):\ x+y-z=0\}.
$$

Verificamos con los generadores: $1+0-1=0$ y $2+1-3=0$. Con $w$: $4+1-5=0$; con $w'$:
$1+1-1=1\neq0$, consistente con a) y b).

**d)** $(3,k,6)\in S$ si $3+k-6=0$, es decir $k=3$. **Comprobación:** $(3,3,6)=-3v_1+3v_2=(-3+6,\ 3,\ -3+9)$.

:::tip[Resultado]
$w=2v_1+v_2\in S$; $w'\notin S$; $S:\ x+y-z=0$; $k=3$.
:::

</details>

### Ejercicio 4 · La misma terna, independiente en ℝ³ y dependiente en ℤ₂³
<!-- ejercicio: U1.04 | nivel: inicial | tipo: conceptual | verificacion: sympy -->

:::note[Enunciado]
Sean $u_1=(1,1,0)$, $u_2=(0,1,1)$, $u_3=(1,0,1)$.

a) Decidir si $\{u_1,u_2,u_3\}$ es linealmente independiente en $\mathbb{R}^3$.

b) Decidir lo mismo en $\mathbb{Z}_2^3$, y si es dependiente, dar una combinación no trivial igual a $0$.

c) ¿Cuántos elementos tiene $\operatorname{gen}\{u_1,u_2,u_3\}$ en $\mathbb{Z}_2^3$?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Plantear $\alpha u_1+\beta u_2+\gamma u_3=0$ y resolver en cada cuerpo.

La ecuación equivale al sistema
$$
\begin{cases}\alpha+\gamma=0\\ \alpha+\beta=0\\ \beta+\gamma=0.\end{cases}
$$

**a)** En $\mathbb{R}$: $\gamma=-\alpha$ y $\beta=-\alpha$; la tercera ecuación da $-2\alpha=0$, o sea
$\alpha=0$ y entonces $\beta=\gamma=0$. Solo la solución trivial: **independientes**. Equivalentemente
$\det(u_1\mid u_2\mid u_3)=2\neq0$.

**b)** En $\mathbb{Z}_2$, $-1=1$: $\gamma=\alpha$, $\beta=\alpha$ y la tercera ecuación es
$\beta+\gamma=2\alpha=0$, que se cumple siempre. Hay una variable libre, así que existen soluciones no
triviales: **dependientes**. Con $\alpha=1$:

$$
u_1+u_2+u_3=(1+0+1,\ 1+1+0,\ 0+1+1)=(0,0,0).
$$

(El determinante vale $2\equiv 0$ en $\mathbb{Z}_2$.)

**c)** Como $u_3=u_1+u_2$ y $u_1,u_2$ no son proporcionales, $\{u_1,u_2\}$ es base del generado, de
dimensión $2$. Hay $2^2=4$ elementos: $000$, $110$, $011$, $101$.

:::tip[Resultado]
LI en $\mathbb{R}^3$, LD en $\mathbb{Z}_2^3$ (porque $u_1+u_2+u_3=0$); el generado en $\mathbb{Z}_2^3$ tiene
$4$ elementos.
:::

</details>

### Ejercicio 5 · Cuatro afirmaciones: verdadero o falso
<!-- ejercicio: U1.05 | nivel: inicial | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
Decidir si cada afirmación es verdadera o falsa y justificar (con una demostración o un contraejemplo).

a) $\{(x,y)\in\mathbb{R}^2:\ xy=0\}$ es un subespacio de $\mathbb{R}^2$.

b) Todo conjunto de vectores que contiene al vector nulo es linealmente dependiente.

c) $\mathbb{Z}_2^3$ tiene exactamente $7$ subespacios de dimensión $1$.

d) Un subespacio de $\mathbb{Z}_2^5$ de dimensión $3$ tiene $6$ elementos.
:::

<details>
<summary>Resolución</summary>

**a) Falsa.** Contraejemplo: $(1,0)$ y $(0,1)$ pertenecen al conjunto (producto de coordenadas nulo) pero
$(1,0)+(0,1)=(1,1)$ no, porque $1\cdot1\neq0$.

**b) Verdadera.** Si $v_1=0$ pertenece al conjunto $\{v_1,\dots,v_k\}$, entonces
$1\cdot v_1+0\cdot v_2+\cdots+0\cdot v_k=0$ es una combinación lineal nula con un coeficiente no nulo.

**c) Verdadera.** Un subespacio de dimensión $1$ es $\{0,v\}$ con $v\neq0$ (los múltiplos de $v$ son
$0\cdot v=0$ y $1\cdot v=v$). Cada vector no nulo da un subespacio distinto y hay $2^3-1=7$ vectores no
nulos.

**d) Falsa.** Una base de $3$ vectores da $2^3=8$ combinaciones distintas (cada coeficiente es $0$ o $1$ y
las coordenadas son únicas). Tiene $8$ elementos, no $6$.

**Comprobación de c).** Enumerando los siete vectores no nulos de $\mathbb{Z}_2^3$, cada $\{0,v\}$ es
cerrado por la suma ($v+v=0$) y no hay otros subespacios de ese tamaño.

:::tip[Resultado]
a) F, b) V, c) V, d) F (tiene $8$ elementos).
:::

</details>

### Ejercicio 6 · Subespacios de una matriz y rango–nulidad
<!-- ejercicio: U1.06 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea
$$
A=\begin{pmatrix}1&2&0&1\\2&4&1&5\\1&2&1&4\end{pmatrix}.
$$

a) Hallar bases de $\operatorname{fil}(A)$, $\operatorname{col}(A)$ y $\operatorname{nul}(A)$.

b) Verificar el teorema de rango–nulidad.

c) Decidir si $b=(1,3,2)$ pertenece a $\operatorname{col}(A)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escalonar $A$: las filas no nulas de la forma escalonada dan una base de
$\operatorname{fil}(A)$; las columnas de $A$ en las posiciones pivote, una base de $\operatorname{col}(A)$;
las soluciones de $Ax=0$, el núcleo.

$$
A\ \xrightarrow{\ F_2-2F_1,\ F_3-F_1\ }\ 
\begin{pmatrix}1&2&0&1\\0&0&1&3\\0&0&1&3\end{pmatrix}
\ \xrightarrow{\ F_3-F_2\ }\ 
\begin{pmatrix}1&2&0&1\\0&0&1&3\\0&0&0&0\end{pmatrix}.
$$

Los pivotes están en las columnas $1$ y $3$; $\operatorname{rango}(A)=2$.

**a)** $\operatorname{fil}(A)$: $\{(1,2,0,1),(0,0,1,3)\}$. $\operatorname{col}(A)$: columnas $1$ y $3$ de $A$
(no de la escalonada): $\{(1,2,1),(0,1,1)\}$.

Para $\operatorname{nul}(A)$ las variables libres son $x_2=s$ y $x_4=t$. De la segunda fila,
$x_3=-3t$; de la primera, $x_1=-2s-t$:

$$
x=s(-2,1,0,0)+t(-1,0,-3,1).
$$

Base de $\operatorname{nul}(A)$: $\{(-2,1,0,0),(-1,0,-3,1)\}$.

**Comprobación:** $A(-2,1,0,0)^t=(-2+2,\ -4+4,\ -2+2)=0$ y
$A(-1,0,-3,1)^t=(-1+1,\ -2-3+5,\ -1-3+4)=0$.

**b)** $\operatorname{rango}(A)+\dim\operatorname{nul}(A)=2+2=4=$ cantidad de columnas.

**c)** $b=(1,3,2)=1\cdot(1,2,1)+1\cdot(0,1,1)$, así que $b\in\operatorname{col}(A)$.

:::tip[Resultado]
$\dim\operatorname{fil}(A)=\dim\operatorname{col}(A)=2$, $\dim\operatorname{nul}(A)=2$; $b\in\operatorname{col}(A)$.
:::

</details>

### Ejercicio 7 · Coordenadas, orden de la base y tamaño de $[v]_B$
<!-- ejercicio: U1.07 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) En $\mathbb{R}^2$ sean $B=\{(2,1),(1,1)\}$ y $B'=\{(1,1),(2,1)\}$ (los mismos vectores en otro orden).
Calcular $[v]_B$ y $[v]_{B'}$ para $v=(5,3)$.

b) En $P_2[\mathbb{R}]$ calcular $[p]_E$ y $[p]_{B''}$ para $p=3-x+2x^2$, con $E=\{1,x,x^2\}$ y
$B''=\{x^2,x,1\}$.

c) Para $M=\begin{pmatrix}1&2\\0&3\end{pmatrix}$ y la base canónica ordenada $\{E_{11},E_{12},E_{21},E_{22}\}$
de $\mathbb{R}^{2\times2}$, ¿cuántas componentes tiene $[M]$ y cuáles son?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las coordenadas son los coeficientes de la **única** combinación lineal de la base que da
el vector; si se cambia el orden de la base, se permutan las coordenadas.

**a)** $a(2,1)+b(1,1)=(5,3)$ da $2a+b=5$ y $a+b=3$; restando, $a=2$ y $b=1$. Entonces
$[v]_B=(2,1)^t$. Para $B'$ los coeficientes se asocian a $(1,1)$ y a $(2,1)$, en ese orden:
$v=1\cdot(1,1)+2\cdot(2,1)$, es decir $[v]_{B'}=(1,2)^t$.

**Comprobación:** $2(2,1)+1(1,1)=(5,3)$ y $1(1,1)+2(2,1)=(5,3)$.

**b)** $p=3\cdot1+(-1)x+2x^2$: $[p]_E=(3,-1,2)^t$. En $B''=\{x^2,x,1\}$ el primer coeficiente es el de
$x^2$: $[p]_{B''}=(2,-1,3)^t$.

**c)** $[M]$ tiene $\dim\mathbb{R}^{2\times2}=4$ componentes (no $2\times2$): como
$M=1E_{11}+2E_{12}+0E_{21}+3E_{22}$, $[M]=(1,2,0,3)^t$.

:::tip[Resultado]
$[v]_B=(2,1)^t$, $[v]_{B'}=(1,2)^t$; $[p]_E=(3,-1,2)^t$, $[p]_{B''}=(2,-1,3)^t$; $[M]=(1,2,0,3)^t$ (cuatro
componentes). La longitud de $[v]_B$ es siempre $\dim V$.
:::

</details>

### Ejercicio 8 · Un código de paridad $(5,4)$
<!-- ejercicio: U1.08 | nivel: inicial | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Un emisor agrega a cada bloque de $4$ bits un quinto bit para que la cantidad de unos del bloque de $5$
bits sea par. Sea $\mathcal C\subseteq\mathbb{Z}_2^5$ el conjunto de las palabras resultantes.

a) Probar que $\mathcal C=\operatorname{nul}(H)$ con $H=(1\ 1\ 1\ 1\ 1)$ y calcular $\dim\mathcal C$ y
$|\mathcal C|$.

b) Hallar una matriz generadora $G$ y codificar el mensaje $1011$.

c) Calcular la distancia mínima de $\mathcal C$. ¿Cuántos errores detecta y cuántos corrige?

d) Se reciben $10101$ y $01111$. Decidir en cada caso si se detecta un error.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** «Cantidad par de unos» es la condición $v_1+\cdots+v_5=0$ en $\mathbb{Z}_2$, es decir
$Hv^t=0$.

**a)** $Hv^t=v_1+v_2+v_3+v_4+v_5$, que vale $0$ exactamente cuando hay una cantidad par de unos. Luego
$\mathcal C=\operatorname{nul}(H)$. Como $\operatorname{rango}(H)=1$, $\dim\mathcal C=5-1=4$ y
$|\mathcal C|=2^4=16$ (uno por cada mensaje de $4$ bits).

**b)** Con $x_1,\dots,x_4$ libres, $x_5=x_1+x_2+x_3+x_4$. Las filas de

$$
G=\left(\begin{array}{cccc|c}1&0&0&0&1\\0&1&0&0&1\\0&0&1&0&1\\0&0&0&1&1\end{array}\right)
$$

están en $\mathcal C$ (peso $2$) y son $4$ vectores independientes: base. Para $a=(1,0,1,1)$:
$u=aG=g_1+g_3+g_4=(1,0,1,1,\ 1+1+1)=(1,0,1,1,1)$. **Comprobación:** $Hu^t=1+0+1+1+1=0$.

**c)** Una palabra de peso $1$ tiene síndrome $1\neq0$, luego no está en $\mathcal C$; hay palabras de peso $2$
(las filas de $G$). Entonces $d(\mathcal C)=2$. Detecta $d-1=1$ error y corrige $\lfloor(d-1)/2\rfloor=0$.

**d)** $10101$ tiene tres unos: síndrome $1$, **se detecta** un error (no se sabe en qué posición).
$01111$ tiene cuatro unos: síndrome $0$, **no** se detecta nada (podría ser una palabra válida o tener
dos errores).

:::tip[Resultado]
$\dim\mathcal C=4$, $|\mathcal C|=16$, $1011\mapsto10111$, $d=2$: detecta un error, no corrige ninguno.
:::

</details>
