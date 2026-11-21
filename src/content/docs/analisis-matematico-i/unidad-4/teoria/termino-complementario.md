---
title: Término complementario
description: El resto de Lagrange, cómo acotar el error de una aproximación de Taylor en un intervalo y cómo elegir el orden necesario para una precisión dada.
slug: analisis-matematico-i/unidad-4/teoria/termino-complementario
sidebar:
  order: 3
---

## Qué vas a aprender

- Definir el término complementario (resto) $R_n(x) = f(x) - P_n(x)$ y enunciar el teorema de Lagrange con sus hipótesis.
- Acotar el error de una aproximación en un intervalo, explicitando dónde está el punto intermedio $c$.
- Elegir el orden $n$ para obtener una precisión dada.
- Deducir el signo del error de la aproximación lineal.

**Antes de empezar.** Esta lección usa el [polinomio de Taylor](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/) y su [orden de contacto](/analisis-matematico-i/unidad-4/teoria/orden-de-contacto/), el teorema de Rolle en su forma más simple (si $F$ es continua en $[a, b]$, derivable en $(a, b)$ y $F(a) = F(b)$, hay un punto intermedio con $F' = 0$; la materia lo toma como resultado conocido y no lo demuestra, y aquí se usa una sola vez, en la demostración opcional) y el cálculo de máximos de una función en un intervalo con su derivada.

## Introducción: ¿cuánto nos equivocamos?

Aproximar $\sqrt[3]{8{,}3}$ por $2{,}0246875$ sirve si sabemos cuántas cifras confiar. La calculadora no nos dice nada acerca del error, y una aproximación sin error conocido es poco confiable. Necesitamos una **garantía**: un número que el error no pueda superar, calculado sin conocer el valor exacto.

:::note[Definición · Término complementario]
El **término complementario** (o **resto**) del polinomio de Taylor de orden $n$ de $f$ en $a$ es la diferencia entre la función y su aproximación:

$$
R_n(x) = f(x) - P_n(x).
$$

El **error absoluto** de la aproximación en $x$ es $\lvert R_n(x) \rvert$.
:::

Por definición, $f(x) = P_n(x) + R_n(x)$: el valor exacto es la aproximación más el resto. El resto no se puede calcular sin conocer $f(x)$, pero se puede **acotar**.

## El teorema de Lagrange

:::note[Teorema · Fórmula de Lagrange para el resto]
**Hipótesis.** $f$ tiene derivadas hasta el orden $n + 1$ en un intervalo abierto $I$ que contiene a $a$ y a $x$.

**Tesis.** Existe un número $c$ **estrictamente entre $a$ y $x$** tal que

$$
R_n(x) = \dfrac{f^{(n+1)}(c)}{(n + 1)!}\,(x - a)^{n+1}.
$$
:::

Dicho con palabras: el resto tiene la forma del siguiente término del polinomio, pero con la derivada $(n+1)$-ésima evaluada en un punto $c$ desconocido entre $a$ y $x$, y no en $a$. Cuando $x < a$ vale lo mismo, con $c \in (x, a)$.

**Sobre las hipótesis.** Se necesita que $f^{(n+1)}$ exista *en todo el intervalo* entre $a$ y $x$, no solo en $a$: si falla en algún punto intermedio, el teorema no se aplica. Ejemplo: para $f(x) = \ln x$ con $a = 1$ y $x = -0{,}5$ no hay teorema, porque $\ln$ no está definida en $x \le 0$. Para $f(x) = \sqrt[3]{x}$ con $a = -1$ y $x = 1$ falla ya la primera derivada en el $0$ que está en medio.

**Casos particulares.** Con $n = 0$: $f(x) - f(a) = f'(c)(x - a)$, que es el teorema del valor medio. Con $n = 1$: $f(x) = f(a) + f'(a)(x - a) + \frac{f''(c)}{2}(x - a)^2$, es decir, el error de la aproximación lineal.

### Demostración (formal, opcional)

Fijemos $x \neq a$ y sea $K$ el número definido por

$$
f(x) = P_n(x) + K\,\dfrac{(x - a)^{n+1}}{(n + 1)!}, \qquad \text{es decir,} \qquad K\,\dfrac{(x - a)^{n+1}}{(n + 1)!} = R_n(x).
$$

Queremos probar que $K = f^{(n+1)}(c)$ para algún $c$ entre $a$ y $x$. Para $t$ en el intervalo con extremos $a$ y $x$ consideramos la función auxiliar

$$
F(t) = f(x) - \sum_{k=0}^{n} \dfrac{f^{(k)}(t)}{k!}(x - t)^k - K\,\dfrac{(x - t)^{n+1}}{(n + 1)!}.
$$

1. **$F(x) = 0$.** En $t = x$ todos los términos con $(x - t)^k$, $k \ge 1$, se anulan y el de $k = 0$ vale $f(x)$, de modo que $F(x) = f(x) - f(x) - 0 = 0$.
2. **$F(a) = 0$.** En $t = a$, $F(a) = f(x) - P_n(x) - K\frac{(x - a)^{n+1}}{(n+1)!} = 0$ por la definición de $K$.
3. **$F$ es continua en el intervalo cerrado y derivable en el abierto**: aparecen $f, f', \dots, f^{(n)}$, continuas porque $f^{(n+1)}$ existe.

Falta calcular $F'$.

<!-- check: U4.T.RES.1 -->
**Derivada de $F$.** Derivando cada término del sumatorio se obtiene $\frac{d}{dt}\left[\frac{f^{(k)}(t)}{k!}(x - t)^k\right] = \frac{f^{(k+1)}(t)}{k!}(x - t)^k - \frac{f^{(k)}(t)}{(k - 1)!}(x - t)^{k-1}$ para $k \ge 1$, y $f'(t)$ para $k = 0$. Al sumar de $k = 0$ a $n$, los términos se cancelan de a pares y queda solo el último:

$$
\dfrac{d}{dt}\sum_{k=0}^{n} \dfrac{f^{(k)}(t)}{k!}(x - t)^k = \dfrac{f^{(n+1)}(t)}{n!}(x - t)^n.
$$

Como $\frac{d}{dt}\left[K\frac{(x - t)^{n+1}}{(n+1)!}\right] = -K\frac{(x - t)^n}{n!}$, resulta

$$
F'(t) = \dfrac{(x - t)^n}{n!}\,\bigl(K - f^{(n+1)}(t)\bigr).
$$

**Conclusión (Rolle).** Como $F(a) = F(x) = 0$, existe $c$ **entre $a$ y $x$** con $F'(c) = 0$. Como $(x - c)^n \neq 0$, debe ser $K = f^{(n+1)}(c)$, y entonces $R_n(x) = K\frac{(x - a)^{n+1}}{(n+1)!} = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$. $\blacksquare$

## Cómo acotar el error

La fórmula de Lagrange contiene a $c$, que no conocemos. Pero sí sabemos que está en el intervalo entre $a$ y $x$, y eso alcanza.

:::note[Propiedad · Cota del error]
Con las hipótesis del teorema, si $M$ es un número tal que $\lvert f^{(n+1)}(t) \rvert \le M$ para **todo $t$ entre $a$ y $x$** (incluidos los extremos), entonces

$$
\lvert R_n(x) \rvert \le \dfrac{M}{(n + 1)!}\,\lvert x - a \rvert^{n+1}.
$$
:::

**Por qué funciona.** Como $c$ está entre $a$ y $x$, $\lvert f^{(n+1)}(c) \rvert \le M$, y se reemplaza en el valor absoluto de la fórmula de Lagrange.

### Procedimiento

1. Identificá $f$, el centro $a$, el orden $n$ y el punto $x$ donde se aproxima.
2. Escribí el intervalo $[\,\min(a, x),\ \max(a, x)\,]$ y **decí dónde está $c$**: $c \in (a, x)$ o $c \in (x, a)$.
3. Calculá $f^{(n+1)}$ y hallá una cota $M$ de su valor absoluto en ese intervalo. Si $f^{(n+1)}$ es monótona, el máximo de $\lvert f^{(n+1)} \rvert$ está en un extremo; si no, buscá los puntos críticos o acotá con desigualdades sencillas.
4. Reemplazá en $\frac{M}{(n+1)!}\lvert x - a \rvert^{n+1}$.

No hace falta que $M$ sea el máximo exacto: cualquier cota sirve, y una cota simple y segura suele ser mejor que una cota exacta difícil de justificar.

### Ejemplo 1 · Error de $e^{0{,}3}$ con orden $3$
<!-- check: U4.T.RES.2 -->

Aproximamos $e^{0{,}3}$ con el Mac Laurin de orden $3$ de $f(x) = e^x$: $P_3(x) = 1 + x + \frac{x^2}{2} + \frac{x^3}{6}$, de modo que

$$
P_3(0{,}3) = 1 + 0{,}3 + 0{,}045 + 0{,}0045 = 1{,}3495.
$$

Cota del error. $f^{(4)}(t) = e^t$ y $c \in (0;\ 0{,}3)$. Como $e^t$ es creciente, $e^c < e^{0{,}3}$. Una cota simple: $e^{0{,}3} < 2$, porque equivale a $e^3 < 2^{10} = 1024$ y se cumple ($e < 3$, luego $e^3 < 27$). Con $M = 2$:

$$
\lvert R_3(0{,}3) \rvert \le \dfrac{2}{4!}\,(0{,}3)^4 = \dfrac{2}{24} \cdot 0{,}0081 = 0{,}000675.
$$

Entonces $e^{0{,}3} = 1{,}3495 \pm 0{,}000675$: garantizamos que el valor está entre $1{,}348825$ y $1{,}350175$. El error real es $0{,}00036$, menor que la cota, como debe ser.

### Ejemplo 2 · Error de $\ln 1{,}2$
<!-- check: U4.T.RES.4 -->

Con $f(x) = \ln x$, $a = 1$, $n = 3$ y $x = 1{,}2$: $P_3(x) = (x - 1) - \frac{(x - 1)^2}{2} + \frac{(x - 1)^3}{3}$ y

$$
P_3(1{,}2) = 0{,}2 - 0{,}02 + \dfrac{0{,}008}{3} = \dfrac{137}{750} \approx 0{,}182667.
$$

Para el error, $f^{(4)}(t) = -\dfrac{6}{t^4}$, con $c \in (1;\ 1{,}2)$. En el intervalo $[1;\ 1{,}2]$ la función $\frac{6}{t^4}$ decrece, de modo que su máximo está en $t = 1$ y vale $M = 6$:

$$
\lvert R_3(1{,}2) \rvert \le \dfrac{6}{4!}(0{,}2)^4 = \dfrac14 \cdot 0{,}0016 = 0{,}0004.
$$

El valor real es $\ln 1{,}2 = 0{,}1823216\ldots$ y el error real es $0{,}000345$.

### Ejemplo 3 · Cuando $x$ está a la izquierda de $a$
<!-- check: U4.T.RES.5 -->

Aproximemos $\sqrt{0{,}9}$ con $f(x) = \sqrt{x}$, $a = 1$ y $n = 2$: $P_2(x) = 1 + \frac{x - 1}{2} - \frac{(x - 1)^2}{8}$, de modo que

$$
P_2(0{,}9) = 1 - 0{,}05 - 0{,}00125 = 0{,}94875 = \dfrac{759}{800}.
$$

Ahora $x = 0{,}9 < a = 1$ y $c \in (0{,}9;\ 1)$. La derivada tercera es $f'''(t) = \frac38 t^{-5/2}$, **decreciente**, así que su máximo en $[0{,}9;\ 1]$ está en el extremo **izquierdo**: $t = 0{,}9$. Para acotarlo sin calculadora: $0{,}9^{-5/2} \le \frac43$, porque equivale a $\left(\frac{10}{9}\right)^5 \le \frac{16}{9}$, y en efecto $\frac{100000}{59049} \approx 1{,}694 < 1{,}778$. Entonces $M = \frac38 \cdot \frac43 = \frac12$ y

$$
\lvert R_2(0{,}9) \rvert \le \dfrac{1/2}{3!}\,(0{,}1)^3 = \dfrac{1}{12000} \approx 0{,}0000833.
$$

El error real ($\sqrt{0{,}9} = 0{,}9486833\ldots$) es de $0{,}0000667$.

## Elegir el orden para una precisión dada

Si queremos que el error sea menor que $\varepsilon$, buscamos el **menor $n$** para el cual la cota de Lagrange sea menor que $\varepsilon$.

![Gráfico del error absoluto de la exponencial con polinomios de Mac Laurin de orden 1, 2 y 3](/analisis-matematico-i/figuras/u4-error-taylor.svg)

*El error de $e^x$ crece al alejarse de $0$ y baja mucho al subir el orden: el comportamiento cerca del origen es como $\lvert x \rvert^{n+1}$ (una curva más plana cuanto mayor es $n$).*

### Ejemplo 4 · ¿Qué orden necesito para $\operatorname{sen} 0{,}5$?
<!-- check: U4.T.RES.3 -->

Queremos un error menor que $10^{-4}$ al aproximar $\operatorname{sen}(0{,}5)$ con el Mac Laurin de $\operatorname{sen}$. Todas las derivadas de $\operatorname{sen}$ cumplen $\lvert f^{(n+1)}(t) \rvert \le 1$, de modo que $M = 1$ para cualquier $n$, y la cota es $\frac{(1/2)^{n+1}}{(n + 1)!}$:

| $n$ | cota $\dfrac{(1/2)^{n+1}}{(n+1)!}$ | ¿menor que $10^{-4}$? |
|---|---|---|
| $3$ | $\dfrac{1}{384} \approx 2{,}6 \cdot 10^{-3}$ | no |
| $4$ | $\dfrac{1}{3840} \approx 2{,}6 \cdot 10^{-4}$ | no |
| $5$ | $\dfrac{1}{46080} \approx 2{,}2 \cdot 10^{-5}$ | **sí** |

El menor orden es $n = 5$: $P_5(0{,}5) = 0{,}5 - \frac{1}{48} + \frac{1}{3840} = \frac{1841}{3840} \approx 0{,}47943$. Fijate que $P_3 = P_4$ (el coeficiente de $x^4$ es $0$), pero la cota con $n = 4$ ($2{,}6 \cdot 10^{-4}$) es **mejor** que con $n = 3$ ($2{,}6 \cdot 10^{-3}$): al ver a $P_3$ como polinomio de orden $4$ usamos la derivada quinta y una potencia mayor de $\lvert x - a \rvert$.

### Ejemplo 5 · Cuánto se equivoca $\operatorname{sen} x \approx x$
<!-- check: U4.T.RES.6 -->

Para $\lvert x \rvert \le 0{,}1$, $P_1(x) = x$ y $P_1 = P_2$. Con $n = 1$ y $M = 1$: $\lvert R_1(x) \rvert \le \frac{1}{2}x^2 \le \frac{1}{200} = 0{,}005$. Pero con $n = 2$ ($f''' = -\cos$, $M = 1$): $\lvert R_2(x) \rvert \le \frac{1}{6}\lvert x \rvert^3 \le \frac{1}{6000} \approx 1{,}7 \cdot 10^{-4}$. La segunda cota es treinta veces mejor: el mismo polinomio, mejor análisis.

