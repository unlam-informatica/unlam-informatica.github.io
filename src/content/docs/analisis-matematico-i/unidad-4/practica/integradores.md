---
title: Integradores — Unidad 4
description: Ejercicios integradores de estilo parcial sobre polinomios de Taylor y Mac Laurin, orden de contacto, aproximación lineal y acotación del error con el resto de Lagrange.
slug: analisis-matematico-i/unidad-4/practica/integradores
sidebar:
  order: 90
  label: Integradores
---

Estos ejercicios combinan los temas de la unidad con el formato de un parcial: desarrollo con justificación, un ítem de opción múltiple y un ejercicio que pide GeoGebra. Antes de empezar conviene haber leído las tres lecciones: [orden de contacto](/analisis-matematico-i/unidad-4/teoria/orden-de-contacto/), [polinomio de Taylor y de Mac Laurin](/analisis-matematico-i/unidad-4/teoria/polinomio-de-taylor/) y [término complementario](/analisis-matematico-i/unidad-4/teoria/termino-complementario/). Intentá resolverlos sin mirar la resolución y después comparalos paso a paso.

### Ejercicio 14 · Una función con exponencial: polinomio, valor, error y contacto
<!-- ejercicio: U4.14 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = x\,e^{-x}$.

a) Hallá el polinomio de Mac Laurin de orden $4$ de $f$.

b) Usalo para aproximar $f(0{,}2)$ y escribí el resultado como fracción.

c) Acotá el error de b) con el resto de Lagrange, indicando el intervalo donde está $c$ y justificando la cota $M$.

d) ¿Qué orden de contacto tienen en $x = 0$ la función $f$ y el polinomio $g(x) = x - x^2 + \frac{x^3}{2}$? ¿Y la función $f$ y el polinomio del ítem a)?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reconocer el patrón de las derivadas de $x\,e^{-x}$; con él se obtienen los coeficientes, el resto y el orden de contacto.

**Desarrollo.** a) Por la regla del producto: $f'(x) = (1 - x)e^{-x}$, $f''(x) = (x - 2)e^{-x}$, $f'''(x) = (3 - x)e^{-x}$, $f^{(4)}(x) = (x - 4)e^{-x}$ y $f^{(5)}(x) = (5 - x)e^{-x}$. En $0$ valen $f(0) = 0$, $f'(0) = 1$, $f''(0) = -2$, $f'''(0) = 3$, $f^{(4)}(0) = -4$ (y $f^{(5)}(0) = 5$). Los coeficientes $\frac{f^{(k)}(0)}{k!}$ son $0,\ 1,\ -1,\ \frac12,\ -\frac16$:

$$
P_4(x) = x - x^2 + \dfrac{x^3}{2} - \dfrac{x^4}{6}.
$$

b) $f(0{,}2) \approx P_4(0{,}2) = \dfrac15 - \dfrac{1}{25} + \dfrac{1}{250} - \dfrac{1}{3750} = \dfrac{750 - 150 + 15 - 1}{3750} = \dfrac{614}{3750} = \dfrac{307}{1875} \approx 0{,}163733$.

c) El resto es $R_4(0{,}2) = \frac{f^{(5)}(c)}{5!}(0{,}2)^5$ con $c \in (0;\ 0{,}2)$, y $f^{(5)}(t) = (5 - t)e^{-t}$, positiva en ese intervalo. Su derivada es $-(6 - t)e^{-t} < 0$, de modo que $f^{(5)}$ es decreciente en $[0;\ 0{,}2]$ y su máximo está en $t = 0$: $M = f^{(5)}(0) = 5$. Entonces

$$
\lvert R_4(0{,}2) \rvert \le \dfrac{5}{120}(0{,}2)^5 = \dfrac{5 \cdot 0{,}00032}{120} = \dfrac{1}{75000} \approx 1{,}33 \cdot 10^{-5}.
$$

El valor real es $f(0{,}2) = 0{,}2\,e^{-0{,}2} = 0{,}1637461\ldots$ y el error real, $1{,}28 \cdot 10^{-5}$, queda dentro de la cota.

d) $g$ es el polinomio de Mac Laurin de orden $3$ de $f$, así que $g^{(k)}(0) = f^{(k)}(0)$ para $k = 0, 1, 2, 3$. Pero $g^{(4)}(0) = 0 \neq -4 = f^{(4)}(0)$: contacto de orden $3$. Con $P_4$ las derivadas coinciden hasta $k = 4$, y $P_4^{(5)} = 0 \neq 5 = f^{(5)}(0)$: contacto de orden $4$.

