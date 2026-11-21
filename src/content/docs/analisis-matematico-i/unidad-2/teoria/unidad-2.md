---
title: Unidad 2 — Resumen integrador
slug: analisis-matematico-i/unidad-2/teoria/unidad-2
sidebar:
  hidden: true
  label: Resumen integrador
---

:::tip[Cómo usar este resumen]
- **Antes de estudiar:** leelo de corrido para tener el mapa de la unidad, de la definición de límite a la continuidad.
- **Después de estudiar:** usalo para repasar y conectar los temas.
- **Antes del primer parcial:** identificá los temas principales y volvé a la lección de cada uno.

No reemplaza a las lecciones, que desarrollan cada tema con demostraciones, ejemplos resueltos, ejercicios y
autoevaluación:

1. [Entornos y límite finito](/analisis-matematico-i/unidad-2/teoria/entornos-y-limite/)
2. [Límites laterales y propiedades](/analisis-matematico-i/unidad-2/teoria/limites-laterales-y-propiedades/)
3. [Infinitésimos](/analisis-matematico-i/unidad-2/teoria/infinitesimos/)
4. [Límites infinitos y en el infinito](/analisis-matematico-i/unidad-2/teoria/limites-infinitos/)
5. [Cálculo de límites e indeterminaciones](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/)
6. [Asíntotas](/analisis-matematico-i/unidad-2/teoria/asintotas/)
7. [Continuidad y discontinuidades](/analisis-matematico-i/unidad-2/teoria/continuidad/)

La ruta completa de la unidad está en la [presentación](/analisis-matematico-i/unidad-2/).
:::






---

## 1. Distancia y entorno

Antes de hablar de límites, necesitamos una forma precisa de decir “cerca de”.

- La **distancia** entre dos números reales $a$ y $b$ es $\lvert a - b \rvert$.
- Si $\lvert a-b\rvert$ es pequeña, entonces $a$ y $b$ están cerca.

Un **entorno** de centro $a$ y radio $r>0$ reúne todos los números que quedan a menos de $r$ de $a$:



$$
E(a, r) = (a - r,\; a + r) = \{x \in \mathbb{R} : \lvert x - a \rvert < r\}
$$



El **entorno reducido** es ese mismo entorno, pero sin el punto central:



$$
E^{*}(a, r) = E(a, r) - \{a\} = \{x \in \mathbb{R} : 0 < \lvert x - a \rvert < r\}
$$



**Idea clave:** cuando hablamos de límites, importa lo que pasa cerca de $a$, no necesariamente en $a$ mismo.

---

## 2. Límite finito

### Definición ($\varepsilon$-$\delta$)



$$
\lim_{x \to a} f(x) = L
$$



quiere decir que podemos hacer que $f(x)$ quede tan cerca de $L$ como queramos, siempre que tomemos $x$ suficientemente cerca de $a$.

La definición formal dice que para todo $\varepsilon > 0$ existe $\delta > 0$ tal que:



$$
0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \varepsilon
$$



Interpretación:

- $\varepsilon$ fija qué tan cerca queremos estar de $L$
- $\delta$ fija qué tan cerca debemos tomar a $x$ de $a$

> El valor de $f$ en $x = a$ (si existe) **no importa** para la definición del límite.

### Interpretación gráfica

Gráficamente, esto significa que si nos movemos hacia $a$ por izquierda o por derecha, los valores de la función se acercan a $L$.

No hace falta que la función valga exactamente $L$ en $x=a$; basta con que se acerque.

---

## 3. Límites laterales

- **Límite por la derecha:** $\displaystyle\lim_{x \to a^+} f(x) = L^+$.
- **Límite por la izquierda:** $\displaystyle\lim_{x \to a^-} f(x) = L^-$.

Sirven para estudiar qué pasa al acercarse a un punto desde un solo lado. Esto es muy útil cuando una función cambia de definición en un punto.

**Teorema:**



