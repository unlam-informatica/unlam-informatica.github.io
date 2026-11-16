---
title: Subespacios
description: Definición de subespacio, criterio de las tres condiciones con demostración, rectas y planos por el origen, ejemplos en ℝ³, matrices, polinomios y ℤ₂ⁿ, intersección, unión y errores frecuentes.
slug: algebra-ii/unidad-1/teoria/subespacios
sidebar:
  order: 3
  label: 1.3 Subespacios
---

## Para qué sirve

Dentro de un espacio vectorial grande suelen interesar subconjuntos que, por sí mismos, se comportan
como espacios vectoriales: las soluciones de un sistema lineal homogéneo, los planos que pasan por el
origen, las matrices simétricas, los polinomios que cumplen cierta condición o, en informática, las
**palabras válidas de un código**: en un código lineal, la suma de dos palabras válidas es otra palabra
válida. Esos subconjuntos son los **subespacios**. Esta lección da un criterio rápido para reconocerlos
y muestra los errores más comunes al aplicarlo.

## Definición

:::note[Definición (subespacio)]
Sea $(V,+,K,\cdot)$ un espacio vectorial. Un subconjunto no vacío $S\subseteq V$ es un **subespacio** de
$V$ si $S$, con la misma suma y el mismo producto por escalar de $V$ restringidos a sus elementos, es un
espacio vectorial sobre $K$.
:::

Todo espacio $V$ tiene al menos dos subespacios, llamados **triviales**: $\{0_V\}$ y el propio $V$.

## El criterio de las tres condiciones

Verificar diez axiomas cada vez sería largo e innecesario: la mayoría de ellos son igualdades que ya
valen para **todos** los elementos de $V$ y, por lo tanto, para los de $S$. Lo que puede fallar es que
las operaciones se salgan de $S$, o que $S$ no contenga los elementos que los axiomas exigen.

:::note[Teorema (criterio de subespacio)]
Sea $V$ un espacio vectorial sobre $K$ y $S\subseteq V$. Entonces $S$ es un subespacio de $V$ si y solo si
se cumplen las tres condiciones:

1. $0_V\in S$.
2. Para todos $u,v\in S$: $u+v\in S$ (cierre para la suma).
3. Para todos $\lambda\in K$ y $v\in S$: $\lambda v\in S$ (cierre para el producto por escalar).
:::

**Demostración.** ($\Rightarrow$) Si $S$ es subespacio, las condiciones 2 y 3 son los axiomas de cierre
de $S$. Para la condición 1: $S$ tiene un neutro $e$ para la suma, así que $e+e=e$. Como esa igualdad
vale también en $V$ y $e=e+0_V$, tenemos $e+e=e+0_V$, y por cancelación en $V$, $e=0_V$. Entonces
$0_V=e\in S$.

($\Leftarrow$) Supongamos que valen 1, 2 y 3. Por la condición 1, $S\neq\varnothing$. Revisamos los diez
axiomas en $S$:

- Los cierres (axiomas 1 y 6) son las condiciones 2 y 3.
- La asociativa, la conmutativa, $1\cdot v=v$, la asociativa mixta y las dos distributivas (axiomas 2, 5,
  7, 8, 9 y 10) son igualdades que valen para todos los elementos de $V$; en particular valen para los
  de $S$. Decimos que se **heredan**.
- Neutro (axioma 3): $0_V\in S$ por la condición 1, y $v+0_V=v$ para todo $v\in S$.
- Opuesto (axioma 4): si $v\in S$, por la condición 3 con $\lambda=-1$ tenemos $(-1)v\in S$, y
  $(-1)v=-v$ por las propiedades elementales de los
  [espacios vectoriales](/algebra-ii/unidad-1/teoria/espacios-vectoriales/). $\blacksquare$

Observaciones sobre el criterio:

- **El nulo como filtro.** Si $0_V\notin S$, el conjunto no es subespacio y no hace falta seguir. Por eso
  conviene revisar la condición 1 primero. Pero que $0_V\in S$ **no alcanza**: hay que probar también 2 y 3.
