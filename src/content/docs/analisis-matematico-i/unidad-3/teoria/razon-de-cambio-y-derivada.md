---
title: Razón de cambio y derivada
description: Razón de cambio media e instantánea, derivada en un punto como límite del cociente incremental, recta tangente y normal y problemas de tangencia.
slug: analisis-matematico-i/unidad-3/teoria/razon-de-cambio-y-derivada
sidebar:
  order: 1
---

## Qué vas a aprender

- Calcular la razón de cambio media de una magnitud en un intervalo y la razón de cambio instantánea como límite, indicando siempre las unidades.
- Definir la derivada de $f$ en un punto con el cociente incremental, e interpretarla como pendiente de la recta tangente y como velocidad instantánea.
- Escribir las ecuaciones de las rectas tangente y normal.
- Resolver problemas de tangencia: pendiente dada, rectas paralelas o perpendiculares a otra, tangentes que pasan por un punto exterior y parámetros desconocidos.

**Antes de empezar.** Necesitás calcular [límites con la forma $\frac{0}{0}$](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/), conocer la ecuación de la recta (pendiente, rectas paralelas y perpendiculares) y haber trabajado con [modelos funcionales](/analisis-matematico-i/unidad-1/teoria/funciones-y-modelos/).

## Introducción: ¿qué tan rápido cambia?

Un tren recorre $s(t)$ kilómetros durante las primeras $t$ horas de viaje. El velocímetro no mide una distancia dividida por un tiempo: marca *la velocidad en este instante*. Pero la única herramienta que tenemos para medir velocidades es el cociente entre una distancia y un tiempo, que siempre abarca un intervalo.

La salida es la que ya conocemos de la Unidad 2: calcular ese cociente en intervalos cada vez más cortos y mirar a qué valor se acerca. Ese límite es la **derivada**. El mismo cálculo responde una pregunta geométrica: ¿qué pendiente tiene la recta que «toca» a una curva en un punto? Y una pregunta de modelado: ¿a qué ritmo crece una población, se enfría una pieza o se llena un tanque *en este momento*?

## Razón de cambio media

:::note[Definición · Razón de cambio media]
Sea $f$ definida en $[a, b]$. La **razón de cambio media** (o **tasa media de variación**) de $f$ entre $a$ y $b$ es

$$
\dfrac{\Delta f}{\Delta x} = \dfrac{f(b) - f(a)}{b - a}.
$$

Si $x$ se mide en la unidad $[x]$ y $f$ en la unidad $[f]$, la razón se mide en $[f]/[x]$.
:::

Si $f$ es la posición, es la **velocidad media**; si es el volumen de un tanque en litros y $t$ el tiempo en minutos, es un caudal medio en l/min. El signo informa el sentido del cambio: positivo si $f$ crece en promedio y negativo si decrece.

**Interpretación geométrica.** El cociente $\frac{f(b)-f(a)}{b-a}$ es la pendiente de la **recta secante** que une los puntos $(a, f(a))$ y $(b, f(b))$ del gráfico.

### Ejemplo 1 · Velocidad media de un tren
<!-- check: U3.T.RAZ.1 -->

Un tren se aleja de la estación según $s(t) = 2t^2 + t$ kilómetros, con $t$ en horas. Calculemos su velocidad media entre $t = 1$ y $t = 3$ y, en general, en el intervalo $[1, 1+h]$.

Como $s(1) = 3$ y $s(3) = 21$,

$$
\dfrac{s(3) - s(1)}{3 - 1} = \dfrac{21 - 3}{2} = 9 \ \text{km/h}.
$$

Para $[1, 1+h]$ con $h > 0$: $s(1+h) = 2(1 + 2h + h^2) + 1 + h = 3 + 5h + 2h^2$, de modo que

$$
\dfrac{s(1+h) - s(1)}{h} = \dfrac{5h + 2h^2}{h} = 5 + 2h.
$$

