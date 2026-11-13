---
title: GeoGebra para Funciones (Unidad 1)
slug: analisis-matematico-i/geogebra/funciones
sidebar:
  order: 2
---


Esta página cubre todo lo que necesitás de GeoGebra para resolver los ejercicios de la **Práctica 1**.

## Graficar una función

En la barra de entrada, escribir directamente la regla de asignación:

```
f(x) = -2x^2 + 12x
g(x) = sqrt(x - 2)
h(x) = ln(x + 1)
m(x) = abs(x - 2)
```

Aparece automáticamente la gráfica y la función se lista en la vista Algebraica.

**Tip:** para graficar varias funciones a la vez y compararlas, definirlas con distintos nombres (`f`, `g`, `h`, …). Cada una toma un color distinto.

## Restringir el dominio de una función

Para graficar una función solo en un intervalo, se usa el comando `Función`:

```
f(x) = Función(-2x^2 + 12x; 0; 6)
```

Esto grafica $-2x^2+12x$ únicamente en $[0,6]$. Útil para los ejercicios con **dominio en contexto** (Ej. 3, 4, 5, 8, 31 de la práctica).

Para condiciones más complejas (por ejemplo, intervalos abiertos o exclusiones puntuales), usar `Si`:

```
f(x) = Si(0 < x < 6; -2x^2 + 12x)
```

## Funciones definidas por tramos

Para los ejercicios del tipo Ej. 11 de la práctica, hay dos formas:

**Forma 1: anidar `Si()`**

```
f(x) = Si(x <= -1; x + 2;
       Si(-1 < x <= 1; -x;
       Si(1 < x <= 3; 3x - 4;
                       2)))
```

**Forma 2: comando `Si(<condiciones>; <valores>)`** (más limpia):

```
f(x) = Si(x <= -1; x + 2; -1 < x <= 1; -x; 1 < x <= 3; 3x - 4; 2)
```

El último argumento es el "caso por defecto" (cuando ninguna condición se cumple).

## Encontrar raíces (ceros)

Si la función es polinómica:

```
Raíz(f)
```

Devuelve una lista con todas las raíces. Para funciones no polinómicas o si querés raíces en un intervalo:

```
Raíz(f; a; b)
```

devuelve las raíces en $[a,b]$. Para una raíz cercana a un valor inicial:

```
Raíz(f; 1.5)
```

usa el método de Newton arrancando en $x=1{,}5$.

## Intersecciones entre funciones o con ejes

| Qué querés | Comando |
|------------|---------|
| Intersecciones de $f$ y $g$ | `Interseca(f; g)` |
| Intersección con el eje $x$ | `Interseca(f; EjeX)` (equivalente a `Raíz(f)`) |
| Intersección con el eje $y$ | `Interseca(f; EjeY)` o simplemente evaluar `f(0)` |
| Intersecciones en un intervalo | `Interseca(f; g; a; b)` |


## Encontrar extremos

```
Extremo(f)              # mínimos y máximos locales (función global)
Extremo(f; a; b)        # extremos en un intervalo cerrado
Máximo(f; a; b)         # solo el máximo absoluto en [a,b]
Mínimo(f; a; b)         # solo el mínimo absoluto en [a,b]
```

Útil para los ejercicios de **optimización** (Ej. 5, 6, 12, 24) donde hay que encontrar el valor de $x$ que maximiza un área, volumen o beneficio.

## Asíntotas

```
Asíntota(f)
```

Devuelve una lista con las asíntotas verticales y horizontales/oblicuas de la función. Útil para los ejercicios de funciones racionales y exponenciales/logarítmicas (Ej. 10c, 10d, 10f, 10g, etc.).

## Composición de funciones

GeoGebra acepta sustitución directa:

```
f(x) = x^2 + 1
g(x) = sqrt(x)

(f ∘ g)(x) = f(g(x))    # o tipear f(g(x)) directamente
```

Para verlo como una nueva función:

```
h(x) = f(g(x))
```

## Función inversa

```
FunciónInversa(f)
```

Devuelve la inversa simbólica. **Importante:** GeoGebra solo encuentra la inversa cuando la función es invertible en una rama clara (por ejemplo $f(x)=2x+1$ o $f(x)=e^x$). Para funciones no inyectivas como $f(x)=x^2$, hay que restringir el dominio primero.

