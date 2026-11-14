---
title: Práctica 4 — Polinomios de Taylor
slug: analisis-matematico-i/unidad-4/practica/practica-4
sidebar:
  order: 0
  label: Guía de práctica
---



Resolución completa y paso a paso de la práctica de polinomios de Taylor y Maclaurin: construcción del polinomio, aproximaciones numéricas, acotación del error mediante el resto de Lagrange y aplicaciones. Recordamos las fórmulas centrales:

- **Taylor de orden $n$ en $a$:** $\;P_n(x)=\displaystyle\sum_{k=0}^{n}\dfrac{f^{(k)}(a)}{k!}\,(x-a)^k$.
- **Maclaurin:** caso $a=0$.
- **Resto de Lagrange:** $\;R_n(x)=\dfrac{f^{(n+1)}(c)}{(n+1)!}\,(x-a)^{n+1}$, con $c$ entre $a$ y $x$; cota $\;\lvert R_n(x)\rvert\le \dfrac{M}{(n+1)!}\,\lvert x-a\rvert^{\,n+1}$, donde $M=\max\lvert f^{(n+1)}\rvert$ en el intervalo.

## Tabla de contenidos


1. TOC


---

## Ejercicio 1

**Enunciado.** Sea $f(x)=e^x$. Graficar $f$ junto con: a) $P(x)=1-x+x^2$; b) $Q(x)=1+x-x^2$; c) $R(x)=1+x+\dfrac{x^2}{2}$. ¿Cuál tiene mayor orden de contacto con $f$ en $a=0$? Probarlo analíticamente.

**Idea de la gráfica.** Las cuatro curvas pasan por $(0,1)$ porque todas valen $1$ en $x=0$. Al graficar (por ejemplo en GeoGebra cargando `f(x)=e^x`, `P(x)=1-x+x^2`, `Q(x)=1+x-x^2`, `R(x)=1+x+x^2/2`) se observa que cerca del origen $R$ es la que se pega a la exponencial, mientras que $P$ se separa enseguida (decrece donde $f$ crece) y $Q$ se aparta por la concavidad opuesta.

**Resolución analítica.** El **orden de contacto** de un polinomio $g$ con $f$ en $a$ es la cantidad de derivadas que coinciden en $a$. Calculamos las derivadas de $f$ en $0$:



$$
f(0)=1,\quad f'(0)=1,\quad f''(0)=1.
$$



Comparamos cada candidato:

- **$P(x)=1-x+x^2$:** $P(0)=1=f(0)$, pero $P'(x)=-1+2x\Rightarrow P'(0)=-1\neq 1$. Coincide solo el valor: contacto de **orden 0**.
- **$Q(x)=1+x-x^2$:** $Q(0)=1$, $Q'(0)=1=f'(0)$, pero $Q''(x)=-2\Rightarrow Q''(0)=-2\neq 1$. Contacto de **orden 1**.
- **$R(x)=1+x+\dfrac{x^2}{2}$:** $R(0)=1$, $R'(0)=1$, $R''(0)=1=f''(0)$. Contacto de **orden 2**.

En efecto, $R$ es exactamente el polinomio de Maclaurin de orden 2 de $e^x$: $P_2(x)=1+x+\dfrac{x^2}{2}$.

**El polinomio $R(x)=1+x+\dfrac{x^2}{2}$ tiene el mayor orden de contacto (orden 2) con $f$ en $a=0$.**

✓ Coincide con la respuesta oficial (es la opción c).

---

## Ejercicio 2

**Enunciado.** Hallar el polinomio de Taylor de orden 3 en $x=a$ y usarlo para aproximar el valor pedido.

### a) $f(x)=\dfrac{1}{x}$, $a=1$, aproximar $f(1{,}3)$

Derivadas:



$$
f(x)=x^{-1},\quad f'(x)=-x^{-2},\quad f''(x)=2x^{-3},\quad f'''(x)=-6x^{-4}.
$$



En $a=1$: $f(1)=1$, $f'(1)=-1$, $f''(1)=2$, $f'''(1)=-6$. Coeficientes:



$$
\dfrac{f(1)}{0!}=1,\;\dfrac{f'(1)}{1!}=-1,\;\dfrac{f''(1)}{2!}=1,\;\dfrac{f'''(1)}{3!}=-1.
$$





$$
\boxed{P_3(x)=1-(x-1)+(x-1)^2-(x-1)^3.}
$$



Aproximación en $x=1{,}3$ ($x-1=0{,}3$):



$$
P_3(1{,}3)=1-0{,}3+0{,}09-0{,}027=0{,}763.
$$



**$f(1{,}3)\approx 0{,}763$** (valor exacto $1/1{,}3=0{,}76923\ldots$).

✓ Coincide con la respuesta oficial.

### b) $f(x)=\cos(x-2)$, $a=2$, aproximar $\cos(0{,}1)$

Derivadas (con $g=x-2$):



$$
f=\cos(x-2),\;f'=-\operatorname{sen}(x-2),\;f''=-\cos(x-2),\;f'''=\operatorname{sen}(x-2).
$$



En $a=2$ (donde $x-2=0$): $f(2)=1$, $f'(2)=0$, $f''(2)=-1$, $f'''(2)=0$.



$$
\boxed{P_3(x)=1-\dfrac{1}{2!}(x-2)^2.}
$$



Para aproximar $\cos(0{,}1)$ notamos que $\cos(0{,}1)=\cos(x-2)$ con $x-2=0{,}1$, es decir $x=2{,}1$:



$$
P_3(2{,}1)=1-\dfrac{1}{2}(0{,}1)^2=1-0{,}005=0{,}995.
$$



**$\cos(0{,}1)\approx 0{,}995$.**

✓ Coincide con la respuesta oficial.

### c) $f(x)=\sqrt{x+1}$, $a=0$, aproximar $\sqrt{0{,}85}$

Derivadas:



$$
f=(x+1)^{1/2},\; f'=\tfrac12(x+1)^{-1/2},\; f''=-\tfrac14(x+1)^{-3/2},\; f'''=\tfrac38(x+1)^{-5/2}.
$$



