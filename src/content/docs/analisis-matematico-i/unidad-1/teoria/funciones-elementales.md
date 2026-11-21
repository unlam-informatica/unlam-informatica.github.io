---
title: Funciones elementales
description: Catálogo de las funciones algebraicas y trascendentes que se usan en toda la materia, con sus gráficos, dominio, imagen, ceros y características.
slug: analisis-matematico-i/unidad-1/teoria/funciones-elementales
sidebar:
  order: 3
---

## Qué vas a aprender

- Reconocer y graficar las funciones lineal, cuadrática, polinómica, racional (homográfica), irracional, valor absoluto y por tramos.
- Reconocer y graficar exponenciales, logarítmicas, trigonométricas y trigonométricas inversas, con su dominio, imagen, ceros, período y asíntotas.

## Antes de empezar

Conviene haber leído [funciones y modelos](/analisis-matematico-i/unidad-1/teoria/funciones-y-modelos/) y [ceros, signo, paridad y acotación](/analisis-matematico-i/unidad-1/teoria/caracteristicas/). Para cada función de este catálogo vamos a dar los mismos datos, siempre en el mismo orden: **dominio, imagen, ceros y signo, paridad, monotonía y asíntotas**. Una asíntota es una recta a la que la curva se acerca indefinidamente; su definición precisa con límites está en la [Unidad 2](/analisis-matematico-i/unidad-2/teoria/asintotas/); aquí las reconocemos desde la forma de la fórmula y del gráfico.

**Monotonía.** Una función es **estrictamente creciente** en un conjunto $S$ si $x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$ para todo par $x_1, x_2 \in S$, y **estrictamente decreciente** si $x_1 < x_2 \Rightarrow f(x_1) > f(x_2)$. Dice que, al avanzar hacia la derecha, el gráfico siempre sube (o siempre baja).

## Funciones algebraicas

Son las que se obtienen con un número finito de sumas, productos, cocientes, potencias y raíces de la variable.

![Gráficos de x², x³/3, √x y 1/x en una misma ventana.](/analisis-matematico-i/figuras/u1-algebraicas.svg)

*Observá cómo cambia la forma según la potencia: $x^2$ es par (simétrica respecto del eje $y$), $x^3$ y $1/x$ son impares (simétricas respecto del origen), $\sqrt{x}$ solo existe a la derecha del origen y $1/x$ tiene dos ramas separadas por el eje $y$.*

### Función lineal

$f(x) = mx + b$. Gráfico: una recta. $m$ es la **pendiente** ($m = \tan\alpha$, con $\alpha$ el ángulo con el eje $x$) y $b$ la ordenada al origen. Si $m \ne 0$: dominio e imagen $\mathbb{R}$; un único cero $x = -b/m$; estrictamente creciente si $m > 0$, decreciente si $m < 0$. Si $m = 0$ es la función **constante**, con imagen $\{b\}$. Se la determina con dos puntos: $m = \dfrac{y_2 - y_1}{x_2 - x_1}$. Dos rectas son paralelas si tienen igual pendiente y perpendiculares si $m_1 m_2 = -1$.

### Función cuadrática

$f(x) = ax^2 + bx + c$, con $a \ne 0$. Gráfico: **parábola** de eje vertical.

| Forma | Expresión | Qué se lee directamente |
|---|---|---|
| Polinómica | $ax^2 + bx + c$ | ordenada al origen $c$ |
| Canónica | $a(x - h)^2 + k$ | vértice $(h, k)$ y eje $x = h$ |
| Factorizada | $a(x - x_1)(x - x_2)$ | ceros $x_1, x_2$ |

El vértice tiene $h = -\dfrac{b}{2a}$ y $k = f(h)$. Los ceros se calculan con $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$; el signo del **discriminante** $\Delta = b^2 - 4ac$ dice cuántos hay ($\Delta > 0$: dos; $\Delta = 0$: uno doble; $\Delta < 0$: ninguno). La imagen es $[k, +\infty)$ si $a > 0$ y $(-\infty, k]$ si $a < 0$. Se pasa de la forma polinómica a la canónica **completando cuadrados**.

