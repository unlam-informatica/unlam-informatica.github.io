---
title: Cuadrados mínimos
description: Solución aproximada de sistemas incompatibles, ecuaciones normales, ajuste de rectas, parábolas y exponenciales a datos experimentales, y una aplicación al análisis del tiempo de ejecución.
slug: algebra-ii/unidad-4/teoria/cuadrados-minimos
sidebar:
  order: 7
  label: 4.7 Cuadrados mínimos
---

Los datos que se miden, ya sean tiempos de ejecución, temperaturas o precios, casi nunca satisfacen exactamente un modelo. Si pedimos que una recta pase por cinco puntos medidos, el sistema que queda es **incompatible**: tiene más ecuaciones que incógnitas y ninguna solución exacta. Los **cuadrados mínimos** buscan la mejor solución aproximada: la que hace mínima la suma de los cuadrados de los errores. La idea es la de la lección anterior: el mejor candidato es una proyección ortogonal.

En esta lección usamos siempre el producto usual de $\mathbb{R}^m$.

## El problema y su solución geométrica

Sea $A$ una matriz de $m\times n$ y $b\in\mathbb{R}^m$ tales que $Ax=b$ no tiene solución, es decir, $b\notin\operatorname{col}(A)$. Para cada $x\in\mathbb{R}^n$ definimos el **residuo** $e(x)=b-Ax$.

:::note[Definición (solución de cuadrados mínimos)]
Un vector $\bar x\in\mathbb{R}^n$ es una **solución de cuadrados mínimos** de $Ax=b$ si

$$
\lVert b-A\bar x\rVert\le\lVert b-Ax\rVert\qquad\text{para todo }x\in\mathbb{R}^n .
$$

El número $\lVert b-A\bar x\rVert^2$ es el **error cuadrático** (suma de los cuadrados de las componentes del residuo).
:::

Como $\{Ax:\ x\in\mathbb{R}^n\}=\operatorname{col}(A)$, buscar $\bar x$ equivale a buscar, **entre los vectores de $\operatorname{col}(A)$, el más cercano a $b$**. Por el teorema de mejor aproximación (lección [4.6](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/)), ese vector es $\operatorname{proy}_{\operatorname{col}(A)}(b)$. Por lo tanto:

$$
\bar x\ \text{es solución de cuadrados mínimos}\iff A\bar x=\operatorname{proy}_{\operatorname{col}(A)}(b).
$$

Esta ecuación **siempre tiene solución**: la proyección está en $\operatorname{col}(A)$, así que es de la forma $A\bar x$ para algún $\bar x$. Falta una manera de hallar $\bar x$ sin calcular antes la proyección.

## Ecuaciones normales

:::note[Teorema (ecuaciones normales)]
Un vector $\bar x$ es solución de cuadrados mínimos de $Ax=b$ si y solo si satisface

$$
A^tA\,\bar x=A^tb .
$$

Además, la solución es única si y solo si las columnas de $A$ son linealmente independientes, y en ese caso $A^tA$ es inversible y

$$
\bar x=(A^tA)^{-1}A^tb .
$$
:::

**Demostración.** *Ecuaciones normales.* Por lo anterior, $\bar x$ es solución si y solo si $A\bar x=\operatorname{proy}_{\operatorname{col}(A)}(b)$, y esto vale si y solo si $A\bar x\in\operatorname{col}(A)$ (siempre) y $b-A\bar x\in\operatorname{col}(A)^\perp$ (unicidad de la descomposición ortogonal). Con el producto usual, $\operatorname{col}(A)^\perp=\operatorname{fil}(A^t)^\perp=\operatorname{nul}(A^t)$ (lección [4.5](/algebra-ii/unidad-4/teoria/complemento-ortogonal/)), de modo que la condición es $A^t(b-A\bar x)=0$, es decir, $A^tA\bar x=A^tb$.