Con $h = 2$ obtenemos $9$ km/h, el valor anterior. Con $h = 1$, $h = 0{,}1$ y $h = 0{,}01$ resultan $7$, $5{,}2$ y $5{,}02$ km/h: las velocidades medias se acercan a $5$ km/h a medida que el intervalo se acorta.

## Razón de cambio instantánea y derivada

El ejemplo anterior sugiere la definición central de la unidad.

:::note[Definición · Derivada en un punto]
Sea $f$ definida en un entorno de $a$. La **derivada de $f$ en $a$** es

$$
f'(a) = \lim_{h \to 0} \dfrac{f(a + h) - f(a)}{h} = \lim_{x \to a} \dfrac{f(x) - f(a)}{x - a},
$$

siempre que el límite **exista y sea finito**. En ese caso decimos que $f$ es **derivable** en $a$. El cociente se llama **cociente incremental**.
:::

Las dos expresiones del límite son equivalentes (se pasa de una a otra con $x = a + h$). La primera suele ser cómoda para funciones concretas; la segunda, para demostraciones y cuando el punto de cambio es un tramo.

La derivada es la **razón de cambio instantánea**: el límite de las razones de cambio medias cuando el intervalo se contrae al punto $a$. Se escribe también $\dfrac{df}{dx}\Big|_{x=a}$ o, si $y = f(x)$, $\dfrac{dy}{dx}\Big|_{x=a}$. La unidad de $f'(a)$ es $[f]/[x]$, igual que la de la razón media.

### Ejemplo 2 · Velocidad instantánea del tren
<!-- check: U3.T.RAZ.2 -->

Con $s(t) = 2t^2 + t$, la velocidad instantánea en $t = 1$ es

$$
s'(1) = \lim_{h \to 0} \dfrac{s(1+h) - s(1)}{h} = \lim_{h \to 0} (5 + 2h) = 5 \ \text{km/h}.
$$

El resultado de las velocidades medias del Ejemplo 1 ($7$; $5{,}2$; $5{,}02$) era una señal de este límite.

### Ejemplo 3 · Derivada por definición con una raíz
<!-- check: U3.T.DER.1 -->

Calculemos $f'(1)$ para $f(x) = \sqrt{x + 3}$. Es $f(1) = 2$ y

$$
\dfrac{f(1+h) - f(1)}{h} = \dfrac{\sqrt{4 + h} - 2}{h}.
$$

Al sustituir $h = 0$ se obtiene la forma $\frac{0}{0}$. Racionalizamos multiplicando y dividiendo por el conjugado:

$$
\dfrac{\sqrt{4 + h} - 2}{h} \cdot \dfrac{\sqrt{4 + h} + 2}{\sqrt{4 + h} + 2} = \dfrac{(4 + h) - 4}{h\,(\sqrt{4 + h} + 2)} = \dfrac{1}{\sqrt{4 + h} + 2}.
$$

Para $h \neq 0$ la expresión coincide con el cociente, así que $f'(1) = \lim_{h \to 0} \dfrac{1}{\sqrt{4 + h} + 2} = \dfrac{1}{4}$.

## Interpretación geométrica: la tangente como límite de secantes

Fijemos el punto $P(a, f(a))$ y tomemos otro punto $Q(a + h, f(a + h))$ del gráfico. La secante $PQ$ tiene pendiente igual al cociente incremental. Cuando $h \to 0$, $Q$ se acerca a $P$ y las secantes giran hasta una posición límite: la **recta tangente** en $P$. Su pendiente es el límite de las pendientes, es decir, $f'(a)$.

![Tres rectas secantes a la parábola y = x² por el punto (1,1) que se acercan a la recta tangente de pendiente 2](/analisis-matematico-i/figuras/u3-secantes.svg)

*Observá cómo las pendientes $4$, $3$ y $2{,}5$ de las secantes decrecen hacia $2$, la pendiente de la tangente, a medida que el segundo punto se acerca a $(1, 1)$.*

:::note[Definición · Recta tangente]
Si $f$ es derivable en $a$, la **recta tangente** al gráfico de $f$ en $(a, f(a))$ es la recta que pasa por ese punto con pendiente $f'(a)$:

