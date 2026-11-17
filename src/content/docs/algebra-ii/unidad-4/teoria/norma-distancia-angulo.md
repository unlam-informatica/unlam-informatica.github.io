---
title: Norma, distancia y ángulo
description: Norma inducida, distancia y ángulo en un espacio euclídeo, desigualdades de Cauchy-Schwarz y triangular, Pitágoras, ley del coseno y similitud coseno entre documentos.
slug: algebra-ii/unidad-4/teoria/norma-distancia-angulo
sidebar:
  order: 2
  label: 4.2 Norma, distancia y ángulo
---

En $\mathbb{R}^2$ la longitud de $v=(v_1,v_2)$ es $\sqrt{v_1^2+v_2^2}=\sqrt{v\cdot v}$ (Pitágoras), la distancia entre dos puntos es la longitud de su diferencia y el ángulo entre dos vectores sale de $u\cdot v=\lVert u\rVert\lVert v\rVert\cos\theta$. En esta lección copiamos esas tres definiciones en cualquier espacio euclídeo, reemplazando el producto punto por el producto interno. Lo que hay que demostrar es que siguen teniendo sentido: que el "coseno" que obtenemos está entre $-1$ y $1$ (Cauchy-Schwarz) y que la distancia cumple la desigualdad triangular.

Como cada producto interno define sus propias longitudes y ángulos, los mismos vectores pueden ser unitarios y perpendiculares con un producto y no serlo con otro. Al final aplicamos el ángulo a un problema de recuperación de información: medir cuán parecidos son dos documentos.

En toda la lección, $(V,\langle\,,\rangle)$ es un espacio euclídeo (ver [4.1 Producto interno](/algebra-ii/unidad-4/teoria/producto-interno/)).

## Norma

:::note[Definición (norma inducida)]
La **norma** (o módulo, o longitud) de $v\in V$ es

$$
\lVert v\rVert=\sqrt{\langle v,v\rangle}.
$$

Un vector con $\lVert v\rVert=1$ se llama **unitario**. Si $v\neq0$, el vector $\dfrac{v}{\lVert v\rVert}$ es unitario y tiene la misma dirección y sentido que $v$: dividir por la norma se llama **normalizar**.
:::

La raíz está bien definida porque $\langle v,v\rangle\ge0$. Con el producto usual de $\mathbb{R}^n$ es la longitud euclídea $\sqrt{v_1^2+\dots+v_n^2}$; con un producto no usual, la norma cambia aunque el vector sea el mismo.

## La desigualdad de Cauchy-Schwarz

:::note[Teorema (desigualdad de Cauchy-Schwarz)]
Para todos $u,v\in V$,

$$
\langle u,v\rangle^2\le\langle u,u\rangle\,\langle v,v\rangle,\qquad\text{es decir,}\qquad \lvert\langle u,v\rangle\rvert\le\lVert u\rVert\,\lVert v\rVert .
$$

Además, vale la igualdad si y solo si $\{u,v\}$ es linealmente dependiente.
:::

**Demostración.** Si $v=0_V$, los dos miembros valen $0$ y $\{u,v\}$ es LD: el enunciado se cumple. Supongamos $v\neq0_V$, de modo que $\langle v,v\rangle>0$. Para cada $t\in\mathbb{R}$, por positividad y la propiedad de desarrollo de la lección 4.1,

$$
0\le\langle u-tv,\,u-tv\rangle=\langle u,u\rangle-2t\langle u,v\rangle+t^2\langle v,v\rangle .
$$

Elegimos el valor de $t$ que minimiza esa expresión, $t_0=\dfrac{\langle u,v\rangle}{\langle v,v\rangle}$ (el vértice de la parábola en $t$). Reemplazando,

$$
0\le\langle u,u\rangle-2\frac{\langle u,v\rangle^2}{\langle v,v\rangle}+\frac{\langle u,v\rangle^2}{\langle v,v\rangle}=\langle u,u\rangle-\frac{\langle u,v\rangle^2}{\langle v,v\rangle},
$$

y multiplicando por $\langle v,v\rangle>0$ se obtiene $\langle u,v\rangle^2\le\langle u,u\rangle\langle v,v\rangle$. Tomando raíz cuadrada queda la segunda forma.

*Caso de igualdad.* Si hay igualdad (con $v\neq0$), la cuenta anterior dice $\langle u-t_0v,u-t_0v\rangle=0$, y por positividad $u=t_0v$: el conjunto es LD. Recíprocamente, si $\{u,v\}$ es LD y $v\neq0$, entonces $u=kv$ para algún $k$ y $\langle u,v\rangle^2=k^2\langle v,v\rangle^2=\langle kv,kv\rangle\langle v,v\rangle$. $\blacksquare$

