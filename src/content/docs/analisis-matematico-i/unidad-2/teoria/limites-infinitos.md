---
title: Límites infinitos y en el infinito
description: Límites infinitos, límites cuando x tiende a más o menos infinito y límites infinitos de variable infinita, con definiciones, interpretación gráfica y cálculo para cocientes de polinomios, exponenciales y logaritmos.
slug: analisis-matematico-i/unidad-2/teoria/limites-infinitos
sidebar:
  order: 4
---

## Qué vas a aprender

- Definir e interpretar gráficamente los límites infinitos y los de variable infinita.
- Operar con $\pm\infty$: qué casos son determinados y cuáles no.
- Calcular límites de cocientes de polinomios, de raíces, de exponenciales y de logaritmos cuando $x\to\pm\infty$.

**Antes de empezar.** [Límites laterales y propiedades](/analisis-matematico-i/unidad-2/teoria/limites-laterales-y-propiedades/) e [Infinitésimos](/analisis-matematico-i/unidad-2/teoria/infinitesimos/).

## Tres situaciones distintas

Con $\infty$ aparecen tres ideas que conviene no mezclar:

| Situación | Qué pasa con $x$ | Qué pasa con $f(x)$ | Ejemplo |
|---|---|---|---|
| Límite **infinito** | $x\to a$ (finito) | $f(x)\to\pm\infty$ | $\displaystyle\lim_{x\to1}\frac1{(x-1)^2}=+\infty$ |
| Límite de **variable infinita** | $x\to\pm\infty$ | $f(x)\to L$ (finito) | $\displaystyle\lim_{x\to+\infty}\frac{2x+1}{x+3}=2$ |
| Límite **infinito de variable infinita** | $x\to\pm\infty$ | $f(x)\to\pm\infty$ | $\displaystyle\lim_{x\to+\infty}(x^2-3x)=+\infty$ |

:::note[Cómo se lee «$=+\infty$»]
Escribir $\lim_{x\to a}f(x)=+\infty$ **no** significa que el límite exista como número: significa que la función **diverge** a $+\infty$ (crece sin cota). Se lo llama «límite infinito» por costumbre, pero no es un número real.
:::

## Límites infinitos

:::note[Definición · Límite infinito]
- $\displaystyle\lim_{x\to a}f(x)=+\infty$ si $\forall M>0\ \exists\delta>0:\ 0<\lvert x-a\rvert<\delta\Rightarrow f(x)>M$.
- $\displaystyle\lim_{x\to a}f(x)=-\infty$ si $\forall M>0\ \exists\delta>0:\ 0<\lvert x-a\rvert<\delta\Rightarrow f(x)<-M$.

Para los laterales se reemplaza $0<\lvert x-a\rvert<\delta$ por $a<x<a+\delta$ (derecha) o $a-\delta<x<a$ (izquierda).
:::

Ahora la tolerancia no es $\varepsilon$ (cercanía a un número) sino $M$ (qué tan alto quiero que supere $f$). Es el mismo desafío: dado $M$, hay que dar un $\delta$.

![Gráfico de 1/(x−1)² con la recta horizontal y = 9 y una banda vertical de radio 1/3 alrededor de x = 1; dentro de la banda la curva queda por encima de 9](/analisis-matematico-i/figuras/u2-limite-infinito.svg)

*Qué observar: dentro de la banda vertical $E^{*}(1,\delta)$, la curva está por encima de la recta $y=M$. Si subimos $M$, hay que angostar la banda.*

### Ejemplo 1 · Por definición

<!-- check: U2.T.LIN.1 -->

Probar que $\displaystyle\lim_{x\to1}\frac1{(x-1)^2}=+\infty$.

Dado $M>0$, queremos $\dfrac1{(x-1)^2}>M$, es decir $(x-1)^2<\dfrac1M$, es decir $\lvert x-1\rvert<\dfrac1{\sqrt M}$. Tomamos $\delta=\dfrac1{\sqrt M}$. Para $M=9$ resulta $\delta=\tfrac13$, como en la figura. $\blacksquare$