$$
y = f(a) + f'(a)\,(x - a).
$$
:::

Si el cociente incremental tiende a $+\infty$ o a $-\infty$ (la función es continua en $a$), las secantes tienden a la recta vertical $x = a$, que se llama **tangente vertical**; en ese caso $f$ **no** es derivable en $a$, porque el límite no es finito. Lo veremos en [la derivada como función](/analisis-matematico-i/unidad-3/teoria/derivada-como-funcion/).

Cerca del punto de tangencia, la curva y su tangente casi no se distinguen: para $x$ próximo a $a$ vale $f(x) \approx f(a) + f'(a)(x - a)$. La tangente es la recta que **mejor aproxima** a $f$ cerca de $a$; esa idea se precisa y se extiende a polinomios de mayor grado en la [Unidad 4](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/).

## Recta normal

:::note[Definición · Recta normal]
La **recta normal** al gráfico de $f$ en $(a, f(a))$ es la recta perpendicular a la tangente que pasa por ese punto. Si $f'(a) \neq 0$ su pendiente es $-\dfrac{1}{f'(a)}$ y

$$
y = f(a) - \dfrac{1}{f'(a)}\,(x - a).
$$

Si $f'(a) = 0$, la tangente es horizontal y la normal es la recta vertical $x = a$.
:::

Dos rectas no verticales son perpendiculares si el producto de sus pendientes es $-1$. Esa es la razón del signo y del inverso en la pendiente de la normal.

![Gráfico de y = x²/2 con su tangente de pendiente 2 y su normal de pendiente −1/2 en el punto (2,2)](/analisis-matematico-i/figuras/u3-tangente-normal.svg)

*Los dos ejes tienen la misma escala, por eso se ve el ángulo recto entre la tangente (pendiente $2$) y la normal (pendiente $-\tfrac12$).*

### Ejemplo 4 · Tangente y normal
<!-- check: U3.T.DER.2 -->

Sigamos con $f(x) = \sqrt{x + 3}$ en $a = 1$, donde $f(1) = 2$ y $f'(1) = \frac14$ (Ejemplo 3). La tangente es

$$
y = 2 + \dfrac{1}{4}(x - 1) = \dfrac{x}{4} + \dfrac{7}{4}.
$$

La pendiente de la normal es $-\dfrac{1}{1/4} = -4$ y su ecuación es

$$
y = 2 - 4(x - 1) = -4x + 6.
$$

Comprobación: ambas pasan por $(1, 2)$ y el producto de las pendientes es $\frac14 \cdot (-4) = -1$.

## Problemas de tangencia

Casi todos se resuelven con una idea: **escribir lo que se pide como condiciones sobre el punto de tangencia $(a, f(a))$**, que casi siempre es la incógnita.

En los ejemplos y ejercicios de esta lección derivamos polinomios con $(c)' = 0$ y $(x^n)' = n\,x^{n-1}$. Son resultados que todavía no demostramos: en [reglas de derivación](/analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion/) se deducen de la definición. Mientras tanto, podés comprobar cada uno armando el cociente incremental, como en el Ejemplo 1.

1. **Pendiente dada $m$.** Se resuelve $f'(a) = m$. Una recta *paralela* a otra de pendiente $m$ exige esa misma pendiente; una *perpendicular* exige $f'(a) = -\frac{1}{m}$.
2. **Tangente que pasa por un punto $(p, q)$ exterior.** El punto no es de tangencia. Se plantea $q = f(a) + f'(a)(p - a)$, una ecuación en $a$. Cada solución es una tangente.
3. **Parámetros.** Si la tangente en $x = a$ es una recta dada, se imponen dos condiciones: $f(a)$ coincide con el valor de la recta y $f'(a)$ con su pendiente.

### Ejemplo 5 · Tangentes perpendiculares a una recta dada
<!-- check: U3.T.DER.3 -->

Hallemos las tangentes a $f(x) = x^3 - 3x$ perpendiculares a la recta $y = -\frac{x}{6} + 1$.

La recta tiene pendiente $-\frac16$; las tangentes pedidas tienen pendiente $6$. Como $f'(x) = 3x^2 - 3$:

$$
3x^2 - 3 = 6 \iff x^2 = 3 \iff x = \pm\sqrt{3}.
$$

En ambos puntos $f(\pm\sqrt{3}) = \pm 3\sqrt{3} \mp 3\sqrt{3} = 0$. Las tangentes son

$$
y = 6\,(x - \sqrt{3}) \qquad \text{y} \qquad y = 6\,(x + \sqrt{3}).
$$

### Ejemplo 6 · Tangentes que pasan por un punto exterior
<!-- check: U3.T.DER.4 -->

Hallemos las rectas tangentes a $f(x) = x^2$ que pasan por $(1, -3)$. Este punto no está en la parábola, porque $f(1) = 1 \neq -3$.

La tangente en $x = a$ es $y = a^2 + 2a(x - a)$. Pasa por $(1, -3)$ si

$$
-3 = a^2 + 2a(1 - a) = 2a - a^2 \iff a^2 - 2a - 3 = 0 \iff (a - 3)(a + 1) = 0.
$$

Hay dos tangentes. Para $a = 3$: $y = 9 + 6(x - 3) = 6x - 9$. Para $a = -1$: $y = 1 - 2(x + 1) = -2x - 1$. Verificamos que ambas contienen a $(1, -3)$: $6 - 9 = -3$ y $-2 - 1 = -3$.

### Ejemplo 7 · Parámetros para que una recta sea tangente
<!-- check: U3.T.DER.5 -->

¿Para qué $a$ y $b$ la recta $y = 5x - 4$ es tangente a $f(x) = ax^2 + bx$ en $x = 1$?

Condiciones: $f(1) = 5 \cdot 1 - 4 = 1$ y $f'(1) = 5$. Como $f'(x) = 2ax + b$:

$$
\begin{cases} a + b = 1 \\ 2a + b = 5 \end{cases} \implies a = 4,\ b = -3.
$$

## Contenido complementario

:::note[Contenido complementario]
**Diferencial.** Los apuntes de la cátedra introducen, además, el *diferencial* $dy = f'(a)\,dx$ de una función derivable. No forma parte del programa de la materia, pero ayuda a leer $\frac{dy}{dx}$ como un cociente y a estimar valores: si $dx = h$ es pequeño, $f(a + h) \approx f(a) + f'(a)\,h$, que es la altura de la recta tangente en $a + h$. Por ejemplo, para $f(x) = \sqrt{x}$ en $a = 4$ (con $f'(4) = \frac14$):

<!-- check: U3.T.DER.6 -->

$$
\sqrt{4{,}1} \approx 2 + \dfrac{1}{4} \cdot 0{,}1 = 2{,}025.
$$

El valor exacto es $2{,}02484\ldots$: la aproximación es buena porque el incremento es chico. Retomaremos esta idea con error acotado en la [Unidad 4](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/).
:::

:::caution[Errores frecuentes]
- **Olvidar las unidades.** Una razón de cambio sin unidades no dice nada: «$-10$» no es una respuesta; «$-10$ °C por minuto» sí.
- **Confundir razón media con instantánea.** La media usa dos puntos distintos; la instantánea, un límite.
- **Escribir $\frac{0}{0}$ como si fuera el resultado del límite.** Al sustituir $h = 0$ se obtiene una forma indeterminada: hay que simplificar el cociente antes de pasar al límite.
- **Usar el punto exterior como punto de tangencia.** En «la tangente pasa por $(p, q)$» el punto $(p, q)$ no tiene por qué estar en la curva.
- **Pendiente de la normal.** Es $-\frac{1}{f'(a)}$: hay que cambiar el signo *y* invertir. Y si $f'(a) = 0$ la normal es vertical.
- **Pensar que la tangente solo toca en un punto.** Una tangente puede cortar la curva en otros puntos; lo que la define es la pendiente en el punto de tangencia.
:::

## Ejercicios

Podés explorar las secantes y la tangente con los deslizadores de la guía de [GeoGebra para derivada](/analisis-matematico-i/geogebra/derivada/) (`Tangente(2, f)` en GeoGebra Clásico 6).

### Ejercicio 1 · Enfriamiento de un horno
<!-- ejercicio: U3.01 | nivel: inicial | tipo: modelado | verificacion: sympy -->

:::note[Enunciado]
La temperatura de un horno, en °C, $t$ minutos después de apagarlo es $T(t) = 300 - 12t + \dfrac{t^2}{10}$ para $0 \le t \le 30$.

a) Calculá la razón de cambio media de $T$ entre $t = 0$ y $t = 10$.

b) Calculá $T'(10)$ por definición e interpretá el resultado con sus unidades.

c) ¿En qué instante la razón de cambio instantánea es $-8$ °C/min? ¿Qué temperatura tiene el horno en ese momento?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La media es el cociente entre la variación de $T$ y la del tiempo; la instantánea, el límite del cociente incremental.