La demostración solo usa los axiomas: vale para el producto usual, para cualquier producto no usual de $\mathbb{R}^n$, para la traza en matrices y para la evaluación en polinomios. Por ejemplo, con el producto por evaluación en $-1,0,1$ dice que, para todo par de polinomios de grado a lo sumo 2,

$$
\big(p(-1)q(-1)+p(0)q(0)+p(1)q(1)\big)^2\le\big(p(-1)^2+p(0)^2+p(1)^2\big)\big(q(-1)^2+q(0)^2+q(1)^2\big).
$$

## Propiedades de la norma y la distancia

:::note[Propiedad (norma)]
Para todos $u,v\in V$ y $k\in\mathbb{R}$:

1. $\lVert v\rVert\ge0$, y $\lVert v\rVert=0$ si y solo si $v=0_V$.
2. $\lVert kv\rVert=\lvert k\rvert\,\lVert v\rVert$.
3. **Desigualdad triangular:** $\lVert u+v\rVert\le\lVert u\rVert+\lVert v\rVert$.
:::

**Demostración.** (1) Es la positividad. (2) $\lVert kv\rVert^2=\langle kv,kv\rangle=k^2\langle v,v\rangle$, y $\sqrt{k^2}=\lvert k\rvert$. (3) Usando el desarrollo de $\langle u+v,u+v\rangle$ y Cauchy-Schwarz:

$$
\lVert u+v\rVert^2=\lVert u\rVert^2+2\langle u,v\rangle+\lVert v\rVert^2\le\lVert u\rVert^2+2\lVert u\rVert\lVert v\rVert+\lVert v\rVert^2=\big(\lVert u\rVert+\lVert v\rVert\big)^2 .
$$

Como ambas cantidades son no negativas, se puede tomar raíz. $\blacksquare$

Geométricamente, la desigualdad triangular dice que en el triángulo de lados $u$, $v$ y $u+v$ un lado no supera la suma de los otros dos.

:::note[Definición (distancia)]
La **distancia** entre $u$ y $v$ es $d(u,v)=\lVert u-v\rVert$.
:::

:::note[Propiedad (distancia)]
Para todos $u,v,w\in V$:

1. $d(u,v)\ge0$, y $d(u,v)=0$ si y solo si $u=v$.
2. $d(u,v)=d(v,u)$.
3. $d(u,w)\le d(u,v)+d(v,w)$.
:::

**Demostración.** (1) es la propiedad 1 de la norma aplicada a $u-v$. (2) $\lVert u-v\rVert=\lVert(-1)(v-u)\rVert=\lvert-1\rvert\lVert v-u\rVert$. (3) $u-w=(u-v)+(v-w)$ y se aplica la desigualdad triangular de la norma. $\blacksquare$

Una función con estas tres propiedades se llama **métrica**. En la [lección 4.8](/algebra-ii/unidad-4/teoria/codigos-y-z2/) aparece otra métrica que no proviene de ningún producto interno: la distancia de Hamming en $\mathbb{Z}_2^n$.

## Ángulo entre dos vectores

Si $u$ y $v$ no son nulos, Cauchy-Schwarz garantiza que

$$
-1\le\frac{\langle u,v\rangle}{\lVert u\rVert\,\lVert v\rVert}\le1 .
$$

Como el coseno es una biyección entre $[0,\pi]$ y $[-1,1]$, existe un único ángulo en ese intervalo con ese coseno.

:::note[Definición (ángulo)]
Si $u,v\in V$ son no nulos, el **ángulo** entre ellos es el único $\theta=\angle(u,v)\in[0,\pi]$ tal que

$$
\cos\theta=\frac{\langle u,v\rangle}{\lVert u\rVert\,\lVert v\rVert}.
$$

Si $\langle u,v\rangle=0$ decimos que $u$ y $v$ son **ortogonales** y escribimos $u\perp v$ (la ortogonalidad se desarrolla en la [lección 4.3](/algebra-ii/unidad-4/teoria/ortogonalidad/)).
:::

Para vectores no nulos: $\theta=\pi/2$ si y solo si $u\perp v$; $\theta=0$ si y solo si $v$ es un múltiplo positivo de $u$; $\theta=\pi$ si y solo si es un múltiplo negativo (los dos últimos son el caso de igualdad de Cauchy-Schwarz). El vector nulo es ortogonal a todos, pero no forma ángulo con ninguno.

:::note[Teorema (Pitágoras generalizado y ley del coseno)]
Para todos $u,v\in V$:

1. $u\perp v$ si y solo si $\lVert u+v\rVert^2=\lVert u\rVert^2+\lVert v\rVert^2$.
2. Si $u,v\neq0$ y $\theta=\angle(u,v)$, entonces $\lVert u-v\rVert^2=\lVert u\rVert^2+\lVert v\rVert^2-2\lVert u\rVert\lVert v\rVert\cos\theta$.
:::

**Demostración.** (1) $\lVert u+v\rVert^2=\lVert u\rVert^2+2\langle u,v\rangle+\lVert v\rVert^2$, que coincide con $\lVert u\rVert^2+\lVert v\rVert^2$ si y solo si $\langle u,v\rangle=0$. (2) $\lVert u-v\rVert^2=\lVert u\rVert^2-2\langle u,v\rangle+\lVert v\rVert^2$ y, por la definición de ángulo, $\langle u,v\rangle=\lVert u\rVert\lVert v\rVert\cos\theta$. $\blacksquare$

Por inducción, si $u_1,\dots,u_k$ son ortogonales dos a dos, $\lVert u_1+\dots+u_k\rVert^2=\lVert u_1\rVert^2+\dots+\lVert u_k\rVert^2$. Esta versión es la que usaremos en proyecciones.

### Ejemplo 1 · Norma, distancia y ángulo con el producto usual
<!-- check: U4.T02.E1 -->

En $\mathbb{R}^3$ con el producto usual, sean $u=(2,1,-2)$ y $v=(1,1,0)$. Calcular $\lVert u\rVert$, $\lVert v\rVert$, $d(u,v)$ y $\angle(u,v)$, y un vector unitario en la dirección de $u$.

**Resolución.** $\lVert u\rVert=\sqrt{4+1+4}=3$ y $\lVert v\rVert=\sqrt{1+1+0}=\sqrt2$. Como $u-v=(1,0,-2)$, resulta $d(u,v)=\sqrt{1+0+4}=\sqrt5$. Además $u\cdot v=2+1+0=3$, así que

$$
\cos\theta=\frac{3}{3\sqrt2}=\frac{1}{\sqrt2}\quad\Longrightarrow\quad\angle(u,v)=\frac{\pi}{4}.
$$

El unitario en la dirección de $u$ es $\frac13(2,1,-2)$.

**Comprobación.** Cauchy-Schwarz: $3\le3\sqrt2$. Ley del coseno: $\lVert u\rVert^2+\lVert v\rVert^2-2\cdot3\cdot\sqrt2\cdot\frac1{\sqrt2}=9+2-6=5=d(u,v)^2$.

## Las medidas dependen del producto interno

### Ejemplo 2 · Los canónicos con un producto no usual
<!-- check: U4.T02.E2 -->

En $\mathbb{R}^2$ con $\langle x,y\rangle=x_1y_1+(x_1+x_2)(y_1+y_2)$ (el producto del Ejemplo 2 de la lección 4.1), calcular $\lVert e_1\rVert$, $\lVert e_2\rVert$, $\angle(e_1,e_2)$ y $d(e_1,e_2)$. Hallar los vectores ortogonales a $e_1$.

**Resolución.** Con la fórmula:

$$
\lVert e_1\rVert^2=1\cdot1+(1+0)(1+0)=2,\qquad\lVert e_2\rVert^2=0+(0+1)(0+1)=1,\qquad\langle e_1,e_2\rangle=0+(1)(1)=1 .
$$

Entonces $\lVert e_1\rVert=\sqrt2$, $e_2$ es unitario y

$$
\cos\angle(e_1,e_2)=\frac{1}{\sqrt2\cdot1}\quad\Longrightarrow\quad\angle(e_1,e_2)=\frac{\pi}{4}.
$$

Para la distancia, $e_1-e_2=(1,-1)$ y $\lVert(1,-1)\rVert^2=1+(1-1)^2=1$, así que $d(e_1,e_2)=1$ (con el producto usual sería $\sqrt2$).

Un vector $y$ es ortogonal a $e_1$ si $\langle e_1,y\rangle=y_1+(y_1+y_2)=2y_1+y_2=0$, es decir, $y\in\operatorname{gen}\{(1,-2)\}$.

**Comprobación.** Ley del coseno: $2+1-2\cdot\sqrt2\cdot1\cdot\frac{1}{\sqrt2}=1=d(e_1,e_2)^2$. Y $\langle e_1,(1,-2)\rangle=1+(1)(1-2)=0$.

La conclusión es importante para toda la unidad: **la base canónica no es ortonormal con cualquier producto**. En este espacio euclídeo $e_1$ y $e_2$ forman $45^\circ$, $e_1$ mide $\sqrt2$ y la dirección perpendicular a $e_1$ es la de $(1,-2)$, no la de $e_2$.

