---
title: Espacios vectoriales
description: Definición de espacio vectorial con sus diez axiomas, ejemplos en ℝⁿ, ℤ₂ⁿ, matrices, polinomios y funciones, no ejemplos y propiedades elementales demostradas.
slug: algebra-ii/unidad-1/teoria/espacios-vectoriales
sidebar:
  order: 2
  label: 1.2 Espacios vectoriales
---

## Para qué sirve

En Álgebra I trabajamos con vectores de $\mathbb{R}^2$ y $\mathbb{R}^3$, con matrices y con polinomios, y en
cada caso aprendimos a sumar y a multiplicar por números. Las cuentas se parecen mucho: sumar dos
matrices $2\times 2$ es sumar cuatro números en paralelo, igual que sumar dos vectores de $\mathbb{R}^4$;
sumar dos polinomios de grado a lo sumo $2$ es sumar sus tres coeficientes. Lo mismo ocurre con objetos
propios de la informática:

- una **señal** muestreada en $n$ instantes (audio, una serie de mediciones de un sensor) es una lista
  de $n$ números reales; mezclar dos señales o amplificar una son sumas y productos por escalares;
- una **imagen** en escala de grises de $m\times n$ píxeles es una matriz real $m\times n$; superponer dos
  imágenes o cambiar el contraste son operaciones del mismo tipo;
- una **palabra de $n$ bits** es una $n$-upla de $\mathbb{Z}_2$; el XOR bit a bit es una suma.

Un **espacio vectorial** es la estructura común a todos estos ejemplos. Lo que probemos una vez a partir
de los axiomas (propiedades, criterios de subespacio, bases, coordenadas) vale automáticamente para
todos ellos, incluidos los que todavía no conocemos.

## Definición

Un espacio vectorial tiene cuatro componentes: un conjunto $V$ de **vectores**, un cuerpo $K$ de
**escalares** (ver [cuerpos y ℤ₂](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/)), una **suma** de vectores y
un **producto por escalar**, que a cada $\lambda\in K$ y $v\in V$ le asigna un elemento $\lambda v$.

:::note[Definición (espacio vectorial)]
Sean $V$ un conjunto no vacío y $K$ un cuerpo. Decimos que $(V,+,K,\cdot)$ es un **espacio vectorial
sobre $K$** si, para todos $u,v,w\in V$ y todos $\lambda,\mu\in K$:

**Suma de vectores, $(V,+)$**

1. Cierre: $u+v\in V$.
2. Asociativa: $(u+v)+w=u+(v+w)$.
3. Neutro: existe un elemento $0_V\in V$ tal que $v+0_V=v$ para todo $v\in V$.
4. Opuesto: para cada $v\in V$ existe $-v\in V$ tal que $v+(-v)=0_V$.
5. Conmutativa: $u+v=v+u$.

**Producto por escalar**

6. Cierre: $\lambda v\in V$.
7. Neutro del cuerpo: $1\cdot v=v$.
8. Asociativa mixta: $(\lambda\mu)v=\lambda(\mu v)$.
9. Distributiva respecto de la suma de vectores: $\lambda(u+v)=\lambda u+\lambda v$.
10. Distributiva respecto de la suma de escalares: $(\lambda+\mu)v=\lambda v+\mu v$.
:::

Algunas aclaraciones de lectura:

- En los axiomas aparecen **dos sumas distintas**: en el 10, $\lambda+\mu$ es una suma en $K$ y
  $\lambda v+\mu v$ es una suma en $V$. También hay dos productos: $\lambda\mu$ en el axioma 8 es el
  producto del cuerpo. Usamos los mismos símbolos porque el contexto indica cuál es cuál.
- Cuando $K=\mathbb{R}$ hablamos de **espacio vectorial real**; cuando $K=\mathbb{Z}_2$, de espacio
  vectorial sobre $\mathbb{Z}_2$. Si las operaciones son las usuales, escribimos solo $V$.
- Los axiomas de cierre (1 y 6) suelen darse por sentados cuando se dice "una operación en $V$", pero
  conviene escribirlos: es el lugar donde fallan casi todos los no ejemplos.
- La resta se define como $u-v=u+(-v)$.

## Ejemplos

### Las $n$-uplas: $\mathbb{R}^n$ y $\mathbb{Z}_2^n$

Para un cuerpo $K$, el conjunto $K^n=\{(x_1,\dots,x_n): x_i\in K\}$ con las operaciones componente a
componente,

