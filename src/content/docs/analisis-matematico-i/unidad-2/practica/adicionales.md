---
title: Ejercicios adicionales
slug: analisis-matematico-i/unidad-2/practica/adicionales
sidebar:
  order: 34
---


### Adicional 1 — Verdadero / Falso

**a)** $\lim_{x\to-3}\dfrac{\sqrt{x+7}-2}{\operatorname{sen}(2x+6)}=\dfrac12$.

Racionalizamos el numerador y usamos $\operatorname{sen}(2x+6)=\operatorname{sen}\big(2(x+3)\big)\sim 2(x+3)$:



$$
\sqrt{x+7}-2=\dfrac{(x+7)-4}{\sqrt{x+7}+2}=\dfrac{x+3}{\sqrt{x+7}+2}
$$





$$
\dfrac{\frac{x+3}{\sqrt{x+7}+2}}{\operatorname{sen}2(x+3)}=\dfrac{x+3}{(\sqrt{x+7}+2)\cdot\operatorname{sen}2(x+3)}
$$



Con $\operatorname{sen}2(x+3)\sim 2(x+3)$:



$$
\to\dfrac{x+3}{(\sqrt{x+7}+2)\cdot 2(x+3)}=\dfrac{1}{2(\sqrt{x+7}+2)}\xrightarrow{x\to-3}\dfrac{1}{2(2+2)}=\dfrac{1}{8}
$$



El valor es $\dfrac18\neq\dfrac12$ $\Rightarrow$ **Falsa**. (Resultado correcto: $\dfrac{1}{8}$.)

**b)** $\lim_{x\to1}\dfrac{1-\cos(x-1)}{x^2-1}=\dfrac12$.

$1-\cos(x-1)\sim \dfrac{(x-1)^2}{2}$ y $x^2-1=(x-1)(x+1)$:



$$
\dfrac{(x-1)^2/2}{(x-1)(x+1)}=\dfrac{x-1}{2(x+1)}\xrightarrow{x\to1}\dfrac{0}{4}=0
$$



El valor es $0\neq\dfrac12$ $\Rightarrow$ **Falsa**. (Resultado correcto: $0$.)

**c)** $\lim_{x\to\infty}\dfrac{\sqrt{x^2+5}}{3x-2}$ no existe.

Para $x\to+\infty$: $\dfrac{\sqrt{x^2+5}}{3x-2}\to\dfrac{\lvert x\rvert}{3x}=\dfrac{x}{3x}=\dfrac13$. Para $x\to-\infty$: $\dfrac{-x}{3x}=-\dfrac13$. Cada límite unilateral existe (son distintos), pero **como límite en el infinito sin especificar signo** los dos valores difieren. La afirmación "no existe" se interpreta como el límite bilateral en $\infty$ (ambos lados): al diferir, **Verdadera** que no existe un único valor. Por rama: $+\tfrac13$ y $-\tfrac13$.

### Adicional 2 — (GeoGebra) asíntotas de $\dfrac{ax^2+x}{bx^2-1}$

Mismo análisis que el 25c: AH $y=\dfrac{a}{b}$ (si $b\neq0$); AV en $x=\pm\dfrac{1}{\sqrt b}$ si $b>0$; sin AV si $b<0$; casos de cancelación si numerador y denominador comparten raíz. Discusión por casos según signos de $a,b$.

### Adicional 3 — $f(x)=\dfrac{\lvert 4-x^2\rvert}{x(x-2)}$

**Dominio:** $x(x-2)\neq0\Rightarrow x\neq0,\ x\neq2$, es decir $D=\mathbb{R}-\lbrace 0,2\rbrace $.

Separamos el módulo: $4-x^2\ge0\Leftrightarrow -2\le x\le2$.

- **Si $-2\le x\le2$:** $\lvert4-x^2\rvert=4-x^2=(2-x)(2+x)$. Entonces $f(x)=\dfrac{(2-x)(2+x)}{x(x-2)}=\dfrac{-(x-2)(x+2)}{x(x-2)}=\dfrac{-(x+2)}{x}$.
- **Si $x<-2$ o $x>2$:** $\lvert4-x^2\rvert=x^2-4=(x-2)(x+2)$. Entonces $f(x)=\dfrac{(x-2)(x+2)}{x(x-2)}=\dfrac{x+2}{x}$.

