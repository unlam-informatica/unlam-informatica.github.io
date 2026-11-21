---
title: Ceros, signo, paridad y acotación
description: Cálculo de ceros y de los conjuntos de positividad y negatividad, clasificación de funciones pares e impares y funciones acotadas.
slug: analisis-matematico-i/unidad-1/teoria/caracteristicas
sidebar:
  order: 2
---

## Qué vas a aprender

- Calcular ceros y los conjuntos de positividad y negatividad de funciones polinómicas, racionales y definidas por tramos, y justificar el signo en cada intervalo.
- Clasificar una función como par, impar o ninguna de las dos, verificando antes que el dominio sea simétrico, y relacionar la paridad con la simetría del gráfico.
- Decidir si una función es acotada superior o inferiormente en un conjunto y dar cotas.

## Antes de empezar

Tenés que dominar la definición de función y el dominio ([funciones y modelos](/analisis-matematico-i/unidad-1/teoria/funciones-y-modelos/)), la factorización de polinomios y la resolución de desigualdades.

## Ceros y signo

:::note[Definición]
Sea $f\colon D_f \to \mathbb{R}$.

- Los **ceros** (o raíces) de $f$ son los $x \in D_f$ con $f(x) = 0$: $C_0 = \{x \in D_f : f(x) = 0\}$.
- El **conjunto de positividad** es $C^{+} = \{x \in D_f : f(x) > 0\}$.
- El **conjunto de negatividad** es $C^{-} = \{x \in D_f : f(x) < 0\}$.
:::

Los tres conjuntos son **disjuntos** y cubren el dominio: $C_0 \cup C^{+} \cup C^{-} = D_f$. Geométricamente, $C_0$ son las abscisas de los puntos donde el gráfico **corta o toca** el eje $x$; $C^{+}$, donde el gráfico queda por encima del eje, y $C^{-}$, por debajo. La ordenada al origen es el punto $(0, f(0))$, si $0 \in D_f$.

Un cero se calcula resolviendo $f(x) = 0$ **dentro del dominio**: una solución de la ecuación que no pertenece al dominio no es un cero.

### Por qué la tabla de signos funciona

Para armar $C^{+}$ y $C^{-}$ se usa un hecho sobre las funciones **continuas**: si en un intervalo $f$ es continua y no se anula, entonces tiene **signo constante** en ese intervalo. (Es una consecuencia del teorema del valor intermedio, que se estudia en la [Unidad 2](/analisis-matematico-i/unidad-2/teoria/continuidad/); aquí lo usamos para los polinomios, las funciones racionales y las demás funciones elementales, que son continuas en cada intervalo de su dominio.) Entonces el signo solo puede cambiar en:

- un **cero** de la función, o
- un punto **fuera del dominio** (donde la función no está definida).

El procedimiento es:

1. Hallar el dominio y los ceros.
2. Marcar todos esos puntos en la recta; dividen al dominio en intervalos.
3. Elegir **un punto de prueba** en cada intervalo (o usar el signo de cada factor) y determinar el signo.
4. Escribir $C^{+}$ y $C^{-}$ como uniones de intervalos.

Cuando $f$ está factorizada, $f(x) = a (x - r_1)^{m_1}\cdots(x - r_k)^{m_k}$, la **multiplicidad** $m_i$ decide: si $m_i$ es **impar**, el signo cambia al pasar por $r_i$; si es **par**, el signo se **mantiene** (la curva toca el eje y vuelve).

![Gráfico de p(x) = (x+2)(x−1)²(x−3) con sus tres ceros marcados.](/analisis-matematico-i/figuras/u1-signo.svg)

*Observá que el gráfico cruza el eje en $-2$ y en $3$ (multiplicidad 1) y solo lo toca en $1$ (multiplicidad 2): a ambos lados de $x = 1$ la función es negativa.*

### Ejemplo 1 · Polinomio factorizado

Hallar ceros y signo de $p(x) = (x + 2)(x - 1)^2(x - 3)$.

