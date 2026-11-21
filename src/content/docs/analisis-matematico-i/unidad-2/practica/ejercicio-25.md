---
title: Ejercicio 25 — Asíntotas con parámetros
slug: analisis-matematico-i/unidad-2/practica/ejercicio-25
sidebar:
  order: 25
  label: Ejercicio 25
---


## 25a
$f(x)=\dfrac{x^2-2}{ax+b}$, $y=\tfrac12x-4$ asíntota; hallar $a,b,k$

Para AO $y=mx+n$ de un cociente con numerador grado $2$ y denominador grado $1$, hacemos la división:



$$
\dfrac{x^2-2}{ax+b}=\dfrac{1}{a}x-\dfrac{b}{a^2}+\dfrac{\text{resto}}{ax+b}
$$



El coeficiente angular es $\dfrac{1}{a}=\dfrac12\Rightarrow a=2$. El término independiente: $-\dfrac{b}{a^2}=-\dfrac{b}{4}=-4\Rightarrow b=16$.

El valor $k$ es el punto que se excluye del dominio $\mathbb{R}-\lbrace k\rbrace$: el que anula el denominador $ax+b=2x+16$, es decir $k=-\dfrac{b}{a}=-8$. (Con esos valores, $\dfrac{x^2-2}{2x+16}=\dfrac{x}{2}-4+\dfrac{31}{x+8}$, y la recta $y=\tfrac12x-4$ es asíntota oblicua; además $x=-8$ es asíntota vertical.)



$$
\boxed{a=2,\quad b=16,\quad k=-8.}
$$



✓ Coincide con la respuesta oficial.

## 25b
* $f(x)=\dfrac{x^3+x+a}{x^2+bx+c}$ y $g(x)=\dfrac{x^2+x-2}{x+1}$ con las mismas asíntotas

**Asíntotas de $g$:** $g(x)=\dfrac{(x+2)(x-1)}{x+1}$. División: $\dfrac{x^2+x-2}{x+1}=x-\dfrac{2}{x+1}$, luego AO $y=x$ y AV $x=-1$ (numerador $\neq0$ en $-1$).

**Para que $f$ tenga AV en $x=-1$:** el denominador debe anularse allí. Veamos qué exige además la AO $y=x$.

Dividiendo $\dfrac{x^3+x+a}{x^2+bx+c}$: el cociente comienza con $x-b$. Para AO $y=x$ se necesita el término independiente del cociente nulo, es decir $b=0$. Con $b=0$: denominador $x^2+c$, y AV $x=-1$ requiere $1+c=0\Rightarrow c=-1$, o sea $x^2-1=(x-1)(x+1)$, que da AV en $x=-1$ **y** $x=1$.

División $\dfrac{x^3+x+a}{x^2-1}=x+\dfrac{2x+a}{x^2-1}$, con residuo $\to0\Rightarrow$ AO $y=x$. Para que $f$ comparta **exactamente** las asíntotas de $g$ (AV $x=-1$, AO $y=x$) y se cancele la AV en $x=1$, el numerador debe anularse en $x=1$: $1+1+a=0\Rightarrow a=-2$.



$$
\boxed{a=-2,\quad b=0,\quad c=-1;\quad \text{AV: }x=-1,\ \text{AO: }y=x.}
$$



✓ Coincide con la respuesta oficial.

## 25c
(GeoGebra) $f(x)=\dfrac{ax^2+x}{bx^2-1}$: discusión de asíntotas

- **AH:** si $b\neq0$, grados iguales $\Rightarrow y=\dfrac{a}{b}$. Si $a=0$, $f=\dfrac{x}{bx^2-1}\Rightarrow$ AH $y=0$.
- **AV:** $bx^2-1=0\Rightarrow x=\pm\dfrac{1}{\sqrt{b}}$ si $b>0$ (dos AV); si $b<0$ no hay raíces reales (sin AV); si $b=0$ el denominador es la constante $-1$ y $f(x)=-ax^2-x$ es una parábola: sin asíntotas (solo si $a=0$, caso que el enunciado excluye, $f(x)=-x$ sería una recta).
- **Cancelaciones:** si el numerador $x(ax+1)$ comparte raíz con el denominador, esa AV se vuelve discontinuidad evitable. Eso ocurre exactamente cuando $b=a^2$: entonces $f(x)=\dfrac{x}{ax-1}$ para $x\neq-\frac1a$, y queda **una sola** AV, $x=\frac1a$. Por ejemplo, $a=b=1$ da $f(x)=\frac{x}{x-1}$ con hueco en $x=-1$.

:::caution[Diferencia con la respuesta oficial]
La respuesta oficial afirma que «no existe valor de $b$ para el cual tenga una sola AV». El caso $b=a^2$ es un contraejemplo. El resto de la respuesta oficial (dos AV si $b>0$, ninguna si $b\le0$, AH $y=\frac ab$ si $b\neq0$) coincide.
:::

Se grafican casos representativos en GeoGebra ($a,b>0$; $b<0$; $b=0$) para ilustrar.

