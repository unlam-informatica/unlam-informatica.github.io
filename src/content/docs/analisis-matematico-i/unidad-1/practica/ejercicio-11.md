---
title: Ejercicio 11 — Funciones por tramos
slug: analisis-matematico-i/unidad-1/practica/ejercicio-11
sidebar:
  order: 11
  label: Ejercicio 11
---


Dada las siguientes funciones definidas por tramos, determinar dominio, imagen, ceros y graficar aproximadamente.

## 11a

:::note[Enunciado]
$f(x)=\begin{cases} x+2 & x\leq -1, \\ -x & -1<x\leq 1, \\ 3x-4 & 1<x\leq 3, \\ 2 & x>3 \end{cases}$
:::

:::tip[Resolución]
**Dominio.** Los cuatro tramos cubren toda la recta real sin solapamientos:



$$
D_f=\mathbb{R}
$$



**Imagen.** Analizamos cada tramo por separado.

- Tramo $x\leq -1$ con $f(x)=x+2$: como $x+2$ es creciente y $x\leq -1$, se tiene $f(x)\leq 1$. Aporta $(-\infty,1]$.
- Tramo $-1<x\leq 1$ con $f(x)=-x$: $-x$ es decreciente, en los extremos vale $1$ (excluido) y $-1$ (incluido). Aporta $[-1,1)$.
- Tramo $1<x\leq 3$ con $f(x)=3x-4$: creciente, en los extremos vale $-1$ (excluido) y $5$ (incluido). Aporta $(-1,5]$.
- Tramo $x>3$ con $f(x)=2$: constante. Aporta $\lbrace 2\rbrace $.

Unión: $(-\infty,1]\cup[-1,1)\cup(-1,5]\cup\lbrace 2\rbrace =(-\infty,5]$.



$$
I_f=(-\infty,5]
$$



**Ceros.** Resolvemos $f(x)=0$ en cada tramo y verificamos que el cero quede dentro del dominio del tramo.

- $x+2=0\iff x=-2$, válido porque $-2\leq -1$.
- $-x=0\iff x=0$, válido porque $-1<0\leq 1$.
- $3x-4=0\iff x=\dfrac43$, válido porque $1<\dfrac43\leq 3$.
- El tramo $f(x)=2$ no se anula.

Ceros: $\left\lbrace -2,\,0,\,\dfrac43\right\rbrace $.

**Resultado:** $D_f=\mathbb{R}$, $I_f=(-\infty,5]$, ceros $\left\lbrace -2,\,0,\,\dfrac43\right\rbrace $.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 11b

:::note[Enunciado]
$f(x)=\begin{cases} \dfrac{x^2-6x+9}{x-3} & x\neq 3, \\ 4 & x=3 \end{cases}$
:::

:::tip[Resolución]
**Simplificación del primer tramo.** El numerador es un trinomio cuadrado perfecto:



$$
x^2-6x+9=(x-3)^2
$$



Para $x\neq 3$ podemos simplificar:



$$
\dfrac{(x-3)^2}{x-3}=x-3
$$



La función equivale a la recta $y=x-3$ con un único punto reasignado: en $x=3$, en lugar de tomar el valor "natural" $0$, vale $4$.

**Dominio.** Los dos tramos cubren todos los reales:



$$
D_f=\mathbb{R}
$$



**Imagen.** La recta $y=x-3$ recorrería todo $\mathbb{R}$, pero al excluir $x=3$ pierde el valor $0$ que esa recta tomaba allí. El valor reasignado en $x=3$ es $4$, pero $4$ ya está cubierto por la recta en $x=7$. Por lo tanto:



$$
I_f=\mathbb{R}-\lbrace 0\rbrace
$$



**Ceros.** Si fuera $x-3=0\iff x=3$, pero en $x=3$ la función vale $4\neq 0$. La función no tiene ceros.

