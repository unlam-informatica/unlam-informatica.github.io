---
title: Repaso de Álgebra I
description: Repaso preparatorio de vectores, matrices, determinantes, sistemas lineales, polinomios, rectas y planos, con autodiagnóstico y guía de qué repasar para cada unidad.
slug: algebra-ii/repaso
sidebar:
  order: 0
  label: Presentación
---

## Para qué sirve este repaso

Álgebra y Geometría Analítica II tiene como correlativa Álgebra y Geometría Analítica I, y su programa declara como conocimientos necesarios vectores y matrices, cálculo vectorial y matricial, resolución de sistemas de ecuaciones y factorización de polinomios. Esta sección reúne justamente eso, en cinco lecciones cortas, para que las unidades de Álgebra II se puedan leer sin trabarse en las cuentas. No es una segunda materia: cada lección repasa las definiciones y los procedimientos que después se usan, con ejemplos resueltos, los errores más comunes y algunos ejercicios con resolución.

| Lección | Contenido |
|---|---|
| [R.1 Vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/) | operaciones en $\mathbb{R}^n$, producto escalar y norma, producto de matrices, transpuesta, inversa, traza, matrices especiales |
| [R.2 Determinantes](/algebra-ii/repaso/determinantes/) | cofactores, Sarrus, propiedades, triangulación, inversibilidad, parámetros |
| [R.3 Sistemas lineales](/algebra-ii/repaso/sistemas-lineales/) | eliminación gaussiana, rango, Rouché-Frobenius, homogéneos, parámetros, matriz ampliada múltiple, $\mathbb{Z}_2$ |
| [R.4 Polinomios](/algebra-ii/repaso/polinomios/) | raíces y multiplicidad, teorema del resto, Ruffini, criterio de Gauss, factorización en $\mathbb{R}$ |
| [R.5 Rectas y planos](/algebra-ii/repaso/rectas-y-planos/) | ecuaciones vectorial, paramétricas e implícita, producto vectorial, rectas y planos por el origen, posiciones relativas |

## Cómo usarlo