**Desarrollo.**

a) $T(0) = 300$ y $T(10) = 300 - 120 + 10 = 190$. Entonces $\dfrac{T(10) - T(0)}{10 - 0} = \dfrac{190 - 300}{10} = -11$ °C/min.

b) $T(10 + h) = 300 - 12(10 + h) + \dfrac{(10 + h)^2}{10} = 190 - 10h + \dfrac{h^2}{10}$. Entonces

$$
\dfrac{T(10 + h) - T(10)}{h} = \dfrac{-10h + h^2/10}{h} = -10 + \dfrac{h}{10} \xrightarrow[h \to 0]{} -10.
$$

c) Con la derivada $T'(t) = -12 + \dfrac{t}{5}$ (que sale del mismo cálculo con $t$ genérico), $T'(t) = -8 \iff \dfrac{t}{5} = 4 \iff t = 20$, que está dentro del intervalo del modelo. En ese instante $T(20) = 300 - 240 + 40 = 100$ °C. Como $T'(t) < 0$ en todo $[0, 30]$, el horno se enfría durante todo el intervalo, cada vez más despacio (de $12$ a $6$ °C/min), y termina en $T(30) = 30$ °C.

**Resultado.** a) $-11$ °C/min. b) $T'(10) = -10$ °C/min: a los $10$ minutos el horno se enfría a razón de $10$ °C por minuto. c) $t = 20$ min, con el horno a $100$ °C.

