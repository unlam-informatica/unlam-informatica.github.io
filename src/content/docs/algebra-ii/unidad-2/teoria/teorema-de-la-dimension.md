---
title: Teorema de la dimensión
description: La relación dim V = dim Nu(T) + dim Im(T), su demostración completa, su vínculo con rango y nulidad de matrices y cómo usarla para decidir sin hacer cuentas.
slug: algebra-ii/unidad-2/teoria/teorema-de-la-dimension
sidebar:
  order: 3
  label: 2.3 Teorema de la dimensión
---

## Para qué sirve

En los ejemplos de [2.2](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/) apareció siempre la misma cuenta: la dimensión del núcleo más la de la imagen daba la dimensión del espacio de salida. No es casualidad. La intuición es una "conservación de dimensiones": cada dimensión de $V$ o bien la aplasta $T$ (va al núcleo) o bien sobrevive en la imagen. Ninguna se crea y ninguna se pierde sin quedar registrada en el núcleo.

El teorema tiene un uso práctico enorme: conociendo una de las dos dimensiones se obtiene la otra **sin calcular**, y muchas preguntas de existencia ("¿hay una TL tal que...?") se responden con una suma.

## Enunciado

:::note[Teorema de la dimensión]
Sea $V$ un espacio vectorial de dimensión finita y $T:V\to W$ una TL. Entonces

$$
\dim V=\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T).
$$
:::

Observaciones sobre las hipótesis:

- Se pide que $V$ tenga dimensión finita. De $W$ no se pide nada: la demostración prueba que $\operatorname{Im}(T)$ tiene dimensión finita de todos modos. (En este curso todos los espacios son de dimensión finita.)
- Al número $\dim\operatorname{Nu}(T)$ algunos libros lo llaman **nulidad** de $T$, y a $\dim\operatorname{Im}(T)$, **rango** de $T$. Nosotros reservamos "rango" para matrices; en la lección [2.6](/algebra-ii/unidad-2/teoria/matriz-asociada/) veremos que $\dim\operatorname{Im}(T)$ es el rango de cualquier matriz asociada a $T$.

## Demostración

Sea $n=\dim V$ y $k=\dim\operatorname{Nu}(T)$. Como $\operatorname{Nu}(T)$ es un subespacio de $V$, $0\le k\le n$. Probaremos que $\dim\operatorname{Im}(T)=n-k$.

**Paso 1: una base de $V$ que empieza por una base del núcleo.** Sea $\{u_1,\dots,u_k\}$ una base de $\operatorname{Nu}(T)$ (vacía si $k=0$). Es un conjunto LI de $V$, así que, por el teorema de [extensión de un conjunto LI a una base](/algebra-ii/unidad-1/teoria/base-y-dimension/), existen $v_{k+1},\dots,v_n\in V$ tales que

$$
B=\{u_1,\dots,u_k,\ v_{k+1},\dots,v_n\}
$$

es una base de $V$. Afirmamos que $\{T(v_{k+1}),\dots,T(v_n)\}$ es una base de $\operatorname{Im}(T)$; como tiene $n-k$ vectores, eso termina la prueba.

**Paso 2: generan la imagen.** Sea $w\in\operatorname{Im}(T)$. Por definición existe $v\in V$ con $T(v)=w$. Escribimos $v$ en la base $B$:

$$
v=a_1u_1+\cdots+a_ku_k+b_{k+1}v_{k+1}+\cdots+b_nv_n.
$$

Aplicando $T$ y usando que $T(u_i)=0_W$ (porque $u_i\in\operatorname{Nu}(T)$):

$$
w=T(v)=\underbrace{a_1T(u_1)+\cdots+a_kT(u_k)}_{=\,0_W}+b_{k+1}T(v_{k+1})+\cdots+b_nT(v_n).
$$

Luego $w\in\operatorname{gen}\{T(v_{k+1}),\dots,T(v_n)\}$.

**Paso 3: son LI.** Supongamos $c_{k+1}T(v_{k+1})+\cdots+c_nT(v_n)=0_W$. Por linealidad, $T(c_{k+1}v_{k+1}+\cdots+c_nv_n)=0_W$, es decir, el vector $c_{k+1}v_{k+1}+\cdots+c_nv_n$ está en el núcleo. Entonces se escribe en la base del núcleo:

$$
c_{k+1}v_{k+1}+\cdots+c_nv_n=d_1u_1+\cdots+d_ku_k
\quad\Longrightarrow\quad
-d_1u_1-\cdots-d_ku_k+c_{k+1}v_{k+1}+\cdots+c_nv_n=0_V.
$$

Es una combinación lineal nula de los vectores de la base $B$, que son LI; luego todos los coeficientes son cero, en particular $c_{k+1}=\cdots=c_n=0$.

