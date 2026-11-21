---
title: Continuidad y discontinuidades
description: Continuidad en un punto y en intervalos, álgebra de funciones continuas, teoremas de Bolzano, del valor intermedio y de Weierstrass, y clasificación de las discontinuidades.
slug: analisis-matematico-i/unidad-2/teoria/continuidad
sidebar:
  order: 7
---

## Qué vas a aprender

- Verificar las tres condiciones de continuidad en un punto y la continuidad lateral en los extremos de un intervalo cerrado.
- Usar el álgebra de funciones continuas y la continuidad de la composición.
- Enunciar y aplicar los teoremas de Bolzano, del valor intermedio y de Weierstrass, con sus hipótesis.
- Clasificar discontinuidades (evitable; esencial de primera especie, de salto finito o infinito; esencial de segunda especie), calcular el salto y redefinir las evitables.

**Antes de empezar.** Necesitás la definición de límite y de entorno ([Entornos y límite finito](/analisis-matematico-i/unidad-2/teoria/entornos-y-limite/)), los límites laterales y el álgebra de límites ([Límites laterales y propiedades](/analisis-matematico-i/unidad-2/teoria/limites-laterales-y-propiedades/)), las técnicas para resolver indeterminaciones ([Cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/)) y, de la [Unidad 1](/analisis-matematico-i/unidad-1/), dominio, composición de funciones, valor absoluto e intervalos. Esta lección es autocontenida: está pensada para que el tema se pueda estudiar de manera autónoma, de principio a fin, con ejemplos resueltos y ejercicios al final.

## Idea: una gráfica sin cortes

Una función es continua en un punto si su gráfica se puede recorrer ahí «sin levantar el lápiz». Eso hay que traducirlo a condiciones verificables: hay un valor $f(a)$ (el lápiz está apoyado en un punto), la función se acerca a algo cuando $x\to a$, y ese algo es justamente $f(a)$.

## Continuidad en un punto

:::note[Definición · Continuidad en un punto]
Sea $a$ un número tal que $f$ está definida en algún entorno reducido $E^{*}(a,r)$ ($a$ puede pertenecer o no al dominio). $f$ es **continua en $x=a$** si se cumplen las tres condiciones:

1. existe $f(a)$ (es decir, $a\in D_f$);
2. existe $\displaystyle\lim_{x\to a}f(x)$ (como número real);
3. $\displaystyle\lim_{x\to a}f(x)=f(a)$.
:::

Las tres se resumen en $\lim_{x\to a}f(x)=f(a)$: si vale esa igualdad, ambos miembros existen. Si falla alguna condición, $f$ es **discontinua** en $a$; en particular, un punto que no pertenece al dominio pero está rodeado por él (como $x=2$ en $\frac{1}{x-2}$) es un punto de discontinuidad. Si $a$ es un extremo del dominio (por ejemplo, el extremo de un intervalo cerrado), se usan los límites laterales: lo vemos en la sección siguiente. «Existe» quiere decir que es un número real: un límite infinito no cuenta.

Con $\varepsilon$ y $\delta$: $f$ es continua en $a$ si $\forall\varepsilon>0\ \exists\delta>0:\ \lvert x-a\rvert<\delta\Rightarrow\lvert f(x)-f(a)\rvert<\varepsilon$ (ahora el entorno **no** es reducido: $x=a$ se admite).

### Continuidad lateral

$f$ es **continua por derecha** en $a$ si $\lim_{x\to a^{+}}f(x)=f(a)$, y **continua por izquierda** si $\lim_{x\to a^{-}}f(x)=f(a)$. Resulta: $f$ es continua en $a$ si y solo si es continua por ambos lados.

### Ejemplo 1 · Las tres condiciones

<!-- check: U2.T.CONT.1 -->

Sea $f(x)=\begin{cases}\dfrac{x^2-4}{x-2} & \text{si } x\ne2\\[4pt] k & \text{si } x=2\end{cases}$. ¿Para qué $k$ es continua en $2$?

Para $x\ne2$, $f(x)=x+2$ y $\lim_{x\to2}f=4$ (existe). La condición 1 pide $f(2)=k$ y la 3 pide $k=4$. Con $k=4$ es continua; con cualquier otro valor, el límite existe pero es distinto de $f(2)$.