*Unicidad.* Primero, $\operatorname{nul}(A^tA)=\operatorname{nul}(A)$. Si $Ax=0$ entonces $A^tAx=0$. Recíprocamente, si $A^tAx=0$ entonces $0=x^tA^tAx=(Ax)\cdot(Ax)=\lVert Ax\rVert^2$, y por lo tanto $Ax=0$. Las columnas de $A$ son LI si y solo si $\operatorname{nul}(A)=\{0\}$, es decir, si y solo si $\operatorname{nul}(A^tA)=\{0\}$, y como $A^tA$ es cuadrada de $n\times n$, esto equivale a que $A^tA$ sea inversible. En ese caso la ecuación normal tiene como única solución $\bar x=(A^tA)^{-1}A^tb$. Si las columnas son LD, el sistema $A^tAx=A^tb$ es compatible (porque hay solución) y tiene infinitas soluciones. $\blacksquare$

Observaciones:

- Si $\bar x$ es solución y las columnas son LD, todas las soluciones dan el **mismo** vector $A\bar x$ (la proyección); lo único que cambia es cómo se lo escribe como combinación de las columnas.
- La matriz $A^tA$ es simétrica de $n\times n$: mucho más chica que $A$ cuando hay muchos datos y pocos parámetros.
- La proyección de $b$ sobre $\operatorname{col}(A)$ es $A\bar x=A(A^tA)^{-1}A^tb$: la matriz $P=A(A^tA)^{-1}A^t$ de la lección 4.6 es la matriz de la proyección ortogonal sobre $\operatorname{col}(A)$ (cuando las columnas son LI).
- El error: por Pitágoras, $\lVert b-A\bar x\rVert^2=\lVert b\rVert^2-\lVert A\bar x\rVert^2$.

## Ajuste de rectas y de otras curvas

Dados los datos $(x_1,y_1),\dots,(x_m,y_m)$, la **recta de mejor ajuste** $y=\alpha+\beta x$ se obtiene pidiendo $\alpha+\beta x_i\approx y_i$ para todos los puntos. El sistema es

$$
\underbrace{\begin{pmatrix}1&x_1\\ \vdots&\vdots\\ 1&x_m\end{pmatrix}}_{A}\begin{pmatrix}\alpha\\ \beta\end{pmatrix}\approx\underbrace{\begin{pmatrix}y_1\\ \vdots\\ y_m\end{pmatrix}}_{b},\qquad A^tA=\begin{pmatrix}m&\sum x_i\\ \sum x_i&\sum x_i^2\end{pmatrix},\qquad A^tb=\begin{pmatrix}\sum y_i\\ \sum x_iy_i\end{pmatrix}.
$$

Las columnas de $A$ son LI cuando al menos dos de los $x_i$ son distintos, de modo que la solución es única. El residuo $e_i=y_i-(\alpha+\beta x_i)$ es la distancia **vertical** del punto a la recta, y el método minimiza $\sum e_i^2$, de donde viene su nombre. Como la primera columna de $A$ es el vector de unos y $A^te=0$, **la suma de los residuos es $0$**.

El método no se limita a rectas. Lo único que se exige es que el modelo sea **lineal en los parámetros**: una parábola $y=\alpha+\beta x+\gamma x^2$ usa las columnas $(1,x_i,x_i^2)$; un modelo $y=\alpha+\beta n^2$ usa $(1,n_i^2)$. Cada función base aporta una columna de $A$.