### Funciones polinómicas

$p(x) = a_n x^n + \dots + a_1 x + a_0$ con $a_n \ne 0$. Dominio $\mathbb{R}$. Un polinomio de grado $n$ tiene **a lo sumo $n$ ceros** reales. Para $|x|$ grande, el gráfico se parece al de su término de mayor grado, $a_n x^n$: con grado **impar** las dos ramas apuntan en sentidos opuestos (imagen $\mathbb{R}$); con grado **par** las dos apuntan al mismo lado. No tienen asíntotas. La más simple de grado $3$, $x^3$, es impar y estrictamente creciente.

### Función racional

$f(x) = \dfrac{P(x)}{Q(x)}$; dominio $\mathbb{R}$ menos los ceros de $Q$. El caso básico es $f(x) = \dfrac{1}{x}$: dominio e imagen $\mathbb{R} \setminus \{0\}$, impar, sin ceros, con asíntota vertical $x = 0$ y horizontal $y = 0$; su gráfico es una **hipérbola**.

La **función homográfica** $f(x) = \dfrac{ax + b}{cx + d}$, con $c \ne 0$ y $ad - bc \ne 0$ (la segunda condición evita que se reduzca a una constante), se reescribe dividiendo:

$$
\frac{ax + b}{cx + d} = \frac{a}{c} + \frac{bc - ad}{c^2}\cdot\frac{1}{x + d/c}.
$$

Así se ve que su gráfico es el de $\dfrac{1}{x}$ trasladado y reescalado (si la constante $\frac{bc - ad}{c^2}$ es negativa, además reflejado). Tiene asíntota vertical $x = -\dfrac{d}{c}$, horizontal $y = \dfrac{a}{c}$, dominio $\mathbb{R} \setminus \{-d/c\}$ e imagen $\mathbb{R} \setminus \{a/c\}$; el centro de simetría es el cruce de las asíntotas.

### Función irracional

$f(x) = \sqrt[n]{g(x)}$. Con $n$ **par**, el dominio exige $g(x) \ge 0$; con $n$ **impar**, el dominio es el de $g$. El caso básico $\sqrt{x}$: dominio e imagen $[0, +\infty)$, único cero en $x = 0$, estrictamente creciente. Además $\sqrt{x} \ge 0$ **siempre**: la raíz cuadrada es la raíz *no negativa*. Por eso $\sqrt{x^2} = |x|$, no $x$.

### Valor absoluto

$$
|x| = \begin{cases} x & \text{si } x \ge 0, \\ -x & \text{si } x < 0. \end{cases}
$$

Dominio $\mathbb{R}$, imagen $[0, +\infty)$, par, gráfico en «V» con vértice en el origen. Propiedades: $|xy| = |x||y|$; $|x + y| \le |x| + |y|$ (desigualdad triangular); para $a > 0$, $|x| < a \iff -a < x < a$ y $|x| > a \iff x < -a$ o $x > a$.

### Funciones por tramos

La regla cambia según el intervalo: $f(x) = f_k(x)$ si $x \in I_k$, con los $I_k$ disjuntos cuya unión es el dominio. La imagen es la **unión de las imágenes** de cada tramo; los ceros se buscan **dentro de cada tramo** (como en el ejemplo 3 de [ceros y signo](/analisis-matematico-i/unidad-1/teoria/caracteristicas/)); el valor absoluto es un caso de función por tramos.

### Ejemplo 1 · Parábola en sus tres formas

Analizar $f(x) = 2x^2 - 12x + 10$.