### Signo del denominador: los laterales deciden

<!-- check: U2.T.LIN.2 -->

Cuando el numerador tiende a $L\ne0$ y el denominador a $0$, el cociente diverge, pero el **signo** depende del lado. Por ejemplo $\displaystyle\lim_{x\to-1}\frac{x+3}{x+1}$: el numerador tiende a $2>0$.

- Por derecha, $x+1\to0^{+}$ (positivo): el cociente tiende a $+\infty$.
- Por izquierda, $x+1\to0^{-}$ (negativo): el cociente tiende a $-\infty$.

Con laterales distintos, el límite no existe, ni siquiera como $\pm\infty$. (Si fueran el mismo infinito, como en $\frac1{(x-1)^2}$, escribimos $\lim=+\infty$.)

## Límites de variable infinita

:::note[Definición · Límite finito en el infinito]
$\displaystyle\lim_{x\to+\infty}f(x)=L$ si $\forall\varepsilon>0\ \exists N:\ x>N\Rightarrow\lvert f(x)-L\rvert<\varepsilon$.

$\displaystyle\lim_{x\to-\infty}f(x)=L$ si $\forall\varepsilon>0\ \exists N:\ x<N\Rightarrow\lvert f(x)-L\rvert<\varepsilon$.
:::

:::note[Definición · Límite infinito en el infinito]
$\displaystyle\lim_{x\to+\infty}f(x)=+\infty$ si $\forall M>0\ \exists N:\ x>N\Rightarrow f(x)>M$. Los otros tres casos ($-\infty$ y $x\to-\infty$) se definen análogamente.
:::

### Ejemplo 2 · Por definición

<!-- check: U2.T.LIN.3 -->

Probar que $\displaystyle\lim_{x\to+\infty}\frac{2x+1}{x+3}=2$.

Para $x>0$: $\left\lvert\dfrac{2x+1}{x+3}-2\right\rvert=\dfrac{5}{x+3}<\dfrac5x$. Dado $\varepsilon>0$, esto es menor que $\varepsilon$ si $x>\dfrac5\varepsilon$. Tomamos $N=\dfrac5\varepsilon$. Con $\varepsilon=0{,}01$ resulta $N=500$, y efectivamente $\frac5{503}<0{,}01$. $\blacksquare$

## Operaciones con infinitos

Con $L$ un número real fijo:

| Caso **determinado** | Resultado |
|---|---|
| $(+\infty)+(+\infty)$, $\ L+(+\infty)$ | $+\infty$ |
| $(+\infty)\cdot(+\infty)$, $\ L\cdot(+\infty)$ con $L>0$, $\ L\cdot(+\infty)$ con $L<0$ | $+\infty$, $+\infty$, $-\infty$ |
| $\dfrac{L}{\pm\infty}$ | $0$ |
| $\dfrac{L}{0}$ con $L\neq0$ (el denominador tiende a $0$ con signo constante) | $\pm\infty$ (según los signos de $L$ y del denominador) |
| $\dfrac{\pm\infty}{L}$ con $L\neq0$ | $\pm\infty$ (según signos) |
| $(+\infty)^{+\infty}$, $\ a^{+\infty}$ con $a>1$, $\ a^{-\infty}$ con $a>1$ | $+\infty$, $+\infty$, $0$ |
| $\dfrac{\text{acotada}}{\pm\infty}$ (por ejemplo $\dfrac{\operatorname{sen}x}{x}$ si $x\to+\infty$) | $0$ |
| $\text{acotada}+(\pm\infty)$ (por ejemplo $x+\cos x$ si $x\to+\infty$) | $\pm\infty$ |

Las **formas indeterminadas** son $\infty-\infty$, $0\cdot\infty$, $\dfrac00$, $\dfrac\infty\infty$, $1^\infty$, $0^0$ e $\infty^0$: con ellas el resultado depende de las funciones concretas, y se tratan en [Cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/). Los símbolos de la tabla describen **comportamientos de límites**, no operaciones con un «número» $\infty$.

