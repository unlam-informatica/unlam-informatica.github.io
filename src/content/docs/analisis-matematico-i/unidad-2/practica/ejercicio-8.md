---
title: Ejercicio 8 — Calcular los siguientes límites indeterminados
slug: analisis-matematico-i/unidad-2/practica/ejercicio-8
sidebar:
  order: 8
  label: Ejercicio 8
---


Calcular los siguientes límites indeterminados.

**Recordatorio.** Los límites de la forma $\dfrac{0}{0}$ son indeterminaciones que se resuelven con técnicas algebraicas: factorización, racionalización, simplificación, infinitésimos equivalentes, etc.

## 8a

:::note[Enunciado]
$\lim\limits_{x\to 3}\dfrac{x-3}{x^2-9}$
:::

:::tip[Resolución]
Reemplazando: $\dfrac{0}{0}$ (indeterminación).

Factorizamos el denominador:



$$
x^2-9=(x-3)(x+3)
$$



Entonces:



$$
\dfrac{x-3}{(x-3)(x+3)}=\dfrac{1}{x+3}\quad (\text{para }x\neq 3)
$$





$$
\lim_{x\to 3}\dfrac{1}{x+3}=\dfrac{1}{6}
$$



**Resultado:** $\lim\limits_{x\to 3}\dfrac{x-3}{x^2-9}=\dfrac{1}{6}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8b

:::note[Enunciado]
$\lim\limits_{x\to 2}\dfrac{x^2-5x+6}{x^2-9x+14}$
:::

:::tip[Resolución]
Reemplazando: $\dfrac{4-10+6}{4-18+14}=\dfrac{0}{0}$ (indeterminación).

Factorizamos ambos polinomios.

Numerador: raíces $x=2$ y $x=3$ → $(x-2)(x-3)$.

Denominador: raíces $x=2$ y $x=7$ → $(x-2)(x-7)$.

Simplificamos:



$$
\dfrac{(x-2)(x-3)}{(x-2)(x-7)}=\dfrac{x-3}{x-7}\quad (\text{para }x\neq 2)
$$





$$
\lim_{x\to 2}\dfrac{x-3}{x-7}=\dfrac{-1}{-5}=\dfrac{1}{5}
$$



**Resultado:** $\lim\limits_{x\to 2}\dfrac{x^2-5x+6}{x^2-9x+14}=\dfrac{1}{5}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8c*

:::note[Enunciado]
$\lim\limits_{h\to 0}\dfrac{(3+h)^{-1}-3^{-1}}{h}$
:::

:::tip[Resolución]
Reemplazando $h=0$: $\dfrac{3^{-1}-3^{-1}}{0}=\dfrac{0}{0}$ (indeterminación).

Reescribimos las potencias negativas como inversos:



$$
\dfrac{\dfrac{1}{3+h}-\dfrac{1}{3}}{h}
$$



Sacando común denominador en el numerador:



$$
\dfrac{1}{3+h}-\dfrac{1}{3}=\dfrac{3-(3+h)}{3(3+h)}=\dfrac{-h}{3(3+h)}
$$



Sustituimos:



$$
\dfrac{-h/(3(3+h))}{h}=\dfrac{-1}{3(3+h)}\quad (h\neq 0)
$$





$$
\lim_{h\to 0}\dfrac{-1}{3(3+h)}=\dfrac{-1}{3\cdot 3}=-\dfrac{1}{9}
$$



**Resultado:** $\lim\limits_{h\to 0}\dfrac{(3+h)^{-1}-3^{-1}}{h}=-\dfrac{1}{9}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8d

:::note[Enunciado]
$\lim\limits_{x\to 2}\dfrac{x-\sqrt{3x-2}}{x^2-4}$
:::

:::tip[Resolución]
Reemplazando: $\dfrac{2-\sqrt{4}}{0}=\dfrac{0}{0}$ (indeterminación).

Racionalizamos el numerador multiplicando por el conjugado $x+\sqrt{3x-2}$:



$$
\dfrac{x-\sqrt{3x-2}}{x^2-4}\cdot\dfrac{x+\sqrt{3x-2}}{x+\sqrt{3x-2}}=\dfrac{x^2-(3x-2)}{(x^2-4)(x+\sqrt{3x-2})}
$$



Numerador: $x^2-3x+2=(x-1)(x-2)$.

Denominador: $(x-2)(x+2)(x+\sqrt{3x-2})$.

Simplificamos:



$$
\dfrac{(x-1)(x-2)}{(x-2)(x+2)(x+\sqrt{3x-2})}=\dfrac{x-1}{(x+2)(x+\sqrt{3x-2})}
$$



Evaluamos en $x=2$:



$$
\dfrac{2-1}{(2+2)(2+\sqrt{4})}=\dfrac{1}{4\cdot 4}=\dfrac{1}{16}
$$



**Resultado:** $\lim\limits_{x\to 2}\dfrac{x-\sqrt{3x-2}}{x^2-4}=\dfrac{1}{16}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8e*

:::note[Enunciado]
$\lim\limits_{t\to 2}\dfrac{t^3-8}{t^5-32}$
:::

:::tip[Resolución]
Reemplazando: $\dfrac{0}{0}$ (indeterminación). Ambos numerador y denominador se anulan en $t=2$.

Factorizamos usando las identidades $a^n-b^n=(a-b)(a^{n-1}+a^{n-2}b+\cdots+b^{n-1})$.

