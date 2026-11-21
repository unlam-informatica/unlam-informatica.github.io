---
title: Derivación implícita y logarítmica
description: Derivada de funciones definidas por una ecuación F(x, y) = 0, tangentes horizontales y verticales, y derivación logarítmica de potencias f(x)^g(x) y de productos o cocientes extensos.
slug: analisis-matematico-i/unidad-3/teoria/implicita-y-logaritmica
sidebar:
  order: 5
---

## Qué vas a aprender

- Derivar implícitamente una ecuación en $x$ e $y$, hallar la recta tangente y la normal en un punto de la curva y reconocer los puntos de tangente horizontal y vertical.
- Derivar funciones de la forma $f(x)^{g(x)}$ y productos o cocientes extensos con derivación logarítmica, indicando dónde valen las fórmulas.

**Antes de empezar.** Necesitás dominar [la regla de la cadena](/analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa/) y [las reglas de derivación](/analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion/).

## Introducción: funciones que no se pueden despejar

La circunferencia $x^2 + y^2 = 25$ no es el gráfico de una función: a casi cada $x$ le corresponden dos valores de $y$. Y la ecuación $x^3 + xy + y^3 = 11$ ni siquiera se puede despejar con álgebra elemental. Sin embargo, cerca de un punto de la curva, $y$ **se comporta como una función de $x$**, y tiene sentido preguntar por la pendiente de la tangente en ese punto. La derivación implícita permite calcularla sin despejar $y$.

Por otro lado, la expresión $x^{\operatorname{sen} x}$ no es una potencia (el exponente no es constante) ni una exponencial (la base no es constante): las reglas de la tabla no la cubren. La derivación logarítmica la resuelve y también simplifica productos y cocientes largos.

## Derivación implícita

