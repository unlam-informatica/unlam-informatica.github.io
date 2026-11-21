---
title: Límites laterales y propiedades
description: Límites laterales, unicidad del límite, álgebra de límites con sus hipótesis, teorema de intercalación y el límite de sen x sobre x.
slug: analisis-matematico-i/unidad-2/teoria/limites-laterales-y-propiedades
sidebar:
  order: 2
---

## Qué vas a aprender

- Calcular límites laterales y decidir si existe el límite (funciones por tramos, con valor absoluto).
- Demostrar y usar la unicidad del límite.
- Aplicar el álgebra de límites indicando sus hipótesis.
- Aplicar el teorema de intercalación, incluido el producto de una función que tiende a $0$ por una función acotada, y conocer el límite $\lim_{x\to0}\frac{\operatorname{sen}x}{x}=1$.

**Antes de empezar.** Tenés que dominar la definición de límite de [Entornos y límite finito](/analisis-matematico-i/unidad-2/teoria/entornos-y-limite/).

## Límites laterales

Cuando una función cambia de regla en $a$, o tiene un valor absoluto, o un denominador que se anula, conviene mirar cada lado de $a$ por separado.

:::note[Definición · Límites laterales]
- $\displaystyle\lim_{x\to a^{+}}f(x)=L$ (**límite por derecha**) si $\forall\varepsilon>0\ \exists\delta>0:\ a<x<a+\delta\Rightarrow\lvert f(x)-L\rvert<\varepsilon$.
- $\displaystyle\lim_{x\to a^{-}}f(x)=L$ (**límite por izquierda**) si $\forall\varepsilon>0\ \exists\delta>0:\ a-\delta<x<a\Rightarrow\lvert f(x)-L\rvert<\varepsilon$.
:::

:::note[Teorema · Límite y límites laterales]
Sea $f$ definida en un entorno reducido de $a$. Entonces

$$
\lim_{x\to a}f(x)=L\iff\lim_{x\to a^{-}}f(x)=L\ \text{ y }\ \lim_{x\to a^{+}}f(x)=L .
$$
:::

**Demostración.** ($\Rightarrow$) Si $0<\lvert x-a\rvert<\delta$ implica $\lvert f(x)-L\rvert<\varepsilon$, en particular vale para los $x$ con $a<x<a+\delta$ y con $a-\delta<x<a$.
($\Leftarrow$) Dado $\varepsilon>0$, sean $\delta_1$ el que sirve por izquierda y $\delta_2$ el que sirve por derecha. Con $\delta=\min\{\delta_1,\delta_2\}$, todo $x$ con $0<\lvert x-a\rvert<\delta$ está a la izquierda o a la derecha de $a$, dentro del radio correspondiente, y cumple $\lvert f(x)-L\rvert<\varepsilon$. $\blacksquare$

La consecuencia práctica: **si los laterales existen y son distintos, el límite no existe**. Y si uno de los laterales no existe, tampoco.

![Gráfico de una función con una rama que tiende a 2 por izquierda y otra que tiende a 3 por derecha en x = 1, con puntos huecos en esas alturas y un punto lleno en (1, 1)](/analisis-matematico-i/figuras/u2-laterales-distintos.svg)

*Qué observar: por izquierda la curva se acerca a $2$ y por derecha a $3$; el valor $f(1)=1$ (punto lleno) no tiene nada que ver con ninguno de los dos. Como los laterales difieren, no existe $\lim_{x\to1}f(x)$.*

### Ejemplo 1 · Valor absoluto

<!-- check: U2.T.LAT.1 -->

Estudiar $\displaystyle\lim_{x\to2}\frac{x^2-4}{\lvert x-2\rvert}$.

Al sustituir se obtiene la forma $\frac00$. Hay un módulo, así que separamos los lados.

- Si $x>2$: $\lvert x-2\rvert=x-2$ y $\dfrac{(x-2)(x+2)}{x-2}=x+2\to4$.
- Si $x<2$: $\lvert x-2\rvert=-(x-2)$ y $\dfrac{(x-2)(x+2)}{-(x-2)}=-(x+2)\to-4$.