- **No vacío o nulo.** La condición 1 puede reemplazarse por "$S\neq\varnothing$": si $v\in S$, la
  condición 3 con $\lambda=0$ da $0\cdot v=0_V\in S$.
- **Una sola condición.** Las condiciones 2 y 3 equivalen a pedir que $\lambda u+\mu v\in S$ para todos
  $u,v\in S$ y $\lambda,\mu\in K$: $S$ es cerrado para combinaciones lineales de dos elementos.
- **Sobre $\mathbb{Z}_2$, la condición 3 es automática si vale la 1.** Los únicos escalares son $0$ y $1$, y
  $0\cdot v=0_V\in S$, $1\cdot v=v\in S$. Para un subconjunto de $\mathbb{Z}_2^n$ alcanza con verificar que
  contiene al nulo y que es cerrado para la suma.

### Sistemas homogéneos

La herramienta que más usaremos para fabricar subespacios es la siguiente.

:::note[Propiedad]
Sea $A\in K^{m\times n}$. El conjunto de soluciones del sistema homogéneo $Ax=0$,
$\{x\in K^{n}: Ax=0\}$ (con $x$ escrito como columna), es un subespacio de $K^n$. El conjunto de soluciones
de $Ax=b$ con $b\neq 0$ **no** es un subespacio.
:::

**Demostración.** $A\,0=0$, así que el nulo es solución. Si $Au=0$ y $Av=0$, entonces
$A(u+v)=Au+Av=0$ y $A(\lambda u)=\lambda Au=0$, por las propiedades del producto de matrices. Si
$b\neq 0$, el nulo no es solución porque $A\,0=0\neq b$. $\blacksquare$

Este subespacio es el **espacio nulo** de $A$, que estudiaremos en
[subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/).

## Interpretación geométrica: rectas y planos por el origen

En $\mathbb{R}^2$, una recta de ecuación $ax+by=c$ (con $a$ y $b$ no ambos nulos) es subespacio si y solo si
$c=0$, es decir, si **pasa por el origen**: si $c\neq 0$, el origen no la satisface; si $c=0$, es el
conjunto solución de un sistema homogéneo. Lo mismo ocurre con los planos $ax+by+cz=d$ de $\mathbb{R}^3$
y con las rectas del espacio dadas por dos ecuaciones.

### Ejemplo 1 · Una recta por el origen y una recta desplazada
<!-- check: U1.T03.E1 -->

Sean $S=\{(x,y)\in\mathbb{R}^2: x-2y=0\}$ y $L=\{(x,y)\in\mathbb{R}^2: x-2y=-4\}$. Probar que $S$ es subespacio
de $\mathbb{R}^2$ y que $L$ no lo es, mostrando todas las condiciones que fallan en $L$.

**$S$ es subespacio.** (1) $0-2\cdot 0=0$, así que $(0,0)\in S$. (2) Si $(x,y)$ y $(x',y')$ están en $S$,
entonces $(x+x')-2(y+y')=(x-2y)+(x'-2y')=0+0=0$. (3) Si $(x,y)\in S$ y $\lambda\in\mathbb{R}$,
$\lambda x-2\lambda y=\lambda(x-2y)=\lambda\cdot 0=0$.

**$L$ no es subespacio.** Ya la primera condición falla: $0-2\cdot 0=0\neq -4$. Pero vale la pena ver que
también fallan las otras dos. Los puntos $p=(0,2)$ y $q=(2,3)$ están en $L$, porque $0-4=-4$ y $2-6=-4$.
Sin embargo:

- $p+q=(2,5)$ y $2-10=-8\neq -4$: la suma se sale de $L$.
- $2p=(0,4)$ y $0-8=-8\neq-4$: el producto por escalar se sale de $L$.

Comprobación general: si $(x,y),(x',y')\in L$, entonces $(x+x')-2(y+y')=-4-4=-8$; la suma de dos puntos
de $L$ **siempre** cae en la recta paralela $x-2y=-8$, nunca en $L$.

