---
title: Infinitésimos
description: Infinitésimos, su álgebra, comparación de órdenes, infinitésimos equivalentes y cuándo se pueden sustituir en un límite.
slug: analisis-matematico-i/unidad-2/teoria/infinitesimos
sidebar:
  order: 3
---

## Qué vas a aprender

- Reconocer infinitésimos y aplicar su álgebra.
- Comparar infinitésimos: de orden superior, del mismo orden, equivalentes, de orden $k$.
- Usar infinitésimos equivalentes para calcular límites, con sus condiciones de validez.

**Antes de empezar.** Límites laterales, álgebra de límites e intercalación: [Límites laterales y propiedades](/analisis-matematico-i/unidad-2/teoria/limites-laterales-y-propiedades/).

## Para qué sirve

Al calcular $\lim_{x\to0}\frac{\operatorname{sen}x}{1-\cos x}$ o $\lim_{x\to0}\frac{e^{2x}-1}{\ln(1+5x)}$ numerador y denominador tienden a $0$: ¿cuál «llega más rápido»? Los infinitésimos dan un lenguaje para comparar esa velocidad y una herramienta para reemplazar expresiones complicadas por otras simples que se les parecen cerca del punto.

## Definición y álgebra

:::note[Definición · Infinitésimo]
Una función $\varphi$ es un **infinitésimo** en $x=a$ si $\displaystyle\lim_{x\to a}\varphi(x)=0$.
:::

Ser infinitésimo depende del punto: $\varphi(x)=x-3$ lo es en $a=3$, $\varphi(x)=x^2-4$ lo es en $a=2$ y en $a=-2$, $\varphi(x)=\operatorname{sen}(\pi x)$ lo es en todo entero, y $\varphi(x)=x^2+1$ no lo es en ningún punto real.

<!-- check: U2.T.INF.1 -->

Toda función con límite finito $L$ es «$L$ más un infinitésimo»: $\lim_{x\to a}f=L\iff f(x)-L$ es un infinitésimo en $a$.

:::note[Propiedad · Álgebra de infinitésimos]
Si $\varphi_1,\varphi_2$ son infinitésimos en $a$:

1. $\varphi_1+\varphi_2$, $\varphi_1-\varphi_2$ y $\varphi_1\cdot\varphi_2$ son infinitésimos en $a$, y $k\varphi_1$ también ($k\in\mathbb{R}$).
2. Si $g$ está acotada en un entorno reducido de $a$, $\varphi_1\cdot g$ es un infinitésimo en $a$ (es el corolario de la [intercalación](/analisis-matematico-i/unidad-2/teoria/limites-laterales-y-propiedades/)).
:::

Las dos primeras salen del álgebra de límites. **El cociente de infinitésimos no tiene regla fija:** $\frac{x^2}{x}\to0$, $\frac{x}{x^2}$ no está acotado, $\frac{3x}{x}\to3$: depende de cuál es «más chico». Eso es lo que miden los órdenes.

## Comparación de infinitésimos

:::note[Definición · Orden]
Sean $\alpha,\beta$ infinitésimos en $a$, con $\beta(x)\ne0$ en un entorno reducido de $a$. Se mira $\displaystyle\lim_{x\to a}\frac{\alpha(x)}{\beta(x)}$:

| Límite del cociente | Se dice que |
|---|---|
| $0$ | $\alpha$ es de **orden superior** a $\beta$ ($\alpha$ tiende a $0$ más rápido); se escribe $\alpha=o(\beta)$ |
| $\ell\neq0$, finito | $\alpha$ y $\beta$ son del **mismo orden** |
| $1$ | $\alpha$ y $\beta$ son **equivalentes**: $\alpha\sim\beta$ si $x\to a$ |
| $\infty$ | $\alpha$ es de **orden inferior** a $\beta$ |
| no existe | no son comparables |
:::

Equivalentes es un caso particular del mismo orden. El **orden de $\alpha$ respecto de $x-a$** es el número $k>0$ tal que $\displaystyle\lim_{x\to a}\frac{\alpha(x)}{(x-a)^k}=\ell\ne0$ (finito). Entonces $\alpha\sim\ell\,(x-a)^k$.

### Ejemplo 1 · Orden de $1-\cos x$ en $0$

<!-- check: U2.T.INF.2 -->

Comparamos $\alpha(x)=1-\cos x$ con $x$ y con $x^2$ cuando $x\to0$. Multiplicando por el conjugado,

$$
\frac{1-\cos x}{x^2}=\frac{1-\cos^2x}{x^2(1+\cos x)}=\left(\frac{\operatorname{sen}x}{x}\right)^2\cdot\frac1{1+\cos x}\ \longrightarrow\ 1^2\cdot\frac12=\frac12 .
$$