Los laterales son $4$ y $-4$: **el límite no existe**.

### Ejemplo 2 · Función por tramos con un parámetro

<!-- check: U2.T.LAT.2 -->

Hallar $k$ para que exista $\displaystyle\lim_{x\to2}f(x)$, si $f(x)=\begin{cases}kx+1 & \text{si } x<2\\ x^2-k & \text{si } x\ge2\end{cases}$

Por izquierda, $\lim_{x\to2^{-}}(kx+1)=2k+1$; por derecha, $\lim_{x\to2^{+}}(x^2-k)=4-k$. Existe el límite si y solo si son iguales: $2k+1=4-k$, es decir $k=1$. El límite vale entonces $3$.

## Unicidad del límite

:::note[Teorema · Unicidad]
Si $\lim_{x\to a}f(x)=L_1$ y $\lim_{x\to a}f(x)=L_2$, entonces $L_1=L_2$.
:::

**Demostración.** Supongamos $L_1\neq L_2$ y tomemos $\varepsilon=\dfrac{\lvert L_1-L_2\rvert}{2}>0$. Por la definición, existen $\delta_1,\delta_2>0$ tales que $0<\lvert x-a\rvert<\delta_1\Rightarrow\lvert f(x)-L_1\rvert<\varepsilon$ y $0<\lvert x-a\rvert<\delta_2\Rightarrow\lvert f(x)-L_2\rvert<\varepsilon$. Sea $\delta=\min\{\delta_1,\delta_2\}$ y un $x$ con $0<\lvert x-a\rvert<\delta$ (existe, porque $f$ está definida alrededor de $a$). Por la desigualdad triangular,

$$
\lvert L_1-L_2\rvert\le\lvert L_1-f(x)\rvert+\lvert f(x)-L_2\rvert<2\varepsilon=\lvert L_1-L_2\rvert,
$$

lo cual es absurdo. Luego $L_1=L_2$. $\blacksquare$

Gracias a la unicidad, «el límite» tiene sentido como número. Y es lo que justifica que **dos laterales distintos impiden la existencia del límite**: si existiera, tendría que ser igual a cada uno.

:::note[Propiedad · Conservación del signo]
Si $\lim_{x\to a}f(x)=L>0$, existe un entorno reducido de $a$ donde $f(x)>0$. Si $L<0$, donde $f(x)<0$.
:::

**Idea de la demostración.** Con $\varepsilon=L/2$ la definición da un $\delta$ tal que $\lvert f(x)-L\rvert<L/2$, o sea $f(x)>L-L/2=L/2>0$ en $E^{*}(a,\delta)$.

## Álgebra de límites

:::note[Teorema · Álgebra de límites]
**Hipótesis:** existen (como números reales) $\lim_{x\to a}f(x)=L$ y $\lim_{x\to a}g(x)=M$. Entonces:

| Operación | Resultado | Condición adicional |
|---|---|---|
| Suma y diferencia | $\lim(f\pm g)=L\pm M$ | ninguna |
| Múltiplo | $\lim(kf)=kL$ | $k\in\mathbb{R}$ |
| Producto | $\lim(f\cdot g)=L\cdot M$ | ninguna |
| Cociente | $\lim\dfrac fg=\dfrac LM$ | $M\neq0$ |
| Potencia | $\lim f^{\,n}=L^{n}$ | $n\in\mathbb{N}$ |
| Raíz | $\lim\sqrt[n]{f}=\sqrt[n]{L}$ | $n$ impar, o $n$ par y $L>0$ (si $L=0$, con $f\ge0$ cerca de $a$) |
| Potencia de base y exponente variables | $\lim f^{\,g}=L^{M}$ | $L>0$ |

