---
title: Independencia lineal
description: Independencia y dependencia lineal como ausencia de generadores redundantes, criterios por sistemas, determinantes y rango, interpretación geométrica, propiedades demostradas y dependencia del cuerpo de escalares.
slug: algebra-ii/unidad-1/teoria/independencia-lineal
sidebar:
  order: 5
  label: 1.5 Independencia lineal
---

## Para qué sirve

Un generador puede tener vectores de más. En $\mathbb{R}^2$, los vectores $(1,2)$, $(2,4)$ y $(3,6)$
generan una recta, la misma que genera $(1,2)$ solo: los otros dos **no aportan nada nuevo**. Reconocer
esa redundancia permite describir un subespacio con la menor cantidad posible de vectores, que es lo que
hace una base.

La redundancia tiene un lado útil en informática. Un bloque de paridad es redundante a propósito: es la
suma de los demás, y esa dependencia es la que permite reconstruir un bloque perdido (ver el ejemplo de
[espacios vectoriales](/algebra-ii/unidad-1/teoria/espacios-vectoriales/)). Un código corrector agrega
bits que dependen linealmente de los de información. En cambio, en un sistema de ecuaciones, una ecuación
dependiente de las otras es una fila que no informa nada. Distinguir ambos casos es el
objetivo de esta lección.

Usamos [combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/) y el cálculo del
rango por escalonamiento ([sistemas lineales](/algebra-ii/repaso/sistemas-lineales/)).

## Definición

La idea es: un conjunto es dependiente si alguno de sus vectores se puede escribir con los otros. Para
no tener que decir "alguno" ni excluir casos, se usa una formulación equivalente con una sola ecuación.

:::note[Definición]
Sea $V$ un espacio vectorial sobre $K$. Los vectores $v_1,\dots,v_k\in V$ son **linealmente
independientes** (LI) si la única combinación lineal nula es la trivial:

$$
\alpha_1v_1+\dots+\alpha_kv_k=0_V\ \Longrightarrow\ \alpha_1=\dots=\alpha_k=0 .
$$

Son **linealmente dependientes** (LD) si existen escalares $\alpha_1,\dots,\alpha_k$, **no todos
nulos**, con $\alpha_1v_1+\dots+\alpha_kv_k=0_V$. Esa igualdad es una **relación de dependencia**.
:::

Dos aclaraciones. La combinación trivial siempre da $0_V$; independencia significa que es la **única**.
Y "linealmente independiente" es una propiedad de la lista de vectores: si un vector se repite, la lista
es dependiente ($1\cdot v+(-1)\cdot v=0$).

:::note[Teorema (caracterización)]
Sean $v_1,\dots,v_k\in V$.

1. Si $k=1$: $\{v_1\}$ es LD si y solo si $v_1=0_V$.
2. Si $k\ge2$: $\{v_1,\dots,v_k\}$ es LD si y solo si **algún** $v_j$ es combinación lineal de los
   demás.
:::

**Demostración.** (1) Si $v_1=0_V$, $1\cdot v_1=0_V$ es una relación con coeficiente no nulo. Si
$\alpha v_1=0_V$ con $\alpha\neq0$, entonces $v_1=\alpha^{-1}(\alpha v_1)=0_V$ (propiedad 7 de los
espacios vectoriales); luego si $v_1\neq0_V$ solo vale $\alpha=0$.

(2) ($\Rightarrow$) Sea $\sum\alpha_iv_i=0_V$ con algún $\alpha_j\neq0$. Despejando,
$v_j=-\alpha_j^{-1}\sum_{i\neq j}\alpha_iv_i$, combinación lineal de los otros. ($\Leftarrow$) Si
$v_j=\sum_{i\neq j}\beta_iv_i$, entonces $\sum_{i\neq j}\beta_iv_i+(-1)v_j=0_V$ es una relación con
coeficiente $-1\neq0$ en $v_j$. $\blacksquare$

La palabra "algún" es esencial: en un conjunto dependiente **no** todos los vectores son combinación de
los otros. En $\{(1,0),(2,0),(0,1)\}$, el vector $(0,1)$ no es combinación de los otros dos, pero el
conjunto es dependiente porque $(2,0)=2(1,0)$.

## Cómo decidir si un conjunto es independiente

