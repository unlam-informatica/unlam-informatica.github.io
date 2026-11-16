---
title: Determinantes
description: Desarrollo por cofactores, regla de Sarrus, efecto de las operaciones de fila, cálculo por triangulación, inversibilidad y determinantes con parámetros.
slug: algebra-ii/repaso/determinantes
sidebar:
  order: 2
  label: R.2 Determinantes
---

## Para qué sirve

El determinante asigna a cada matriz cuadrada un número que decide, de un solo golpe, si la matriz es inversible. En Álgebra II se usa para decidir si $n$ vectores de $\mathbb{R}^n$ forman una base, si una transformación lineal es un isomorfismo y, sobre todo, para hallar autovalores: el polinomio característico $p_A(\lambda)=\det(\lambda I-A)$ de la Unidad 3 es un determinante con un parámetro. Esta lección repasa la definición, las propiedades que permiten calcularlo sin desarrollar a ciegas y el trabajo con parámetros.

## Definición por desarrollo por cofactores

Para matrices chicas:

$$
\det(a)=a,\qquad \det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc .
$$

:::note[Definición]
Sea $A\in\mathbb{R}^{n\times n}$ con $n\geq2$. El **menor** $M_{ij}$ es el determinante de la matriz de $(n-1)\times(n-1)$ que se obtiene al eliminar la fila $i$ y la columna $j$ de $A$. El **cofactor** de la posición $(i,j)$ es $C_{ij}=(-1)^{i+j}M_{ij}$. El determinante de $A$ es

$$
\det A=a_{11}C_{11}+a_{12}C_{12}+\dots+a_{1n}C_{1n}
$$

(desarrollo por la primera fila). También se escribe $\lvert A\rvert$.
:::

:::note[Teorema (desarrollo de Laplace)]
El determinante puede desarrollarse por **cualquier** fila $i$ o **cualquier** columna $j$:

$$
\det A=\sum_{k=1}^{n}a_{ik}C_{ik}=\sum_{k=1}^{n}a_{kj}C_{kj}.
$$
:::

Los signos $(-1)^{i+j}$ alternan como un tablero de ajedrez, empezando con $+$ en la esquina superior izquierda. En la práctica se elige la fila o columna con **más ceros**, porque cada cero anula un sumando.

**Regla de Sarrus.** Para $3\times3$, desarrollar por la primera fila y expandir los tres determinantes de $2\times2$ da seis productos:

$$
\det\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix}=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}.
$$

Los tres primeros son los productos en la dirección de la diagonal principal (completando con las columnas repetidas a la derecha) y los tres últimos, en la dirección de la otra diagonal. Es un caso particular del desarrollo por cofactores y **solo vale para $3\times3$**.

### Ejemplo 1 · Un determinante de 3×3 por dos caminos
<!-- check: R.T02.E1 -->

Calculamos el determinante de

$$
A=\begin{pmatrix}2&-1&3\\0&4&1\\1&2&-2\end{pmatrix}.
$$

**Por cofactores.** La primera columna tiene un cero, así que desarrollamos por ella; los signos de esa columna son $+,-,+$:

$$
\det A=2\begin{vmatrix}4&1\\2&-2\end{vmatrix}-0\begin{vmatrix}-1&3\\2&-2\end{vmatrix}+1\begin{vmatrix}-1&3\\4&1\end{vmatrix}=2(-8-2)+(-1-12)=-20-13=-33 .
$$

**Por Sarrus.** Productos en la dirección de la diagonal principal: $2\cdot4\cdot(-2)+(-1)\cdot1\cdot1+3\cdot0\cdot2=-16-1+0=-17$. En la otra dirección: $3\cdot4\cdot1+2\cdot1\cdot2+(-1)\cdot0\cdot(-2)=12+4+0=16$. Entonces $\det A=-17-16=-33$.

**Comprobación.** Ambos métodos dan $-33$. Como $\det A\neq0$, $A$ es inversible.

## Propiedades

:::note[Propiedad (operaciones elementales de fila)]
Sea $A\in\mathbb{R}^{n\times n}$.

1. Si $B$ se obtiene **intercambiando** dos filas de $A$, entonces $\det B=-\det A$.
2. Si $B$ se obtiene **multiplicando** una fila de $A$ por $c$, entonces $\det B=c\det A$.
3. Si $B$ se obtiene **sumando** a una fila un múltiplo de otra ($F_i+cF_j\to F_i$, $i\neq j$), entonces $\det B=\det A$.

