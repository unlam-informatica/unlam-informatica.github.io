---
title: Potencias de una matriz
description: La fórmula A^k = C D^k C^{-1}, potencias enteras negativas, inversibilidad de polinomios en A, límites de A^k y costo computacional frente a la exponenciación binaria.
slug: algebra-ii/unidad-3/teoria/potencias
sidebar:
  order: 6
  label: 3.6 Potencias
---

## Para qué sirve

Muchos procesos discretos se describen con $x_{k+1}=Ax_k$, de modo que el estado después de $k$
pasos es $x_k=A^kx_0$. Calcular $A^k$ multiplicando $A$ por sí misma $k-1$ veces es inviable
para $k$ grande y no dice nada sobre qué pasa cuando $k\to\infty$. Si $A$ es diagonalizable,
$A^k=CD^kC^{-1}$ y $D^k$ se obtiene **elevando cada autovalor a la $k$**: una fórmula cerrada en
$k$ de la que se leen el crecimiento, el decaimiento y los límites. Esta es la herramienta de las
dos últimas lecciones de la unidad ([recurrencias](/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/)
y [cadenas de Markov](/algebra-ii/unidad-3/teoria/cadenas-de-markov/)).

## Potencias de una matriz diagonalizable

:::note[Teorema]
Si $A=CDC^{-1}$ con $D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$, entonces para todo entero
$k\ge0$

$$
A^k=CD^kC^{-1},\qquad D^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k).
$$
:::

**Demostración.** Por inducción en $k$. Para $k=0$, $A^0=I=CIC^{-1}=CD^0C^{-1}$. Si
$A^k=CD^kC^{-1}$, entonces

$$
A^{k+1}=A^kA=(CD^kC^{-1})(CDC^{-1})=CD^k(C^{-1}C)DC^{-1}=CD^{k+1}C^{-1}.
$$

Por otra parte, el producto de matrices diagonales es diagonal y multiplica las entradas
correspondientes; por inducción, $D^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k)$.
$\blacksquare$

Es el caso particular, para la semejanza $A=CBC^{-1}$ con $B$ diagonal, de la fórmula
$A^k=CB^kC^{-1}$ de la [lección 3.4](/algebra-ii/unidad-3/teoria/matrices-semejantes/). Las columnas
de $A^k$ se leen como combinaciones de los autovectores: si $x_0=\sum_j\beta_jv_j$, entonces

$$
A^kx_0=\sum_{j=1}^n\beta_j\lambda_j^kv_j.
$$

Así, a largo plazo domina el autovalor de **mayor módulo** (siempre que su coeficiente $\beta_j$ no
sea nulo).

### Potencias enteras negativas

:::note[Propiedad]
Si $A=CDC^{-1}$ es inversible, entonces todos los $\lambda_i\neq0$ y para todo $k\in\mathbb{Z}$,
$A^k=CD^kC^{-1}$, con $D^{-k}=\operatorname{diag}(\lambda_1^{-k},\dots,\lambda_n^{-k})$.
:::

**Demostración.** $A$ es inversible si y solo si $\det(A)=\det(D)=\lambda_1\cdots\lambda_n\neq0$.
Entonces $A^{-1}=(CDC^{-1})^{-1}=CD^{-1}C^{-1}$, y aplicando el teorema a $A^{-1}=CD^{-1}C^{-1}$ (con
$D^{-1}$ diagonal) se obtiene $A^{-k}=CD^{-k}C^{-1}$ para $k\ge0$. $\blacksquare$

## Polinomios en $A$ e inversibilidad

Sea $p(x)=c_mx^m+\dots+c_1x+c_0$ y $p(A)=c_mA^m+\dots+c_1A+c_0I$.

:::note[Propiedad]
Si $A=CDC^{-1}$, entonces $p(A)=C\,p(D)\,C^{-1}$ con $p(D)=\operatorname{diag}(p(\lambda_1),\dots,p(\lambda_n))$.
En consecuencia, $\det p(A)=p(\lambda_1)\cdots p(\lambda_n)$ y

$$
p(A)\ \text{es inversible}\iff p(\lambda_i)\neq0\ \text{para todo autovalor }\lambda_i\text{ de }A.
$$
:::

