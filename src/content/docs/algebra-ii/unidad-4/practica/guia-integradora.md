---
title: Práctica — Guía integradora
description: Cinco problemas de varios ítems, al estilo de un parcial, que integran productos internos no usuales, Gram-Schmidt, complemento ortogonal, proyección, mejor aproximación, cuadrados mínimos y códigos, con puntaje orientativo y resolución completa.
slug: algebra-ii/unidad-4/practica/guia-integradora
sidebar:
  order: 4
  label: Guía integradora
---

:::note[Cómo usar esta página]
Cinco problemas **originales** de varios ítems, con el formato y el nivel de un parcial de la unidad. Cada problema vale **10 puntos orientativos**, repartidos por ítem (entre paréntesis); no son los de ningún examen tomado por la cátedra. Sugerencia: resolvé uno en unos 25 minutos, con todas las respuestas justificadas y sin mirar la resolución, y recién después corregite con ella.

**Presupone:** toda la teoría de la unidad,
[4.1 Producto interno](/algebra-ii/unidad-4/teoria/producto-interno/),
[4.2 Norma, distancia y ángulo](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/),
[4.3 Ortogonalidad](/algebra-ii/unidad-4/teoria/ortogonalidad/),
[4.4 Gram-Schmidt](/algebra-ii/unidad-4/teoria/gram-schmidt/),
[4.5 Complemento ortogonal](/algebra-ii/unidad-4/teoria/complemento-ortogonal/),
[4.6 Proyección y distancia](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/),
[4.7 Cuadrados mínimos](/algebra-ii/unidad-4/teoria/cuadrados-minimos/) y
[4.8 Códigos y $\mathbb{Z}_2^n$](/algebra-ii/unidad-4/teoria/codigos-y-z2/). Para practicar de a un tema por vez, ver el [nivel inicial](/algebra-ii/unidad-4/practica/nivel-inicial/), el [intermedio](/algebra-ii/unidad-4/practica/nivel-intermedio/) y el [avanzado](/algebra-ii/unidad-4/practica/nivel-avanzado/).
:::

### Ejercicio 28 · Un producto interno matricial en $\mathbb{R}^3$
<!-- ejercicio: U4.28 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^3$ se define $\langle x,y\rangle=x^tMy$ con $M=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix}$.

a) **(2)** Probar que $\langle\ ,\ \rangle$ es un producto interno.

b) **(2)** Para $u=(1,0,1)$ y $v=(0,1,0)$, calcular $\langle u,v\rangle$, $\lVert u\rVert$, $\lVert v\rVert$ y el ángulo entre $u$ y $v$.

c) **(2)** Sea $S=\operatorname{gen}\{e_1,e_2\}$. Aplicar Gram-Schmidt a $\{e_1,e_2\}$ y hallar una base ortogonal de $S$.

d) **(2)** Hallar una base de $S^\perp$.

e) **(2)** Calcular $\operatorname{proy}_S(w)$ y $d(w,S)$ para $w=(2,1,3)$.
:::

<details>
<summary>Resolución</summary>

**a)** $M$ es simétrica, de modo que $\langle\ ,\ \rangle$ es simétrica y bilineal. Para la positividad definida usamos el criterio de los menores principales: $\det(2)=2>0$, $\det\begin{pmatrix}2&1\\1&2\end{pmatrix}=3>0$ y $\det M=2(4-1)-1(2-0)=4>0$. Entonces $M$ es definida positiva y **es producto interno**.

**b)** $Mu=(2,2,2)^t$, de modo que $\langle u,v\rangle=u^tMv=(Mu)^tv=2$ (segunda coordenada de $Mu$, pues $v=e_2$). Además $\langle u,u\rangle=u\cdot Mu=2+0+2=4$, o sea $\lVert u\rVert=2$, y $\langle v,v\rangle=m_{22}=2$, o sea $\lVert v\rVert=\sqrt2$. Entonces
$$
\cos\angle(u,v)=\frac{2}{2\sqrt2}=\frac{\sqrt2}{2},\qquad\angle(u,v)=\frac\pi4.
$$