Sea $F(x, y) = 0$ una ecuación y $(x_0, y_0)$ un punto de la curva. Supongamos que cerca de $x_0$ existe una función derivable $y = y(x)$ con $F(x, y(x)) = 0$ y $y(x_0) = y_0$. (Que exista se garantiza con el *teorema de la función implícita*, que no demostramos; en la práctica, si el procedimiento da una expresión finita para $y'$ en el punto, el cálculo es válido allí.)

:::note[Procedimiento · Derivación implícita]
1. Derivar **ambos miembros** de la ecuación respecto de $x$, recordando que $y$ depende de $x$: cada vez que aparece una expresión con $y$ se aplica la regla de la cadena, por ejemplo $\dfrac{d}{dx}\,y^3 = 3y^2\,y'$ y $\dfrac{d}{dx}\,(xy) = y + x\,y'$.
2. Agrupar los términos con $y'$ en un miembro y los demás en el otro.
3. Despejar $y'$. El resultado suele depender de $x$ **e** $y$.
4. Evaluar en el punto $(x_0, y_0)$ (que debe satisfacer la ecuación).
:::

### Ejemplo 1 · La circunferencia
<!-- check: U3.T.IMP.1 -->

Para $x^2 + y^2 = 25$ derivamos: $2x + 2y\,y' = 0$, de donde $y' = -\dfrac{x}{y}$ si $y \neq 0$. En el punto $(3, 4)$, que cumple la ecuación ($9 + 16 = 25$), $y' = -\frac34$ y la tangente es

$$
y = 4 - \dfrac{3}{4}(x - 3).
$$

En $(3, -4)$ la pendiente es $+\frac34$, consistente con la simetría de la curva. En $(\pm 5, 0)$ el denominador $y$ se anula y la tangente es vertical.

### Ejemplo 2 · Una ecuación que no se despeja
<!-- check: U3.T.IMP.2 -->

La curva $x^3 + xy + y^3 = 11$ pasa por $(1, 2)$, porque $1 + 2 + 8 = 11$. Derivando:

$$
3x^2 + y + x\,y' + 3y^2\,y' = 0 \implies y'\,(x + 3y^2) = -(3x^2 + y) \implies y' = -\dfrac{3x^2 + y}{x + 3y^2}.
$$

En $(1, 2)$: $y' = -\dfrac{3 + 2}{1 + 12} = -\dfrac{5}{13}$. La tangente es $y = 2 - \dfrac{5}{13}(x - 1)$ y la normal, $y = 2 + \dfrac{13}{5}(x - 1)$.

## Tangentes horizontales y verticales

Al despejar se obtiene un cociente $y' = \dfrac{N(x, y)}{D(x, y)}$. Entonces:

- **Tangente horizontal** donde $N = 0$ y $D \neq 0$.
- **Tangente vertical** donde $D = 0$ y $N \neq 0$.
- Si $N = D = 0$ la fórmula no informa (es una forma $\frac00$); el punto requiere un estudio aparte.

En ambos casos el punto debe estar **sobre la curva**: se resuelve el sistema formado por la condición ($N = 0$ o $D = 0$) y la ecuación original.

### Ejemplo 3 · Una elipse inclinada
<!-- check: U3.T.IMP.3 -->

Para $x^2 + xy + y^2 = 3$: $2x + y + x\,y' + 2y\,y' = 0$, entonces $y' = -\dfrac{2x + y}{x + 2y}$.

*Horizontales.* $2x + y = 0 \Rightarrow y = -2x$. En la ecuación: $x^2 - 2x^2 + 4x^2 = 3x^2 = 3$, entonces $x = \pm 1$. Puntos $(1, -2)$ y $(-1, 2)$; allí $x + 2y = -3$ y $3$, no nulo.

*Verticales.* $x + 2y = 0 \Rightarrow x = -2y$: $4y^2 - 2y^2 + y^2 = 3y^2 = 3$, entonces $y = \pm 1$. Puntos $(-2, 1)$ y $(2, -1)$; allí $2x + y = -3$ y $3$, no nulo.

![Curva x² + xy + y² = 3 con las tangentes horizontales en y = ±2 y las verticales en x = ±2](/analisis-matematico-i/figuras/u3-implicita.svg)

*Los puntos rojos son los de tangente horizontal y los verdes, los de tangente vertical: la elipse queda inscrita en el cuadrado $\lvert x \rvert \le 2$, $\lvert y \rvert \le 2$.*

## Derivación logarítmica

Si $y = f(x)^{g(x)}$ con $f(x) > 0$ (condición para que la potencia con exponente real esté definida), se toma logaritmo natural:

$$
\ln y = g(x)\,\ln f(x).
$$

Como $f^g = e^{g \ln f}$ es una composición de funciones derivables, $y$ es derivable y podemos derivar ambos miembros respecto de $x$, con la cadena del lado izquierdo y el producto del derecho: $\dfrac{y'}{y} = g'(x)\ln f(x) + g(x)\dfrac{f'(x)}{f(x)}$.

:::note[Propiedad · Derivada de $f(x)^{g(x)}$]
Si $f$ y $g$ son derivables y $f(x) > 0$,

$$
\bigl(f^{g}\bigr)' = f^{g}\left(g'\,\ln f + g\,\dfrac{f'}{f}\right).
$$
:::

Es la suma de dos términos conocidos: si $g$ fuera constante quedaría la regla de la potencia ($g\,f^{g-1}f'$) y si $f$ fuera constante, la de la exponencial ($f^g\ln f\;g'$).

Para productos y cocientes con muchos factores, el logaritmo convierte productos en sumas y cocientes en restas. Cuando alguno de los factores puede ser negativo se usa $\ln\lvert y\rvert$: como $(\ln\lvert y\rvert)' = \dfrac{y'}{y}$ siempre que $y \neq 0$, la fórmula $y' = y\,(\ln\lvert y\rvert)'$ vale en todos los puntos donde $y$ es derivable y no nula.

### Ejemplo 4 · Una potencia con exponente variable
<!-- check: U3.T.LOG.1 -->

Para $y = x^{\operatorname{sen} x}$, con $x > 0$: $\ln y = \operatorname{sen} x \ln x$, y derivando

$$
\dfrac{y'}{y} = \cos x \ln x + \dfrac{\operatorname{sen} x}{x} \implies y' = x^{\operatorname{sen} x}\left(\cos x \ln x + \dfrac{\operatorname{sen} x}{x}\right).
$$

### Ejemplo 5 · La regla de la potencia para cualquier exponente
<!-- check: U3.T.LOG.2 -->

Para $y = x^{\alpha}$ con $x > 0$ y $\alpha$ real: $\ln y = \alpha \ln x$, $\dfrac{y'}{y} = \dfrac{\alpha}{x}$ y

$$
y' = x^{\alpha}\cdot\dfrac{\alpha}{x} = \alpha\,x^{\alpha - 1}.
$$

Esto justifica la fila $(x^{\alpha})' = \alpha x^{\alpha - 1}$ de la tabla de derivadas para exponentes reales cualesquiera.

### Ejemplo 6 · Un producto y cociente largo
<!-- check: U3.T.LOG.3 -->

Sea $f(x) = \dfrac{(x^2 + 1)^3\sqrt{x - 2}}{(x + 5)^4}$, definida para $x \ge 2$ (y derivable para $x > 2$). Con $x > 2$ todos los factores son positivos y

$$
\ln f = 3\ln(x^2 + 1) + \dfrac12\ln(x - 2) - 4\ln(x + 5).
$$

Derivando, $\dfrac{f'}{f} = \dfrac{6x}{x^2 + 1} + \dfrac{1}{2(x - 2)} - \dfrac{4}{x + 5}$, de modo que

$$
f'(x) = \dfrac{(x^2 + 1)^3\sqrt{x - 2}}{(x + 5)^4}\left(\dfrac{6x}{x^2 + 1} + \dfrac{1}{2(x - 2)} - \dfrac{4}{x + 5}\right).
$$

Con las reglas de producto y cociente se llega a lo mismo, pero con muchísimo más trabajo.

### Ejemplo 7 · Factores que pueden ser negativos
<!-- check: U3.T.LOG.4 -->

Sea $f(x) = \dfrac{(x - 1)^3(x + 2)}{(x - 3)^2}$, para $x \notin \{1, -2, 3\}$. En algunos intervalos $f < 0$, así que usamos $\ln\lvert f\rvert = 3\ln\lvert x - 1\rvert + \ln\lvert x + 2\rvert - 2\ln\lvert x - 3\rvert$ y $(\ln\lvert u\rvert)' = \frac{u'}{u}$:

$$
\dfrac{f'}{f} = \dfrac{3}{x - 1} + \dfrac{1}{x + 2} - \dfrac{2}{x - 3}.
$$

La fórmula $f' = f\left(\frac{3}{x-1} + \frac{1}{x+2} - \frac{2}{x-3}\right)$ es válida en todo el dominio, sea $f$ positiva o negativa.

:::caution[Errores frecuentes]
- **Olvidar $y'$ al derivar un término con $y$.** $(y^2)' = 2y\,y'$, no $2y$; $(xy)' = y + x\,y'$, no $y$.
- **Dejar $y'$ en ambos miembros** o no despejarlo antes de evaluar.
- **Evaluar en un punto que no está en la curva.** Siempre se verifica que $(x_0, y_0)$ satisface la ecuación; para tangente horizontal o vertical, además, el punto se halla *sobre la curva*.
- **Declarar tangente vertical cuando se anulan numerador y denominador a la vez.** Una forma $\frac00$ no informa. Por ejemplo, en $y^2 = x^3$ resulta $y' = \frac{3x^2}{2y}$, y en el origen se obtiene $\frac00$: ese punto es una cúspide, no una tangente vertical.
- **Derivar $x^x$ con la regla de la potencia** ($x\cdot x^{x-1}$) **o de la exponencial** ($x^x \ln x$): cada una cubre solo la mitad del resultado. La derivada es $x^x(\ln x + 1)$.
- **Tomar logaritmo de una cantidad negativa.** Usá $\ln\lvert y\rvert$, o restringí el dominio.
- **Olvidar multiplicar por $y$ al final**: $\frac{y'}{y}$ no es la derivada pedida.
:::

## Ejercicios

Con GeoGebra podés graficar una curva implícita escribiendo la ecuación en la línea de entrada (por ejemplo `x^2 + x y + y^2 = 3`) y trazar la tangente con `Tangente(A, c)`, siendo `A` un punto de la curva y `c` la curva; ver la guía de [GeoGebra para derivada](/analisis-matematico-i/geogebra/derivada/) (GeoGebra Clásico 6).

### Ejercicio 15 · Tangente y normal a una curva implícita
<!-- ejercicio: U3.15 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea la curva $2x^2 + 3y^2 = 14$.

a) Verificá que $P(1, 2)$ pertenece a la curva y hallá $y'$ por derivación implícita.

b) Escribí las ecuaciones de la tangente y de la normal en $P$.

c) Hallá otro punto de la curva donde la tangente sea paralela a la de $P$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Derivar ambos miembros respecto de $x$, despejar $y'$, evaluar en $P$, y para c) igualar $y'$ a la pendiente hallada y combinarla con la ecuación de la curva.

**Desarrollo.** a) $2\cdot 1 + 3\cdot 4 = 14$, entonces $P$ está en la curva. Derivando, $4x + 6y\,y' = 0$, de donde $y' = -\dfrac{2x}{3y}$ (con $y \neq 0$). En $P$: $y' = -\dfrac{2}{6} = -\dfrac13$.

b) Tangente: $y = 2 - \dfrac13(x - 1)$. Normal (pendiente $3$): $y = 2 + 3(x - 1)$.

c) $-\dfrac{2x}{3y} = -\dfrac13 \iff y = 2x$. En la curva: $2x^2 + 12x^2 = 14 \iff x^2 = 1$. Para $x = 1$ se obtiene $P$; para $x = -1$, $y = -2$.

**Resultado.** $y' = -\dfrac{2x}{3y}$; tangente $y = 2 - \dfrac{x - 1}{3}$; normal $y = 2 + 3(x - 1)$; otro punto $(-1, -2)$.

</details>

### Ejercicio 16 · Tangentes horizontales y verticales
<!-- ejercicio: U3.16 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallá todos los puntos de la curva $x^2 - 2xy + 2y^2 = 4$ donde la recta tangente es horizontal y todos aquellos donde es vertical.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Derivar implícitamente, igualar a cero numerador y denominador por separado y resolver cada caso junto con la ecuación de la curva.

**Desarrollo.** Derivando: $2x - 2y - 2x\,y' + 4y\,y' = 0 \Rightarrow y'\,(4y - 2x) = 2y - 2x \Rightarrow y' = \dfrac{y - x}{2y - x}$.

*Horizontal:* numerador nulo, $y = x$. En la curva: $x^2 - 2x^2 + 2x^2 = x^2 = 4$, entonces $x = \pm 2$: puntos $(2, 2)$ y $(-2, -2)$. En ellos el denominador vale $2y - x = x = \pm 2 \neq 0$.

*Vertical:* denominador nulo, $x = 2y$. En la curva: $4y^2 - 4y^2 + 2y^2 = 2y^2 = 4$, entonces $y = \pm\sqrt{2}$ y $x = \pm 2\sqrt{2}$: puntos $(2\sqrt2, \sqrt2)$ y $(-2\sqrt2, -\sqrt2)$. En ellos el numerador vale $y - x = -y = \mp\sqrt2 \neq 0$.

**Resultado.** Horizontales en $(2, 2)$ y $(-2, -2)$ (rectas $y = 2$ e $y = -2$); verticales en $(2\sqrt2, \sqrt2)$ y $(-2\sqrt2, -\sqrt2)$ (rectas $x = \pm 2\sqrt2$).

</details>

### Ejercicio 17 · Derivación logarítmica
<!-- ejercicio: U3.17 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Derivá, indicando el dominio donde vale el resultado:

a) $f(x) = (\ln x)^x$.