$$
(x_1,\dots,x_n)+(y_1,\dots,y_n)=(x_1+y_1,\dots,x_n+y_n),\qquad \lambda(x_1,\dots,x_n)=(\lambda x_1,\dots,\lambda x_n),
$$

es un espacio vectorial sobre $K$. Cada axioma se reduce a la propiedad correspondiente del cuerpo,
aplicada en cada componente. El neutro es $0_V=(0,\dots,0)$ y el opuesto de $(x_1,\dots,x_n)$ es
$(-x_1,\dots,-x_n)$.

- Con $K=\mathbb{R}$ obtenemos $\mathbb{R}^n$, el espacio de Álgebra I.
- Con $K=\mathbb{Z}_2$ obtenemos $\mathbb{Z}_2^n$, el espacio de las **palabras binarias de longitud $n$**.
  Cada componente puede valer $0$ o $1$ de manera independiente, así que $\mathbb{Z}_2^n$ tiene
  exactamente $2^n$ elementos: $4$ en $\mathbb{Z}_2^2$, $8$ en $\mathbb{Z}_2^3$, $256$ en $\mathbb{Z}_2^8$ (los
  bytes). La suma es el XOR bit a bit. Solo hay dos escalares: $0\cdot v=(0,\dots,0)$ y $1\cdot v=v$.

Por ejemplo, $\mathbb{Z}_2^2=\{(0,0),(1,0),(0,1),(1,1)\}$, y en él $(1,0)+(1,1)=(0,1)$.

### Matrices: $\mathbb{R}^{m\times n}$

El conjunto $\mathbb{R}^{m\times n}$ de las matrices reales de $m$ filas y $n$ columnas, con la suma
entrada por entrada y el producto de un número por una matriz, es un espacio vectorial real. El neutro es
la matriz nula y el opuesto de $A$ es $-A$. Es "como $\mathbb{R}^{mn}$ con las entradas ordenadas en un
rectángulo". Del mismo modo, $\mathbb{Z}_2^{m\times n}$ (matrices de ceros y unos operadas módulo $2$) es un
espacio vectorial sobre $\mathbb{Z}_2$ con $2^{mn}$ elementos.

### Polinomios: $P_n[\mathbb{R}]$

$P_n[\mathbb{R}]$ es el conjunto de los polinomios en la variable $x$, con coeficientes reales, de grado
menor o igual que $n$, **junto con el polinomio nulo** (que no tiene grado). Con la suma de polinomios y
el producto de un número por un polinomio es un espacio vectorial real:

$$
(a_0+a_1x+\dots+a_nx^n)+(b_0+b_1x+\dots+b_nx^n)=(a_0+b_0)+(a_1+b_1)x+\dots+(a_n+b_n)x^n .
$$

La suma de dos polinomios de grado a lo sumo $n$ tiene grado a lo sumo $n$ o es el polinomio nulo, así
que vale el cierre. El neutro es el polinomio nulo y el opuesto de $p$ es $-p$, con todos los
coeficientes cambiados de signo.

### Funciones

Sea $X$ un conjunto cualquiera y $\mathcal{F}(X,\mathbb{R})$ el conjunto de todas las funciones
$f:X\to\mathbb{R}$. Definimos las operaciones **punto a punto**:

$$
(f+g)(t)=f(t)+g(t),\qquad (\lambda f)(t)=\lambda\,f(t)\qquad\text{para todo } t\in X .
$$

Con ellas, $\mathcal{F}(X,\mathbb{R})$ es un espacio vectorial real: cada axioma es una igualdad de
funciones que se verifica evaluando en cada $t$ y usando la propiedad correspondiente de $\mathbb{R}$. El
neutro es la función nula, $t\mapsto 0$, y el opuesto de $f$ es $t\mapsto -f(t)$. Si $X=\{1,2,\dots,n\}$,
una función $f:X\to\mathbb{R}$ es lo mismo que la lista $(f(1),\dots,f(n))$: recuperamos $\mathbb{R}^n$,
que es exactamente la forma en que se almacena una señal muestreada.

### El espacio nulo

$V=\{0_V\}$, con $0_V+0_V=0_V$ y $\lambda 0_V=0_V$, cumple los diez axiomas. Es el espacio vectorial más
chico posible.

### Ejemplo 1 · Paridad de bloques en ℤ₂⁴
<!-- check: U1.T02.E1 -->