**c)** $w_1=e_1$, con $\langle e_1,e_1\rangle=2$. $\langle e_2,e_1\rangle=m_{12}=1$, entonces $w_2=e_2-\frac12e_1=\left(-\frac12,1,0\right)$. Reescalado, $w_2'=(-1,2,0)$. Su norma: $Mw_2'=(0,3,2)^t$ y $\langle w_2',w_2'\rangle=0+6+0=6$. Una base ortogonal de $S$ es $\{(1,0,0),(-1,2,0)\}$ con normas al cuadrado $2$ y $6$.

**d)** $x\in S^\perp$ si y solo si $\langle x,e_1\rangle=0$ y $\langle x,e_2\rangle=0$, es decir, las dos primeras coordenadas de $Mx$ se anulan: $2x_1+x_2=0$ y $x_1+2x_2+x_3=0$. De la primera $x_2=-2x_1$; de la segunda $x_3=-x_1-2x_2=3x_1$. Entonces $S^\perp=\operatorname{gen}\{n\}$ con $n=(1,-2,3)$.

**e)** $Mn=(0,0,4)^t$ y $\langle n,n\rangle=12$. Para $w=(2,1,3)$: $\langle w,n\rangle=w\cdot Mn=12$, de modo que $\operatorname{proy}_{S^\perp}(w)=\frac{12}{12}n=(1,-2,3)$ y
$$
\operatorname{proy}_S(w)=w-n=(1,3,0),\qquad d(w,S)=\lVert n\rVert=\sqrt{12}=2\sqrt3.
$$

**Comprobación.** Con la base ortogonal de c): $\langle w,e_1\rangle=w\cdot Me_1=(2,1,3)\cdot(2,1,0)=5$ y $\langle w,w_2'\rangle=(2,1,3)\cdot(0,3,2)=9$; entonces $\frac52e_1+\frac96w_2'=(\frac52,0,0)+(-\frac32,3,0)=(1,3,0)$ ✓. Además $(1,3,0)\in S$ y $w-(1,3,0)=n\in S^\perp$.

:::tip[Resultado]
a) $M$ es definida positiva (menores $2,3,4$). b) $\langle u,v\rangle=2$, $\lVert u\rVert=2$, $\lVert v\rVert=\sqrt2$, ángulo $\pi/4$. c) $\{(1,0,0),(-1,2,0)\}$. d) $S^\perp=\operatorname{gen}\{(1,-2,3)\}$. e) $\operatorname{proy}_S(w)=(1,3,0)$, $d(w,S)=2\sqrt3$.
:::

</details>

### Ejercicio 29 · Un subespacio de matrices con el producto de la traza
<!-- ejercicio: U4.29 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
En $\mathbb{R}^{2\times2}$ con $\langle A,B\rangle=\operatorname{tr}(B^tA)$ sean $B_1=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $B_2=\begin{pmatrix}1&2\\1&0\end{pmatrix}$, $S=\operatorname{gen}\{B_1,B_2\}$ y $A=\begin{pmatrix}1&3\\2&2\end{pmatrix}$.

a) **(2)** Aplicar Gram-Schmidt a $\{B_1,B_2\}$ y obtener una base ortogonal de $S$.

b) **(2)** Hallar una base de $S^\perp$.

c) **(3)** Calcular $\operatorname{proy}_S(A)$ y $d(A,S)$.

d) **(3)** Escribir $A-\operatorname{proy}_S(A)$ en la base de $S^\perp$ del ítem b) y verificar el teorema de Pitágoras para $A$.
:::

<details>
<summary>Resolución</summary>

**a)** $w_1=B_1$, con $\langle B_1,B_1\rangle=1+1+0+1=3$. $\langle B_2,B_1\rangle=1+2+0+0=3$, entonces $w_2=B_2-\frac33B_1=\begin{pmatrix}0&1\\1&-1\end{pmatrix}$, con $\langle w_2,w_2\rangle=0+1+1+1=3$. Base ortogonal: $\left\{\begin{pmatrix}1&1\\0&1\end{pmatrix},\begin{pmatrix}0&1\\1&-1\end{pmatrix}\right\}$.

