---
title: Polinomio característico
description: Deducción de la ecuación det(λI − A) = 0, cálculo de autovalores y autoespacios en matrices 2×2 y 3×3, multiplicidades algebraica y geométrica, y la traza y el determinante en los coeficientes.
slug: algebra-ii/unidad-3/teoria/polinomio-caracteristico
sidebar:
  order: 2
  label: 3.2 Polinomio característico
---

## Para qué sirve

En la [lección anterior](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/) aprendimos a
*verificar*: dado un vector, multiplicamos; dado un número $\lambda$, estudiamos si
$\lambda I-A$ es singular. Pero en los problemas nadie nos da los candidatos. Necesitamos un
método para **encontrar todos los autovalores** de una matriz, y después todos sus autovectores.
El polinomio característico convierte esa búsqueda en el cálculo de las raíces de un polinomio.

## De $Av=\lambda v$ a una ecuación en $\lambda$

Sea $A\in\mathbb{R}^{n\times n}$. Para un número $\lambda$ fijo, encadenamos equivalencias:

$$
\begin{aligned}
\lambda \text{ es autovalor de } A
&\iff \text{existe } v\neq0 \text{ con } Av=\lambda v\\
&\iff \text{existe } v\neq0 \text{ con } (\lambda I-A)v=0\\
&\iff \text{el sistema homogéneo } (\lambda I-A)x=0 \text{ es compatible indeterminado}\\
&\iff \lambda I-A \text{ no es inversible}\\
&\iff \det(\lambda I-A)=0 .
\end{aligned}
$$

El segundo paso usa que $\lambda v=\lambda Iv$; el tercero, que un sistema homogéneo siempre es
compatible y tiene soluciones no nulas exactamente cuando es indeterminado. Si ahora dejamos
$\lambda$ como variable, $\det(\lambda I-A)$ es una expresión en $\lambda$.

:::note[Definición]
El **polinomio característico** de $A\in\mathbb{R}^{n\times n}$ es

$$
p_A(\lambda)=\det(\lambda I-A).
$$

La ecuación $p_A(\lambda)=0$ se llama **ecuación característica** de $A$.
:::

:::note[Teorema]
Un número real $\lambda_0$ es autovalor de $A$ si y solo si $p_A(\lambda_0)=0$. Es decir, los
autovalores de $A$ son las raíces reales de su polinomio característico.
:::

La demostración es la cadena de equivalencias anterior con $\lambda=\lambda_0$.

## Grado, coeficiente principal y los otros coeficientes

:::note[Propiedad]
Si $A=(a_{ij})\in\mathbb{R}^{n\times n}$, entonces $p_A$ es un polinomio **mónico de grado $n$**
y

$$
p_A(\lambda)=\lambda^n-\operatorname{tr}(A)\,\lambda^{n-1}+\dots+(-1)^n\det(A),
$$

donde $\operatorname{tr}(A)=a_{11}+a_{22}+\dots+a_{nn}$ es la **traza** de $A$. En particular, para
$n=2$,

$$
p_A(\lambda)=\lambda^2-\operatorname{tr}(A)\,\lambda+\det(A).
$$
:::

**Demostración.** La matriz $\lambda I-A$ tiene en la diagonal $\lambda-a_{11},\dots,\lambda-a_{nn}$
y fuera de ella los números $-a_{ij}$, que no dependen de $\lambda$. El determinante es una suma
de productos de $n$ entradas, una por fila y una por columna, con signo. Cada término es entonces
un polinomio en $\lambda$, y su grado es a lo sumo la cantidad de entradas diagonales que usa.

- El término que usa toda la diagonal es $(\lambda-a_{11})(\lambda-a_{22})\cdots(\lambda-a_{nn})$.
  Al desarrollarlo, el término de grado $n$ es $\lambda^n$ y el de grado $n-1$ es
  $-(a_{11}+\dots+a_{nn})\lambda^{n-1}$.
- Cualquier otro término omite al menos una entrada diagonal, digamos la de la fila $i$; usa
  entonces una entrada $(i,j)$ con $j\neq i$, y la columna $i$ tiene que aportar desde otra fila
  $k\neq i$, así que la entrada diagonal $(k,k)$ también se omite. Por lo tanto usa a lo sumo
  $n-2$ entradas diagonales y tiene grado a lo sumo $n-2$.