Sea $A=(v_1\mid\cdots\mid v_k)\in K^{n\times k}$ la matriz de columnas $v_i$. La combinación
$\alpha_1v_1+\dots+\alpha_kv_k$ es $A\alpha$, de modo que:

$$
v_1,\dots,v_k\ \text{LI}\iff A\alpha=0\ \text{solo tiene la solución trivial}\iff\operatorname{nul}(A)=\{0\}\iff\operatorname{rango}(A)=k .
$$

De acá salen los criterios prácticos.

1. **Sistema homogéneo / rango.** Se escalona $A$. Si hay un pivote en cada columna, son LI; si hay una
   columna sin pivote (variable libre), son LD, y la solución no trivial da una relación de dependencia.
   También se pueden poner los vectores como **filas**: el rango es el mismo, y el conjunto es LI si no
   aparece ninguna fila nula al escalonar.
2. **Determinante** (solo si hay tantos vectores como componentes, $k=n$). $v_1,\dots,v_n\in K^n$ son LI
   si y solo si $\det(A)\neq0$ (ver [determinantes](/algebra-ii/repaso/determinantes/)). En $\mathbb{Z}_2$
   el determinante se calcula en $\mathbb{Z}_2$: es el resto módulo $2$ del determinante entero.
3. **Un vector es combinación de los otros.** Si se encuentra uno que lo es, el conjunto es LD (teorema
   anterior). Sirve para dar una respuesta rápida, pero la falta de ese vector "a ojo" no prueba
   independencia.
4. **Dos vectores:** $\{u,v\}$ es LD si y solo si uno es múltiplo del otro (proporcionales).
5. **Demasiados vectores.** Más de $n$ vectores de $K^n$ siempre son LD: el rango es a lo sumo $n$ y hay
   más de $n$ columnas. (Se prueba en [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/).)

En $P_n[\mathbb{R}]$, $\mathbb{R}^{m\times n}$ y subespacios en general, se pasa a coordenadas: por el
teorema de [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/), un conjunto es LI en $V$ si y solo
si lo son sus vectores de coordenadas en $K^n$.

## Interpretación geométrica

- En $\mathbb{R}^2$: dos vectores son LD si y solo si son **colineales** (están en una misma recta por el
  origen) y LI si apuntan en direcciones distintas. Tres vectores de $\mathbb{R}^2$ son siempre LD.
- En $\mathbb{R}^3$: dos vectores son LD si son colineales; tres vectores son LD si y solo si son
  **coplanares** (están en un mismo plano por el origen), y LI si "salen" del plano que generan los
  otros dos. Cuatro vectores de $\mathbb{R}^3$ son siempre LD.
- Un conjunto que contiene al vector nulo es LD, porque el nulo es "colineal con todo".

