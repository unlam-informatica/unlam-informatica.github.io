---
title: Unidad 4 — Bases de datos no relacionales
slug: bbdd-aplicadas/unidad-4/teoria
description: "Modelos NoSQL, MongoDB (CRUD, agregación e índices), relación con POO, data lakes y KDD: ruta de estudio, prácticas y repaso para el parcial."
sidebar:
  hidden: true
  label: Presentación y ruta
---

Esta unidad estudia las bases de datos no relacionales: qué modelos existen, cuándo conviene cada uno y cómo se trabaja con MongoDB, la base orientada a documentos que se usa en la materia. Es el contrapunto de las unidades 2 y 3: las garantías ACID, el control de concurrencia y las transacciones son el punto de comparación para comprender BASE y CAP.

El programa 2024 denomina la unidad «Bases de datos no relacionales»; el programa anterior la llamaba «no transaccionales». Esa denominación no debe interpretarse como «sin transacciones»: MongoDB admite transacciones multidocumento con garantías ACID (desde la versión 4.0 en conjuntos de réplicas y la 4.2 en clústeres con particionado). El foco está en los modelos NoSQL, la distribución y la consistencia configurable.

:::note[Evaluación]
En el esquema 2024 hay **un único parcial sobre las unidades 1 a 4**. La Unidad 4 se evalúa junto con las anteriores y con ella se completa el temario del parcial; la [guía para el parcial](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/) lista los ejes que conviene repasar.
:::

## Objetivos de aprendizaje

Al terminar la unidad deberías poder:

- identificar cuándo un problema justifica un modelo NoSQL y seleccionar el tipo adecuado, con los matices de ACID, BASE y CAP;
- modelar documentos BSON y operar MongoDB con MQL, Compass y Aggregation Pipeline;
- medir el efecto de los índices con `explain()` y construir vistas de solo lectura;
- explicar el desajuste de impedancia objeto-relacional y decidir cuándo embeber y cuándo referenciar;
- distinguir un data warehouse de un data lake, y ubicar la minería de datos dentro del proceso KDD de cinco etapas;
- explicar decisiones técnicas, costos y límites con criterio profesional, y resolver y comunicar una solución individualmente o en equipo, incorporando herramientas nuevas de manera autónoma.

## Antes de comenzar

