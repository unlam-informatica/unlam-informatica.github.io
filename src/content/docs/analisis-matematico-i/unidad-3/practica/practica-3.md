---
title: Práctica 3 — Derivada
slug: analisis-matematico-i/unidad-3/practica/practica-3
sidebar:
  order: 2
---



Resolución completa y paso a paso de la Práctica 3 de Análisis Matemático I (UNLaM). Cada ejercicio reproduce el enunciado, lo resuelve con notación LaTeX y compara el resultado con la respuesta oficial. Se usan: definición de derivada por límite del cociente incremental, reglas de derivación (suma, producto, cociente, constante), regla de la cadena, derivada de funciones elementales, derivada de la inversa $(f^{-1})'(y)=\dfrac{1}{f'(f^{-1}(y))}$, derivación implícita y derivación logarítmica. Para la recta tangente usamos $y-f(a)=f'(a)(x-a)$ y para la normal la pendiente $-\dfrac{1}{f'(a)}$.

## Tabla de contenidos


1. TOC


---

## Ejercicio 1 — Recta tangente a $f(x)=x^2$ en $(1,1)$

**Enunciado.** Hallar la recta tangente a $f(x)=x^2$ en $(1,1)$ usando pendientes de rectas secantes.

### a) Pendientes de secantes

La pendiente de la secante entre $(1,1)$ y $(x,x^2)$ es $m_s=\dfrac{x^2-1}{x-1}$.

| $x$ | $m_s=\dfrac{x^2-1}{x-1}$ |
|------|------|
| $2$ | $3$ |
| $1{,}5$ | $2{,}5$ |
| $1{,}1$ | $2{,}1$ |
| $1{,}01$ | $2{,}01$ |
| $1{,}001$ | $2{,}001$ |
| $0$ | $1$ |
| $0{,}5$ | $1{,}5$ |
| $0{,}9$ | $1{,}9$ |
| $0{,}99$ | $1{,}99$ |
| $0{,}999$ | $1{,}999$ |

### b) Pendiente genérica



$$
m_s=\dfrac{f(x)-f(1)}{x-1}=\dfrac{x^2-1}{x-1}=\dfrac{(x-1)(x+1)}{x-1}=x+1,\qquad x\neq1.
$$



**$m_s=x+1$ (para $x\neq1$).**

### c) Límite cuando $x\to1$



$$
m=\lim_{x\to1}(x+1)=2.
$$



**La pendiente de la tangente es $m=2$.**

### d) Corroboración

Por la regla de la potencia, $f'(x)=2x$, luego $f'(1)=2$, lo que confirma el límite.

### e) Ecuación de la tangente



$$
y-f(1)=f'(1)(x-1)\;\Rightarrow\; y-1=2(x-1)\;\Rightarrow\; \boxed{y=2x-1.}
$$



✓ Coincide con la respuesta oficial.

---

## Ejercicio 2 — Caída libre $s(t)=5t^2$

**Enunciado.** Para $s(t)=5t^2$ hallar velocidades medias y la velocidad instantánea en $t=2$.

### a) Velocidades medias

La velocidad media en $[t_1,t_2]$ es $\bar v=\dfrac{s(t_2)-s(t_1)}{t_2-t_1}$. Con $s(2)=20$:

| Intervalo | $\bar v$ (m/s) |
|------|------|
| $[2;\,2{,}5]$ | $22{,}5$ |
| $[2;\,2{,}1]$ | $20{,}5$ |
| $[2;\,2{,}05]$ | $20{,}25$ |
| $[2;\,2{,}001]$ | $20{,}005$ |
| $[1{,}5;\,2]$ | $17{,}5$ |
| $[1{,}9;\,2]$ | $19{,}5$ |
| $[1{,}95;\,2]$ | $19{,}75$ |
| $[1{,}999;\,2]$ | $19{,}995$ |

Por ejemplo $[2;\,2{,}5]$: $\dfrac{5(2{,}5)^2-20}{0{,}5}=\dfrac{31{,}25-20}{0{,}5}=22{,}5$.

### b) Velocidad instantánea en $t=2$



$$
v(2)=\lim_{h\to0}\dfrac{s(2+h)-s(2)}{h}=\lim_{h\to0}\dfrac{5(2+h)^2-20}{h}=\lim_{h\to0}\dfrac{20h+5h^2}{h}=\lim_{h\to0}(20+5h)=20.
$$



**$v(2)=20$ m/s.**

### c) Comparación

Las velocidades medias se acercan a $20$ m/s por ambos lados, confirmando la velocidad instantánea.

✓ Coincide con la respuesta oficial.

---

## Ejercicio 3 — Función derivada por definición, dominios

**Enunciado.** Hallar $f'$ por definición y los dominios de $f$ y $f'$.

Usamos $f'(x)=\lim_{h\to0}\dfrac{f(x+h)-f(x)}{h}$.

### a) $f(x)=x^2+2x$



$$
f'(x)=\lim_{h\to0}\dfrac{(x+h)^2+2(x+h)-x^2-2x}{h}=\lim_{h\to0}\dfrac{2xh+h^2+2h}{h}=\lim_{h\to0}(2x+h+2)=2x+2.
$$



**$f'(x)=2x+2$, $\;D_f=D_{f'}=\mathbb{R}$.**

✓ Coincide con la respuesta oficial.

### b) $f(x)=\dfrac{1}{x}$



$$
f'(x)=\lim_{h\to0}\dfrac{\tfrac{1}{x+h}-\tfrac1x}{h}=\lim_{h\to0}\dfrac{x-(x+h)}{h\,x(x+h)}=\lim_{h\to0}\dfrac{-1}{x(x+h)}=-\dfrac{1}{x^2}.
$$



**$f'(x)=-\dfrac{1}{x^2}$, $\;D_f=D_{f'}=\mathbb{R}-\{0\}$.**

✓ Coincide con la respuesta oficial.

### c)* $f(x)=\sqrt{x}$



$$
f'(x)=\lim_{h\to0}\dfrac{\sqrt{x+h}-\sqrt{x}}{h}=\lim_{h\to0}\dfrac{(x+h)-x}{h(\sqrt{x+h}+\sqrt{x})}=\lim_{h\to0}\dfrac{1}{\sqrt{x+h}+\sqrt{x}}=\dfrac{1}{2\sqrt{x}}.
$$



Multiplicamos por el conjugado. **$f'(x)=\dfrac{1}{2\sqrt{x}}$, $\;D_f=[0,\infty)$, $\;D_{f'}=(0,\infty)$** (en $0$ la tangente es vertical).

✓ Coincide con la respuesta oficial.

### d) $f(x)=\dfrac{1}{\sqrt{x}}$



$$
f'(x)=\lim_{h\to0}\dfrac{\tfrac{1}{\sqrt{x+h}}-\tfrac{1}{\sqrt x}}{h}=\lim_{h\to0}\dfrac{\sqrt x-\sqrt{x+h}}{h\sqrt{x}\sqrt{x+h}}.
$$



Racionalizando el numerador:



$$
=\lim_{h\to0}\dfrac{x-(x+h)}{h\sqrt{x}\sqrt{x+h}(\sqrt x+\sqrt{x+h})}=\lim_{h\to0}\dfrac{-1}{\sqrt{x}\sqrt{x+h}(\sqrt x+\sqrt{x+h})}=\dfrac{-1}{\sqrt x\cdot\sqrt x\cdot 2\sqrt x}=-\dfrac{1}{2\sqrt{x^3}}.
$$



**$f'(x)=-\dfrac{1}{2\sqrt{x^3}}$, $\;D_f=D_{f'}=(0,\infty)$.**

✓ Coincide con la respuesta oficial.

### e)* $f(x)=\operatorname{sen}x$



$$
f'(x)=\lim_{h\to0}\dfrac{\operatorname{sen}(x+h)-\operatorname{sen}x}{h}=\lim_{h\to0}\dfrac{\operatorname{sen}x\cos h+\cos x\operatorname{sen}h-\operatorname{sen}x}{h}.
$$





$$
=\operatorname{sen}x\underbrace{\lim_{h\to0}\dfrac{\cos h-1}{h}}_{0}+\cos x\underbrace{\lim_{h\to0}\dfrac{\operatorname{sen}h}{h}}_{1}=\cos x.
$$



**$f'(x)=\cos x$, $\;D_f=D_{f'}=\mathbb{R}$.**

✓ Coincide con la respuesta oficial.

### f)* $f(x)=\ln x$



$$
f'(x)=\lim_{h\to0}\dfrac{\ln(x+h)-\ln x}{h}=\lim_{h\to0}\dfrac1h\ln\!\left(1+\dfrac hx\right)=\lim_{h\to0}\dfrac1x\ln\!\left(1+\dfrac hx\right)^{x/h}=\dfrac1x\ln e=\dfrac1x.
$$



**$f'(x)=\dfrac1x$, $\;D_f=D_{f'}=(0,\infty)$.**

✓ Coincide con la respuesta oficial.

### g)* $f(x)=e^x$



$$
f'(x)=\lim_{h\to0}\dfrac{e^{x+h}-e^x}{h}=e^x\lim_{h\to0}\dfrac{e^h-1}{h}=e^x\cdot1=e^x.
$$



**$f'(x)=e^x$, $\;D_f=D_{f'}=\mathbb{R}$.**

✓ Coincide con la respuesta oficial.

### h) $f(x)=c$



$$
f'(x)=\lim_{h\to0}\dfrac{c-c}{h}=0.
$$

 **$f'(x)=0$.** ✓ Coincide con la respuesta oficial.

### i) $f(x)=kx$



$$
f'(x)=\lim_{h\to0}\dfrac{k(x+h)-kx}{h}=\lim_{h\to0}\dfrac{kh}{h}=k.
$$

 **$f'(x)=k$.** ✓ Coincide con la respuesta oficial.

---

## Ejercicio 4 — Recta tangente

**Enunciado.** Hallar la recta tangente a cada $f$ en $a$.

### a)* $f(x)=5-3x$ en $a=3$

$f'(x)=-3$, $f(3)=5-9=-4$. Por ser recta, la tangente coincide con la propia función:



$$
y-(-4)=-3(x-3)\;\Rightarrow\;\boxed{y=5-3x.}
$$



✓ Coincide con la respuesta oficial.