Completamos cuadrados: $2x^2 - 12x + 10 = 2(x^2 - 6x) + 10 = 2\left[(x - 3)^2 - 9\right] + 10 = 2(x - 3)^2 - 8$. El vértice es $(3, -8)$ y la imagen $[-8, +\infty)$. Los ceros: $2(x - 3)^2 = 8 \Rightarrow x - 3 = \pm 2 \Rightarrow x = 1$ o $x = 5$, así que $f(x) = 2(x - 1)(x - 5)$. La ordenada al origen es $f(0) = 10$ y

<!-- check: U1.T.ELE.1 -->
$$
C^{+} = (-\infty, 1) \cup (5, +\infty), \qquad C^{-} = (1, 5).
$$

### Ejemplo 2 · Homográfica

Analizar $h(x) = \dfrac{3x - 1}{x + 2}$.

<!-- check: U1.T.ELE.2 -->
Dividimos: $3x - 1 = 3(x + 2) - 7$, entonces $h(x) = 3 - \dfrac{7}{x + 2}$. Por lo tanto: dominio $\mathbb{R} \setminus \{-2\}$; asíntota vertical $x = -2$; asíntota horizontal $y = 3$; centro $(-2, 3)$. El valor $y = 3$ **no** se alcanza ($3x - 1 = 3x + 6$ es imposible), de modo que $\operatorname{Im} h = \mathbb{R} \setminus \{3\}$. El cero es $x = \frac13$ y la ordenada al origen $h(0) = -\frac12$. El signo: $h > 0$ si $x < -2$ o $x > \frac13$.

### Ejemplo 3 · Función irracional

Analizar $f(x) = \sqrt{6 - 2x} + 1$.

<!-- check: U1.T.ELE.3 -->
El radicando debe cumplir $6 - 2x \ge 0 \iff x \le 3$: dominio $(-\infty, 3]$. Como $\sqrt{6 - 2x} \ge 0$, $f(x) \ge 1$, y el valor $1$ se alcanza en $x = 3$; a medida que $x \to -\infty$ el radicando crece sin tope, así que la imagen es $[1, +\infty)$. No tiene ceros (nunca vale menos de $1$). Su gráfico es el de $\sqrt{x}$ reflejado, estirado y desplazado (lo vemos en [transformaciones](/analisis-matematico-i/unidad-1/teoria/algebra-y-transformaciones/)).

### Ejemplo 4 · Valor absoluto como función por tramos

Escribir $g(x) = |2x - 6|$ por tramos y resolver $g(x) = 4$.

$2x - 6 \ge 0 \iff x \ge 3$. Entonces
<!-- check: U1.T.ELE.4 -->
$$
g(x) = \begin{cases} 2x - 6 & \text{si } x \ge 3, \\ 6 - 2x & \text{si } x < 3. \end{cases}
$$
Además $g(x) = 2|x - 3|$: una «V» de vértice $(3, 0)$ y pendientes $\pm 2$. Para $g(x) = 4$: $2x - 6 = 4$ da $x = 5$ (cumple $x \ge 3$) y $6 - 2x = 4$ da $x = 1$ (cumple $x < 3$). La imagen es $[0, +\infty)$.

## Funciones trascendentes

Son las que no son algebraicas: exponenciales, logarítmicas y trigonométricas (con sus inversas).

### Exponencial

$f(x) = a^x$, con $a > 0$ y $a \ne 1$. Dominio $\mathbb{R}$, imagen $(0, +\infty)$, pasa por $(0, 1)$, **no tiene ceros**, es estrictamente creciente si $a > 1$ y decreciente si $0 < a < 1$. Tiene asíntota horizontal $y = 0$ (hacia la izquierda si $a > 1$, hacia la derecha si $a < 1$). No tiene paridad. El caso $a = e \approx 2{,}71828$ es la **exponencial natural** $e^x$. Propiedades: $a^{x + y} = a^x a^y$, $(a^x)^y = a^{xy}$, $a^{-x} = 1/a^x$.

### Logaritmo

