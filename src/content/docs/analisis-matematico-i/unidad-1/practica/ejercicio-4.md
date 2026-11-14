---
title: Ejercicio 4 — Resorte
slug: analisis-matematico-i/unidad-1/practica/ejercicio-4
sidebar:
  order: 4
  label: Ejercicio 4
---


Para diseñar un vehículo es necesario crear un modelo que permita determinar la respuesta de un resorte con diferentes cargas. Se realizó un experimento para medir el estiramiento ($y$) de un resorte, en pulgadas, como una función del número ($x$) de unidades de masa colocadas como carga en él y se obtuvieron los siguientes resultados:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| $y$ | $0$ | $0{,}875$ | $1{,}721$ | $2{,}641$ | $3{,}531$ | $4{,}391$ | $5{,}241$ | $6{,}120$ | $6{,}992$ |


## 4a

:::note[Enunciado]
¿Cuál es la variable independiente y dependiente del problema? (con sus unidades).
:::

:::tip[Resolución]
El experimento consiste en colocar distintas cargas en el resorte y medir cuánto se estira. La causa es la masa que colgamos, y el efecto es el estiramiento que provoca. Entonces:

- Variable independiente: $x$, el número de unidades de masa colocadas como carga (adimensional, "unidades de masa").
- Variable dependiente: $y$, el estiramiento del resorte, medido en pulgadas.

**Resultado:** $x$ (unidades de masa) es la independiente; $y$ (pulgadas) es la dependiente.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 4b

:::note[Enunciado]
Usar **Tabla** en GeoGebra para graficar los puntos en un par de ejes cartesianos y comprobar la hipótesis de que el estiramiento "y" es proporcional a la masa "x" que se cuelga del resorte.
:::

:::tip[Resolución]
Dos cantidades $x$ e $y$ son proporcionales cuando existe una constante $k$ tal que



$$
y=k\,x,
$$



es decir, el cociente $\dfrac{y}{x}$ se mantiene aproximadamente constante para todos los valores observados (excluyendo $x=0$). Verificamos esa condición con la tabla:

| $x$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| $y/x$ | $0{,}875$ | $0{,}861$ | $0{,}880$ | $0{,}883$ | $0{,}878$ | $0{,}874$ | $0{,}874$ | $0{,}874$ |

Todos los cocientes están muy próximos a $0{,}875$, con pequeñas variaciones atribuibles al error de medición. Esto confirma la hipótesis de proporcionalidad directa.

Al graficar los puntos en GeoGebra (comando **Tabla**), los $9$ puntos quedan prácticamente alineados sobre una recta que pasa por el origen, lo que es consistente con $y=k\,x$.

**Resultado:** los cocientes $y/x$ son aproximadamente constantes ($\approx 0{,}875$) y los puntos se alinean sobre una recta por el origen, por lo que la hipótesis de proporcionalidad se verifica.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 4c

:::note[Enunciado]
Estimar la constante de proporcionalidad con GeoGebra utilizando el comando **Regresión** (se puede encontrar en los "tres puntitos" en la tabla) y armar la función obtenida. O hacerlo manualmente.
:::

:::tip[Resolución]
Para estimar la constante de proporcionalidad $k$ de la relación $y=k\,x$, podemos:

- **Usar GeoGebra:** seleccionar la tabla, elegir **Regresión** $\to$ **Lineal** y obtener la ecuación $y\approx 0{,}875\,x$.
- **Hacerlo manualmente:** promediar los cocientes $y/x$ calculados en `4b`:



$$
\bar{k}=\dfrac{0{,}875+0{,}861+0{,}880+0{,}883+0{,}878+0{,}874+0{,}874+0{,}874}{8}
$$





$$
\bar{k}\approx 0{,}875
$$



Ambos caminos llevan al mismo valor:



$$
k\approx 0{,}875
$$



La función obtenida es:



$$
f(x)=0{,}875\,x
$$



**Resultado:** $k\approx 0{,}875$ pulgadas por unidad de masa, y la función es $f(x)=0{,}875\,x$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 4d

:::note[Enunciado]
Identificar dominio e imagen de la función definida en el ítem c) bajo el contexto del problema.
:::

:::tip[Resolución]
En el contexto del experimento, la variable $x$ representa la cantidad de unidades de masa colocadas como carga, y se midió para los valores enteros entre $0$ y $8$. Considerando el rango medido como dominio del modelo:



$$
D_f=[0,8]
$$



Como $f(x)=0{,}875\,x$ es una función lineal creciente, los valores mínimo y máximo de la imagen se alcanzan en los extremos del dominio:



$$
f(0)=0{,}875\cdot 0=0
$$





$$
f(8)=0{,}875\cdot 8=7
$$



Por lo tanto:



$$
I_f=[0,7]
$$



La función expresada como terna queda:



$$
f:[0,8]\to[0,7]\,/\,f(x)=0{,}875\,x
$$



**Resultado:** $f:[0,8]\to[0,7]\,/\,f(x)=0{,}875\,x$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 4e

:::note[Enunciado]
Predecir el estiramiento del resorte si se le carga una masa de $10$ unidades de masa.
:::

:::tip[Resolución]
Para predecir el estiramiento con $10$ unidades de masa, evaluamos la función obtenida en `4c`:



$$
f(x)=0{,}875\,x
$$



Reemplazamos $x=10$:



$$
f(10)=0{,}875\cdot 10
$$





$$
f(10)=8{,}75
$$



Observación: el valor $x=10$ queda fuera del dominio en contexto $[0,8]$, por lo que es una **extrapolación** del modelo. La predicción asume que la relación de proporcionalidad sigue siendo válida fuera del rango medido, lo que físicamente solo se cumple mientras no se supere el límite elástico del resorte.

**Resultado:** se predice un estiramiento de $8{,}75$ pulgadas.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 4f

:::note[Enunciado]
¿Cuál es la razón de cambio del estiramiento del resorte respecto a la carga colgada? Interpretar gráficamente.
:::

:::tip[Resolución]
La razón de cambio media del estiramiento respecto a la carga en un intervalo $[x_1,x_2]$ es:



$$
\dfrac{\Delta y}{\Delta x}=\dfrac{f(x_2)-f(x_1)}{x_2-x_1}
$$



Como $f(x)=0{,}875\,x$ es una función lineal, esa razón es constante e igual a la pendiente para cualquier intervalo:



$$
\dfrac{\Delta y}{\Delta x}=0{,}875\ \dfrac{\text{pulgadas}}{\text{unidad de masa}}
$$



**Interpretación gráfica:** la razón de cambio es la inclinación de la recta $y=0{,}875\,x$. Al ser constante, a incrementos iguales en el eje $x$ les corresponden incrementos iguales en el eje $y$: por cada unidad de masa adicional que se cuelga del resorte, el estiramiento aumenta $0{,}875$ pulgadas.

**Resultado:** la razón de cambio es constante e igual a $0{,}875$ pulgadas por unidad de masa.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