Los ceros son $-2$ (multiplicidad 1), $1$ (multiplicidad 2) y $3$ (multiplicidad 1). Dividen la recta en $(-\infty, -2)$, $(-2, 1)$, $(1, 3)$ y $(3, +\infty)$. Como $(x - 1)^2 \ge 0$ siempre, el signo de $p$ es el de $(x + 2)(x - 3)$ salvo en $x = 1$ (donde vale $0$):

| Intervalo | $x + 2$ | $(x-1)^2$ | $x - 3$ | $p(x)$ |
|---|---|---|---|---|
| $(-\infty, -2)$ | $-$ | $+$ | $-$ | $+$ |
| $(-2, 1)$ | $+$ | $+$ | $-$ | $-$ |
| $(1, 3)$ | $+$ | $+$ | $-$ | $-$ |
| $(3, +\infty)$ | $+$ | $+$ | $+$ | $+$ |

<!-- check: U1.T.ZER.1 -->
$$
C_0 = \{-2, 1, 3\}, \qquad C^{+} = (-\infty, -2) \cup (3, +\infty), \qquad C^{-} = (-2, 1) \cup (1, 3).
$$

### Ejemplo 2 · Un cero aparente que no es cero

Hallar ceros y signo de $r(x) = \dfrac{x^2 - 4}{x^2 - x - 6}$.

**Dominio.** El denominador es $x^2 - x - 6 = (x - 3)(x + 2)$, que se anula en $3$ y en $-2$: $D_r = \mathbb{R} \setminus \{-2, 3\}$.

**Ceros.** El numerador es $(x - 2)(x + 2)$, que vale $0$ en $x = 2$ y en $x = -2$. Pero $-2 \notin D_r$: **no es un cero**. Queda solo $x = 2$ (que sí está en el dominio).

**Signo.** En $D_r$ podemos simplificar: $r(x) = \dfrac{x - 2}{x - 3}$ para $x \ne -2, 3$. Los puntos críticos son $2$ (cero) y $3$ (fuera del dominio); además hay que excluir $-2$:

- $x < 2$ (con $x \ne -2$): $x - 2 < 0$ y $x - 3 < 0$, cociente positivo.
- $2 < x < 3$: numerador positivo, denominador negativo, cociente negativo.
- $x > 3$: ambos positivos, cociente positivo.

<!-- check: U1.T.ZER.2 -->
$$
C_0 = \{2\}, \qquad C^{+} = (-\infty, -2) \cup (-2, 2) \cup (3, +\infty), \qquad C^{-} = (2, 3).
$$

### Ejemplo 3 · Función por tramos y el signo sin continuidad

Sea
$$
f(x) = \begin{cases} x^2 - 4x + 3 & \text{si } x < 2, \\ 8 - 2x & \text{si } x \ge 2. \end{cases}
$$

**Ceros.** En cada tramo se resuelve dentro del tramo. Primer tramo: $x^2 - 4x + 3 = (x - 1)(x - 3) = 0$ da $x = 1$ y $x = 3$; solo $x = 1$ cumple $x < 2$. Segundo tramo: $8 - 2x = 0$ da $x = 4$, que cumple $x \ge 2$. Entonces $C_0 = \{1, 4\}$.

**Signo.** Primer tramo ($x < 2$): $(x - 1)(x - 3) > 0$ si $x < 1$ y $< 0$ si $1 < x < 2$. Segundo tramo ($x \ge 2$): $8 - 2x > 0$ si $2 \le x < 4$ y $< 0$ si $x > 4$.

<!-- check: U1.T.ZER.3 -->
$$
C^{+} = (-\infty, 1) \cup [2, 4), \qquad C^{-} = (1, 2) \cup (4, +\infty).
$$

Observá que el signo pasa de negativo a positivo en $x = 2$ **sin que haya un cero ahí**: $f(2) = 4$ y, para $x$ cerca de $2$ por izquierda, $f(x)$ está cerca de $-1$. La regla «el signo solo cambia en los ceros o fuera del dominio» **requiere continuidad**; esta función tiene un salto en $x = 2$. Es un ejemplo de por qué la hipótesis importa.

