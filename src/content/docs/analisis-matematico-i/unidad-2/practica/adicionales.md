---
title: Ejercicios adicionales
slug: analisis-matematico-i/unidad-2/practica/adicionales
sidebar:
  order: 34
---


Los enunciados se transcriben de la Guía de Trabajos Prácticos 2026, a partir de la página del PDF renderizada. La guía **no publica respuestas** para los ejercicios adicionales: los resultados de esta página se verificaron con SymPy y no se contrastan con una respuesta oficial.

### Adicional 1 — Verdadero / Falso

**a)** $\lim_{x\to-3}\dfrac{\sqrt{x+7}-2}{\operatorname{sen}(2x+6)}=\dfrac12$.

Racionalizamos el numerador y usamos $\operatorname{sen}(2x+6)=\operatorname{sen}\big(2(x+3)\big)\sim 2(x+3)$:



$$
\sqrt{x+7}-2=\dfrac{(x+7)-4}{\sqrt{x+7}+2}=\dfrac{x+3}{\sqrt{x+7}+2}
$$





$$
\dfrac{\frac{x+3}{\sqrt{x+7}+2}}{\operatorname{sen}2(x+3)}=\dfrac{x+3}{(\sqrt{x+7}+2)\cdot\operatorname{sen}2(x+3)}
$$



Con $\operatorname{sen}2(x+3)\sim 2(x+3)$:



$$
\to\dfrac{x+3}{(\sqrt{x+7}+2)\cdot 2(x+3)}=\dfrac{1}{2(\sqrt{x+7}+2)}\xrightarrow{x\to-3}\dfrac{1}{2(2+2)}=\dfrac{1}{8}
$$



El valor es $\dfrac18\neq\dfrac12$ $\Rightarrow$ **Falsa**. (Resultado correcto: $\dfrac{1}{8}$.)

**b)** $\lim_{x\to1}\dfrac{1-\cos(x-1)}{x^2-1}=\dfrac12$.

$1-\cos(x-1)\sim \dfrac{(x-1)^2}{2}$ y $x^2-1=(x-1)(x+1)$:



$$
\dfrac{(x-1)^2/2}{(x-1)(x+1)}=\dfrac{x-1}{2(x+1)}\xrightarrow{x\to1}\dfrac{0}{4}=0
$$



El valor es $0\neq\dfrac12$ $\Rightarrow$ **Falsa**. (Resultado correcto: $0$.)

**c)** $\lim_{x\to\infty}\dfrac{\sqrt{x^2+5}}{3x-2}$ no existe.

Dividiendo por $\lvert x\rvert=\sqrt{x^2}$: si $x\to+\infty$, $\lvert x\rvert=x$ y el cociente tiende a $\dfrac{1}{3}$; si $x\to-\infty$, $\lvert x\rvert=-x$ y tiende a $-\dfrac{1}{3}$. **Verdadera**, si «$x\to\infty$» se lee como $x\to\pm\infty$ (sin signo): los límites en $+\infty$ y en $-\infty$ existen pero son distintos, así que no hay un único límite. Si se pidiera solo $x\to+\infty$, el límite existiría y valdría $\dfrac13$.

<div id="adicional-2--geogebra-asíntotas-de-dfracax2xbx2-1" aria-hidden="true"></div>

### Adicional 2 — Asíntotas de $f(x)=\dfrac{ax^2+x}{bx^2-1}$ con GeoGebra

:::note[Enunciado]
Estudiar, usando GeoGebra, las asíntotas de $f:D_f\to\mathbb{R}\,/\,f(x)=\dfrac{ax^2+x}{bx^2-1}$, siendo $a\in\mathbb{R}$, $a\neq0$ y $b\in\mathbb{R}$. Luego responder:

a) Analizar, utilizando GeoGebra, las posibles asíntotas de $f$ al variar los valores de $a$ y $b$. Explicar en un breve párrafo los pasos realizados.

b) ¿Para qué valores de $b$ la función tiene dos asíntotas verticales? ¿Existen valores de $b$ para los cuales tiene sólo una asíntota vertical? ¿Y ninguna? Justificar la respuesta.

c) Tomar un valor de $a$ y otro de $b$ para el cual tenga dos asíntotas verticales. Escribir las ecuaciones de todas las asíntotas de la función elegida. Justificar la respuesta utilizando límite.
:::

