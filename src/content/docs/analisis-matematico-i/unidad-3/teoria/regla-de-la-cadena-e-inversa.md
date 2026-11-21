---
title: Regla de la cadena e inversa
description: Derivada de una función compuesta (también con datos por tabla o por recta tangente), derivada de la función inversa con sus hipótesis y derivadas de las trigonométricas inversas.
slug: analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa
sidebar:
  order: 4
---

## Qué vas a aprender

- Descomponer una función como composición y derivarla con la regla de la cadena, incluso cuando de $f$ y $g$ solo se conocen datos puntuales (una tabla o una recta tangente).
- Calcular $(f^{-1})'(b)$ sin hallar $f^{-1}$, conociendo las hipótesis que lo permiten, y saber qué falla si no se cumplen.
- Derivar las funciones trigonométricas inversas.

**Antes de empezar.** Necesitás [las reglas de derivación](/analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion/), la [composición de funciones](/analisis-matematico-i/unidad-1/teoria/algebra-y-transformaciones/) y la [función inversa](/analisis-matematico-i/unidad-1/teoria/inversa/).

## Introducción

Las reglas de la lección anterior derivan sumas, productos y cocientes de funciones elementales, pero no una función como $\operatorname{sen}(x^2)$, $e^{3x}$ o $\sqrt{1 + x^2}$: son **composiciones**, en las que una función «se aplica a otra». Si la velocidad de un auto depende del régimen del motor y este de la posición del pedal, la rapidez con que cambia la velocidad respecto del pedal es el producto de dos rapideces. Esa es la idea de la regla de la cadena.

## La regla de la cadena

:::note[Teorema · Regla de la cadena]
**Hipótesis:** $g$ es derivable en $a$ y $f$ es derivable en $g(a)$.
**Tesis:** $f \circ g$ es derivable en $a$ y

$$
(f \circ g)'(a) = f'\bigl(g(a)\bigr)\,g'(a).
$$
:::

En notación de Leibniz, si $y = f(u)$ y $u = g(x)$, se escribe $\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$.

**Demostración (formal).** Sea $b = g(a)$. Definimos $\varepsilon(k) = \dfrac{f(b + k) - f(b)}{k} - f'(b)$ para $k \neq 0$ y $\varepsilon(0) = 0$. Como $f$ es derivable en $b$, $\varepsilon(k) \to 0$ cuando $k \to 0$, y para todo $k$ (también $k = 0$) vale $f(b + k) - f(b) = \bigl(f'(b) + \varepsilon(k)\bigr)\,k$. Tomemos $k = g(a + h) - g(a)$; como $g$ es continua en $a$, $k \to 0$ cuando $h \to 0$. Entonces

$$
\dfrac{f(g(a + h)) - f(g(a))}{h} = \bigl(f'(b) + \varepsilon(k)\bigr)\,\dfrac{g(a + h) - g(a)}{h} \xrightarrow[h \to 0]{} \bigl(f'(b) + 0\bigr)\,g'(a). \qquad \blacksquare
$$

La definición de $\varepsilon$ evita dividir por $g(a + h) - g(a)$, que puede ser $0$ para valores de $h$ arbitrariamente chicos (por ejemplo, si $g$ es constante en tramos).

**Cómo se aplica.** Se identifica la función **de afuera** $f$ y la **de adentro** $g$, se deriva la de afuera *evaluada en la de adentro* y se multiplica por la derivada de la de adentro. Si hay más capas, se repite de afuera hacia adentro:

$$
\bigl[f(g(h(x)))\bigr]' = f'\bigl(g(h(x))\bigr)\,g'\bigl(h(x)\bigr)\,h'(x).
$$

Consecuencias de uso permanente (con $u = u(x)$ derivable):

