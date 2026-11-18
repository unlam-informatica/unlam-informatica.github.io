---
title: Unidad 4 — Teoría
slug: bbdd-aplicadas/unidad-4/teoria
sidebar:
  order: 0
  label: Presentación
---
Resúmenes teóricos y guías de referencia de la Unidad 4.

## Bases de datos no relacionales

Modelos de datos heterogéneos (jerárquicos, de texto, de grafos), BASE y ACID, bases clave-valor, columnares y de documentos, MongoDB Query Language (MQL), inserción masiva, `upsert`, agregación, estadísticas de ejecución e índices, relación con la programación orientada a objetos, data lakes, introducción al data mining y KDD.

El programa 2024 denomina la unidad «Bases de datos no relacionales»; el programa anterior la llamaba «no transaccionales». Esa denominación no debe interpretarse como «sin transacciones»: MongoDB admite transacciones multidocumento con garantías ACID (desde la versión 4.0 en conjuntos de réplicas y la 4.2 en clústeres con particionado). El foco está en los modelos NoSQL, la distribución y la consistencia configurable.

:::note[Evaluación]
En el esquema 2024 hay **un único parcial sobre las unidades 1 a 4**. La Unidad 4 se evalúa junto con las anteriores; la [guía para el parcial](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/) lista los ejes que conviene repasar.
:::

**Ruta sugerida:** [conceptos NoSQL](/bbdd-aplicadas/unidad-4/teoria/nosql-conceptos/) → MongoDB (introducción, CRUD, agregación e índices) → [POO y bases de datos](/bbdd-aplicadas/unidad-4/teoria/poo-y-bases/) → [datos, data lake y KDD](/bbdd-aplicadas/unidad-4/teoria/datos-data-lake-kdd/) → práctica de MongoDB → [guía para el parcial](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/). El [resumen integrador](/bbdd-aplicadas/unidad-4/teoria/apunte-completo/) sirve para ver el conjunto antes de empezar y para repasar al final.

### Antes de comenzar

Conviene repasar la arquitectura de las bases transaccionales, las propiedades ACID, el control de concurrencia y las transacciones (Unidades 2 y 3). Son el punto de comparación para comprender BASE y CAP.

### Resultados de aprendizaje

Al finalizar la unidad deberías poder:

- identificar cuándo un problema justifica un modelo NoSQL y seleccionar el tipo adecuado, con los matices de ACID, BASE y CAP;
- modelar documentos BSON y operar MongoDB con MQL, Compass y Aggregation Pipeline;
- medir el efecto de los índices con `explain()` y construir vistas de solo lectura;
- explicar el desajuste de impedancia objeto-relacional y decidir cuándo embeber y cuándo referenciar;
- distinguir un data warehouse de un data lake, y ubicar la minería de datos dentro del proceso KDD de cinco etapas;
- explicar decisiones técnicas, costos y límites con criterio profesional, y resolver y comunicar una solución individualmente o en equipo, incorporando herramientas nuevas de manera autónoma.

## Teoría

| Página | Contenido |
|---------|-----------|
| [Unidad 4 — Bases de datos no relacionales](/bbdd-aplicadas/unidad-4/teoria/apunte-completo/) | Resumen integrador: recorre todos los temas de la unidad y enlaza a cada página temática |
| [NoSQL — Conceptos y modelos](/bbdd-aplicadas/unidad-4/teoria/nosql-conceptos/) | Surgimiento de NoSQL, modelos jerárquico, de texto y de grafos, ACID y BASE, teorema CAP con sus matices, y los modelos clave-valor, de documentos, de grafos y de columnas |
| [MongoDB — Introducción](/bbdd-aplicadas/unidad-4/teoria/mongodb-introduccion/) | Documentos BSON, tipos de datos, `_id` y `ObjectId`, esquema y validación, `mongosh`, bases y colecciones |
| [MongoDB — CRUD y consultas](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/) | Inserción (`ordered`), `find()` y sus operadores, fechas, proyección, `sort`, actualización con `upsert`, `replaceOne()`, eliminación y `bulkWrite()` |
| [MongoDB — Aggregation Pipeline, Índices y Vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/) | Etapas del pipeline, `$lookup`, `$group`, fechas, vistas, y los índices con `explain()`, consultas cubiertas e `hint()` |
| [MongoDB Compass](/bbdd-aplicadas/unidad-4/teoria/mongodb-compass/) | La interfaz gráfica oficial: conexión, filtros, importación, pipeline visual, índices y plan de ejecución |
| [POO y bases de datos](/bbdd-aplicadas/unidad-4/teoria/poo-y-bases/) | Desajuste de impedancia, correspondencia objeto-relacional y objeto-documental (embeber o referenciar), ORM y ODM |
| [Datos, Data Lake y KDD](/bbdd-aplicadas/unidad-4/teoria/datos-data-lake-kdd/) | Datos estructurados, semiestructurados y no estructurados, data warehouse y ETL, data lake y ELT, y el proceso KDD en cinco etapas |
| [Instalación y conexión de MongoDB](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/) | Material de apoyo para el laboratorio: `mongod`, `mongosh`, Compass y Atlas sin publicar credenciales |
| [Guía para el parcial — Unidad 4](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/) | Comparaciones que hay que dominar, cómo leer una consulta y un pipeline, preguntas con respuesta y simulacro |

## Práctica

[Ir a los ejercicios y laboratorios de la unidad](/bbdd-aplicadas/unidad-4/practica/).