### Ejemplo 2 · Funciones definidas en un punto

<!-- check: U2.T.CONT.2 -->

a) $g(x)=\dfrac{\operatorname{sen}x}{x}$ si $x\ne0$ y $g(0)=1$: como $\lim_{x\to0}g=1=g(0)$, es continua en $0$.

b) $h(x)=\dfrac{1-\cos x}{x^2}$ si $x\ne0$ y $h(0)=1$: el límite es $\frac12\neq1=h(0)$. **Discontinua** en $0$. Con $h(0)=\frac12$ sería continua.

## Continuidad en intervalos

:::note[Definición · Continuidad en un intervalo]
- $f$ es continua en un intervalo **abierto** $(a,b)$ si es continua en cada punto de $(a,b)$.
- $f$ es continua en un intervalo **cerrado** $[a,b]$ si es continua en $(a,b)$, **continua por derecha** en $a$ y **continua por izquierda** en $b$.
:::

En los extremos solo se pide continuidad del lado que pertenece al intervalo, porque del otro lado la función ni siquiera está definida. Decir «$f$ es continua en su dominio» significa continua en cada punto donde está definida (con la continuidad lateral correspondiente en los extremos).

### Ejemplo 3 · Extremos

<!-- check: U2.T.CONT.3 -->

$f(x)=\sqrt{4-x^2}$ tiene dominio $[-2,2]$. En $(-2,2)$ es continua (composición de continuas, ver más abajo). En $x=2$: $\lim_{x\to2^{-}}\sqrt{4-x^2}=0=f(2)$. En $x=-2$: $\lim_{x\to-2^{+}}\sqrt{4-x^2}=0=f(-2)$. Es continua en $[-2,2]$.

## Funciones continuas conocidas

Aceptamos sin demostración que son continuas en todo su dominio: los **polinomios** (en $\mathbb{R}$), las **racionales** (donde el denominador no se anula), $\sqrt[n]{x}$, $\lvert x\rvert$, $e^x$, $\ln x$ (en $x>0$), $\operatorname{sen}x$, $\cos x$ (en $\mathbb{R}$), $\tan x$ (donde $\cos x\ne0$) y las inversas trigonométricas en su dominio. Para los polinomios sale de $\lim_{x\to a}x=a$ y del álgebra de límites: $\lim_{x\to a}P(x)=P(a)$.

## Álgebra de funciones continuas

:::note[Teorema · Operaciones y composición]
**Hipótesis:** $f$ y $g$ son continuas en $a$. Entonces son continuas en $a$: $f+g$, $f-g$, $kf$, $f\cdot g$, y $\dfrac fg$ **si $g(a)\ne0$**.

**Composición.** Si $f$ es continua en $a$ y $g$ es continua en $f(a)$, entonces $g\circ f$ es continua en $a$.
:::

**Demostración (suma).** $\lim_{x\to a}(f+g)(x)=\lim f+\lim g=f(a)+g(a)=(f+g)(a)$, por el álgebra de límites y la continuidad de cada una. Para el producto y el cociente es igual. $\blacksquare$

**Idea de la composición.** Si $x$ está cerca de $a$, $f(x)$ está cerca de $f(a)$ por la continuidad de $f$; y como $g$ es continua en $f(a)$, $g(f(x))$ está cerca de $g(f(a))$.

:::note[Propiedad · Límite de una composición]
Si $\lim\limits_{x\to a}f(x)=L$ y $g$ es continua en $L$, entonces $\lim\limits_{x\to a}g\bigl(f(x)\bigr)=g(L)$: el límite «pasa adentro» de una función continua.
:::

La idea es la misma que la de la composición, pero ahora $f$ no necesita estar definida en $a$ ni ser continua allí: alcanza con que $f(x)$ se acerque a $L$. Es la propiedad que justifica, en [Cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/), pasos como $\lim \ln\bigl(f(x)\bigr)=\ln\bigl(\lim f(x)\bigr)$ o $\lim e^{f(x)}=e^{\lim f(x)}$.

**Las hipótesis importan.** Sea $g(y)=0$ si $y\ne0$ y $g(0)=1$ (discontinua en $0$), y $f(x)=x^2$ (continua). Entonces $g(f(x))=0$ para $x\neq0$ y $g(f(0))=1$: la composición es **discontinua** en $0$ porque $g$ no era continua en $f(0)=0$.