:::caution[Errores frecuentes]
- Aceptar como cero una solución de $f(x) = 0$ que no está en el dominio (ejemplo 2) o que no cae en el tramo (ejemplo 3).
- Simplificar una expresión racional y olvidar las restricciones del dominio original.
- Pasar de «$f(x) \ge 0$» a «$f(x) > 0$»: los ceros no pertenecen a $C^{+}$ ni a $C^{-}$.
- Creer que el signo siempre cambia en un cero: no cambia si la multiplicidad es par.
:::

## Funciones pares e impares

:::note[Definición]
Sea $f$ una función cuyo dominio es **simétrico respecto del origen** (si $x \in D_f$, entonces $-x \in D_f$).

- $f$ es **par** si $f(-x) = f(x)$ para todo $x \in D_f$.
- $f$ es **impar** si $f(-x) = -f(x)$ para todo $x \in D_f$.
:::

La condición de simetría del dominio es **parte de la definición**: sin ella, $f(-x)$ ni siquiera está definida. Por eso $f(x) = x^2$ restringida a $[-1, 3]$ **no** es par.

**Interpretación geométrica.** Si $f$ es par, el punto $(x, f(x))$ y su reflejado $(-x, f(x))$ están ambos en el gráfico: el gráfico es **simétrico respecto del eje $y$**. Si $f$ es impar, $(x, f(x))$ y $(-x, -f(x))$ están ambos: el gráfico es **simétrico respecto del origen** (invariante ante una rotación de $180^\circ$).

![Gráfico de f(x) = x⁴ − 3x² + 1 con dos pares de puntos simétricos respecto del eje y.](/analisis-matematico-i/figuras/u1-simetria-par.svg)

*Observá que cada punto a la derecha del eje $y$ tiene un gemelo a la izquierda a la misma altura (segmentos punteados horizontales).*

![Gráfico de g(x) = x³ − 3x con dos pares de puntos simétricos respecto del origen.](/analisis-matematico-i/figuras/u1-simetria-impar.svg)

*Observá que los pares de puntos están alineados con el origen y que ese punto es el centro del segmento que los une.*

**Método.** 1) Verificar que el dominio sea simétrico (si no, la función no es par ni impar). 2) Calcular $f(-x)$ y simplificar. 3) Comparar con $f(x)$ y con $-f(x)$. Para probar que **no** tiene paridad hace falta un contraejemplo: un $x_0$ tal que $f(-x_0) \ne f(x_0)$ y $f(-x_0) \ne -f(x_0)$.

### Propiedades

:::note[Propiedad]
Sean $f$ y $g$ definidas en un dominio simétrico.

- La suma de dos funciones pares es par; la de dos impares es impar.
- El producto (o cociente) de dos pares es par; de dos impares es **par**; de una par y una impar es **impar**.
- Si $f$ es impar y $0 \in D_f$, entonces $f(0) = 0$.
- La composición $f \circ g$ es par si $g$ es par, o si $f$ es par y $g$ es impar.
:::

**Demostración (formal).** Para el producto de dos impares: $(fg)(-x) = f(-x)g(-x) = (-f(x))(-g(x)) = f(x)g(x) = (fg)(x)$. Para $f$ impar con $0 \in D_f$: $f(0) = f(-0) = -f(0)$, luego $2f(0) = 0$. Las demás se prueban igual, aplicando la definición. $\blacksquare$

Estas reglas ahorran cuentas: $x\,|x|$ es impar (producto de impar por par); $e^{x} + e^{-x}$ es par.

### Ejemplo 4 · Clasificar funciones

Clasificar: a) $f(x) = x^4 - 3x^2 + 1$; b) $g(x) = x^3 - 4x$; c) $h(x) = x^2 + x$; d) $k(x) = \dfrac{1}{x - 1}$.