Así, $p_A$ es mónico de grado $n$ y su coeficiente de $\lambda^{n-1}$ es $-\operatorname{tr}(A)$.
El término independiente es $p_A(0)=\det(0I-A)=\det(-A)=(-1)^n\det(A)$, porque multiplicar
las $n$ filas por $-1$ multiplica el determinante por $(-1)^n$. $\blacksquare$

Dos consecuencias inmediatas:

- Una matriz $n\times n$ tiene **a lo sumo $n$ autovalores** distintos, porque un polinomio de
  grado $n$ tiene a lo sumo $n$ raíces.
- Si $n$ es **impar**, $A$ tiene **al menos un autovalor real**, porque todo polinomio real de
  grado impar tiene una raíz real.

### ¿Y $\det(A-\lambda I)$?

Algunos textos y apuntes escriben la ecuación característica como $\det(A-\lambda I)=0$. Como
$A-\lambda I=-(\lambda I-A)$,

$$
\det(A-\lambda I)=(-1)^n\det(\lambda I-A)=(-1)^np_A(\lambda),
$$

que tiene **las mismas raíces**: para buscar autovalores da igual. La diferencia es el signo del
coeficiente principal cuando $n$ es impar. Nosotros usamos $\det(\lambda I-A)$ porque resulta
siempre mónico y porque sus coeficientes muestran directamente la traza y el determinante.

## Procedimiento

Para hallar autovalores y autoespacios de $A\in\mathbb{R}^{n\times n}$:

1. **Calcular** $p_A(\lambda)=\det(\lambda I-A)$. Conviene desarrollar por la fila o columna con
   más ceros y **factorizar** lo antes posible; expandir todo y después factorizar suele ser
   más trabajoso.
2. **Hallar las raíces reales** de $p_A$. En $2\times2$, con la resolvente. En $3\times3$ o más,
   buscar raíces racionales entre los divisores del término independiente (cuando $p_A$ tiene
   coeficientes enteros y es mónico) y bajar el grado con la regla de Ruffini. Ver
   [polinomios](/algebra-ii/repaso/polinomios/).
3. **Para cada autovalor $\lambda_i$, resolver** el sistema homogéneo $(\lambda_iI-A)x=0$ por
   escalonamiento. Una base de su conjunto solución es una base de $E_{\lambda_i}(A)$.
4. **Verificar** con $Av=\lambda_iv$ al menos un vector de cada base.

Si en el paso 3 el sistema queda compatible determinado, hay un error de cuentas: por
construcción, $\lambda_iI-A$ es singular.

## Ejemplos resueltos

### Ejemplo 1 · Una matriz 2×2

<!-- check: U3.T02.E1 -->

Hallar autovalores y autoespacios de

$$
A=\begin{pmatrix}5&-2\\6&-2\end{pmatrix}.
$$

**Polinomio característico.** Con la fórmula para $2\times2$: $\operatorname{tr}(A)=5-2=3$ y
$\det(A)=-10+12=2$, así que

$$
p_A(\lambda)=\lambda^2-3\lambda+2=(\lambda-1)(\lambda-2).
$$

Se obtiene lo mismo desarrollando
$\det\begin{pmatrix}\lambda-5&2\\-6&\lambda+2\end{pmatrix}=(\lambda-5)(\lambda+2)+12$.
Los autovalores son $\lambda_1=1$ y $\lambda_2=2$.

**Autoespacio de $1$.**

$$
I-A=\begin{pmatrix}-4&2\\-6&3\end{pmatrix}\sim\begin{pmatrix}-2&1\\0&0\end{pmatrix}
\ \Rightarrow\ y=2x\ \Rightarrow\ E_1(A)=\operatorname{gen}\{(1,2)\}.
$$

**Autoespacio de $2$.**

$$
2I-A=\begin{pmatrix}-3&2\\-6&4\end{pmatrix}\sim\begin{pmatrix}-3&2\\0&0\end{pmatrix}
\ \Rightarrow\ 3x=2y\ \Rightarrow\ E_2(A)=\operatorname{gen}\{(2,3)\}.
$$

**Comprobación.** $A(1,2)^t=(5-4,\,6-4)^t=(1,2)^t$ y $A(2,3)^t=(10-6,\,12-6)^t=(4,6)^t=2(2,3)^t$.