**b)** Para $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, las condiciones $\langle X,w_1\rangle=a+b+d=0$ y $\langle X,w_2\rangle=b+c-d=0$ (con la base ortogonal, equivalentes a las de $B_1,B_2$) dan $c=d-b$ y $a=-b-d$. Con $b,d$ libres: $b=1,d=0$ da $\begin{pmatrix}-1&1\\-1&0\end{pmatrix}$ y $b=0,d=1$ da $\begin{pmatrix}-1&0\\1&1\end{pmatrix}$. Una base de $S^\perp$ es $\left\{\begin{pmatrix}-1&1\\-1&0\end{pmatrix},\begin{pmatrix}-1&0\\1&1\end{pmatrix}\right\}$, con $\dim S^\perp=2$ (coherente con $\dim S+\dim S^\perp=4$).

**c)** $\langle A,w_1\rangle=1+3+0+2=6$ y $\langle A,w_2\rangle=0+3+2-2=3$. Entonces
$$
\operatorname{proy}_S(A)=\frac63w_1+\frac33w_2=2\begin{pmatrix}1&1\\0&1\end{pmatrix}+\begin{pmatrix}0&1\\1&-1\end{pmatrix}=\begin{pmatrix}2&3\\1&1\end{pmatrix}.
$$
El resto es $A-\operatorname{proy}_S(A)=\begin{pmatrix}-1&0\\1&1\end{pmatrix}$, de norma al cuadrado $1+0+1+1=3$: $d(A,S)=\sqrt3$.

**d)** El resto $\begin{pmatrix}-1&0\\1&1\end{pmatrix}$ es exactamente el segundo vector de la base de $S^\perp$ hallada (coordenadas $(0,1)$ en esa base). Pitágoras: $\lVert A\rVert^2=1+9+4+4=18$ y $\lVert\operatorname{proy}_S(A)\rVert^2+\lVert A-\operatorname{proy}_S(A)\rVert^2=(4+9+1+1)+3=18$.

**Comprobación.** $\langle\begin{pmatrix}-1&0\\1&1\end{pmatrix},B_1\rangle=-1+0+0+1=0$ y $\left\langle\begin{pmatrix}-1&0\\1&1\end{pmatrix},B_2\right\rangle=-1+0+1+0=0$. Además $2B_1+w_2=2B_1+(B_2-B_1)=B_1+B_2=\begin{pmatrix}2&3\\1&1\end{pmatrix}$, que pertenece a $S$.

:::tip[Resultado]
a) $\{B_1,\ B_2-B_1\}$. b) Base de $S^\perp$: $\begin{pmatrix}-1&1\\-1&0\end{pmatrix}$, $\begin{pmatrix}-1&0\\1&1\end{pmatrix}$. c) $\operatorname{proy}_S(A)=B_1+B_2=\begin{pmatrix}2&3\\1&1\end{pmatrix}$ y $d(A,S)=\sqrt3$. d) $A-\operatorname{proy}_S(A)$ es el segundo vector de la base de $S^\perp$; $18=15+3$.
:::

</details>

### Ejercicio 30 · Un producto por evaluación con un parámetro
<!-- ejercicio: U4.30 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Para $a\in\mathbb{R}$ se define en $P_2[\mathbb{R}]$ la función $\langle p,q\rangle_a=p(-1)q(-1)+2p(0)q(0)+a\,p(1)q(1)$.

a) **(3)** Hallar todos los $a$ para los cuales $\langle\ ,\ \rangle_a$ es un producto interno.

b) **(2)** Para $a=1$, aplicar Gram-Schmidt a $\{1,x,x^2\}$ y calcular las normas de la base ortogonal obtenida.

c) **(3)** Para $a=1$, hallar el polinomio de $P_1[\mathbb{R}]$ más cercano a $q=2x^2+x$ y la distancia de $q$ a $P_1[\mathbb{R}]$.