$y = \log_a x \iff a^y = x$, con $a > 0$, $a \ne 1$. Es la **inversa** de la exponencial (lo justificamos en [inversa](/analisis-matematico-i/unidad-1/teoria/inversa/)). Dominio $(0, +\infty)$, imagen $\mathbb{R}$, único cero en $x = 1$, asíntota vertical $x = 0$, creciente si $a > 1$ y decreciente si $0 < a < 1$. Se escribe $\ln x = \log_e x$ y $\log x = \log_{10} x$. Para $x, y > 0$:

$$
\log_a(xy) = \log_a x + \log_a y, \quad \log_a\frac{x}{y} = \log_a x - \log_a y, \quad \log_a x^n = n\log_a x, \quad \log_a x = \frac{\ln x}{\ln a}.
$$

La condición $x, y > 0$ importa: $\ln(x^2) = 2\ln|x|$, que **no** es $2\ln x$ si $x < 0$.

![Gráficos de 2ˣ y log₂ x, simétricos respecto de la recta y = x.](/analisis-matematico-i/figuras/u1-exp-log.svg)

*Observá que los dos gráficos son reflejos uno del otro respecto de la recta punteada $y = x$: el punto $(0, 1)$ de la exponencial se corresponde con $(1, 0)$ del logaritmo, y la asíntota $y = 0$ con la asíntota $x = 0$.*

### Trigonométricas

Con $x$ en radianes. $\operatorname{sen}$ y $\cos$ tienen dominio $\mathbb{R}$, imagen $[-1, 1]$ y **período** $2\pi$ (es decir, $f(x + 2\pi) = f(x)$); $\operatorname{sen}$ es impar y $\cos$ es par. Ceros: $\operatorname{sen} x = 0 \iff x = k\pi$; $\cos x = 0 \iff x = \frac{\pi}{2} + k\pi$, con $k \in \mathbb{Z}$. La tangente $\tan x = \dfrac{\operatorname{sen} x}{\cos x}$ tiene dominio $\mathbb{R} \setminus \{\frac{\pi}{2} + k\pi\}$, imagen $\mathbb{R}$, período $\pi$, es impar y tiene asíntotas verticales en cada $x = \frac{\pi}{2} + k\pi$. Identidad fundamental: $\operatorname{sen}^2 x + \cos^2 x = 1$.

![Gráficos de sen x y cos x entre −2π y 2π.](/analisis-matematico-i/figuras/u1-trigonometricas.svg)

*Observá que las dos curvas oscilan entre $-1$ y $1$ y se repiten cada $2\pi$; el coseno es el seno desplazado $\frac{\pi}{2}$ hacia la izquierda.*

Para $y = A\operatorname{sen}(Bx) + D$ (y lo mismo con $\cos$), la **amplitud** es $|A|$, el **período** $\dfrac{2\pi}{|B|}$ y la imagen $[D - |A|, D + |A|]$.

### Trigonométricas inversas

Como $\operatorname{sen}$, $\cos$ y $\tan$ no son inyectivas en todo $\mathbb{R}$, se las **restringe** a un intervalo donde sí lo son (la justificación está en la lección de la [inversa](/analisis-matematico-i/unidad-1/teoria/inversa/)):

| Función | Dominio | Imagen | Es la inversa de |
|---|---|---|---|
| $\operatorname{arcsen} x$ | $[-1, 1]$ | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ | $\operatorname{sen}$ en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| $\arccos x$ | $[-1, 1]$ | $[0, \pi]$ | $\cos$ en $[0, \pi]$ |
| $\arctan x$ | $\mathbb{R}$ | $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ | $\tan$ en $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |

$\operatorname{arcsen} y$ es **el único** ángulo del intervalo $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ cuyo seno es $y$. Por eso $\operatorname{sen}(\operatorname{arcsen} y) = y$ para todo $y \in [-1, 1]$, pero $\operatorname{arcsen}(\operatorname{sen} x) = x$ **solo** si $x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$.

### Ejemplo 5 · Exponenciales y logaritmos

