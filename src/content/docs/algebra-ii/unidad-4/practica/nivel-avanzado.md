---
title: Práctica — Nivel avanzado
description: Siete ejercicios resueltos de espacios con producto interno de mayor exigencia. Verdadero o falso, contraejemplos, demostraciones, mejor aproximación en P₂, ajuste de una parábola y decodificación por síndrome.
slug: algebra-ii/unidad-4/practica/nivel-avanzado
sidebar:
  order: 3
  label: Nivel avanzado
---

Esta página sigue al [nivel intermedio](/algebra-ii/unidad-4/practica/nivel-intermedio/) con ejercicios que piden justificar, demostrar o interpretar resultados, además de calcular. Presupone la unidad completa: [4.1 Producto interno](/algebra-ii/unidad-4/teoria/producto-interno/), [4.2 Norma, distancia y ángulo](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/), [4.3 Ortogonalidad](/algebra-ii/unidad-4/teoria/ortogonalidad/), [4.4 Gram-Schmidt](/algebra-ii/unidad-4/teoria/gram-schmidt/), [4.5 Complemento ortogonal](/algebra-ii/unidad-4/teoria/complemento-ortogonal/), [4.6 Proyección y distancia](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/), [4.7 Cuadrados mínimos](/algebra-ii/unidad-4/teoria/cuadrados-minimos/) y [4.8 Códigos y $\mathbb{Z}_2^n$](/algebra-ii/unidad-4/teoria/codigos-y-z2/).

Cómo usarla: en los ejercicios de demostración, escribí primero tu argumento completo y recién después compará con la resolución; lo que se evalúa es que cada paso esté justificado con un axioma o un resultado de la teoría. Los enunciados son originales de este manual. Después de esta página, la [guía integradora](/algebra-ii/unidad-4/practica/guia-integradora/) propone problemas de varios ítems.

### Ejercicio 21 · Verdadero o falso sobre ortogonalidad y proyección
<!-- ejercicio: U4.21 | nivel: avanzado | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
Decidir si cada afirmación es verdadera o falsa y justificar con una demostración o un contraejemplo.

a) Si $S$ es un subespacio de un espacio euclídeo $V$, entonces $S\cap S^\perp=\{0\}$.

b) En $\mathbb{Z}_2^n$ con el producto punto, $S\cap S^\perp=\{0\}$ para todo subespacio $S$.

c) Si $\operatorname{proy}_S(v)=\operatorname{proy}_S(w)$, entonces $v=w$.

d) Para todo subespacio $S$ de dimensión finita y todo $v$ vale $\lVert\operatorname{proy}_S(v)\rVert\le\lVert v\rVert$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las verdaderas se demuestran con los axiomas y con la descomposición ortogonal $v=\operatorname{proy}_S(v)+(v-\operatorname{proy}_S(v))$; las falsas, con un caso chico verificado.

**a) Verdadera.** Si $u\in S\cap S^\perp$, como $u\in S^\perp$ es ortogonal a todos los vectores de $S$, en particular a $u\in S$: $\langle u,u\rangle=0$. Por la positividad definida, $u=0$.

**b) Falsa.** El producto punto de $\mathbb{Z}_2^n$ no es definido positivo: $x\cdot x=w(x)\bmod2$ puede ser $0$ con $x\neq0$. Contraejemplo en $\mathbb{Z}_2^2$: $S=\operatorname{gen}\{11\}$. Como $11\cdot11=1+1=0$, se cumple $11\in S^\perp$, luego $S\cap S^\perp=S\neq\{0\}$ (de hecho $S^\perp=S$).

**c) Falsa.** La proyección «olvida» la componente en $S^\perp$. Contraejemplo en $\mathbb{R}^2$ con el producto usual: $S=\operatorname{gen}\{(1,0)\}$, $v=(1,1)$ y $w=(1,2)$. Entonces $\operatorname{proy}_S(v)=(1,0)=\operatorname{proy}_S(w)$ pero $v\neq w$.