$$
\lim_{x \to a} f(x) = L \iff \lim_{x \to a^+} f(x) = \lim_{x \to a^-} f(x) = L
$$



En palabras: el límite total existe solo si ambos límites laterales existen y coinciden.

---

## 4. Unicidad del límite

Si $\displaystyle\lim_{x \to a} f(x)$ existe, es **único**.

No puede haber dos resultados distintos para el mismo proceso de aproximación.

**Consecuencia:** si los límites laterales son distintos, el límite global no existe.

---

## 5. Propiedades del límite (álgebra de límites)

Sean $\displaystyle\lim_{x \to a} f(x) = L$ y $\displaystyle\lim_{x \to a} g(x) = M$. Entonces:

| Propiedad | Resultado |
|-----------|-----------|
| Suma | $\displaystyle\lim_{x \to a}[f(x) + g(x)] = L + M$ |
| Diferencia | $\displaystyle\lim_{x \to a}[f(x) - g(x)] = L - M$ |
| Producto | $\displaystyle\lim_{x \to a}[f(x) \cdot g(x)] = L \cdot M$ |
| Cociente | $\displaystyle\lim_{x \to a}\frac{f(x)}{g(x)} = \frac{L}{M}$, si $M \neq 0$ |
| Potencia | $\displaystyle\lim_{x \to a}[f(x)]^n = L^n$ |
| Raíz | $\displaystyle\lim_{x \to a}\sqrt[n]{f(x)} = \sqrt[n]{L}$, si aplica |
| Constante | $\displaystyle\lim_{x \to a} c = c$ |
| Identidad | $\displaystyle\lim_{x \to a} x = a$ |

La utilidad de estas propiedades es que permiten desarmar un límite complicado en partes simples.

En la práctica, casi siempre se empieza por:

1. sustituir directamente
2. ver si aparece una indeterminación
3. aplicar alguna propiedad algebraica o alguna técnica de simplificación

---

## 6. Teorema de intercalación (Sandwich)

Si una función queda atrapada entre otras dos, y esas dos se acercan al mismo valor, entonces la función intermedia también se acerca a ese valor.

Si $g(x) \leq f(x) \leq h(x)$ en un entorno reducido de $a$, y



$$
\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L
$$



entonces:



$$
\lim_{x \to a} f(x) = L
$$



**Aplicación típica:** controlar funciones con oscilación o con factores acotados.



$$
\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1
$$



La idea central es que, aunque no podamos calcular directamente la expresión, sí podemos encerrar su comportamiento entre dos límites conocidos.

---

## 7. Infinitésimos

Una función $\alpha(x)$ es un **infinitésimo** cuando $x \to a$ si $\displaystyle\lim_{x \to a} \alpha(x) = 0$.

En otras palabras, es una cantidad que se hace cada vez más pequeña hasta desaparecer en el límite.

### Álgebra de infinitésimos

- Suma de infinitésimos: infinitésimo.
- Producto de infinitésimo por función acotada: infinitésimo.

Estas propiedades ayudan a simplificar expresiones sin cambiar el comportamiento del límite.

### Comparación de infinitésimos

Sean $\alpha$ y $\beta$ infinitésimos cuando $x \to a$:

| Caso | Nombre |
|------|--------|
| $\displaystyle\lim_{x \to a} \frac{\alpha}{\beta} = L \neq 0$ | $\alpha$ y $\beta$ son del mismo orden |
| $\displaystyle\lim_{x \to a} \frac{\alpha}{\beta} = 0$ | $\alpha$ es de orden superior a $\beta$ $\bigl(\alpha = o(\beta)\bigr)$ |
| $\displaystyle\lim_{x \to a} \frac{\alpha}{\beta} = \infty$ | $\alpha$ es de orden inferior a $\beta$ |
| $\displaystyle\lim_{x \to a} \frac{\alpha}{\beta^k} = L \neq 0$ | $\alpha$ es de orden $k$ respecto a $\beta$ |

