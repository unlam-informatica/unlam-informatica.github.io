---
title: Códigos y el producto en ℤ₂ⁿ
description: Producto punto en ℤ₂ⁿ, código dual y códigos autoduales, distancia de Hamming, distancia mínima, detección y corrección de errores y decodificación por síndrome.
slug: algebra-ii/unidad-4/teoria/codigos-y-z2
sidebar:
  order: 8
  label: 4.8 Códigos y ℤ₂ⁿ
---

Cuando un mensaje binario viaja por un canal con ruido, algunos bits llegan cambiados. Un código lineal agrega redundancia para que el receptor pueda **detectar** y a veces **corregir** esos cambios. En la [lección 1.10](/algebra-ii/unidad-1/teoria/codigos-lineales/) vimos cómo se construye un código con una matriz generadora $G$ y una matriz de control de paridad $H$. Ahora usamos las ideas de la unidad (ortogonalidad, complemento, distancia) para estudiarlos: el **código dual** es un complemento ortogonal, la **distancia de Hamming** es una métrica y la **distancia mínima** decide cuántos errores se corrigen.

Hay una advertencia de fondo: en $\mathbb{Z}_2^n$ **no hay producto interno**, y por eso varias propiedades de $\mathbb{R}^n$ cambian. Las dos lecciones previas de la unidad nos van a servir como contraste.

## Convenciones

Trabajamos en $\mathbb{Z}_2^n$ con $\mathbb{Z}_2=\{0,1\}$ y aritmética módulo $2$ (también escrito $\mathbb{F}_2$ o $\mathrm{GF}(2)$). Un **código lineal $(n,k)$** es un subespacio $\mathcal C\subseteq\mathbb{Z}_2^n$ de dimensión $k$. Su matriz generadora $G$ es de $k\times n$ y tiene por filas una base de $\mathcal C$ (se codifica $a\mapsto aG$ con $a\in\mathbb{Z}_2^k$ fila); su matriz de control de paridad $H$ es de $(n-k)\times n$ y cumple $\mathcal C=\operatorname{nul}(H)$, o sea $Hv^t=0\iff v\in\mathcal C$. El **peso** $w(v)$ es la cantidad de unos de $v$.

## El producto punto en $\mathbb{Z}_2^n$

:::note[Definición (producto punto en $\mathbb{Z}_2^n$)]
Para $x=(x_1,\dots,x_n)$ e $y=(y_1,\dots,y_n)$ en $\mathbb{Z}_2^n$,

$$
x\cdot y=x_1y_1+\dots+x_ny_n\in\mathbb{Z}_2\qquad(\text{suma módulo }2).
$$

Decimos que $x$ e $y$ son **ortogonales** si $x\cdot y=0$.
:::