**Resultado.** a) $P_4(x) = x - x^2 + \frac{x^3}{2} - \frac{x^4}{6}$; b) $f(0{,}2) \approx \frac{307}{1875}$; c) $c \in (0;\ 0{,}2)$, $M = 5$, $\lvert R_4(0{,}2) \rvert \le \frac{1}{75000}$; d) orden $3$ con $g$ y orden $4$ con $P_4$.

</details>

### Ejercicio 15 · $f(x) = x\cos x$ (con GeoGebra)
<!-- ejercicio: U4.15 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x) = x\cos x$.

a) Hallá el polinomio de Mac Laurin de orden $5$.

b) **Con GeoGebra** (Clásico 6 o calculadora en línea): definí `f(x) = x cos(x)`, graficá `PolinomioTaylor(f, 0, 3)` y `PolinomioTaylor(f, 0, 5)` y estimá visualmente en qué intervalo de $x$ se pegan a $f$. Luego definí `t(x) = PolinomioTaylor(f, 0, 5)` y evaluá `f(0.5) - t(0.5)`. (En la versión en inglés el comando es `TaylorPolynomial`.) Después hacé la resolución analítica.

c) Aproximá $f(0{,}5)$ con el polinomio del ítem a).

d) Acotá el error de c) de dos maneras: viéndolo como polinomio de orden $5$ y como polinomio de orden $6$. ¿Cuál cota es mejor y por qué?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Multiplicar el polinomio de $\cos x$ por $x$ y, para el error, escribir una fórmula de las derivadas de $f$ que permita acotarlas.

**Desarrollo.** a) $\cos x \approx 1 - \frac{x^2}{2} + \frac{x^4}{24}$, y $f(x) = x\cos x$; al multiplicar por $x$ se obtiene el polinomio de orden $5$:

$$
P_5(x) = x - \dfrac{x^3}{2} + \dfrac{x^5}{24}.
$$

Se puede confirmar con derivadas: $f'(0) = 1$, $f'''(0) = -3$ y $f^{(5)}(0) = 5$ dan los coeficientes $1,\ -\frac36 = -\frac12,\ \frac{5}{120} = \frac{1}{24}$, y las derivadas de orden par se anulan en $0$ ($f$ es impar).

b) En GeoGebra, ambas curvas se confunden con $f$ en un entorno del origen, y ese entorno es más grande para la de orden $5$ que para la de orden $3$. La diferencia pedida en $0{,}5$ es de unas $-1{,}1 \cdot 10^{-5}$ (negativa: $P_5$ queda apenas por encima de $f$ en ese punto). Tomá nota de lo que ves y comparalo con la resolución analítica de los ítems siguientes.

c) $P_5(0{,}5) = \dfrac12 - \dfrac{1}{16} + \dfrac{1}{768} = \dfrac{384 - 48 + 1}{768} = \dfrac{337}{768} \approx 0{,}438802$.

d) Para las derivadas (la fórmula se prueba por inducción con la regla del producto), $f^{(n)}(x) = x\cos\left(x + \frac{n\pi}{2}\right) + n\cos\left(x + \frac{(n-1)\pi}{2}\right)$. En particular $f^{(6)}(x) = -x\cos x - 6\operatorname{sen} x$ y $f^{(7)}(x) = x\operatorname{sen} x - 7\cos x$. En $[0;\ 0{,}5]$ ($c \in (0;\ 0{,}5)$):

- *Orden $5$.* $\lvert f^{(6)}(t) \rvert \le \lvert t \rvert + 6 \le 6{,}5$, así que $\lvert R_5(0{,}5) \rvert \le \dfrac{6{,}5}{6!}\left(\dfrac12\right)^6 = \dfrac{6{,}5}{46080} \approx 1{,}41 \cdot 10^{-4}$.
- *Orden $6$* (es el mismo polinomio, porque $f^{(6)}(0) = 0$). $\lvert f^{(7)}(t) \rvert \le \lvert t \rvert + 7 \le 7{,}5$, así que $\lvert R_6(0{,}5) \rvert \le \dfrac{7{,}5}{7!}\left(\dfrac12\right)^7 = \dfrac{7{,}5}{645120} \approx 1{,}16 \cdot 10^{-5}$.

