---
title: Clasificación de transformaciones lineales
description: Monomorfismos, epimorfismos e isomorfismos; cómo se reconocen con el núcleo y la imagen, qué dicen las dimensiones y por qué todo espacio de dimensión n es isomorfo a K^n.
slug: algebra-ii/unidad-2/teoria/clasificacion
sidebar:
  order: 4
  label: 2.4 Clasificación
---

## Para qué sirve

Una TL $T:V\to W$ puede perder información (si aplasta vectores distintos sobre el mismo), puede no llegar a todo $W$, o puede hacer ambas cosas. Clasificar $T$ es decidir cuál de esas situaciones ocurre. Importa por razones muy concretas:

- **Codificar** un mensaje es útil solo si mensajes distintos dan palabras distintas: la TL de codificación tiene que ser inyectiva.
- **Cambiar de representación** (de polinomios a ternas de números, de matrices a columnas) sin perder nada exige que la TL sea biyectiva: un isomorfismo.
- **Resolver $T(v)=w$** para todo $w$ exige que $T$ sea sobreyectiva, y para que la solución sea única, inyectiva.

Con el [núcleo y la imagen](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/) y el [teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/), la clasificación se reduce a calcular dos dimensiones.

## Definiciones

:::note[Definición]
Sea $T:V\to W$ una TL.

- $T$ es un **monomorfismo** si es inyectiva: $T(u)=T(v)\Rightarrow u=v$.
- $T$ es un **epimorfismo** si es sobreyectiva: $\operatorname{Im}(T)=W$.
- $T$ es un **isomorfismo** si es monomorfismo y epimorfismo (es decir, biyectiva). Si existe un isomorfismo $T:V\to W$, decimos que $V$ y $W$ son **isomorfos**.
- Un **endomorfismo** es una TL de un espacio en sí mismo, $T:V\to V$. Un endomorfismo que es isomorfismo se llama **automorfismo**.
:::

En todo lo que sigue $V$ y $W$ tienen dimensión finita.

## Los criterios con núcleo e imagen

:::note[Teorema · Caracterización de monomorfismos y epimorfismos]
Sea $T:V\to W$ una TL.

1. $T$ es monomorfismo si y solo si $\operatorname{Nu}(T)=\{0_V\}$.
2. $T$ es epimorfismo si y solo si $\dim\operatorname{Im}(T)=\dim W$.
:::

**Demostración.**

1. ($\Rightarrow$) Si $v\in\operatorname{Nu}(T)$, entonces $T(v)=0_W=T(0_V)$; por inyectividad, $v=0_V$. ($\Leftarrow$) Si $T(u)=T(v)$, entonces $T(u-v)=T(u)-T(v)=0_W$, así que $u-v\in\operatorname{Nu}(T)=\{0_V\}$ y $u=v$.
2. ($\Rightarrow$) Si $\operatorname{Im}(T)=W$, las dimensiones coinciden. ($\Leftarrow$) $\operatorname{Im}(T)$ es un subespacio de $W$ con la misma dimensión que $W$ (que es finita); un subespacio de un espacio de dimensión finita con igual dimensión es todo el espacio. Luego $\operatorname{Im}(T)=W$. $\blacksquare$

El punto 1 es una comodidad enorme: para saber si $T$ distingue vectores distintos no hay que comparar pares; alcanza con resolver **un** sistema homogéneo. Es una propiedad de las TL, no de las funciones en general: $f(x)=x^2$ cumple $f(x)=0\Rightarrow x=0$ y sin embargo no es inyectiva, porque no es lineal.

## Consecuencias para las dimensiones

Por el teorema de la dimensión, $\dim V=\dim\operatorname{Nu}(T)+\dim\operatorname{Im}(T)$. De ahí salen las tres restricciones siguientes.

:::note[Propiedad · Dimensiones y clasificación]
Sea $T:V\to W$ una TL.

- Si $T$ es monomorfismo, $\dim V=\dim\operatorname{Im}(T)\le\dim W$. En particular, **no hay monomorfismos hacia un espacio de menor dimensión**.
- Si $T$ es epimorfismo, $\dim V=\dim\operatorname{Nu}(T)+\dim W\ge\dim W$. En particular, **no hay epimorfismos desde un espacio de menor dimensión**.
- Si $T$ es isomorfismo, $\dim V=\dim W$.
:::

Y cuando las dimensiones coinciden, las tres propiedades son equivalentes.