Es el mismo planteo que el [ejercicio 25 c)](/analisis-matematico-i/unidad-2/practica/ejercicio-25/).

**a)** En GeoGebra se crean dos deslizadores, `a` y `b`, y se define `f(x) = (a x^2 + x) / (b x^2 - 1)`. Al mover `b` se observa:
- si $b>0$, aparecen dos rectas verticales y la curva se aplana hacia una altura;
- si $b<0$, la curva se aplana sin rectas verticales;
- si $b=0$, la curva es una parábola.

Cada observación se confirma con límites en los incisos siguientes.

**b)** El numerador es $x(ax+1)$ y el denominador se anula si $bx^2=1$.

- **$b\le0$: ninguna AV.** Si $b<0$, $bx^2-1<0$ para todo $x$. Si $b=0$, el denominador vale $-1$ y $f(x)=-ax^2-x$ es una parábola, sin asíntotas.
- **$b>0$ y $b\neq a^2$: dos AV**, en $x=\pm\frac{1}{\sqrt b}$. El numerador solo se anula en $x=0$ y $x=-\frac1a$. Que $-\frac1a$ coincida con $\pm\frac1{\sqrt b}$ equivale a $b=a^2$, así que en este caso el numerador no se anula en las raíces del denominador y el cociente diverge en las dos.
- **$b=a^2$: una sola AV.** Con $b=a^2$ el denominador es $(ax-1)(ax+1)$ y
$$
f(x)=\frac{x(ax+1)}{(ax-1)(ax+1)}=\frac{x}{ax-1}\qquad(x\neq-\tfrac1a).
$$
En $x=-\frac1a$ el límite es finito, $\frac{1}{2a}$: es una discontinuidad evitable, no una asíntota. La única AV es $x=\frac1a$.

:::caution[Diferencia con la respuesta oficial del ejercicio 25]
La respuesta oficial del ejercicio 25 c) dice que «no existe valor de $b$ para el cual tenga una sola AV». El caso $b=a^2$ muestra que sí existe. Por ejemplo, con $a=1$ y $b=1$, $f(x)=\frac{x}{x-1}$ para $x\neq-1$, con una única AV $x=1$.
:::

**c)** Con $a=1$ y $b=4$ (vale $b>0$ y $b\neq a^2$): $f(x)=\dfrac{x^2+x}{4x^2-1}$.
- **AV $x=\frac12$:** el numerador tiende a $\frac34\neq0$ y el denominador a $0$, así que $\lim_{x\to\frac12^{-}}f=-\infty$ y $\lim_{x\to\frac12^{+}}f=+\infty$.
- **AV $x=-\frac12$:** el numerador tiende a $-\frac14$, así que $\lim_{x\to-\frac12^{-}}f=-\infty$ y $\lim_{x\to-\frac12^{+}}f=+\infty$.
- **AH $y=\frac14$:** $\lim_{x\to\pm\infty}f=\frac14$, por el cociente de los coeficientes principales.
- **Sin AO:** hay AH en los dos extremos.


### Adicional 3 — $f(x)=\dfrac{\lvert 4-x^2\rvert}{x(x-2)}$

**Dominio:** $x(x-2)\neq0\Rightarrow x\neq0,\ x\neq2$, es decir $D=\mathbb{R}-\lbrace 0,2\rbrace $.

Separamos el módulo: $4-x^2\ge0\Leftrightarrow -2\le x\le2$.

- **Si $-2\le x\le2$:** $\lvert4-x^2\rvert=4-x^2=(2-x)(2+x)$. Entonces $f(x)=\dfrac{(2-x)(2+x)}{x(x-2)}=\dfrac{-(x-2)(x+2)}{x(x-2)}=\dfrac{-(x+2)}{x}$.
- **Si $x<-2$ o $x>2$:** $\lvert4-x^2\rvert=x^2-4=(x-2)(x+2)$. Entonces $f(x)=\dfrac{(x-2)(x+2)}{x(x-2)}=\dfrac{x+2}{x}$.

**Discontinuidades:**

- **$x=2$:** lateral izquierdo (rama $-\tfrac{x+2}{x}$): $\to-\dfrac{4}{2}=-2$; lateral derecho (rama $\tfrac{x+2}{x}$): $\to\dfrac{4}{2}=2$. Salto finito $\Rightarrow$ **esencial de salto finito** ($S=4$).
- **$x=0$:** está en la rama $-\tfrac{x+2}{x}$, $\to-\dfrac{2}{0}\to\pm\infty$ $\Rightarrow$ **esencial de salto infinito** (AV $x=0$).