### b) $f(x)=x^3$ en $a=1$

$f'(x)=3x^2$, $f'(1)=3$, $f(1)=1$.



$$
y-1=3(x-1)\;\Rightarrow\;\boxed{y=3x-2.}
$$



✓ Coincide con la respuesta oficial.

### c) $f(x)=2\sqrt{x}$ en $a=9$

$f'(x)=\dfrac{2}{2\sqrt x}=\dfrac{1}{\sqrt x}$, $f'(9)=\dfrac13$, $f(9)=6$.



$$
y-6=\dfrac13(x-9)\;\Rightarrow\;\boxed{y=\tfrac13x+3.}
$$



✓ Coincide con la respuesta oficial.

---

## Ejercicio 5 — Continuidad y derivabilidad; graficar $f$ y $f'$

**Enunciado.** Analizar continuidad y derivabilidad y graficar $f$ y $f'$.

**Método gráfico (GeoGebra).** Se carga $f$ como función definida a trozos (`Si(...)` o `If(...)`) y se grafica `f'(x)` con el comando `Derivada(f)`. Visualmente: $f$ continua $\Leftrightarrow$ trazo sin saltos; derivable $\Leftrightarrow$ trazo suave sin picos ni tangentes verticales. A continuación el análisis analítico.

### a) Función a trozos



$$
f(x)=\begin{cases}x+3 & x<-1\\ x^2 & -1\le x\le2\\ x+2 & x>2\end{cases}
$$



**Continuidad.** En $x=-1$: $\lim_{x\to-1^-}f=2$ y $\lim_{x\to-1^+}f=1$: salto finito $\Rightarrow$ discontinuidad esencial (de salto). En $x=2$: $\lim_{x\to2^-}f=4=\lim_{x\to2^+}f=4=f(2)$: continua.

**Derivabilidad.** En $x=-1$ no es derivable (ni siquiera continua). En $x=2$: $f'_-(2)=2x\big|_2=4$ y $f'_+(2)=1$, distintas $\Rightarrow$ no derivable (pico). La derivada:



$$
f'(x)=\begin{cases}1 & x<-1\\ 2x & -1<x<2\\ 1 & x>2\end{cases}
$$



✓ Coincide con la respuesta oficial.

### b) $g(x)=\lvert x-3\rvert$

$g$ es continua en $\mathbb{R}$. Para $x>3$, $g=x-3\Rightarrow g'=1$; para $x<3$, $g=3-x\Rightarrow g'=-1$. En $x=3$: $g'_-=-1\neq g'_+=1\Rightarrow$ no derivable.



$$
g'(x)=\begin{cases}-1 & x<3\\ 1 & x>3\end{cases}\qquad\text{derivable en }\mathbb{R}-\{3\}.
$$



✓ Coincide con la respuesta oficial.

### c) $n(x)=x^{2/3}$

Continua en $\mathbb{R}$. $n'(x)=\dfrac23x^{-1/3}=\dfrac{2}{3\sqrt[3]{x}}$. En $x=0$, $\lim_{x\to0}n'(x)=\pm\infty\Rightarrow$ tangente vertical, no derivable.

**$n'(x)=\dfrac23x^{-1/3}$, derivable en $\mathbb{R}-\{0\}$.**

✓ Coincide con la respuesta oficial.

### d) $f(x)=x\lvert x\rvert$

$f(x)=x^2$ si $x\ge0$ y $f(x)=-x^2$ si $x<0$. Continua en $\mathbb{R}$. Derivadas laterales en $0$: $f'_+(0)=2x\big|_0=0$ y $f'_-(0)=-2x\big|_0=0$, iguales $\Rightarrow$ derivable en $0$.



$$
f'(x)=\begin{cases}-2x & x<0\\ 2x & x\ge0\end{cases}=2\lvert x\rvert,\qquad\text{derivable en }\mathbb{R}.
$$



✓ Coincide con la respuesta oficial.

### e) $h(x)=x+2\lvert1-2x\rvert$

$\lvert1-2x\rvert=1-2x$ si $x<\tfrac12$ y $=2x-1$ si $x>\tfrac12$. Entonces:



$$
h(x)=\begin{cases}x+2(1-2x)=-3x+2 & x<\tfrac12\\ x+2(2x-1)=5x-2 & x\ge\tfrac12\end{cases}
$$



Continua en $\mathbb{R}$ (en $\tfrac12$ ambas dan $\tfrac12$). $h'_-(\tfrac12)=-3\neq h'_+(\tfrac12)=5\Rightarrow$ no derivable en $\tfrac12$.



$$
h'(x)=\begin{cases}-3 & x<\tfrac12\\ 5 & x>\tfrac12\end{cases}\qquad\text{derivable en }\mathbb{R}-\{\tfrac12\}.
$$



✓ Coincide con la respuesta oficial.

---

## Ejercicio 6 — Derivar (reglas)

**Enunciado.** Derivar aplicando las reglas básicas, producto y cociente.

### a) $f(x)=x^5-2x^4+\sqrt3$



$$
f'(x)=5x^4-8x^3.
$$

 ✓ Coincide con la respuesta oficial.

### b) $f(x)=\sqrt{x}+\tfrac32\sqrt[3]{x^2}-\sqrt[4]{x^3}+\dfrac{0{,}34}{x^5}$

Reescribimos con potencias: $x^{1/2}+\tfrac32x^{2/3}-x^{3/4}+0{,}34\,x^{-5}$.



$$
f'(x)=\tfrac12x^{-1/2}+\tfrac32\cdot\tfrac23x^{-1/3}-\tfrac34x^{-1/4}-5\cdot0{,}34\,x^{-6}=\dfrac{1}{2\sqrt x}+\dfrac{1}{\sqrt[3]{x}}-\dfrac{3}{4\sqrt[4]{x}}-\dfrac{1{,}7}{x^6}.
$$



✓ Coincide con la respuesta oficial.

### c) $h(z)=\dfrac{z^3-z^2+1}{5}$



$$
h'(z)=\dfrac{3z^2-2z}{5}.
$$

 ✓ Coincide con la respuesta oficial.

### d) $g(x)=\dfrac{x}{m}-\dfrac{m}{b}+\dfrac{x^2}{n^2}$ (constantes $m,b,n$)



$$
g'(x)=\dfrac1m+\dfrac{2x}{n^2}.
$$

 ✓ Coincide con la respuesta oficial.

### e) $f(x)=e^x-2\ln x+\sqrt{5x^3}$

$\sqrt{5x^3}=\sqrt5\,x^{3/2}$, derivada $\sqrt5\cdot\tfrac32x^{1/2}=\dfrac{3\sqrt5}{2}\sqrt{x}$. Entonces:



$$
f'(x)=e^x-\dfrac2x+\dfrac{3\sqrt5}{2}\sqrt{x}.
$$



> ⚠️ **Discrepancia:** Resultado calculado: $f'(x)=e^x-\dfrac{2}{x}+\dfrac{3\sqrt5}{2}\sqrt{x}$. Respuesta del documento: $e^x-\dfrac2x+3\sqrt5\,x^2$.
>
> El término $3\sqrt5\,x^2$ de la respuesta oficial es incorrecto: surge de derivar mal $\sqrt5\,x^{3/2}$. La derivada correcta es $\sqrt5\cdot\tfrac32x^{1/2}=\dfrac{3\sqrt5}{2}\sqrt{x}$, no $3\sqrt5\,x^2$. Verificado con cálculo simbólico: $\dfrac{d}{dx}\sqrt{5x^3}=\dfrac{3\sqrt5\sqrt{x}}{2}$.

### f) $f(t)=\dfrac{\operatorname{sen}t}{3}-4\cos t$



$$
f'(t)=\dfrac{\cos t}{3}+4\operatorname{sen}t.
$$

 ✓ Coincide con la respuesta oficial.

### g) $f(t)=\operatorname{sen}t\cos t$

Regla del producto: $f'(t)=\cos t\cos t+\operatorname{sen}t(-\operatorname{sen}t)=\cos^2 t-\operatorname{sen}^2 t$. ✓ Coincide con la respuesta oficial.

### h) $f(x)=\left(-x^2+\tfrac{x}{4}\right)e^x$



$$
f'(x)=\left(-2x+\tfrac14\right)e^x+\left(-x^2+\tfrac x4\right)e^x=e^x\left(-x^2-\tfrac74x+\tfrac14\right).
$$

 ✓ Coincide con la respuesta oficial.

### i) $f(x)=3x(\sqrt{x}+\operatorname{sen}x)$

$f(x)=3x^{3/2}+3x\operatorname{sen}x$. Entonces $f'(x)=\tfrac92x^{1/2}+3\operatorname{sen}x+3x\cos x=\dfrac92\sqrt x+3\operatorname{sen}x+3x\cos x$. ✓ Coincide con la respuesta oficial.

### j) $f(t)=2t\operatorname{sen}t-(t^2-2)\cos t$



$$
f'(t)=2\operatorname{sen}t+2t\cos t-\big[2t\cos t+(t^2-2)(-\operatorname{sen}t)\big]=2\operatorname{sen}t+(t^2-2)\operatorname{sen}t=t^2\operatorname{sen}t.
$$

 ✓ Coincide con la respuesta oficial.

### k) $f(x)=x^3\ln x-\dfrac{x^3}{3}$



$$
f'(x)=3x^2\ln x+x^3\cdot\dfrac1x-x^2=3x^2\ln x+x^2-x^2=3x^2\ln x.
$$

 ✓ Coincide con la respuesta oficial.

### l) $f(x)=\dfrac{\ln x}{x}$



$$
f'(x)=\dfrac{\tfrac1x\cdot x-\ln x\cdot1}{x^2}=\dfrac{1-\ln x}{x^2}.
$$

 ✓ Coincide con la respuesta oficial.

### ll) $g(t)=\dfrac{t}{t+a/t}$

Multiplicamos numerador y denominador por $t$: $g(t)=\dfrac{t^2}{t^2+a}$.



$$
g'(t)=\dfrac{2t(t^2+a)-t^2\cdot2t}{(t^2+a)^2}=\dfrac{2at}{(t^2+a)^2}.
$$

 ✓ Coincide con la respuesta oficial.

### m) $h(s)=\dfrac{\sqrt{s}-1}{\sqrt{s}+1}$