| Función | Derivada |
|---|---|
| $u^{\alpha}$ | $\alpha\,u^{\alpha - 1}\,u'$ |
| $e^{u}$ | $e^{u}\,u'$ |
| $a^{u}$ | $a^{u} \ln a\; u'$ |
| $\ln u$ | $\dfrac{u'}{u}$ |
| $\operatorname{sen} u$ | $\cos u\; u'$ |
| $\cos u$ | $-\operatorname{sen} u\; u'$ |
| $\tan u$ | $\dfrac{u'}{\cos^2 u}$ |

En particular, $(\ln\lvert x\rvert)' = \frac1x$ para $x \neq 0$: si $x < 0$, $\ln\lvert x\rvert = \ln(-x)$ y la cadena da $\frac{-1}{-x} = \frac1x$.

### Ejemplo 1 · Una potencia de un polinomio
<!-- check: U3.T.CAD.1 -->

Para $f(x) = (5x - 2)^7$ tomamos de afuera $F(u) = u^7$ y de adentro $u = 5x - 2$:

$$
f'(x) = 7\,(5x - 2)^6 \cdot 5 = 35\,(5x - 2)^6.
$$

### Ejemplo 2 · Una raíz
<!-- check: U3.T.CAD.2 -->

Para $f(x) = \sqrt{x^2 + 1} = (x^2 + 1)^{1/2}$, definida en todo $\mathbb{R}$:

$$
f'(x) = \dfrac{1}{2}(x^2 + 1)^{-1/2} \cdot 2x = \dfrac{x}{\sqrt{x^2 + 1}}.
$$

### Ejemplo 3 · Tres capas
<!-- check: U3.T.CAD.3 -->

Para $f(x) = \operatorname{sen}^2\!\bigl(e^{3x}\bigr) = \bigl[\operatorname{sen}(e^{3x})\bigr]^2$ las capas, de afuera hacia adentro, son $u^2$, $\operatorname{sen} v$, $e^w$ y $w = 3x$:

$$
f'(x) = 2\operatorname{sen}(e^{3x}) \cdot \cos(e^{3x}) \cdot e^{3x} \cdot 3 = 3e^{3x}\operatorname{sen}\bigl(2e^{3x}\bigr),
$$

donde se usó $2\operatorname{sen}\theta\cos\theta = \operatorname{sen} 2\theta$.

### Ejemplo 4 · Cadena junto con producto
<!-- check: U3.T.CAD.4 -->

Para $f(x) = x^2 e^{-x^2}$ usamos el producto y, para el segundo factor, la cadena con $u = -x^2$:

$$
f'(x) = 2x\,e^{-x^2} + x^2 \cdot e^{-x^2}\cdot(-2x) = 2x\,(1 - x^2)\,e^{-x^2}.
$$

## La regla de la cadena con datos puntuales

Muchas veces no se conocen las fórmulas de $f$ y $g$, solo algunos valores. La cadena necesita únicamente **valores** de las funciones y de sus derivadas en los puntos adecuados. Una **recta tangente** a $f$ en $x = c$ de ecuación $y = mx + n$ informa dos datos: $f(c) = mc + n$ y $f'(c) = m$.

### Ejemplo 5 · Datos por tabla
<!-- check: U3.T.CAD.5 -->

De dos funciones derivables se conoce la tabla

| $x$ | $f(x)$ | $f'(x)$ | $g(x)$ | $g'(x)$ |
|---|---|---|---|---|
| $1$ | $2$ | $3$ | $3$ | $-2$ |
| $2$ | $1$ | $-1$ | $1$ | $4$ |
| $3$ | $3$ | $5$ | $2$ | $1$ |

Calculemos tres derivadas.

- $(f \circ g)'(1) = f'(g(1))\,g'(1) = f'(3)\cdot(-2) = 5 \cdot (-2) = -10$.
- $(g \circ f)'(2) = g'(f(2))\,f'(2) = g'(1)\cdot f'(2) = (-2)\cdot(-1) = 2$.
- $\left(\dfrac{f}{g}\right)'(2) = \dfrac{f'(2)\,g(2) - f(2)\,g'(2)}{g(2)^2} = \dfrac{(-1)\cdot 1 - 1 \cdot 4}{1^2} = -5$.

Observá que $(f \circ g)'(1)$ y $(g \circ f)'(1)$ son, en general, distintos: el orden de la composición importa.

### Ejemplo 6 · Datos por la recta tangente
<!-- check: U3.T.CAD.6 -->

La recta tangente a $f$ en $x = 2$ es $y = -x + 7$. Sea $h(x) = f(2x^2 - 6)$. Hallemos la tangente a $h$ en $x = 2$.

De la recta: $f(2) = -2 + 7 = 5$ y $f'(2) = -1$. La función de adentro es $u(x) = 2x^2 - 6$, con $u(2) = 2$ y $u'(x) = 4x$, $u'(2) = 8$. Por lo tanto

$$
h(2) = f(u(2)) = f(2) = 5, \qquad h'(2) = f'(u(2))\,u'(2) = f'(2) \cdot 8 = -8.
$$

La tangente a $h$ en $x = 2$ es $y = 5 - 8(x - 2)$.

## Derivada de la función inversa

Si $f$ transforma $a$ en $b = f(a)$, su inversa transforma $b$ en $a$, y las gráficas de $f$ y $f^{-1}$ son simétricas respecto de la recta $y = x$. Esa simetría intercambia los catetos de un triángulo pendiente, así que las pendientes de las tangentes en puntos simétricos son **inversas**.

:::note[Teorema · Derivada de la función inversa]
**Hipótesis:** $f$ es continua y estrictamente monótona en un intervalo $I$, derivable en $a \in I$ y $f'(a) \neq 0$.
**Tesis:** $f^{-1}$ es derivable en $b = f(a)$ y

$$
\bigl(f^{-1}\bigr)'(b) = \dfrac{1}{f'(a)} = \dfrac{1}{f'\bigl(f^{-1}(b)\bigr)}.
$$
:::

**Demostración (formal).** La hipótesis garantiza que $f$ es inyectiva y que $f^{-1}$ es continua en $f(I)$ (resultado que aceptamos: una función continua y estrictamente monótona en un intervalo tiene inversa continua). Para $y \neq b$ en $f(I)$ sea $x = f^{-1}(y)$; entonces $x \neq a$ (por inyectividad) y $x \to a$ cuando $y \to b$ (por la continuidad de $f^{-1}$). Luego

$$
\dfrac{f^{-1}(y) - f^{-1}(b)}{y - b} = \dfrac{x - a}{f(x) - f(a)} = \dfrac{1}{\dfrac{f(x) - f(a)}{x - a}} \xrightarrow[y \to b]{} \dfrac{1}{f'(a)},
$$

porque el denominador tiende a $f'(a) \neq 0$. $\blacksquare$

**Idea alternativa.** Si ya se sabe que $f^{-1}$ es derivable, se deriva con la cadena la identidad $f\bigl(f^{-1}(y)\bigr) = y$ y resulta $f'\bigl(f^{-1}(y)\bigr)\,(f^{-1})'(y) = 1$.

**Qué pasa si falla la hipótesis $f'(a) \neq 0$.** Sea $f(x) = x^3$, estrictamente creciente y derivable, con $f'(0) = 0$. Su inversa $f^{-1}(y) = \sqrt[3]{y}$ **no** es derivable en $y = 0$ (tiene tangente vertical): la fórmula daría $\frac{1}{0}$.

Atención al punto donde se evalúa: $(f^{-1})'(b)$ usa $f'$ en $a = f^{-1}(b)$, **no** en $b$.

### Ejemplo 7 · Derivada de la inversa sin hallar la inversa
<!-- check: U3.T.INV.1 -->

Sea $f(x) = x^5 + x^3 + x$. Como $f'(x) = 5x^4 + 3x^2 + 1 > 0$, $f$ es estrictamente creciente (criterio de monotonía: derivada positiva en un intervalo implica función estrictamente creciente en él) y tiene inversa. Calculemos $(f^{-1})'(3)$.

Hay que encontrar $a$ con $f(a) = 3$. Probando, $f(1) = 1 + 1 + 1 = 3$, luego $a = 1$ (única, por inyectividad). Entonces $f'(1) = 5 + 3 + 1 = 9$ y

$$
\bigl(f^{-1}\bigr)'(3) = \dfrac{1}{f'(1)} = \dfrac{1}{9}.
$$

### Ejemplo 8 · Tangente a la gráfica de la inversa
<!-- check: U3.T.INV.2 -->

Sea $f(x) = x + e^x$, con $f'(x) = 1 + e^x > 0$. Como $f(0) = 1$ y $f'(0) = 2$, la inversa pasa por $(1, 0)$ y $(f^{-1})'(1) = \frac12$. La tangente a la gráfica de $f^{-1}$ en ese punto es

$$
y = 0 + \dfrac{1}{2}(x - 1) = \dfrac{x - 1}{2}.
$$

Es la reflexión, respecto de $y = x$, de la tangente $y = 1 + 2x$ a $f$ en $(0, 1)$.

## Derivadas de las funciones trigonométricas inversas

Se obtienen de la fórmula de la inversa, restringiendo cada función trigonométrica a un intervalo donde es estrictamente monótona.

- **Arco seno.** $\operatorname{sen}$ restringido a $\left[-\frac\pi2, \frac\pi2\right]$ tiene inversa $\operatorname{arcsen}\colon [-1, 1] \to \left[-\frac\pi2, \frac\pi2\right]$. Para $x \in (-1, 1)$, con $y = \operatorname{arcsen} x$: $(\operatorname{arcsen})'(x) = \dfrac{1}{\cos y}$, y como $y \in \left(-\frac\pi2, \frac\pi2\right)$ tiene $\cos y > 0$, o sea $\cos y = \sqrt{1 - \operatorname{sen}^2 y} = \sqrt{1 - x^2}$.
- **Arco tangente.** Con $y = \arctan x$, $(\arctan)'(x) = \dfrac{1}{1/\cos^2 y} = \cos^2 y = \dfrac{1}{1 + \tan^2 y} = \dfrac{1}{1 + x^2}$.
- **Arco coseno.** Como $\arccos x = \frac\pi2 - \operatorname{arcsen} x$, la derivada es la opuesta de la del arco seno.

| $f(x)$ | $f'(x)$ | Dominio de $f'$ |
|---|---|---|
| $\operatorname{arcsen} x$ | $\dfrac{1}{\sqrt{1 - x^2}}$ | $(-1, 1)$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1 - x^2}}$ | $(-1, 1)$ |
| $\arctan x$ | $\dfrac{1}{1 + x^2}$ | $\mathbb{R}$ |