### Ejemplo 4 · Dónde es continua

<!-- check: U2.T.CONT.4 -->

$f(x)=\dfrac{\ln(4-x^2)}{x+1}$. El logaritmo exige $4-x^2>0\iff-2<x<2$; el cociente exige $x\ne-1$. Por el álgebra y la composición, $f$ es continua en $(-2,-1)\cup(-1,2)$, que es su dominio. En $x=-1$ no está definida; en $x=\pm2$ tampoco.

## Discontinuidades

Hay discontinuidad en $a$ cuando falla alguna de las tres condiciones. Se las clasifica por el comportamiento del límite.

:::note[Definición · Clasificación de las discontinuidades]
Sea $a$ un punto de discontinuidad.

- **Evitable**: existe $\lim_{x\to a}f(x)=\ell$ (número real) pero $f(a)$ no existe o es distinto de $\ell$.
- **Esencial**: el límite no existe o es infinito. Dentro de ellas:
  - de **primera especie**, que pueden ser de **salto finito** (los dos laterales existen, son finitos y distintos) o de **salto infinito** (al menos un lateral es infinito);
  - de **segunda especie**: al menos un lateral no existe, ni finito ni infinito (la función oscila, como $\operatorname{sen}\frac1x$ en $0$).
:::

El **salto** de una discontinuidad esencial de salto finito es $\bigl\lvert\lim_{x\to a^{+}}f-\lim_{x\to a^{-}}f\bigr\rvert$.

Las de segunda especie no tienen salto definido, porque algún lateral no existe.

![Cuatro gráficos: discontinuidad evitable (hueco con otro valor), esencial de salto finito, esencial de salto infinito y esencial oscilante de sen(1/x)](/analisis-matematico-i/figuras/u2-discontinuidades.svg)

*Qué observar: en la evitable la curva se acerca a un único valor; en la de salto finito hay dos alturas distintas; en la de salto infinito la curva escapa; en la oscilante no se acerca a nada.*

**Redefinir.** Una discontinuidad **evitable** se elimina redefiniendo (o definiendo) $f(a):=\ell$. Una esencial no se puede evitar: ningún valor de $f(a)$ arregla un salto o una divergencia.

### Procedimiento para estudiar una función

1. Hallar el dominio y los puntos candidatos: ceros de denominadores, bordes del dominio, empalmes de funciones por tramos, ceros de un módulo.
2. En cada candidato, calcular **los dos laterales** (o el límite) y $f(a)$ si existe.
3. Decidir: si el límite existe finito y coincide con $f(a)$, continua; si existe finito pero no coincide o $f(a)$ no existe, evitable; si no, esencial: de salto finito, de salto infinito o, si algún lateral no existe, de segunda especie.

### Ejemplo 5 · Evitable y salto infinito

<!-- check: U2.T.CONT.5 -->

$f(x)=\dfrac{x^2-x-2}{x^2-4}=\dfrac{(x-2)(x+1)}{(x-2)(x+2)}$. Dominio $\mathbb{R}-\{-2,2\}$.

- $x=2$: $\lim f=\lim\frac{x+1}{x+2}=\frac34$, finito, y $f(2)$ no existe: **evitable**. Se redefine $f(2):=\frac34$.
- $x=-2$: $\frac{x+1}{x+2}$ con numerador $\to-1$: por derecha $\frac{-1}{0^{+}}=-\infty$ y por izquierda $\frac{-1}{0^{-}}=+\infty$: **esencial de salto infinito** (AV $x=-2$).

### Ejemplo 6 · Salto finito

<!-- check: U2.T.CONT.6 -->

$g(x)=\begin{cases}2x+1 & x<3\\ 12-x & x\ge3\end{cases}$. En $x=3$: por izquierda $7$, por derecha $9$, $g(3)=9$. Laterales finitos distintos: **esencial de salto finito**, con salto $\lvert9-7\rvert=2$. Es continua por derecha en $3$ (porque $g(3)=\lim_{x\to3^{+}}g$) pero no por izquierda.

### Ejemplo 7 · Con exponencial

