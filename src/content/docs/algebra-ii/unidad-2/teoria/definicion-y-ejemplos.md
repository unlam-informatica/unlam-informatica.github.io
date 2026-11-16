---
title: Definición y ejemplos
description: Qué es una transformación lineal, sus propiedades básicas, el test del vector nulo, ejemplos y no ejemplos, y su uso en gráficos por computadora.
slug: algebra-ii/unidad-2/teoria/definicion-y-ejemplos
sidebar:
  order: 1
  label: 2.1 Definición y ejemplos
---

## Para qué sirve

En la Unidad 1 estudiamos espacios vectoriales: conjuntos donde se puede sumar y multiplicar por escalares. El paso siguiente es estudiar las **funciones entre espacios vectoriales que respetan esas dos operaciones**. Se llaman transformaciones lineales (TL) y aparecen en todas partes:

- en gráficos por computadora, rotar, escalar o cizallar una figura es aplicar una TL del plano a cada uno de sus puntos;
- en teoría de códigos, codificar un mensaje $a\in\mathbb{Z}_2^k$ como palabra $aG\in\mathbb{Z}_2^n$ es una TL;
- en análisis, derivar un polinomio es una TL de $P_n[\mathbb{R}]$ en sí mismo;
- todo sistema de ecuaciones lineales $Ax=b$ pregunta por las preimágenes de $b$ bajo la TL $x\mapsto Ax$.

La idea que conviene fijar desde el principio: **una TL queda determinada por lo que hace con pocos vectores** (los de una base), porque todo lo demás se obtiene sumando y multiplicando por escalares. Esa es la razón de que las TL se puedan representar con matrices y de que se calculen tan bien.

## La definición

:::note[Definición]
Sean $V$ y $W$ espacios vectoriales sobre el mismo cuerpo $K$. Una función $T:V\to W$ es una **transformación lineal** si cumple:

1. **Aditividad:** $T(u+v)=T(u)+T(v)$ para todo $u,v\in V$.
2. **Homogeneidad:** $T(\lambda v)=\lambda\,T(v)$ para todo $v\in V$ y todo $\lambda\in K$.

$V$ es el **espacio de salida** y $W$ el **espacio de llegada**.
:::

Conviene leer cada igualdad señalando dónde vive cada operación:

- En $T(u+v)$ la suma $u+v$ se hace **en $V$**; en $T(u)+T(v)$ la suma se hace **en $W$**. La aditividad dice que da lo mismo sumar antes de transformar (en $V$) que transformar y después sumar (en $W$).
- En $T(\lambda v)$ el producto $\lambda v$ es el producto por escalar **de $V$**; en $\lambda T(v)$ es el **de $W$**.

Las dos condiciones se pueden fundir en una sola.

:::note[Propiedad · Condición única]
$T:V\to W$ es lineal si y solo si

$$
T(\alpha u+\beta v)=\alpha\,T(u)+\beta\,T(v)\qquad\text{para todo } u,v\in V,\ \alpha,\beta\in K.
$$
:::

**Demostración.** Si $T$ es lineal, por aditividad y después por homogeneidad,
$T(\alpha u+\beta v)=T(\alpha u)+T(\beta v)=\alpha T(u)+\beta T(v)$.
Recíprocamente, si vale la condición única, con $\alpha=\beta=1$ se obtiene la aditividad, y con $\beta=0$ (y cualquier $v$) se obtiene $T(\alpha u)=\alpha T(u)+0\cdot T(v)=\alpha T(u)$, que es la homogeneidad. $\blacksquare$

### Ejemplo 1 · Una transformación de ℝ³ en ℝ²
<!-- check: U2.T01.E1 -->

Probar que $T:\mathbb{R}^3\to\mathbb{R}^2$, $T(x,y,z)=(x-2y+z,\ 3y-z)$, es una TL y calcular $T(2,1,-1)$.

