---
title: Relaciones de recurrencia lineales
description: Recurrencias lineales de orden 2 resueltas con la matriz compañera, el polinomio característico y la diagonalización; Fibonacci completo con la fórmula de Binet y el número áureo, el caso de raíz doble y aplicaciones de conteo y análisis de algoritmos.
slug: algebra-ii/unidad-3/teoria/relaciones-de-recurrencia
sidebar:
  order: 7
  label: 3.7 Relaciones de recurrencia
---

## Para qué sirve

Una **relación de recurrencia** define cada término de una sucesión a partir de los anteriores. Es
la forma natural de describir algoritmos recursivos, problemas de conteo y modelos de crecimiento,
pero para saber cuánto vale $a_{1000}$ o cómo crece $a_n$ hace falta una **fórmula cerrada**, es
decir, una expresión en $n$ que no dependa de los términos previos. Los autovalores la
proporcionan: la recurrencia se escribe como un sistema $x_{n+1}=Ax_n$, y $x_n=A^nx_0$ se calcula
con la [diagonalización](/algebra-ii/unidad-3/teoria/diagonalizacion/) y las
[potencias](/algebra-ii/unidad-3/teoria/potencias/). El caso más famoso es el de la sucesión de
Fibonacci.

## Recurrencias lineales homogéneas de orden 2

:::note[Definición]
Una **relación de recurrencia lineal homogénea de orden 2 con coeficientes constantes** es

$$
a_{n+1}=r\,a_n+s\,a_{n-1}\qquad(n\ge1),\qquad r,s\in\mathbb{R},\ s\neq0,
$$

junto con las **condiciones iniciales** $a_0$ y $a_1$. Los dos primeros términos determinan toda la
sucesión; el conjunto de **soluciones** (sucesiones que cumplen la relación) queda en
correspondencia con los pares $(a_0,a_1)$.
:::

"Lineal" significa que los términos aparecen sin potencias ni productos; "homogénea", que no hay un
término independiente; "orden 2", que se usan los dos términos anteriores.

### Forma matricial y matriz compañera

Definimos el vector de estado $x_n=\begin{pmatrix}a_{n+1}\\a_n\end{pmatrix}$. Entonces

$$
x_{n+1}=\begin{pmatrix}a_{n+2}\\a_{n+1}\end{pmatrix}=\begin{pmatrix}r\,a_{n+1}+s\,a_n\\a_{n+1}\end{pmatrix}
=\underbrace{\begin{pmatrix}r&s\\1&0\end{pmatrix}}_{A}\begin{pmatrix}a_{n+1}\\a_n\end{pmatrix}=Ax_n,
$$

y por lo tanto $x_n=A^nx_0$ con $x_0=(a_1,a_0)^t$. La matriz $A$ se llama **matriz compañera** de
la recurrencia. Su polinomio característico es

$$
p_A(\lambda)=\lambda^2-\operatorname{tr}(A)\lambda+\det(A)=\lambda^2-r\lambda-s,
$$

la llamada **ecuación característica** de la recurrencia: se obtiene reemplazando $a_n$ por
$\lambda^n$ en la relación y dividiendo por $\lambda^{n-1}$. Además, si $\lambda$ es raíz de
$p_A$, el vector $(\lambda,1)^t$ es autovector de $A$:

$$
A\begin{pmatrix}\lambda\\1\end{pmatrix}=\begin{pmatrix}r\lambda+s\\\lambda\end{pmatrix}=\begin{pmatrix}\lambda^2\\\lambda\end{pmatrix}=\lambda\begin{pmatrix}\lambda\\1\end{pmatrix}.
$$

**Orden $k$.** Para $a_{n+k}=r_1a_{n+k-1}+\dots+r_ka_n$ el vector de estado es
$x_n=(a_{n+k-1},\dots,a_n)^t$, la matriz compañera $k\times k$ tiene en la primera fila
$(r_1,\dots,r_k)$, unos en la subdiagonal y ceros en el resto, y su polinomio característico es
$\lambda^k-r_1\lambda^{k-1}-\dots-r_k$. El procedimiento es el mismo; en la lección trabajamos el
orden $2$.