a) Resolver $2^{x + 1} = 20$. b) Resolver $\ln(x - 1) + \ln(x + 1) = \ln 8$.

<!-- check: U1.T.ELE.5 -->
a) Aplicamos $\log_2$: $x + 1 = \log_2 20$, entonces $x = \log_2 20 - 1 = \dfrac{\ln 20}{\ln 2} - 1 \approx 3{,}32$.

b) El dominio exige $x - 1 > 0$ y $x + 1 > 0$: $x > 1$. Por la propiedad del producto, $\ln\big[(x - 1)(x + 1)\big] = \ln 8$, y como el logaritmo es inyectivo, $x^2 - 1 = 8$, de donde $x = 3$ o $x = -3$. Solo $x = 3$ pertenece al dominio: $\ln 2 + \ln 4 = \ln 8$. La solución $x = -3$ es **extraña**: apareció al combinar los logaritmos, que cambia el dominio.

### Ejemplo 6 · Función trigonométrica con amplitud y período

Analizar $y = 2\cos\left(\dfrac{\pi}{3}x\right) + 1$ en $[0, 6]$.

<!-- check: U1.T.ELE.6 -->
Amplitud $2$, período $\dfrac{2\pi}{\pi/3} = 6$, nivel medio $1$: imagen $[-1, 3]$. Los ceros: $\cos\left(\frac{\pi}{3}x\right) = -\frac12$ con $\frac{\pi}{3}x \in [0, 2\pi]$ da $\frac{\pi}{3}x = \frac{2\pi}{3}$ o $\frac{4\pi}{3}$, es decir, $x = 2$ o $x = 4$. Máximo $3$ en $x = 0$ y $x = 6$; mínimo $-1$ en $x = 3$.

### Ejemplo 7 · Valores de las inversas trigonométricas

Calcular: a) $\operatorname{arcsen}\left(-\tfrac12\right)$; b) $\arccos\left(-\tfrac12\right)$; c) $\arctan 1$; d) $\operatorname{arcsen}\left(\operatorname{sen}\tfrac{7\pi}{6}\right)$.

<!-- check: U1.T.ELE.7 -->
a) Buscamos el ángulo en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ con seno $-\frac12$: $-\frac{\pi}{6}$.
b) El ángulo en $[0, \pi]$ con coseno $-\frac12$: $\frac{2\pi}{3}$.
c) El ángulo en $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ con tangente $1$: $\frac{\pi}{4}$.
d) $\operatorname{sen}\frac{7\pi}{6} = -\frac12$, y $\frac{7\pi}{6}$ **no** está en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, así que no vale «$=\frac{7\pi}{6}$»: $\operatorname{arcsen}\left(-\frac12\right) = -\frac{\pi}{6}$.

:::caution[Errores frecuentes]
- Olvidar que $\sqrt{x^2} = |x|$ y que la raíz cuadrada es siempre $\ge 0$.
- Confundir $(\ln x)^2$ con $\ln x^2$ y $\log_a(x + y)$ con $\log_a x + \log_a y$ (no hay propiedad de la suma).
- Resolver una ecuación logarítmica sin verificar el dominio: aparecen soluciones extrañas.
- Decir que $\operatorname{arcsen}(\operatorname{sen} x) = x$ siempre.
- Usar grados en las fórmulas: en análisis los ángulos van en **radianes**.
- Calcular la imagen de una homográfica sin excluir el valor de la asíntota horizontal.
:::

## Ejercicios

### Ejercicio 10 · Parábola a partir de su vértice
<!-- ejercicio: U1.10 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Una parábola tiene vértice en $(2, -3)$ y pasa por $(0, 5)$. Hallar $f$ en forma canónica y polinómica, la imagen, los ceros y la ordenada al origen.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con el vértice conocido, la forma canónica $a(x - 2)^2 - 3$ deja un solo parámetro, que se despeja con el punto.