<figure class="math-figure">
<svg viewBox="-25 -135 215 160" role="img" aria-labelledby="cm-t cm-d" xmlns="http://www.w3.org/2000/svg">
<title id="cm-t">Recta de cuadrados mínimos con residuos verticales</title>
<desc id="cm-d">Cinco puntos (0,1), (1,2), (2,2), (3,4) y (4,6), la recta y=0,6+1,2x y los segmentos verticales de cada punto a la recta, que son los residuos 2/5, 1/5, -1, -1/5 y 3/5.</desc>
<g transform="scale(1,-1)">
<line class="grid" x1="0" y1="40" x2="165" y2="40"/>
<line class="grid" x1="0" y1="80" x2="165" y2="80"/>
<line class="grid" x1="0" y1="120" x2="165" y2="120"/>
<line class="grid" x1="40" y1="0" x2="40" y2="125"/>
<line class="grid" x1="80" y1="0" x2="80" y2="125"/>
<line class="grid" x1="120" y1="0" x2="120" y2="125"/>
<line class="grid" x1="160" y1="0" x2="160" y2="125"/>
<line class="axis" x1="-5" y1="0" x2="170" y2="0"/>
<line class="axis" x1="0" y1="-5" x2="0" y2="130"/>
<line class="line-a" x1="0" y1="12" x2="160" y2="108"/>
<line class="line-c" x1="0" y1="12" x2="0" y2="20"/>
<line class="line-c" x1="40" y1="36" x2="40" y2="40"/>
<line class="line-c" x1="80" y1="60" x2="80" y2="40"/>
<line class="line-c" x1="120" y1="84" x2="120" y2="80"/>
<line class="line-c" x1="160" y1="108" x2="160" y2="120"/>
<circle class="dot-b" cx="0" cy="20" r="3"/>
<circle class="dot-b" cx="40" cy="40" r="3"/>
<circle class="dot-b" cx="80" cy="40" r="3"/>
<circle class="dot-b" cx="120" cy="80" r="3"/>
<circle class="dot-b" cx="160" cy="120" r="3"/>
</g>
<text class="small" x="-3" y="10" text-anchor="middle">0</text>
<text class="small" x="40" y="10" text-anchor="middle">1</text>
<text class="small" x="80" y="10" text-anchor="middle">2</text>
<text class="small" x="120" y="10" text-anchor="middle">3</text>
<text class="small" x="160" y="10" text-anchor="middle">4</text>
<text class="small" x="-8" y="-38" text-anchor="end">2</text>
<text class="small" x="-8" y="-78" text-anchor="end">4</text>
<text class="small" x="-8" y="-118" text-anchor="end">6</text>
<text class="math" x="150" y="-84">y = 0,6 + 1,2x</text>
</svg>
<figcaption>Los cinco puntos del Ejemplo 1 y la recta de cuadrados mínimos y = 0,6 + 1,2x. Los segmentos son los residuos verticales; la recta minimiza la suma de sus cuadrados, 8/5, y la suma (con signo) de los residuos es cero. Escala: 1 unidad en x son 40 y 1 unidad en y son 20 unidades del dibujo.</figcaption>
</figure>

## Ejemplos

### Ejemplo 1 · Recta de ajuste con cinco puntos
<!-- check: U4.T07.E1 -->

Hallar la recta de cuadrados mínimos $y=\alpha+\beta x$ para los puntos $(0,1)$, $(1,2)$, $(2,2)$, $(3,4)$ y $(4,6)$, y el error cuadrático.

**Resolución.** Las matrices del sistema son $A=\begin{pmatrix}1&0\\1&1\\1&2\\1&3\\1&4\end{pmatrix}$ y $b=(1,2,2,4,6)^t$. Las sumas son $\sum x_i=10$, $\sum x_i^2=30$, $\sum y_i=15$ y $\sum x_iy_i=0+2+4+12+24=42$, entonces

$$
A^tA=\begin{pmatrix}5&10\\10&30\end{pmatrix},\qquad A^tb=\begin{pmatrix}15\\42\end{pmatrix},\qquad\det(A^tA)=150-100=50 .
$$

Las columnas de $A$ son LI, así que $\bar x=(A^tA)^{-1}A^tb$ con $(A^tA)^{-1}=\frac1{50}\begin{pmatrix}30&-10\\-10&5\end{pmatrix}$:

$$
\begin{pmatrix}\alpha\\ \beta\end{pmatrix}=\frac1{50}\begin{pmatrix}30\cdot15-10\cdot42\\-10\cdot15+5\cdot42\end{pmatrix}=\frac1{50}\begin{pmatrix}30\\60\end{pmatrix}=\begin{pmatrix}3/5\\6/5\end{pmatrix}.
$$

La recta es $y=\frac35+\frac65x$. Los valores ajustados son $A\bar x=\left(\tfrac35,\tfrac95,3,\tfrac{21}5,\tfrac{27}5\right)^t$ y el residuo $e=b-A\bar x=\left(\tfrac25,\tfrac15,-1,-\tfrac15,\tfrac35\right)^t$. El error cuadrático es

$$
\lVert e\rVert^2=\frac{4+1+1\cdot25+1+9}{25}=\frac{40}{25}=\frac85 .
$$