### Término general con raíces distintas

:::note[Teorema]
Si $\lambda^2-r\lambda-s$ tiene dos raíces reales distintas $\lambda_1\neq\lambda_2$, la solución
con condiciones iniciales $a_0,a_1$ es

$$
a_n=c_1\lambda_1^n+c_2\lambda_2^n,
$$

donde $c_1,c_2$ son la única solución de $c_1+c_2=a_0$, $c_1\lambda_1+c_2\lambda_2=a_1$.
:::

**Demostración.** Como $\lambda_1\neq\lambda_2$, la matriz compañera $A$ tiene dos autovectores
independientes $w_1=(\lambda_1,1)$ y $w_2=(\lambda_2,1)$, y es diagonalizable. Escribimos
$x_0=c_1w_1+c_2w_2$; el sistema para $(c_1,c_2)$ tiene matriz $C=(w_1\mid w_2)$, inversible, así
que $c_1,c_2$ existen y son únicos; sus ecuaciones son las dos coordenadas de $x_0=(a_1,a_0)^t$: la
primera dice $c_1\lambda_1+c_2\lambda_2=a_1$ y la segunda, $c_1+c_2=a_0$. Por
$A^nw_i=\lambda_i^nw_i$,

$$
x_n=A^nx_0=c_1\lambda_1^nw_1+c_2\lambda_2^nw_2,
$$

y la **segunda coordenada** de $x_n=(a_{n+1},a_n)^t$ es $a_n=c_1\lambda_1^n+c_2\lambda_2^n$. $\blacksquare$

**Procedimiento.** (1) Escribir la ecuación característica $\lambda^2-r\lambda-s=0$ y hallar las
raíces. (2) Plantear $a_n=c_1\lambda_1^n+c_2\lambda_2^n$. (3) Usar $a_0$ y $a_1$ para obtener $c_1$ y
$c_2$. (4) Verificar con los primeros términos.

## Ejemplos resueltos

### Ejemplo 1 · Una recurrencia con raíces enteras

<!-- check: U3.T07.E1 -->

Resolver $a_{n+1}=a_n+6a_{n-1}$ con $a_0=0$ y $a_1=5$.

**Matriz compañera.** $A=\begin{pmatrix}1&6\\1&0\end{pmatrix}$, con
$p_A(\lambda)=\lambda^2-\lambda-6=(\lambda-3)(\lambda+2)$. Los autovalores son $3$ y $-2$, con
autovectores $(3,1)$ y $(-2,1)$.

**Diagonalización.** $C=\begin{pmatrix}3&-2\\1&1\end{pmatrix}$, $D=\operatorname{diag}(3,-2)$ y
$C^{-1}=\tfrac15\begin{pmatrix}1&2\\-1&3\end{pmatrix}$. Con $x_0=(a_1,a_0)^t=(5,0)^t$,

$$
C^{-1}x_0=\tfrac15\begin{pmatrix}5\\-5\end{pmatrix}=\begin{pmatrix}1\\-1\end{pmatrix}\ \Rightarrow\ c_1=1,\ c_2=-1,
\qquad a_n=3^n-(-2)^n .
$$

**Comprobación.** Los términos de la fórmula son $a_0=0$, $a_1=3+2=5$, $a_2=9-4=5$, $a_3=27+8=35$,
$a_4=81-16=65$, y la recurrencia da lo mismo: $a_2=5+6\cdot0=5$, $a_3=5+6\cdot5=35$,
$a_4=35+6\cdot5=65$.

:::tip[Resultado]
$a_n=3^n-(-2)^n$. Crece como $3^n$: el autovalor de mayor módulo domina.
:::

### Ejemplo 2 · Fibonacci

<!-- check: U3.T07.E2 -->

La sucesión de Fibonacci es $F_{n+1}=F_n+F_{n-1}$ con $F_0=0$, $F_1=1$: $0,1,1,2,3,5,8,13,\dots$
Hallar una fórmula para $F_n$ y estudiar $F_{n+1}/F_n$.