**Asíntotas:**

- **AV:** $x=0$ (no $x=2$, que es salto finito).
- **AH:** $x\to+\infty$ usa $\dfrac{x+2}{x}\to1\Rightarrow y=1$; $x\to-\infty$ usa $\dfrac{x+2}{x}\to1\Rightarrow y=1$. AH $y=1$.



$$
\boxed{D=\mathbb{R}-\lbrace 0,2\rbrace ;\ \text{AV }x=0,\ \text{AH }y=1;\ x=2\ \text{salto finito},\ x=0\ \text{salto infinito}.}
$$



Dominio: $\mathbb{R}-\lbrace 0,2\rbrace$.

<div id="adicional-4--opción-múltiple-función-por-tramos-continua" aria-hidden="true"></div>

### Adicional 4 — Parámetros para la continuidad (opción múltiple)

:::note[Enunciado]
Sea $m:D_m\to\mathbb{R}\,/\,m(x)=\begin{cases} e^{\frac{1}{3-x}} & \text{si } x>3\\ ax+b & \text{si } 1\le x\le3\\ \dfrac{x^2+4x-5}{2x^2-6x+4} & \text{si } x<1\end{cases}$. Los valores de $a$ y $b$ que hacen que $m$ sea continua en $\mathbb{R}$ son:

a) $a=\frac32$; $b=-\frac92$. b) $a=\frac32$; $b=\frac92$. c) $a=-\frac32$; $b=-\frac92$. d) Ninguna de las anteriores.
:::

Cada tramo es continuo en su intervalo abierto. El denominador $2x^2-6x+4=2(x-1)(x-2)$ se anula en $1$ y en $2$, que no son menores que $1$. Falta imponer la continuidad en los empalmes.

- **En $x=3$:** $m(3)=3a+b$. Por derecha, $\frac{1}{3-x}\to-\infty$, así que $e^{\frac{1}{3-x}}\to0$. Por izquierda el tramo lineal da $3a+b$. Condición: $3a+b=0$.
- **En $x=1$:** $m(1)=a+b$. Por izquierda, $\dfrac{(x+5)(x-1)}{2(x-1)(x-2)}=\dfrac{x+5}{2(x-2)}\to\dfrac{6}{-2}=-3$. Condición: $a+b=-3$.

Restando, $2a=3$, de donde $a=\frac32$ y $b=-\frac92$.

$$
\boxed{\text{Opción a): } a=\tfrac32,\ b=-\tfrac92.}
$$


<div id="adicional-5--opción-límites-laterales" aria-hidden="true"></div>

### Adicional 5 — Límites laterales (opción múltiple)

:::note[Enunciado]
Sea $f$ una función tal que $\lim\limits_{x\to x_0^-}f(x)=L\in\mathbb{R}$ y se sabe que existe el límite finito de $f$ para $x$ tendiendo a $x_0$. Entonces:

a) $\dfrac{\lim_{x\to x_0^+}f(x)}{\lim_{x\to x_0^-}f(x)}=1$  b) $\lim\limits_{x\to x_0^+}f(x)+\lim\limits_{x\to x_0^-}f(x)=2L$  c) $f(x_0)+\lim\limits_{x\to x_0}f(x)=2L$  d) $\dfrac{f(x_0)}{\lim_{x\to x_0^-}f(x)}=1$
:::

Si el límite existe, los dos laterales existen y valen lo mismo: $\lim_{x\to x_0^+}f=\lim_{x\to x_0^-}f=\lim_{x\to x_0}f=L$.

- **a)** No vale si $L=0$: el cociente no está definido. Contraejemplo: $f(x)=x$, $x_0=0$.
- **b)** Siempre vale: $L+L=2L$. **Es la correcta.**
- **c)** Exige $f(x_0)=L$, es decir, continuidad, que no es dato. Contraejemplo: $f(x)=x$ para $x\neq0$ y $f(0)=5$, con $x_0=0$. Da $5+0\neq0$.
- **d)** Falla por la misma razón, y además si $L=0$ o si $f(x_0)$ no existe.