## Cociente de polinomios en $\pm\infty$

Para $\dfrac{p(x)}{q(x)}$ con grados $m=\operatorname{gr}p$, $n=\operatorname{gr}q$ y coeficientes principales $a_m,b_n$, se divide numerador y denominador por $x^{n}$ (la mayor potencia del denominador):

| Grados | $\displaystyle\lim_{x\to\pm\infty}\frac{p(x)}{q(x)}$ |
|---|---|
| $m<n$ | $0$ |
| $m=n$ | $\dfrac{a_m}{b_n}$ |
| $m>n$ | $\pm\infty$ (el signo depende de $a_m/b_n$ y de $x^{m-n}$) |

**Por qué funciona.** Al dividir por $x^n$ cada término $c\,x^{k}/x^{n}$ con $k<n$ tiende a $0$ (es $c/x^{n-k}$), y solo sobreviven los términos de mayor grado.

### Ejemplo 3 · Tres cocientes

<!-- check: U2.T.LIN.4 -->

- $\displaystyle\lim_{x\to\pm\infty}\frac{3x^3-x}{x^3+2}=\lim\frac{3-\frac1{x^2}}{1+\frac2{x^3}}=3$ (mismo grado).
- $\displaystyle\lim_{x\to\pm\infty}\frac{x+1}{x^2+4}=\lim\frac{\frac1x+\frac1{x^2}}{1+\frac4{x^2}}=0$ (grado menor arriba).
- $\displaystyle\frac{2x^2+1}{x-3}$: grado mayor arriba. Para $x\to+\infty$ es $+\infty$; para $x\to-\infty$, como $\frac{2x^2}{x}=2x\to-\infty$, es $-\infty$.

### Ejemplo 4 · Raíces: el módulo importa

<!-- check: U2.T.LIN.5 -->

$\displaystyle\lim_{x\to\pm\infty}\frac{\sqrt{x^2+1}}{x}$. Como $\sqrt{x^2+1}\approx\lvert x\rvert$ para $\lvert x\rvert$ grande:

- si $x\to+\infty$, $\lvert x\rvert=x$ y el cociente tiende a $\dfrac xx=1$;
- si $x\to-\infty$, $\lvert x\rvert=-x$ y el cociente tiende a $\dfrac{-x}{x}=-1$.

Los dos infinitos dan resultados **distintos**. Siempre que haya una raíz de un cuadrado, hay que distinguir $+\infty$ de $-\infty$.

## Exponenciales y logaritmos

Para $a>1$:

$$
\lim_{x\to+\infty}a^x=+\infty,\qquad\lim_{x\to-\infty}a^x=0,\qquad\lim_{x\to+\infty}\ln x=+\infty,\qquad\lim_{x\to0^{+}}\ln x=-\infty .
$$

(Con $0<a<1$ los comportamientos de $a^x$ se intercambian.) Y, cuando $x\to+\infty$ y para cualquier $p>0$, vale la **jerarquía**

$$
\ln x\ \ll\ x^{p}\ \ll\ a^{x}\qquad\text{es decir}\qquad\lim_{x\to+\infty}\frac{\ln x}{x^{p}}=0,\quad\lim_{x\to+\infty}\frac{x^{p}}{a^{x}}=0 .
$$

La exponencial gana a cualquier potencia y la potencia gana a cualquier logaritmo. Aceptamos estos hechos sin demostración: su prueba usa herramientas del cálculo diferencial que no desarrollamos en esta unidad.

### Ejemplo 5 · Cociente de exponenciales

<!-- check: U2.T.LIN.6 -->

$\displaystyle\lim_{x\to\pm\infty}\frac{2^x+3}{3^x-1}$.

- $x\to+\infty$: dividimos por $3^x$: $\dfrac{(2/3)^x+3\cdot3^{-x}}{1-3^{-x}}\to\dfrac{0+0}{1-0}=0$.
- $x\to-\infty$: $2^x\to0$ y $3^x\to0$, así que el límite se obtiene por sustitución: $\dfrac{0+3}{0-1}=-3$.