<figure class="math-figure">
<svg viewBox="-150 -150 300 260" role="img" aria-labelledby="sub-rectas-t sub-rectas-d" xmlns="http://www.w3.org/2000/svg">
<title id="sub-rectas-t">Recta por el origen y recta desplazada</title>
<desc id="sub-rectas-d">Grilla con unidad de 20 píxeles. La recta S de ecuación x − 2y = 0 pasa por el origen. La recta L de ecuación x − 2y = −4 es paralela a S y pasa por p = (0, 2) y q = (2, 3). La suma p + q = (2, 5) no está en L: está sobre la recta paralela x − 2y = −8, dibujada en línea de trazos.</desc>
<defs><marker id="sub-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker><marker id="sub-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="scale(1,-1)">
<path class="grid" d="M-140 -100V140 M-120 -100V140 M-100 -100V140 M-80 -100V140 M-60 -100V140 M-40 -100V140 M-20 -100V140 M20 -100V140 M40 -100V140 M60 -100V140 M80 -100V140 M100 -100V140 M120 -100V140 M140 -100V140 M-140 -100H140 M-140 -80H140 M-140 -60H140 M-140 -40H140 M-140 -20H140 M-140 20H140 M-140 40H140 M-140 60H140 M-140 80H140 M-140 100H140 M-140 120H140 M-140 140H140"/>
<line class="axis" x1="-140" y1="0" x2="140" y2="0"/>
<line class="axis" x1="0" y1="-100" x2="0" y2="140"/>
<line class="line-a" x1="-140" y1="-70" x2="140" y2="70"/>
<line class="line-b" x1="-140" y1="-30" x2="140" y2="110"/>
<line class="guide" x1="-140" y1="10" x2="120" y2="140"/>
<line class="vec-b" x1="0" y1="0" x2="0" y2="40" marker-end="url(#sub-arrow-b)"/>
<line class="vec-b" x1="0" y1="0" x2="40" y2="60" marker-end="url(#sub-arrow-b)"/>
<line class="guide" x1="0" y1="40" x2="40" y2="100"/>
<line class="guide" x1="40" y1="60" x2="40" y2="100"/>
<line class="vec-c" x1="0" y1="0" x2="40" y2="100" marker-end="url(#sub-arrow-c)"/>
<circle class="dot-a" cx="0" cy="0" r="3"/>
<circle class="dot-b" cx="0" cy="40" r="3"/>
<circle class="dot-b" cx="40" cy="60" r="3"/>
<circle class="dot-c" cx="40" cy="100" r="3"/>
</g>
<text class="math" x="128" y="-78">S</text>
<text class="math" x="122" y="-118">L</text>
<text class="math" x="-16" y="-44">p</text>
<text class="math" x="46" y="-44">q</text>
<text class="math" x="48" y="-100">p + q</text>
<text x="-14" y="14">0</text>
<text class="math" x="142" y="14">x</text>
<text class="math" x="6" y="-140">y</text>
</svg>
<figcaption>S pasa por el origen y es cerrada para las operaciones. L no contiene al origen y, además, la suma de dos de sus puntos cae siempre en otra recta paralela (trazos): ninguna de las tres condiciones se cumple.</figcaption>
</figure>

Más en general, vale la siguiente descripción, que demostraremos cuando tengamos la noción de
dimensión (ver [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/)):

- los subespacios de $\mathbb{R}^2$ son $\{0\}$, las rectas que pasan por el origen y $\mathbb{R}^2$;
- los subespacios de $\mathbb{R}^3$ son $\{0\}$, las rectas que pasan por el origen, los planos que pasan
  por el origen y $\mathbb{R}^3$.

Una recta o un plano que no pasa por el origen es un subespacio **trasladado**, pero no un subespacio.

### Ejemplo 2 · Un plano de ℝ³
<!-- check: U1.T03.E2 -->

Probar que $\Pi=\{(x,y,z)\in\mathbb{R}^3: 2x-y+3z=0\}$ es subespacio de $\mathbb{R}^3$ y decidir si
$(1,5,1)$, $(2,1,-1)$ y $(1,1,1)$ pertenecen a $\Pi$.

