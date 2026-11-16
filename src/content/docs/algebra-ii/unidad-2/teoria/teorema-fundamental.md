---
title: Teorema fundamental de las transformaciones lineales
description: Una TL queda determinada por lo que hace en una base y cualquier asignación sobre una base se extiende; fórmulas por coordenadas y por matriz, núcleo e imagen prescritos y datos sobre vectores LD.
slug: algebra-ii/unidad-2/teoria/teorema-fundamental
sidebar:
  order: 5
  label: 2.5 Teorema fundamental
---

## Para qué sirve

¿Cuánta información hace falta para describir una TL? Una función cualquiera de $\mathbb{R}^2$ en $\mathbb{R}^3$ necesita un valor por cada punto del plano. Una TL, en cambio, queda completamente fijada por **dos** vectores de $\mathbb{R}^3$: los transformados de una base. El resto se calcula por linealidad. Esa es la idea del teorema fundamental, que responde dos preguntas:

- **Unicidad.** Si dos TL coinciden sobre una base, son la misma.
- **Existencia.** Cualquier elección de imágenes para los vectores de una base se realiza con una TL.

Con él se construyen TL a pedido ("hallar una TL tal que..."), se decide cuándo no existe ninguna y se cuentan cuántas hay. Es la herramienta de existencia de toda la unidad.

## Enunciado

:::note[Teorema fundamental de las transformaciones lineales]
Sea $V$ un espacio de dimensión finita con base $B=\{b_1,\dots,b_n\}$ y sean $w_1,\dots,w_n$ vectores cualesquiera de un espacio $W$ (repetidos o no, LI o no). Entonces existe **una única** TL $T:V\to W$ tal que

$$
T(b_i)=w_i\qquad\text{para } i=1,\dots,n.
$$
:::

Observaciones: los $w_i$ no tienen ninguna restricción; la base es de $V$ (el espacio de salida), no de $W$; y "única" se refiere a la TL con esos datos sobre **esa** base.

## Demostración

**Existencia.** Definimos $T:V\to W$ por

$$
T(v)=x_1w_1+\cdots+x_nw_n,\qquad\text{donde }(x_1,\dots,x_n)=[v]_B.
$$

Está bien definida porque las coordenadas de $v$ en $B$ existen y son únicas. *Es lineal:* como $[u+v]_B=[u]_B+[v]_B$ y $[\lambda v]_B=\lambda[v]_B$ (resultado de [2.4](/algebra-ii/unidad-2/teoria/clasificacion/)), $T(u+v)=\sum(x_i+y_i)w_i=\sum x_iw_i+\sum y_iw_i=T(u)+T(v)$, y $T(\lambda v)=\sum(\lambda x_i)w_i=\lambda T(v)$. *Cumple los datos:* $[b_j]_B=e_j$, así que $T(b_j)=0\,w_1+\cdots+1\,w_j+\cdots+0\,w_n=w_j$.

**Unicidad.** Sea $S:V\to W$ otra TL con $S(b_i)=w_i$ para todo $i$. Si $v=x_1b_1+\cdots+x_nb_n$, por linealidad

$$
S(v)=x_1S(b_1)+\cdots+x_nS(b_n)=x_1w_1+\cdots+x_nw_n=T(v).
$$

Entonces $S=T$. $\blacksquare$

**Corolario.** Dos TL $T,S:V\to W$ que coinciden sobre una base de $V$ son iguales. Y la TL que se anula sobre una base es la TL nula.

## Cómo se arma la fórmula

Sea $T$ la TL con $T(b_i)=w_i$. Hay dos caminos para obtener $T(v)$ para un $v$ genérico.

**Por coordenadas.** Se calculan las coordenadas $[v]_B=(x_1,\dots,x_n)$ (resolviendo un sistema, o con $C_{EB}$ si $V=\mathbb{R}^n$) y se arma $T(v)=x_1w_1+\cdots+x_nw_n$. Sirve en cualquier espacio, de polinomios o de matrices incluido.

