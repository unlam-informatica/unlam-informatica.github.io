---
title: Álgebra de funciones y transformaciones
description: Igualdad de funciones, operaciones y composición con su dominio, cálculo del dominio natural, y desplazamientos, alargamientos, contracciones y reflexiones de un gráfico.
slug: analisis-matematico-i/unidad-1/teoria/algebra-y-transformaciones
sidebar:
  order: 4
---

## Qué vas a aprender

- Decidir cuándo dos funciones son iguales.
- Operar con funciones (suma, producto, cociente, composición) y determinar el dominio del resultado.
- Calcular el dominio natural de expresiones con cocientes, raíces de índice par y logaritmos.
- Obtener el gráfico de $a\,f\big(b(x - c)\big) + d$ a partir del de $f$, y saber cómo cambian dominio, imagen, ceros y período.

## Antes de empezar

Necesitás la [definición de función como terna](/analisis-matematico-i/unidad-1/teoria/funciones-y-modelos/), el catálogo de [funciones elementales](/analisis-matematico-i/unidad-1/teoria/funciones-elementales/) y la resolución de desigualdades (cuadros de signos, como en [ceros y signo](/analisis-matematico-i/unidad-1/teoria/caracteristicas/)).

## Igualdad de funciones

:::note[Definición]
Dos funciones $f\colon A \to B$ y $g\colon C \to D$ son **iguales** si y solo si $A = C$, $B = D$ y $f(x) = g(x)$ para todo $x$ del dominio común.
:::

Dos fórmulas que coinciden «donde ambas tienen sentido» pueden definir funciones **distintas** porque los dominios no coinciden. Para decidir, se calculan los dominios naturales y se comparan, y después se comparan las reglas (por simplificación algebraica o con un contraejemplo).

### Ejemplo 1 · ¿Son iguales?

<!-- check: U1.T.ALG.1 -->
a) $f(x) = \dfrac{x^2 - 9}{x - 3}$ y $g(x) = x + 3$. Los dominios son $D_f = \mathbb{R} \setminus \{3\}$ y $D_g = \mathbb{R}$. Para $x \ne 3$, $\dfrac{(x - 3)(x + 3)}{x - 3} = x + 3$: las reglas coinciden donde ambas existen, pero los dominios difieren, así que **no son iguales**. Lo serían si se restringiera $g$ a $\mathbb{R} \setminus \{3\}$.

b) $f(x) = \ln(x^2)$ y $g(x) = 2\ln x$. $D_f = \mathbb{R} \setminus \{0\}$ y $D_g = (0, +\infty)$. **No son iguales**: $f(-1) = \ln 1 = 0$, pero $g(-1)$ no existe. Sí son iguales si se restringen las dos a $(0, +\infty)$.

c) $f(x) = \sqrt{x^2}$ y $g(x) = |x|$. Ambas tienen dominio $\mathbb{R}$ y, como $\sqrt{x^2} = |x|$ para todo real, las reglas coinciden: **son iguales**. En cambio $h(x) = x$ no es igual a ellas: $h(-2) = -2 \ne 2$.

## Álgebra de funciones

Dadas $f$ y $g$, las operaciones se definen punto a punto y exigen que **ambas** estén definidas:

| Operación | Regla | Dominio |
|---|---|---|
| Suma / resta | $(f \pm g)(x) = f(x) \pm g(x)$ | $D_f \cap D_g$ |
| Producto | $(f \cdot g)(x) = f(x)\,g(x)$ | $D_f \cap D_g$ |
| Cociente | $\left(\dfrac{f}{g}\right)(x) = \dfrac{f(x)}{g(x)}$ | $(D_f \cap D_g) \setminus \{x : g(x) = 0\}$ |
| Producto por constante | $(k f)(x) = k f(x)$ | $D_f$ |
| Composición | $(f \circ g)(x) = f\big(g(x)\big)$ | $\{x \in D_g : g(x) \in D_f\}$ |

### Composición

$f \circ g$ aplica **primero $g$ y después $f$**. Para que $f(g(x))$ tenga sentido hacen falta **dos** cosas: que $g(x)$ exista y que el valor $g(x)$ pertenezca al dominio de $f$. La composición **no es conmutativa**: en general $f \circ g \ne g \circ f$ (y puede suceder que una exista y la otra tenga un dominio distinto). Es **asociativa**: $(f \circ g) \circ h = f \circ (g \circ h)$.

