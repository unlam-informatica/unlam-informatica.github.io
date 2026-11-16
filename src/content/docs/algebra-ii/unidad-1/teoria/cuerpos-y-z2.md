---
title: Cuerpos y ℤ₂
description: Estructura de cuerpo, ejemplos y no ejemplos, el cuerpo de dos elementos ℤ₂ con la aritmética de bits y los cuerpos ℤₚ con p primo.
slug: algebra-ii/unidad-1/teoria/cuerpos-y-z2
sidebar:
  order: 1
  label: 1.1 Cuerpos y ℤ₂
---

## Para qué sirve

Un espacio vectorial combina dos clases de objetos: los **vectores**, que se suman entre sí, y los
**escalares**, que multiplican a los vectores. Antes de definir espacio vectorial necesitamos fijar qué
le pedimos al conjunto de escalares. En Álgebra y Geometría Analítica I los escalares fueron siempre
números reales y nunca hizo falta preguntarse por qué la eliminación gaussiana funciona: dividimos por
un pivote no nulo, restamos filas, despejamos. Todo eso depende de unas pocas reglas de cálculo que los
reales cumplen.

En informática aparece otro conjunto de escalares con el que esas mismas reglas siguen valiendo: el de
los **bits**, $\{0,1\}$, con la suma "o exclusivo" y el producto "y". Con él se describen palabras
binarias, bits de paridad, sumas de verificación y los códigos detectores y correctores de errores de
esta unidad. La noción de **cuerpo** reúne las reglas que necesitamos para que toda el álgebra lineal
(sistemas, determinantes, inversas, bases) funcione igual con números reales que con bits.

## La idea: sumar, restar, multiplicar y dividir sin salir del conjunto

Para resolver $ax=b$ con $a\neq 0$ en $\mathbb{R}$ multiplicamos ambos miembros por $a^{-1}$. En los
enteros esto falla: $2x=1$ no tiene solución en $\mathbb{Z}$, porque $2$ no tiene inverso entero. Un
cuerpo es, informalmente, un conjunto en el que las cuatro operaciones (con la división restringida a
divisores no nulos) dan siempre resultados dentro del conjunto y respetan las propiedades usuales.

:::note[Definición (cuerpo)]
Un **cuerpo** (o campo de escalares) es una terna $(K,+,\cdot)$ formada por un conjunto $K$ y dos
operaciones, suma y producto, tales que:

**Para la suma, en $(K,+)$:**

1. Cierre: $a+b\in K$ para todo $a,b\in K$.
2. Asociativa: $(a+b)+c=a+(b+c)$.
3. Neutro: existe $0\in K$ con $a+0=a$ para todo $a$.
4. Opuesto: para cada $a$ existe $-a\in K$ con $a+(-a)=0$.
5. Conmutativa: $a+b=b+a$.

**Para el producto, en $(K\setminus\{0\},\cdot)$:**

6. Cierre: si $a\neq 0$ y $b\neq 0$, entonces $ab\in K$ y $ab\neq 0$.
7. Asociativa: $(ab)c=a(bc)$.
8. Neutro: existe $1\in K\setminus\{0\}$ con $1\cdot a=a$ para todo $a$.
9. Inverso: para cada $a\neq 0$ existe $a^{-1}\in K$ con $a\,a^{-1}=1$.
10. Conmutativa: $ab=ba$.

**Distributiva:** $a(b+c)=ab+ac$ para todo $a,b,c\in K$.
:::

Cuando las operaciones están claras escribimos simplemente $K$. Dos observaciones sobre la definición:

- Como el neutro del producto vive en $K\setminus\{0\}$, en todo cuerpo vale $1\neq 0$; en particular,
  un cuerpo tiene al menos dos elementos.
- La condición 6 dice algo más fuerte que "el producto no se sale de $K$": el producto de dos elementos
  no nulos **no puede dar cero**. Esa condición es la que fallará en $\mathbb{Z}_4$.

La resta y la división se definen a partir de opuestos e inversos: $a-b=a+(-b)$ y, si $b\neq 0$,
$\dfrac{a}{b}=a\,b^{-1}$.

### Consecuencias de los axiomas

:::note[Propiedad]
En todo cuerpo $K$, para $a,b\in K$:

1. $a\cdot 0=0$.
2. Si $ab=0$, entonces $a=0$ o $b=0$.
3. Si $a\neq 0$, la ecuación $ax=b$ tiene una única solución en $K$, que es $x=a^{-1}b$.
:::

**Demostración.**

1. Por neutro y distributiva, $a\cdot 0=a(0+0)=a\cdot 0+a\cdot 0$. Sumando a ambos miembros el opuesto
   de $a\cdot 0$ queda $0=a\cdot 0$.
2. Supongamos $ab=0$ y $a\neq 0$. Entonces
   $b=1\cdot b=(a^{-1}a)\,b=a^{-1}(ab)=a^{-1}\cdot 0=0$, usando el ítem anterior.
3. Existencia: $a(a^{-1}b)=(aa^{-1})b=1\cdot b=b$. Unicidad: si $ax=b$ y $ax'=b$, restando,
   $a(x-x')=0$; como $a\neq 0$, el ítem 2 da $x-x'=0$, es decir, $x=x'$. $\blacksquare$

El ítem 3 es la justificación de cada despeje que hacemos al resolver un sistema lineal: dividir por un
pivote no nulo es multiplicar por su inverso, y el resultado no depende del camino elegido.

## Ejemplos: ℚ, ℝ y ℂ

- **Los racionales** $\mathbb{Q}$. La suma y el producto de fracciones son fracciones:
  $\dfrac{a}{b}+\dfrac{c}{d}=\dfrac{ad+bc}{bd}$ y $\dfrac{a}{b}\cdot\dfrac{c}{d}=\dfrac{ac}{bd}$. El inverso
  de $\dfrac{a}{b}\neq 0$ es $\dfrac{b}{a}$. Las propiedades asociativas, conmutativas y la distributiva
  se heredan de los enteros.
- **Los reales** $\mathbb{R}$, el cuerpo con el que trabajamos en Álgebra I y en Análisis Matemático.
- **Los complejos** $\mathbb{C}=\{a+bi : a,b\in\mathbb{R}\}$, con $i^2=-1$ y las operaciones usuales.

En $\mathbb{C}$ el único axioma que requiere una cuenta es el inverso: si $z=a+bi\neq 0$, entonces
$a^2+b^2>0$ y

$$
z^{-1}=\frac{a-bi}{a^2+b^2},\qquad\text{pues}\qquad (a+bi)(a-bi)=a^2+b^2 .
$$

Por ejemplo, $(3+4i)^{-1}=\dfrac{3-4i}{25}$, ya que $(3+4i)(3-4i)=9+16=25$.

Los tres cumplen $\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$ con las mismas operaciones: cada uno es un
**subcuerpo** del siguiente.

## No ejemplos: ℕ, ℤ y otros

Para mostrar que un conjunto con dos operaciones **no** es cuerpo alcanza con señalar un axioma que
falla y exhibir un testigo concreto.

| Conjunto con sus operaciones usuales | Axioma que falla | Testigo |
|---|---|---|
| $\mathbb{N}=\{1,2,3,\dots\}$ | neutro de la suma (y opuestos) | $0\notin\mathbb{N}$; $1+x=0$ no tiene solución en $\mathbb{N}$ |
| $\mathbb{N}_0=\{0,1,2,\dots\}$ | opuesto | $1+x=0$ no tiene solución en $\mathbb{N}_0$ |
| $\mathbb{Z}$ | inverso del producto | $2x=1$ no tiene solución entera |
| $\{x\in\mathbb{R}: x\ge 0\}$ | opuesto | $1+x=0$ exige $x=-1<0$ |
| matrices reales $2\times 2$ con suma y producto de matrices | conmutativa, cierre de los no nulos e inverso | la matriz $E$ de abajo cumple $E\neq 0$ y $E^2=0$ |

Para la última fila,

$$
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad E^2=\begin{pmatrix}0&0\\0&0\end{pmatrix},
$$

y $E$ no puede tener inversa: si $XE=I$, multiplicando por $E$ a derecha quedaría $XE^2=IE$, es
decir, $0=E$, absurdo.

En $\mathbb{Z}$ solo $1$ y $-1$ tienen inverso. Ese es el motivo por el que los sistemas con
coeficientes enteros suelen tener soluciones fraccionarias: la eliminación gaussiana necesita dividir,
y para dividir hace falta un cuerpo.

## El cuerpo ℤ₂

Llamamos $\mathbb{Z}_2=\{0,1\}$ al conjunto de dos elementos con las operaciones definidas por las tablas

| $+$ | $0$ | $1$ |
|---|---|---|
| $0$ | $0$ | $1$ |
| $1$ | $1$ | $0$ |

| $\cdot$ | $0$ | $1$ |
|---|---|---|
| $0$ | $0$ | $0$ |
| $1$ | $0$ | $1$ |

En algunos libros aparece con los nombres $\mathbb{F}_2$ o GF(2); en esta materia escribimos
$\mathbb{Z}_2$. Hay tres maneras equivalentes de leer las tablas:

- **Como paridades.** $0$ representa "par" y $1$ "impar": impar más impar es par ($1+1=0$), impar por
  impar es impar ($1\cdot 1=1$). Es decir, $\mathbb{Z}_2$ son los restos de la división por $2$ y las
  operaciones son "operar en $\mathbb{Z}$ y quedarse con el resto".
- **Como lógica.** La suma es el **o exclusivo** (XOR): vale $1$ cuando exactamente uno de los sumandos
  es $1$. El producto es el **y** (AND): vale $1$ solo cuando ambos factores son $1$.
- **Como bits.** Un bit se invierte al sumarle $1$ ($0+1=1$, $1+1=0$) y queda igual al sumarle $0$.

:::note[Teorema]
$(\mathbb{Z}_2,+,\cdot)$ es un cuerpo. Además, en $\mathbb{Z}_2$ vale $-1=1$ y $a+a=0$ para todo $a$.
:::

**Demostración.** El cierre se lee en las tablas: solo aparecen $0$ y $1$, y el único producto de
elementos no nulos, $1\cdot 1$, da $1\neq 0$. Ambas tablas son simétricas, así que las dos operaciones
son conmutativas. La fila del $0$ en la tabla de la suma muestra que $0$ es neutro, y $1\cdot 1=1$
muestra que $1$ es neutro del producto en $\mathbb{Z}_2\setminus\{0\}=\{1\}$. Opuestos: $0+0=0$ y
$1+1=0$, así que $-0=0$ y $-1=1$. Inverso: el único elemento no nulo es $1$ y $1^{-1}=1$.

Quedan la asociatividad y la distributiva. Pueden verificarse caso por caso ($2^3=8$ ternas para
cada propiedad), pero hay un argumento mejor: cada operación de $\mathbb{Z}_2$ consiste en operar en
$\mathbb{Z}$ y tomar el resto módulo $2$, y el resto de una suma (o de un producto) solo depende de los
restos de los operandos. Por eso toda identidad entre sumas y productos que vale en $\mathbb{Z}$, como
$a(b+c)=ab+ac$, sigue valiendo después de reducir módulo $2$. Finalmente, $a+a=0$ se lee en la diagonal
de la tabla de la suma. $\blacksquare$

:::tip[Cómo se calcula en ℤ₂]
- **Restar es sumar**: como $-1=1$, $a-b=a+(-b)=a+b$.
- **$2=0$**: $1+1=0$, así que nunca se divide por $2$ y todo coeficiente par desaparece.
- **$a+b=0$ equivale a $a=b$**: sumando $b$ a ambos miembros.
- Más adelante, en $\mathbb{Z}_2^n$, estas reglas darán $v+v=0$ y $-v=v$ para todo vector $v$.
:::

### Aritmética de bits

Una palabra de $n$ bits es una $n$-upla de elementos de $\mathbb{Z}_2$. Sumarlas componente a componente
es aplicar XOR bit a bit:

$$
(1,0,1,1)+(0,1,1,0)=(1+0,\;0+1,\;1+1,\;1+0)=(1,1,0,1).
$$

En C, Java o Python, el operador `^` aplicado a enteros calcula ese XOR bit a bit y el operador `&`
calcula el AND. El **bit de paridad** de una palabra es la suma en $\mathbb{Z}_2$ de sus bits: para
$1011$ vale $1+0+1+1=1$, porque la palabra tiene una cantidad impar de unos. Agregar ese bit al final
produce una palabra con una cantidad par de unos; si durante una transmisión se invierte un solo bit,
la paridad deja de ser par y el error se detecta. Esta idea, formulada con subespacios de
$\mathbb{Z}_2^n$, es el punto de partida de la lección de
[códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/).

### Ejemplo 1 · Un sistema sobre ℤ₂ y el mismo sistema sobre ℝ
<!-- check: U1.T01.E1 -->

Resolver en $\mathbb{Z}_2$ y en $\mathbb{R}$ el sistema

$$
\begin{cases}
x+y=1\\
y+z=1\\
x+y+z=0
\end{cases}
$$

**En $\mathbb{Z}_2$.** Sumamos la primera ecuación a la tercera: $(x+y+z)+(x+y)=0+1$. Como $x+x=0$ e
$y+y=0$, queda $z=1$. De la segunda, $y=1-z=1+z=1+1=0$ (restar es sumar). De la primera,
$x=1+y=1+0=1$. La solución es única: $(x,y,z)=(1,0,1)$.

**En $\mathbb{R}$.** Restamos la primera ecuación de la tercera: $z=0-1=-1$. De la segunda,
$y=1-z=2$; de la primera, $x=1-y=-1$. La solución es $(x,y,z)=(-1,2,-1)$.

Comprobación: en $\mathbb{Z}_2$, $1+0=1$, $0+1=1$ y $1+0+1=0$; en $\mathbb{R}$, $-1+2=1$, $2-1=1$ y
$-1+2-1=0$.

Observemos que la solución real, reducida módulo $2$, da la solución en $\mathbb{Z}_2$:
$(-1,2,-1)\mapsto(1,0,1)$. Esto ocurre aquí porque la solución real es entera, pero **no** es una regla.
El sistema

$$
\begin{cases}
x+y=1\\
x-y=0
\end{cases}
$$

tiene en $\mathbb{R}$ la única solución $x=y=\tfrac12$, mientras que en $\mathbb{Z}_2$ la segunda ecuación
es $x+y=0$ (porque $-1=1$), que contradice a la primera: el sistema es **incompatible** en
$\mathbb{Z}_2$. La fracción $\tfrac12$ no tiene sentido en $\mathbb{Z}_2$ porque $2=0$ no tiene inverso.
Cada sistema se resuelve en su cuerpo, desde el principio.

## Los cuerpos ℤₚ

La construcción de $\mathbb{Z}_2$ se generaliza a cualquier $n\ge 2$: $\mathbb{Z}_n=\{0,1,\dots,n-1\}$ con
la suma y el producto de $\mathbb{Z}$ seguidos del resto de la división por $n$. Por ejemplo, en
$\mathbb{Z}_3$:

| $+$ | $0$ | $1$ | $2$ |
|---|---|---|---|
| $0$ | $0$ | $1$ | $2$ |
| $1$ | $1$ | $2$ | $0$ |
| $2$ | $2$ | $0$ | $1$ |

| $\cdot$ | $0$ | $1$ | $2$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $0$ |
| $1$ | $0$ | $1$ | $2$ |
| $2$ | $0$ | $2$ | $1$ |

En $\mathbb{Z}_3$, $-1=2$ (porque $1+2=0$) y $2^{-1}=2$ (porque $2\cdot 2=4$, cuyo resto es $1$). Por el
mismo argumento que en $\mathbb{Z}_2$, las propiedades asociativas, conmutativas y distributiva, los
neutros y los opuestos ($-a=n-a$ si $a\neq 0$) se heredan de $\mathbb{Z}$ para todo $n$. La pregunta es
cuándo existen los inversos.

:::note[Teorema]
Sea $n\ge 2$. $\mathbb{Z}_n$ es un cuerpo si y solo si $n$ es primo.
:::

**Demostración.** ($\Leftarrow$) Sea $p$ primo y $a\in\mathbb{Z}_p$, $a\neq 0$. Consideremos los $p$
productos $a\cdot 0,\ a\cdot 1,\ \dots,\ a\cdot(p-1)$ calculados en $\mathbb{Z}_p$. Son distintos entre
sí: si $a\cdot x$ y $a\cdot y$ tuvieran el mismo resto con $0\le y<x\le p-1$, entonces $p$ dividiría
a $a(x-y)$ en $\mathbb{Z}$. Por el lema de Euclides ($p$ primo divide a un producto solo si divide a
alguno de los factores), $p$ dividiría a $a$ o a $x-y$, y ninguno es posible porque $0<a<p$ y
$0<x-y<p$. Entonces los $p$ productos son exactamente los $p$ elementos de $\mathbb{Z}_p$, y alguno de
ellos es $1$: existe $x$ con $ax=1$. El mismo lema de Euclides da el cierre de los no nulos: si
$ab$ tuviera resto $0$, $p$ dividiría a $a$ o a $b$.

($\Rightarrow$) Si $n$ no es primo, $n=rs$ con $1<r<n$ y $1<s<n$. En $\mathbb{Z}_n$ los elementos $r$ y
$s$ son no nulos y $r\cdot s=0$, lo que viola el cierre del producto en $\mathbb{Z}_n\setminus\{0\}$.
Además $r$ no tiene inverso: si $xr=1$, entonces $s=1\cdot s=(xr)s=x(rs)=x\cdot 0=0$, absurdo. $\blacksquare$

### Ejemplo 2 · Inversos y una ecuación en ℤ₅
<!-- check: U1.T01.E2 -->

Hallar el inverso de cada elemento no nulo de $\mathbb{Z}_5$ y resolver $3x+4=1$ en $\mathbb{Z}_5$.

Buscamos, para cada $a\neq 0$, el $x$ con $ax$ de resto $1$ al dividir por $5$:

| $a$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|
| $a^{-1}$ | $1$ | $3$ | $2$ | $4$ |
| comprobación | $1\cdot 1=1$ | $2\cdot 3=6\equiv 1$ | $3\cdot 2=6\equiv 1$ | $4\cdot 4=16\equiv 1$ |

Para la ecuación, sumamos el opuesto de $4$, que es $-4=1$, a ambos miembros: $3x=1+1=2$. Multiplicamos
por $3^{-1}=2$: $x=2\cdot 2=4$.

Comprobación: $3\cdot 4+4=16$, cuyo resto al dividir por $5$ es $1$. Además, por la propiedad de
unicidad, $x=4$ es la **única** solución en $\mathbb{Z}_5$, lo que se confirma probando los cinco valores.

### Ejemplo 3 · ℤ₄ no es cuerpo
<!-- check: U1.T01.E3 -->

Construir la tabla del producto de $\mathbb{Z}_4$ y mostrar qué axiomas de cuerpo fallan.

| $\cdot$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| $0$ | $0$ | $0$ | $0$ | $0$ |
| $1$ | $0$ | $1$ | $2$ | $3$ |
| $2$ | $0$ | $2$ | $0$ | $2$ |
| $3$ | $0$ | $3$ | $2$ | $1$ |

- **Cierre de los no nulos:** $2\neq 0$ pero $2\cdot 2=4\equiv 0$.
- **Inverso:** la fila del $2$ solo contiene $0$ y $2$; nunca aparece el $1$, así que $2$ no tiene inverso.
  Los únicos elementos invertibles son $1$ y $3$ ($3\cdot 3=9\equiv 1$).
- **Consecuencias prácticas:** la ecuación $2x=1$ no tiene solución en $\mathbb{Z}_4$, y la ecuación
  $2x=0$ tiene **dos** soluciones, $x=0$ y $x=2$. Es decir, falla la propiedad de unicidad del despeje y
  no se puede "cancelar" el $2$ en $2x=2y$.

Comprobación: la tabla coincide con los restos de $ab$ módulo $4$, y basta recorrer la fila del $2$ para
confirmar las afirmaciones sobre $2x=1$ y $2x=0$.

Existe un cuerpo de cuatro elementos, pero no es $\mathbb{Z}_4$: se construye de otra manera (ver
"Para seguir").

:::caution[Errores frecuentes]
- **"En $\mathbb{Z}_2$, $1+1=2$."** El $2$ no es un elemento de $\mathbb{Z}_2$: $1+1=0$.
- **Resolver en $\mathbb{R}$ y reducir módulo $2$ al final.** Puede dar resultados sin sentido: el
  sistema $x+y=1$, $x-y=0$ tiene solución $\left(\tfrac12,\tfrac12\right)$ en $\mathbb{R}$ y es incompatible
  en $\mathbb{Z}_2$. Se resuelve en el cuerpo indicado desde el primer paso.
- **"$-1$ es negativo, así que no está en $\mathbb{Z}_2$."** En $\mathbb{Z}_2$, $-1$ es el opuesto de $1$,
  que es el propio $1$.
- **"Todo $\mathbb{Z}_n$ es cuerpo."** Solo cuando $n$ es primo; en $\mathbb{Z}_4$, $2\cdot 2=0$.
- **"$\mathbb{Z}$ es cuerpo porque es cerrado para la suma, la resta y el producto."** Falta la división:
  $2$ no tiene inverso entero.
:::

## Autoevaluación

**1.** Hallar el inverso de $2$ en $\mathbb{Z}_3$.

<details>
<summary>Respuesta</summary>

$2^{-1}=2$, porque $2\cdot 2=4\equiv 1$ módulo $3$.

</details>

**2.** Calcular en $\mathbb{Z}_2$: $1+1+1$ y $(1+1)\cdot 1$.

<details>
<summary>Respuesta</summary>

$1+1+1=(1+1)+1=0+1=1$ y $(1+1)\cdot 1=0\cdot 1=0$.

</details>

**3.** ¿Por qué $\mathbb{Z}_6$ no es cuerpo? Dar un testigo.

<details>
<summary>Respuesta</summary>

$6=2\cdot 3$ no es primo. Testigo: $2\cdot 3=6\equiv 0$ con $2\neq 0$ y $3\neq 0$. Además, $2$ no tiene
inverso: $2x$ solo toma los valores $0$, $2$ y $4$ en $\mathbb{Z}_6$.

</details>

**4.** Resolver $3x=5$ en $\mathbb{Z}_7$.

<details>
<summary>Respuesta</summary>

$3^{-1}=5$ porque $15\equiv 1$ módulo $7$. Entonces $x=5\cdot 5=25\equiv 4$. Comprobación:
$3\cdot 4=12\equiv 5$.

</details>

:::tip[En resumen]
- Un **cuerpo** $K$ es un conjunto con suma y producto en el que valen las propiedades usuales y todo
  elemento no nulo tiene inverso. En todo cuerpo, $ab=0$ implica $a=0$ o $b=0$, y $ax=b$ con $a\neq 0$
  tiene solución única.
- $\mathbb{Q}$, $\mathbb{R}$ y $\mathbb{C}$ son cuerpos; $\mathbb{N}$ y $\mathbb{Z}$ no lo son.
- $\mathbb{Z}_2=\{0,1\}$ es un cuerpo: la suma es XOR y el producto es AND. En $\mathbb{Z}_2$, $-1=1$,
  restar es sumar y $a+a=0$.
- $\mathbb{Z}_n$ es cuerpo si y solo si $n$ es primo. En $\mathbb{Z}_4$, $2\cdot 2=0$ y $2$ no tiene inverso.
- Un sistema lineal se resuelve en el cuerpo indicado: el resultado puede cambiar al cambiar de cuerpo.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 1.1, subsección "Vectores
  binarios y aritmética modular" (pp. 13–16): $\mathbb{Z}_2$, $\mathbb{Z}_2^n$ y la aritmética módulo $m$.
- Poole, 3.ª ed., sección 1.4, "Vectores código" (pp. 53–57): bit de paridad y dígitos de control.
- **Para seguir:** existen cuerpos finitos con $p^k$ elementos para todo primo $p$ y todo $k\ge 1$ (por
  ejemplo, uno de $4$ y uno de $256$ elementos); no son $\mathbb{Z}_{p^k}$. El de $256$ elementos se usa
  en el cifrado AES y en los códigos de Reed-Solomon. No forman parte del programa.

Lección siguiente: [espacios vectoriales](/algebra-ii/unidad-1/teoria/espacios-vectoriales/).
Repaso relacionado: [sistemas lineales](/algebra-ii/repaso/sistemas-lineales/).