$$
h'(s)=\dfrac{\tfrac{1}{2\sqrt s}(\sqrt s+1)-(\sqrt s-1)\tfrac{1}{2\sqrt s}}{(\sqrt s+1)^2}=\dfrac{\tfrac{1}{2\sqrt s}\,[(\sqrt s+1)-(\sqrt s-1)]}{(\sqrt s+1)^2}=\dfrac{\tfrac{2}{2\sqrt s}}{(\sqrt s+1)^2}=\dfrac{1}{\sqrt s(\sqrt s+1)^2}.
$$

 ✓ Coincide con la respuesta oficial.

### n) $f(x)=\cot(x)(3x+2)$



$$
f'(x)=-\csc^2 x\,(3x+2)+\cot x\cdot3=-(3x+2)\csc^2 x+3\cot x.
$$

 ✓ Coincide con la respuesta oficial.

### o) $f(x)=\dfrac{x^2}{\ln x}$



$$
f'(x)=\dfrac{2x\ln x-x^2\cdot\tfrac1x}{\ln^2 x}=\dfrac{2x\ln x-x}{\ln^2 x}=\dfrac{x(2\ln x-1)}{\ln^2 x}.
$$

 ✓ Coincide con la respuesta oficial.

### p) $m(x)=(\operatorname{sen}x+\cos x)\sec x$

$(\operatorname{sen}x+\cos x)\sec x=\tan x+1$. Luego $m'(x)=\sec^2 x$. ✓ Coincide con la respuesta oficial.

### q) $l(z)=z^2\operatorname{sen}z+2z\cos z-2\operatorname{sen}z$



$$
l'(z)=2z\operatorname{sen}z+z^2\cos z+2\cos z-2z\operatorname{sen}z-2\cos z=z^2\cos z.
$$

 ✓ Coincide con la respuesta oficial.

### r) $a(x)=\dfrac{e^x}{x}$



$$
a'(x)=\dfrac{e^x\cdot x-e^x\cdot1}{x^2}=\dfrac{e^x x-e^x}{x^2}=\dfrac{e^x(x-1)}{x^2}.
$$

 ✓ Coincide con la respuesta oficial.

### s) $s(t)=\dfrac{\cos t}{1+\operatorname{sen}t}$



$$
s'(t)=\dfrac{-\operatorname{sen}t(1+\operatorname{sen}t)-\cos t\cos t}{(1+\operatorname{sen}t)^2}=\dfrac{-\operatorname{sen}t-\operatorname{sen}^2t-\cos^2t}{(1+\operatorname{sen}t)^2}=\dfrac{-\operatorname{sen}t-1}{(1+\operatorname{sen}t)^2}=-\dfrac{1}{1+\operatorname{sen}t}.
$$

 ✓ Coincide con la respuesta oficial.

---

## Ejercicio 7* — Tangente que pasa por $(0,2)$

**Enunciado.** La tangente a $y=f(x)$ en $(4,3)$ pasa por $(0,2)$. Hallar $f(4)$ y $f'(4)$.

Como el punto de tangencia es $(4,3)$, $f(4)=3$. La pendiente de la tangente es la de la recta que une $(4,3)$ y $(0,2)$:



$$
f'(4)=\dfrac{3-2}{4-0}=\dfrac14.
$$



**$f(4)=3$ y $f'(4)=\dfrac14$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 8 — Tangentes perpendiculares de $y=x$ y $y=1/x$

**Enunciado.** Mostrar que en las intersecciones de $y=x$ e $y=1/x$ las tangentes son perpendiculares.

Intersecciones: $x=\dfrac1x\Rightarrow x^2=1\Rightarrow x=\pm1$, puntos $(1,1)$ y $(-1,-1)$.

La recta $y=x$ tiene pendiente $1$ en todo punto. Para $g(x)=\dfrac1x$, $g'(x)=-\dfrac{1}{x^2}$, y en $x=\pm1$ vale $g'(\pm1)=-1$.

Producto de pendientes: $1\cdot(-1)=-1$, **por lo tanto las tangentes son perpendiculares** en ambas intersecciones.

✓ Coincide con el resultado esperado.

---

## Ejercicio 9* — Tangente horizontal de $f(x)=x+2\operatorname{sen}x$

**Enunciado.** ¿Para qué $x$ la gráfica tiene tangente horizontal?

Tangente horizontal $\Leftrightarrow f'(x)=0$. $f'(x)=1+2\cos x=0\Rightarrow\cos x=-\dfrac12$.



$$
x=\dfrac{2\pi}{3}+2k\pi\quad\text{o}\quad x=\dfrac{4\pi}{3}+2k\pi,\qquad k\in\mathbb{Z}.
$$



✓ Coincide con la respuesta oficial.

---

## Ejercicio 10 — Normal a $y=x-x^2$ en $(1,0)$

**Enunciado.** ¿La normal en $(1,0)$ corta la parábola otra vez?

$f'(x)=1-2x$, $f'(1)=-1$. Pendiente de la normal: $-\dfrac{1}{-1}=1$. Normal: $y-0=1(x-1)\Rightarrow y=x-1$.

Intersección con la parábola: $x-1=x-x^2\Rightarrow x^2=1\Rightarrow x=\pm1$. Para $x=1$, $y=0$ (el punto dado); para $x=-1$, $y=-2$.

**Sí: la normal corta la parábola otra vez en $P_1(-1,-2)$ (además de $P_2(1,0)$).**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 11 — Ángulo de la tangente a $y=\operatorname{sen}x$ en $x=\pi$

**Enunciado.** ¿Qué ángulo forma la tangente?

$f'(x)=\cos x$, $f'(\pi)=\cos\pi=-1$. El ángulo de inclinación cumple $\tan\alpha=-1$, con $\alpha\in[0°,180°)$:



$$
\alpha=135°.
$$



✓ Coincide con la respuesta oficial.

---

## Ejercicio 12* — Tangente con inclinación 45° en $f(x)=\dfrac{x}{1-x^2}$

**Enunciado.** Hallar los puntos con tangente de inclinación $45°$ ($m=\tan45°=1$).



$$
f'(x)=\dfrac{(1-x^2)-x(-2x)}{(1-x^2)^2}=\dfrac{1+x^2}{(1-x^2)^2}=1.
$$



$1+x^2=(1-x^2)^2=1-2x^2+x^4\Rightarrow x^4-3x^2=0\Rightarrow x^2(x^2-3)=0\Rightarrow x=0,\ x=\pm\sqrt3$.

Evaluando $f$: $f(0)=0$; $f(\sqrt3)=\dfrac{\sqrt3}{1-3}=-\dfrac{\sqrt3}{2}$; $f(-\sqrt3)=\dfrac{\sqrt3}{2}$.

**$P_1(0,0)$, $P_2\!\left(\sqrt3,-\tfrac{\sqrt3}{2}\right)$, $P_3\!\left(-\sqrt3,\tfrac{\sqrt3}{2}\right)$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 13 — Tangentes a $1/x$ y $1/x^2$

**Enunciado.** a) La tangente a $f(x)=1/x$ en $(a,f(a))$ no corta la curva salvo en el punto. b) La tangente a $f(x)=1/x^2$ en $(a,f(a))$ la corta en dos puntos.

### a) $f(x)=1/x$

$f'(a)=-\dfrac{1}{a^2}$. Tangente: $y=\dfrac1a-\dfrac{1}{a^2}(x-a)=\dfrac2a-\dfrac{x}{a^2}$. Intersección con la curva:



$$
\dfrac1x=\dfrac2a-\dfrac{x}{a^2}\;\Rightarrow\;a^2=2ax-x^2\;\Rightarrow\;x^2-2ax+a^2=0\;\Rightarrow\;(x-a)^2=0.
$$



Raíz doble $x=a$: **la tangente solo toca la curva en $(a,1/a)$.**

### b) $f(x)=1/x^2$

$f'(a)=-\dfrac{2}{a^3}$. Tangente: $y=\dfrac{1}{a^2}-\dfrac{2}{a^3}(x-a)=\dfrac{3}{a^2}-\dfrac{2x}{a^3}$. Intersección:



$$
\dfrac{1}{x^2}=\dfrac{3}{a^2}-\dfrac{2x}{a^3}\;\Rightarrow\;a^3=3a x^2-2x^3\;\Rightarrow\;2x^3-3ax^2+a^3=0.
$$



Como $x=a$ es raíz (tangencia, doble), factorizamos: $2x^3-3ax^2+a^3=(x-a)^2(2x+a)$. La otra raíz: $2x+a=0\Rightarrow x=-\dfrac a2$.

**La tangente corta la curva en $(a,1/a^2)$ y además en $\left(-\tfrac a2,\tfrac{4}{a^2}\right)$, es decir en dos puntos.**

✓ Coincide con el resultado esperado.

---

## Ejercicio 14 — Normal con inclinación 60° en $y=\dfrac{1-x}{1+x}$

**Enunciado.** Hallar los puntos donde la normal tiene inclinación $60°$.

La normal tiene pendiente $\tan60°=\sqrt3$, luego la tangente tiene pendiente $m=-\dfrac{1}{\sqrt3}$.



$$
f'(x)=\dfrac{-(1+x)-(1-x)}{(1+x)^2}=\dfrac{-2}{(1+x)^2}=-\dfrac{1}{\sqrt3}.
$$



$\dfrac{2}{(1+x)^2}=\dfrac{1}{\sqrt3}\Rightarrow(1+x)^2=2\sqrt3\Rightarrow 1+x=\pm\sqrt{2\sqrt3}=\pm\sqrt[4]{12}$.



$$
x_1=-1-\sqrt[4]{12},\qquad x_2=-1+\sqrt[4]{12}.
$$



Las ordenadas: $y=\dfrac{1-x}{1+x}$. Con $1+x=\pm\sqrt[4]{12}$ y $1-x=2-(1+x)$:



$$
P_1\!\left(-1-\sqrt[4]{12},\ \dfrac{2+\sqrt[4]{12}}{-\sqrt[4]{12}}\right)\approx(-2{,}861,\ 3{,}303),\qquad P_2\!\left(-1+\sqrt[4]{12},\ \dfrac{2-\sqrt[4]{12}}{\sqrt[4]{12}}\right)\approx(0{,}861,\ 0{,}075).
$$