**d) Verdadera.** Sea $p=\operatorname{proy}_S(v)$. Como $v-p\in S^\perp$ y $p\in S$, por Pitágoras $\lVert v\rVert^2=\lVert p\rVert^2+\lVert v-p\rVert^2\ge\lVert p\rVert^2$. La igualdad vale si y solo si $v=p$, o sea $v\in S$.

**Comprobación.** En c): $\langle v,(1,0)\rangle/1=1$ y $\langle w,(1,0)\rangle/1=1$. En d) con los mismos datos, $\lVert\operatorname{proy}_S(v)\rVert=1\le\sqrt2=\lVert v\rVert$.

:::tip[Resultado]
a) V. b) F ($S=\operatorname{gen}\{11\}\subset\mathbb{Z}_2^2$). c) F ($S=\operatorname{gen}\{(1,0)\}$, $v=(1,1)$, $w=(1,2)$). d) V.
:::

</details>

### Ejercicio 22 · Tres contraejemplos sobre productos internos
<!-- ejercicio: U4.22 | nivel: avanzado | tipo: contraejemplo | verificacion: sympy -->

:::note[Enunciado]
Refutar cada afirmación con un contraejemplo explícito.

a) «En $P_2[\mathbb{R}]$, $\langle p,q\rangle=p(0)q(0)+p(1)q(1)$ es un producto interno.»

b) «Si una matriz simétrica $M\in\mathbb{R}^{2\times2}$ tiene sus entradas diagonales positivas, entonces $\langle x,y\rangle=x^tMy$ es un producto interno de $\mathbb{R}^2$.»

c) «Si dos vectores son ortogonales para el producto usual de $\mathbb{R}^2$, también lo son para cualquier otro producto interno de $\mathbb{R}^2$.»
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se identifica el axioma que falla y se exhibe un caso concreto con las cuentas completas.

**a)** La simetría y la bilinealidad se cumplen, pero un polinomio de grado $\le2$ puede anularse en solo dos puntos sin ser nulo. Tomemos $p=x^2-x=x(x-1)\neq0$: $p(0)=0$ y $p(1)=0$, de modo que $\langle p,p\rangle=0$ con $p\neq0$. **Falla la positividad definida.** (Hacen falta al menos tres puntos para $P_2[\mathbb{R}]$.)

**b)** Sea $M=\begin{pmatrix}1&2\\2&1\end{pmatrix}$, simétrica con diagonal positiva. Para $x=(1,-1)$:
$$
x^tMx=1\cdot1+2\cdot1\cdot(-1)+2\cdot(-1)\cdot1+1\cdot1=1-2-2+1=-2<0.
$$
Falla la positividad ($\det M=1-4=-3<0$). Con $m_{11}>0$ y diagonal positiva no alcanza: hace falta $\det M>0$.

**c)** Los vectores $u=(1,1)$ y $v=(1,-1)$ cumplen $u\cdot v=1-1=0$. Con $\langle x,y\rangle'=x_1y_1+2x_2y_2$ (un producto interno), $\langle u,v\rangle'=1-2=-1\neq0$.

**Comprobación.** En c), $\langle\ ,\ \rangle'$ es producto interno porque $\operatorname{diag}(1,2)$ es simétrica con $1>0$ y $\det=2>0$. En a), $p(0)^2+p(1)^2=0$ confirma $\langle p,p\rangle=0$.

:::tip[Resultado]
a) $p=x^2-x$ tiene norma $0$. b) $M=\begin{pmatrix}1&2\\2&1\end{pmatrix}$ y $x=(1,-1)$ da $x^tMx=-2$. c) $(1,1)\perp(1,-1)$ para el usual, pero $\langle(1,1),(1,-1)\rangle'=-1$ con el producto ponderado $x_1y_1+2x_2y_2$.
:::

</details>

### Ejercicio 23 · Paralelogramo e igualdad en la desigualdad triangular
<!-- ejercicio: U4.23 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $(V,\langle\ ,\ \rangle)$ un espacio euclídeo.