<!-- check: U2.T.CONT.7 -->

$h(x)=e^{1/(x-1)}$ en $x=1$: si $x\to1^{+}$, $\frac1{x-1}\to+\infty$ y $h\to+\infty$; si $x\to1^{-}$, $\frac1{x-1}\to-\infty$ y $h\to0$. Un lateral es infinito: **esencial de salto infinito**.

### Ejemplo 8 · Parámetros

<!-- check: U2.T.CONT.8 -->

Hallar $a,b$ para que $f$ sea continua en $\mathbb{R}$:
$f(x)=\begin{cases}\dfrac{e^{ax}-1}{x} & x<0\\ bx+3 & 0\le x\le1\\ \dfrac{x^2-1}{x-1} & x>1\end{cases}$

En $x=0$: por izquierda, $\frac{e^{ax}-1}{x}\to a$; por derecha y en $0$: $3$. Entonces $a=3$. En $x=1$: por izquierda $b+3$; por derecha $\frac{x^2-1}{x-1}=x+1\to2$. Entonces $b+3=2$, $b=-1$. Con $a=3$, $b=-1$ las tres condiciones valen en $0$ y en $1$; en el resto de los intervalos las expresiones son continuas.

## Propiedades de las funciones continuas en un intervalo cerrado

Los tres teoremas que siguen son de existencia: garantizan que ciertos valores aparecen. **Se enuncian aquí con sus hipótesis y sin demostración formal** (su demostración usa la completitud de $\mathbb{R}$); no los pide el programa literalmente, pero conviene conocerlos.

:::note[Teorema · Estabilidad del signo]
Si $f$ es continua en $a$ y $f(a)>0$, existe un entorno de $a$ donde $f>0$. (Es la conservación del signo con $L=f(a)$.)
:::

:::note[Teorema · Bolzano]
**Hipótesis:** $f$ es continua en $[a,b]$ y $f(a)\cdot f(b)<0$ (signos opuestos). **Tesis:** existe $c\in(a,b)$ con $f(c)=0$.
:::

**Idea de la demostración.** Una función continua no puede pasar de negativa a positiva sin cruzar el $0$: el conjunto de puntos donde $f<0$ tiene un «borde», y ahí $f$ debe valer $0$ por continuidad. (No es una demostración formal.)

![Gráfico de x³ + x − 1 en el intervalo [0, 1]: vale −1 en 0, 1 en 1 y se anula en c ≈ 0,68](/analisis-matematico-i/figuras/u2-bolzano.svg)

*Qué observar: $f(0)=-1<0$, $f(1)=1>0$ y la curva, continua, tiene que cruzar el eje $x$ entre $0$ y $1$.*

**Si falla una hipótesis, falla la tesis.**

- Sin continuidad en $[a,b]$: $f(x)=-1$ si $x<0$, $f(x)=1$ si $x\ge0$ en $[-1,1]$ tiene $f(-1)f(1)<0$ y no se anula.
- Sin continuidad en un extremo: $f(0)=-1$ y $f(x)=x^2$ para $0<x\le1$. Es continua en $(0,1]$, $f(0)f(1)<0$, pero no se anula (es discontinua por derecha en $0$).
- La recíproca es falsa: $f(x)=x^2$ en $[-1,1]$ se anula en $0$ con $f(-1)f(1)>0$. Bolzano da una condición suficiente, no necesaria.

:::note[Teorema · Valor intermedio]
**Hipótesis:** $f$ continua en $[a,b]$. **Tesis:** para todo $k$ entre $f(a)$ y $f(b)$ existe $c\in[a,b]$ con $f(c)=k$.
:::

**Demostración (a partir de Bolzano).** Si $k$ está entre $f(a)$ y $f(b)$, la función $\varphi(x)=f(x)-k$ es continua en $[a,b]$ y $\varphi(a),\varphi(b)$ tienen signos opuestos (o alguno es $0$). Por Bolzano existe $c$ con $\varphi(c)=0$, o sea $f(c)=k$; y si $\varphi(a)=0$ o $\varphi(b)=0$, directamente $c=a$ o $c=b$. $\blacksquare$