**Aditividad.** Tomamos $u=(x_1,y_1,z_1)$ y $v=(x_2,y_2,z_2)$ genéricos. Entonces $u+v=(x_1+x_2,\,y_1+y_2,\,z_1+z_2)$ y, aplicando la fórmula,

$$
\begin{aligned}
T(u+v)&=\big((x_1+x_2)-2(y_1+y_2)+(z_1+z_2),\ 3(y_1+y_2)-(z_1+z_2)\big)\\
&=\big(x_1-2y_1+z_1,\ 3y_1-z_1\big)+\big(x_2-2y_2+z_2,\ 3y_2-z_2\big)=T(u)+T(v).
\end{aligned}
$$

En el segundo renglón reagrupamos los términos de $u$ y los de $v$ (propiedades asociativa y conmutativa de los reales).

**Homogeneidad.** Para $\lambda\in\mathbb{R}$, $\lambda u=(\lambda x_1,\lambda y_1,\lambda z_1)$ y

$$
T(\lambda u)=(\lambda x_1-2\lambda y_1+\lambda z_1,\ 3\lambda y_1-\lambda z_1)=\lambda\,(x_1-2y_1+z_1,\ 3y_1-z_1)=\lambda\,T(u).
$$

Luego $T$ es lineal. Además $T(2,1,-1)=(2-2-1,\ 3+1)=(-1,4)$.

**Otra mirada.** Escribiendo los vectores como columnas,

$$
T\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}1&-2&1\\0&3&-1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix},
$$

y la linealidad es consecuencia de las propiedades del producto de matrices: $A(u+v)=Au+Av$ y $A(\lambda u)=\lambda Au$. Toda función de la forma $x\mapsto Ax$ es lineal; en la lección [2.6](/algebra-ii/unidad-2/teoria/matriz-asociada/) veremos que, en cierto sentido, toda TL entre espacios de dimensión finita es de esta forma.

## Propiedades básicas

:::note[Propiedad · Consecuencias inmediatas de la linealidad]
Si $T:V\to W$ es lineal, entonces:

1. $T(0_V)=0_W$.
2. $T(-v)=-T(v)$ para todo $v\in V$.
3. $T(u-v)=T(u)-T(v)$.
4. $T$ preserva combinaciones lineales: $T(\lambda_1v_1+\cdots+\lambda_kv_k)=\lambda_1T(v_1)+\cdots+\lambda_kT(v_k)$.
:::

**Demostración.**

1. Como $0_V=0\cdot 0_V$, por homogeneidad $T(0_V)=T(0\cdot 0_V)=0\cdot T(0_V)=0_W$. (El último paso usa que, en cualquier espacio vectorial, el escalar $0$ por un vector da el vector nulo.)
2. $T(-v)=T((-1)v)=(-1)T(v)=-T(v)$.
3. $T(u-v)=T(u+(-v))=T(u)+T(-v)=T(u)-T(v)$, por aditividad y por 2.
4. Por inducción en $k$. Para $k=1$ es la homogeneidad. Si vale para $k-1$ vectores, separamos el último sumando y usamos aditividad, la hipótesis inductiva y la homogeneidad:
   $T\big(\sum_{i=1}^{k}\lambda_iv_i\big)=T\big(\sum_{i=1}^{k-1}\lambda_iv_i\big)+T(\lambda_kv_k)=\sum_{i=1}^{k-1}\lambda_iT(v_i)+\lambda_kT(v_k)$. $\blacksquare$

La propiedad 4 es la que más vamos a usar: **si conocemos $T$ en $v_1,\dots,v_k$, la conocemos en todo $\operatorname{gen}\{v_1,\dots,v_k\}$**. Es la semilla del [teorema fundamental](/algebra-ii/unidad-2/teoria/teorema-fundamental/).

## El test del vector nulo

La propiedad 1 da un filtro rápido, por su contrarrecíproca:

:::tip[Test del nulo]
Si $T(0_V)\neq 0_W$, entonces $T$ **no** es lineal.
:::