**Matriz compañera.** $A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ y $x_n=(F_{n+1},F_n)^t$, con
$x_0=(1,0)^t$. El polinomio característico es

$$
p_A(\lambda)=\lambda^2-\lambda-1,\qquad
\lambda_1=\varphi=\frac{1+\sqrt5}{2}\approx1{,}618,\qquad \lambda_2=\psi=\frac{1-\sqrt5}{2}\approx-0{,}618 .
$$

Valen $\varphi+\psi=1$, $\varphi\psi=-1$, $\varphi-\psi=\sqrt5$ y $\varphi^2=\varphi+1$,
$\psi^2=\psi+1$. Los autovectores son $(\varphi,1)$ y $(\psi,1)$.

**Diagonalización.** Con $C=\begin{pmatrix}\varphi&\psi\\1&1\end{pmatrix}$, $\det(C)=\varphi-\psi=\sqrt5$
y $C^{-1}=\frac1{\sqrt5}\begin{pmatrix}1&-\psi\\-1&\varphi\end{pmatrix}$:

$$
C^{-1}x_0=\frac1{\sqrt5}\begin{pmatrix}1\\-1\end{pmatrix}\ \Rightarrow\ c_1=\frac1{\sqrt5},\ c_2=-\frac1{\sqrt5},
$$

y por el teorema del término general (**fórmula de Binet**):

$$
F_n=\frac{\varphi^n-\psi^n}{\sqrt5}=\frac1{\sqrt5}\left[\left(\frac{1+\sqrt5}{2}\right)^n-\left(\frac{1-\sqrt5}{2}\right)^n\right].
$$

**Verificación de términos.** Usamos $\varphi^2=\varphi+1$ para calcular las potencias: $\varphi^3=2\varphi+1$,
$\varphi^4=3\varphi+2$, $\varphi^5=5\varphi+3$ (y lo mismo para $\psi$, que satisface la misma
ecuación). Entonces

$$
F_2=\frac{\varphi^2-\psi^2}{\sqrt5}=\frac{(\varphi-\psi)(\varphi+\psi)}{\sqrt5}=1,\qquad
F_3=\frac{2(\varphi-\psi)}{\sqrt5}=2,\qquad F_4=\frac{3(\varphi-\psi)}{\sqrt5}=3,\qquad F_5=5 .
$$

Y numéricamente, $\varphi^{10}/\sqrt5\approx55{,}0036$ y $\psi^{10}/\sqrt5\approx0{,}0036$, con
diferencia $F_{10}=55$. Como $|\psi^n/\sqrt5|<\tfrac12$ para todo $n$, **$F_n$ es el entero más
cercano a $\varphi^n/\sqrt5$**.

**El cociente $F_{n+1}/F_n$.** Calculamos

$$
F_{n+1}-\varphi F_n=\frac{\varphi^{n+1}-\psi^{n+1}-\varphi^{n+1}+\varphi\psi^n}{\sqrt5}=\frac{\psi^n(\varphi-\psi)}{\sqrt5}=\psi^n .
$$

Dividiendo por $F_n\ge1$ (para $n\ge1$): $\ \dfrac{F_{n+1}}{F_n}-\varphi=\dfrac{\psi^n}{F_n}$, y
$\left|\psi^n/F_n\right|\le|\psi|^n\to0$ porque $|\psi|<1$. Por lo tanto

$$
\lim_{n\to\infty}\frac{F_{n+1}}{F_n}=\varphi=\frac{1+\sqrt5}{2},
$$

el **número áureo**. Es la ley de los autovectores: $x_n=(F_{n+1},F_n)^t$ se acerca a la dirección
del autovector dominante $(\varphi,1)$, y el cociente de sus coordenadas tiende a $\varphi$.
Numéricamente, $F_{31}/F_{30}=1\,346\,269/832\,040\approx1{,}6180339888$.

:::tip[Resultado]
$F_n=\dfrac{\varphi^n-\psi^n}{\sqrt5}$, $F_{10}=55$, $F_{30}=832\,040$ y $F_{n+1}/F_n\to\varphi\approx1{,}618$. La
fórmula usa irracionales pero da siempre enteros.
:::

