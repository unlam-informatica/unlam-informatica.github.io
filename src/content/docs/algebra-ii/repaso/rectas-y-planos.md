---
title: Rectas y planos
description: Ecuaciones vectorial, paramétricas e implícita de rectas y planos, vector normal, producto vectorial, rectas y planos por el origen y posiciones relativas.
slug: algebra-ii/repaso/rectas-y-planos
sidebar:
  order: 5
  label: R.5 Rectas y planos
---

## Para qué sirve

Las rectas y los planos que pasan por el origen son los primeros ejemplos de **subespacios** que se estudian en la Unidad 1: una recta por el origen es el conjunto de múltiplos de un vector, $\operatorname{gen}\{d\}$, y un plano por el origen es $\operatorname{gen}\{u,v\}$. Pasar de la descripción con generadores (ecuaciones paramétricas) a la descripción con ecuaciones (implícitas), y al revés, es una tarea que se repite en toda la materia. En la Unidad 4 el vector normal de un plano reaparece como generador del complemento ortogonal. Esta lección repasa las ecuaciones, el producto vectorial y las posiciones relativas.

## Rectas

:::note[Definición]
La **recta** que pasa por el punto $P$ con **vector director** $d\neq0$ es el conjunto de puntos

$$
X=P+t\,d,\qquad t\in\mathbb{R}
$$

(**ecuación vectorial**). Escribiendo componente a componente se obtienen las **ecuaciones paramétricas**; en $\mathbb{R}^3$, con $P=(p_1,p_2,p_3)$ y $d=(d_1,d_2,d_3)$:

$$
\begin{cases}x=p_1+t\,d_1\\ y=p_2+t\,d_2\\ z=p_3+t\,d_3\end{cases}\qquad t\in\mathbb{R}.
$$
:::

Cualquier punto de la recta sirve como $P$ y cualquier múltiplo no nulo de $d$ sirve como director: las ecuaciones no son únicas. Si la recta pasa por $P$ y $Q$, un director es $d=Q-P$.

**En $\mathbb{R}^2$** una recta tiene además **ecuación implícita** $ax+by=c$, con $(a,b)\neq(0,0)$. El vector $(a,b)$ es **normal** (perpendicular) a la recta: si $X$ y $P$ están en la recta, $(a,b)\cdot(X-P)=c-c=0$. Por eso un director es $(-b,a)$.

**En $\mathbb{R}^3$** una sola ecuación lineal describe un plano, no una recta. Una recta se describe en forma implícita con **dos** ecuaciones lineales independientes (la intersección de dos planos). Se obtienen eliminando el parámetro $t$ de las paramétricas.

### Ejemplo 1 · Recta por dos puntos en ℝ³
<!-- check: R.T05.E1 -->

Hallamos ecuaciones de la recta $r$ que pasa por $P=(1,2,-1)$ y $Q=(3,1,1)$.

Un director es $d=Q-P=(2,-1,2)$. La ecuación vectorial y las paramétricas son

$$
X=(1,2,-1)+t\,(2,-1,2),\qquad \begin{cases}x=1+2t\\ y=2-t\\ z=-1+2t\end{cases}\quad t\in\mathbb{R}.
$$

Para las implícitas despejamos $t$ de la segunda, $t=2-y$, y reemplazamos en las otras dos: $x=1+2(2-y)$, o sea $x+2y=5$; y $z=-1+2(2-y)$, o sea $2y+z=3$. Restando estas dos ecuaciones se obtiene otra forma equivalente, más simple: $x-z=2$. Entonces

$$
r:\ \begin{cases}x+2y=5\\ x-z=2\end{cases}
$$

¿Pertenece $R=(5,0,3)$ a $r$? Cumple $5+0=5$ y $5-3=2$: sí. En las paramétricas corresponde a $t=2$.

**Comprobación.** $P$: $1+4=5$ y $1-(-1)=2$. $Q$: $3+2=5$ y $3-1=2$. El director cumple las ecuaciones homogéneas asociadas: $2+2(-1)=0$ y $2-2=0$.