### Ejemplo 6 · Jerarquía

<!-- check: U2.T.LIN.7 -->

$\displaystyle\lim_{x\to+\infty}\frac{\ln x}{\sqrt x}=0$ (el logaritmo pierde contra la potencia) y $\displaystyle\lim_{x\to+\infty}x\,e^{-x}=\lim\frac{x}{e^{x}}=0$ (la potencia pierde contra la exponencial).

:::caution[Errores frecuentes]
- **Tratar a $\infty$ como un número.** $\infty-\infty=0$ es falso; $\frac\infty\infty=1$ es falso. Son indeterminaciones.
- **Dar un solo resultado cuando hay raíces o exponenciales y $x\to\pm\infty$.** Calcular los dos extremos.
- **Olvidar el signo del denominador** al dividir por cero: $\frac{1}{0^{+}}=+\infty$, $\frac1{0^{-}}=-\infty$.
- **Escribir $\lim=\infty$ cuando los laterales son $+\infty$ y $-\infty$.** En $\frac1x$ en $0$ el límite no existe; hay dos laterales distintos.
- **Confundir «$f\to\infty$» con «$f$ no está acotada»:** $x\operatorname{sen}x$ no está acotada pero no tiende a $\pm\infty$.
:::

## Ejercicios

### Ejercicio 12 · Límites infinitos con signo
<!-- ejercicio: U2.12 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Calculá:

a) $\displaystyle\lim_{x\to3^{+}}\frac{2x+1}{x-3}$

b) $\displaystyle\lim_{x\to3^{-}}\frac{2x+1}{x-3}$

c) $\displaystyle\lim_{x\to1}\frac{x-2}{(x-1)^2}$
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El numerador tiene límite no nulo y el denominador tiende a $0$: el resultado es $\pm\infty$; hay que determinar el signo.

**Desarrollo.**

a) El numerador tiende a $7>0$. Con $x\to3^{+}$, $x-3\to0^{+}$. Cociente: $\frac{7}{0^{+}}=+\infty$.

b) Con $x\to3^{-}$, $x-3\to0^{-}$. Cociente: $\frac7{0^{-}}=-\infty$.

c) El numerador tiende a $-1<0$ y $(x-1)^2\to0^{+}$ por **ambos** lados (es un cuadrado). Cociente: $\frac{-1}{0^{+}}=-\infty$ en los dos laterales, así que $\lim_{x\to1}=-\infty$.

**Resultado.** a) $+\infty$; b) $-\infty$; c) $-\infty$.

</details>

### Ejercicio 13 · Límites en el infinito
<!-- ejercicio: U2.13 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Calculá, distinguiendo $x\to+\infty$ y $x\to-\infty$ cuando haga falta:

a) $\displaystyle\lim_{x\to\pm\infty}\frac{4x^2-x+1}{2-x^2}$

b) $\displaystyle\lim_{x\to\pm\infty}\frac{x^3-2x}{5x^2+1}$

c) $\displaystyle\lim_{x\to\pm\infty}\frac{3^x+2^x}{3^x-2^x}$

d) $\displaystyle\lim_{x\to\pm\infty}\frac{\sqrt{x^2+x}}{2x+1}$ (donde esté definida)
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dividir por la mayor potencia o por la exponencial dominante; con raíces, usar $\sqrt{x^2}=\lvert x\rvert$.

**Desarrollo.**

a) Mismo grado: $\frac{4}{-1}=-4$ en ambos extremos.

b) Grado $3>2$: $\frac{x^3}{5x^2}=\frac x5$. Tiende a $+\infty$ si $x\to+\infty$ y a $-\infty$ si $x\to-\infty$.

