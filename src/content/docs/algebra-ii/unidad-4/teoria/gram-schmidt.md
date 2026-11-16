---
title: Método de Gram-Schmidt
description: Construcción de una base ortogonal u ortonormal a partir de cualquier base, con demostración, casos con producto no usual y completado de bases ortogonales.
slug: algebra-ii/unidad-4/teoria/gram-schmidt
sidebar:
  order: 4
  label: 4.4 Gram-Schmidt
---

La lección anterior mostró que las bases ortogonales simplifican todo, pero no dijo cómo conseguir una. El **método de Gram-Schmidt** responde esa pregunta: parte de cualquier conjunto linealmente independiente y fabrica, uno por uno, vectores ortogonales que generan los mismos subespacios. Como el método usa solamente productos internos, funciona igual en $\mathbb{R}^n$ con el producto usual, con un producto no usual, en matrices y en polinomios.

En toda la lección, $(V,\langle\,,\rangle)$ es un espacio euclídeo.

## Idea del método

Dados $v_1,v_2$ linealmente independientes, conservamos $w_1=v_1$. El vector $v_2$ no es ortogonal a $w_1$ en general; para corregirlo le restamos su componente en la dirección de $w_1$, que es $\dfrac{\langle v_2,w_1\rangle}{\langle w_1,w_1\rangle}w_1$:

$$
w_2=v_2-\frac{\langle v_2,w_1\rangle}{\langle w_1,w_1\rangle}\,w_1 .
$$

Entonces $\langle w_2,w_1\rangle=\langle v_2,w_1\rangle-\langle v_2,w_1\rangle=0$. Con tres vectores, a $v_3$ se le restan sus componentes sobre $w_1$ y sobre $w_2$, y así sucesivamente: cada paso quita de $v_j$ lo que ya está "explicado" por los vectores anteriores.

