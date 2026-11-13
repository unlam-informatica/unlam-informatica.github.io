---
title: Ejercicio 8 — Concentración de un calmante
slug: analisis-matematico-i/unidad-1/practica/ejercicio-8
sidebar:
  order: 8
---


La concentración de un calmante en el torrente sanguíneo de una persona $t$ horas después de haberlo ingerido está dada por $C(t)=-t^2+6t$, donde $C$ es la concentración medida en miligramos por litro.

## 8a

:::note[Enunciado]
Hallar el dominio y la imagen de $C$ bajo contexto. Graficar.
:::

:::tip[Resolución]
La función $C(t)=-t^2+6t$ es cuadrática con coeficiente principal $a=-1<0$: su gráfica es una parábola que abre hacia abajo. Factorizándola se observan sus raíces:



$$
C(t)=t\,(6-t)
$$



Las raíces son $t=0$ y $t=6$. Físicamente:

- En $t=0$ la persona ingiere el calmante y la concentración es $0$.
- En $t=6$ horas el organismo ya eliminó la sustancia y la concentración vuelve a $0$.

Entre ambos instantes la concentración es positiva. Por lo tanto, el dominio en contexto es:



$$
D_C=[0,6]\ \text{(horas)}
$$



Para la imagen, buscamos el valor máximo de $C$. Como la parábola abre hacia abajo, el máximo está en el vértice, en el punto medio de las raíces:



$$
t_v=\dfrac{0+6}{2}=3
$$



Evaluamos $C$ en $t=3$:



$$
C(3)=-(3)^2+6\cdot 3=-9+18=9
$$



La concentración varía entonces entre $0$ y $9$ mg/l:



$$
I_C=[0,9]\ \text{(mg/l)}
$$



Gráficamente, la parábola arranca en el origen $(0,0)$, sube hasta el vértice $(3,9)$ y baja simétricamente hasta $(6,0)$.

**Resultado:** $C:[0,6]\to[0,9]\,/\,C(t)=-t^2+6t$, con $D_C=[0,6]$ h y $I_C=[0,9]$ mg/l.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8b

:::note[Enunciado]
¿En qué instantes de tiempo la concentración es mayor a $8$ mg/l?
:::

:::tip[Resolución]
Planteamos la inecuación:



$$
C(t)>8
$$





$$
-t^2+6t>8
$$



Pasamos todo a un solo miembro:



$$
-t^2+6t-8>0
$$



Multiplicamos ambos miembros por $-1$ (invierte el sentido de la desigualdad):



$$
t^2-6t+8<0
$$



Factorizamos el trinomio. Buscamos dos números que multiplicados den $8$ y sumados $-6$: son $-2$ y $-4$. Por lo tanto:



$$
(t-2)(t-4)<0
$$



El producto de dos factores es negativo cuando tienen signos opuestos. Esto ocurre justamente entre las raíces:



$$
2<t<4
$$



Como ambos extremos están dentro del dominio $[0,6]$, no hay restricciones adicionales por contexto.

**Resultado:** la concentración supera los $8$ mg/l en el intervalo $(2,4)$, es decir, entre las $2$ y las $4$ horas después de ingerir el calmante.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

## 8c

:::note[Enunciado]
Calcular la razón de cambio media de la concentración en los intervalos de tiempo $[1,2]$, $[1;1{,}5]$. Interpretar bajo el contexto del problema.
:::

:::tip[Resolución]
La razón de cambio media de la concentración en un intervalo $[t_1,t_2]$ se define como:



$$
\text{RCM}=\dfrac{C(t_2)-C(t_1)}{t_2-t_1}
$$



**Intervalo $[1,2]$.** Calculamos $C(1)$ y $C(2)$:



$$
C(1)=-(1)^2+6\cdot 1=-1+6=5
$$





$$
C(2)=-(2)^2+6\cdot 2=-4+12=8
$$



Aplicamos la fórmula:



$$
\text{RCM}_{[1,2]}=\dfrac{8-5}{2-1}=\dfrac{3}{1}=3
$$



**Intervalo $[1;1{,}5]$.** Calculamos $C(1{,}5)$:



$$
C(1{,}5)=-(1{,}5)^2+6\cdot 1{,}5=-2{,}25+9=6{,}75
$$



Aplicamos la fórmula:



$$
\text{RCM}_{[1;1{,}5]}=\dfrac{6{,}75-5}{1{,}5-1}=\dfrac{1{,}75}{0{,}5}=3{,}5
$$



**Interpretación.** Cada razón de cambio media indica cuánto crece la concentración por hora en promedio durante el intervalo considerado. En $[1,2]$ la concentración aumenta a un promedio de $3$ mg/l por hora, mientras que en $[1;1{,}5]$ aumenta a $3{,}5$ mg/l por hora. La razón de cambio más alta en el intervalo más corto indica que cerca de $t=1$ h la concentración crece más rápido que entre $t=1$ y $t=2$: a medida que nos acercamos al vértice $t=3$, la pendiente instantánea va disminuyendo hasta anularse en el máximo.

**Resultado:** $\text{RCM}_{[1,2]}=3$ mg/l por hora y $\text{RCM}_{[1;1{,}5]}=3{,}5$ mg/l por hora.

**Verificación:** Coincide con la respuesta indicada en la guía.
:::