**Comprobación.** $A^te=\left(\tfrac25+\tfrac15-1-\tfrac15+\tfrac35,\ 0+\tfrac15-2-\tfrac35+\tfrac{12}5\right)=(0,0)$: el residuo es ortogonal a las dos columnas de $A$.

### Ejemplo 2 · Una parábola
<!-- check: U4.T07.E2 -->

Hallar la parábola $y=\alpha+\beta x+\gamma x^2$ de cuadrados mínimos para los puntos $(-1,2{,}8)$, $(0,1{,}6)$, $(1,0{,}4)$ y $(2,3{,}2)$.

**Resolución.** Con las columnas $(1,x_i,x_i^2)$, las sumas son $\sum x=2$, $\sum x^2=6$, $\sum x^3=8$, $\sum x^4=18$, $\sum y=8$, $\sum xy=-2{,}8+0+0{,}4+6{,}4=4$ y $\sum x^2y=2{,}8+0+0{,}4+12{,}8=16$. Las ecuaciones normales son

$$
\begin{pmatrix}4&2&6\\2&6&8\\6&8&18\end{pmatrix}\begin{pmatrix}\alpha\\ \beta\\ \gamma\end{pmatrix}=\begin{pmatrix}8\\4\\16\end{pmatrix}.
$$

Simplificando cada ecuación a la mitad: $2\alpha+\beta+3\gamma=4$, $\alpha+3\beta+4\gamma=2$ y $3\alpha+4\beta+9\gamma=8$. De la primera, $\beta=4-2\alpha-3\gamma$. Reemplazando en la segunda queda $-5\alpha-5\gamma=-10$, o sea $\alpha+\gamma=2$; y en la tercera, $-5\alpha-3\gamma=-8$. Con $\alpha=2-\gamma$ resulta $-10+5\gamma-3\gamma=-8$, luego $\gamma=1$, $\alpha=1$ y $\beta=4-2-3=-1$. La parábola es $y=1-x+x^2$.

Los valores ajustados en $-1,0,1,2$ son $3,1,1,3$ y el residuo es $e=(-0{,}2,\ 0{,}6,\ -0{,}6,\ 0{,}2)^t$, con error cuadrático $0{,}04+0{,}36+0{,}36+0{,}04=0{,}8=\frac45$.

**Comprobación.** $A^te=\left(-0{,}2+0{,}6-0{,}6+0{,}2,\ 0{,}2+0-0{,}6+0{,}4,\ -0{,}2+0-0{,}6+0{,}8\right)=(0,0,0)$. Las columnas de $A$ son LI porque hay tres abscisas distintas, así que la solución es única.

### Ejemplo 3 · Un ajuste exponencial por linealización
<!-- check: U4.T07.E3 -->

Ajustar un modelo $y=c\cdot b^t$ a los datos $(0,1)$, $(1,2)$, $(2,8)$, $(3,16)$.

**Resolución.** El modelo no es lineal en $c$ y $b$, pero aplicando logaritmo en base $2$ queda $\log_2y=\log_2c+(\log_2b)\,t$, que sí es una recta en $t$. Con $z=\log_2y=(0,1,3,4)$ ajustamos $z=\alpha+\beta t$:

$$
A^tA=\begin{pmatrix}4&6\\6&14\end{pmatrix},\quad A^tz=\begin{pmatrix}8\\19\end{pmatrix},\quad(A^tA)^{-1}=\frac1{20}\begin{pmatrix}14&-6\\-6&4\end{pmatrix}\ \Longrightarrow\ \begin{pmatrix}\alpha\\ \beta\end{pmatrix}=\frac1{20}\begin{pmatrix}112-114\\-48+76\end{pmatrix}=\begin{pmatrix}-1/10\\7/5\end{pmatrix}.
$$

Entonces $\log_2y\approx-0{,}1+1{,}4t$, es decir $y\approx2^{-0{,}1}\cdot(2^{1{,}4})^t\approx0{,}93\cdot2{,}64^t$. En escala logarítmica los residuos son $(0{,}1,-0{,}3,0{,}3,-0{,}1)$ y el error cuadrático vale $0{,}2=\tfrac15$.

