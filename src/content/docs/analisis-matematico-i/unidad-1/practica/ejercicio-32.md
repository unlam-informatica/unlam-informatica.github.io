---
title: Ejercicio 32 — Verdadero o Falso (justificar)
slug: analisis-matematico-i/unidad-1/practica/ejercicio-32
sidebar:
  order: 32
  label: Ejercicio 32
---


**a) Si $f(x)=mx+b$, entonces $\Delta y=m$ en intervalos de longitud $1$.** En una recta $\Delta y=m\,\Delta x$; con $\Delta x=1$, $\Delta y=m$. **Verdadero.** ✓

**b) Si la imagen consta de un solo número, su dominio también.** Una función constante $f(x)=k$ tiene imagen $\lbrace k\rbrace $ pero dominio $\mathbb{R}$. **Falso.** ✓

**c) Si $f$ y $g$ tienen el mismo dominio, $f/g$ también.** Contraejemplo: $f=x+1$, $g=x-2$ (ambas con $D=\mathbb{R}$), pero $\dfrac fg$ excluye $x=2$, $D=\mathbb{R}-\lbrace 2\rbrace $. **Falso.** ✓

**d) Si $\cos s=\cos t$ entonces $s=t$.** El coseno no es inyectivo: $\cos0=\cos2\pi=1$ pero $0\neq2\pi$. **Falso.** ✓

**e) Si $f$ es biyectiva, entonces $f^{-1}(x)=\tfrac{1}{f(x)}$.** Confunde inversa con recíproco. Contraejemplo: $f(x)=2x$, $f^{-1}(x)=\tfrac x2\neq\tfrac{1}{2x}$. **Falso.** ✓

**f) Las rectas $ax+y=c$ y $ax-y=c$ son perpendiculares.** Pendientes $-a$ y $a$; son perpendiculares solo si $(-a)(a)=-1\Rightarrow a^2=1\Rightarrow a=\pm1$. No en general. **Falso.** ✓

**g) Si $x>0$, $(\ln x)^6=6\ln x$.** $(\ln x)^6$ es la potencia sexta; $6\ln x=\ln x^6$. Son distintas (p. ej. $x=e$: $1\neq6$). **Falso.** ✓

**h) Si $f(a)=f(b)\Rightarrow a=b$.** Eso solo vale para funciones inyectivas. Contraejemplo: $f(x)=x^2$, $f(-2)=f(2)$ pero $-2\neq2$. **Falso.** ✓

**i) Si $f$ es función, $f(ax)=af(x)$.** Solo vale para lineales homogéneas. Contraejemplo: $f=\operatorname{sen}$, $\operatorname{sen}(2x)\neq2\operatorname{sen}x$. **Falso.** ✓

**j) $f(x)=\sqrt{\dfrac{x+3}{2-5x}}$ y $g(x)=\dfrac{\sqrt{x+3}}{\sqrt{2-5x}}$ son iguales.** Estudiemos dominios. Para $f$: $\dfrac{x+3}{2-5x}\ge0\Rightarrow x\in\left[-3,\tfrac25\right)$. Para $g$: $x+3\ge0$ y $2-5x>0\Rightarrow x\ge-3$ y $x<\tfrac25\Rightarrow\left[-3,\tfrac25\right)$. Coinciden los dominios y, donde existen, los valores son iguales (ambos factores no negativos). **Verdadero.** ✓

**k) $f(x)=4+\ln(3-x)$ surge de $\ln x$ por: traslación 3 a la izquierda, reflexión respecto al eje $y$, traslación 4 arriba.** $\ln(3-x)=\ln(-(x-3))$: reflexión en $y$ y traslación; sumar $4$ desplaza arriba. La descripción es válida. **Verdadero.** ✓

**l) Toda función inyectiva es sobreyectiva.** Contraejemplo: $f:\mathbb{R}\to\mathbb{R}$, $f(x)=e^x$ es inyectiva pero su imagen es $(0,+\infty)\neq\mathbb{R}$. **Falso.** ✓

**Resultado: Verdaderas $\lbrace a,j,k\rbrace $; Falsas $\lbrace b,c,d,e,f,g,h,i,l\rbrace $.** ✓ Coincide con la respuesta oficial.

