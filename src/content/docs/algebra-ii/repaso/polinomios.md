---
title: Polinomios
description: Grado, raíces y multiplicidad, teorema del resto, regla de Ruffini, criterio de Gauss, factorización en ℝ y polinomios de grado 3 como los que aparecen al buscar autovalores.
slug: algebra-ii/repaso/polinomios
sidebar:
  order: 4
  label: R.4 Polinomios
---

## Para qué sirve

En la Unidad 3 los autovalores de una matriz $A$ son las raíces del polinomio característico $p_A(\lambda)=\det(\lambda I-A)$, y la multiplicidad de cada raíz ($m_a(\lambda)$) decide, junto con otros datos, si $A$ es diagonalizable. Para matrices de $3\times3$ eso significa factorizar polinomios de grado 3 a mano, rápido y sin errores. Esta lección repasa las herramientas: teorema del resto, regla de Ruffini, búsqueda de raíces racionales, discriminante y la relación entre coeficientes y raíces. Además, los polinomios de grado $\le n$ forman el espacio vectorial $P_n[\mathbb{R}]$, que aparece como ejemplo en las Unidades 1 y 2.

## Grado, raíces y multiplicidad

Un **polinomio** con coeficientes reales en la variable $x$ es una expresión $p(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_1x+a_0$ con $a_i\in\mathbb{R}$. Si $a_n\neq0$, el **grado** de $p$ es $n$ y $a_n$ es el **coeficiente principal**; si $a_n=1$, $p$ es **mónico**. El polinomio nulo no tiene grado. El grado del producto es la suma de los grados.

Un número $a$ es **raíz** de $p$ si $p(a)=0$.

:::note[Teorema (algoritmo de división y teorema del resto)]
Dados $p$ y $d\neq0$, existen polinomios únicos $q$ (cociente) y $r$ (resto) con $p=d\,q+r$ y $r=0$ o $\operatorname{gr}(r)<\operatorname{gr}(d)$. En particular, al dividir $p(x)$ por $x-a$ el resto es el número $p(a)$:

$$
p(x)=(x-a)\,q(x)+p(a).
$$

En consecuencia, $a$ es raíz de $p$ si y solo si $x-a$ divide a $p$.
:::

**Demostración del teorema del resto.** Como $x-a$ tiene grado 1, el resto $r$ es una constante: $p(x)=(x-a)q(x)+r$. Evaluando en $x=a$ resulta $p(a)=0\cdot q(a)+r=r$. $\blacksquare$

:::note[Definición]
$a$ es raíz de **multiplicidad** $m$ de $p$ si $p(x)=(x-a)^m\,q(x)$ con $q(a)\neq0$. Si $m=1$ la raíz es **simple**; si $m=2$, **doble**; etc.
:::

Como cada raíz aporta un factor lineal, un polinomio de grado $n$ tiene **a lo sumo $n$ raíces reales contando multiplicidades**.

## Regla de Ruffini

Para dividir $p(x)=a_nx^n+\dots+a_0$ por $x-a$ se escriben los coeficientes (incluidos los nulos) y se repite: bajar el primero; multiplicarlo por $a$ y sumarlo al siguiente; multiplicar el resultado por $a$ y sumarlo al siguiente; y así hasta el final. Los números obtenidos son los coeficientes del cociente (de grado $n-1$) y el último es el resto, que por el teorema del resto vale $p(a)$.

### Ejemplo 1 · Ruffini, resto y factorización completa
<!-- check: R.T04.E1 -->

Sea $p(x)=x^3-2x^2-5x+6$.

**Resto de dividir por $x-2$.** Por el teorema del resto es $p(2)=8-8-10+6=-4$. Con Ruffini se obtiene lo mismo:

$$
\begin{array}{r|rrrr} & 1 & -2 & -5 & 6\\ 2 & & 2 & 0 & -10\\ \hline & 1 & 0 & -5 & -4\end{array}
$$

es decir, $p(x)=(x-2)(x^2-5)-4$.

**Factorización.** Si $p$ tiene una raíz entera, divide al término independiente $6$ (lo justificamos en la sección siguiente): las candidatas son $\pm1,\pm2,\pm3,\pm6$. Probamos $p(1)=1-2-5+6=0$: $1$ es raíz. Dividimos por $x-1$:

$$
\begin{array}{r|rrrr} & 1 & -2 & -5 & 6\\ 1 & & 1 & -1 & -6\\ \hline & 1 & -1 & -6 & 0\end{array}
$$

El cociente es $x^2-x-6$, cuyas raíces son $\frac{1\pm\sqrt{1+24}}{2}=\frac{1\pm5}{2}$, es decir $3$ y $-2$. Entonces

$$
p(x)=(x-1)(x-3)(x+2).
$$

**Comprobación.** $(x-3)(x+2)=x^2-x-6$ y $(x-1)(x^2-x-6)=x^3-x^2-6x-x^2+x+6=x^3-2x^2-5x+6$.

## Raíces racionales: criterio de Gauss

:::note[Teorema (criterio de Gauss)]
Sea $p(x)=a_nx^n+\dots+a_1x+a_0$ con coeficientes **enteros**, $a_n\neq0$ y $a_0\neq0$. Si $\frac{r}{s}$, con $r,s$ enteros coprimos, es raíz de $p$, entonces $r$ divide a $a_0$ y $s$ divide a $a_n$.
:::

**Demostración.** De $p(r/s)=0$, multiplicando por $s^n$: $a_nr^n+a_{n-1}r^{n-1}s+\dots+a_1rs^{n-1}+a_0s^n=0$. Todos los términos salvo $a_0s^n$ son múltiplos de $r$, así que $r$ divide a $a_0s^n$; como $r$ y $s$ son coprimos, $r$ divide a $a_0$. Análogamente, todos los términos salvo $a_nr^n$ son múltiplos de $s$, y $s$ divide a $a_n$. $\blacksquare$

Si $p$ es mónico ($a_n=1$), las raíces racionales son **enteras** y dividen a $a_0$. Este es el caso del polinomio característico $\det(\lambda I-A)$ de una matriz con elementos enteros. El criterio solo da candidatas; hay que probarlas. Y si ninguna funciona, el polinomio no tiene raíces racionales (puede tener irracionales).

### Ejemplo 2 · Raíz doble y raíces fraccionarias
<!-- check: R.T04.E2 -->

**(a)** Factorizamos $p(\lambda)=\lambda^3-5\lambda^2+8\lambda-4$. Es mónico: las candidatas son los divisores de $-4$, $\pm1,\pm2,\pm4$. $p(1)=1-5+8-4=0$. Por Ruffini con $1$ y luego, sobre el cociente, con $2$:

$$
\begin{array}{r|rrrr} & 1 & -5 & 8 & -4\\ 1 & & 1 & -4 & 4\\ \hline & 1 & -4 & 4 & 0\\ 2 & & 2 & -4 & \\ \hline & 1 & -2 & 0 & \end{array}
$$

El cociente $\lambda^2-4\lambda+4=(\lambda-2)^2$ tiene a $2$ como raíz doble. Entonces $p(\lambda)=(\lambda-1)(\lambda-2)^2$: $1$ es raíz simple y $2$ es raíz doble.

**(b)** Factorizamos $q(x)=2x^3-3x^2-3x+2$. Por el criterio de Gauss, $r$ divide a $2$ y $s$ divide a $2$: candidatas $\pm1,\pm2,\pm\frac12$. $q(-1)=-2-3+3+2=0$. Ruffini con $-1$:

$$
\begin{array}{r|rrrr} & 2 & -3 & -3 & 2\\ -1 & & -2 & 5 & -2\\ \hline & 2 & -5 & 2 & 0\end{array}
$$

El cociente $2x^2-5x+2$ tiene raíces $\frac{5\pm\sqrt{25-16}}{4}=\frac{5\pm3}{4}$, es decir $2$ y $\frac12$. Por lo tanto

$$
q(x)=2\,(x+1)\left(x-\tfrac12\right)(x-2)=(x+1)(2x-1)(x-2).
$$

**Comprobación.** En (a), la suma de raíces con multiplicidad es $1+2+2=5$ y el producto $1\cdot2\cdot2=4$, en acuerdo con las relaciones de la sección siguiente. En (b), $q\left(\frac12\right)=\frac14-\frac34-\frac32+2=0$.

## Factorización en ℝ

Para un polinomio de grado 2, $ax^2+bx+c$ con $a\neq0$, el **discriminante** $\Delta=b^2-4ac$ decide:

- $\Delta>0$: dos raíces reales distintas, $\frac{-b\pm\sqrt\Delta}{2a}$, y $ax^2+bx+c=a(x-x_1)(x-x_2)$;
- $\Delta=0$: una raíz doble $-\frac{b}{2a}$, y $ax^2+bx+c=a\left(x+\frac{b}{2a}\right)^2$;
- $\Delta<0$: ninguna raíz real; el polinomio es **irreducible** en $\mathbb{R}$ (sus raíces son complejas conjugadas).

:::note[Teorema (factorización en ℝ)]
Todo polinomio real de grado $n\geq1$ se escribe, de manera única salvo el orden, como su coeficiente principal por un producto de factores lineales mónicos $x-a$ y de factores cuadráticos mónicos irreducibles ($x^2+bx+c$ con $b^2-4c<0$).
:::

En Álgebra II trabajamos con autovalores **reales**: si el polinomio característico tiene un factor cuadrático irreducible, esas raíces no son autovalores reales, y eso ya impide diagonalizar sobre $\mathbb{R}$.

**Relación entre coeficientes y raíces.** Si $x_1,x_2$ son las raíces (reales o complejas, contadas con multiplicidad) de $ax^2+bx+c$, entonces

$$
x_1+x_2=-\frac{b}{a},\qquad x_1\,x_2=\frac{c}{a}.
$$

Se obtiene comparando coeficientes en $a(x-x_1)(x-x_2)=ax^2-a(x_1+x_2)x+ax_1x_2$. Para un mónico de grado 3, $x^3+a_2x^2+a_1x+a_0=(x-x_1)(x-x_2)(x-x_3)$ da del mismo modo $x_1+x_2+x_3=-a_2$ y $x_1x_2x_3=-a_0$. Son controles rápidos de una factorización. En la Unidad 3 se verá que, para $p_A(\lambda)$, la suma de las raíces es $\operatorname{tr}(A)$ y el producto es $\det A$.

## Polinomios característicos de grado 3

Al calcular $\det(\lambda I-A)$ para una matriz de $3\times3$ conviene seguir este orden:

1. **No expandir de más.** Si al desarrollar el determinante aparece un factor común (por ejemplo, porque una fila o columna tiene dos ceros), dejarlo factorizado.
2. **Sacar factor común $\lambda$** si el término independiente es $0$.
3. **Probar divisores enteros** del término independiente (el polinomio es mónico) y bajar el grado con Ruffini.
4. **Resolver la cuadrática** que queda con el discriminante.
5. **Controlar** con la suma y el producto de las raíces.

### Ejemplo 3 · Un factor irreducible y un polinomio que no hay que expandir
<!-- check: R.T04.E3 -->

**(a)** Factorizamos en $\mathbb{R}$ $p(x)=x^3-3x^2+4x-2$. Candidatas: $\pm1,\pm2$. $p(1)=1-3+4-2=0$. Ruffini con $1$:

$$
\begin{array}{r|rrrr} & 1 & -3 & 4 & -2\\ 1 & & 1 & -2 & 2\\ \hline & 1 & -2 & 2 & 0\end{array}
$$

El cociente $x^2-2x+2$ tiene $\Delta=4-8=-4<0$: es irreducible en $\mathbb{R}$ (sus raíces son $1\pm i$). La factorización en $\mathbb{R}$ es $p(x)=(x-1)(x^2-2x+2)$, con una única raíz real, $x=1$.

**(b)** Supongamos que al desarrollar $\det(\lambda I-A)$ por una fila con dos ceros se obtuvo

$$
q(\lambda)=(\lambda-2)\big[(\lambda-1)(\lambda-3)-3\big].
$$

No conviene expandir todo: el factor $\lambda-2$ ya está a la vista. Dentro del corchete, $(\lambda-1)(\lambda-3)-3=\lambda^2-4\lambda+3-3=\lambda^2-4\lambda=\lambda(\lambda-4)$. Entonces

$$
q(\lambda)=\lambda\,(\lambda-2)(\lambda-4),
$$

con raíces simples $0$, $2$ y $4$.

**Comprobación.** En (a), las tres raíces complejas $1$, $1+i$, $1-i$ suman $3=-(-3)$ y su producto es $1\cdot(1+1)=2=-(-2)$. En (b), expandiendo, $q(\lambda)=\lambda^3-6\lambda^2+8\lambda$: la suma de raíces es $6$ y el término independiente es $0$, como corresponde a la raíz $0$.

:::caution[Errores frecuentes]
- **Perder una raíz al dividir.** Si en $\lambda^3-4\lambda=0$ se divide por $\lambda$, se pierde la raíz $0$. Lo correcto es factorizar: $\lambda(\lambda-2)(\lambda+2)=0$.
- **Olvidar coeficientes nulos en Ruffini.** Para $x^3-2x+1$ la fila de coeficientes es $1,\ 0,\ -2,\ 1$; omitir el $0$ da un cociente equivocado.
- **Confundir los signos en la factorización.** Si $-2$ es raíz, el factor es $x+2$, no $x-2$.
- **Contar mal la multiplicidad.** En $(\lambda-1)(\lambda-2)^2$, $2$ es raíz doble: no basta con listar "raíces $1$ y $2$" si después hace falta $m_a$.
- **Olvidar el coeficiente principal.** $2x^2-5x+2=(x-2)(2x-1)$, no $(x-2)\left(x-\frac12\right)$.
- **Expandir sin necesidad.** Multiplicar todo un $\det(\lambda I-A)$ que venía parcialmente factorizado obliga a buscar de nuevo las raíces que ya estaban a la vista.
:::

:::tip[En resumen]
- $p(a)$ es el resto de dividir por $x-a$; $a$ es raíz $\iff$ $(x-a)$ divide a $p$.
- Ruffini divide por $x-a$ y da el cociente y el resto.
- Criterio de Gauss: raíces racionales $\frac rs$ con $r\mid a_0$ y $s\mid a_n$; si $p$ es mónico, enteras y divisoras de $a_0$.
- En $\mathbb{R}$, todo polinomio se factoriza en lineales y cuadráticos irreducibles ($\Delta<0$).
- Grado 2: suma $-\frac ba$, producto $\frac ca$. Mónico de grado 3: suma $-a_2$, producto $-a_0$.
:::

## Ejercicios de repaso

### Ejercicio R.13 · Factorizar un polinomio de grado 3
<!-- ejercicio: R.13 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Factorizar $p(x)=x^3+2x^2-5x-6$ y hallar todas sus raíces.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Mónico con coeficientes enteros: probar divisores de $-6$ y bajar el grado con Ruffini.

Candidatas: $\pm1,\pm2,\pm3,\pm6$. $p(1)=1+2-5-6=-8\neq0$; $p(-1)=-1+2+5-6=0$. Ruffini con $-1$:

$$
\begin{array}{r|rrrr} & 1 & 2 & -5 & -6\\ -1 & & -1 & -1 & 6\\ \hline & 1 & 1 & -6 & 0\end{array}
$$

El cociente $x^2+x-6$ tiene raíces $\frac{-1\pm5}{2}$, es decir $2$ y $-3$.

**Comprobación.** Suma de raíces $-1+2-3=-2=-a_2$; producto $(-1)\cdot2\cdot(-3)=6=-a_0$.

:::tip[Resultado]
$p(x)=(x+1)(x-2)(x+3)$; raíces $-1$, $2$ y $-3$, todas simples.
:::

</details>

### Ejercicio R.14 · Teorema del resto con un parámetro
<!-- ejercicio: R.14 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallar $k\in\mathbb{R}$ para que $p(x)=x^3+kx^2-x+2$ sea divisible por $x-2$. Para ese valor, factorizar $p$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $x-2$ divide a $p$ si y solo si $p(2)=0$ (teorema del resto).

$p(2)=8+4k-2+2=8+4k$, que se anula si y solo si $k=-2$. Con $k=-2$, $p(x)=x^3-2x^2-x+2$, y Ruffini con $2$:

$$
\begin{array}{r|rrrr} & 1 & -2 & -1 & 2\\ 2 & & 2 & 0 & -2\\ \hline & 1 & 0 & -1 & 0\end{array}
$$

El cociente es $x^2-1=(x-1)(x+1)$.

**Comprobación.** También se puede agrupar: $x^3-2x^2-x+2=x^2(x-2)-(x-2)=(x-2)(x^2-1)$.

:::tip[Resultado]
$k=-2$ y $p(x)=(x-2)(x-1)(x+1)$.
:::

</details>

### Ejercicio R.15 · Raíces y multiplicidades
<!-- ejercicio: R.15 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Factorizar $p(\lambda)=\lambda^3-4\lambda^2+5\lambda-2$, indicar la multiplicidad de cada raíz y verificar las relaciones entre los coeficientes y las raíces.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Probar divisores de $-2$; después de la primera división, mirar si la raíz se repite.

$p(1)=1-4+5-2=0$. Ruffini con $1$:

$$
\begin{array}{r|rrrr} & 1 & -4 & 5 & -2\\ 1 & & 1 & -3 & 2\\ \hline & 1 & -3 & 2 & 0\end{array}
$$

El cociente $\lambda^2-3\lambda+2=(\lambda-1)(\lambda-2)$ vuelve a anularse en $1$: la raíz $1$ es doble.

**Comprobación.** Con multiplicidad, las raíces son $1,1,2$: suma $4=-(-4)$ y producto $2=-(-2)$.

:::tip[Resultado]
$p(\lambda)=(\lambda-1)^2(\lambda-2)$: $\lambda=1$ con multiplicidad 2 y $\lambda=2$ con multiplicidad 1.
:::

</details>

### Ejercicio R.16 · Raíz fraccionaria y factor irreducible
<!-- ejercicio: R.16 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallar las raíces racionales de $p(x)=3x^3-x^2+3x-1$ y dar su factorización en $\mathbb{R}$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Criterio de Gauss: $r$ divide a $-1$ y $s$ divide a $3$.

Candidatas: $\pm1,\pm\frac13$. $p(1)=4$ y $p(-1)=-8$; en cambio $p\left(\frac13\right)=\frac19-\frac19+1-1=0$. Ruffini con $\frac13$:

$$
\begin{array}{r|rrrr} & 3 & -1 & 3 & -1\\ \tfrac13 & & 1 & 0 & 1\\ \hline & 3 & 0 & 3 & 0\end{array}
$$

El cociente es $3x^2+3=3(x^2+1)$, con $\Delta=-4<0$: irreducible en $\mathbb{R}$. Así $p(x)=\left(x-\frac13\right)\cdot3\,(x^2+1)=(3x-1)(x^2+1)$. La última candidata tampoco es raíz: $p\left(-\frac13\right)=-\frac19-\frac19-1-1\neq0$.

**Comprobación.** Agrupando: $3x^3-x^2+3x-1=x^2(3x-1)+(3x-1)=(3x-1)(x^2+1)$.

:::tip[Resultado]
Única raíz racional (y única real): $\frac13$. Factorización en $\mathbb{R}$: $(3x-1)(x^2+1)$.
:::

</details>

## Dónde se usa en Álgebra II

- Raíces de $p_A(\lambda)$ y multiplicidades algebraicas: [polinomio característico](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/), [propiedades](/algebra-ii/unidad-3/teoria/propiedades/) (traza y determinante como suma y producto de autovalores) y [diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/).
- Polinomio característico de una recurrencia de orden 2 (una cuadrática): [relaciones de recurrencia](/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/).
- $P_n[\mathbb{R}]$ como espacio vectorial y sus bases: [espacios vectoriales](/algebra-ii/unidad-1/teoria/espacios-vectoriales/) y [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/); la derivación como transformación lineal en [definición y ejemplos](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/).

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: secciones 4.1 y 4.3, donde la factorización de polinomios se usa para hallar autovalores.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de valores propios y vectores propios (ecuación característica).
- Lección anterior: [R.3 Sistemas lineales](/algebra-ii/repaso/sistemas-lineales/). Siguiente: [R.5 Rectas y planos](/algebra-ii/repaso/rectas-y-planos/).
