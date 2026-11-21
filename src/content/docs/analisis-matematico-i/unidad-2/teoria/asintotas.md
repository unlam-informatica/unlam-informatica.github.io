---
title: Asíntotas
description: Asíntotas verticales, horizontales y oblicuas de una curva, con el comportamiento en más y menos infinito y su interpretación en modelos de saturación.
slug: analisis-matematico-i/unidad-2/teoria/asintotas
sidebar:
  order: 6
---

## Qué vas a aprender

- Hallar asíntotas verticales, horizontales y oblicuas, distinguiendo el comportamiento en $+\infty$ y en $-\infty$.
- Interpretar una asíntota en un modelo (valor límite, saturación).

**Antes de empezar.** [Límites infinitos y en el infinito](/analisis-matematico-i/unidad-2/teoria/limites-infinitos/) y [Cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/).

## Idea

Una **asíntota** es una recta de la que la curva se acerca indefinidamente. Hay tres tipos y cada uno sale de un límite.

## Asíntota vertical (AV)

:::note[Definición · Asíntota vertical]
La recta $x=a$ es **asíntota vertical** de $f$ si al menos uno de los límites laterales en $a$ es infinito:
$\lim_{x\to a^{+}}f(x)=\pm\infty$ o $\lim_{x\to a^{-}}f(x)=\pm\infty$.
:::

Los candidatos son los puntos donde el denominador se anula, los bordes abiertos del dominio (por ejemplo $\ln x$ en $0$) y los empalmes de funciones por tramos. **Hay que verificar con el límite**: un cero del denominador que también anula el numerador puede ser solo un hueco.

## Asíntota horizontal (AH)

:::note[Definición · Asíntota horizontal]
La recta $y=L$ es **asíntota horizontal** de $f$ si $\lim_{x\to+\infty}f(x)=L$ (por derecha) o $\lim_{x\to-\infty}f(x)=L$ (por izquierda), con $L$ finito.
:::

Pueden existir dos distintas, una en cada extremo: $\arctan x$ tiene $y=\frac\pi2$ en $+\infty$ e $y=-\frac\pi2$ en $-\infty$.

<!-- check: U2.T.ASI.1 -->

**Ejemplo 1.** Para $f(x)=\dfrac{2x+1}{x-1}$: en $x=1$ el numerador vale $3\neq0$ y el denominador se anula; $\lim_{x\to1^{+}}f=+\infty$ y $\lim_{x\to1^{-}}f=-\infty$, luego $x=1$ es AV. En el infinito, $\lim_{x\to\pm\infty}f=2$, luego $y=2$ es AH.

![Gráfico de (2x+1)/(x−1) con la recta vertical x = 1 y la recta horizontal y = 2](/analisis-matematico-i/figuras/u2-asintotas-vh.svg)

*Qué observar: la curva se pega a la recta $x=1$ subiendo por la derecha y bajando por la izquierda, y se aplana hacia $y=2$ en ambos extremos.*

<!-- check: U2.T.ASI.2 -->

**Ejemplo 2 (hueco, no AV).** $f(x)=\dfrac{x^2-1}{x^2-3x+2}=\dfrac{(x-1)(x+1)}{(x-1)(x-2)}$. En $x=1$ el límite es $\frac{2}{-1}=-2$ (finito): hay un hueco, **no** asíntota. En $x=2$ el numerador vale $3$ y el denominador tiende a $0$: AV. Además $\lim_{x\to\pm\infty}f=1$: AH $y=1$.

## Asíntota oblicua (AO)

:::note[Definición · Asíntota oblicua]
La recta $y=mx+n$ con $m\neq0$ es **asíntota oblicua** de $f$ en $+\infty$ si $\lim_{x\to+\infty}\bigl[f(x)-(mx+n)\bigr]=0$ (análogo en $-\infty$). Se calcula con

$$
m=\lim_{x\to\pm\infty}\frac{f(x)}{x},\qquad n=\lim_{x\to\pm\infty}\bigl[f(x)-mx\bigr],
$$

y hacen falta **ambos** límites finitos, con $m\ne0$ (si $m=0$ es una asíntota horizontal).
:::

**Por qué funciona.** Si $f(x)=mx+n+\epsilon(x)$ con $\epsilon\to0$, al dividir por $x$ queda $\frac{f}{x}=m+\frac nx+\frac{\epsilon}{x}\to m$, y después $f-mx=n+\epsilon\to n$. Recíprocamente, si ambos límites existen, $f-mx-n\to0$.

Como la AH y la AO describen el comportamiento en cada extremo, **en una misma dirección no pueden coexistir**; pero en $+\infty$ puede haber una y en $-\infty$ otra distinta.

<!-- check: U2.T.ASI.3 -->

