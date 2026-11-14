---
title: Ejercicio 6* — Suma y diferencia de límites
slug: analisis-matematico-i/unidad-2/practica/ejercicio-6
sidebar:
  order: 6
  label: Ejercicio 6
---


:::note[Enunciado]
Si $\lim\limits_{x\to a}(f(x)+g(x))=2$ y $\lim\limits_{x\to a}(f(x)-g(x))=1$ encontrar $\lim\limits_{x\to a}(f(x)\cdot g(x))$.
:::

:::tip[Resolución]
Llamemos $L_1=\lim_{x\to a}f(x)$ y $L_2=\lim_{x\to a}g(x)$, suponiendo que ambos existen y son finitos. Por las propiedades algebraicas del límite (suma y resta):



$$
L_1+L_2=2 \tag{1}
$$





$$
L_1-L_2=1 \tag{2}
$$



**Resolución del sistema.** Sumando (1) y (2):



$$
2L_1=3\implies L_1=\dfrac{3}{2}
$$



Restando (2) de (1):



$$
2L_2=1\implies L_2=\dfrac{1}{2}
$$



**Aplicación al producto.** Por la propiedad del límite del producto:



$$
\lim_{x\to a}(f(x)\cdot g(x))=L_1\cdot L_2=\dfrac{3}{2}\cdot\dfrac{1}{2}=\dfrac{3}{4}
$$



**Observación.** La existencia de $\lim(f+g)$ y $\lim(f-g)$ es **equivalente** a la existencia conjunta de $\lim f$ y $\lim g$: sumando y restando obtenemos $2\lim f=\lim(f+g)+\lim(f-g)$ y $2\lim g=\lim(f+g)-\lim(f-g)$.

**Resultado:** $\lim\limits_{x\to a}(f(x)\cdot g(x))=\dfrac{3}{4}$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