## Consecuencias

### Signo del error de la aproximación lineal

Con $n = 1$, $R_1(x) = \frac{f''(c)}{2}(x - a)^2$ y $(x - a)^2 \ge 0$: **el signo de $R_1$ es el de $f''(c)$**. Si $f'' > 0$ en el intervalo, $f(x) - L(x) > 0$ y la tangente **subestima**; si $f'' < 0$, la tangente **sobreestima**. Es lo que observamos con $\sqrt[4]{16{,}2}$ en la lección anterior.

### El error es de orden superior a $(x - a)^n$

Si $\lvert f^{(n+1)} \rvert \le M$ en un entorno de $a$, entonces $\left\lvert \frac{R_n(x)}{(x - a)^n} \right\rvert \le \frac{M}{(n+1)!}\lvert x - a \rvert \to 0$. Es decir, el resto es un infinitésimo de orden superior a $(x - a)^n$: precisa el significado de «el polinomio de orden $n$ aproxima bien cerca de $a$» y enlaza con el [orden de contacto](/analisis-matematico-i/unidad-4/teoria/orden-de-contacto/).

### Ejemplo 6 · Límites del resto
<!-- check: U4.T.RES.7 -->

Para $f(x) = e^x$ y $n = 2$: $\lim\limits_{x \to 0} \dfrac{e^x - 1 - x - \frac{x^2}{2}}{x^2} = 0$. Para $f(x) = \operatorname{sen} x$ y $n = 3$: $\lim\limits_{x \to 0} \dfrac{\operatorname{sen} x - x + \frac{x^3}{6}}{x^3} = 0$. En ambos, los límites laterales coinciden.