Es **simétrico** y **bilineal** (como el producto punto de $\mathbb{R}^n$): $(x+x')\cdot y=x\cdot y+x'\cdot y$, $(ax)\cdot y=a(x\cdot y)$ para $a\in\mathbb{Z}_2$. Pero **no es un producto interno**: falla la positividad, y ni siquiera tiene sentido hablar de "positivo" porque $\mathbb{Z}_2$ no es un cuerpo ordenado. Lo que pasa en concreto es que, como $x_i^2=x_i$ en $\mathbb{Z}_2$,

$$
x\cdot x=x_1+\dots+x_n=w(x)\bmod2 .
$$

Entonces un vector es **ortogonal a sí mismo si y solo si su peso es par**, y hay vectores no nulos con esa propiedad, como $(1,1,0)$: $(1,1,0)\cdot(1,1,0)=1+1=0$. Consecuencias: no hay norma $\sqrt{x\cdot x}$, no hay ángulos, no valen Cauchy-Schwarz ni Gram-Schmidt. Sí siguen valiendo todas las propiedades que solo usan bilinealidad y simetría: se pueden definir el complemento ortogonal y probar su dimensión (que usa solamente el teorema de rango y nulidad), como hacemos a continuación. Lo que se pierde es $S\cap S^\perp=\{0\}$.

### Ejemplo 1 · Ortogonalidad en $\mathbb{Z}_2^n$
<!-- check: U4.T08.E1 -->

Sean $u=10110$ y $v=11101$ en $\mathbb{Z}_2^5$. Calcular $u\cdot v$ y $u\cdot u$, y hallar los vectores de $\mathbb{Z}_2^3$ ortogonales a sí mismos.

**Resolución.** $u\cdot v=1\cdot1+0\cdot1+1\cdot1+1\cdot0+0\cdot1=1+0+1+0+0=0$: son ortogonales. Además $u\cdot u=1+0+1+1+0=1$, que coincide con el peso $w(u)=3$ módulo $2$. El vector $11000$ cumple $11000\cdot11000=1+1=0$ y es no nulo.

En $\mathbb{Z}_2^3$ se tiene $x\cdot x=w(x)\bmod2$, de modo que los autoortogonales son los de peso par: $000$, $110$, $101$ y $011$. Forman un subespacio de dimensión $2$ (los vectores de peso par: es el núcleo de $x\mapsto x\cdot(1,1,1)$).

**Comprobación.** Para todo $x\in\mathbb{Z}_2^5$ vale $x\cdot x=w(x)\bmod2$: es una identidad por coordenadas, que se puede verificar en los $32$ vectores.

## Código dual

:::note[Definición (código dual)]
Si $\mathcal C\subseteq\mathbb{Z}_2^n$ es un código lineal, su **dual** (o complemento ortogonal) es

$$
\mathcal C^\perp=\{x\in\mathbb{Z}_2^n:\ x\cdot c=0\ \text{ para todo }c\in\mathcal C\}.
$$
:::

:::note[Teorema (dimensión y descripción del dual)]
Sea $\mathcal C$ un código $(n,k)$ con matriz generadora $G$ y matriz de control $H$. Entonces:

1. $\mathcal C^\perp=\operatorname{nul}(G)=\{x:\ Gx^t=0\}$, y es un código $(n,n-k)$.
2. $(\mathcal C^\perp)^\perp=\mathcal C$.
3. Las filas de $H$ generan $\mathcal C^\perp$: $\mathcal C^\perp=\operatorname{fil}(H)$.
:::

**Demostración.** (1) Sean $g_1,\dots,g_k$ las filas de $G$. Si $x\cdot g_i=0$ para todo $i$, entonces para $c=\sum a_ig_i\in\mathcal C$ se tiene $x\cdot c=\sum a_i(x\cdot g_i)=0$ por la bilinealidad; luego $x\in\mathcal C^\perp$. La recíproca es inmediata porque $g_i\in\mathcal C$. Así, $x\in\mathcal C^\perp\iff Gx^t=0$. Como $G$ tiene rango $k$, el teorema de rango y nulidad da $\dim\operatorname{nul}(G)=n-k$ (vale sobre cualquier cuerpo, también $\mathbb{Z}_2$).

(2) Por simetría, $c\cdot x=x\cdot c=0$ para todo $c\in\mathcal C$ y $x\in\mathcal C^\perp$; es decir, $\mathcal C\subseteq(\mathcal C^\perp)^\perp$. Por (1) aplicado dos veces, $\dim(\mathcal C^\perp)^\perp=n-(n-k)=k=\dim\mathcal C$. Un subespacio contenido en otro de la misma dimensión es igual a él.

(3) Que $\mathcal C=\operatorname{nul}(H)$ dice $\mathcal C=\operatorname{fil}(H)^\perp$ (un vector es ortogonal a todas las filas de $H$ si y solo si $Hv^t=0$). El argumento de (1) y (2) se aplica a cualquier subespacio $D\subseteq\mathbb{Z}_2^n$ (las dos pruebas usan solo bilinealidad, simetría y rango-nulidad), de modo que $D^{\perp\perp}=D$. Con $D=\operatorname{fil}(H)$ resulta $\mathcal C^\perp=(\operatorname{fil}(H)^\perp)^\perp=\operatorname{fil}(H)$. $\blacksquare$

Entonces: **el dual intercambia los papeles de $G$ y $H$.** $G$ es matriz de control de $\mathcal C^\perp$ y $H$ es matriz generadora de $\mathcal C^\perp$ (hay que leer $H$ con las filas como base; las $n-k$ filas de $H$ son LI).

### Ejemplo 2 · El dual de un código $(5,2)$
<!-- check: U4.T08.E2 -->

Sea $\mathcal C$ el código de matriz generadora $G=\begin{pmatrix}1&0&1&1&0\\0&1&0&1&1\end{pmatrix}$ y de matriz de control $H=\begin{pmatrix}1&0&1&0&0\\1&1&0&1&0\\0&1&0&0&1\end{pmatrix}$. Verificar $HG^t=0$, hallar $\mathcal C$ y $\mathcal C^\perp$ y la intersección $\mathcal C\cap\mathcal C^\perp$.

**Resolución.** $HG^t$ tiene por entradas los productos $h_i\cdot g_j$, que son todos cero (por ejemplo, $h_1\cdot g_1=1+1=0$ y $h_2\cdot g_2=1+1=0$): $HG^t=0$, y como $\operatorname{rango}(G)=2$ y $\operatorname{rango}(H)=3$ con $2+3=5$, $\mathcal C=\operatorname{nul}(H)$. Las palabras del código son las combinaciones de $g_1,g_2$:

$$
\mathcal C=\{00000,\ 10110,\ 01011,\ 11101\}.
$$

Por el teorema, $\mathcal C^\perp=\operatorname{fil}(H)$ tiene $n-k=3$ de dimensión y $2^3=8$ palabras: sumando las filas $h_1=10100$, $h_2=11010$ y $h_3=01001$ se obtiene

$$
\mathcal C^\perp=\{00000,\ 10100,\ 11010,\ 01001,\ 01110,\ 11101,\ 10011,\ 00111\}.
$$

La intersección es $\mathcal C\cap\mathcal C^\perp=\{00000,\ 11101\}$: la palabra $11101=g_1+g_2=h_1+h_3$ está en los dos y es ortogonal a sí misma ($w=4$ es par). En particular $\mathcal C\cap\mathcal C^\perp\neq\{0\}$ y $\mathbb{Z}_2^5\neq\mathcal C\oplus\mathcal C^\perp$, aunque $\dim\mathcal C+\dim\mathcal C^\perp=5$.

**Comprobación.** Se verifica por enumeración que los $8$ vectores de $\mathcal C^\perp$ son los únicos de $\mathbb{Z}_2^5$ ortogonales a $10110$ y a $01011$, y que $(\mathcal C^\perp)^\perp=\mathcal C$.

## Códigos autoduales

:::note[Definición (código autodual)]
Un código lineal $\mathcal C$ es **autodual** si $\mathcal C^\perp=\mathcal C$.
:::

:::note[Teorema]
Si $\mathcal C$ es un código autodual $(n,k)$, entonces:

1. $n=2k$.
2. Todas sus palabras tienen peso par.
3. El vector $\mathbf 1=(1,\dots,1)$ pertenece a $\mathcal C$.

Recíprocamente, si $n=2k$ y $GG^t=0$, el código es autodual.
:::

**Demostración.** (1) $k=\dim\mathcal C=\dim\mathcal C^\perp=n-k$. (2) Cada $c\in\mathcal C=\mathcal C^\perp$ cumple $c\cdot c=0$, o sea $w(c)$ par. (3) Para toda $c\in\mathcal C$, $\mathbf1\cdot c=c_1+\dots+c_n=w(c)\bmod2=0$ por (2). Entonces $\mathbf1\in\mathcal C^\perp=\mathcal C$. *Recíproca:* $GG^t=0$ significa $g_i\cdot g_j=0$ para todos $i,j$; por la bilinealidad cada palabra de $\mathcal C$ es ortogonal a las otras, es decir $\mathcal C\subseteq\mathcal C^\perp$, y con $\dim\mathcal C=k=n-k=\dim\mathcal C^\perp$ son iguales. $\blacksquare$

### Ejemplo 3 · El código de doble repetición de longitud 4
<!-- check: U4.T08.E3 -->

Sea $\mathcal C$ el código de $\mathbb{Z}_2^4$ con $G=\begin{pmatrix}1&1&0&0\\0&0&1&1\end{pmatrix}$ (cada bit del mensaje se repite dos veces). Probar que es autodual.

**Resolución.** Aquí $n=4$ y $k=2=n/2$. Además $g_1\cdot g_1=1+1=0$, $g_2\cdot g_2=1+1=0$ y $g_1\cdot g_2=0$, o sea $GG^t=0$. Por la recíproca del teorema, $\mathcal C^\perp=\mathcal C$. Las palabras son $\{0000,1100,0011,1111\}$: todas de peso par y $1111\in\mathcal C$, como dice el teorema.

**Comprobación.** $\mathcal C^\perp=\operatorname{nul}(G)=\{x:\ x_1+x_2=0,\ x_3+x_4=0\}=\{(a,a,b,b)\}=\mathcal C$. Su distancia mínima es $2$ (peso de $1100$), por lo que detecta un error pero no corrige ninguno.

El código de Hamming extendido $(8,4)$ de más abajo (Ejemplo 6) es otro ejemplo de código autodual, que además tiene distancia $4$.

## Distancia de Hamming

:::note[Definición (distancia de Hamming)]
Para $u,v\in\mathbb{Z}_2^n$, $d_H(u,v)=w(u+v)$ es la cantidad de posiciones en que $u$ y $v$ difieren.
:::

Es la distancia que importa en comunicaciones: cuenta cuántos bits se cambiaron.

:::note[Propiedad (métrica)]
Para todos $u,v,z\in\mathbb{Z}_2^n$:

1. $d_H(u,v)\ge0$, y $d_H(u,v)=0$ si y solo si $u=v$.
2. $d_H(u,v)=d_H(v,u)$.
3. $d_H(u,z)\le d_H(u,v)+d_H(v,z)$ (desigualdad triangular).
:::

**Demostración.** (1) y (2) son inmediatas: $u+v=0$ si y solo si $u=v$, y $u+v=v+u$. (3) Sean $x=u+v$ e $y=v+z$, de modo que $u+z=x+y$. Si $(x+y)_i=1$, alguna de las dos coordenadas $x_i$ o $y_i$ vale $1$ (en caso contrario la suma sería $0$). Entonces las posiciones donde $x+y$ vale $1$ están contenidas en la unión de las de $x$ y las de $y$, y $w(x+y)\le w(x)+w(y)$. Es decir, $d_H(u,z)\le d_H(u,v)+d_H(v,z)$. $\blacksquare$

Es entonces una **métrica**, como la distancia euclídea de la lección [4.2](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/), pero **no proviene de un producto interno**: en $\mathbb{Z}_2^n$ no existe producto interno, y por eso aparecen fenómenos sin análogo euclídeo (no hay ángulos, ni "distancia al cuadrado igual a producto"). Además es invariante por traslaciones: $d_H(u+z,v+z)=d_H(u,v)$.

## Distancia mínima

:::note[Definición (distancia mínima)]
La **distancia mínima** de un código $\mathcal C$ con al menos dos palabras es

$$
d(\mathcal C)=\min\{d_H(u,v):\ u,v\in\mathcal C,\ u\neq v\}.
$$

Un código lineal $(n,k)$ con distancia mínima $d$ se denota $(n,k,d)$.
:::

Calcularla con la definición exigiría comparar todos los pares. Para códigos lineales alcanza con mirar los pesos:

:::note[Teorema]
Si $\mathcal C$ es un código lineal no nulo, $d(\mathcal C)$ es el menor peso de una palabra no nula: $d(\mathcal C)=\min\{w(c):\ c\in\mathcal C,\ c\neq0\}$.
:::

**Demostración.** Si $u\neq v$ están en $\mathcal C$, entonces $u+v\in\mathcal C$ es no nula y $d_H(u,v)=w(u+v)\ge m$, donde $m$ es el menor peso no nulo. Recíprocamente, si $c\in\mathcal C$ es no nula con $w(c)=m$, entonces $d_H(c,0)=m$ con $c\neq0$ y $0\in\mathcal C$. Luego $d(\mathcal C)=m$. $\blacksquare$

También se puede leer en $H$: $c$ es palabra del código si y solo si $Hc^t=0$, es decir, si la suma de las columnas de $H$ en las posiciones donde $c$ vale $1$ es cero. Por lo tanto, $d(\mathcal C)$ es la menor cantidad de columnas de $H$ linealmente dependientes (una dependencia con $m$ columnas es una palabra de peso $m$). En particular, **$d\ge3$ si y solo si las columnas de $H$ son no nulas y distintas entre sí.**

## Detección y corrección de errores

Se transmite una palabra $c\in\mathcal C$ y se recibe $r=c+e$, donde $e\in\mathbb{Z}_2^n$ es el **vector de error** ($w(e)$ es la cantidad de bits cambiados). El receptor decodifica por el **vecino más próximo**: elige la palabra de $\mathcal C$ más cercana a $r$ en distancia de Hamming.

:::note[Teorema (detección y corrección)]
Sea $\mathcal C$ un código con distancia mínima $d$.

1. $\mathcal C$ **detecta** hasta $d-1$ errores: si $1\le w(e)\le d-1$, entonces $r\notin\mathcal C$.
2. $\mathcal C$ **corrige** hasta $t=\lfloor(d-1)/2\rfloor$ errores: si $w(e)\le t$, la palabra de $\mathcal C$ más cercana a $r$ es única y es $c$.
:::

**Demostración.** (1) Si $r=c+e\in\mathcal C$ con $e\neq0$, entonces $r$ sería otra palabra del código a distancia $d_H(r,c)=w(e)\le d-1<d$ de $c$, contra la definición de $d$. (2) Sea $w(e)\le t$, de modo que $d_H(r,c)\le t$. Si otra palabra $c'\neq c$ estuviera a distancia $d_H(r,c')\le t$, la desigualdad triangular daría $d_H(c,c')\le d_H(c,r)+d_H(r,c')\le2t\le d-1<d$, contra la definición de $d$. Así, las bolas de radio $t$ alrededor de las palabras del código son disjuntas, y la palabra más cercana a $r$ es $c$. $\blacksquare$