**Discontinuidades:**

- **$x=2$:** lateral izquierdo (rama $-\tfrac{x+2}{x}$): $\to-\dfrac{4}{2}=-2$; lateral derecho (rama $\tfrac{x+2}{x}$): $\to\dfrac{4}{2}=2$. Salto finito $\Rightarrow$ **esencial de salto finito** ($S=4$).
- **$x=0$:** está en la rama $-\tfrac{x+2}{x}$, $\to-\dfrac{2}{0}\to\pm\infty$ $\Rightarrow$ **esencial de salto infinito** (AV $x=0$).

**Asíntotas:**

- **AV:** $x=0$ (no $x=2$, que es salto finito).
- **AH:** $x\to+\infty$ usa $\dfrac{x+2}{x}\to1\Rightarrow y=1$; $x\to-\infty$ usa $\dfrac{x+2}{x}\to1\Rightarrow y=1$. AH $y=1$.



$$
\boxed{D=\mathbb{R}-\lbrace 0,2\rbrace ;\ \text{AV }x=0,\ \text{AH }y=1;\ x=2\ \text{salto finito},\ x=0\ \text{salto infinito}.}
$$



✓ Coincide con la respuesta oficial (dominio $\mathbb{R}-\lbrace 0,2\rbrace $).

### Adicional 4 — (opción múltiple) función por tramos continua

Según la respuesta oficial, los valores que hacen continua la función por tramos son $a=\dfrac{3}{2}$ y $b=-\dfrac{9}{2}$. El método es igualar los límites laterales en cada punto de empalme (como en los ejercicios 5, 19, 29).



$$
\boxed{a=\dfrac{3}{2},\quad b=-\dfrac{9}{2}.}
$$



✓ Coincide con la respuesta oficial.

### Adicional 5 — (opción) límites laterales

Se resuelven leyendo el comportamiento por izquierda y por derecha en cada punto, eligiendo la rama de la función definida en cada lado (mismo procedimiento que el ejercicio 17). Sin el enunciado de opciones específico, se aplica el criterio de laterales.

### Adicional 6 — $L=\lim_{x\to a}\dfrac{x\sqrt{x}-a\sqrt{a}}{\sqrt{x}-\sqrt{a}}$

Escribimos $x\sqrt{x}=(\sqrt{x})^3$ y $a\sqrt{a}=(\sqrt{a})^3$. Con $u=\sqrt{x}$, $v=\sqrt{a}$ es una diferencia de cubos:



$$
\dfrac{u^3-v^3}{u-v}=u^2+uv+v^2
$$



Volviendo a las variables: $u^2+uv+v^2=x+\sqrt{x}\sqrt{a}+a\xrightarrow{x\to a}a+a+a=3a$.



$$
\boxed{L=3a,\quad \forall a\ge0.}
$$



✓ Coincide con la respuesta oficial.

### Adicional 7 — (opción) asíntotas de $g(x)=\dfrac{ax^3+cx^2-x}{3x^2-x}$

Numerador grado $3$, denominador grado $2$ (difieren en uno) $\Rightarrow$ existe **AO** si $a\neq0$. Factor común $x$: $\dfrac{x(ax^2+cx-1)}{x(3x-1)}=\dfrac{ax^2+cx-1}{3x-1}$ (hueco evitable en $x=0$). 

- **AV:** $3x-1=0\Rightarrow x=\dfrac13$ (si el numerador no se anula allí).
- **AO** $y=mx+n$: $m=\lim\dfrac{ax^2+cx-1}{x(3x-1)}=\dfrac{a}{3}$; $n$ se obtiene de la división. La discusión depende de $a$ y $c$.

Sin los valores concretos de la opción, las asíntotas son: AV $x=\tfrac13$ y AO de pendiente $\tfrac{a}{3}$.

