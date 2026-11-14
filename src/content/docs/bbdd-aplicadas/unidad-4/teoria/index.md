---
title: Unidad 4 — Teoría
slug: bbdd-aplicadas/unidad-4/teoria
sidebar:
  order: 0
  label: Presentación
---
Resúmenes teóricos y guías de referencia de la Unidad 4.

## BD No Transaccionales (NoSQL) · 2do parcial

NoSQL, MongoDB, MongoDB Query Language (MQL), Aggregation Pipeline, Índices, Vistas, Data Lakes, KDD.


“No transaccionales” es la denominación curricular de la unidad. No debe interpretarse como “sin transacciones”: MongoDB moderno admite garantías ACID y transacciones multidocumento. El foco está en modelos NoSQL, distribución y consistencia configurable.

**Ruta sugerida:** apunte completo → guías temáticas → ejercicios MongoDB → integrador → guía para el parcial.

### Antes de comenzar

Conviene repasar arquitectura de bases transaccionales, propiedades ACID, control de concurrencia y transacciones. Son el punto de comparación para comprender BASE y CAP.

### Resultados de aprendizaje

Al finalizar la unidad deberías poder:

- identificar cuándo un problema justifica un modelo NoSQL y seleccionar el tipo adecuado;
- modelar documentos BSON y operar MongoDB con MQL, Compass y Aggregation Pipeline;
- medir el efecto de índices y construir vistas de solo lectura;
- integrar datos heterogéneos en un flujo Data Lake/KDD;
- explicar decisiones técnicas, costos, límites e impacto con criterio profesional y responsable;
- resolver y comunicar una solución individualmente o en equipo, incorporando herramientas nuevas de manera autónoma.


## Teoría

| Apunte | Tema |
|---------|------|
| [Unidad 4 — BD No Transaccionales (NoSQL)](/bbdd-aplicadas/unidad-4/teoria/apunte-completo/) | Apunte completo de la unidad: NoSQL, MongoDB, MQL, Aggregation Pipeline, Data Lakes, KDD |
| [NoSQL — Conceptos y modelos](/bbdd-aplicadas/unidad-4/teoria/nosql-conceptos/) | Qué es NoSQL, por qué existe, los cuatro modelos de almacenamiento |
| [MongoDB — Introducción](/bbdd-aplicadas/unidad-4/teoria/mongodb-introduccion/) | BSON, terminología, tipos de datos, ObjectId, schema, shell, bases y colecciones |
| [MongoDB — CRUD y consultas](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/) | Operaciones CRUD: inserción, `find()` y sus operadores, actualización y eliminación |
| [MongoDB — Aggregation Pipeline, Índices y Vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/) | Aggregation Pipeline, gestión de índices y creación de vistas |
| [MongoDB Compass](/bbdd-aplicadas/unidad-4/teoria/mongodb-compass/) | Uso de la interfaz gráfica oficial de MongoDB |
| [Datos, Data Lake y KDD](/bbdd-aplicadas/unidad-4/teoria/datos-data-lake-kdd/) | Datos estructurados, semiestructurados y no estructurados; Data Lake, OCR, NLP y proceso KDD |
| [Instalación y conexión de MongoDB](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/) | Arquitectura `mongod`/`mongosh`, instalación, conexión local y Atlas sin publicar credenciales |
| [Guía para el parcial — Unidad 4](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/) | Mapa conceptual, comparaciones que suelen evaluarse, preguntas de parcial y autoevaluación |


## Práctica

[Ir a los ejercicios y laboratorios de la unidad](/bbdd-aplicadas/unidad-4/practica/).