En $x = \pm 1$, $\operatorname{arcsen}$ y $\arccos$ tienen tangente vertical: la tangente a $\operatorname{sen}$ en $\pm\frac\pi2$ es horizontal, justo la excepción $f'(a) = 0$ del teorema.

### Ejemplo 9 · Arco tangente de una función
<!-- check: U3.T.INV.3 -->

Para $f(x) = \arctan(3x)$, la cadena con $u = 3x$ da

$$
f'(x) = \dfrac{1}{1 + (3x)^2} \cdot 3 = \dfrac{3}{1 + 9x^2}.
$$

### Ejemplo 10 · Arco seno de una raíz
<!-- check: U3.T.INV.4 -->

Para $f(x) = \operatorname{arcsen}\sqrt{x}$ con $0 < x < 1$:

$$
f'(x) = \dfrac{1}{\sqrt{1 - (\sqrt{x})^2}} \cdot \dfrac{1}{2\sqrt{x}} = \dfrac{1}{2\sqrt{x}\,\sqrt{1 - x}}.
$$

### Ejemplo 11 · Una identidad que se prueba derivando
<!-- check: U3.T.INV.5 -->

Sea $\varphi(x) = \arctan x + \arctan\dfrac{1}{x}$ para $x \neq 0$. Entonces