:::tip[Resultado]
Autovalores $1$ y $2$; $E_1(A)=\operatorname{gen}\{(1,2)\}$, $E_2(A)=\operatorname{gen}\{(2,3)\}$.
:::

### Ejemplo 2 · Una matriz 3×3 y la regla de Ruffini

<!-- check: U3.T02.E2 -->

Hallar autovalores y autoespacios de

$$
A=\begin{pmatrix}1&2&-2\\-2&1&2\\-2&2&1\end{pmatrix}.
$$

**Polinomio característico.** Desarrollamos por la primera fila:

$$
\lambda I-A=\begin{pmatrix}\lambda-1&-2&2\\2&\lambda-1&-2\\2&-2&\lambda-1\end{pmatrix},
$$

$$
\begin{aligned}
p_A(\lambda)&=(\lambda-1)\big[(\lambda-1)^2-4\big]-(-2)\big[2(\lambda-1)+4\big]+2\big[-4-2(\lambda-1)\big]\\
&=(\lambda-1)\big[(\lambda-1)^2-4\big]+2(2\lambda+2)+2(-2\lambda-2)\\
&=(\lambda-1)\big[(\lambda-1)^2-4\big].
\end{aligned}
$$

En este caso el factor $\lambda-1$ aparece solo. Si no lo hubiéramos visto y hubiéramos expandido
todo, tendríamos $p_A(\lambda)=\lambda^3-3\lambda^2-\lambda+3$. El polinomio es mónico con
coeficientes enteros, así que sus raíces racionales posibles son los divisores de $3$:
$\pm1,\pm3$. Como $p_A(1)=1-3-1+3=0$, dividimos por $\lambda-1$ con Ruffini:

$$
\begin{array}{c|rrrr}
 & 1 & -3 & -1 & 3\\
1 & & 1 & -2 & -3\\
\hline
 & 1 & -2 & -3 & 0
\end{array}
$$

Queda $p_A(\lambda)=(\lambda-1)(\lambda^2-2\lambda-3)=(\lambda-1)(\lambda-3)(\lambda+1)$. Los
autovalores son $-1$, $1$ y $3$.

**Autoespacios.** Escalonamos $\lambda I-A$ para cada autovalor:

$$
-I-A=\begin{pmatrix}-2&-2&2\\2&-2&-2\\2&-2&-2\end{pmatrix}\sim\begin{pmatrix}1&1&-1\\0&-2&0\\0&0&0\end{pmatrix}
\Rightarrow y=0,\ x=z\Rightarrow E_{-1}(A)=\operatorname{gen}\{(1,0,1)\};
$$

$$
I-A=\begin{pmatrix}0&-2&2\\2&0&-2\\2&-2&0\end{pmatrix}\sim\begin{pmatrix}1&0&-1\\0&1&-1\\0&0&0\end{pmatrix}
\Rightarrow x=y=z\Rightarrow E_{1}(A)=\operatorname{gen}\{(1,1,1)\};
$$

$$
3I-A=\begin{pmatrix}2&-2&2\\2&2&-2\\2&-2&2\end{pmatrix}\sim\begin{pmatrix}1&-1&1\\0&1&-1\\0&0&0\end{pmatrix}
\Rightarrow y=z,\ x=0\Rightarrow E_{3}(A)=\operatorname{gen}\{(0,1,1)\}.
$$

**Comprobación.** $A(1,0,1)^t=(-1,0,-1)^t$, $A(1,1,1)^t=(1,1,1)^t$, $A(0,1,1)^t=(0,3,3)^t$. Además,
los coeficientes cumplen la propiedad: el de $\lambda^2$ es $-3=-\operatorname{tr}(A)$ y el término
independiente es $3=(-1)^3\det(A)$, con $\det(A)=-3$.

:::tip[Resultado]
Autovalores $-1$, $1$, $3$, con $E_{-1}=\operatorname{gen}\{(1,0,1)\}$,
$E_1=\operatorname{gen}\{(1,1,1)\}$ y $E_3=\operatorname{gen}\{(0,1,1)\}$.
:::

## Multiplicidad algebraica y geométrica

Cuando una raíz del polinomio característico se repite, aparecen dos números que miden "cuánto"
autovalor hay.