**Por matriz** (cuando $V=K^n$ y $W=K^m$). Sea $C=(b_1\mid\cdots\mid b_n)$ la matriz cuyas columnas son los vectores de la base, y $\mathcal W=(w_1\mid\cdots\mid w_n)$ la de los vectores imagen. Buscamos $A\in K^{m\times n}$ con $T(v)=Av$. Los datos dicen $Ab_j=w_j$ para cada $j$, es decir $AC=\mathcal W$. Como $C$ es inversible (sus columnas son una base),

$$
A=\mathcal W\,C^{-1}.
$$

Conviene el primer camino si hay que evaluar en pocos vectores, y el segundo si se necesita la fórmula completa y $C^{-1}$ es fácil de obtener.

### Ejemplo 1 · Una TL de ℝ² en ℝ³ definida sobre una base no canónica
<!-- check: U2.T05.E1 -->

Hallar la TL $T:\mathbb{R}^2\to\mathbb{R}^3$ tal que $T(1,2)=(3,1,0)$ y $T(1,3)=(4,1,-1)$.

Los datos están sobre $B=\{(1,2),(1,3)\}$, que es base de $\mathbb{R}^2$ (el determinante $1\cdot3-1\cdot2=1\neq0$ muestra que es LI). Por el teorema existe una única TL.

**Primer método (coordenadas).** Para $(x,y)$ planteamos $(x,y)=\alpha(1,2)+\beta(1,3)$:

$$
\begin{cases}\alpha+\beta=x\\2\alpha+3\beta=y\end{cases}\ \Longrightarrow\ \beta=y-2x,\quad\alpha=3x-y.
$$

Luego

$$
T(x,y)=(3x-y)(3,1,0)+(y-2x)(4,1,-1)=(x+y,\ \ x,\ \ 2x-y).
$$

**Segundo método (matriz).** $C=\begin{pmatrix}1&1\\2&3\end{pmatrix}$, $C^{-1}=\begin{pmatrix}3&-1\\-2&1\end{pmatrix}$ y $\mathcal W=\begin{pmatrix}3&4\\1&1\\0&-1\end{pmatrix}$. Entonces

$$
A=\mathcal W\,C^{-1}=\begin{pmatrix}3&4\\1&1\\0&-1\end{pmatrix}\begin{pmatrix}3&-1\\-2&1\end{pmatrix}=\begin{pmatrix}1&1\\1&0\\2&-1\end{pmatrix},
$$

que da la misma fórmula: $A\binom xy=(x+y,\ x,\ 2x-y)$.

**Comprobación.** $T(1,2)=(3,1,0)$ y $T(1,3)=(1+3,\ 1,\ 2-3)=(4,1,-1)$. Se cumplen los dos datos.

## Datos sobre vectores linealmente dependientes

El teorema pide una base. ¿Qué pasa si se dan imágenes de vectores que no son una base: demasiados, o dependientes, o pocos?

:::note[Propiedad · Datos sobre vectores cualesquiera]
Sean $v_1,\dots,v_k\in V$ y $w_1,\dots,w_k\in W$.

1. **Condición necesaria.** Si existe una TL con $T(v_i)=w_i$, entonces toda relación lineal entre los $v_i$ se respeta entre los $w_i$: si $\sum\lambda_iv_i=0_V$, entonces $\sum\lambda_iw_i=0_W$.
2. **Existencia.** Si los $v_i$ generan $V$, la condición anterior (para todas las relaciones) también es suficiente.
3. **Unicidad.** La TL, si existe, es única si y solo si $\operatorname{gen}\{v_1,\dots,v_k\}=V$. Si no generan, hay infinitas (sobre $\mathbb{R}$).
:::

**Demostración.**

1. $0_W=T(0_V)=T\big(\sum\lambda_iv_i\big)=\sum\lambda_iT(v_i)=\sum\lambda_iw_i$.
2. Los $v_i$ generan $V$, así que contienen una base: renumerando, $v_1,\dots,v_n$. Por el teorema fundamental existe una TL $T$ con $T(v_i)=w_i$ para $i\le n$. Para $j>n$ escribimos $v_j=\sum_{i\le n}c_iv_i$; esto es la relación $v_j-\sum c_iv_i=0_V$, que por hipótesis se respeta: $w_j=\sum c_iw_i=\sum c_iT(v_i)=T(v_j)$. Entonces $T(v_j)=w_j$ para todo $j$.
3. Si los $v_i$ generan, dos TL que coinciden sobre ellos coinciden sobre todo $V$. Si no generan, existe $v\notin\operatorname{gen}\{v_i\}$; tomamos una base de $\operatorname{gen}\{v_i\}$ y la extendemos a una base de $V$ agregando $v$ y, si hace falta, otros vectores. Por el teorema fundamental, $T$ se puede definir con los mismos datos sobre la base de $\operatorname{gen}\{v_i\}$ y con cualquier valor de $T(v)$; cada valor distinto da una TL distinta que cumple los datos (para los $v_i$ restantes valen las relaciones, como en el punto 2). $\blacksquare$

