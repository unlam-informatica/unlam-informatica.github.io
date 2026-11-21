---
title: Reglas de derivación
description: Derivadas de las funciones elementales deducidas de la definición, tabla de derivadas y reglas de la constante, la suma, el producto y el cociente con sus demostraciones.
slug: analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion
sidebar:
  order: 3
---

## Qué vas a aprender

- Deducir a partir de la definición la derivada de una potencia, del seno, de la exponencial y del logaritmo.
- Usar la tabla de derivadas elementales.
- Aplicar las reglas del producto por una constante, de la suma, del producto y del cociente, con sus hipótesis, y demostrar la del producto.

**Antes de empezar.** Tenés que dominar [la derivada como función](/analisis-matematico-i/unidad-3/teoria/derivada-como-funcion/) y los límites notables $\lim\limits_{h\to 0}\frac{\operatorname{sen} h}{h} = 1$ y $\lim\limits_{h\to 0}\frac{e^h - 1}{h} = 1$ de la Unidad 2 (el primero, en [infinitésimos](/analisis-matematico-i/unidad-2/teoria/infinitesimos/) y en [cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/); el segundo y el número $e$ como límite de $(1+u)^{1/u}$, en [cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/#límites-notables-y-el-número-e)).

## Introducción

Calcular una derivada con el límite del cociente incremental funciona, pero es lento y en cuanto la función se complica (un producto de tres factores, un cociente con raíces) se vuelve impracticable. La estrategia es conocida: **calcular con la definición unas pocas derivadas elementales y demostrar reglas que combinan derivadas**. Con eso se deriva cualquier expresión armada con esas piezas.

## Derivadas elementales a partir de la definición

### Constante y potencias

Si $f(x) = c$, el cociente incremental es $\frac{c - c}{h} = 0$ y $f'(x) = 0$.

Si $f(x) = x^n$ con $n$ natural, el binomio de Newton da $(x + h)^n = x^n + n x^{n-1} h + \binom{n}{2} x^{n-2} h^2 + \cdots + h^n$, de donde

$$
\dfrac{(x+h)^n - x^n}{h} = n x^{n-1} + \binom{n}{2} x^{n-2} h + \cdots + h^{n-1} \xrightarrow[h \to 0]{} n x^{n-1}.
$$

### Ejemplo 1 · Una potencia por definición
<!-- check: U3.T.REG.1 -->

Para $f(x) = x^4$:

$$
\dfrac{(x + h)^4 - x^4}{h} = \dfrac{4x^3 h + 6x^2 h^2 + 4x h^3 + h^4}{h} = 4x^3 + 6x^2 h + 4x h^2 + h^3 \xrightarrow[h \to 0]{} 4x^3.
$$

### Ejemplo 2 · La raíz cuadrada
<!-- check: U3.T.REG.2 -->

Para $x > 0$ y $f(x) = \sqrt{x}$ multiplicamos y dividimos por el conjugado:

$$
\dfrac{\sqrt{x + h} - \sqrt{x}}{h} = \dfrac{(x + h) - x}{h\,(\sqrt{x + h} + \sqrt{x})} = \dfrac{1}{\sqrt{x + h} + \sqrt{x}} \xrightarrow[h \to 0]{} \dfrac{1}{2\sqrt{x}}.
$$

Es el caso $n = \frac12$ de la fórmula $(x^\alpha)' = \alpha x^{\alpha - 1}$, que vale para todo exponente real $\alpha$ (en los puntos donde $x^\alpha$ está definida y es derivable); la justificaremos en [derivación logarítmica](/analisis-matematico-i/unidad-3/teoria/implicita-y-logaritmica/). Para exponentes enteros negativos alcanza con la regla del cociente más abajo: $x^{-n} = \frac{1}{x^n}$ da $-\frac{n x^{n-1}}{x^{2n}} = -n\,x^{-n-1}$.

### Seno y coseno

### Ejemplo 3 · Derivada del seno
<!-- check: U3.T.REG.3 -->

Con $\operatorname{sen}(x + h) = \operatorname{sen} x \cos h + \cos x \operatorname{sen} h$:

$$
\dfrac{\operatorname{sen}(x + h) - \operatorname{sen} x}{h} = \operatorname{sen} x \cdot \dfrac{\cos h - 1}{h} + \cos x \cdot \dfrac{\operatorname{sen} h}{h} \xrightarrow[h \to 0]{} \operatorname{sen} x \cdot 0 + \cos x \cdot 1 = \cos x.
$$

Se usó que $\lim\limits_{h \to 0}\frac{\operatorname{sen} h}{h} = 1$ y que $\frac{\cos h - 1}{h} = -\frac{\operatorname{sen}^2 h}{h\,(\cos h + 1)} = -\frac{\operatorname{sen} h}{h} \cdot \frac{\operatorname{sen} h}{\cos h + 1} \to -1 \cdot 0 = 0$. De manera análoga, con $\cos(x + h) = \cos x \cos h - \operatorname{sen} x \operatorname{sen} h$, resulta $(\cos x)' = -\operatorname{sen} x$.

### Exponencial y logaritmo

Para $e^x$: $\dfrac{e^{x+h} - e^x}{h} = e^x \cdot \dfrac{e^h - 1}{h} \to e^x \cdot 1$. Para $\ln x$ con $x > 0$:

$$
\dfrac{\ln(x + h) - \ln x}{h} = \dfrac{1}{h}\ln\!\left(1 + \dfrac{h}{x}\right) = \dfrac{1}{x} \ln\!\left(1 + \dfrac{h}{x}\right)^{x/h} \xrightarrow[h \to 0]{} \dfrac{1}{x} \ln e = \dfrac{1}{x},
$$

porque $\left(1 + \frac{h}{x}\right)^{x/h} \to e$ cuando $h \to 0$ y $\ln$ es continua.

## Tabla de derivadas elementales

| $f(x)$ | $f'(x)$ | Dónde vale |
|---|---|---|
| $c$ (constante) | $0$ | $\mathbb{R}$ |
| $x^{\alpha}$ | $\alpha\,x^{\alpha - 1}$ | $x > 0$ para cualquier $\alpha$ real; también en los puntos donde $x^\alpha$ y $x^{\alpha-1}$ están definidas (por ejemplo, $x \neq 0$ si $\alpha$ es entero negativo) |
| $e^{x}$ | $e^{x}$ | $\mathbb{R}$ |
| $a^{x}$ ($a > 0$) | $a^{x} \ln a$ | $\mathbb{R}$ |
| $\ln x$ | $\dfrac{1}{x}$ | $x > 0$ |
| $\log_a x$ | $\dfrac{1}{x \ln a}$ | $x > 0$ |
| $\operatorname{sen} x$ | $\cos x$ | $\mathbb{R}$ |
| $\cos x$ | $-\operatorname{sen} x$ | $\mathbb{R}$ |
| $\tan x$ | $\dfrac{1}{\cos^2 x} = \sec^2 x$ | $\cos x \neq 0$ |
| $\cot x$ | $-\dfrac{1}{\operatorname{sen}^2 x} = -\csc^2 x$ | $\operatorname{sen} x \neq 0$ |

Las derivadas de $a^x$ y $\log_a x$ salen de $e^x$ y $\ln x$ con la regla de la cadena, porque $a^x = e^{x \ln a}$ y $\log_a x = \frac{\ln x}{\ln a}$. Las de las funciones trigonométricas inversas se deducen en [la lección siguiente](/analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa/).

## Reglas de derivación

:::note[Teorema · Reglas de derivación]
Sean $f$ y $g$ **derivables en $a$** y $c$ una constante. Entonces:

- **Constante por función:** $(c\,f)'(a) = c\,f'(a)$.
- **Suma y diferencia:** $(f \pm g)'(a) = f'(a) \pm g'(a)$.
- **Producto:** $(f\,g)'(a) = f'(a)\,g(a) + f(a)\,g'(a)$.
- **Cociente:** si además $g(a) \neq 0$, $\left(\dfrac{f}{g}\right)'(a) = \dfrac{f'(a)\,g(a) - f(a)\,g'(a)}{g(a)^2}$.
:::

**Demostración (formal) de la suma y de la constante.** Para $(f + g)$: $\dfrac{(f + g)(a + h) - (f + g)(a)}{h} = \dfrac{f(a + h) - f(a)}{h} + \dfrac{g(a + h) - g(a)}{h}$, y el límite de la suma es la suma de los límites, que existen por hipótesis. La constante sale del límite igual que de cualquier límite. $\blacksquare$

**Demostración (formal) de la regla del producto.** Sumamos y restamos $f(a)\,g(a+h)$:

$$
\dfrac{f(a+h)\,g(a+h) - f(a)\,g(a)}{h} = \dfrac{f(a+h) - f(a)}{h}\,g(a+h) + f(a)\,\dfrac{g(a+h) - g(a)}{h}.
$$

Cuando $h \to 0$: el primer cociente tiende a $f'(a)$; $g(a + h) \to g(a)$ porque $g$ es derivable y, por lo tanto, [continua](/analisis-matematico-i/unidad-3/teoria/derivada-como-funcion/) en $a$; el último cociente tiende a $g'(a)$. El límite resulta $f'(a)\,g(a) + f(a)\,g'(a)$. $\blacksquare$

**Demostración (formal) de la regla del cociente.** Primero el recíproco. Como $g$ es continua en $a$ y $g(a) \neq 0$, $g(a + h) \neq 0$ para $h$ chico, y

$$
\dfrac{1}{h}\left(\dfrac{1}{g(a+h)} - \dfrac{1}{g(a)}\right) = -\dfrac{g(a+h) - g(a)}{h} \cdot \dfrac{1}{g(a+h)\,g(a)} \xrightarrow[h \to 0]{} -\dfrac{g'(a)}{g(a)^2}.
$$

Luego $\frac{f}{g} = f \cdot \frac{1}{g}$ y la regla del producto da $f' \cdot \frac{1}{g} + f \cdot \left(-\frac{g'}{g^2}\right) = \frac{f'g - fg'}{g^2}$. $\blacksquare$

:::caution[Cuidado]
La derivada de un producto **no** es el producto de las derivadas, ni la de un cociente el cociente de las derivadas. Un contraejemplo inmediato: $(x \cdot x)' = 2x$, pero $x' \cdot x' = 1$.
:::

Cada regla vale en los puntos donde las funciones involucradas son derivables; en un punto donde alguna no lo es, la regla no se puede usar y hay que volver a la definición.

### Ejemplo 4 · Suma y múltiplos con potencias
<!-- check: U3.T.REG.4 -->

Derivemos $f(x) = 4x^5 - 7\sqrt{x} + \dfrac{3}{x^2} + \pi$. Reescribimos con potencias: $f(x) = 4x^5 - 7x^{1/2} + 3x^{-2} + \pi$, con $x > 0$. Término a término:

$$
f'(x) = 20x^4 - \dfrac{7}{2}x^{-1/2} - 6x^{-3} + 0 = 20x^4 - \dfrac{7}{2\sqrt{x}} - \dfrac{6}{x^3}.
$$

La constante $\pi$ aporta $0$.

### Ejemplo 5 · Producto
<!-- check: U3.T.REG.5 -->

Para $f(x) = (3x^2 - x)\ln x$, con $x > 0$, tomamos $u = 3x^2 - x$ y $v = \ln x$, de modo que $u' = 6x - 1$ y $v' = \frac1x$:

$$
f'(x) = (6x - 1)\ln x + (3x^2 - x)\cdot\dfrac{1}{x} = (6x - 1)\ln x + 3x - 1.
$$

### Ejemplo 6 · Producto de tres factores
<!-- check: U3.T.REG.6 -->

Para $f(x) = x^2 e^x \operatorname{sen} x$ agrupamos: $f = (x^2 e^x)\cdot\operatorname{sen} x$. Primero $(x^2 e^x)' = 2x e^x + x^2 e^x$. Entonces

$$
f'(x) = (2x e^x + x^2 e^x)\operatorname{sen} x + x^2 e^x \cos x = x e^x\bigl[(x + 2)\operatorname{sen} x + x \cos x\bigr].
$$

### Ejemplo 7 · Cociente
<!-- check: U3.T.REG.7 -->

Para $f(x) = \dfrac{2x + 1}{x^2 + 4}$ (el denominador nunca se anula):

$$
f'(x) = \dfrac{2\,(x^2 + 4) - (2x + 1)\,2x}{(x^2 + 4)^2} = \dfrac{-2x^2 - 2x + 8}{(x^2 + 4)^2} = \dfrac{2\,(4 - x - x^2)}{(x^2 + 4)^2}.
$$

### Ejemplo 8 · Tangente y secante
<!-- check: U3.T.REG.8 -->

La tangente es $\tan x = \dfrac{\operatorname{sen} x}{\cos x}$, con $\cos x \neq 0$. Por la regla del cociente,

$$
(\tan x)' = \dfrac{\cos x \cdot \cos x - \operatorname{sen} x \cdot (-\operatorname{sen} x)}{\cos^2 x} = \dfrac{\cos^2 x + \operatorname{sen}^2 x}{\cos^2 x} = \dfrac{1}{\cos^2 x}.
$$

De igual modo, para $\sec x = \dfrac{1}{\cos x}$: $(\sec x)' = \dfrac{\operatorname{sen} x}{\cos^2 x} = \sec x \tan x$.

### Ejemplo 9 · Simplificar antes de derivar (y cuidar el dominio)
<!-- check: U3.T.REG.9 -->

Sea $f(x) = \dfrac{x^2 - 4}{x - 2}$, con $D_f = \mathbb{R} - \{2\}$. Si aplicamos la regla del cociente:

$$
f'(x) = \dfrac{2x\,(x - 2) - (x^2 - 4)\cdot 1}{(x - 2)^2} = \dfrac{x^2 - 4x + 4}{(x - 2)^2} = 1 \qquad (x \neq 2).
$$

Se llega al mismo resultado simplificando antes: $f(x) = x + 2$ para $x \neq 2$, cuya derivada es $1$. Pero la simplificación **no cambia el dominio**: $f'$ está definida solo para $x \neq 2$, porque $f$ ni siquiera está definida en $2$.

:::caution[Errores frecuentes]
- **$(fg)' = f'g'$** o **$(f/g)' = f'/g'$.** Son falsas; usá las reglas con los cuatro términos.
- **Signo en el cociente.** El numerador es $f'g - fg'$ (derivada del numerador por el denominador **menos** numerador por derivada del denominador); invertir el orden cambia el signo.
- **Derivar $a^x$ como una potencia.** $(2^x)' \neq x\,2^{x-1}$: la variable está en el exponente y la derivada es $2^x \ln 2$.
- **Derivar una constante como si dependiera de $x$.** $(\pi^5)' = 0$ y $(\ln 2)' = 0$.
- **No reescribir raíces y cocientes con potencias** antes de derivar términos como $\frac{3}{x^2}$ o $\sqrt[3]{x^2}$.
- **Simplificar sin cuidar el dominio**, como en el Ejemplo 9.
:::

## Ejercicios

### Ejercicio 8 · Derivadas de sumas con potencias
<!-- ejercicio: U3.08 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Derivá (indicá en cada caso dónde vale el resultado):

a) $f(x) = 6x^5 - 4x^3 + 2x - 9$.

