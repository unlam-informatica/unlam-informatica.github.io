---
title: Unidad 3 — Teoría
slug: bbdd-aplicadas/unidad-3/teoria
sidebar:
  order: 0
  label: Presentación
---
Resúmenes teóricos y guías de referencia de la Unidad 3.

## Bases de datos relacionales: aspectos avanzados

La unidad tiene dos grandes bloques: la **concurrencia** (transacciones, aislamiento, bloqueos y transacciones distribuidas) y el **rendimiento** (planes de ejecución, índices, estadísticas, optimización de consultas, columnstore y métricas de performance).

## Teoría

| Apunte | Tema |
|---------|------|
| [Concurrencia, bloqueos y transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/) | Planificaciones serializables, locks S/X, fenómenos y niveles de aislamiento, SNAPSHOT y RCSI, bloqueos y esperas, deadlocks, transacciones distribuidas (2PC, MS DTC) |
| [Control de transacciones (TCL)](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/) | ACID, modos de transacción, BEGIN/COMMIT/ROLLBACK/SAVE, @@TRANCOUNT, TRY/CATCH, XACT_STATE, XACT_ABORT y procedimiento transaccional |
| [Plan de ejecución y estadísticas](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/) | Fases de una consulta (parser, algebrizer, optimizer, execution engine), plan estimado y real, caché de planes, extracción de operadores del plan XML, estadísticas (encabezado, densidad, histograma), actualización automática y manual |
| [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/) | Heap y clúster, uniquifier, page splits, no clúster, cobertura, selectividad, fill factor, rebuild y reorganize, filtrados, índices no usados, reescritura de consultas (sargabilidad, conversiones, subconsultas), rowstore y columnstore |
| [Métricas de rendimiento](/bbdd-aplicadas/unidad-3/teoria/metricas-de-rendimiento/) | Línea de base, recuento de filas, E/S de archivos, consumo por consulta y esperas, modelos de recuperación (SIMPLE, FULL, BULK_LOGGED), tamaño del backup del log, esperas y bloqueos activos, Monitor de actividad |

## Práctica

[Ir a los ejercicios y laboratorios de la unidad](/bbdd-aplicadas/unidad-3/practica/).