**Conclusión.** $\dim\operatorname{Im}(T)=n-k$, y entonces $\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)=k+(n-k)=n=\dim V$. $\blacksquare$

**Casos extremos.** El argumento los cubre, pero conviene leerlos por separado:

- $k=0$ ($\operatorname{Nu}(T)=\{0_V\}$): la base del núcleo es vacía, $B$ es cualquier base $\{v_1,\dots,v_n\}$ de $V$ y la prueba muestra que $\{T(v_1),\dots,T(v_n)\}$ es base de la imagen: $\dim\operatorname{Im}(T)=n$. El paso 3 se reduce a "si $T(\sum c_iv_i)=0_W$, entonces $\sum c_iv_i\in\{0_V\}$, luego todos los $c_i$ son cero".
- $k=n$: el núcleo es un subespacio de $V$ con la misma dimensión, así que $\operatorname{Nu}(T)=V$ y $T$ es la TL nula. No hay vectores $v_j$ que agregar, la imagen es $\{0_W\}$, generada por el conjunto vacío, y tiene dimensión $0=n-n$.

## Relación con rango y nulidad de una matriz

Si $A\in K^{m\times n}$ y $T_A:K^n\to K^m$, $T_A(x)=Ax$, vimos que $\operatorname{Nu}(T_A)=\operatorname{nul}(A)$ e $\operatorname{Im}(T_A)=\operatorname{col}(A)$, y que $\dim\operatorname{col}(A)=\operatorname{rango}(A)$. El teorema de la dimensión aplicado a $T_A$ es exactamente la relación de [rango–nulidad](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/):

$$
\operatorname{rango}(A)+\dim\operatorname{nul}(A)=n\quad(\text{cantidad de columnas}).
$$

En términos de sistemas: la cantidad de parámetros libres de la solución de $Ax=0$ es la cantidad de incógnitas menos la cantidad de pivotes.

## Consecuencias

De $\dim\operatorname{Im}(T)=\dim V-\dim\operatorname{Nu}(T)$ y de que $\operatorname{Im}(T)\subseteq W$ salen cotas que conviene tener a mano:

:::tip[Cotas que da el teorema]
Si $T:V\to W$ es lineal, con $\dim V=n$ y $\dim W=m$:

1. $\dim\operatorname{Im}(T)\le n$: una TL **no puede aumentar la dimensión**.
2. $\dim\operatorname{Im}(T)\le m$, porque la imagen es un subespacio de $W$.
3. $\dim\operatorname{Nu}(T)\ge n-m$. En particular, si $n>m$, el núcleo **no es trivial**.
4. Si $n<m$, entonces $\dim\operatorname{Im}(T)\le n<m$: la imagen **no es todo $W$**.
:::

Por ejemplo, no existe una TL de $\mathbb{R}^3$ en $\mathbb{R}^2$ con núcleo trivial (sería $\dim\operatorname{Im}=3>2$), ni una TL de $\mathbb{R}^2$ en $\mathbb{R}^3$ cuya imagen sea todo $\mathbb{R}^3$. Ningún programa puede "comprimir sin pérdida" todos los vectores de $\mathbb{R}^3$ en $\mathbb{R}^2$ mediante una TL: siempre hay vectores distintos con la misma imagen.

## Decidir sin hacer cuentas

En los parciales es habitual pedir que se decida algo **antes** de calcular, o en lugar de calcular. El esquema es siempre el mismo: acotar una de las dimensiones y despejar la otra.

- $T:\mathbb{R}^5\to\mathbb{R}^3$ con $\operatorname{Im}(T)=\mathbb{R}^3$. Entonces $\dim\operatorname{Nu}(T)=5-3=2$.
- $T:P_3[\mathbb{R}]\to\mathbb{R}^{2\times 2}$ con $\dim\operatorname{Nu}(T)=1$. Entonces $\dim\operatorname{Im}(T)=4-1=3<4$: la imagen no es todo $\mathbb{R}^{2\times 2}$.
- Si $T:V\to W$ cumple $\operatorname{Nu}(T)=\operatorname{Im}(T)$ (posible solo si $V=W$ o al menos $\operatorname{Nu}(T)\subseteq W$), entonces $\dim V=2\dim\operatorname{Nu}(T)$: **$\dim V$ debe ser par**.

### Ejemplo 1 · Imagen sin calcularla
<!-- check: U2.T03.E1 -->

