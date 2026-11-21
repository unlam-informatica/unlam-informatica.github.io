---
title: Integradores — Unidad 1
description: Ejercicios integradores de estilo parcial de la Unidad 1 (Funciones), con resolución completa.
slug: analisis-matematico-i/unidad-1/practica/integradores
sidebar:
  order: 90
  label: Integradores
---

Cuatro ejercicios que combinan los temas de la unidad, como en un parcial: dominio, ceros y signo, transformaciones, composición, inversa y modelos. Intentalos primero sin mirar la resolución. Teoría de apoyo: [funciones y modelos](/analisis-matematico-i/unidad-1/teoria/funciones-y-modelos/), [características](/analisis-matematico-i/unidad-1/teoria/caracteristicas/), [funciones elementales](/analisis-matematico-i/unidad-1/teoria/funciones-elementales/), [álgebra y transformaciones](/analisis-matematico-i/unidad-1/teoria/algebra-y-transformaciones/) e [inversa](/analisis-matematico-i/unidad-1/teoria/inversa/).

### Ejercicio 22 · Estudio completo de una logarítmica
<!-- ejercicio: U1.22 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \ln(x + 3) - 2$.
a) Hallar dominio, imagen, ceros, $C^{+}$, $C^{-}$ y la asíntota vertical.
b) Describir cómo se obtiene el gráfico de $f$ a partir del de $\ln x$.
c) Probar que $f$ es biyectiva de su dominio en su imagen y hallar $f^{-1}$ con su terna.
d) Sea $g(x) = x^2 - 1$. Hallar $f \circ g$, su dominio, y decidir si es par, impar o ninguna.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Usar la forma $a\,f(b(x-c)) + d$ con $\ln x$ como base, y las condiciones del logaritmo para el dominio.

**Desarrollo.** a) El argumento debe ser positivo: $x + 3 > 0 \iff x > -3$, así que $D_f = (-3, +\infty)$. El logaritmo toma todos los reales y el desplazamiento vertical no cambia eso: $\operatorname{Im} f = \mathbb{R}$. Ceros: $\ln(x + 3) = 2 \Rightarrow x + 3 = e^2 \Rightarrow x = e^2 - 3 \approx 4{,}39$, que está en el dominio. Como $\ln$ es creciente, $f < 0$ a la izquierda del cero y $f > 0$ a la derecha: $C^{+} = (e^2 - 3, +\infty)$, $C^{-} = (-3, e^2 - 3)$. La asíntota vertical es $x = -3$.

b) $\ln(x + 3)$ es $\ln x$ desplazado $3$ a la izquierda; restar $2$ lo baja $2$ unidades. La asíntota $x = 0$ pasa a $x = -3$.

c) $f$ es estrictamente creciente (logaritmo de base $e > 1$ compuesto con $x + 3$ creciente), luego inyectiva; su imagen es $\mathbb{R}$, que tomamos como codominio, y así es sobreyectiva. De $y = \ln(x + 3) - 2$: $\ln(x + 3) = y + 2$, $x = e^{y + 2} - 3$. Entonces

$$
f^{-1}\colon \mathbb{R} \to (-3, +\infty) \,/\, f^{-1}(x) = e^{x + 2} - 3.
$$

d) $(f \circ g)(x) = \ln(x^2 - 1 + 3) - 2 = \ln(x^2 + 2) - 2$. Hace falta $g(x) \in D_f$, es decir, $x^2 - 1 > -3 \iff x^2 > -2$, que vale para todo real: $D_{f \circ g} = \mathbb{R}$ (simétrico). Como $x^2 + 2$ no cambia al sustituir $x$ por $-x$, $(f \circ g)(-x) = (f \circ g)(x)$: es **par**.

**Resultado.** a) $D_f = (-3, +\infty)$, $\operatorname{Im} f = \mathbb{R}$, $C_0 = \{e^2 - 3\}$, $C^{+} = (e^2 - 3, +\infty)$, $C^{-} = (-3, e^2 - 3)$, AV $x = -3$; b) $3$ a la izquierda y $2$ hacia abajo; c) $f^{-1}(x) = e^{x+2} - 3$, $\mathbb{R} \to (-3, +\infty)$; d) $\ln(x^2 + 2) - 2$ con dominio $\mathbb{R}$, par.

</details>