**Una advertencia.** La cota de Lagrange habla de **un** $x$ y **un** $n$ a la vez. No dice que el error tienda a $0$ al aumentar $n$ para todo $x$: para algunas funciones (por ejemplo, $\frac{1}{1 + x^2}$ en $x = 2$) el error de los polinomios de Mac Laurin crece con $n$.

:::caution[Errores frecuentes]
- **Evaluar $f^{(n+1)}$ en $a$ y no en $c$.** El resto no es $\frac{f^{(n+1)}(a)}{(n+1)!}(x - a)^{n+1}$; el punto $c$ es intermedio y desconocido.
- **Usar la derivada de orden $n$ en lugar de la de orden $n + 1$.** Para $P_n$, el resto lleva $f^{(n+1)}$ y $\lvert x - a \rvert^{n+1}$.
- **Tomar $M$ en un solo extremo sin justificar.** Hay que ver que $\lvert f^{(n+1)} \rvert$ es máxima ahí (por monotonía o puntos críticos) en **todo** el intervalo entre $a$ y $x$.
- **Olvidar el intervalo** o no decir dónde está $c$: es parte de la respuesta.
- **Confundir cota con error.** $\frac{M}{(n+1)!}\lvert x - a \rvert^{n+1}$ es una garantía, no el error real, que suele ser menor.
- **Aplicar el teorema fuera de las hipótesis**, por ejemplo con una derivada que no existe en un punto intermedio.
:::