**Demostración.** Por el teorema, $p(A)=\sum_jc_jCD^jC^{-1}=C\big(\sum_jc_jD^j\big)C^{-1}=Cp(D)C^{-1}$,
y $\sum_jc_jD^j$ es diagonal con entradas $p(\lambda_i)$. El determinante de $p(A)$ es el de $p(D)$,
el producto de su diagonal, y es no nulo si y solo si $p(A)$ es inversible. $\blacksquare$

Esto permite decidir la inversibilidad de expresiones como $A^{100}-I$ o $A^2+A$ **sin calcular
la matriz**: basta evaluar $p$ en los autovalores. Si $A$ no es diagonalizable sobre $\mathbb{R}$,
la equivalencia puede fallar (ejemplo 5).

## Límites de $A^k$

Decimos que $A^k\to L$ si cada entrada de $A^k$ converge a la entrada correspondiente de $L$.

:::note[Propiedad]
Si $A=CDC^{-1}$ es diagonalizable, la sucesión $A^k$ converge si y solo si cada autovalor cumple
$|\lambda_i|<1$ o $\lambda_i=1$. En ese caso

$$
\lim_{k\to\infty}A^k=C\,\operatorname{diag}(\ell_1,\dots,\ell_n)\,C^{-1},\qquad
\ell_i=\begin{cases}0&\text{si }|\lambda_i|<1,\\1&\text{si }\lambda_i=1.\end{cases}
$$
:::

**Demostración.** $\lambda^k$ converge si y solo si $|\lambda|<1$ (límite $0$) o $\lambda=1$ (límite
$1$): para $|\lambda|>1$ o $\lambda=-1$ diverge u oscila. Como $A^k=CD^kC^{-1}$ y
$D^k=C^{-1}A^kC$, la sucesión $A^k$ converge si y solo si lo hace $D^k$, es decir, cada
$\lambda_i^k$; el límite se obtiene multiplicando por $C$ y $C^{-1}$, que son operaciones continuas.
$\blacksquare$

Si hay un autovalor con $|\lambda|>1$ y un vector inicial con $\beta_j\neq0$ para ese autovector,
$\lVert A^kx_0\rVert\to\infty$. Si algún autovalor es $-1$, $A^k x_0$ oscila (ver las cadenas
periódicas de la lección 3.8).

## Costo computacional

Calcular $A^k$ para $A\in\mathbb{R}^{n\times n}$ cuesta, con el algoritmo directo, $k-1$
productos de matrices, cada uno de orden $n^3$ operaciones: $O(kn^3)$. Con **exponenciación
binaria** (elevar al cuadrado y multiplicar según los bits de $k$) alcanzan del orden de
$2\log_2k$ productos: $O(n^3\log k)$, y no hace falta diagonalizar.

```python
def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(m)) for j in range(p)] for i in range(n)]

def mat_pow(A, k):
    """A^k para k >= 0, por exponenciación binaria (enteros exactos)."""
    resultado = [[int(i == j) for j in range(len(A))] for i in range(len(A))]
    while k > 0:
        if k & 1:
            resultado = mat_mul(resultado, A)
        A = mat_mul(A, A)
        k >>= 1
    return resultado
```

<!-- check: U3.T06.E6 -->

Por ejemplo, `mat_pow([[4, -2], [1, 1]], 10)` devuelve
`[[117074, -116050], [58025, -57001]]`, el mismo resultado que el ejemplo 1 de abajo.

¿Entonces para qué diagonalizar? Porque aporta **información**, no solo velocidad: una fórmula
cerrada $A^k=\sum_j\lambda_j^kP_j$ (con $P_j$ matrices fijas), el comportamiento para $k\to\infty$, la
inversibilidad de $p(A)$ y la dependencia con un parámetro. Computacionalmente, una vez hallados
$C$, $D$ y $C^{-1}$, cada potencia cuesta $n$ potencias escalares y dos productos de matrices,
independientemente de $k$ salvo por las $n$ potencias de números. Pero las cuentas de punto
flotante con autovalores irracionales acumulan error, y para enteros grandes la exponenciación
binaria con aritmética exacta es la opción estándar en algoritmos.