$$
\varphi'(x) = \dfrac{1}{1 + x^2} + \dfrac{1}{1 + 1/x^2}\cdot\left(-\dfrac{1}{x^2}\right) = \dfrac{1}{1 + x^2} - \dfrac{1}{x^2 + 1} = 0.
$$

Una función con derivada nula en un intervalo es constante en él (otra consecuencia del [teorema del valor medio](/analisis-matematico-i/unidad-4/teoria/termino-complementario/), que se demuestra en la Unidad 4); así, $\varphi$ es constante en $(0, +\infty)$ y en $(-\infty, 0)$ (aunque no necesariamente la misma constante). Con $x = 1$, $\varphi = \frac\pi4 + \frac\pi4 = \frac\pi2$; con $x = -1$, $\varphi = -\frac\pi2$.

:::caution[Errores frecuentes]
- **Olvidar el factor de la derivada interna.** $(\operatorname{sen} 3x)' = 3\cos 3x$, no $\cos 3x$; $(e^{x^2})' = 2x\,e^{x^2}$, no $e^{x^2}$.
- **Evaluar $f'$ en el lugar equivocado.** En $(f \circ g)'(a)$ se evalúa $f'$ en $g(a)$, no en $a$.
- **Confundir $(f^{-1})'$ con $\frac{1}{f}$ o con $\frac{1}{f'(b)}$.** La fórmula correcta es $(f^{-1})'(b) = \frac{1}{f'(f^{-1}(b))}$, con $f'$ evaluada en la preimagen de $b$.
- **Aplicar la fórmula de la inversa con $f'(a) = 0$.** Si $f'(a) = 0$, la inversa no es derivable en $b$ (tangente vertical).
- **Elegir mal la capa exterior.** En $\operatorname{sen}^2 x$ la capa de afuera es el cuadrado; en $\operatorname{sen}(x^2)$, el seno. Resultados distintos: $2\operatorname{sen}x\cos x$ frente a $2x\cos(x^2)$.
:::

