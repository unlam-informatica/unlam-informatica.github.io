---
title: Polinomio de Taylor y de Mac Laurin
description: Construcción del polinomio de Taylor de orden n, desarrollos de Mac Laurin de las funciones elementales, aproximación de valores, ecuaciones y parámetros, y aproximación lineal.
slug: analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor
sidebar:
  order: 2
---

## Qué vas a aprender

- Construir el polinomio de Taylor de orden $n$ de una función en un punto y distinguir **orden** de **grado**.
- Escribir los desarrollos de Mac Laurin de $e^x$, $\operatorname{sen} x$, $\cos x$, $\ln(1+x)$ y $(1+x)^{\alpha}$.
- Usar el polinomio para aproximar valores, resolver ecuaciones de forma aproximada y hallar parámetros a partir de un polinomio dado.
- Reconocer la aproximación lineal como el polinomio de orden 1 y relacionarla con la recta tangente.

**Antes de empezar.** Repasá el [orden de contacto](/analisis-matematico-i/unidad-4/teoria/orden-de-contacto/) y el desarrollo de un polinomio por sus derivadas. Necesitás derivar con soltura: [reglas de derivación](/analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion/), [regla de la cadena](/analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa/) y la [recta tangente](/analisis-matematico-i/unidad-3/teoria/razon-de-cambio-y-derivada/).

## Introducción: el polinomio que mejor imita a $f$

En la lección anterior vimos que, entre los polinomios de grado $\le n$, hay **uno solo** con contacto al menos $n$ con $f$ en $a$, y que sus coeficientes son $\frac{f^{(k)}(a)}{k!}$. Ese polinomio es la herramienta central de la unidad: reemplaza una función por un polinomio, que se evalúa con sumas y productos, se deriva sin esfuerzo y se iguala a otros fácilmente.

## Definición

:::note[Definición · Polinomio de Taylor y de Mac Laurin]
Sea $f$ una función con derivadas hasta el orden $n$ en $x = a$. El **polinomio de Taylor de orden $n$** de $f$ centrado en $x = a$ es

$$
P_n(x) = \sum_{k=0}^{n} \dfrac{f^{(k)}(a)}{k!}\,(x - a)^k = f(a) + f'(a)(x - a) + \dfrac{f''(a)}{2!}(x - a)^2 + \dots + \dfrac{f^{(n)}(a)}{n!}(x - a)^n.
$$

Si $a = 0$, se lo llama **polinomio de Mac Laurin**: $P_n(x) = \displaystyle\sum_{k=0}^{n} \dfrac{f^{(k)}(0)}{k!}\,x^k$. Se usa $0! = 1$ y $f^{(0)} = f$.
:::

Por construcción $P_n^{(k)}(a) = f^{(k)}(a)$ para $k = 0, \dots, n$: $P_n$ tiene con $f$ un contacto **al menos de orden $n$** en $a$, y es el único polinomio de grado $\le n$ con esa propiedad. Si además $f^{(n+1)}(a) \neq 0$, como $P_n^{(n+1)} = 0$ el contacto es exactamente de orden $n$.

**Orden y grado no son lo mismo.** El *orden* $n$ es hasta qué derivada se usó; el *grado* de $P_n$ es el exponente más alto que realmente aparece. Cuando una derivada se anula en $a$, el grado puede ser menor que el orden. Siempre: $\operatorname{grado} P_n \le n$.

### Ejemplo 1 · Orden $4$, grado $3$
<!-- check: U4.T.TAY.1 -->

Para $f(x) = \operatorname{sen} x$ en $a = 0$ las derivadas son $\operatorname{sen} x,\ \cos x,\ -\operatorname{sen} x,\ -\cos x,\ \operatorname{sen} x$, que valen $0, 1, 0, -1, 0$ en $0$. Entonces

$$
P_4(x) = 0 + 1 \cdot x + \dfrac{0}{2!}x^2 + \dfrac{-1}{3!}x^3 + \dfrac{0}{4!}x^4 = x - \dfrac{x^3}{6}.
$$

Es el polinomio de **orden $4$** y **grado $3$**; coincide con $P_3$. La información que se agrega al pasar de orden $3$ a $4$ es que el coeficiente de $x^4$ es cero.

## Cómo se construye, paso a paso

1. Fijá la función $f$, el centro $a$ y el orden $n$.
2. Calculá $f, f', \dots, f^{(n)}$ (simplificá antes de evaluar: ahorra errores).
3. Evaluá en $a$ y dividí por $k!$ para obtener cada coeficiente.
4. Escribí $P_n(x) = \sum \frac{f^{(k)}(a)}{k!}(x - a)^k$. **No lo desarrolles** salvo que te lo pidan: en potencias de $(x - a)$ es más útil.

## Polinomios de Mac Laurin de las funciones elementales

Las derivadas sucesivas de estas funciones siguen un patrón, y por eso sus polinomios de Mac Laurin se recuerdan fácilmente.