**$P_1\!\left(-1-\sqrt[4]{12},\ \tfrac{2+\sqrt[4]{12}}{-\sqrt[4]{12}}\right)$ y $P_2\!\left(-1+\sqrt[4]{12},\ \tfrac{2-\sqrt[4]{12}}{\sqrt[4]{12}}\right)$.**

✓ Coincide con la respuesta oficial (las abscisas $-1\mp\sqrt[4]{12}$).

---

## Ejercicio 15 — Tangente paralela a $3x-y+6=0$

**Enunciado.** ¿En qué punto de $f(x)=x\sqrt{x}$ la tangente es paralela a $3x-y+6=0$?

La recta dada es $y=3x+6$, pendiente $3$. $f(x)=x^{3/2}$, $f'(x)=\dfrac32\sqrt{x}=3\Rightarrow\sqrt x=2\Rightarrow x=4$. Entonces $f(4)=4\cdot2=8$.

**$P(4,8)$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 16 — Determinar $a$ para que $y=9x+24$ sea tangente

**Enunciado.** Hallar $a$ tal que $y=9x+24$ sea tangente a $f(x)=\dfrac{ax}{2x+3}$ en $x=-2$.

Punto de tangencia en $x=-2$ sobre la recta: $y=9(-2)+24=6$. Debe ser $f(-2)=6$:



$$
f(-2)=\dfrac{-2a}{2(-2)+3}=\dfrac{-2a}{-1}=2a=6\;\Rightarrow\;a=3.
$$



Verificación de pendiente: $f'(x)=\dfrac{a(2x+3)-ax\cdot2}{(2x+3)^2}=\dfrac{3a}{(2x+3)^2}$, en $x=-2$: $\dfrac{3\cdot3}{1}=9=$ pendiente de la recta. ✓

**$a=3$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 17 — Hallar $a,b$ para tangente dada

**Enunciado.** Hallar $a,b$ para que $f(x)=ax^3+bx^2+x$ tenga tangente $y=2x-4$ en $x=1$.

Dos condiciones: $f(1)=2(1)-4=-2$ y $f'(1)=2$.

$f(1)=a+b+1=-2\Rightarrow a+b=-3$.
$f'(x)=3ax^2+2bx+1$, $f'(1)=3a+2b+1=2\Rightarrow3a+2b=1$.

Resolviendo: de la primera $b=-3-a$; sustituyendo $3a+2(-3-a)=1\Rightarrow a-6=1\Rightarrow a=7$, $b=-10$.

**$a=7$, $b=-10$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 18* — $f(x)=x+\ln x$ tiene tangente por el origen

**Enunciado.** Mostrar que existe una tangente que pasa por el origen.

En $x=a>0$: $f(a)=a+\ln a$, $f'(a)=1+\dfrac1a$. Tangente: $y-(a+\ln a)=\left(1+\tfrac1a\right)(x-a)$. Que pase por $(0,0)$:



$$
-(a+\ln a)=\left(1+\tfrac1a\right)(-a)=-a-1\;\Rightarrow\;-a-\ln a=-a-1\;\Rightarrow\;\ln a=1\;\Rightarrow\;a=e.
$$



**Existe la tangente en $x=e$:** pendiente $1+\tfrac1e$, y como $f(e)=e+1$, la tangente es $y=\left(1+\tfrac1e\right)x$, que pasa por el origen.

✓ Coincide con el resultado esperado.

---

## Ejercicio 19* — Dos tangentes a $y=4x-x^2$ por $(2,5)$

**Enunciado.** Hallar las dos tangentes que pasan por $(2,5)$.

En $x=a$: $f(a)=4a-a^2$, $f'(a)=4-2a$. La tangente pasa por $(2,5)$:



$$
5-(4a-a^2)=(4-2a)(2-a)\;\Rightarrow\;5-4a+a^2=8-8a+2a^2\;\Rightarrow\;a^2-4a+3=0\;\Rightarrow\;a=1,\ a=3.
$$



- $a=1$: $f(1)=3$, $m=2$: $y-3=2(x-1)\Rightarrow y=2x+1$.
- $a=3$: $f(3)=3$, $m=-2$: $y-3=-2(x-3)\Rightarrow y=-2x+9$.

**$y=2x+1$ y $y=-2x+9$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 20 — Derivar (regla de la cadena)

**Enunciado.** Derivar usando la regla de la cadena.

### a) $f(x)=\sqrt[3]{x^2+2x}$

$f=(x^2+2x)^{1/3}$, $f'=\tfrac13(x^2+2x)^{-2/3}(2x+2)=\dfrac{2x+2}{3(x^2+2x)^{2/3}}$. ✓ Coincide con la respuesta oficial.

### b) $f(x)=e^{-x^2}$

$f'=e^{-x^2}\cdot(-2x)=-2xe^{-x^2}$. ✓ Coincide con la respuesta oficial.

### c) $f(t)=\operatorname{sen}^2 t$

$f'=2\operatorname{sen}t\cos t$. ✓ Coincide con la respuesta oficial.

### d) $f(x)=\cos\sqrt{x}$

$f'=-\operatorname{sen}\sqrt x\cdot\dfrac{1}{2\sqrt x}=-\dfrac{\operatorname{sen}\sqrt x}{2\sqrt x}$. ✓ Coincide con la respuesta oficial.

### e) $f(x)=\sqrt{x^2+a^2}$

$f'=\dfrac{2x}{2\sqrt{x^2+a^2}}=\dfrac{x}{\sqrt{x^2+a^2}}$. ✓ Coincide con la respuesta oficial.

### f) $f(x)=\ln^4(3x^2+5x^4)$

$f'=4\ln^3(3x^2+5x^4)\cdot\dfrac{1}{3x^2+5x^4}\cdot(6x+20x^3)=\dfrac{4(6x+20x^3)\ln^3(3x^2+5x^4)}{3x^2+5x^4}$. ✓ Coincide con la respuesta oficial.

### g) $f(x)=\sqrt{\ln(x^2)}$

$f'=\dfrac{1}{2\sqrt{\ln(x^2)}}\cdot\dfrac{2x}{x^2}=\dfrac{1}{2\sqrt{\ln(x^2)}}\cdot\dfrac{2}{x}=\dfrac{1}{x\sqrt{\ln(x^2)}}$. ✓ Coincide con la respuesta oficial.

### h) $f(t)=\operatorname{sen}\left(\dfrac{t}{\sqrt{t+1}}\right)$

Derivada interna: $\left(\dfrac{t}{\sqrt{t+1}}\right)'=\dfrac{\sqrt{t+1}-t\cdot\tfrac{1}{2\sqrt{t+1}}}{t+1}=\dfrac{(t+1)-\tfrac t2}{(t+1)^{3/2}}=\dfrac{t+2}{2(t+1)^{3/2}}$.



$$
f'(t)=\cos\!\left(\dfrac{t}{\sqrt{t+1}}\right)\cdot\dfrac{t+2}{2(t+1)^{3/2}}.
$$

 ✓ Coincide con la respuesta oficial.

### i) $f(x)=\ln^2(x)+\ln(\ln x)$

$f'=2\ln x\cdot\dfrac1x+\dfrac{1}{\ln x}\cdot\dfrac1x=\dfrac1x\left(2\ln x+\dfrac{1}{\ln x}\right)$. ✓ Coincide con la respuesta oficial.

### j) $f(x)=\ln\sqrt{\dfrac{1+x}{1-x}}$

$f=\dfrac12\big[\ln(1+x)-\ln(1-x)\big]$, $f'=\dfrac12\left(\dfrac{1}{1+x}+\dfrac{1}{1-x}\right)=\dfrac12\cdot\dfrac{2}{1-x^2}=\dfrac{1}{1-x^2}$. ✓ Coincide con la respuesta oficial.

### k) $f(x)=\ln(2x)+\log 2+\log(2x)$

$\log2$ es constante. $\dfrac{d}{dx}\ln(2x)=\dfrac1x$; $\dfrac{d}{dx}\log(2x)=\dfrac{1}{x\ln10}$.



$$
f'(x)=\dfrac1x+\dfrac{1}{x\ln10}.
$$

 ✓ Coincide con la respuesta oficial.

### l) $f(t)=2^{\operatorname{sen}\sqrt{t}}\cos\sqrt{t}$

Producto. Primer factor: $\left(2^{\operatorname{sen}\sqrt t}\right)'=2^{\operatorname{sen}\sqrt t}\ln2\cdot\cos\sqrt t\cdot\dfrac{1}{2\sqrt t}$. Segundo factor: $\left(\cos\sqrt t\right)'=-\operatorname{sen}\sqrt t\cdot\dfrac{1}{2\sqrt t}$.



$$
f'(t)=\ln2\cdot2^{\operatorname{sen}\sqrt t}\cdot\dfrac{\cos^2\sqrt t}{2\sqrt t}-2^{\operatorname{sen}\sqrt t}\cdot\dfrac{\operatorname{sen}\sqrt t}{2\sqrt t}.
$$

 ✓ Coincide con la respuesta oficial.

### m) $f(r)=\sqrt[3]{\tan(2r)}$

$f=\tan^{1/3}(2r)$, $f'=\tfrac13\tan^{-2/3}(2r)\cdot\sec^2(2r)\cdot2=\dfrac23\tan^{-2/3}(2r)\sec^2(2r)$. ✓ Coincide con la respuesta oficial.

### n) $f(x)=\cos(x^2-\operatorname{sen}x)\tan(2x)$



$$
f'(x)=-\operatorname{sen}(x^2-\operatorname{sen}x)(2x-\cos x)\tan(2x)+2\cos(x^2-\operatorname{sen}x)\sec^2(2x).
$$

 ✓ Coincide con la respuesta oficial.

### o) $g(z)=10^{z\tan z}$

$g'=10^{z\tan z}\ln10\cdot(z\tan z)'=10^{z\tan z}\ln10\,(\tan z+z\sec^2 z)$. ✓ Coincide con la respuesta oficial.

### p) $y=\sqrt{1+x}-\ln(1+\sqrt{1+x})$

