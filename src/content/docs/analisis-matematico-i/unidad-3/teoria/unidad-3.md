---
title: Unidad 3 — Derivada
slug: analisis-matematico-i/unidad-3/teoria/unidad-3
sidebar:
  order: 1
---




## Tabla de contenidos


1. TOC


---

## 1. Razón de cambio media

La **razón de cambio media** de $f$ en el intervalo $[x_0,\, x_0 + h]$ es:



$$
\frac{\Delta f}{\Delta x} = \frac{f(x_0 + h) - f(x_0)}{h}
$$



Geométricamente: pendiente de la **recta secante** que pasa por $(x_0,\, f(x_0))$ y $(x_0 + h,\, f(x_0 + h))$.

---

## 2. Derivada en un punto — razón de cambio instantánea

La **derivada de $f$ en $x_0$** es el límite de la razón de cambio media cuando $h \to 0$:



$$
f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
$$



Si este límite existe (y es finito), $f$ es **derivable en $x_0$**.

### Significado geométrico

$f'(x_0)$ es la **pendiente de la recta tangente** a la gráfica de $f$ en el punto $(x_0,\, f(x_0))$.

### Significado físico

Si $f(t)$ es la posición de un objeto en el instante $t$, entonces $f'(t_0)$ es la **velocidad instantánea** en $t_0$.

---

## 3. La derivada como función

La **función derivada** $f' : \text{Dom}\, f' \to \mathbb{R}$ asigna a cada $x$ el valor $f'(x)$.

Notaciones equivalentes:



$$
f'(x) = \frac{df}{dx} = y' = Df(x) = \frac{d}{dx}\bigl[f(x)\bigr]
$$



---

## 4. Recta tangente y recta normal

**Recta tangente** en $(x_0,\, f(x_0))$:



$$
y - f(x_0) = f'(x_0)\,(x - x_0)
$$



**Recta normal** (perpendicular a la tangente) en $(x_0,\, f(x_0))$:



$$
y - f(x_0) = -\frac{1}{f'(x_0)}\,(x - x_0) \qquad \bigl[f'(x_0) \neq 0\bigr]
$$



---

## 5. Derivadas laterales

- **Derivada por la derecha:** $\displaystyle f'_+(x_0) = \lim_{h \to 0^+} \frac{f(x_0+h)-f(x_0)}{h}$
- **Derivada por la izquierda:** $\displaystyle f'_-(x_0) = \lim_{h \to 0^-} \frac{f(x_0+h)-f(x_0)}{h}$



$$
f \text{ es derivable en } x_0 \iff f'_+(x_0) = f'_-(x_0) = f'(x_0)
$$



---

## 6. Continuidad y derivabilidad

**Teorema:** Si $f$ es derivable en $x_0$, entonces $f$ es continua en $x_0$.

**El recíproco es falso:** $f$ puede ser continua en $x_0$ sin ser derivable. Ejemplo: $f(x) = \lvert x \rvert$ en $x = 0$.

---

## 7. Derivadas de funciones elementales

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $c$ (constante) | $0$ |
| $x^n$ | $n\, x^{n-1}$ |
| $\sqrt{x}$ | $\dfrac{1}{2\sqrt{x}}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\dfrac{1}{x}$ |
| $\log_a x$ | $\dfrac{1}{x \ln a}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x = \dfrac{1}{\cos^2 x}$ |
| $\cot x$ | $-\csc^2 x = -\dfrac{1}{\sin^2 x}$ |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\dfrac{1}{1+x^2}$ |

---

## 8. Reglas de derivación

Sean $f$ y $g$ derivables y $c$ una constante:

| Regla | Fórmula |
|-------|---------|
| Constante por función | $(c \cdot f)' = c \cdot f'$ |
| Suma | $(f + g)' = f' + g'$ |
| Diferencia | $(f - g)' = f' - g'$ |
| Producto | $(f \cdot g)' = f' g + f g'$ |
| Cociente | $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$ |

---

## 9. Regla de la cadena (composición)

Si $h(x) = f(g(x))$, entonces:



$$
h'(x) = f'(g(x)) \cdot g'(x)
$$



**Notación de Leibniz:**



$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$



**Ejemplo:** si $h(x) = \sin(x^2)$, entonces $h'(x) = \cos(x^2) \cdot 2x$.

---

## 10. Derivada de la función inversa

Si $f$ es biyectiva y derivable, y $f^{-1}$ es su inversa:



$$
(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}
$$



Equivalentemente:



$$
\frac{dx}{dy} = \frac{1}{\;\dfrac{dy}{dx}\;}
$$



---

## 11. Derivada implícita

Cuando $y$ no se puede despejar explícitamente de $F(x, y) = 0$:

1. Derivar ambos lados respecto a $x$ (usando la regla de la cadena para los términos con $y$, tratando $y$ como función de $x$).
2. Despejar $\dfrac{dy}{dx}$.

**Ejemplo:** $x^2 + y^2 = 1$



$$
2x + 2y \frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}
$$



---

## 12. Derivación logarítmica

Técnica útil para funciones del tipo $f(x) = [u(x)]^{v(x)}$ o productos/cocientes complejos.

**Procedimiento:**
1. Tomar logaritmo natural: $\ln y = v(x) \cdot \ln(u(x))$
2. Derivar implícitamente: $\dfrac{y'}{y} = \ldots$
3. Despejar: $y' = y \cdot (\ldots)$

**Ejemplo:** $y = x^{\sin x}$



$$
\ln y = \sin x \cdot \ln x
$$





$$
\frac{y'}{y} = \cos x \cdot \ln x + \frac{\sin x}{x}
$$





$$
y' = x^{\sin x}\!\left(\cos x \cdot \ln x + \frac{\sin x}{x}\right)
$$