| Distancia mínima $d$ | Errores detectados | Errores corregidos |
|---|---|---|
| $2$ | $1$ | $0$ |
| $3$ | $2$ | $1$ |
| $4$ | $3$ | $1$ |
| $5$ | $4$ | $2$ |

La cota es ajustada: con $d=3$ hay palabras $c,c'$ a distancia $3$, y con dos errores sobre $c$ se puede llegar a un vector que está a distancia $1$ de $c'$, que se decodifica mal como $c'$. Detección y corrección no son excluyentes: con un código que corrige $t$ errores se pueden detectar más si se renuncia a corregir.

## Decodificación por síndrome

Comparar $r$ con las $2^k$ palabras es costoso. La matriz $H$ ofrece un atajo. El **síndrome** de $r$ es $s=Hr^t\in\mathbb{Z}_2^{n-k}$. Como $r=c+e$ y $Hc^t=0$,

$$
s=Hr^t=Hc^t+He^t=He^t .
$$

**El síndrome solo depende del error**, no de la palabra enviada. Si $s=0$, se acepta $r$ (no hay errores detectables). Si $s\neq0$, se busca el **patrón de error de menor peso** con $He^t=s$ y se corrige $c=r+e$. Como $He^t$ es la suma de las columnas de $H$ en las posiciones del error, **un error simple en la posición $j$ produce como síndrome la columna $j$ de $H$**. Si las columnas de $H$ son no nulas y distintas, un solo error siempre se identifica y se corrige.