d) **(2)** Para $a=3$, hallar $c\in\mathbb{R}$ tal que $x^2+c\perp1$.
:::

<details>
<summary>Resolución</summary>

**a)** La función es simétrica y bilineal para todo $a$. Para la positividad, $\langle p,p\rangle_a=p(-1)^2+2p(0)^2+a\,p(1)^2$. Si $a>0$, es $\ge0$ y se anula solo si $p(-1)=p(0)=p(1)=0$, que implica $p=0$ (grado $\le2$ con tres raíces). Si $a\le0$, el polinomio $p=x^2+x$ cumple $p(-1)=0$, $p(0)=0$ y $p(1)=2$, de modo que $\langle p,p\rangle_a=4a\le0$ con $p\neq0$. Entonces **es producto interno si y solo si $a>0$**.

**b)** Con $a=1$ los pesos en $(-1,0,1)$ son $(1,2,1)$. Los valores son $1\leftrightarrow(1,1,1)$, $x\leftrightarrow(-1,0,1)$ y $x^2\leftrightarrow(1,0,1)$. $w_1=1$ con $\langle1,1\rangle=1+2+1=4$. $\langle x,1\rangle=-1+0+1=0$, de modo que $w_2=x$, con $\langle x,x\rangle=1+0+1=2$. $\langle x^2,1\rangle=1+0+1=2$ y $\langle x^2,x\rangle=-1+0+1=0$, de modo que $w_3=x^2-\frac24\cdot1=x^2-\frac12$, con valores $(\frac12,-\frac12,\frac12)$ y $\langle w_3,w_3\rangle=\frac14+2\cdot\frac14+\frac14=1$. La base ortogonal $\{1,x,x^2-\frac12\}$ tiene normas $2$, $\sqrt2$ y $1$.

**c)** $P_1[\mathbb{R}]=\operatorname{gen}\{1,x\}$ y $\{1,x\}$ es ortogonal. Los valores de $q=2x^2+x$ en $(-1,0,1)$ son $(1,0,3)$. $\langle q,1\rangle=1+0+3=4$ y $\langle q,x\rangle=-1+0+3=2$. Entonces
$$
\operatorname{proy}(q)=\frac44\cdot1+\frac22x=1+x.
$$
El resto es $q-(1+x)=2x^2-1=2\left(x^2-\frac12\right)$, de norma $2\cdot1=2$. La distancia es $2$.

**d)** Con $a=3$: $\langle x^2+c,1\rangle=1\cdot(1+c)+2\cdot c+3\cdot(1+c)=4+6c=0$ si y solo si $c=-\frac23$.

**Comprobación.** Para a), con $a=0$: $\langle x^2+x,x^2+x\rangle_0=0+0+0=0$. Para c), $\langle2x^2-1,1\rangle=1\cdot1+2\cdot(-1)+1\cdot1=0$ y $\langle2x^2-1,x\rangle=-1+0+1=0$. Para d), con $c=-\frac23$: $\frac13+2\cdot(-\frac23)+3\cdot\frac13=\frac13-\frac43+1=0$.

:::tip[Resultado]
a) producto interno si y solo si $a>0$. b) $\{1,x,x^2-\frac12\}$ con normas $2,\sqrt2,1$. c) $1+x$ y distancia $2$. d) $c=-\frac23$.
:::

</details>

### Ejercicio 31 · Ajuste de datos con cuadrados mínimos
<!-- ejercicio: U4.31 | nivel: avanzado | tipo: aplicacion | verificacion: sympy -->

:::note[Enunciado]
Se midió el tiempo de respuesta $y$ (ms) de un servicio para lotes de 1, 2, 3, 4 y 5 centenas de peticiones. Para simplificar las cuentas se usa la variable centrada $x=\text{lote}-3$:

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
|---|---|---|---|---|---|
| $y$ | 10 | 4 | 7 | 14 | 20 |

a) **(2)** Ajustar la recta $y=c+bx$ por cuadrados mínimos.