### Ejemplo 2 · Operaciones y dominios

Sean $f(x) = \sqrt{x + 3}$ y $g(x) = \sqrt{5 - x}$. Los dominios son $D_f = [-3, +\infty)$ y $D_g = (-\infty, 5]$, con intersección $[-3, 5]$. Entonces $f + g$, $f - g$ y $f \cdot g$ tienen dominio $[-3, 5]$; $g$ se anula solo en $x = 5$, así que

<!-- check: U1.T.ALG.2 -->
$$
\frac{f}{g}(x) = \sqrt{\frac{x + 3}{5 - x}}, \qquad D_{f/g} = [-3, 5).
$$

Por ejemplo, $\dfrac{f}{g}(1) = \sqrt{\dfrac{4}{4}} = 1$.

### Ejemplo 3 · Composición y no conmutatividad

Sean $f(x) = \sqrt{x}$ y $g(x) = x^2 - 4x$.

<!-- check: U1.T.ALG.3 -->
**$f \circ g$.** $(f \circ g)(x) = \sqrt{x^2 - 4x}$. Hace falta $x^2 - 4x = x(x - 4) \ge 0$, es decir, $x \le 0$ o $x \ge 4$: $D_{f \circ g} = (-\infty, 0] \cup [4, +\infty)$.

**$g \circ f$.** $(g \circ f)(x) = (\sqrt{x})^2 - 4\sqrt{x} = x - 4\sqrt{x}$, con $D_{g \circ f} = [0, +\infty)$ (el interior $\sqrt{x}$ exige $x \ge 0$ y $g$ acepta cualquier real).

Son distintas: $(f \circ g)(4) = \sqrt{0} = 0$, pero $(g \circ f)(4) = 4 - 8 = -4$. Además $f \circ g$ no existe en $x = 2$ mientras $g \circ f$ sí.

### Ejemplo 4 · Otra composición

Con $f(x) = \dfrac{1}{x - 1}$ y $g(x) = \ln x$:

<!-- check: U1.T.ALG.4 -->
$(f \circ g)(x) = \dfrac{1}{\ln x - 1}$ exige $x > 0$ (para $\ln x$) y $\ln x \ne 1$, o sea $x \ne e$: dominio $(0, +\infty) \setminus \{e\}$.

$(g \circ f)(x) = \ln\dfrac{1}{x - 1}$ exige $x \ne 1$ y $\dfrac{1}{x - 1} > 0$, o sea $x > 1$: dominio $(1, +\infty)$.

## Dominio natural

Cuando solo se da la fórmula, el **dominio natural** es el conjunto de reales donde cada operación de la fórmula tiene sentido. El método es **recorrer la expresión e imponer una condición por cada operación**, y luego **intersecar** todas:

| Aparece | Condición |
|---|---|
| Cociente $\dfrac{u}{v}$ | $v \ne 0$ |
| Raíz de índice par $\sqrt[2k]{u}$ | $u \ge 0$ (y $u > 0$ si la raíz está en un denominador) |
| Raíz de índice impar | ninguna (más las de $u$) |
| Logaritmo $\log_a u$ | $u > 0$ |
| $\operatorname{arcsen} u$, $\arccos u$ | $-1 \le u \le 1$ |
| $\tan u$ | $u \ne \frac{\pi}{2} + k\pi$ |
| Función por tramos | dominio de cada tramo **intersecado con su intervalo**, y luego unión |

Las condiciones de **funciones anidadas** se aplican de adentro hacia afuera.

### Ejemplo 5 · Tres dominios naturales

<!-- check: U1.T.ALG.5 -->
a) $f(x) = \dfrac{\ln(4 - x^2)}{\sqrt{x + 1}}$. Condiciones: $4 - x^2 > 0 \iff -2 < x < 2$; $x + 1 > 0$ (raíz en el denominador, estricta) $\iff x > -1$. La intersección es $(-1, 2)$.

b) $g(x) = \sqrt{x^2 - x - 6} + \dfrac{1}{x - 4}$. Condiciones: $x^2 - x - 6 = (x - 3)(x + 2) \ge 0 \iff x \le -2$ o $x \ge 3$; y $x \ne 4$. El dominio es $(-\infty, -2] \cup [3, 4) \cup (4, +\infty)$.