### Ejercicio 23 · El café que se enfría
<!-- ejercicio: U1.23 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
La temperatura (en °C) de un café $t$ minutos después de servirlo es $T(t) = 20 + 60\cdot\left(\tfrac12\right)^{t/10}$, y se lo toma como máximo a los $60$ minutos.
a) Escribir la terna de $T$.
b) ¿Cuándo está a $50\,^\circ$C?
c) Calcular la razón de cambio media en $[0, 10]$ y en $[10, 20]$ e interpretarlas.
d) Hallar la inversa, con su terna, e interpretarla.
e) **Con GeoGebra:** graficar $T$, ubicar el punto con $T = 50$ y verificar los resultados de b) y c).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Modelo exponencial decreciente con asíntota $y = 20$ (la temperatura ambiente); la inversa se obtiene con $\log_2$.

**Desarrollo.** a) $T(0) = 20 + 60 = 80$ y $T(60) = 20 + \dfrac{60}{2^6} = 20 + \dfrac{15}{16} = \dfrac{335}{16} = 20{,}9375$. Como $T$ es estrictamente decreciente:

$$
T\colon [0, 60] \to \left[\tfrac{335}{16}, 80\right] \,/\, T(t) = 20 + 60\left(\tfrac12\right)^{t/10}.
$$

b) $20 + 60\cdot 2^{-t/10} = 50 \Rightarrow 2^{-t/10} = \tfrac12 \Rightarrow -\tfrac{t}{10} = -1 \Rightarrow t = 10$ minutos.

c) $T(10) = 50$ y $T(20) = 20 + 15 = 35$. Entonces $\dfrac{50 - 80}{10} = -3$ y $\dfrac{35 - 50}{10} = -1{,}5$ °C/min. El café se enfría más rápido al principio (la razón media tiene módulo mayor) y la razón se **reduce a la mitad** en cada intervalo de $10$ minutos: cambio no uniforme.

d) De $y = 20 + 60\cdot 2^{-t/10}$: $2^{-t/10} = \dfrac{y - 20}{60}$, $-\dfrac{t}{10} = \log_2\dfrac{y - 20}{60}$, así que

$$
t(T) = 10\log_2\frac{60}{T - 20}, \qquad t\colon \left[\tfrac{335}{16}, 80\right] \to [0, 60].
$$

Da el tiempo que tarda el café en llegar a una temperatura $T$ dada. Por ejemplo $t(50) = 10\log_2 2 = 10$.

e) En GeoGebra Clásico 6 (o la calculadora en línea): `T(x) = Función(20 + 60 * 0.5^(x / 10), 0, 60)`; `Interseca(T, y = 50)` devuelve $(10, 50)$; `Pendiente(Recta((0, 80), (10, 50)))` devuelve $-3$ y `Pendiente(Recta((10, 50), (20, 35)))` devuelve $-1{,}5$. Hay que ver que el gráfico decrece, se achata hacia $y = 20$ y que las dos secantes tienen pendientes distintas.

**Resultado.** a) la terna anterior; b) $10$ min; c) $-3$ y $-1{,}5$ °C/min; d) $t(T) = 10\log_2\frac{60}{T - 20}$; e) coincide con lo calculado.

</details>

### Ejercicio 24 · Opción múltiple: inversa y dominio
<!-- ejercicio: U1.24 | nivel: avanzado | tipo: opcion-multiple | verificacion: sympy -->

:::note[Enunciado]
Sea $f\colon \mathbb{R} \setminus \{-2\} \to \mathbb{R} \setminus \{1\}$, $f(x) = \dfrac{x - 1}{x + 2}$.

**Parte 1.** Indicar la opción correcta sobre su inversa.
a) $f^{-1}(x) = \dfrac{x + 2}{x - 1}$, con dominio $\mathbb{R} \setminus \{1\}$.
b) $f^{-1}(x) = \dfrac{2x + 1}{1 - x}$, de $\mathbb{R} \setminus \{1\}$ en $\mathbb{R} \setminus \{-2\}$.
c) $f^{-1}(x) = \dfrac{2x + 1}{1 - x}$, de $\mathbb{R}$ en $\mathbb{R}$.
d) $f$ no tiene inversa porque tiene una asíntota vertical.

**Parte 2.** El dominio natural de $h(x) = \dfrac{\ln(x - 1)}{\sqrt{5 - x}}$ es: a) $(1, 5]$; b) $(1, 5)$; c) $(-\infty, 5)$; d) $[1, 5)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Despejar $x$ en $y = f(x)$ y contrastar cada opción con el dominio; en la parte 2, una condición por operación.