El test es una condición **necesaria pero no suficiente**: hay funciones que llevan el nulo al nulo y no son lineales. Por eso, si $T(0_V)=0_W$, el test no decide nada y hay que verificar las dos condiciones (o encontrar un contraejemplo).

### Ejemplo 2 · Fija el origen pero no es lineal
<!-- check: U2.T01.E2 -->

Decidir si $F:\mathbb{R}^2\to\mathbb{R}^2$, $F(x,y)=(x+y,\ xy)$, es una TL.

$F(0,0)=(0,0)$: el test del nulo no la descarta. Sospechamos por el producto $xy$, que no es de primer grado, y buscamos un contraejemplo concreto.

- **Falla la homogeneidad.** $F(1,1)=(2,1)$, así que $2F(1,1)=(4,2)$; en cambio $F\big(2\cdot(1,1)\big)=F(2,2)=(4,4)$. Como $(4,4)\neq(4,2)$, $F(2v)\neq 2F(v)$ para $v=(1,1)$.
- **También falla la aditividad.** $F(1,0)+F(0,1)=(1,0)+(1,0)=(2,0)$, mientras que $F\big((1,0)+(0,1)\big)=F(1,1)=(2,1)$.

Basta uno de los dos contraejemplos para concluir: **$F$ no es lineal**, aunque $F(0,0)=(0,0)$.

:::note[Observación · Sobre ℤ₂ alcanza con la aditividad]
Si $K=\mathbb{Z}_2$, los únicos escalares son $0$ y $1$. La homogeneidad con $\lambda=1$ es trivial, y con $\lambda=0$ dice $T(0_V)=0_W$, que ya se deduce de la aditividad: $T(0_V)=T(0_V+0_V)=T(0_V)+T(0_V)$, y restando $T(0_V)$ queda $0_W=T(0_V)$. Por lo tanto, **una función entre espacios sobre $\mathbb{Z}_2$ es lineal si y solo si es aditiva**.
:::

## Catálogo de ejemplos

### Transformaciones matriciales

Si $A\in K^{m\times n}$, la función $T_A:K^n\to K^m$, $T_A(x)=Ax$ (con $x$ columna) es lineal, como vimos en el ejemplo 1. Casos geométricos en $\mathbb{R}^2$:

| Transformación | Fórmula | Matriz |
|---|---|---|
| Proyección sobre el eje $x$ | $(x,y)\mapsto(x,0)$ | filas $(1,0)$ y $(0,0)$ |
| Simetría respecto del eje $x$ | $(x,y)\mapsto(x,-y)$ | filas $(1,0)$ y $(0,-1)$ |
| Homotecia de razón $k$ | $(x,y)\mapsto(kx,ky)$ | $kI$ |
| Rotación de ángulo $\theta$ | $(x,y)\mapsto(x\cos\theta-y\sin\theta,\ x\sin\theta+y\cos\theta)$ | filas $(\cos\theta,-\sin\theta)$ y $(\sin\theta,\cos\theta)$ |

La fórmula de la rotación sale de mirar qué les pasa a los vectores canónicos: al rotar $e_1=(1,0)$ un ángulo $\theta$ se obtiene $(\cos\theta,\sin\theta)$, y al rotar $e_2=(0,1)$ se obtiene $(-\sin\theta,\cos\theta)$. Como la rotación respeta paralelogramos (lleva la diagonal de un paralelogramo en la diagonal del paralelogramo rotado) y estiramientos, es lineal, y entonces $R(x,y)=xR(e_1)+yR(e_2)$.

### Ejemplo 3 · Rotación del cuadrado unidad
<!-- check: U2.T01.E3 -->

Sea $R$ la rotación de ángulo $\theta$ con $\cos\theta=\tfrac45$ y $\sin\theta=\tfrac35$ (es un ángulo de unos $36{,}9^\circ$; los valores son consistentes porque $\tfrac{16}{25}+\tfrac{9}{25}=1$). Hallar la imagen del cuadrado unidad, de vértices $(0,0)$, $(1,0)$, $(1,1)$ y $(0,1)$.

La matriz es

