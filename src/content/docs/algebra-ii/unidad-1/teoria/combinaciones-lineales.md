---
title: Combinaciones lineales
description: Combinación lineal y subespacio generado como el menor subespacio que contiene a un conjunto, pertenencia por sistemas, paso entre generadores y ecuaciones implícitas, e igualdad de generados.
slug: algebra-ii/unidad-1/teoria/combinaciones-lineales
sidebar:
  order: 4
  label: 1.4 Combinaciones lineales
---

## Para qué sirve

Un subespacio puede describirse de dos maneras. Por **ecuaciones**: "los $(x,y,z)$ con
$2x-y+3z=0$". Por **generadores**: "todo lo que se obtiene combinando estos vectores". La primera sirve
para *verificar* si un vector pertenece; la segunda, para *producir* elementos. Casi todos los problemas
de la unidad consisten en pasar de una descripción a la otra, y para eso hace falta la noción de
combinación lineal.

En informática la idea es literal. Un bloque de paridad es una combinación lineal de los bloques de
datos (con coeficientes $1$ en $\mathbb{Z}_2$); un color RGB es una combinación de tres colores
primarios; la salida de un filtro de señales es una combinación de las muestras de entrada. Y un código
corrector de errores es el conjunto de **todas** las combinaciones de unas pocas palabras base
(ver [códigos lineales](/algebra-ii/unidad-1/teoria/codigos-lineales/)).

Partimos de [espacios vectoriales](/algebra-ii/unidad-1/teoria/espacios-vectoriales/) y de
[subespacios](/algebra-ii/unidad-1/teoria/subespacios/).

## Combinación lineal

:::note[Definición]
Sea $V$ un espacio vectorial sobre $K$ y sean $v_1,\dots,v_k\in V$. Una **combinación lineal** de
$v_1,\dots,v_k$ es un vector de la forma

$$
\alpha_1v_1+\alpha_2v_2+\dots+\alpha_kv_k,\qquad \alpha_1,\dots,\alpha_k\in K .
$$

Los $\alpha_i$ son los **coeficientes** (o escalares) de la combinación.
:::

Por ejemplo, en $\mathbb{R}^2$ con $u=(2,1)$ y $v=(-1,1)$, el vector $w=2u+v=(3,3)$ es una combinación
lineal de $u$ y $v$ con coeficientes $2$ y $1$. En $\mathbb{Z}_2^3$, $(1,0,1)+(0,1,1)=(1,1,0)$ es una
combinación lineal de $(1,0,1)$ y $(0,1,1)$ con coeficientes $1$ y $1$; como los únicos escalares son
$0$ y $1$, combinar en $\mathbb{Z}_2$ es **elegir qué vectores sumar**.

Siempre hay una combinación lineal trivial: con todos los coeficientes nulos se obtiene $0_V$. Y todo
$v_i$ es combinación lineal de $v_1,\dots,v_k$ (coeficiente $1$ en $v_i$ y $0$ en los demás).