:::note[Propiedad · Desarrollos de Mac Laurin básicos]
Para cada función se indican las derivadas en $0$ y el polinomio de orden $n$:

| Función | $f^{(k)}(0)$ | Polinomio de Mac Laurin |
|---|---|---|
| $e^x$ | $1$ para todo $k$ | $1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \dots + \dfrac{x^n}{n!}$ |
| $\operatorname{sen} x$ | $0, 1, 0, -1, 0, 1, \dots$ | $x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \dots$ (solo potencias impares) |
| $\cos x$ | $1, 0, -1, 0, 1, 0, \dots$ | $1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \dots$ (solo potencias pares) |
| $\ln(1 + x)$ | $0, 1, -1, 2, -6, 24, \dots$ | $x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dots + (-1)^{n-1}\dfrac{x^n}{n}$ |
| $(1 + x)^{\alpha}$ | $\alpha(\alpha - 1)\cdots(\alpha - k + 1)$ | $1 + \alpha x + \dfrac{\alpha(\alpha - 1)}{2!}x^2 + \dots + \dbinom{\alpha}{n}x^n$ |

con $\dbinom{\alpha}{k} = \dfrac{\alpha(\alpha - 1)\cdots(\alpha - k + 1)}{k!}$. En $\operatorname{sen} x$ y $\cos x$ se toman los términos hasta el exponente $n$.
:::

**Por qué funciona.** Basta calcular las derivadas en $0$. Para $e^x$, derivar no cambia la función: $f^{(k)}(0) = e^0 = 1$. Para $\operatorname{sen} x$ las derivadas se repiten cada cuatro pasos con el ciclo $\operatorname{sen}, \cos, -\operatorname{sen}, -\cos$. Para $\ln(1 + x)$: $f' = (1 + x)^{-1}$, $f'' = -(1 + x)^{-2}$, $f''' = 2(1 + x)^{-3}$, y en general $f^{(k)}(x) = (-1)^{k-1}(k - 1)!\,(1 + x)^{-k}$, de modo que $\frac{f^{(k)}(0)}{k!} = \frac{(-1)^{k-1}}{k}$. Para $(1 + x)^\alpha$, cada derivación baja el exponente en $1$ y multiplica por el exponente anterior: $f^{(k)}(x) = \alpha(\alpha - 1)\cdots(\alpha - k + 1)(1 + x)^{\alpha - k}$.

### Ejemplo 2 · Casos particulares de $(1 + x)^{\alpha}$
<!-- check: U4.T.TAY.2 -->

Con $\alpha = \frac12$ los coeficientes son $\binom{1/2}{2} = \frac{\frac12 \cdot (-\frac12)}{2} = -\frac18$ y $\binom{1/2}{3} = \frac{\frac12 \cdot (-\frac12)(-\frac32)}{6} = \frac{1}{16}$:

$$
\sqrt{1 + x} \approx 1 + \dfrac{x}{2} - \dfrac{x^2}{8} + \dfrac{x^3}{16}.
$$

Con $\alpha = -1$ es $\binom{-1}{k} = (-1)^k$: $\dfrac{1}{1 + x} \approx 1 - x + x^2 - x^3 + \dots$ (cada coeficiente es $\pm 1$). Los demás casos de la tabla se obtienen del mismo modo.

![Gráfico de seno de x y de sus polinomios de Mac Laurin de orden 1, 3 y 5](/analisis-matematico-i/figuras/u4-seno-taylor.svg)

*Cada polinomio acompaña a $\operatorname{sen} x$ en un entorno del origen que se agranda al subir el orden. Lejos del origen se separa rápidamente; observá que en $x = 2\pi$ el polinomio de orden $3$ está mucho peor que el de orden $1$: para un $x$ fijo, subir el orden no siempre mejora.*

### Reglas que ahorran cuentas

Tres propiedades de la derivada permiten obtener polinomios sin repetir todo el cálculo.

**Linealidad.** El polinomio de orden $n$ de $\lambda f + \mu g$ es $\lambda P_n^{f} + \mu P_n^{g}$, porque la derivada es lineal.

**Cambio de escala.** Si $P_n(x) = \sum c_k x^k$ es el polinomio de Mac Laurin de $f$, el de $f(\lambda x)$ es $\sum c_k \lambda^k x^k$: por la regla de la cadena $\frac{d^k}{dx^k} f(\lambda x) = \lambda^k f^{(k)}(\lambda x)$ y se evalúa en $0$.

**Paridad.** Sea $f$ derivable $n$ veces en un entorno de $0$ simétrico respecto del origen. Si $f$ es **par**, su polinomio de Mac Laurin solo tiene potencias pares; si es **impar**, solo impares.