<figure class="math-figure">
<svg viewBox="-200 -85 400 160" role="img" aria-labelledby="il-t il-d" xmlns="http://www.w3.org/2000/svg">
<title id="il-t">Vectores independientes y dependientes en el plano</title>
<desc id="il-d">A la izquierda, los vectores u = (2, 1) y v = (1, 2) con unidad de 20 píxeles apuntan en direcciones distintas y el paralelogramo que forman cubre el plano: son linealmente independientes. A la derecha, u = (2, 1) y w = (−4, −2) están sobre la misma recta por el origen, trazada en líneas de trazos: son linealmente dependientes porque w = −2u.</desc>
<defs><marker id="il-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker><marker id="il-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="translate(-100,0) scale(1,-1)">
<line class="axis" x1="-70" y1="0" x2="70" y2="0"/>
<line class="axis" x1="0" y1="-60" x2="0" y2="70"/>
<line class="guide" x1="40" y1="20" x2="60" y2="60"/>
<line class="guide" x1="20" y1="40" x2="60" y2="60"/>
<line class="vec-a" x1="0" y1="0" x2="40" y2="20" marker-end="url(#il-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="20" y2="40" marker-end="url(#il-arrow-b)"/>
</g>
<g transform="translate(100,0) scale(1,-1)">
<line class="axis" x1="-70" y1="0" x2="70" y2="0"/>
<line class="axis" x1="0" y1="-60" x2="0" y2="70"/>
<line class="guide" x1="-90" y1="-45" x2="70" y2="35"/>
<line class="vec-a" x1="0" y1="0" x2="40" y2="20" marker-end="url(#il-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="-80" y2="-40" marker-end="url(#il-arrow-b)"/>
</g>
<text x="-100" y="-72" text-anchor="middle">u, v independientes</text>
<text x="100" y="-72" text-anchor="middle">u, w dependientes</text>
<text class="math" x="-56" y="-26">u</text>
<text class="math" x="-90" y="-46">v</text>
<text class="math" x="144" y="-26">u</text>
<text class="math" x="22" y="56">w</text>
</svg>
<figcaption>A la izquierda, u y v apuntan en direcciones distintas: ninguno es múltiplo del otro y juntos generan todo el plano. A la derecha, w = −2u cae sobre la misma recta que u (trazos): el par genera solo esa recta y sobra uno de los dos.</figcaption>
</figure>

## Propiedades

:::note[Propiedades]
Sea $V$ un espacio vectorial.

1. Todo subconjunto de un conjunto LI es LI.
2. Todo conjunto que contiene al vector nulo es LD.
3. Si $\{v_1,\dots,v_k\}$ es LI y $v\notin\operatorname{gen}\{v_1,\dots,v_k\}$, entonces
   $\{v_1,\dots,v_k,v\}$ es LI. Recíprocamente, si $\{v_1,\dots,v_k\}$ es LI y
   $\{v_1,\dots,v_k,v\}$ es LD, entonces $v\in\operatorname{gen}\{v_1,\dots,v_k\}$.
4. Si $\{v_1,\dots,v_k\}$ es LI, cada vector de $\operatorname{gen}\{v_1,\dots,v_k\}$ se escribe de
   **una única** manera como combinación lineal de $v_1,\dots,v_k$.
:::

**Demostración.**

1. Sea $\{v_1,\dots,v_k\}$ LI y $\{v_{i_1},\dots,v_{i_m}\}$ un subconjunto. Si
   $\sum_{j}\beta_jv_{i_j}=0_V$, completamos con coeficiente $0$ en los vectores que faltan y obtenemos
   una combinación nula de todos los $v_i$; por independencia, todos los coeficientes, en particular los
   $\beta_j$, son $0$.
2. Si $v_j=0_V$, entonces $1\cdot v_j+\sum_{i\neq j}0\cdot v_i=0_V$ es una relación con un coeficiente no
   nulo.
3. Sea $c\,v+c_1v_1+\dots+c_kv_k=0_V$. Si fuera $c\neq0$, despejaríamos
   $v=-c^{-1}(c_1v_1+\dots+c_kv_k)\in\operatorname{gen}\{v_1,\dots,v_k\}$, contra la hipótesis. Luego
   $c=0$, queda $c_1v_1+\dots+c_kv_k=0_V$ y, por independencia, $c_1=\dots=c_k=0$. Para la recíproca:
   en una relación no trivial $c\,v+\sum c_iv_i=0_V$ debe ser $c\neq0$ (si $c=0$, quedaría una relación
   no trivial entre los $v_i$, que son LI), y se despeja $v$ como antes.
4. Si $\sum\alpha_iv_i=\sum\beta_iv_i$, entonces $\sum(\alpha_i-\beta_i)v_i=0_V$ y la independencia da
   $\alpha_i=\beta_i$ para todo $i$. $\blacksquare$

La propiedad 3 es el paso de construcción de bases: se agregan vectores fuera del generado y la
independencia se conserva. La propiedad 4 es la unicidad de coordenadas
([coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/)).

## La independencia depende del cuerpo

Los criterios usan el cuerpo $K$ en cada cuenta (restar, dividir por pivotes). Un mismo conjunto de
vectores con entradas $0$ y $1$ puede ser LI sobre $\mathbb{R}$ y LD sobre $\mathbb{Z}_2$, porque en
$\mathbb{Z}_2$ aparecen relaciones como $1+1=0$ que no existen en $\mathbb{R}$. El ejemplo 1 lo muestra
con un conjunto concreto y el ejemplo 3 con vectores abstractos.

## Ejemplos resueltos

### Ejemplo 1 · El mismo conjunto, independiente en ℝ³ y dependiente en ℤ₂³
<!-- check: U1.T05.E1 -->

Sean $v_1=(1,1,0)$, $v_2=(0,1,1)$ y $v_3=(1,0,1)$. Decidir si son LI en $\mathbb{R}^3$ y en
$\mathbb{Z}_2^3$.

**Sobre $\mathbb{R}$.** Con los vectores como columnas:

$$
\begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix}
\xrightarrow{F_2-F_1\to F_2}
\begin{pmatrix}1&0&1\\0&1&-1\\0&1&1\end{pmatrix}
\xrightarrow{F_3-F_2\to F_3}
\begin{pmatrix}1&0&1\\0&1&-1\\0&0&2\end{pmatrix}.
$$

Tres pivotes: son LI. El determinante es $1\cdot1\cdot2=2\neq0$. Directamente: si
$a v_1+b v_2+c v_3=(a+c,\ a+b,\ b+c)=0$, entonces $a=-c$, $b=-a=c$ y $b+c=2c=0$, así que $c=0$ y, por
lo tanto, $a=b=0$.

**Sobre $\mathbb{Z}_2$.** Ahora $-1=1$ y $2=0$:

$$
\begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix}
\xrightarrow{F_2+F_1\to F_2}
\begin{pmatrix}1&0&1\\0&1&1\\0&1&1\end{pmatrix}
\xrightarrow{F_3+F_2\to F_3}
\begin{pmatrix}1&0&1\\0&1&1\\0&0&0\end{pmatrix}.
$$