Numerador: $t^3-2^3=(t-2)(t^2+2t+4)$.

Denominador: $t^5-2^5=(t-2)(t^4+2t^3+4t^2+8t+16)$.

Simplificamos:



$$
\dfrac{t^2+2t+4}{t^4+2t^3+4t^2+8t+16}
$$



Evaluamos en $t=2$:

Numerador: $4+4+4=12$.

Denominador: $16+16+16+16+16=80$.



$$
\dfrac{12}{80}=\dfrac{3}{20}
$$



**Resultado:** $\lim\limits_{t\to 2}\dfrac{t^3-8}{t^5-32}=\dfrac{3}{20}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8f

:::note[Enunciado]
$\lim\limits_{x\to 8}\dfrac{\sqrt{2x}-4}{64-x^2}$
:::

:::tip[Resolución]
Reemplazando: $\dfrac{\sqrt{16}-4}{64-64}=\dfrac{0}{0}$.

Racionalizamos el numerador con conjugado $\sqrt{2x}+4$:



$$
\dfrac{\sqrt{2x}-4}{64-x^2}\cdot\dfrac{\sqrt{2x}+4}{\sqrt{2x}+4}=\dfrac{2x-16}{(64-x^2)(\sqrt{2x}+4)}=\dfrac{2(x-8)}{(64-x^2)(\sqrt{2x}+4)}
$$



Factorizamos $64-x^2=(8-x)(8+x)=-(x-8)(x+8)$:



$$
\dfrac{2(x-8)}{-(x-8)(x+8)(\sqrt{2x}+4)}=\dfrac{-2}{(x+8)(\sqrt{2x}+4)}\quad (x\neq 8)
$$



Evaluamos en $x=8$:



$$
\dfrac{-2}{16\cdot 8}=\dfrac{-2}{128}=-\dfrac{1}{64}
$$



**Resultado:** $\lim\limits_{x\to 8}\dfrac{\sqrt{2x}-4}{64-x^2}=-\dfrac{1}{64}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8g

:::note[Enunciado]
$\lim\limits_{x\to 1/2}\dfrac{4x^2-x-1/2}{1-16x^4}$
:::

:::tip[Resolución]
Reemplazando: $\dfrac{1-1/2-1/2}{1-1}=\dfrac{0}{0}$.

Factorizamos el denominador como diferencia de cuadrados:



$$
1-16x^4=(1-4x^2)(1+4x^2)=(1-2x)(1+2x)(1+4x^2)
$$



Para el numerador, multiplicamos por $2$ para evitar fracciones:



$$
2\cdot\left(4x^2-x-\dfrac{1}{2}\right)=8x^2-2x-1
$$



Factorizamos: raíces de $8x^2-2x-1=0$:



$$
x=\dfrac{2\pm\sqrt{4+32}}{16}=\dfrac{2\pm 6}{16}
$$



Raíces: $x=1/2$ y $x=-1/4$. Por lo tanto $8x^2-2x-1=8\left(x-\dfrac{1}{2}\right)\left(x+\dfrac{1}{4}\right)=(2x-1)(4x+1)$.

Entonces $4x^2-x-\dfrac{1}{2}=\dfrac{1}{2}(2x-1)(4x+1)$.

Sustituimos:



$$
\dfrac{\dfrac{1}{2}(2x-1)(4x+1)}{(1-2x)(1+2x)(1+4x^2)}=\dfrac{-\dfrac{1}{2}(4x+1)}{(1+2x)(1+4x^2)}
$$



donde usamos $(2x-1)=-(1-2x)$.

Evaluamos en $x=1/2$:



$$
\dfrac{-\dfrac{1}{2}\cdot 3}{2\cdot 2}=\dfrac{-3/2}{4}=-\dfrac{3}{8}
$$



**Resultado:** $\lim\limits_{x\to 1/2}\dfrac{4x^2-x-1/2}{1-16x^4}=-\dfrac{3}{8}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8h

:::note[Enunciado]
$\lim\limits_{x\to 1}\dfrac{2x-\sqrt{x+3}}{\sqrt{x}-1}$
:::

:::tip[Resolución]
Reemplazando: $\dfrac{2-2}{0}=\dfrac{0}{0}$.

Racionalizamos numerador y denominador.

Multiplicamos por $\dfrac{2x+\sqrt{x+3}}{2x+\sqrt{x+3}}\cdot\dfrac{\sqrt{x}+1}{\sqrt{x}+1}$:



$$
\dfrac{(4x^2-(x+3))(\sqrt{x}+1)}{(x-1)(2x+\sqrt{x+3})}=\dfrac{(4x^2-x-3)(\sqrt{x}+1)}{(x-1)(2x+\sqrt{x+3})}
$$



Factorizamos $4x^2-x-3$: raíces $x=1$ y $x=-3/4$ → $(x-1)(4x+3)$.



$$
\dfrac{(x-1)(4x+3)(\sqrt{x}+1)}{(x-1)(2x+\sqrt{x+3})}=\dfrac{(4x+3)(\sqrt{x}+1)}{2x+\sqrt{x+3}}
$$



Evaluamos en $x=1$:



$$
\dfrac{7\cdot 2}{2+2}=\dfrac{14}{4}=\dfrac{7}{2}
$$



**Resultado:** $\lim\limits_{x\to 1}\dfrac{2x-\sqrt{x+3}}{\sqrt{x}-1}=\dfrac{7}{2}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