**Demostración.** Primero, derivar cambia la paridad: si $f(-x) = f(x)$ para todo $x$ del entorno, derivando ambos miembros con la regla de la cadena queda $-f'(-x) = f'(x)$, es decir, $f'$ es impar; del mismo modo, si $f$ es impar, $f'$ es par. Aplicando esto $k$ veces: si $f$ es impar, sus derivadas de orden par son impares; si $f$ es par, sus derivadas de orden impar son impares. Por último, una función impar $g$ definida en $0$ cumple $g(0) = -g(0)$, o sea $g(0) = 0$. Entonces, para $f$ impar se anulan $f(0), f''(0), f^{(4)}(0), \dots$ (los coeficientes de las potencias pares), y para $f$ par se anulan $f'(0), f'''(0), \dots$ (los de las potencias impares). $\blacksquare$

### Ejemplo 3 · Producto de $x$ por una exponencial
<!-- check: U4.T.TAY.4 -->

Mac Laurin de orden $3$ de $f(x) = x\,e^x$. Por la regla del producto, $f'(x) = (1 + x)e^x$, $f''(x) = (2 + x)e^x$ y $f'''(x) = (3 + x)e^x$, que valen en $0$: $0, 1, 2, 3$. Los coeficientes $\frac{f^{(k)}(0)}{k!}$ son $0,\ 1,\ \frac{2}{2} = 1,\ \frac{3}{6} = \frac12$ y

$$
P_3(x) = x + x^2 + \dfrac{x^3}{2}.
$$

### Ejemplo 4 · Cambio de escala
<!-- check: U4.T.TAY.5 -->

El Mac Laurin de orden $4$ de $f(x) = \cos 2x$ se obtiene del de $\cos x$ ($1 - \frac{x^2}{2} + \frac{x^4}{24}$) reemplazando $x$ por $2x$:

$$
P_4(x) = 1 - \dfrac{(2x)^2}{2} + \dfrac{(2x)^4}{24} = 1 - 2x^2 + \dfrac{2}{3}x^4.
$$

(Con derivadas directas: $f^{(k)}(0) = 1, 0, -4, 0, 16$, y $\frac{16}{4!} = \frac23$.)

## Taylor centrado en otro punto

Cuando la función no tiene valores sencillos en $0$, o se quiere aproximar cerca de otro punto, se centra en un $a$ conveniente: uno **cercano** a lo que se quiere aproximar y donde la función y sus derivadas se calculen con exactitud.

### Ejemplo 5 · Polinomio de la raíz cúbica en $a = 8$ y aproximación de $\sqrt[3]{8{,}3}$
<!-- check: U4.T.TAY.3 -->

Para $f(x) = \sqrt[3]{x} = x^{1/3}$ y $a = 8$ (porque $\sqrt[3]{8} = 2$ es exacta), con orden $n = 2$:

$$
f'(x) = \tfrac13 x^{-2/3},\quad f''(x) = -\tfrac29 x^{-5/3}; \qquad f(8) = 2,\quad f'(8) = \tfrac13 \cdot \tfrac14 = \tfrac{1}{12},\quad f''(8) = -\tfrac29 \cdot \tfrac{1}{32} = -\tfrac{1}{144}.
$$

Los coeficientes son $2$, $\frac{1}{12}$ y $\frac{-1/144}{2} = -\frac{1}{288}$:

$$
P_2(x) = 2 + \dfrac{x - 8}{12} - \dfrac{(x - 8)^2}{288}.
$$

Para aproximar $\sqrt[3]{8{,}3}$ evaluamos en $x = 8{,}3$ (no en $0{,}3$: ese es $x - a$):

$$
P_2(8{,}3) = 2 + \dfrac{0{,}3}{12} - \dfrac{0{,}09}{288} = 2 + 0{,}025 - 0{,}0003125 = 2{,}0246875 = \dfrac{6479}{3200}.
$$

La calculadora da $\sqrt[3]{8{,}3} \approx 2{,}0246939$: el error es de unas seis millonésimas.

### Ejemplo 6 · Seno en $a = \pi/4$
<!-- check: U4.T.TAY.6 -->

Las derivadas de $\operatorname{sen} x$ en $\frac{\pi}{4}$ son $\frac{\sqrt2}{2},\ \frac{\sqrt2}{2},\ -\frac{\sqrt2}{2},\ -\frac{\sqrt2}{2}$ (de $k = 0$ a $3$, con el ciclo $\operatorname{sen}, \cos, -\operatorname{sen}, -\cos$). Por lo tanto el polinomio de orden $3$ es

$$
P_3(x) = \dfrac{\sqrt2}{2}\left[1 + \left(x - \dfrac{\pi}{4}\right) - \dfrac{1}{2}\left(x - \dfrac{\pi}{4}\right)^2 - \dfrac{1}{6}\left(x - \dfrac{\pi}{4}\right)^3\right].
$$

![Gráfico de ln x y sus polinomios de Taylor de orden 1, 2 y 3 en a = 1](/analisis-matematico-i/figuras/u4-ln-taylor.svg)

