---
title: Integradores — Unidad 2
description: Ejercicios integradores de estilo parcial sobre límites, asíntotas y continuidad, con un ítem de opción múltiple y otro con GeoGebra.
slug: analisis-matematico-i/unidad-2/practica/integradores
sidebar:
  order: 90
  label: Integradores
---

Ejercicios que combinan varias lecciones de la unidad: [límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/), [asíntotas](/analisis-matematico-i/unidad-2/teoria/asintotas/) y [continuidad](/analisis-matematico-i/unidad-2/teoria/continuidad/). Intentalos sin mirar la resolución.

### Ejercicio 29 · Parámetros, discontinuidades y asíntotas
<!-- ejercicio: U2.29 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x)=\dfrac{x^2+ax+b}{x^2-x-6}$.

a) Hallá $a$ y $b$ para que $f$ tenga en $x=3$ una discontinuidad evitable con $\lim_{x\to3}f(x)=\frac15$.

b) Con esos valores, hallá y clasificá todas las discontinuidades y redefiní $f$ donde sea posible.

c) Hallá todas las asíntotas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Factorizar el denominador, $x^2-x-6=(x-3)(x+2)$. Para que $x=3$ sea evitable, el numerador debe anularse en $3$; el valor del límite fija el otro factor.

**Desarrollo.**

a) El numerador es $(x-3)(x+s)$ para algún $s$. Entonces $f=\frac{x+s}{x+2}$ cerca de $3$ y $\lim_{x\to3}f=\frac{3+s}{5}=\frac15$, o sea $s=-2$. El numerador es $(x-3)(x-2)=x^2-5x+6$: $a=-5$, $b=6$.

b) Con esos valores, $f=\frac{(x-3)(x-2)}{(x-3)(x+2)}$ y el dominio es $\mathbb{R}-\{-2,3\}$. En $x=3$: $\lim f=\frac15$ y $f(3)$ no existe: evitable; se redefine $f(3):=\frac15$. En $x=-2$: el numerador vale $20\ne0$ y el denominador tiende a $0$; $\frac{x-2}{x+2}\to\frac{-4}{0^{+}}=-\infty$ por derecha y $+\infty$ por izquierda: esencial de salto infinito.

c) AV $x=-2$. En el infinito, $\frac{x-2}{x+2}\to1$ por ambos lados: AH $y=1$. No hay AO.

**Resultado.** $a=-5$, $b=6$; $x=3$ evitable (con $f(3):=\frac15$), $x=-2$ esencial de salto infinito; AV $x=-2$ y AH $y=1$.

</details>

### Ejercicio 30 · Con GeoGebra
<!-- ejercicio: U2.30 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x)=\dfrac{\sqrt{x^2+9}-3}{x^2}$.

a) Con GeoGebra, graficá $f$ y conjeturá el comportamiento en $x=0$ y en el infinito. Escribí los comandos que usaste.

b) Calculá analíticamente $\lim_{x\to0}f(x)$, clasificá la discontinuidad en $x=0$ y hallá las asíntotas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Explorar en GeoGebra y justificar con álgebra (racionalización).

**GeoGebra** (GeoGebra Clásico 6 o calculadora en línea; en algunas configuraciones regionales el separador de argumentos es `;`):

- `f(x) = (sqrt(x^2 + 9) - 3) / x^2`
- `Límite(f, 0)`, `LímiteIzquierda(f, 0)`, `LímiteDerecha(f, 0)`: deberían dar aproximadamente $0{,}1667$ en ambos lados.
- `Asíntota(f)`: debería devolver la recta $y=0$. Se observa que la gráfica tiene un hueco en $x=0$ y se aplana hacia $0$ en ambos extremos.

**Desarrollo analítico.** En $x=0$ se obtiene la forma $\frac00$. Con el conjugado:

$$
\frac{\sqrt{x^2+9}-3}{x^2}\cdot\frac{\sqrt{x^2+9}+3}{\sqrt{x^2+9}+3}=\frac{x^2}{x^2(\sqrt{x^2+9}+3)}=\frac1{\sqrt{x^2+9}+3}\quad(x\ne0).
$$