</details>

### Ejercicio 2 · Derivada, tangente y normal por definición
<!-- ejercicio: U3.02 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $f(x) = 3x^2 - x$, calculá $f'(2)$ con la definición y hallá las ecuaciones de las rectas tangente y normal en $x = 2$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Calcular $f(2)$, formar el cociente incremental, simplificar y tomar el límite; después usar las fórmulas de tangente y normal.

**Desarrollo.** $f(2) = 12 - 2 = 10$. Además $f(2 + h) = 3(4 + 4h + h^2) - 2 - h = 10 + 11h + 3h^2$, de modo que

$$
\dfrac{f(2 + h) - f(2)}{h} = \dfrac{11h + 3h^2}{h} = 11 + 3h \xrightarrow[h \to 0]{} 11.
$$

Tangente: $y = 10 + 11(x - 2) = 11x - 12$. Normal: pendiente $-\frac{1}{11}$, $y = 10 - \frac{1}{11}(x - 2)$.

**Resultado.** $f'(2) = 11$; tangente $y = 11x - 12$; normal $y = 10 - \dfrac{x - 2}{11}$.

</details>

### Ejercicio 3 · Tangentes desde un punto exterior
<!-- ejercicio: U3.03 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallá las rectas tangentes a la gráfica de $f(x) = x^2 - 6x + 10$ que pasan por el punto $(2, -2)$. Indicá los puntos de tangencia.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El punto $(2, -2)$ no pertenece a la curva (porque $f(2) = 2$), así que el punto de tangencia es una incógnita $a$.