**Infinitésimos equivalentes** ($\alpha \sim \beta$): $\displaystyle\lim_{x \to a} \frac{\alpha}{\beta} = 1$. Se pueden sustituir en productos/cocientes.

Esto significa que, cerca del punto, ambas funciones se comportan prácticamente igual.

Equivalencias fundamentales cuando $x \to 0$:



$$
\operatorname{sen} x \sim x \qquad \tan(x) \sim x \qquad 1 - \cos(x) \sim \frac{x^2}{2}
$$





$$
\ln(1 + x) \sim x \qquad e^x - 1 \sim x
$$



Conviene aprender estas equivalencias porque son una de las herramientas más útiles para calcular límites sin desarrollar series de Taylor.

---

## 8. Límites infinitos



$$
\lim_{x \to a} f(x) = +\infty
$$



significa que la función crece sin cota superior cuando $x$ se acerca a $a$.

Formalmente, para todo $M > 0$ existe $\delta > 0$ tal que:



$$
0 < \lvert x - a \rvert < \delta \implies f(x) > M
$$



Análogamente, $\displaystyle\lim_{x \to a} f(x) = -\infty$ significa que la función baja sin cota inferior.

**Lectura intuitiva:** cuanto más nos acercamos a $a$, más grande en valor absoluto se vuelve la función.

---

## 9. Límites de variable infinita



$$
\lim_{x \to +\infty} f(x) = L
$$



significa que, cuando $x$ crece mucho, los valores de la función se acercan a $L$.

Formalmente, para todo $\varepsilon > 0$ existe $N$ tal que:



$$
x > N \implies \lvert f(x) - L \rvert < \varepsilon
$$



La idea es la misma que en un límite finito: no buscamos un valor exacto en infinito, sino el comportamiento de la función muy lejos del origen.

---

## 10. Cálculo de límites e indeterminaciones

### Formas indeterminadas

| Forma | Técnicas habituales |
|-------|---------------------|
| $\dfrac{0}{0}$ | Factorizar, racionalizar, infinitésimos equivalentes |
| $\dfrac{\infty}{\infty}$ | Dividir por la potencia dominante |
| $0 \cdot \infty$ | Reescribir como $\dfrac{0}{0}$ o $\dfrac{\infty}{\infty}$ |
| $\infty - \infty$ | Factorizar, conjugado |
| $1^\infty$ | Usar $e^{\lim (f-1)\cdot g}$ |
| $0^0$ | Usar logaritmo |
| $\infty^0$ | Usar logaritmo |

Una forma indeterminada no significa que el límite “no exista” automáticamente. Significa que todavía no tenemos información suficiente y hay que reescribir la expresión.

### Estrategia de cálculo

1. Probar sustitución directa
2. Si aparece una indeterminación, simplificar algebraicamente
3. Usar factorización, racionalización o equivalencias
4. Si hace falta, recurrir a límites notables

### Límites notables



$$
\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e \qquad \lim_{x \to 0} (1 + x)^{1/x} = e
$$





$$
\lim_{x \to 0} \frac{\operatorname{sen} x}{x} = 1 \qquad \lim_{x \to 0} \frac{e^x - 1}{x} = 1 \qquad \lim_{x \to 0} \frac{\ln(1+x)}{x} = 1
$$



Estos límites sirven como “bloques base” para resolver muchos ejercicios por comparación.

---

## 11. Asíntotas

### Asíntota vertical (AV)

La recta $x = a$ es una asíntota vertical si la función se dispara hacia $+\infty$ o hacia $-\infty$ al acercarse a ese valor.

En la gráfica, eso se ve como una recta que la curva se aproxima cada vez más, pero nunca “tranquilamente”.

### Asíntota horizontal (AH)

La recta $y = L$ es una asíntota horizontal si la función se acerca a ese valor cuando $x$ se hace muy grande en positivo o en negativo.

Sirve para describir el comportamiento final de la gráfica.

### Asíntota oblicua (AO)

