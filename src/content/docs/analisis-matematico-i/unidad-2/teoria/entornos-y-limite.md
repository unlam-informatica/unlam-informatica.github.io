---
title: Entornos y límite finito
description: Distancia, entorno y entorno reducido, definición ε-δ del límite finito, su interpretación gráfica y cómo probar un límite con la definición.
slug: analisis-matematico-i/unidad-2/teoria/entornos-y-limite
sidebar:
  order: 1
---

## Qué vas a aprender

- Escribir entornos y entornos reducidos como intervalos y como desigualdades con valor absoluto.
- Enunciar e interpretar gráficamente la definición $\varepsilon$-$\delta$ de límite finito.
- Probar con la definición límites de funciones lineales, cuadráticas y con raíz, hallando $\delta$ en función de $\varepsilon$.

**Antes de empezar.** Necesitás manejar el valor absoluto y las desigualdades con módulo, y la notación de intervalos y funciones de la [Unidad 1](/analisis-matematico-i/unidad-1/teoria/unidad-1/).

## Para qué sirve: «cerca de»

Queremos estudiar qué hace una función $f$ **cerca** de un punto $a$, aunque en $a$ la función no esté definida o valga otra cosa. «Cerca» hay que volverlo preciso: eso es un entorno. Y «se acerca a $L$» también: eso es la definición con $\varepsilon$ y $\delta$.

Un ejemplo. La función $f(x)=\dfrac{x^2-9}{x-3}$ no está definida en $x=3$. Veamos sus valores cerca de ese punto:

<!-- check: U2.T.LIM.1 -->

| $x$ | $2{,}9$ | $2{,}99$ | $2{,}999$ | $3$ | $3{,}001$ | $3{,}01$ | $3{,}1$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $5{,}9$ | $5{,}99$ | $5{,}999$ | no existe | $6{,}001$ | $6{,}01$ | $6{,}1$ |

Para $x\neq 3$ vale $f(x)=x+3$, así que los valores se acercan a $6$ desde ambos lados. Decimos que **el límite de $f$ cuando $x$ tiende a $3$ es $6$**, aunque $f(3)$ no exista. La tabla da una idea; la definición que sigue da la certeza.

## Distancia y entorno

:::note[Definición · Distancia]
La **distancia** entre dos números reales $a$ y $b$ es $d(a,b)=\lvert a-b\rvert$.
:::

:::note[Definición · Entorno y entorno reducido]
Sean $a\in\mathbb{R}$ y $r>0$.

- El **entorno** de centro $a$ y radio $r$ es
  $E(a,r)=\{x\in\mathbb{R} : \lvert x-a\rvert<r\}=(a-r,\ a+r)$.
- El **entorno reducido** de centro $a$ y radio $r$ es
  $E^{*}(a,r)=E(a,r)-\{a\}=\{x\in\mathbb{R} : 0<\lvert x-a\rvert<r\}=(a-r,a)\cup(a,a+r)$.
:::

El entorno reducido deja afuera el centro. Esa exclusión es el corazón de la idea de límite: **importa lo que pasa cerca de $a$, no lo que pasa en $a$**.

### Ejemplos

<!-- check: U2.T.ENT.1 -->

1. $\lvert x-3\rvert<2$ describe $E(3,2)=(1,5)$.
2. $0<\lvert x+1\rvert<\tfrac12$ describe $E^{*}(-1,\tfrac12)=(-\tfrac32,-1)\cup(-1,-\tfrac12)$.
3. $\lvert 2x-3\rvert<1$: dividiendo por $2$ queda $\lvert x-\tfrac32\rvert<\tfrac12$, es decir $E(\tfrac32,\tfrac12)=(1,2)$.

<!-- check: U2.T.ENT.2 -->

Al revés, un intervalo abierto $(p,q)$ es un entorno con centro en el punto medio $\frac{p+q}{2}$ y radio $\frac{q-p}{2}$. Por ejemplo, $(-4,6)$ es $E(1,5)$ y $(-\tfrac52,\tfrac72)$ es $E(\tfrac12,3)$. Un intervalo como $(2,9]$ **no** es un entorno de ningún punto: incluye un extremo.

## Definición de límite finito

:::note[Definición · Límite finito]
Sea $f$ definida en un entorno reducido de $a$ (en $a$ puede estar o no definida) y sea $L\in\mathbb{R}$. Se dice que

$$
\lim_{x\to a} f(x)=L
$$

si para todo $\varepsilon>0$ existe $\delta>0$ (que depende de $\varepsilon$) tal que