*Para $\ln x$ centrado en $a = 1$, los tres polinomios coinciden con la función en $x = 1$ y se separan al alejarse. A la izquierda de $1$ se hunden menos que $\ln x$ (que tiende a $-\infty$ cerca de $0$). A la derecha, $P_2$ se cierra hacia abajo y $P_1$, $P_3$ suben: no hay una regla sencilla de «mejor» lejos del centro.*

## Para qué sirve: tres usos

### 1. Aproximar valores

Elegí una $f$ y un centro $a$ tales que el valor pedido sea $f(x_0)$ con $x_0$ cerca de $a$ y $f(a)$, $f'(a), \dots$ sean exactos. Calculá $P_n(x_0)$. **Cuidado con el punto de evaluación**: en $P_n(x)$ la variable es $x$, no la distancia $x - a$ (ejemplo 5 con $x = 8{,}3$).

### 2. Resolver ecuaciones de forma aproximada

Cuando una ecuación mezcla polinomios con funciones trascendentes, se reemplaza la función por su polinomio de Taylor o de Mac Laurin y se resuelve la ecuación polinómica resultante. Se elige el orden mínimo que permita resolverla y se verifica que la solución caiga en la zona donde el polinomio aproxima bien (cerca del centro).

### Ejemplo 7 · Resolver $\cos x = x^2$
<!-- check: U4.T.TAY.7 -->

