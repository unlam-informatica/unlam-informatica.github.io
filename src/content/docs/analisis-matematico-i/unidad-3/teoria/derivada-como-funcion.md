---
title: La derivada como función
description: Función derivada y su dominio, derivadas laterales, puntos donde una función no es derivable y demostración de que derivable implica continua.
slug: analisis-matematico-i/unidad-3/teoria/derivada-como-funcion
sidebar:
  order: 2
---

## Qué vas a aprender

- Obtener la función derivada $f'$ por definición y determinar su dominio.
- Estudiar la derivabilidad en un punto con las derivadas laterales, en especial en los puntos donde cambia la expresión de una función definida por tramos.
- Distinguir los casos en que una función continua no es derivable: punta, tangente vertical y cúspide.
- Demostrar que derivable implica continua y explicar con contraejemplos por qué la recíproca es falsa.

**Antes de empezar.** Repasá [la derivada en un punto](/analisis-matematico-i/unidad-3/teoria/razon-de-cambio-y-derivada/) y la [continuidad](/analisis-matematico-i/unidad-2/teoria/continuidad/), en particular los límites laterales.

## Introducción: una derivada en cada punto

En la lección anterior fijamos un punto $a$ y calculamos $f'(a)$, un número. Si repetimos el cálculo en cada $x$ donde sea posible, obtenemos una nueva función: la que a cada $x$ le asigna la pendiente de la tangente en ese punto.

:::note[Definición · Función derivada]
La **función derivada** de $f$ es

$$
f'(x) = \lim_{h \to 0} \dfrac{f(x + h) - f(x)}{h},
$$

definida en $D_{f'} = \{x \in D_f : f \text{ es derivable en } x\}$.
:::

Siempre $D_{f'} \subseteq D_f$, y la inclusión puede ser estricta: la derivada puede perder puntos que están en el dominio de $f$. Las notaciones $f'(x)$, $y'$ y $\frac{dy}{dx}$ son equivalentes. Si $x$ y $f$ tienen unidades $[x]$ y $[f]$, la función $f'$ tiene unidades $[f]/[x]$.

Como $f'$ es una función, puede derivarse otra vez: la **derivada segunda** es $f'' = (f')'$, o $\dfrac{d^2 y}{dx^2}$, y en general la **derivada $n$-ésima** $f^{(n)}$ se obtiene derivando $n$ veces. Las necesitaremos en la [Unidad 4](/analisis-matematico-i/unidad-4/); por ahora basta saber que se calculan derivando el resultado anterior, y que cada derivación puede achicar el dominio.

![Gráfico de f(x) = x³/3 − x y de su derivada f′(x) = x² − 1](/analisis-matematico-i/figuras/u3-f-y-derivada.svg)

*Donde $f'$ vale $0$ (en $x = \pm 1$, puntos huecos) la gráfica de $f$ tiene tangente horizontal (puntos llenos); donde $f'$ es negativa, $f$ decrece.*

### Ejemplo 1 · Derivada de un cociente por definición
<!-- check: U3.T.FUN.1 -->

Para $f(x) = \dfrac{1}{x + 2}$ ($D_f = \mathbb{R} - \{-2\}$) y $x \neq -2$:

$$
\dfrac{f(x + h) - f(x)}{h} = \dfrac{1}{h}\left(\dfrac{1}{x + h + 2} - \dfrac{1}{x + 2}\right) = \dfrac{1}{h} \cdot \dfrac{(x + 2) - (x + h + 2)}{(x + h + 2)(x + 2)} = \dfrac{-1}{(x + h + 2)(x + 2)}.
$$

Al hacer $h \to 0$ (el denominador no se anula, pues $x \neq -2$) resulta

$$
f'(x) = -\dfrac{1}{(x + 2)^2}, \qquad D_f = D_{f'} = \mathbb{R} - \{-2\}.
$$

### Ejemplo 2 · Cuando el dominio de la derivada es menor
<!-- check: U3.T.FUN.2 -->

Sea $g(x) = \sqrt{2x - 1}$, con $D_g = \left[\tfrac12, +\infty\right)$. Para $x > \frac12$:

$$
\dfrac{g(x + h) - g(x)}{h} = \dfrac{(2x - 1 + 2h) - (2x - 1)}{h\,\bigl(\sqrt{2x - 1 + 2h} + \sqrt{2x - 1}\bigr)} = \dfrac{2}{\sqrt{2x - 1 + 2h} + \sqrt{2x - 1}} \xrightarrow[h \to 0]{} \dfrac{1}{\sqrt{2x - 1}}.
$$

Entonces $g'(x) = \dfrac{1}{\sqrt{2x - 1}}$ con $D_{g'} = \left(\tfrac12, +\infty\right)$. El punto $x = \tfrac12$ está en $D_g$ pero no en $D_{g'}$: allí el cociente incremental, que solo puede calcularse con $h > 0$, vale $\frac{\sqrt{2h}}{h} = \sqrt{\frac{2}{h}} \to +\infty$ (tangente vertical).

## Derivadas laterales

Como $f'(a)$ es un límite, existe si y solo si existen los dos límites laterales y coinciden. Los nombramos.

:::note[Definición · Derivadas laterales]
La **derivada por la derecha** y **por la izquierda** de $f$ en $a$ son

$$
f'_{+}(a) = \lim_{h \to 0^{+}} \dfrac{f(a + h) - f(a)}{h}, \qquad f'_{-}(a) = \lim_{h \to 0^{-}} \dfrac{f(a + h) - f(a)}{h}.
$$
:::

:::note[Propiedad]
$f$ es derivable en $a$ si y solo si existen $f'_{+}(a)$ y $f'_{-}(a)$, son finitas y son iguales; en ese caso, $f'(a) = f'_{+}(a) = f'_{-}(a)$.
:::

Esto es la propiedad de los [límites laterales](/analisis-matematico-i/unidad-2/teoria/limites-laterales-y-propiedades/) aplicada al cociente incremental. Se usa cuando la función cambia de expresión, tiene valor absoluto o está definida por tramos.

### Ejemplo 3 · La función módulo en el origen
<!-- check: U3.T.FUN.3 -->

Para $f(x) = \lvert x \rvert$ y $a = 0$, el cociente incremental es $\dfrac{\lvert h \rvert}{h}$. Por derecha, $h > 0$ y vale $1$; por izquierda, $h < 0$, $\lvert h \rvert = -h$ y vale $-1$:

$$
f'_{+}(0) = 1, \qquad f'_{-}(0) = -1.
$$

Los laterales son distintos, de modo que $f$ no es derivable en $0$. El gráfico tiene una **punta** (punto angular): las secantes de un lado tienen pendiente $-1$ y las del otro, $+1$, y no se acercan a una única recta.

### Ejemplo 4 · Una función definida por tramos
<!-- check: U3.T.FUN.4 -->

Sea

$$
f(x) = \begin{cases} x^2 + 1 & \text{si } x \le 1 \\ 3x - 1 & \text{si } x > 1. \end{cases}
$$

*Continuidad en $x = 1$.* $f(1) = 2$, $\lim_{x \to 1^-} f(x) = 2$ y $\lim_{x \to 1^+} f(x) = 3 - 1 = 2$: es continua.

*Derivadas laterales en $x = 1$*, con la definición y el valor $f(1) = 2$:

$$
f'_{-}(1) = \lim_{h \to 0^-} \dfrac{(1 + h)^2 + 1 - 2}{h} = \lim_{h \to 0^-} (2 + h) = 2, \qquad f'_{+}(1) = \lim_{h \to 0^+} \dfrac{3(1 + h) - 1 - 2}{h} = \lim_{h \to 0^+} 3 = 3.
$$

Como $2 \neq 3$, $f$ no es derivable en $x = 1$, aunque es continua. La función derivada es

$$
f'(x) = \begin{cases} 2x & \text{si } x < 1 \\ 3 & \text{si } x > 1, \end{cases} \qquad D_{f'} = \mathbb{R} - \{1\}.
$$

### Ejemplo 5 · Parámetros para derivabilidad
<!-- check: U3.T.FUN.5 -->

