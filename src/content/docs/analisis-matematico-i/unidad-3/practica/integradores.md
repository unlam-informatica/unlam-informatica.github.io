---
title: Integradores — Unidad 3
description: Ejercicios integradores de estilo parcial sobre derivada, rectas tangentes, funciones por tramos, regla de la cadena, inversa y derivación logarítmica.
slug: analisis-matematico-i/unidad-3/practica/integradores
sidebar:
  order: 90
  label: Integradores
---

Estos ejercicios combinan temas de toda la unidad y tienen el formato de un parcial: desarrollo con justificación y un ítem de opción múltiple. Antes de empezar conviene haber leído las cinco lecciones: [razón de cambio y derivada](/analisis-matematico-i/unidad-3/teoria/razon-de-cambio-y-derivada/), [la derivada como función](/analisis-matematico-i/unidad-3/teoria/derivada-como-funcion/), [reglas de derivación](/analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion/), [regla de la cadena e inversa](/analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa/) y [derivación implícita y logarítmica](/analisis-matematico-i/unidad-3/teoria/implicita-y-logaritmica/). Intentá resolverlos sin mirar la resolución y después comparalos paso a paso.

### Ejercicio 19 · Función por tramos con logaritmo
<!-- ejercicio: U3.19 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \begin{cases} a x^2 + b & \text{si } x \le 1 \\ 1 + \ln x & \text{si } x > 1. \end{cases}$

a) Hallá $a$ y $b$ para que $f$ sea derivable en $x = 1$.

b) Con esos valores, escribí $f'$ en todo su dominio y la recta tangente en $x = 1$.

c) Hallá la recta tangente a la gráfica de $f$ en un punto con $x > 1$ que sea paralela a $y = \dfrac{x}{4} + 7$.

d) ¿Es $f'$ continua en $x = 1$?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para derivabilidad en el punto de empalme se pide continuidad y coincidencia de las derivadas laterales; después se deriva por tramos.

**Desarrollo.** a) Continuidad en $1$: $f(1) = a + b$ y $\lim_{x \to 1^+}(1 + \ln x) = 1$, luego $a + b = 1$. Derivadas laterales: la del tramo izquierdo es $2ax\big|_{x=1} = 2a$ y la del derecho es $\frac{1}{x}\big|_{x=1} = 1$. Igualando, $2a = 1$, entonces $a = \frac12$ y $b = \frac12$.

b) Con $a = b = \frac12$: $f(x) = \frac12 x^2 + \frac12$ si $x \le 1$. Entonces $f'(x) = x$ si $x < 1$, $f'(x) = \dfrac1x$ si $x > 1$, y $f'(1) = 1$ (por los laterales, que valen $1$). La función está definida en todo $\mathbb{R}$ (el logaritmo solo se usa para $x > 1$) y es derivable en todo punto: $D_{f'} = \mathbb{R}$. Tangente en $x = 1$: $f(1) = 1$, $y = 1 + 1\cdot(x - 1) = x$.

c) La pendiente buscada es $\frac14$. Para $x > 1$: $\frac1x = \frac14 \Rightarrow x = 4$, que cumple $x > 1$. $f(4) = 1 + \ln 4$, y la tangente es $y = 1 + \ln 4 + \dfrac14(x - 4)$.

d) $\lim_{x \to 1^-} f'(x) = 1$, $\lim_{x \to 1^+} f'(x) = 1$ y $f'(1) = 1$: $f'$ es continua en $1$.

**Resultado.** a) $a = b = \frac12$; b) $f'(x) = x$ ($x < 1$), $f'(1) = 1$, $f'(x) = \frac1x$ ($x > 1$), tangente $y = x$; c) $y = 1 + \ln 4 + \frac{x - 4}{4}$; d) sí.

</details>

### Ejercicio 20 · Concentración de un fármaco (con GeoGebra)
<!-- ejercicio: U3.20 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
La concentración de un fármaco en sangre, en mg/l, $t$ horas después de la inyección es $C(t) = 20\,t\,e^{-t/2}$ para $t \ge 0$.

a) Calculá $C'(t)$ e indicá su unidad.

b) ¿En qué instante deja de crecer la concentración y cuál es el valor máximo? Justificá con el signo de $C'$.

c) Calculá e interpretá $C'(4)$.

d) Hallá la recta tangente a la gráfica de $C$ en $t = 0$.

e) **Con GeoGebra** (Clásico 6 o calculadora en línea): definí `C(t) = 20 t exp(-t/2)`, graficá `Derivada(C)` y trazá `Tangente(2, C)`. Verificá que la tangente en $t = 2$ es horizontal y que `Derivada(C)` corta al eje $t$ en ese mismo valor. Luego hacé la resolución analítica.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Producto con una cadena en la exponencial; estudio del signo de $C'$; interpretación con unidades.

**Desarrollo.** a) $C'(t) = 20e^{-t/2} + 20t\cdot\left(-\tfrac12\right)e^{-t/2} = 10\,(2 - t)\,e^{-t/2}$, en mg/l por hora.

b) Como $e^{-t/2} > 0$, el signo de $C'$ es el de $2 - t$: $C' > 0$ si $0 \le t < 2$ (la concentración crece) y $C' < 0$ si $t > 2$ (decrece). Deja de crecer en $t = 2$ h, con $C(2) = 40e^{-1} = \dfrac{40}{e} \approx 14{,}7$ mg/l.

c) $C'(4) = 10\,(2 - 4)\,e^{-2} = -20e^{-2} \approx -2{,}71$ mg/l por hora: a las $4$ horas la concentración disminuye a razón de unos $2{,}7$ mg/l por cada hora.