## Ejercicios

### Ejercicio 10 · Aproximar y acotar $\ln 0{,}9$
<!-- ejercicio: U4.10 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Aproximá $\ln 0{,}9$ con el polinomio de Mac Laurin de orden $3$ de $f(x) = \ln(1 + x)$ y acotá el error con el resto de Lagrange. Indicá en qué intervalo está $c$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $\ln 0{,}9 = f(-0{,}1)$. Con $x = -0{,}1 < a = 0$, el intervalo es $[-0{,}1;\ 0]$.

**Desarrollo.** $P_3(x) = x - \frac{x^2}{2} + \frac{x^3}{3}$, de modo que

$$
P_3(-0{,}1) = -0{,}1 - 0{,}005 - \dfrac{0{,}001}{3} = -\dfrac{79}{750} \approx -0{,}105333.
$$

Para el resto: $f^{(4)}(t) = -\dfrac{6}{(1 + t)^4}$ y $c \in (-0{,}1;\ 0)$. En $[-0{,}1;\ 0]$, $\frac{6}{(1 + t)^4}$ crece cuando $t$ decrece (el denominador es menor), así que su máximo está en $t = -0{,}1$: $M = \frac{6}{0{,}9^4} = 6\left(\frac{10}{9}\right)^4$. Entonces