<figure class="math-figure">
<svg viewBox="-45 -105 160 125" role="img" aria-labelledby="gs-t gs-d" xmlns="http://www.w3.org/2000/svg">
<title id="gs-t">Primeros dos pasos de Gram-Schmidt en el plano</title>
<desc id="gs-d">Los vectores v1=(3,1) y v2=(1,3). Se toma w1=v1; a v2 se le resta su proyección (9/5,3/5) sobre w1 y queda w2=(-4/5,12/5), perpendicular a w1.</desc>
<defs>
<marker id="gs-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker>
<marker id="gs-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker>
<marker id="gs-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker>
</defs>
<g transform="scale(1,-1)">
<line class="axis" x1="-40" y1="0" x2="105" y2="0"/>
<line class="axis" x1="0" y1="-8" x2="0" y2="100"/>
<line class="guide" x1="54" y1="18" x2="30" y2="90"/>
<polyline class="guide" points="46.8,15.6 44.4,22.8 51.6,25.2"/>
<line class="vec-a" x1="0" y1="0" x2="90" y2="30" marker-end="url(#gs-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="30" y2="90" marker-end="url(#gs-arrow-b)"/>
<line class="vec-c" x1="0" y1="0" x2="-24" y2="72" marker-end="url(#gs-arrow-c)"/>
<circle class="dot-muted" cx="54" cy="18" r="2.5"/>
</g>
<text class="math" x="94" y="-26">w₁ = v₁</text>
<text class="math" x="34" y="-92">v₂</text>
<text class="math" x="-42" y="-76">w₂</text>
<text class="small" x="52" y="-4">proy</text>
</svg>
<figcaption>Con v<sub>1</sub> = (3, 1) y v<sub>2</sub> = (1, 3): se toma w<sub>1</sub> = v<sub>1</sub>, se proyecta v<sub>2</sub> sobre w<sub>1</sub> (el punto marcado, (9/5, 3/5)) y se resta. Lo que queda, w<sub>2</sub> = v<sub>2</sub> − proy = (−4/5, 12/5), es perpendicular a w<sub>1</sub>; la segunda flecha punteada es w<sub>2</sub> trasladada a la punta de la proyección.</figcaption>
</figure>

## El método y su demostración

:::note[Teorema (Gram-Schmidt)]
Sea $\{v_1,\dots,v_k\}$ un conjunto linealmente independiente de $V$. Los vectores definidos por

$$
w_1=v_1,\qquad w_j=v_j-\sum_{i=1}^{j-1}\frac{\langle v_j,w_i\rangle}{\langle w_i,w_i\rangle}\,w_i\quad(j=2,\dots,k)
$$

cumplen, para cada $j=1,\dots,k$:

1. $w_j\neq0_V$ (la fórmula tiene sentido);
2. $\{w_1,\dots,w_j\}$ es ortogonal;
3. $\operatorname{gen}\{w_1,\dots,w_j\}=\operatorname{gen}\{v_1,\dots,v_j\}$.

En particular, $\{w_1,\dots,w_k\}$ es una base ortogonal de $\operatorname{gen}\{v_1,\dots,v_k\}$.
:::

**Demostración.** Por inducción en $j$. Para $j=1$: $w_1=v_1\neq0_V$ (por ser $\{v_1\}$ LI), un conjunto de un vector es ortogonal y $\operatorname{gen}\{w_1\}=\operatorname{gen}\{v_1\}$.

Supongamos que las tres afirmaciones valen para $j-1$, con $j\ge2$. Entonces los $w_1,\dots,w_{j-1}$ son no nulos y la fórmula de $w_j$ no divide por cero.

*Span.* Por construcción, $w_j=v_j-s$ con $s\in\operatorname{gen}\{w_1,\dots,w_{j-1}\}=\operatorname{gen}\{v_1,\dots,v_{j-1}\}$ (hipótesis inductiva). Luego $w_j\in\operatorname{gen}\{v_1,\dots,v_j\}$, y también $v_j=w_j+s\in\operatorname{gen}\{w_1,\dots,w_j\}$. Como $\operatorname{gen}\{w_1,\dots,w_{j-1}\}=\operatorname{gen}\{v_1,\dots,v_{j-1}\}$, se concluye $\operatorname{gen}\{w_1,\dots,w_j\}=\operatorname{gen}\{v_1,\dots,v_j\}$. Es la afirmación 3.

*No nulidad.* Si fuera $w_j=0_V$, tendríamos $v_j=s\in\operatorname{gen}\{v_1,\dots,v_{j-1}\}$, contra la independencia lineal de $\{v_1,\dots,v_j\}$.

*Ortogonalidad.* Basta ver que $w_j\perp w_l$ para cada $l<j$, porque el resto ya es ortogonal por hipótesis. Usando $\langle w_i,w_l\rangle=0$ si $i\neq l$ (hipótesis inductiva), en la suma sobrevive solamente el término $i=l$:

$$
\langle w_j,w_l\rangle=\langle v_j,w_l\rangle-\sum_{i=1}^{j-1}\frac{\langle v_j,w_i\rangle}{\langle w_i,w_i\rangle}\langle w_i,w_l\rangle=\langle v_j,w_l\rangle-\frac{\langle v_j,w_l\rangle}{\langle w_l,w_l\rangle}\langle w_l,w_l\rangle=0 .
$$

Esto completa el paso inductivo. $\blacksquare$

:::note[Corolario]
Todo espacio euclídeo de dimensión finita tiene una base ortogonal y una base ortonormal. Más aún, toda base ortogonal de un subespacio $S\subseteq V$ se puede extender a una base ortogonal de $V$.
:::

La primera parte sale de aplicar el teorema a una base cualquiera y normalizar. Para la segunda, se completa la base ortogonal $\{w_1,\dots,w_k\}$ de $S$ a una base de $V$ con vectores cualesquiera y se aplica Gram-Schmidt: como los primeros $k$ vectores ya son ortogonales, el método los deja **sin cambios**, porque cada $\langle w_j,w_i\rangle=0$ anula todos los términos de la resta.

## Cómo conviene calcular

- **El orden importa.** Una base distinta de ordenar los $v_j$ produce otra base ortogonal del mismo subespacio. Se puede elegir el orden que dé las cuentas más cómodas, siempre que sea un orden fijo.
- **Reescalar para evitar fracciones.** Si $w_j$ se reemplaza por un múltiplo no nulo $\alpha w_j$, los pasos siguientes no cambian, porque el sumando $\dfrac{\langle v,w\rangle}{\langle w,w\rangle}w$ es el mismo para $w$ y para $\alpha w$ (el escalar se cancela). Entonces conviene multiplicar cada $w_j$ por un entero que elimine denominadores *antes* de usarlo en el paso siguiente.
- **Normalizar al final.** Las raíces cuadradas aparecen solo cuando hace falta una base ortonormal, y se agregan al terminar: $\hat w_j=w_j/\lVert w_j\rVert$. Normalizar en cada paso complica las cuentas sin cambiar el resultado.
- **Comprobar.** Después de cada vector, verificar que su producto interno con los anteriores es $0$. Un error se detecta en el paso en que ocurre, no al final.
- **Con un producto no usual**, las fórmulas son idénticas, pero *todos* los productos y normas son los del producto elegido.

:::tip[Dependencia lineal]
Si los vectores de partida son LD, el método no falla: en algún paso $w_j=0_V$, porque $v_j$ está en el generado de los anteriores. Se descarta ese $w_j$ y se sigue con el resto. Los $w$ no nulos que quedan son una base ortogonal del generado. Así se puede usar Gram-Schmidt también para detectar dependencias (Ejemplo 4).
:::

## Ejemplos

### Ejemplo 1 · Tres vectores de $\mathbb{R}^4$ con el producto usual
<!-- check: U4.T04.E1 -->

Aplicar Gram-Schmidt a $v_1=(1,1,1,1)$, $v_2=(1,2,0,1)$ y $v_3=(2,0,1,3)$, y hallar una base ortonormal del generado.

**Resolución.** *Paso 1.* $w_1=v_1=(1,1,1,1)$, con $\langle w_1,w_1\rangle=4$.

*Paso 2.* $\langle v_2,w_1\rangle=1+2+0+1=4$, entonces

$$
w_2=(1,2,0,1)-\frac44(1,1,1,1)=(0,1,-1,0),\qquad\langle w_2,w_2\rangle=2 .
$$

*Paso 3.* $\langle v_3,w_1\rangle=2+0+1+3=6$ y $\langle v_3,w_2\rangle=0+0-1+0=-1$. Entonces

$$
w_3=(2,0,1,3)-\frac64(1,1,1,1)-\frac{-1}{2}(0,1,-1,0)=\left(\tfrac12,\,-1,\,-1,\,\tfrac32\right).
$$

Reescalamos multiplicando por $2$: $w_3'=(1,-2,-2,3)$, con $\langle w_3',w_3'\rangle=1+4+4+9=18$. La base ortogonal es $\{(1,1,1,1),\ (0,1,-1,0),\ (1,-2,-2,3)\}$, con normas al cuadrado $4$, $2$ y $18$. Normalizando,

$$
\hat w_1=\tfrac12(1,1,1,1),\qquad\hat w_2=\tfrac1{\sqrt2}(0,1,-1,0),\qquad\hat w_3=\tfrac1{3\sqrt2}(1,-2,-2,3).
$$

**Comprobación.** $w_1\cdot w_2=0$; $w_1\cdot w_3'=1-2-2+3=0$; $w_2\cdot w_3'=-2+2=0$. Además $v_3=\tfrac32w_1-\tfrac12w_2+\tfrac12w_3'$ y los tres vectores originales y los tres nuevos generan el mismo subespacio, de dimensión $3$.

### Ejemplo 2 · Una base de un plano con un producto no usual
<!-- check: U4.T04.E2 -->

En $\mathbb{R}^3$ con el producto ponderado $\langle x,y\rangle=x_1y_1+2x_2y_2+3x_3y_3$, los vectores $v_1=(2,1,0)$ y $v_2=(1,1,1)$ generan el plano $S:\ x_1-2x_2+x_3=0$. Hallar una base ortogonal de $S$ para ese producto.

**Resolución.** Ambos pertenecen al plano: $2-2+0=0$ y $1-2+1=0$. Tomamos $w_1=v_1=(2,1,0)$, con $\langle w_1,w_1\rangle=4+2=6$. Con el producto ponderado, $\langle v_2,w_1\rangle=1\cdot2+2\cdot1\cdot1+0=4$, de modo que

$$
w_2=(1,1,1)-\frac46(2,1,0)=\left(-\tfrac13,\ \tfrac13,\ 1\right).
$$

Reescalamos por $3$: $w_2'=(-1,1,3)$. Verificamos la ortogonalidad con el producto ponderado: $\langle w_1,w_2'\rangle=2\cdot(-1)+2\cdot1\cdot1+0=0$. La norma es $\langle w_2',w_2'\rangle=1+2+27=30$. Una base ortonormal de $S$ es $\left\{\tfrac1{\sqrt6}(2,1,0),\ \tfrac1{\sqrt{30}}(-1,1,3)\right\}$.

**Comprobación.** $w_2'$ está en el plano: $-1-2+3=0$. Con el producto **usual** estos vectores no serían ortogonales: $(2,1,0)\cdot(-1,1,3)=-1$. Hallar una base ortogonal de $S$ para el producto usual daría otros vectores.

### Ejemplo 3 · Gram-Schmidt en $P_2[\mathbb{R}]$ con el producto por evaluación
<!-- check: U4.T04.E3 -->

En $P_2[\mathbb{R}]$ con $\langle p,q\rangle=p(-1)q(-1)+p(0)q(0)+p(1)q(1)$, aplicar Gram-Schmidt a la base canónica $E=\{1,x,x^2\}$ (en ese orden) y hallar las coordenadas de $p=1+2x+3x^2$ en la base ortogonal obtenida.

**Resolución.** Cada polinomio se evalúa en $-1,0,1$: $1\mapsto(1,1,1)$, $x\mapsto(-1,0,1)$ y $x^2\mapsto(1,0,1)$. *Paso 1.* $w_1=1$, con $\langle1,1\rangle=3$.

*Paso 2.* $\langle x,1\rangle=-1+0+1=0$, así que $w_2=x$, con $\langle x,x\rangle=2$.

*Paso 3.* $\langle x^2,1\rangle=2$ y $\langle x^2,x\rangle=-1+0+1=0$:

$$
w_3=x^2-\frac23\cdot1-\frac02\,x=x^2-\frac23 ,
$$

y reescalando por $3$, $q_3=3x^2-2$, que toma los valores $(1,-2,1)$, con $\langle q_3,q_3\rangle=6$. La base ortogonal es $\{1,\ x,\ 3x^2-2\}$, con normas al cuadrado $3$, $2$ y $6$.

Para $p=1+2x+3x^2$, que toma los valores $(2,1,6)$:

$$
c_1=\frac{\langle p,1\rangle}{3}=\frac93=3,\qquad c_2=\frac{\langle p,x\rangle}{2}=\frac{-2+0+6}{2}=2,\qquad c_3=\frac{\langle p,q_3\rangle}{6}=\frac{2-2+6}{6}=1 .
$$

**Comprobación.** $3\cdot1+2x+1\cdot(3x^2-2)=1+2x+3x^2=p$. Cuando se usa un producto distinto, por ejemplo evaluando en otros nodos, se obtiene una base ortogonal distinta: el polinomio ortogonal depende de los nodos elegidos.

### Ejemplo 4 · Gram-Schmidt detecta una dependencia lineal
<!-- check: U4.T04.E4 -->

Aplicar el método a $v_1=(1,0,1)$, $v_2=(1,1,0)$ y $v_3=(3,1,2)$ en $\mathbb{R}^3$ con el producto usual.

**Resolución.** $w_1=(1,0,1)$ con $\langle w_1,w_1\rangle=2$. Como $\langle v_2,w_1\rangle=1$, $w_2=(1,1,0)-\frac12(1,0,1)=\left(\tfrac12,1,-\tfrac12\right)$, que reescalado es $w_2'=(1,2,-1)$ con $\langle w_2',w_2'\rangle=6$. Para $v_3$: $\langle v_3,w_1\rangle=5$ y $\langle v_3,w_2'\rangle=3+2-2=3$, luego

$$
w_3=(3,1,2)-\frac52(1,0,1)-\frac36(1,2,-1)=\left(3-\tfrac52-\tfrac12,\ 1-0-1,\ 2-\tfrac52+\tfrac12\right)=(0,0,0).
$$

El tercer vector se anula: $v_3\in\operatorname{gen}\{v_1,v_2\}$. De hecho $v_3=2v_1+v_2$. Se descarta $w_3$ y $\{(1,0,1),(1,2,-1)\}$ es una base ortogonal de $\operatorname{gen}\{v_1,v_2,v_3\}$, que tiene dimensión $2$.

**Comprobación.** $2(1,0,1)+(1,1,0)=(3,1,2)$. El producto $(1,0,1)\cdot(1,2,-1)=0$.

### Ejemplo 5 · Completar una base ortogonal
<!-- check: U4.T04.E5 -->

Completar $\{w_1,w_2,w_3\}$ del Ejemplo 1, con $w_3=(1,-2,-2,3)$, a una base ortogonal de $\mathbb{R}^4$.

**Resolución.** *Primer método (sistema).* El cuarto vector debe ser ortogonal a los tres primeros, es decir, pertenecer al complemento ortogonal que se estudia en la [lección 4.5](/algebra-ii/unidad-4/teoria/complemento-ortogonal/). Como $y\perp w_i$ equivale a $w_i\cdot y=0$, resolvemos

$$
\begin{cases}y_1+y_2+y_3+y_4=0\\ y_2-y_3=0\\ y_1-2y_2-2y_3+3y_4=0\end{cases}
$$

De la segunda, $y_2=y_3$. Las otras dos quedan $y_1+2y_2+y_4=0$ y $y_1-4y_2+3y_4=0$; restando, $6y_2-2y_4=0$, o sea $y_4=3y_2$, y $y_1=-2y_2-3y_2=-5y_2$. Con $y_2=1$ resulta $w_4=(-5,1,1,3)$.

*Segundo método (Gram-Schmidt).* Se agrega un vector que complete una base, por ejemplo $e_1$, y se ortogonaliza: $\langle e_1,w_1\rangle=1$, $\langle e_1,w_2\rangle=0$ y $\langle e_1,w_3\rangle=1$, entonces

$$
u_4=e_1-\frac14(1,1,1,1)-0-\frac1{18}(1,-2,-2,3)=\frac5{36}(5,-1,-1,-3),
$$

un múltiplo de $(5,-1,-1,-3)=-w_4$. Los dos métodos dan la misma dirección, como debe ser: el complemento ortogonal de un subespacio de dimensión $3$ en $\mathbb{R}^4$ es una recta.

**Comprobación.** $w_4\cdot w_1=-5+1+1+3=0$; $w_4\cdot w_2=1-1=0$; $w_4\cdot w_3=-5-2-2+9=0$, y $\lVert w_4\rVert^2=36$.

:::caution[Errores frecuentes]
- **Restar la proyección sobre $v_i$ en vez de sobre $w_i$.** Las fórmulas usan los vectores *ya ortogonalizados* $w_i$; con los $v_i$ originales el resultado no es ortogonal.
- **Olvidar dividir por $\langle w_i,w_i\rangle$.** El coeficiente es $\langle v_j,w_i\rangle/\langle w_i,w_i\rangle$, no el producto solo. Solo con $w_i$ unitario el denominador vale $1$.
- **Reescalar de más.** Multiplicar $w_j$ por un escalar no nulo está permitido; sumarle otro vector al reescalar o cambiar el sentido de la resta, no.
- **Cambiar de producto a mitad del cálculo.** En un producto no usual, cada $\langle\cdot,\cdot\rangle$ y cada norma usan la misma fórmula.
- **Normalizar con la norma usual** cuando el producto no lo es (Ejemplo 2: $\lVert w_1\rVert=\sqrt6$, no $\sqrt5$).
- **Aplicar el método a un conjunto LD y suponer que el vector nulo es una base.** El $w_j=0_V$ se descarta; no forma parte de ninguna base.
- **Creer que la base ortogonal es única.** Depende del orden de los $v_j$ y de los factores de escala.
:::

## Autoevaluación

<details>
<summary>1. Si {v₁, v₂} ya es ortogonal, ¿qué devuelve Gram-Schmidt?</summary>

Los mismos vectores: $w_1=v_1$ y $\langle v_2,w_1\rangle=0$ anula el término de la resta, así que $w_2=v_2$.

</details>

<details>
<summary>2. Aplicar Gram-Schmidt a (1, 1) y (1, 0) con el producto usual, en los dos órdenes. ¿Dan la misma base?</summary>

En el orden $(1,1),(1,0)$: $w_2=(1,0)-\tfrac12(1,1)=(\tfrac12,-\tfrac12)$. En el orden $(1,0),(1,1)$: $w_1=(1,0)$ y $w_2=(1,1)-(1,0)=(0,1)$. Son bases ortogonales distintas, ambas de $\mathbb{R}^2$.

</details>

<details>
<summary>3. ¿Por qué Gram-Schmidt no necesita dividir por cero?</summary>

Porque cada $w_i$ es no nulo mientras los $v$ sean LI (parte 1 del teorema): si $w_j=0$ entonces $v_j$ dependería de los anteriores.

</details>

:::tip[En resumen]
- $w_1=v_1$ y $w_j=v_j-\sum_{i<j}\dfrac{\langle v_j,w_i\rangle}{\langle w_i,w_i\rangle}w_i$: cada $w_j$ es ortogonal a los anteriores y $\operatorname{gen}\{w_1,\dots,w_j\}=\operatorname{gen}\{v_1,\dots,v_j\}$.
- Se puede reescalar cada $w_j$ para evitar fracciones; se normaliza solo al final.
- Si los $v_j$ son LD, aparece algún $w_j=0_V$, que se descarta.
- Todo espacio euclídeo de dimensión finita tiene bases ortonormales, y toda base ortogonal de un subespacio se extiende a una de todo el espacio.
- Las cuentas dependen del producto interno: con productos no usuales los vectores resultantes son otros.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 5.3, "El proceso de Gram-Schmidt y la factorización QR" (p. 399); sección 7.1 (p. 554) para espacios con producto interno generales.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ortogonalidad y mínimos cuadrados (proceso de Gram-Schmidt y factorización QR).
- Anterior: [4.3 Ortogonalidad](/algebra-ii/unidad-4/teoria/ortogonalidad/). Siguiente: [4.5 Complemento ortogonal](/algebra-ii/unidad-4/teoria/complemento-ortogonal/).
- Repaso: [sistemas lineales](/algebra-ii/repaso/sistemas-lineales/); [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/).
