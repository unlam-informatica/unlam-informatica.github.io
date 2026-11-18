---
title: 'Unidad 3 — Bases de datos relacionales: aspectos avanzados'
description: "Transacciones, control de concurrencia y rendimiento en SQL Server: TCL, aislamiento, bloqueos, índices, planes de ejecución, optimización y métricas."
slug: bbdd-aplicadas/unidad-3/teoria
sidebar:
  hidden: true
  label: Presentación y ruta
---
Esta unidad estudia cómo un motor relacional mantiene los datos correctos cuando muchas sesiones trabajan a la vez y cómo hacer que las consultas respondan bien. Parte de la arquitectura y la instalación de la [Unidad 2](/bbdd-aplicadas/unidad-2/teoria/) y del SQL de la [Unidad 1](/bbdd-aplicadas/unidad-1/teoria/), y se organiza en tres bloques: transacciones, concurrencia y rendimiento.

## Objetivos de aprendizaje

Al terminar la unidad deberías poder:

- Controlar transacciones con `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVE TRANSACTION`, `TRY/CATCH` y `XACT_ABORT`.
- Reconocer lecturas sucias, no repetibles y fantasmas, y elegir el nivel de aislamiento adecuado.
- Interpretar bloqueos compartidos y exclusivos, esperas e interbloqueos.
- Explicar el commit en dos fases y usar `BEGIN DISTRIBUTED TRANSACTION` con MS DTC.
- Diseñar índices clúster, no clúster y de cobertura para una consulta dada.
- Leer planes estimados y reales e identificar operadores costosos, e interpretar histogramas y densidad y mantener estadísticas.
- Reescribir consultas para hacerlas sargables y medir la mejora con el plan y las estadísticas de E/S.
- Decidir entre almacenamiento por filas y por columnas según la carga.
- Construir una línea de base y medir con DMVs y Activity Monitor.

## Antes de comenzar

