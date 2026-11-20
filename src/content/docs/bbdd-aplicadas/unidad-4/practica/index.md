---
title: Unidad 4 — Práctica
slug: bbdd-aplicadas/unidad-4/practica
sidebar:
  order: 0
  label: Índice de prácticas
---
Prácticas de la Unidad 4 sobre bases de datos no relacionales con MongoDB.

## Prácticas

Resolvelas en este orden. Todas requieren un servidor MongoDB 7.0 o posterior con `mongosh` ([instalación y conexión](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/)).

- **[Práctica — Unidad 4 NoSQL / MongoDB](/bbdd-aplicadas/unidad-4/practica/ejercicios/)** · 13 ejercicios — ventas de una ferretería. Los ejercicios 1 a 7 trabajan CRUD y consultas (filtros con operadores de arrays y fechas, proyección y orden, validación, `upsert` y `bulkWrite`); del 8 al 13, agregación (`$group`, `$lookup`, `$facet`), un índice con `explain` y una vista. Requiere: [CRUD y consultas](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/), [Aggregation Pipeline, índices y vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/).
- **[Laboratorio — Tienda online](/bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online/)** · 7 ejercicios — decimales exactos y actualizaciones con pipeline (14 y 15, CRUD), uniones con `$lookup` y resúmenes con `$facet` y `$bucket` (16 a 18 y 26), e índices único, compuesto y TTL (19). Requiere: [CRUD y consultas](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/), [Aggregation Pipeline, índices y vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/).
- **[Integrador — Películas y Préstamos](/bbdd-aplicadas/unidad-4/practica/integrador-peliculas/)** · 7 ejercicios — campos ausentes y nulos y conversión de fechas (20 y 21, CRUD), retrasos con `$dateDiff`, integridad referencial y rankings (22 a 24 y 27), índices multiclave y vistas (25). Requiere: [CRUD y consultas](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/), [Aggregation Pipeline, índices y vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/).

Los tres conjuntos de datos son propios, están publicados en este sitio y todos los ejercicios tienen resolución y resultado esperado; los resultados se obtuvieron con MongoDB 7.0.

## Cómo usar los archivos

Cada práctica publica sus datos en formato JSON extendido y un script de preparación para `mongosh`. Descargá los archivos en una carpeta, ajustá la ruta `dir` del script y cargalos en una base vacía de práctica (en MongoDB una base se crea al insertar el primer documento, así que alcanza con `use nombreBase` y ejecutar el script de preparación; no uses una base con datos reales). Los ejercicios que modifican datos indican cuándo volver a cargar.

Volvé a la [ruta de la unidad](/bbdd-aplicadas/unidad-4/teoria/).