Entonces $\lim_{x\to0}f=\frac1{3+3}=\frac16$ (por ambos lados, pues la expresión es par). Como $f(0)$ no existe, la discontinuidad es evitable y se redefine $f(0):=\frac16$. En el infinito, $\sqrt{x^2+9}+3\to+\infty$, luego $f\to0$ en $\pm\infty$: AH $y=0$. No hay AV: el único punto problemático, $x=0$, tiene límite finito.

**Resultado.** $\lim_{x\to0}f=\frac16$ (evitable, $f(0):=\frac16$); AH $y=0$; sin AV ni AO.

</details>

### Ejercicio 31 · Opción múltiple
<!-- ejercicio: U2.31 | nivel: avanzado | tipo: opcion-multiple | verificacion: sympy -->

:::note[Enunciado]
El valor de $\displaystyle\lim_{x\to0}\frac{x+\operatorname{sen}3x}{x^2+2x}$ es:

a) $0$

b) $1$

c) $2$

d) $4$

e) no existe
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Forma $\frac00$. Dividir numerador y denominador por $x$, así la suma no obliga a sustituir equivalentes en una resta.

**Desarrollo.** $\dfrac{x+\operatorname{sen}3x}{x^2+2x}=\dfrac{1+\frac{\operatorname{sen}3x}{x}}{x+2}$. Como $\frac{\operatorname{sen}3x}{x}=3\frac{\operatorname{sen}3x}{3x}\to3$, el límite es $\dfrac{1+3}{0+2}=2$.

- a) Falsa: viene de «$\frac00=0$» o de decir que en el numerador se cancelan términos.
- b) Falsa: sale de tomar $\frac{\operatorname{sen}3x}{x}\to1$ (olvidando el $3$): $\frac{1+1}{2}$.
- c) **Verdadera.**
- d) Falsa: sale de olvidar el $2$ del denominador ($\frac{1+3}{1}$).
- e) Falsa: los dos laterales existen y valen $2$.

**Resultado.** Opción c).

</details>

### Ejercicio 32 · Continuidad de una función definida por partes
<!-- ejercicio: U2.32 | nivel: avanzado | tipo: integrador | verificacion: sympy -->

:::note[Enunciado]
Sea

$$
f(x)=\begin{cases}
\dfrac{1}{x+1} & \text{si } x<-1\\[2mm]
\dfrac{\operatorname{sen}(3x)}{2x} & \text{si } -1\le x<0\\[2mm]
ax+b & \text{si } 0\le x\le 2\\[2mm]
\dfrac{x^2-5x+6}{\lvert x-3\rvert} & \text{si } x>2,\ x\neq3
\end{cases}
$$

a) Calculá los límites laterales de $f$ en $x=0$ y en $x=2$, en función de $a$ y $b$ cuando corresponda.

b) Hallá $a$ y $b$ para que $f$ sea continua en $x=0$ y en $x=2$.

c) Con esos valores, estudiá la continuidad de $f$ en $x=-1$ y en $x=3$. Para cada punto de discontinuidad, decí si existe el límite, clasificá la discontinuidad y, si corresponde, calculá el salto o redefiní $f$.

d) Si se toma $b=\frac32$ pero $a\neq-\frac34$, ¿qué tipo de discontinuidad aparece en $x=2$ y cuánto mide el salto?

e) Si en el primer tramo se reemplaza $\frac{1}{x+1}$ por $\operatorname{sen}\frac{1}{x+1}$, ¿cómo cambia la clasificación en $x=-1$?
:::

<details>
<summary>Resolución</summary>

**Estrategia.**
- Cada tramo es continuo en su intervalo abierto: es un cociente de continuas con denominador no nulo, o un polinomio.
- Los únicos candidatos a discontinuidad son los empalmes, $-1$, $0$ y $2$, y el punto $3$, que no está en el dominio.
- En cada uno se calculan los dos laterales con la expresión del tramo que corresponde a cada lado.

**Desarrollo.**

