---
title: Programa de la materia
description: Contenidos, objetivos, cronograma y evaluación del programa analítico 2023 de Álgebra y Geometría Analítica II, con la página donde se desarrolla cada tema.
slug: algebra-ii/programa
sidebar:
  order: 2
---

Resumen del **programa analítico 2023** de la asignatura 3645 — Álgebra y Geometría Analítica II,
Ingeniería en Informática, Departamento de Ingeniería e Investigaciones Tecnológicas (DIIT), UNLaM.
El documento oficial está publicado en la página de la asignatura:
[programa en PDF](https://ingenieria.unlam.edu.ar/descargas/661_3645_AlgebrayGeometriaAnaliticaII.pdf).
Al momento de preparar este manual (noviembre de 2026) es la versión vigente que ofrece el sitio del
departamento; ante cualquier diferencia, vale el programa oficial y lo que indique la cátedra.

## Datos generales

| Dato | Valor |
|---|---|
| Carrera | Ingeniería en Informática (Plan 2023) |
| Ubicación en el plan | Tercer año, primer cuatrimestre |
| Trayecto | Ciencias Básicas |
| Carga horaria | 4 horas semanales, 64 horas totales |
| Modalidad | Presencial |
| Correlativa anterior | Álgebra y Geometría Analítica I (3627) |
| Correlativas posteriores | Probabilidad y Estadística; Virtualización de Hardware |
| Conocimientos necesarios | Vectores y matrices, cálculo vectorial y matricial, sistemas de ecuaciones, factorización de polinomios |

## Objetivos

El programa espera que, al terminar la cursada, se puedan:

- comprender las definiciones y propiedades de espacio vectorial y de espacio euclídeo, y su conexión
  con temas de informática;
- conocer las propiedades de las transformaciones lineales y elegir bases convenientes para
  representarlas con matrices (cambio de coordenadas, cambio de base, matriz de una transformación);
- definir transformaciones lineales con condiciones dadas;
- hallar autovalores y autovectores y representar una transformación en una base de autovectores;
- ortonormalizar bases, hallar complementos ortogonales, proyectar sobre subespacios y calcular
  distancias;
- interpretar aplicaciones del campo informático y usar en ellas las técnicas aprendidas;
- usar con flexibilidad representaciones vectoriales y matriciales, numéricas y simbólicas.

## Contenidos y dónde se desarrollan

### Unidad 1 — Espacios vectoriales

Espacios vectoriales y sus propiedades. Subespacios. Combinación lineal y conjunto generador.
Independencia lineal, con su interpretación geométrica en el plano y el espacio. Rango de una matriz.
Ecuaciones de un subespacio. Base, coordenadas, unicidad de las coordenadas y dimensión. Extensión de
un conjunto linealmente independiente a una base. Cambio de base y matriz de cambio de coordenadas.
Aplicación: espacios de $n$-uplas y matrices sobre $\mathbb{R}$ y sobre $\mathbb{Z}_2$; teoría de
codificación, matriz de paridad, códigos $(n,k)$ y detección de errores.

Se desarrolla en la [Unidad 1](/algebra-ii/unidad-1/), lecciones
[1.1](/algebra-ii/unidad-1/teoria/cuerpos-y-z2/) a
[1.10](/algebra-ii/unidad-1/teoria/codigos-lineales/).

### Unidad 2 — Transformaciones lineales

Definición y propiedades. Núcleo e imagen. Monomorfismo, epimorfismo e isomorfismo. Teorema
fundamental de las transformaciones lineales. Teorema de la dimensión. Matriz de una transformación
lineal. Composición y matriz de la composición. Transformación inversa y su matriz.

Se desarrolla en la [Unidad 2](/algebra-ii/unidad-2/), lecciones
[2.1](/algebra-ii/unidad-2/teoria/definicion-y-ejemplos/) a
[2.8](/algebra-ii/unidad-2/teoria/composicion-e-inversa/).

### Unidad 3 — Autovalores y autovectores

Autovalores y autovectores de una matriz cuadrada real. Matrices semejantes. Diagonalización.
Aplicación a cadenas de Markov y a relaciones de recurrencia lineal.

Se desarrolla en la [Unidad 3](/algebra-ii/unidad-3/), lecciones
[3.1](/algebra-ii/unidad-3/teoria/autovalores-y-autovectores/) a
[3.8](/algebra-ii/unidad-3/teoria/cadenas-de-markov/).

### Unidad 4 — Espacios con producto interno (espacios euclídeos)

Espacio euclídeo. Distancia definida por el producto interno. Ortogonalidad. Bases ortonormales.
Método de Gram-Schmidt. Complemento ortogonal. Proyecciones ortogonales. Aplicación a la teoría de
códigos: producto en $\mathbb{Z}_2^n$, códigos autoduales, distancia de Hamming y detección de errores
en la transmisión. Aplicación: aproximación de datos experimentales por cuadrados mínimos.

Se desarrolla en la [Unidad 4](/algebra-ii/unidad-4/), lecciones
[4.1](/algebra-ii/unidad-4/teoria/producto-interno/) a
[4.8](/algebra-ii/unidad-4/teoria/codigos-y-z2/).

## Cronograma orientativo

El programa distribuye los temas en dieciséis semanas:

| Semanas | Temas | Unidad |
|---|---|---|
| 1 | Cuerpos y espacios vectoriales; ejemplos con $\mathbb{R}^n$ y $\mathbb{Z}_2^n$ | 1 |
| 2 | Subespacios, independencia lineal, base y dimensión | 1 |
| 3 | Cambio de coordenadas y aplicaciones de la unidad | 1 |
| 4–5 | Transformaciones lineales, núcleo, imagen, clasificación, teoremas de la dimensión y fundamental, composición e inversa | 2 |
| 6–7 | Matriz de una transformación lineal y cambio de coordenadas | 2 |
| 8 | Primer parcial; definición de autovalores y autovectores | 2 y 3 |
| 9–10 | Cálculo de autovalores, matrices semejantes, diagonalización | 3 |
| 11 | Cadenas de Markov; espacios euclídeos, ortogonalidad, norma y distancia | 3 y 4 |
| 12–13 | Ortogonalización, complemento ortogonal, proyección y distancia | 4 |
| 14 | Segundo parcial | — |
| 15 | Aplicación de los espacios euclídeos a la teoría de códigos | 4 |
| 16 | Recuperatorio | — |

## Evaluación

Según el programa, la evaluación es sumativa e incluye:

- **Primer parcial** (semana 8, dos horas): espacios vectoriales y subespacios sobre $\mathbb{R}$ y
  sobre $\mathbb{Z}_2$; base, dimensión y cambio de coordenadas; subespacios asociados a una matriz
  (rango y nulidad); transformaciones lineales (determinación por el teorema fundamental, núcleo e
  imagen, transformaciones inversibles, composición, cálculos con la matriz de la transformación);
  aplicación a códigos de Hamming.
- **Segundo parcial** (semana 14, tres horas, integrador): transformaciones lineales y cambio de
  coordenadas; autovalores y autovectores; diagonalización; espacios con producto interno;
  ortogonalización; proyección ortogonal; aplicaciones a ecuaciones de recurrencia y a corrección de
  errores en códigos.
- **Recuperatorio** (semana 16, tres horas).
- **Trabajos prácticos obligatorios** sobre aplicaciones: autovalores y recurrencias (la sucesión de
  Fibonacci) y espacios con producto interno aplicados al código de Hamming.

Cada parcial combina ejercicios prácticos y preguntas teóricas o conceptuales. Los
[simulacros](/algebra-ii/integradores/) de este manual siguen esa distribución de temas.

## Bibliografía del programa

Obligatoria: Poole, *Álgebra lineal. Una introducción moderna* (4.ª ed., Cengage, 2017) y Lay,
*Álgebra lineal y sus aplicaciones* (5.ª ed., Pearson, 2016). Complementaria: Grossman y Flores
Godoy, *Álgebra lineal* (7.ª ed., McGraw Hill, 2012); Anton, *Introducción al álgebra lineal*
(3.ª ed., Limusa, 2005); Strang, *Álgebra lineal y sus aplicaciones* (4.ª ed., Thomson, 2007). Para
códigos, el programa remite a Nakos y Joyner, *Álgebra lineal con aplicaciones*. Ver
[Bibliografía](/algebra-ii/bibliografia/).
