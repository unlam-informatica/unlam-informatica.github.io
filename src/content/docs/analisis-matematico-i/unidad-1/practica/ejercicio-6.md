---
title: Ejercicio 6 — Caja sin tapa
slug: analisis-matematico-i/unidad-1/practica/ejercicio-6
sidebar:
  order: 6
---


:::note[Enunciado]
Expresar el volumen $V(x)$ de una caja sin tapa que se construye a partir de una pieza de cartón de $24\text{cm}\times 32\text{cm}$ cortando en las esquinas cuadrados de lado $x$. ¿Cuál es el dominio de dicha función de acuerdo al contexto? Con ayuda de GG estimar cuántos centímetros debe tener el cuadrado que se corte para que el volumen de la caja sea máximo.
:::

:::tip[Resolución]
**Planteo de la fórmula.** Partimos de una pieza rectangular de cartón de $24\text{ cm}\times 32\text{ cm}$ y cortamos un cuadrado de lado $x$ en cada una de las cuatro esquinas. Al doblar las solapas hacia arriba se forma una caja sin tapa con:

- Base rectangular de dimensiones $(24-2x)$ por $(32-2x)$ cm.
- Altura igual al lado del cuadrado recortado, es decir, $x$ cm.

El volumen de la caja es el producto de la base por la altura:



$$
V(x)=(24-2x)\,(32-2x)\,x
$$



Sacando factor común $2$ en cada paréntesis se obtiene una expresión equivalente más cómoda para analizar:



$$
V(x)=4\,x\,(12-x)\,(16-x)
$$



**Dominio en contexto.** Para que la caja exista físicamente deben cumplirse simultáneamente tres condiciones:



$$
x>0,\qquad 24-2x>0,\qquad 32-2x>0
$$



Despejando las dos últimas:



$$
x<12,\qquad x<16
$$



La restricción más fuerte es $x<12$ (la otra se cumple automáticamente). Combinando con $x>0$:



$$
D_V=(0,12)
$$



**Estimación del máximo con GeoGebra.** Como $V(x)=4x(12-x)(16-x)$ es un polinomio de grado $3$ con coeficiente principal positivo en $-x^3$ (al expandir queda $V(x)=4x^3-112x^2+768x$ con signo principal positivo en $4x^3$, pero al evaluar en el intervalo $(0,12)$ presenta un único máximo local), graficamos $V$ en GeoGebra restringida al dominio $(0,12)$. Con el comando `Extremo[V, 0, 12]` o moviendo el cursor sobre la curva se obtiene:



$$
x_{\max}\approx 4{,}53\text{ cm}
$$



Evaluando $V$ en ese valor:



$$
V(4{,}53)=4\cdot 4{,}53\cdot(12-4{,}53)\cdot(16-4{,}53)
$$





$$
V(4{,}53)\approx 4\cdot 4{,}53\cdot 7{,}47\cdot 11{,}47
$$





$$
V(4{,}53)\approx 1552{,}5\text{ cm}^3
$$



Observación: el valor exacto se obtiene resolviendo $V'(x)=0$ (Unidad 3), que da $x_{\max}=\dfrac{4(7-\sqrt{13})}{3}\approx 4{,}526\text{ cm}$.

**Resultado:** $V(x)=(24-2x)(32-2x)\,x=4x(12-x)(16-x)$, con $D_V=(0,12)$. El volumen es máximo cuando se cortan cuadrados de $x\approx 4{,}53$ cm de lado, alcanzando $V_{\max}\approx 1552{,}5$ cm³.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