Primero localizamos la solución. Si $g(x) = \cos x - x^2$, entonces $g(0) = 1 > 0$ y $g(1) = \cos 1 - 1 < 0$; en $[0, \frac{\pi}{2}]$ la función $g$ es decreciente ($g'(x) = -\operatorname{sen} x - 2x < 0$), así que en $[0, \frac{\pi}{2}]$ hay exactamente una solución, en $(0, 1)$ (para $x > \frac{\pi}{2}$ no hay ninguna, porque $x^2 > 1 \ge \cos x$), es decir, una única solución positiva, y por simetría una negativa opuesta. Usamos el Mac Laurin de $\cos x$.

- **Orden $2$:** $\cos x \approx 1 - \frac{x^2}{2}$. La ecuación $1 - \frac{x^2}{2} = x^2$ da $x^2 = \frac23$ y $x \approx 0{,}8165$.
- **Orden $4$:** $\cos x \approx 1 - \frac{x^2}{2} + \frac{x^4}{24}$. La ecuación $1 - \frac{x^2}{2} + \frac{x^4}{24} = x^2$, multiplicada por $24$, es $x^4 - 36x^2 + 24 = 0$: bicuadrada, con $t = x^2$, $t^2 - 36t + 24 = 0$ y

$$
t = \dfrac{36 \pm \sqrt{1296 - 96}}{2} = 18 \pm 10\sqrt3.
$$

La raíz grande, $18 + 10\sqrt3 \approx 35{,}3$, da $x \approx \pm 5{,}9$, lejos del centro, donde el polinomio no representa al coseno: se descarta. La pequeña, $18 - 10\sqrt3 \approx 0{,}68$, da $x = \sqrt{18 - 10\sqrt3} \approx 0{,}8243$.

La solución exacta de $\cos x = x^2$ está entre $0{,}8241$ y $0{,}8242$ (porque $g(0{,}8241) > 0 > g(0{,}8242)$): el orden $4$ da un error de unas $2 \cdot 10^{-4}$ y el orden $2$, de unas $8 \cdot 10^{-3}$.

### 3. Hallar parámetros desde un polinomio dado

Si se sabe que el polinomio de Taylor de una función con parámetros es uno dado, se igualan los coeficientes: el de $(x - a)^k$ debe ser $\frac{f^{(k)}(a)}{k!}$. Se obtiene un sistema que, si el polinomio es compatible, se resuelve; si sobran ecuaciones, sirven para controlar.

### Ejemplo 8 · Parámetros de una exponencial
<!-- check: U4.T.TAY.8 -->

Sea $f(x) = a\,e^{bx}$ con Mac Laurin de orden $2$ igual a $5 - 10x + 10x^2$. Las derivadas son $f^{(k)}(0) = a\,b^k$, y los coeficientes $a,\ ab,\ \frac{ab^2}{2}$. Igualando:

$$
a = 5, \qquad ab = -10 \Rightarrow b = -2, \qquad \dfrac{ab^2}{2} = \dfrac{5 \cdot 4}{2} = 10 \ \checkmark
$$

La tercera ecuación no se usó para hallar $a$ y $b$: se cumple, así que el polinomio es compatible con $f(x) = 5e^{-2x}$.

### Ejemplo 9 · Leer las derivadas de un polinomio de Taylor
<!-- check: U4.T.TAY.9 -->

Si el Taylor de orden $2$ de $f$ en $a = -1$ es $P_2(x) = 4 - 6(x + 1) + 5(x + 1)^2$, entonces, comparando con $f(-1) + f'(-1)(x + 1) + \frac{f''(-1)}{2}(x + 1)^2$: $f(-1) = 4$, $f'(-1) = -6$ y $\frac{f''(-1)}{2} = 5$, o sea $f''(-1) = 10$. La recta tangente en $x = -1$ es $y = 4 - 6(x + 1)$. Además $f(-0{,}9) \approx P_2(-0{,}9) = 4 - 0{,}6 + 0{,}05 = 3{,}45$.

## Aproximación lineal

El polinomio de Taylor de **orden $1$** en $a$ es

$$
P_1(x) = f(a) + f'(a)(x - a),
$$

que es exactamente la **ecuación de la recta tangente** a $f$ en $x = a$ (ver [recta tangente](/analisis-matematico-i/unidad-3/teoria/razon-de-cambio-y-derivada/)). A $P_1$ se lo llama también **linealización** o **aproximación lineal** de $f$ en $a$ y se lo suele denotar $L(x)$. Entre todas las rectas, la tangente es la única con contacto al menos de orden $1$ con la curva.

Para $x$ cerca de $a$ vale $f(x) \approx f(a) + f'(a)(x - a)$, o sea que la variación de la función es aproximadamente la derivada por la variación de $x$:
$\Delta f \approx f'(a)\,\Delta x$.

**El signo del error.** Si $f'' > 0$ cerca de $a$ (concavidad hacia arriba), la curva queda por encima de la tangente y la aproximación lineal **subestima**; si $f'' < 0$ queda por debajo y **sobreestima**. Esta afirmación se demuestra en la [lección siguiente](/analisis-matematico-i/unidad-4/teoria/termino-complementario/) con el término complementario.

![Gráfico de la raíz cuarta de x y su recta tangente en x = 16](/analisis-matematico-i/figuras/u4-aprox-lineal.svg)

*La raíz cuarta tiene $f'' < 0$, es cóncava hacia abajo: la tangente en $x = 16$ queda por encima de la curva a ambos lados del punto. En $x = 20$ (puntos huecos) la diferencia entre la tangente y la curva ya se ve.*

### Ejemplo 10 · Estimar $\sqrt[4]{16{,}2}$
<!-- check: U4.T.LIN.1 -->

Con $f(x) = \sqrt[4]{x}$ y $a = 16$: $f(16) = 2$ y $f'(x) = \frac14 x^{-3/4}$, de modo que $f'(16) = \frac14 \cdot \frac18 = \frac{1}{32}$. La linealización es $L(x) = 2 + \frac{x - 16}{32}$ y

$$
\sqrt[4]{16{,}2} \approx L(16{,}2) = 2 + \dfrac{0{,}2}{32} = 2{,}00625.
$$

El valor con calculadora es $2{,}0062209\ldots$, y como $f''(16) < 0$ la estimación queda **por encima** del valor real, como predice la concavidad.

### Ejemplo 11 · Linealizaciones en el origen
<!-- check: U4.T.LIN.2 -->

Los desarrollos de la tabla, tomados hasta el orden $1$, dan las aproximaciones para $x$ cercano a $0$:

$$
\operatorname{sen} x \approx x, \qquad e^x \approx 1 + x, \qquad \ln(1 + x) \approx x, \qquad (1 + x)^{\alpha} \approx 1 + \alpha x.
$$

Con $\alpha = -\frac12$ y $x = 0{,}04$: $\dfrac{1}{\sqrt{1{,}04}} = (1 + 0{,}04)^{-1/2} \approx 1 - \dfrac{0{,}04}{2} = 0{,}98$. La calculadora da $0{,}98058\ldots$.

### Ejemplo 12 · Variación aproximada del volumen
<!-- check: U4.T.LIN.3 -->

El volumen de una esfera es $V(r) = \frac43 \pi r^3$ y $V'(r) = 4\pi r^2$. Si el radio pasa de $10$ cm a $10{,}2$ cm, la variación del volumen es aproximadamente $\Delta V \approx V'(10)\,\Delta r = 400\pi \cdot 0{,}2 = 80\pi \approx 251{,}3$ cm$^3$. La variación exacta es $\frac43\pi(10{,}2^3 - 10^3) = 81{,}6107\ldots\,\pi \approx 256{,}4$ cm$^3$: la aproximación lineal subestima, porque $V'' > 0$.

Los comandos para explorar todo esto con deslizadores (polinomios de distinto orden, recta tangente y centro $a$ móvil) están en la [guía de GeoGebra para Taylor](/analisis-matematico-i/geogebra/taylor/).

:::caution[Errores frecuentes]
- **Olvidar $k!$**: $e^x$ no tiene $\frac{x^3}{3}$ sino $\frac{x^3}{3!} = \frac{x^3}{6}$.
- **Evaluar en el punto equivocado.** Para $\sqrt[3]{8{,}3}$ con centro $8$, se reemplaza $x = 8{,}3$ (de modo que $x - a = 0{,}3$), no $x = 0{,}3$.
- **Confundir orden con grado**: el polinomio de orden $4$ de $\operatorname{sen} x$ tiene grado $3$, y el de orden $3$ de $\cos x$ tiene grado $2$.
- **Usar un centro lejano** al valor que se aproxima: el polinomio de orden bajo solo imita bien cerca de $a$.
- **Aceptar toda solución de la ecuación polinómica.** Hay soluciones espurias lejos del centro, como $x \approx \pm 5{,}9$ en el ejemplo 7.
- **Derivar mal antes de evaluar**: simplificá cada derivada (por ejemplo, $(2 + x)e^x$) antes de reemplazar.
:::

## Ejercicios

### Ejercicio 5 · Mac Laurin con cambio de escala
<!-- ejercicio: U4.05 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) Hallá el polinomio de Mac Laurin de orden $4$ de $f(x) = e^{-2x}$ y de $g(x) = \cos 3x$.

