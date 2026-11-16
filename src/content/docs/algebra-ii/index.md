---
title: Álgebra y Geometría Analítica II — UNLaM
description: "Manual de estudio de Álgebra II para Ingeniería en Informática: teoría, ejemplos, ejercicios resueltos y simulacros."
slug: algebra-ii
sidebar:
  order: 1
  label: Álgebra y Geometría Analítica II
---

Manual de estudio de **Álgebra y Geometría Analítica II** (asignatura 3645) de Ingeniería en
Informática, organizado según el [programa analítico 2023](/algebra-ii/programa/). La materia se
cursa en el primer cuatrimestre de tercer año y tiene como correlativa a Álgebra y Geometría
Analítica I.

:::note[Material no oficial]
Este manual es material de estudio independiente. No es un documento de la cátedra ni de la
Universidad Nacional de La Matanza, y no reemplaza las clases, las guías ni las indicaciones de los
docentes. Los ejercicios y los simulacros son originales: ninguno reproduce un examen tomado.
:::

## De qué trata la materia

Álgebra II es el tramo central del álgebra lineal. Estudia estructuras —espacios vectoriales,
transformaciones lineales, espacios con producto interno— que aparecen en casi toda la informática:
los datos se representan como vectores, los cambios de representación son transformaciones lineales,
los sistemas que evolucionan por pasos se analizan con autovalores y la mejor aproximación de un
conjunto de mediciones es una proyección ortogonal. El programa pone especial atención en
aplicaciones propias de la carrera: **códigos detectores y correctores de errores** sobre
$\mathbb{Z}_2$, **relaciones de recurrencia**, **cadenas de Markov** y **ajuste de datos por cuadrados
mínimos**.

## Cómo está organizado

| Sección | Contenido |
|---|---|
| [Repaso de Álgebra I](/algebra-ii/repaso/) | Vectores, matrices, determinantes, sistemas, polinomios, rectas y planos: lo que se usa desde el primer día. |
| [Unidad 1 — Espacios vectoriales](/algebra-ii/unidad-1/) | Cuerpos y $\mathbb{Z}_2$, subespacios, independencia lineal, base, dimensión, coordenadas, cambio de coordenadas y códigos lineales. |
| [Unidad 2 — Transformaciones lineales](/algebra-ii/unidad-2/) | Núcleo e imagen, teorema de la dimensión, clasificación, teorema fundamental, matriz asociada, cambio de base, composición e inversa. |
| [Unidad 3 — Autovalores y autovectores](/algebra-ii/unidad-3/) | Polinomio característico, semejanza, diagonalización, potencias, recurrencias lineales y cadenas de Markov. |
| [Unidad 4 — Espacios con producto interno](/algebra-ii/unidad-4/) | Norma, ángulo, ortogonalidad, Gram-Schmidt, complemento ortogonal, proyección, cuadrados mínimos y códigos en $\mathbb{Z}_2^n$. |
| [Integradores y simulacros](/algebra-ii/integradores/) | Dos simulacros originales con resolución completa, uno por parcial. |

Cada unidad tiene una **presentación** (objetivos, índice y qué se evalúa), **lecciones de teoría**
con definiciones, demostraciones, ejemplos resueltos, figuras y errores frecuentes, y una
**práctica** en cuatro páginas: nivel inicial, intermedio y avanzado, y una guía integradora con
problemas de varios ítems en el estilo de un parcial. Todas las resoluciones están plegadas para
que primero intentes cada ejercicio.

## Por dónde empezar

1. Leé [Cómo estudiar con este manual](/algebra-ii/como-estudiar/) y revisá la
   [notación](/algebra-ii/notacion/): la de la cátedra difiere de la de los libros en detalles que
   cambian el resultado (por ejemplo, el orden de los subíndices de una matriz de cambio de base).
2. Hacé el autodiagnóstico del [repaso](/algebra-ii/repaso/) y repasá solo lo que haga falta.
3. Seguí las unidades en orden: cada una usa la anterior.

## Verificación del contenido

Las cuentas de los ejemplos y de los ejercicios se comprueban con programas reproducibles
(SymPy, y aritmética modular exacta para $\mathbb{Z}_2$) que forman parte del repositorio del sitio.
Las demostraciones se revisan por separado: una comprobación numérica no reemplaza un argumento.
Si encontrás un error, podés informarlo en el
[repositorio del portal](https://github.com/unlam-informatica/unlam-informatica.github.io/issues).

## Bibliografía principal

- Poole, D. *Álgebra lineal. Una introducción moderna*. Cengage Learning.
- Lay, D. *Álgebra lineal y sus aplicaciones*. Pearson.

Detalle, ediciones y secciones por tema en [Bibliografía](/algebra-ii/bibliografia/).