## Raíz doble: la matriz compañera no es diagonalizable

Si $\lambda^2-r\lambda-s=(\lambda-\mu)^2$ con $\mu\neq0$, la ecuación característica tiene una única
raíz $\mu$, con $r=2\mu$ y $s=-\mu^2$, y la matriz compañera es

$$
A=\begin{pmatrix}2\mu&-\mu^2\\1&0\end{pmatrix},\qquad A-\mu I=\begin{pmatrix}\mu&-\mu^2\\1&-\mu\end{pmatrix}.
$$

La primera fila de $A-\mu I$ es $\mu$ veces la segunda: el rango es $1$ y $m_g(\mu)=1<2=m_a(\mu)$.
**La matriz compañera no es diagonalizable** y el método anterior no sirve tal cual. Pero se
puede completar con el siguiente resultado.

:::note[Teorema]
Si la ecuación característica tiene raíz doble $\mu\neq0$, la solución con condiciones iniciales
$a_0,a_1$ es

$$
a_n=(c_1+c_2n)\mu^n,\qquad c_1=a_0,\quad c_2=\frac{a_1}{\mu}-a_0 .
$$
:::

**Demostración.** (i) $\mu^n$ es solución: es el caso de una raíz de la ecuación característica.
(ii) $n\mu^n$ también:

$$
(n+1)\mu^{n+1}-2\mu\cdot n\mu^n+\mu^2(n-1)\mu^{n-1}=\mu^{n+1}\big[(n+1)-2n+(n-1)\big]=0 .
$$

(iii) Cualquier solución queda determinada por $(a_0,a_1)$, y las soluciones $\mu^n$ y $n\mu^n$
tienen pares iniciales $(1,\mu)$ y $(0,\mu)$, linealmente independientes porque
$\det\begin{pmatrix}1&0\\\mu&\mu\end{pmatrix}=\mu\neq0$. Entonces generan todos los pares iniciales
y, por lo tanto, todas las soluciones. Las constantes salen de $a_0=c_1$ y $a_1=(c_1+c_2)\mu$.
$\blacksquare$

### Ejemplo 3 · Raíz doble con condiciones iniciales

<!-- check: U3.T07.E3 -->

Resolver $a_{n+1}=4a_n-4a_{n-1}$ con $a_0=1$ y $a_1=4$.

La ecuación característica es $\lambda^2-4\lambda+4=(\lambda-2)^2$, con raíz doble $\mu=2$. La matriz
compañera $A=\begin{pmatrix}4&-4\\1&0\end{pmatrix}$ tiene $E_2(A)=\operatorname{gen}\{(2,1)\}$ y
$m_g(2)=1$: no es diagonalizable. Planteamos $a_n=(c_1+c_2n)2^n$:

$$
a_0=c_1=1,\qquad a_1=(c_1+c_2)\cdot2=4\ \Rightarrow\ c_2=1 ,\qquad a_n=(1+n)2^n .
$$

**Comprobación.** Los términos de la fórmula son $1,\,4,\,12,\,32,\,80,\,192$; la recurrencia da
$a_2=4\cdot4-4\cdot1=12$, $a_3=4\cdot12-4\cdot4=32$, $a_4=4\cdot32-4\cdot12=80$, $a_5=4\cdot80-4\cdot32=192$.

:::tip[Resultado]
$a_n=(n+1)\,2^n$. El factor $n$ extra aparece porque falta un autovector.
:::

## Aplicaciones informáticas

### Ejemplo 4 · Teselados de una franja

<!-- check: U3.T07.E4 -->

¿De cuántas maneras se puede cubrir una franja de $1\times n$ con fichas de tres tipos: un
cuadrado de $1\times1$, un dominó rojo de $1\times2$ y un dominó azul de $1\times2$?

Sea $t_n$ la cantidad. La última ficha es un cuadrado (queda una franja de $n-1$) o un dominó de
alguno de los dos colores (queda una de $n-2$):

$$
t_n=t_{n-1}+2t_{n-2},\qquad t_0=1,\ t_1=1 .
$$