$$
0<\lvert x-a\rvert<\delta\ \Longrightarrow\ \lvert f(x)-L\rvert<\varepsilon .
$$

Con entornos: $x\in E^{*}(a,\delta)\Rightarrow f(x)\in E(L,\varepsilon)$.
:::

Leída con calma, es un **desafío con respuesta**. Alguien elige una tolerancia $\varepsilon>0$ tan chica como quiera (qué tan cerca de $L$ quiere ver los valores de $f$). Nosotros tenemos que contestar con un $\delta>0$ (qué tan cerca de $a$ hay que tomar a $x$) que cumpla la tolerancia. Si siempre podemos responder, el límite es $L$.

### Interpretación gráfica

![Gráfico de f(x) = x²/2 cerca de x = 2 con una banda horizontal de radio ε alrededor de L = 2 y una banda vertical de radio δ alrededor de a = 2; la curva dentro de la banda vertical queda dentro de la banda horizontal](/analisis-matematico-i/figuras/u2-banda-epsilon-delta.svg)

*Qué observar: elegimos la banda horizontal (los valores de $f$ a menos de $\varepsilon$ de $L$). Existe una banda vertical, de radio $\delta$ alrededor de $a$, tal que todo el trozo de curva que queda dentro de ella (salvo, a lo sumo, el punto central) está dentro de la banda horizontal. Si achicamos $\varepsilon$, hay que achicar $\delta$.*

Tres observaciones que conviene tener claras:

- **$\delta$ no es único.** Si un $\delta$ funciona, cualquier $\delta'$ menor también. Basta encontrar uno.
- **$\delta$ depende de $\varepsilon$** (y, en general, del punto $a$): a menor tolerancia, menor $\delta$.
- **$f(a)$ no interviene**: $0<\lvert x-a\rvert$ excluye $x=a$. Dos funciones que difieren solo en $a$ tienen el mismo límite en $a$.

:::note[Cuándo tiene sentido]
Para hablar de $\lim_{x\to a}f(x)$ hace falta que $a$ sea **punto de acumulación** del dominio: que todo entorno reducido de $a$ contenga puntos del dominio. En $x=a$ la función puede no estar definida, pero tiene que estar definida «alrededor».
:::

## Cómo probar un límite con la definición

Receta para demostrar $\lim_{x\to a}f(x)=L$:

1. Tomar $\varepsilon>0$ arbitrario.
2. Partir de $\lvert f(x)-L\rvert$ y **acotarlo** por algo de la forma $K\cdot\lvert x-a\rvert$, con $K$ una constante (o una cota válida en un entorno de $a$).
3. Elegir $\delta$ en función de $\varepsilon$ para que $K\lvert x-a\rvert<\varepsilon$.
4. Verificar que, con ese $\delta$, la implicación de la definición se cumple.

### Ejemplo 1 · Una función lineal

<!-- check: U2.T.LIM.2 -->

Probar que $\displaystyle\lim_{x\to 3}(3x-2)=7$.

Sea $\varepsilon>0$. Calculamos

$$
\lvert (3x-2)-7\rvert=\lvert 3x-9\rvert=3\,\lvert x-3\rvert .
$$

Queremos $3\lvert x-3\rvert<\varepsilon$, o sea $\lvert x-3\rvert<\varepsilon/3$. Tomamos $\delta=\varepsilon/3$: si $0<\lvert x-3\rvert<\delta$, entonces $\lvert f(x)-7\rvert=3\lvert x-3\rvert<3\delta=\varepsilon$. $\blacksquare$

Con $\varepsilon=0{,}01$ resulta $\delta=\tfrac1{300}$: en $x=3\pm\tfrac1{300}$ la función vale justo $7\pm0{,}01$, el borde de la tolerancia.

### Ejemplo 2 · Una función cuadrática: acotar el factor extra

<!-- check: U2.T.LIM.3 -->

Probar que $\displaystyle\lim_{x\to 2}x^2=4$.

Sea $\varepsilon>0$. Ahora

$$
\lvert x^2-4\rvert=\lvert x-2\rvert\,\lvert x+2\rvert .
$$

El factor $\lvert x+2\rvert$ no es constante, pero se puede acotar cerca de $2$. **Primero pedimos $\delta\le 1$**: entonces $1<x<3$, de modo que $3<x+2<5$ y $\lvert x+2\rvert<5$. Con eso,

$$
\lvert x^2-4\rvert<5\,\lvert x-2\rvert .
$$