La segunda cota es unas doce veces mejor: como $f^{(6)}(0) = 0$, el polinomio de orden $5$ es también el de orden $6$, y usar $n = 6$ aprovecha una potencia más de $\lvert x \rvert$ y un factorial más grande. El error real ($f(0{,}5) = 0{,}4387912\ldots$) es de $1{,}08 \cdot 10^{-5}$, consistente con ambas cotas.

**Resultado.** a) $P_5(x) = x - \frac{x^3}{2} + \frac{x^5}{24}$; c) $f(0{,}5) \approx \frac{337}{768}$; d) $\lvert R_5 \rvert \le 1{,}41 \cdot 10^{-4}$ y, con $n = 6$, $\lvert R_6 \rvert \le 1{,}16 \cdot 10^{-5}$ (mejor).

</details>

### Ejercicio 16 · Opción múltiple con un polinomio dado
<!-- ejercicio: U4.16 | nivel: avanzado | tipo: opcion-multiple | verificacion: sympy -->

:::note[Enunciado]
El polinomio de Taylor de orden $3$ de una función $f$ en $a = 1$ es $P_3(x) = 3 - 2(x - 1) + 6(x - 1)^2 - 4(x - 1)^3$.

a) El valor de $f'''(1)$ es:

1. $-4$
2. $-24$
3. $-12$
4. $-\frac23$

b) La recta tangente a la gráfica de $f$ en $x = 1$ es:

1. $y = 3 - 2(x - 1)$
2. $y = 3 + 6(x - 1)$
3. $y = 3 - 2x$
4. $y = 3 - 2(x - 1) + 6(x - 1)^2$

c) Si se sabe que $\lvert f^{(4)}(t) \rvert \le 10$ para todo $t \in [1;\ 1{,}2]$, una cota del error al aproximar $f(1{,}2)$ con $P_3(1{,}2)$ es:

1. $\dfrac{10}{4!}\,(0{,}2)^4$
2. $\dfrac{10}{3!}\,(0{,}2)^3$
3. $10\,(0{,}2)^4$
4. $\dfrac{10}{4!}\,(0{,}2)^3$

d) La aproximación $f(1{,}2) \approx P_3(1{,}2)$ vale:

1. $2{,}6$
2. $2{,}84$
3. $2{,}808$
4. $2{,}872$
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada ítem es una lectura directa de la definición: el coeficiente de $(x - 1)^k$ es $\frac{f^{(k)}(1)}{k!}$, la tangente es $P_1$, el resto de Lagrange usa $f^{(n+1)}$ con $n = 3$ y $\lvert x - a \rvert = 0{,}2$.

**Desarrollo.** a) **Correcta: la 2.** El coeficiente de $(x - 1)^3$ es $-4 = \frac{f'''(1)}{3!}$, así que $f'''(1) = -4 \cdot 6 = -24$. La 1 olvida el factorial (confunde el coeficiente con la derivada); la 3 multiplica por $3$ en lugar de por $3! = 6$; la 4 divide por $3!$ en lugar de multiplicar.

b) **Correcta: la 1.** La recta tangente es $P_1(x) = f(1) + f'(1)(x - 1) = 3 - 2(x - 1)$ (con $f(1) = 3$ y $f'(1) = -2$). La 2 usa el coeficiente del término cuadrático como pendiente; la 3 escribe $-2x$ en lugar de $-2(x - 1)$, que no pasa por $(1, 3)$ (da $y = 1$ en $x = 1$); la 4 es una parábola, que es $P_2$, no una recta.

c) **Correcta: la 1.** Para $P_3$ el resto es $R_3$, con la derivada **cuarta**, $4! = 24$ y $\lvert x - a \rvert^{4} = (0{,}2)^4$: $\frac{M}{4!}\lvert x - a \rvert^{4}$ con $M = 10$. La 2 usa $n = 2$ (derivada tercera, $3!$ y exponente $3$); la 3 omite el factorial; la 4 mezcla el factorial $4!$ con el exponente $3$. El valor de la opción 1 es $\frac{10}{24} \cdot 0{,}0016 = \frac{1}{1500} \approx 6{,}7 \cdot 10^{-4}$.

d) **Correcta: la 3.** $P_3(1{,}2) = 3 - 2(0{,}2) + 6(0{,}04) - 4(0{,}008) = 3 - 0{,}4 + 0{,}24 - 0{,}032 = 2{,}808$. La 1 es solo la recta tangente ($3 - 0{,}4$); la 2 es $P_2$ (sin el término cúbico); la 4 suma el término cúbico en lugar de restarlo.

**Resultado.** a) opción 2; b) opción 1; c) opción 1; d) opción 3. Con ello, $f(1{,}2) = 2{,}808 \pm \frac{1}{1500}$.

</details>

### Ejercicio 17 · Presión atmosférica: modelo lineal y su error
<!-- ejercicio: U4.17 | nivel: avanzado | tipo: modelado | verificacion: sympy -->

:::note[Enunciado]
En un modelo simple, la presión del aire a una altura $h$ (en metros sobre un punto de referencia) es $p(h) = 100\,e^{-h/8000}$ kPa.

a) Hallá la linealización de $p$ en $h = 0$ y usala para estimar $p(400)$.

b) Acotá el error de esa estimación con el resto de Lagrange. ¿La estimación queda por debajo o por encima del valor del modelo? Justificá con $p''$.

c) ¿Hasta qué altura $h \in [0;\ H]$ garantiza la aproximación lineal un error menor que $0{,}05$ kPa? Dá un valor entero de $H$ que sirva, justificándolo.

d) Mejorá la estimación de $p(400)$ con el polinomio de orden $2$ y acotá el nuevo error.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Derivar la exponencial con la regla de la cadena y acotar las derivadas en $[0;\ h]$, donde la exponencial vale a lo sumo $1$.

**Desarrollo.** a) $p'(h) = -\frac{100}{8000}e^{-h/8000} = -\frac{1}{80}e^{-h/8000}$; $p(0) = 100$ y $p'(0) = -\frac{1}{80}$. La linealización es $L(h) = 100 - \frac{h}{80}$ y $p(400) \approx L(400) = 100 - 5 = 95$ kPa.

b) $p''(h) = \frac{1}{80 \cdot 8000}e^{-h/8000} = \frac{1}{640000}e^{-h/8000}$, positiva y decreciente: en $[0;\ 400]$ vale a lo sumo $M = \frac{1}{640000}$, con $c \in (0;\ 400)$. Entonces

$$
\lvert R_1(400) \rvert \le \dfrac{M}{2!}\,400^2 = \dfrac{160000}{2 \cdot 640000} = \dfrac18 = 0{,}125 \text{ kPa}.
$$

Como $p'' > 0$, $R_1 = \frac{p''(c)}{2}h^2 > 0$ y $p(400) > L(400)$: la estimación queda **por debajo** del valor del modelo. El valor del modelo es $100e^{-0{,}05} = 95{,}1229\ldots$ kPa y el error real es $0{,}1229$, dentro de la cota.

c) Para $h \in [0;\ H]$, $M = \frac{1}{640000}$ sigue valiendo y $\lvert R_1(h) \rvert \le \frac{h^2}{1280000}$. Pedimos $\frac{H^2}{1280000} < 0{,}05$, es decir $H^2 < 64000$, o sea $H < 252{,}98$. Sirve $H = 250$: $\frac{250^2}{1280000} = \frac{62500}{1280000} \approx 0{,}0488 < 0{,}05$.

d) $p''(0) = \frac{1}{640000}$, de modo que $P_2(h) = 100 - \frac{h}{80} + \frac{h^2}{1280000}$ y $P_2(400) = 95 + \frac{160000}{1280000} = 95{,}125$ kPa. Para el error, $p'''(h) = -\frac{1}{5{,}12 \cdot 10^{9}}e^{-h/8000}$, con $\lvert p''' \rvert \le \frac{1}{5{,}12 \cdot 10^9}$ en $[0;\ 400]$, y

$$
\lvert R_2(400) \rvert \le \dfrac{1/(5{,}12 \cdot 10^9)}{3!}\,400^3 = \dfrac{6{,}4 \cdot 10^7}{3{,}072 \cdot 10^{10}} = \dfrac{1}{480} \approx 0{,}0021 \text{ kPa}.
$$

El error real es $0{,}00206$, dentro de la cota.

**Resultado.** a) $L(h) = 100 - \frac{h}{80}$, $p(400) \approx 95$ kPa; b) $\lvert R_1(400) \rvert \le 0{,}125$ kPa, por defecto; c) $H = 250$ m; d) $p(400) \approx 95{,}125 \pm \frac{1}{480}$ kPa.

</details>