Además $\lim_{x\to a}c=c$ y $\lim_{x\to a}x=a$. La última fila se justifica escribiendo $f^{\,g}=e^{\,g\ln f}$: como $g\ln f\to M\ln L$ y la exponencial es continua, $f^{\,g}\to e^{M\ln L}=L^{M}$ (la continuidad de $\ln$ y de $e^x$ se estudia en [Continuidad](/analisis-matematico-i/unidad-2/teoria/continuidad/)). Si $L=1$ y $g\to\pm\infty$, la expresión es la forma indeterminada $1^{\infty}$, que se trata en [Cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/).
:::

**Demostración (suma).** Dado $\varepsilon>0$, existen $\delta_1,\delta_2$ con $0<\lvert x-a\rvert<\delta_1\Rightarrow\lvert f(x)-L\rvert<\varepsilon/2$ y $0<\lvert x-a\rvert<\delta_2\Rightarrow\lvert g(x)-M\rvert<\varepsilon/2$. Con $\delta=\min\{\delta_1,\delta_2\}$,

$$
\lvert (f(x)+g(x))-(L+M)\rvert\le\lvert f(x)-L\rvert+\lvert g(x)-M\rvert<\tfrac\varepsilon2+\tfrac\varepsilon2=\varepsilon .\ \blacksquare
$$

Las demás propiedades se demuestran de manera análoga (el producto, escribiendo $fg-LM=(f-L)g+L(g-M)$; el cociente, acotando $1/\lvert g\rvert$ cerca de $a$ con la conservación del signo).

**Las hipótesis importan.** La tabla no dice qué pasa si los límites no existen o si $M=0$:

- El cociente con $M=0$ **no** se calcula con la propiedad: puede dar $\frac00$ (indeterminado), o $\frac{L}{0}$ con $L\neq 0$ (diverge). Ver [Cálculo de límites](/analisis-matematico-i/unidad-2/teoria/calculo-de-limites/).
- La recíproca es falsa: $\lim(f+g)$ puede existir sin que existan $\lim f$ ni $\lim g$ (por ejemplo, $f(x)=\operatorname{sen}\frac1x$ y $g(x)=-\operatorname{sen}\frac1x$ suman $0$).

### Ejemplo 3 · Límite inmediato, paso por paso

<!-- check: U2.T.LAT.3 -->

Calcular $\displaystyle\lim_{x\to4}\frac{3x^2-x}{\sqrt{x}+1}$.

Los límites del numerador y del denominador existen: $\lim(3x^2-x)=3\cdot16-4=44$ (suma, múltiplo, potencia) y $\lim(\sqrt x+1)=2+1=3\neq0$ (raíz con $L=4>0$, suma). Como el límite del denominador no es cero, vale la propiedad del cociente:

$$
\lim_{x\to4}\frac{3x^2-x}{\sqrt{x}+1}=\frac{44}{3}.
$$

Cuando esto funciona (la sustitución da un número), decimos que el límite es **inmediato**.

## Teorema de intercalación

:::note[Teorema · Intercalación (o del sándwich)]
**Hipótesis:** $g(x)\le f(x)\le h(x)$ para todo $x$ de un entorno reducido de $a$, y $\lim_{x\to a}g(x)=\lim_{x\to a}h(x)=L$.

**Tesis:** $\lim_{x\to a}f(x)=L$.
:::

**Demostración.** Dado $\varepsilon>0$ existen $\delta_1,\delta_2$ (y el radio $r$ del entorno donde vale la desigualdad) tales que $L-\varepsilon<g(x)$ si $0<\lvert x-a\rvert<\delta_1$ y $h(x)<L+\varepsilon$ si $0<\lvert x-a\rvert<\delta_2$. Con $\delta=\min\{\delta_1,\delta_2,r\}$ resulta $L-\varepsilon<g(x)\le f(x)\le h(x)<L+\varepsilon$, es decir $\lvert f(x)-L\rvert<\varepsilon$. $\blacksquare$

Si falla la hipótesis de que **ambas** cotas tienen el mismo límite, no hay conclusión: $-1\le\operatorname{sen}\frac1x\le1$ no dice nada sobre $\lim_{x\to0}\operatorname{sen}\frac1x$ (que, de hecho, no existe).