Solo dos pivotes: hay una variable libre y los vectores son LD. El determinante $2$ es $0$ módulo $2$.
La relación de dependencia sale de la solución del sistema homogéneo, $(a,b,c)=(1,1,1)$:

$$
v_1+v_2+v_3=(1+0+1,\ 1+1+0,\ 0+1+1)=(0,0,0).
$$

Equivalentemente, $v_1+v_2=v_3$: el tercero es la suma de los otros dos.

**Comprobación.** Sobre $\mathbb{R}$ los tres vectores generan $\mathbb{R}^3$ (rango $3$). Sobre
$\mathbb{Z}_2$ generan un subespacio de dimensión $2$ con $4$ elementos: $(0,0,0)$, $(1,1,0)$, $(0,1,1)$
y $(1,0,1)$. El vector $(1,1,1)$ de $\mathbb{Z}_2^3$ no pertenece a ese subespacio.

:::tip[Resultado]
$\{v_1,v_2,v_3\}$ es LI sobre $\mathbb{R}$ y LD sobre $\mathbb{Z}_2$ (con $v_1+v_2+v_3=0$).
:::

### Ejemplo 2 · Un parámetro: cuándo son dependientes
<!-- check: U1.T05.E2 -->

Para cada $k\in\mathbb{R}$ sean $v_1=(1,1,1)$, $v_2=(1,2,4)$ y $v_3=(1,k,k^2)$. Hallar los $k$ para los
que $\{v_1,v_2,v_3\}$ es LD.

Ponemos los vectores como **filas** (el rango no cambia al transponer) y escalonamos:

$$
\begin{pmatrix}1&1&1\\1&2&4\\1&k&k^2\end{pmatrix}
\xrightarrow[F_3-F_1\to F_3]{F_2-F_1\to F_2}
\begin{pmatrix}1&1&1\\0&1&3\\0&k-1&k^2-1\end{pmatrix}
\xrightarrow{F_3-(k-1)F_2\to F_3}
\begin{pmatrix}1&1&1\\0&1&3\\0&0&k^2-3k+2\end{pmatrix}.
$$

El último elemento es $k^2-1-3(k-1)=k^2-3k+2=(k-1)(k-2)$. Hay tres pivotes si y solo si
$(k-1)(k-2)\neq0$. Entonces los vectores son LD exactamente para $k=1$ y $k=2$.

**Interpretación.** Para $k=1$, $v_3=(1,1,1)=v_1$; para $k=2$, $v_3=(1,2,4)=v_2$: en ambos casos hay un
vector repetido. Para cualquier otro $k$ son LI. Por ejemplo, con $k=3$ el último pivote es $2$.

**Comprobación.** El determinante de la matriz es $(k-1)(k-2)$ (es un determinante de Vandermonde); para
$k=0$ da $2$, para $k=3$ da $2$, para $k=1$ y $k=2$ da $0$.

