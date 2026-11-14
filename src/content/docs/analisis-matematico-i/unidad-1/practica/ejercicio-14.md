---
title: Ejercicio 14 — Efecto de transformaciones
slug: analisis-matematico-i/unidad-1/practica/ejercicio-14
sidebar:
  order: 14
  label: Ejercicio 14
---


Describir qué efecto produce en la gráfica de $y=f(x)$ realizar las siguientes operaciones en la regla de asignación, siendo $c\in\mathbb{R}$.

**Sugerencia:** definir en GeoGebra una función cualquiera (puede ser $y=x^2$; $y=\lvert x\rvert$; u otra), definir un deslizador $c$ que varíe teniendo en cuenta números positivos y negativos y las funciones de todos los ítems para observar qué sucede con la original. Se puede ir cambiando de función para poder visualizar mejor. Escribir en el cuaderno las conclusiones extraídas.

## 14a

:::note[Enunciado]
$y=f(x)+c$.
:::

:::tip[Resolución]
Sumar la constante $c$ al valor de salida desplaza cada punto $(x,f(x))$ a $(x,f(x)+c)$: se mueve solo en el eje $y$.

- Si $c>0$: la gráfica se desplaza **$c$ unidades hacia arriba**.
- Si $c<0$: la gráfica se desplaza **$\lvert c\rvert$ unidades hacia abajo**.
- Si $c=0$: no hay cambio.

El dominio se mantiene; la imagen se desplaza la misma cantidad en sentido vertical. La forma de la curva no cambia (no se estira ni se refleja).

**Resultado:** desplazamiento vertical de $\lvert c\rvert$ unidades, hacia arriba si $c>0$ y hacia abajo si $c<0$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 14b

:::note[Enunciado]
$y=f(x-c)$.
:::

:::tip[Resolución]
Reemplazar la variable de entrada $x$ por $x-c$ desplaza la gráfica en el eje $x$. Para que el argumento valga lo mismo que antes hay que entrar con un $x$ corrido en $c$, así que el punto $(x_0,f(x_0))$ se mueve a $(x_0+c,f(x_0))$.

- Si $c>0$: la gráfica se desplaza **$c$ unidades hacia la derecha**.
- Si $c<0$: la gráfica se desplaza **$\lvert c\rvert$ unidades hacia la izquierda**.
- Si $c=0$: no hay cambio.

La imagen se mantiene; el dominio se desplaza la misma cantidad en sentido horizontal. La forma de la curva no cambia.

**Resultado:** desplazamiento horizontal de $\lvert c\rvert$ unidades, hacia la derecha si $c>0$ y hacia la izquierda si $c<0$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 14c

:::note[Enunciado]
$y=f(c\cdot x)$.
:::

:::tip[Resolución]
Multiplicar la entrada por $c$ produce un escalado horizontal alrededor del eje $y$. El argumento $cx$ alcanza el valor "natural" $x_0$ cuando se entra con $x=x_0/c$, así que el punto $(x_0,f(x_0))$ se mueve a $(x_0/c,\,f(x_0))$.

- Si $c>1$: la gráfica se **comprime horizontalmente** por un factor $c$ (cada $x$ se acerca al eje $y$).
- Si $0<c<1$: la gráfica se **dilata horizontalmente** por un factor $1/c$.
- Si $c=1$: no hay cambio.
- Si $-1<c<0$: dilatación horizontal **más reflexión respecto al eje $y$**.
- Si $c=-1$: reflexión pura respecto al eje $y$.
- Si $c<-1$: compresión horizontal **más reflexión respecto al eje $y$**.
- Si $c=0$: $y=f(0)$ es una constante, no una transformación de la curva original.

La imagen se mantiene siempre que $c\neq 0$; el dominio se escala por el factor $1/c$.

**Resultado:** escalado horizontal por factor $1/\lvert c\rvert$ (compresión si $\lvert c\rvert>1$, dilatación si $0<\lvert c\rvert<1$); si $c<0$ se compone además con una reflexión respecto al eje $y$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 14d

:::note[Enunciado]
$y=c\cdot f(x)$.
:::

:::tip[Resolución]
Multiplicar la salida por $c$ produce un escalado vertical respecto al eje $x$. El punto $(x_0,f(x_0))$ se mueve a $(x_0,\,c\cdot f(x_0))$.

- Si $c>1$: la gráfica se **estira verticalmente** por un factor $c$ (cada $y$ se aleja del eje $x$).
- Si $0<c<1$: la gráfica se **comprime verticalmente** por un factor $c$.
- Si $c=1$: no hay cambio.
- Si $-1<c<0$: compresión vertical **más reflexión respecto al eje $x$**.
- Si $c=-1$: reflexión pura respecto al eje $x$.
- Si $c<-1$: estiramiento vertical **más reflexión respecto al eje $x$**.
- Si $c=0$: $y\equiv 0$, todos los puntos colapsan sobre el eje $x$.

El dominio se mantiene; la imagen se escala por $\lvert c\rvert$ (y se refleja si $c<0$).

**Resultado:** escalado vertical por factor $\lvert c\rvert$ (estiramiento si $\lvert c\rvert>1$, compresión si $0<\lvert c\rvert<1$); si $c<0$ se compone además con una reflexión respecto al eje $x$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