**Desarrollo.** Como $f'(x) = 2x - 6$, la tangente en $x = a$ es $y = a^2 - 6a + 10 + (2a - 6)(x - a)$. Pasa por $(2, -2)$ si

$$
-2 = a^2 - 6a + 10 + (2a - 6)(2 - a) = -a^2 + 4a - 2 \iff a^2 - 4a = 0 \iff a(a - 4) = 0.
$$

Para $a = 0$: punto $(0, 10)$ y pendiente $-6$, recta $y = 10 - 6x$. Para $a = 4$: punto $(4, 2)$ y pendiente $2$, recta $y = 2 + 2(x - 4) = 2x - 6$. Ambas pasan por $(2, -2)$: $10 - 12 = -2$ y $4 - 6 = -2$.

**Resultado.** $y = -6x + 10$ (tangente en $(0, 10)$) e $y = 2x - 6$ (tangente en $(4, 2)$).

</details>

### Ejercicio 4 · Parámetros de una tangente
<!-- ejercicio: U3.04 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
La recta $y = 4x - 3$ es tangente a $f(x) = a x^3 + b x$ en el punto de abscisa $x = 1$. Hallá $a$ y $b$ y la ecuación de la recta normal en ese punto.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En el punto de tangencia coinciden el valor de la función y el de la recta, y también sus pendientes.

**Desarrollo.** La recta vale $4 \cdot 1 - 3 = 1$ en $x = 1$, luego $f(1) = a + b = 1$. Como $f'(x) = 3ax^2 + b$, la pendiente exige $f'(1) = 3a + b = 4$. Restando las ecuaciones: $2a = 3$, entonces $a = \frac32$ y $b = 1 - \frac32 = -\frac12$.

La normal pasa por $(1, 1)$ con pendiente $-\frac14$: $y = 1 - \frac14(x - 1)$.

**Resultado.** $a = \dfrac32$, $b = -\dfrac12$; normal $y = 1 - \dfrac{x - 1}{4}$.

</details>

## Autoevaluación

**1. ¿Qué diferencia hay entre $\frac{f(b)-f(a)}{b-a}$ y $f'(a)$?**

<details>
<summary>Respuesta</summary>

La primera es la razón de cambio media en $[a, b]$ (pendiente de una secante); la segunda es el límite de esas razones cuando $b \to a$ (pendiente de la tangente), y puede no existir.
</details>

**2. Si $s(t)$ está en metros y $t$ en segundos, ¿qué unidad tiene $s'(t)$?**

<details>
<summary>Respuesta</summary>

Metros por segundo (m/s): $[f]/[x]$.
</details>

**3. La tangente a una curva en $(3, 5)$ pasa por $(0, 2)$. ¿Cuánto vale $f'(3)$?**

<details>
<summary>Respuesta</summary>

La pendiente es la de la recta que une los dos puntos: $\dfrac{5 - 2}{3 - 0} = 1$.
</details>

**4. Si $f'(a) = 0$, ¿cómo son la tangente y la normal en $a$?**

<details>
<summary>Respuesta</summary>

La tangente es horizontal, $y = f(a)$, y la normal es vertical, $x = a$.
</details>

:::tip[En resumen]
- La razón de cambio media es la pendiente de una secante; la instantánea, su límite cuando el intervalo se contrae.
- $f'(a) = \lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$, si el límite existe y es finito; mide el ritmo de cambio de $f$ en $a$, en unidades $[f]/[x]$.
- La tangente es $y = f(a) + f'(a)(x-a)$ y la normal, $y = f(a) - \frac{1}{f'(a)}(x-a)$ si $f'(a) \neq 0$.
- En los problemas de tangencia, el punto de tangencia es la incógnita: se plantean condiciones sobre $f(a)$ y $f'(a)$.
:::

**Para seguir.** Hasta acá fijamos el punto. En [la derivada como función](/analisis-matematico-i/unidad-3/teoria/derivada-como-funcion/) dejamos que $a$ varíe, estudiamos las derivadas laterales y qué relación hay entre derivabilidad y continuidad.