b) **(3)** Ajustar la parábola $y=\alpha+\beta x+\gamma x^2$ por cuadrados mínimos.

c) **(2)** Comparar los errores cuadráticos de ambos modelos y verificar que el residuo de la parábola es ortogonal a las columnas de su matriz.

d) **(1)** Estimar el tiempo para un lote de 6 centenas ($x=3$) con cada modelo.

e) **(2)** Probar que si las columnas de $A\in\mathbb{R}^{m\times n}$ son linealmente independientes, entonces $A^tA$ es inversible.
:::

<details>
<summary>Resolución</summary>

**a)** Con $A=(\mathbf 1\mid x)$: $A^tA=\begin{pmatrix}5&0\\0&10\end{pmatrix}$ (porque $\sum x=0$ y $\sum x^2=10$) y $A^ty=\begin{pmatrix}55\\30\end{pmatrix}$ (con $\sum y=55$ y $\sum xy=-20-4+0+14+40=30$). Las ecuaciones normales quedan desacopladas: $5c=55$ y $10b=30$, de modo que $c=11$ y $b=3$. La recta es $y=11+3x$.

**b)** Con $A=(\mathbf 1\mid x\mid x^2)$ se tiene $\sum x^3=0$, $\sum x^4=34$ y $\sum x^2y=40+4+0+14+80=138$:
$$
\begin{pmatrix}5&0&10\\0&10&0\\10&0&34\end{pmatrix}\begin{pmatrix}\alpha\\\beta\\\gamma\end{pmatrix}=\begin{pmatrix}55\\30\\138\end{pmatrix}.
$$
De la segunda ecuación, $\beta=3$. Las otras dos son $5\alpha+10\gamma=55$ y $10\alpha+34\gamma=138$; con $\alpha=11-2\gamma$: $110-20\gamma+34\gamma=138$, o sea $\gamma=2$ y $\alpha=7$. La parábola es $y=7+3x+2x^2$.

**c)** Residuos de la recta: $y-(11+3x)=(5,-4,-4,0,3)$, con error cuadrático $25+16+16+0+9=66$. Residuos de la parábola: $y-(7+3x+2x^2)=(1,-2,0,2,-1)$, con error cuadrático $1+4+0+4+1=10$. La parábola ajusta mucho mejor. El residuo de la parábola es ortogonal a las columnas: $(1,-2,0,2,-1)\cdot(1,1,1,1,1)=0$; $\cdot(-2,-1,0,1,2)=-2+2+0+2-2=0$; $\cdot(4,1,0,1,4)=4-2+0+2-4=0$.

**d)** Para $x=3$: recta $11+9=20$ ms; parábola $7+9+18=34$ ms.

**e) Demostración.** Sea $x\in\mathbb{R}^n$ con $A^tAx=0$. Multiplicando por $x^t$: $0=x^tA^tAx=(Ax)^t(Ax)=\lVert Ax\rVert^2$. Entonces $Ax=0$, y como las columnas de $A$ son LI, $x=0$. Así $\operatorname{nul}(A^tA)=\{0\}$ y la matriz cuadrada $A^tA$ es inversible. $\blacksquare$ (Por eso las ecuaciones normales tienen solución única cuando las columnas de $A$ son LI.)

**Comprobación.** Las ecuaciones normales de la parábola con $(\alpha,\beta,\gamma)=(7,3,2)$: $35+0+20=55$, $30$ y $70+0+68=138$ ✓.

:::tip[Resultado]
Recta $y=11+3x$ (error $66$); parábola $y=7+3x+2x^2$ (error $10$). Estimaciones para $x=3$: $20$ ms y $34$ ms. Si las columnas de $A$ son LI, $A^tA$ es inversible.
:::

</details>

### Ejercicio 32 · Códigos autoduales y duales de subcódigos
<!-- ejercicio: U4.32 | nivel: avanzado | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $\mathcal C\subseteq\mathbb{Z}_2^6$ el código generado por $110000$, $001100$ y $000011$.

a) **(2)** Probar que $\mathcal C$ es autodual.