Sea $T:P_3[\mathbb{R}]\to\mathbb{R}^3$, $T(p)=\big(p(1),\ p(-1),\ p'(0)\big)$. Hallar $\operatorname{Nu}(T)$ y, sin más cuentas, $\operatorname{Im}(T)$.

**Núcleo.** Con $p=a+bx+cx^2+dx^3$: $p(1)=a+b+c+d$, $p(-1)=a-b+c-d$ y $p'(0)=b$. El sistema homogéneo tiene matriz

$$
\begin{pmatrix}1&1&1&1\\1&-1&1&-1\\0&1&0&0\end{pmatrix}\xrightarrow{F_2-F_1\to F_2}\begin{pmatrix}1&1&1&1\\0&-2&0&-2\\0&1&0&0\end{pmatrix}\xrightarrow{F_3+\frac12F_2\to F_3}\begin{pmatrix}1&1&1&1\\0&-2&0&-2\\0&0&0&-1\end{pmatrix}.
$$

De abajo hacia arriba: $d=0$; $-2b-2d=0$, así que $b=0$; $a+c=0$, así que $a=-c$. Entonces $p=-c+cx^2=c\,(x^2-1)$ y

$$
\operatorname{Nu}(T)=\operatorname{gen}\{x^2-1\},\qquad\dim\operatorname{Nu}(T)=1.
$$

Corroboramos: si $p=x^2-1$, $p(1)=0$, $p(-1)=0$ y $p'(x)=2x$ da $p'(0)=0$.

**Imagen.** Por el teorema de la dimensión, $\dim\operatorname{Im}(T)=\dim P_3[\mathbb{R}]-1=4-1=3$. Como $\operatorname{Im}(T)$ es un subespacio de $\mathbb{R}^3$ de dimensión 3, **$\operatorname{Im}(T)=\mathbb{R}^3$**. Interpretación: para cualquier terna $(r,s,t)$ hay un polinomio de grado $\le 3$ con $p(1)=r$, $p(-1)=s$ y $p'(0)=t$; y hay infinitos, porque se le puede sumar cualquier múltiplo de $x^2-1$.

### Ejemplo 2 · Núcleo e imagen de A ↦ A − Aᵗ
<!-- check: U2.T03.E2 -->

Sea $T:\mathbb{R}^{2\times 2}\to\mathbb{R}^{2\times 2}$, $T(A)=A-A^t$. Hallar núcleo e imagen.

**Núcleo.** $T(A)=0$ si y solo si $A=A^t$: el núcleo es el subespacio $\mathcal S$ de las matrices simétricas, de dimensión 3 (base $\{E_{11},\ E_{12}+E_{21},\ E_{22}\}$).

**Imagen.** Por el teorema, $\dim\operatorname{Im}(T)=4-3=1$. Para identificarla basta un vector no nulo de la imagen. Con $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,

$$
A-A^t=\begin{pmatrix}0&b-c\\c-b&0\end{pmatrix}=(b-c)\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

así que $\operatorname{Im}(T)=\operatorname{gen}\left\{\begin{pmatrix}0&1\\-1&0\end{pmatrix}\right\}$: son las matrices **antisimétricas** ($A^t=-A$).

**Comprobación.** $3+1=4=\dim\mathbb{R}^{2\times 2}$.

### Ejemplo 3 · Una TL que no existe
<!-- check: U2.T03.E3 -->

Decidir si existe una TL $T:\mathbb{R}^3\to\mathbb{R}^4$ tal que $T(1,2,0)=2\,T(0,1,1)$ y cuya imagen contenga a los vectores $(1,0,1,0)$, $(0,1,0,1)$ y $(1,1,0,0)$.

Supongamos que existe.

1. **Cota para el núcleo.** De $T(1,2,0)-2T(0,1,1)=0$ y la linealidad, $T\big((1,2,0)-2(0,1,1)\big)=T(1,0,-2)=(0,0,0,0)$. Como $(1,0,-2)\neq 0$, $\dim\operatorname{Nu}(T)\ge 1$.
2. **Cota para la imagen.** Los tres vectores dados son LI: si $\alpha(1,0,1,0)+\beta(0,1,0,1)+\gamma(1,1,0,0)=(\alpha+\gamma,\ \beta+\gamma,\ \alpha,\ \beta)=0$, la tercera y la cuarta componente dan $\alpha=\beta=0$, y entonces $\gamma=0$. Como están en $\operatorname{Im}(T)$, $\dim\operatorname{Im}(T)\ge 3$.
3. **Contradicción.** $\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)\ge 1+3=4$, pero el teorema de la dimensión exige que la suma sea $\dim\mathbb{R}^3=3$.

Por lo tanto, **no existe** tal TL (y no tiene sentido preguntar si es única).

### Ejemplo 4 · El tamaño del código de Hamming sin listar sus palabras
<!-- check: U2.T03.E4 -->

La matriz de control de paridad del código de Hamming $(7,4)$ tiene como columnas los siete vectores no nulos de $\mathbb{Z}_2^3$:

$$
H=\begin{pmatrix}0&0&0&1&1&1&1\\0&1&1&0&0&1&1\\1&0&1&0&1&0&1\end{pmatrix},
$$