$y'=\dfrac{1}{2\sqrt{1+x}}-\dfrac{\tfrac{1}{2\sqrt{1+x}}}{1+\sqrt{1+x}}=\dfrac{1}{2\sqrt{1+x}}\left(1-\dfrac{1}{1+\sqrt{1+x}}\right)=\dfrac{1}{2\sqrt{1+x}}\cdot\dfrac{\sqrt{1+x}}{1+\sqrt{1+x}}=\dfrac{1}{2+2\sqrt{1+x}}$. ✓ Coincide con la respuesta oficial.

### q) $y=\dfrac{(2x^3+3)^2}{\ln(x^2+1)}$

Cociente, con $u=(2x^3+3)^2$, $u'=2(2x^3+3)\cdot6x^2=12x^2(2x^3+3)$, y $v=\ln(x^2+1)$, $v'=\dfrac{2x}{x^2+1}$:



$$
y'=\dfrac{12x^2(2x^3+3)\ln(x^2+1)-(2x^3+3)^2\cdot\tfrac{2x}{x^2+1}}{\ln^2(x^2+1)}.
$$

 ✓ Coincide con la respuesta oficial (reordenada).

### r) $y=\cos^2\left(\dfrac{1-\sqrt{x}}{1+\sqrt{x}}\right)$

Sea $u=\dfrac{1-\sqrt x}{1+\sqrt x}$. Derivada interna: $u'=\dfrac{-\tfrac{1}{2\sqrt x}(1+\sqrt x)-(1-\sqrt x)\tfrac{1}{2\sqrt x}}{(1+\sqrt x)^2}=\dfrac{-\tfrac{1}{2\sqrt x}\cdot2}{(1+\sqrt x)^2}=\dfrac{-1}{\sqrt x(1+\sqrt x)^2}$.

$y'=2\cos u(-\operatorname{sen}u)\,u'=-\operatorname{sen}(2u)\,u'=\dfrac{1}{\sqrt x(1+\sqrt x)^2}\operatorname{sen}\!\left(2\cdot\dfrac{1-\sqrt x}{1+\sqrt x}\right)$. ✓ Coincide con la respuesta oficial.

---

## Ejercicio 21 — Tangente a una composición

**Enunciado.** La tangente a $f$ en $x=-1$ es $y=-5x+3$. Hallar la tangente a $g(x)=f(-x^2+\operatorname{sen}(\pi x))$ en $x=1$.

De la tangente: $f(-1)=-5(-1)+3=8$ y $f'(-1)=-5$.

Sea $u(x)=-x^2+\operatorname{sen}(\pi x)$. $u(1)=-1+\operatorname{sen}\pi=-1$. $u'(x)=-2x+\pi\cos(\pi x)$, $u'(1)=-2+\pi\cos\pi=-2-\pi$.



$$
g(1)=f(u(1))=f(-1)=8,\qquad g'(1)=f'(-1)\cdot u'(1)=(-5)(-2-\pi)=10+5\pi.
$$



Tangente: $y-8=(10+5\pi)(x-1)$, es decir **$y=(10+5\pi)(x-1)+8$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 22 — Hallar $a,b$ para tangente $y=-5x+8$

**Enunciado.** $f(x)=ax^2e^{x^3-1}+b$; hallar $a,b$ para que $y=-5x+8$ sea tangente en $x=1$.

$f(1)=a\cdot1\cdot e^0+b=a+b$. En la recta $x=1$ da $y=3$, luego $a+b=3$.

$f'(x)=a\big[2xe^{x^3-1}+x^2e^{x^3-1}\cdot3x^2\big]=ae^{x^3-1}(2x+3x^4)$. En $x=1$: $f'(1)=a(2+3)=5a$. Debe ser $-5$: $5a=-5\Rightarrow a=-1$, entonces $b=4$.

**$a=-1$, $b=4$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 23 — Derivadas de composiciones y productos

### a)* $h(x)=\dfrac{f(\ln(x+1))}{g(e^x)}$, tangente a $f$ en $x=0$ es $y=2x$, $g(1)=4$

De $y=2x$: $f(0)=0$, $f'(0)=2$. En $x=0$: $\ln(0+1)=0$, $e^0=1$.

$h'(x)=\dfrac{f'(\ln(x+1))\cdot\tfrac{1}{x+1}\cdot g(e^x)-f(\ln(x+1))\cdot g'(e^x)e^x}{g(e^x)^2}$.

En $x=0$: $h'(0)=\dfrac{f'(0)\cdot1\cdot g(1)-f(0)\cdot g'(1)\cdot1}{g(1)^2}=\dfrac{2\cdot4-0}{16}=\dfrac{8}{16}=\dfrac12$.

**$h'(0)=\dfrac12$.** ✓ Coincide con la respuesta oficial.

### b)* $y=2x+3$ tangente a $g$ en $x=-2$; $f(x)=\dfrac{x}{x^2+1}$; calcular $(f\circ g)'(-2)$

De la tangente: $g(-2)=2(-2)+3=-1$, $g'(-2)=2$.

$f'(x)=\dfrac{(x^2+1)-x\cdot2x}{(x^2+1)^2}=\dfrac{1-x^2}{(x^2+1)^2}$, $f'(-1)=\dfrac{1-1}{4}=0$.

$(f\circ g)'(-2)=f'(g(-2))\cdot g'(-2)=f'(-1)\cdot2=0$.

**$(f\circ g)'(-2)=0$.** ✓ Coincide con la respuesta oficial.

### c)* $h(x)=f(x)g(x)$, $g(x)=\dfrac{e^{x^2}}{2x-3}$, tangente a $f$ en $x=1$ es $y=-3x+5$

De la tangente: $f(1)=2$, $f'(1)=-3$. Calculamos $g(1)=\dfrac{e}{-1}=-e$.

$g'(x)=\dfrac{2xe^{x^2}(2x-3)-e^{x^2}\cdot2}{(2x-3)^2}$, $g'(1)=\dfrac{2e(-1)-2e}{1}=-4e$.

$h'(1)=f'(1)g(1)+f(1)g'(1)=(-3)(-e)+2(-4e)=3e-8e=-5e$.

**$h'(1)=-5e$.** ✓ Coincide con la respuesta oficial.

### d) $p(x)=\dfrac{1}{x-9}$, $m(x)=x^2-16$, $h=p\circ m$: tangente horizontal en intersección con eje $y$

$h(x)=p(m(x))=\dfrac{1}{x^2-16-9}=\dfrac{1}{x^2-25}$. Intersección con el eje $y$: $x=0$.

$h'(x)=-\dfrac{2x}{(x^2-25)^2}$, $h'(0)=0$. **La pendiente es $0$, por lo tanto la tangente es horizontal** (es $y=h(0)=-\tfrac{1}{25}$).

✓ Coincide con el resultado esperado.

---

## Ejercicio 24 — $f(x)=x^2\operatorname{sen}(1/x)$

**Enunciado.** Estudiar continuidad de $f$ en $0$, derivabilidad en $0$ y continuidad de $f'$ en $0$, con $f(x)=x^2\operatorname{sen}(1/x)$ ($x\neq0$), $f(0)=0$.

**Continuidad en $0$.** $\lvert x^2\operatorname{sen}(1/x)\rvert\le x^2\to0$, luego $\lim_{x\to0}f(x)=0=f(0)$: **continua en $0$.**

**Derivabilidad en $0$.** Por definición:



$$
f'(0)=\lim_{h\to0}\dfrac{h^2\operatorname{sen}(1/h)-0}{h}=\lim_{h\to0}h\operatorname{sen}(1/h)=0
$$



(acotación: $\lvert h\operatorname{sen}(1/h)\rvert\le\lvert h\rvert\to0$). **Derivable en $0$, $f'(0)=0$.**

**Continuidad de $f'$ en $0$.** Para $x\neq0$: $f'(x)=2x\operatorname{sen}(1/x)+x^2\cos(1/x)\cdot\left(-\tfrac{1}{x^2}\right)=2x\operatorname{sen}(1/x)-\cos(1/x)$.

$\lim_{x\to0}f'(x)$ no existe (el término $\cos(1/x)$ oscila entre $-1$ y $1$). Como $\lim_{x\to0}f'(x)\neq f'(0)=0$, **$f'$ NO es continua en $0$.**

✓ Coincide con el resultado esperado (es el ejemplo clásico de función derivable con derivada discontinua).

---

## Ejercicio 25 — Hallar $m,b$ para derivabilidad en $\mathbb{R}$

**Enunciado.** Hallar $m,b$ para que cada función sea derivable en todo $\mathbb{R}$. Se exige continuidad y coincidencia de derivadas laterales en el punto de empalme.

### a) $f(x)=x^2$ ($x\le2$); $mx+b$ ($x>2$)

Continuidad en $2$: $4=2m+b$. Derivadas: $2x\big|_2=4$ y $m$, igualdad $m=4$. Entonces $b=4-2\cdot4=-4$.

**$m=4$, $b=-4$.** ✓ Coincide con la respuesta oficial.

### b) $f(x)=xe^{-1/x}$ ($x>0$); $mx+b$ ($x\le0$)

Cuando $x\to0^+$, $e^{-1/x}\to0$ y $xe^{-1/x}\to0$, así que para continuidad $b=0$. La derivada por derecha en $0$: $\lim_{x\to0^+}\dfrac{xe^{-1/x}}{x}=\lim_{x\to0^+}e^{-1/x}=0$. Por izquierda la pendiente es $m$, luego $m=0$.

**$m=0$, $b=0$.** ✓ Coincide con la respuesta oficial.

### c) $f(x)=mx^3$ ($x<2$); $x^2+b$ ($x\ge2$)

Continuidad en $2$: $8m=4+b$. Derivadas: $3mx^2\big|_2=12m$ y $2x\big|_2=4$, igualdad $12m=4\Rightarrow m=\tfrac13$. Entonces $b=8m-4=\tfrac83-4=-\tfrac43$.

**$m=\dfrac13$, $b=-\dfrac43$.** ✓ Coincide con la respuesta oficial.

---

## Ejercicio 26 — Tangente paralela a $y-4x+6=0$ en $f(x)=x\lvert x\rvert$

**Enunciado.** ¿En qué puntos la tangente es paralela a $y-4x+6=0$? Hallar la tangente.

La recta es $y=4x-6$, pendiente $4$. Del Ejercicio 5d, $f'(x)=2\lvert x\rvert$. Igualamos: $2\lvert x\rvert=4\Rightarrow\lvert x\rvert=2\Rightarrow x=\pm2$.