d) $C(0) = 0$ y $C'(0) = 20$: la tangente es $y = 20t$.

e) En GeoGebra, `Tangente(2, C)` es la recta $y = C(2) = 40/e$, horizontal. `Derivada(C)` grafica $C'$, que cruza el eje en $t = 2$ y es positiva antes y negativa después, de acuerdo con b).

**Resultado.** a) $C'(t) = 10(2 - t)e^{-t/2}$ mg/l/h; b) máximo en $t = 2$ h, $C = \dfrac{40}{e}$; c) $C'(4) = -20e^{-2} \approx -2{,}71$ mg/l/h; d) $y = 20t$.

</details>

### Ejercicio 21 · Opción múltiple con datos de tangente
<!-- ejercicio: U3.21 | nivel: avanzado | tipo: opcion-multiple | verificacion: sympy -->

:::note[Enunciado]
Sea $g$ derivable y biyectiva en $\mathbb{R}$, con recta tangente $y = 3x - 1$ en $x = 2$. Sea $f$ derivable en $\mathbb{R}$ con $f(5) = -1$ y $f'(5) = 4$. Se define $h(x) = f\bigl(g(x)\bigr)\,x^2$.

a) El valor de $h'(2)$ es:

1. $44$
2. $48$
3. $12$
4. No se puede determinar con los datos.

b) Calculá $(g^{-1})'(5)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Extraer de la recta tangente los datos $g(2)$ y $g'(2)$ y aplicar producto, cadena e inversa.

**Desarrollo.** De $y = 3x - 1$ en $x = 2$: $g(2) = 5$ y $g'(2) = 3$. Entonces $f(g(2)) = f(5) = -1$ y $f'(g(2)) = f'(5) = 4$. Por el producto y la cadena,

$$
h'(x) = f'\bigl(g(x)\bigr)\,g'(x)\,x^2 + f\bigl(g(x)\bigr)\cdot 2x \implies h'(2) = 4\cdot 3\cdot 4 + (-1)\cdot 4 = 48 - 4 = 44.
$$

*Justificación de cada opción.*

1. **$44$: correcta**, es el cálculo anterior.
2. $48$ es **incorrecta**: es el primer sumando; se omitió el segundo término de la regla del producto, $f(g(2))\cdot 2\cdot 2 = -4$.
3. $12$ es **incorrecta**: es $f'(5)\,g'(2)$, la derivada de $f\circ g$ sola; se ignoró el factor $x^2$ y, con él, los dos términos de la regla del producto.
4. **Incorrecta**: los datos determinan $g(2)$, $g'(2)$, $f(5)$ y $f'(5)$, que son todos los valores que aparecen en $h'(2)$.

b) Una función continua e inyectiva en un intervalo es estrictamente monótona, así que $g$ cumple las hipótesis de la fórmula de la inversa. Como $g(2) = 5$, es $g^{-1}(5) = 2$, y $g'(2) = 3 \neq 0$, de modo que $(g^{-1})'(5) = \dfrac{1}{g'(2)} = \dfrac13$.

**Resultado.** a) la opción 1, $h'(2) = 44$; b) $(g^{-1})'(5) = \dfrac13$.

</details>

### Ejercicio 22 · Inversa, derivación logarítmica y tangentes
<!-- ejercicio: U3.22 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = x\,e^{x}$ definida para $x \ge -1$.

a) Probá que $f$ es estrictamente creciente en $[-1, +\infty)$ y, por lo tanto, inyectiva.

b) Calculá $(f^{-1})'(e)$ y escribí la recta tangente a la gráfica de $f^{-1}$ en $x = e$.

c) Sea $h(x) = \bigl(f(x)\bigr)^{x}$ para $x > 0$. Calculá $h'(x)$ por derivación logarítmica y la recta tangente a $h$ en $x = 1$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El signo de $f'$ da la monotonía; con $f(a) = e$ se aplica la fórmula de la inversa; en c) se toma $\ln h$.

**Desarrollo.** a) $f'(x) = e^x + x e^x = (1 + x)e^x$, que es positiva si $x > -1$. Luego $f$ es estrictamente creciente en $[-1, +\infty)$ (es continua y su derivada es positiva en el interior), así que es inyectiva y tiene inversa allí.

b) $f(1) = e$, luego $f^{-1}(e) = 1$ y $f'(1) = 2e \neq 0$. Entonces $(f^{-1})'(e) = \dfrac{1}{2e}$. La tangente a $f^{-1}$ en $(e, 1)$ es $y = 1 + \dfrac{1}{2e}(x - e)$.

c) Para $x > 0$ es $f(x) = x e^x > 0$ y $h(x) = (x e^x)^x$. Entonces $\ln h = x\ln(x e^x) = x(\ln x + x) = x\ln x + x^2$. Derivando, $\dfrac{h'}{h} = \ln x + 1 + 2x$, de modo que $h'(x) = (x e^x)^x\,(\ln x + 2x + 1)$. En $x = 1$: $h(1) = e$ y $h'(1) = e\,(0 + 2 + 1) = 3e$. La tangente es $y = e + 3e\,(x - 1)$.

**Resultado.** a) $f'(x) = (1 + x)e^x > 0$ en $(-1, +\infty)$; b) $(f^{-1})'(e) = \dfrac{1}{2e}$, tangente $y = 1 + \dfrac{x - e}{2e}$; c) $h'(x) = (xe^x)^x(\ln x + 2x + 1)$ y tangente $y = e + 3e(x - 1)$.

</details>