Consecuencias: si $A$ tiene una fila nula, o dos filas iguales o proporcionales, $\det A=0$.
:::

:::note[Propiedad]
Para $A,B\in\mathbb{R}^{n\times n}$ y $c\in\mathbb{R}$:

1. $\det(A^t)=\det A$. Por eso todo lo dicho para filas vale para columnas.
2. $\det(AB)=\det A\,\det B$.
3. Si $A$ es inversible, $\det(A^{-1})=\dfrac{1}{\det A}$.
4. $\det(cA)=c^n\det A$.
5. Si $A$ es triangular (superior o inferior) o diagonal, $\det A=a_{11}a_{22}\cdots a_{nn}$. En particular $\det I=1$.
:::

**Demostración de 3 y 4.** De $AA^{-1}=I$ y la propiedad 2, $\det A\,\det(A^{-1})=\det I=1$, de donde $\det A\neq0$ y $\det(A^{-1})=1/\det A$. Para 4, $cA$ se obtiene de $A$ multiplicando cada una de sus $n$ filas por $c$; cada vez el determinante queda multiplicado por $c$, así que en total por $c^n$. $\blacksquare$

**Demostración de 5 (triangular superior).** Desarrollamos por la primera columna, que solo tiene $a_{11}$ como posible elemento no nulo: $\det A=a_{11}\det A'$, donde $A'$ es triangular superior de $(n-1)\times(n-1)$ con diagonal $a_{22},\dots,a_{nn}$. Repitiendo el argumento se obtiene el producto de la diagonal. $\blacksquare$

Ojo: $\det(A+B)$ **no** se relaciona de manera simple con $\det A$ y $\det B$; la propiedad multiplicativa vale para el producto, no para la suma.

## Cálculo por triangulación

Desarrollar por cofactores una matriz de $4\times4$ sin ceros exige cuatro determinantes de $3\times3$. Es más eficiente **triangular** con operaciones de fila, llevando la cuenta de cómo cambia el determinante:

- las operaciones $F_i+cF_j\to F_i$ no lo cambian (son las que más se usan);
- cada intercambio de filas cambia el signo;
- si se multiplica una fila por $c$, el determinante queda multiplicado por $c$ (hay que compensar dividiendo).

Al llegar a una matriz triangular $U$, $\det A=(-1)^s\det U$, donde $s$ es la cantidad de intercambios (si no se escaló ninguna fila).

### Ejemplo 2 · Un determinante de 4×4 por triangulación
<!-- check: R.T02.E2 -->

Calculamos $\det B$ para

$$
B=\begin{pmatrix}0&1&2&1\\1&2&1&0\\2&3&0&1\\1&1&1&2\end{pmatrix}.
$$

El elemento $b_{11}$ es $0$, así que intercambiamos $F_1\leftrightarrow F_2$ (el signo cambia). Luego $F_3-2F_1\to F_3$ y $F_4-F_1\to F_4$ (no cambian el determinante):

$$
\det B=-\begin{vmatrix}1&2&1&0\\0&1&2&1\\2&3&0&1\\1&1&1&2\end{vmatrix}=-\begin{vmatrix}1&2&1&0\\0&1&2&1\\0&-1&-2&1\\0&-1&0&2\end{vmatrix}.
$$

Con $F_3+F_2\to F_3$ y $F_4+F_2\to F_4$:

$$
\det B=-\begin{vmatrix}1&2&1&0\\0&1&2&1\\0&0&0&2\\0&0&2&3\end{vmatrix}.
$$

En la posición $(3,3)$ quedó un $0$ y debajo hay un $2$: intercambiamos $F_3\leftrightarrow F_4$ (el signo vuelve a cambiar) y la matriz queda triangular:

$$
\det B=(-1)(-1)\begin{vmatrix}1&2&1&0\\0&1&2&1\\0&0&2&3\\0&0&0&2\end{vmatrix}=1\cdot1\cdot2\cdot2=4 .
$$