:::note[Teorema · Igual dimensión]
Si $\dim V=\dim W=n$ y $T:V\to W$ es una TL, entonces

$$
T\text{ es monomorfismo}\iff T\text{ es epimorfismo}\iff T\text{ es isomorfismo}.
$$
:::

**Demostración.** Si $T$ es mono, $\operatorname{Nu}(T)=\{0_V\}$ y por el teorema de la dimensión $\dim\operatorname{Im}(T)=n=\dim W$: $T$ es epi. Si $T$ es epi, $\dim\operatorname{Im}(T)=n$ y entonces $\dim\operatorname{Nu}(T)=n-n=0$: $T$ es mono. Como "isomorfismo" significa mono y epi a la vez, las tres afirmaciones son equivalentes. $\blacksquare$

Para un endomorfismo $T:V\to V$ esto es lo que más se usa: **basta comprobar una sola de las dos condiciones**. Es el análogo de que una matriz cuadrada con columnas LI es inversible. Fuera del caso de igual dimensión, la equivalencia es falsa: $T:\mathbb{R}\to\mathbb{R}^2$, $T(t)=(t,0)$ es mono y no epi; $S:\mathbb{R}^2\to\mathbb{R}$, $S(x,y)=x$ es epi y no mono.

## Qué hacen con los conjuntos de vectores

:::note[Propiedad · Imágenes de conjuntos LI y de generadores]
Sea $T:V\to W$ una TL.

1. Si $T$ es monomorfismo y $\{v_1,\dots,v_k\}\subseteq V$ es LI, entonces $\{T(v_1),\dots,T(v_k)\}$ es LI.
2. Si $T$ es epimorfismo y $V=\operatorname{gen}\{v_1,\dots,v_k\}$, entonces $W=\operatorname{gen}\{T(v_1),\dots,T(v_k)\}$.
3. Si $T$ es isomorfismo y $B$ es una base de $V$, entonces $T(B)$ es una base de $W$.
:::

**Demostración.**

1. Supongamos $c_1T(v_1)+\cdots+c_kT(v_k)=0_W$. Por linealidad, $T(c_1v_1+\cdots+c_kv_k)=0_W$, o sea $c_1v_1+\cdots+c_kv_k\in\operatorname{Nu}(T)=\{0_V\}$. Como los $v_i$ son LI, todos los $c_i$ son $0$.
2. Es la propiedad de la imagen de un generador de [2.2](/algebra-ii/unidad-2/teoria/nucleo-e-imagen/) con $\operatorname{Im}(T)=W$.
3. Es la unión de 1 y 2: $T(B)$ es LI y generador. $\blacksquare$

La recíproca de 3 también vale: si $T$ lleva **una** base de $V$ en una base de $W$, entonces $T$ es isomorfismo (la imagen está generada por $T(B)$, que es $W$, y las dimensiones coinciden, así que $T$ es epi entre espacios de igual dimensión). Y vale una caracterización más: $T$ es mono si y solo si transforma conjuntos LI en conjuntos LI. Lo que **no** conserva un monomorfismo es la sobreyectividad ni, en general, la forma: la imagen de $\mathbb{R}^2$ por un mono a $\mathbb{R}^5$ es un plano de $\mathbb{R}^5$.

### Ejemplo 1 · Ni mono ni epi
<!-- check: U2.T04.E1 -->

Clasificar $T:\mathbb{R}^3\to\mathbb{R}^3$, $T(x,y,z)=(x+y,\ y+z,\ x+2y+z)$.

**Núcleo.** $T(x,y,z)=0$ equivale a $x+y=0$, $y+z=0$ (la tercera ecuación es la suma de las dos primeras, así que no agrega nada). Entonces $y=-x$, $z=-y=x$:

$$
\operatorname{Nu}(T)=\{(x,-x,x)\}=\operatorname{gen}\{(1,-1,1)\},\qquad\dim\operatorname{Nu}(T)=1.
$$

Como $\operatorname{Nu}(T)\neq\{0\}$, **$T$ no es monomorfismo**. Corroboramos: $T(1,-1,1)=(0,\ 0,\ 1-2+1)=(0,0,0)$.