<!-- check: U1.T.PAR.1 -->
a) El dominio es $\mathbb{R}$. $f(-x) = (-x)^4 - 3(-x)^2 + 1 = x^4 - 3x^2 + 1 = f(x)$: **par**.

b) $g(-x) = (-x)^3 - 4(-x) = -x^3 + 4x = -(x^3 - 4x) = -g(x)$: **impar**.

c) $h(-x) = x^2 - x$. Con $x_0 = 1$: $h(1) = 2$ y $h(-1) = 0$; ni $0 = 2$ ni $0 = -2$. **Ninguna.**

d) El dominio es $\mathbb{R} \setminus \{1\}$: contiene a $-1$ pero **no** a $1$, así que no es simétrico. **Ninguna** (no hace falta calcular $k(-x)$).

### Ejemplo 5 · Reglas de paridad

Clasificar $m(x) = (x^2 + 1)\,x^3$ y $n(x) = \dfrac{\operatorname{sen} x}{x}$.

<!-- check: U1.T.PAR.2 -->
$m$ es producto de una función par ($x^2 + 1$) y una impar ($x^3$): es **impar**. Directamente: $m(-x) = (x^2 + 1)(-x^3) = -m(x)$.

$n$ tiene dominio $\mathbb{R} \setminus \{0\}$ (simétrico) y es cociente de dos impares: es **par**. Directamente: $n(-x) = \dfrac{\operatorname{sen}(-x)}{-x} = \dfrac{-\operatorname{sen} x}{-x} = n(x)$.

### Toda función se descompone en una parte par y una impar

:::note[Propiedad]
Si $D_f$ es simétrico, toda $f$ se escribe de una única forma como $f = f_p + f_i$ con $f_p$ par y $f_i$ impar:
$$
f_p(x) = \frac{f(x) + f(-x)}{2}, \qquad f_i(x) = \frac{f(x) - f(-x)}{2}.
$$
:::

**Demostración (formal).** Sumando, $f_p + f_i = f$. $f_p(-x) = \frac{f(-x) + f(x)}{2} = f_p(x)$ y $f_i(-x) = \frac{f(-x) - f(x)}{2} = -f_i(x)$. Unicidad: si $f = a + b$ con $a$ par y $b$ impar, entonces $f(-x) = a(x) - b(x)$; sumando y restando $f(x)$ y $f(-x)$ se obtiene $a = f_p$ y $b = f_i$. $\blacksquare$

### Ejemplo 6 · Descomposición de un polinomio

Para $f(x) = x^3 + 2x^2 - x + 5$: $f(-x) = -x^3 + 2x^2 + x + 5$. Entonces
<!-- check: U1.T.PAR.3 -->
$$
f_p(x) = \frac{4x^2 + 10}{2} = 2x^2 + 5, \qquad f_i(x) = \frac{2x^3 - 2x}{2} = x^3 - x.
$$
La parte par junta los términos de grado par y la impar los de grado impar.

:::caution[Errores frecuentes]
- Olvidar chequear el dominio: $\dfrac{1}{x - 1}$ o $x^2$ en $[-1, 3]$ no tienen paridad.
- Concluir que no tiene paridad porque «no se parece a $f(x)$»: puede ser $-f(x)$.
- Pensar que «ni par ni impar» y «par e impar» son lo mismo: la única función par **e** impar a la vez (con dominio simétrico) es la nula.
- Creer que un polinomio con algún término par es par: $x^2 + x$ mezcla ambas partes.
:::

## Funciones acotadas

:::note[Definición]
Sea $f$ una función y $S \subseteq D_f$ un conjunto (por defecto, $S = D_f$).

- $f$ está **acotada superiormente** en $S$ si existe $M \in \mathbb{R}$ con $f(x) \le M$ para todo $x \in S$. $M$ es una **cota superior**.
- $f$ está **acotada inferiormente** en $S$ si existe $m \in \mathbb{R}$ con $f(x) \ge m$ para todo $x \in S$. $m$ es una **cota inferior**.
- $f$ está **acotada** si lo está superior e inferiormente; equivale a que exista $k > 0$ con $|f(x)| \le k$ para todo $x \in S$.
:::