¿Qué valores de $a$ y $b$ hacen derivable en $x = 1$ a la función $f(x) = \begin{cases} x^3 + 1 & \text{si } x \le 1 \\ ax + b & \text{si } x > 1\end{cases}$?

Para que haya derivada se necesitan dos cosas, y en este orden: (i) **continuidad**, $f(1) = 2 = a + b$; (ii) **derivadas laterales iguales**, $f'_{-}(1) = 3 \cdot 1^2 = 3$ y $f'_{+}(1) = a$. De (ii) $a = 3$ y de (i) $b = -1$. Con esos valores, $f$ es derivable en $1$ y $f'(1) = 3$.

La derivada lateral se calcula derivando la expresión de cada tramo porque, una vez asegurada la continuidad, el cociente incremental de cada lado usa solo valores de ese tramo (con $f(1) = 2$, que coincide con el valor de ambas expresiones en $x = 1$). Por eso el orden importa: sin continuidad, $f(1)$ no sería el valor del tramo derecho y el cálculo no valdría.

## Cuando una función continua no es derivable

Hay tres comportamientos típicos de una función **continua** en $a$ que no es derivable en $a$:

| Situación | Derivadas laterales | Gráfico | Ejemplo en $a = 0$ |
|---|---|---|---|
| **Punta** (punto angular) | finitas y distintas | dos tangentes distintas | $\lvert x \rvert$ |
| **Tangente vertical** | ambas $+\infty$ o ambas $-\infty$ | una sola tangente, vertical | $\sqrt[3]{x}$ |
| **Cúspide** (punto de retroceso) | infinitas de signo opuesto | tangente vertical, con la curva que vuelve sobre sí misma | $\sqrt[3]{x^2}$ |

![Gráficos de |x|, de la raíz cúbica y de x elevado a 2/3 cerca del origen](/analisis-matematico-i/figuras/u3-no-derivable.svg)

*En el origen, $\lvert x \rvert$ tiene una punta, $x^{1/3}$ sube con pendiente vertical y $x^{2/3}$ forma una cúspide con las dos ramas hacia arriba.*

### Ejemplo 6 · Tangente vertical frente a cúspide
<!-- check: U3.T.FUN.6 -->

Para $f(x) = \sqrt[3]{x}$ en $a = 0$ el cociente es $\dfrac{\sqrt[3]{h}}{h} = h^{-2/3}$, que tiende a $+\infty$ cuando $h \to 0^{+}$ y también cuando $h \to 0^{-}$ (porque $h^{-2/3} = \frac{1}{\sqrt[3]{h^2}} > 0$). Ambas derivadas laterales valen $+\infty$: tangente vertical $x = 0$. No es derivable (el límite no es finito).

Para $n(x) = \sqrt[3]{x^2}$ el cociente es $\dfrac{\sqrt[3]{h^2}}{h}$: vale $h^{-1/3} \to +\infty$ si $h \to 0^{+}$ y, si $h \to 0^{-}$, es negativo y tiende a $-\infty$. Las derivadas laterales son infinitas de signo opuesto: cúspide. Las secantes por el origen se acercan a la recta vertical $x = 0$ desde los dos lados, así que esa recta es tangente; lo que distingue a la cúspide es que las dos ramas llegan al origen desde el mismo lado (aquí, desde arriba) y la curva vuelve sobre sí misma. Algunos libros reservan el nombre «tangente vertical» para el caso de infinitos del mismo signo; en los dos casos la función **no es derivable** en el punto.

## Derivable implica continua

:::note[Teorema]
**Hipótesis:** $f$ es derivable en $a$. **Tesis:** $f$ es continua en $a$.
:::

**Demostración (formal).** Que $f$ sea derivable en $a$ incluye que está definida en un entorno de $a$. Para $x \neq a$ en ese entorno escribimos

$$
f(x) - f(a) = \dfrac{f(x) - f(a)}{x - a}\,(x - a).
$$

Cuando $x \to a$, el primer factor tiende a $f'(a)$, un número real, y el segundo tiende a $0$. Por el límite de un producto,