## Ejemplos resueltos

### Ejemplo 1 · Fórmula de $A^k$ y cálculo de $A^{10}$

<!-- check: U3.T06.E1 -->

Hallar $A^k$ para $A=\begin{pmatrix}4&-2\\1&1\end{pmatrix}$ y calcular $A^{10}$.

Por el ejemplo 1 de la [lección 3.5](/algebra-ii/unidad-3/teoria/diagonalizacion/),
$A=CDC^{-1}$ con $C=\begin{pmatrix}1&2\\1&1\end{pmatrix}$, $D=\operatorname{diag}(2,3)$ y
$C^{-1}=\begin{pmatrix}-1&2\\1&-1\end{pmatrix}$. Entonces

$$
A^k=CD^kC^{-1}=\begin{pmatrix}1&2\\1&1\end{pmatrix}\begin{pmatrix}2^k&0\\0&3^k\end{pmatrix}\begin{pmatrix}-1&2\\1&-1\end{pmatrix}
=\begin{pmatrix}2^k&2\cdot3^k\\2^k&3^k\end{pmatrix}\begin{pmatrix}-1&2\\1&-1\end{pmatrix},
$$

$$
A^k=\begin{pmatrix}-2^k+2\cdot3^k&\ 2\cdot2^k-2\cdot3^k\\[2pt]-2^k+3^k&\ 2\cdot2^k-3^k\end{pmatrix}.
$$

**Comprobación.** Para $k=1$: $\begin{pmatrix}-2+6&4-6\\-2+3&4-3\end{pmatrix}=A$. Para $k=0$ se
obtiene $I$. Con $2^{10}=1024$ y $3^{10}=59049$:

$$
A^{10}=\begin{pmatrix}-1024+118098&2048-118098\\-1024+59049&2048-59049\end{pmatrix}
=\begin{pmatrix}117074&-116050\\58025&-57001\end{pmatrix}.
$$

:::tip[Resultado]
$A^k=\begin{pmatrix}-2^k+2\cdot3^k&2^{k+1}-2\cdot3^k\\-2^k+3^k&2^{k+1}-3^k\end{pmatrix}$ y
$A^{10}=\begin{pmatrix}117074&-116050\\58025&-57001\end{pmatrix}$.
:::

### Ejemplo 2 · Potencias negativas

<!-- check: U3.T06.E2 -->

Calcular $A^{-1}$ y $A^{-2}$ para la misma matriz.

Los autovalores $2$ y $3$ son no nulos, y la fórmula vale para $k=-1$ y $k=-2$:

$$
A^{-1}:\ \begin{pmatrix}-\tfrac12+\tfrac23&1-\tfrac23\\-\tfrac12+\tfrac13&1-\tfrac13\end{pmatrix}
=\begin{pmatrix}\tfrac16&\tfrac13\\-\tfrac16&\tfrac23\end{pmatrix},\qquad
A^{-2}:\ \begin{pmatrix}-\tfrac14+\tfrac29&\tfrac12-\tfrac29\\-\tfrac14+\tfrac19&\tfrac12-\tfrac19\end{pmatrix}
=\begin{pmatrix}-\tfrac1{36}&\tfrac5{18}\\-\tfrac5{36}&\tfrac7{18}\end{pmatrix}.
$$

**Comprobación.** $\det(A)=6$ y la fórmula de la inversa $2\times2$ da
$A^{-1}=\tfrac16\begin{pmatrix}1&2\\-1&4\end{pmatrix}$, que coincide. Además,
$A^{-1}A^{-1}=A^{-2}$ y $A\,A^{-1}=I$.

:::tip[Resultado]
$A^{-1}=\begin{pmatrix}\frac16&\frac13\\-\frac16&\frac23\end{pmatrix}$ y
$A^{-2}=\begin{pmatrix}-\frac1{36}&\frac5{18}\\-\frac5{36}&\frac7{18}\end{pmatrix}$.
:::

### Ejemplo 3 · Inversibilidad de polinomios en $A$

<!-- check: U3.T06.E3 -->