**Comprobación.** Desarrollando $B$ por la primera fila (en la que $b_{11}=0$) se obtiene $-1\cdot M_{12}+2M_{13}-1\cdot M_{14}$ con $M_{12}=-4$, $M_{13}=-1$ y $M_{14}=-2$, es decir $4-2+2=4$.

## Determinante e inversibilidad

:::note[Teorema]
Una matriz $A\in\mathbb{R}^{n\times n}$ es inversible si y solo si $\det A\neq0$.
:::

**Demostración.** Si $A$ es inversible, ya vimos que $\det A\,\det(A^{-1})=1$, así que $\det A\neq0$. Recíprocamente, escalonamos $A$ por filas hasta una matriz triangular superior $U$. Las operaciones de fila multiplican el determinante por números no nulos, así que $\det A\neq0$ implica $\det U\neq0$: todos los elementos diagonales de $U$ son no nulos. Entonces hay $n$ pivotes, Gauss-Jordan lleva $A$ a $I$ y $A$ es inversible. $\blacksquare$

Este teorema se suma a una lista de condiciones equivalentes que se completa en [R.3](/algebra-ii/repaso/sistemas-lineales/) y en la Unidad 1. Para $A\in\mathbb{R}^{n\times n}$ son equivalentes:

1. $A$ es inversible;
2. $\det A\neq0$;
3. el sistema $Ax=b$ tiene solución única para todo $b$;
4. el sistema homogéneo $Ax=0$ solo tiene la solución trivial;
5. $\operatorname{rango}(A)=n$.

## Determinantes con parámetros

Cuando una matriz depende de un parámetro $k$, su determinante es un polinomio en $k$, y la pregunta "¿para qué valores de $k$ la matriz no es inversible?" se reduce a hallar las raíces de ese polinomio. Dos consejos: hacer primero operaciones de fila o columna que generen ceros o factores comunes (así el polinomio sale ya factorizado), y no dividir por expresiones que puedan anularse.

### Ejemplo 3 · Valores del parámetro que anulan el determinante
<!-- check: R.T02.E3 -->

Hallamos los $k\in\mathbb{R}$ para los que $A_k=\begin{pmatrix}k&1&1\\1&k&1\\1&1&k\end{pmatrix}$ no es inversible.

**Método 1: desarrollo directo.** Por la primera fila:

$$
\det A_k=k(k^2-1)-1\,(k-1)+1\,(1-k)=k^3-3k+2 .
$$

Para factorizar, $k=1$ es raíz ($1-3+2=0$); por Ruffini (ver [R.4](/algebra-ii/repaso/polinomios/)), $k^3-3k+2=(k-1)(k^2+k-2)=(k-1)^2(k+2)$.

**Método 2: operaciones que factorizan.** Los elementos de cada fila suman lo mismo, $k+2$. Con $C_1+C_2+C_3\to C_1$ (no cambia el determinante) la primera columna queda con $k+2$ en todas sus posiciones; sacamos ese factor común y restamos la primera fila a las otras dos:

$$
\det A_k=(k+2)\begin{vmatrix}1&1&1\\1&k&1\\1&1&k\end{vmatrix}=(k+2)\begin{vmatrix}1&1&1\\0&k-1&0\\0&0&k-1\end{vmatrix}=(k+2)(k-1)^2 .
$$

El segundo método evita factorizar un polinomio de grado 3, y por eso conviene cuando la matriz tiene una estructura así.

**Conclusión.** $\det A_k=0\iff k=1$ o $k=-2$. Para esos dos valores $A_k$ no es inversible; para cualquier otro $k$ sí lo es.

**Comprobación.** Con $k=0$, $\det A_0=0-0+2=2$ y la fórmula da $(0+2)(0-1)^2=2$. Con $k=-2$ las tres filas suman el vector nulo, así que son linealmente dependientes, de acuerdo con $\det A_{-2}=0$.

En la Unidad 3 se hace exactamente esto con $\det(\lambda I-A)$: el parámetro es $\lambda$ y los valores que anulan el determinante son los autovalores.

