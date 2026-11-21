---
title: Orden de contacto
description: Cuánto se parecen dos curvas cerca de un punto, y cómo se escribe un polinomio en potencias de (x − a) a partir de sus derivadas en a.
slug: analisis-matematico-i/unidad-4/teoria/orden-de-contacto
sidebar:
  order: 1
---

## Qué vas a aprender

- Definir el orden de contacto entre dos funciones en un punto y determinarlo comparando valores y derivadas sucesivas.
- Interpretar el orden de contacto geométricamente (corte, tangencia, igual concavidad) y relacionarlo con un límite.
- Reescribir un polinomio en potencias de $(x - a)$ usando sus derivadas en $a$, y deducir por qué los coeficientes son $\dfrac{P^{(k)}(a)}{k!}$.

**Antes de empezar.** Necesitás derivar con soltura funciones elementales, productos y composiciones ([reglas de derivación](/analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion/) y [regla de la cadena](/analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa/)), calcular derivadas sucesivas y manejar límites con la forma $\frac{0}{0}$ y la idea de [infinitésimo](/analisis-matematico-i/unidad-2/teoria/infinitesimos/).

## Introducción: aproximar una curva cerca de un punto

Una calculadora no sabe «calcular» $\operatorname{sen} 0{,}3$ ni $e^{0{,}2}$: solo suma, resta, multiplica y divide. Lo que hace es reemplazar la función por un **polinomio** que se le parece mucho cerca del punto donde se necesita el valor. Esa idea (cambiar una curva complicada por una simple que la imita localmente) se usa también para simplificar ecuaciones difíciles y para estimar errores.

Falta precisar qué significa «parecerse». Ya conocemos un primer nivel: la recta tangente a $f$ en $a$ es la recta que mejor «copia» a la gráfica en ese punto, porque coincide con $f$ en valor y en derivada. Si pedimos que también coincida la derivada segunda, la copia mejora; y así sucesivamente. El **orden de contacto** mide cuántos de esos niveles se cumplen.

## Orden de contacto

:::note[Definición · Orden de contacto]
Sean $f$ y $g$ funciones con derivadas hasta el orden $n + 1$ en $x = a$. Decimos que $f$ y $g$ tienen **contacto de orden $n$** en $x = a$ ($n$ entero, $n \ge 0$) si

$$
f(a) = g(a), \quad f'(a) = g'(a), \quad \dots, \quad f^{(n)}(a) = g^{(n)}(a), \qquad \text{pero} \qquad f^{(n+1)}(a) \neq g^{(n+1)}(a).
$$

Si las igualdades valen hasta el orden $n$ sin exigir nada sobre la derivada siguiente, decimos que el contacto es **al menos de orden $n$**.
:::

Dicho de otro modo: el orden de contacto es el mayor $n$ tal que las funciones y sus primeras $n$ derivadas coinciden en $a$. Si ya los valores $f(a)$ y $g(a)$ son distintos, las curvas no se tocan en $a$ y no hay contacto. Si coinciden todas las derivadas de todos los órdenes, el contacto no tiene un orden finito (pasa, por ejemplo, entre una función y ella misma).

### Ejemplo 1 · Una recta con contacto de orden 2
<!-- check: U4.T.CON.1 -->

Comparemos $f(x) = \operatorname{sen} x$ con la recta $g(x) = x$ en $a = 0$. Derivamos y evaluamos:

| $k$ | $f^{(k)}(0)$ | $g^{(k)}(0)$ | ¿Coinciden? |
|---|---|---|---|
| $0$ | $\operatorname{sen} 0 = 0$ | $0$ | sí |
| $1$ | $\cos 0 = 1$ | $1$ | sí |
| $2$ | $-\operatorname{sen} 0 = 0$ | $0$ | sí |
| $3$ | $-\cos 0 = -1$ | $0$ | **no** |

Coinciden hasta el orden $2$ y fallan en el orden $3$: el contacto es de **orden $2$**. Es notable: una recta puede tener contacto de orden 2 con una curva (aquí, porque $\operatorname{sen}$ tiene un punto de inflexión en el origen y su derivada segunda se anula).