a) Probar la ley del paralelogramo: $\lVert u+v\rVert^2+\lVert u-v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2$ para todo $u,v\in V$.

b) Probar que si $u\neq0$ y $\lVert u+v\rVert=\lVert u\rVert+\lVert v\rVert$, entonces $v=\lambda u$ para algún $\lambda\ge0$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En a) se desarrollan las normas al cuadrado con bilinealidad y simetría. En b) se eleva al cuadrado para obtener la igualdad en Cauchy-Schwarz y se muestra directamente que $v-\lambda u=0$ para un $\lambda$ adecuado.

**a) Demostración.** Por bilinealidad y simetría,
$$
\lVert u\pm v\rVert^2=\langle u\pm v,u\pm v\rangle=\lVert u\rVert^2\pm2\langle u,v\rangle+\lVert v\rVert^2.
$$
Sumando ambas expresiones, los términos $\pm2\langle u,v\rangle$ se cancelan y queda $2\lVert u\rVert^2+2\lVert v\rVert^2$. $\blacksquare$

**b) Demostración.** Elevando al cuadrado la hipótesis y desarrollando el lado izquierdo,
$$
\lVert u\rVert^2+2\langle u,v\rangle+\lVert v\rVert^2=\lVert u\rVert^2+2\lVert u\rVert\lVert v\rVert+\lVert v\rVert^2,
$$
de donde $\langle u,v\rangle=\lVert u\rVert\lVert v\rVert$. Sea $\lambda=\dfrac{\langle u,v\rangle}{\lVert u\rVert^2}=\dfrac{\lVert v\rVert}{\lVert u\rVert}\ge0$ (está bien definido porque $u\neq0$). Entonces
$$
\lVert v-\lambda u\rVert^2=\lVert v\rVert^2-2\lambda\langle u,v\rangle+\lambda^2\lVert u\rVert^2=\lVert v\rVert^2-2\lVert v\rVert^2+\lVert v\rVert^2=0,
$$
pues $\lambda\langle u,v\rangle=\dfrac{\langle u,v\rangle^2}{\lVert u\rVert^2}=\lVert v\rVert^2$ y $\lambda^2\lVert u\rVert^2=\lVert v\rVert^2$. Por la positividad definida, $v-\lambda u=0$, o sea $v=\lambda u$ con $\lambda\ge0$. $\blacksquare$

**Comprobación (casos borde).** Si $v=0$, la hipótesis vale y $\lambda=0$. La recíproca también es cierta: si $v=\lambda u$ con $\lambda\ge0$, entonces $\lVert u+v\rVert=(1+\lambda)\lVert u\rVert=\lVert u\rVert+\lVert v\rVert$. Para $v=-u$ la igualdad falla (da $0\neq2\lVert u\rVert$), consistente con $\lambda<0$. Para a), con $u=(1,0)$ y $v=(0,1)$ en $\mathbb{R}^2$: $\lVert u+v\rVert^2+\lVert u-v\rVert^2=2+2=2\cdot1+2\cdot1$.

:::tip[Resultado]
a) Se cumple la ley del paralelogramo, por cancelación de los términos cruzados. b) La igualdad en la desigualdad triangular ocurre solo si $v$ es un múltiplo no negativo de $u$ (misma dirección y sentido).
:::

</details>

### Ejercicio 24 · Códigos autoduales
<!-- ejercicio: U4.24 | nivel: avanzado | tipo: demostracion | verificacion: razonamiento -->

:::note[Enunciado]
Sea $\mathcal C\subseteq\mathbb{Z}_2^n$ un código lineal $(n,k)$ **autodual**, es decir, $\mathcal C^\perp=\mathcal C$. Probar que:

a) $n=2k$ (en particular $n$ es par);

b) todas las palabras de $\mathcal C$ tienen peso par;

c) la palabra $\mathbf 1=11\cdots1$ pertenece a $\mathcal C$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se usa la fórmula de dimensiones del dual, $\dim\mathcal C+\dim\mathcal C^\perp=n$ (que vale en $\mathbb{Z}_2^n$ porque $\mathcal C^\perp=\operatorname{nul}(G)$ y rango más nulidad es $n$), y la identidad $x\cdot x=w(x)\bmod2$.