**Ejemplo 3 (racional).** $f(x)=\dfrac{x^3+2x^2-1}{x^2+1}$: grado del numerador = grado del denominador + 1. Dividiendo, $f(x)=x+2+\dfrac{-x-3}{x^2+1}$ y el resto tiende a $0$: AO $y=x+2$ (en $\pm\infty$). Con la fórmula, $m=\lim\frac{f}{x}=1$ y $n=\lim(f-x)=2$.

<!-- check: U2.T.ASI.4 -->

**Ejemplo 4 (distintas en cada extremo).** $f(x)=\sqrt{(x+2)^2+1}$.

- $x\to+\infty$: $m=\lim\frac{f}{x}=1$ y $n=\lim\bigl(f-x\bigr)=\lim\frac{(x+2)^2+1-x^2}{f+x}=\lim\frac{4x+5}{f+x}=2$. AO $y=x+2$.
- $x\to-\infty$: $m=\lim\frac fx=-1$ (porque $f\approx\lvert x+2\rvert=-(x+2)$) y $n=\lim(f+x)=\lim\frac{4x+5}{f-x}=-2$. AO $y=-x-2$.

![Gráfico de raíz de (x+2)²+1 con las rectas y = x + 2 en +∞ e y = −x − 2 en −∞](/analisis-matematico-i/figuras/u2-asintota-oblicua.svg)

*Qué observar: a la derecha la curva se pega a $y=x+2$; a la izquierda, a $y=-x-2$. Son dos asíntotas oblicuas distintas.*

<!-- check: U2.T.ASI.5 -->

**Ejemplo 5 (asíntotas horizontales distintas).** $f(x)=\dfrac{6e^{x}}{e^{x}+2}$: $\lim_{x\to+\infty}f=6$ y $\lim_{x\to-\infty}f=0$. AH $y=6$ en $+\infty$ e $y=0$ en $-\infty$.

<!-- check: U2.T.ASI.6 -->

**Ejemplo 6 (la curva puede cortar su asíntota).** $f(x)=\dfrac{\operatorname{sen}x}{x}$ tiene AH $y=0$ y vale $0$ en $x=k\pi$: la cruza infinitas veces. Una asíntota describe el comportamiento lejano, no impide cruces.

<!-- check: U2.T.ASI.7 -->

**Ejemplo 7 (sin AO).** $f(x)=x+\operatorname{sen}x$: $m=\lim\frac fx=1$, pero $f-x=\operatorname{sen}x$ oscila y no tiene límite: no hay AO. Y $f(x)=x^2$: $m=+\infty$, no hay AO.

## Asíntotas en un modelo

Una asíntota horizontal en un modelo es un **valor límite**: aquello a lo que tiende la cantidad con el tiempo, la saturación.

<!-- check: U2.T.ASI.8 -->

**Ejemplo 8.** La concentración de un fármaco en sangre, en mg/L, es $C(t)=\dfrac{12t}{t+3}$ para $t\ge0$ (horas). Como $\lim_{t\to+\infty}C=12$, la recta $C=12$ es AH: la concentración se estabiliza en $12$ mg/L sin alcanzarla nunca ($C<12$ siempre, pues $12t<12(t+3)$). Llega a la mitad, $6$, cuando $\frac{12t}{t+3}=6\iff t=3$ h.

:::caution[Errores frecuentes]
- **Declarar AV todo punto fuera del dominio.** Si el límite es finito es un hueco ($\frac{\operatorname{sen}x}{x}$ en $0$).
- **Calcular solo $x\to+\infty$.** Con raíces, módulos y exponenciales los dos extremos difieren.
- **Dar $m$ sin calcular $n$,** o aceptar $n$ cuando el límite no existe ($x+\operatorname{sen}x$).
- **Creer que la curva no puede tocar su asíntota.**
- **Decir que hay AH y AO en el mismo extremo.**
:::

## Ejercicios

### Ejercicio 19 · Asíntotas de una racional
<!-- ejercicio: U2.19 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallá todas las asíntotas de $f(x)=\dfrac{3x^2-2}{x^2-x-2}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Factorizar el denominador, estudiar cada cero y el límite en el infinito.

**Desarrollo.** $x^2-x-2=(x-2)(x+1)$. En $x=2$ el numerador vale $10\ne0$ y en $x=-1$ vale $1\ne0$: ambos son AV (los laterales divergen). Mismo grado: $\lim_{x\to\pm\infty}f=3$.

**Resultado.** AV $x=2$ y $x=-1$; AH $y=3$.

</details>

### Ejercicio 20 · Oblicuas
<!-- ejercicio: U2.20 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallá las asíntotas de a) $f(x)=\dfrac{x^2+2x-3}{x-2}$ y b) $g(x)=\sqrt{4x^2+3x}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** División de polinomios en a); en b), fórmulas de $m$ y $n$ en cada extremo.

**Desarrollo.**