### Ejemplo 2 · Contacto mayor que el grado
<!-- check: U4.T.CON.2 -->

Sea $f(x) = \cos x$ y $g(x) = 1 - \dfrac{x^2}{2} + \dfrac{x^4}{24}$, con $a = 0$. Las derivadas de $f$ en $0$ son, para $k = 0, 1, \dots, 6$: $1, 0, -1, 0, 1, 0, -1$. Las de $g$ en $0$ son $1, 0, -1, 0, 1, 0, 0$: la derivada sexta de un polinomio de grado $4$ es $0$. Las dos sucesiones coinciden hasta $k = 5$ y difieren en $k = 6$, de modo que el contacto es de **orden $5$**, mayor que el grado $4$ de $g$.

## Qué significa geométricamente

| Orden | Qué se cumple en $a$ | Cómo se ven las gráficas |
|---|---|---|
| $0$ | $f(a) = g(a)$ | Se cortan (o se tocan) en un punto; con otras pendientes. |
| $1$ | además $f'(a) = g'(a)$ | Tienen la **misma recta tangente**. |
| $2$ | además $f''(a) = g''(a)$ | Misma tangente y misma concavidad: se curvan igual. |
| $3, 4, \dots$ | además coinciden las derivadas siguientes | Se separan cada vez más lentamente al alejarse de $a$. |

![Gráfico de la exponencial junto a tres polinomios con contacto de orden 0, 1 y 2 en el origen](/analisis-matematico-i/figuras/u4-orden-contacto.svg)

*Los cuatro gráficos pasan por $(0, 1)$. Mirá cómo cada polinomio se despega de $e^x$ al alejarte del origen: la recta horizontal enseguida, la tangente $1 + x$ más tarde, y la parábola $1 + x + \frac{x^2}{2}$ casi no se distingue de la exponencial cerca del cero.*

Cuanto mayor es el orden de contacto, más pegadas están las curvas **en un entorno de $a$**. Esto no es una afirmación global: lejos de $a$, un polinomio de orden de contacto alto puede alejarse mucho de la función.

### Ejemplo 3 · El orden depende del punto
<!-- check: U4.T.CON.3 -->

Sean $f(x) = x^3$ y $g(x) = 3x - 2$. Vemos que $f(x) - g(x) = x^3 - 3x + 2 = (x - 1)^2 (x + 2)$: se cortan en $x = 1$ y en $x = -2$, y en $x = 1$ la raíz de la diferencia es doble.

- En $a = 1$: $f(1) = 1 = g(1)$ y $f'(1) = 3 = g'(1)$, pero $f''(1) = 6 \neq 0 = g''(1)$. Contacto de **orden $1$**: $g$ es la recta tangente a $f$ en $x = 1$.
- En $a = -2$: $f(-2) = -8 = g(-2)$ y $f'(-2) = 12 \neq 3 = g'(-2)$. Contacto de **orden $0$**: la recta corta a la cúbica, no es tangente.

Para dos polinomios, esto es general: el orden de contacto en $a$ es $n$ exactamente cuando $x = a$ es raíz **de multiplicidad $n + 1$** del polinomio $f - g$.

## Relación con el límite

El orden de contacto también se lee en el comportamiento de la diferencia $f(x) - g(x)$ cuando $x \to a$.

:::note[Teorema · Caracterización por límites]
Sean $f$ y $g$ con derivadas hasta el orden $n + 1$ en $a$. Entonces:

1. $f$ y $g$ tienen contacto de orden al menos $n$ en $a$ si y solo si $\displaystyle\lim_{x \to a} \dfrac{f(x) - g(x)}{(x - a)^n} = 0$.
2. En ese caso, $\displaystyle\lim_{x \to a} \dfrac{f(x) - g(x)}{(x - a)^{n+1}} = \dfrac{f^{(n+1)}(a) - g^{(n+1)}(a)}{(n + 1)!}$, que es distinto de cero exactamente cuando el contacto es de orden $n$.
:::

Es decir: si el contacto es de orden $n$, la diferencia $f - g$ es un [infinitésimo](/analisis-matematico-i/unidad-2/teoria/infinitesimos/) de orden $n + 1$ respecto de $(x - a)$: tiende a cero como $(x - a)^{n+1}$.

