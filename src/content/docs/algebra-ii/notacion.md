---
title: Notación
description: Notación usada en el manual, que sigue a la cátedra, y su equivalencia con la de Poole y Lay.
slug: algebra-ii/notacion
sidebar:
  order: 4
---

El manual usa la notación de la cátedra en todas las unidades. Los libros de la bibliografía
escriben varios objetos de otra manera y, en dos casos —la matriz de cambio de coordenadas y la
matriz de una transformación lineal—, **con los subíndices en el orden inverso**. Conviene tener esta
página a mano cuando se lee un libro y se resuelve un ejercicio de la guía al mismo tiempo.

## Conjuntos, cuerpos y espacios

| Objeto | En este manual | Observaciones |
|---|---|---|
| Cuerpo de escalares | $K$; en general $\mathbb{R}$ o $\mathbb{Z}_2$ | $\mathbb{Z}_2=\{0,1\}$ con suma y producto módulo 2. Algunos textos escriben $\mathbb{F}_2$ o GF(2). |
| $n$-uplas | $\mathbb{R}^n$, $\mathbb{Z}_2^n$ | En el texto, con comas: $(1,0,-2)$. En las cuentas matriciales, como columnas. |
| Matrices | $\mathbb{R}^{m\times n}$, $\mathbb{Z}_2^{m\times n}$ | $m$ filas, $n$ columnas. |
| Polinomios | $P_n[\mathbb{R}]$ | Polinomios de grado menor o igual que $n$, más el polinomio nulo. |
| Vector nulo | $0_V$ o $0$ | |
| Base | $B=\{v_1,\dots,v_n\}$ | Siempre **ordenada**: cambiar el orden cambia las coordenadas. |
| Base canónica | $E$ | En $P_2[\mathbb{R}]$, $E=\{1,x,x^2\}$ en ese orden. |

## Unidad 1

| Objeto | En este manual | En Poole / Lay |
|---|---|---|
| Subespacio generado | $\operatorname{gen}\{v_1,\dots,v_k\}$ | Poole: gen; Lay: Gen o Span |
| Espacio fila, columna y nulo | $\operatorname{fil}(A)$, $\operatorname{col}(A)$, $\operatorname{nul}(A)$ | Poole: renglón$(A)$, col$(A)$, nul$(A)$; Lay: Fil, Col, Nul |
| Rango de una matriz | $\operatorname{rango}(A)$ | Poole: rank$(A)$ |
| Coordenadas de $v$ en $B$ | $[v]_B$, vector columna | Igual en ambos |
| Matriz de cambio de $B$ a $B'$ | $C_{BB'}$, columnas $[b_j]_{B'}$ | $P_{B'\leftarrow B}$ |

La propiedad que define a la matriz de cambio es

$$
C_{BB'}\,[v]_B=[v]_{B'},
$$

de modo que $C_{B'B}=C_{BB'}^{-1}$ y $C_{BB''}=C_{B'B''}\,C_{BB'}$. En la notación de los libros, la
misma matriz se escribe $P_{B'\leftarrow B}$: la flecha apunta hacia la base de llegada, y la base de
salida queda **a la derecha**. En la notación de la cátedra la base de salida es el **primer**
subíndice.

| Códigos | En este manual | En Poole |
|---|---|---|
| Código lineal | $(n,k)$: subespacio de dimensión $k$ de $\mathbb{Z}_2^n$ | Igual |
| Matriz generadora | $G\in\mathbb{Z}_2^{k\times n}$, sus **filas** forman una base del código; se codifica $a\mapsto aG$ | $G\in\mathbb{Z}_2^{n\times k}$, sus **columnas** generan el código; se codifica $x\mapsto Gx$ |
| Matriz de control de paridad | $H$, con $\mathcal C=\operatorname{nul}(H)$: $v\in\mathcal C \iff Hv^t=0$ | $P$, con $Pc=0$ |
| Síndrome | $Hv^t$ | Poole no usa la palabra; calcula $Pc'$ |
| Peso y distancia de Hamming | $w(v)$, $d_H(u,v)=w(u+v)$ | $w(v)$, $d_H(u,v)$ |

Las dos convenciones describen los mismos códigos: la matriz generadora de una es la transpuesta de
la de la otra.

## Unidad 2

| Objeto | En este manual | En Poole / Lay |
|---|---|---|
| Núcleo | $\operatorname{Nu}(T)$ | kernel, $\ker(T)$ |
| Imagen | $\operatorname{Im}(T)$ | Poole: rango$(T)$ (¡no confundir con el rango de una matriz!) |
| Matriz de $T$ de $B$ a $B'$ | $M(T)_{BB'}$, columnas $[T(b_j)]_{B'}$ | Poole: $[T]_{B'\leftarrow B}$; Lay: "matriz de $T$ relativa a las bases $B$ y $B'$" |
| Endomorfismo en una base | $M(T)_B$ | $[T]_B$ |

