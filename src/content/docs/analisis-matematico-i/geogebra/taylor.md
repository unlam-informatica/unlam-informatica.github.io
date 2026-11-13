---
title: GeoGebra para Polinomio de Taylor (Unidad 4)
slug: analisis-matematico-i/geogebra/taylor
sidebar:
  order: 5
---


GeoGebra tiene un comando dedicado para Taylor que evita el cálculo manual de derivadas sucesivas y la suma de términos.

## Polinomio de Taylor

```
PolinomioTaylor(<función>; <a>; <n>)
```

donde:

- `<función>` es la función $f$ a aproximar.
- `<a>` es el centro del desarrollo (el "punto base").
- `<n>` es el orden del polinomio.

**Ejemplo:**

```
f(x) = e^x
T2 = PolinomioTaylor(f; 0; 2)
# Devuelve: 1 + x + x^2/2
```

Este es el polinomio de **Maclaurin** (Taylor centrado en $a=0$) de orden 2 para $e^x$. Coincide con $1 + x + \dfrac{x^2}{2}$ como esperábamos.

## Polinomio de Maclaurin

Es el caso particular de Taylor con $a=0$:

```
M3 = PolinomioTaylor(sin(x); 0; 5)
# Devuelve: x - x^3/6 + x^5/120
```

Notar que en $\sin x$ solo aparecen potencias impares, así que orden 5 incluye los términos $x$, $x^3$, $x^5$.

## Aproximación lineal

La aproximación lineal de $f$ en torno a $a$ es el polinomio de Taylor de orden 1:

```
L = PolinomioTaylor(f; a; 1)
```

equivale a la **recta tangente** en $x=a$:

```
L = Tangente(a; f)
```

Ambos comandos devuelven la misma recta.

## Comparar $f$ con su polinomio de Taylor

Una visualización muy útil es graficar la función junto con varios polinomios de Taylor de distintos órdenes para ver cómo se aproxima mejor al aumentar el orden:

```
f(x) = sin(x)
T1 = PolinomioTaylor(f; 0; 1)         # x
T3 = PolinomioTaylor(f; 0; 3)         # x - x^3/6
T5 = PolinomioTaylor(f; 0; 5)         # x - x^3/6 + x^5/120
T7 = PolinomioTaylor(f; 0; 7)         # añade término en x^7
```

Graficados todos juntos, se observa cómo $T_1$ solo coincide con $\sin x$ cerca de $0$, mientras que $T_7$ aproxima bien en un intervalo más amplio.

## Animar el orden con un deslizador

```
n = 1                                  # deslizador entero, rango (1; 15) con paso 1
T(x) = PolinomioTaylor(sin(x); 0; n)
```

Mover el deslizador `n` muestra cómo el polinomio mejora su aproximación al aumentar el orden. Excelente para entender visualmente la convergencia.

## Calcular el resto

El **resto** o **error de Taylor** es la diferencia entre la función y su polinomio:

```
f(x) = e^x
T = PolinomioTaylor(f; 0; 3)
R(x) = f(x) - T(x)
```

Graficar $R$ permite ver el tamaño del error en función de $x$: cerca de $a=0$ es muy chico, lejos crece.

Para acotar el resto teóricamente (fórmula de Lagrange), GeoGebra no tiene un comando directo, pero podés calcular la $(n+1)$-ésima derivada para acotarla en un intervalo:

```
g(x) = Derivada(f; 4)               # f^(4) para resto de T3
Máximo(abs(g); 0; 1)                # cota de |f^(4)| en [0,1]
```

## Aplicaciones típicas

### Aproximar un valor

Para estimar $\sin(0{,}5)$ usando Taylor:

```
T5 = PolinomioTaylor(sin(x); 0; 5)
T5(0.5)
# Devuelve ≈ 0.4794
sin(0.5)
# Devuelve ≈ 0.4794
```

Coinciden hasta 4 decimales, lo que confirma que $T_5$ aproxima bien a $\sin$ en $x=0{,}5$.

### Verificar la fórmula clásica

Para chequear que $e^x \approx 1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \cdots$:

```
PolinomioTaylor(e^x; 0; 5)
# Devuelve: 1 + x + x^2/2 + x^3/6 + x^4/24 + x^5/120
```

Coincide con la serie de Maclaurin de $e^x$ truncada.

### Comparar Taylor centrado en distintos puntos

Para una función con singularidad o cambio brusco, conviene centrar el polinomio cerca del punto de interés:

```
f(x) = ln(x)
T_en_1 = PolinomioTaylor(f; 1; 3)     # bueno para x cercanos a 1
T_en_e = PolinomioTaylor(f; e; 3)     # bueno para x cercanos a e
```

(Notar que $\ln$ no es analítica en $x=0$, así que **no existe** su Taylor en $0$.)

## Comandos resumidos

| Comando | Para qué |
|---------|----------|
| `PolinomioTaylor(f; a; n)` | Polinomio de Taylor de $f$ centrado en $a$, orden $n$ |
| `PolinomioTaylor(f; 0; n)` | Polinomio de Maclaurin de orden $n$ |
| `Tangente(a; f)` | Aproximación lineal (Taylor orden 1) |
| `Derivada(f; n)` | Útil para calcular $f^{(n)}$ y armar el resto |