Entonces $1-\cos x$ es de **orden $2$** respecto de $x$ y $1-\cos x\sim\tfrac{x^2}{2}$. Respecto de $x$ (orden $1$), $\frac{1-\cos x}{x}=x\cdot\frac{1-\cos x}{x^2}\to0$: es de orden superior a $x$.

![Gráfico de x², de 1 − cos x y de x²/2 entre −2 y 2; las dos últimas casi coinciden cerca del origen](/analisis-matematico-i/figuras/u2-infinitesimos.svg)

*Qué observar: cerca de $0$, $1-\cos x$ y $\tfrac{x^2}{2}$ son indistinguibles (equivalentes); lejos del origen se separan. $x^2$ es del mismo orden pero con otro coeficiente.*

### Ejemplo 2 · Del mismo orden

<!-- check: U2.T.INF.3 -->

En $x\to0$, $\alpha(x)=x^3+2x^2$ y $\beta(x)=x^2$: $\dfrac{\alpha}{\beta}=x+2\to2\ne0,1$. Son del mismo orden, **no** equivalentes. En cambio $\alpha(x)\sim2x^2$ porque $\frac{x^3+2x^2}{2x^2}=\frac x2+1\to1$.

## Infinitésimos equivalentes fundamentales

Si $u(x)\to0$ cuando $x\to a$ y $u(x)\neq0$ cerca de $a$ (salvo quizás en $a$), entonces, cuando $x\to a$:

<!-- check: U2.T.INF.4 -->

$$
\operatorname{sen}u\sim u,\quad \tan u\sim u,\quad 1-\cos u\sim\frac{u^2}{2},\quad \ln(1+u)\sim u,\quad e^{u}-1\sim u,\quad \operatorname{arcsen}u\sim u,\quad \arctan u\sim u .
$$

Cada una se lee como un límite notable con $u\to0$. Las dos primeras y la tercera ya las deducimos ($\operatorname{sen}u/u\to1$, $\tan u/u\to1$ y el ejemplo 1). Las de $\ln(1+u)$ y $e^u-1$ se demuestran con el número $e$ en [Cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/); hasta llegar ahí, usalas como dato. Las de $\operatorname{arcsen}u$ y $\arctan u$ salen del cambio $t=\operatorname{arcsen}u$ (entonces $t\to0$, $u=\operatorname{sen}t$ y $\frac{u}{t}=\frac{\operatorname{sen}t}{t}\to1$), y de igual modo con la tangente. Es esencial que el argumento $u$ **tienda a cero**: $\operatorname{sen}x\sim x$ vale cuando $x\to0$, no cuando $x\to2$.

También es útil, para raíces, $\sqrt{1+u}-1\sim\tfrac u2$ (se prueba racionalizando: $\sqrt{1+u}-1=\frac{u}{\sqrt{1+u}+1}$).

## Principio de sustitución

:::note[Teorema · Sustitución de infinitésimos equivalentes]
Si $\alpha\sim\alpha'$ y $\beta\sim\beta'$ cuando $x\to a$, entonces

$$
\lim_{x\to a}\frac{\alpha(x)}{\beta(x)}=\lim_{x\to a}\frac{\alpha'(x)}{\beta'(x)}
$$

en el sentido de que si uno existe, el otro también y son iguales. Lo mismo vale para productos: se puede sustituir **cada factor** (o cada factor del numerador y del denominador) por un equivalente.
:::

**Idea de la demostración.** $\frac\alpha\beta=\frac{\alpha}{\alpha'}\cdot\frac{\alpha'}{\beta'}\cdot\frac{\beta'}{\beta}$, y el primero y el tercer factor tienden a $1$.

**La condición clave: se sustituyen factores, no sumandos.** En una suma o resta, reemplazar cada término por su equivalente puede dar un resultado **falso**, porque los términos principales pueden cancelarse y lo que decide está en los de orden superior.

### Ejemplo 3 · Sustituir en un cociente (correcto)

<!-- check: U2.T.INF.5 -->

$\displaystyle\lim_{x\to0}\frac{1-\cos3x}{x\tan2x}$. Es la forma $\frac00$. Con $u=3x\to0$ y $v=2x\to0$: $1-\cos3x\sim\frac{(3x)^2}{2}=\frac{9x^2}{2}$ y $\tan2x\sim2x$. Son factores del numerador y del denominador, así que:

$$
\lim_{x\to0}\frac{1-\cos3x}{x\tan2x}=\lim_{x\to0}\frac{9x^2/2}{x\cdot2x}=\frac94 .
$$