b) $g(x) = (2x + 1)^{\operatorname{sen} x}$.

c) Hallá la recta tangente a la gráfica de $h(x) = x^x$ en $x = 1$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Tomar logaritmo natural, derivar ambos miembros y multiplicar por la función original.

**Desarrollo.**

a) La base $\ln x$ debe ser positiva: $x > 1$. $\ln f = x\ln(\ln x)$, entonces $\dfrac{f'}{f} = \ln(\ln x) + x\cdot\dfrac{1}{x\ln x} = \ln(\ln x) + \dfrac{1}{\ln x}$ y $f'(x) = (\ln x)^x\left(\ln(\ln x) + \dfrac{1}{\ln x}\right)$ para $x > 1$.

b) La base debe ser positiva: $x > -\frac12$. $\ln g = \operatorname{sen} x\,\ln(2x + 1)$, entonces $\dfrac{g'}{g} = \cos x\,\ln(2x + 1) + \dfrac{2\operatorname{sen} x}{2x + 1}$ y $g'(x) = (2x + 1)^{\operatorname{sen} x}\left(\cos x\ln(2x + 1) + \dfrac{2\operatorname{sen} x}{2x + 1}\right)$ para $x > -\frac12$.

c) $h'(x) = x^x(\ln x + 1)$ para $x > 0$; $h(1) = 1$, $h'(1) = 1\cdot(0 + 1) = 1$. La tangente es $y = 1 + (x - 1) = x$.