b) $g(x) = 3\sqrt[3]{x} - \dfrac{5}{x^2} + 4e^x$.

c) $h(t) = 7\operatorname{sen} t - \dfrac{t^2}{2} + \ln t - \pi^2$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reescribir raíces y cocientes como potencias y derivar término a término con la tabla.

**Desarrollo.**

a) $f'(x) = 30x^4 - 12x^2 + 2$ para todo $x \in \mathbb{R}$.

b) $g(x) = 3x^{1/3} - 5x^{-2} + 4e^x$, para $x \neq 0$. Entonces $g'(x) = 3 \cdot \frac13 x^{-2/3} + 10x^{-3} + 4e^x = \dfrac{1}{\sqrt[3]{x^2}} + \dfrac{10}{x^3} + 4e^x$, para $x \neq 0$.

c) Para $t > 0$: $h'(t) = 7\cos t - t + \dfrac{1}{t}$; el término $\pi^2$ es constante.

**Resultado.** a) $30x^4 - 12x^2 + 2$; b) $\dfrac{1}{\sqrt[3]{x^2}} + \dfrac{10}{x^3} + 4e^x$; c) $7\cos t - t + \dfrac1t$.

</details>

### Ejercicio 9 · Producto y cociente
<!-- ejercicio: U3.09 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Derivá y simplificá:

a) $f(x) = (x^2 - 2x)\,e^x$. ¿En qué puntos tiene la gráfica tangente horizontal?

b) $g(x) = \dfrac{\operatorname{sen} x}{x^2 + 1}$.

c) $h(x) = x \tan x$ (indicá su dominio).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reconocer producto o cociente y aplicar la regla, simplificando al final.

**Desarrollo.**

a) $f'(x) = (2x - 2)e^x + (x^2 - 2x)e^x = (x^2 - 2)e^x$. Como $e^x > 0$, $f'(x) = 0 \iff x^2 = 2 \iff x = \pm\sqrt{2}$.

b) $g'(x) = \dfrac{\cos x\,(x^2 + 1) - \operatorname{sen} x \cdot 2x}{(x^2 + 1)^2}$.

c) $D_h = \{x \in \mathbb{R} : \cos x \neq 0\}$. $h'(x) = 1 \cdot \tan x + x\cdot\dfrac{1}{\cos^2 x} = \tan x + \dfrac{x}{\cos^2 x}$.

**Resultado.** a) $f'(x) = (x^2 - 2)e^x$, tangente horizontal en $x = \pm\sqrt{2}$, es decir, en $\left(\pm\sqrt2,\ (2 \mp 2\sqrt2)e^{\pm\sqrt2}\right)$; b) $g'(x) = \dfrac{(x^2 + 1)\cos x - 2x \operatorname{sen} x}{(x^2 + 1)^2}$; c) $h'(x) = \tan x + \dfrac{x}{\cos^2 x}$ en $\cos x \neq 0$.