### Ejemplo 3 · Ángulo y Pitágoras entre polinomios
<!-- check: U4.T02.E3 -->

En $P_2[\mathbb{R}]$ con $\langle p,q\rangle=p(-1)q(-1)+p(0)q(0)+p(1)q(1)$, calcular el ángulo entre $p=x$ y $q=x+x^2$. Verificar que $1\perp x$ y comprobar Pitágoras para $1$ y $x$.

**Resolución.** Los valores en $-1,0,1$ son: $p\mapsto(-1,0,1)$ y $q\mapsto(0,0,2)$. Entonces $\langle p,q\rangle=0+0+2=2$, $\lVert p\rVert^2=1+0+1=2$ y $\lVert q\rVert^2=0+0+4=4$:

$$
\cos\angle(p,q)=\frac{2}{\sqrt2\cdot2}=\frac{1}{\sqrt2}\quad\Longrightarrow\quad\angle(x,\,x+x^2)=\frac{\pi}{4}.
$$

Para $1$ y $x$: los valores son $(1,1,1)$ y $(-1,0,1)$, y $\langle 1,x\rangle=-1+0+1=0$, así que $1\perp x$. Por Pitágoras debería ser $\lVert 1+x\rVert^2=\lVert1\rVert^2+\lVert x\rVert^2=3+2=5$.

**Comprobación.** $1+x$ toma los valores $(0,1,2)$, y $\lVert1+x\rVert^2=0+1+4=5$.

## Aplicación: similitud coseno entre documentos

En recuperación de información, un documento se representa por un **vector de frecuencias**: se fija un vocabulario de $n$ términos y la componente $i$ cuenta cuántas veces aparece el término $i$. Para comparar dos documentos se usa la **similitud coseno**

$$
\operatorname{sim}(a,b)=\cos\angle(a,b)=\frac{a\cdot b}{\lVert a\rVert\,\lVert b\rVert},
$$

con el producto usual de $\mathbb{R}^n$. Como las frecuencias son no negativas, $a\cdot b\ge0$ y la similitud está entre $0$ (sin términos en común) y $1$ (misma proporción de términos).

¿Por qué el ángulo y no la distancia? Un documento que repite dos veces el texto de otro tiene el vector duplicado: el **contenido** es el mismo, pero la distancia entre los vectores es grande. El ángulo no cambia al multiplicar un vector por un escalar positivo, así que mide la proporción de términos e ignora la longitud del texto. Normalizar los vectores ($\hat a=a/\lVert a\rVert$) resuelve lo mismo, porque para vectores unitarios

$$
\lVert\hat a-\hat b\rVert^2=\lVert\hat a\rVert^2+\lVert\hat b\rVert^2-2\,\hat a\cdot\hat b=2-2\cos\angle(a,b):
$$

ordenar por distancia entre vectores normalizados es lo mismo que ordenar por similitud coseno (de mayor a menor).

### Ejemplo 4 · Cuatro documentos
<!-- check: U4.T02.E4 -->

Con el vocabulario (matriz, vector, base, gol, partido), cuatro documentos tienen frecuencias

$$
d_1=(2,1,2,0,0),\quad d_2=(4,2,4,0,0),\quad d_3=(1,0,0,2,2),\quad d_4=(2,2,1,0,0).
$$

Ordenar $d_2,d_3,d_4$ según su parecido con $d_1$ usando la distancia y usando la similitud coseno.

**Resolución.** $\lVert d_1\rVert=\sqrt{4+1+4}=3$, $\lVert d_2\rVert=6$, $\lVert d_3\rVert=\sqrt{1+4+4}=3$, $\lVert d_4\rVert=\sqrt{4+4+1}=3$.

| Documento | Producto con $d_1$ | Similitud coseno | Distancia a $d_1$ |
|---|---|---|---|
| $d_2$ | $18$ | $18/18=1$ | $\sqrt9=3$ |
| $d_3$ | $2$ | $2/9\approx0{,}22$ | $\sqrt{14}\approx3{,}74$ |
| $d_4$ | $8$ | $8/9\approx0{,}89$ | $\sqrt2\approx1{,}41$ |

Las distancias salen de $d_1-d_2=(-2,-1,-2,0,0)$, $d_1-d_3=(1,1,2,-2,-2)$ y $d_1-d_4=(0,-1,1,0,0)$.

