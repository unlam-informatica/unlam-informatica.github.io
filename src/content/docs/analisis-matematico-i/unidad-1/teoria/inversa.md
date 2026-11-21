---
title: Funciones biyectivas y función inversa
description: Inyectividad, sobreyectividad y biyectividad; cómo restringir dominio o codominio, cómo hallar la función inversa y por qué su gráfico es el reflejo respecto de y = x.
slug: analisis-matematico-i/unidad-1/teoria/inversa
sidebar:
  order: 5
---

## Qué vas a aprender

- Probar inyectividad y sobreyectividad (analítica y gráficamente) y restringir dominio o codominio para obtener una biyección.
- Hallar la inversa de una función biyectiva, su dominio e imagen, y relacionar los gráficos por simetría respecto de $y = x$.

## Antes de empezar

Necesitás la [terna de una función](/analisis-matematico-i/unidad-1/teoria/funciones-y-modelos/), la [composición](/analisis-matematico-i/unidad-1/teoria/algebra-y-transformaciones/) y las [funciones elementales](/analisis-matematico-i/unidad-1/teoria/funciones-elementales/).

## Introducción

Si $T = 1{,}8\,C + 32$ convierte grados Celsius a Fahrenheit, siempre se puede «deshacer»: dada $T$, hay un único $C$. Eso no pasa con todas las funciones: dado $y = x^2 = 4$, no sabemos si $x$ era $2$ o $-2$. La inversa existe exactamente cuando cada valor de llegada viene de **un único** valor de partida, y de **alguno**.

## Inyectividad, sobreyectividad y biyectividad

:::note[Definición]
Sea $f\colon A \to B$.

- $f$ es **inyectiva** si elementos distintos tienen imágenes distintas: $x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)$. Equivalentemente (contrarrecíproco): $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$.
- $f$ es **sobreyectiva** si todo elemento del codominio es imagen de alguno: $\operatorname{Im} f = B$.
- $f$ es **biyectiva** si es inyectiva y sobreyectiva.
:::

**Test de la recta horizontal.** $f$ es inyectiva si y solo si toda recta horizontal corta al gráfico **a lo sumo una vez**. Es sobreyectiva si toda recta horizontal $y = k$, con $k \in B$, lo corta **al menos una vez**.

![Parábola f(x) = x² − 4x con la recta horizontal y = 0 que la corta en x = 0 y x = 4.](/analisis-matematico-i/figuras/u1-no-inyectiva.svg)

*Observá que la recta $y = 0$ corta dos veces: $f(0) = f(4) = 0$ con $0 \ne 4$. El eje de simetría $x = 2$ marca dónde habría que cortar el dominio.*

**Método analítico.** Para probar inyectividad se supone $f(x_1) = f(x_2)$ y se deduce $x_1 = x_2$. Para refutarla basta **un par** $x_1 \ne x_2$ con igual imagen. Para probar sobreyectividad se toma $y \in B$ y se resuelve $f(x) = y$ viendo que tiene solución en $A$.

:::note[Propiedad]
Si $f$ es **estrictamente creciente** (o estrictamente decreciente) en su dominio, entonces es inyectiva.
:::

**Demostración (formal).** Si $x_1 \ne x_2$, digamos $x_1 < x_2$, y $f$ es estrictamente creciente, entonces $f(x_1) < f(x_2)$, en particular $f(x_1) \ne f(x_2)$. El caso decreciente es igual. $\blacksquare$

La recíproca es falsa en general (una función inyectiva puede no ser monótona si tiene saltos), pero sí vale para las funciones continuas **definidas en un intervalo**. Si el dominio no es un intervalo, tampoco alcanza la continuidad: la homográfica del ejemplo 1 es continua e inyectiva en $\mathbb{R}-\lbrace 3\rbrace$ y no es monótona en todo su dominio (crece o decrece en cada rama por separado).

### Ejemplo 1 · Inyectividad analítica

Probar que $f(x) = \dfrac{2x + 1}{x - 3}$, con dominio $\mathbb{R} \setminus \{3\}$, es inyectiva.