Para que sea menor que $\varepsilon$ alcanza $\lvert x-2\rvert<\varepsilon/5$. Las dos exigencias se cumplen a la vez con

$$
\delta=\min\left\{1,\ \frac{\varepsilon}{5}\right\}.
$$

Si $0<\lvert x-2\rvert<\delta$, entonces $\lvert x+2\rvert<5$ y $\lvert x-2\rvert<\varepsilon/5$, y el producto es menor que $\varepsilon$. $\blacksquare$

Con $\varepsilon=\tfrac12$ sale $\delta=\tfrac1{10}$ y en los bordes $f(1{,}9)=3{,}61$ y $f(2{,}1)=4{,}41$ distan menos de $\tfrac12$ de $4$.

### Ejemplo 3 · El punto excluido no importa

<!-- check: U2.T.LIM.4 -->

Probar que $\displaystyle\lim_{x\to 3}\frac{x^2-9}{x-3}=6$.

Para $x\neq3$ vale $\dfrac{x^2-9}{x-3}=x+3$. Entonces $\lvert f(x)-6\rvert=\lvert x+3-6\rvert=\lvert x-3\rvert$. Con $\delta=\varepsilon$: si $0<\lvert x-3\rvert<\delta$, resulta $\lvert f(x)-6\rvert<\varepsilon$. $\blacksquare$

La simplificación fue legítima porque $x\neq3$ en el entorno **reducido**. Es exactamente lo que confirma la tabla del comienzo.

### Ejemplo 4 · Una raíz

<!-- check: U2.T.LIM.5 -->

Probar que $\displaystyle\lim_{x\to 4}\sqrt{x}=2$.

Para $x\ge0$, multiplicamos y dividimos por el conjugado:

$$
\lvert\sqrt{x}-2\rvert=\frac{\lvert x-4\rvert}{\sqrt{x}+2}\le\frac{\lvert x-4\rvert}{2},
$$

porque $\sqrt{x}+2\ge2$. Queremos $\frac{\lvert x-4\rvert}{2}<\varepsilon$, o sea $\lvert x-4\rvert<2\varepsilon$. Además $x$ tiene que estar en el dominio ($x\ge0$), lo que se asegura con $\delta\le4$. Tomamos $\delta=\min\{4,\ 2\varepsilon\}$. $\blacksquare$

### Ejemplo 5 · Un límite que no existe

<!-- check: U2.T.LIM.6 -->

Probar con la definición que $f(x)=\dfrac{\lvert x\rvert}{x}$ **no** tiene límite en $x=0$.

Para $x>0$ vale $f(x)=1$ y para $x<0$ vale $f(x)=-1$. Supongamos que el límite fuera un número $L$ y tomemos $\varepsilon=1$. Para cualquier $\delta>0$ hay puntos de $E^{*}(0,\delta)$ de ambos signos, así que tendrían que cumplirse $\lvert 1-L\rvert<1$ y $\lvert -1-L\rvert<1$. Pero entonces

$$
2=\lvert 1-(-1)\rvert\le\lvert 1-L\rvert+\lvert L-(-1)\rvert<1+1=2,
$$

una contradicción. Ningún $L$ sirve. $\blacksquare$

Para mostrar que un límite **no es** $L$ hay que encontrar **un** $\varepsilon$ para el cual **ningún** $\delta$ alcance: es la negación de la definición ($\exists\varepsilon\ \forall\delta\ \exists x\ldots$).

:::caution[Errores frecuentes]
- **Pensar que $\delta$ es único o que hay que hallar «el mejor».** Cualquier $\delta$ válido alcanza, y uno menor también sirve.
- **Elegir $\delta$ sin haber acotado los factores extra.** En el ejemplo 2, $\delta=\varepsilon/\lvert x+2\rvert$ no es válido: $\delta$ no puede depender de $x$.
- **Olvidar el entorno reducido.** Si se incluyera $x=a$, no se podría simplificar en el ejemplo 3, y el valor $f(a)$ (si existe) importaría.
- **Confundir $\varepsilon$ y $\delta$.** $\varepsilon$ mide la cercanía de los valores de $f$; $\delta$, la de los valores de $x$.
- **Creer que la tabla demuestra el límite.** Una tabla sugiere un valor; solo la definición (o las propiedades demostradas con ella) lo prueban.
:::

## Ejercicios

Para explorar la definición con un deslizador de $\varepsilon$, mirá la guía de [GeoGebra para límites y continuidad](/analisis-matematico-i/geogebra/limites-continuidad/).