:::note[Teorema · Weierstrass]
**Hipótesis:** $f$ continua en un intervalo **cerrado y acotado** $[a,b]$. **Tesis:** $f$ alcanza un máximo absoluto y un mínimo absoluto en $[a,b]$ (existen $c_1,c_2\in[a,b]$ con $f(c_1)\le f(x)\le f(c_2)$ para todo $x$). En particular está acotada.
:::

Si falla una hipótesis: $f(x)=x$ en $(0,1)$ (intervalo abierto) es continua pero no tiene máximo ni mínimo; $f(x)=\frac1x$ en $(0,1]$ es continua y no está acotada; $f(x)=\frac1x$ si $x\ne0$ y $f(0)=0$ en $[0,1]$ no es continua en $0$ y no está acotada.

Juntando Weierstrass y el valor intermedio: si $f$ es continua en $[a,b]$ con mínimo $m$ y máximo $M$, su imagen es exactamente el intervalo $[m,M]$.

### Ejemplo 9 · Aplicar Bolzano y aproximar

<!-- check: U2.T.CONT.9 -->

Probar que $x^3+x-1=0$ tiene una raíz en $[0,1]$ y acotarla con bisección. $f(x)=x^3+x-1$ es un polinomio (continuo), $f(0)=-1<0$ y $f(1)=1>0$: por Bolzano hay raíz $c\in(0,1)$. Mirando el punto medio: $f(0{,}5)=-0{,}375<0$ → $c\in(0{,}5;1)$; $f(0{,}75)=0{,}171875>0$ → $c\in(0{,}5;0{,}75)$; $f(0{,}625)=-0{,}130859\ldots<0$ → $c\in(0{,}625;0{,}75)$; $f(0{,}6875)=0{,}012451\ldots>0$ → $c\in(0{,}625;0{,}6875)$.

### Ejemplo 10 · Valor intermedio

<!-- check: U2.T.CONT.10 -->

La ecuación $\cos x=x$ tiene solución en $[0,1]$: $g(x)=\cos x-x$ es continua, $g(0)=1>0$ y $g(1)=\cos1-1<0$ (porque $\cos1<1$). Por Bolzano existe $c\in(0,1)$ con $\cos c=c$.

### Ejemplo 11 · Weierstrass

<!-- check: U2.T.CONT.11 -->

$f(x)=x^2-4x+1=(x-2)^2-3$ en $[0,3]$ es continua. El mínimo es $-3$ (en $x=2$) y el máximo es $f(0)=1$ ($f(3)=-2$). La imagen es $[-3,1]$.

:::caution[Errores frecuentes]
- **Decir «continua» mirando solo el límite** y olvidar $f(a)$, o al revés.
- **Escribir $\frac00$ como si fuera un valor** al estudiar el límite en el punto de discontinuidad.
- **No calcular los dos laterales** en una función por tramos o con módulo.
- **Clasificar como evitable una discontinuidad con límite infinito.** Evitable requiere límite **finito**.
- **Aplicar Bolzano a una función que no es continua en todo $[a,b]$**, o concluir «no hay raíz» porque $f(a)f(b)>0$.
- **Pensar que toda discontinuidad se puede redefinir.** Solo las evitables.
- **Olvidar que en los extremos de un intervalo cerrado** solo cuenta el lado que pertenece al intervalo.
:::

## Ejercicios

Para graficar la función y explorar el punto con el comando de límite lateral, mirá la guía de [GeoGebra para límites y continuidad](/analisis-matematico-i/geogebra/limites-continuidad/).

### Ejercicio 23 · Continuidad en un punto
<!-- ejercicio: U2.23 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x)=\begin{cases}\dfrac{x^2-5x+6}{x-2} & \text{si } x\ne2\\ 3 & \text{si } x=2\end{cases}$. Estudiá la continuidad en $x=2$, clasificá la discontinuidad si la hay y redefiní $f$ si es posible.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Verificar las tres condiciones.

**Desarrollo.** (1) $f(2)=3$ existe. (2) Para $x\neq2$, $\frac{(x-2)(x-3)}{x-2}=x-3$, y $\lim_{x\to2}f=-1$ existe. (3) $-1\ne3=f(2)$: falla. Discontinuidad **evitable**; se redefine $f(2):=-1$.

**Resultado.** Discontinua y evitable en $2$; con $f(2)=-1$ queda continua.

</details>