La ecuación característica es $\lambda^2-\lambda-2=(\lambda-2)(\lambda+1)$, así que
$t_n=c_12^n+c_2(-1)^n$, con $c_1+c_2=1$ y $2c_1-c_2=1$: $c_1=\tfrac23$ y $c_2=\tfrac13$.

**Comprobación.** $t_n=\dfrac{2^{n+1}+(-1)^n}{3}$ da $1,1,3,5,11,21,\dots$, y la recurrencia da
$t_2=1+2=3$, $t_3=3+2=5$, $t_4=5+6=11$, $t_5=11+10=21$.

:::tip[Resultado]
$t_n=\dfrac{2^{n+1}+(-1)^n}{3}$; la cantidad de teselados crece como $2^n$ (el autovalor $2$ domina).
:::

### Ejemplo 5 · Cadenas binarias sin dos unos consecutivos

<!-- check: U3.T07.E5 -->

Sea $b_n$ la cantidad de cadenas de $n$ bits que no contienen dos unos consecutivos. Hallar $b_n$.

Una cadena válida de longitud $n\ge2$ termina en $0$, y lo que antecede es cualquier cadena válida
de longitud $n-1$ ($b_{n-1}$ formas), o termina en $1$, y entonces el bit anterior es $0$ y lo que
antecede a esos dos bits es una cadena válida de longitud $n-2$ ($b_{n-2}$ formas). Entonces

$$
b_n=b_{n-1}+b_{n-2},\qquad b_0=1\ (\text{la cadena vacía}),\quad b_1=2\ (\texttt{0},\texttt{1}).
$$

Es la recurrencia de Fibonacci con los mismos valores iniciales que $F_2=1$ y $F_3=2$, de modo que
$b_n=F_{n+2}$. Para $n=2$: $00,01,10$, es decir $3=F_4$; para $n=10$: $b_{10}=F_{12}=144$.

**Comprobación.** Para $n=3$ las cadenas válidas son $000,001,010,100,101$: $5=F_5$.

:::tip[Resultado]
$b_n=F_{n+2}=\dfrac{\varphi^{n+2}-\psi^{n+2}}{\sqrt5}$; crece como $\varphi^n$. Por ejemplo, hay $144$ cadenas
válidas de $10$ bits sobre $1024$ posibles.
:::

### Ejemplo 6 · Costo de la recursión ingenua de Fibonacci

<!-- check: U3.T07.E6 -->

El programa

```python
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

calcula $F_n$. Sea $L(n)$ el número de llamadas a `fib` que genera `fib(n)` (contando la primera).
Entonces

$$
L(0)=L(1)=1,\qquad L(n)=1+L(n-1)+L(n-2).
$$

La recurrencia es no homogénea, pero $u_n=L(n)+1$ cumple $u_n=u_{n-1}+u_{n-2}$ con
$u_0=u_1=2$, es decir, $u_n=2F_{n+1}$. Por lo tanto

$$
L(n)=2F_{n+1}-1 .
$$

**Comprobación.** $L(2)=1+1+1=3=2F_3-1$ y $L(10)=2F_{11}-1=2\cdot89-1=177$. Como
$F_{n+1}\approx\varphi^{n+1}/\sqrt5$, $L(n)$ **crece exponencialmente**, con razón
$\varphi\approx1{,}618$ por cada incremento de $n$: $L(30)=2\,692\,537$ llamadas y $L(50)=40\,730\,022\,147$.

:::tip[Resultado]
$L(n)=2F_{n+1}-1\in\Theta(\varphi^n)$. La versión iterativa con dos variables hace $n$ pasos, y por
exponenciación binaria de la matriz compañera se llega a $F_n$ con $O(\log n)$ productos de
matrices $2\times2$ (ver [potencias](/algebra-ii/unidad-3/teoria/potencias/)).
:::

Un programa corto que calcula términos con enteros exactos (Python maneja enteros de tamaño
arbitrario):

```python
def fib_iterativo(n):
    a, b = 0, 1            # (F_k, F_{k+1}) con k = 0
    for _ in range(n):
        a, b = b, a + b    # (F_k, F_{k+1}) -> (F_{k+1}, F_{k+2})
    return a