Un sistema de almacenamiento guarda tres bloques de datos de 4 bits, $d_1=(1,0,1,1)$, $d_2=(0,1,1,0)$ y
$d_3=(1,1,0,0)$, y un **bloque de paridad** $p=d_1+d_2+d_3$ calculado en $\mathbb{Z}_2^4$. Calcular $p$ y
mostrar cómo se recupera $d_2$ si ese bloque se pierde.

**Cálculo de $p$.** Sumamos componente a componente en $\mathbb{Z}_2$:

$$
p=(1+0+1,\;0+1+1,\;1+1+0,\;1+0+0)=(0,0,0,1).
$$

**Recuperación.** Sumamos $d_1$ y $d_3$ a $p$. Por las propiedades asociativa y conmutativa,

$$
p+d_1+d_3=(d_1+d_1)+d_2+(d_3+d_3)=0_V+d_2+0_V=d_2 ,
$$

porque en cada componente $a+a=0$ en $\mathbb{Z}_2$. Con los datos:

$$
p+d_1+d_3=(0+1+1,\;0+0+1,\;0+1+0,\;1+1+0)=(0,1,1,0)=d_2 .
$$

Comprobación: el resultado coincide con el bloque original. Este es el mecanismo de los arreglos de
discos con paridad (como RAID 5): el bloque perdido es la suma de todos los demás, porque en
$\mathbb{Z}_2^n$ cada vector es su propio opuesto. Cualquier bloque, no solo $d_2$, se recupera de la
misma manera.

## "Vector" no quiere decir flecha

En Física y en Álgebra I un vector se dibuja como una flecha. En esta materia, **vector** significa
simplemente **elemento de un espacio vectorial**: un polinomio, una matriz, una función o una palabra
binaria son vectores cuando se los considera como elementos de $P_n[\mathbb{R}]$, $\mathbb{R}^{m\times n}$,
$\mathcal{F}(X,\mathbb{R})$ o $\mathbb{Z}_2^n$. Las flechas son una representación útil de $\mathbb{R}^2$ y
$\mathbb{R}^3$, nada más; en $\mathbb{Z}_2^n$ no hay ninguna flecha que dibujar. Lo que hace que algo sea un
vector no es su aspecto sino el hecho de que se pueda sumar con otros elementos del mismo conjunto y
multiplicar por escalares cumpliendo los diez axiomas.

Una consecuencia práctica: el mismo conjunto puede ser o no ser espacio vectorial según qué operaciones
se usen, y el elemento neutro no tiene por qué "parecerse a un cero". Los dos ejemplos siguientes lo
muestran.

### Ejemplo 2 · Un espacio vectorial con operaciones no usuales
<!-- check: U1.T02.E2 -->

En $V=\mathbb{R}$ con $K=\mathbb{R}$ definimos

$$
x\oplus y=x+y-1,\qquad \lambda\odot x=\lambda x-\lambda+1 .
$$

Probar que $(\mathbb{R},\oplus,\mathbb{R},\odot)$ es un espacio vectorial, hallar su vector nulo y el opuesto
de cada $x$, y calcular $(3\odot 5)\oplus\big((-2)\odot 4\big)$.

**Neutro.** Buscamos $e$ con $x\oplus e=x$ para todo $x$: $x+e-1=x$ da $e=1$. El vector nulo es el
**número $1$**: $0_V=1$.

**Opuesto.** Buscamos $y$ con $x\oplus y=1$: $x+y-1=1$ da $y=2-x$.

**Axiomas restantes.** Los cierres son inmediatos (las fórmulas dan números reales). Conmutativa:
$x\oplus y=x+y-1=y\oplus x$. Asociativa: $(x\oplus y)\oplus z=(x+y-1)+z-1=x+y+z-2$, y lo mismo da
$x\oplus(y\oplus z)$. Para los axiomas del producto:

- $1\odot x=x-1+1=x$.
- $(\lambda\mu)\odot x=\lambda\mu x-\lambda\mu+1$, y
  $\lambda\odot(\mu\odot x)=\lambda(\mu x-\mu+1)-\lambda+1=\lambda\mu x-\lambda\mu+1$.
- $\lambda\odot(x\oplus y)=\lambda(x+y-1)-\lambda+1=\lambda x+\lambda y-2\lambda+1$, y
  $(\lambda\odot x)\oplus(\lambda\odot y)=(\lambda x-\lambda+1)+(\lambda y-\lambda+1)-1$, que es lo mismo.