### Ejemplo 4 · Decodificación de un código $(5,2)$ con tabla de síndromes
<!-- check: U4.T08.E4 -->

Sea el código del Ejemplo 2, con $H=\begin{pmatrix}1&0&1&0&0\\1&1&0&1&0\\0&1&0&0&1\end{pmatrix}$. Las columnas de $H$ son $110$, $011$, $100$, $010$ y $001$: no nulas y distintas, y $d(\mathcal C)=3$ (menor peso de $10110$, $01011$, $11101$). El código corrige $\lfloor(3-1)/2\rfloor=1$ error. La tabla con el patrón de error de menor peso para cada uno de los $2^3=8$ síndromes es:

| Síndrome | Patrones de error de peso mínimo | Decisión |
|---|---|---|
| $000$ | $00000$ | sin errores |
| $110$ | $10000$ | corregir bit 1 |
| $011$ | $01000$ | corregir bit 2 |
| $100$ | $00100$ | corregir bit 3 |
| $010$ | $00010$ | corregir bit 4 |
| $001$ | $00001$ | corregir bit 5 |
| $101$ | $11000$ y $00101$ | dos errores: se detecta, no se corrige |
| $111$ | $01100$ y $10001$ | dos errores: se detecta, no se corrige |

Los síndromes $101$ y $111$ no son columnas de $H$; cada uno tiene dos patrones de peso $2$ y no hay una elección única.