**Resultado.** a) $(\ln x)^x\left(\ln\ln x + \dfrac{1}{\ln x}\right)$ en $x > 1$; b) $(2x+1)^{\operatorname{sen} x}\left(\cos x\ln(2x+1) + \dfrac{2\operatorname{sen} x}{2x+1}\right)$ en $x > -\frac12$; c) $y = x$.

</details>

### Ejercicio 18 · Derivación logarítmica de un producto y cociente
<!-- ejercicio: U3.18 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \dfrac{(x + 1)^2\,(x - 2)^3}{(x^2 + 1)^4}$.

a) Escribí $\dfrac{f'(x)}{f(x)}$ usando $\ln\lvert f\rvert$ y explicá por qué vale también donde $f$ es negativa.

b) Hallá la recta tangente a la gráfica de $f$ en $x = 0$.

c) Calculá $f'(-2)$ y decidí si $f$ crece o decrece en $x = -2$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Convertir el producto y el cociente en sumas con $\ln\lvert f\rvert$; derivar; despejar $f'$.

**Desarrollo.** a) Para $x \neq -1$ y $x \neq 2$: $\ln\lvert f\rvert = 2\ln\lvert x + 1\rvert + 3\ln\lvert x - 2\rvert - 4\ln(x^2 + 1)$, y como $(\ln\lvert u\rvert)' = \frac{u'}{u}$ para $u \neq 0$,