- $x=2$: $f(2)=2\cdot2=4\Rightarrow P(2,4)$. Tangente: $y-4=4(x-2)\Rightarrow y=4x-4$.
- $x=-2$: $f(-2)=-2\cdot2=-4\Rightarrow Q(-2,-4)$. Tangente: $y+4=4(x+2)\Rightarrow y=4x+4$.

**Puntos $P(2,4)$ y $Q(-2,-4)$; tangentes $y=4x-4$ y $y=4x+4$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 27 — Movimiento $s(t)=t^3-6t^2+9t$

**Enunciado.** Analizar el movimiento dado por $s(t)=t^3-6t^2+9t$ (en metros, $t$ en segundos, $t\ge0$).

### a) Velocidad

$v(t)=s'(t)=3t^2-12t+9=3(t-1)(t-3)$.

### b) $v(2)$ y $v(4)$

$v(2)=3(1)(-1)=-3$ m/s; $v(4)=3(3)(1)=9$ m/s.

### c) Reposo

$v(t)=0\Rightarrow t=1$ y $t=3$ s.

### d) Sentido positivo

$v(t)>0\Leftrightarrow(t-1)(t-3)>0\Leftrightarrow 0\le t<1$ o $t>3$.

### e) Diagrama

Posiciones clave: $s(0)=0$, $s(1)=4$ (máx local), $s(3)=0$ (mín local), $s(5)=20$. La partícula avanza de $0$ a $4$, retrocede de $4$ a $0$, y vuelve a avanzar de $0$ a $20$.

### f) Distancia total en 5 s



$$
\lvert s(1)-s(0)\rvert+\lvert s(3)-s(1)\rvert+\lvert s(5)-s(3)\rvert=4+4+20=28\ \text{m}.
$$



**$v(t)=3t^2-12t+9$; $v(2)=-3$, $v(4)=9$ m/s; reposo en $t=1,3$ s; sentido positivo en $0\le t<1$ o $t>3$; distancia total $28$ m.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 28 — Dos partículas

**Enunciado.** $s_1(t)=t^2-4t$ y $s_2(t)=3t-t^2$ (paran a los 6 s).

### a) Posiciones en $t=1$ y $t=4$

$s_1(1)=1-4=-3$ (3 m a la izquierda); $s_2(1)=3-1=2$ (2 m a la derecha).
$s_1(4)=16-16=0$ (vuelve al inicio); $s_2(4)=12-16=-4$ (4 m a la izquierda).

### b) Gráfica, dominio/imagen y posición final

Dominio $[0,6]$. $s_1$ es parábola con vértice en $t=2$ ($s_1(2)=-4$); $s_2$ con vértice en $t=1{,}5$ ($s_2(1{,}5)=2{,}25$). Posición final ($t=6$): $s_1(6)=36-24=12$ (12 m a la derecha); $s_2(6)=18-36=-18$ (18 m a la izquierda).

### c) Igual velocidad

$v_1(t)=2t-4$, $v_2(t)=3-2t$. Igualando: $2t-4=3-2t\Rightarrow4t=7\Rightarrow t=1{,}75$ s. Velocidad común: $v_1(1{,}75)=2(1{,}75)-4=-0{,}5$ m/s.

**En $t=1$: $p_1$ a $3$ m a la izquierda, $p_2$ a $2$ m a la derecha; en $t=4$: $p_1$ al inicio, $p_2$ a $4$ m a la izquierda; final: $p_1$ a $12$ m derecha, $p_2$ a $18$ m izquierda; igual velocidad en $t=1{,}75$ s, $v=-\tfrac12$ m/s.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 29* — Vaciado de Torricelli $V(t)=5000(1-t/40)^2$

**Enunciado.** $V(t)=5000(1-t/40)^2$ litros, $0\le t\le40$ min.

### a) Dominio e imagen

Dominio $[0,40]$. $V(0)=5000$, $V(40)=0$, decreciente: imagen $[0,5000]$.

### b) Tasa instantánea en $t=20$

$V'(t)=5000\cdot2(1-t/40)\cdot(-\tfrac{1}{40})=-250(1-t/40)$. En $t=20$: $V'(20)=-250(1-\tfrac12)=-125$ l/min.

**El signo negativo indica que el volumen decrece (sale agua) a razón de $125$ l/min.**

### c) Significado de $V^{-1}$

$V^{-1}(\ell)$ da el tiempo en que quedan $\ell$ litros. Despejando: $\ell=5000(1-t/40)^2\Rightarrow\sqrt{\ell/5000}=1-t/40\Rightarrow t=40-40\sqrt{\ell/5000}$, o sea $V^{-1}(\ell)=40-40\sqrt{\ell/5000}$.

✓ Coincide con la respuesta oficial.

---

## Ejercicio 30* — Clavadista $s(t)=-16t^2+16t+32$

**Enunciado.** $s(t)=-16t^2+16t+32$ (pies). Hallar el tiempo de llegada al agua y la velocidad de impacto.

### a) Tiempo al agua ($s=0$)

$-16t^2+16t+32=0\Rightarrow t^2-t-2=0\Rightarrow(t-2)(t+1)=0\Rightarrow t=2$ s (la raíz negativa se descarta).

### b) Velocidad de impacto

$v(t)=s'(t)=-32t+16$, $v(2)=-64+16=-48$ pies/s.

**Llega al agua a los $2$ s con velocidad $-48$ pies/s** (el signo indica que baja).

✓ Coincide con la respuesta oficial.

---

## Ejercicio 31* — Enfriamiento $C(t)=20+70e^{-0{,}1t}$

**Enunciado.** $C(t)=20+70e^{-0{,}1t}$ (°C, $t$ en min).

### a) Velocidad a los 5 min

$C'(t)=70e^{-0{,}1t}(-0{,}1)=-7e^{-0{,}1t}$. $C'(5)=-7e^{-0{,}5}\approx-7\cdot0{,}6065\approx-4{,}246$ °C/min.

### b) Proporcional a $C-20$

$C-20=70e^{-0{,}1t}$, y $C'(t)=-7e^{-0{,}1t}=-0{,}1\,(70e^{-0{,}1t})=-0{,}1\,(C-20)$. **La velocidad es proporcional a $C-20$ con constante $-0{,}1$** (ley de enfriamiento de Newton).

### c) Tiende a 0

Cuando $t\to\infty$, $e^{-0{,}1t}\to0$, así que $C'(t)\to0$: la temperatura tiende a estabilizarse en $20$ °C.

**$C'(5)\approx-4{,}246$ °C/min.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 32 — Derivada de la inversa

**Enunciado.** Usar $(f^{-1})'(y)=\dfrac{1}{f'(f^{-1}(y))}$.

### a) $f$ derivable, inversa, pasa por $(2,4)$ con pendiente $1/3$; tangente a la inversa en $x=4$

$f(2)=4$ y $f'(2)=\tfrac13$. La inversa pasa por $(4,2)$ (se invierten coordenadas) y $(f^{-1})'(4)=\dfrac{1}{f'(2)}=3$.

Tangente a $f^{-1}$ en $(4,2)$: $y-2=3(x-4)\Rightarrow y=3x-10$.

**$y=3x-10$.** ✓ Coincide con la respuesta oficial.

### b)* $f(x)=x^3+x-2$; calcular $(f^{-1})'(-2)$

Buscamos $a$ con $f(a)=-2$: $a^3+a-2=-2\Rightarrow a^3+a=0\Rightarrow a(a^2+1)=0\Rightarrow a=0$. $f'(x)=3x^2+1$, $f'(0)=1$.

$(f^{-1})'(-2)=\dfrac{1}{f'(0)}=\dfrac11=1$.

**$(f^{-1})'(-2)=1$.** ✓ Coincide con la respuesta oficial.

---

## Ejercicio 33 — Derivadas con funciones trigonométricas inversas

### a) $f(x)=e^{\arcsin(3x)}$

$f'(x)=e^{\arcsin(3x)}\cdot\dfrac{3}{\sqrt{1-(3x)^2}}=e^{\arcsin(3x)}\cdot\dfrac{3}{\sqrt{1-9x^2}}$. ✓ Coincide con la respuesta oficial.

### b) $f(x)=x\arccos(2x)$

$f'(x)=\arccos(2x)+x\cdot\dfrac{-2}{\sqrt{1-4x^2}}=\arccos(2x)-\dfrac{2x}{\sqrt{1-4x^2}}$. ✓ Coincide con la respuesta oficial.

### c) $h(x)=\dfrac{\arctan x}{g(x)}$, $g(0)\neq0$, $g'(0)=0$; calcular $h'(0)$

$h'(x)=\dfrac{\tfrac{1}{1+x^2}g(x)-\arctan x\cdot g'(x)}{g(x)^2}$. En $x=0$: $\arctan0=0$ y $g'(0)=0$:



$$
h'(0)=\dfrac{1\cdot g(0)-0}{g(0)^2}=\dfrac{1}{g(0)}.
$$



**$h'(0)=\dfrac{1}{g(0)}$.** ✓ Coincide con la respuesta oficial.

---

## Ejercicio 34 — Derivación implícita

**Enunciado.** Hallar $y'$ por derivación implícita.

### a) $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$

$\dfrac{2x}{a^2}+\dfrac{2y\,y'}{b^2}=0\Rightarrow y'=-\dfrac{b^2x}{a^2y}$. ✓ Coincide con la respuesta oficial.

### b)* $y^3-3y+2x=0$ (tangente en $(-1,2)$ y $(-1,-1)$)

Derivando: $3y^2y'-3y'+2=0\Rightarrow y'(3y^2-3)=-2\Rightarrow y'=\dfrac{-2}{3(y^2-1)}$.

En $(-1,2)$: $y'=\dfrac{-2}{3(3)}=-\dfrac29$. Tangente: $y-2=-\tfrac29(x+1)\Rightarrow y=-\tfrac29x+\tfrac{16}{9}$.

En $(-1,-1)$: $y^2-1=0$, $y'$ no está definida (denominador nulo) $\Rightarrow$ **tangente vertical $x=-1$.**

**$y'=\dfrac{-2}{3(y^2-1)}$; tangente en $(-1,2)$: $y=-\tfrac29x+\tfrac{16}{9}$; en $(-1,-1)$: $x=-1$.**

✓ Coincide con la respuesta oficial.

### c) $2y=2+xy^3$

$2y'=y^3+x\cdot3y^2y'\Rightarrow2y'-3xy^2y'=y^3\Rightarrow y'=\dfrac{y^3}{2-3xy^2}$. ✓ Coincide con la respuesta oficial.

### d) $x^2y-xy^2+x^2+y^2=0$

Derivando: $2xy+x^2y'-(y^2+x\cdot2yy')+2x+2yy'=0$.

