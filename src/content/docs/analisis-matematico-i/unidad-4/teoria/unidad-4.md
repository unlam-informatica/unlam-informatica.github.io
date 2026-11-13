---
title: Unidad 4 — Polinomios de Taylor
slug: analisis-matematico-i/unidad-4/teoria/unidad-4
sidebar:
  order: 1
---




## Tabla de contenidos


1. TOC


---

## 1. Órdenes de contacto entre dos curvas

Dos funciones $f$ y $g$ tienen **contacto de orden $n$** en $x = a$ si:



$$
f(a) = g(a),\quad f'(a) = g'(a),\quad \ldots,\quad f^{(n)}(a) = g^{(n)}(a)
$$



pero $f^{(n+1)}(a) \neq g^{(n+1)}(a)$.

**Equivalentemente:**



$$
\lim_{x \to a} \frac{f(x) - g(x)}{(x-a)^n} = 0 \qquad \text{y} \qquad \lim_{x \to a} \frac{f(x) - g(x)}{(x-a)^{n+1}} \neq 0
$$



Cuanto mayor el orden de contacto, mejor se "ajustan" las dos curvas cerca de $x = a$.

---

## 2. Expresión de un polinomio por sus derivadas

Un polinomio $P(x)$ de grado $n$ puede escribirse en función de sus derivadas en $x = a$:



$$
P(x) = P(a) + P'(a)(x-a) + \frac{P''(a)}{2!}(x-a)^2 + \cdots + \frac{P^{(n)}(a)}{n!}(x-a)^n
$$



Esta es la base de la construcción del polinomio de Taylor.

---

## 3. Polinomio de Taylor

El **polinomio de Taylor de orden $n$ de $f$ en $x = a$** es el único polinomio de grado $\leq n$ que tiene contacto de orden $n$ con $f$ en $x = a$:



$$
\boxed{P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k}
$$



Desarrollado:



$$
P_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n
$$



**Requisito:** $f$ debe ser $n$ veces derivable en $x = a$.

### Polinomios de Maclaurin de funciones comunes

| Función | Polinomio de Taylor en $x = 0$ |
|---------|--------------------------------|
| $e^x$ | $1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \cdots + \dfrac{x^n}{n!}$ |
| $\sin x$ | $x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \cdots$ |
| $\cos x$ | $1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \cdots$ |
| $\ln(1+x)$ | $x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \cdots$ |
| $\dfrac{1}{1-x}$ | $1 + x + x^2 + x^3 + \cdots + x^n$ |
| $(1+x)^\alpha$ | $1 + \alpha x + \dfrac{\alpha(\alpha-1)}{2!}x^2 + \cdots$ |

---

## 4. Polinomio de Maclaurin

Es el caso particular de Taylor con **$a = 0$**:



$$
P_n(x) = f(0) + f'(0)\,x + \frac{f''(0)}{2!}\,x^2 + \cdots + \frac{f^{(n)}(0)}{n!}\,x^n
$$



---

## 5. Aproximación lineal

El polinomio de Taylor de **orden 1** en $x = a$ es la **recta tangente**:



$$
P_1(x) = f(a) + f'(a)(x - a)
$$



**Uso práctico:** para $x \approx a$, se puede aproximar $f(x) \approx f(a) + f'(a)(x - a)$.

Aproximaciones de primer orden para $x \approx 0$:



$$
\sin x \approx x \qquad \cos x \approx 1 \qquad e^x \approx 1 + x
$$





$$
\ln(1+x) \approx x \qquad (1+x)^\alpha \approx 1 + \alpha x
$$



---

## 6. Término complementario (resto de Taylor)

La diferencia entre $f(x)$ y su polinomio de Taylor $P_n(x)$ se llama **resto** o **término complementario**:



$$
R_n(x) = f(x) - P_n(x)
$$



### Forma de Lagrange

Si $f$ es $(n+1)$ veces derivable en un intervalo que contiene a $a$ y $x$, existe $c$ entre $a$ y $x$ tal que:



$$
\boxed{R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}}
$$



### Estimación del error

Para acotar el error de aproximación:



$$
\lvert R_n(x) \rvert \leq \frac{M}{(n+1)!}\,\lvert x - a \rvert^{n+1}
$$



donde $M$ es una cota de $\lvert f^{(n+1)} \rvert$ en el intervalo considerado.

**Uso:** dado un error máximo tolerable $\varepsilon$, se puede determinar qué orden $n$ de polinomio garantiza $\lvert R_n(x) \rvert < \varepsilon$.