**Criterio.** (1) $2\cdot 0-0+3\cdot 0=0$. (2) Si $u=(x,y,z)$ y $u'=(x',y',z')$ están en $\Pi$,

$$
2(x+x')-(y+y')+3(z+z')=(2x-y+3z)+(2x'-y'+3z')=0+0=0 .
$$

(3) Si $u\in\Pi$ y $\lambda\in\mathbb{R}$, $2\lambda x-\lambda y+3\lambda z=\lambda(2x-y+3z)=0$. (Alternativamente:
$\Pi$ es el conjunto solución del sistema homogéneo de una ecuación con matriz $(2\ \ -1\ \ 3)$.)

**Pertenencias.** $2-5+3=0$, así que $(1,5,1)\in\Pi$; $4-1-3=0$, así que $(2,1,-1)\in\Pi$;
$2-1+3=4\neq 0$, así que $(1,1,1)\notin\Pi$.

Comprobación del cierre con datos: $(1,5,1)+(2,1,-1)=(3,6,0)$ y $6-6+0=0$; $(-2)(1,5,1)=(-2,-10,-2)$ y
$-4+10-6=0$. Ambos resultados están en $\Pi$, como garantiza el criterio.

### Ejemplo 3 · Matrices simétricas y matrices de traza nula
<!-- check: U1.T03.E3 -->

En $\mathbb{R}^{2\times 2}$ sean $\mathcal{S}=\{A: A^t=A\}$ (matrices simétricas) y
$\mathcal{T}=\{A: \operatorname{tr}(A)=0\}$ (matrices de traza nula). Probar que ambos son subespacios y
describir $\mathcal{S}\cap\mathcal{T}$.

**Simétricas.** (1) La matriz nula cumple $0^t=0$. (2) Si $A^t=A$ y $B^t=B$, entonces
$(A+B)^t=A^t+B^t=A+B$. (3) $(\lambda A)^t=\lambda A^t=\lambda A$. Usamos las propiedades de la
transpuesta (ver [repaso de vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/)).

**Traza nula.** La traza es la suma de la diagonal: $\operatorname{tr}\begin{pmatrix}a&b\\c&d\end{pmatrix}=a+d$.
Cumple $\operatorname{tr}(A+B)=\operatorname{tr}(A)+\operatorname{tr}(B)$ y
$\operatorname{tr}(\lambda A)=\lambda\operatorname{tr}(A)$. Entonces: (1) $\operatorname{tr}(0)=0$;
(2) si $\operatorname{tr}(A)=\operatorname{tr}(B)=0$, $\operatorname{tr}(A+B)=0$; (3)
$\operatorname{tr}(\lambda A)=\lambda\cdot 0=0$.

**Forma genérica.** Una matriz es simétrica si y solo si $b=c$, y tiene traza nula si y solo si $d=-a$:

$$
\mathcal{S}=\left\{\begin{pmatrix}a&b\\b&d\end{pmatrix}: a,b,d\in\mathbb{R}\right\},\qquad
\mathcal{S}\cap\mathcal{T}=\left\{\begin{pmatrix}a&b\\b&-a\end{pmatrix}: a,b\in\mathbb{R}\right\}.
$$

Comprobación: $A=\begin{pmatrix}1&2\\2&-1\end{pmatrix}$ y $B=\begin{pmatrix}0&3\\3&0\end{pmatrix}$ están en
$\mathcal{S}\cap\mathcal{T}$, y $A+B=\begin{pmatrix}1&5\\5&-1\end{pmatrix}$ también: es simétrica y su traza
es $1-1=0$.

### Ejemplo 4 · Un subespacio de $P_2[\mathbb{R}]$ definido por evaluaciones
<!-- check: U1.T03.E4 -->

Sea $S=\{p\in P_2[\mathbb{R}]: p(-1)=p(2)\}$. Probar que $S$ es subespacio de $P_2[\mathbb{R}]$, describir sus
elementos y decidir si $q=3+2x-2x^2$ y $r=x$ pertenecen a $S$.

Mostramos dos caminos, como conviene hacer cuando ambos son razonables.