En la práctica: **para saber si un conjunto de datos sobre vectores LD es compatible, hay que mirar las relaciones de dependencia y verificar que las imágenes cumplan la misma relación.**

### Ejemplo 2 · Existen infinitas TL
<!-- check: U2.T05.E2 -->

¿Existe $T:\mathbb{R}^3\to\mathbb{R}^2$ con $T(1,0,1)=(1,2)$, $T(0,1,1)=(2,-1)$ y $T(1,1,2)=(3,1)$? ¿Es única?

Sean $v_1=(1,0,1)$, $v_2=(0,1,1)$, $v_3=(1,1,2)$. Son LD: $v_3=v_1+v_2$. Los datos respetan la relación, pues $w_1+w_2=(1,2)+(2,-1)=(3,1)=w_3$. **Entonces existe.**

No es única: $\{v_1,v_2\}$ genera solo un plano de $\mathbb{R}^3$. Completamos con $e_3=(0,0,1)$ para obtener la base $\{v_1,v_2,e_3\}$ (la matriz con esas columnas es triangular inferior con unos en la diagonal, de determinante $1$; o bien: $e_3$ no es combinación de $v_1,v_2$, porque $xv_1+yv_2=(x,y,x+y)$ con $x=y=0$ da el vector nulo). Las coordenadas de $(x,y,z)$ son $(x,\ y,\ z-x-y)$, porque $xv_1+yv_2=(x,y,x+y)$. Dejamos $T(e_3)=w$ libre, con $w\in\mathbb{R}^2$ cualquiera:

$$
T(x,y,z)=x(1,2)+y(2,-1)+(z-x-y)\,w.
$$

Para $w=(0,0)$ la TL es $T_0(x,y,z)=(x+2y,\ 2x-y)$ y para $w=(1,1)$ es $T_1(x,y,z)=(y+z,\ x-2y+z)$. Las dos cumplen los tres datos: $T_1(1,0,1)=(1,2)$, $T_1(0,1,1)=(2,-1)$, $T_1(1,1,2)=(3,1)$, y análogamente $T_0$. Pero $T_0(e_3)=(0,0)\neq(1,1)=T_1(e_3)$: son TL distintas.

### Ejemplo 3 · No existe ninguna TL
<!-- check: U2.T05.E3 -->

¿Existe $T:\mathbb{R}^3\to\mathbb{R}^2$ con $T(1,0,1)=(1,2)$, $T(0,1,1)=(2,-1)$ y $T(1,1,2)=(3,0)$?

Los vectores son los mismos del ejemplo 2, con la relación $v_3=v_1+v_2$. Si $T$ existiera, por linealidad

$$
T(v_3)=T(v_1)+T(v_2)=(1,2)+(2,-1)=(3,1)\neq(3,0).
$$

Contradicción: **no existe ninguna TL con esos datos.** Basta una sola relación violada para descartarla; no hace falta buscar más.

## Núcleo e imagen prescritos

El teorema permite construir TL con un núcleo y una imagen dados, siempre que las dimensiones sean compatibles con el [teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/).

:::note[Propiedad · Núcleo e imagen a pedido]
Sean $V$ de dimensión $n$, $S\subseteq V$ un subespacio de dimensión $k$ y $U\subseteq W$ un subespacio de dimensión $n-k$. Entonces existe una TL $T:V\to W$ con $\operatorname{Nu}(T)=S$ e $\operatorname{Im}(T)=U$. Recíprocamente, si existe, $\dim S+\dim U=n$.
:::