$$
\dfrac{f'}{f} = \dfrac{2}{x + 1} + \dfrac{3}{x - 2} - \dfrac{8x}{x^2 + 1}.
$$

Vale en cualquier punto donde $f \neq 0$, positiva o negativa, porque $(\ln\lvert f\rvert)'= \frac{f'}{f}$ no depende del signo de $f$.

b) $f(0) = \dfrac{1\cdot(-8)}{1} = -8$. En $x = 0$: $\dfrac{f'(0)}{f(0)} = 2 - \dfrac32 - 0 = \dfrac12$, de modo que $f'(0) = -8\cdot\dfrac12 = -4$. La tangente es $y = -8 - 4x$.

c) $f(-2) = \dfrac{(-1)^2\,(-4)^3}{5^4} = -\dfrac{64}{625}$. Además $\dfrac{f'(-2)}{f(-2)} = \dfrac{2}{-1} + \dfrac{3}{-4} - \dfrac{-16}{5} = -2 - \dfrac34 + \dfrac{16}{5} = \dfrac{9}{20}$. Entonces $f'(-2) = -\dfrac{64}{625}\cdot\dfrac{9}{20} = -\dfrac{144}{3125} < 0$: $f$ decrece en $x = -2$.

**Resultado.** a) $\dfrac{f'}{f} = \dfrac{2}{x+1} + \dfrac{3}{x-2} - \dfrac{8x}{x^2+1}$; b) $y = -4x - 8$; c) $f'(-2) = -\dfrac{144}{3125}$ (decreciente).

</details>

## Autoevaluación

**1. En $x^2 + y^2 = 25$, ¿por qué $y' = -\frac{x}{y}$ no sirve en $(5, 0)$?**

<details>
<summary>Respuesta</summary>

Porque el denominador se anula. En ese punto la tangente es vertical ($x = 5$) y $y$ no es función derivable de $x$ allí.
</details>

**2. ¿Cuál es la derivada de $xy$ respecto de $x$ cuando $y = y(x)$?**

<details>
<summary>Respuesta</summary>

$y + x\,y'$.
</details>

**3. ¿Para qué valores de $x$ está definida $x^{x}$ en este curso?**

<details>
<summary>Respuesta</summary>

Para $x > 0$ (la base debe ser positiva para tener exponente real cualquiera).
</details>

**4. ¿Por qué se usa $\ln\lvert y\rvert$ en lugar de $\ln y$ en productos y cocientes?**

<details>
<summary>Respuesta</summary>

Porque $y$ puede ser negativa; $\ln\lvert y\rvert$ está definida si $y \neq 0$ y tiene la misma derivada $\frac{y'}{y}$.
</details>

:::tip[En resumen]
- Derivación implícita: derivar los dos miembros respecto de $x$, aplicar la cadena a cada término con $y$, y despejar $y'$; evaluar en un punto **de la curva**.
- Tangente horizontal: numerador de $y'$ nulo y denominador no nulo; vertical: denominador nulo y numerador no nulo; $\frac00$ no informa.
- $\bigl(f^{g}\bigr)' = f^{g}\left(g'\ln f + g\frac{f'}{f}\right)$ para $f > 0$; incluye $(x^\alpha)' = \alpha x^{\alpha-1}$.
- En productos y cocientes largos, $\frac{f'}{f} = (\ln\lvert f\rvert)'$ convierte todo en sumas.
:::

**Para seguir.** Cerrás la unidad con los [ejercicios integradores](/analisis-matematico-i/unidad-3/practica/integradores/), y la [Unidad 4](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/) usa derivadas sucesivas para aproximar funciones.