**a) Demostración.** $\mathcal C^\perp=\operatorname{nul}(G)$ con $G$ de $k\times n$ y rango $k$, de modo que $\dim\mathcal C^\perp=n-k$. Si $\mathcal C^\perp=\mathcal C$, entonces $n-k=k$, o sea $n=2k$. $\blacksquare$

**b) Demostración.** Sea $c\in\mathcal C=\mathcal C^\perp$. Como $c\in\mathcal C^\perp$ es ortogonal a todas las palabras de $\mathcal C$, y $c\in\mathcal C$, resulta $c\cdot c=0$. Pero en $\mathbb{Z}_2$ vale $c_i^2=c_i$, luego $c\cdot c=\sum c_i=w(c)\bmod2$. Entonces $w(c)\equiv0\pmod2$. $\blacksquare$

**c) Demostración.** Para toda $c\in\mathcal C$, $c\cdot\mathbf 1=\sum c_i=w(c)\bmod2=0$ por b). Entonces $\mathbf 1$ es ortogonal a todo $\mathcal C$, o sea $\mathbf 1\in\mathcal C^\perp=\mathcal C$. $\blacksquare$

**Comprobación.** El código $\{0000,1100,0011,1111\}\subset\mathbb{Z}_2^4$ es autodual con $n=4=2\cdot2$, todas sus palabras tienen peso par y contiene $1111$. Por a), no existe ningún código autodual de longitud $5$.

:::tip[Resultado]
Un código autodual cumple $n=2k$, tiene todas sus palabras de peso par y contiene a la palabra de unos.
:::

</details>

### Ejercicio 25 · Mejor aproximación en $P_2[\mathbb{R}]$
<!-- ejercicio: U4.25 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $P_2[\mathbb{R}]$ con $\langle p,q\rangle=p(0)q(0)+p(1)q(1)+p(2)q(2)$ sea $S=P_1[\mathbb{R}]=\operatorname{gen}\{1,x\}$.

a) Hallar el polinomio de $S$ más cercano a $q=x^2$ y la distancia $d(x^2,S)$.

b) Comprobar que la solución es la de cuadrados mínimos para ajustar una recta a los puntos $(0,0)$, $(1,1)$ y $(2,4)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La mejor aproximación de $q$ en $S$ es $\operatorname{proy}_S(q)$ y la distancia es $\lVert q-\operatorname{proy}_S(q)\rVert$. Una base ortogonal de $S$ para este producto es $\{1,x-1\}$ (ya calculada en el ejercicio 12).

**a)** $\langle1,1\rangle=3$, $\langle x-1,x-1\rangle=2$, $\langle x^2,1\rangle=5$ y $\langle x^2,x-1\rangle=4$. Entonces
$$
\operatorname{proy}_S(x^2)=\frac53\cdot1+\frac42(x-1)=2x-\frac13.
$$
El resto es $x^2-2x+\frac13$, con valores $(\frac13,-\frac23,\frac13)$ en $0,1,2$, y su norma cumple $\frac19+\frac49+\frac19=\frac23$. Entonces $d(x^2,S)=\sqrt{2/3}=\dfrac{\sqrt6}{3}$.

**b)** Ajustar $y=a+bx$ a los puntos equivale a minimizar $\sum_i(y_i-a-bx_i)^2=\lVert x^2-(a+bx)\rVert^2$ en este producto, porque el producto evalúa en $x=0,1,2$. Las ecuaciones normales, con $A=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix}$ y $y=(0,1,4)^t$, son $A^tA=\begin{pmatrix}3&3\\3&5\end{pmatrix}$ y $A^ty=\begin{pmatrix}5\\9\end{pmatrix}$:
$$
\begin{cases}3a+3b=5\\3a+5b=9\end{cases}\ \Longrightarrow\ 2b=4,\ b=2,\ a=\tfrac53-2=-\tfrac13,
$$
la misma recta $-\frac13+2x$.