**Imagen.** Por el teorema de la dimensión, $\dim\operatorname{Im}(T)=3-1=2<3=\dim\mathbb{R}^3$, así que **$T$ no es epimorfismo**. Podemos describirla: los transformados de la base canónica son $T(e_1)=(1,0,1)$, $T(e_2)=(1,1,2)$, $T(e_3)=(0,1,1)$, con $T(e_2)=T(e_1)+T(e_3)$. Una base de la imagen es $\{(1,0,1),(0,1,1)\}$ y

$$
\operatorname{Im}(T)=\{(a,b,c):\ c=a+b\}.
$$

**Conclusión.** $T$ no es mono, no es epi y no es isomorfismo. Con $\dim V=\dim W$, el teorema de igual dimensión dice que las dos fallas ocurren juntas: no podía fallar una sola.

### Ejemplo 2 · Una familia de endomorfismos de matrices
<!-- check: U2.T04.E2 -->

Para $k\in\mathbb{R}$ sea $T_k:\mathbb{R}^{2\times 2}\to\mathbb{R}^{2\times 2}$, $T_k(A)=A+kA^t$ (es lineal porque la transposición lo es). Hallar los valores de $k$ para los cuales $T_k$ es un automorfismo.

Como $T_k$ es un endomorfismo, alcanza con decidir cuándo es mono, o sea cuándo $\operatorname{Nu}(T_k)=\{0\}$.

**Núcleo.** $T_k(A)=0$ significa $A=-kA^t$. Transponiendo, $A^t=-kA$; sustituyendo en la primera igualdad,

$$
A=-k\,(-kA)=k^2A\quad\Longrightarrow\quad(1-k^2)A=0.
$$

- Si $k\neq 1$ y $k\neq-1$, entonces $1-k^2\neq 0$ y $A=0$: $\operatorname{Nu}(T_k)=\{0\}$.
- Si $k=1$, la condición es $A=-A^t$: el núcleo es el subespacio de las matrices antisimétricas, que no es trivial (por ejemplo, $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$).
- Si $k=-1$, la condición es $A=A^t$: el núcleo es el de las matrices simétricas, de dimensión 3.

**Conclusión.** $T_k$ es automorfismo si y solo si $k\neq 1$ y $k\neq -1$.

**Comprobación con la matriz.** En la base canónica $\{E_{11},E_{12},E_{21},E_{22}\}$ tenemos $T_k(E_{11})=(1+k)E_{11}$, $T_k(E_{12})=E_{12}+kE_{21}$, $T_k(E_{21})=kE_{12}+E_{21}$ y $T_k(E_{22})=(1+k)E_{22}$. Poniendo las coordenadas en columnas,

$$
\begin{pmatrix}1+k&0&0&0\\0&1&k&0\\0&k&1&0\\0&0&0&1+k\end{pmatrix},\qquad\det=(1+k)^2(1-k^2)=(1+k)^3(1-k),
$$

que se anula exactamente para $k=-1$ y $k=1$. Para $k=2$, por ejemplo, el determinante vale $27\cdot(-1)=-27\neq0$. (Veremos en [2.6](/algebra-ii/unidad-2/teoria/matriz-asociada/) por qué el determinante de esta matriz decide la pregunta.)

### Ejemplo 3 · Codificar es un monomorfismo
<!-- check: U2.T04.E3 -->

En $\mathbb{Z}_2$, sea $G=\begin{pmatrix}1&0&1&1&0\\0&1&0&1&1\end{pmatrix}$ y $T:\mathbb{Z}_2^2\to\mathbb{Z}_2^5$, $T(a)=aG$, con $a$ fila (la codificación de [2.1](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/)). Clasificar $T$.

**Núcleo.** $aG=a_1(1,0,1,1,0)+a_2(0,1,0,1,1)=(a_1,\ a_2,\ a_1,\ a_1+a_2,\ a_2)$. Esto es $(0,0,0,0,0)$ si y solo si $a_1=a_2=0$ (las filas de $G$ son LI: sus dos primeras coordenadas forman la matriz identidad). Entonces $\operatorname{Nu}(T)=\{0\}$ y **$T$ es monomorfismo**.

**Imagen.** $\dim\operatorname{Im}(T)=2<5=\dim\mathbb{Z}_2^5$, así que no es epimorfismo. No hay forma de que lo sea: un epimorfismo no puede salir de un espacio de menor dimensión.

**Lectura.** Los cuatro mensajes producen palabras distintas:

$$
00\mapsto 00000,\quad 10\mapsto 10110,\quad 01\mapsto 01011,\quad 11\mapsto 11101.
$$