b) Usá el de $f$ para aproximar $e^{-0{,}2}$ (evaluá en $x = 0{,}1$) y escribí el resultado como fracción.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Derivar con la regla de la cadena: $f^{(k)}(0) = (-2)^k$; o reemplazar $x$ por $-2x$ y por $3x$ en los desarrollos básicos.

**Desarrollo.** a) Para $f(x) = e^{-2x}$ las derivadas $f^{(k)}(x) = (-2)^k e^{-2x}$ valen $(-2)^k$ en $0$. Los coeficientes $\frac{(-2)^k}{k!}$, de $k = 0$ a $4$, son $1,\ -2,\ \frac{4}{2} = 2,\ -\frac{8}{6} = -\frac43,\ \frac{16}{24} = \frac23$:

$$
P_4(x) = 1 - 2x + 2x^2 - \dfrac43 x^3 + \dfrac23 x^4.
$$

Para $g(x) = \cos 3x$: reemplazando en $1 - \frac{u^2}{2} + \frac{u^4}{24}$ con $u = 3x$:

$$
P_4(x) = 1 - \dfrac{9x^2}{2} + \dfrac{81x^4}{24} = 1 - \dfrac92 x^2 + \dfrac{27}{8}x^4.
$$

b) Como $e^{-0{,}2} = f(0{,}1)$:

$$
P_4(0{,}1) = 1 - \dfrac{1}{5} + \dfrac{2}{100} - \dfrac43 \cdot \dfrac{1}{1000} + \dfrac23 \cdot \dfrac{1}{10000} = 1 - \dfrac15 + \dfrac1{50} - \dfrac1{750} + \dfrac1{15000} = \dfrac{12281}{15000}.
$$

Esto es $0{,}818733\ldots$; el valor de la calculadora es $e^{-0{,}2} = 0{,}818730\ldots$.

**Resultado.** a) $P_4^{f} = 1 - 2x + 2x^2 - \frac43 x^3 + \frac23 x^4$, $P_4^{g} = 1 - \frac92 x^2 + \frac{27}{8}x^4$; b) $e^{-0{,}2} \approx \frac{12281}{15000} \approx 0{,}81873$.

</details>

### Ejercicio 6 · Aproximación lineal de una raíz
<!-- ejercicio: U4.06 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \sqrt{x}$.

a) Hallá la linealización de $f$ en $a = 36$.

b) Estimá $\sqrt{37}$ y $\sqrt{35}$.

c) ¿Las estimaciones son mayores o menores que los valores reales? Justificá con $f''$ y confirmá con la calculadora.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $L(x) = f(36) + f'(36)(x - 36)$; el signo del error se lee de la concavidad.

**Desarrollo.** a) $f(36) = 6$ y $f'(x) = \frac{1}{2\sqrt{x}}$, de modo que $f'(36) = \frac{1}{12}$. Entonces $L(x) = 6 + \frac{x - 36}{12}$.

b) $L(37) = 6 + \frac{1}{12} = \frac{73}{12} \approx 6{,}08333$ y $L(35) = 6 - \frac{1}{12} = \frac{71}{12} \approx 5{,}91667$.

c) $f''(x) = -\frac{1}{4}x^{-3/2} < 0$ para $x > 0$: la curva es cóncava hacia abajo y queda por debajo de su tangente, de modo que ambas estimaciones **sobreestiman**. Con calculadora: $\sqrt{37} = 6{,}08276\ldots < 6{,}08333$ y $\sqrt{35} = 5{,}91608\ldots < 5{,}91667$.

**Resultado.** $L(x) = 6 + \frac{x - 36}{12}$; $\sqrt{37} \approx \frac{73}{12}$, $\sqrt{35} \approx \frac{71}{12}$, ambas por exceso.

</details>

### Ejercicio 7 · Una ecuación con seno
<!-- ejercicio: U4.07 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Resolvé aproximadamente $\operatorname{sen} x = x^2$.

a) Con el Mac Laurin de orden $3$ de $\operatorname{sen} x$, hallá las soluciones de la ecuación polinómica resultante.

b) ¿Cuáles de ellas tienen sentido como aproximación de una solución de $\operatorname{sen} x = x^2$? Justificá.