</details>

### Ejercicio 10 · Una identidad para la derivada
<!-- ejercicio: U3.10 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = \dfrac{e^x - e^{-x}}{e^x + e^{-x}}$.

a) Probá que $f'(x) = 1 - \big(f(x)\big)^2$ y que $f'(x) = \dfrac{4}{(e^x + e^{-x})^2}$.

b) Deducí que $f$ es creciente en $\mathbb{R}$ y hallá la recta tangente en $x = 0$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Aplicar la regla del cociente con $u = e^x - e^{-x}$, $v = e^x + e^{-x}$ y notar que $u' = v$ y $v' = u$.

**Desarrollo.** a) $(e^{-x})' = -e^{-x}$, así que $u' = e^x + e^{-x} = v$ y $v' = e^x - e^{-x} = u$. Entonces

$$
f'(x) = \dfrac{u'v - uv'}{v^2} = \dfrac{v^2 - u^2}{v^2} = 1 - \left(\dfrac{u}{v}\right)^2 = 1 - f(x)^2.
$$

Además $v^2 - u^2 = (e^x + e^{-x})^2 - (e^x - e^{-x})^2 = 4e^x e^{-x} = 4$, luego $f'(x) = \dfrac{4}{v^2} = \dfrac{4}{(e^x + e^{-x})^2}$.