**Comprobación.** Con $\alpha=-0{,}1$ y $\beta=1{,}4$, los valores ajustados de $z$ son $-0{,}1,\ 1{,}3,\ 2{,}7,\ 4{,}1$, y los residuos son ortogonales a $(1,1,1,1)$ y a $(0,1,2,3)$.

Este método minimiza el error de $\log_2y$, **no** el error de $y$. Los resultados son parecidos cuando el modelo ajusta bien, pero no son el ajuste de cuadrados mínimos de $y$, que no se resuelve con ecuaciones normales.

## Aplicación: tiempo de ejecución en función del tamaño de entrada

En análisis de algoritmos se mide el tiempo $t$ de un programa para distintos tamaños de entrada $n$ y se busca el modelo que mejor explica los datos. Como el número de parámetros es el mismo, se pueden comparar dos modelos (lineal y cuadrático, por ejemplo) mirando el error cuadrático.

### Ejemplo 4 · ¿Modelo lineal o cuadrático?
<!-- check: U4.T07.E4 -->

Un experimento (con datos ficticios) mide el tiempo de un procedimiento para entradas de $n=1,2,3,4$ (en miles de elementos): $t=3{,}5$, $8{,}2$, $19{,}3$ y $33$ milisegundos. Ajustar $t=\alpha+\beta n$ y $t=\alpha+\beta n^2$, compararlos y predecir el tiempo para $n=5$.

**Resolución.** *Modelo cuadrático.* Las columnas son $(1,1,1,1)$ y $(n^2)=(1,4,9,16)$, con $A^tA=\begin{pmatrix}4&30\\30&354\end{pmatrix}$ y $A^tt=\begin{pmatrix}64\\738\end{pmatrix}$ ($\det=516$). Resolviendo,

$$
\begin{pmatrix}\alpha\\ \beta\end{pmatrix}=\frac1{516}\begin{pmatrix}354\cdot64-30\cdot738\\-30\cdot64+4\cdot738\end{pmatrix}=\frac1{516}\begin{pmatrix}516\\1032\end{pmatrix}=\begin{pmatrix}1\\2\end{pmatrix}.
$$

El modelo es $t=1+2n^2$, con valores ajustados $3,9,19,33$ y residuos $(0{,}5,-0{,}8,0{,}3,0)$: error cuadrático $0{,}25+0{,}64+0{,}09+0=0{,}98$.

*Modelo lineal.* Con $A^tA=\begin{pmatrix}4&10\\10&30\end{pmatrix}$ y $A^tt=\begin{pmatrix}64\\209{,}8\end{pmatrix}$ ($\det=20$) se obtiene $t=-8{,}9+9{,}96\,n$, con error cuadrático $20{,}972$. Los residuos $(2{,}44,-2{,}82,-1{,}68,2{,}06)$ siguen un patrón de signos $+,-,-,+$, típico de una curva que se ignoró.

La diferencia es grande: $20{,}97$ contra $0{,}98$. Los datos son compatibles con un costo cuadrático. La predicción para $n=5$ es $1+2\cdot25=51$ ms (el modelo lineal daría $40{,}9$).

**Comprobación.** En el modelo cuadrático, el residuo es ortogonal a las dos columnas: $0{,}5-0{,}8+0{,}3+0=0$ y $0{,}5-3{,}2+2{,}7+0=0$.

:::caution[Advertencia: extrapolar]
El modelo se ajustó con $n$ entre $1$ y $4$. Predecir dentro de ese rango (interpolar) es razonable; predecir lejos (extrapolar) no: el costo real puede cambiar por efectos de memoria caché, recolección de basura o paginación, y un buen ajuste con pocos puntos no prueba que el algoritmo sea cuadrático. Un ajuste pequeño en cuatro puntos tampoco distingue un modelo cuadrático de uno cúbico con coeficientes chicos. Los cuadrados mínimos describen datos observados; no prueban una cota teórica de complejidad.
:::

## Interpretación