y el código es $\mathcal C=\operatorname{nul}(H)=\operatorname{Nu}(T_H)$, donde $T_H:\mathbb{Z}_2^7\to\mathbb{Z}_2^3$, $T_H(v)=Hv^t$. ¿Cuántas palabras tiene?

Entre las columnas de $H$ están las tres canónicas de $\mathbb{Z}_2^3$ (columnas 1, 2 y 4), así que $\operatorname{Im}(T_H)=\mathbb{Z}_2^3$ y $\operatorname{rango}(H)=3$. Por el teorema de la dimensión (que vale sobre cualquier cuerpo), $\dim\mathcal C=7-3=4$, y un subespacio de dimensión 4 de $\mathbb{Z}_2^7$ tiene $2^4=16$ elementos: las 16 palabras código, sin haber escrito ninguna.

:::caution[Errores frecuentes]
- **Usar la dimensión de la llegada en lugar de la de salida.** Para $T:\mathbb{R}^3\to\mathbb{R}^4$ la suma da $3$, no $4$. El ejemplo 3 se apoya justamente en eso.
- **Concluir igualdad de subespacios solo por igualdad de dimensiones.** $\dim\operatorname{Im}(T)=3$ en $\mathbb{R}^3$ sí implica $\operatorname{Im}(T)=\mathbb{R}^3$, porque la imagen está contenida en $\mathbb{R}^3$. Pero dos planos distintos de $\mathbb{R}^3$ tienen la misma dimensión y no son iguales: hace falta la inclusión.
- **Creer que si $\dim V=\dim W$ entonces la imagen es $W$.** La TL nula de $\mathbb{R}^2$ en $\mathbb{R}^2$ tiene imagen $\{0\}$.
- **Sumar dimensiones de subespacios que viven en espacios distintos sin el teorema.** La igualdad $\dim V=\dim\operatorname{Nu}+\dim\operatorname{Im}$ es un teorema sobre una TL concreta; no dice nada de subespacios cualesquiera de $V$ y $W$.
- **Extender la base del núcleo con vectores del núcleo.** En la demostración, los $v_j$ agregados no están en $\operatorname{Nu}(T)$ (si alguno estuviera, la base extendida sería LD).
:::

## Autoevaluación

1. $T:\mathbb{R}^4\to\mathbb{R}^2$ es lineal y no es nula. ¿Qué valores puede tomar $\dim\operatorname{Nu}(T)$?

<details>
<summary>Respuesta</summary>

$\dim\operatorname{Im}(T)\in\{1,2\}$ (no es $0$ porque $T$ no es nula, y no supera $2$). Luego $\dim\operatorname{Nu}(T)=4-\dim\operatorname{Im}(T)\in\{2,3\}$.

</details>

2. ¿Existe una TL $T:\mathbb{R}^3\to\mathbb{R}^3$ con $\operatorname{Nu}(T)=\operatorname{Im}(T)$?

<details>
<summary>Respuesta</summary>

No: sería $3=2\dim\operatorname{Nu}(T)$, imposible con dimensiones enteras.

</details>

3. Sea $D:P_3[\mathbb{R}]\to P_3[\mathbb{R}]$ la derivación. Calcular $\dim\operatorname{Im}(D)$ usando el núcleo.

<details>
<summary>Respuesta</summary>

$\operatorname{Nu}(D)$ son los polinomios constantes, de dimensión 1. Entonces $\dim\operatorname{Im}(D)=4-1=3$ (y, en efecto, $\operatorname{Im}(D)=P_2[\mathbb{R}]$).

</details>

:::tip[En resumen]
- Si $\dim V$ es finita, $\dim V=\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)$.
- La prueba extiende una base del núcleo a una base de $V$; las imágenes de los vectores agregados forman una base de la imagen.
- Para matrices es la relación rango–nulidad: $\operatorname{rango}(A)+\dim\operatorname{nul}(A)=n$.
- Si $\dim V>\dim W$, el núcleo no es trivial; si $\dim V<\dim W$, la imagen no es todo $W$.
- Patrón de no existencia: cotas para $\dim\operatorname{Nu}$ y $\dim\operatorname{Im}$ cuya suma no puede ser $\dim V$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 6.5, "El kernel y el rango de una transformación lineal" (p. 499), donde el resultado aparece como teorema del rango; y sección 3.5, "Subespacios, bases, dimensión y rank" (p. 197), para la versión matricial.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: la sección sobre el rango de una matriz y el teorema del rango.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed.: sección 5.4 (p. 195).
- Antes: [2.2 Núcleo e imagen](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/) y [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/) (extensión de un conjunto LI a una base).
- Después: [2.4 Clasificación](/algebra-ii/unidad-2/teoria/clasificacion/), donde el teorema se usa para comparar inyectividad y suryectividad.