**Resultado:** $D_f=\mathbb{R}$, $I_f=\mathbb{R}-\lbrace 0\rbrace $, sin ceros.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 11c

:::note[Enunciado]
$f(x)=\begin{cases} \lvert x+\tfrac12\rvert & x\leq 2, \\ \lvert x-4\rvert & x>2 \end{cases}$
:::

:::tip[Resolución]
**Dominio.** Los dos tramos cubren todo $\mathbb{R}$:



$$
D_f=\mathbb{R}
$$



**Imagen.** Cada tramo es un valor absoluto, que nunca es negativo.

- Tramo $x\leq 2$ con $f(x)=\lvert x+\tfrac12\rvert$: el mínimo $0$ se alcanza en $x=-\dfrac12$. En el extremo derecho $x=2$ vale $\lvert 2+\tfrac12\rvert=\dfrac52$. Aporta $\left[0,\dfrac52\right]$.
- Tramo $x>2$ con $f(x)=\lvert x-4\rvert$: el mínimo $0$ se alcanza en $x=4$. En $x\to 2^+$ vale $2$, y crece sin cota cuando $x\to+\infty$. Aporta $[0,+\infty)$.

Unión: $\left[0,\dfrac52\right]\cup[0,+\infty)=[0,+\infty)$.



$$
I_f=[0,+\infty)
$$



**Ceros.**

- $\lvert x+\tfrac12\rvert=0\iff x=-\dfrac12$, válido porque $-\dfrac12\leq 2$.
- $\lvert x-4\rvert=0\iff x=4$, válido porque $4>2$.

Ceros: $\left\lbrace -\dfrac12,\,4\right\rbrace $.

**Resultado:** $D_f=\mathbb{R}$, $I_f=[0,+\infty)$, ceros $\left\lbrace -\dfrac12,\,4\right\rbrace $.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 11d

:::note[Enunciado]
$f(x)=\begin{cases} \sqrt{x+4} & x\geq -3, \\ x+3 & -4\leq x<-3, \\ \sqrt[3]{x}+3 & x<-4 \end{cases}$
:::

:::tip[Resolución]
**Dominio.** Los tres tramos cubren $x<-4$, $-4\leq x<-3$ y $x\geq -3$, es decir todo $\mathbb{R}$:



$$
D_f=\mathbb{R}
$$



**Imagen.** Analizamos cada tramo.

- Tramo $x\geq -3$ con $f(x)=\sqrt{x+4}$: el radicando $x+4\geq 1$, así que $\sqrt{x+4}\geq 1$. Es creciente y no tiene cota superior. Aporta $[1,+\infty)$.
- Tramo $-4\leq x<-3$ con $f(x)=x+3$: recta creciente. En los extremos vale $-1$ (incluido) y $0$ (excluido). Aporta $[-1,0)$.
- Tramo $x<-4$ con $f(x)=\sqrt[3]{x}+3$: la raíz cúbica es creciente, así que cuando $x\to-\infty$, $\sqrt[3]{x}\to-\infty$ y $f\to-\infty$. En el extremo derecho $x=-4$ (excluido) vale $\sqrt[3]{-4}+3\approx -1{,}587+3\approx 1{,}413$. Aporta $(-\infty,\,\sqrt[3]{-4}+3)$.

La unión de los tres recorridos cubre todo $\mathbb{R}$:



$$
I_f=\mathbb{R}
$$



**Ceros.**

- $\sqrt{x+4}=0\iff x=-4$, pero $-4\notin[-3,+\infty)$: no es válido.
- $x+3=0\iff x=-3$, pero $-3\notin[-4,-3)$: no es válido.
- $\sqrt[3]{x}+3=0\iff \sqrt[3]{x}=-3\iff x=-27$, válido porque $-27<-4$.

Cero: $\lbrace -27\rbrace $.

**Resultado:** $D_f=\mathbb{R}$, $I_f=\mathbb{R}$, cero $\lbrace -27\rbrace $.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