:::note[Corolario · Infinitésimo por función acotada]
Una función que tiende a $0$ en $a$ se llama **infinitésimo** en $a$ (lo estudiamos en la [próxima lección](/analisis-matematico-i/unidad-2/teoria/infinitesimos/)). Si $\lim_{x\to a}f(x)=0$ y $g$ está **acotada** en un entorno reducido de $a$ ($\lvert g(x)\rvert\le K$), entonces $\lim_{x\to a}f(x)g(x)=0$.
:::

Se deduce de $-K\lvert f\rvert\le fg\le K\lvert f\rvert$ y del teorema (con $\lim\lvert f\rvert=0$).

### Ejemplo 4 · Oscilación controlada

<!-- check: U2.T.LAT.4 -->

Calcular $\displaystyle\lim_{x\to0}x^2\operatorname{sen}\frac1x$.

La función $\operatorname{sen}\frac1x$ no tiene límite en $0$, pero está acotada: $-1\le\operatorname{sen}\frac1x\le1$. Multiplicando por $x^2\ge0$,

$$
-x^2\le x^2\operatorname{sen}\frac1x\le x^2 .
$$

Como $\lim_{x\to0}(-x^2)=\lim_{x\to0}x^2=0$, por intercalación el límite pedido es $0$. (Es un infinitésimo, $x^2$, por una función acotada.)

![Gráfico de x² sen(1/x), que oscila cada vez más rápido al acercarse a 0, encerrada entre las parábolas x² y −x²](/analisis-matematico-i/figuras/u2-intercalacion.svg)

*Qué observar: la curva oscila infinitas veces cerca de $0$, pero queda atrapada entre $-x^2$ y $x^2$, que se juntan en el origen; por eso se aplasta hacia $0$.*

## El límite fundamental $\operatorname{sen}x/x$

:::note[Teorema · Límite notable]
$$
\lim_{x\to0}\frac{\operatorname{sen}x}{x}=1 .
$$
:::

**Demostración (geométrica).** Usa dos hechos que aceptamos: el área de un sector circular de radio $1$ y ángulo $x$ (en radianes) es $\tfrac x2$, y una región contenida en otra tiene menor área. Sea $0<x<\tfrac\pi2$. En la circunferencia unidad, el triángulo de vértices el origen, $(1,0)$ y $(\cos x,\operatorname{sen}x)$ está contenido en el sector, que a su vez está contenido en el triángulo rectángulo de catetos $1$ y $\tan x$. Comparando áreas,

$$
\tfrac12\operatorname{sen}x<\tfrac12x<\tfrac12\tan x\ \Longrightarrow\ \cos x<\frac{\operatorname{sen}x}{x}<1 .
$$

Falta ver que $\cos x\to1$. De $\operatorname{sen}t<t$ para $t>0$ (primera desigualdad) y de $1-\cos x=2\operatorname{sen}^2\frac x2$ sale $0<1-\cos x<\tfrac{x^2}{2}$, que tiende a $0$ por intercalación. Entonces $\cos x<\frac{\operatorname{sen}x}{x}<1$ da, por intercalación, $\lim_{x\to0^{+}}\frac{\operatorname{sen}x}{x}=1$. Como $\frac{\operatorname{sen}x}{x}$ es **par** (no cambia al cambiar $x$ por $-x$), el límite por izquierda es el mismo. $\blacksquare$

### Ejemplo 5 · Consecuencias

<!-- check: U2.T.LAT.5 -->

Con el cambio de variable $u=5x$ (que tiende a $0$ cuando $x\to0$):

$$
\lim_{x\to0}\frac{\operatorname{sen}5x}{x}=5\lim_{x\to0}\frac{\operatorname{sen}5x}{5x}=5\cdot1=5 .
$$

Y para la tangente, $\dfrac{\tan x}{x}=\dfrac{\operatorname{sen}x}{x}\cdot\dfrac1{\cos x}\to1\cdot1=1$, porque $\cos x\to1$.