**Camino A: directo con la condición.** Usamos que evaluar es compatible con las operaciones:
$(p+q)(t)=p(t)+q(t)$ y $(\lambda p)(t)=\lambda\,p(t)$.

1. El polinomio nulo vale $0$ en todo punto: $0(-1)=0=0(2)$.
2. Si $p,q\in S$: $(p+q)(-1)=p(-1)+q(-1)=p(2)+q(2)=(p+q)(2)$, donde la igualdad del medio usa que
   $p\in S$ y $q\in S$.
3. Si $p\in S$ y $\lambda\in\mathbb{R}$: $(\lambda p)(-1)=\lambda\,p(-1)=\lambda\,p(2)=(\lambda p)(2)$.

**Camino B: forma genérica de los elementos.** Escribimos $p=a+bx+cx^2$. Entonces $p(-1)=a-b+c$ y
$p(2)=a+2b+4c$, así que

$$
p\in S\iff a-b+c=a+2b+4c\iff 3b+3c=0\iff b=-c .
$$

Los elementos de $S$ son los polinomios $a-cx+cx^2=a\cdot 1+c\,(x^2-x)$ con $a,c\in\mathbb{R}$ libres.
Con esta descripción el criterio es inmediato: la suma
$\big(a\cdot 1+c(x^2-x)\big)+\big(a'\cdot 1+c'(x^2-x)\big)=(a+a')\cdot 1+(c+c')(x^2-x)$ tiene la misma forma, y
lo mismo ocurre con $\lambda\big(a\cdot 1+c(x^2-x)\big)=(\lambda a)\cdot 1+(\lambda c)(x^2-x)$.

**¿Cuál conviene?** El camino A es más corto si solo se pide probar que es subespacio. El camino B da
además una descripción explícita de los elementos, que es la que se necesita para hallar
[generadores](/algebra-ii/unidad-1/teoria/combinaciones-lineales/) y una
[base](/algebra-ii/unidad-1/teoria/base-y-dimension/).

**Pertenencias.** $q(-1)=3-2-2=-1$ y $q(2)=3+4-8=-1$: $q\in S$. En efecto, $q=3\cdot 1-2(x^2-x)$, con
$a=3$ y $c=-2$. En cambio, $r(-1)=-1$ y $r(2)=2$: $r\notin S$.

Comprobación: $3\cdot 1-2(x^2-x)=3+2x-2x^2=q$.

Interpretación: como $x^2-x=\left(x-\tfrac12\right)^2-\tfrac14$, los elementos de $S$ son los polinomios cuyo
gráfico es simétrico respecto de la recta $x=\tfrac12$ (incluidas las constantes). Los puntos $-1$ y $2$
son simétricos respecto de $\tfrac12$.

:::caution[Trabajar en el espacio propio]
Los elementos de $S$ son **polinomios**, no ternas. En el camino B usamos la terna de coeficientes
$(a,b,c)$ como herramienta para resolver una ecuación, pero la respuesta se escribe en $P_2[\mathbb{R}]$:
"$S$ está formado por los polinomios $a\cdot 1+c(x^2-x)$", no "$S=\{(a,-c,c)\}$". Del mismo modo, los
elementos de $\mathcal{S}\cap\mathcal{T}$ del Ejemplo 3 son matrices. Mezclar objetos de espacios distintos
(escribir que un polinomio "es igual" a una terna) es un error de tipo que se penaliza en los exámenes.
:::

### Ejemplo 5 · Un subespacio de ℤ₂³ con todos sus elementos
<!-- check: U1.T03.E5 -->

Sea $S=\{(a,b,c)\in\mathbb{Z}_2^3: a+b+c=0\}$. Listar sus elementos y probar que es subespacio. ¿Es
subespacio $T=\{(a,b,c)\in\mathbb{Z}_2^3: a+b+c=1\}$?

**Elementos.** $a+b+c=0$ en $\mathbb{Z}_2$ significa que la terna tiene una cantidad **par** de unos.
Recorriendo las $8$ ternas:

$$
S=\{(0,0,0),\ (0,1,1),\ (1,0,1),\ (1,1,0)\}.
$$

