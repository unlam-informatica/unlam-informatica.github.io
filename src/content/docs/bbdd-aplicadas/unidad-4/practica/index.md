---
title: Unidad 4 — Práctica
slug: bbdd-aplicadas/unidad-4/practica
sidebar:
  order: 0
  label: Presentación
---
Prácticas de la Unidad 4 sobre bases de datos no relacionales con MongoDB. Los tres conjuntos de datos son propios, están publicados en este sitio y todos los ejercicios tienen resolución y resultado esperado verificados con MongoDB 7.0.

## Prácticas

| Práctica | Qué se trabaja | Nivel | Ejercicios |
|---|---|---|---:|
| [Práctica — Unidad 4 NoSQL / MongoDB](/bbdd-aplicadas/unidad-4/practica/ejercicios/) | Ventas de una ferretería: filtros con operadores de arrays y fechas, proyección y orden, validación, `upsert` y `bulkWrite`, índices con `explain`, `$group`, `$lookup`, `$facet`, `$bucket` y vistas | Inicial a avanzado | 13 |
| [Laboratorio Práctico — tienda_online](/bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online/) | Tienda en línea: decimales exactos, actualizaciones con pipeline, uniones con `$lookup`, resúmenes con `$facet` y `$bucket`, índices único, compuesto y TTL | Inicial a avanzado | 7 |
| [Integrador — Películas y Préstamos](/bbdd-aplicadas/unidad-4/practica/integrador-peliculas/) | Videoclub: campos ausentes y nulos, conversión de fechas, retrasos con `$dateDiff`, integridad referencial, índices multiclave y vistas | Inicial a avanzado | 7 |

## Cómo usar los archivos

Cada práctica publica sus datos en formato JSON extendido y un script de preparación para `mongosh`. Descargá los archivos en una carpeta, ajustá la ruta `dir` del script y cargalos en una base vacía. Los ejercicios que modifican datos indican cuándo volver a cargar.

[Consultar la teoría de la unidad](/bbdd-aplicadas/unidad-4/teoria/).