**Demostración.** ($\Leftarrow$) es el teorema de la dimensión. ($\Rightarrow$) Sea $\{s_1,\dots,s_k\}$ una base de $S$; la extendemos a una base $B=\{s_1,\dots,s_k,v_{k+1},\dots,v_n\}$ de $V$. Sea $\{u_1,\dots,u_{n-k}\}$ una base de $U$. Por el teorema fundamental existe $T$ con

$$
T(s_i)=0_W\ (i\le k),\qquad T(v_{k+j})=u_j\ (j=1,\dots,n-k).
$$

Entonces $\operatorname{Im}(T)=\operatorname{gen}\{T(s_i),T(v_{k+j})\}=\operatorname{gen}\{u_1,\dots,u_{n-k}\}=U$. Además $S\subseteq\operatorname{Nu}(T)$ y, por el teorema de la dimensión, $\dim\operatorname{Nu}(T)=n-(n-k)=k=\dim S$; un subespacio contenido en otro de la misma dimensión es igual: $\operatorname{Nu}(T)=S$. $\blacksquare$

La receta es: **base del núcleo, completar a una base de $V$, mandar los vectores agregados a una base de la imagen.**

### Ejemplo 4 · Núcleo e imagen prescritos
<!-- check: U2.T05.E4 -->

Hallar una TL $T:\mathbb{R}^3\to P_2[\mathbb{R}]$ con $\operatorname{Nu}(T)=\operatorname{gen}\{(1,-1,0)\}$ e $\operatorname{Im}(T)=\operatorname{gen}\{1+x,\ x-x^2\}$.

**Compatibilidad.** $\dim\operatorname{Nu}+\dim\operatorname{Im}=1+2=3=\dim\mathbb{R}^3$: el pedido es posible.

**Base.** Completamos $(1,-1,0)$ con $(0,1,0)$ y $(0,0,1)$: $B=\{(1,-1,0),(0,1,0),(0,0,1)\}$ es base de $\mathbb{R}^3$ (la matriz con esas columnas es triangular con unos en la diagonal). Definimos

$$
T(1,-1,0)=0,\qquad T(0,1,0)=1+x,\qquad T(0,0,1)=x-x^2.
$$

**Fórmula.** $(a,b,c)=a(1,-1,0)+(a+b)(0,1,0)+c(0,0,1)$ (en efecto, $a(1,-1,0)+(a+b)(0,1,0)=(a,b,0)$). Entonces

$$
T(a,b,c)=(a+b)(1+x)+c(x-x^2)=(a+b)+(a+b+c)\,x-c\,x^2.
$$

**Comprobación.** $T(1,-1,0)=0+0x+0x^2$. Respecto de las bases canónicas $E=\{e_1,e_2,e_3\}$ y $\{1,x,x^2\}$, la matriz tiene columnas $T(e_1)=1+x$, $T(e_2)=1+x$, $T(e_3)=x-x^2$, es decir

$$
\begin{pmatrix}1&1&0\\1&1&1\\0&0&-1\end{pmatrix}.
$$

El núcleo de esta matriz se obtiene de $a+b=0$ y $c=0$: es $\operatorname{gen}\{(1,-1,0)\}$. La imagen está generada por $1+x$ y $x-x^2$, que son LI. Se cumplen los dos requisitos. Hay otras TL que también los cumplen (por ejemplo, cambiando $(0,1,0)\mapsto 1+x$ por $(0,1,0)\mapsto x-x^2$ y $(0,0,1)\mapsto 1+x$): el pedido no determina una única TL.

### Ejemplo 5 · Un endomorfismo con núcleo igual a imagen
<!-- check: U2.T05.E5 -->

Hallar $T:\mathbb{R}^4\to\mathbb{R}^4$ con $\operatorname{Nu}(T)=\operatorname{Im}(T)$.

Si existe, el teorema de la dimensión da $4=\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)=2\dim\operatorname{Im}(T)$, así que ambos son de dimensión 2. Elegimos $S=\operatorname{gen}\{e_1,e_2\}$ y definimos sobre la base canónica

$$
T(e_1)=0,\quad T(e_2)=0,\quad T(e_3)=e_1,\quad T(e_4)=e_2.
$$