### Ejercicio 1 · Entornos como intervalos
<!-- ejercicio: U2.01 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
a) Escribí $E(-2,\tfrac32)$ como intervalo y como desigualdad con valor absoluto.

b) Hallá el centro y el radio de los entornos $\left(-\tfrac52,\ \tfrac72\right)$ y $(-5,\,3)$.

c) Resolvé $\lvert 3x+1\rvert<5$ y expresá el conjunto como un entorno.

d) Escribí $E^{*}(4,\tfrac15)$ como unión de intervalos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un entorno $E(a,r)$ es $(a-r,a+r)$; al revés, el centro es el punto medio y el radio, la mitad de la longitud.

**Desarrollo.**

a) $E(-2,\tfrac32)=(-2-\tfrac32,\ -2+\tfrac32)=(-\tfrac72,-\tfrac12)$, que es $\lvert x+2\rvert<\tfrac32$.

b) Para $(-\tfrac52,\tfrac72)$: centro $\tfrac{-5/2+7/2}{2}=\tfrac12$, radio $\tfrac{7/2-(-5/2)}{2}=3$. Para $(-5,3)$: centro $-1$, radio $4$.

c) $\lvert 3x+1\rvert<5\iff-5<3x+1<5\iff-6<3x<4\iff-2<x<\tfrac43$. El intervalo $(-2,\tfrac43)$ tiene centro $-\tfrac13$ y radio $\tfrac53$: es $E(-\tfrac13,\tfrac53)$. (Equivale a $\lvert x+\tfrac13\rvert<\tfrac53$.)

d) $E^{*}(4,\tfrac15)=(\tfrac{19}{5},4)\cup(4,\tfrac{21}{5})$.

**Resultado.** a) $(-\tfrac72,-\tfrac12)$; b) $E(\tfrac12,3)$ y $E(-1,4)$; c) $(-2,\tfrac43)=E(-\tfrac13,\tfrac53)$; d) $(\tfrac{19}5,4)\cup(4,\tfrac{21}5)$.

</details>

### Ejercicio 2 · Hallar δ en una función lineal
<!-- ejercicio: U2.02 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $\displaystyle\lim_{x\to3}(5-2x)=-1$:

a) Hallá $\delta$ en función de $\varepsilon$ y demostrá el límite con la definición.

b) Para $\varepsilon=0{,}02$, calculá $\delta$ y comprobá que los puntos $3\pm\delta$ dan valores de $f$ a distancia exactamente $\varepsilon$ de $L$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Acotar $\lvert f(x)-L\rvert$ por una constante por $\lvert x-3\rvert$.

**Desarrollo.**

a) $\lvert(5-2x)-(-1)\rvert=\lvert6-2x\rvert=2\lvert x-3\rvert$. Para que sea menor que $\varepsilon$ alcanza $\lvert x-3\rvert<\varepsilon/2$. Tomamos $\delta=\varepsilon/2$: si $0<\lvert x-3\rvert<\delta$, entonces $\lvert f(x)+1\rvert=2\lvert x-3\rvert<2\delta=\varepsilon$.

b) Con $\varepsilon=0{,}02$, $\delta=0{,}01$. Entonces $f(3{,}01)=5-6{,}02=-1{,}02$ y $f(2{,}99)=5-5{,}98=-0{,}98$. Ambos distan $0{,}02$ de $-1$: son los bordes (excluidos) de la banda.

**Resultado.** $\delta=\varepsilon/2$; para $\varepsilon=0{,}02$, $\delta=0{,}01$.

</details>

### Ejercicio 3 · Límite cuadrático con la definición
<!-- ejercicio: U2.03 | nivel: intermedio | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Demostrá con la definición que $\displaystyle\lim_{x\to-1}x^2=1$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Factorizar $x^2-1$ y acotar el factor que no es constante pidiendo $\delta\le1$.

**Desarrollo.** Sea $\varepsilon>0$. Vale $\lvert x^2-1\rvert=\lvert x-1\rvert\,\lvert x+1\rvert$. Si $\delta\le1$ y $0<\lvert x+1\rvert<\delta$, entonces $-2<x<0$, de donde $-3<x-1<-1$ y $\lvert x-1\rvert<3$. Luego $\lvert x^2-1\rvert<3\lvert x+1\rvert$, que es menor que $\varepsilon$ si $\lvert x+1\rvert<\varepsilon/3$. Tomamos