**Subespacio.** Contiene al nulo. Para el cierre de la suma podemos argumentar en general: si
$a+b+c=0$ y $a'+b'+c'=0$, entonces $(a+a')+(b+b')+(c+c')=0+0=0$. O podemos verificar la tabla
completa de sumas, escribiendo $011$ en lugar de $(0,1,1)$:

| $+$ | $000$ | $011$ | $101$ | $110$ |
|---|---|---|---|---|
| $000$ | $000$ | $011$ | $101$ | $110$ |
| $011$ | $011$ | $000$ | $110$ | $101$ |
| $101$ | $101$ | $110$ | $000$ | $011$ |
| $110$ | $110$ | $101$ | $011$ | $000$ |

Todas las sumas quedan en $S$. Como el cuerpo es $\mathbb{Z}_2$, el cierre por escalares es automático.

**El conjunto $T$** (ternas con una cantidad impar de unos) no contiene a $(0,0,0)$, así que no es
subespacio. Además $(1,0,0)+(0,1,0)=(1,1,0)\notin T$.

Comprobación: $S$ y $T$ tienen $4$ elementos cada uno y juntos forman las $8$ ternas de $\mathbb{Z}_2^3$.
$S$ es el **código de paridad** de longitud $3$: las palabras de $2$ bits $(a,b)$ con el bit de paridad
$c=a+b$ agregado al final.

### Ejemplo 6 · Todos los subespacios de ℤ₂²
<!-- check: U1.T03.E6 -->

Hallar todos los subespacios de $\mathbb{Z}_2^2=\{(0,0),(1,0),(0,1),(1,1)\}$.

Todo subespacio contiene a $(0,0)$. Separamos casos según cuántos vectores no nulos contiene.

- **Ninguno:** $\{(0,0)\}$.
- **Exactamente uno, $v$:** $\{(0,0),v\}$ es subespacio, porque $v+v=(0,0)$, $0+v=v$ y los escalares son
  $0$ y $1$. Hay tres: $\{(0,0),(1,0)\}$, $\{(0,0),(0,1)\}$ y $\{(0,0),(1,1)\}$.
- **Dos o más:** si contiene dos vectores no nulos distintos $u$ y $v$, contiene $u+v$, que es el tercer
  vector no nulo (por ejemplo, $(1,0)+(0,1)=(1,1)$). Entonces es todo $\mathbb{Z}_2^2$.

En total hay $1+3+1=5$ subespacios. Los tres del medio son las "rectas por el origen" de $\mathbb{Z}_2^2$,
cada una con solo dos puntos.

Comprobación: un recorrido exhaustivo de los $16$ subconjuntos de $\mathbb{Z}_2^2$ encuentra exactamente
estos cinco.

**Comentario sobre $\mathbb{Z}_2^3$.** El mismo razonamiento muestra que un subespacio de $\mathbb{Z}_2^3$ solo
puede tener $1$, $2$, $4$ u $8$ elementos. En efecto, si contiene dos vectores no nulos distintos $u,v$,
contiene $P=\{0,u,v,u+v\}$, que es subespacio. Si además contiene un $w\notin P$, contiene los cuatro
vectores $w,\ w+u,\ w+v,\ w+u+v$, que son distintos entre sí y no están en $P$ (si $w+p=p'$ con
$p,p'\in P$, sería $w=p+p'\in P$); en total, $8$ elementos, todo $\mathbb{Z}_2^3$. Contamos:

- $1$ subespacio con $1$ elemento y $1$ con $8$;
- $7$ con $2$ elementos, uno por cada vector no nulo;
- con $4$ elementos: hay $\binom{7}{2}=21$ pares de vectores no nulos distintos, y cada subespacio de $4$
  elementos contiene $3$ vectores no nulos, es decir, $\binom{3}{2}=3$ de esos pares. Son $21/3=7$.

En total, $\mathbb{Z}_2^3$ tiene $1+7+7+1=16$ subespacios. Los $7$ de cuatro elementos son exactamente los
conjuntos de soluciones de las $7$ ecuaciones $a_1x_1+a_2x_2+a_3x_3=0$ con $(a_1,a_2,a_3)\neq(0,0,0)$; el
Ejemplo 5 es el caso $(1,1,1)$.