$2xy+x^2y'-y^2-2xyy'+2x+2yy'=0\Rightarrow y'(x^2-2xy+2y)=y^2-2xy-2x$.



$$
y'=\dfrac{y^2-2xy-2x}{x^2+2y-2xy}.
$$

 ✓ Coincide con la respuesta oficial.

---

## Ejercicio 35 — Normal a $x^3+y^3=3xy$ en $(3/2,3/2)$ pasa por el origen

**Enunciado.** Mostrar que la normal en $(3/2,3/2)$ pasa por el origen (folium de Descartes).

Derivando: $3x^2+3y^2y'=3y+3xy'\Rightarrow y'(y^2-x)=y-x^2\Rightarrow y'=\dfrac{y-x^2}{y^2-x}$.

En $(3/2,3/2)$: $y'=\dfrac{3/2-9/4}{9/4-3/2}=\dfrac{-3/4}{3/4}=-1$. Pendiente de la normal: $-\dfrac{1}{-1}=1$.

Normal: $y-\tfrac32=1\left(x-\tfrac32\right)\Rightarrow y=x$. **La recta $y=x$ pasa por el origen $(0,0)$.**

✓ Coincide con el resultado esperado.

---

## Ejercicio 36* — Tangentes horizontales y verticales de $x^2-xy+y^2=27$

**Enunciado.** Hallar los puntos con tangente horizontal y vertical.