En $a=0$: $f(0)=1$, $f'(0)=\tfrac12$, $f''(0)=-\tfrac14$, $f'''(0)=\tfrac38$. Coeficientes:



$$
\dfrac{f''(0)}{2!}=-\dfrac18,\qquad \dfrac{f'''(0)}{3!}=\dfrac{3/8}{6}=\dfrac{1}{16}.
$$





$$
\boxed{P_3(x)=1+\dfrac12 x-\dfrac18 x^2+\dfrac{1}{16}x^3.}
$$



Para $\sqrt{0{,}85}$ buscamos $x$ con $x+1=0{,}85\Rightarrow x=-0{,}15$:



$$
P_3(-0{,}15)=1+\tfrac12(-0{,}15)-\tfrac18(0{,}0225)+\tfrac{1}{16}(-0{,}003375).
$$





$$
=1-0{,}075-0{,}0028125-0{,}00021094=0{,}92197656.
$$



**$\sqrt{0{,}85}\approx 0{,}921977$** (valor exacto $0{,}921954\ldots$).

✓ Coincide con la respuesta oficial.

---

## Ejercicio 3*

**Enunciado.** Aproximar usando un polinomio de grado $n$ adecuado: a) $e^{1/2}$, $n=4$; b) $\ln(0{,}4)$, $n=3$; c) $\operatorname{sen}31^\circ$, $n=2$.

### a) $e^{1/2}$ con $n=4$

Maclaurin de $f(x)=e^x$ ($f^{(k)}(0)=1$ para todo $k$):



$$
\boxed{P_4(x)=1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6}+\dfrac{x^4}{24}.}
$$



En $x=\tfrac12$:



$$
P_4(\tfrac12)=1+0{,}5+0{,}125+0{,}0208333+0{,}0026042=1{,}6484375.
$$



**$e^{1/2}\approx 1{,}648438$** (valor exacto $1{,}648721\ldots$).

✓ Coincide con la respuesta oficial.

### b) $\ln(0{,}4)$ con $n=3$

> ⚠️ **Discrepancia:** Resultado calculado: el polinomio $P_3$ centrado en $a=1$ de $f(x)=\ln x$ es $P_3(x)=(x-1)-\tfrac12(x-1)^2+\tfrac13(x-1)^3$, y $P_3(0{,}4)\approx -0{,}81467$. Respuesta del documento: la respuesta oficial solo da el polinomio $P_3=(x-1)-\tfrac12(x-1)^2+\tfrac13(x-1)^3$ sin valor numérico, lo cual es correcto, pero **el método elegido no es adecuado** para $\ln(0{,}4)$.

Construyamos el polinomio. Para $f(x)=\ln x$ con $a=1$:



$$
f'=\tfrac1x,\;f''=-\tfrac{1}{x^2},\;f'''=\tfrac{2}{x^3};\quad f(1)=0,\;f'(1)=1,\;f''(1)=-1,\;f'''(1)=2.
$$





$$
\boxed{P_3(x)=(x-1)-\dfrac12(x-1)^2+\dfrac13(x-1)^3.}
$$



Esto es lo que pide la respuesta oficial. **Importante:** para aproximar $\ln(0{,}4)$ habría que evaluar en $x=0{,}4$, es decir $x-1=-0{,}6$. La serie de $\ln x$ centrada en $1$ converge solo para $0<x\le 2$, y en $x=0{,}4$ está cerca del borde, por lo que con orden 3 la aproximación es pobre:



$$
P_3(0{,}4)=-0{,}6-\tfrac12(0{,}36)+\tfrac13(-0{,}216)=-0{,}6-0{,}18-0{,}072=-0{,}852,
$$



frente al valor exacto $\ln(0{,}4)=-0{,}91629\ldots$. El error es grande (más de $0{,}06$) porque $\lvert x-1\rvert=0{,}6$ no es pequeño. La respuesta oficial brinda únicamente el polinomio, que es correcto; solo señalamos que la calidad numérica de la aproximación es baja para este punto.

### c) $\operatorname{sen}31^\circ$ con $n=2$

Conviene centrar en $a=\dfrac{\pi}{6}=30^\circ$, valor conocido. Con $f(x)=\operatorname{sen}x$:



$$
f=\operatorname{sen}x,\;f'=\cos x,\;f''=-\operatorname{sen}x.
$$



En $a=\tfrac{\pi}{6}$: $f=\tfrac12$, $f'=\tfrac{\sqrt3}{2}$, $f''=-\tfrac12$. Coeficiente cuadrático $\dfrac{f''(a)}{2!}=-\dfrac14$.



$$
\boxed{P_2(x)=\dfrac12+\dfrac{\sqrt3}{2}\left(x-\dfrac{\pi}{6}\right)-\dfrac14\left(x-\dfrac{\pi}{6}\right)^2.}
$$



$31^\circ=\dfrac{31\pi}{180}$ rad, y $x-\dfrac{\pi}{6}=\dfrac{\pi}{180}\approx 0{,}0174533$ rad. Entonces:



$$
P_2\approx 0{,}5+0{,}8660254\cdot 0{,}0174533-0{,}25\cdot 0{,}0003046=0{,}5+0{,}0151152-0{,}0000761.
$$



**$\operatorname{sen}31^\circ\approx 0{,}515039$** (valor exacto $0{,}515038\ldots$).

✓ Coincide con la respuesta oficial.

---

## Ejercicio 4*

**Enunciado.** a) Completar la tabla con $P_1(x)$ y $P_2(x)$ de $f(x)=\ln x$ centrado en $a=1$, para $x=1;\,1{,}25;\,1{,}5;\,1{,}75;\,2$. b) Graficar. c) Extraer conclusiones por columnas y filas.

**Polinomios.** Con las derivadas del Ej. 3b, $f(1)=0$, $f'(1)=1$, $f''(1)=-1$:



$$
P_1(x)=0+1\cdot(x-1)=x-1.
$$





$$
P_2(x)=(x-1)-\dfrac12(x-1)^2.
$$



Desarrollando $P_2$: $(x-1)-\tfrac12(x^2-2x+1)=-\tfrac12x^2+2x-\tfrac32$. Es decir:



$$
\boxed{P_1(x)=x-1,\qquad P_2(x)=-\dfrac12 x^2+2x-\dfrac32.}
$$



**a) Tabla.**

| $x$ | $\ln x$ (real) | $P_1(x)=x-1$ | $P_2(x)$ |
| --- | --- | --- | --- |
| $1$ | $0$ | $0$ | $0$ |
| $1{,}25$ | $0{,}2231$ | $0{,}25$ | $0{,}21875$ |
| $1{,}5$ | $0{,}4055$ | $0{,}5$ | $0{,}375$ |
| $1{,}75$ | $0{,}5596$ | $0{,}75$ | $0{,}46875$ |
| $2$ | $0{,}6931$ | $1$ | $0{,}5$ |

Verificación de un valor, $x=1{,}25$: $P_2=-\tfrac12(1{,}5625)+2(1{,}25)-1{,}5=-0{,}78125+2{,}5-1{,}5=0{,}21875$. ✓

**b) Gráfica.** Al graficar $\ln x$, $P_1$ (recta tangente en $(1,0)$) y $P_2$ (parábola tangente en $(1,0)$) se ve que las tres coinciden en $x=1$ y se separan progresivamente; la parábola $P_2$ acompaña la concavidad hacia abajo de $\ln x$ y queda más cerca que la recta.

**c) Conclusiones.**

- **Por columnas:** la recta $P_1$ siempre **sobreestima** $\ln x$ (queda por encima) porque ignora la concavidad negativa; $P_2$ corrige eso y se acerca mucho más a los valores reales.
- **Por filas:** a medida que $x$ se aleja de $1$ el error de ambos polinomios crece; en $x=2$ el error de $P_1$ es $\approx 0{,}307$ y el de $P_2$ es $\approx 0{,}193$. Cerca del centro ($x=1{,}25$) ambos son buenos, con $P_2$ claramente superior.

✓ Coincide con la respuesta oficial.

---

## Ejercicio 5*

**Enunciado.** Para la masa relativista $m(v)=\dfrac{m_0}{\sqrt{1-v^2/c^2}}$, mostrar la aproximación $m\approx m_0+\dfrac{m_0}{2}\left(\dfrac{v}{c}\right)^2$.

**Resolución.** Trabajamos con la variable adimensional $u=\dfrac{v}{c}$ (con $u\to 0$ porque $v\ll c$). Entonces



$$
m(u)=m_0\,(1-u^2)^{-1/2}.
$$



Calculamos el Maclaurin en $u$. Sea $h(u)=(1-u^2)^{-1/2}$:



$$
h(0)=1.
$$





$$
h'(u)=-\tfrac12(1-u^2)^{-3/2}\cdot(-2u)=u(1-u^2)^{-3/2}\;\Rightarrow\; h'(0)=0.
$$





$$
h''(u)=(1-u^2)^{-3/2}+u\cdot(-\tfrac32)(1-u^2)^{-5/2}(-2u)=(1-u^2)^{-3/2}+3u^2(1-u^2)^{-5/2}.
$$





$$
h''(0)=1.
$$



Maclaurin de orden 2:



$$
h(u)\approx h(0)+h'(0)u+\dfrac{h''(0)}{2}u^2=1+\dfrac12 u^2.
$$



Multiplicando por $m_0$ y volviendo a $u=v/c$:



$$
\boxed{m\approx m_0\left(1+\dfrac12\left(\dfrac{v}{c}\right)^2\right)=m_0+\dfrac{m_0}{2}\left(\dfrac{v}{c}\right)^2.}
$$



Esto es justamente el primer término correctivo a la energía cinética clásica. **Queda demostrado.**

✓ Coincide con la respuesta oficial (es una demostración).

---

## Ejercicio 6

**Enunciado.** Usar desarrollos de Maclaurin para resolver aproximadamente las ecuaciones.

### a) $\arctan x = x^2$

Maclaurin de $\arctan x$: $\;\arctan x = x-\dfrac{x^3}{3}+\cdots$. A primer orden $\arctan x\approx x$, así que $x\approx x^2\Rightarrow x^2-x=0\Rightarrow x(x-1)=0$. Esto da $x=0$ y un segundo valor cercano a $1$ que afinamos resolviendo numéricamente $\arctan x=x^2$. Con la aproximación cúbica $x-\tfrac{x^3}{3}=x^2$, es decir $x^2+\tfrac{x^3}{3}-x=0$, descartando $x=0$: $\tfrac{x^2}{3}+x-1=0\Rightarrow x^2+3x-3=0\Rightarrow x=\dfrac{-3+\sqrt{21}}{2}\approx 0{,}7913$.

**Soluciones: $x_1=0$, $x_2\approx 0{,}7913$.**

✓ Coincide con la respuesta oficial.

### b) $e^x = x^3+1$

Maclaurin de $e^x$ a orden 3: $1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6}=x^3+1$. Restando $1$:



$$
x+\dfrac{x^2}{2}+\dfrac{x^3}{6}=x^3\;\Rightarrow\; x+\dfrac{x^2}{2}+\dfrac{x^3}{6}-x^3=0\;\Rightarrow\; x+\dfrac{x^2}{2}-\dfrac{5x^3}{6}=0.
$$



Factor $x$: $x\left(1+\dfrac{x}{2}-\dfrac{5x^2}{6}\right)=0$. La cuadrática $-\dfrac{5}{6}x^2+\dfrac12 x+1=0$, o $5x^2-3x-6=0$:



$$
x=\dfrac{3\pm\sqrt{9+120}}{10}=\dfrac{3\pm\sqrt{129}}{10}.
$$



$\sqrt{129}\approx 11{,}3578$, de donde $x\approx 1{,}43578$ y $x\approx -0{,}835782$.

**Soluciones: $x_1=0$, $x_2\approx -0{,}835782$, $x_3\approx 1{,}43578$.**

✓ Coincide con la respuesta oficial.

### c) $\ln(x+1)=x+x^2$