$$
\delta=\min\left\{1,\ \frac{\varepsilon}{3}\right\}
$$

y se cumple la implicación de la definición. $\blacksquare$

**Resultado.** $\lim_{x\to-1}x^2=1$ con $\delta=\min\{1,\varepsilon/3\}$.

</details>

### Ejercicio 4 · Límite de un cociente con la definición
<!-- ejercicio: U2.04 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Demostrá con la definición que $\displaystyle\lim_{x\to2}\frac1x=\frac12$. Pista: acotá $\dfrac1{\lvert x\rvert}$ en un entorno de $2$ de radio menor que $2$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Llevar $\lvert f(x)-L\rvert$ a la forma $\lvert x-2\rvert$ por un factor y acotar ese factor lejos de $x=0$, donde $f$ no está definida.

**Desarrollo.** Sea $\varepsilon>0$. Entonces

$$
\left\lvert\frac1x-\frac12\right\rvert=\left\lvert\frac{2-x}{2x}\right\rvert=\frac{\lvert x-2\rvert}{2\lvert x\rvert}.
$$

Si pedimos $\delta\le1$, resulta $1<x<3$; en particular $x>1$ y $\dfrac1{2\lvert x\rvert}<\dfrac12$. Entonces $\left\lvert\dfrac1x-\dfrac12\right\rvert<\dfrac{\lvert x-2\rvert}{2}$, que es menor que $\varepsilon$ si $\lvert x-2\rvert<2\varepsilon$. Tomamos

$$
\delta=\min\{1,\ 2\varepsilon\}.
$$

Con ese $\delta$, $0<\lvert x-2\rvert<\delta$ implica $x>1$ (así $x\neq0$ y $f$ está definida) y $\lvert f(x)-\tfrac12\rvert<\varepsilon$. $\blacksquare$

**Resultado.** $\lim_{x\to2}\frac1x=\frac12$ con $\delta=\min\{1,2\varepsilon\}$. La cota $\delta\le1$ no es un adorno: impide que el entorno llegue a $x=0$, donde $1/x$ explota.

</details>

## Autoevaluación

1. ¿Es cierto que si $f(a)$ no existe entonces $\lim_{x\to a}f(x)$ no existe?

<details>
<summary>Respuesta</summary>

No. El límite solo mira $E^{*}(a,\delta)$. Por ejemplo $\frac{x^2-9}{x-3}$ no está definida en $3$ y su límite en $3$ es $6$.

</details>

2. Si para $\varepsilon=0{,}1$ un $\delta=0{,}05$ funciona, ¿funciona $\delta=0{,}01$? ¿Y $\delta=0{,}2$?

<details>
<summary>Respuesta</summary>

$\delta=0{,}01$ sí (un entorno más chico dentro del anterior). Para $\delta=0{,}2$ no se puede asegurar: puede salirse de la banda.

</details>

3. ¿Por qué en el ejemplo 2 pedimos $\delta\le1$?

<details>
<summary>Respuesta</summary>

Para poder acotar el factor $\lvert x+2\rvert$ por una constante ($5$). Sin esa cota, $\delta$ tendría que depender de $x$.

</details>

:::tip[En resumen]
- $E(a,r)=(a-r,a+r)$ y $E^{*}(a,r)=E(a,r)-\{a\}$.
- $\lim_{x\to a}f(x)=L$ si $\forall\varepsilon>0\ \exists\delta>0:\ 0<\lvert x-a\rvert<\delta\Rightarrow\lvert f(x)-L\rvert<\varepsilon$.
- El valor $f(a)$ no interviene; el entorno es reducido.
- Para probar un límite: acotar $\lvert f(x)-L\rvert$ por $K\lvert x-a\rvert$ (pidiendo, si hace falta, $\delta\le1$) y elegir $\delta=\min\{1,\varepsilon/K\}$.
- Para refutar un límite: encontrar un $\varepsilon$ para el que ningún $\delta$ sirva.
:::

## Para seguir

La definición no sirve para calcular límites complicados: para eso están los límites laterales, el álgebra de límites y el teorema de intercalación de la lección siguiente, [Límites laterales y propiedades](/analisis-matematico-i/unidad-2/teoria/limites-laterales-y-propiedades/).

## Bibliografía

Stewart (*Cálculo. Trascendentes tempranas*), Thomas (*Cálculo. Una variable*) y Purcell (*Cálculo diferencial e integral*) desarrollan la definición $\varepsilon$-$\delta$; en cada uno, el capítulo de límites.