- $(\lambda+\mu)\odot x=(\lambda+\mu)x-(\lambda+\mu)+1$, y
  $(\lambda\odot x)\oplus(\mu\odot x)=(\lambda x-\lambda+1)+(\mu x-\mu+1)-1$, que es lo mismo.

**Cálculo.** $3\odot 5=15-3+1=13$ y $(-2)\odot 4=-8+2+1=-5$; entonces
$13\oplus(-5)=13-5-1=7$.

Comprobación por otro camino: la función $\varphi(x)=x-1$ traduce estas operaciones a las usuales, pues
$\varphi(x\oplus y)=\varphi(x)+\varphi(y)$ y $\varphi(\lambda\odot x)=\lambda\,\varphi(x)$. Como
$\varphi(5)=4$ y $\varphi(4)=3$, el resultado traducido es $3\cdot 4+(-2)\cdot 3=6$, y $\varphi^{-1}(6)=7$.
La estructura es la de $\mathbb{R}$ "corrida una unidad": por eso el nulo es $1$.

### Ejemplo 3 · Un producto por escalar que rompe un solo axioma
<!-- check: U1.T02.E3 -->

En $\mathbb{R}^2$ con la suma usual definimos $\lambda\odot(x,y)=(\lambda x,\,y)$. Decidir si es un espacio
vectorial real.

Los axiomas 1 a 5 se cumplen porque la suma es la usual. Revisamos los del producto, con $v=(x,y)$ y
$w=(x',y')$:

- Axioma 7: $1\odot(x,y)=(x,y)$. Se cumple.
- Axioma 8: $(\lambda\mu)\odot(x,y)=(\lambda\mu x,y)$ y $\lambda\odot(\mu\odot(x,y))=\lambda\odot(\mu x,y)=(\lambda\mu x,y)$.
  Se cumple.
- Axioma 9: $\lambda\odot(x+x',y+y')=(\lambda x+\lambda x',\,y+y')$ y
  $\lambda\odot v+\lambda\odot w=(\lambda x,y)+(\lambda x',y')=(\lambda x+\lambda x',\,y+y')$. Se cumple.
- Axioma 10: $(\lambda+\mu)\odot(x,y)=((\lambda+\mu)x,\,y)$, mientras que
  $\lambda\odot(x,y)+\mu\odot(x,y)=((\lambda+\mu)x,\,2y)$. Coinciden solo si $y=0$.

Para refutar el axioma 10 basta un contraejemplo concreto: con $v=(1,2)$ y $\lambda=\mu=1$,

$$
(1+1)\odot(1,2)=(2,2)\qquad\text{pero}\qquad 1\odot(1,2)+1\odot(1,2)=(1,2)+(1,2)=(2,4).
$$

No es un espacio vectorial, y el único axioma que falla es el 10.

Comprobación: $(2,2)\neq(2,4)$ porque difieren en la segunda componente.

Un caso parecido muestra que el axioma 7 tampoco se deduce de los demás: con la suma usual y
$\lambda\odot(x,y)=(\lambda x,0)$ se cumplen los axiomas 8, 9 y 10, pero $1\odot(1,2)=(1,0)\neq(1,2)$.
Sin el axioma 7, "multiplicar por $1$" podría borrar información.

### Ejemplo 4 · Cálculos en $P_2[\mathbb{R}]$ y un conjunto de polinomios que no es espacio
<!-- check: U1.T02.E4 -->

Sean $p=1+2x-x^2$ y $q=3-x+2x^2$ en $P_2[\mathbb{R}]$. Calcular $2p-q$. Decidir si el conjunto $G$ de los
polinomios de grado **exactamente** $2$, con las operaciones usuales, es un espacio vectorial.

**Cálculo.** Operamos coeficiente a coeficiente:

$$
2p-q=(2-3)+(4+1)x+(-2-2)x^2=-1+5x-4x^2 .
$$

**El conjunto $G$.** Los polinomios $x+x^2$ y $1-x^2$ tienen grado $2$, pero su suma

$$
(x+x^2)+(1-x^2)=1+x
$$

tiene grado $1$. Falla el cierre de la suma (axioma 1). Además, $G$ no contiene al polinomio nulo, así
que tampoco hay neutro. $G$ no es un espacio vectorial; $P_2[\mathbb{R}]$ sí lo es justamente porque
incluye los grados menores y el polinomio nulo.