:::tip[Resultado]
$\{v_1,v_2,v_3\}$ es LD si y solo si $k\in\{1,2\}$.
:::

### Ejemplo 3 · Vectores abstractos: el cuerpo decide
<!-- check: U1.T05.E3 -->

Sea $V$ un espacio vectorial sobre $K$ y $\{u,v,w\}$ un conjunto LI. Estudiar la independencia de
$\{u+v,\ u-v,\ w\}$ cuando $K=\mathbb{R}$ y cuando $K=\mathbb{Z}_2$.

Planteamos $a(u+v)+b(u-v)+c\,w=0_V$. Agrupando según $u,v,w$:

$$
(a+b)\,u+(a-b)\,v+c\,w=0_V .
$$

Como $\{u,v,w\}$ es LI, los tres coeficientes son nulos: $a+b=0$, $a-b=0$, $c=0$. Sumando las dos
primeras, $2a=0$.

- **Si $K=\mathbb{R}$** (o cualquier cuerpo donde $2\neq0$), $a=0$, luego $b=0$ y $c=0$: el conjunto es
  **LI**. Matricialmente, la matriz de coordenadas $\begin{pmatrix}1&1&0\\1&-1&0\\0&0&1\end{pmatrix}$
  tiene determinante $-2\neq0$.
- **Si $K=\mathbb{Z}_2$**, $2a=0$ no obliga a $a=0$: la solución $a=b=1$, $c=0$ cumple las tres
  ecuaciones. En efecto, $u+v=u-v$ porque $-v=v$, y entonces $(u+v)+(u-v)=0_V$: el conjunto es **LD**.
  El determinante $-2$ es $0$ módulo $2$.

**Comprobación.** En $\mathbb{Z}_2$, la lista tiene dos vectores iguales ($u+v$ y $u-v$); una lista con
repetidos nunca es independiente.

:::tip[Resultado]
$\{u+v,u-v,w\}$ es LI sobre $\mathbb{R}$ y LD sobre $\mathbb{Z}_2$.
:::

### Ejemplo 4 · Matrices de ℝ²ˣ² por coordenadas
<!-- check: U1.T05.E4 -->

Sean
$A_1=\begin{pmatrix}1&0\\1&1\end{pmatrix}$, $A_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}$,
$A_3=\begin{pmatrix}2&1\\3&2\end{pmatrix}$ y $A_4=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ en
$\mathbb{R}^{2\times2}$. Decidir si $\{A_1,A_2,A_3\}$ y $\{A_1,A_2,A_4\}$ son LI.

Pasamos a coordenadas en $E=\{E_{11},E_{12},E_{21},E_{22}\}$: $[A_1]_E=(1,0,1,1)^t$,
$[A_2]_E=(0,1,1,0)^t$, $[A_3]_E=(2,1,3,2)^t$ y $[A_4]_E=(1,1,0,0)^t$.

**$\{A_1,A_2,A_3\}$.** Notamos que $2[A_1]_E+[A_2]_E=(2,1,3,2)^t=[A_3]_E$. Entonces
$A_3=2A_1+A_2$ y la relación $2A_1+A_2-A_3=0$ muestra que el conjunto es **LD**. (Con el método
sistemático, la matriz de coordenadas tiene rango $2<3$.)

**$\{A_1,A_2,A_4\}$.** Escalonamos las columnas de coordenadas:

$$
\begin{pmatrix}1&0&1\\0&1&1\\1&1&0\\1&0&0\end{pmatrix}
\xrightarrow[F_4-F_1\to F_4]{F_3-F_1\to F_3}
\begin{pmatrix}1&0&1\\0&1&1\\0&1&-1\\0&0&-1\end{pmatrix}
\xrightarrow{F_3-F_2\to F_3}
\begin{pmatrix}1&0&1\\0&1&1\\0&0&-2\\0&0&-1\end{pmatrix}.
$$

Hay tres pivotes: el conjunto es **LI**.

**Comprobación.** $2A_1+A_2=\begin{pmatrix}2&0\\2&2\end{pmatrix}+\begin{pmatrix}0&1\\1&0\end{pmatrix}=A_3$.
Como la respuesta final es sobre matrices, la relación de dependencia se escribe con matrices:
$A_3=2A_1+A_2$, no con ternas.