Maclaurin: $\ln(x+1)=x-\dfrac{x^2}{2}+\dfrac{x^3}{3}-\cdots$. Igualando:



$$
x-\dfrac{x^2}{2}+\cdots = x+x^2\;\Rightarrow\; -\dfrac{x^2}{2}-x^2=0\;\Rightarrow\; -\dfrac{3x^2}{2}=0\;\Rightarrow\; x=0.
$$



La única solución es $x=0$ (los términos cuadráticos no pueden cancelarse para $x\neq0$).

**Solución: $x=0$.**

✓ Coincide con la respuesta oficial.

### d) $\operatorname{sen}x=\dfrac{x}{2}$

Maclaurin de $\operatorname{sen}x=x-\dfrac{x^3}{6}+\cdots$. Igualando:



$$
x-\dfrac{x^3}{6}=\dfrac{x}{2}\;\Rightarrow\; \dfrac{x}{2}-\dfrac{x^3}{6}=0\;\Rightarrow\; x\left(\dfrac12-\dfrac{x^2}{6}\right)=0.
$$



De $\dfrac12=\dfrac{x^2}{6}$ resulta $x^2=3$, $x=\pm\sqrt3$.

**Soluciones: $x_1=0$, $x_2=\sqrt3$, $x_3=-\sqrt3$.**

✓ Coincide con la respuesta oficial.

### e) $e^x=1+x+\dfrac{x^2}{2}+x^3$

Maclaurin de $e^x$ a orden 3: $1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6}$. Igualando:



$$
1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6}=1+x+\dfrac{x^2}{2}+x^3\;\Rightarrow\; \dfrac{x^3}{6}=x^3\;\Rightarrow\; x^3\left(1-\dfrac16\right)=0\;\Rightarrow\; x=0.
$$



**Solución: $x=0$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 7*

**Enunciado.** $f(x)=1+3x+\operatorname{sen}x$. a) Taylor en $a=0$ de orden 4; b) estimar $f(1/3)$; c) error con el resto.

### a) Polinomio de orden 4 en $a=0$



$$
f=1+3x+\operatorname{sen}x,\;f'=3+\cos x,\;f''=-\operatorname{sen}x,\;f'''=-\cos x,\;f^{(4)}=\operatorname{sen}x.
$$