*Caso 1.* Se envía $a=(1,1)$, que se codifica $c=aG=g_1+g_2=11101$. Se recibe $r=11001$. Calculamos $h_1\cdot r=1+0+0+0+0=1$, $h_2\cdot r=1+1+0+0+0=0$ y $h_3\cdot r=0+1+0+0+1=0$, o sea $s=(1,0,0)^t$, que es la columna $3$ de $H$. Se corrige el bit $3$: $c=11101$. Como $G$ tiene identidad en las dos primeras columnas, el mensaje son los primeros dos bits: $a=(1,1)$.

*Caso 2.* Se recibe $r=01110$. El síndrome es $s=(1,0,1)$: no es una columna de $H$; hay (al menos) dos errores. Las distancias de $r$ a las cuatro palabras del código son $2,2,3,3$: dos palabras a distancia mínima. Se detecta el error pero no hay una corrección única.

**Comprobación.** Para $r=11001$, las distancias a $\mathcal C$ son $1,2,3,4$ (única a distancia $1$: $11101$). Para $r=01110$ son $2,2,3,3$.

## Códigos de Hamming

El **código de Hamming $(7,4)$** se define por la matriz de control cuyas columnas son todos los vectores no nulos de $\mathbb{Z}_2^3$, ordenados como los números $1,\dots,7$ escritos en binario:

$$
H=\begin{pmatrix}0&0&0&1&1&1&1\\0&1&1&0&0&1&1\\1&0&1&0&1&0&1\end{pmatrix}.
$$

La columna $j$ es la escritura binaria de $j$. Una matriz generadora es

$$
G=\begin{pmatrix}1&1&1&0&0&0&0\\1&0&0&1&1&0&0\\0&1&0&1&0&1&0\\1&1&0&1&0&0&1\end{pmatrix},
$$

con $HG^t=0$ y rango $4$. Las posiciones $3,5,6,7$ de $aG$ son las cuatro coordenadas del mensaje $a$, y las posiciones $1,2,4$ son de control.

:::note[Dos presentaciones del mismo código]
En la [lección 1.10](/algebra-ii/unidad-1/teoria/codigos-lineales/) las columnas de $H$ se ordenaron para
obtener la forma sistemática $H=(A^t\mid I_3)$. Acá se ordenan como los números en binario, lo que tiene una
ventaja práctica: el síndrome de un error simple, leído en binario, **es** la posición del bit equivocado.
Los dos códigos se obtienen uno del otro permutando las posiciones de todas las palabras (son
*equivalentes*): tienen la misma longitud, dimensión y distancia mínima, y corrigen los mismos errores.
:::

### Ejemplo 5 · El código de Hamming $(7,4)$
<!-- check: U4.T08.E5 -->

Hallar la distancia mínima del código de Hamming $(7,4)$ y decodificar una palabra con un error.

**Resolución.** *Distancia $3$.* Las siete columnas de $H$ son no nulas y distintas: por el criterio de las columnas, $d\ge3$. Además la columna $1$ más la columna $2$ es la columna $3$, de modo que $c=1110000$ cumple $Hc^t=0$ y $w(c)=3$: entonces $d=3$. El código tiene $16$ palabras, con $1$ de peso $0$, $7$ de peso $3$, $7$ de peso $4$ y $1$ de peso $7$. Corrige $1$ error y detecta $2$. Es un código **perfecto**: las bolas de radio $1$ tienen $1+7=8$ palabras y $16\cdot8=128=2^7$ cubren todo $\mathbb{Z}_2^7$.