La imagen es un subespacio de $\mathbb{Z}_2^5$ con cuatro elementos, el código lineal $(5,2)$. Que $T$ sea mono garantiza que se puede decodificar sin ambigüedad cuando no hubo errores; que no sea epi es justamente lo que deja "lugar" para detectar errores (las otras 28 palabras de $\mathbb{Z}_2^5$ no son palabras código).

## Coordenadas: todo espacio de dimensión n es isomorfo a Kⁿ

:::note[Teorema · Las coordenadas son un isomorfismo]
Sea $V$ un espacio de dimensión $n$ sobre $K$ y $B=\{b_1,\dots,b_n\}$ una base. La función

$$
\Phi_B:V\to K^n,\qquad\Phi_B(v)=[v]_B
$$

es un isomorfismo.
:::

**Demostración.** *Lineal.* Si $u=\sum a_ib_i$ y $v=\sum c_ib_i$, entonces $u+v=\sum(a_i+c_i)b_i$ y, por la unicidad de las coordenadas, $[u+v]_B=[u]_B+[v]_B$. Del mismo modo $\lambda v=\sum(\lambda c_i)b_i$ da $[\lambda v]_B=\lambda[v]_B$.
*Mono.* $[v]_B=0$ significa $v=0\,b_1+\cdots+0\,b_n=0_V$.
*Epi.* Dado $c=(c_1,\dots,c_n)\in K^n$, el vector $v=c_1b_1+\cdots+c_nb_n$ cumple $[v]_B=c$. $\blacksquare$

De ahí sale el resultado de clasificación de los espacios de dimensión finita.

:::note[Teorema · Isomorfos si y solo si igual dimensión]
Dos espacios vectoriales $V$ y $W$ sobre el mismo cuerpo $K$, de dimensión finita, son isomorfos si y solo si $\dim V=\dim W$.
:::