:::note[Definición]
Sea $\lambda_0$ un autovalor de $A$.

- La **multiplicidad algebraica** $m_a(\lambda_0)$ es la multiplicidad de $\lambda_0$ como raíz de
  $p_A$: el mayor $k$ tal que $(\lambda-\lambda_0)^k$ divide a $p_A(\lambda)$.
- La **multiplicidad geométrica** $m_g(\lambda_0)$ es la dimensión del autoespacio:
  $m_g(\lambda_0)=\dim E_{\lambda_0}(A)=n-\operatorname{rango}(\lambda_0I-A)$.
:::

:::note[Teorema]
Para todo autovalor $\lambda_0$ de $A$,

$$
1\le m_g(\lambda_0)\le m_a(\lambda_0).
$$
:::

**Demostración.** La desigualdad $1\le m_g(\lambda_0)$ vale porque $\lambda_0$ es autovalor: hay
al menos un autovector, y $E_{\lambda_0}(A)\neq\{0\}$.

Para la otra, sea $k=m_g(\lambda_0)$ y sea $\{v_1,\dots,v_k\}$ una base de $E_{\lambda_0}(A)$.
Completamos a una base $\{v_1,\dots,v_k,v_{k+1},\dots,v_n\}$ de $\mathbb{R}^n$ y formamos la matriz
inversible $C=(v_1\mid\cdots\mid v_n)$. Como $Av_j=\lambda_0v_j$ para $j\le k$ y $C^{-1}v_j=e_j$
(porque $Ce_j=v_j$), las primeras $k$ columnas de $C^{-1}AC$ son

$$
C^{-1}Av_j=\lambda_0C^{-1}v_j=\lambda_0e_j,\qquad j=1,\dots,k .
$$

Entonces $C^{-1}AC$ tiene la forma en bloques

$$
C^{-1}AC=\begin{pmatrix}\lambda_0I_k&X\\0&Y\end{pmatrix},
$$

con $X$ de $k\times(n-k)$ e $Y$ de $(n-k)\times(n-k)$. Ahora usamos que
$\lambda I-C^{-1}AC=C^{-1}(\lambda I-A)C$ y que $\det(C^{-1})\det(C)=1$:

$$
p_A(\lambda)=\det(\lambda I-A)=\det\big(C^{-1}(\lambda I-A)C\big)
=\det\begin{pmatrix}(\lambda-\lambda_0)I_k&-X\\0&\lambda I-Y\end{pmatrix}
=(\lambda-\lambda_0)^k\det(\lambda I-Y).
$$

La última igualdad se obtiene desarrollando $k$ veces por la primera columna, que en cada paso
tiene una sola entrada no nula, $\lambda-\lambda_0$. Así, $(\lambda-\lambda_0)^k$ divide a
$p_A(\lambda)$ y $m_a(\lambda_0)\ge k=m_g(\lambda_0)$. $\blacksquare$

En particular, **si $m_a(\lambda_0)=1$, entonces $m_g(\lambda_0)=1$**: para autovalores simples
no hace falta calcular el rango. La comparación interesa en los autovalores repetidos, y será el
criterio central de la [diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/).

### Ejemplo 3 · Autovalor doble con autoespacio de dimensión 1

<!-- check: U3.T02.E3 -->

Hallar autovalores, multiplicidades y autoespacios de

$$
A=\begin{pmatrix}3&0&1\\1&-1&-2\\-1&0&1\end{pmatrix}.
$$

**Polinomio característico.** La segunda columna de $\lambda I-A$ tiene una sola entrada no
nula, así que desarrollamos por ella:

$$
p_A(\lambda)=\det\begin{pmatrix}\lambda-3&0&-1\\-1&\lambda+1&2\\1&0&\lambda-1\end{pmatrix}
=(\lambda+1)\det\begin{pmatrix}\lambda-3&-1\\1&\lambda-1\end{pmatrix}
=(\lambda+1)\big[(\lambda-3)(\lambda-1)+1\big].
$$

Como $(\lambda-3)(\lambda-1)+1=\lambda^2-4\lambda+4=(\lambda-2)^2$, queda

$$
p_A(\lambda)=(\lambda+1)(\lambda-2)^2 ,\qquad m_a(-1)=1,\quad m_a(2)=2 .
$$