**Visualizar la inversa gráficamente:** definir la recta $y=x$ y reflejar la gráfica.

```
recta(x) = x
g(x) = FunciónInversa(f)
```

La gráfica de $g$ aparece como el simétrico de $f$ respecto a $y=x$.

## Tabla de valores

Para tabular una función:

```
Secuencia((x; f(x)); x; 0; 8; 1)
```

Genera la lista de puntos $(0,f(0)), (1,f(1)), …, (8,f(8))$.

Alternativa con la **Hoja de Cálculo**:

1. Abrir la vista Hoja de Cálculo.
2. En la columna A escribir los valores de $x$.
3. En B1 escribir `=f(A1)` y arrastrar hacia abajo.

## Regresión sobre datos

Usado en el **Ej. 4 (resorte)** de la práctica.

### Paso 1: Cargar los datos en la Hoja de Cálculo

Columna A: valores de $x$. Columna B: valores de $y$. Seleccionar las dos columnas con datos.

### Paso 2: Crear la lista de puntos

Con la selección hecha, clic derecho → **Crear** → **Lista de puntos**. Aparece una lista `l1 = {(0,0), (1, 0.875), …}` en la vista Algebraica.

### Paso 3: Aplicar el comando de regresión

| Modelo | Comando |
|--------|---------|
| Lineal $y=a x+b$ | `RegLineal(l1)` |
| Polinómica de grado $n$ | `RegPolinómica(l1; n)` |
| Potencial $y = a\,x^b$ | `RegPotencial(l1)` |
| Exponencial $y=a\,e^{bx}$ | `RegExponencial(l1)` |
| Logarítmica $y=a+b\ln x$ | `RegLogarítmica(l1)` |


Para el ejercicio del resorte: `RegLineal(l1)` da la recta $y \approx 0{,}875\,x$ que confirma la proporcionalidad directa.

## Transformaciones con deslizador

Para visualizar los efectos de los ejercicios 14, 15 y 16:

```
c = 1                      # deslizador
f(x) = x^2                  # función base
g(x) = f(x) + c             # traslación vertical
h(x) = f(x - c)             # traslación horizontal
k(x) = c * f(x)             # escalado vertical
m(x) = f(c * x)             # escalado horizontal
n(x) = -f(x)                # reflexión respecto al eje x
p(x) = f(-x)                # reflexión respecto al eje y
```

Activar el deslizador `c` con rango `[-3; 3]` y mover. Cada función se actualiza en tiempo real.

## Verificar paridad

Una función es **par** si $f(-x)=f(x)$, **impar** si $f(-x)=-f(x)$. Para verificarlo gráficamente:

```
f(x) = x^2 - 4
g(x) = f(-x)
h(x) = -f(x)
```

Si la gráfica de $g$ coincide con la de $f$ → par. Si coincide con la de $h$ → impar. Si no coincide con ninguna → no tiene paridad.

## Ejemplo completo: Ejercicio 4 (resorte)

```
# Datos del experimento (cargados en Hoja de Cálculo, columnas A y B)
# A1:A9 = {0,1,2,3,4,5,6,7,8}
# B1:B9 = {0, 0.875, 1.721, 2.641, 3.531, 4.391, 5.241, 6.120, 6.992}

# Seleccionar A1:B9 → clic derecho → Crear lista de puntos
# Aparece: l1 = {(0,0), (1, 0.875), …, (8, 6.992)}

# Regresión lineal
f = RegLineal(l1)

# Resultado: f(x) ≈ 0.875 x

# Predicción para x = 10
f(10)
# Devuelve ≈ 8.75 pulgadas
```

## Ejemplo completo: Ejercicio 5 (canaleta)

```
# Función del área de la sección transversal
A(x) = (12 - 2x) * x

# Restringir el dominio en contexto
A_ctx(x) = Función(A(x); 0; 6)

# Buscar el máximo en (0; 6)
Extremo(A; 0; 6)
# Resultado: (3, 18) → x = 3 cm da área máxima 18 cm²

# Para el volumen total (largo = 100 cm)
V(x) = 100 * A(x)
Extremo(V; 0; 6)
# Resultado: (3, 1800) → volumen máximo 1800 cm³
```