Las cotas **no son únicas**: si $M$ es cota superior, también lo es cualquier número mayor. Una función está acotada superiormente cuando su **imagen** está acotada superiormente. Por eso $\operatorname{sen} x$ está acotada ($|\operatorname{sen} x| \le 1$), $x^2$ está acotada inferiormente por $0$ pero **no** superiormente, y los polinomios de grado impar no están acotados ni superior ni inferiormente.

Para mostrar que una función **no** está acotada superiormente se prueba que para **todo** $M$ hay un $x$ con $f(x) > M$.

La acotación depende del conjunto: $\dfrac{1}{x}$ no está acotada superiormente en $(0, 1]$, pero sí en $[1, +\infty)$ (por $1$).

### Ejemplo 7 · Una función acotada, con su imagen

Probar que $f(x) = \dfrac{x}{1 + x^2}$ está acotada y hallar su imagen.

**Cota.** Para todo real, $(1 - |x|)^2 \ge 0$, o sea $1 + x^2 \ge 2|x|$. Como $1 + x^2 > 0$, dividiendo: $|f(x)| = \dfrac{|x|}{1 + x^2} \le \dfrac12$. Entonces $-\dfrac12 \le f(x) \le \dfrac12$.

**Imagen.** Planteamos $\dfrac{x}{1 + x^2} = y$, es decir $y x^2 - x + y = 0$. Si $y = 0$, $x = 0$ sirve. Si $y \ne 0$ es una cuadrática en $x$ con discriminante $1 - 4y^2$; tiene solución real si y solo si $1 - 4y^2 \ge 0$, o sea $|y| \le \dfrac12$. Además $f(1) = \dfrac12$ y $f(-1) = -\dfrac12$, así que las cotas se alcanzan:

<!-- check: U1.T.ACO.1 -->
$$
\operatorname{Im} f = \left[-\tfrac12, \tfrac12\right].
$$

### Ejemplo 8 · Acotada inferiormente pero no superiormente

<!-- check: U1.T.ACO.2 -->
Para $g(x) = x^2 + 3$: como $x^2 \ge 0$, $g(x) \ge 3$ (cota inferior; se alcanza en $x = 0$). No está acotada superiormente: dado $M > 3$, tomamos $x_0 = \sqrt{M}$; entonces $g(x_0) = M + 3 > M$. Como $M$ era arbitrario, ninguna cota superior sirve. La imagen es $[3, +\infty)$.

### Ejemplo 9 · Acotación según el conjunto

<!-- check: U1.T.ACO.3 -->
$h(x) = \dfrac{1}{x}$ en $S = (0, 1]$. Dado $M > 0$, tomamos $x_0 = \dfrac{1}{M + 1} \in (0, 1]$: $h(x_0) = M + 1 > M$. No está acotada superiormente en $S$. Sí está acotada inferiormente: $h(x) \ge 1$ en $(0, 1]$. En cambio, en $[1, +\infty)$ vale $0 < h(x) \le 1$: acotada.

:::caution[Errores frecuentes]
- Confundir «acotada» con «alcanza sus cotas»: $\dfrac{1}{1 + x^2}$ está acotada inferiormente por $0$, pero nunca vale $0$.
- Decir que $\dfrac{1}{x}$ no está acotada sin aclarar el conjunto.
- Dar una cota como si fuera la única, o tomar «el máximo valor que veo en el gráfico» como prueba: hace falta una desigualdad que valga para todo $x$.
:::

## Ejercicios

### Ejercicio 6 · Ceros y signo de un polinomio
<!-- ejercicio: U1.06 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $p(x) = x^3 - x^2 - 6x$. Hallar los ceros y los conjuntos de positividad y negatividad.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Factorizar, marcar los ceros y estudiar el signo de cada factor.