**Idea de la demostración.** Sea $h = f - g$. Si $h(a) = h'(a) = \dots = h^{(n)}(a) = 0$, el cociente $\frac{h(x)}{(x - a)^n}$ tiene la forma $\frac{0}{0}$; aplicando la regla de L'Hôpital $n - 1$ veces llegamos a $\lim \frac{h^{(n-1)}(x)}{n!\,(x - a)}$, que es $\frac{h^{(n)}(a)}{n!} = 0$ por la definición de derivada (porque $h^{(n-1)}(a) = 0$). El mismo argumento con $(x - a)^{n+1}$ en el denominador conduce a $\lim \frac{h^{(n)}(x)}{(n+1)!\,(x - a)} = \frac{h^{(n+1)}(a)}{(n+1)!}$, que es el valor del enunciado en 2. Recíprocamente, si $h(x)/(x - a)^n \to 0$ pero $m \le n$ fuera el primer orden con $h^{(m)}(a) \neq 0$, el mismo argumento daría $h(x)/(x - a)^m \to h^{(m)}(a)/m! \neq 0$ y entonces $h(x)/(x - a)^n$ no podría tender a $0$: contradicción.

### Ejemplo 4 · El límite confirma el orden
<!-- check: U4.T.CON.5 -->

En el ejemplo 1, $f - g = \operatorname{sen} x - x$ y $n = 2$. Los límites (por derecha y por izquierda coinciden) son

$$
\lim_{x \to 0} \dfrac{\operatorname{sen} x - x}{x^2} = 0, \qquad \lim_{x \to 0} \dfrac{\operatorname{sen} x - x}{x^3} = -\dfrac16 \neq 0,
$$

y el segundo valor coincide con $\dfrac{f'''(0) - g'''(0)}{3!} = \dfrac{-1 - 0}{6}$, tal como dice el teorema.

### Ejemplo 5 · Parámetros para un contacto dado
<!-- check: U4.T.CON.4 -->

Hallemos $a$ y $b$ para que $f(x) = \dfrac{1}{1 + 2x}$ y $g(x) = 1 + ax + bx^2$ tengan contacto de orden al menos $2$ en $x = 0$, y decidamos cuál es el orden exacto.

Las derivadas de $f$ en $0$: $f(0) = 1$, $f'(x) = -\dfrac{2}{(1 + 2x)^2}$, de modo que $f'(0) = -2$; $f''(x) = \dfrac{8}{(1 + 2x)^3}$, así que $f''(0) = 8$; $f'''(x) = -\dfrac{48}{(1 + 2x)^4}$ y $f'''(0) = -48$. Para $g$: $g(0) = 1$, $g'(0) = a$, $g''(0) = 2b$. El valor ya coincide ($1 = 1$); imponemos

$$
a = f'(0) = -2, \qquad 2b = f''(0) = 8 \Rightarrow b = 4.
$$

Con $g(x) = 1 - 2x + 4x^2$ resulta $g'''(x) = 0$, mientras que $f'''(0) = -48 \neq 0$: el contacto es de **orden exactamente $2$**. Con dos parámetros libres alcanzamos el orden $2$, no más: para el orden $3$ haría falta un tercer parámetro (un término cúbico).

## Expresar un polinomio por sus derivadas en un punto

Un polinomio suele darse en potencias de $x$. Para estudiarlo cerca de $a$ conviene tenerlo en potencias de $(x - a)$, porque entonces los primeros términos describen el comportamiento en $a$. Esto es posible siempre, y los coeficientes se leen de las derivadas.

:::note[Teorema · Polinomio y derivadas en un punto]
Si $P$ es un polinomio de grado $\le n$ y $a$ es un número real, entonces

$$
P(x) = \sum_{k=0}^{n} \dfrac{P^{(k)}(a)}{k!}\,(x - a)^k = P(a) + P'(a)(x - a) + \dfrac{P''(a)}{2!}(x - a)^2 + \dots + \dfrac{P^{(n)}(a)}{n!}(x - a)^n.
$$
:::