$$
R=\begin{pmatrix}\tfrac45&-\tfrac35\\[2pt]\tfrac35&\tfrac45\end{pmatrix}.
$$

Las imágenes de los vértices son $R(0,0)=(0,0)$, $R(1,0)=\big(\tfrac45,\tfrac35\big)$ (primera columna), $R(0,1)=\big(-\tfrac35,\tfrac45\big)$ (segunda columna) y, por aditividad, $R(1,1)=R(1,0)+R(0,1)=\big(\tfrac15,\tfrac75\big)$.

Como $R$ es lineal, lleva cada segmento en un segmento y cada paralelogramo en un paralelogramo: la imagen del cuadrado es el cuadrado de vértices $(0,0)$, $\big(\tfrac45,\tfrac35\big)$, $\big(\tfrac15,\tfrac75\big)$, $\big(-\tfrac35,\tfrac45\big)$.

**Comprobación.** $\det R=\tfrac{16}{25}+\tfrac{9}{25}=1$: el área se conserva, como corresponde a una rotación.

<figure class="math-figure">
<svg viewBox="-110 -170 270 205" role="img" aria-labelledby="dye-rot-t dye-rot-d" xmlns="http://www.w3.org/2000/svg">
<title id="dye-rot-t">Imagen del cuadrado unidad por una rotación</title>
<desc id="dye-rot-d">El cuadrado unidad con los vectores e1=(1,0) y e2=(0,1), y su imagen por la rotación con coseno 4/5 y seno 3/5: un cuadrado congruente con vértices (0,0), (4/5,3/5), (1/5,7/5) y (-3/5,4/5).</desc>
<defs><marker id="dye-rot-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker><marker id="dye-rot-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="scale(1,-1)">
<line class="axis" x1="-100" y1="0" x2="150" y2="0"/>
<line class="axis" x1="0" y1="-25" x2="0" y2="160"/>
<polygon class="region-a" points="0,0 100,0 100,100 0,100"/>
<polygon class="region-b" points="0,0 80,60 20,140 -60,80"/>
<line class="vec-a" x1="0" y1="0" x2="100" y2="0" marker-end="url(#dye-rot-arrow-a)"/>
<line class="vec-a" x1="0" y1="0" x2="0" y2="100" marker-end="url(#dye-rot-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="80" y2="60" marker-end="url(#dye-rot-arrow-b)"/>
<line class="vec-b" x1="0" y1="0" x2="-60" y2="80" marker-end="url(#dye-rot-arrow-b)"/>
</g>
<text class="math" x="104" y="16">e₁</text>
<text class="math" x="6" y="-104">e₂</text>
<text class="math" x="86" y="-62">R(e₁)</text>
<text class="math" x="-66" y="-86" text-anchor="end">R(e₂)</text>
<text class="math" x="24" y="-146">R(e₁+e₂)</text>
</svg>
<figcaption>El cuadrado unidad (sombreado claro) y su imagen por la rotación R. Las columnas de la matriz son exactamente R(e₁) y R(e₂): conociendo esos dos vectores se dibuja la imagen de toda la figura.</figcaption>
</figure>

### Derivación y evaluación de polinomios

- **Derivación.** $D:P_n[\mathbb{R}]\to P_n[\mathbb{R}]$, $D(p)=p'$, es lineal porque $(p+q)'=p'+q'$ y $(\lambda p)'=\lambda p'$. (También se puede tomar $P_{n-1}[\mathbb{R}]$ como llegada.)
- **Evaluación en un punto.** Para $a\in\mathbb{R}$ fijo, $\operatorname{ev}_a:P_n[\mathbb{R}]\to\mathbb{R}$, $\operatorname{ev}_a(p)=p(a)$, es lineal: $(p+q)(a)=p(a)+q(a)$ y $(\lambda p)(a)=\lambda\,p(a)$, por la definición de las operaciones de polinomios.

### Ejemplo 4 · Una TL de polinomios en ℝ²
<!-- check: U2.T01.E4 -->

Probar que $T:P_2[\mathbb{R}]\to\mathbb{R}^2$, $T(p)=\big(p(1),\,p'(0)\big)$, es lineal y calcular $T(2-x+3x^2)$.

**Linealidad.** Cada componente es lineal: la primera es la evaluación en $1$; la segunda es la composición de la derivación con la evaluación en $0$. Hagámoslo directamente con la condición única. Si $p,q\in P_2[\mathbb{R}]$ y $\alpha,\beta\in\mathbb{R}$,

$$
T(\alpha p+\beta q)=\big((\alpha p+\beta q)(1),\ (\alpha p+\beta q)'(0)\big)=\big(\alpha p(1)+\beta q(1),\ \alpha p'(0)+\beta q'(0)\big)=\alpha T(p)+\beta T(q).
$$

**Fórmula general.** Para $p=a_0+a_1x+a_2x^2$: $p(1)=a_0+a_1+a_2$ y $p'(x)=a_1+2a_2x$, así que $p'(0)=a_1$. Luego $T(a_0+a_1x+a_2x^2)=(a_0+a_1+a_2,\ a_1)$.

**Cálculo.** $T(2-x+3x^2)=(2-1+3,\ -1)=(4,-1)$.

Observá que $T$ **recibe polinomios** y devuelve pares de números: escribir $T(2,-1,3)$ sería un error de tipo, aunque $(2,-1,3)$ sean las coordenadas de $p$ en la base $\{1,x,x^2\}$.

### Traza y transposición

- **Traza.** $\operatorname{tr}:\mathbb{R}^{n\times n}\to\mathbb{R}$, $\operatorname{tr}(A)=a_{11}+\cdots+a_{nn}$, es lineal: $\operatorname{tr}(A+B)=\operatorname{tr}(A)+\operatorname{tr}(B)$ y $\operatorname{tr}(\lambda A)=\lambda\operatorname{tr}(A)$.
- **Transposición.** $T:\mathbb{R}^{m\times n}\to\mathbb{R}^{n\times m}$, $T(A)=A^t$, es lineal: $(A+B)^t=A^t+B^t$ y $(\lambda A)^t=\lambda A^t$.
- Combinándolas: $A\mapsto A+A^t$ o $A\mapsto A-A^t$ son TL de $\mathbb{R}^{n\times n}$ en sí mismo (las retomamos en [2.3](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/) y [2.4](/algebra-ii/unidad-2/teoria/clasificacion/)).

### Ejemplo 5 · Codificar es aplicar una TL sobre ℤ₂
<!-- check: U2.T01.E5 -->

En la Unidad 1 vimos que un [código lineal](/algebra-ii/unidad-1/teoria/codigos-lineales/) $(n,k)$ se describe con una matriz generadora $G$ de $k\times n$, y que un mensaje $a\in\mathbb{Z}_2^k$ (fila) se codifica como $u=aG\in\mathbb{Z}_2^n$. Tomemos

$$
G=\begin{pmatrix}1&0&1&1&0\\0&1&0&1&1\end{pmatrix}\in\mathbb{Z}_2^{2\times 5}
$$

y $T:\mathbb{Z}_2^2\to\mathbb{Z}_2^5$, $T(a)=aG$. Las cuatro palabras código son:

| Mensaje $a$ | Palabra $aG$ |
|---|---|
| $(0,0)$ | $(0,0,0,0,0)$ |
| $(1,0)$ | $(1,0,1,1,0)$ |
| $(0,1)$ | $(0,1,0,1,1)$ |
| $(1,1)$ | $(1,1,1,0,1)$ |

$T$ es lineal porque $(a+b)G=aG+bG$ (distributiva del producto de matrices, que vale en $\mathbb{Z}_2$). En la tabla se ve: la palabra de $(1,1)=(1,0)+(0,1)$ es la suma, componente a componente y módulo 2, de las otras dos: $(1,0,1,1,0)+(0,1,0,1,1)=(1,1,1,0,1)$. Por la observación sobre $\mathbb{Z}_2$, no hace falta verificar la homogeneidad.

La linealidad es lo que permite **codificar con una tabla de $k$ filas** (las filas de $G$, que son las imágenes de los mensajes canónicos) en lugar de una tabla de $2^k$ entradas.

## No ejemplos

### Ejemplo 6 · Cuatro funciones que no son lineales
<!-- check: U2.T01.E6 -->

Para cada función, un contraejemplo concreto alcanza.

1. **Traslación.** $\tau:\mathbb{R}^2\to\mathbb{R}^2$, $\tau(x,y)=(x+1,\ y-2)$. Falla el test del nulo: $\tau(0,0)=(1,-2)\neq(0,0)$. En general, una traslación por un vector $b\neq 0$ nunca es lineal.
2. **Longitud.** $N:\mathbb{R}^2\to\mathbb{R}$, $N(x,y)=\sqrt{x^2+y^2}$. Cumple $N(0,0)=0$, pero con $v=(3,4)$: $N(-v)=\sqrt{9+16}=5$, mientras que $-N(v)=-5$. Falla $T(-v)=-T(v)$.
3. **Determinante.** $\det:\mathbb{R}^{2\times 2}\to\mathbb{R}$. Con $A=B=I$: $\det(I+I)=\det(2I)=4$, pero $\det I+\det I=2$. Falla la aditividad (y también la homogeneidad: $\det(\lambda A)=\lambda^2\det A$ en $2\times 2$).
4. **Cuadrado.** $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$. $f(1+1)=4$, pero $f(1)+f(1)=2$.

:::caution[Lineal en el sentido de este curso]
En Análisis se llama "función lineal" a $f(x)=mx+b$. Para nosotros es lineal solo si $b=0$: con $b\neq 0$ es una función **afín** (lineal más una traslación). Las únicas TL de $\mathbb{R}$ en $\mathbb{R}$ son $x\mapsto mx$, porque $f(x)=f(x\cdot 1)=x\,f(1)$.
:::

## Aplicación: transformaciones del plano en gráficos por computadora

En un programa de gráficos, una figura plana se guarda como una lista de puntos (los vértices de sus polígonos). Si los ponemos como columnas de una matriz $P$ de $2\times N$, aplicar una TL con matriz $A$ a toda la figura es un único producto $AP$. Como las TL llevan segmentos en segmentos, alcanza con transformar los vértices y volver a unirlos.

Las transformaciones básicas son lineales:

- **Escalado:** $\begin{pmatrix}s_x&0\\0&s_y\end{pmatrix}$ estira o comprime cada eje.
- **Rotación** de ángulo $\theta$: la matriz del ejemplo 3.
- **Cizalla horizontal:** $\begin{pmatrix}1&k\\0&1\end{pmatrix}$, que desplaza cada punto horizontalmente en proporción a su altura (así se obtiene, por ejemplo, el efecto de letra inclinada).

Aplicar una transformación y después otra corresponde a multiplicar las matrices (lo justificamos en [2.8](/algebra-ii/unidad-2/teoria/composicion-e-inversa/)); por eso los programas acumulan una sola matriz para toda la cadena de transformaciones.

### Ejemplo 7 · Cizalla de una grilla y traslación en coordenadas homogéneas
<!-- check: U2.T01.E7 -->

**a) Cizalla.** Sea $S(x,y)=(x+y,\ y)$, de matriz $\begin{pmatrix}1&1\\0&1\end{pmatrix}$. Cada punto de la grilla $\{0,1,2\}^2$ va a $S(i,j)=(i+j,\ j)$: los puntos de altura $j$ se corren $j$ unidades a la derecha. Las rectas horizontales quedan fijas como conjuntos (cada una se desliza sobre sí misma) y las verticales se inclinan.

<figure class="math-figure">
<svg viewBox="-30 -135 260 160" role="img" aria-labelledby="dye-ciz-t dye-ciz-d" xmlns="http://www.w3.org/2000/svg">
<title id="dye-ciz-t">Imagen de una grilla por una cizalla</title>
<desc id="dye-ciz-d">La grilla de puntos con coordenadas entre 0 y 2, en línea punteada, y su imagen por la cizalla S(x,y)=(x+y,y), en trazo continuo: los segmentos verticales se inclinan y los horizontales se desplazan. El vector e2=(0,1) va a S(e2)=(1,1).</desc>
<defs><marker id="dye-ciz-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker><marker id="dye-ciz-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="scale(1,-1)">
<line class="axis" x1="-20" y1="0" x2="220" y2="0"/>
<line class="axis" x1="0" y1="-15" x2="0" y2="125"/>
<line class="guide" x1="0" y1="0" x2="0" y2="100"/>
<line class="guide" x1="50" y1="0" x2="50" y2="100"/>
<line class="guide" x1="100" y1="0" x2="100" y2="100"/>
<line class="guide" x1="0" y1="50" x2="100" y2="50"/>
<line class="guide" x1="0" y1="100" x2="100" y2="100"/>
<line class="line-b" x1="0" y1="0" x2="100" y2="100"/>
<line class="line-b" x1="50" y1="0" x2="150" y2="100"/>
<line class="line-b" x1="100" y1="0" x2="200" y2="100"/>
<line class="line-b" x1="0" y1="0" x2="100" y2="0"/>
<line class="line-b" x1="50" y1="50" x2="150" y2="50"/>
<line class="line-b" x1="100" y1="100" x2="200" y2="100"/>
<line class="vec-a" x1="0" y1="0" x2="0" y2="50" marker-end="url(#dye-ciz-arrow-a)"/>
<line class="vec-c" x1="0" y1="0" x2="50" y2="50" marker-end="url(#dye-ciz-arrow-c)"/>
</g>
<text class="math" x="-24" y="-40">e₂</text>
<text class="math" x="54" y="-56">S(e₂)</text>
<text class="small" x="150" y="-108">imagen</text>
<text class="small" x="-24" y="-108">grilla</text>
</svg>
<figcaption>Grilla original (punteada) e imagen por la cizalla (trazo continuo). El segmento vertical que va de (0,0) a (0,2) se transforma en el que va de (0,0) a (2,2); cada recta horizontal se desliza sobre sí misma.</figcaption>
</figure>

**b) Traslación.** Por el ejemplo 6, trasladar no es lineal en $\mathbb{R}^2$. Los programas de gráficos lo resuelven con **coordenadas homogéneas**: el punto $(x,y)$ se representa como $(x,y,1)\in\mathbb{R}^3$ y la traslación por $(2,-1)$ se escribe como una TL de $\mathbb{R}^3$:

$$
\begin{pmatrix}1&0&2\\0&1&-1\\0&0&1\end{pmatrix}\begin{pmatrix}3\\1\\1\end{pmatrix}=\begin{pmatrix}5\\0\\1\end{pmatrix}.
$$

El punto $(3,1)$ va a $(5,0)$, como debe. La transformación de $\mathbb{R}^3$ es lineal; lo que no es lineal es su efecto sobre el plano $z=1$, que no es un subespacio. Con esta representación, "rotar $90^\circ$ y después trasladar por $(2,-1)$" es el producto

$$
\begin{pmatrix}1&0&2\\0&1&-1\\0&0&1\end{pmatrix}\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}=\begin{pmatrix}0&-1&2\\1&0&-1\\0&0&1\end{pmatrix},
$$