$$
\lvert R_3(-0{,}1) \rvert \le \dfrac{M}{4!}(0{,}1)^4 = \dfrac{6 \cdot 10^4}{9^4 \cdot 24} \cdot 10^{-4} = \dfrac{1}{4 \cdot 6561} = \dfrac{1}{26244} \approx 3{,}8 \cdot 10^{-5}.
$$

El valor real $\ln 0{,}9 = -0{,}1053605\ldots$ dista $2{,}7 \cdot 10^{-5}$ de $P_3(-0{,}1)$, dentro de la cota.

**Resultado.** $\ln 0{,}9 \approx -\frac{79}{750} \approx -0{,}10533$, con $c \in (-0{,}1;\ 0)$ y $\lvert R_3(-0{,}1) \rvert \le \frac{1}{26244} \approx 3{,}8 \cdot 10^{-5}$.

</details>

### Ejercicio 11 · Elegir el orden
<!-- ejercicio: U4.11 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Se quiere aproximar $e^{-1/2}$ con un polinomio de Mac Laurin de $e^x$ con error menor que $10^{-3}$.

a) Hallá el menor orden $n$ que lo garantiza con la fórmula de Lagrange, indicando dónde está $c$ y qué $M$ usás.

b) Calculá la aproximación como fracción.

c) ¿El polinomio de orden $3$ habría bastado en la práctica, aunque la cota no lo garantice? Comprobalo con el valor real.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con $f^{(n+1)}(t) = e^t$ y $c \in \left(-\frac12;\ 0\right)$, buscar el menor $n$ con $\frac{M}{(n+1)!}\left(\frac12\right)^{n+1} < 10^{-3}$.