**Demostración.** ($\Rightarrow$) Un isomorfismo cumple $\dim V=\dim W$ por la propiedad de dimensiones. ($\Leftarrow$) Sean $B$ una base de $V$ y $B'$ una base de $W$, ambas con $n$ elementos. Por el [teorema fundamental](/algebra-ii/unidad-2/teoria/teorema-fundamental/) de la próxima lección existe una TL $T:V\to W$ con $T(b_i)=b_i'$; lleva una base en una base y por lo tanto es isomorfismo. (Otra manera: componer $\Phi_B$ con la inversa de $\Phi_{B'}$; la inversa de un isomorfismo es lineal, como se prueba en [2.8](/algebra-ii/unidad-2/teoria/composicion-e-inversa/).) $\blacksquare$

Consecuencias: $P_2[\mathbb{R}]$ y $\mathbb{R}^3$ son isomorfos; $\mathbb{R}^{2\times 2}$ y $\mathbb{R}^4$ también; $P_2[\mathbb{R}]$ y $\mathbb{R}^{2\times 2}$ no lo son. Los isomorfismos preservan toda la estructura de espacio vectorial: independencia, generadores, bases, dimensiones de subespacios. Por eso se puede **traducir cualquier pregunta de dependencia lineal en $V$ a una pregunta sobre columnas en $K^n$** escalonando.

### Ejemplo 4 · Polinomios como ternas
<!-- check: U2.T04.E4 -->

En $P_2[\mathbb{R}]$ sea la base $B=\{1,\ 1+x,\ 1+x+x^2\}$. (a) Hallar $[3+2x-x^2]_B$. (b) Decidir si $\{1+x,\ x-x^2,\ 1+3x-2x^2\}$ es LI.

**(a)** Buscamos $c_1,c_2,c_3$ con $c_1+c_2(1+x)+c_3(1+x+x^2)=3+2x-x^2$. Igualando coeficientes de $x^2$, $x$ y $1$:

$$
c_3=-1,\qquad c_2+c_3=2\Rightarrow c_2=3,\qquad c_1+c_2+c_3=3\Rightarrow c_1=1.
$$

Entonces $[3+2x-x^2]_B=(1,3,-1)$. Comprobación: $1+3(1+x)-(1+x+x^2)=3+2x-x^2$. Con $\Phi_B$ esto es la función "polinomio $\mapsto$ terna"; su inversa reconstruye el polinomio desde la terna.

**(b)** Pasamos los tres polinomios a coordenadas en la base canónica $\{1,x,x^2\}$: $(1,1,0)$, $(0,1,-1)$ y $(1,3,-2)$. Como $\Phi$ es isomorfismo, los polinomios son LI si y solo si estas ternas lo son. Se ve que $(1,1,0)+2(0,1,-1)=(1,3,-2)$, así que son **LD**: la misma relación vale entre los polinomios,

$$
(1+x)+2(x-x^2)=1+3x-2x^2.
$$

:::caution[Errores frecuentes]
- **Creer que "misma dimensión" implica isomorfismo.** Que $V$ y $W$ sean isomorfos no significa que *toda* TL entre ellos lo sea: $T(x,y)=(x,0)$ va de $\mathbb{R}^2$ en $\mathbb{R}^2$ y no es mono ni epi. Hay que mirar la TL, no solo las dimensiones.
- **Mirar solo las imágenes de la base.** Que $T(e_1),\dots,T(e_n)$ sean no nulos no alcanza para el monomorfismo. En el ejemplo 1, los tres transformados de la base canónica son no nulos y $T$ no es mono. Hay que ver si son **LI**.
- **Pensar que mono implica epi (o al revés) sin igualdad de dimensiones.** El teorema de igual dimensión no vale en general: $t\mapsto(t,0)$ es mono y no epi.
- **Dar por cierto "$\operatorname{Nu}(T)=\{0\}$" por ser la única solución visible.** El núcleo se determina resolviendo $T(v)=0_W$ completo; en el ejemplo 2, olvidar $k=-1$ (núcleo = simétricas) da un resultado falso.
- **Confundir isomorfo con igual.** $P_2[\mathbb{R}]$ y $\mathbb{R}^3$ son isomorfos, pero un polinomio no es una terna: el isomorfismo depende de la base elegida.
:::

## Autoevaluación

<details>
<summary>1. ¿Existe un monomorfismo $T:\mathbb{R}^4\to\mathbb{R}^3$? ¿Y un epimorfismo?</summary>

Mono no: exigiría $4=\dim\operatorname{Im}(T)\le 3$. Epi sí: por ejemplo $T(x_1,x_2,x_3,x_4)=(x_1,x_2,x_3)$; su núcleo es $\operatorname{gen}\{e_4\}$ y $4=1+3$.

</details>

<details>
<summary>2. Si $T:V\to V$ cumple $T(T(v))=0_V$ para todo $v$ y $V\neq\{0\}$, ¿puede ser automorfismo?</summary>

No. Si lo fuera, sería mono, y $T(T(v))=0$ implicaría $T(v)=0$ y luego $v=0$ para todo $v$, o sea $V=\{0\}$.

</details>

<details>
<summary>3. ¿Son isomorfos $\mathbb{R}^{2\times 3}$ y $P_5[\mathbb{R}]$?</summary>

Sí: ambos tienen dimensión 6. Un isomorfismo es $\begin{pmatrix}a&b&c\\d&e&f\end{pmatrix}\mapsto a+bx+cx^2+dx^3+ex^4+fx^5$.

</details>

:::tip[En resumen]
- $T$ es mono $\iff\operatorname{Nu}(T)=\{0\}$; es epi $\iff\dim\operatorname{Im}(T)=\dim W$; es iso si es ambas.
- Mono exige $\dim V\le\dim W$; epi exige $\dim V\ge\dim W$; iso exige igualdad.
- Si $\dim V=\dim W$: mono $\iff$ epi $\iff$ iso. Para endomorfismos basta una condición.
- Un mono conserva la independencia lineal; un epi conserva los generadores; un iso lleva bases en bases.
- $V\cong W\iff\dim V=\dim W$; las coordenadas $v\mapsto[v]_B$ son un isomorfismo $V\to K^n$.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: secciones 6.4 (p. 490) a 6.5 (p. 499), sobre transformaciones uno a uno, sobre e isomorfismos. Poole usa "uno a uno" y "sobre".
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: las secciones sobre transformaciones lineales y sobre espacios vectoriales isomorfos a $\mathbb{R}^n$ mediante coordenadas.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed.: sección 5.4, "Aplicaciones lineales inyectivas y suprayectivas" (p. 195).
- Antes: [2.3 Teorema de la dimensión](/algebra-ii/unidad-2/teoria/teorema-de-la-dimension/) y [coordenadas](/algebra-ii/unidad-1/teoria/coordenadas/).
- Después: [2.5 Teorema fundamental](/algebra-ii/unidad-2/teoria/teorema-fundamental/).