:::caution[Errores frecuentes]
- **Aplicar la propiedad del cociente cuando $M=0$.** Con $\lim_{x\to1}\frac{x-1}{x^2-1}$ el denominador tiende a $0$: la propiedad no aplica (el límite existe y vale $\tfrac12$, pero hay que simplificar primero).
- **Decir que un límite «no existe» sin calcular los dos laterales.** Hay que mostrar que son distintos (o que alguno falla).
- **Usar intercalación con cotas de distinto límite**, o con una cota que no vale en un entorno de $a$.
- **Olvidar que el límite de $x\,\operatorname{sen}\frac1x$ en $0$ es $0$ y no «no existe»:** infinitésimo por acotada.
- **Creer que $\lim_{x\to a}f(x)=L$ implica $f(a)=L$.** Eso es continuidad, no límite.
:::

## Ejercicios

### Ejercicio 5 · Laterales con valor absoluto
<!-- ejercicio: U2.05 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Calculá, estudiando los límites laterales, y decidí si existe cada límite:

a) $\displaystyle\lim_{x\to3}\frac{x^2-x-6}{\lvert x-3\rvert}$

b) $\displaystyle\lim_{x\to-1}\frac{\lvert x+1\rvert}{x^2-1}$
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Escribir el valor absoluto sin barras en cada lado, factorizar y simplificar.

**Desarrollo.**

a) Al sustituir se obtiene la forma $\frac00$ (numerador $9-3-6=0$ y denominador $0$). Como $x^2-x-6=(x-3)(x+2)$:

- $x\to3^{+}$: $\lvert x-3\rvert=x-3$, el cociente es $x+2\to5$.
- $x\to3^{-}$: $\lvert x-3\rvert=-(x-3)$, el cociente es $-(x+2)\to-5$.

Los laterales difieren: no existe el límite.

b) Al sustituir se obtiene la forma $\frac{0}{0}$. Con $x^2-1=(x-1)(x+1)$:

- $x\to-1^{+}$: $\lvert x+1\rvert=x+1$ y el cociente es $\dfrac1{x-1}\to-\dfrac12$.
- $x\to-1^{-}$: $\lvert x+1\rvert=-(x+1)$ y el cociente es $-\dfrac1{x-1}\to\dfrac12$.

**Resultado.** a) los laterales son $5$ y $-5$, no existe; b) los laterales son $\tfrac12$ (izquierda) y $-\tfrac12$ (derecha), no existe.

</details>

### Ejercicio 6 · Dos parámetros por continuidad del límite
<!-- ejercicio: U2.06 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $f(x)=\begin{cases}ax+4 & \text{si } x<-1\\ x^2+b & \text{si } -1\le x\le3\\ 12-x & \text{si } x>3\end{cases}$

Hallá $a$ y $b$ para que existan $\lim_{x\to-1}f(x)$ y $\lim_{x\to3}f(x)$, y calculá esos límites.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En cada punto de empalme, igualar los dos límites laterales.

**Desarrollo.** En $x=3$: por izquierda $\lim(x^2+b)=9+b$; por derecha $\lim(12-x)=9$. Igualando, $b=0$.

En $x=-1$: por izquierda $\lim(ax+4)=-a+4$; por derecha $\lim(x^2+b)=1+b=1$. Igualando, $-a+4=1$, es decir $a=3$.

**Resultado.** $a=3$, $b=0$; $\lim_{x\to-1}f(x)=1$ y $\lim_{x\to3}f(x)=9$.

</details>

### Ejercicio 7 · Intercalación
<!-- ejercicio: U2.07 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Calculá, justificando con el teorema de intercalación o con el corolario del infinitésimo por función acotada:

a) $\displaystyle\lim_{x\to2}(x-2)^2\operatorname{sen}\frac{5}{x-2}$

b) $\displaystyle\lim_{x\to0^{+}}\sqrt{x}\,\bigl(3+\cos\tfrac1x\bigr)$
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reconocer un infinitésimo multiplicado por una función acotada y encerrarlo entre dos cotas que tienden a $0$.

**Desarrollo.**

a) $(x-2)^2\to0$ y $\bigl\lvert\operatorname{sen}\frac5{x-2}\bigr\rvert\le1$. Entonces $-(x-2)^2\le(x-2)^2\operatorname{sen}\frac5{x-2}\le(x-2)^2$ y ambas cotas tienden a $0$.