## Intersección y unión

:::note[Teorema]
Si $S$ y $T$ son subespacios de $V$, entonces $S\cap T$ es un subespacio de $V$.
:::

**Demostración.** (1) $0_V\in S$ y $0_V\in T$, así que $0_V\in S\cap T$. (2) Si $u,v\in S\cap T$,
entonces $u+v\in S$ porque $S$ es subespacio y $u+v\in T$ porque $T$ lo es; luego $u+v\in S\cap T$.
(3) Igual con $\lambda v$. $\blacksquare$

Por eso un sistema homogéneo de varias ecuaciones define un subespacio: es la intersección de los
subespacios que define cada ecuación. En $\mathbb{R}^3$, dos planos distintos por el origen se cortan en una
recta por el origen.

La unión se comporta muy distinto. En $\mathbb{R}^2$, la unión de los dos ejes,
$\{(x,y): x=0\}\cup\{(x,y): y=0\}$, contiene a $(1,0)$ y a $(0,1)$ pero no a su suma $(1,1)$. El
fenómeno es general:

:::note[Teorema]
Sean $S$ y $T$ subespacios de $V$. $S\cup T$ es subespacio si y solo si $S\subseteq T$ o $T\subseteq S$.
:::

**Demostración.** Si $S\subseteq T$, entonces $S\cup T=T$, que es subespacio; análogamente si
$T\subseteq S$. Recíprocamente, supongamos que ninguno está contenido en el otro: existen $s\in S$ con
$s\notin T$ y $t\in T$ con $t\notin S$. Si $S\cup T$ fuera subespacio, $s+t$ estaría en $S$ o en $T$. Si
$s+t\in S$, entonces $t=(s+t)-s\in S$, absurdo. Si $s+t\in T$, entonces $s=(s+t)-t\in T$, absurdo. Luego
$S\cup T$ no es subespacio. $\blacksquare$

El menor subespacio que contiene a $S\cup T$ se construye con combinaciones lineales; lo veremos en
[combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/).

### Ejemplo 7 · Tres conjuntos que no son subespacios
<!-- check: U1.T03.E7 -->

Decidir qué condiciones del criterio cumplen los siguientes conjuntos.

**(a) $A=\{(x,y)\in\mathbb{R}^2: xy=0\}$** (la unión de los dos ejes). Contiene a $(0,0)$. Es cerrado por
escalares: si $xy=0$, $(\lambda x)(\lambda y)=\lambda^2xy=0$. No es cerrado para la suma:
$(1,0),(0,1)\in A$, pero $(1,1)\notin A$ porque $1\cdot 1=1\neq 0$.

**(b) $D=\{M\in\mathbb{R}^{2\times 2}: \det M=0\}$.** Contiene a la matriz nula y es cerrado por escalares,
porque $\det(\lambda M)=\lambda^2\det M$. No es cerrado para la suma:

$$
\begin{pmatrix}1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&1\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix},
$$

con los dos sumandos de determinante $0$ y la suma de determinante $1$.

**(c) $H=\{(x,y)\in\mathbb{R}^2: x\ge 0\}$** (un semiplano). Contiene a $(0,0)$ y es cerrado para la suma
(la suma de números no negativos es no negativa). No es cerrado por escalares: $(1,0)\in H$ pero
$(-1)(1,0)=(-1,0)\notin H$.

Comprobación: en cada caso el contraejemplo usa elementos concretos que están en el conjunto y un
resultado concreto que no está. Los casos (a) y (c) muestran además que las condiciones 2 y 3 son
independientes: ninguna se deduce de la otra.

:::caution[Errores frecuentes]
- **"Contiene al nulo, entonces es subespacio."** El conjunto $A$ del Ejemplo 7 contiene al nulo y no es
  subespacio. La condición 1 es necesaria, no suficiente.
