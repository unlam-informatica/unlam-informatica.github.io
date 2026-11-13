---
title: Ejercicios adicionales
slug: analisis-matematico-i/unidad-1/practica/adicionales
sidebar:
  order: 33
---


### Adicional 1 — Paridad (V/F)

**a) $h(x)=\dfrac{2x}{x^2+5}$ "no tiene paridad".**



$$
h(-x)=\dfrac{2(-x)}{(-x)^2+5}=\dfrac{-2x}{x^2+5}=-h(x)
$$



La función es **impar** (sí tiene paridad).

> ⚠️ **Discrepancia:** Resultado calculado: $h$ es **impar** ($h(-x)=-h(x)$). Respuesta del documento: "no tiene paridad".
>
> **Causa probable:** el enunciado afirma erróneamente que no tiene paridad. Como cumple $h(-x)=-h(x)$, es impar. La afirmación del documento es **falsa**.

**b) $h(x)=\dfrac{3x^2}{x-5}$ "es par".**



$$
h(-x)=\dfrac{3x^2}{-x-5}=-\dfrac{3x^2}{x+5}
$$



Esto **no** es igual a $h(x)=\dfrac{3x^2}{x-5}$ ni a $-h(x)$. No tiene paridad (ni par ni impar).

> ⚠️ **Discrepancia:** Resultado calculado: $h$ **no es par** (no tiene paridad). Respuesta del documento: "es par".
>
> **Causa probable:** aunque el numerador $3x^2$ es par, el denominador $x-5$ rompe toda simetría; además el dominio $\mathbb{R}-\lbrace 5\rbrace $ no es simétrico respecto al origen, condición necesaria para tener paridad. La afirmación del documento es **falsa**.

**c) $k(x)=\dfrac{x^3}{16-x^2}$ "es impar".**



$$
k(-x)=\dfrac{(-x)^3}{16-(-x)^2}=\dfrac{-x^3}{16-x^2}=-k(x)
$$



Cociente de impar ($x^3$) sobre par ($16-x^2$) = impar; dominio $(-4,4)\setminus$... simétrico. Es **impar**.

**Resultado: impar.** ✓ Coincide con la respuesta oficial.

### Adicional 2 — $N(t)=227\,e^{0{,}007t}$ (millones, $t$ años post-1980)

**a) Variables y función:** independiente $t$ (años desde 1980), dependiente $N$ (millones). $N(t)=227\,e^{0{,}007t}$, con $N(0)=227$.

**b) Variación 1980–1990 ($t:0\to10$):**



$$
N(10)=227\,e^{0{,}07}\approx227\cdot1{,}0725\approx243{,}46
$$



Variación $\approx243{,}46-227=16{,}46$ millones. Razón media $\approx1{,}65$ millones/año.

**c) Inversa:**



$$
N=227\,e^{0{,}007t}\Rightarrow e^{0{,}007t}=\dfrac{N}{227}\Rightarrow t=\dfrac{1}{0{,}007}\ln\!\left(\dfrac{N}{227}\right)=\dfrac{\ln(N/227)}{0{,}007}
$$



Da el tiempo (años desde 1980) para una población dada.

**d) ¿Cuándo más del doble de 1980?** $N=2\cdot227=454$:



$$
e^{0{,}007t}=2\Rightarrow t=\dfrac{\ln2}{0{,}007}\approx\dfrac{0{,}6931}{0{,}007}\approx99{,}0
$$



**Resultado: a los $\approx99$ años (alrededor del año 2079).**

### Adicional 3 — $L(d)=-10\log_2(d)+120$ (dB)

**a) Si $L=90$, hallar la distancia:**



$$
90=-10\log_2(d)+120\Rightarrow-10\log_2 d=-30\Rightarrow\log_2 d=3\Rightarrow d=2^3=8\ \text{m}
$$



Terna en contexto: $L:(0,+\infty)\to\mathbb{R}$ (físicamente acotado por la fuente). **Distancia inicial $=8$ m.**

**b) Distancia para $60$ dB:**



$$
60=-10\log_2 d+120\Rightarrow\log_2 d=6\Rightarrow d=2^6=64\ \text{m}
$$



**c) Inversa:**



$$
L=-10\log_2 d+120\Rightarrow\log_2 d=\dfrac{120-L}{10}\Rightarrow d=2^{(120-L)/10}
$$



