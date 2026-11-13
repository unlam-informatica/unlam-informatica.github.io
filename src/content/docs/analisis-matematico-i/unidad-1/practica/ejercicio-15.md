---
title: Ejercicio 15 — Reflexiones
slug: analisis-matematico-i/unidad-1/practica/ejercicio-15
sidebar:
  order: 15
---


Describir qué efecto produce en la gráfica de $y=f(x)$ realizar las siguientes operaciones en la regla de asignación.

## 15a

:::note[Enunciado]
$y=-f(x)$.
:::

:::tip[Resolución]
Multiplicar la salida por $-1$ cambia el signo de cada valor $f(x)$. El punto $(x,f(x))$ pasa a $(x,-f(x))$: la coordenada $x$ se mantiene y la $y$ cambia de signo. Geométricamente, cada punto se "voltea" verticalmente respecto al eje $x$.

Es un caso particular de `14d` con $c=-1$: no hay estiramiento ni compresión, solo cambio de signo.

Lo que estaba arriba del eje $x$ pasa abajo y viceversa. Los puntos sobre el eje $x$ (donde $f(x)=0$, los ceros) quedan fijos.

El dominio se mantiene; la imagen se refleja: si la imagen original era $[a,b]$, la nueva es $[-b,-a]$.

**Resultado:** reflexión respecto al eje $x$ ("vertical"). Los ceros de $f$ se preservan.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 15b

:::note[Enunciado]
$y=f(-x)$.
:::

:::tip[Resolución]
Reemplazar la entrada por $-x$ evalúa $f$ en el valor opuesto. El punto $(x,f(x))$ pasa a $(-x,f(x))$: la coordenada $y$ se mantiene y la $x$ cambia de signo. Geométricamente, cada punto se "voltea" horizontalmente respecto al eje $y$.

Es un caso particular de `14c` con $c=-1$: no hay estiramiento ni compresión, solo intercambio de izquierda y derecha.

Lo que estaba a la derecha del eje $y$ pasa a la izquierda y viceversa. Los puntos sobre el eje $y$ (donde $x=0$) quedan fijos.

La imagen se mantiene; el dominio se refleja: si el dominio original era $[a,b]$, el nuevo es $[-b,-a]$.

**Observación.** Si $f$ es **par**, $f(-x)=f(x)$ y la gráfica queda igual. Si $f$ es **impar**, $f(-x)=-f(x)$ y se obtiene el mismo efecto que en `15a` (reflexión respecto al eje $x$).

**Resultado:** reflexión respecto al eje $y$ ("horizontal"). Los puntos sobre el eje $y$ se preservan.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
