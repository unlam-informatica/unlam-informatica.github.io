---
title: GeoGebra para Límites y Continuidad (Unidad 2)
slug: analisis-matematico-i/geogebra/limites-continuidad
sidebar:
  order: 3
---


Esta página cubre los comandos de GeoGebra útiles para resolver ejercicios de límites, asíntotas y continuidad.

## Calcular un límite

El comando básico es `Límite(<función>; <punto>)`:

```
Límite(f; 3)               # límite de f(x) cuando x → 3
Límite(sin(x)/x; 0)        # devuelve 1
Límite((x^2 - 1)/(x - 1); 1)   # devuelve 2
```

Para límites al infinito, usar `infinito` (o el símbolo `∞`):

```
Límite(f; infinito)        # límite cuando x → +∞
Límite(f; -infinito)       # límite cuando x → -∞
```

El comando funciona tanto en la **vista Algebraica** como en la **CAS** — la diferencia es que la CAS devuelve resultados simbólicos exactos, mientras que la Algebraica los devuelve numéricos.

**Recomendación:** para límites simbólicos (con expresiones tipo $\frac{0}{0}$ que se simplifican algebraicamente), usar la **vista CAS**.

## Límites laterales

```
LímiteIzquierda(f; 0)      # x → 0⁻
LímiteDerecha(f; 0)        # x → 0⁺
```

Útiles cuando la función tiene comportamiento distinto a izquierda y derecha del punto (típico en funciones por tramos o con denominador que cambia de signo).

**Ejemplo: función racional con asíntota vertical**

```
f(x) = 1/(x - 2)
LímiteIzquierda(f; 2)      # devuelve -∞
LímiteDerecha(f; 2)        # devuelve +∞
```

## Detectar discontinuidades visualmente

Cuando la función tiene una **discontinuidad evitable** (hueco), GeoGebra la grafica como si fuera continua porque el hueco es un único punto que no es perceptible. Para marcar el hueco explícitamente:

```
f(x) = (x^2 - 4)/(x - 2)
P = (2; Límite(f; 2))       # punto donde está el hueco
# clic derecho en P → propiedades → marcar como círculo vacío
```

Para una **discontinuidad esencial** (asíntota vertical), GeoGebra suele dibujar una línea vertical artificial uniendo los dos extremos de la asíntota. Para limpiarla:

```
# Clic derecho en la función → Propiedades → Estilo → Cortar en discontinuidades
```

## Asíntotas

```
Asíntota(f)
```

Devuelve una **lista** con las asíntotas verticales y horizontales/oblicuas. Cada elemento es una ecuación que GeoGebra grafica automáticamente.

**Ejemplo:**

```
f(x) = (2x^2 + 3x - 1)/(x^2 - 1)
Asíntota(f)
# Devuelve: {x = -1, x = 1, y = 2}
```

Las dos primeras son verticales (raíces del denominador) y la tercera horizontal (cociente de coeficientes principales).

Para asíntota oblicua, GeoGebra la calcula sola cuando el grado del numerador supera en 1 al del denominador:

```
f(x) = (x^2 + 1)/(x - 1)
Asíntota(f)
# Devuelve: {x = 1, y = x + 1}   ← y = x + 1 es la oblicua
```

## Comprobar continuidad en un punto

Una función es continua en $x=a$ si:

1. $f(a)$ está definida.
2. $\lim_{x \to a} f(x)$ existe (límites laterales iguales y finitos).
3. $\lim_{x \to a} f(x) = f(a)$.

En GeoGebra, comprobar las tres condiciones:

```
f(x) = (x^2 - 4)/(x - 2)    # función a estudiar
a = 2                        # punto

f(a)                         # devuelve "?" → no definido (paso 1 falla)
Límite(f; a)                 # devuelve 4 (paso 2 OK)

# Conclusión: discontinuidad evitable en x=2.
# Para "remediarla", redefinir:
g(x) = Si(x ≠ 2; (x^2-4)/(x-2); 4)
# Ahora g es continua en todo R.
```

## Tipos de discontinuidad — diagnóstico rápido

| Comportamiento de los límites laterales | Tipo de discontinuidad |
|------------------------------------------|------------------------|
| Ambos iguales y finitos, pero $\neq f(a)$ o $f(a)$ no existe | **Evitable** (hay un valor $L$ que "completa" $f$) |
| Distintos pero ambos finitos | **De salto** finito |
| Al menos uno es infinito | **Esencial / infinita** (asíntota vertical) |
| Al menos uno no existe (oscilante) | **Esencial / oscilatoria** (tipo $\sin(1/x)$ en $x=0$) |


## Comparar dos funciones cerca de un punto

Para ver si dos funciones son **infinitésimos equivalentes** en $x \to a$, graficar el cociente:

```
f(x) = sin(x)
g(x) = x
h(x) = f(x)/g(x)
Límite(h; 0)        # devuelve 1 → equivalentes en x=0
```

Si el límite del cociente es $1$, son equivalentes (notación $f \sim g$ en $x \to a$).

## Ejemplo completo: Estudio de continuidad por tramos

Función típica de los ejercicios:

```
f(x) = Si(x < 1; x^2;
       Si(x = 1; 3;
                 2x + 1))
```

Para verificar continuidad en $x=1$:

```
LímiteIzquierda(f; 1)       # devuelve 1   (de x^2 con x → 1⁻)
LímiteDerecha(f; 1)         # devuelve 3   (de 2x+1 con x → 1⁺)
f(1)                         # devuelve 3
```

Como los límites laterales son distintos, hay **discontinuidad de salto** finito en $x=1$ (salto de tamaño $3-1=2$).

## Comandos resumidos

| Comando | Para qué |
|---------|----------|
| `Límite(f; a)` | $\lim_{x\to a} f(x)$ |
| `Límite(f; infinito)` | $\lim_{x\to+\infty} f(x)$ |
| `LímiteIzquierda(f; a)` | $\lim_{x\to a^-} f(x)$ |
| `LímiteDerecha(f; a)` | $\lim_{x\to a^+} f(x)$ |
| `Asíntota(f)` | Lista de asíntotas |
| `LímiteSuperior(f)`, `LímiteInferior(f)` | $\limsup$ y $\liminf$ (raramente usados en esta materia) |