- **Geométrica.** Las columnas de $A$ generan un subespacio de $\mathbb{R}^m$; $b$ queda fuera y $A\bar x$ es su proyección. El residuo $b-A\bar x$ es perpendicular a todas las columnas: eso es lo que dicen las ecuaciones normales.
- **Estadística elemental.** Minimizar $\sum e_i^2$ penaliza mucho los errores grandes; un dato atípico puede mover bastante la recta.
- **Computacional.** Formar $A^tA$ puede empeorar el condicionamiento; en la práctica numérica se prefiere factorizar $A=QR$ (a partir de Gram-Schmidt, lección [4.4](/algebra-ii/unidad-4/teoria/gram-schmidt/)) y resolver $R\bar x=Q^tb$.

:::caution[Errores frecuentes]
- **Resolver $Ax=b$ directamente** cuando es incompatible. Hay que resolver $A^tAx=A^tb$.
- **Olvidar la columna de unos** en la recta de ajuste: sin ella se fuerza $y=\beta x$ por el origen.
- **Invertir $A^tA$ sin verificar que las columnas son LI.** Si $\det(A^tA)=0$, no hay solución única (por ejemplo, todos los $x_i$ iguales).
- **Escribir $\bar x=A^{-1}b$.** $A$ no es cuadrada ni inversible: la fórmula correcta es $(A^tA)^{-1}A^tb$. Solo si $A$ es cuadrada e inversible coinciden.
- **Calcular mal el error:** es la suma de cuadrados de $b-A\bar x$, no la de $b-A x$ con otro $x$, ni la suma sin cuadrados (que da $0$ por la columna de unos).
- **Linealizar sin advertirlo.** El ajuste exponencial por logaritmos minimiza el error de $\log y$.
- **Extrapolar con confianza.** Un modelo ajustado en un rango no vale fuera de él.
:::

## Autoevaluación

<details>
<summary>1. Ajustar y = α con cuadrados mínimos a los datos y₁, …, yₘ. ¿Qué resulta?</summary>

$A=(1,\dots,1)^t$, $A^tA=m$, $A^tb=\sum y_i$, y $\bar\alpha=\frac1m\sum y_i$: el promedio.

</details>

<details>
<summary>2. ¿Cuándo la recta de ajuste pasa exactamente por todos los puntos?</summary>

Cuando $b\in\operatorname{col}(A)$, es decir, cuando los puntos ya están alineados; entonces el residuo es nulo y el error cuadrático es $0$.

</details>

<details>
<summary>3. Probar que si las columnas de A son LI, entonces AᵗA es simétrica e inversible.</summary>

$(A^tA)^t=A^tA$. Si $A^tAx=0$ entonces $\lVert Ax\rVert^2=x^tA^tAx=0$, luego $Ax=0$ y $x=0$ por la independencia de las columnas.

</details>

:::tip[En resumen]
- $\bar x$ es solución de cuadrados mínimos de $Ax=b$ si y solo si $A\bar x=\operatorname{proy}_{\operatorname{col}(A)}(b)$, si y solo si $A^tA\bar x=A^tb$ (ecuaciones normales). Siempre existe.
- Es única si y solo si las columnas de $A$ son LI; entonces $\bar x=(A^tA)^{-1}A^tb$ y $\operatorname{proy}_{\operatorname{col}(A)}(b)=A(A^tA)^{-1}A^tb$.
- El residuo $b-A\bar x$ es ortogonal a $\operatorname{col}(A)$. El error cuadrático es $\lVert b-A\bar x\rVert^2=\lVert b\rVert^2-\lVert A\bar x\rVert^2$.
- Rectas, parábolas y otros modelos lineales en los parámetros se ajustan eligiendo las columnas de $A$; los modelos exponenciales se linealizan con logaritmos.
- Interpolar es razonable; extrapolar exige cuidado.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 7.3, "Aproximación por mínimos cuadrados" (p. 591): teorema de mejor aproximación, ecuaciones normales y ajustes de recta, parábola y exponencial.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ortogonalidad y mínimos cuadrados (problemas de mínimos cuadrados, modelos lineales).
- Anterior: [4.6 Proyección y distancia](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/). Siguiente: [4.8 Códigos y $\mathbb{Z}_2^n$](/algebra-ii/unidad-4/teoria/codigos-y-z2/).
- Repaso: [sistemas lineales](/algebra-ii/repaso/sistemas-lineales/).