que lleva $(3,1,1)$ a $(1,2,1)$: primero $(3,1)\mapsto(-1,3)$ por la rotación, y después $(-1,3)\mapsto(1,2)$ por la traslación.

**Comprobación.** $\begin{pmatrix}0&-1&2\\1&0&-1\\0&0&1\end{pmatrix}\begin{pmatrix}3\\1\\1\end{pmatrix}=\begin{pmatrix}-1+2\\3-1\\1\end{pmatrix}=\begin{pmatrix}1\\2\\1\end{pmatrix}$.

:::caution[Errores frecuentes]
- **Concluir linealidad porque $T(0)=0$.** El test del nulo solo sirve para descartar. Contraejemplo: $F(x,y)=(x+y,xy)$ del ejemplo 2.
- **Verificar con números en vez de con vectores genéricos.** Comprobar $T(u+v)=T(u)+T(v)$ para un par particular no prueba nada; hay que hacerlo para $u,v$ arbitrarios. Para refutar, en cambio, sí alcanza un par particular.
- **Sumar en el espacio equivocado.** En $T:P_2[\mathbb{R}]\to\mathbb{R}^2$, la suma $p+q$ es de polinomios y $T(p)+T(q)$ es de pares. Mezclarlas lleva a escribir cosas como $T(p)+q$, que no tienen sentido.
- **Confundir afín con lineal.** $f(x)=3x+1$ no es lineal: $f(0)=1$.
- **Creer que "fórmula con productos" implica no lineal.** $T(x,y)=(2x,\ 3y)$ tiene productos por constantes y es lineal; lo que rompe la linealidad es multiplicar variables entre sí ($xy$, $x^2$) o sumar constantes.
:::