**Demostración (formal).** Todo polinomio de grado $\le n$ se puede escribir como $P(x) = c_0 + c_1(x - a) + \dots + c_n(x - a)^n$: basta reemplazar $x$ por $(x - a) + a$ en cada potencia y desarrollar con el binomio de Newton, lo que produce potencias de $(x - a)$ hasta el grado $n$. Calculamos ahora las derivadas de esa expresión y las evaluamos en $x = a$:

- $P(a) = c_0$, porque todos los demás términos tienen el factor $(x - a)$.
- $P'(x) = c_1 + 2c_2(x - a) + 3c_3(x - a)^2 + \dots$, luego $P'(a) = c_1$.
- $P''(x) = 2c_2 + 3 \cdot 2\,c_3(x - a) + \dots$, luego $P''(a) = 2c_2$.
- $P'''(x) = 3 \cdot 2\,c_3 + 4 \cdot 3 \cdot 2\,c_4 (x - a) + \dots$, luego $P'''(a) = 3!\,c_3$.

En general, al derivar $k$ veces, el término $c_k(x - a)^k$ se transforma en la constante $k(k-1)\cdots 2 \cdot 1\, c_k = k!\,c_k$; los términos de grado menor que $k$ desaparecen y los de grado mayor conservan el factor $(x - a)$, que se anula en $a$. Por lo tanto $P^{(k)}(a) = k!\,c_k$, es decir

$$
c_k = \dfrac{P^{(k)}(a)}{k!}, \qquad k = 0, 1, \dots, n. \qquad \blacksquare
$$

<!-- check: U4.T.POL.3 -->
Es el mismo cálculo para cualquier grado: por ejemplo, con un polinomio de grado $4$ y coeficientes literales, derivar $k$ veces $\sum c_j (x - a)^j$ y evaluar en $a$ da $k!\,c_k$ para $k = 0, \dots, 4$.

### Ejemplo 6 · Cambiar de potencias de $x$ a potencias de $(x - 2)$
<!-- check: U4.T.POL.1 -->

Reescribamos $P(x) = x^4 - 3x^3 + 2x - 5$ en potencias de $(x - 2)$. Derivamos y evaluamos en $a = 2$:

| $k$ | $P^{(k)}(x)$ | $P^{(k)}(2)$ | $\dfrac{P^{(k)}(2)}{k!}$ |
|---|---|---|---|
| $0$ | $x^4 - 3x^3 + 2x - 5$ | $16 - 24 + 4 - 5 = -9$ | $-9$ |
| $1$ | $4x^3 - 9x^2 + 2$ | $32 - 36 + 2 = -2$ | $-2$ |
| $2$ | $12x^2 - 18x$ | $48 - 36 = 12$ | $6$ |
| $3$ | $24x - 18$ | $30$ | $5$ |
| $4$ | $24$ | $24$ | $1$ |

Entonces $P(x) = -9 - 2(x - 2) + 6(x - 2)^2 + 5(x - 2)^3 + (x - 2)^4$. Se puede comprobar desarrollando: el resultado es de nuevo $x^4 - 3x^3 + 2x - 5$.

### Ejemplo 7 · Armar un polinomio a partir de sus derivadas
<!-- check: U4.T.POL.2 -->

¿Cuál es el polinomio de grado $\le 3$ con $P(1) = 2$, $P'(1) = -1$, $P''(1) = 4$ y $P'''(1) = 12$? Por el teorema, los coeficientes de las potencias de $(x - 1)$ son $\frac{2}{0!} = 2$, $\frac{-1}{1!} = -1$, $\frac{4}{2!} = 2$ y $\frac{12}{3!} = 2$:

$$
P(x) = 2 - (x - 1) + 2(x - 1)^2 + 2(x - 1)^3 = 2x^3 - 4x^2 + x + 3.
$$

## De los polinomios a cualquier función

El teorema anterior dice algo más profundo, que usaremos en la próxima lección. Dada una función $f$ con $n$ derivadas en $a$, buscamos un polinomio $P$ de grado $\le n$ con contacto de orden **al menos $n$** con $f$ en $a$, es decir, con $P^{(k)}(a) = f^{(k)}(a)$ para $k = 0, \dots, n$. Como los coeficientes de $P$ en potencias de $(x - a)$ son $\frac{P^{(k)}(a)}{k!}$, esas condiciones los determinan sin ambigüedad:

$$
c_k = \dfrac{f^{(k)}(a)}{k!}, \qquad k = 0, 1, \dots, n.
$$

Existe, entonces, **un único** polinomio de grado $\le n$ con contacto al menos $n$ con $f$ en $a$. Ese es el polinomio de Taylor de $f$, que construimos en [la lección siguiente](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/).

:::caution[Errores frecuentes]
- **Olvidar el factorial.** El coeficiente de $(x - a)^k$ es $\frac{P^{(k)}(a)}{k!}$, no $P^{(k)}(a)$. Es el error más común (por ejemplo, escribir $\frac{x^3}{3}$ en lugar de $\frac{x^3}{6}$ para $e^x$).
- **Contar mal el orden.** El contacto es de orden $n$ cuando coinciden las derivadas de orden $0$ a $n$; con $k = 0, 1, 2$ iguales y $k = 3$ distinta el orden es $2$, no $3$.
- **Cambiar de punto y no recalcular.** El orden de contacto depende de $a$: $x^3$ y $3x - 2$ tienen orden $1$ en $x = 1$ y orden $0$ en $x = -2$.
- **Creer que el orden es el grado.** Un polinomio de grado 4 puede tener contacto de orden 5 con una función (ejemplo 2).
- **Desarrollar $P(x) = \dots$ en potencias de $(x - a)$ sin las derivadas** y sin el factor $\frac{1}{k!}$ al armar el polinomio.
:::

## Ejercicios

### Ejercicio 1 · Orden de contacto de pares de funciones
<!-- ejercicio: U4.01 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Determiná el orden de contacto en $x = 0$ de cada par de funciones:

a) $f(x) = \ln(1 + x)$ y $g(x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3}$.

b) $f(x) = \cos x$ y $g(x) = 1 - \dfrac{x^2}{2}$.

c) $f(x) = e^x$ y $g(x) = 1 + x + x^2$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Calcular las derivadas de ambas funciones en $0$ hasta encontrar la primera que difiere; el orden es el índice anterior.

**Desarrollo.** a) Para $f(x) = \ln(1 + x)$: $f'(x) = \frac{1}{1 + x}$, $f''(x) = -\frac{1}{(1 + x)^2}$, $f'''(x) = \frac{2}{(1 + x)^3}$, $f^{(4)}(x) = -\frac{6}{(1 + x)^4}$; en $0$ valen $0, 1, -1, 2, -6$. Para $g$: $g(0) = 0$, $g'(0) = 1$, $g''(0) = -1$, $g'''(0) = 2$ y $g^{(4)}(0) = 0$. Coinciden de $k = 0$ a $k = 3$ y difieren en $k = 4$ ($-6 \neq 0$): orden $3$.

b) Para $\cos x$: $1, 0, -1, 0, 1$ para $k = 0, \dots, 4$. Para $g$: $1, 0, -1, 0, 0$. Coinciden hasta $k = 3$ y difieren en $k = 4$ ($1 \neq 0$): orden $3$.

c) Para $e^x$ todas las derivadas valen $1$ en $0$. Para $g$: $g(0) = 1$, $g'(0) = 1$, $g''(0) = 2$. Coinciden hasta $k = 1$ y difieren en $k = 2$ ($1 \neq 2$): orden $1$.

**Resultado.** a) orden $3$; b) orden $3$; c) orden $1$.

</details>

### Ejercicio 2 · Parámetros y orden exacto
<!-- ejercicio: U4.02 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \sqrt{1 + x}$.

a) Hallá $a$ y $b$ para que $g(x) = 1 + ax + bx^2$ tenga con $f$ un contacto de orden al menos $2$ en $x = 0$. ¿Cuál es el orden exacto?

b) Hallá $k$ para que $h(x) = g(x) + kx^3$ (con los $a$, $b$ del ítem anterior) tenga con $f$ contacto de orden al menos $3$. ¿Cuál es entonces el orden exacto?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Igualar las derivadas de $g$ y de $f$ en $0$ hasta el orden pedido y, después, mirar la derivada siguiente.