<figure class="math-figure">
<svg viewBox="-70 -110 230 180" role="img" aria-labelledby="cl-t cl-d" xmlns="http://www.w3.org/2000/svg">
<title id="cl-t">Combinación lineal y generado en el plano</title>
<desc id="cl-d">Grilla con unidad de 25 píxeles. Los vectores u = (2, 1) y v = (−1, 1) salen del origen. El vector 2u = (4, 2) se dibuja en trazos y, al sumarle v, se llega a w = 2u + v = (3, 3). Los trazos completan el paralelogramo. La recta que pasa por el origen con dirección u es el generado de u.</desc>
<defs><marker id="cl-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker><marker id="cl-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker><marker id="cl-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="scale(1,-1)">
<path class="grid" d="M-50 -60V105 M-25 -60V105 M25 -60V105 M50 -60V105 M75 -60V105 M100 -60V105 M125 -60V105 M-60 -50H150 M-60 -25H150 M-60 25H150 M-60 50H150 M-60 75H150 M-60 100H150"/>
<line class="axis" x1="-60" y1="0" x2="150" y2="0"/>
<line class="axis" x1="0" y1="-60" x2="0" y2="105"/>
<line class="line-a" x1="-60" y1="-30" x2="150" y2="75"/>
<line class="guide" x1="50" y1="25" x2="100" y2="50"/>
<line class="guide" x1="100" y1="50" x2="75" y2="75"/>
<line class="guide" x1="-25" y1="25" x2="75" y2="75"/>
<line class="vec-a" x1="0" y1="0" x2="50" y2="25" marker-end="url(#cl-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="-25" y2="25" marker-end="url(#cl-arrow-b)"/>
<line class="vec-c" x1="0" y1="0" x2="75" y2="75" marker-end="url(#cl-arrow-c)"/>
<circle class="dot-a" cx="100" cy="50" r="3"/>
</g>
<text class="math" x="54" y="-28">u</text>
<text class="math" x="-40" y="-32">v</text>
<text class="math" x="80" y="-82">w = 2u + v</text>
<text class="math" x="104" y="-54">2u</text>
<text x="-66" y="52">gen{u}</text>
<text x="-14" y="14">0</text>
<text class="math" x="152" y="14">x</text>
<text class="math" x="6" y="-104">y</text>
</svg>
<figcaption>El vector w = 2u + v se llega recorriendo dos veces u y luego v (trazos: el paralelogramo). La recta del color de u, por el origen, es gen{u}: todas las combinaciones de u solo.</figcaption>
</figure>

## El subespacio generado

:::note[Definición]
El **subespacio generado** (o **generado**) por $v_1,\dots,v_k\in V$ es el conjunto de todas sus
combinaciones lineales:

$$
\operatorname{gen}\{v_1,\dots,v_k\}=\{\alpha_1v_1+\dots+\alpha_kv_k:\ \alpha_1,\dots,\alpha_k\in K\}.
$$

Si $S=\operatorname{gen}\{v_1,\dots,v_k\}$ decimos que $\{v_1,\dots,v_k\}$ **genera** $S$ o es un
**generador** de $S$. Por convención, $\operatorname{gen}\varnothing=\{0_V\}$.
:::

El nombre está justificado por el siguiente teorema, que dice dos cosas: que el generado es un
subespacio y que es el **menor** que contiene a los vectores dados.

:::note[Teorema]
Sean $v_1,\dots,v_k\in V$ y $G=\operatorname{gen}\{v_1,\dots,v_k\}$.

1. $G$ es un subespacio de $V$ y contiene a $v_1,\dots,v_k$.
2. Si $W$ es un subespacio de $V$ que contiene a $v_1,\dots,v_k$, entonces $G\subseteq W$.
:::

**Demostración.**

1. *Contiene al nulo:* $0_V=0v_1+\dots+0v_k\in G$. *Cierre de la suma:* si
   $u=\sum\alpha_iv_i$ y $w=\sum\beta_iv_i$, entonces $u+w=\sum(\alpha_i+\beta_i)v_i\in G$, por las
   propiedades conmutativa, asociativa y distributiva. *Cierre del producto:* $\lambda u=\sum(\lambda\alpha_i)v_i\in G$.
   Además, cada $v_i=0v_1+\dots+1v_i+\dots+0v_k$ está en $G$.
2. Un subespacio es cerrado para el producto por escalares y para la suma, así que cada $\alpha_iv_i$
   está en $W$ y, sumando de a uno (inducción sobre $k$), $\alpha_1v_1+\dots+\alpha_kv_k\in W$. Luego
   todo elemento de $G$ está en $W$. $\blacksquare$

Consecuencias inmediatas:

- **Si $S$ es un subespacio**, $\operatorname{gen}S=S$ (porque $S$ es el menor subespacio que contiene a $S$).
- **Agregar una combinación no cambia el generado.** Si $w\in\operatorname{gen}\{v_1,\dots,v_k\}$,
  entonces $\operatorname{gen}\{v_1,\dots,v_k,w\}=\operatorname{gen}\{v_1,\dots,v_k\}$. En efecto, el
  segundo contiene al primero; y el primero es un subespacio que contiene a $v_1,\dots,v_k$ y a $w$, así
  que por el punto 2 contiene al segundo. Este hecho es la raíz de la noción de independencia
  lineal ([siguiente lección](/algebra-ii/unidad-1/teoria/independencia-lineal/)): un vector que es
  combinación de los otros "sobra".
- **Vale en todo espacio vectorial.** $\operatorname{gen}\{1,x\}$ en $P_2[\mathbb{R}]$ son los polinomios
  de grado a lo sumo $1$; $\operatorname{gen}\{E_{11},E_{22}\}$ en $\mathbb{R}^{2\times2}$ son las
  matrices diagonales.

### Suma de subespacios

En [subespacios](/algebra-ii/unidad-1/teoria/subespacios/) vimos que la unión de dos subespacios casi
nunca es un subespacio. El menor subespacio que contiene a $S\cup T$ es el generado por la unión, y
tiene una descripción explícita:

:::note[Propiedad]
Si $S$ y $T$ son subespacios de $V$, entonces
$\operatorname{gen}(S\cup T)=S+T=\{s+t:\ s\in S,\ t\in T\}$.
:::

**Demostración.** Todo $s+t$ es combinación lineal de elementos de $S\cup T$ (con coeficientes $1$).
Recíprocamente, una combinación lineal de elementos de $S\cup T$ se separa agrupando los términos que
vienen de $S$ y los que vienen de $T$: queda $s+t$, donde $s\in S$ y $t\in T$ porque ambos son
subespacios. $\blacksquare$

Por ejemplo, en $\mathbb{R}^3$, $\operatorname{gen}\{e_1\}+\operatorname{gen}\{e_2\}=\operatorname{gen}\{e_1,e_2\}$
es el plano $z=0$.

## Decidir si un vector pertenece al generado

Sea $A=(v_1\mid\cdots\mid v_k)\in K^{n\times k}$ la matriz cuyas **columnas** son los generadores.
Como $A\alpha=\alpha_1v_1+\dots+\alpha_kv_k$ (ver
[subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/)),

$$
b\in\operatorname{gen}\{v_1,\dots,v_k\}\iff Ax=b\ \text{es compatible}\iff \operatorname{rango}(A\mid b)=\operatorname{rango}(A).
$$

Es decir, $\operatorname{gen}\{v_1,\dots,v_k\}=\operatorname{col}(A)$. Para decidir, escalonamos la matriz
ampliada $(A\mid b)$: si aparece una fila $(0\ \cdots\ 0\mid c)$ con $c\neq0$, el vector **no** pertenece;
si no, pertenece y la solución da los coeficientes. Con varios vectores $b$ a la vez, se escalonan todos
juntos con varias columnas ampliadas. Cuando $A$ tiene columnas dependientes, hay infinitos
conjuntos de coeficientes válidos: el vector es combinación lineal "de muchas maneras".

En $P_n[\mathbb{R}]$ o $\mathbb{R}^{m\times n}$ se hace lo mismo pasando a coordenadas en la base
canónica ([coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/)); la respuesta se escribe con
polinomios o matrices, no con ternas.

### Ejemplo 1 · Pertenencia a un plano de ℝ³
<!-- check: U1.T04.E1 -->

Sean $v_1=(1,2,-1)$, $v_2=(2,1,3)$, $v_3=(0,3,-5)$ y $S=\operatorname{gen}\{v_1,v_2,v_3\}$. Decidir si
$w=(4,5,1)$ y $z=(1,1,1)$ pertenecen a $S$, y describir $S$.

Escribimos las columnas $v_1,v_2,v_3$ con $w$ y $z$ como columnas ampliadas y escalonamos:

$$
\left(\begin{array}{ccc|c|c} 1&2&0&4&1\\2&1&3&5&1\\-1&3&-5&1&1 \end{array}\right)
\xrightarrow[F_3+F_1\to F_3]{F_2-2F_1\to F_2}
\left(\begin{array}{ccc|c|c} 1&2&0&4&1\\0&-3&3&-3&-1\\0&5&-5&5&2 \end{array}\right).
$$

Multiplicamos $F_2$ por $-\tfrac13$ y restamos $5F_2$ de $F_3$:

$$
\left(\begin{array}{ccc|c|c} 1&2&0&4&1\\0&1&-1&1&\tfrac13\\0&0&0&0&\tfrac13 \end{array}\right).
$$

**Lectura.** Las columnas de $v_1,v_2,v_3$ tienen rango $2$. La columna de $w$ no produce pivote: el
sistema es compatible. La columna de $z$ produce la fila $(0\ 0\ 0\mid\tfrac13)$: es incompatible.
Entonces $w\in S$ y $z\notin S$.

Para $w$, la variable libre es el coeficiente de $v_3$, $x_3=t$: $x_2=1+t$ y $x_1=4-2x_2=2-2t$. Con
$t=0$ queda $w=2v_1+v_2$. Con otros $t$ se obtienen otras combinaciones, porque $v_3=2v_1-v_2$ es combinación
de los otros dos (y entonces $S=\operatorname{gen}\{v_1,v_2\}$).

**Descripción de $S$.** Como $v_1$ y $v_2$ no son proporcionales, $S$ es un plano por el origen, con
normal $v_1\times v_2=(7,-5,-3)$:

$$
S=\{(x,y,z)\in\mathbb{R}^3:\ 7x-5y-3z=0\}.
$$

**Comprobación.** $7\cdot4-5\cdot5-3\cdot1=0$ para $w$; para $z$, $7-5-3=-1\neq0$. Los tres
generadores cumplen la ecuación: $7-10+3=0$, $14-5-9=0$ y $0-15+15=0$.

:::tip[Resultado]
$w=2v_1+v_2\in S$; $z\notin S$; $S=\{7x-5y-3z=0\}=\operatorname{gen}\{v_1,v_2\}$.
:::

## Interpretación geométrica

En $\mathbb{R}^2$ y $\mathbb{R}^3$, el generado de pocos vectores es:

| Generadores | Generado |
|---|---|
| un vector $v\neq0$ | la recta por el origen con dirección $v$ |
| dos vectores no proporcionales | el plano por el origen que los contiene (en $\mathbb{R}^2$, todo el plano) |
| tres vectores de $\mathbb{R}^3$ no contenidos en un mismo plano por el origen | $\mathbb{R}^3$ |
| vectores todos proporcionales a uno | la misma recta |

La cantidad de generadores no determina la dimensión: $\operatorname{gen}\{(1,2),(2,4),(3,6)\}$ tiene tres
generadores y es una **recta**. La dimensión es la cantidad de generadores "que no sobran", que es el
tema de [independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/) y de
[base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/).

## Dos descripciones del mismo subespacio

### De generadores a ecuaciones implícitas

Sea $S=\operatorname{gen}\{g_1,\dots,g_k\}\subseteq K^n$. Una **ecuación implícita** es una condición
$c_1x_1+\dots+c_nx_n=0$ que cumplen todos los elementos de $S$. Hay dos métodos.

**Método 1: escalonar con segundo miembro genérico.** Se arma $(g_1\mid\cdots\mid g_k\mid x)$ con
$x=(x_1,\dots,x_n)$ y se escalona. El vector $x$ pertenece a $S$ si y solo si las filas que quedan sin
pivote en la parte de los $g_i$ tienen segundo miembro nulo. Cada una de esas condiciones es una
ecuación implícita, y hay $n-\operatorname{rango}$ de ellas.

**Método 2: vectores de coeficientes.** El vector $c=(c_1,\dots,c_n)$ define una ecuación válida para
$S$ si y solo si $c\cdot g_i=0$ para cada $i$, es decir, si $c$ está en $\operatorname{nul}(G)$, donde
$G$ es la matriz que tiene a los $g_i$ como **filas**. Una base de $\operatorname{nul}(G)$ da
$n-r$ ecuaciones independientes, con $r=\operatorname{rango}(G)=\dim S$.

*Por qué alcanzan.* Sea $N$ el conjunto solución del sistema formado por esas $n-r$ ecuaciones
independientes. Por rango–nulidad, $\dim N=n-(n-r)=r$. Como $S\subseteq N$ y ambos tienen dimensión
$r$, $S=N$ (si un subespacio está contenido en otro de igual dimensión, son iguales; ver
[base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/)).

### De ecuaciones implícitas a generadores

Si $S=\{x\in K^n: Ax=0\}=\operatorname{nul}(A)$, se resuelve el sistema homogéneo y se escribe la
solución general como combinación de las variables libres; los vectores que acompañan a cada variable
libre generan $S$ (ver [subespacios de una matriz](/algebra-ii/unidad-1/teoria/subespacios-de-una-matriz/)).

### Ejemplo 2 · Ida y vuelta en ℝ⁴
<!-- check: U1.T04.E2 -->

Sea $S=\operatorname{gen}\{g_1,g_2,g_3,g_4\}\subseteq\mathbb{R}^4$ con $g_1=(1,1,0,2)$, $g_2=(0,1,1,-1)$,
$g_3=(1,2,1,1)$ y $g_4=(2,1,-1,5)$. Hallar ecuaciones implícitas de $S$ y volver a generadores.

**Reducción previa.** $g_3=g_1+g_2$ y $g_4=2g_1-g_2$, así que $S=\operatorname{gen}\{g_1,g_2\}$ y
$\dim S=2$: esperamos $4-2=2$ ecuaciones.

**Método 1.** Escalonamos $(g_1\mid g_2\mid x)$:

$$
\left(\begin{array}{cc|c} 1&0&x_1\\1&1&x_2\\0&1&x_3\\2&-1&x_4 \end{array}\right)
\xrightarrow[F_4-2F_1\to F_4]{F_2-F_1\to F_2}
\left(\begin{array}{cc|c} 1&0&x_1\\0&1&x_2-x_1\\0&1&x_3\\0&-1&x_4-2x_1 \end{array}\right)
\xrightarrow[F_4+F_2\to F_4]{F_3-F_2\to F_3}
\left(\begin{array}{cc|c} 1&0&x_1\\0&1&x_2-x_1\\0&0&x_1-x_2+x_3\\0&0&-3x_1+x_2+x_4 \end{array}\right).
$$

Las dos últimas filas exigen
$$
x_1-x_2+x_3=0,\qquad -3x_1+x_2+x_4=0 .
$$

**Método 2.** Los vectores $c$ con $c\cdot g_1=c\cdot g_2=0$ son las soluciones de
$c_1+c_2+2c_4=0$, $c_2+c_3-c_4=0$. Con $c_3,c_4$ libres, $c_2=-c_3+c_4$ y $c_1=c_3-3c_4$:

$$
c=c_3(1,-1,1,0)+c_4(-3,1,0,1),
$$

que reproduce exactamente las mismas dos ecuaciones. Otra base de $\operatorname{nul}(G)$ daría otro
sistema equivalente para el mismo $S$: por ejemplo, $2x_1-x_3-x_4=0$ es el opuesto de la suma de las dos
ecuaciones, y podría reemplazar a cualquiera de ellas.

**Vuelta a generadores.** Del sistema, con $x_1$ y $x_3$ libres: $x_2=x_1+x_3$ y $x_4=3x_1-x_2=2x_1-x_3$.
Entonces
$$
x=(x_1,\ x_1+x_3,\ x_3,\ 2x_1-x_3)=x_1(1,1,0,2)+x_3(0,1,1,-1)=x_1g_1+x_3g_2 .
$$

**Comprobación.** $g_1$ cumple $1-1+0=0$ y $-3+1+2=0$; $g_2$ cumple $0-1+1=0$ y $0+1-1=0$; $g_3$ y
$g_4$ también (por ser combinaciones). El vector $(1,0,0,0)$ no cumple la primera ecuación
($1\neq0$), así que no pertenece a $S$.

:::tip[Resultado]
$S=\{x\in\mathbb{R}^4:\ x_1-x_2+x_3=0,\ -3x_1+x_2+x_4=0\}=\operatorname{gen}\{g_1,g_2\}$, de dimensión $2$.
:::

## Igualdad de generados

Para probar que $\operatorname{gen}A=\operatorname{gen}B$ se prueba la doble inclusión, y alcanza con
mirar los **generadores**: $\operatorname{gen}A\subseteq\operatorname{gen}B$ si y solo si cada vector de
$A$ es combinación lineal de los de $B$ (por el punto 2 del teorema). En términos de matrices con los
generadores en columnas,

$$
\operatorname{gen}A=\operatorname{gen}B\iff \operatorname{rango}(A)=\operatorname{rango}(B)=\operatorname{rango}(A\mid B).
$$

### Ejemplo 3 · Dos generadores del mismo subespacio de polinomios
<!-- check: U1.T04.E3 -->

En $P_2[\mathbb{R}]$ sean $p_1=1+x$, $p_2=x+x^2$, $q_1=1+2x+x^2$ y $q_2=1-x^2$. Probar que
$\operatorname{gen}\{p_1,p_2\}=\operatorname{gen}\{q_1,q_2\}$ y decidir si $r=1+x^2$ pertenece.

**Los $q$ en términos de los $p$.** $q_1=p_1+p_2$ y $q_2=p_1-p_2$, porque
$(1+x)-(x+x^2)=1-x^2$. Entonces $\operatorname{gen}\{q_1,q_2\}\subseteq\operatorname{gen}\{p_1,p_2\}$.

**Los $p$ en términos de los $q$.** Sumando y restando, $p_1=\tfrac12(q_1+q_2)$ y
$p_2=\tfrac12(q_1-q_2)$. Entonces $\operatorname{gen}\{p_1,p_2\}\subseteq\operatorname{gen}\{q_1,q_2\}$ y
vale la igualdad.

**Pertenencia de $r$.** Un elemento del generado es $a(1+x)+b(x+x^2)=a+(a+b)x+bx^2$. Para que sea
$1+x^2$ hace falta $a=1$, $b=1$ y $a+b=0$, que es contradictorio. Por coordenadas: los vectores
$(1,1,0)$, $(0,1,1)$ y $(1,0,1)$ tienen rango $3$ (el sistema es incompatible), así que
$r\notin\operatorname{gen}\{p_1,p_2\}$. En coordenadas $(c_0,c_1,c_2)$, el generado es el plano
$c_0-c_1+c_2=0$, y $r$ da $1-0+1=2\neq0$.

**Comprobación.** $p_1+p_2=1+2x+x^2=q_1$ y $\tfrac12(q_1+q_2)=\tfrac12(2+2x)=p_1$.

:::tip[Resultado]
Los dos generados coinciden (un plano de $P_2[\mathbb{R}]$ de ecuación $c_0-c_1+c_2=0$) y
$1+x^2$ no pertenece.
:::

## Un ejemplo en ℤ₂ⁿ: enumerar el generado

Sobre $\mathbb{Z}_2$ el generado de $k$ vectores tiene **a lo sumo** $2^k$ elementos: cada coeficiente es
$0$ o $1$, así que hay $2^k$ combinaciones. Puede tener menos si algunas coinciden.

### Ejemplo 4 · Ocho combinaciones, cuatro vectores
<!-- check: U1.T04.E4 -->

En $\mathbb{Z}_2^4$ sean $g_1=(1,1,0,1)$, $g_2=(0,1,1,1)$ y $g_3=(1,0,1,0)$. Enumerar
$\operatorname{gen}\{g_1,g_2,g_3\}$, decidir si $(1,1,1,1)$ pertenece y hallar ecuaciones implícitas.

**Enumeración.** Calculamos las $2^3=8$ combinaciones $a_1g_1+a_2g_2+a_3g_3$:

| $(a_1,a_2,a_3)$ | combinación |
|---|---|
| $(0,0,0)$ | $(0,0,0,0)$ |
| $(1,0,0)$ | $(1,1,0,1)$ |
| $(0,1,0)$ | $(0,1,1,1)$ |
| $(0,0,1)$ | $(1,0,1,0)$ |
| $(1,1,0)$ | $(1,0,1,0)$ |
| $(1,0,1)$ | $(0,1,1,1)$ |
| $(0,1,1)$ | $(1,1,0,1)$ |
| $(1,1,1)$ | $(0,0,0,0)$ |

Hay solo **cuatro** vectores distintos: $\operatorname{gen}\{g_1,g_2,g_3\}=\{(0,0,0,0),(1,1,0,1),(0,1,1,1),(1,0,1,0)\}$.
La causa es que $g_1+g_2=(1,0,1,0)=g_3$, es decir, $g_3$ es combinación de los otros. Entonces
$\operatorname{gen}\{g_1,g_2,g_3\}=\operatorname{gen}\{g_1,g_2\}$, de dimensión $2$ y con $2^2=4$ elementos.

**Pertenencia.** $(1,1,1,1)$ no está en la lista. Por sistemas: $a_1g_1+a_2g_2=(a_1,\ a_1+a_2,\ a_2,\ a_1+a_2)$
igualada a $(1,1,1,1)$ da $a_1=1$, $a_2=1$ y $a_1+a_2=1$, pero $1+1=0$.

**Ecuaciones.** Un elemento $x$ del generado cumple $x=(a_1,a_1+a_2,a_2,a_1+a_2)$, es decir
$x_2=x_1+x_3$ y $x_4=x_2$. En $\mathbb{Z}_2$, restar es sumar:

$$
x_1+x_2+x_3=0,\qquad x_2+x_4=0 .
$$

**Comprobación.** $g_1$: $1+1+0=0$ y $1+1=0$; $g_2$: $0+1+1=0$ y $1+1=0$. Un sistema de dos ecuaciones
independientes en $\mathbb{Z}_2^4$ tiene $2^{4-2}=4$ soluciones, que son los cuatro vectores de la
tabla.

:::tip[Resultado]
$\operatorname{gen}\{g_1,g_2,g_3\}$ tiene $4$ elementos, no contiene a $(1,1,1,1)$ y es el conjunto
solución de $x_1+x_2+x_3=0$, $x_2+x_4=0$.
:::

:::caution[Errores frecuentes]
- **Confundir el conjunto con su generado.** $\{v\}$ tiene un elemento; $\operatorname{gen}\{v\}$ tiene
  infinitos en $\mathbb{R}^n$ (si $v\neq0$) y $2$ en $\mathbb{Z}_2^n$.
- **Creer que $k$ generadores dan siempre un subespacio de dimensión $k$.** En el ejemplo 4, tres
  generadores dan dimensión $2$; en $\operatorname{gen}\{(1,2),(2,4)\}$ dos generadores dan una recta.
- **Pensar que los coeficientes son únicos.** Solo lo son si los generadores son independientes. En
  el ejemplo 1, $w=2v_1+v_2+0v_3$ y también $w=0v_1+2v_2+1v_3$ (es el caso $t=1$ de la familia de soluciones).
- **Decidir pertenencia "a ojo".** Hay que resolver el sistema; que no se encuentre una combinación
  probando no prueba que no exista.
- **Dar generadores donde se pedían ecuaciones (o al revés).** Un plano de $\mathbb{R}^3$ tiene $1$
  ecuación y $2$ generadores independientes; una recta tiene $2$ ecuaciones y $1$ generador.
- **Coeficientes fraccionarios en $\mathbb{Z}_2$.** Los coeficientes están en el cuerpo de escalares:
  en $\mathbb{Z}_2$ solo existen $0$ y $1$. En el ejemplo 3, el factor $\tfrac12$ es válido porque
  $K=\mathbb{R}$; sobre $\mathbb{Z}_2$ no existe.
- **Responder con ternas en un espacio de polinomios.** El resultado del ejemplo 3 es "$r$ no es combinación
  de $p_1$ y $p_2$", con polinomios; las coordenadas son auxiliares.
:::

## Autoevaluación

**1.** ¿Pertenece $(3,1,2)$ a $\operatorname{gen}\{(1,0,1),(0,1,-1)\}$?

<details>
<summary>Respuesta</summary>

Sí: $3(1,0,1)+1\,(0,1,-1)=(3,1,2)$. Equivalentemente, ese generado es el plano $x-y-z=0$ y
$3-1-2=0$.

</details>

**2.** ¿Qué subespacio genera $\{(1,2),(2,4),(3,6)\}$?

<details>
<summary>Respuesta</summary>

La recta $y=2x$, porque los tres vectores son múltiplos de $(1,2)$.

</details>

**3.** ¿Cuántos elementos tiene $\operatorname{gen}\{(1,0,1),(0,1,1)\}\subseteq\mathbb{Z}_2^3$?

<details>
<summary>Respuesta</summary>

Cuatro: $(0,0,0)$, $(1,0,1)$, $(0,1,1)$ y $(1,1,0)$. Los dos generadores son independientes, así que
la dimensión es $2$ y hay $2^2$ elementos.

</details>

:::tip[En resumen]
- Una combinación lineal es $\alpha_1v_1+\dots+\alpha_kv_k$; $\operatorname{gen}\{v_1,\dots,v_k\}$ es el
  conjunto de todas ellas.
- $\operatorname{gen}\{v_1,\dots,v_k\}$ es un subespacio y es el **menor** que contiene a los $v_i$.
  Para un subespacio $S$, $\operatorname{gen}S=S$. $\operatorname{gen}(S\cup T)=S+T$.
- $b\in\operatorname{gen}\{v_1,\dots,v_k\}$ si y solo si $Ax=b$ es compatible, con $A$ de columnas $v_i$.
- Generadores a ecuaciones: escalonar con segundo miembro genérico, o hallar $\operatorname{nul}$ de la
  matriz de generadores en filas ($n-r$ ecuaciones). Ecuaciones a generadores: variables libres.
- $\operatorname{gen}A=\operatorname{gen}B$ si y solo si cada vector de $A$ es combinación de los de $B$ y
  viceversa, es decir, $\operatorname{rango}(A)=\operatorname{rango}(B)=\operatorname{rango}(A\mid B)$.
- Sobre $\mathbb{Z}_2$, $k$ generadores dan a lo sumo $2^k$ vectores.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 2.3, "Conjuntos generadores e
  independencia lineal" (p. 94), y sección 6.1, "Espacios y subespacios vectoriales" (p. 447).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: combinaciones lineales y subespacio generado
  (capítulos de ecuaciones lineales y de espacios vectoriales).
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed., sección 4.4 (subespacios,
  intersección y suma, p. 162), como lectura complementaria.

Lección anterior: [subespacios](/algebra-ii/unidad-1/teoria/subespacios/). Lección siguiente:
[independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/). Repaso relacionado:
[sistemas lineales](/algebra-ii/repaso/sistemas-lineales/) y
[rectas y planos](/algebra-ii/repaso/rectas-y-planos/).