**Autoespacio de $2$.**

$$
2I-A=\begin{pmatrix}-1&0&-1\\-1&3&2\\1&0&1\end{pmatrix}\sim\begin{pmatrix}1&0&1\\0&3&3\\0&0&0\end{pmatrix}.
$$

El rango es $2$, así que $m_g(2)=3-2=1$. Las soluciones cumplen $x=-z$, $y=-z$:
$E_2(A)=\operatorname{gen}\{(1,1,-1)\}$.

**Autoespacio de $-1$.** Como $m_a(-1)=1$, ya sabemos que $m_g(-1)=1$. La segunda columna de $A$
es $(0,-1,0)$, es decir $Ae_2=-e_2$: $E_{-1}(A)=\operatorname{gen}\{(0,1,0)\}$.

**Comprobación.** $A(1,1,-1)^t=(3-1,\;1-1+2,\;-1-1)^t=(2,2,-2)^t=2(1,1,-1)^t$.

:::tip[Resultado]
$m_a(2)=2$ pero $m_g(2)=1$, con $E_2(A)=\operatorname{gen}\{(1,1,-1)\}$; $m_a(-1)=m_g(-1)=1$,
con $E_{-1}(A)=\operatorname{gen}\{(0,1,0)\}$. Todos los autovectores de $A$ están en dos rectas:
no hay tres autovectores LI.
:::

## Matrices sin autovalores reales

Si $p_A$ no tiene raíces reales, $A$ no tiene autovalores reales. En $2\times2$ esto ocurre
exactamente cuando el discriminante de $\lambda^2-\operatorname{tr}(A)\lambda+\det(A)$ es negativo.

### Ejemplo 4 · Discriminante negativo

<!-- check: U3.T02.E4 -->

Decidir si

$$
A=\begin{pmatrix}1&-2\\1&3\end{pmatrix}
$$

tiene autovalores reales.

$\operatorname{tr}(A)=4$ y $\det(A)=3+2=5$, así que $p_A(\lambda)=\lambda^2-4\lambda+5$, con
discriminante $16-20=-4<0$. Las raíces son los complejos $2\pm i$.

:::tip[Resultado]
$A$ no tiene autovalores reales: ningún vector no nulo de $\mathbb{R}^2$ conserva su dirección.
:::

Para la rotación de ángulo $\frac{\pi}{2}$, $R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, se obtiene
$p_R(\lambda)=\lambda^2+1$, que tampoco tiene raíces reales: la cuenta confirma lo que la geometría
mostraba en la lección anterior. Los autovalores complejos tienen interpretación (combinan giro
y escala) y se estudian en cursos posteriores; en esta asignatura alcanza con detectarlos.

## Matrices triangulares

:::note[Propiedad]
Si $A$ es triangular (superior o inferior) o diagonal, sus autovalores son las entradas de la
diagonal, repetidas según aparecen: $p_A(\lambda)=(\lambda-a_{11})(\lambda-a_{22})\cdots(\lambda-a_{nn})$.
:::

**Demostración.** Si $A$ es triangular, $\lambda I-A$ también lo es, con diagonal
$\lambda-a_{11},\dots,\lambda-a_{nn}$, y el determinante de una matriz triangular es el producto
de su diagonal. $\blacksquare$

### Ejemplo 5 · Triangular con autovalor repetido

<!-- check: U3.T02.E5 -->

Sea

$$
A=\begin{pmatrix}2&5&-1\\0&-3&4\\0&0&2\end{pmatrix}.
$$

Leemos $p_A(\lambda)=(\lambda-2)^2(\lambda+3)$: $m_a(2)=2$, $m_a(-3)=1$. Para $m_g(2)$:

$$
2I-A=\begin{pmatrix}0&-5&1\\0&5&-4\\0&0&0\end{pmatrix}\sim\begin{pmatrix}0&-5&1\\0&0&-3\\0&0&0\end{pmatrix},
$$

de rango $2$: $m_g(2)=1$ y $E_2(A)=\operatorname{gen}\{(1,0,0)\}$ (de las ecuaciones, $z=0$ e $y=0$).
Para $-3$: $-3I-A=\begin{pmatrix}-5&-5&1\\0&0&-4\\0&0&-5\end{pmatrix}$ da $z=0$, $x=-y$, así que
$E_{-3}(A)=\operatorname{gen}\{(1,-1,0)\}$.