### Ejemplo 4 · Exponencial y logaritmo

<!-- check: U2.T.INF.6 -->

$\displaystyle\lim_{x\to0}\frac{e^{2x}-1}{\ln(1+5x)}$. Con $e^{2x}-1\sim2x$ y $\ln(1+5x)\sim5x$:

$$
\lim_{x\to0}\frac{e^{2x}-1}{\ln(1+5x)}=\lim_{x\to0}\frac{2x}{5x}=\frac25 .
$$

### Ejemplo 5 · Argumento que no es $x$

<!-- check: U2.T.INF.7 -->

$\displaystyle\lim_{x\to2}\frac{\operatorname{sen}(x^2-4)}{x-2}$. Cuando $x\to2$, $u=x^2-4\to0$, así que $\operatorname{sen}(x^2-4)\sim x^2-4=(x-2)(x+2)$ y

$$
\lim_{x\to2}\frac{(x-2)(x+2)}{x-2}=4 .
$$

### Ejemplo 6 · Cuando la sustitución en una resta falla

<!-- check: U2.T.INF.8 -->

Calcular $\displaystyle\lim_{x\to0}\frac{\tan x-\operatorname{sen}x}{x^3}$.

Un error tentador: como $\tan x\sim x$ y $\operatorname{sen}x\sim x$, el numerador sería $x-x=0$ y el límite, $0$. **Es incorrecto**: los dos sumandos se cancelan en el orden $1$ y lo que queda es de orden $3$. Hacemos bien: sacamos factor común y sustituimos **factores**.

$$
\tan x-\operatorname{sen}x=\operatorname{sen}x\left(\frac1{\cos x}-1\right)=\operatorname{sen}x\cdot\frac{1-\cos x}{\cos x}\ \sim\ x\cdot\frac{x^2/2}{1}=\frac{x^3}{2}.
$$

Entonces el límite es $\dfrac{x^3/2}{x^3}=\dfrac12$. (Con una tabla: en $x=0{,}01$ el cociente vale aproximadamente $0{,}50001$.)

:::caution[Errores frecuentes]
- **Sustituir equivalentes dentro de una suma o diferencia** (ejemplo 6). Solo se pueden reemplazar factores; para sumas, factorizar primero.
- **Aplicar $\operatorname{sen}u\sim u$ sin que $u\to0$.** En $\lim_{x\to2}\frac{\operatorname{sen}x}{x-2}$ no vale: $\operatorname{sen}x\to\operatorname{sen}2\ne0$.
- **Confundir «equivalentes» con «del mismo orden».** $2x$ y $x$ son del mismo orden pero no equivalentes.
- **Decir que el cociente de infinitésimos es un infinitésimo.** Puede tender a cualquier valor, a $\infty$ o no existir.
- **Olvidar que $x^2+1$ no es infinitésimo:** su límite en cualquier punto real es positivo.
:::

## Ejercicios

### Ejercicio 9 · Orden de varios infinitésimos
<!-- ejercicio: U2.09 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $x\to0$, hallá el orden respecto de $x$ y el equivalente de la forma $\ell x^k$ de cada infinitésimo, y decí cuáles son equivalentes entre sí:

$\varphi_1=3x$, $\quad\varphi_2=x^2-x^3$, $\quad\varphi_3=\operatorname{sen}(x^2)$, $\quad\varphi_4=1-\cos x$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para cada $\varphi$ buscar $k$ tal que $\varphi/x^k$ tenga límite finito no nulo.

**Desarrollo.**

- $\varphi_1=3x$: $\varphi_1/x=3$, orden $1$, $\varphi_1\sim3x$.
- $\varphi_2=x^2-x^3$: $\varphi_2/x^2=1-x\to1$, orden $2$, $\varphi_2\sim x^2$.
- $\varphi_3=\operatorname{sen}(x^2)$: como $x^2\to0$, $\operatorname{sen}(x^2)\sim x^2$; $\varphi_3/x^2\to1$, orden $2$.
- $\varphi_4=1-\cos x$: $\varphi_4/x^2\to\tfrac12$, orden $2$, $\varphi_4\sim\tfrac12x^2$.

$\varphi_2\sim x^2\sim\varphi_3$, así que $\varphi_2$ y $\varphi_3$ son equivalentes. $\varphi_4$ es del mismo orden que ellos pero no equivalente ($\varphi_4/\varphi_2\to\tfrac12$). Y $\varphi_2,\varphi_3,\varphi_4$ son de orden superior a $\varphi_1$ ($\varphi_2/\varphi_1\to0$).

**Resultado.** Órdenes $1,2,2,2$; equivalentes: $\varphi_2$ y $\varphi_3$.