$$
\boxed{\text{Opción b).}}
$$


<div id="adicional-6--llim_xto-adfracxsqrtx-asqrtasqrtx-sqrta" aria-hidden="true"></div>

### Adicional 6 — $L=\lim_{x\to a}\dfrac{x\sqrt{x}-a\sqrt{a}}{\sqrt{x}-\sqrt{a}}$ (opción múltiple)

:::note[Enunciado]
Dado el siguiente límite $L=\lim\limits_{x\to a}\dfrac{x\sqrt{x}-a\sqrt{a}}{\sqrt{x}-\sqrt{a}}$, se verifica:

a) $L=3a\ \ \forall a\in\mathbb{R}$  b) $L\ \ \forall a\ge0$  c) $L=3\sqrt a\ \ \forall a\ge0$  d) $L=3a\ \ \forall a\ge0$  e) No existe $L\ \ \forall a\ge0$

(La opción b) aparece así en la guía, incompleta.)
:::

Escribimos $x\sqrt{x}=(\sqrt{x})^3$ y $a\sqrt{a}=(\sqrt{a})^3$. Con $u=\sqrt{x}$, $v=\sqrt{a}$ es una diferencia de cubos:



$$
\dfrac{u^3-v^3}{u-v}=u^2+uv+v^2
$$



Volviendo a las variables: $u^2+uv+v^2=x+\sqrt{x}\sqrt{a}+a\xrightarrow{x\to a}a+a+a=3a$.



La expresión solo está definida para $x\ge0$ (y $x\neq a$), así que $a<0$ queda descartado. Para $a=0$ el cociente vale $x$ y el límite, que es lateral por derecha por el dominio, da $0=3\cdot0$.

$$
\boxed{L=3a\ \ \forall a\ge0:\ \text{opción d).}}
$$

<div id="adicional-7--opción-asíntotas-de-gxdfracax3cx2-x3x2-x" aria-hidden="true"></div>

### Adicional 7 — Asíntotas de $g(x)=\dfrac{ax^3+cx^2-x}{3x^2-x}$ (opción múltiple)

:::note[Enunciado]
Sea la función $g(x)=\dfrac{ax^3+cx^2-x}{3x^2-x}$ con $a,c\in\mathbb{R}$; entonces:

a) Para todo valor de $a$ y $c$, $f$ tiene una asíntota vertical en $x=\frac13$ y en $x=0$.

b) No existe valor de $a$ y $c$ para que $f$ tenga asíntota oblicua.

c) $\forall a$ la función $g(x)$ tiene una asíntota oblicua y tiene asíntota vertical que varía según el valor de $c$.

d) Si $a=0$, $f$ tiene una asíntota horizontal para cualquier valor de $c$. En este caso, $f$ tiene una asíntota vertical en $x=\frac13$ siempre que $c\neq3$.

e) Si $a=0$, $f$ tiene una asíntota horizontal para cualquier valor de $c$. En este caso, $f$ tiene una asíntota vertical en $x=\frac13$.

(Las opciones nombran $f$ a la función $g$, como en la guía.)
:::

Se simplifica el factor $x$: $g(x)=\dfrac{x(ax^2+cx-1)}{x(3x-1)}=\dfrac{ax^2+cx-1}{3x-1}$, con $x\neq0$ y $x\neq\frac13$.

- **a)** Falsa. En $x=0$ el límite es $\frac{-1}{-1}=1$, finito: hay un hueco, no una AV.
- **b)** Falsa. Si $a\neq0$, el numerador simplificado tiene grado $2$ y el denominador grado $1$, así que hay AO de pendiente $\frac a3$.
- **c)** Falsa. Si $a=0$ no hay AO, y la única AV posible está siempre en $x=\frac13$: lo que depende de $c$ es si existe, no dónde está.
- **d)** Verdadera. Con $a=0$, $g(x)=\dfrac{cx-1}{3x-1}$ y $\lim_{x\to\pm\infty}g=\frac c3$: hay AH para todo $c$. En $x=\frac13$ el numerador vale $\frac c3-1$. Si $c\neq3$ es no nulo y hay AV. Si $c=3$, $g(x)=1$ para $x\neq0,\frac13$ y en $\frac13$ hay un hueco.
- **e)** Falsa por el caso $c=3$.

$$
\boxed{\text{Opción d).}}
$$