:::caution[Errores frecuentes]
- **Suma.** $\det(A+B)\neq\det A+\det B$ en general: con $A=B=I_2$, $\det(2I_2)=4$ y $\det A+\det B=2$.
- **Escalar.** $\det(cA)=c^n\det A$, no $c\det A$: si $A$ es de $3\times3$, $\det(2A)=8\det A$.
- **Sarrus fuera de lugar.** La regla de Sarrus no vale para $4\times4$; aplicar "diagonales" a una matriz de $4\times4$ da un número que en general no es el determinante.
- **Signo del intercambio.** Olvidar que cada intercambio de filas cambia el signo. En el Ejemplo 2 hubo dos intercambios y el signo final es $+$.
- **Escalar una fila sin compensar.** Si al triangular se reemplaza $F_2$ por $3F_2$, el determinante queda multiplicado por $3$. Usar $F_i+cF_j\to F_i$ con la fila que se modifica sin multiplicar.
- **Dividir por un parámetro.** Al trabajar con $A_k$, dividir una fila por $k-1$ supone $k\neq1$; el caso $k=1$ debe analizarse aparte.
:::

:::tip[En resumen]
- $\det A=\sum_k a_{ik}C_{ik}$ por cualquier fila o columna, con $C_{ij}=(-1)^{i+j}M_{ij}$; Sarrus es el caso $3\times3$.
- Intercambio: cambia el signo; multiplicar una fila por $c$: multiplica por $c$; $F_i+cF_j\to F_i$: no cambia.
- $\det(A^t)=\det A$, $\det(AB)=\det A\det B$, $\det(A^{-1})=1/\det A$, $\det(cA)=c^n\det A$; triangular: producto de la diagonal.
- $A$ inversible $\iff\det A\neq0$.
- Con parámetros: el determinante es un polinomio; sus raíces son los valores que hacen a la matriz no inversible.
:::

## Ejercicios de repaso

### Ejercicio R.05 · Cofactores y propiedades
<!-- ejercicio: R.05 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Sea $C=\begin{pmatrix}3&0&-1\\2&1&4\\-1&0&2\end{pmatrix}$. Calcular $\det C$ eligiendo convenientemente la fila o columna de desarrollo y, sin hacer más productos de matrices, deducir $\det(C^t)$, $\det(2C)$, $\det(C^{-1})$ y $\det(C^3)$.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La segunda columna tiene dos ceros: desarrollamos por ella y luego usamos las propiedades.

El único elemento no nulo de la columna 2 es $c_{22}=1$, con signo $(-1)^{2+2}=+$:

$$
\det C=1\cdot\begin{vmatrix}3&-1\\-1&2\end{vmatrix}=6-1=5 .
$$

Entonces $\det(C^t)=5$; $\det(2C)=2^3\cdot5=40$; como $\det C\neq0$, $C$ es inversible y $\det(C^{-1})=\frac15$; y $\det(C^3)=(\det C)^3=125$.

**Comprobación.** Por Sarrus: $3\cdot1\cdot2+0\cdot4\cdot(-1)+(-1)\cdot2\cdot0-\big((-1)\cdot1\cdot(-1)+3\cdot4\cdot0+0\cdot2\cdot2\big)=6-1=5$.

:::tip[Resultado]
$\det C=5$, $\det(C^t)=5$, $\det(2C)=40$, $\det(C^{-1})=\frac15$, $\det(C^3)=125$.
:::

</details>

### Ejercicio R.06 · Triangulación de una matriz de 4×4
<!-- ejercicio: R.06 | nivel: inicial | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Calcular por triangulación el determinante de $D=\begin{pmatrix}1&1&1&1\\1&2&2&2\\1&2&3&3\\1&2&3&4\end{pmatrix}$ y decidir si $D$ es inversible.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Usar solo operaciones del tipo $F_i-F_j\to F_i$, que no cambian el determinante.

Con $F_2-F_1\to F_2$, $F_3-F_1\to F_3$ y $F_4-F_1\to F_4$; después $F_3-F_2\to F_3$ y $F_4-F_2\to F_4$; por último $F_4-F_3\to F_4$:

$$
\det D=\begin{vmatrix}1&1&1&1\\0&1&1&1\\0&1&2&2\\0&1&2&3\end{vmatrix}=\begin{vmatrix}1&1&1&1\\0&1&1&1\\0&0&1&1\\0&0&1&2\end{vmatrix}=\begin{vmatrix}1&1&1&1\\0&1&1&1\\0&0&1&1\\0&0&0&1\end{vmatrix}=1 .
$$

**Comprobación.** No hubo intercambios ni escalamientos, así que el determinante es el producto de la diagonal final, $1\cdot1\cdot1\cdot1$.

