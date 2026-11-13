---
title: Primeros pasos en GeoGebra
slug: analisis-matematico-i/geogebra/basico
sidebar:
  order: 1
---


## Las vistas principales

GeoGebra Classic organiza su pantalla en **vistas** que se pueden mostrar/ocultar desde el menú **Vista**:

| Vista | Para qué sirve |
|-------|----------------|
| **Algebraica** | Lista todos los objetos definidos (funciones, números, puntos). Acá aparecen las definiciones que tipeás. |
| **Gráfica 2D** | El plano cartesiano donde se dibujan las funciones y figuras. |
| **CAS** (Cálculo Simbólico) | Para cálculos algebraicos exactos: derivar, integrar, factorizar, resolver ecuaciones de forma simbólica. |
| **Hoja de Cálculo** | Tabla tipo Excel. Útil para introducir datos del tipo $(x_i, y_i)$ y aplicarles regresión. |
| **Gráfica 3D** | Para superficies $z=f(x,y)$. No se usa en esta materia. |


Configuración mínima recomendada: abrir simultáneamente **Algebraica + Gráfica 2D + CAS**. La hoja de cálculo se agrega solo cuando hay datos tabulados (Ej. 4 de la práctica, resorte).

## Configurar el idioma a español

**Menú** → **Opciones** → **Idioma** → **Español / Argentina**. Esto cambia los nombres de los comandos (por ejemplo `Derivative` pasa a `Derivada`), los textos de los menús y los separadores numéricos.

Con español argentino:

- El **separador decimal** es coma: $3{,}14$ en lugar de $3.14$.
- Como la coma queda ocupada para decimales, el **separador de argumentos** dentro de comandos pasa a ser **punto y coma**: `Derivada(f; x)` en lugar de `Derivada(f, x)`.

**Importante:** todos los ejemplos de esta guía usan punto y coma como separador (`;`), asumiendo que tenés GeoGebra configurado en español argentino. Si tu instalación usa coma (idioma inglés u otra variante), reemplazá los `;` por `,`.

## La barra de entrada

En la parte inferior de la vista Algebraica hay una **barra de entrada** donde se tipean comandos y definiciones. Algunas acciones básicas:

| Acción | Cómo |
|--------|------|
| Definir una función | `f(x) = x^2 - 4` |
| Reasignar | volver a tipear `f(x) = …` reemplaza la definición anterior |
| Evaluar | `f(3)` devuelve $f(3)$ |
| Definir un número | `a = 5` |
| Definir un punto | `A = (2; 3)` (coordenadas separadas con `;`) |
| Borrar un objeto | seleccionar en la vista algebraica y `Suprimir` |
| Buscar comandos | tipear las primeras letras: aparece autocompletado |


## Sintaxis: paréntesis y operadores

| Operación | Sintaxis | Ejemplo |
|-----------|----------|---------|
| Suma, resta | `+`, `-` | `3 + 2` |
| Producto | `*` (también espacio o adyacencia) | `2*x`, `2 x`, `2x` |
| División | `/` | `x/2` |
| Potencia | `^` | `x^2`, `e^x` |
| Raíz cuadrada | `sqrt(x)` o `√(x)` | `sqrt(x+4)` |
| Raíz $n$-ésima | `nroot(x, n)` o `surd(x, n)` | `nroot(x; 3)` |
| Valor absoluto | `abs(x)` o `\|x\|` con barras | `abs(x-2)` |
| Logaritmo natural | `ln(x)` | `ln(x+1)` |
| Logaritmo decimal | `lg(x)` o `log(10; x)` | `log(10; 100)` |
| Logaritmo base $a$ | `log(a; x)` | `log(2; 8)` |
| Exponencial | `exp(x)` o `e^x` | `e^x`, `exp(-x^2)` |
| Trigonométricas | `sin(x)`, `cos(x)`, `tan(x)` | `sin(x)` |
| Constantes | `pi`, `e` | `pi`, `e^2` |


## Definir funciones

```
f(x) = -2x^2 + 12x
g(t) = (9/5) t + 32
h(x) = sqrt(x + 2)
```

Una vez definida, la función aparece graficada en la vista Gráfica y como entrada en la vista Algebraica.

## Deslizadores (sliders)

Un **deslizador** es un parámetro que se puede mover con el mouse y ver el efecto en tiempo real. Forma rápida de crearlo desde la barra de entrada:

```
a = 1
```

Hacer clic derecho en el número `a` en la vista Algebraica → **Habilitar deslizador**. Aparece la barra en la vista Gráfica. Para cambiar rango (mínimo, máximo, paso) → **Propiedades** → pestaña **Deslizador**.

**Uso típico:** definir una función con un parámetro y un deslizador para verlo variar.

```
a = 1
f(x) = a*(x-1)^2 + 2
```

Al mover el deslizador `a`, la parábola se estira/comprime y se refleja según el signo. Útil para los ejercicios 14 y 15 de la práctica.

## Texto LaTeX en la gráfica

Para anotar la gráfica con texto matemático (etiquetas con fórmulas):

1. Herramienta **Texto** (icono ABC) → clic en la posición.
2. En el cuadro de texto, marcar **Fórmula LaTeX** y escribir entre signos `$ ... $` o directamente.

Ejemplo: `f(x) = \dfrac{x^2 - 6x + 9}{x - 3}` aparece formateado.

## Configurar la vista gráfica

| Acción | Cómo |
|--------|------|
| Zoom | rueda del mouse o herramienta lupa |
| Pan (mover) | herramienta **Desplaza Vista Gráfica** (flechas) o tecla `Ctrl` + arrastrar |
| Ajustar a un objeto | clic derecho en la función → **Centrar en este objeto** |
| Cambiar rangos de ejes | clic derecho en el área gráfica → **Vista Gráfica** → pestaña **EjeX** / **EjeY** |
| Mostrar cuadrícula | clic derecho en el área gráfica → **Cuadrícula** |


## Exportar gráficos

**Archivo** → **Exporta** → **Vista Gráfica como imagen** (PNG, SVG, PDF). Útil para incluir el gráfico en un informe o en el cuaderno.

## Atajos útiles

| Atajo | Acción |
|-------|--------|
| `Ctrl + Z` / `Ctrl + Y` | Deshacer / Rehacer |
| `Ctrl + S` | Guardar el archivo `.ggb` |
| `Ctrl + Shift + V` | Activar/desactivar Vista CAS |
| Doble clic en un objeto algebraico | Editar definición |
| Clic en el ojito | Mostrar / ocultar objeto en la gráfica |

