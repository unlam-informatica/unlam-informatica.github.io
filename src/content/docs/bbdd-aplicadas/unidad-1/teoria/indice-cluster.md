---
title: Índice Clustered
slug: bbdd-aplicadas/unidad-1/teoria/indice-cluster
sidebar:
  hidden: true
---

En SQL Server, la `PRIMARY KEY` de una tabla crea por defecto un **índice clúster**: la tabla queda almacenada como un árbol B+ ordenado por esa clave, y las filas completas están en las hojas. Para `INT IDENTITY` esto significa que las inserciones entran casi siempre al final del índice.

Este tema pertenece a la Unidad 3 y se desarrolla en [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/): heap frente a clúster, clave del clúster y uniquifier, inserción y *page splits* (con la comparación entre `IDENTITY` y `NEWID()`), índices no clúster, cobertura y mantenimiento. Todos los ejemplos ahí se ejecutan y miden en el motor.

El registro de transacciones, el *write-ahead logging* y la recuperación REDO/UNDO que acompañan a cada inserción se explican en la Unidad 5: [Registro de transacciones y modelos de recuperación](/bbdd-aplicadas/unidad-5/teoria/log-recuperacion/).