**Desarrollo.** Sacamos factor común: $p(x) = x(x^2 - x - 6) = x(x - 3)(x + 2)$. Los ceros son $-2$, $0$ y $3$ (todos de multiplicidad $1$, así que el signo cambia en cada uno). Para $x > 3$ los tres factores son positivos y $p > 0$; al cruzar $3$ cambia a negativo en $(0, 3)$, luego positivo en $(-2, 0)$ y negativo en $(-\infty, -2)$.

**Resultado.** $C_0 = \{-2, 0, 3\}$, $C^{+} = (-2, 0) \cup (3, +\infty)$, $C^{-} = (-\infty, -2) \cup (0, 3)$.

</details>

### Ejercicio 7 · Cociente con una raíz excluida
<!-- ejercicio: U1.07 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $f(x) = \dfrac{x^3 - 9x}{x^2 - x - 6}$ hallar el dominio, los ceros y los conjuntos de positividad y negatividad.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Factorizar numerador y denominador; el dominio sale del denominador **antes** de simplificar.

**Desarrollo.** $x^3 - 9x = x(x - 3)(x + 3)$ y $x^2 - x - 6 = (x - 3)(x + 2)$. El denominador se anula en $3$ y en $-2$: $D_f = \mathbb{R} \setminus \{-2, 3\}$. Los candidatos a cero son $0$, $3$ y $-3$, pero $3 \notin D_f$: los ceros son $0$ y $-3$.

Para $x \ne 3$, $f(x) = \dfrac{x(x + 3)}{x + 2}$. Los puntos críticos son $-3$, $-2$ y $0$ (y hay que excluir $3$ del resultado):

| Intervalo | $x$ | $x + 3$ | $x + 2$ | $f$ |
|---|---|---|---|---|
| $(-\infty, -3)$ | $-$ | $-$ | $-$ | $-$ |
| $(-3, -2)$ | $-$ | $+$ | $-$ | $+$ |
| $(-2, 0)$ | $-$ | $+$ | $+$ | $-$ |
| $(0, +\infty)$ | $+$ | $+$ | $+$ | $+$ |

**Resultado.** $D_f = \mathbb{R} \setminus \{-2, 3\}$, $C_0 = \{-3, 0\}$, $C^{+} = (-3, -2) \cup (0, 3) \cup (3, +\infty)$, $C^{-} = (-\infty, -3) \cup (-2, 0)$.

</details>

### Ejercicio 8 · Clasificar por paridad
<!-- ejercicio: U1.08 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Clasificar como par, impar o ninguna (analizando el dominio) y justificar:
a) $f(x) = \dfrac{x^5 - x}{x^2 + 1}$; b) $g(x) = \ln\dfrac{2 + x}{2 - x}$; c) $h(x) = e^{x^2} + \cos x$; d) $k(x) = \operatorname{sen} x + \cos x$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dominio simétrico, después $f(-x)$ y las reglas de paridad.

**Desarrollo.**
a) El dominio es $\mathbb{R}$. $f(-x) = \dfrac{-x^5 + x}{x^2 + 1} = -f(x)$: **impar** (cociente de impar y par).

b) El dominio es $\dfrac{2 + x}{2 - x} > 0$, es decir, $(-2, 2)$, simétrico. $g(-x) = \ln\dfrac{2 - x}{2 + x} = \ln\left(\dfrac{2 + x}{2 - x}\right)^{-1} = -g(x)$: **impar**.

c) El dominio es $\mathbb{R}$. $e^{(-x)^2} = e^{x^2}$ y $\cos(-x) = \cos x$: $h(-x) = h(x)$, **par**.

d) $k(-x) = -\operatorname{sen} x + \cos x$. Elegimos $x_0 = \frac{\pi}{4}$: $k(x_0) = \sqrt2$ y $k(-x_0) = -\frac{\sqrt2}{2} + \frac{\sqrt2}{2} = 0$. Como $0 \ne \sqrt2$ y $0 \ne -\sqrt2$, no es par ni impar. **Ninguna.**

**Resultado.** a) impar; b) impar; c) par; d) ninguna.

</details>