Sea $A=\begin{pmatrix}0&1&1\\1&0&1\\3&-3&2\end{pmatrix}$. Decidir si son inversibles
$A^{100}-I$, $A^2+A$, $A^2+I$, $A^3-3A$ y $A^{101}+I$, y calcular el determinante cuando no sea nulo.

**Autovalores y diagonalización.** $p_A(\lambda)=\lambda^3-2\lambda^2-\lambda+2=(\lambda-2)(\lambda^2-1)$,
con autovalores $-1,1,2$. Los autovectores son $(1,0,-1)$ para $-1$, $(1,1,0)$ para $1$ y $(1,1,1)$
para $2$; como son tres autovalores distintos, $A$ es diagonalizable con

$$
C=\begin{pmatrix}1&1&1\\0&1&1\\-1&0&1\end{pmatrix},\qquad C^{-1}AC=\operatorname{diag}(-1,1,2).
$$

**Evaluación en los autovalores.**

| polinomio $p$ | $p(-1)$ | $p(1)$ | $p(2)$ | $p(A)$ |
|---|---|---|---|---|
| $x^{100}-1$ | $0$ | $0$ | $2^{100}-1$ | no inversible |
| $x^2+x$ | $0$ | $2$ | $6$ | no inversible |
| $x^2+1$ | $2$ | $2$ | $5$ | inversible, $\det=20$ |
| $x^3-3x$ | $2$ | $-2$ | $2$ | inversible, $\det=-8$ |
| $x^{101}+1$ | $0$ | $2$ | $2^{101}+1$ | no inversible |

**Comprobación.** $A^3-3A=\begin{pmatrix}6&-8&4\\4&-6&4\\0&0&2\end{pmatrix}$, de determinante
$2\cdot(6\cdot(-6)+8\cdot4)=2\cdot(-4)=-8$, como indica la tabla.

:::tip[Resultado]
Solo $A^2+I$ y $A^3-3A$ son inversibles, con $\det(A^2+I)=20$ y $\det(A^3-3A)=-8$.
:::

### Ejemplo 4 · Límite de $A^k$

<!-- check: U3.T06.E4 -->

Sea $A=\begin{pmatrix}\frac32&-\frac12\\1&0\end{pmatrix}$. Estudiar el límite de $A^k$.

**Diagonalización.** $\operatorname{tr}(A)=\tfrac32$ y $\det(A)=\tfrac12$, entonces
$p_A(\lambda)=\lambda^2-\tfrac32\lambda+\tfrac12=(\lambda-1)(\lambda-\tfrac12)$. Los autovectores
son $(1,1)$ para $1$ y $(1,2)$ para $\tfrac12$: $A(1,2)^t=(\tfrac32-1,\,1)^t=\tfrac12(1,2)^t$. Con
$C=\begin{pmatrix}1&1\\1&2\end{pmatrix}$ y $C^{-1}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$,

$$
A^k=C\begin{pmatrix}1&0\\0&2^{-k}\end{pmatrix}C^{-1}
=\begin{pmatrix}2-2^{-k}&-1+2^{-k}\\2-2\cdot2^{-k}&-1+2\cdot2^{-k}\end{pmatrix}.
$$

**Límite.** Como $2^{-k}\to0$,

$$
A^k\to L=\begin{pmatrix}2&-1\\2&-1\end{pmatrix},\qquad A^k-L=2^{-k}\begin{pmatrix}-1&1\\-2&2\end{pmatrix}.
$$

**Comprobación.** $L^2=L$ (un límite de potencias de $A$ cumple $AL=L$ y $L^2=L$) y $AL=L$:
$\begin{pmatrix}\frac32&-\frac12\\1&0\end{pmatrix}\begin{pmatrix}2&-1\\2&-1\end{pmatrix}
=\begin{pmatrix}3-1&-\frac32+\frac12\\2&-1\end{pmatrix}=L$.

:::tip[Resultado]
$A^k$ converge a $L=\begin{pmatrix}2&-1\\2&-1\end{pmatrix}$ y el error decae como $2^{-k}$. Para el
vector inicial $x_0=(a_1,a_0)$, $A^kx_0\to(2a_1-a_0)(1,1)$: la sucesión
$a_{n+1}=\tfrac32a_n-\tfrac12a_{n-1}$ converge a $2a_1-a_0$.
:::