## Ejercicios

### Ejercicio 11 · Cadena en cuatro funciones
<!-- ejercicio: U3.11 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Derivá:

a) $f(x) = (3x^2 - 5x + 1)^4$.

b) $g(x) = e^{x^2 - 2x}$.

c) $h(x) = \ln(x^3 + 1)$. Indicá el dominio de $h$ y el de $h'$.

d) $k(t) = \operatorname{sen}\sqrt{t}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Identificar la función de afuera y la de adentro, derivar la de afuera evaluada en la de adentro y multiplicar por la derivada de la de adentro.

**Desarrollo.**

a) Afuera $u^4$, adentro $3x^2 - 5x + 1$: $f'(x) = 4(3x^2 - 5x + 1)^3(6x - 5)$.

b) Afuera $e^u$, adentro $x^2 - 2x$: $g'(x) = (2x - 2)\,e^{x^2 - 2x}$.

c) Afuera $\ln u$, adentro $x^3 + 1$: $h'(x) = \dfrac{3x^2}{x^3 + 1}$. El logaritmo exige $x^3 + 1 > 0$, o sea $x > -1$: $D_h = D_{h'} = (-1, +\infty)$.

d) Afuera $\operatorname{sen} u$, adentro $\sqrt{t}$, con $t > 0$: $k'(t) = \cos\sqrt{t}\cdot\dfrac{1}{2\sqrt{t}}$.

**Resultado.** a) $4(6x - 5)(3x^2 - 5x + 1)^3$; b) $(2x - 2)e^{x^2 - 2x}$; c) $\dfrac{3x^2}{x^3 + 1}$ en $(-1, +\infty)$; d) $\dfrac{\cos\sqrt{t}}{2\sqrt{t}}$ para $t > 0$.

</details>

### Ejercicio 12 · Cadena con una tabla
<!-- ejercicio: U3.12 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $f$ y $g$ derivables con los datos de la tabla.

| $x$ | $f(x)$ | $f'(x)$ | $g(x)$ | $g'(x)$ |
|---|---|---|---|---|
| $1$ | $2$ | $3$ | $3$ | $-2$ |
| $2$ | $1$ | $-1$ | $1$ | $4$ |
| $3$ | $3$ | $5$ | $2$ | $1$ |