La recta $y = mx + n$ es AO si:



$$
m = \lim_{x \to \pm\infty} \frac{f(x)}{x} \qquad n = \lim_{x \to \pm\infty} \bigl[f(x) - mx\bigr]
$$



La asíntota oblicua aparece cuando la función se parece a una recta inclinada para valores grandes de $x$.

> Si existe AH, no hay AO (en esa misma dirección).

**Idea práctica:** primero se revisa si hay comportamiento horizontal; si no lo hay, puede aparecer una recta oblicua.

---

## 12. Continuidad

### Función continua en un punto

La continuidad expresa que la gráfica no tiene cortes, saltos ni huecos en un punto.

$f$ es **continua en $x = a$** si se cumplen las tres condiciones:

1. $f(a)$ existe $\;(a \in D_f)$.
2. $\displaystyle\lim_{x \to a} f(x)$ existe y es finito.
3. $\displaystyle\lim_{x \to a} f(x) = f(a)$.

Si una sola de esas condiciones falla, la función no es continua en ese punto.

### Continuidad en intervalos

- **Intervalo abierto $(a, b)$:** continua en cada punto interior.
- **Intervalo cerrado $[a, b]$:** continua en $(a, b)$, con $\displaystyle\lim_{x \to a^+} f(x) = f(a)$ y $\displaystyle\lim_{x \to b^-} f(x) = f(b)$.

En los extremos de un intervalo cerrado solo se pide continuidad por el lado que pertenece al intervalo.

### Álgebra de funciones continuas

Si $f$ y $g$ son continuas en $a$, entonces $f+g$, $f-g$, $f \cdot g$ y $\dfrac{f}{g}$ (si $g(a) \neq 0$) son continuas en $a$. Además, si $f$ es continua en $a$ y $g$ es continua en $f(a)$, la composición $g \circ f$ es continua en $a$.

Esto permite construir funciones continuas a partir de otras ya conocidas como continuas.

### Propiedades de funciones continuas en $[a, b]$

- **Teorema de Bolzano:** si $f(a) \cdot f(b) < 0$, existe $c \in (a, b)$ con $f(c) = 0$.
- **Teorema del valor intermedio:** $f$ toma todos los valores entre $f(a)$ y $f(b)$ (se deduce de Bolzano).
- **Teorema de Weierstrass:** $f$ alcanza su máximo y su mínimo absolutos.

Estas propiedades son muy importantes porque convierten la continuidad en una herramienta de existencia: no solo describen la gráfica, también garantizan que ciertos valores aparecen.

---

## 13. Clasificación de discontinuidades

Sea $x = a$ un punto de discontinuidad de $f$:

| Tipo | Condición | Característica |
|------|-----------|----------------|
| **Evitable** | $\displaystyle\lim_{x \to a} f(x) = \ell$ existe (finito) pero $f(a)$ no existe o es $\neq \ell$ | Se redefine $f(a) := \ell$ |
| **Esencial de 1ª especie, de salto finito** | Los dos laterales existen, son finitos y distintos | Salto $S = \lvert L^{+} - L^{-} \rvert$ |
| **Esencial de 1ª especie, de salto infinito** | Algún lateral es $\pm\infty$ | Asíntota vertical $x = a$ |
| **Esencial de 2ª especie** | Algún lateral no existe (ni finito ni infinito), p. ej. $\operatorname{sen}\frac{1}{x}$ en $0$ | La función oscila; no hay salto |

### Cómo reconocerlas

- **Evitable:** el límite existe y es finito, pero falta $f(a)$ o tiene otro valor.
- **Esencial de salto finito:** los dos laterales existen y son finitos, pero no coinciden.
- **Esencial de salto infinito:** algún lateral se va a $\pm\infty$.
- **Esencial de 2ª especie:** algún lateral no existe.

Este cuadro ayuda mucho en ejercicios de análisis de gráficas, porque muchas veces basta con mirar el tipo de ruptura para clasificar la discontinuidad.