$$
\lim_{x \to a} \bigl(f(x) - f(a)\bigr) = f'(a) \cdot 0 = 0,
$$

es decir, $\lim_{x \to a} f(x) = f(a)$, que es la continuidad de $f$ en $a$. $\blacksquare$

**Consecuencia útil (contrarrecíproca).** Si $f$ **no** es continua en $a$, entonces $f$ **no** es derivable en $a$. No hace falta calcular ningún cociente: una discontinuidad (evitable, de salto o infinita) ya impide la derivada.

**La recíproca es falsa.** La hipótesis «continua» no alcanza: $\lvert x \rvert$ es continua en $0$ y no es derivable (punta); $\sqrt[3]{x}$ y $\sqrt[3]{x^2}$ también son continuas en $0$ y no son derivables (tangente vertical y cúspide).

:::note[Observación · $f'$ puede no ser continua]
Aun siendo $f$ derivable en $a$, la función derivada puede no ser continua en $a$. El ejemplo clásico es $f(x) = x^2 \operatorname{sen}\frac{1}{x}$ si $x \neq 0$ y $f(0) = 0$: es derivable en $0$ con $f'(0) = 0$, pero $f'(x) = 2x \operatorname{sen}\frac1x - \cos\frac1x$ para $x \neq 0$ oscila entre valores cercanos a $-1$ y $1$ cuando $x \to 0$, y su límite en $0$ no existe.
:::

### Ejemplo 7 · Derivable en el origen con derivada discontinua
<!-- check: U3.T.FUN.7 -->

Para el $f$ de la observación: $\left\lvert h \operatorname{sen}\frac1h \right\rvert \le \lvert h \rvert \to 0$, de modo que

$$
f'(0) = \lim_{h \to 0} \dfrac{h^2 \operatorname{sen}(1/h)}{h} = \lim_{h \to 0} h \operatorname{sen}\dfrac1h = 0.
$$

Para $x \neq 0$, la regla del producto y la de la cadena (que veremos en las próximas lecciones) dan $f'(x) = 2x \operatorname{sen}\frac1x - \cos\frac1x$. En la sucesión $x_k = \frac{1}{2k\pi} \to 0$ vale $f'(x_k) = -1$ y en $y_k = \frac{1}{(2k+1)\pi} \to 0$ vale $f'(y_k) = 1$: el límite $\lim_{x\to 0} f'(x)$ no existe y, en particular, $f'$ no es continua en $0$.

:::caution[Errores frecuentes]
- **Derivar el tramo y no mirar el empalme.** En el punto donde cambia la expresión hay que verificar primero la continuidad y después comparar $f'_{-}$ y $f'_{+}$. Con una discontinuidad no hay derivada.
- **Calcular $f'_{+}(a)$ con la expresión del tramo equivocado**, o con $f(a)$ tomado del otro tramo.
- **Creer que «continua» alcanza para «derivable»**, o que «derivable» garantiza que $f'$ sea continua. Ninguna implicación es cierta.
- **Confundir tangente vertical con cúspide.** En ambas el cociente incremental no tiene límite finito, pero el signo de los infinitos laterales los distingue.
- **Olvidar que $D_{f'}$ puede ser menor que $D_f$** (extremos del dominio, puntas, tangentes verticales).
:::

## Ejercicios

### Ejercicio 5 · Derivada por definición y tangente
<!-- ejercicio: U3.05 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \dfrac{x}{x - 1}$.

a) Hallá $f'(x)$ con la definición e indicá $D_f$ y $D_{f'}$.

b) Calculá $f'(3)$ y la ecuación de la recta tangente en $x = 3$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escribir el cociente incremental, restar las fracciones con denominador común, simplificar el factor $h$ y tomar el límite.

**Desarrollo.** a) $D_f = \mathbb{R} - \{1\}$. Para $x \neq 1$,

$$
\dfrac{f(x + h) - f(x)}{h} = \dfrac{1}{h} \cdot \dfrac{(x + h)(x - 1) - x(x + h - 1)}{(x + h - 1)(x - 1)} = \dfrac{1}{h} \cdot \dfrac{-h}{(x + h - 1)(x - 1)} = \dfrac{-1}{(x + h - 1)(x - 1)},
$$