**Desarrollo.** a) En $\left[-\frac12;\ 0\right]$ la exponencial es creciente y $e^t \le e^0 = 1$: $M = 1$ para cualquier $n$. La cota es $\frac{(1/2)^{n+1}}{(n+1)!}$: para $n = 3$ vale $\frac{1}{16 \cdot 24} = \frac{1}{384} \approx 2{,}6 \cdot 10^{-3} > 10^{-3}$; para $n = 4$ vale $\frac{1}{32 \cdot 120} = \frac{1}{3840} \approx 2{,}6 \cdot 10^{-4} < 10^{-3}$. El menor orden que garantiza la precisión es $n = 4$.

b) $P_4\left(-\frac12\right) = 1 - \frac12 + \frac18 - \frac{1}{48} + \frac{1}{384} = \frac{384 - 192 + 48 - 8 + 1}{384} = \frac{233}{384} \approx 0{,}606771$.

c) Con orden $3$: $P_3\left(-\frac12\right) = 1 - \frac12 + \frac18 - \frac1{48} = \frac{29}{48} \approx 0{,}604167$, mientras que $e^{-1/2} = 0{,}606531\ldots$: el error real es $0{,}00236 > 10^{-3}$. Entonces el orden $3$ **no** alcanzaba tampoco en la práctica. (Con $n = 4$ el error real es $2{,}4 \cdot 10^{-4}$, dentro de la cota $\frac{1}{3840}$.)

**Resultado.** a) $n = 4$; b) $e^{-1/2} \approx \frac{233}{384} \approx 0{,}6068$; c) no, el error del orden $3$ es $0{,}0024$.

</details>

### Ejercicio 12 · Cuánto vale el error de $\cos x \approx 1 - \frac{x^2}{2}$
<!-- ejercicio: U4.12 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Se aproxima $\cos x$ por $1 - \frac{x^2}{2}$ cerca del origen.