**Desarrollo.** Derivadas de $f$ en $0$: $f(0) = 1$; $f'(x) = \frac12 (1 + x)^{-1/2}$, $f'(0) = \frac12$; $f''(x) = -\frac14 (1 + x)^{-3/2}$, $f''(0) = -\frac14$; $f'''(x) = \frac38 (1 + x)^{-5/2}$, $f'''(0) = \frac38$; $f^{(4)}(x) = -\frac{15}{16}(1 + x)^{-7/2}$, $f^{(4)}(0) = -\frac{15}{16}$.

a) $g(0) = 1$ coincide. $g'(0) = a$ debe valer $\frac12$; $g''(0) = 2b$ debe valer $-\frac14$, así que $b = -\frac18$. Entonces $g(x) = 1 + \frac12 x - \frac18 x^2$, con $g'''(0) = 0 \neq \frac38 = f'''(0)$: el contacto es de orden exactamente $2$.

b) Con $h(x) = g(x) + kx^3$: $h'''(0) = 6k$ debe ser igual a $f'''(0) = \frac38$, de donde $k = \frac{1}{16}$. Ahora $h^{(4)}(0) = 0 \neq -\frac{15}{16} = f^{(4)}(0)$: el contacto es de orden exactamente $3$.

**Resultado.** a) $a = \frac12$, $b = -\frac18$, orden exacto $2$; b) $k = \frac{1}{16}$, orden exacto $3$.

</details>

### Ejercicio 3 · Un polinomio en potencias de $(x + 1)$
<!-- ejercicio: U4.03 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $Q(x) = 2x^4 - x^3 + 3x^2 + x - 4$.

a) Escribí $Q$ en potencias de $(x + 1)$.

b) Calculá $Q'''(-1)$ y $Q^{(4)}(-1)$ sin derivar de nuevo, a partir del resultado de a).

c) ¿Qué orden de contacto tiene $Q$ en $x = -1$ con su recta tangente en ese punto?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Usar $c_k = \frac{Q^{(k)}(-1)}{k!}$ con $a = -1$; los ítems b) y c) se leen de los coeficientes.

**Desarrollo.** a) Derivadas: $Q'(x) = 8x^3 - 3x^2 + 6x + 1$, $Q''(x) = 24x^2 - 6x + 6$, $Q'''(x) = 48x - 6$, $Q^{(4)}(x) = 48$. En $x = -1$: $Q(-1) = 2 + 1 + 3 - 1 - 4 = 1$; $Q'(-1) = -8 - 3 - 6 + 1 = -16$; $Q''(-1) = 24 + 6 + 6 = 36$; $Q'''(-1) = -54$; $Q^{(4)}(-1) = 48$. Los coeficientes $\frac{Q^{(k)}(-1)}{k!}$ son $1,\ -16,\ 18,\ -9,\ 2$:

$$
Q(x) = 1 - 16(x + 1) + 18(x + 1)^2 - 9(x + 1)^3 + 2(x + 1)^4.
$$

b) Del desarrollo, el coeficiente de $(x + 1)^3$ es $-9 = \frac{Q'''(-1)}{3!}$, luego $Q'''(-1) = -9 \cdot 6 = -54$; y el de $(x + 1)^4$ es $2 = \frac{Q^{(4)}(-1)}{4!}$, luego $Q^{(4)}(-1) = 2 \cdot 24 = 48$.

c) La recta tangente en $x = -1$ es $T(x) = 1 - 16(x + 1)$, con $T'' = 0$. Como $Q''(-1) = 36 \neq 0$, coinciden $Q$ y $T$ en valor y derivada primera, pero no en la segunda: el contacto es de orden $1$.