porque $(x + h)(x - 1) - x(x + h - 1) = x^2 - x + hx - h - x^2 - xh + x = -h$. Al hacer $h \to 0$ queda $f'(x) = -\dfrac{1}{(x - 1)^2}$, con $D_{f'} = \mathbb{R} - \{1\} = D_f$.

b) $f'(3) = -\dfrac{1}{4}$ y $f(3) = \dfrac{3}{2}$. La tangente es $y = \dfrac{3}{2} - \dfrac{1}{4}(x - 3)$.

**Resultado.** $f'(x) = -\dfrac{1}{(x-1)^2}$, $D_f = D_{f'} = \mathbb{R} - \{1\}$; en $x = 3$: $f'(3) = -\frac14$ y $y = \frac32 - \frac{x - 3}{4}$.

</details>

### Ejercicio 6 · Derivabilidad de una función por tramos
<!-- ejercicio: U3.06 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \begin{cases} a x^2 + 1 & \text{si } x \le 2 \\ b x - 3 & \text{si } x > 2. \end{cases}$

a) Hallá $a$ y $b$ para que $f$ sea derivable en $x = 2$.

b) Con esos valores escribí $f'$ y calculá $f'_{-}(2)$ y $f'_{+}(2)$ con la definición.

c) Si $a = 1$ y $b = 0$, ¿es $f$ continua en $2$? ¿Derivable?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Imponer continuidad y, luego, igualdad de las derivadas laterales.

**Desarrollo.** a) Continuidad: $f(2) = 4a + 1$ y $\lim_{x \to 2^+}(bx - 3) = 2b - 3$, luego $4a + 1 = 2b - 3$. Derivadas de cada tramo en $x = 2$: $2ax\big|_{2} = 4a$ y $b$, luego $4a = b$. Reemplazando: $4a + 1 = 8a - 3 \Rightarrow a = 1$ y $b = 4$.

b) $f(x) = x^2 + 1$ si $x \le 2$ y $f(x) = 4x - 3$ si $x > 2$; $f(2) = 5$. Por definición:

$$
f'_{-}(2) = \lim_{h \to 0^-} \dfrac{(2 + h)^2 + 1 - 5}{h} = \lim_{h \to 0^-} (4 + h) = 4, \qquad f'_{+}(2) = \lim_{h \to 0^+} \dfrac{4(2 + h) - 3 - 5}{h} = \lim_{h \to 0^+} 4 = 4.
$$

Por lo tanto $f'(x) = 2x$ si $x < 2$, $f'(2) = 4$ y $f'(x) = 4$ si $x > 2$.

c) Con $a = 1$ y $b = 0$: $f(2) = 5$ pero $\lim_{x \to 2^+}(0 \cdot x - 3) = -3 \neq 5$. Hay un salto, $f$ no es continua en $2$ y, por lo tanto, tampoco derivable (aunque $4a = 4 \neq 0 = b$ ya lo impediría).

**Resultado.** a) $a = 1$, $b = 4$. b) $f'_{-}(2) = f'_{+}(2) = 4$. c) No es continua ni derivable en $2$.

</details>

### Ejercicio 7 · Derivada de una función par
<!-- ejercicio: U3.07 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $f$ una función definida en $\mathbb{R}$ y derivable en todo punto.

a) Demostrá que si $f$ es **par** ($f(-x) = f(x)$ para todo $x$), entonces $f'$ es **impar**.

b) ¿Qué ocurre con $f'$ si $f$ es impar? Justificá.

c) Concluí que si $f$ es par y derivable en $0$, entonces $f'(0) = 0$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escribir $f'(-a)$ por definición, usar la paridad para llevar el cociente al punto $a$ y cambiar de variable $k = -h$.

**Desarrollo.** a) Fijemos $a \in \mathbb{R}$. Por definición y por la paridad ($f(-a + h) = f(a - h)$ y $f(-a) = f(a)$):