c) $h(x) = \operatorname{arcsen}\left(\dfrac{2x - 1}{3}\right)$. Condición: $-1 \le \dfrac{2x - 1}{3} \le 1 \iff -3 \le 2x - 1 \le 3 \iff -1 \le x \le 2$. El dominio es $[-1, 2]$.

:::caution[Errores frecuentes]
- Simplificar antes de hallar el dominio: $\frac{x^2 - 9}{x - 3}$ y $x + 3$ **no** tienen el mismo dominio.
- Olvidar que la raíz cuadrada en un denominador exige radicando **estrictamente** positivo.
- Calcular el dominio de $f \circ g$ como el de $f$ o el de $g$ solamente: hacen falta ambas condiciones.
- Pasar de $\ln(xy)$ a $\ln x + \ln y$ sin cambiar el dominio.
- Dar la composición en el orden inverso: $f \circ g$ aplica $g$ primero.
:::

## Transformaciones de gráficos

Si se conoce el gráfico de $y = f(x)$, se puede obtener el de muchas funciones relacionadas sin recalcular punto por punto. La forma general es

$$
g(x) = a \, f\big(b\,(x - c)\big) + d.
$$

Los cuatro parámetros actúan así sobre un punto $(u, v)$ del gráfico de $f$:

$$
(u, v) \longmapsto \left(c + \frac{u}{b},\ a\,v + d\right).
$$

| Parámetro | Efecto | Detalle |
|---|---|---|
| $d$ | **desplazamiento vertical** | sube si $d > 0$, baja si $d < 0$ |
| $c$ | **desplazamiento horizontal** | derecha si $c > 0$, izquierda si $c < 0$ |
| $a$ | **alargamiento / contracción vertical** | se estira si $|a| > 1$, se comprime si $0 < |a| < 1$; si $a < 0$, además **refleja respecto del eje $x$** |
| $b$ | **contracción / alargamiento horizontal** | se comprime si $|b| > 1$, se estira si $0 < |b| < 1$; si $b < 0$, además **refleja respecto del eje $y$** |

![Gráficos de √x, √(x−3), √(x+2) y √x + 1,5.](/analisis-matematico-i/figuras/u1-transf-desplazamientos.svg)

*Observá que restar dentro de la raíz mueve el gráfico a la **derecha**, sumar lo mueve a la izquierda, y sumar afuera lo sube; la forma no cambia.*

![Gráficos de √x, −√x, √(−x) y 2√x.](/analisis-matematico-i/figuras/u1-transf-reflexiones.svg)

*Observá que $-f(x)$ voltea el gráfico respecto del eje $x$ (queda debajo), $f(-x)$ lo voltea respecto del eje $y$ (queda a la izquierda) y $2f(x)$ lo estira al doble de altura.*

**Regla práctica.** Lo que se hace **afuera** de $f$ (sobre $y$) actúa como se espera: sumar sube, multiplicar estira. Lo que se hace **adentro** (sobre $x$) actúa «al revés»: restar mueve a la derecha, multiplicar por un número mayor que $1$ comprime.

**Orden.** Para dibujar $g$ se aplica, en este orden: (1) el escalamiento horizontal por $b$ (y su reflexión), (2) el desplazamiento horizontal $c$, (3) el escalamiento vertical por $a$ (y su reflexión), (4) el desplazamiento vertical $d$. Es muy importante escribir el interior como $b(x - c)$: en $f(2x - 6)$ el desplazamiento **no** es $6$, porque $2x - 6 = 2(x - 3)$ y entonces $b = 2$, $c = 3$.

### Qué cambia

Si $g(x) = a f\big(b(x - c)\big) + d$:

- **Dominio:** $D_g = \{x : b(x - c) \in D_f\}$, es decir, $c + \frac{1}{b} D_f$.
- **Imagen:** $\operatorname{Im} g = a \operatorname{Im} f + d$.
- **Ceros:** son los $x$ con $f\big(b(x - c)\big) = -\dfrac{d}{a}$; si $d = 0$, son $c + \dfrac{z}{b}$ para cada cero $z$ de $f$.
- **Período:** si $f$ tiene período $P$, $g$ tiene período $\dfrac{P}{|b|}$.
- **Asíntotas:** una vertical $x = v$ pasa a $x = c + \dfrac{v}{b}$; una horizontal $y = k$ pasa a $y = a k + d$.

### Ejemplo 6 · Cuatro movimientos sobre $\sqrt{x}$