### Ejercicio 9 · Imagen y cotas
<!-- ejercicio: U1.09 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \dfrac{2x}{x^2 + 4}$.
a) Probar que $f$ está acotada con la desigualdad $(|x| - 2)^2 \ge 0$ y dar la mejor cota para $|f|$.
b) Hallar la imagen de $f$ y decir si es par, impar o ninguna.
c) ¿Está $f$ acotada en $[0, +\infty)$ inferiormente por $0$? ¿Y en $(-\infty, 0]$ superiormente por $0$?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Una desigualdad de la forma «cuadrado $\ge 0$» da la cota; la imagen se obtiene despejando $x$ en $y = f(x)$ y exigiendo que haya solución real.

**Desarrollo.** a) $(|x| - 2)^2 \ge 0 \iff x^2 + 4 \ge 4|x|$. Dividiendo por $x^2 + 4 > 0$ resulta $\dfrac{4|x|}{x^2 + 4} \le 1$, y entonces $|f(x)| = \dfrac{2|x|}{x^2 + 4} \le \dfrac12$. La igualdad se da en $|x| = 2$, así que $\frac12$ es la mejor cota.

b) De $y = \dfrac{2x}{x^2 + 4}$ resulta $y x^2 - 2x + 4y = 0$. Si $y \ne 0$, el discriminante $4 - 16y^2$ debe ser $\ge 0$: $|y| \le \dfrac12$. $y = 0$ se alcanza en $x = 0$. Como $f(2) = \dfrac12$ y $f(-2) = -\dfrac12$, la imagen es $\left[-\tfrac12, \tfrac12\right]$. Además $f(-x) = -f(x)$ con dominio $\mathbb{R}$: es **impar**.

c) Para $x \ge 0$, $f(x) \ge 0$ (numerador y denominador no negativos): sí. Para $x \le 0$, $f(x) \le 0$: sí.

**Resultado.** a) $|f(x)| \le \tfrac12$, la mejor cota; b) $\operatorname{Im} f = \left[-\tfrac12, \tfrac12\right]$, impar; c) sí en ambos casos.

</details>

## Autoevaluación

**1. ¿Por qué $x = -2$ no es un cero de $\dfrac{x^2 - 4}{x + 2}$?**

<details>
<summary>Respuesta</summary>

Porque $-2$ no pertenece al dominio: el denominador se anula. Un cero debe estar en el dominio.
</details>

**2. Si $p(x) = (x - 1)^2(x + 3)$, ¿cambia el signo de $p$ al pasar por $x = 1$?**

<details>
<summary>Respuesta</summary>

No: la multiplicidad es $2$ (par), el signo se mantiene.
</details>

**3. ¿Es par $f(x) = x^2$ con dominio $[-2, 3]$?**

<details>
<summary>Respuesta</summary>

No. El dominio no es simétrico respecto del origen: $3$ está pero $-3$ no.
</details>

<details>
<summary>4. ¿Una función impar tiene que pasar por el origen?</summary>

Solo si $0$ pertenece a su dominio; en ese caso $f(0) = 0$. La función $\dfrac1x$ es impar y no pasa por el origen.
</details>

:::tip[En resumen]
- Los ceros se buscan **dentro del dominio** y, por tramos, **dentro de cada tramo**. $C_0$, $C^{+}$ y $C^{-}$ particionan el dominio.
- En funciones continuas el signo solo cambia en un cero de multiplicidad impar o en un punto fuera del dominio; sin continuidad la regla falla.
- Par: $f(-x) = f(x)$ (simetría respecto del eje $y$). Impar: $f(-x) = -f(x)$ (simetría respecto del origen). Ambas exigen **dominio simétrico**.
- Acotada: existe una cota superior y una inferior en el conjunto considerado; la acotación depende del conjunto.
:::

**Para seguir.** Con estas herramientas de análisis, ya se pueden estudiar las [funciones elementales](/analisis-matematico-i/unidad-1/teoria/funciones-elementales/). Para graficar y comprobar ceros y simetrías con software, mirá la [guía de GeoGebra](/analisis-matematico-i/geogebra/funciones/).