### Ejemplo 5 · Cuando no hay autovalores reales

<!-- check: U3.T06.E5 -->

Para la rotación $R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $p_R(\lambda)=\lambda^2+1$ no tiene raíces
reales y $R$ no es diagonalizable sobre $\mathbb{R}$. Sin embargo, $R^2=-I$, de modo que
$p(R)=R^2+I=0$ **no es inversible**, aunque no haya ningún autovalor real en el que $p(x)=x^2+1$
se anule. La equivalencia "$p(A)$ inversible $\iff$ $p(\lambda_i)\neq0$" necesita que $A$ sea
diagonalizable sobre $\mathbb{R}$.

Tampoco hay fórmula $CD^kC^{-1}$ real para $N=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, que no es
diagonalizable, pero sus potencias se calculan por inducción: $N^k=\begin{pmatrix}1&k\\0&1\end{pmatrix}$.

:::caution[Errores frecuentes]
- **Elevar la matriz $C$ o $C^{-1}$ a la $k$.** La fórmula es $CD^kC^{-1}$, no $C^kD^kC^{-k}$.
- **Elevar las entradas de $A$ a la $k$.** $A^k\neq(a_{ij}^k)$; solo en una diagonal se eleva
  entrada a entrada.
- **Cambiar el orden de $C$ y $D$.** $A^k=CD^kC^{-1}$, con $D^k$ en el mismo orden que las
  columnas de $C$.
- **Usar $A^k=CD^kC^{-1}$ sin que $A$ sea diagonalizable.** No hay $C$ ni $D$; para
  $N=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ hay que usar otro argumento.
- **Afirmar que $A^k\to0$ si hay autovalores de módulo $1$.** Para $\lambda=1$ el límite no es $0$;
  para $\lambda=-1$ no hay límite.
- **Olvidar que $A^{-k}$ exige $A$ inversible.** Un autovalor nulo impide potencias negativas.
- **Pensar que $p(A)$ inversible equivale a que $p$ no tenga raíces reales.** Hay que evaluar $p$
  en los autovalores de $A$, no en cualquier número.
:::

## Autoevaluación

<details>
<summary>1. Si los autovalores de A son 2, −1 y 1/2, ¿cuáles son los de A⁵ y A⁻²?</summary>

$A^5$: $32,\,-1,\,\tfrac1{32}$. $A^{-2}$: $\tfrac14,\,1,\,4$.

</details>

<details>
<summary>2. ¿Converge Aᵏ si A diagonalizable tiene autovalores 1 y −1/3?</summary>

Sí: $1^k=1$ y $(-\tfrac13)^k\to0$. El límite es $C\operatorname{diag}(1,0)C^{-1}$.

</details>

<details>
<summary>3. ¿Cuántos productos de matrices requiere calcular A¹⁰⁰⁰ por exponenciación binaria?</summary>

$1000=1111101000_2$ tiene $10$ cifras y seis unos: del orden de $9$ cuadrados y $6$ productos del
resultado parcial, unos $15$ productos en total (contra $999$ del método directo).

</details>

:::tip[En resumen]
- $A=CDC^{-1}\Rightarrow A^k=CD^kC^{-1}$ con $D^k=\operatorname{diag}(\lambda_i^k)$; vale para
  $k<0$ si $A$ es inversible.
- $p(A)=Cp(D)C^{-1}$; $p(A)$ es inversible si y solo si $p(\lambda_i)\neq0$ para todo autovalor.
- Una diagonalizable tiene $A^k\to L$ si y solo si cada $\lambda_i$ cumple $|\lambda_i|<1$ o
  $\lambda_i=1$.
- Costo: exponenciación binaria, $O(n^3\log k)$ sin diagonalizar; la diagonalización da además la
  fórmula cerrada y el límite.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 4.4, Semejanza y
  diagonalización (p. 312), con potencias de matrices diagonalizables.
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: sección de diagonalización y potencias.
- Anterior: [3.5 Diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/). Siguiente:
  [3.7 Relaciones de recurrencia](/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/).