Describir $g(x) = -2\sqrt{x - 3} + 1$ a partir de $f(x) = \sqrt{x}$.

Aquí $a = -2$, $b = 1$, $c = 3$, $d = 1$. Los movimientos: desplazar $3$ a la derecha; estirar verticalmente al doble; reflejar respecto del eje $x$; subir $1$. El punto $(0, 0)$ de $f$ va a $(3, 1)$.

![Gráficos de √x y de g(x) = −2√(x−3) + 1, con el punto de inicio (3, 1) y el cero marcado.](/analisis-matematico-i/figuras/u1-transf-composicion.svg)

*Observá que el gráfico de $g$ nace en $(3, 1)$, baja (por la reflexión) y cruza el eje $x$ en $\frac{13}{4}$.*

<!-- check: U1.T.TRA.1 -->
Dominio: $x - 3 \ge 0 \Rightarrow D_g = [3, +\infty)$. Imagen: $-2\,[0, +\infty) + 1 = (-\infty, 1]$. Cero: $-2\sqrt{x - 3} + 1 = 0 \Rightarrow \sqrt{x - 3} = \frac12 \Rightarrow x = \frac{13}{4}$.

### Ejemplo 7 · El desplazamiento horizontal oculto

<!-- check: U1.T.TRA.2 -->
a) $y = (2x - 6)^2$ a partir de $f(x) = x^2$. Como $2x - 6 = 2(x - 3)$, $b = 2$ y $c = 3$: se comprime horizontalmente a la mitad y se desplaza **3** (no $6$) a la derecha. Equivale a $4(x - 3)^2$: vértice en $(3, 0)$.

b) Sea $f$ con $D_f = [0, 4]$ y $f(x) = (x - 1)(x - 3)$ (ceros $1$ y $3$), y $g(x) = f(2x - 1) = f\big(2(x - \tfrac12)\big)$. Entonces $b = 2$, $c = \frac12$. Dominio: $0 \le 2x - 1 \le 4 \iff \frac12 \le x \le \frac52$. Ceros: $2x - 1 = 1 \Rightarrow x = 1$ y $2x - 1 = 3 \Rightarrow x = 2$; es decir, $c + z/b = \frac12 + \frac{1}{2} = 1$ y $\frac12 + \frac32 = 2$. La expresión es $g(x) = (2x - 2)(2x - 4) = 4(x - 1)(x - 2)$.

### Ejemplo 8 · Transformaciones de una función periódica

Analizar $g(x) = 3\operatorname{sen}\left(2x - \dfrac{\pi}{2}\right) + 1$.

<!-- check: U1.T.TRA.3 -->
Reescribimos el interior: $2x - \frac{\pi}{2} = 2\left(x - \frac{\pi}{4}\right)$. Entonces $a = 3$, $b = 2$, $c = \frac{\pi}{4}$, $d = 1$: amplitud $3$, período $\dfrac{2\pi}{2} = \pi$, desfase $\frac{\pi}{4}$ a la derecha y nivel medio $1$. La imagen es $[1 - 3, 1 + 3] = [-2, 4]$. El máximo se da cuando $2x - \frac{\pi}{2} = \frac{\pi}{2}$, es decir, en $x = \frac{\pi}{2}$ (con $g = 4$); el mínimo en $x = 0$ ($\operatorname{sen}(-\frac{\pi}{2}) = -1$, $g = -2$).

### Ejemplo 9 · Transformaciones de una exponencial

Analizar $g(x) = -3\cdot 2^{x + 1} + 5$ a partir de $f(x) = 2^x$.

<!-- check: U1.T.TRA.4 -->
Movimientos: desplazar $1$ a la izquierda ($c = -1$), estirar al triple, reflejar respecto del eje $x$ y subir $5$. La asíntota horizontal $y = 0$ pasa a $y = -3\cdot 0 + 5 = 5$. Imagen: $-3\,(0, +\infty) + 5 = (-\infty, 5)$. Ordenada al origen: $g(0) = -6 + 5 = -1$. Cero: $2^{x + 1} = \frac53 \Rightarrow x = \log_2\frac53 - 1 \approx -0{,}263$.