print(fib_iterativo(30))   # 832040
print(fib_iterativo(90))   # 2880067194370816120
```

<!-- check: U3.T07.E7 -->

:::caution[Errores frecuentes]
- **Usar $\lambda^n$ con $a_n$ y $a_{n+1}$ al revés.** La ecuación característica de
  $a_{n+1}=ra_n+sa_{n-1}$ es $\lambda^2=r\lambda+s$, no $\lambda^2=s\lambda+r$.
- **Olvidar las condiciones iniciales.** Las raíces solo dan la *forma* de la solución; las
  constantes $c_1,c_2$ salen de $a_0$ y $a_1$.
- **Mezclar los índices del vector de estado.** Si $x_n=(a_{n+1},a_n)^t$, entonces $x_0=(a_1,a_0)^t$
  y $a_n$ es la **segunda** coordenada de $x_n$.
- **Usar $c_1\lambda^n+c_2\lambda^n$ con raíz doble.** Es la misma función; falta el término
  $n\lambda^n$.
- **Armar $C$ con autovectores $(1,\lambda)$.** Para la matriz compañera de esta lección los
  autovectores son $(\lambda,1)$.
- **Afirmar $a_n=\varphi^n/\sqrt5$ exactamente.** Es una aproximación; el término $\psi^n/\sqrt5$
  no es nulo (pero tiende a $0$).
- **Resolver una recurrencia no homogénea como si fuera homogénea.** El ejemplo 6 requiere el cambio
  $u_n=L(n)+1$ para volverla homogénea.
:::

## Autoevaluación

<details>
<summary>1. Hallar la ecuación característica de a_{n+1} = 5a_n − 6a_{n−1} y la forma de la solución.</summary>

$\lambda^2-5\lambda+6=(\lambda-2)(\lambda-3)$: $a_n=c_12^n+c_23^n$.

</details>

<details>
<summary>2. ¿Cómo es la solución de a_{n+1} = 6a_n − 9a_{n−1}?</summary>

$\lambda^2-6\lambda+9=(\lambda-3)^2$: raíz doble, $a_n=(c_1+c_2n)3^n$.

</details>

<details>
<summary>3. ¿Por qué F_n/F_{n−1} no puede ser exactamente φ para ningún n?</summary>

$F_n/F_{n-1}$ es racional y $\varphi$ es irracional.

</details>

:::tip[En resumen]
- $a_{n+1}=ra_n+sa_{n-1}$ equivale a $x_{n+1}=Ax_n$ con $A=\begin{pmatrix}r&s\\1&0\end{pmatrix}$,
  $x_n=(a_{n+1},a_n)^t$ y $p_A(\lambda)=\lambda^2-r\lambda-s$.
- Raíces distintas: $a_n=c_1\lambda_1^n+c_2\lambda_2^n$, con $c_i$ determinados por $a_0,a_1$.
- Raíz doble $\mu\neq0$: $a_n=(c_1+c_2n)\mu^n$; la matriz compañera no es diagonalizable.
- Fibonacci: $F_n=\dfrac{\varphi^n-\psi^n}{\sqrt5}$ y $F_{n+1}/F_n\to\varphi$.
- El autovalor de mayor módulo domina el crecimiento: $\varphi^n$ en Fibonacci y en las cadenas sin
  unos consecutivos, $2^n$ en los teselados.
:::

## Para profundizar

- Poole, *Álgebra lineal. Una introducción moderna*, 3.ª ed.: sección 4.6, "Relaciones de
  recurrencia lineal" (p. 346–351), y sección 6.0, Fibonacci en el espacio vectorial (p. 445).
- Lay, *Álgebra lineal y sus aplicaciones*, 5.ª ed.: capítulo de valores propios y la aplicación a
  sistemas dinámicos discretos.
- Anterior: [3.6 Potencias de una matriz](/algebra-ii/unidad-3/teoria/potencias/). Siguiente:
  [3.8 Cadenas de Markov](/algebra-ii/unidad-3/teoria/cadenas-de-markov/).