## Autoevaluación

<details>
<summary>1. ¿Es lineal $T:\mathbb{R}^{2\times 2}\to\mathbb{R}$, $T(A)=a_{11}a_{22}$?</summary>

No. Con $A=B=I$: $T(I+I)=2\cdot 2=4$ y $T(I)+T(I)=2$. Falla la aditividad aunque $T(0)=0$.

</details>

<details>
<summary>2. Sea $T:\mathbb{R}^2\to\mathbb{R}^3$ lineal con $T(1,0)=(1,1,0)$ y $T(0,1)=(0,2,-1)$. Calcular $T(3,-2)$.</summary>

Por la propiedad 4, $T(3,-2)=3T(1,0)-2T(0,1)=(3,3,0)-(0,4,-2)=(3,-1,2)$.

</details>

<details>
<summary>3. ¿Puede una TL $T:\mathbb{R}^2\to\mathbb{R}^2$ cumplir $T(1,1)=(2,0)$ y $T(2,2)=(3,1)$?</summary>

No: por homogeneidad, $T(2,2)=2T(1,1)=(4,0)\neq(3,1)$.

</details>

:::tip[En resumen]
- $T:V\to W$ es lineal si $T(u+v)=T(u)+T(v)$ y $T(\lambda v)=\lambda T(v)$; equivalentemente, si $T(\alpha u+\beta v)=\alpha T(u)+\beta T(v)$.
- Toda TL cumple $T(0_V)=0_W$, $T(-v)=-T(v)$ y preserva combinaciones lineales.
- $T(0_V)\neq 0_W$ prueba que $T$ no es lineal; $T(0_V)=0_W$ no prueba nada.
- Sobre $\mathbb{Z}_2$, lineal equivale a aditiva.
- Son lineales: $x\mapsto Ax$, proyecciones, simetrías y rotaciones que fijan el origen, derivación, evaluación, traza, transposición y la codificación $a\mapsto aG$. No lo son: traslaciones no nulas, longitud, determinante, $x\mapsto x^2$.
- La traslación se vuelve lineal en coordenadas homogéneas, a costa de trabajar en una dimensión más.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 3.6, "Introducción a las transformaciones lineales" (p. 217), para el caso matricial y las transformaciones geométricas; sección 6.4, "Transformaciones lineales" (p. 490), para espacios vectoriales generales.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: las secciones de introducción a las transformaciones lineales y a su matriz, con ejemplos de gráficos por computadora y coordenadas homogéneas.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed.: sección 5.1, "Definición de aplicación lineal" (p. 178).
- Antes: [espacios vectoriales](/algebra-ii/unidad-1/teoria/espacios-vectoriales/), [cuerpos y ℤ₂](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/), [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/) y el repaso de [vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/).
- Después: [2.2 Núcleo e imagen](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/).