Derivando: $2x-(y+xy')+2yy'=0\Rightarrow y'(2y-x)=y-2x\Rightarrow y'=\dfrac{y-2x}{2y-x}$.

**Tangente horizontal** ($y'=0$): $y=2x$. Sustituyendo en la curva: $x^2-x(2x)+4x^2=27\Rightarrow3x^2=27\Rightarrow x=\pm3$. Puntos $P(3,6)$ y $Q(-3,-6)$.

**Tangente vertical** ($2y-x=0\Rightarrow x=2y$): $4y^2-2y\cdot y+y^2=27\Rightarrow3y^2=27\Rightarrow y=\pm3$. Puntos $R(6,3)$ y $S(-6,-3)$.

**Horizontal: $P(3,6)$, $Q(-3,-6)$. Vertical: $R(6,3)$, $S(-6,-3)$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 37 — $a$ para tangente horizontal en $x=2$

**Enunciado.** Hallar $a$ para que $x^2-xy+y^2=a$ tenga tangente horizontal en $x=2$; dar los puntos.

Tangente horizontal: $y'=\dfrac{y-2x}{2y-x}=0\Rightarrow y=2x$. En $x=2$, $y=4$. Sustituyendo en la curva:



$$
a=2^2-2\cdot4+4^2=4-8+16=12.
$$



Con $a=12$, la otra solución de $y=2x$ es $x=-2$, $y=-4$ (que también cumple $x^2-xy+y^2=4-8+16=12$).

**$a=12$; puntos $(2,4)$ y $(-2,-4)$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 38 — Tangente a $(x-2)^2-y^2=9$ en $(7,4)$

**Enunciado.** Verificar que en $(7,4)$ la tangente es paralela a $y=\tfrac54x+9$ y hallar otro punto con esa pendiente.

Derivando: $2(x-2)-2yy'=0\Rightarrow y'=\dfrac{x-2}{y}$. En $(7,4)$: $y'=\dfrac{5}{4}$, **igual a la pendiente de la recta** $\Rightarrow$ paralelas. ✓

Otro punto con $y'=\tfrac54$: $\dfrac{x-2}{y}=\tfrac54\Rightarrow x-2=\tfrac54y\Rightarrow x=2+\tfrac54y$. Sustituyendo en la curva: $\left(\tfrac54y\right)^2-y^2=9\Rightarrow\tfrac{25}{16}y^2-y^2=9\Rightarrow\tfrac{9}{16}y^2=9\Rightarrow y^2=16\Rightarrow y=\pm4$.

Para $y=4$: el punto $(7,4)$. Para $y=-4$: $x=2-5=-3$, punto $P(-3,-4)$.

**Otro punto: $P(-3,-4)$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 39 — Derivación logarítmica

**Enunciado.** Derivar tomando logaritmo natural en ambos miembros.

### a) $f(x)=x^x$

$\ln f=x\ln x\Rightarrow\dfrac{f'}{f}=\ln x+x\cdot\tfrac1x=\ln x+1\Rightarrow f'=x^x(1+\ln x)$. ✓ Coincide con la respuesta oficial.

### b) $f(x)=x^{\ln x}$

$\ln f=\ln x\cdot\ln x=\ln^2 x\Rightarrow\dfrac{f'}{f}=2\ln x\cdot\tfrac1x=\dfrac{2\ln x}{x}\Rightarrow f'=x^{\ln x}\cdot\dfrac{2\ln x}{x}$. ✓ Coincide con la respuesta oficial.

### c) $f(x)=(\operatorname{sen}x)^x$

$\ln f=x\ln\operatorname{sen}x\Rightarrow\dfrac{f'}{f}=\ln\operatorname{sen}x+x\cdot\dfrac{\cos x}{\operatorname{sen}x}=\ln\operatorname{sen}x+x\cot x$.

$f'=(\operatorname{sen}x)^x(\ln\operatorname{sen}x+x\cot x)$. ✓ Coincide con la respuesta oficial.

### d) $f(x)=e^{x^x}$

Cadena: $f'=e^{x^x}\cdot(x^x)'$, y por (a) $(x^x)'=x^x(1+\ln x)$. Entonces $f'=e^{x^x}x^x(1+\ln x)$. ✓ Coincide con la respuesta oficial.

### e) $f(x)=(2+\cos x)^{x+1}$

$\ln f=(x+1)\ln(2+\cos x)\Rightarrow\dfrac{f'}{f}=\ln(2+\cos x)+(x+1)\dfrac{-\operatorname{sen}x}{2+\cos x}$.

$f'=(2+\cos x)^{x+1}\left[\ln(2+\cos x)-\dfrac{(x+1)\operatorname{sen}x}{2+\cos x}\right]$. ✓ Coincide con la respuesta oficial.

### f) $y=(x+1)^{x^2}$

$\ln y=x^2\ln(x+1)\Rightarrow\dfrac{y'}{y}=2x\ln(x+1)+\dfrac{x^2}{x+1}$.



$$
y'=(x+1)^{x^2}\left[2x\ln(x+1)+\dfrac{x^2}{x+1}\right].
$$

 (No figura en la lista oficial; resultado verificado.)

---

## Ejercicio 40 — Derivar (potencias variables y mixtas)

### a) $f(x)=3^x$

$f'=3^x\ln3$. ✓

### b) $f(x)=(\operatorname{sen}^3 x)^{\ln x}$

$\ln f=\ln x\cdot\ln(\operatorname{sen}^3x)=3\ln x\ln\operatorname{sen}x$.

$\dfrac{f'}{f}=3\left[\dfrac{\ln\operatorname{sen}x}{x}+\ln x\cdot\cot x\right]\Rightarrow f'=(\operatorname{sen}^3x)^{\ln x}\cdot3\left(\dfrac{\ln\operatorname{sen}x}{x}+\ln x\cot x\right)$.

### c) $f(x)=(\cos x)^{e^x}$

$\ln f=e^x\ln\cos x\Rightarrow\dfrac{f'}{f}=e^x\ln\cos x+e^x\dfrac{-\operatorname{sen}x}{\cos x}$.

$f'=(\cos x)^{e^x}\,e^x\,(\ln\cos x-\tan x)$.

### d) $f(x)=\sqrt[x]{x}=x^{1/x}$

$\ln f=\dfrac{\ln x}{x}\Rightarrow\dfrac{f'}{f}=\dfrac{1-\ln x}{x^2}\Rightarrow f'=x^{1/x}\cdot\dfrac{1-\ln x}{x^2}$.

### e) $f(x)=2^{\operatorname{sen}x}+\sqrt{\operatorname{sen}(3x)}$

$f'=2^{\operatorname{sen}x}\ln2\cos x+\dfrac{3\cos(3x)}{2\sqrt{\operatorname{sen}(3x)}}$.

### f) $f(x)=(\operatorname{sen}x)^{x^2}+\pi e^x$

Para el primer término, $\ln u=x^2\ln\operatorname{sen}x\Rightarrow u'=(\operatorname{sen}x)^{x^2}\!\left(2x\ln\operatorname{sen}x+x^2\cot x\right)$.

$f'=(\operatorname{sen}x)^{x^2}\!\left(2x\ln\operatorname{sen}x+x^2\cot x\right)+\pi e^x$.

(El ejercicio 40 no figura en la lista oficial; resultados verificados con las reglas de derivación logarítmica.)

---

## Ejercicio 41* — Tangente a $y=(1-x)^{3/(x+1)}$ en $x=0$

**Enunciado.** Hallar la tangente en $x=0$.

$f(0)=(1)^{3}=1$. Derivación logarítmica: $\ln f=\dfrac{3}{x+1}\ln(1-x)$.



$$
\dfrac{f'}{f}=-\dfrac{3}{(x+1)^2}\ln(1-x)+\dfrac{3}{x+1}\cdot\dfrac{-1}{1-x}.
$$



En $x=0$: $\dfrac{f'(0)}{f(0)}=-3\ln1+3\cdot(-1)=-3$, y como $f(0)=1$, $f'(0)=-3$.

Tangente: $y-1=-3(x-0)\Rightarrow y=-3x+1$.

**$y=-3x+1$.**

✓ Coincide con la respuesta oficial.

---

## Ejercicio 42 — Verdadero / Falso

**Enunciado.** Decidir si cada afirmación es verdadera o falsa, justificando.

| Ítem | Afirmación | V/F | Justificación |
|------|------------|-----|---------------|
| a | continua en $a\Rightarrow$ derivable en $a$ | **F** | Contraejemplo: $\lvert x\rvert$ es continua en $0$ pero no derivable |
| b | tangente a $y=x^2$ en $(-2,4)$ es $y-4=2x(x+2)$ | **F** | La pendiente es $f'(-2)=-4$, no $2x$; la tangente es $y-4=-4(x+2)$ |
| c | si $f'(r)$ existe entonces $\lim_{x\to r}f=f(r)$ | **V** | Derivable $\Rightarrow$ continua |
| d | la tangente no puede cortar la curva en otro punto | **F** | Contraejemplo: la tangente a $y=x^3$ en $0$ es $y=0$ y la cruza ahí; muchas tangentes cortan la curva en otros puntos |
| e | $y=x+c\Rightarrow dy=dx$ | **V** | $dy=y'\,dx=1\cdot dx=dx$ |
| f | $f'=g'\Rightarrow f=g$ | **F** | Difieren en una constante: $f=g+C$ |
| g | $g(x)=\lvert x^2+x\rvert\Rightarrow g'(x)=\lvert2x+1\rvert$ | **F** | La derivada del valor absoluto no es el valor absoluto de la derivada |
| h | $y=ax+b\Rightarrow\dfrac{\Delta y}{\Delta x}=\dfrac{dy}{dx}$ | **V** | En una recta la razón incremental es constante e igual a la derivada |
| i | $y=\pi^5\Rightarrow y'=5\pi^4$ | **F** | $\pi^5$ es constante, $y'=0$ |
| j | pendiente de tangente a $f$ en $(1,2)$ es $4\Rightarrow$ a $f^{-1}$ en $(2,1)$ es $1/4$ | **V** | $(f^{-1})'(2)=\dfrac{1}{f'(1)}=\dfrac14$ |
| k | $f'(a)$ existe $\Rightarrow f'$ continua en $a$ | **F** | Contraejemplo: Ejercicio 24, derivable con derivada discontinua |
| l | $\dfrac{f(x)-f(a)}{x-a}$ es la pendiente de la secante | **V** | Es la definición de pendiente de secante |
| m | $f$ creciente derivable, $\Delta x>0\Rightarrow\Delta y\ge dy$ | **F** | Depende de la concavidad; si $f$ es cóncava hacia abajo, $\Delta y<dy$ |

**Verdaderas: c, e, h, j, k... ¡revisar!**

> ⚠️ **Discrepancia:** La respuesta oficial lista **k como Verdadera**, pero el análisis muestra que es **Falsa**.
>
> El ítem k afirma "si $f'(a)$ existe entonces $f'$ es continua en $a$". El **Ejercicio 24** de esta misma práctica es el contraejemplo clásico: $f(x)=x^2\operatorname{sen}(1/x)$ es derivable en $0$ ($f'(0)=0$) pero $f'$ NO es continua en $0$. Por lo tanto k es **Falsa**. Resultado calculado: k = Falsa. Respuesta del documento: k = Verdadera.

**Verdaderas: c, e, h, j, l. Falsas: a, b, d, f, g, i, k, m.**

> ⚠️ **Discrepancia (resumen del ejercicio):** Resultado calculado: Verdaderas $\{c,e,h,j,l\}$, Falsas $\{a,b,d,f,g,i,k,m\}$. Respuesta del documento: Verdaderas $\{c,e,h,j,k,l\}$, Falsas $\{a,b,d,f,g,i,m\}$. La única diferencia es el ítem **k**, que debe ser Falsa por el contraejemplo del Ejercicio 24.

---

## Ejercicios adicionales

### Adicional 1 — $H(t)=15\ln(t+1)$

**Enunciado.** a) Tasa instantánea de cambio en $t=3$. b) Para qué $t$ la tasa es $2$ (unidades/h por semana).

$H'(t)=\dfrac{15}{t+1}$.

a) $H'(3)=\dfrac{15}{4}=3{,}75$.

b) $\dfrac{15}{t+1}=2\Rightarrow t+1=7{,}5\Rightarrow t=6{,}5$.

**a) $3{,}75$; b) $t=6{,}5$.**

### Adicional 2 — $x^2y+y^2-4x=0$, tangentes verticales

**Enunciado.** Hallar los puntos con tangente vertical.

Derivando: $2xy+x^2y'+2yy'-4=0\Rightarrow y'(x^2+2y)=4-2xy\Rightarrow y'=\dfrac{4-2xy}{x^2+2y}$.

Tangente vertical: $x^2+2y=0\Rightarrow y=-\dfrac{x^2}{2}$. Sustituyendo en la curva: $x^2\left(-\tfrac{x^2}{2}\right)+\dfrac{x^4}{4}-4x=0\Rightarrow-\dfrac{x^4}{2}+\dfrac{x^4}{4}-4x=0\Rightarrow-\dfrac{x^4}{4}-4x=0$.

$-x\left(\dfrac{x^3}{4}+4\right)=0\Rightarrow x=0$ o $x^3=-16\Rightarrow x=-\sqrt[3]{16}=-2\sqrt[3]{2}$.

Para $x=0$: $y=0$, pero hay que verificar que el numerador no se anule también: en $(0,0)$ numerador $=4\neq0$, válido $\Rightarrow$ tangente vertical en $(0,0)$. Para $x=-2\sqrt[3]{2}$: $y=-\dfrac{(2\sqrt[3]{2})^2}{2}=-\dfrac{4\sqrt[3]{4}}{2}=-2\sqrt[3]{4}$.

**Puntos: $(0,0)$ y $\left(-2\sqrt[3]{2},\,-2\sqrt[3]{4}\right)$.**

### Adicional 3 — $h(x)=f(x^3-7)\cdot\dfrac{x^2}{e^{x-2}}$

**Enunciado.** Tangente a $f$ en $x=1$ es $y+2x=7$ (o sea $y=-2x+7$). Hallar $h'(2)$.

De la tangente: $f(1)=-2(1)+7=5$, $f'(1)=-2$.

Sea $u(x)=f(x^3-7)$ y $v(x)=\dfrac{x^2}{e^{x-2}}=x^2e^{2-x}$. En $x=2$: $x^3-7=1$.

$u(2)=f(1)=5$. $u'(x)=f'(x^3-7)\cdot3x^2$, $u'(2)=f'(1)\cdot12=-24$.

$v(2)=4e^0=4$. $v'(x)=2xe^{2-x}+x^2e^{2-x}(-1)=e^{2-x}(2x-x^2)$, $v'(2)=e^0(4-4)=0$.

$h'(2)=u'(2)v(2)+u(2)v'(2)=(-24)(4)+5(0)=-96$.

**$h'(2)=-96$.**

### Adicional 4 — $h(x)=(x+1)^{x^2+x}$, tangente horizontal en $x=0$

**Enunciado.** Mostrar que tiene tangente horizontal en $x=0$ y dar su ecuación.

$h(0)=(1)^0=1$. Derivación logarítmica: $\ln h=(x^2+x)\ln(x+1)$.



$$
\dfrac{h'}{h}=(2x+1)\ln(x+1)+(x^2+x)\cdot\dfrac{1}{x+1}=(2x+1)\ln(x+1)+x.
$$



En $x=0$: $\dfrac{h'(0)}{h(0)}=1\cdot\ln1+0=0\Rightarrow h'(0)=0$. **Tangente horizontal**; su ecuación es $y=h(0)=1$, es decir $y=1$.

### Adicional 5 (opción) — $h=f\circ g^{-1}$

**Enunciado.** $g$ tiene tangente $y=-2x+5$ en $x=1$.

De la tangente: $g(1)=3$, $g'(1)=-2$. Entonces $g^{-1}(3)=1$ y $(g^{-1})'(3)=\dfrac{1}{g'(1)}=-\dfrac12$. Si además se conoce $f$, por la cadena $h'(3)=f'(g^{-1}(3))\cdot(g^{-1})'(3)=-\dfrac12 f'(1)$. (Sin datos de $f$ queda en función de $f'(1)$.)

### Adicional 6 (opción) — $a$ para tangente vertical en $x=-2$ de $ax^2-3xy-y^2=21$

Tangente vertical: $\dfrac{dy}{dx}\to\infty$. Derivando: $2ax-3y-3xy'-2yy'=0\Rightarrow y'=\dfrac{2ax-3y}{3x+2y}$. Vertical $\Leftrightarrow3x+2y=0\Rightarrow y=-\dfrac{3x}{2}$. En $x=-2$: $y=3$. Sustituyendo en la curva: $a(4)-3(-2)(3)-9=21\Rightarrow4a+18-9=21\Rightarrow4a=12\Rightarrow a=3$.

**$a=3$, con punto de tangencia $(-2,3)$.**

### Adicional 7 (opción) — Qué NO se puede asegurar si $g$ es derivable en $a$

Si $g$ es derivable en $a$, se asegura que $g$ es continua en $a$ y que $g'(a)$ existe, **pero NO se puede asegurar que $\lim_{x\to a}g'(x)=g'(a)$** (es decir, que $g'$ sea continua en $a$). Contraejemplo: el Ejercicio 24.

### Adicional 8 (opción) — $(g^{-1})'$

Por la fórmula general, $(g^{-1})'(y)=\dfrac{1}{g'(g^{-1}(y))}$, válida cuando $g'(g^{-1}(y))\neq0$.

### Adicional 9 (opción) — Recta normal a $u(x)$

La normal en $(a,u(a))$ tiene pendiente $-\dfrac{1}{u'(a)}$ (si $u'(a)\neq0$) y ecuación $y-u(a)=-\dfrac{1}{u'(a)}(x-a)$. Si $u'(a)=0$ la normal es vertical: $x=a$.

---

## Resumen de discrepancias

Durante la resolución se detectaron **2 discrepancias** con las respuestas oficiales:

1. **Ejercicio 6e:** la respuesta oficial escribe $3\sqrt5\,x^2$ para la derivada de $\sqrt{5x^3}$; lo correcto es $\dfrac{3\sqrt5}{2}\sqrt{x}$.
2. **Ejercicio 42k:** la respuesta oficial la marca Verdadera; el análisis (y el propio Ejercicio 24) muestra que es **Falsa**.
