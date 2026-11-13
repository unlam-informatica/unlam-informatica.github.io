---
title: GeoGebra para Derivada (Unidad 3)
slug: analisis-matematico-i/geogebra/derivada
sidebar:
  order: 4
---


Esta página cubre derivadas simbólicas, rectas tangentes, derivación implícita y optimización con GeoGebra.

## Derivada simbólica

```
Derivada(f)                # devuelve f'(x)
Derivada(f; n)             # derivada n-ésima
Derivada(f; x; n)          # alternativa explicitando la variable
```

**Ejemplo:**

```
f(x) = x^3 - 6x^2 + 9x - 2

Derivada(f)
# Devuelve: f'(x) = 3x^2 - 12x + 9

Derivada(f; 2)
# Devuelve: f''(x) = 6x - 12
```

Para verlo simbólicamente con todos los pasos, usar la **vista CAS**:

```
# En la celda 1 de CAS:
f(x) := x^3 - 6x^2 + 9x - 2

# Celda 2:
Derivada(f(x); x)
```

El operador `:=` define una expresión sin evaluarla (útil cuando se trabaja simbólicamente).

## Evaluar la derivada en un punto

Una vez definida `f`, también queda definida `f'` (notación con apóstrofe):

```
f(x) = x^2 + 3x

f'(2)         # devuelve 2*2 + 3 = 7

# Equivalente:
Derivada(f)(2)
```

## Recta tangente

```
Tangente(<punto>; <función>)
Tangente(<x>; <función>)        # tangente en x = <valor>
```

**Ejemplo:**

```
f(x) = sin(x)
t = Tangente(pi/4; f)
# Devuelve: y = (sqrt(2)/2) x + sqrt(2)/2 (1 - pi/4)
```

GeoGebra grafica automáticamente la recta tangente. Combinado con un deslizador, se puede animar:

```
a = 0                          # deslizador con rango (-3; 3)
P = (a; f(a))                  # punto sobre la curva
t = Tangente(a; f)             # tangente animada
```

Al mover el deslizador `a`, el punto $P$ recorre la curva y la tangente se actualiza. **Muy útil para visualizar cómo varía la pendiente** y entender la relación entre la curva y su derivada.

## Recta normal

La normal en un punto es perpendicular a la tangente.

```
Perpendicular(<punto>; <tangente>)
```

O directamente con la pendiente:

```
n(x) = -1/f'(a) (x - a) + f(a)
```

## Derivación implícita

Para una curva dada por una ecuación implícita $F(x,y)=0$:

```
c: x^2 + y^2 = 25              # circunferencia (curva implícita)
DerivadaImplícita(c)
# Devuelve: -x/y
```

**Importante:** el resultado se interpreta como $\dfrac{dy}{dx}$. Para evaluar en un punto $(x_0, y_0)$, sustituir manualmente o usar:

```
DerivadaImplícita(c)(3; 4)     # da -3/4 → pendiente de la tangente en (3,4)
```

## Derivación logarítmica

GeoGebra no tiene un comando específico para derivación logarítmica, pero la podés hacer paso a paso en la **vista CAS**:

```
# Definir
f(x) := x^x

# Tomar logaritmo
g(x) := ln(f(x))         # → x ln(x)

# Derivar
Derivada(g(x); x)         # → ln(x) + 1

# Y multiplicar por f(x)
f(x) * (ln(x) + 1)
```

El resultado $f'(x) = x^x (\ln x + 1)$ coincide con la derivada directa que también GeoGebra calcula: `Derivada(x^x; x)`.

## Optimización: máximos y mínimos

### Locales

```
Extremo(f)                    # todos los extremos relativos
Extremo(f; a; b)              # extremos relativos en [a,b]
```

### Absolutos en un intervalo

```
Máximo(f; a; b)               # devuelve el x donde se alcanza el máximo
Mínimo(f; a; b)               # devuelve el x donde se alcanza el mínimo
```

**Ejemplo: caja sin tapa (Ej. 6 de la práctica)**

```
V(x) = x (24 - 2x) (32 - 2x)
Extremo(V; 0; 12)
# Devuelve aproximadamente (4.53; 1552.5)
# x ≈ 4.53 cm da el volumen máximo
```

### Inflexiones

```
PuntoInflexión(f)             # puntos donde f'' cambia de signo
```

## Análisis completo de una función

Combinando todo:

```
f(x) = (x - 1)^3 / (x + 2)

# Dominio (manualmente: x ≠ -2)
# Asíntotas:
Asíntota(f)

# Raíces (cortes con eje x):
Raíz(f)

# Corte con eje y:
f(0)

# Extremos:
Extremo(f)

# Derivada (para signo y crecimiento):
g(x) = Derivada(f)
Raíz(g)                       # candidatos a extremo

# Segunda derivada (para concavidad):
h(x) = Derivada(f; 2)
Raíz(h)                       # candidatos a inflexión
```

## Comparar $f$, $f'$ y $f''$

Estrategia útil para entender la información geométrica de las derivadas:

```
f(x) = x^3 - 3x
g(x) = Derivada(f)
h(x) = Derivada(f; 2)
```

Graficar las tres simultáneamente y observar:

- Donde $g(x)=0$, $f$ tiene extremo relativo.
- Donde $g(x)>0$, $f$ es creciente; donde $g(x)<0$, decreciente.
- Donde $h(x)=0$, $f$ tiene punto de inflexión.
- Donde $h(x)>0$, $f$ es cóncava hacia arriba; donde $h(x)<0$, cóncava hacia abajo.

## Movimiento rectilíneo (problemas de razón de cambio)

Si $s(t)$ es la posición en función del tiempo:

```
s(t) = -5t^2 + 10t + 40       # posición (Ej. 24 — caída)
v(t) = Derivada(s)             # velocidad
a(t) = Derivada(s; 2)          # aceleración
```

## Comandos resumidos

| Comando | Para qué |
|---------|----------|
| `Derivada(f)` | $f'(x)$ |
| `Derivada(f; n)` | $f^{(n)}(x)$ |
| `f'(a)` | Valor de la derivada en $a$ (notación corta) |
| `Tangente(a; f)` | Recta tangente en $x=a$ |
| `Tangente(P; f)` | Recta tangente en el punto $P$ |
| `Perpendicular(P; t)` | Recta perpendicular a $t$ por $P$ (normal) |
| `DerivadaImplícita(c)` | $dy/dx$ para una curva implícita |
| `Extremo(f; a; b)` | Extremos relativos en $[a,b]$ |
| `Máximo(f; a; b)` | Máximo absoluto en $[a,b]$ |
| `Mínimo(f; a; b)` | Mínimo absoluto en $[a,b]$ |
| `PuntoInflexión(f)` | Puntos de inflexión |
| `Raíz(f)` | Raíces (para combinar con $f'$) |