a) En $x=2$ el numerador vale $5$: AV. $x^2+2x-3=(x-2)(x+4)+5$, así que $f=x+4+\frac5{x-2}$: AO $y=x+4$.

b) Dominio $x\le-\frac34$ o $x\ge0$. En $+\infty$: $m=2$; $n=\lim(\sqrt{4x^2+3x}-2x)=\lim\frac{3x}{\sqrt{4x^2+3x}+2x}=\frac34$. AO $y=2x+\frac34$. En $-\infty$: $m=-2$; $n=\lim(\sqrt{4x^2+3x}+2x)=\lim\frac{3x}{\sqrt{4x^2+3x}-2x}=-\frac34$. AO $y=-2x-\frac34$. No hay AV.

**Resultado.** a) AV $x=2$, AO $y=x+4$; b) AO $y=2x+\frac34$ en $+\infty$ e $y=-2x-\frac34$ en $-\infty$.

</details>

### Ejercicio 21 · Modelo de saturación
<!-- ejercicio: U2.21 | nivel: intermedio | tipo: modelado | verificacion: sympy -->

:::note[Enunciado]
El número de usuarios (en miles) de una aplicación es $N(t)=\dfrac{800}{1+15e^{-0{,}4t}}$, con $t$ en meses.

a) ¿Cuántos usuarios hay al inicio? b) ¿Hacia qué valor tiende $N$? c) ¿Cuándo llega a la mitad de ese valor?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Evaluar en $0$, calcular el límite en $+\infty$ y resolver una ecuación.

**Desarrollo.** a) $N(0)=\frac{800}{16}=50$ (mil). b) $e^{-0{,}4t}\to0$, entonces $N\to800$: AH $N=800$. c) $N=400\iff1+15e^{-0{,}4t}=2\iff e^{-0{,}4t}=\frac1{15}\iff t=\frac{\ln15}{0{,}4}\approx6{,}77$ meses.

**Resultado.** $50$ mil; $800$ mil (saturación); $t=\frac{\ln 15}{0{,}4}\approx6{,}77$ meses.

</details>

### Ejercicio 22 · Parámetros
<!-- ejercicio: U2.22 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallá $a$ y $b$ para que $f(x)=\dfrac{ax^2+3}{x-b}$ tenga asíntota oblicua $y=2x+8$, y dá su asíntota vertical.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dividir y comparar con la recta.

**Desarrollo.** $ax^2+3=(x-b)(ax+ab)+ab^2+3$, luego $f=ax+ab+\frac{ab^2+3}{x-b}$: AO $y=ax+ab$. Igualando con $2x+8$: $a=2$ y $ab=8$, o sea $b=4$. Entonces $ab^2+3=35\ne0$ y $x=4$ es AV.

**Resultado.** $a=2$, $b=4$; AV $x=4$.

</details>

## Autoevaluación

1. ¿$x=0$ es AV de $\frac{\operatorname{sen}x}{x}$?

<details>
<summary>Respuesta</summary>

No: el límite es $1$.

</details>

2. ¿Puede una función tener AH $y=1$ en $+\infty$ y AO en $-\infty$?

<details>
<summary>Respuesta</summary>

Sí: cada extremo se estudia por separado. Por ejemplo, $f(x)=1+\dfrac{x}{1+e^{x}}$. Si $x\to+\infty$, $\dfrac{x}{1+e^{x}}\to0$ (la exponencial domina), así que hay AH $y=1$. Si $x\to-\infty$, $e^{x}\to0$: $m=\lim\frac{f(x)}{x}=1$ y $f(x)-(x+1)=\dfrac{x}{1+e^{x}}-x=-\dfrac{xe^{x}}{1+e^{x}}\to0$, así que hay AO $y=x+1$.

</details>

3. ¿Puede el gráfico de una función cortar a su asíntota horizontal? ¿Y a una asíntota vertical?

<details>
<summary>Respuesta</summary>

A la horizontal, sí: la AH describe el comportamiento en el extremo, no prohíbe valores cerca del origen; por ejemplo $\dfrac{\operatorname{sen}x}{x}$ toma el valor $0$ infinitas veces y tiene AH $y=0$. A una vertical $x=a$ el gráfico la corta como mucho en un punto, si $f(a)$ está definido (como en una función por tramos), pero cerca de $a$ la función no está acotada.

</details>

:::tip[En resumen]
- AV $x=a$: algún lateral en $a$ es infinito.
- AH $y=L$: $\lim_{x\to\pm\infty}f=L$, por extremo.
- AO $y=mx+n$: $m=\lim\frac fx\ne0$ y $n=\lim(f-mx)$ finitos; por extremo.
- Una asíntota horizontal en un modelo es el valor de saturación.
:::

## Para seguir

[Continuidad](/analisis-matematico-i/unidad-2/teoria/continuidad/): cuándo la curva no tiene cortes, y qué tipo de corte aparece cuando los hay.