c) Verificá, evaluando la diferencia $\operatorname{sen} x - x^2$ en $0{,}87$ y en $0{,}88$, que hay una solución entre esos valores y comparala con la aproximación.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reemplazar $\operatorname{sen} x$ por $x - \frac{x^3}{6}$, factorizar $x$ y resolver la cuadrática; luego descartar soluciones lejos del centro.

**Desarrollo.** a) $x - \frac{x^3}{6} = x^2 \iff x\left(1 - \frac{x^2}{6} - x\right) = 0$. Una solución es $x = 0$. El otro factor da $x^2 + 6x - 6 = 0$, así que $x = \frac{-6 \pm \sqrt{36 + 24}}{2} = -3 \pm \sqrt{15}$, es decir $x \approx 0{,}8730$ y $x \approx -6{,}8730$.

b) $x = 0$ es solución exacta ($\operatorname{sen} 0 = 0 = 0^2$). Para $x \approx 0{,}873$ el polinomio aproxima bien al seno: tiene sentido. Para $x \approx -6{,}873$, lejos del centro, el polinomio de orden $3$ vale $x - \frac{x^3}{6} \approx 47$ mientras que $\operatorname{sen} x$ está entre $-1$ y $1$: es espuria. De hecho, $\operatorname{sen} x \le 1$ y $x^2 \le 1$ exige $\lvert x \rvert \le 1$, de modo que no hay soluciones con $\lvert x \rvert > 1$.

c) Sea $g(x) = \operatorname{sen} x - x^2$: $g(0{,}87) \approx 0{,}0074 > 0$ y $g(0{,}88) \approx -0{,}0037 < 0$, de modo que hay una solución en $(0{,}87;\ 0{,}88)$. La aproximación $0{,}8730$ cae en ese intervalo.

**Resultado.** Soluciones de la ecuación aproximada: $x = 0$ y $x = -3 \pm \sqrt{15}$; sirven $x = 0$ y $x = -3 + \sqrt{15} \approx 0{,}873$; la solución exacta positiva está en $(0{,}87;\ 0{,}88)$.

</details>

### Ejercicio 8 · Parámetros y derivadas a partir de un polinomio
<!-- ejercicio: U4.08 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) Hallá $a$, $b$ y $c$ para que el Mac Laurin de orden $2$ de $f(x) = a\,e^{bx} + c$ sea $P_2(x) = 5 + 6x + 6x^2$ y calculá $f'''(0)$.

b) El polinomio de Taylor de orden $3$ de $g$ en $x = 2$ es $Q(x) = 1 + 3(x - 2) - (x - 2)^2 + 4(x - 2)^3$. Hallá $g(2)$, $g'(2)$, $g''(2)$, $g'''(2)$ y la recta tangente en $x = 2$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Igualar los coeficientes $\frac{f^{(k)}(0)}{k!}$ con los del polinomio dado; en b), $g^{(k)}(2) = k! \cdot (\text{coeficiente de } (x - 2)^k)$.

**Desarrollo.** a) Con $f^{(k)}(x) = a b^k e^{bx}$ para $k \ge 1$: $f(0) = a + c$, $f'(0) = ab$, $f''(0) = ab^2$. Entonces

$$
a + c = 5, \qquad ab = 6, \qquad \dfrac{ab^2}{2} = 6.
$$

De $ab^2 = 12$ y $ab = 6$ resulta $b = 2$, luego $a = 3$ y $c = 2$ (así $f(x) = 3e^{2x} + 2$). Además $f'''(0) = ab^3 = 3 \cdot 8 = 24$.

b) Por los coeficientes: $g(2) = 1$; $g'(2) = 3$; $\frac{g''(2)}{2!} = -1 \Rightarrow g''(2) = -2$; $\frac{g'''(2)}{3!} = 4 \Rightarrow g'''(2) = 24$. La recta tangente es $y = 1 + 3(x - 2)$.

**Resultado.** a) $a = 3$, $b = 2$, $c = 2$, $f'''(0) = 24$; b) $g(2) = 1$, $g'(2) = 3$, $g''(2) = -2$, $g'''(2) = 24$, tangente $y = 1 + 3(x - 2)$.

</details>

### Ejercicio 9 · Polinomio de un producto a partir de datos
<!-- ejercicio: U4.09 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $g$ una función derivable tres veces, con $g(0) = 2$, $g'(0) = -1$, $g''(0) = 4$ y $g'''(0) = 6$, y sea $h(x) = g(x)\,e^{2x}$.

a) Hallá $h(0)$, $h'(0)$, $h''(0)$ y $h'''(0)$.

b) Escribí el polinomio de Mac Laurin de orden $3$ de $h$ y la recta tangente a $h$ en $x = 0$.

c) Obtené el mismo polinomio multiplicando los polinomios de Mac Laurin de orden $3$ de $g$ y de $e^{2x}$ y quedándote con los términos de grado $\le 3$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Derivar el producto con la regla de Leibniz (o aplicando tres veces la regla del producto) y evaluar en $0$.