:::tip[Resultado]
$\{A_1,A_2,A_3\}$ es LD ($A_3=2A_1+A_2$); $\{A_1,A_2,A_4\}$ es LI.
:::

:::caution[Errores frecuentes]
- **"$0\cdot v+0\cdot w=0$, entonces $v$ y $w$ son LI."** Esa igualdad vale **siempre**, para cualquier
  par de vectores. La independencia exige que sea la **única** combinación nula. Para $v=(1,2)$ y
  $w=(2,4)$ también vale $2v-w=0$ con coeficientes no nulos: son LD.
- **Revisar solo de a pares.** $(1,0)$, $(0,1)$ y $(1,1)$ son de a dos no proporcionales, pero el conjunto
  es LD: $(1,1)=(1,0)+(0,1)$. Hay que mirar combinaciones de todos a la vez.
- **Creer que en un conjunto LD cada vector es combinación de los demás.** Solo **alguno** lo es:
  en $\{(1,0),(2,0),(0,1)\}$, el vector $(0,1)$ no.
- **Olvidar el cuerpo.** El conjunto del ejemplo 1 es LI en $\mathbb{R}^3$ y LD en $\mathbb{Z}_2^3$;
  sin decir el cuerpo, la pregunta no está bien planteada.
- **Usar el determinante cuando la matriz no es cuadrada.** Con $k\neq n$ vectores de $K^n$ no hay
  determinante: se usa el rango.
- **Ignorar el vector nulo o los repetidos.** Un conjunto con el nulo, o con dos vectores iguales, es LD.
- **Confundir independencia con generación.** Tres vectores LI de $\mathbb{R}^4$ no generan $\mathbb{R}^4$;
  generan un subespacio de dimensión $3$.
:::

## Autoevaluación

**1.** ¿Es LI $\{(1,2,3),(2,4,6)\}$ en $\mathbb{R}^3$?

<details>
<summary>Respuesta</summary>

No: $(2,4,6)=2(1,2,3)$, así que $2(1,2,3)-(2,4,6)=0$ es una relación no trivial.

</details>

**2.** ¿Pueden ser LI cuatro vectores de $\mathbb{R}^3$?

<details>
<summary>Respuesta</summary>

No. La matriz de columnas es de $3\times4$, su rango es a lo sumo $3$ y, por rango–nulidad, el sistema
homogéneo tiene una variable libre.

</details>

**3.** ¿Cuántos conjuntos de dos vectores LI tiene $\mathbb{Z}_2^2$?

<details>
<summary>Respuesta</summary>

Tres: dos vectores de $\mathbb{Z}_2^2$ son LD solo si alguno es nulo o si son iguales (el único
escalar no nulo es $1$). Los tres vectores no nulos son $(1,0)$, $(0,1)$ y $(1,1)$, y cualquier par de
ellos es LI: $\{(1,0),(0,1)\}$, $\{(1,0),(1,1)\}$ y $\{(0,1),(1,1)\}$.

</details>

:::tip[En resumen]
- $v_1,\dots,v_k$ son LI si $\sum\alpha_iv_i=0$ solo se cumple con todos los $\alpha_i=0$; son LD si hay una
  relación con algún coeficiente no nulo.
- Un conjunto de al menos dos vectores es LD si y solo si algún vector es combinación de los demás.
- En $K^n$: $k$ vectores son LI si y solo si la matriz de columnas tiene rango $k$ (pivote en cada
  columna); con $k=n$, si y solo si $\det\neq0$. Más de $n$ vectores son siempre LD.
- En $\mathbb{R}^2$ y $\mathbb{R}^3$: LD significa colineales (dos vectores) o coplanares (tres).
- Subconjuntos de LI son LI; un conjunto con el nulo es LD; agregar un vector fuera del generado
  conserva la independencia; los coeficientes de una combinación de LI son únicos.
- La independencia depende del cuerpo.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 2.3, "Conjuntos generadores e
  independencia lineal" (p. 94), y sección 6.2, "Independencia lineal, bases y dimensión" (p. 461).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: conjuntos linealmente independientes y bases.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed., sección 4.2, "Base y dimensión"
  (p. 148), como lectura complementaria.

Lección anterior: [combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/).
Lección siguiente: [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/).
Repaso relacionado: [determinantes](/algebra-ii/repaso/determinantes/).