### Ejercicio 24 · Clasificar discontinuidades
<!-- ejercicio: U2.24 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallá y clasificá las discontinuidades de $f(x)=\dfrac{x+3}{x^2+x-6}$ y redefiní las evitables.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Factorizar el denominador y estudiar cada cero.

**Desarrollo.** $x^2+x-6=(x+3)(x-2)$; dominio $\mathbb{R}-\{-3,2\}$. Para $x\ne-3$, $f=\frac1{x-2}$.
- $x=-3$: $\lim f=\frac1{-5}=-\frac15$, finito, $f(-3)$ no existe: evitable; $f(-3):=-\frac15$.
- $x=2$: $\frac1{x-2}\to+\infty$ por derecha y $-\infty$ por izquierda: esencial de salto infinito.

**Resultado.** $x=-3$ evitable (redefinir $-\frac15$); $x=2$ esencial de salto infinito.

</details>

### Ejercicio 25 · Parámetros
<!-- ejercicio: U2.25 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallá $k$ y $m$ para que $f$ sea continua en $\mathbb{R}$:
$f(x)=\begin{cases}\dfrac{\operatorname{sen}4x}{kx} & x<0\\ mx+2 & 0\le x\le1\\ \dfrac{x^3-1}{x-1} & x>1\end{cases}$
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Igualar los laterales y el valor en cada punto de empalme.

**Desarrollo.** En $x=0$: $\lim_{x\to0^{-}}\frac{\operatorname{sen}4x}{kx}=\frac4k$ y $f(0)=2=\lim_{x\to0^{+}}(mx+2)$. Entonces $\frac4k=2$, $k=2$. En $x=1$: por izquierda $m+2$ (y $f(1)=m+2$); por derecha $\frac{x^3-1}{x-1}=x^2+x+1\to3$. Entonces $m+2=3$, $m=1$.

**Resultado.** $k=2$, $m=1$.

</details>

### Ejercicio 26 · Bolzano y bisección
<!-- ejercicio: U2.26 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x)=x^3-3x+1$.

a) Mostrá que $f$ tiene una raíz en cada uno de los intervalos $[-2,-1]$, $[0,1]$ y $[1,2]$, y concluí cuántas raíces reales tiene.

b) Con dos pasos de bisección en $[1,2]$, acotá la raíz de ese intervalo en un intervalo de longitud $\frac14$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $f$ es un polinomio (continuo): buscar cambios de signo.

**Desarrollo.** a) $f(-2)=-1$, $f(-1)=3$, $f(0)=1$, $f(1)=-1$, $f(2)=3$. Hay cambio de signo en $[-2,-1]$, $[0,1]$ y $[1,2]$: por Bolzano hay una raíz en cada uno. Un polinomio de grado $3$ tiene a lo sumo $3$ raíces, así que son exactamente tres.

b) $f(1{,}5)=3{,}375-4{,}5+1=-0{,}125<0$, y $f(2)>0$: la raíz está en $(1{,}5;2)$. $f(1{,}75)=5{,}359375-5{,}25+1=1{,}109375>0$: está en $(1{,}5;1{,}75)$.

**Resultado.** Tres raíces reales; la de $[1,2]$ está en $(1{,}5;\,1{,}75)$.

</details>

### Ejercicio 27 · Opción múltiple
<!-- ejercicio: U2.27 | nivel: intermedio | tipo: opcion-multiple | verificacion: razonamiento -->

:::note[Enunciado]
Sea $f(x)=\dfrac{\lvert x-2\rvert}{x-2}$ si $x\ne2$ y $f(2)=1$. Entonces:

a) $f$ es continua en $2$.

b) $f$ es continua por derecha pero no por izquierda en $2$.

c) $f$ es continua por izquierda pero no por derecha en $2$.

d) $f$ tiene en $2$ una discontinuidad evitable.

e) $f$ tiene en $2$ una discontinuidad esencial de salto infinito.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Calcular los laterales y compararlos con $f(2)$.

**Desarrollo.** Para $x>2$, $f(x)=1$: $\lim_{x\to2^{+}}f=1=f(2)$. Para $x<2$, $f(x)=-1$: $\lim_{x\to2^{-}}f=-1\ne f(2)$.