**Desarrollo.** $f(0) = a(0 - 2)^2 - 3 = 4a - 3 = 5 \Rightarrow a = 2$. Entonces $f(x) = 2(x - 2)^2 - 3 = 2x^2 - 8x + 5$. Como $a > 0$, la imagen es $[-3, +\infty)$. Ceros: $2(x - 2)^2 = 3 \Rightarrow x = 2 \pm \sqrt{\tfrac32}$. La ordenada al origen es $f(0) = 5$.

**Resultado.** $f(x) = 2(x-2)^2 - 3 = 2x^2 - 8x + 5$; $\operatorname{Im} f = [-3, +\infty)$; ceros $2 \pm \sqrt{3/2} = 2 \pm \frac{\sqrt6}{2}$; $f(0) = 5$.

</details>

### Ejercicio 11 · Función por tramos
<!-- ejercicio: U1.11 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea
$$
f(x) = \begin{cases} 2^x - 3 & \text{si } x \le 1, \\ 4 - x^2 & \text{si } x > 1. \end{cases}
$$
Hallar dominio, imagen y ceros.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Imagen de cada tramo, y después la unión; ceros dentro de cada tramo.

**Desarrollo.** El dominio es $(-\infty, 1] \cup (1, +\infty) = \mathbb{R}$.

*Primer tramo* ($x \le 1$): $2^x$ es creciente con imagen $(0, 2]$ en $(-\infty, 1]$; entonces $2^x - 3$ toma los valores de $(-3, -1]$. Cero: $2^x = 3 \Rightarrow x = \log_2 3 \approx 1{,}58$, que **no** cumple $x \le 1$: sin ceros en este tramo.

*Segundo tramo* ($x > 1$): $4 - x^2$ es decreciente para $x > 1$, con valores en $(-\infty, 3)$ (en $x \to 1^+$ se acerca a $3$ sin alcanzarlo). Cero: $x^2 = 4$, $x = 2$ (cumple $x > 1$) o $x = -2$ (no cumple).

Unión de imágenes: $(-3, -1] \cup (-\infty, 3) = (-\infty, 3)$.

**Resultado.** $D_f = \mathbb{R}$, $\operatorname{Im} f = (-\infty, 3)$, $C_0 = \{2\}$.

</details>

### Ejercicio 12 · Ecuación logarítmica
<!-- ejercicio: U1.12 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Resolver $\log_2(x + 1) + \log_2(x - 3) = 5$, indicando el dominio y descartando las soluciones extrañas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Determinar el dominio, combinar los logaritmos, pasar a forma exponencial y verificar.

**Desarrollo.** El dominio exige $x + 1 > 0$ y $x - 3 > 0$, es decir, $x > 3$. Por la propiedad del producto, $\log_2\big[(x + 1)(x - 3)\big] = 5$, o sea $(x + 1)(x - 3) = 2^5 = 32$. Entonces $x^2 - 2x - 3 = 32$, $x^2 - 2x - 35 = 0$ y $(x - 7)(x + 5) = 0$: $x = 7$ o $x = -5$. Solo $x = 7$ cumple $x > 3$. Verificación: $\log_2 8 + \log_2 4 = 3 + 2 = 5$.

**Resultado.** $x = 7$; $x = -5$ es extraña.

</details>

### Ejercicio 13 · Inversas trigonométricas
<!-- ejercicio: U1.13 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) Calcular $\cos\left(\operatorname{arcsen}\tfrac35\right)$ y $\tan\left(\arccos\left(-\tfrac13\right)\right)$.
b) Calcular $\operatorname{arcsen}\left(\operatorname{sen}\tfrac{11\pi}{6}\right)$.
c) Hallar dominio e imagen de $g(x) = \dfrac{\pi}{2} - 2\arctan x$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Llamar $\theta$ al ángulo de la inversa, ubicarlo en su intervalo para fijar el signo, y usar $\operatorname{sen}^2 + \cos^2 = 1$.