b) **(2)** Hallar $d(\mathcal C)$ y decir cuántos errores detecta y corrige.

c) **(3)** Sea $\mathcal C_2=\operatorname{gen}\{111100,\ 001111\}$. Verificar que $\mathcal C_2\subseteq\mathcal C$, hallar una base de $\mathcal C_2^\perp$ y calcular $d(\mathcal C_2)$.

d) **(3)** Se recibe $r_1=101100$ y $r_2=100100$ con el código $\mathcal C_2$. Decodificarlas por mínima distancia y comentar.
:::

<details>
<summary>Resolución</summary>

**a)** Cada generador tiene peso $2$, luego $g\cdot g=0$; y los generadores tienen soportes disjuntos, luego $g_i\cdot g_j=0$ para $i\neq j$. Por bilinealidad, todo par de palabras de $\mathcal C$ es ortogonal: $\mathcal C\subseteq\mathcal C^\perp$. Como $\dim\mathcal C=3$ (los generadores son LI) y $\dim\mathcal C^\perp=6-3=3$, resulta $\mathcal C=\mathcal C^\perp$.

**b)** Las palabras de $\mathcal C$ son sumas de bloques $11$ en posiciones $\{1,2\}$, $\{3,4\}$ y $\{5,6\}$. El peso mínimo de una no nula es $2$, por ejemplo $110000$, de modo que $d(\mathcal C)=2$. Detecta $d-1=1$ error y corrige $\lfloor1/2\rfloor=0$.

**c)** $111100=110000+001100\in\mathcal C$ y $001111=001100+000011\in\mathcal C$, luego $\mathcal C_2\subseteq\mathcal C$. Sus palabras son $000000$, $111100$, $001111$ y $110011$ (suma de ambas). $\mathcal C_2^\perp$ tiene dimensión $6-2=4$. Resolviendo $x_1+x_2+x_3+x_4=0$ y $x_3+x_4+x_5+x_6=0$ (equivalen a $x_1=x_2+x_5+x_6$ y $x_3=x_4+x_5+x_6$) con $x_2,x_4,x_5,x_6$ libres:
$$
\{110000,\ 001100,\ 101010,\ 101001\}.
$$
Los pesos de las palabras no nulas de $\mathcal C_2$ son $4$, $4$ y $4$, de modo que $d(\mathcal C_2)=4$ (detecta $3$ y corrige $1$).

**d)** Distancias de $r_1=101100$ a $000000$, $111100$, $001111$ y $110011$: $3$, $1$, $3$ y $5$. La menor es única: se decodifica $111100$ (error en la posición $2$). Para $r_2=100100$: distancias $2$, $2$, $4$ y $4$: **hay dos palabras a distancia $2$** ($000000$ y $111100$), de modo que se detecta el error pero no se puede corregir de forma única. Es consistente con $d=4$: corrige un error, pero con dos errores solo detecta.

**Comprobación.** Los cuatro vectores de la base de $\mathcal C_2^\perp$ son ortogonales a $111100$ y $001111$: por ejemplo $101010\cdot111100=1+0+1+0=0$ y $101010\cdot001111=1+0+1+0=0$; $101001\cdot111100=1+0+1=0$ y $101001\cdot001111=1+0+1=0$. Además $\mathcal C=\mathcal C^\perp\subseteq\mathcal C_2^\perp$ (todo lo ortogonal a $\mathcal C$ lo es a $\mathcal C_2\subseteq\mathcal C$): $110000$ y $001100$ están en la base hallada.

:::tip[Resultado]
a) $\mathcal C=\mathcal C^\perp$. b) $d(\mathcal C)=2$: detecta $1$ error y no corrige. c) $\mathcal C_2\subseteq\mathcal C$, base de $\mathcal C_2^\perp$: $\{110000,001100,101010,101001\}$ y $d(\mathcal C_2)=4$. d) $r_1\mapsto111100$; $r_2=100100$ está a distancia $2$ de dos palabras (no se corrige).
:::

</details>