- **Conviene repasar:** la arquitectura de las bases transaccionales, las propiedades ACID, el control de concurrencia y las transacciones, en la [Unidad 2](/bbdd-aplicadas/unidad-2/teoria/) y la [Unidad 3](/bbdd-aplicadas/unidad-3/teoria/).
- **Herramientas:** un servidor MongoDB 7.0 o posterior con `mongosh` (o un clúster gratuito de Atlas); Compass es opcional. La [instalación](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/) es el paso 3 de la ruta, y solo hace falta cuando vayas a ejecutar código. Más opciones en [Cómo estudiar · Herramientas](/bbdd-aplicadas/como-estudiar/#herramientas).

## Ruta de aprendizaje

Seguí las etapas en orden. Cada una indica qué leer y, cuando existe, qué practicar antes de pasar a la siguiente. El [resumen integrador](/bbdd-aplicadas/unidad-4/teoria/apunte-completo/) sirve como vista general antes de empezar.

### 1. Conceptos y modelos NoSQL

Por qué surgió NoSQL, qué tipos de datos maneja, los modelos jerárquico, de texto y de grafos, ACID frente a BASE, el teorema CAP y los cuatro modelos de almacenamiento (clave-valor, documentos, grafos y columnas).

- **Leé:** [NoSQL — Conceptos y modelos](/bbdd-aplicadas/unidad-4/teoria/nosql-conceptos/)
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-4/teoria/nosql-conceptos/#autoevaluación)

### 2. MongoDB: documentos y BSON

El modelo de datos de MongoDB: documentos BSON, tipos, `_id` y `ObjectId`, esquema y validación, `mongosh`, bases y colecciones.

- **Leé:** [MongoDB — Introducción](/bbdd-aplicadas/unidad-4/teoria/mongodb-introduccion/)
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-4/teoria/mongodb-introduccion/#autoevaluación)

### 3. Preparar el entorno

Material de apoyo: no es un tema evaluable, pero las etapas siguientes se practican sobre un servidor propio o un clúster de Atlas.

- **Leé:** [Instalación y conexión de MongoDB](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/)
- **Comprobá:** [checklist de laboratorio](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/#checklist-de-laboratorio)

### 4. CRUD y consultas

Insertar, consultar con `find()` y sus operadores, actualizar (incluido `upsert`), reemplazar, eliminar y combinar escrituras con `bulkWrite()`.

- **Leé:** [MongoDB — CRUD y consultas](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/)
- **Practicá:** [Práctica — Unidad 4 NoSQL / MongoDB](/bbdd-aplicadas/unidad-4/practica/ejercicios/), ejercicios 1 a 7; en el [laboratorio de la tienda online](/bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online/), los ejercicios 14 y 15; en el [integrador de películas](/bbdd-aplicadas/unidad-4/practica/integrador-peliculas/), los ejercicios 20 y 21.
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/#autoevaluación)

### 5. Aggregation Pipeline y vistas

Procesar documentos por etapas: `$match`, `$group`, `$lookup`, fechas y vistas de solo lectura. Presupone el CRUD de la etapa anterior.

- **Leé:** [MongoDB — Aggregation Pipeline, Índices y Vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/), secciones [Aggregation Pipeline](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#aggregation-pipeline), [Fechas en el pipeline](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#fechas-en-el-pipeline) y [Vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#vistas)
- **Practicá:** ejercicios 8, 9, 11, 12 y 13 de la [práctica de la unidad](/bbdd-aplicadas/unidad-4/practica/ejercicios/); 16, 17, 18 y 26 del [laboratorio de la tienda online](/bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online/); 22, 23, 24 y 27 del [integrador de películas](/bbdd-aplicadas/unidad-4/practica/integrador-peliculas/).

### 6. Índices y `explain()`

Cuándo ayuda un índice, qué tipos hay y cómo medir su efecto con las estadísticas de ejecución.

- **Leé:** [Índices y estadísticas de ejecución](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#índices-y-estadísticas-de-ejecución), en la misma página que el pipeline.
- **Practicá:** ejercicio 10 de la [práctica de la unidad](/bbdd-aplicadas/unidad-4/practica/ejercicios/), 19 del [laboratorio de la tienda online](/bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online/) y 25 del [integrador de películas](/bbdd-aplicadas/unidad-4/practica/integrador-peliculas/).
- **Comprobá:** [autoevaluación de la página de agregación e índices](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#autoevaluación)

### 7. MongoDB Compass

La interfaz gráfica oficial como herramienta de apoyo: cada operación tiene su equivalente en `mongosh`, que ya conocés de las etapas anteriores.

- **Leé:** [MongoDB Compass](/bbdd-aplicadas/unidad-4/teoria/mongodb-compass/)
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-4/teoria/mongodb-compass/#autoevaluación)

### 8. Consolidar con ejercicios y laboratorios

Resolvé completas las tres prácticas, en este orden, y compará cada resolución con la tuya: [práctica de ventas](/bbdd-aplicadas/unidad-4/practica/ejercicios/), [laboratorio de la tienda online](/bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online/) e [integrador de películas](/bbdd-aplicadas/unidad-4/practica/integrador-peliculas/). Presuponen CRUD, agregación e índices, y el entorno de la etapa 3.

### 9. Relación con la programación orientada a objetos

Desajuste de impedancia, correspondencia objeto-relacional y objeto-documental (embeber o referenciar), ORM y ODM.

- **Leé:** [POO y bases de datos](/bbdd-aplicadas/unidad-4/teoria/poo-y-bases/)
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-4/teoria/poo-y-bases/#autoevaluación)

### 10. Data lakes, data mining y KDD

Datos estructurados, semiestructurados y no estructurados, data warehouse y ETL, data lake y ELT, y el proceso KDD en cinco etapas.

- **Leé:** [Datos, Data Lake y KDD](/bbdd-aplicadas/unidad-4/teoria/datos-data-lake-kdd/)
- **Comprobá:** [autoevaluación](/bbdd-aplicadas/unidad-4/teoria/datos-data-lake-kdd/#autoevaluación)

### 11. Repaso para el parcial

- **Leé:** [Guía para el parcial — Unidad 4](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/): comparaciones que hay que dominar, cómo leer una consulta y un pipeline, preguntas con respuesta y simulacro.

## Ejercicios y laboratorios

- **[Práctica — Unidad 4 NoSQL / MongoDB](/bbdd-aplicadas/unidad-4/practica/ejercicios/)** · 13 ejercicios — ventas de una ferretería: CRUD, validación, índices, agregación y vistas.
- **[Laboratorio — Tienda online](/bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online/)** · 7 ejercicios — decimales exactos, `$lookup`, `$facet`, `$bucket` e índices único, compuesto y TTL.
- **[Integrador — Películas y Préstamos](/bbdd-aplicadas/unidad-4/practica/integrador-peliculas/)** · 7 ejercicios — campos ausentes y nulos, conversión de fechas, integridad referencial, índices multiclave y vistas.

Detalle en el [índice de prácticas](/bbdd-aplicadas/unidad-4/practica/).

## Autoevaluación y repaso

- Cada lección termina con una autoevaluación, enlazada en la ruta; las de NoSQL, POO y data lake incluyen además ejercicios propios.
- El [resumen integrador](/bbdd-aplicadas/unidad-4/teoria/apunte-completo/) es una vista general antes de empezar y un repaso después; cada sección enlaza a su lección.
- La [guía para el parcial](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/) es la preparación de examen.

## Continuar

Cuando puedas resolver las prácticas sin mirar la resolución y explicar las comparaciones de la guía, habrás completado el temario del parcial (unidades 1 a 4): repasalo con la [guía para el parcial](/bbdd-aplicadas/unidad-4/teoria/guia-parcial/). Después seguí con la [Unidad 5 — Protección de los datos](/bbdd-aplicadas/unidad-5/teoria/).