a) Acotá el error para $\lvert x \rvert \le 0{,}2$ eligiendo el orden que da la mejor cota (pista: ese polinomio es el de orden $2$ y también el de orden $3$).

b) Probá que para $\lvert x \rvert \le 0{,}22$ el error es menor que $10^{-4}$, y mostrá que con esa misma cota el valor $\lvert x \rvert \le 0{,}23$ ya no queda garantizado.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Como $P_2 = P_3$, usamos $n = 3$ y la derivada cuarta, $f^{(4)}(t) = \cos t$, con $\lvert \cos t \rvert \le 1$.

**Desarrollo.** a) Con $n = 3$ y $M = 1$: $\lvert R_3(x) \rvert \le \frac{1}{4!}\lvert x \rvert^4 = \frac{x^4}{24}$. Para $\lvert x \rvert \le 0{,}2$: $\frac{0{,}2^4}{24} = \frac{0{,}0016}{24} = \frac{1}{15000} \approx 6{,}7 \cdot 10^{-5}$. (Con $n = 2$ obtendríamos $\frac{\lvert x \rvert^3}{6} \le \frac{0{,}008}{6} \approx 1{,}3 \cdot 10^{-3}$, una cota veinte veces peor.)

b) Para $\lvert x \rvert \le 0{,}22$: $\frac{0{,}22^4}{24} = \frac{0{,}00234256}{24} \approx 9{,}76 \cdot 10^{-5} < 10^{-4}$. Con $\lvert x \rvert = 0{,}23$ la cota es $\frac{0{,}23^4}{24} = \frac{0{,}00279841}{24} \approx 1{,}17 \cdot 10^{-4} > 10^{-4}$: la garantía se pierde. (El valor exacto que separa los casos es $\lvert x \rvert = \sqrt[4]{0{,}0024} \approx 0{,}2213$.)

**Resultado.** a) $\lvert R_3(x) \rvert \le \frac{1}{15000}$ para $\lvert x \rvert \le 0{,}2$; b) para $\lvert x \rvert \le 0{,}22$ el error es menor que $10^{-4}$; con $0{,}23$ la cota ya lo supera.

</details>

### Ejercicio 13 · Cotas por ambos lados con el signo del resto
<!-- ejercicio: U4.13 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $f(x) = \sqrt{1 + x}$ y $x \ge 0$.

a) Con la fórmula de Lagrange, demostrá que $1 + \dfrac{x}{2} - \dfrac{x^2}{8} \le \sqrt{1 + x} \le 1 + \dfrac{x}{2}$.

b) Demostrá además que $\sqrt{1 + x} \le 1 + \dfrac{x}{2} - \dfrac{x^2}{8} + \dfrac{x^3}{16}$.

c) Usá a) y b) con $x = 0{,}44$ para encerrar $\sqrt{1{,}44}$ y compará con el valor exacto.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Mirar el **signo** del resto, no solo su tamaño: el signo de $R_n$ es el de $f^{(n+1)}(c)$ cuando $x > a$.

**Desarrollo.** Con $a = 0$: $f'(t) = \frac12(1 + t)^{-1/2}$, $f''(t) = -\frac14(1 + t)^{-3/2}$, $f'''(t) = \frac38(1 + t)^{-5/2}$. Las derivadas existen en $(-1, +\infty) \supset [0, x]$, de modo que se cumplen las hipótesis.