- a) Falsa: los laterales difieren, no existe el límite.
- b) **Verdadera**: continua por derecha ($1=f(2)$) y no por izquierda ($-1\neq1$).
- c) Falsa: es al revés.
- d) Falsa: evitable requiere que exista el límite; acá los laterales son distintos.
- e) Falsa: los laterales son finitos (salto finito, de $2$).

**Resultado.** Opción b).

</details>

### Ejercicio 28 · Verdadero o falso
<!-- ejercicio: U2.28 | nivel: avanzado | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Decidí si es verdadero o falso y justificá (con demostración o contraejemplo):

a) Si $f$ es continua en $a$ y $g$ es discontinua en $a$, entonces $f+g$ es discontinua en $a$.

b) Si $f$ y $g$ son discontinuas en $a$, entonces $f+g$ es discontinua en $a$.

c) Si $\lvert f\rvert$ es continua en $a$, entonces $f$ es continua en $a$.

d) Si $f$ es continua en $[a,b]$ y $f(a)f(b)>0$, entonces $f$ no se anula en $[a,b]$.

e) Si $f$ es continua en $[0,1]$, entonces está acotada.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para las verdaderas, una demostración corta; para las falsas, un contraejemplo.

**Desarrollo.**

a) **Verdadera.** Si $f+g$ fuera continua en $a$, entonces $g=(f+g)-f$ sería continua (diferencia de continuas): contradicción.

b) **Falsa.** $f(x)=\begin{cases}1&x\ge0\\-1&x<0\end{cases}$ y $g=-f$ son discontinuas en $0$, pero $f+g=0$ es continua.

c) **Falsa.** Con la misma $f$, $\lvert f\rvert=1$ es continua y $f$ no lo es en $0$.

d) **Falsa.** $f(x)=x^2$ en $[-1,1]$: $f(-1)f(1)=1>0$ y $f(0)=0$.

e) **Verdadera.** Es Weierstrass: continua en un cerrado y acotado, alcanza máximo y mínimo.

**Resultado.** V, F, F, F, V.

</details>

## Autoevaluación

1. ¿Puede una función ser continua en un punto fuera de su dominio?

<details>
<summary>Respuesta</summary>

No: la primera condición pide que $f(a)$ exista.

</details>

2. Si $\lim_{x\to a}f(x)=+\infty$, ¿la discontinuidad es evitable?

<details>
<summary>Respuesta</summary>

No: es esencial de salto infinito. Evitable requiere límite finito.

</details>

3. ¿Por qué no se puede aplicar Bolzano a $f(x)=\frac1x$ en $[-1,1]$ aunque $f(-1)f(1)<0$?

<details>
<summary>Respuesta</summary>

Porque $f$ no está definida (y no es continua) en $0\in[-1,1]$. Y, efectivamente, no se anula.

</details>

4. ¿Cuál es el salto de la función signo, $f(x)=\operatorname{sg}(x)$ (que vale $1$ si $x>0$, $0$ si $x=0$ y $-1$ si $x<0$), en $0$?

<details>
<summary>Respuesta</summary>

Los laterales son $1$ y $-1$: salto $\lvert1-(-1)\rvert=2$.

</details>

:::tip[En resumen]
- Continua en $a$: existe $f(a)$, existe el límite (finito) y son iguales.
- En $[a,b]$: continua en $(a,b)$, por derecha en $a$ y por izquierda en $b$.
- Suma, producto, cociente (con $g(a)\ne0$) y composición (con $g$ continua en $f(a)$) de continuas son continuas.
- Evitable: límite finito $\neq f(a)$ o $f(a)$ inexistente (se redefine). Esencial de primera especie: salto finito (laterales finitos distintos; salto $=\lvert L^{+}-L^{-}\rvert$) o salto infinito (algún lateral infinito). Esencial de segunda especie: algún lateral no existe.
- En $[a,b]$ con $f$ continua: Bolzano ($f(a)f(b)<0\Rightarrow$ raíz), valor intermedio, Weierstrass (máximo y mínimo). Sin las hipótesis, fallan.
:::

## Para seguir

Con la continuidad cerramos la Unidad 2. La Unidad 3 usa el límite para definir la derivada: [Unidad 3](/analisis-matematico-i/unidad-3/).
