---
title: Cómo estudiar con este manual
description: Método de estudio, plan semanal alineado al cronograma, uso de la práctica y herramientas para comprobar cuentas.
slug: algebra-ii/como-estudiar
sidebar:
  order: 3
---

Álgebra II tiene pocas cuentas difíciles y muchas ideas nuevas. Los errores típicos de examen no son
aritméticos: son confundir un vector con sus coordenadas, multiplicar matrices de cambio en el orden
equivocado o justificar con un ejemplo una afirmación general. Esta página propone una forma de
trabajar que apunta a esos problemas.

## Un ciclo de estudio por lección

1. **Leé la motivación y la intuición** sin detenerte en las demostraciones. Mirá las figuras: cada una
   muestra algo concreto que conviene poder explicar con palabras.
2. **Copiá a mano las definiciones** y escribí un ejemplo y un no ejemplo propios de cada una. Si no
   te sale un no ejemplo, la definición todavía no está clara.
3. **Seguí los ejemplos resueltos con lápiz**, tapando la resolución y destapándola de a un paso.
4. **Leé las demostraciones** de los resultados principales e intentá reconstruirlas al día siguiente.
   En los parciales no se piden demostraciones del apunte, pero sí demostraciones cortas nuevas que
   usan las mismas ideas.
5. **Revisá los errores frecuentes** de la lección: muchos son, literalmente, opciones falsas de un
   ejercicio de verdadero o falso.
6. **Hacé la práctica** (sección siguiente) antes de pasar a la lección que sigue.

## Cómo usar la práctica

Cada unidad tiene cuatro páginas de práctica:

| Página | Para qué sirve |
|---|---|
| Nivel inicial | Aplicar una definición o un procedimiento. Si un ejercicio de este nivel no sale, volvé a la lección. |
| Nivel intermedio | Combinar dos o tres ideas y elegir el método. Es el grueso de un parcial. |
| Nivel avanzado | Demostraciones, parámetros, problemas abstractos y aplicaciones. |
| Guía integradora | Problemas de varios ítems encadenados, con el formato de un parcial. |

Las resoluciones están plegadas. Abrilas solo después de terminar el ejercicio o de trabarte al menos
diez minutos. Al corregir, compará también la **justificación**, no solo el resultado: en el parcial
se exige que los pasos estén explicitados y justificados.

Cada resolución termina con una **comprobación**. Acostumbrate a hacerla siempre: reconstruir un
vector a partir de sus coordenadas, aplicar la transformación a un vector del núcleo, verificar que
$C^{-1}AC$ dé la matriz diagonal o que el residuo de cuadrados mínimos sea ortogonal a las columnas.
Es la forma más barata de detectar un error antes de entregar.

## Plan semanal sugerido

El plan sigue el cronograma del [programa](/algebra-ii/programa/). La columna "práctica" indica qué
resolver esa semana.

| Semana | Teoría | Práctica |
|---|---|---|
| 0 | [Repaso](/algebra-ii/repaso/) según el autodiagnóstico | Ejercicios del repaso |
| 1 | [1.1](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/) a [1.3](/algebra-ii/unidad-1/teoria/subespacios/) | U1 inicial |
| 2 | [1.4](/algebra-ii/unidad-1/teoria/combinaciones-lineales/) a [1.7](/algebra-ii/unidad-1/teoria/base-y-dimension/) | U1 inicial e intermedio |
| 3 | [1.8](/algebra-ii/unidad-1/teoria/coordenadas/) a [1.10](/algebra-ii/unidad-1/teoria/codigos-lineales/) | U1 avanzado e integradora |
| 4 | [2.1](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/) a [2.4](/algebra-ii/unidad-2/teoria/clasificacion/) | U2 inicial |
| 5 | [2.5](/algebra-ii/unidad-2/teoria/teorema-fundamental/) y [2.8](/algebra-ii/unidad-2/teoria/composicion-e-inversa/) | U2 intermedio |
| 6–7 | [2.6](/algebra-ii/unidad-2/teoria/matriz-asociada/) y [2.7](/algebra-ii/unidad-2/teoria/cambio-de-base/) | U2 avanzado e integradora |
| 8 | Repaso para el primer parcial | [Simulacro 1](/algebra-ii/integradores/simulacro-1/) |
| 9 | [3.1](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/) a [3.3](/algebra-ii/unidad-3/teoria/propiedades/) | U3 inicial |
| 10 | [3.4](/algebra-ii/unidad-3/teoria/matrices-semejantes/) a [3.6](/algebra-ii/unidad-3/teoria/potencias/) | U3 intermedio |
| 11 | [3.7](/algebra-ii/unidad-3/teoria/relaciones-de-recurrencia/), [3.8](/algebra-ii/unidad-3/teoria/cadenas-de-markov/), [4.1](/algebra-ii/unidad-4/teoria/producto-interno/) y [4.2](/algebra-ii/unidad-4/teoria/norma-distancia-angulo/) | U3 avanzado e integradora; U4 inicial |
| 12 | [4.3](/algebra-ii/unidad-4/teoria/ortogonalidad/) a [4.5](/algebra-ii/unidad-4/teoria/complemento-ortogonal/) | U4 intermedio |
| 13 | [4.6](/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/) y [4.7](/algebra-ii/unidad-4/teoria/cuadrados-minimos/) | U4 avanzado e integradora |
| 14 | Repaso para el segundo parcial | [Simulacro 2](/algebra-ii/integradores/simulacro-2/) |
| 15 | [4.8](/algebra-ii/unidad-4/teoria/codigos-y-z2/) | Ejercicios de códigos de U1 y U4 |

## Antes de un parcial

- Hacé el simulacro correspondiente **con tiempo**: dos horas para el primero y tres para el segundo,
  sin abrir resoluciones ni apuntes.
- Corregilo con las resoluciones y anotá el tipo de error de cada ítem (concepto, método, cuenta,
  justificación). La lista de errores es más útil que la nota.
- Repasá la página de [notación](/algebra-ii/notacion/): un subíndice invertido en $C_{BB'}$ o en
  $M(T)_{BB'}$ arruina un ejercicio entero aunque las cuentas estén bien.

## Herramientas para comprobar cuentas

El programa propone trabajar también con calculadoras de matrices y GeoGebra. Úsalas para **verificar**
lo que hiciste a mano, no para reemplazarlo: en el parcial no están disponibles.

- **GeoGebra** (vista CAS): `Determinante(A)`, `Inversa(A)`, `EscalonadaReducida(A)`,
  `Autovalores(A)`, `Autovectores(A)`.
- **Python con SymPy** (gratuito), útil también para $\mathbb{Z}_2$:

```python
import sympy as sp

A = sp.Matrix([[2, 1], [1, 2]])
print(A.charpoly().as_expr())      # polinomio característico
print(A.eigenvects())              # autovalores, multiplicidad y autovectores
C, D = A.diagonalize()             # A = C D C^(-1)
print(C, D, C * D * C.inv() == A)
print(sp.Matrix([[1, 1, 0], [0, 1, 1]]).rref())  # forma escalonada reducida
```

Para cuentas en $\mathbb{Z}_2$ hay que reducir módulo 2 en cada paso: una calculadora de matrices
reales da, en general, resultados distintos (por ejemplo, un rango mayor).