- **Conviene repasar:** [Repaso de SQL](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/) (consultas, `JOIN`, restricciones) y, de la Unidad 2, [Arquitectura e instalación de un motor relacional](/bbdd-aplicadas/unidad-2/teoria/bd-transaccionales/) (ACID a nivel conceptual, archivos de datos y de log) y [Bases de datos de sistema y de usuario](/bbdd-aplicadas/unidad-2/teoria/bases-de-sistema/).
- **Herramientas:** SQL Server 2022 y dos ventanas de consulta (dos sesiones independientes) para los experimentos de concurrencia. Ver [Cómo estudiar · Herramientas](/bbdd-aplicadas/como-estudiar/#herramientas).

## Ruta de aprendizaje

Seguí las etapas en orden. Cada una indica qué leer y, cuando existe, qué practicar antes de pasar a la siguiente.

:::caution[Qué está verificado y qué no]
Los ejemplos y ejercicios de **una sola sesión** se ejecutaron en SQL Server 2022. Los que necesitan **dos o tres sesiones** (bloqueos entre sesiones, deadlocks, lectura sucia, fantasmas, experimentos de la tarjeta de crédito) y los de **transacciones distribuidas con MS DTC** se presentan como guiones paso a paso, revisados contra la documentación de Microsoft y con verificación específica pendiente. Cuando los reproduzcas, comprobá el comportamiento en tu propio motor.
:::

### Bloque 1 · Transacciones

#### 1. Control de transacciones (TCL)

Qué es una transacción, las propiedades ACID y cómo se abre, confirma y deshace desde una sesión, incluido el manejo de errores.

- **Leé:** [Control de transacciones (TCL)](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/)
- **Practicá:** [Laboratorio TCL](/bbdd-aplicadas/unidad-3/practica/laboratorio-tcl/), [parte 1](/bbdd-aplicadas/unidad-3/practica/laboratorio-tcl/#parte-1-ejercicios-de-una-sesión) (diez ejercicios de una sola sesión).
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/#autoevaluación)

### Bloque 2 · Concurrencia

#### 2. Concurrencia y niveles de aislamiento

Qué pasa cuando varias transacciones se ejecutan a la vez: planificaciones serializables, locks, fenómenos de concurrencia, niveles de aislamiento y versionado de filas. Es la continuación natural del TCL.

- **Leé:** [Concurrencia, bloqueos y transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/), desde [Planificaciones: serie y serializable](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/#planificaciones-serie-y-serializable) hasta [SNAPSHOT y READ_COMMITTED_SNAPSHOT](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/#snapshot-y-read_committed_snapshot).
- **Practicá:** [parte 2 del Laboratorio TCL](/bbdd-aplicadas/unidad-3/practica/laboratorio-tcl/#parte-2-laboratorio-guiado-tarjeta-de-crédito) (tarjeta de crédito) y el [Laboratorio de niveles de aislamiento](/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento/): laboratorios 1 a 5 y ejercicios 11 a 15, 18 y 24. Los experimentos con dos o más sesiones figuran como pendientes de verificación específica.

#### 3. Bloqueos, esperas y deadlocks

Cómo diagnosticar un bloqueo, limitar la espera y entender un interbloqueo.

- **Leé:** la sección [Bloqueos y esperas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/#bloqueos-y-esperas) de la misma página, que incluye [Deadlock](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/#deadlock).
- **Practicá:** ejercicios 16, 17 y 25 del [Laboratorio de niveles de aislamiento](/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento/). El 25 (deadlock) requiere dos sesiones y está revisado, no verificado en motor.

#### 4. Transacciones distribuidas

Commit en dos fases y `BEGIN DISTRIBUTED TRANSACTION` con MS DTC.

- **Leé:** [Transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/#transacciones-distribuidas)
- **Practicá:** ejercicios 19 y 20 del [Laboratorio de niveles de aislamiento](/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento/). Un ejemplo completo requiere una segunda instancia, un servidor vinculado y MS DTC: la lección lo presenta como pendiente de verificación específica.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/#autoevaluación), que cierra el bloque de concurrencia.

### Bloque 3 · Rendimiento

Antes del bloque conviene saber que la práctica de rendimiento tiene veinte ejercicios ordenados por nivel (inicial, intermedio y avanzado) y no por tema. En cada etapa se indica qué ejercicios corresponden.

#### 5. Índices

Heap, índice clúster, no clúster, cobertura, selectividad, mantenimiento e índices filtrados. Se estudian antes que los planes porque la lección de planes presupone conocer índices clúster y no clúster.

- **Leé:** [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/), desde [Datos de ejemplo y cómo medimos](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/#datos-de-ejemplo-y-cómo-medimos) hasta [Índices filtrados, únicos y no usados](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/#índices-filtrados-únicos-y-no-usados).
- **Practicá:** [Práctica de rendimiento](/bbdd-aplicadas/unidad-3/practica/rendimiento/), ejercicios 1, 2, 3, 8, 11, 12, 13, 16 y 17.

#### 6. Plan de ejecución y estadísticas

Cómo se genera y reutiliza un plan, cómo leerlo y cómo las estadísticas alimentan las estimaciones.

- **Leé:** [Plan de ejecución y estadísticas](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/)
- **Practicá:** ejercicios 4, 6, 7 y 15 de la [Práctica de rendimiento](/bbdd-aplicadas/unidad-3/practica/rendimiento/).
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/#autoevaluación)

#### 7. Optimización de consultas

Reescribir consultas para que el motor pueda usar los índices: predicados sargables, conversiones implícitas, `LIKE`, `OR` y subconsultas.

- **Leé:** la sección [Optimización de consultas](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/#optimización-de-consultas) de [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/).
- **Practicá:** ejercicios 9, 10 y 18 de la [Práctica de rendimiento](/bbdd-aplicadas/unidad-3/practica/rendimiento/).

#### 8. Rowstore y columnstore

Cuándo conviene almacenar por filas y cuándo por columnas.

- **Leé:** la sección [Rowstore y columnstore](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/#rowstore-y-columnstore) de la misma página.
- **Practicá:** ejercicio 14 de la [Práctica de rendimiento](/bbdd-aplicadas/unidad-3/practica/rendimiento/).
- **Comprobá:** [autoevaluación de Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/#autoevaluación)

#### 9. Métricas de rendimiento

Línea de base, recuento de filas, entrada y salida de archivos, consumo por consulta, esperas y Activity Monitor.

- **Leé:** [Métricas de rendimiento](/bbdd-aplicadas/unidad-3/teoria/metricas-de-rendimiento/)
- **Practicá:** ejercicios 5 y 19 de la [Práctica de rendimiento](/bbdd-aplicadas/unidad-3/practica/rendimiento/). Para cerrar el bloque, el ejercicio 20 (diseñar los índices de una carga de trabajo) integra índices, planes y optimización.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-3/teoria/metricas-de-rendimiento/#autoevaluación)

## Ejercicios y laboratorios

- **[Laboratorio TCL](/bbdd-aplicadas/unidad-3/practica/laboratorio-tcl/)** · 13 ejercicios — diez de una sola sesión sobre control de transacciones y tres experimentos de un laboratorio guiado con tarjeta de crédito (más un experimento 0 de una sesión).
- **[Laboratorio de niveles de aislamiento](/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento/)** · 12 ejercicios — fenómenos de concurrencia, `SNAPSHOT` y RCSI con dos sesiones; locks, versiones de fila, deadlock y transacciones distribuidas.
- **[Práctica de rendimiento](/bbdd-aplicadas/unidad-3/practica/rendimiento/)** · 20 ejercicios — índices, plan de ejecución, estadísticas, optimización, columnstore y métricas.

Ver el [índice de prácticas](/bbdd-aplicadas/unidad-3/practica/).

## Autoevaluación y repaso

Las cinco lecciones terminan en una autoevaluación (enlazadas en la ruta). La unidad no tiene resumen integrador ni guía de examen: el repaso son esas autoevaluaciones y las prácticas.

## Continuar

Cuando puedas resolver las prácticas de la unidad sin mirar la resolución, seguí con la [Unidad 4 — Bases de datos no relacionales](/bbdd-aplicadas/unidad-4/teoria/).