<!-- check: U1.T.INV.1 -->
Suponemos $f(a) = f(b)$ con $a, b \ne 3$: $\dfrac{2a + 1}{a - 3} = \dfrac{2b + 1}{b - 3}$. Multiplicando cruzado, $(2a + 1)(b - 3) = (2b + 1)(a - 3)$. Desarrollando: $2ab - 6a + b - 3 = 2ab - 6b + a - 3$, de donde $-7a + 7b = 0$ y $a = b$. Luego $f$ es inyectiva.

### Cómo forzar una biyección

- Si **no es inyectiva**: se **restringe el dominio** a un conjunto donde lo sea.
- Si **no es sobreyectiva**: se **redefine el codominio** igualándolo a la imagen.

### Ejemplo 2 · Restringir una parábola

$f(x) = x^2 - 4x = (x - 2)^2 - 4$ no es inyectiva en $\mathbb{R}$ (figura anterior). Restringimos a $[2, +\infty)$, donde es estrictamente creciente, y fijamos como codominio su imagen $[-4, +\infty)$:

<!-- check: U1.T.INV.2 -->
$$
f\colon [2, +\infty) \to [-4, +\infty) \,/\, f(x) = x^2 - 4x \quad \text{(biyectiva)}.
$$

Para hallar la inversa: $y = (x - 2)^2 - 4 \Rightarrow (x - 2)^2 = y + 4$. Como en el dominio $x - 2 \ge 0$, tomamos la raíz positiva: $x = 2 + \sqrt{y + 4}$. Entonces

$$
f^{-1}\colon [-4, +\infty) \to [2, +\infty) \,/\, f^{-1}(x) = 2 + \sqrt{x + 4}.
$$

Si se hubiese restringido a $(-\infty, 2]$, la inversa sería $2 - \sqrt{x + 4}$: **la elección del dominio determina la inversa**.

## Función inversa

:::note[Definición]
Si $f\colon A \to B$ es biyectiva, la **función inversa** es la única función $f^{-1}\colon B \to A$ tal que
$$
f^{-1}(y) = x \iff f(x) = y.
$$
Cumple $f^{-1}\big(f(x)\big) = x$ para todo $x \in A$ y $f\big(f^{-1}(y)\big) = y$ para todo $y \in B$.
:::

Observá que $D_{f^{-1}} = \operatorname{Im} f = B$ y $\operatorname{Im} f^{-1} = D_f = A$: **dominio e imagen se intercambian**. Y $f^{-1}(x)$ **no** es $\dfrac{1}{f(x)}$.

**Por qué existe y es única.** Dado $y \in B$, la sobreyectividad garantiza algún $x$ con $f(x) = y$ y la inyectividad garantiza que es único; $f^{-1}(y)$ es ese $x$.

### Procedimiento

1. Verificar la biyectividad (restringir dominio y/o codominio si hace falta).
2. Escribir $y = f(x)$ y **despejar $x$** en función de $y$.
3. Intercambiar los nombres: $f^{-1}(x) = \dots$
4. Dar la terna completa: dominio $= \operatorname{Im} f$, codominio $= D_f$.
5. Comprobar con $f(f^{-1}(x)) = x$.

### Propiedad gráfica

:::note[Propiedad]
El gráfico de $f^{-1}$ es el **simétrico** del de $f$ respecto de la recta $y = x$.
:::

**Demostración (formal).** El punto $(a, b)$ está en el gráfico de $f$ si y solo si $b = f(a)$, es decir, si y solo si $a = f^{-1}(b)$, es decir, si y solo si $(b, a)$ está en el gráfico de $f^{-1}$. Pero el simétrico de $(a, b)$ respecto de $y = x$ es exactamente $(b, a)$. $\blacksquare$

![Gráficos de f(x) = x² − 1 en [0, ∞) y de su inversa √(x+1), simétricos respecto de y = x.](/analisis-matematico-i/figuras/u1-inversa-reflejo.svg)