**Comprobación.** $A(1,-1,0)^t=(2-5,\,3,\,0)^t=(-3,3,0)^t=-3(1,-1,0)^t$.

:::tip[Resultado]
Autovalores $2$ (con $m_a=2$, $m_g=1$) y $-3$. Leer los autovalores en la diagonal es inmediato;
los autovectores, en cambio, hay que calcularlos.
:::

:::caution[Errores frecuentes]
- **Escalonar $A$ antes de buscar autovalores.** Las operaciones por filas cambian los
  autovalores. Por ejemplo, $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ tiene autovalores $0$ y $2$,
  pero su forma escalonada $\begin{pmatrix}1&1\\0&0\end{pmatrix}$ tiene autovalores $1$ y $0$. Se
  escalona $\lambda_iI-A$, una vez conocido $\lambda_i$, para hallar el autoespacio.
- **Dividir una fila de $\lambda I-A$ por una expresión con $\lambda$**, como $\lambda-2$. Esa
  expresión se anula justamente en un candidato a autovalor; si se divide, se pierde esa raíz.
- **Calcular $m_g$ con el rango de $A$** en lugar del de $\lambda I-A$.
- **Suponer que $m_g=m_a$ siempre.** El ejemplo 3 tiene $m_a(2)=2$ y $m_g(2)=1$.
- **Obtener un sistema compatible determinado al buscar $E_\lambda$.** Si $(\lambda I-A)x=0$ solo
  tiene la solución nula, $\lambda$ no es autovalor: hay un error en el polinomio o en sus raíces.
- **Equivocar signos al pasar de $\det(A-\lambda I)$ a $\det(\lambda I-A)$.** Para $n$ impar
  difieren en el signo; las raíces son las mismas.
:::

## Autoevaluación

<details>
<summary>1. Una matriz 2 × 2 tiene traza 7 y determinante 10. ¿Cuáles son sus autovalores?</summary>

$p_A(\lambda)=\lambda^2-7\lambda+10=(\lambda-2)(\lambda-5)$: los autovalores son $2$ y $5$.

</details>

<details>
<summary>2. ¿Puede una matriz 3 × 3 real no tener autovalores reales?</summary>

No: $p_A$ tiene grado $3$, impar, y todo polinomio real de grado impar tiene al menos una raíz
real.

</details>

<details>
<summary>3. Si el polinomio característico es (λ − 4)³ y el rango de 4I − A es 1, ¿cuánto valen las multiplicidades?</summary>

$m_a(4)=3$ y $m_g(4)=3-1=2$.

</details>

:::tip[En resumen]
- $\lambda$ es autovalor de $A$ si y solo si $p_A(\lambda)=\det(\lambda I-A)=0$.
- $p_A$ es mónico de grado $n$:
  $p_A(\lambda)=\lambda^n-\operatorname{tr}(A)\lambda^{n-1}+\dots+(-1)^n\det(A)$; en $2\times2$,
  $\lambda^2-\operatorname{tr}(A)\lambda+\det(A)$.
- $\det(A-\lambda I)=(-1)^np_A(\lambda)$ tiene las mismas raíces.
- Procedimiento: polinomio factorizado, raíces reales, $E_{\lambda_i}=\operatorname{nul}(\lambda_iI-A)$
  para cada una, verificación.
- $1\le m_g(\lambda)\le m_a(\lambda)$; si $m_a(\lambda)=1$, entonces $m_g(\lambda)=1$.
- En una triangular los autovalores son las entradas diagonales.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 4.2, Determinantes
  (p. 274), y sección 4.3, Eigenvalores y eigenvectores de matrices $n\times n$ (p. 303), donde
  se definen las multiplicidades algebraica y geométrica.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: sección sobre la ecuación característica.
- Repaso: [determinantes](/algebra-ii/repaso/determinantes/) y
  [polinomios](/algebra-ii/repaso/polinomios/) (raíces racionales y Ruffini).
- Anterior: [3.1 Autovalores y autovectores](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/).
  Siguiente: [3.3 Propiedades](/algebra-ii/unidad-3/teoria/propiedades/).