## Planos

:::note[Definición]
El **plano** que pasa por $P$ con **vectores directores** $u$ y $v$ (no paralelos) es

$$
X=P+s\,u+t\,v,\qquad s,t\in\mathbb{R}
$$

(**ecuación vectorial**; las paramétricas se obtienen componente a componente). Su **ecuación implícita** o **general** es

$$
ax+by+cz=d,
$$

donde $n=(a,b,c)\neq0$ es un **vector normal** al plano y $d=n\cdot P$. Equivalentemente, $X$ está en el plano si y solo si $n\cdot(X-P)=0$.
:::

Para pasar de la ecuación vectorial a la implícita hace falta un vector perpendicular a $u$ y a $v$. En $\mathbb{R}^3$ lo da el producto vectorial.

### Producto vectorial

:::note[Definición]
Para $u=(u_1,u_2,u_3)$ y $v=(v_1,v_2,v_3)$ en $\mathbb{R}^3$, el **producto vectorial** es

$$
u\times v=(u_2v_3-u_3v_2,\ \ u_3v_1-u_1v_3,\ \ u_1v_2-u_2v_1).
$$

Como regla mnemotécnica, es el "determinante" de la matriz de filas $(e_1,e_2,e_3)$, $u$ y $v$ desarrollado por la primera fila, donde $e_1,e_2,e_3$ son los vectores canónicos.
:::

:::note[Propiedad]
Para $u,v,w\in\mathbb{R}^3$ y $c\in\mathbb{R}$:

1. $u\times v$ es ortogonal a $u$ y a $v$: $(u\times v)\cdot u=(u\times v)\cdot v=0$.
2. $v\times u=-(u\times v)$ (no es conmutativo) y $u\times u=0$.
3. $u\times(v+w)=u\times v+u\times w$ y $(cu)\times v=c\,(u\times v)$.
4. $u\times v=0$ si y solo si $u$ y $v$ son paralelos (uno es múltiplo del otro).
5. $\lVert u\times v\rVert$ es el área del paralelogramo de lados $u$ y $v$.
:::

La propiedad 1 se verifica desarrollando: $(u\times v)\cdot u=u_1u_2v_3-u_1u_3v_2+u_2u_3v_1-u_1u_2v_3+u_1u_3v_2-u_2u_3v_1=0$. El producto vectorial solo está definido en $\mathbb{R}^3$; en $\mathbb{R}^n$ el normal se obtiene resolviendo un sistema homogéneo, que es el método que se generaliza en la Unidad 4.

### Ejemplo 2 · Plano por tres puntos
<!-- check: R.T05.E2 -->

Hallamos la ecuación implícita del plano $\pi$ que pasa por $A=(1,0,1)$, $B=(2,1,0)$ y $C=(0,2,3)$.

Dos directores: $u=B-A=(1,1,-1)$ y $v=C-A=(-1,2,2)$, que no son paralelos. Un normal es

$$
n=u\times v=\big(1\cdot2-(-1)\cdot2,\ \ (-1)(-1)-1\cdot2,\ \ 1\cdot2-1\cdot(-1)\big)=(4,-1,3).
$$

Entonces $\pi:\ 4x-y+3z=d$, y como $A\in\pi$, $d=4\cdot1-0+3\cdot1=7$:

$$
\pi:\ 4x-y+3z=7 .
$$

Además, el área del triángulo $ABC$ es la mitad de la del paralelogramo: $\frac12\lVert n\rVert=\frac12\sqrt{16+1+9}=\frac{\sqrt{26}}2$.

**Comprobación.** $n\cdot u=4-1-3=0$ y $n\cdot v=-4-2+6=0$. Los tres puntos verifican la ecuación: $B$: $8-1+0=7$; $C$: $0-2+9=7$.

## Rectas y planos por el origen

Una recta o un plano **pasa por el origen** cuando se puede tomar $P=0$. Entonces:

- la recta es $\{t\,d: t\in\mathbb{R}\}=\operatorname{gen}\{d\}$, el conjunto de múltiplos de $d$;
- el plano es $\{s\,u+t\,v: s,t\in\mathbb{R}\}=\operatorname{gen}\{u,v\}$;
- las ecuaciones implícitas son **homogéneas**: $ax+by+cz=0$ para un plano, dos ecuaciones homogéneas para una recta de $\mathbb{R}^3$.

Estos conjuntos tienen tres propiedades que no tienen las rectas y los planos que no pasan por el origen: contienen al $0$, la suma de dos de sus vectores sigue en el conjunto y un múltiplo de uno de sus vectores también. Por ejemplo, si $n\cdot X=0$ y $n\cdot Y=0$, entonces $n\cdot(X+Y)=0$ y $n\cdot(cX)=0$. Esas tres propiedades definen un [subespacio](/algebra-ii/unidad-1/teoria/subespacios/). En cambio, el plano $x+y+z=1$ no contiene al origen y no es cerrado para la suma: $(1,0,0)$ y $(0,1,0)$ están en él, pero su suma $(1,1,0)$ no.

<figure class="math-figure">
<svg viewBox="-200 -145 400 260" role="img" aria-labelledby="rp-t rp-d" xmlns="http://www.w3.org/2000/svg">
<title id="rp-t">Plano por el origen con sus generadores y su vector normal</title>
<desc id="rp-d">Perspectiva caballera de los ejes x, y, z. Un trozo del plano que pasa por el origen generado por u=(1,0,0) y v=(0,2,1), cuya ecuación es -y+2z=0, dibujado como paralelogramo sombreado. Desde el origen salen u y v, contenidos en el plano, y el vector normal n=(0,-1,2), que sale del plano.</desc>
<defs><marker id="rp-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-a" d="M0 0 10 5 0 10z"/></marker><marker id="rp-arrow-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-b" d="M0 0 10 5 0 10z"/></marker><marker id="rp-arrow-c" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="head-c" d="M0 0 10 5 0 10z"/></marker></defs>
<g transform="scale(1,-1)">
<polygon class="region-a" points="66,18 -174,-102 -66,-18 174,102"/>
<line class="axis" x1="54" y1="42" x2="-81" y2="-63"/>
<line class="axis" x1="-190" y1="0" x2="190" y2="0"/>
<line class="axis" x1="0" y1="-100" x2="0" y2="135"/>
<line class="vec-a" x1="0" y1="0" x2="-27" y2="-21" marker-end="url(#rp-arrow-a)"/>
<line class="vec-b" x1="0" y1="0" x2="120" y2="60" marker-end="url(#rp-arrow-b)"/>
<line class="vec-c" x1="0" y1="0" x2="-60" y2="120" marker-end="url(#rp-arrow-c)"/>
</g>
<text class="math" x="-98" y="76">x</text>
<text class="math" x="184" y="16">y</text>
<text class="math" x="7" y="-132">z</text>
<text class="math" x="-22" y="40">u</text>
<text class="math" x="124" y="-66">v</text>
<text class="math" x="-80" y="-112">n</text>
<text class="math" x="-150" y="80">π₀</text>
</svg>
<figcaption>El plano π₀: −y+2z=0 pasa por el origen y contiene a u=(1,0,0) y v=(0,2,1); el normal n=u×v=(0,−1,2) es perpendicular a ambos. El eje x se dibuja en diagonal (perspectiva caballera), así que sobre él las longitudes y los ángulos rectos aparecen deformados: la perpendicularidad se lee en n·u=n·v=0, no en el dibujo.</figcaption>
</figure>

### Ejemplo 3 · De generadores a ecuación y de ecuación a generadores
<!-- check: R.T05.E3 -->

**(a)** Sea $\pi_0=\operatorname{gen}\{u,v\}$ con $u=(1,0,0)$ y $v=(0,2,1)$, el plano de la figura. Un normal es

$$
n=u\times v=(0\cdot1-0\cdot2,\ \ 0\cdot0-1\cdot1,\ \ 1\cdot2-0\cdot0)=(0,-1,2),
$$

