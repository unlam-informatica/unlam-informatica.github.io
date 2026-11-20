---
title: Unidad 3 — Práctica
slug: bbdd-aplicadas/unidad-3/practica
sidebar:
  order: 0
  label: Índice de prácticas
---
Ejercicios prácticos de la Unidad 3, en el orden en que conviene resolverlos.

- **[Laboratorio TCL](/bbdd-aplicadas/unidad-3/practica/laboratorio-tcl/)** · 13 ejercicios — diez ejercicios de una sesión sobre transacciones, savepoints, errores y `XACT_ABORT`, y un laboratorio guiado con tarjeta de crédito (dirty read, `REPEATABLE READ`, `SERIALIZABLE`). Requiere: [Control de transacciones (TCL)](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/); la parte 2 requiere además [Concurrencia, bloqueos y transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/).
- **[Laboratorio de niveles de aislamiento](/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento/)** · 12 ejercicios — fenómenos de concurrencia, `SNAPSHOT` y RCSI con dos sesiones; locks, versiones de fila, deadlock y transacciones distribuidas. Requiere: [Concurrencia, bloqueos y transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/), [Control de transacciones (TCL)](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/).
- **[Práctica de rendimiento](/bbdd-aplicadas/unidad-3/practica/rendimiento/)** · 20 ejercicios — índices, plan de ejecución, estadísticas, optimización de consultas, columnstore y métricas, con resoluciones y resultados obtenidos en SQL Server 2022. Requiere: [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/), [Plan de ejecución y estadísticas](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/), [Métricas de rendimiento](/bbdd-aplicadas/unidad-3/teoria/metricas-de-rendimiento/).

Los experimentos con dos o más sesiones y los de MS DTC se presentan como guion y no se probaron en un motor; ver el aviso de cada laboratorio. Cada práctica indica al comienzo en qué base trabaja y qué script ejecutar antes. Trabajá siempre en una **base de práctica**, nunca con datos reales; qué es, cómo crearla, qué es una «preparación» y cómo abrir dos sesiones está en [Cómo estudiar · Antes de ejecutar los ejemplos](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos).

Volvé a la [ruta de la unidad](/bbdd-aplicadas/unidad-3/teoria/).