La fórmula es $T(x_1,x_2,x_3,x_4)=(x_3,x_4,0,0)$. Su imagen es $\operatorname{gen}\{e_1,e_2\}$ (dimensión 2), contiene a $e_1$ y $e_2$, que están en el núcleo, y por dimensión el núcleo es exactamente $\operatorname{gen}\{e_1,e_2\}$. Luego $\operatorname{Nu}(T)=\operatorname{Im}(T)$.

**Comprobación.** $T(5,-1,2,3)=(2,3,0,0)$. Además $T(T(v))=0$ para todo $v$ (la imagen está en el núcleo), es decir, $T\circ T$ es la TL nula. Observación: esto no puede pasar en dimensión impar, porque $2\dim\operatorname{Im}(T)=\dim V$ exige $\dim V$ par.

:::caution[Errores frecuentes]
- **Dar imágenes para vectores que no son base y decir que "existe una única TL".** En el ejemplo 2 los tres vectores son LD y hay infinitas; con una base de $\mathbb{R}^3$ habría exactamente una.
- **Asignar imágenes arbitrarias a vectores LD.** Los datos de los ejemplos 2 y 3 difieren solo en $w_3$, y en un caso hay infinitas TL y en el otro ninguna.
- **Usar la matriz de la base en lugar de su inversa.** En $A=\mathcal W\,C^{-1}$ el factor $C^{-1}$ va a la derecha; $\mathcal W\,C$ no tiene sentido (a veces ni las dimensiones) ni da la TL. Siempre se verifica $A\,b_j=w_j$.
- **Tomar los $w_i$ como coordenadas.** La fórmula $T(v)=\sum x_iw_i$ produce un vector de $W$ (una terna, un polinomio, una matriz), no una lista de coeficientes.
- **Pedir núcleo e imagen sin controlar las dimensiones.** No existe $T:\mathbb{R}^3\to\mathbb{R}^3$ con $\operatorname{Nu}(T)=\operatorname{gen}\{e_1\}$ e $\operatorname{Im}(T)=\operatorname{gen}\{e_1\}$: $1+1\neq 3$.
:::

## Autoevaluación

1. ¿Cuántas TL $T:\mathbb{R}^2\to\mathbb{R}^2$ cumplen $T(1,1)=(2,0)$?

<details>
<summary>Respuesta</summary>

Infinitas: $\{(1,1)\}$ no es base de $\mathbb{R}^2$. Hay que elegir $T(0,1)$ libremente y queda determinada $T(1,0)=(2,0)-T(0,1)$.

</details>

2. ¿Existe $T:\mathbb{R}^2\to\mathbb{R}^2$ con $T(1,2)=(1,0)$, $T(2,4)=(0,1)$?

<details>
<summary>Respuesta</summary>

No: $(2,4)=2(1,2)$ obligaría a $T(2,4)=2(1,0)=(2,0)\neq(0,1)$.

</details>

3. Si $T,S:V\to W$ coinciden sobre un conjunto generador de $V$, ¿qué se concluye?

<details>
<summary>Respuesta</summary>

Que $T=S$: el conjunto contiene una base y las dos TL coinciden sobre ella (corolario del teorema).

</details>

:::tip[En resumen]
- Dada una base $\{b_i\}$ de $V$ y vectores $w_i\in W$ cualesquiera, existe **una única** TL con $T(b_i)=w_i$.
- Fórmula: $T(v)=\sum x_iw_i$ con $x=[v]_B$; en $K^n$, $A=(w_1\mid\cdots\mid w_n)\,(b_1\mid\cdots\mid b_n)^{-1}$.
- Núcleo e imagen a pedido: base del núcleo $\to$ completar a base de $V$ $\to$ enviar lo agregado a una base de la imagen; hace falta $\dim S+\dim U=\dim V$.
- Datos sobre vectores LD: compatibles si las imágenes respetan cada relación de dependencia; hay unicidad si y solo si los vectores generan $V$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 6.4 (p. 490), donde se prueba que una TL queda determinada por su acción sobre una base.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: la parte sobre transformaciones lineales y su matriz estándar.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed.: capítulo 5, sección 5.1 (p. 178).
- Antes: [2.4 Clasificación](/algebra-ii/unidad-2/teoria/clasificacion/) y [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/).
- Después: [2.6 Matriz asociada](/algebra-ii/unidad-2/teoria/matriz-asociada/).