y como el plano pasa por el origen, $\pi_0:\ -y+2z=0$. El punto $w=(3,4,2)$ está en $\pi_0$ porque $-4+4=0$; de hecho $w=3u+2v$. En cambio $(1,1,1)$ no está: $-1+2=1\neq0$.

**(b)** Recíprocamente, sea $\sigma:\ x-y+2z=0$. Es un sistema homogéneo de una ecuación con tres incógnitas: $x$ es principal y $y,z$ son libres. Despejando $x=y-2z$:

$$
(x,y,z)=(y-2z,\,y,\,z)=y\,(1,1,0)+z\,(-2,0,1),\qquad y,z\in\mathbb{R},
$$

así que $\sigma=\operatorname{gen}\{(1,1,0),(-2,0,1)\}$.

**Comprobación.** En (b), $(1,1,0)\times(-2,0,1)=(1\cdot1-0\cdot0,\ 0\cdot(-2)-1\cdot1,\ 1\cdot0-1\cdot(-2))=(1,-1,2)$, que es el normal de $\sigma$. En (a), $n\cdot u=0$ y $n\cdot v=-2+2=0$.

## Posiciones relativas

Con directores y normales se deciden las posiciones relativas sin resolver todo:

| Objetos | Criterio | Posiciones |
|---|---|---|
| Dos rectas (directores $d_1$, $d_2$) | ¿$d_1$ es múltiplo de $d_2$? | Si lo es: paralelas o coincidentes. Si no: en $\mathbb{R}^2$ se cortan en un punto; en $\mathbb{R}^3$ se cortan o son alabeadas (no se cortan ni son paralelas). |
| Recta (director $d$) y plano (normal $n$) | ¿$d\cdot n=0$? | Si $d\cdot n\neq0$: se cortan en un punto. Si $d\cdot n=0$: la recta es paralela al plano o está contenida en él (según un punto de la recta cumpla o no la ecuación). |
| Dos planos (normales $n_1$, $n_2$) | ¿$n_1$ es múltiplo de $n_2$? | Si lo es: paralelos o coincidentes. Si no: se cortan en una recta de director $n_1\times n_2$. |

En todos los casos, el punto o la recta de intersección se halla resolviendo el sistema formado por las ecuaciones de ambos objetos (o reemplazando las paramétricas de la recta en la ecuación del plano), y la clasificación coincide con la de [R.3](/algebra-ii/repaso/sistemas-lineales/): incompatible si no se cortan, compatible determinado si se cortan en un punto, indeterminado si se cortan en una recta o coinciden.

:::caution[Errores frecuentes]
- **Una ecuación para una recta de $\mathbb{R}^3$.** $x+2y=5$ en $\mathbb{R}^3$ es un plano (paralelo al eje $z$), no una recta.
- **Confundir normal con director.** En $\pi:\ 4x-y+3z=7$, el vector $(4,-1,3)$ es perpendicular al plano; no es un vector "dentro" del plano.
- **Directores paralelos.** $X=P+s\,(1,2,0)+t\,(2,4,0)$ no es un plano sino una recta: los dos directores son paralelos y su producto vectorial es $0$.
- **Ignorar el término independiente.** $2x-y-z=1$ y $2x-y-z=0$ tienen el mismo normal pero son planos distintos (paralelos); solo el segundo pasa por el origen y es un subespacio.
- **Orden del producto vectorial.** $u\times v=-(v\times u)$. Para hallar un normal cualquiera de los dos sirve, pero si se pide $u\times v$ el signo importa.
:::

:::tip[En resumen]
- Recta: $X=P+t\,d$. Plano: $X=P+s\,u+t\,v$ o $n\cdot(X-P)=0$, es decir $ax+by+cz=d$ con $n=(a,b,c)$.
- En $\mathbb{R}^3$ una recta en forma implícita necesita dos ecuaciones.
- $u\times v$ es perpendicular a $u$ y $v$, se anula si son paralelos y su norma es el área del paralelogramo.
- Rectas y planos por el origen: $\operatorname{gen}\{d\}$ y $\operatorname{gen}\{u,v\}$, con ecuaciones homogéneas; son los primeros ejemplos de subespacios.
- Posiciones relativas: comparar directores y normales, y resolver el sistema conjunto.
:::