$$
f'(-a) = \lim_{h \to 0} \dfrac{f(-a + h) - f(-a)}{h} = \lim_{h \to 0} \dfrac{f(a - h) - f(a)}{h}.
$$

Con $k = -h$ (cuando $h \to 0$, también $k \to 0$) el último límite es $\lim_{k \to 0} \dfrac{f(a + k) - f(a)}{-k} = -f'(a)$. Luego $f'(-a) = -f'(a)$ para todo $a$: $f'$ es impar.

b) Si $f$ es impar, $f(-a + h) = -f(a - h)$ y $f(-a) = -f(a)$. Entonces $f'(-a) = \lim_{h \to 0} \dfrac{f(a) - f(a - h)}{h}$. Con $k = -h$ el cociente es $\dfrac{f(a) - f(a + k)}{-k} = \dfrac{f(a + k) - f(a)}{k}$, que tiende a $f'(a)$. Por lo tanto $f'(-a) = f'(a)$ y $f'$ es **par**.

c) Si $f$ es par, $f'(-0) = -f'(0)$, es decir $f'(0) = -f'(0)$, de donde $2f'(0) = 0$ y $f'(0) = 0$. Geométricamente: una curva simétrica respecto del eje $y$, si es suave en el eje, tiene allí tangente horizontal. Notá que $\lvert x \rvert$ es par y **no** cumple la conclusión, porque no es derivable en $0$.

**Resultado.** Par $\Rightarrow$ $f'$ impar; impar $\Rightarrow$ $f'$ par; par y derivable en $0$ $\Rightarrow$ $f'(0) = 0$.

</details>

## Autoevaluación

**1. ¿Puede ser $D_{f'}$ mayor que $D_f$?**

<details>
<summary>Respuesta</summary>

No. Para que exista $f'(x)$ hace falta que $f$ esté definida en $x$ (y en un entorno), de modo que $D_{f'} \subseteq D_f$.
</details>

**2. $f$ es continua en $a$ y $f'_{-}(a) = 3$, $f'_{+}(a) = 5$. ¿Es derivable en $a$? ¿Qué forma tiene el gráfico?**

<details>
<summary>Respuesta</summary>

No, porque los laterales son distintos. El gráfico tiene una punta con dos tangentes de pendientes $3$ (a la izquierda) y $5$ (a la derecha).
</details>

**3. Si $f$ tiene un salto en $a$, ¿puede ser derivable en $a$?**

<details>
<summary>Respuesta</summary>

No: derivable implica continua; la contrarrecíproca dice que sin continuidad no hay derivada.
</details>

**4. Si $f'$ es continua en $a$, ¿$f$ es derivable en $a$? Si $f$ es derivable en $a$, ¿$f'$ es continua en $a$?**

<details>
<summary>Respuesta</summary>

Hablar de la continuidad de $f'$ en $a$ ya supone que $f'(a)$ existe, es decir, que $f$ es derivable en $a$: la primera pregunta no agrega nada. La segunda es la importante: de que $f$ sea derivable en $a$ no se sigue que $f'$ sea continua en $a$ ($x^2\operatorname{sen}\frac1x$ es el contraejemplo).
</details>

:::tip[En resumen]
- La función derivada $f'(x)$ se define con el mismo límite para cada $x$; su dominio es el conjunto de puntos donde $f$ es derivable y está contenido en $D_f$.
- $f$ es derivable en $a$ si y solo si existen y coinciden, finitas, las derivadas laterales.
- Una función continua puede no ser derivable en $a$: punta (laterales finitas distintas), tangente vertical (ambas infinitas del mismo signo) o cúspide (infinitas de signo opuesto).
- Derivable $\Rightarrow$ continua (demostración con $f(x)-f(a) = \frac{f(x)-f(a)}{x-a}(x-a)$); la recíproca es falsa.
:::

**Para seguir.** Calcular cada derivada con la definición es lento. En [reglas de derivación](/analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion/) deducimos las derivadas de las funciones elementales y las reglas que permiten derivar sumas, productos y cocientes sin volver al límite.