Con la distancia, el orden es $d_4$, $d_2$, $d_3$: el documento $d_2$, que es $d_1$ "repetido dos veces", queda segundo. Con la similitud coseno el orden es $d_2$ (similitud 1: mismo contenido), $d_4$ (comparte los términos de álgebra con otras proporciones) y $d_3$ (habla sobre todo de fútbol).

**Comprobación.** Normalizando, $\hat d_1=\frac13(2,1,2,0,0)=\frac16(4,2,4,0,0)=\hat d_2$, de modo que $\lVert\hat d_1-\hat d_2\rVert^2=0=2-2\cdot1$.

En sistemas reales las frecuencias se ponderan (por ejemplo, restando peso a palabras muy comunes) antes de calcular el coseno; la geometría es la misma.

:::caution[Errores frecuentes]
- **Calcular la norma con la fórmula usual cuando el producto no es usual.** En el Ejemplo 2, $\lVert e_1\rVert=\sqrt2$, no $1$.
- **Suponer que $\lVert u+v\rVert=\lVert u\rVert+\lVert v\rVert$.** En general solo vale "$\le$". Con $u=(1,0)$, $v=(0,1)$ y el producto usual: $\sqrt2<2$.
- **Escribir $\lVert kv\rVert=k\lVert v\rVert$.** Con $k<0$ da una norma negativa; lo correcto es $\lvert k\rvert\lVert v\rVert$.
- **Olvidar la raíz.** $\langle v,v\rangle$ es $\lVert v\rVert^2$, no $\lVert v\rVert$; al calcular cosenos hay que dividir por el producto de las normas, no de sus cuadrados.
- **Calcular el ángulo con un vector nulo.** No está definido: el denominador se anula.
- **Usar Pitágoras sin verificar ortogonalidad.** La igualdad $\lVert u+v\rVert^2=\lVert u\rVert^2+\lVert v\rVert^2$ es *equivalente* a $u\perp v$.
- **Comparar documentos de distinta longitud por distancia sin normalizar** (Ejemplo 4).
:::

## Autoevaluación

<details>
<summary>1. Si u y v son unitarios y ‖u + v‖ = √3 con un cierto producto interno, ¿cuánto vale ⟨u, v⟩ y qué ángulo forman?</summary>

$3=\lVert u+v\rVert^2=1+2\langle u,v\rangle+1$, así que $\langle u,v\rangle=\frac12$ y $\cos\theta=\frac12$: $\theta=\frac{\pi}{3}$.

</details>

<details>
<summary>2. ¿Puede haber dos vectores unitarios con ‖u + v‖ = 3?</summary>

No: por la desigualdad triangular $\lVert u+v\rVert\le1+1=2$. Equivalentemente, se necesitaría $\langle u,v\rangle=\frac72>1=\lVert u\rVert\lVert v\rVert$, contra Cauchy-Schwarz.

</details>

<details>
<summary>3. Probar la ley del paralelogramo: ‖u + v‖² + ‖u − v‖² = 2‖u‖² + 2‖v‖².</summary>

Se suman los desarrollos $\lVert u\pm v\rVert^2=\lVert u\rVert^2\pm2\langle u,v\rangle+\lVert v\rVert^2$: los términos con $\langle u,v\rangle$ se cancelan.

</details>

:::tip[En resumen]
- $\lVert v\rVert=\sqrt{\langle v,v\rangle}$, $d(u,v)=\lVert u-v\rVert$, y $\cos\angle(u,v)=\dfrac{\langle u,v\rangle}{\lVert u\rVert\lVert v\rVert}$ para $u,v\neq0$.
- Cauchy-Schwarz: $\lvert\langle u,v\rangle\rvert\le\lVert u\rVert\lVert v\rVert$, con igualdad si y solo si $u$ y $v$ son LD. Garantiza que el ángulo está bien definido y da la desigualdad triangular.
- Pitágoras: $u\perp v\iff\lVert u+v\rVert^2=\lVert u\rVert^2+\lVert v\rVert^2$; ley del coseno para el caso general.
- Normas, distancias, ángulos y ortogonalidad dependen del producto interno elegido.
- La similitud coseno compara direcciones e ignora longitudes: es la herramienta adecuada para vectores de frecuencias.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 1.2, "Longitud y ángulo: el producto punto" (p. 18); sección 7.1, "Espacios con producto interno" (p. 554); sección 7.2, "Normas y funciones de distancia" (p. 575).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ortogonalidad y mínimos cuadrados (longitud, distancia y desigualdades en espacios con producto interno).
- Anterior: [4.1 Producto interno](/algebra-ii/unidad-4/teoria/producto-interno/). Siguiente: [4.3 Ortogonalidad](/algebra-ii/unidad-4/teoria/ortogonalidad/).
- Repaso: [vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/).