a) *Cota superior.* $P_1(x) = 1 + \frac{x}{2}$ y $R_1(x) = \frac{f''(c)}{2}x^2$ con $c \in (0, x)$ y $f''(c) < 0$: entonces $R_1(x) \le 0$ y $\sqrt{1 + x} = P_1(x) + R_1(x) \le 1 + \frac{x}{2}$. *Cota inferior.* $P_2(x) = 1 + \frac{x}{2} - \frac{x^2}{8}$ y $R_2(x) = \frac{f'''(c)}{6}x^3$ con $f'''(c) > 0$ y $x^3 \ge 0$: $R_2(x) \ge 0$, luego $\sqrt{1 + x} \ge P_2(x)$.

b) $R_2(x) = \frac{f'''(c)}{6}x^3 = \frac{1}{16}(1 + c)^{-5/2}x^3$ con $c \in (0, x)$. Como $(1 + c)^{-5/2} \le 1$ para $c \ge 0$, resulta $R_2(x) \le \frac{x^3}{16}$, o sea $\sqrt{1 + x} \le P_2(x) + \frac{x^3}{16}$.

c) Con $x = 0{,}44$: $P_2 = 1 + 0{,}22 - 0{,}0242 = 1{,}1958$; $P_2 + \frac{x^3}{16} = 1{,}1958 + \frac{0{,}085184}{16} = 1{,}1958 + 0{,}005324 = 1{,}201124$; $1 + \frac{x}{2} = 1{,}22$. Entonces $1{,}1958 \le \sqrt{1{,}44} \le 1{,}201124$ (la cota de b) es mejor que la de a)), y el valor exacto es $\sqrt{1{,}44} = 1{,}2$.

**Resultado.** a) y b) demostrados por el signo y el tamaño de $f''(c)$ y $f'''(c)$; c) $1{,}1958 \le 1{,}2 \le 1{,}2011\ldots$

</details>

## Autoevaluación

**1. En la fórmula de Lagrange, ¿dónde se evalúa la derivada $(n+1)$-ésima y qué se sabe de ese punto?**

<details>
<summary>Respuesta</summary>

En un punto $c$ desconocido, estrictamente entre $a$ y $x$. Solo se sabe en qué intervalo está.
</details>

**2. Si $\lvert f^{(4)} \rvert \le 12$ en $[1;\ 1{,}5]$, ¿qué cota se obtiene para $\lvert R_3(1{,}5) \rvert$ con $a = 1$?**

<details>
<summary>Respuesta</summary>

$\frac{12}{4!}(0{,}5)^4 = \frac12 \cdot 0{,}0625 = 0{,}03125$.
</details>

**3. Con $n = 1$, si $f'' < 0$ en el intervalo, ¿la aproximación lineal sobreestima o subestima?**

<details>
<summary>Respuesta</summary>

Sobreestima: $R_1 = f - L = \frac{f''(c)}{2}(x - a)^2 \le 0$, o sea $f \le L$.
</details>

**4. ¿Puede aplicarse el teorema de Lagrange para $f(x) = \lvert x \rvert$, $a = -1$, $x = 1$, $n = 1$?**

<details>
<summary>Respuesta</summary>

No: $f$ no es derivable en $x = 0$, que está en el intervalo entre $a$ y $x$.
</details>

:::tip[En resumen]
- $R_n(x) = f(x) - P_n(x)$ y, bajo las hipótesis (derivadas hasta orden $n + 1$ en un intervalo que contiene a $a$ y a $x$), $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$ con $c$ entre $a$ y $x$.
- Cota del error: $\lvert R_n(x) \rvert \le \frac{M}{(n+1)!}\lvert x - a \rvert^{n+1}$, con $M$ una cota de $\lvert f^{(n+1)} \rvert$ en el intervalo entre $a$ y $x$. Siempre se explicita ese intervalo.
- Para una precisión $\varepsilon$ se busca el menor $n$ con la cota menor que $\varepsilon$.
- El signo de $R_1$ es el de $f''(c)$: la tangente subestima si $f'' > 0$ y sobreestima si $f'' < 0$.
:::

**Para seguir.** Con esta lección cerramos la unidad: tenés las herramientas para construir polinomios, aproximar y garantizar la precisión. Para integrar todo en problemas de estilo parcial, pasá a los [integradores de la Unidad 4](/analisis-matematico-i/unidad-4/practica/integradores/), o volvé a [la guía de práctica](/analisis-matematico-i/unidad-4/practica/practica-4/).