*Decodificación.* Como la columna $j$ de $H$ es $j$ en binario, el síndrome de un error en la posición $j$ **es $j$ escrito en binario**. Para $a=(1,0,1,1)$, $c=aG=0110011$. Si se recibe $r=0110001$ (cambió el bit $6$), el síndrome es $Hr^t=(1,1,0)^t$, que es $110_2=6$: se corrige el bit $6$ y se recupera $c$. El mensaje está en las posiciones $3,5,6,7$ de $c$: $(1,0,1,1)$.

**Comprobación.** $HG^t=0$; las filas de $G$ son LI (rango $4$) y generan exactamente $\operatorname{nul}(H)$, que tiene $2^4=16$ palabras; $c=0110011$ cumple $Hc^t=0$ y $0110011+0110001=0000010$ tiene peso $1$.

### Ejemplo 6 · El código de Hamming extendido $(8,4)$
<!-- check: U4.T08.E6 -->

Extender el código de Hamming $(7,4)$ con un bit de paridad global, probar que el resultado es autodual, hallar su distancia mínima y decodificar tres palabras recibidas.

**Resolución.** Agregamos a cada fila de $G$ un bit de paridad (el peso de la fila módulo $2$): las filas de $G_8$ son

$$
11100001,\quad10011001,\quad01010101,\quad11010010 .
$$

Es el código de $\mathbb{Z}_2^8$ formado por las palabras de Hamming con un bit de paridad al final. Cada fila tiene peso par y las cuatro son ortogonales dos a dos, de modo que $G_8G_8^t=0$; como $n=8=2\cdot4$, **es autodual**. Sus pesos son $0$ (una palabra), $4$ (catorce palabras) y $8$ (una): $d=4$. Se entiende por qué: el código de Hamming tiene peso mínimo $3$, el bit de paridad vuelve pares todos los pesos, y por eso el peso mínimo del extendido es $4$ (lo alcanza $11100001$). La matriz de control es

$$
H_8=\begin{pmatrix}0&0&0&1&1&1&1&0\\0&1&1&0&0&1&1&0\\1&0&1&0&1&0&1&0\\1&1&1&1&1&1&1&1\end{pmatrix}
$$

y, por ser autodual, sus filas son palabras del código. El síndrome $s=(s_1,s_2,s_3,s_4)$ se interpreta así: si $s_4=1$ hay un número impar de errores y se supone uno solo, cuya posición es $s_1s_2s_3$ en binario (con $000$ se refiere a la posición $8$); si $s_4=0$ y $s\neq0$ hay un número par de errores (dos o más): se detecta, no se corrige. Para $a=(1,0,1,1)$, $c=01100110$ y los casos son:

| Errores en las posiciones | Síndrome | Interpretación |
|---|---|---|
| ninguno | $0000$ | sin errores |
| $5$ | $1011$ | $s_4=1$, posición $101_2=5$: se corrige |
| $8$ | $0001$ | $s_4=1$, posición $000$: el bit $8$ |
| $2$ y $6$ | $1000$ | $s_4=0$ y $s\neq0$: dos errores, solo se detectan |

El extendido corrige $1$ error y detecta $2$ ($d=4$), a costa de un bit más por palabra.

**Comprobación.** Cada fila de $H_8$ pertenece al código (por ser autodual) y los síndromes de la tabla salen de sumar las columnas de $H_8$ en las posiciones de error: por ejemplo, las columnas $2$ y $6$ son $(0,1,0,1)$ y $(1,1,0,1)$, y su suma es $(1,0,0,0)$.

### Vínculo con el trabajo práctico

El trabajo práctico de la unidad pide aplicar los espacios con producto interno al código de Hamming. Los pasos de esta lección son el esqueleto: construir $H$ y $G$, verificar $HG^t=0$, calcular $d$, codificar un mensaje, perturbar $1$ y $2$ bits y decodificar con el síndrome. Los ejemplos de arriba se pueden repetir con otros mensajes.