Calculá: a) $(g \circ f)'(1)$; b) $(f \circ g)'(2)$ y la ecuación de la recta tangente a $f \circ g$ en $x = 2$; c) $\left(\dfrac{f}{g}\right)'(3)$; d) $H'(3)$ si $H(x) = f(x)^2\,g(x)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Aplicar la regla correspondiente y leer de la tabla solo los valores que esa regla necesita.

**Desarrollo.**

a) $(g \circ f)'(1) = g'(f(1))\,f'(1)$. Primero se busca $f(1) = 2$ (columna $f$, fila $1$) y después $g'$ en ese valor: $g'(2) = 4$. Entonces $(g \circ f)'(1) = 4 \cdot 3 = 12$.

b) $(f \circ g)'(2) = f'(g(2))\,g'(2) = f'(1)\,g'(2) = 3 \cdot 4 = 12$. Para la recta tangente hace falta además el punto: $(f \circ g)(2) = f(g(2)) = f(1) = 2$, de modo que la tangente es $y = 2 + 12(x - 2)$.

c) Como $g(3) = 2 \neq 0$, vale la regla del cociente: $\left(\dfrac{f}{g}\right)'(3) = \dfrac{f'(3)\,g(3) - f(3)\,g'(3)}{g(3)^2} = \dfrac{5 \cdot 2 - 3 \cdot 1}{2^2} = \dfrac{7}{4}$.

d) $H'(x) = 2f(x)f'(x)\,g(x) + f(x)^2 g'(x)$ (cadena en $f^2$ y producto). En $x = 3$: $H'(3) = 2\cdot 3\cdot 5\cdot 2 + 9 \cdot 1 = 60 + 9 = 69$.

**Resultado.** a) $12$; b) $12$ y $y = 2 + 12(x - 2)$; c) $\dfrac{7}{4}$; d) $69$.

</details>

### Ejercicio 13 · Derivada de la inversa
<!-- ejercicio: U3.13 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = 2x^3 + 3x$.

a) Justificá que $f$ tiene inversa en $\mathbb{R}$.

b) Calculá $(f^{-1})'(5)$ y $(f^{-1})'(0)$ sin hallar $f^{-1}$.

c) Hallá la ecuación de la recta tangente a la gráfica de $f^{-1}$ en $x = 5$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Verificar las hipótesis (monotonía y $f' \neq 0$), hallar la preimagen de cada valor y aplicar $(f^{-1})'(b) = 1/f'(f^{-1}(b))$.

**Desarrollo.**

a) $f'(x) = 6x^2 + 3 > 0$ para todo $x$, entonces $f$ es estrictamente creciente, inyectiva y continua en $\mathbb{R}$, y $f'$ nunca se anula: se cumplen las hipótesis en todo punto.

b) $f(1) = 2 + 3 = 5$, luego $f^{-1}(5) = 1$ y $f'(1) = 9$: $(f^{-1})'(5) = \dfrac19$. Además $f(0) = 0$, $f^{-1}(0) = 0$ y $f'(0) = 3$: $(f^{-1})'(0) = \dfrac13$.

c) La gráfica de $f^{-1}$ pasa por $(5, 1)$ con pendiente $\frac19$: $y = 1 + \dfrac{1}{9}(x - 5)$.

**Resultado.** $(f^{-1})'(5) = \dfrac19$, $(f^{-1})'(0) = \dfrac13$; tangente $y = 1 + \dfrac{x - 5}{9}$.

</details>

### Ejercicio 14 · Una función cuya derivada es un arco seno
<!-- ejercicio: U3.14 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = x\operatorname{arcsen} x + \sqrt{1 - x^2}$, definida en $[-1, 1]$.

a) Probá que $f'(x) = \operatorname{arcsen} x$ para $x \in (-1, 1)$.

b) Hallá la recta tangente a la gráfica de $f$ en $x = \frac12$.

c) Escribí la derivada de $F(x) = f(x^2 - 1)$ en los puntos donde $x^2 - 1 \in (-1, 1)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Producto para el primer sumando, cadena para la raíz, y se espera una cancelación.