:::caution[Errores frecuentes]
- Desplazar en el sentido contrario: $f(x - 3)$ va a la **derecha**.
- Tomar el desplazamiento de $f(2x - 6)$ como $6$ en vez de $3$.
- Aplicar las transformaciones en cualquier orden: escalar y desplazar **no** conmutan.
- Reflejar un dominio o una imagen sin reflejar los extremos: la imagen de $-2\sqrt{x}$ es $(-\infty, 0]$.
- Pensar que el período de $\operatorname{sen}(bx)$ es $2\pi b$ (es $2\pi/|b|$).
:::

## Ejercicios

### Ejercicio 14 · Dominio natural
<!-- ejercicio: U1.14 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallar el dominio natural de $f(x) = \sqrt{2x - 6} + \dfrac{1}{x - 5}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Una condición por operación y después la intersección.

**Desarrollo.** La raíz exige $2x - 6 \ge 0 \iff x \ge 3$. El cociente exige $x \ne 5$. Intersecando, $[3, +\infty) \setminus \{5\}$.

**Resultado.** $D_f = [3, 5) \cup (5, +\infty)$.

</details>

### Ejercicio 15 · ¿Son iguales?
<!-- ejercicio: U1.15 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Decidir si son iguales los pares siguientes (con dominio natural). Si no lo son, indicar cómo restringir para que lo sean.
a) $f(x) = \dfrac{x^2 - 1}{x + 1}$ y $g(x) = x - 1$.
b) $f(x) = \ln\big((x - 1)(x + 1)\big)$ y $g(x) = \ln(x - 1) + \ln(x + 1)$.
c) $f(x) = e^{\ln x}$ y $g(x) = x$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Comparar dominios naturales y después las reglas.

**Desarrollo.** a) $D_f = \mathbb{R} \setminus \{-1\}$ y $D_g = \mathbb{R}$. Para $x \ne -1$, $f(x) = x - 1$. No son iguales; lo serían restringiendo $g$ a $\mathbb{R} \setminus \{-1\}$.

b) $D_f$: $(x - 1)(x + 1) > 0 \iff x < -1$ o $x > 1$. $D_g$: $x - 1 > 0$ y $x + 1 > 0 \iff x > 1$. Los dominios difieren (por ejemplo $f(-2) = \ln 3$, pero $g(-2)$ no existe). Coinciden las reglas en $(1, +\infty)$: restringiendo $f$ a ese intervalo, son iguales.

c) $D_f = (0, +\infty)$ y $D_g = \mathbb{R}$. En $(0, +\infty)$, $e^{\ln x} = x$. No son iguales; lo serían restringiendo $g$ a $(0, +\infty)$.

**Resultado.** Ninguno de los tres pares es de funciones iguales; se igualan restringiendo: a) $g$ a $\mathbb{R} \setminus \{-1\}$; b) $f$ a $(1, +\infty)$; c) $g$ a $(0, +\infty)$.

</details>

### Ejercicio 16 · Composiciones
<!-- ejercicio: U1.16 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $f(x) = \ln(x - 1)$ y $g(x) = \sqrt{9 - x^2}$.
a) Hallar el dominio de $f \circ g$ y calcular $(f \circ g)(0)$.
b) Hallar el dominio de $g \circ f$ y calcular $(g \circ f)(2)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para $f \circ g$ se pide $x \in D_g$ y $g(x) \in D_f$; para $g \circ f$, $x \in D_f$ y $f(x) \in D_g$.

**Desarrollo.** a) $D_g = [-3, 3]$. Además $g(x) \in D_f = (1, +\infty)$: $\sqrt{9 - x^2} > 1 \iff 9 - x^2 > 1 \iff x^2 < 8 \iff |x| < 2\sqrt2$. Como $2\sqrt2 \approx 2{,}83 < 3$, el dominio es $\left(-2\sqrt2, 2\sqrt2\right)$. $(f \circ g)(0) = \ln(3 - 1) = \ln 2$.

b) $D_f = (1, +\infty)$. Además $f(x) \in D_g = [-3, 3]$: $-3 \le \ln(x - 1) \le 3 \iff e^{-3} \le x - 1 \le e^{3}$. El dominio es $\left[1 + e^{-3},\ 1 + e^{3}\right]$. $(g \circ f)(2) = \sqrt{9 - (\ln 1)^2} = 3$.

**Resultado.** a) $D_{f \circ g} = (-2\sqrt2, 2\sqrt2)$, $(f \circ g)(0) = \ln 2$; b) $D_{g \circ f} = [1 + e^{-3}, 1 + e^{3}]$, $(g \circ f)(2) = 3$.

