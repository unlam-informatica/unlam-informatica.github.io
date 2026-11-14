---
title: Ejercicio 7* — Límites con módulo
slug: analisis-matematico-i/unidad-2/practica/ejercicio-7
sidebar:
  order: 7
  label: Ejercicio 7
---


Encontrar cada uno de los siguientes límites o establecer que no existen.

**Recordatorio.** Para $\lvert u\rvert$ cerca de $u=0$:



$$
\lvert u\rvert = \begin{cases} u & \text{si } u\geq 0 \\ -u & \text{si } u<0 \end{cases}
$$



Para resolver límites donde aparece $\lvert u(x)\rvert$ cerca de un cero de $u$, hay que analizar **límites laterales** según el signo de $u$.

## 7a

:::note[Enunciado]
$\lim\limits_{x\to 1}\dfrac{\lvert x-1\rvert}{x-1}$
:::

:::tip[Resolución]
Cerca de $x=1$, $x-1$ cambia de signo. Calculamos laterales.

Por izquierda ($x\to 1^-$, $x-1<0$, $\lvert x-1\rvert=-(x-1)$):



$$
\lim_{x\to 1^-}\dfrac{-(x-1)}{x-1}=-1
$$



Por derecha ($x\to 1^+$, $x-1>0$, $\lvert x-1\rvert=x-1$):



$$
\lim_{x\to 1^+}\dfrac{x-1}{x-1}=1
$$



Los laterales **no coinciden**: el límite **no existe**.

**Resultado:** $\lim\limits_{x\to 1}\dfrac{\lvert x-1\rvert}{x-1}$ no existe (salto de $-1$ a $1$).

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 7b

:::note[Enunciado]
$\lim\limits_{x\to 1^-}\dfrac{\lvert x-1\rvert}{x-1}$
:::

:::tip[Resolución]
Por izquierda de $1$, $x-1<0$, así que $\lvert x-1\rvert=-(x-1)$. Entonces:



$$
\dfrac{\lvert x-1\rvert}{x-1}=\dfrac{-(x-1)}{x-1}=-1
$$



Es una constante en un entorno reducido por izquierda de $1$.



$$
\lim_{x\to 1^-}\dfrac{\lvert x-1\rvert}{x-1}=-1
$$



**Resultado:** $\lim\limits_{x\to 1^-}\dfrac{\lvert x-1\rvert}{x-1}=-1$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 7c

:::note[Enunciado]
$\lim\limits_{x\to 1^-}\dfrac{x^2-\lvert x-1\rvert-1}{x-1}$
:::

:::tip[Resolución]
Por izquierda de $1$, $\lvert x-1\rvert=-(x-1)=1-x$. Sustituyendo:



$$
\dfrac{x^2-(1-x)-1}{x-1}=\dfrac{x^2+x-2}{x-1}
$$



Factorizamos el numerador: $x^2+x-2=(x-1)(x+2)$.



$$
\dfrac{(x-1)(x+2)}{x-1}=x+2\quad (\text{para }x\neq 1)
$$





$$
\lim_{x\to 1^-}(x+2)=3
$$



**Resultado:** $\lim\limits_{x\to 1^-}\dfrac{x^2-\lvert x-1\rvert-1}{x-1}=3$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 7d

:::note[Enunciado]
$\lim\limits_{x\to 1^+}\left(\dfrac{1}{x-1}-\dfrac{1}{\lvert x-1\rvert}\right)$
:::

:::tip[Resolución]
Por derecha de $1$, $x-1>0$, así que $\lvert x-1\rvert=x-1$. Sustituyendo:



$$
\dfrac{1}{x-1}-\dfrac{1}{x-1}=0
$$



Es la función constantemente $0$ en un entorno reducido por derecha de $1$.



$$
\lim_{x\to 1^+}\left(\dfrac{1}{x-1}-\dfrac{1}{\lvert x-1\rvert}\right)=0
$$



**Resultado:** $0$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 7e

:::note[Enunciado]
$\lim\limits_{x\to 1}\dfrac{\lvert x\rvert-x}{x-1}$
:::

:::tip[Resolución]
Cerca de $x=1$, $x>0$, así que $\lvert x\rvert=x$. Entonces:



$$
\dfrac{\lvert x\rvert-x}{x-1}=\dfrac{x-x}{x-1}=\dfrac{0}{x-1}=0\quad (\text{para }x\neq 1)
$$



La función es constantemente $0$ en un entorno reducido de $1$:



$$
\lim_{x\to 1}\dfrac{\lvert x\rvert-x}{x-1}=0
$$



**Resultado:** $0$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 7f

:::note[Enunciado]
$\lim\limits_{x\to -1}\dfrac{x+x^2}{\lvert x\rvert}$
:::

:::tip[Resolución]
Cerca de $x=-1$, $x<0$, así que $\lvert x\rvert=-x$. Sustituyendo:



$$
\dfrac{x+x^2}{-x}=\dfrac{x(1+x)}{-x}=-(1+x)\quad (\text{para }x\neq 0)
$$





$$
\lim_{x\to -1}\bigl(-(1+x)\bigr)=-(1+(-1))=0
$$



**Resultado:** $\lim\limits_{x\to -1}\dfrac{x+x^2}{\lvert x\rvert}=0$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 7g

:::note[Enunciado]
$\lim\limits_{x\to 0^+}\dfrac{x+x^2}{\lvert x\rvert}$
:::

:::tip[Resolución]
Por derecha de $0$, $x>0$, así que $\lvert x\rvert=x$. Sustituyendo:



$$
\dfrac{x+x^2}{x}=\dfrac{x(1+x)}{x}=1+x\quad (\text{para }x\neq 0)
$$





$$
\lim_{x\to 0^+}(1+x)=1
$$



**Resultado:** $\lim\limits_{x\to 0^+}\dfrac{x+x^2}{\lvert x\rvert}=1$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