**Comprobación.** El error cuadrático es $\left(0+\tfrac13\right)^2+\left(1-\tfrac53\right)^2+\left(4-\tfrac{11}3\right)^2=\tfrac19+\tfrac49+\tfrac19=\tfrac23$. Otro candidato, por ejemplo $x$, da $0+0+4=4>\frac23$.

:::tip[Resultado]
El polinomio más cercano es $2x-\frac13$ y $d(x^2,S)=\sqrt6/3$. Coincide con la recta de cuadrados mínimos de los puntos $(0,0)$, $(1,1)$, $(2,4)$.
:::

</details>

### Ejercicio 26 · Parábola de ajuste para el tiempo de un algoritmo
<!-- ejercicio: U4.26 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Se midió el tiempo $t$ (ms) que tarda un algoritmo sobre entradas de $n$ miles de elementos:

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $t$ | 3 | 10 | 14 | 20 | 33 |

a) Ajustar por cuadrados mínimos el modelo cuadrático $t=\alpha+\beta n+\gamma n^2$ planteando las ecuaciones normales.

b) Ajustar también una recta y comparar los errores cuadráticos de ambos modelos.

c) Estimar el tiempo para $n=6$ con cada modelo y comentar cuál usarías.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con $A$ de columnas $1,\ n,\ n^2$ evaluadas en los datos y $b=t$, las ecuaciones normales $A^tAx=A^tb$ dan los coeficientes. Los errores se comparan con $\lVert b-Ax\rVert^2$.

**a)** Las sumas de potencias para $n=1,\dots,5$ son $\sum n=15$, $\sum n^2=55$, $\sum n^3=225$ y $\sum n^4=979$; y $\sum t=80$, $\sum nt=3+20+42+80+165=310$, $\sum n^2t=3+40+126+320+825=1314$. Entonces
$$
\begin{pmatrix}5&15&55\\15&55&225\\55&225&979\end{pmatrix}\begin{pmatrix}\alpha\\\beta\\\gamma\end{pmatrix}=\begin{pmatrix}80\\310\\1314\end{pmatrix}.
$$
La solución es $\alpha=2$, $\beta=1$, $\gamma=1$, es decir $t=2+n+n^2$. Se verifica en las tres ecuaciones: $10+15+55=80$, $30+55+225=310$ y $110+225+979=1314$.

**b)** Los valores ajustados por la parábola son $4,8,14,22,32$ y los residuos $(-1,2,0,-2,1)$, con error cuadrático $1+4+0+4+1=10$. Para la recta $t=a+bn$: $5a+15b=80$ y $15a+55b=310$ dan $b=7$ y $a=-5$, es decir $t=-5+7n$. Sus residuos son $t-(-5+7n)=(1,1,-2,-3,3)$ y su error cuadrático es $1+1+4+9+9=24$.

**c)** Para $n=6$: parábola $2+6+36=44$ ms; recta $-5+42=37$ ms. La parábola reduce el error de $24$ a $10$ y los residuos de la recta muestran un patrón (negativos en el centro, positivos en los extremos), típico de una curva convexa. Para un algoritmo que se sospecha cuadrático, el modelo $t=2+n+n^2$ es más razonable. Con solo cinco datos y tres parámetros conviene no extrapolar demasiado.

**Comprobación.** Ambos vectores de residuos son ortogonales a las columnas de su matriz: para la parábola, $(-1,2,0,-2,1)\cdot(1,1,1,1,1)=0$, $\cdot(1,2,3,4,5)=-1+4+0-8+5=0$ y $\cdot(1,4,9,16,25)=-1+8+0-32+25=0$.

:::tip[Resultado]
Parábola $t=2+n+n^2$ (error cuadrático $10$); recta $t=-5+7n$ (error $24$). Estimaciones para $n=6$: $44$ ms y $37$ ms.
:::

</details>