:::tip[Resultado]
$\det D=1\neq0$: $D$ es inversible.
:::

</details>

### Ejercicio R.07 · Matriz tridiagonal con parámetro
<!-- ejercicio: R.07 | nivel: intermedio | tipo: calculo | verificacion: sympy -->

:::note[Enunciado]
Hallar todos los $k\in\mathbb{R}$ para los que $A_k=\begin{pmatrix}k&1&0\\1&k&1\\0&1&k\end{pmatrix}$ no es inversible.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Calcular $\det A_k$ como polinomio en $k$, factorizarlo y buscar sus raíces.

Desarrollando por la primera fila:

$$
\det A_k=k\begin{vmatrix}k&1\\1&k\end{vmatrix}-1\begin{vmatrix}1&1\\0&k\end{vmatrix}+0=k(k^2-1)-k=k^3-2k=k\,(k^2-2).
$$

Se anula si $k=0$ o $k^2=2$, es decir $k=\pm\sqrt2$.

**Comprobación.** Para $k=0$, las filas 1 y 3 de $A_0$ son iguales, $(0,1,0)$, así que $\det A_0=0$. Para $k=\sqrt2$: $\sqrt2\,(2-1)-\sqrt2=0$.

:::tip[Resultado]
$A_k$ no es inversible exactamente para $k\in\{0,\sqrt2,-\sqrt2\}$.
:::

</details>

### Ejercicio R.08 · Verdadero o falso sobre determinantes
<!-- ejercicio: R.08 | nivel: intermedio | tipo: verdadero-falso | verificacion: sympy -->

:::note[Enunciado]
Decidir si cada afirmación es verdadera o falsa. Justificar.

1. Para toda $A,B\in\mathbb{R}^{2\times2}$, $\det(A+B)=\det A+\det B$.
2. Si $A\in\mathbb{R}^{3\times3}$ y $\det A=2$, entonces $\det(-A)=-2$.
3. Si $A,B\in\mathbb{R}^{n\times n}$ y $\det(AB)=0$, entonces $A$ o $B$ no es inversible.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Contraejemplo para la falsa; propiedades $\det(cA)=c^n\det A$ y $\det(AB)=\det A\det B$ para las verdaderas.

1. **Falsa.** Con $A=B=I_2$: $\det(A+B)=\det(2I_2)=4$, pero $\det A+\det B=2$.
2. **Verdadera.** $\det(-A)=(-1)^3\det A=-2$. Para $n$ par el resultado sería $+2$: el signo depende del tamaño.
3. **Verdadera.** $0=\det(AB)=\det A\det B$ obliga a que $\det A=0$ o $\det B=0$, y una matriz con determinante nulo no es inversible.

**Comprobación.** Para el ítem 2, con $A=\operatorname{diag}(2,1,1)$ se tiene $\det A=2$ y $-A=\operatorname{diag}(-2,-1,-1)$, cuyo determinante es $-2$.

:::tip[Resultado]
1 falsa, 2 verdadera, 3 verdadera.
:::

</details>

## Dónde se usa en Álgebra II

- Decidir si $n$ vectores de $\mathbb{R}^n$ son linealmente independientes (determinante de la matriz que los tiene como columnas): [independencia lineal](/algebra-ii/unidad-1/teoria/independencia-lineal/) y [base y dimensión](/algebra-ii/unidad-1/teoria/base-y-dimension/).
- Decidir si una transformación lineal es isomorfismo a partir de su matriz: [clasificación](/algebra-ii/unidad-2/teoria/clasificacion/) y [composición e inversa](/algebra-ii/unidad-2/teoria/composicion-e-inversa/).
- Calcular $p_A(\lambda)=\det(\lambda I-A)$ y sus raíces: [polinomio característico](/algebra-ii/unidad-3/teoria/polinomio-caracteristico/); probar que matrices semejantes tienen el mismo determinante: [matrices semejantes](/algebra-ii/unidad-3/teoria/matrices-semejantes/).

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 4.2 (determinantes), que además muestra la conexión con autovalores en 4.1 y 4.3.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de determinantes.
- Lección anterior: [R.1 Vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/). Siguiente: [R.3 Sistemas lineales](/algebra-ii/repaso/sistemas-lineales/).