## Ejercicios de repaso

### Ejercicio R.17 · Plano por un punto con normal dado
<!-- ejercicio: R.17 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallar la ecuación implícita del plano $\pi$ que pasa por $P=(2,-1,3)$ y tiene normal $n=(1,2,-2)$. Decidir si $Q=(0,0,3)$ pertenece a $\pi$ y dar una ecuación vectorial de $\pi$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Usar $n\cdot X=n\cdot P$; para la vectorial, buscar dos vectores no paralelos perpendiculares a $n$.

$n\cdot P=2-2-6=-6$, así que $\pi:\ x+2y-2z=-6$. Para $Q$: $0+0-6=-6$, de modo que $Q\in\pi$.

Un vector $(a,b,c)$ es director de $\pi$ si $a+2b-2c=0$. Por ejemplo, $(2,-1,0)$ y $(2,0,1)$, que no son paralelos. Entonces

$$
\pi:\ X=(2,-1,3)+s\,(2,-1,0)+t\,(2,0,1),\qquad s,t\in\mathbb{R}.
$$

**Comprobación.** $n\cdot(2,-1,0)=2-2+0=0$ y $n\cdot(2,0,1)=2+0-2=0$. Además $(2,-1,0)\times(2,0,1)=(-1,-2,2)=-n$, paralelo a $n$.

:::tip[Resultado]
$\pi:\ x+2y-2z=-6$; $Q\in\pi$; $X=(2,-1,3)+s\,(2,-1,0)+t\,(2,0,1)$.
:::

</details>

### Ejercicio R.18 · Producto vectorial y plano por el origen
<!-- ejercicio: R.18 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sean $u=(1,2,3)$ y $v=(0,1,-1)$. Calcular $w=u\times v$, verificar que es ortogonal a $u$ y a $v$, hallar la ecuación implícita de $\operatorname{gen}\{u,v\}$ y el área del paralelogramo de lados $u$ y $v$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Aplicar la fórmula del producto vectorial; el plano pasa por el origen, así que su ecuación es $w\cdot X=0$.

$$
w=u\times v=\big(2\cdot(-1)-3\cdot1,\ \ 3\cdot0-1\cdot(-1),\ \ 1\cdot1-2\cdot0\big)=(-5,1,1).
$$

El plano es $-5x+y+z=0$ y el área es $\lVert w\rVert=\sqrt{25+1+1}=\sqrt{27}=3\sqrt3$.

**Comprobación.** $w\cdot u=-5+2+3=0$ y $w\cdot v=0+1-1=0$.

:::tip[Resultado]
$u\times v=(-5,1,1)$; $\operatorname{gen}\{u,v\}:\ -5x+y+z=0$; área $3\sqrt3$.
:::

</details>

### Ejercicio R.19 · Recta y plano: paralelos o secantes
<!-- ejercicio: R.19 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $\pi:\ 2x-y+z=7$. Determinar la posición relativa de $\pi$ con cada una de las rectas $r:\ X=(1,0,2)+t\,(1,1,-1)$ y $s:\ X=(1,1,0)+t\,(1,2,1)$, y hallar la intersección cuando exista.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Comparar el director con el normal $n=(2,-1,1)$ y, si hace falta, reemplazar las paramétricas en la ecuación del plano.

**Recta $r$.** $d\cdot n=2-1-1=0$: $r$ es paralela a $\pi$ o está contenida. El punto $(1,0,2)$ de $r$ da $2-0+2=4\neq7$, así que $r$ es paralela a $\pi$ y no lo corta. Reemplazando las paramétricas se llega a lo mismo: $2(1+t)-t+(2-t)=4$, que nunca vale $7$.

**Recta $s$.** $d\cdot n=2-2+1=1\neq0$: se cortan en un punto. Reemplazando $x=1+t$, $y=1+2t$, $z=t$:

$$
2(1+t)-(1+2t)+t=1+t=7\iff t=6 ,
$$

y el punto es $(7,13,6)$.

**Comprobación.** $2\cdot7-13+6=7$: el punto está en $\pi$; y con $t=6$ se obtiene $(1+6,\,1+12,\,0+6)$, que está en $s$.

:::tip[Resultado]
$r$ es paralela a $\pi$ (sin puntos comunes); $s$ corta a $\pi$ en $(7,13,6)$.
:::

</details>

### Ejercicio R.20 · ¿Subespacio o no?
<!-- ejercicio: R.20 | nivel: intermedio | tipo: conceptual | verificacion: sympy -->

:::note[Enunciado]
Sea $\pi=\{s\,(1,0,2)+t\,(0,1,-1): s,t\in\mathbb{R}\}$.

1. Hallar una ecuación implícita de $\pi$.
2. Decidir si la recta $\operatorname{gen}\{(1,1,1)\}$ está contenida en $\pi$.
3. Explicar por qué $\pi'=\{(x,y,z)\in\mathbb{R}^3: 2x-y-z=1\}$ no es cerrado para la suma, dando dos puntos concretos de $\pi'$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El normal sale del producto vectorial de los generadores. Una recta por el origen está contenida en un plano por el origen si su director lo está.

1. $(1,0,2)\times(0,1,-1)=\big(0\cdot(-1)-2\cdot1,\ \ 2\cdot0-1\cdot(-1),\ \ 1\cdot1-0\cdot0\big)=(-2,1,1)$. Como $\pi$ pasa por el origen, $\pi:\ -2x+y+z=0$, o bien $2x-y-z=0$.
2. $(1,1,1)$ cumple $2-1-1=0$, así que está en $\pi$, y todos sus múltiplos también (la ecuación es homogénea). La recta está contenida en $\pi$. Explícitamente, $(1,1,1)=1\cdot(1,0,2)+1\cdot(0,1,-1)$.
3. $(1,1,0)$ y $(1,0,1)$ están en $\pi'$, porque $2-1-0=1$ y $2-0-1=1$. Su suma $(2,1,1)$ da $4-1-1=2\neq1$: no está en $\pi'$. El motivo general: si $2x-y-z=1$ para dos puntos, su suma da $1+1=2$. Además $(0,0,0)\notin\pi'$.

**Comprobación.** El normal $(-2,1,1)$ es ortogonal a ambos generadores: $-2+0+2=0$ y $0+1-1=0$.

:::tip[Resultado]
$\pi:\ 2x-y-z=0$; $\operatorname{gen}\{(1,1,1)\}\subseteq\pi$; $\pi'$ no es cerrado para la suma (ni contiene al origen), así que no es un subespacio.
:::

</details>

## Dónde se usa en Álgebra II

- Rectas y planos por el origen como subespacios de $\mathbb{R}^2$ y $\mathbb{R}^3$: [subespacios](/algebra-ii/unidad-1/teoria/subespacios/) y [combinaciones lineales](/algebra-ii/unidad-1/teoria/combinaciones-lineales/).
- Pasar de generadores a ecuaciones y al revés: [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/).
- Núcleo e imagen de transformaciones de $\mathbb{R}^3$, que suelen ser rectas o planos por el origen: [núcleo e imagen](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/).
- Autoespacios en $\mathbb{R}^3$ (rectas o planos de vectores invariantes): [autovalores y autovectores](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/).
- El normal genera el complemento ortogonal de un plano por el origen: [complemento ortogonal](/algebra-ii/unidad-4/teoria/complemento-ortogonal/) y [proyección y distancia](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/).

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 1.3 (rectas y planos) y sección 1.2 (longitud y ángulo: el producto punto).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de ecuaciones lineales (descripción paramétrica de conjuntos solución).
- Lección anterior: [R.4 Polinomios](/algebra-ii/repaso/polinomios/). Volver a la [presentación del repaso](/algebra-ii/repaso/).