c) Si $x\to+\infty$, dividimos por $3^x$: $\frac{1+(2/3)^x}{1-(2/3)^x}\to\frac{1+0}{1-0}=1$. Si $x\to-\infty$, dividimos por $2^x$: $\frac{(3/2)^x+1}{(3/2)^x-1}$ y $(3/2)^x\to0$, por lo que el límite es $\frac{0+1}{0-1}=-1$.

d) Para $x\to+\infty$: $\sqrt{x^2+x}\approx x$ y el cociente tiende a $\frac x{2x}=\frac12$. Para $x\to-\infty$: $\sqrt{x^2+x}\approx\lvert x\rvert=-x$ y el cociente tiende a $\frac{-x}{2x}=-\frac12$.

**Resultado.** a) $-4$ y $-4$; b) $+\infty$ y $-\infty$; c) $1$ y $-1$; d) $\frac12$ y $-\frac12$.

</details>

### Ejercicio 14 · Límite en el infinito con la definición
<!-- ejercicio: U2.14 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Probá con la definición que $\displaystyle\lim_{x\to+\infty}\frac{3x+1}{x-2}=3$ y calculá $N$ para $\varepsilon=\tfrac1{10}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escribir la distancia a $L=3$ y acotarla por una expresión decreciente en $x$.

**Desarrollo.** Para $x>2$,

$$
\left\lvert\frac{3x+1}{x-2}-3\right\rvert=\left\lvert\frac{3x+1-3(x-2)}{x-2}\right\rvert=\frac{7}{x-2}.
$$

Dado $\varepsilon>0$, $\frac7{x-2}<\varepsilon\iff x-2>\frac7\varepsilon\iff x>2+\frac7\varepsilon$. Tomando $N=2+\frac7\varepsilon$, si $x>N$ entonces $x>2$ y la distancia es menor que $\varepsilon$. $\blacksquare$

Con $\varepsilon=\frac1{10}$: $N=2+70=72$. En $x=72$ la distancia vale $\frac7{70}=\frac1{10}$, justo el borde; todo $x>72$ da menos.

**Resultado.** $\lim_{x\to+\infty}\frac{3x+1}{x-2}=3$, con $N=2+\frac7\varepsilon$ ($N=72$ para $\varepsilon=\frac1{10}$).

</details>

## Autoevaluación

1. ¿Puede ser $\lim_{x\to a}f(x)=+\infty$ y a la vez que $f(a)$ exista?

<details>
<summary>Respuesta</summary>

Sí: el límite solo mira el entorno reducido. Por ejemplo $f(x)=\frac1{(x-1)^2}$ si $x\ne1$ y $f(1)=0$.

</details>

2. $\lim_{x\to+\infty}(x^2-x)$: ¿qué tipo de forma aparece al sustituir y cuánto vale?

<details>
<summary>Respuesta</summary>

Aparece $\infty-\infty$ (indeterminada), pero se factoriza $x^2(1-\frac1x)$ y el producto $(+\infty)\cdot1$ da $+\infty$.

</details>

3. ¿Qué dice la jerarquía sobre $\lim_{x\to+\infty}\frac{x^{100}}{1{,}01^{x}}$?

<details>
<summary>Respuesta</summary>

Que vale $0$: aunque $1{,}01^x$ crezca despacio al principio, a la larga gana a cualquier potencia.

</details>

:::tip[En resumen]
- $\lim_{x\to a}f=\pm\infty$: la función diverge; no es un número. El signo se decide por los laterales.
- $\lim_{x\to\pm\infty}f=L$: la gráfica se acerca a la altura $L$; $\lim_{x\to\pm\infty}f=\pm\infty$: crece sin cota.
- $\infty-\infty$, $0\cdot\infty$, $\frac00$, $\frac\infty\infty$, $1^\infty$, $0^0$, $\infty^0$ son indeterminaciones.
- Cociente de polinomios: se compara el grado; con raíces o exponenciales hay que mirar $+\infty$ y $-\infty$ por separado.
- $\ln x\ll x^p\ll a^x$ cuando $x\to+\infty$.
:::

## Para seguir

Ya podés atacar las indeterminaciones con método: [Cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/).