**Desarrollo.** *Parte 1.* $y(x + 2) = x - 1 \Rightarrow xy + 2y = x - 1 \Rightarrow x(y - 1) = -1 - 2y \Rightarrow x = \dfrac{2y + 1}{1 - y}$. El valor $y = 1$ no se alcanza (la asíntota horizontal), y $\operatorname{Im} f = \mathbb{R} \setminus \{1\}$ es el dominio de $f^{-1}$.
- a) **Incorrecta:** es $\frac{1}{f(x)}$, el recíproco, no la inversa. Por ejemplo $f(0) = -\frac12$ pero esa fórmula en $-\frac12$ da $\frac{3/2}{-3/2} = -1 \ne 0$.
- b) **Correcta:** fórmula y terna coinciden con el cálculo.
- c) **Incorrecta:** la fórmula es la correcta, pero en $x = 1$ se anula el denominador: el dominio no puede ser $\mathbb{R}$.
- d) **Incorrecta:** una asíntota vertical no impide la biyectividad: $f$ es inyectiva y sobreyectiva sobre $\mathbb{R} \setminus \{1\}$.

*Parte 2.* $\ln(x - 1)$ exige $x > 1$; la raíz en el denominador exige $5 - x > 0$, o sea $x < 5$ (estricto: si $x = 5$ se anula el denominador). Intersección: $(1, 5)$.
- a) incorrecta, incluye $5$; c) incorrecta, incluye valores $\le 1$; d) incorrecta, incluye $1$ ($\ln 0$ no existe).

**Resultado.** Parte 1: **b)**. Parte 2: **b)**.

</details>

### Ejercicio 25 · Valor absoluto de una cuadrática
<!-- ejercicio: U1.25 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \lvert x^2 - 2x - 3 \rvert$.
a) Escribirla por tramos y hallar dominio, imagen, ceros y $C^{+}$.
b) Decidir si es par, impar o ninguna.
c) ¿Cuántas soluciones tiene $f(x) = k$ según el valor de $k$?
d) **Con GeoGebra:** graficar $f$ y la recta $y = k$ con un deslizador, y comprobar c).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El valor absoluto refleja hacia arriba la parte negativa de $q(x) = x^2 - 2x - 3 = (x - 3)(x + 1)$; estudiar $q$ y luego reflejar.

**Desarrollo.** a) $q \ge 0$ si $x \le -1$ o $x \ge 3$, y $q < 0$ en $(-1, 3)$. Entonces
$$
f(x) = \begin{cases} x^2 - 2x - 3 & \text{si } x \le -1 \text{ o } x \ge 3, \\ -x^2 + 2x + 3 & \text{si } -1 < x < 3. \end{cases}
$$
Dominio $\mathbb{R}$. Ceros: $-1$ y $3$. $f \ge 0$ siempre, así que $C^{+} = \mathbb{R} \setminus \{-1, 3\}$. El vértice de $q$ es $(1, -4)$, que al reflejarse pasa a $(1, 4)$: un máximo local. Como en los extremos $f \to +\infty$ y $f$ es continua, la imagen es $[0, +\infty)$.

b) El dominio es simétrico, pero $f(1) = 4$ y $f(-1) = 0$: $f(-1) \ne f(1)$ y $f(-1) \ne -f(1)$. **Ninguna.**

c) Con $k < 0$: ninguna. Con $k = 0$: $2$ ($x = -1$, $x = 3$). Con $0 < k < 4$: la recta corta las dos ramas externas (una en cada lado) y el arco central en dos puntos: $4$. Con $k = 4$: toca el máximo local en $x = 1$ y corta las ramas externas: $3$. Con $k > 4$: solo las ramas externas: $2$. Por ejemplo, $k = 1$: $x^2 - 2x - 3 = \pm 1$ da $x = 1 \pm \sqrt5$ y $x = 1 \pm \sqrt3$ (cuatro valores).

d) En GeoGebra: `f(x) = abs(x^2 - 2x - 3)`, `k = Deslizador(-1, 6, 0.1)`, `y = k`, y `Interseca(f, y = k)`. Moviendo $k$ se ve $0$ puntos hasta $k = 0$, luego $2$, $4$, $3$ en $k = 4$ y de nuevo $2$.

**Resultado.** a) la función por tramos anterior, $D_f = \mathbb{R}$, $\operatorname{Im} f = [0, +\infty)$, $C_0 = \{-1, 3\}$, $C^{+} = \mathbb{R} \setminus \{-1, 3\}$; b) ninguna; c) $0$ si $k < 0$; $2$ si $k = 0$; $4$ si $0 < k < 4$; $3$ si $k = 4$; $2$ si $k > 4$.

</details>