*Observá que $(2, 3)$ está en $f$ y $(3, 2)$ en $f^{-1}$; los dos gráficos se cruzan sobre la recta $y = x$, que actúa como espejo: reflejar en ella intercambia las coordenadas de cada punto.*

### Ejemplo 3 · Inversa de una exponencial

$f\colon \mathbb{R} \to (3, +\infty)$, $f(x) = 2e^{x - 1} + 3$ es biyectiva (exponencial estrictamente creciente, con imagen $(3, +\infty)$). De $y = 2e^{x-1} + 3$: $e^{x - 1} = \dfrac{y - 3}{2}$, $x = 1 + \ln\dfrac{y - 3}{2}$.

<!-- check: U1.T.INV.3 -->
$$
f^{-1}\colon (3, +\infty) \to \mathbb{R} \,/\, f^{-1}(x) = 1 + \ln\frac{x - 3}{2}.
$$

### Ejemplo 4 · Inversa de una homográfica

Con $f(x) = \dfrac{2x + 1}{x - 3}$ del ejemplo 1: $y(x - 3) = 2x + 1 \Rightarrow x(y - 2) = 3y + 1 \Rightarrow x = \dfrac{3y + 1}{y - 2}$. La imagen de $f$ es $\mathbb{R} \setminus \{2\}$ (la asíntota horizontal $y = 2$ no se alcanza), así que

<!-- check: U1.T.INV.4 -->
$$
f\colon \mathbb{R} \setminus \{3\} \to \mathbb{R} \setminus \{2\}, \qquad f^{-1}\colon \mathbb{R} \setminus \{2\} \to \mathbb{R} \setminus \{3\}, \quad f^{-1}(x) = \frac{3x + 1}{x - 2}.
$$

La asíntota vertical de $f$ ($x = 3$) se vuelve la horizontal de $f^{-1}$ ($y = 3$), y viceversa.

### Ejemplo 5 · Inversa de una trigonométrica

$f(x) = 1 - 2\operatorname{sen} x$ en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$: ahí $\operatorname{sen}$ es creciente, así que $f$ es decreciente, con $f(-\frac{\pi}{2}) = 3$ y $f(\frac{\pi}{2}) = -1$. De $y = 1 - 2\operatorname{sen} x$: $\operatorname{sen} x = \dfrac{1 - y}{2}$ y, como $x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$, $x = \operatorname{arcsen}\dfrac{1 - y}{2}$.

<!-- check: U1.T.INV.5 -->
$$
f^{-1}\colon [-1, 3] \to \left[-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right] \,/\, f^{-1}(x) = \operatorname{arcsen}\frac{1 - x}{2}.
$$

### Inversa de una composición

:::note[Propiedad]
Si $f\colon A \to B$ y $g\colon B \to C$ son biyectivas (el codominio de $f$ es el dominio de $g$), entonces $g \circ f\colon A \to C$ es biyectiva y $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.
:::

**Demostración (formal).** $(f^{-1} \circ g^{-1})\big((g \circ f)(x)\big) = f^{-1}\big(g^{-1}(g(f(x)))\big) = f^{-1}(f(x)) = x$, y análogamente en el otro orden. $\blacksquare$ (Se «deshace» en orden inverso: primero lo último.)

### Ejemplo 6 · Inversa de una composición

<!-- check: U1.T.INV.6 -->
$f(x) = 2x + 1$ y $g(x) = x^3$. $(g \circ f)(x) = (2x + 1)^3$. De $y = (2x + 1)^3$: $2x + 1 = \sqrt[3]{y}$, $x = \dfrac{\sqrt[3]{y} - 1}{2}$. Coincide con $f^{-1}(g^{-1}(y))$, pues $g^{-1}(y) = \sqrt[3]{y}$ y $f^{-1}(u) = \dfrac{u - 1}{2}$.

### Ejemplo 7 · Valores de una inversa sin hallar su fórmula