b) $f'(x) > 0$ para todo $x$ (cociente de positivos), por lo que $f$ es creciente (usamos que una función con derivada positiva en un intervalo es estrictamente creciente en él: es el criterio de monotonía, que se demuestra con el [teorema del valor medio](/analisis-matematico-i/unidad-4/teoria/termino-complementario/) y por ahora aceptamos). En $x = 0$: $f(0) = 0$ y $f'(0) = \dfrac{4}{(1 + 1)^2} = 1$, entonces la tangente es $y = x$.

**Resultado.** $f' = 1 - f^2 = \dfrac{4}{(e^x + e^{-x})^2} > 0$; tangente en $0$: $y = x$.

</details>

## Autoevaluación

**1. ¿Cuál es la derivada de $\pi^3$? ¿Y la de $x^3$?**

<details>
<summary>Respuesta</summary>

La primera es una constante: $0$. La segunda es $3x^2$.
</details>

**2. ¿Por qué en la demostración de la regla del producto se necesita que $g$ sea continua en $a$?**

<details>
<summary>Respuesta</summary>

Porque aparece $g(a + h)$ y hay que saber que tiende a $g(a)$; la continuidad la da el hecho de que $g$ es derivable en $a$.
</details>

**3. Derivá $\dfrac{1}{x}$ con la regla del cociente.**

<details>
<summary>Respuesta</summary>

$\dfrac{0\cdot x - 1\cdot 1}{x^2} = -\dfrac{1}{x^2}$.
</details>

**4. ¿Cuál es el error en «$(x e^x)' = 1 \cdot e^x$»?**

<details>
<summary>Respuesta</summary>

Se derivó como si fuera $(f g)' = f' g'$. Lo correcto es $1\cdot e^x + x e^x = (1 + x)e^x$.
</details>

:::tip[En resumen]
- Con la definición se deducen $(x^n)' = nx^{n-1}$, $(\operatorname{sen} x)' = \cos x$, $(e^x)' = e^x$, $(\ln x)' = \frac1x$; el resto de la tabla se obtiene con reglas.
- Suma y constante: la derivada es lineal. Producto: $(fg)' = f'g + fg'$. Cociente: $\left(\frac fg\right)' = \frac{f'g - fg'}{g^2}$, con $g(a) \neq 0$.
- El producto y el cociente se demuestran sumando y restando un término adecuado y usando que derivable implica continua.
- Antes de derivar, reescribí raíces y cocientes como potencias, y cuidá el dominio.
:::

**Para seguir.** Las reglas anteriores no alcanzan para $\operatorname{sen}(x^2)$ o $e^{3x}$: son funciones **compuestas**. [La regla de la cadena y la derivada de la inversa](/analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa/) resuelven ese caso.