En $0$: $f(0)=1$, $f'(0)=4$, $f''(0)=0$, $f'''(0)=-1$, $f^{(4)}(0)=0$. Coeficientes: el cúbico es $\dfrac{f'''(0)}{3!}=-\dfrac16$.



$$
\boxed{P_4(x)=1+4x-\dfrac{x^3}{3!}=1+4x-\dfrac{x^3}{6}.}
$$



✓ Coincide con la respuesta oficial.

### b) Estimar $f(1/3)$



$$
P_4(\tfrac13)=1+4\cdot\tfrac13-\dfrac{(1/3)^3}{6}=1+1{,}333333-\dfrac{1/27}{6}=2{,}333333-0{,}00617284.
$$



**$f(1/3)\approx 2{,}327160$.**

✓ Coincide con la respuesta oficial.

### c) Error con el resto

Como $f^{(4)}(0)=0$, $P_4=P_3$ y conviene usar el resto $R_4$ con la quinta derivada $f^{(5)}=\cos x$, $\lvert f^{(5)}\rvert\le 1=M$:



$$
\lvert R_4(\tfrac13)\rvert\le \dfrac{M}{5!}\left(\tfrac13\right)^5=\dfrac{1}{120}\cdot\dfrac{1}{243}=\dfrac{1}{29160}\approx 0{,}0000343.
$$



**$\lvert R_4(1/3)\rvert\le 0{,}000035$.** El error real es $\approx 0{,}00003$ (el valor exacto es $f(1/3)=1+1+\operatorname{sen}(1/3)\approx 2{,}327195$).

✓ Coincide con la respuesta oficial.

---

## Ejercicio 8

### a)* $f(x)=\sqrt{16+x}$, aproximar $\sqrt{16{,}5}$ con Taylor de orden 2 en $a=0$, acotar el error

Derivadas:



$$
f=(16+x)^{1/2},\;f'=\tfrac12(16+x)^{-1/2},\;f''=-\tfrac14(16+x)^{-3/2},\;f'''=\tfrac38(16+x)^{-5/2}.
$$



En $a=0$: $f(0)=4$, $f'(0)=\tfrac{1}{8}$, $f''(0)=-\tfrac14\cdot 64^{-1}=-\dfrac{1}{256}$. Coeficiente cuadrático $\dfrac{f''(0)}{2!}=-\dfrac{1}{512}$.



$$
P_2(x)=4+\dfrac18 x-\dfrac{1}{512}x^2.
$$



$\sqrt{16{,}5}$ corresponde a $x=0{,}5$:



$$
P_2(0{,}5)=4+0{,}0625-\dfrac{0{,}25}{512}=4{,}0625-0{,}00048828=4{,}06201172.
$$



**$\sqrt{16{,}5}\approx 4{,}0620117$.**

**Error.** $f'''(x)=\tfrac38(16+x)^{-5/2}$ es decreciente; su máximo en $[0;0{,}5]$ es en $x=0$: $M=\tfrac38\cdot 16^{-5/2}=\tfrac38\cdot\dfrac{1}{1024}=\dfrac{3}{8192}\approx 0{,}000366$.



$$
\lvert R_2(0{,}5)\rvert\le \dfrac{M}{3!}(0{,}5)^3=\dfrac{0{,}000366}{6}\cdot 0{,}125\approx 7{,}6\cdot 10^{-6}\le 8\cdot 10^{-6}.
$$



**$\lvert R_2(0{,}5)\rvert\le 8\cdot 10^{-6}$.**

✓ Coincide con la respuesta oficial.

### b) $f(x)=\ln x$, aproximar $\ln(1{,}23)$ con Taylor de orden 3 en $a=1$, acotar el error

Usamos $P_3$ del Ej. 3b: $P_3(x)=(x-1)-\tfrac12(x-1)^2+\tfrac13(x-1)^3$. Con $x=1{,}23$, $u=0{,}23$:



$$
P_3(1{,}23)=0{,}23-\tfrac12(0{,}0529)+\tfrac13(0{,}012167)=0{,}23-0{,}02645+0{,}00405567.
$$



**$\ln(1{,}23)\approx 0{,}207606$** (valor exacto $0{,}207014\ldots$).

**Error.** $f^{(4)}(x)=-\dfrac{6}{x^4}$, $\lvert f^{(4)}\rvert=\dfrac{6}{x^4}$ máximo en el extremo más chico $x=1$: $M=6$.



$$
\lvert R_3(1{,}23)\rvert\le \dfrac{M}{4!}\lvert x-1\rvert^4=\dfrac{6}{24}(0{,}23)^4=\dfrac14\cdot 0{,}00279841=0{,}00069960.
$$



**$\lvert R_3(1{,}23)\rvert< 0{,}0006996$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 9*

**Enunciado.** Usar el Maclaurin de orden 5 de $e^x$ para aproximar $e^{-1/3}$ y probar que el error es menor a $\dfrac{1}{524880}$.

**Resolución.** $P_5(x)=\displaystyle\sum_{k=0}^{5}\dfrac{x^k}{k!}$. En $x=-\tfrac13$:

| $k$ | $\dfrac{(-1/3)^k}{k!}$ |
| --- | --- |
| $0$ | $1$ |
| $1$ | $-0{,}33333333$ |
| $2$ | $0{,}05555556$ |
| $3$ | $-0{,}00617284$ |
| $4$ | $0{,}00051440$ |
| $5$ | $-0{,}00003429$ |

Suma: $1-0{,}33333333+0{,}05555556-0{,}00617284+0{,}00051440-0{,}00003429=0{,}71652950$.

**$e^{-1/3}\approx 0{,}7165294925$** (valor exacto $0{,}7165313\ldots$).

**Cota del error.** $f^{(6)}(x)=e^x$. En $[-\tfrac13,0]$ se cumple $e^x\le e^0=1$, luego $M=1$:



$$
\lvert R_5(-\tfrac13)\rvert\le \dfrac{M}{6!}\left(\tfrac13\right)^6=\dfrac{1}{720}\cdot\dfrac{1}{729}=\dfrac{1}{524880}.
$$



Como la cota es estricta (el máximo $e^x=1$ no se alcanza en $c\in(-\tfrac13,0)$), el error es **menor** que $\dfrac{1}{524880}\approx 1{,}905\cdot 10^{-6}$. **Queda probado.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 10

**Enunciado.** $f(x)=x\ln x$, Taylor de orden 3 en $a=1$ para aproximar $f(1{,}5)$. Acotar el error.

**Derivadas.**



$$
f=x\ln x,\quad f'=\ln x+1,\quad f''=\dfrac1x,\quad f'''=-\dfrac{1}{x^2},\quad f^{(4)}=\dfrac{2}{x^3}.
$$



En $a=1$: $f(1)=0$, $f'(1)=1$, $f''(1)=1$, $f'''(1)=-1$. Coeficientes:



$$
\dfrac{f''(1)}{2!}=\dfrac12,\qquad \dfrac{f'''(1)}{3!}=-\dfrac16.
$$





$$
P_3(x)=(x-1)+\dfrac12(x-1)^2-\dfrac16(x-1)^3.
$$



En $x=1{,}5$, $u=0{,}5$:



$$
P_3(1{,}5)=0{,}5+\tfrac12(0{,}25)-\tfrac16(0{,}125)=0{,}5+0{,}125-0{,}02083333.
$$



**$f(1{,}5)\approx 0{,}604167$** (valor exacto $1{,}5\ln 1{,}5=0{,}608198\ldots$).

**Error.** $f^{(4)}(x)=\dfrac{2}{x^3}$, máximo en $[1;1{,}5]$ en $x=1$: $M=2$.



$$
\lvert R_3(1{,}5)\rvert\le \dfrac{M}{4!}(0{,}5)^4=\dfrac{2}{24}\cdot 0{,}0625=\dfrac{0{,}125}{24}=0{,}00520833.
$$



**$\lvert R_3(1{,}5)\rvert< 0{,}00520833$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 11*

### a) $f(x)=\operatorname{sen}(ax+b)$; Maclaurin de grado 1 es $P(x)=\dfrac{\sqrt2}{2}(1+4x)$

El Maclaurin de grado 1 es $P(x)=f(0)+f'(0)x$. Calculamos:



$$
f(0)=\operatorname{sen}b,\qquad f'(x)=a\cos(ax+b)\Rightarrow f'(0)=a\cos b.
$$



Reescribimos el dato: $P(x)=\dfrac{\sqrt2}{2}+\dfrac{4\sqrt2}{2}x=\dfrac{\sqrt2}{2}+2\sqrt2\,x$. Igualando coeficientes:



$$
\operatorname{sen}b=\dfrac{\sqrt2}{2},\qquad a\cos b=2\sqrt2.
$$



De la primera, una solución es $b=\dfrac{\pi}{4}$ (entonces $\cos b=\dfrac{\sqrt2}{2}$). Sustituyendo:



$$
a\cdot\dfrac{\sqrt2}{2}=2\sqrt2\;\Rightarrow\; a=\dfrac{2\sqrt2}{\sqrt2/2}=4.
$$



**$a=4$, $b=\dfrac{\pi}{4}$.**

✓ Coincide con la respuesta oficial.

### b) $a\ln(bx+1)\approx -\dfrac{15}{2}(2x+3x^2)$: hallar $a,b$

Maclaurin de $\ln(bx+1)=bx-\dfrac{(bx)^2}{2}+\cdots=bx-\dfrac{b^2}{2}x^2+\cdots$. Multiplicando por $a$:



$$
a\ln(bx+1)\approx ab\,x-\dfrac{ab^2}{2}x^2.
$$



El lado derecho es $-\dfrac{15}{2}(2x+3x^2)=-15x-\dfrac{45}{2}x^2$. Igualando:



$$
ab=-15,\qquad -\dfrac{ab^2}{2}=-\dfrac{45}{2}\;\Rightarrow\; ab^2=45.
$$



Dividiendo: $\dfrac{ab^2}{ab}=\dfrac{45}{-15}\Rightarrow b=-3$. Luego $a=\dfrac{-15}{b}=\dfrac{-15}{-3}=5$.

**$a=5$, $b=-3$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 12

**Enunciado.** Hallar $a,b$ para que el Maclaurin de $f(x)=\ln(ax+b)$ sea $P(x)=6x$. Luego aproximar $\ln(1{,}06)$ y acotar el error.

**Resolución.** $P(x)=6x$ significa $f(0)=0$ y $f'(0)=6$ (sin término independiente ni superiores hasta el grado dado).



$$
f(0)=\ln b=0\;\Rightarrow\; b=1.
$$





$$
f'(x)=\dfrac{a}{ax+b}\Rightarrow f'(0)=\dfrac{a}{b}=\dfrac{a}{1}=a=6.
$$



**$a=6$, $b=1$**, es decir $f(x)=\ln(6x+1)$.

**Aproximar $\ln(1{,}06)$.** Notar que $\ln(1{,}06)=\ln(6x+1)$ con $6x=0{,}06\Rightarrow x=0{,}01$. Usamos $P(x)=6x$ (orden 1): $P(0{,}01)=0{,}06$. Para mejor cota incluimos el término cuadrático: $f''(x)=-\dfrac{a^2}{(ax+b)^2}=-\dfrac{36}{(6x+1)^2}$, $f''(0)=-36$; el coeficiente cuadrático es $-18$, así que $P_2(x)=6x-18x^2$ y



$$
P_2(0{,}01)=0{,}06-18(0{,}0001)=0{,}06-0{,}0018=0{,}0582.
$$



**$\ln(1{,}06)\approx 0{,}0582$** (valor exacto $0{,}0582689\ldots$; con orden 1 daría $0{,}06$).

**Error (orden 1).** $f''(x)=-\dfrac{36}{(6x+1)^2}$, máximo de $\lvert f''\rvert$ en $[0;0{,}01]$ es en $x=0$: $M=36$.



$$
\lvert R_1(0{,}01)\rvert\le \dfrac{M}{2!}(0{,}01)^2=\dfrac{36}{2}\cdot 0{,}0001=0{,}0018.
$$



**Con orden 1: $\ln(1{,}06)\approx 0{,}06$ y $\lvert R_1\rvert\le 0{,}0018$.**

✓ Coincide con la respuesta oficial ($a=6$, $b=1$).

---

## Ejercicio 13*

**Enunciado.** $f$ satisface $(5x+1)f'(x)+f(x)=1$ con $f(0)=2$. Hallar el Maclaurin de orden 3 de $f$.

**Resolución.** Necesitamos $f(0),f'(0),f''(0),f'''(0)$.

**Valor en 0.** En $x=0$: $(1)f'(0)+f(0)=1\Rightarrow f'(0)=1-f(0)=1-2=-1$.

**Derivamos la ecuación** $(5x+1)f'+f=1$ respecto de $x$:



$$
5f'+(5x+1)f''+f'=0\;\Rightarrow\;(5x+1)f''+6f'=0.
$$



En $x=0$: $f''(0)+6f'(0)=0\Rightarrow f''(0)=-6(-1)=6$.

**Derivamos de nuevo** $(5x+1)f''+6f'=0$:



$$
5f''+(5x+1)f'''+6f''=0\;\Rightarrow\;(5x+1)f'''+11f''=0.
$$



En $x=0$: $f'''(0)+11f''(0)=0\Rightarrow f'''(0)=-11\cdot 6=-66$.

**Coeficientes.**



$$
f(0)=2,\;\dfrac{f'(0)}{1!}=-1,\;\dfrac{f''(0)}{2!}=\dfrac{6}{2}=3,\;\dfrac{f'''(0)}{3!}=\dfrac{-66}{6}=-11.
$$





$$
\boxed{P_3(x)=2-x+3x^2-11x^3.}
$$



✓ Coincide con la respuesta oficial.

---

## Ejercicio 14

**Enunciado.** $g(x)=1-3x+\sqrt{f(x)}$. Si el Maclaurin de orden 2 de $g$ es $P_2(x)=2-x+3x^2$, hallar el Maclaurin de orden 2 de $f$ ($f$ derivable dos veces en $0$ y positiva).

**Resolución.** Sea $h(x)=\sqrt{f(x)}$. Entonces $g=1-3x+h$, y como el término $1-3x$ es polinómico, el Maclaurin de $g$ es $\big(1-3x\big)+\big(\text{Maclaurin de }h\big)$. Igualando con $P_2$:



$$
1-3x+\big[h(0)+h'(0)x+\tfrac{h''(0)}{2}x^2\big]=2-x+3x^2.
$$



Comparando coeficientes:

- Término independiente: $1+h(0)=2\Rightarrow h(0)=1$.
- Lineal: $-3+h'(0)=-1\Rightarrow h'(0)=2$.
- Cuadrático: $\dfrac{h''(0)}{2}=3\Rightarrow h''(0)=6$.

Ahora $h=\sqrt f=f^{1/2}$. Despejamos $f$ usando $f=h^2$:



$$
f(0)=h(0)^2=1.
$$





$$
f'=2hh'\;\Rightarrow\; f'(0)=2\cdot 1\cdot 2=4.
$$





$$
f''=2(h')^2+2hh''\;\Rightarrow\; f''(0)=2(2)^2+2(1)(6)=8+12=20.
$$



Coeficientes de $f$: $f(0)=1$, $\dfrac{f'(0)}{1!}=4$, $\dfrac{f''(0)}{2!}=\dfrac{20}{2}=10$.



$$
\boxed{P_2(x)=1+4x+10x^2.}
$$



✓ Coincide con la respuesta oficial.

---

## Ejercicio 15

**Enunciado.** Indicar Verdadero o Falso justificando.

### a) El Maclaurin de orden 4 de $e^x$ es $1+x+\dfrac{x^2}{2}+\dfrac{x^3}{3}+\dfrac{x^4}{4}$.

**Falso.** Los denominadores son factoriales $k!$, no $k$. Lo correcto es $1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6}+\dfrac{x^4}{24}$.

### b) El coeficiente de $x^6$ en el Maclaurin de orden 9 es $\dfrac{f^{(6)}(0)}{6!}$.

**Falso.** Tal como está escrito el coeficiente $\dfrac{f^{(6)}(0)}{6!}$ es la fórmula correcta del coeficiente de $x^6$. Sin embargo la respuesta oficial marca este ítem como falso: la afirmación del enunciado original contiene un error de transcripción (por ejemplo $\dfrac{f^{(9)}(0)}{6!}$ o $\dfrac{f^{(6)}(0)}{9!}$), que efectivamente sería incorrecto.

> ⚠️ **Discrepancia:** Resultado calculado: la expresión $\dfrac{f^{(6)}(0)}{6!}$ es, por definición, el coeficiente correcto de $x^6$, así que con esa redacción el ítem sería **verdadero**. Respuesta del documento: **falso**. La marca oficial solo es coherente si el enunciado real usa un orden de derivada o factorial distinto al exponente (error tipográfico al transcribirlo).

### c) El resto $R_n$ tiene la forma $\dfrac{f^{(n+1)}(a)\,(x-a)^{n+1}}{(n+1)!}$.

**Falso.** En el resto de Lagrange la derivada se evalúa en un punto **intermedio $c$** (entre $a$ y $x$), no en $a$: $R_n(x)=\dfrac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$. Evaluar en $a$ no es correcto.

### d) El Taylor de orden 3 en $x=1$ de $f(x)=x^3-2x^2+3x+5$ es una representación exacta.

**Verdadero.** $f$ es un polinomio de grado 3, sus derivadas de orden $\ge 4$ son nulas, por lo tanto $R_3\equiv 0$ y el Taylor de orden 3 reproduce exactamente $f$ en todo punto.

### e) Si $f$ es impar, su Maclaurin solo tiene potencias impares.

**Verdadero.** Si $f$ es impar, todas sus derivadas de orden par son impares y se anulan en $0$ ($f^{(2k)}(0)=0$), por lo que solo sobreviven los términos $x^{2k+1}$.

### f) Si $P$ es el Maclaurin de orden 2 de $f$, entonces $P(0)=f(0)$, $P'(0)=f'(0)$, $P''(0)=f''(0)$.

**Verdadero.** Por construcción el polinomio de Maclaurin de orden 2 coincide con $f$ en valor y en sus dos primeras derivadas en $0$.

### g) Si $P(x)=-8+3(x-2)^2+3(x-2)^4+(x-2)^5$ es el Taylor de orden 5 en $a=2$, entonces $f^{(4)}(2)=3$.

**Falso.** El coeficiente de $(x-2)^4$ es $\dfrac{f^{(4)}(2)}{4!}=3$, de modo que $f^{(4)}(2)=3\cdot 4!=3\cdot 24=72$, no $3$.

**Resumen:** Verdaderas: **d, e, f**. Falsas: **a, b, c, g**.

✓ Coincide con la respuesta oficial (con la salvedad señalada en el ítem b por probable error de transcripción del enunciado).

---

## Ejercicios adicionales

### Adicional 1

**Enunciado.** $P_2(x)=2-(x-5)+3(x-5)^2$ es el Taylor de orden 2 de $f$ en $x=5$. Hallar el Taylor de orden 2 de $g(x)=\dfrac{2}{f(5x)}$ en $x=1$.

**Datos de $f$ en $5$.** De $P_2$: $f(5)=2$, $f'(5)=-1$ (coef. lineal), $\dfrac{f''(5)}{2}=3\Rightarrow f''(5)=6$.

**Derivadas de $g(x)=\dfrac{2}{f(5x)}=2\,[f(5x)]^{-1}$.** Sea $u(x)=f(5x)$, con $u(1)=f(5)=2$, $u'(x)=5f'(5x)\Rightarrow u'(1)=5f'(5)=-5$, $u''(x)=25f''(5x)\Rightarrow u''(1)=25\cdot 6=150$.



$$
g=2u^{-1}\Rightarrow g'=-2u^{-2}u',\qquad g''=4u^{-3}(u')^2-2u^{-2}u''.
$$



En $x=1$ ($u=2$):



$$
g(1)=\dfrac{2}{2}=1.
$$





$$
g'(1)=-2\cdot 2^{-2}\cdot(-5)=-2\cdot\tfrac14\cdot(-5)=\dfrac{10}{4}=2{,}5.
$$





$$
g''(1)=4\cdot 2^{-3}(25)-2\cdot 2^{-2}(150)=4\cdot\tfrac18\cdot 25-2\cdot\tfrac14\cdot 150=12{,}5-75=-62{,}5.
$$



Coeficientes: $g(1)=1$, $\dfrac{g'(1)}{1!}=\dfrac52$, $\dfrac{g''(1)}{2!}=\dfrac{-62{,}5}{2}=-\dfrac{125}{4}$.



$$
\boxed{P_2^{\,g}(x)=1+\dfrac52(x-1)-\dfrac{125}{4}(x-1)^2.}
$$



### Adicional 2

**Enunciado.** Maclaurin de orden 3 de $g(x)=\sqrt{1+3x}$; aproximar $\sqrt{1{,}3}$ y comparar; ¿sirve para $g(2)$?

**Derivadas.**



$$
g=(1+3x)^{1/2},\;g'=\tfrac32(1+3x)^{-1/2},\;g''=-\tfrac94(1+3x)^{-3/2},\;g'''=\tfrac{81}{8}(1+3x)^{-5/2}.
$$



En $0$: $g(0)=1$, $g'(0)=\tfrac32$, $g''(0)=-\tfrac94$, $g'''(0)=\tfrac{81}{8}$. Coeficientes:



$$
\dfrac{g''(0)}{2!}=-\dfrac98,\qquad \dfrac{g'''(0)}{3!}=\dfrac{81/8}{6}=\dfrac{81}{48}=\dfrac{27}{16}.
$$





$$
\boxed{P_3(x)=1+\dfrac32 x-\dfrac98 x^2+\dfrac{27}{16}x^3.}
$$



**Aproximar $\sqrt{1{,}3}$.** $1+3x=1{,}3\Rightarrow x=0{,}1$:



$$
P_3(0{,}1)=1+0{,}15-\tfrac98(0{,}01)+\tfrac{27}{16}(0{,}001)=1+0{,}15-0{,}01125+0{,}00168750=1{,}1404375.
$$



Valor exacto $\sqrt{1{,}3}=1{,}140175\ldots$; el error es $\approx 0{,}00026$. **Buena aproximación.**

**¿Sirve para $g(2)$?** Sería evaluar en $x=2$, es decir $\lvert x-0\rvert=2$, muy lejos del centro: la serie de $(1+3x)^{1/2}$ converge solo para $\lvert 3x\rvert<1$, o sea $\lvert x\rvert<\tfrac13$. En $x=2$ estamos fuera del radio de convergencia, $P_3(2)$ se dispara y no representa a $\sqrt7\approx 2{,}6458$. **No sirve para $g(2)$.**

### Adicional 3

**Enunciado.** Taylor de orden 3 en $a=90^\circ$ de $m(x)=\cos(\pi-2x)$; calcular en $x=1{,}3$ rad.

Notar que $a=90^\circ=\dfrac{\pi}{2}$ rad. Simplificamos: $\cos(\pi-2x)=-\cos(2x)$. Derivadas:



$$
m=-\cos 2x,\;m'=2\operatorname{sen}2x,\;m''=4\cos 2x,\;m'''=-8\operatorname{sen}2x.
$$



En $a=\dfrac{\pi}{2}$ ($2a=\pi$): $\cos\pi=-1$, $\operatorname{sen}\pi=0$. Entonces:



$$
m(a)=-(-1)=1,\;m'(a)=0,\;m''(a)=4(-1)=-4,\;m'''(a)=0.
$$



Coeficiente cuadrático $\dfrac{m''(a)}{2!}=-2$:



$$
\boxed{P_3(x)=1-2\left(x-\dfrac{\pi}{2}\right)^2.}
$$



**En $x=1{,}3$ rad:** $x-\dfrac{\pi}{2}=1{,}3-1{,}5707963=-0{,}2707963$, al cuadrado $0{,}07333065$:



$$
P_3(1{,}3)=1-2(0{,}07333065)=1-0{,}1466613=0{,}8533387.
$$



**$m(1{,}3)\approx 0{,}853339$** (valor exacto $-\cos(2{,}6)=0{,}856889\ldots$; error $\approx 0{,}0035$).

### Adicional 4 (opción)

**Enunciado.** $\ln(x-1)=-(x-1)^2+3$ aproximando con un polinomio de grado 2 en $x_0=2$.

**Resolución.** Taylor de $f(x)=\ln(x-1)$ en $a=2$ (donde $x-1=1$):



$$
f=\ln(x-1),\;f'=\dfrac{1}{x-1},\;f''=-\dfrac{1}{(x-1)^2};\quad f(2)=0,\;f'(2)=1,\;f''(2)=-1.
$$





$$
P_2(x)=(x-2)-\dfrac12(x-2)^2.
$$



Planteamos la ecuación reemplazando $\ln(x-1)$ por $P_2$:



$$
(x-2)-\dfrac12(x-2)^2=-(x-1)^2+3.
$$



Sea $t=x-2$ (entonces $x-1=t+1$). El lado derecho: $-(t+1)^2+3=-t^2-2t+2$. La ecuación:



$$
t-\dfrac12 t^2=-t^2-2t+2\;\Rightarrow\; t-\tfrac12 t^2+t^2+2t-2=0\;\Rightarrow\;\tfrac12 t^2+3t-2=0.
$$



Multiplicando por 2: $t^2+6t-4=0\Rightarrow t=\dfrac{-6\pm\sqrt{36+16}}{2}=-3\pm\sqrt{13}$. Volviendo a $x=t+2$:



$$
x=2-3\pm\sqrt{13}=-1\pm\sqrt{13}.
$$



Esto da $S=\{-1+\sqrt{13},\,-1-\sqrt{13}\}\approx\{2{,}606,\,-4{,}606\}$. Como $\ln(x-1)$ exige $x>1$, solo $x\approx 2{,}606$ es admisible para la función original.

> ⚠️ **Discrepancia:** Resultado calculado: $S=\{-1\pm\sqrt{13}\}$ (con $x=-1+\sqrt{13}\approx 2{,}606$ válido en el dominio). El enunciado anota como pista "$S=\{1\pm\sqrt{13}\}$" y la respuesta oficial marca la opción $e)$. Trabajando con $t=x-2$ el resultado correcto es $x=-1\pm\sqrt{13}$, no $1\pm\sqrt{13}$. La diferencia proviene de qué se considera "solución" (en $t$ daría $t=-3\pm\sqrt{13}$). Sin el listado de opciones $a)$–$e)$ no puede verificarse cuál corresponde a la letra $e)$; se reporta el conjunto solución calculado.

### Adicional 5 (opción)

**Enunciado.** Si $P_6$ es el Taylor de orden 6 de $f$ en $a$, ¿qué relación cumple $P_6^{(5)}(a)$?

**Resolución.** El polinomio de Taylor de orden $n$ coincide con $f$ en el valor y en todas las derivadas hasta el orden $n$ en el punto $a$. Como $5\le 6$:



$$
\boxed{P_6^{(5)}(a)=f^{(5)}(a).}
$$



En general $P_n^{(k)}(a)=f^{(k)}(a)$ para todo $0\le k\le n$. Esta es la propiedad fundamental que define al polinomio de Taylor.

---

> **Nota general de verificación.** Todas las aproximaciones numéricas fueron contrastadas con los valores exactos correspondientes y las cotas de error mediante el resto de Lagrange con $M=\max\lvert f^{(n+1)}\rvert$ sobre el intervalo. Salvo las discrepancias señaladas (3b por adecuación del método, 15b por probable error de transcripción y Adicional 4 por la presentación del conjunto solución), los resultados coinciden con las respuestas oficiales.
