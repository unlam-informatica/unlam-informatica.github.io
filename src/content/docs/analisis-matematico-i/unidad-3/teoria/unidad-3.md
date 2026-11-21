---
title: Unidad 3 — Resumen integrador
slug: analisis-matematico-i/unidad-3/teoria/unidad-3
sidebar:
  hidden: true
  label: Resumen integrador
---

:::tip[Cómo usar este resumen]
- **Antes de estudiar:** leelo de corrido para tener el mapa de la unidad, de la razón de cambio a la derivación logarítmica.
- **Después de estudiar:** usalo para repasar y conectar los temas.
- **Antes del segundo parcial:** identificá los temas principales y volvé a la lección de cada uno.

No reemplaza a las lecciones, que desarrollan cada tema con demostraciones, ejemplos resueltos, ejercicios y
autoevaluación:

1. [Razón de cambio y derivada](/analisis-matematico-i/unidad-3/teoria/razon-de-cambio-y-derivada/)
2. [La derivada como función](/analisis-matematico-i/unidad-3/teoria/derivada-como-funcion/)
3. [Reglas de derivación](/analisis-matematico-i/unidad-3/teoria/reglas-de-derivacion/)
4. [Regla de la cadena e inversa](/analisis-matematico-i/unidad-3/teoria/regla-de-la-cadena-e-inversa/)
5. [Derivación implícita y logarítmica](/analisis-matematico-i/unidad-3/teoria/implicita-y-logaritmica/)

La ruta completa de la unidad está en la [presentación](/analisis-matematico-i/unidad-3/).
:::






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

La **función derivada** $f' : D_{f'} \to \mathbb{R}$ asigna a cada $x$ el valor $f'(x)$.

Notaciones equivalentes:



$$
f'(x) = \frac{df}{dx} = y' = \frac{d}{dx}\bigl[f(x)\bigr]
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
f \text{ es derivable en } x_0 \iff f'_+(x_0) \text{ y } f'_-(x_0) \text{ existen, son finitas e iguales}
$$

En ese caso, $f'(x_0)$ es ese valor común. Si las laterales son infinitas (aunque sean iguales), $f$ no es derivable en $x_0$.



---

## 6. Continuidad y derivabilidad

**Teorema:** Si $f$ es derivable en $x_0$, entonces $f$ es continua en $x_0$.

**El recíproco es falso:** $f$ puede ser continua en $x_0$ sin ser derivable. Hay tres situaciones típicas: una **punta** (laterales finitas y distintas, como $\lvert x \rvert$ en $0$), una **tangente vertical** (laterales infinitas del mismo signo, como $\sqrt[3]{x}$ en $0$) y una **cúspide** (infinitas de signo opuesto, como $\sqrt[3]{x^2}$ en $0$). Detalle en [La derivada como función](/analisis-matematico-i/unidad-3/teoria/derivada-como-funcion/).

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
| $\operatorname{sen} x$ | $\cos x$ |
| $\cos x$ | $-\operatorname{sen} x$ |
| $\tan x$ | $\sec^2 x = \dfrac{1}{\cos^2 x}$ |
| $\cot x$ | $-\csc^2 x = -\dfrac{1}{\operatorname{sen}^2 x}$ |
| $\operatorname{arcsen} x$ | $\dfrac{1}{\sqrt{1-x^2}}$ |
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
| Cociente (con $g \neq 0$) | $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$ |

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



**Ejemplo:** si $h(x) = \operatorname{sen}(x^2)$, entonces $h'(x) = \cos(x^2) \cdot 2x$.

---

## 10. Derivada de la función inversa

Si $f$ es continua y estrictamente monótona en un intervalo, derivable en $x_0$ y $f'(x_0) \neq 0$, entonces su inversa $f^{-1}$ es derivable en $y = f(x_0)$ y vale (con $x_0 = f^{-1}(y)$):



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

**Ejemplo:** $y = x^{\operatorname{sen} x}$



$$
\ln y = \operatorname{sen} x \cdot \ln x
$$





$$
\frac{y'}{y} = \cos x \cdot \ln x + \frac{\operatorname{sen} x}{x}
$$





$$
y' = x^{\operatorname{sen} x}\!\left(\cos x \cdot \ln x + \frac{\operatorname{sen} x}{x}\right)
$$