Comprobación: evaluando en $x=1$, $2p(1)-q(1)=2\cdot 2-4=0$ y $-1+5-4=0$; en $x=2$,
$2p(2)-q(2)=2\cdot 1-9=-7$ y $-1+10-16=-7$.

## Propiedades elementales

Las siguientes propiedades parecen obvias en $\mathbb{R}^n$, pero en un espacio vectorial cualquiera hay que
deducirlas de los axiomas: no sabemos de antemano cómo están definidas las operaciones (el Ejemplo 2
muestra que el nulo puede ser el número $1$).

:::note[Propiedad]
Sea $V$ un espacio vectorial sobre $K$. Para todos $u,v,w\in V$ y $\lambda\in K$:

1. El vector nulo es único.
2. El opuesto de cada vector es único.
3. Cancelación: si $u+w=v+w$, entonces $u=v$.
4. $0\cdot v=0_V$ (el escalar cero por cualquier vector da el vector nulo).
5. $\lambda\, 0_V=0_V$ (cualquier escalar por el vector nulo da el vector nulo).
6. $(-1)v=-v$.
7. Si $\lambda v=0_V$, entonces $\lambda=0$ o $v=0_V$.
:::

**Demostración.**

1. Supongamos que $0_V$ y $0'_V$ cumplen el axioma 3. Entonces
   $0_V=0_V+0'_V=0'_V+0_V=0'_V$: la primera igualdad usa que $0'_V$ es neutro, la segunda la
   conmutativa y la tercera que $0_V$ es neutro.