</details>

### Ejercicio 10 · Límites con equivalentes
<!-- ejercicio: U2.10 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Calculá usando infinitésimos equivalentes:

a) $\displaystyle\lim_{x\to0}\frac{\operatorname{sen}6x}{\ln(1+2x)}$

b) $\displaystyle\lim_{x\to0}\frac{1-\cos4x}{x\operatorname{sen}2x}$

c) $\displaystyle\lim_{x\to1}\frac{\operatorname{sen}(x^2-1)}{\ln x}$
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Verificar que cada argumento tiende a $0$ y sustituir factores.

**Desarrollo.**

a) $\operatorname{sen}6x\sim6x$ y $\ln(1+2x)\sim2x$: el cociente tiende a $\frac{6x}{2x}=3$.

b) $1-\cos4x\sim\frac{(4x)^2}2=8x^2$ y $\operatorname{sen}2x\sim2x$: $\frac{8x^2}{x\cdot2x}=4$.

c) Con $x\to1$: $x^2-1\to0$, así que $\operatorname{sen}(x^2-1)\sim x^2-1$. Y $\ln x=\ln(1+(x-1))\sim x-1$, porque $u=x-1\to0$. El cociente es $\frac{(x-1)(x+1)}{x-1}=x+1\to2$.

**Resultado.** a) $3$; b) $4$; c) $2$.

</details>

### Ejercicio 11 · Cuándo no se puede sustituir
<!-- ejercicio: U2.11 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Un compañero calcula $\displaystyle\lim_{x\to0}\frac{\tan2x-\operatorname{sen}2x}{x^3}$ reemplazando $\tan2x\sim2x$ y $\operatorname{sen}2x\sim2x$ y obtiene $0$.

a) Explicá por qué ese procedimiento no es válido.

b) Calculá el límite correctamente.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Factorizar el numerador para sustituir solo factores.

**Desarrollo.**

a) El principio de sustitución vale para productos y cocientes, no para sumas o restas. Aquí los dos términos equivalentes a $2x$ se cancelan y el resultado depende de infinitésimos de orden mayor que se perdieron al sustituir.

b) $\tan2x-\operatorname{sen}2x=\operatorname{sen}2x\cdot\dfrac{1-\cos2x}{\cos2x}$. Con $u=2x\to0$: $\operatorname{sen}2x\sim2x$, $1-\cos2x\sim\frac{(2x)^2}{2}=2x^2$ y $\cos2x\to1$. El numerador es equivalente a $2x\cdot2x^2=4x^3$ y

$$
\lim_{x\to0}\frac{\tan2x-\operatorname{sen}2x}{x^3}=\lim_{x\to0}\frac{4x^3}{x^3}=4 .
$$

**Resultado.** El límite vale $4$, no $0$.

</details>

## Autoevaluación

1. ¿$f(x)=\operatorname{sen}x$ es un infinitésimo en $x=\pi$? ¿Y en $x=\pi/2$?

<details>
<summary>Respuesta</summary>

En $\pi$ sí ($\operatorname{sen}\pi=0$ y es continua). En $\pi/2$ no: el límite es $1$.

</details>

2. $\alpha=x^3$ y $\beta=x$ en $x\to0$: ¿quién es de orden superior?

<details>
<summary>Respuesta</summary>

$\alpha$: $\frac{x^3}{x}=x^2\to0$.

</details>

3. ¿Es cierto que $x+x^2\sim x$ cuando $x\to0$? ¿Y que $(x+x^2)-x\sim x-x=0$?

<details>
<summary>Respuesta</summary>

La primera sí: $\frac{x+x^2}{x}=1+x\to1$. La segunda es absurda: $(x+x^2)-x=x^2\neq0$. Es el error de sustituir en una resta.

</details>

:::tip[En resumen]
- $\varphi$ es infinitésimo en $a$ si $\lim_{x\to a}\varphi=0$; la suma, el producto y el producto por acotada de infinitésimos lo son.
- Se comparan con $\lim\frac\alpha\beta$: $0$ (orden superior), $\ell\ne0$ (mismo orden), $1$ (equivalentes), $\infty$ (orden inferior).
- Si $u\to0$: $\operatorname{sen}u\sim\tan u\sim\ln(1+u)\sim e^u-1\sim u$ y $1-\cos u\sim\tfrac{u^2}2$.
- Se pueden sustituir equivalentes en **productos y cocientes**, nunca (sin cuidado) en sumas y restas.
:::

## Para seguir

Ahora estudiamos qué pasa cuando la función **crece sin cota**: [Límites infinitos y en el infinito](/analisis-matematico-i/unidad-2/teoria/limites-infinitos/).