<!-- check: U1.T.INV.7 -->
$f(x) = x^3 + x$ es estrictamente creciente (suma de dos crecientes), luego biyectiva de $\mathbb{R}$ en $\mathbb{R}$, pero despejar $x$ es difícil. Aun así, $f(2) = 10$ implica $f^{-1}(10) = 2$, y $f(-1) = -2$ implica $f^{-1}(-2) = -1$: se busca por tanteo el $x$ que da el valor pedido.

:::caution[Errores frecuentes]
- Escribir $f^{-1}(x) = \frac{1}{f(x)}$.
- Hallar la inversa sin verificar la biyectividad, o dar la fórmula sin dominio e imagen.
- Elegir la raíz con el signo equivocado al invertir una parábola restringida: depende de la rama.
- Olvidar que la imagen de una homográfica excluye la altura de su asíntota, y por eso el dominio de la inversa también.
- Confundir $f^{-1}$ con la «inversa» $x \mapsto -f(x)$ (opuesta) o $x \mapsto f(-x)$ (reflexión en $y$).
:::

## Ejercicios

### Ejercicio 18 · Tarifa y su inversa
<!-- ejercicio: U1.18 | nivel: inicial | tipo: modelado | verificacion: sympy -->

:::note[Enunciado]
Un taxi cobra $T(d) = 450 + 120\,d$ pesos por $d$ kilómetros, hasta $30$ km. Hallar la terna de $T$, la terna de su inversa e indicar cuántos kilómetros se recorrieron si se pagaron $1350$ pesos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Función lineal creciente: biyectiva sobre su imagen; despejar $d$.

**Desarrollo.** $T(0) = 450$ y $T(30) = 4050$, así que $T\colon [0, 30] \to [450, 4050]$. De $y = 450 + 120 d$: $d = \dfrac{y - 450}{120}$. Para $y = 1350$: $d = \dfrac{900}{120} = 7{,}5$.

**Resultado.** $T^{-1}\colon [450, 4050] \to [0, 30]$, $T^{-1}(x) = \dfrac{x - 450}{120}$; se recorrieron $7{,}5$ km.

</details>

### Ejercicio 19 · Restringir y invertir
<!-- ejercicio: U1.19 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = -x^2 + 6x - 5$. Probar que no es inyectiva en $\mathbb{R}$, restringirla a $[3, +\infty)$ y hallar su inversa con dominio e imagen.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Completar cuadrados para ubicar el vértice y la rama.

**Desarrollo.** $f(x) = -(x - 3)^2 + 4$, vértice $(3, 4)$. Es simétrica respecto de $x = 3$: $f(2) = f(4) = 3$ con $2 \ne 4$, así que no es inyectiva. En $[3, +\infty)$ es estrictamente decreciente con imagen $(-\infty, 4]$. De $y = 4 - (x - 3)^2$: $(x - 3)^2 = 4 - y$ y, como $x - 3 \ge 0$, $x = 3 + \sqrt{4 - y}$.

**Resultado.** $f\colon [3, +\infty) \to (-\infty, 4]$ biyectiva y $f^{-1}\colon (-\infty, 4] \to [3, +\infty)$, $f^{-1}(x) = 3 + \sqrt{4 - x}$.

</details>

### Ejercicio 20 · Una función que es su propia inversa
<!-- ejercicio: U1.20 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \dfrac{3x - 2}{x - 3}$.
a) Hallar su dominio e imagen y mostrar que es biyectiva de $\mathbb{R} \setminus \{3\}$ en $\mathbb{R} \setminus \{3\}$.
b) Probar que $f^{-1} = f$ y explicar qué significa para el gráfico.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reescribir como transformación de $1/x$; despejar $x$ de $y = f(x)$.

**Desarrollo.** a) $3x - 2 = 3(x - 3) + 7$, entonces $f(x) = 3 + \dfrac{7}{x - 3}$: dominio $\mathbb{R} \setminus \{3\}$, asíntota horizontal $y = 3$ que no se alcanza, imagen $\mathbb{R} \setminus \{3\}$. Inyectiva: $3 + \frac{7}{a - 3} = 3 + \frac{7}{b - 3} \Rightarrow a - 3 = b - 3 \Rightarrow a = b$. Sobreyectiva sobre $\mathbb{R} \setminus \{3\}$ por la imagen calculada.