2. Sean $w$ y $w'$ opuestos de $v$. Entonces
   $w=w+0_V=w+(v+w')=(w+v)+w'=0_V+w'=w'$, usando neutro, que $w'$ es opuesto, la asociativa, que $w$
   es opuesto (con la conmutativa) y otra vez neutro.
3. Sumamos $-w$ a ambos miembros de $u+w=v+w$ y asociamos:
   $u=u+(w+(-w))=(u+w)+(-w)=(v+w)+(-w)=v+(w+(-w))=v$.
4. Como $0=0+0$ en $K$, el axioma 10 da $0\cdot v=(0+0)v=0\cdot v+0\cdot v$. Por otro lado
   $0\cdot v=0_V+0\cdot v$. Igualando, $0_V+0\cdot v=0\cdot v+0\cdot v$, y por cancelación $0_V=0\cdot v$.
5. Como $0_V=0_V+0_V$, el axioma 9 da $\lambda 0_V=\lambda(0_V+0_V)=\lambda 0_V+\lambda 0_V$. Igual que
   antes, $0_V+\lambda 0_V=\lambda 0_V+\lambda 0_V$ y por cancelación $\lambda 0_V=0_V$.
6. Por los axiomas 7 y 10 y la propiedad 4,
   $v+(-1)v=1\cdot v+(-1)v=(1+(-1))v=0\cdot v=0_V$. Entonces $(-1)v$ es un opuesto de $v$ y, por la
   unicidad del opuesto, $(-1)v=-v$.
7. Si $\lambda=0$ no hay nada que probar. Si $\lambda\neq 0$, existe $\lambda^{-1}$ en $K$ y, por los
   axiomas 7 y 8 y la propiedad 5,
   $v=1\cdot v=(\lambda^{-1}\lambda)v=\lambda^{-1}(\lambda v)=\lambda^{-1}0_V=0_V$. $\blacksquare$

La propiedad 7 es la primera en la que se usa que $K$ es un **cuerpo**: hace falta el inverso
$\lambda^{-1}$. Si los escalares fueran $\mathbb{Z}_4$, que no es cuerpo, podría ocurrir que $2\cdot v=0$ con
$2\neq 0$ y $v\neq 0$; por ejemplo, en $\mathbb{Z}_4$ mismo, $2\cdot 2=0$.

:::tip[Consecuencia en ℤ₂ⁿ]
Si $V$ es un espacio vectorial sobre $\mathbb{Z}_2$, entonces para todo $v\in V$

$$
v+v=1\cdot v+1\cdot v=(1+1)v=0\cdot v=0_V ,
$$

y por la unicidad del opuesto, $-v=v$. En $\mathbb{Z}_2^n$ **restar es sumar** y cada vector es su propio
opuesto, que es lo que usamos en el Ejemplo 1 para recuperar un bloque.
:::

:::caution[Errores frecuentes]
- **Suponer que el nulo es "el cero".** En el Ejemplo 2 el vector nulo es el número $1$. El nulo se
  calcula a partir de la suma definida, buscando el $e$ que cumple $v+e=v$ para todo $v$.
- **Verificar los axiomas con un ejemplo numérico y concluir que valen.** Un caso particular puede
  refutar un axioma, pero nunca lo prueba: en el Ejemplo 3, con $y=0$ el axioma 10 parece cumplirse.
  Para probar hace falta un argumento con elementos genéricos; para refutar, un contraejemplo concreto.
- **Olvidar el cierre.** Los polinomios de grado exactamente $2$, las matrices inversibles o los
  vectores de $\mathbb{R}^2$ con coordenadas positivas no son espacios vectoriales con las operaciones
  usuales: la suma o el producto por escalar se salen del conjunto.
- **Pensar que $P_2[\mathbb{R}]$ son "ternas".** Un elemento de $P_2[\mathbb{R}]$ es un polinomio como
  $1+2x-x^2$. Podemos usar la terna de coeficientes $(1,2,-1)$ como herramienta de cálculo, pero el
  vector es el polinomio.
- **Llamar vector solo a lo que se dibuja como flecha.** Una palabra de $\mathbb{Z}_2^8$ o una matriz son
  vectores de pleno derecho.
:::

## Autoevaluación

**1.** ¿Cuántos elementos tiene $\mathbb{Z}_2^{2\times 3}$?

<details>
<summary>Respuesta</summary>

Una matriz $2\times 3$ tiene $6$ entradas, cada una con dos valores posibles: $2^6=64$ elementos.

</details>

**2.** ¿Es el conjunto de las matrices reales $2\times 2$ inversibles, con las operaciones usuales, un
espacio vectorial?

<details>
<summary>Respuesta</summary>

No. Falla el cierre de la suma: $I$ y $-I$ son inversibles, pero $I+(-I)$ es la matriz nula, que no lo es.
Tampoco contiene al neutro.

</details>

**3.** Probar que si $u+v=u$ para algún $u\in V$, entonces $v=0_V$.

<details>
<summary>Respuesta</summary>

$u+v=u=u+0_V$; conmutando y aplicando la cancelación, $v=0_V$.

</details>

**4.** En $\mathbb{Z}_3^n$, ¿vale $v+v=0$ para todo $v$?

<details>
<summary>Respuesta</summary>

No. $v+v=2v$, que es nulo solo si $v=0$ (por la propiedad 7, porque $2\neq 0$ en $\mathbb{Z}_3$). Lo que vale
es $v+v+v=3v=0\cdot v=0$.

</details>

:::tip[En resumen]
- Un espacio vectorial $(V,+,K,\cdot)$ es un conjunto con una suma y un producto por escalares de un
  cuerpo $K$ que cumplen diez axiomas: cinco para la suma y cinco para el producto por escalar.
- Ejemplos centrales de la materia: $\mathbb{R}^n$, $\mathbb{Z}_2^n$ (con $2^n$ elementos),
  $\mathbb{R}^{m\times n}$, $P_n[\mathbb{R}]$ y espacios de funciones.
- "Vector" significa elemento de un espacio vectorial, no flecha. El vector nulo depende de las
  operaciones.
- En todo espacio vectorial: el nulo y el opuesto son únicos, $0\cdot v=0_V$, $\lambda 0_V=0_V$,
  $(-1)v=-v$ y $\lambda v=0_V$ implica $\lambda=0$ o $v=0_V$.
- Sobre $\mathbb{Z}_2$: $v+v=0_V$ y $-v=v$.
- Para refutar un axioma alcanza un contraejemplo concreto; para probarlo hace falta un argumento general.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed., sección 6.1, "Espacios y subespacios
  vectoriales" (p. 447).
- Poole, 3.ª ed., sección 1.1, subsección "Vectores binarios y aritmética modular" (pp. 13–16), para
  $\mathbb{Z}_2^n$.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed., capítulo de espacios vectoriales, sección sobre
  espacios y subespacios vectoriales.
- Hernández, Vázquez y Zurro, *Álgebra lineal y Geometría*, 3.ª ed., sección 4.1 (p. 144), como lectura
  complementaria.

Lección anterior: [cuerpos y ℤ₂](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/). Lección siguiente:
[subespacios](/algebra-ii/unidad-1/teoria/subespacios/). Repaso relacionado:
[vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/).