- **Probar el cierre con ejemplos.** Verificar que $(1,5,1)+(2,1,-1)$ está en $\Pi$ no prueba nada sobre
  todas las sumas. El cierre se prueba con elementos genéricos; un ejemplo solo sirve para refutar.
- **Condiciones no homogéneas.** $\{p\in P_2[\mathbb{R}]: p(0)=1\}$ o $\{(x,y,z): x+y+z=2\}$ no contienen
  al nulo. Una ecuación con término independiente no nulo nunca define un subespacio.
- **Condiciones con productos o potencias de las variables.** $xy=0$, $x^2=y$ o $\det M=0$ suelen
  romper el cierre de la suma.
- **Unir subespacios.** La unión de dos subespacios casi nunca es subespacio; la intersección siempre lo es.
- **Olvidar el espacio.** "$\{(a,b,c): a+b+c=0\}$" es un plano de $\mathbb{R}^3$ con infinitos elementos o
  un conjunto de $4$ elementos de $\mathbb{Z}_2^3$, según el cuerpo. Hay que leer en qué espacio se trabaja.
:::

## Autoevaluación

**1.** ¿Es $\{(x,y,z)\in\mathbb{R}^3: x=2y,\ z=0\}$ un subespacio?

<details>
<summary>Respuesta</summary>

Sí: es el conjunto solución del sistema homogéneo $x-2y=0$, $z=0$. Geométricamente, es la recta por el
origen generada por $(2,1,0)$.

</details>

**2.** ¿Es $\{p\in P_2[\mathbb{R}]: p(0)=1\}$ un subespacio?

<details>
<summary>Respuesta</summary>

No: el polinomio nulo vale $0$ en $x=0$, así que no pertenece al conjunto.

</details>

**3.** ¿Es $\{M\in\mathbb{R}^{2\times 2}: M^2=0\}$ un subespacio?

<details>
<summary>Respuesta</summary>

No. $M=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ y $N=\begin{pmatrix}0&0\\1&0\end{pmatrix}$ cumplen $M^2=N^2=0$, pero
$M+N=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ cumple $(M+N)^2=I\neq 0$.

</details>

**4.** ¿Es $\{(0,0,0),(1,1,0),(0,1,1)\}$ un subespacio de $\mathbb{Z}_2^3$?

<details>
<summary>Respuesta</summary>

No: $(1,1,0)+(0,1,1)=(1,0,1)$ no está en el conjunto. Agregándolo se obtiene el subespacio $S$ del
Ejemplo 5.

</details>

:::tip[En resumen]
- $S\subseteq V$ es subespacio si y solo si contiene a $0_V$ y es cerrado para la suma y para el
  producto por escalar. Las demás propiedades se heredan de $V$.
- Si $0_V\notin S$, no es subespacio; si $0_V\in S$, todavía hay que probar los dos cierres.
- Sobre $\mathbb{Z}_2$ alcanza con el nulo y el cierre de la suma.
- El conjunto solución de un sistema homogéneo es subespacio; el de uno no homogéneo, no.
- En $\mathbb{R}^2$ y $\mathbb{R}^3$, los subespacios no triviales son las rectas y los planos **que pasan por el
  origen**.
- La intersección de subespacios es subespacio; la unión, solo si uno contiene al otro.
- $\mathbb{Z}_2^2$ tiene $5$ subespacios y $\mathbb{Z}_2^3$ tiene $16$.
- Los elementos de un subespacio son del mismo tipo que los de $V$: polinomios, matrices o $n$-uplas.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 6.1, "Espacios y subespacios
  vectoriales" (p. 447), y sección 3.5, "Subespacios, bases, dimensión y rank" (p. 197), para los
  subespacios de $\mathbb{R}^n$.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed., capítulo de espacios vectoriales, sección sobre
  espacios y subespacios vectoriales.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed., sección 4.4 (subespacios,
  intersección y suma, p. 162), como lectura complementaria.

Lección anterior: [espacios vectoriales](/algebra-ii/unidad-1/teoria/espacios-vectoriales/). Lección
siguiente: [combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/). Repaso
relacionado: [rectas y planos](/algebra-ii/repaso/rectas-y-planos/).