b) Como $-1\le\cos\frac1x\le1$, resulta $2\le3+\cos\frac1x\le4$ y, multiplicando por $\sqrt x>0$, $2\sqrt x\le\sqrt x\,(3+\cos\tfrac1x)\le4\sqrt x$. Ambas cotas tienden a $0$ cuando $x\to0^{+}$.

**Resultado.** a) $0$; b) $0$.

</details>

### Ejercicio 8 · No existencia con la definición
<!-- ejercicio: U2.08 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Demostrá, usando la definición, que $\displaystyle\lim_{x\to0}\operatorname{sen}\frac1x$ no existe.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Mostrar que, cualquiera sea $\delta$, el entorno reducido contiene puntos donde la función vale $1$ y puntos donde vale $-1$; con $\varepsilon=1$ ningún $L$ puede estar a distancia menor que $1$ de ambos.

**Desarrollo.** Supongamos que el límite es $L$ y tomemos $\varepsilon=1$. Sea $\delta>0$ cualquiera. Elegimos un entero $n$ tan grande que $x_1=\dfrac1{\pi/2+2\pi n}<\delta$ y $x_2=\dfrac1{-\pi/2+2\pi n}<\delta$ (ambos son positivos y tienden a $0$ cuando $n$ crece). Entonces $x_1,x_2\in E^{*}(0,\delta)$ y

$$
\operatorname{sen}\frac1{x_1}=\operatorname{sen}\left(\frac\pi2+2\pi n\right)=1,\qquad\operatorname{sen}\frac1{x_2}=\operatorname{sen}\left(-\frac\pi2+2\pi n\right)=-1 .
$$

La definición exigiría $\lvert1-L\rvert<1$ y $\lvert-1-L\rvert<1$, y entonces $2=\lvert 1-(-1)\rvert\le\lvert1-L\rvert+\lvert L+1\rvert<2$, absurdo. Luego ningún $L$ es el límite. $\blacksquare$

**Resultado.** $\lim_{x\to0}\operatorname{sen}\frac1x$ no existe: ni siquiera existen los laterales, porque la función oscila entre $-1$ y $1$ infinitas veces.

</details>

## Autoevaluación

1. Si $\lim_{x\to a^{-}}f=3$ y $\lim_{x\to a^{+}}f=3$ pero $f(a)=5$, ¿existe $\lim_{x\to a}f$?

<details>
<summary>Respuesta</summary>

Sí, vale $3$. Que $f(a)=5$ solo indica que $f$ no es continua en $a$.

</details>

2. Si $\lim_{x\to a}f(x)=L>0$, ¿puede ser $f(x)<0$ en puntos arbitrariamente cercanos a $a$?

<details>
<summary>Respuesta</summary>

No: por la conservación del signo, $f>0$ en algún entorno reducido de $a$.

</details>

3. ¿Se puede calcular $\lim_{x\to0}\frac{x^2+x}{x}$ con la propiedad del cociente?

<details>
<summary>Respuesta</summary>

No: el denominador tiende a $0$. Se simplifica $\frac{x(x+1)}{x}=x+1$ (para $x\neq0$) y el límite es $1$.

</details>

:::tip[En resumen]
- $\lim_{x\to a}f=L$ si y solo si los dos laterales existen y valen $L$. Con laterales distintos, no hay límite.
- El límite, si existe, es único.
- El álgebra de límites requiere que los límites **existan** y, para el cociente, que el del denominador sea $\neq0$.
- Intercalación: $g\le f\le h$ con $\lim g=\lim h=L$ implica $\lim f=L$. Infinitésimo $\times$ acotada es infinitésimo.
- $\lim_{x\to0}\frac{\operatorname{sen}x}{x}=1$.
:::

## Para seguir

Con estas herramientas ya podés comparar cantidades que tienden a cero: [Infinitésimos](/analisis-matematico-i/unidad-2/teoria/infinitesimos/).