### Ejercicio 27 · Decodificación por síndrome
<!-- ejercicio: U4.27 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C\subseteq\mathbb{Z}_2^6$ el código con matriz de control de paridad
$$
H=\begin{pmatrix}1&1&0&1&0&0\\1&0&1&0&1&0\\0&1&1&0&0&1\end{pmatrix}.
$$

a) Hallar una matriz generadora $G$ y las dimensiones de $\mathcal C$ y de $\mathcal C^\perp$.

b) Probar que $d(\mathcal C)=3$.

c) Se recibe $r=101110$. Calcular el síndrome y corregir.

d) Si se transmitió $c=100110$ y se recibe $r''=010110$ (dos errores), ¿qué decodifica el método del síndrome?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** $\mathcal C=\operatorname{nul}(H)$; el síndrome de $r$ es $s=Hr^t$. Si $r=c+e_j$ con un solo error en la posición $j$, entonces $s=He_j^t$ es la columna $j$ de $H$. Para la distancia mínima se usa que $d(\mathcal C)$ es la menor cantidad de columnas de $H$ linealmente dependientes (que suman $0$).

**a)** $H=(A\mid I_3)$ con $A=\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix}$ (que es simétrica). Resolviendo $Hx^t=0$ con $x_1,x_2,x_3$ libres:
$$
x_4=x_1+x_2,\quad x_5=x_1+x_3,\quad x_6=x_2+x_3.
$$
Una base es $\{100110,\ 010101,\ 001011\}$, de modo que
$$
G=\begin{pmatrix}1&0&0&1&1&0\\0&1&0&1&0&1\\0&0&1&0&1&1\end{pmatrix}.
$$
Entonces $\dim\mathcal C=3$ y $\dim\mathcal C^\perp=6-3=3$ (el dual tiene a $H$ como matriz generadora).

**b)** Las seis columnas de $H$ son no nulas y distintas: $(1,1,0)$, $(1,0,1)$, $(0,1,1)$, $(1,0,0)$, $(0,1,0)$ y $(0,0,1)$. Por eso ninguna palabra tiene peso $1$ ni $2$ (no hay una columna nula ni dos iguales), y $d(\mathcal C)\ge3$. Además la suma de las tres primeras columnas es $(1,1,0)+(1,0,1)+(0,1,1)=(0,0,0)$, de modo que $111000\in\mathcal C$ tiene peso $3$. Entonces $d(\mathcal C)=3$: se detectan $2$ errores y se corrige $1$.

**c)** $s=Hr^t$ con $r=101110$: primera fila $1+0+0+1+0+0=0$; segunda $1+1+1=1$ (posiciones $1,3,5$: $r_1+r_3+r_5=1+1+1=1$); tercera $r_2+r_3+r_6=0+1+0=1$. Entonces $s=(0,1,1)^t$, que es la columna $3$ de $H$. Se corrige la posición $3$: $\hat c=100110$, que está en $\mathcal C$ (es la primera fila de $G$).

**d)** $r''=010110=c+e_1+e_2$. Su síndrome es $He_1^t+He_2^t=(1,1,0)+(1,0,1)=(0,1,1)^t$, otra vez la columna $3$. El método «corrige» la posición $3$ y decodifica $011110$, que es una palabra del código pero **no** la transmitida $100110$. Con $d=3$ la corrección de dos errores no es confiable: se confunden con un error de otra posición.

**Comprobación.** $\hat c=100110$ tiene unos en las posiciones $1,4,5$ y la suma de esas columnas de $H$ es $(1,1,0)+(1,0,0)+(0,1,0)=(0,0,0)$ (en $\mathbb{Z}_2$), de modo que $H\hat c^t=0$. Además $\hat c$ es la primera fila de $G$.

:::tip[Resultado]
$G$ como arriba, $\dim\mathcal C=\dim\mathcal C^\perp=3$ y $d(\mathcal C)=3$. $r=101110$ tiene síndrome $(0,1,1)^t$ y se corrige a $100110$. Con dos errores el método decodifica una palabra equivocada ($011110$).
:::

</details>