a)
- **En $x=0$.** Por izquierda vale $\operatorname{sen}(3x)\sim3x$, así que $\dfrac{\operatorname{sen}(3x)}{2x}\to\dfrac{3}{2}$. Por derecha, $ax+b\to b$, y además $f(0)=b$.
- **En $x=2$.** Por izquierda, $ax+b\to2a+b=f(2)$. Por derecha, $x>2$ y $x$ cerca de $2$ implican $x<3$, así que $\lvert x-3\rvert=3-x$ y
$$
\frac{(x-2)(x-3)}{3-x}=-(x-2)\xrightarrow[x\to2^{+}]{}0.
$$

b) Continuidad en $0$: el límite existe solo si $b=\frac32$, y entonces coincide con $f(0)=b$. Continuidad en $2$: $2a+b=0$, de donde $a=-\frac34$.

c)
- **En $x=-1$.**
  - $f(-1)=\dfrac{\operatorname{sen}(-3)}{-2}=\dfrac{\operatorname{sen}3}{2}\approx0{,}07$ existe.
  - Por derecha, el tramo es continuo y tiende a ese mismo valor: $f$ es continua por derecha en $-1$.
  - Por izquierda, $x+1\to0^{-}$ y $\frac{1}{x+1}\to-\infty$.
  - El límite no existe y un lateral es infinito: es una **discontinuidad esencial de salto infinito**, con asíntota vertical $x=-1$ por izquierda, en un punto que **sí** pertenece al dominio. No se puede redefinir.
- **En $x=3$.**
  - $f(3)$ no existe.
  - Para $x\neq3$ cerca de $3$, $\dfrac{(x-2)(x-3)}{\lvert x-3\rvert}=(x-2)\cdot\operatorname{sg}(x-3)$, donde $\operatorname{sg}$ es la función signo.
  - Por izquierda tiende a $-1$ y por derecha a $1$.
  - Los laterales son finitos y distintos: es una **discontinuidad esencial de salto finito**, con salto $\lvert1-(-1)\rvert=2$. Tampoco se puede redefinir: ningún valor de $f(3)$ une dos laterales distintos.

d) Con $b=\frac32$, por izquierda $f\to2a+\frac32=f(2)$ y por derecha $f\to0$. Si $a\neq-\frac34$, los laterales son finitos y distintos: es una **discontinuidad esencial de salto finito**, con salto $\bigl\lvert2a+\frac32\bigr\rvert$, y $f$ es continua por izquierda en $2$.

e) Por izquierda de $-1$, $\frac{1}{x+1}\to-\infty$ y $\operatorname{sen}\frac{1}{x+1}$ oscila entre $-1$ y $1$ sin acercarse a ningún valor, así que el lateral izquierdo **no existe**, ni finito ni infinito. Es una **discontinuidad esencial de segunda especie**: ya no hay asíntota vertical y tampoco tiene sentido hablar de salto.

**Resultado.**
- $a=-\frac34$ y $b=\frac32$.
- En $x=-1$, esencial de salto infinito, con $f$ continua por derecha.
- En $x=3$, esencial de salto finito, con salto $2$.
- En los demás puntos, $f$ es continua.
- Con $a\neq-\frac34$ aparece en $x=2$ un salto finito de $\bigl\lvert2a+\frac32\bigr\rvert$.
- Con $\operatorname{sen}\frac{1}{x+1}$, la discontinuidad en $-1$ pasa a ser de segunda especie.

**Interpretación.**
- La continuidad se decide **punto por punto** y con los dos laterales. Que $f(-1)$ exista no salva la continuidad en $-1$: la condición que falla es la existencia del límite.
- El valor absoluto obliga a elegir la expresión según el lado. Por eso en $x=2^{+}$ hubo que usar $\lvert x-3\rvert=3-x$ aunque el tramo se defina «para $x>2$».
- La clasificación depende del comportamiento de los laterales, no de la fórmula: el mismo empalme en $-1$ es de salto infinito o de segunda especie según cómo se comporte el lateral izquierdo.

</details>