:::caution[Errores frecuentes]
- **Suponer $x\cdot x=0\Rightarrow x=0$ en $\mathbb{Z}_2^n$.** Falla: $x\cdot x=w(x)\bmod2$ y los vectores de peso par no nulos son autoortogonales.
- **Aplicar $S\cap S^\perp=\{0\}$ a códigos.** En el Ejemplo 2, $\mathcal C\cap\mathcal C^\perp=\{00000,11101\}$.
- **Mezclar los roles de $G$ y $H$.** $\mathcal C=\operatorname{fil}(G)=\operatorname{nul}(H)$ y $\mathcal C^\perp=\operatorname{fil}(H)=\operatorname{nul}(G)$.
- **Calcular $d(\mathcal C)$ como la menor distancia entre un par cualquiera sin usar linealidad**, o confundirla con la menor distancia a una palabra recibida. En un código lineal, $d$ es el menor peso no nulo.
- **Creer que "detecta $t$" y "corrige $t$" son lo mismo.** Con $d=4$ se detectan $3$ errores pero solo se corrige $1$.
- **Corregir cuando hay empate.** Si hay varios patrones de error de peso mínimo para un síndrome, el receptor solo puede detectar.
- **Calcular el síndrome como $Hr$ con $r$ fila.** $r$ debe ser columna: $Hr^t$.
- **Creer que Hamming extendido corrige $2$ errores.** Corrige $1$ y detecta $2$.
:::

## Autoevaluación

<details>
<summary>1. ¿Existe un código autodual de longitud 5?</summary>

No: $n=2k$ obliga a que $n$ sea par.

</details>

<details>
<summary>2. Si un código tiene d = 6, ¿cuántos errores detecta y corrige?</summary>

Detecta $5$ y corrige $\lfloor5/2\rfloor=2$.

</details>

<details>
<summary>3. Probar que si todas las palabras de un código lineal tienen peso par, entonces 1 = (1, …, 1) pertenece a su dual.</summary>

$\mathbf1\cdot c=c_1+\dots+c_n=w(c)\bmod2=0$ para toda $c\in\mathcal C$, así que $\mathbf1\in\mathcal C^\perp$.

</details>

:::tip[En resumen]
- En $\mathbb{Z}_2^n$ el producto punto es bilineal y simétrico pero **no** es un producto interno: $x\cdot x=w(x)\bmod2$, y un vector no nulo puede ser ortogonal a sí mismo.
- $\mathcal C^\perp=\operatorname{nul}(G)=\operatorname{fil}(H)$ es un código $(n,n-k)$ y $(\mathcal C^\perp)^\perp=\mathcal C$; en general $\mathcal C\cap\mathcal C^\perp\neq\{0\}$.
- Autodual ($\mathcal C^\perp=\mathcal C$) implica $n=2k$, pesos pares y $\mathbf1\in\mathcal C$; la doble repetición de longitud $4$ y el Hamming extendido $(8,4)$ son autoduales.
- $d_H(u,v)=w(u+v)$ es una métrica; para un código lineal, $d(\mathcal C)$ es el menor peso no nulo y es el menor número de columnas LD de $H$.
- Con distancia mínima $d$, el código detecta $d-1$ errores y corrige $\lfloor(d-1)/2\rfloor$. Hamming $(7,4)$: $d=3$; extendido $(8,4)$: $d=4$.
- Decodificación por síndrome: $s=Hr^t=He^t$; un error simple en la posición $j$ da la columna $j$ de $H$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 5.5, "Aplicaciones: códigos duales" (p. 419–425); sección 7.2, "Normas y funciones de distancia" (p. 576–578, norma y distancia de Hamming); sección 7.5, "Aplicaciones: códigos de corrección de error" (p. 640–645). Poole usa $G$ de $n\times k$ y $P$ para la matriz de control (ver la nota de equivalencias en la [notación](/algebra-ii/notacion/)).
- Nakos y Joyner, *Álgebra lineal con aplicaciones* (Thomson, 1999): el libro al que remite el programa para la teoría de códigos.
- Anterior: [4.7 Cuadrados mínimos](/algebra-ii/unidad-4/teoria/cuadrados-minimos/). Previo: [1.10 Códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/) y [1.1 Cuerpos y $\mathbb{Z}_2$](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/).
- Repaso: [vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/).