La propiedad que define a la matriz asociada es

$$
M(T)_{BB'}\,[v]_B=[T(v)]_{B'},
$$

y el cambio de bases se escribe

$$
M(T)_{B_1B_1'}=C_{B'B_1'}\;M(T)_{BB'}\;C_{B_1B}.
$$

Leída de derecha a izquierda: se pasa de coordenadas en $B_1$ a coordenadas en $B$, se aplica $T$ y
se pasa de $B'$ a $B_1'$. Los subíndices contiguos coinciden, lo que permite controlar el orden.

## Unidad 3

| Objeto | En este manual | En Poole / Lay |
|---|---|---|
| Autovalor, autovector | $Av=\lambda v$, $v\neq 0$ | Poole: eigenvalor, eigenvector; Lay: valor propio, vector propio |
| Polinomio característico | $p_A(\lambda)=\det(\lambda I-A)$ | $\det(A-\lambda I)$ |
| Autoespacio | $E_\lambda(A)=\operatorname{nul}(\lambda I-A)$ | $E_\lambda$ |
| Multiplicidades | $m_a(\lambda)$ algebraica, $m_g(\lambda)=\dim E_\lambda(A)$ geométrica | Igual |
| Diagonalización | $A=CDC^{-1}$, $C$ con autovectores en columnas | Poole: $P^{-1}AP=D$; Lay: $A=PDP^{-1}$ |
| Matriz de transición (Markov) | $P$ estocástica por columnas, $x_{k+1}=Px_k$ | Igual en Poole |

Los dos polinomios característicos difieren a lo sumo en el signo: $\det(A-\lambda I)=(-1)^n\det(\lambda
I-A)$, así que tienen las mismas raíces. El de la cátedra es mónico.

## Unidad 4

| Objeto | En este manual |
|---|---|
| Producto interno | $\langle u,v\rangle$; el usual de $\mathbb{R}^n$ también se escribe $u\cdot v$ |
| Espacio euclídeo | $(V,\langle\,,\rangle)$ |
| Norma | $\lVert v\rVert=\sqrt{\langle v,v\rangle}$ |
| Distancia y ángulo | $d(u,v)=\lVert u-v\rVert$, $\angle(u,v)$ |
| Ortogonalidad | $u\perp v$; complemento ortogonal $S^\perp$ |
| Proyección ortogonal | $\operatorname{proy}_S(v)$ |
| Distancia a un subespacio | $d(v,S)=\lVert v-\operatorname{proy}_S(v)\rVert$ |
| Código dual | $\mathcal C^\perp$ |

## Otras convenciones

- Transpuesta: $A^t$. Traza: $\operatorname{tr}(A)$. Matriz diagonal: $\operatorname{diag}(d_1,\dots,d_n)$.
- Operaciones de fila: $F_2-2F_1\to F_2$ indica que la fila 2 se reemplaza por $F_2-2F_1$.
- "LI" y "LD": linealmente independiente y dependiente. "CL": combinación lineal. "TL":
  transformación lineal.
