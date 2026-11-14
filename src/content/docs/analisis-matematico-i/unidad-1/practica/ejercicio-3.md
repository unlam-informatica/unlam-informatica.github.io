---
title: Ejercicio 3 — Vaciado de un tanque
slug: analisis-matematico-i/unidad-1/practica/ejercicio-3
sidebar:
  order: 3
  label: Ejercicio 3
---


El siguiente gráfico muestra el vaciado de un tanque de agua. Sólo mirando el gráfico respondan las siguientes preguntas. Del gráfico se lee que la cantidad de agua decrece linealmente desde $4000$ L en $t=0$ hasta $0$ L en $t=16$ min.

![Vaciado de un tanque](/analisis-matematico-i/unidad-1/practica/3.png)

## 3a

:::note[Enunciado]
¿Cuánta agua había en el tanque y en cuánto tiempo tardó en vaciarse?
:::

:::tip[Resolución]
Leyendo el gráfico:

- La recta cruza el eje vertical (cantidad de agua) en el valor $4000$, que corresponde al instante inicial $t=0$.
- La recta cruza el eje horizontal (tiempo) en $t=16$, momento en el que la cantidad de agua vale $0$.

Por lo tanto, la cantidad inicial de agua era $4000$ L y el tanque tardó $16$ minutos en vaciarse.

**Resultado:** había $4000$ L y tardó $16$ minutos en vaciarse.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 3b

:::note[Enunciado]
¿Cuántos litros por minuto salían del tanque cuando se vaciaba?
:::

:::tip[Resolución]
La cantidad de litros por minuto que salen del tanque es el valor absoluto de la razón de cambio del volumen respecto al tiempo, es decir, la pendiente de la recta del gráfico.

Tomamos los dos puntos extremos $(0,4000)$ y $(16,0)$:



$$
m=\dfrac{V_2-V_1}{t_2-t_1}
$$



Reemplazamos:



$$
m=\dfrac{0-4000}{16-0}=\dfrac{-4000}{16}=-250\ \dfrac{\text{L}}{\text{min}}
$$



El signo negativo indica que el volumen disminuye con el tiempo. La cantidad de litros que salen por minuto es el módulo de esa razón.

**Resultado:** salían $250$ L/min del tanque.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 3c

:::note[Enunciado]
Marquen en el gráfico el momento en el que en el tanque había $1000$ litros. ¿Cuánto tiempo había transcurrido desde que se comenzó a vaciar?
:::

:::tip[Resolución]
Necesitamos el instante $t$ para el cual el volumen es $V(t)=1000$. Usamos la fórmula que describe la recta (deducida en el bloque analítico):



$$
V(t)=4000-250\,t
$$



Imponemos $V(t)=1000$:



$$
1000=4000-250\,t
$$



Despejamos $t$:



$$
250\,t=4000-1000
$$





$$
250\,t=3000
$$





$$
t=\dfrac{3000}{250}=12
$$



En el gráfico se marca el punto $(12,1000)$ sobre la recta.

**Resultado:** habían transcurrido $12$ minutos.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 3d

**Trabajando analíticamente**

:::note[Enunciado]
- Si queremos relacionar el tiempo de vaciado con la cantidad de agua en el tanque ¿cuál sería la variable independiente y cuál la dependiente?
- Definirlas con simbología adecuada y unidades correspondientes. ¿Cuál es el dominio e imagen en contexto?
- Escriban una fórmula que calcule la cantidad de agua a los $t$ minutos.
- ¿Cuál es la razón de cambio de volumen respecto al tiempo en un intervalo de $5$ minutos? ¿Y en uno de $10$ minutos?
:::

:::tip[Resolución]
**Variables.** La cantidad de agua en el tanque depende del tiempo transcurrido desde que comenzó el vaciado, por lo que:

- Variable independiente: $t$, el tiempo, medido en minutos.
- Variable dependiente: $V$, el volumen de agua, medido en litros.

**Dominio e imagen en contexto.** El tiempo arranca en $0$ (instante en que empieza a vaciarse) y termina en $16$ (instante en que el tanque queda vacío). El volumen va desde los $4000$ L iniciales hasta los $0$ L finales. Por lo tanto:



$$
D=[0,16]\ \text{min},\qquad I=[0,4000]\ \text{L}
$$



**Fórmula.** Buscamos la recta que pasa por $(0,4000)$ y $(16,0)$. La ordenada al origen es $4000$ y la pendiente, calculada en `3b`, es $-250$. Entonces:



$$
V(t)=4000-250\,t
$$



**Razón de cambio en distintos intervalos.** La razón de cambio media del volumen respecto al tiempo en un intervalo $[t_1,t_2]$ es:



$$
\dfrac{\Delta V}{\Delta t}=\dfrac{V(t_2)-V(t_1)}{t_2-t_1}
$$



Como $V$ es una función lineal con pendiente $-250$, esa razón es constante e igual a la pendiente para cualquier intervalo, sin importar su longitud:



$$
\dfrac{\Delta V}{\Delta t}=-250\ \dfrac{\text{L}}{\text{min}}
$$



En particular:

- En un intervalo de $5$ minutos: $\Delta V=-250\cdot 5=-1250$ L, con razón de cambio $-250$ L/min.
- En un intervalo de $10$ minutos: $\Delta V=-250\cdot 10=-2500$ L, con razón de cambio $-250$ L/min.

El signo negativo refleja que en cualquier intervalo el volumen disminuye.

**Resultado:** $V:[0,16]\to[0,4000]\,/\,V(t)=4000-250\,t$, con razón de cambio constante igual a $-250$ L/min (equivalente a $-1250$ L cada $5$ min y $-2500$ L cada $10$ min).

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