**Desarrollo.** a) Con $u = e^{2x}$: $u^{(k)} = 2^k e^{2x}$, de modo que $u^{(k)}(0) = 2^k$. Por la regla del producto:

- $h(0) = g(0)\cdot 1 = 2$.
- $h' = g' e^{2x} + 2g\,e^{2x}$, luego $h'(0) = -1 + 2 \cdot 2 = 3$.
- $h'' = g'' e^{2x} + 4g'\,e^{2x} + 4g\,e^{2x}$, luego $h''(0) = 4 - 4 + 8 = 8$.
- $h''' = g''' e^{2x} + 6g''\,e^{2x} + 12g'\,e^{2x} + 8g\,e^{2x}$, luego $h'''(0) = 6 + 24 - 12 + 16 = 34$.

b) Coeficientes: $2$, $3$, $\frac{8}{2} = 4$ y $\frac{34}{6} = \frac{17}{3}$:

$$
P_3(x) = 2 + 3x + 4x^2 + \dfrac{17}{3}x^3, \qquad \text{tangente: } y = 2 + 3x.
$$

c) Esto funciona porque, por la regla del producto, la derivada de orden $k \le 3$ de $h$ en $0$ solo depende de las derivadas de orden $\le k$ de $g$ y de $e^{2x}$ en $0$; por eso el polinomio de $h$ se obtiene del producto de los polinomios de los factores, truncado en el grado $3$. El Mac Laurin de orden $3$ de $g$ es $2 - x + 2x^2 + x^3$ (coeficientes $2$, $-1$, $\frac42 = 2$, $\frac66 = 1$) y el de $e^{2x}$ es $1 + 2x + 2x^2 + \frac43 x^3$. Al multiplicar y quedarnos con el grado $\le 3$: término independiente $2$; en $x$: $2 \cdot 2 - 1 = 3$; en $x^2$: $2 \cdot 2 - 1 \cdot 2 + 2 = 4$; en $x^3$: $2 \cdot \frac43 - 1 \cdot 2 + 2 \cdot 2 + 1 = \frac83 + 3 = \frac{17}{3}$. Coincide con b).

**Resultado.** a) $h(0) = 2$, $h'(0) = 3$, $h''(0) = 8$, $h'''(0) = 34$; b) $P_3(x) = 2 + 3x + 4x^2 + \frac{17}{3}x^3$, tangente $y = 2 + 3x$; c) coincide.

</details>

## Autoevaluación

**1. ¿Cuál es el polinomio de Mac Laurin de orden 3 de $\cos x$? ¿Qué grado tiene?**

<details>
<summary>Respuesta</summary>

$1 - \frac{x^2}{2}$ (porque el coeficiente de $x^3$ es $0$). Su grado es $2$ aunque el orden sea $3$.
</details>

**2. Para aproximar $\sqrt{26}$ con un polinomio de Taylor, ¿qué función y qué centro conviene elegir?**

<details>
<summary>Respuesta</summary>

$f(x) = \sqrt{x}$ con $a = 25$, porque $\sqrt{25} = 5$ es exacta y $26$ está cerca de $25$.
</details>

**3. ¿Cómo se relaciona $P_1$ con la recta tangente? ¿Y con la aproximación lineal?**

<details>
<summary>Respuesta</summary>

$P_1(x) = f(a) + f'(a)(x - a)$ es la ecuación de la recta tangente en $a$; usarla para estimar $f(x)$ cerca de $a$ es la aproximación lineal o linealización.
</details>

**4. Si el Taylor de orden 3 de $f$ en $a = 1$ tiene coeficiente $-\frac{1}{2}$ en $(x - 1)^3$, ¿cuánto vale $f'''(1)$?**

<details>
<summary>Respuesta</summary>

$f'''(1) = 3! \cdot \left(-\frac12\right) = -3$.
</details>

:::tip[En resumen]
- $P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k$: el único polinomio de grado $\le n$ con contacto al menos $n$ con $f$ en $a$. Con $a = 0$ es el de Mac Laurin.
- Orden $\neq$ grado: el grado puede ser menor si alguna derivada se anula.
- Mac Laurin básicos: $e^x$, $\operatorname{sen} x$ (impares), $\cos x$ (pares), $\ln(1 + x)$, $(1 + x)^\alpha$.
- Usos: aproximar valores (centro cercano y valores exactos), resolver ecuaciones (descartar soluciones lejanas) y hallar parámetros igualando coeficientes.
- $P_1(x) = f(a) + f'(a)(x - a)$ es la recta tangente: la aproximación lineal.
:::

**Para seguir.** Aproximar es útil si sabemos cuánto nos equivocamos. En [término complementario](/analisis-matematico-i/unidad-4/teoria/termino-complementario/) escribimos el error exacto como resto de Lagrange, lo acotamos en un intervalo y elegimos el orden necesario para una precisión dada.