b) De $y = \dfrac{3x - 2}{x - 3}$: $y(x - 3) = 3x - 2 \Rightarrow x(y - 3) = 3y - 2 \Rightarrow x = \dfrac{3y - 2}{y - 3}$. Es la misma expresión: $f^{-1}(x) = \dfrac{3x - 2}{x - 3} = f(x)$. Equivalente: $f(f(x)) = x$. Gráficamente, el gráfico es simétrico respecto de la recta $y = x$ (coincide con su propio reflejo); las dos asíntotas $x = 3$ e $y = 3$ se intercambian entre sí.

**Resultado.** $D_f = \operatorname{Im} f = \mathbb{R} \setminus \{3\}$; $f^{-1} = f$.

</details>

### Ejercicio 21 · Funciones monótonas y su inversa
<!-- ejercicio: U1.21 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $f\colon A \to B$ biyectiva y estrictamente creciente. Probar que $f^{-1}$ es estrictamente creciente.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Razonar por contradicción usando que $f$ conserva el orden.

**Desarrollo.** Sean $y_1 < y_2$ en $B$ y $x_i = f^{-1}(y_i)$, de modo que $f(x_i) = y_i$. Queremos $x_1 < x_2$. Si no fuera así, sería $x_1 \ge x_2$. Si $x_1 = x_2$ entonces $y_1 = f(x_1) = f(x_2) = y_2$, contradicción con $y_1 < y_2$. Si $x_1 > x_2$, como $f$ es estrictamente creciente, $y_1 = f(x_1) > f(x_2) = y_2$, también contradicción. Entonces $x_1 < x_2$, es decir, $f^{-1}(y_1) < f^{-1}(y_2)$.

**Resultado.** $f^{-1}$ es estrictamente creciente. (Análogamente, la inversa de una decreciente es decreciente.)

</details>

## Autoevaluación

**1. ¿Qué dos condiciones hacen falta para que exista $f^{-1}$?**

<details>
<summary>Respuesta</summary>

Que $f$ sea inyectiva y sobreyectiva (biyectiva) como función $A \to B$.
</details>

**2. Si $f\colon [0, 3] \to [1, 10]$ es biyectiva, ¿cuál es el dominio de $f^{-1}$?**

<details>
<summary>Respuesta</summary>

$[1, 10]$, la imagen de $f$.
</details>

**3. ¿Cuál es la inversa de $f(x) = x^2$ restringida a $(-\infty, 0]$?**

<details>
<summary>Respuesta</summary>

$f^{-1}(x) = -\sqrt{x}$ con dominio $[0, +\infty)$.
</details>

**4. El punto $(5, 2)$ está en el gráfico de $f$. ¿Qué punto está en el de $f^{-1}$?**

<details>
<summary>Respuesta</summary>

$(2, 5)$.
</details>

:::tip[En resumen]
- Inyectiva: valores distintos tienen imágenes distintas (recta horizontal corta a lo sumo una vez); sobreyectiva: imagen igual al codominio; biyectiva: ambas.
- Se fuerza la biyectividad restringiendo el dominio y/o igualando el codominio a la imagen; la rama elegida determina la inversa.
- $f^{-1}\colon B \to A$ intercambia dominio e imagen, y su gráfico es el reflejo del de $f$ respecto de $y = x$.
- Procedimiento: verificar, despejar $x$, intercambiar, dar la terna y comprobar. $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.
:::

**Para seguir.** Cerrá la unidad con los [integradores](/analisis-matematico-i/unidad-1/practica/integradores/) y el [resumen de la Unidad 1](/analisis-matematico-i/unidad-1/teoria/unidad-1/). La [Unidad 3](/analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa/) usa la inversa para derivar logaritmos y trigonométricas inversas. Para comprobar con software, mirá la [guía de GeoGebra](/analisis-matematico-i/geogebra/funciones/).