1. Respondé el **autodiagnóstico** de abajo con lápiz y papel, sin mirar las respuestas. Son ocho preguntas cortas; cada una corresponde a una lección.
2. Abrí la respuesta plegable y compará. Si la pregunta te llevó más de un par de minutos o te equivocaste, estudiá la lección indicada.
3. Antes de empezar una unidad, mirá la tabla [Qué repaso necesito para cada unidad](#qué-repaso-necesito-para-cada-unidad) y hacé al menos los ejercicios de repaso de las lecciones que figuran ahí.
4. Durante la cursada, volvé a la lección puntual cuando una cuenta te frene: cada lección termina con una sección "Dónde se usa en Álgebra II" que indica en qué temas aparece.

La notación es la misma que se usa en toda la materia ($A^t$ para la transpuesta, $\operatorname{rango}(A)$, $\operatorname{tr}(A)$, vectores de $\mathbb{R}^n$ como $n$-uplas con comas en el texto y como columnas en las cuentas). La tabla completa está en [Notación](/algebra-ii/notacion/).

## Autodiagnóstico

### Pregunta 1 · Producto de matrices
<!-- check: R.T00.E1 -->

Sean $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ y $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Calcular $AB$ y $BA$. ¿Son iguales?

<details>
<summary>Respuesta</summary>

$AB=\begin{pmatrix}2&1\\1&0\end{pmatrix}$ y $BA=\begin{pmatrix}0&1\\1&2\end{pmatrix}$: no son iguales. Multiplicar a derecha por $B$ intercambia las columnas de $A$; multiplicar a izquierda intercambia sus filas. El producto de matrices no es conmutativo.

Si dudaste, repasá [R.1 Vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/#producto-de-matrices).

</details>

### Pregunta 2 · Inversa de 2×2
<!-- check: R.T00.E2 -->

Hallar la inversa de $M=\begin{pmatrix}2&1\\5&3\end{pmatrix}$.

<details>
<summary>Respuesta</summary>

$\det M=6-5=1$, así que $M^{-1}=\begin{pmatrix}3&-1\\-5&2\end{pmatrix}$. Se comprueba que $MM^{-1}=I$: $(6-5,\,-2+2)=(1,0)$ y $(15-15,\,-5+6)=(0,1)$.

Si dudaste, repasá [R.1 Vectores y matrices](/algebra-ii/repaso/vectores-y-matrices/#inversa).

</details>

### Pregunta 3 · Determinante y escalares
<!-- check: R.T00.E3 -->

Sea $A=\begin{pmatrix}1&2&3\\0&4&5\\0&0&6\end{pmatrix}$. Calcular $\det A$ y $\det(2A)$.

<details>
<summary>Respuesta</summary>

$A$ es triangular: $\det A=1\cdot4\cdot6=24$. Como $A$ es de $3\times3$, $\det(2A)=2^3\cdot24=192$ (no $48$).

Si dudaste, repasá [R.2 Determinantes](/algebra-ii/repaso/determinantes/#propiedades).

</details>

### Pregunta 4 · Determinante con parámetro
<!-- check: R.T00.E4 -->

¿Para qué valores de $k\in\mathbb{R}$ la matriz $\begin{pmatrix}k&2\\2&k\end{pmatrix}$ es inversible?

<details>
<summary>Respuesta</summary>

Su determinante es $k^2-4=(k-2)(k+2)$. Es inversible si y solo si $k\neq2$ y $k\neq-2$.

Si dudaste, repasá [R.2 Determinantes](/algebra-ii/repaso/determinantes/#determinantes-con-parámetros).

</details>

### Pregunta 5 · Clasificación de un sistema
<!-- check: R.T00.E5 -->

Clasificar según $k\in\mathbb{R}$ el sistema $\begin{cases}x+y=2\\ 2x+2y=k\end{cases}$

<details>
<summary>Respuesta</summary>

Con $F_2-2F_1\to F_2$ la segunda fila queda $(0\ \ 0\mid k-4)$. Si $k=4$, $\operatorname{rango}(A)=\operatorname{rango}(A\mid b)=1<2$: compatible indeterminado, con soluciones $(2-y,\,y)$, $y\in\mathbb{R}$. Si $k\neq4$, $\operatorname{rango}(A)=1<2=\operatorname{rango}(A\mid b)$: incompatible. Nunca es compatible determinado.

Si dudaste, repasá [R.3 Sistemas lineales](/algebra-ii/repaso/sistemas-lineales/#clasificación-el-teorema-de-rouché-frobenius).

</details>

### Pregunta 6 · Un sistema en ℤ₂
<!-- check: R.T00.E6 -->

¿Tiene solución en $\mathbb{Z}_2$ el sistema $\begin{cases}x+y=1\\ y+z=1\\ x+z=1\end{cases}$? ¿Y en $\mathbb{R}$?

<details>
<summary>Respuesta</summary>

En $\mathbb{Z}_2$ no: sumando las tres ecuaciones, el lado izquierdo es $2x+2y+2z=0$ (porque $1+1=0$) y el derecho es $1+1+1=1$, así que se llega a $0=1$. En $\mathbb{R}$ sí, y es única: $x=y=z=\frac12$. El mismo sistema puede cambiar de clasificación al cambiar el cuerpo.

Si dudaste, repasá [R.3 Sistemas lineales](/algebra-ii/repaso/sistemas-lineales/#sistemas-sobre-ℤ₂).

</details>

### Pregunta 7 · Factorizar un polinomio
<!-- check: R.T00.E7 -->

Hallar todas las raíces de $p(\lambda)=\lambda^3-3\lambda^2+2\lambda$.

<details>
<summary>Respuesta</summary>

Sacando factor común, $p(\lambda)=\lambda(\lambda^2-3\lambda+2)=\lambda(\lambda-1)(\lambda-2)$. Las raíces son $0$, $1$ y $2$, todas simples. Dividir por $\lambda$ en lugar de factorizar haría perder la raíz $0$.

Si dudaste, repasá [R.4 Polinomios](/algebra-ii/repaso/polinomios/).

</details>

### Pregunta 8 · Plano por el origen
<!-- check: R.T00.E8 -->

Hallar una ecuación implícita del plano $\operatorname{gen}\{(1,0,1),(0,1,1)\}$.

<details>
<summary>Respuesta</summary>

Un normal es $(1,0,1)\times(0,1,1)=(0\cdot1-1\cdot1,\ 1\cdot0-1\cdot1,\ 1\cdot1-0\cdot0)=(-1,-1,1)$. Como el plano pasa por el origen, su ecuación es $-x-y+z=0$, o bien $x+y-z=0$. Comprobación: $1+0-1=0$ y $0+1-1=0$.

Si dudaste, repasá [R.5 Rectas y planos](/algebra-ii/repaso/rectas-y-planos/#rectas-y-planos-por-el-origen).

</details>

## Qué repaso necesito para cada unidad

| Unidad | Lecciones de repaso | Dónde se usan |
|---|---|---|
| [Unidad 1 · Espacios vectoriales](/algebra-ii/unidad-1/) | [R.1](/algebra-ii/repaso/vectores-y-matrices/), [R.3](/algebra-ii/repaso/sistemas-lineales/), [R.5](/algebra-ii/repaso/rectas-y-planos/); [R.2](/algebra-ii/repaso/determinantes/) como atajo | operaciones en $\mathbb{R}^n$ y en matrices; sistemas homogéneos para subespacios, independencia lineal y bases; sistemas en $\mathbb{Z}_2$ para códigos; matriz ampliada múltiple para cambio de coordenadas; rectas y planos por el origen como subespacios |
| [Unidad 2 · Transformaciones lineales](/algebra-ii/unidad-2/) | [R.1](/algebra-ii/repaso/vectores-y-matrices/), [R.3](/algebra-ii/repaso/sistemas-lineales/), [R.2](/algebra-ii/repaso/determinantes/) | producto de matrices para la matriz asociada y la composición; núcleo como sistema homogéneo; rango para la imagen; inversa y determinante para decidir si hay isomorfismo |
| [Unidad 3 · Autovalores y autovectores](/algebra-ii/unidad-3/) | [R.2](/algebra-ii/repaso/determinantes/), [R.4](/algebra-ii/repaso/polinomios/), [R.3](/algebra-ii/repaso/sistemas-lineales/), [R.1](/algebra-ii/repaso/vectores-y-matrices/) | determinante con parámetro para el polinomio característico; factorización y multiplicidad de raíces; sistemas homogéneos para los autoespacios; inversa, traza y matrices diagonales para la diagonalización y las potencias |
| [Unidad 4 · Espacios con producto interno](/algebra-ii/unidad-4/) | [R.1](/algebra-ii/repaso/vectores-y-matrices/), [R.5](/algebra-ii/repaso/rectas-y-planos/), [R.3](/algebra-ii/repaso/sistemas-lineales/) | producto escalar, norma y transpuesta; vector normal y complemento ortogonal; sistemas para el complemento ortogonal y las ecuaciones normales de cuadrados mínimos |

:::tip[Consejo]
Si tenés poco tiempo, priorizá [R.3 Sistemas lineales](/algebra-ii/repaso/sistemas-lineales/): la eliminación gaussiana aparece en las cuatro unidades. Antes de la Unidad 3, sumá [R.2](/algebra-ii/repaso/determinantes/) y [R.4](/algebra-ii/repaso/polinomios/).
:::