**Resultado.** a) el desarrollo anterior; b) $Q'''(-1) = -54$, $Q^{(4)}(-1) = 48$; c) orden $1$.

</details>

### Ejercicio 4 · Unicidad del polinomio con contacto dado
<!-- ejercicio: U4.04 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
a) Demostrá que si $P$ y $Q$ son polinomios de grado $\le n$ con contacto de orden al menos $n$ en $x = a$, entonces $P = Q$.

b) Mostrá con un ejemplo que la conclusión puede fallar si se permite grado $n + 1$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Aplicar el teorema de «polinomio por sus derivadas» a la diferencia $D = P - Q$.

**Desarrollo.** a) $D = P - Q$ es un polinomio de grado $\le n$. Que el contacto sea al menos de orden $n$ significa $P^{(k)}(a) = Q^{(k)}(a)$ para $k = 0, \dots, n$, es decir, $D^{(k)}(a) = 0$ para todos esos $k$. Por el teorema,

$$
D(x) = \sum_{k=0}^{n} \dfrac{D^{(k)}(a)}{k!}(x - a)^k = 0,
$$

de modo que $D$ es el polinomio nulo y $P = Q$.

b) Con $n = 1$, $a = 0$, $P(x) = 0$ y $Q(x) = x^2$ (de grado $2 = n + 1$): $Q(0) = P(0) = 0$ y $Q'(0) = P'(0) = 0$, así que el contacto es al menos de orden $1$, pero $P \neq Q$. En el argumento del ítem a), la diferencia tiene grado $n + 1$ y el desarrollo necesitaría además el término con $D^{(n+1)}(a)$, que no está controlado.

**Resultado.** Por cada $n$ y cada $a$ hay a lo sumo un polinomio de grado $\le n$ con contacto al menos $n$ con una función dada; con grado $n + 1$ la unicidad se pierde.

</details>

## Autoevaluación

**1. Si $f(a) = g(a)$ y $f'(a) \neq g'(a)$, ¿qué orden de contacto tienen y qué significa geométricamente?**

<details>
<summary>Respuesta</summary>

Orden $0$: las curvas se cortan en el punto $(a, f(a))$ pero con rectas tangentes distintas.
</details>

**2. ¿Puede una recta tener contacto de orden $2$ con una curva?**

<details>
<summary>Respuesta</summary>

Sí: la recta tangente tiene contacto al menos $1$ y, si $f''(a) = 0$ (por ejemplo, en un punto de inflexión como $\operatorname{sen} x$ en $0$), el contacto es de orden $2$ o más.
</details>

**3. Si el contacto entre $f$ y $g$ en $a$ es de orden $4$, ¿cuánto vale $\lim\limits_{x \to a} \dfrac{f(x) - g(x)}{(x - a)^4}$ y qué se puede decir de $\lim\limits_{x \to a} \dfrac{f(x) - g(x)}{(x - a)^5}$?**

<details>
<summary>Respuesta</summary>

El primero vale $0$; el segundo es un número real distinto de $0$, igual a $\frac{f^{(5)}(a) - g^{(5)}(a)}{5!}$.
</details>

**4. ¿Qué coeficiente tiene $(x - 3)^4$ al escribir un polinomio $P$ en potencias de $(x - 3)$?**

<details>
<summary>Respuesta</summary>

$\dfrac{P^{(4)}(3)}{4!}$.
</details>

:::tip[En resumen]
- $f$ y $g$ tienen **contacto de orden $n$** en $a$ si coinciden $f^{(k)}(a) = g^{(k)}(a)$ para $k = 0, \dots, n$ y difieren en $k = n + 1$.
- A mayor orden, más pegadas están las curvas cerca de $a$: orden $0$ (se cortan), $1$ (misma tangente), $2$ (misma concavidad).
- Equivale a que $f - g$ sea un infinitésimo de orden $n + 1$ en $(x - a)$: $\lim \frac{f - g}{(x - a)^n} = 0$ y $\lim \frac{f - g}{(x - a)^{n+1}} \neq 0$.
- Todo polinomio de grado $\le n$ es $P(x) = \sum_{k=0}^{n} \frac{P^{(k)}(a)}{k!}(x - a)^k$; por eso existe un único polinomio de grado $\le n$ con contacto al menos $n$ con una $f$ dada.
:::

**Para seguir.** En [polinomio de Taylor y de Mac Laurin](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/) construimos ese polinomio para cualquier función derivable $n$ veces, lo usamos para aproximar valores y ecuaciones, y estudiamos la aproximación lineal.