**Resultado: $d(L)=2^{(120-L)/10}$.**

### Adicional 4 — $C(q)=10+3\sqrt q$ (costo)

**a) ¿Costo cero si $q=0$?** $C(0)=10+0=10\neq0$. Hay un **costo fijo de $10$** aunque no se produzca nada. (No, no es cero.)

**b) Razón de cambio media de $100$ a $101$:**



$$
\dfrac{C(101)-C(100)}{1}=3\left(\sqrt{101}-\sqrt{100}\right)=3(10{,}0499-10)=3\cdot0{,}0499\approx0{,}1496\approx0{,}15
$$



**c) Costo instantáneo (marginal) en $100$ y comparación.** La derivada (Unidad 3) es $C'(q)=\dfrac{3}{2\sqrt q}$; en $q=100$: $C'(100)=\dfrac{3}{2\cdot10}=0{,}15$.

**Resultado: la razón media ($\approx0{,}15$) coincide casi exactamente con el costo marginal instantáneo ($0{,}15$), porque el intervalo es muy pequeño ($\Delta q=1$).**

### Adicional 5 — (opción múltiple) $V(t)=10\left(1-\tfrac{t}{100}\right)^2$, $0\le t\le100$

Dominio $[0,100]$; $V(0)=10$, $V(100)=0$, decreciente en ese tramo, imagen $[0,10]$.

Inversa: $\dfrac{V}{10}=\left(1-\tfrac{t}{100}\right)^2\Rightarrow1-\tfrac{t}{100}=\sqrt{\dfrac{V}{10}}$ (raíz positiva, pues $1-\tfrac t{100}\ge0$) $\Rightarrow t=100\left(1-\sqrt{\dfrac{V}{10}}\right)$.

$V^{-1}:[0,10]\to[0,100]$. **Resultado: la opción correcta es la c) (terna $V^{-1}:[0,10]\to[0,100]$, $t(V)=100\!\left(1-\sqrt{V/10}\right)$).** ✓ Coincide.

### Adicional 6 — (opción múltiple) $g(x)=\dfrac{x^3}{\sqrt{16-x^2}}$

**Dominio:** $16-x^2>0$ (estricto, en denominador) $\Rightarrow-4<x<4$, es decir $(-4,4)$.

**Paridad:**



$$
g(-x)=\dfrac{(-x)^3}{\sqrt{16-x^2}}=\dfrac{-x^3}{\sqrt{16-x^2}}=-g(x)
$$



Dominio simétrico y $g(-x)=-g(x)$: **impar**.

**Resultado: impar, dominio $(-4,4)$.** ✓ Coincide.

### Adicional 7 — (opción múltiple) $m(x)=3\operatorname{sen}(5x)$

Por convención se restringe $5x\in\left[-\tfrac\pi2,\tfrac\pi2\right]\Rightarrow x\in\left[-\tfrac{\pi}{10},\tfrac{\pi}{10}\right]$; imagen $[-3,3]$.



$$
y=3\operatorname{sen}(5x)\Rightarrow\operatorname{sen}(5x)=\dfrac y3\Rightarrow 5x=\arcsin\!\left(\dfrac y3\right)\Rightarrow x=\dfrac15\arcsin\!\left(\dfrac y3\right)
$$



**Resultado: $m^{-1}:[-3,3]\to\left[-\tfrac{\pi}{10},\tfrac{\pi}{10}\right]$, $m^{-1}(x)=\tfrac15\arcsin\!\left(\tfrac x3\right)$.** ✓ Coincide.

### Adicional 8 — (opción múltiple) $U(t)=1000(1-e^{-0{,}05t})$

Para $t\ge0$: $U(0)=0$ y $U\to1000$ cuando $t\to+\infty$ (sin alcanzarlo). Imagen $[0,1000)$.

Inversa:



$$
U=1000(1-e^{-0{,}05t})\Rightarrow1-e^{-0{,}05t}=\dfrac{U}{1000}\Rightarrow e^{-0{,}05t}=1-\dfrac{U}{1000}\Rightarrow t=-20\ln\!\left(1-\dfrac{U}{1000}\right)
$$



El dominio de la inversa es la imagen de $U$.

**Resultado: $t(U)=-20\ln\!\left(1-\tfrac{U}{1000}\right)$, con dominio $[0,1000)$.** ✓ Coincide.