</details>

### Ejercicio 17 · Transformaciones sobre una parábola
<!-- ejercicio: U1.17 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f\colon [0, 4] \to \mathbb{R}$, $f(x) = 4x - x^2$, y $g(x) = 2f(3 - x) + 1$.
a) Describir los movimientos que llevan el gráfico de $f$ al de $g$.
b) Hallar el dominio, la imagen y los ceros de $g$, y una fórmula polinómica para $g$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escribir $g$ en la forma $a f(b(x - c)) + d$ y leer los parámetros; después comprobar con la fórmula.

**Desarrollo.** a) $f(3 - x) = f\big(-(x - 3)\big)$: $b = -1$, $c = 3$, $a = 2$, $d = 1$. Los movimientos son: reflexión respecto del eje $y$, desplazamiento $3$ a la derecha, estiramiento vertical al doble y desplazamiento $1$ hacia arriba.

b) *Dominio:* $0 \le 3 - x \le 4 \iff -1 \le x \le 3$. *Imagen de $f$:* el vértice está en $x = 2$ con $f(2) = 4$ y los extremos valen $f(0) = f(4) = 0$: $\operatorname{Im} f = [0, 4]$; entonces $\operatorname{Im} g = 2\,[0, 4] + 1 = [1, 9]$. *Fórmula:* $f(3 - x) = 4(3 - x) - (3 - x)^2 = (3 - x)\big(4 - 3 + x\big) = (3 - x)(1 + x)$, así que
$$
g(x) = 2(3 - x)(1 + x) + 1 = -2x^2 + 4x + 7.
$$
Su vértice está en $x = 1$ con $g(1) = 9$ y en los extremos $g(-1) = g(3) = 1$, de acuerdo con la imagen. *Ceros:* como $g \ge 1$ en todo el dominio, no tiene.

**Resultado.** $D_g = [-1, 3]$, $\operatorname{Im} g = [1, 9]$, sin ceros, $g(x) = -2x^2 + 4x + 7$.

</details>

## Autoevaluación

**1. ¿Cuál es el dominio de $\dfrac{f}{g}$ en términos de $D_f$, $D_g$ y los ceros de $g$?**

<details>
<summary>Respuesta</summary>

$(D_f \cap D_g) \setminus \{x : g(x) = 0\}$.
</details>

**2. Si $f(x) = \sqrt{x}$ y $g(x) = x - 5$, ¿cuál es el dominio de $f \circ g$?**

<details>
<summary>Respuesta</summary>

$g(x) \ge 0 \iff x \ge 5$: $[5, +\infty)$.
</details>

**3. ¿Qué movimiento produce $f(x + 2)$?**

<details>
<summary>Respuesta</summary>

Un desplazamiento de $2$ unidades hacia la **izquierda**.
</details>

**4. ¿Qué le pasa a la imagen de $f$ en $g(x) = -3f(x) + 2$?**

<details>
<summary>Respuesta</summary>

Pasa a $-3\operatorname{Im} f + 2$: se estira por $3$, se refleja y se sube $2$. Por ejemplo, si $\operatorname{Im} f = [0, 1]$, entonces $\operatorname{Im} g = [-1, 2]$.
</details>

:::tip[En resumen]
- Dos funciones son iguales si coinciden dominio, codominio y regla; la misma fórmula con distinto dominio da funciones distintas.
- La suma, el producto y el cociente se definen en la intersección de dominios (y el cociente excluye los ceros del divisor); $f \circ g$ aplica primero $g$ y exige $x \in D_g$ y $g(x) \in D_f$.
- Dominio natural: una condición por operación (denominador $\ne 0$, radicando par $\ge 0$, logaritmo $> 0$, arcsen en $[-1, 1]$) e intersección.
- $g = a f(b(x - c)) + d$ lleva $(u, v)$ a $(c + u/b,\ a v + d)$; hay que escribir el interior como $b(x - c)$ y aplicar los movimientos en orden.
:::

**Para seguir.** Con la composición en mano, estudiamos cuándo una función se puede «deshacer»: [funciones biyectivas y función inversa](/analisis-matematico-i/unidad-1/teoria/inversa/). Para visualizar los parámetros $a, b, c, d$ con deslizadores, mirá la [guía de GeoGebra](/analisis-matematico-i/geogebra/funciones/).