**Desarrollo.**

a) Para $x \in (-1, 1)$: $\bigl(x\operatorname{arcsen} x\bigr)' = \operatorname{arcsen} x + \dfrac{x}{\sqrt{1 - x^2}}$ y $\bigl(\sqrt{1 - x^2}\bigr)' = \dfrac{-2x}{2\sqrt{1 - x^2}} = -\dfrac{x}{\sqrt{1 - x^2}}$. Los términos con raíz se cancelan y $f'(x) = \operatorname{arcsen} x$.

b) $f\left(\tfrac12\right) = \tfrac12\cdot\tfrac\pi6 + \sqrt{1 - \tfrac14} = \tfrac{\pi}{12} + \tfrac{\sqrt3}{2}$ y $f'\left(\tfrac12\right) = \operatorname{arcsen}\tfrac12 = \tfrac\pi6$. La tangente es $y = \tfrac{\pi}{12} + \tfrac{\sqrt3}{2} + \tfrac\pi6\left(x - \tfrac12\right)$.

c) $F = f \circ u$ con $u(x) = x^2 - 1$. Se pide $u(x) \in (-1, 1)$, es decir $0 < x^2 < 2$, o sea $x \in (-\sqrt2, 0) \cup (0, \sqrt2)$; ahí se puede usar el inciso a) y la cadena: $F'(x) = f'(x^2 - 1)\cdot 2x = 2x\operatorname{arcsen}(x^2 - 1)$.

**Resultado.** a) $f'(x) = \operatorname{arcsen} x$; b) $y = \dfrac{\pi}{12} + \dfrac{\sqrt3}{2} + \dfrac\pi6\left(x - \dfrac12\right)$; c) $F'(x) = 2x\operatorname{arcsen}(x^2 - 1)$ para $0 < \lvert x \rvert < \sqrt2$.

</details>

## Autoevaluación

**1. ¿Cuál es la derivada de $\ln(\operatorname{sen} x)$? ¿Dónde vale?**

<details>
<summary>Respuesta</summary>

$\dfrac{\cos x}{\operatorname{sen} x} = \cot x$, en los $x$ donde $\operatorname{sen} x > 0$.
</details>

**2. Si $f(2) = 5$, $f'(2) = 3$ y $g(x) = f(x^2 - 2)$, ¿cuánto vale $g'(2)$?**

<details>
<summary>Respuesta</summary>

$g'(2) = f'(2^2 - 2)\cdot 4 = f'(2)\cdot 4 = 12$.
</details>

**3. ¿Por qué la fórmula de la inversa no sirve para $f(x) = x^3$ en $b = 0$?**

<details>
<summary>Respuesta</summary>

Porque $f'(0) = 0$: la inversa $\sqrt[3]{y}$ tiene tangente vertical en $0$ y no es derivable allí.
</details>

**4. Si $f'(a) = \frac{1}{4}$ y $f(a) = 7$, ¿cuál es la pendiente de la tangente a $f^{-1}$ en $(7, a)$?**

<details>
<summary>Respuesta</summary>

$4$, el inverso de $\frac14$.
</details>

:::tip[En resumen]
- Regla de la cadena: $(f \circ g)'(a) = f'(g(a))\,g'(a)$ si $g$ es derivable en $a$ y $f$ en $g(a)$. Se deriva de afuera hacia adentro; con datos puntuales solo hacen falta los valores en los puntos correctos.
- Inversa: si $f$ es continua y estrictamente monótona, derivable en $a$ con $f'(a) \neq 0$, entonces $(f^{-1})'(f(a)) = \frac{1}{f'(a)}$.
- $(\operatorname{arcsen} x)' = \frac{1}{\sqrt{1-x^2}}$, $(\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$ y $(\arctan x)' = \frac{1}{1+x^2}$.
:::

**Para seguir.** Con la cadena podemos derivar [funciones definidas implícitamente y potencias con exponente variable](/analisis-matematico-i/unidad-3/teoria/implicita-y-logaritmica/).
