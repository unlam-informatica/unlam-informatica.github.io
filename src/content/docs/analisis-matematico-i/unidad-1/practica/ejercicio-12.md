---
title: Ejercicio 12* — Beneficio de una empresa
slug: analisis-matematico-i/unidad-1/practica/ejercicio-12
sidebar:
  order: 12
---


El beneficio de una empresa (en miles de euros) a lo largo de sus $8$ años de existencia viene dado por:



$$
B(t)=\begin{cases} -t^2+7t & \text{si } 0\leq t\leq 5, \\ 10 & \text{si } 5<t\leq 8 \end{cases}
$$



Donde $t$ es el tiempo en años.

## 12a

:::note[Enunciado]
Graficar la función.
:::

:::tip[Resolución]
La función $B$ tiene dos tramos.

**Tramo $0\leq t\leq 5$.** $B(t)=-t^2+7t$ es una parábola con coeficiente principal $a=-1<0$: abre hacia abajo. Sus raíces son $0$ y $7$ (despejando $-t^2+7t=t(7-t)=0$). El vértice está en el punto medio entre las raíces:



$$
t_v=\dfrac{0+7}{2}=3{,}5
$$





$$
B(3{,}5)=-(3{,}5)^2+7\cdot 3{,}5=-12{,}25+24{,}5=12{,}25
$$



En $t=0$ vale $0$ y en $t=5$ vale $-25+35=10$.

**Tramo $5<t\leq 8$.** $B(t)=10$ es una recta horizontal a altura $10$.

La gráfica es entonces un arco de parábola que va de $(0,0)$, sube hasta el vértice $(3{,}5;\,12{,}25)$ y baja hasta $(5,10)$, seguido por un segmento horizontal de altura $10$ desde $t=5$ hasta $t=8$. Notar que la unión es **continua** en $t=5$ porque ambos tramos valen $10$ allí.

**Resultado:** ver descripción anterior. Verificable en GeoGebra cargando $B(t)$ como función por tramos.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 12b

:::note[Enunciado]
¿En qué momento tuvo la empresa su mayor beneficio? ¿De cuánto fue ese beneficio?
:::

:::tip[Resolución]
Comparamos los máximos de cada tramo.

**Tramo $0\leq t\leq 5$.** El máximo de la parábola está en el vértice calculado en `12a`:



$$
t_v=3{,}5,\qquad B(3{,}5)=12{,}25
$$



Como $t_v=3{,}5$ está dentro del intervalo $[0,5]$, ese valor es realmente alcanzado.

**Tramo $5<t\leq 8$.** $B(t)=10$ es constante.

Como $12{,}25>10$, el máximo absoluto de $B$ se alcanza en $t=3{,}5$.

**Resultado:** la empresa tuvo su mayor beneficio a los $3{,}5$ años (es decir, a los $3$ años y $6$ meses), y fue de $12{,}25$ miles de euros, equivalente a $12\,250$ euros.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 12c

:::note[Enunciado]
¿Cuándo se espera un beneficio de $11\,250\,000$ euros?
:::

:::tip[Resolución]
Interpretamos el monto en las unidades de la función. El enunciado indica que $B$ está expresado "en miles de euros", pero el máximo absoluto calculado en `12b` es $12{,}25$, valor incompatible con $11\,250\,000$ si la unidad fuera literalmente miles (sería $11\,250$ veces el máximo). La interpretación consistente es que $11\,250\,000$ euros corresponden a $B=11{,}25$ en la unidad nativa de la función (lo que sugiere que la unidad real es millones de euros).

Buscamos los $t$ tales que $B(t)=11{,}25$ analizando cada tramo.

**Tramo $5<t\leq 8$.** $B(t)=10\neq 11{,}25$, sin solución.

**Tramo $0\leq t\leq 5$.** Planteamos:



$$
-t^2+7t=11{,}25
$$





$$
t^2-7t+11{,}25=0
$$



Aplicamos la resolvente:



$$
t=\dfrac{7\pm\sqrt{49-45}}{2}=\dfrac{7\pm 2}{2}
$$



Las dos soluciones son $t=2{,}5$ y $t=4{,}5$. Ambas pertenecen al intervalo $[0,5]$, por lo que son válidas.

**Resultado:** se espera un beneficio de $11\,250\,000$ euros ($B=11{,}25$) en dos momentos: $t=2{,}5$ años (cuando la curva sube hacia el máximo) y $t=4{,}5$ años (cuando vuelve a bajar después del máximo).

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 12d

:::note[Enunciado]
¿Qué le sucedió a la empresa, en cuanto a sus beneficios, después del quinto año?
:::

:::tip[Resolución]
A partir de $t=5$ la función pasa del primer tramo (parábola) al segundo tramo ($B(t)=10$, constante).

En $t=5$ el valor $-25+35=10$ coincide con el del segundo tramo, así que la transición es continua. A partir de allí y hasta $t=8$, el beneficio se mantiene **constante** en $10$ miles de euros, sin crecer ni decrecer.

En términos del negocio: la empresa atravesó una fase de crecimiento parabólico hasta los $3{,}5$ años (su mejor momento, con $B=12{,}25$), luego comenzó a bajar y, al llegar a los $5$ años con $B=10$, esa cifra se estabilizó. Desde el quinto año en adelante el beneficio fue constante.

**Resultado:** después del quinto año el beneficio se estabilizó en $B=10$, manteniéndose constante hasta el año $8$.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::