**Desarrollo.** a) Sea $\theta = \operatorname{arcsen}\frac35 \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$: $\cos\theta \ge 0$, entonces $\cos\theta = \sqrt{1 - \frac{9}{25}} = \frac45$.
Sea $\varphi = \arccos\left(-\frac13\right) \in [0, \pi]$, con $\cos\varphi = -\frac13 < 0$, así que $\varphi \in \left(\frac{\pi}{2}, \pi\right)$ y $\operatorname{sen}\varphi > 0$: $\operatorname{sen}\varphi = \sqrt{1 - \frac19} = \frac{2\sqrt2}{3}$. Entonces $\tan\varphi = \dfrac{2\sqrt2/3}{-1/3} = -2\sqrt2$.

b) $\frac{11\pi}{6}$ está fuera de $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$. Como $\frac{11\pi}{6} = 2\pi - \frac{\pi}{6}$, $\operatorname{sen}\frac{11\pi}{6} = -\frac12$ y $\operatorname{arcsen}\left(-\frac12\right) = -\frac{\pi}{6}$.

c) $\arctan x$ está definida en todo $\mathbb{R}$ con imagen $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. Entonces $2\arctan x \in (-\pi, \pi)$ y $-2\arctan x \in (-\pi, \pi)$, de donde $g(x) \in \left(-\frac{\pi}{2}, \frac{3\pi}{2}\right)$. Los valores extremos no se alcanzan.

**Resultado.** a) $\frac45$ y $-2\sqrt2$; b) $-\frac{\pi}{6}$; c) $D_g = \mathbb{R}$, $\operatorname{Im} g = \left(-\frac{\pi}{2}, \frac{3\pi}{2}\right)$.

</details>

## Autoevaluación

**1. ¿Qué dos números definen el centro de la hipérbola $\dfrac{ax + b}{cx + d}$?**

<details>
<summary>Respuesta</summary>

El centro es $\left(-\dfrac{d}{c}, \dfrac{a}{c}\right)$, el cruce de las asíntotas.
</details>

**2. ¿Por qué $\log_a x$ no está definido para $x \le 0$?**

<details>
<summary>Respuesta</summary>

Porque $a^y > 0$ para todo $y$: ninguna potencia de $a$ da un número negativo o cero.
</details>

**3. ¿Cuál es el período de $y = \operatorname{sen}(4x)$?**

<details>
<summary>Respuesta</summary>

$\dfrac{2\pi}{4} = \dfrac{\pi}{2}$.
</details>

**4. ¿Cuánto vale $\operatorname{arccos}(\cos 2\pi)$?**

<details>
<summary>Respuesta</summary>

$\cos 2\pi = 1$ y $\arccos 1 = 0$, no $2\pi$ (porque $2\pi \notin [0, \pi]$).
</details>

:::tip[En resumen]
- Algebraicas: lineal (recta), cuadrática (parábola), polinómicas, racionales (hipérbola en el caso homográfico), irracionales y valor absoluto; cada una con su dominio, imagen y ceros característicos.
- Exponencial $a^x$: dominio $\mathbb{R}$, imagen $(0, +\infty)$, asíntota $y = 0$. Logaritmo: dominio $(0, +\infty)$, imagen $\mathbb{R}$, asíntota $x = 0$. Son inversas.
- Seno y coseno: período $2\pi$, imagen $[-1, 1]$; en $A\operatorname{sen}(Bx) + D$, amplitud $|A|$, período $2\pi/|B|$.
- Las trigonométricas inversas se definen restringiendo el dominio; $\operatorname{arcsen}(\operatorname{sen} x) = x$ solo en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$.
:::

**Para seguir.** Ahora que conocés el catálogo, vemos cómo **combinar** funciones y cómo **transformar** sus gráficos: [álgebra de funciones y transformaciones](/analisis-matematico-i/unidad-1/teoria/algebra-y-transformaciones/). En la [guía de GeoGebra](/analisis-matematico-i/geogebra/funciones/) encontrás cómo graficar cada una.
