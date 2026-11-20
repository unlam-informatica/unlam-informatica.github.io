---
title: 'Unidad 2 — Bases de datos relacionales: aspectos básicos'
description: "Arquitectura, instalación y configuración de un motor relacional, y manejo de formatos de intercambio (JSON, XML, CSV) e importación de datos en SQL Server."
slug: bbdd-aplicadas/unidad-2/teoria
sidebar:
  hidden: true
  label: Presentación y ruta
---
Esta unidad pasa del SQL que se escribe sobre una base al motor que la sostiene: cómo está armado un motor relacional, qué decisiones hay que tomar al instalarlo (ubicación de archivos, memoria, collation, acceso) y cómo entran y salen los datos (conexión, formatos de intercambio, importación). Se apoya en el SQL de la [Unidad 1](/bbdd-aplicadas/unidad-1/teoria/) y prepara la Unidad 3, donde se estudian transacciones, concurrencia y rendimiento.

## Objetivos de aprendizaje

Al terminar la unidad deberías poder:

- Describir instancia, servicios, archivos de datos y de log, y arquitecturas distribuidas.
- Planificar e instalar una instancia de SQL Server y configurar su acceso, local y remoto.
- Identificar `master`, `model`, `msdb`, `tempdb` y la base de recursos, y su función.
- Elegir y aplicar collations y resolver conflictos entre bases.
- Comparar el almacenamiento en disco y en memoria, y las tablas temporales, las variables de tabla y las tablas en memoria.
- Explicar el papel de un driver y usar ODBC y JDBC.
- Reconocer la estructura y los usos de CSV, ancho fijo, XML, JSON y YAML, y leer y generar XML y JSON desde T-SQL.
- Explicar qué es una API REST.
- Importar CSV, JSON y XML con `BULK INSERT` y `OPENROWSET` usando tablas de staging.

## Antes de comenzar

- **Conviene repasar:** [Repaso de SQL](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/) (DDL, DML, restricciones, procedimientos) y, si hace falta, [Conceptos básicos](/bbdd-aplicadas/unidad-1/teoria/conceptos-basicos/) (qué es un DBMS y cómo se despliega).
- **Herramientas:** una instancia de SQL Server 2022 (la mayoría de los ejemplos y ejercicios se ejecutan allí) y acceso a una carpeta del servidor para los archivos de las prácticas de importación. Ver [Cómo estudiar · Herramientas](/bbdd-aplicadas/como-estudiar/#herramientas).

## Ruta de aprendizaje

Seguí las etapas en orden. Cada una indica qué leer y, cuando existe, qué practicar antes de pasar a la siguiente.

Las diez páginas de teoría no tienen el mismo peso ni el mismo tipo de trabajo:

- **Con práctica dedicada:** collation (retomada en el TP 2), JSON en SQL Server, XML en SQL Server e importación de archivos. Se dominan resolviendo sus prácticas y el TP 2.
- **Con ejercicios dentro de la lección:** arquitectura e instalación, bases de sistema, conexión y drivers, formatos de intercambio y «Qué es una API». Son temas del programa tan evaluables como los anteriores; leelas con atención y resolvé los ejercicios que traen.
- **Complementario:** In-Memory OLTP y las llamadas HTTP desde T-SQL. No forman parte del programa 2024.

### 1. Arquitectura e instalación de un motor relacional

Qué es una base transaccional, cómo se organiza un motor (instancia, servicios, archivos), las arquitecturas distribuidas y qué decidir al instalar.

- **Leé:** [Arquitectura e instalación de un motor relacional](/bbdd-aplicadas/unidad-2/teoria/bd-transaccionales/)
- **Practicá:** ejercicios 47 y 55 incluidos al final de la lección.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-2/teoria/bd-transaccionales/#autoevaluación)

### 2. Bases de datos de sistema y de usuario

Qué guarda cada base que trae la instancia y por qué `tempdb` condiciona el almacenamiento.

- **Leé:** [Bases de datos de sistema y de usuario](/bbdd-aplicadas/unidad-2/teoria/bases-de-sistema/)
- **Practicá:** ejercicios 48 y 49 incluidos al final de la lección.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-2/teoria/bases-de-sistema/#autoevaluación)

### 3. Collation

Cómo se guardan, comparan y ordenan los textos, y cómo resolver los conflictos entre bases.

- **Leé:** [Collation / Intercalación](/bbdd-aplicadas/unidad-2/teoria/collation/)
- **Practicá:** ejercicios 50 a 52 incluidos al final de la lección. Los ejercicios de collation del [TP 2](/bbdd-aplicadas/unidad-2/practica/tp2/) los retomás en la etapa 11.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-2/teoria/collation/#autoevaluación)

### 4. Almacenamiento en disco y en memoria

Compara el almacenamiento en disco con el almacenamiento en memoria, y distingue las tablas variables, las temporales y las tablas en memoria.

- **Leé:** [BD en memoria](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/), desde [Bases de datos en memoria y en disco](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/#bases-de-datos-en-memoria-y-en-disco) hasta [Tablas variables, temporales y en memoria](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/#tablas-variables-temporales-y-en-memoria). Frená antes de «In-Memory OLTP».

### 5. In-Memory OLTP (complementario)

*Complementario: no forma parte del programa 2024; podés saltearlo en una primera lectura.*

- **Leé:** la sección [In-Memory OLTP](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/#in-memory-oltp) de la misma página.
- **Practicá:** [Práctica — BD en memoria (In-Memory OLTP)](/bbdd-aplicadas/unidad-2/practica/bd-en-memoria/) (ejercicios 41 a 46, íntegramente complementaria).
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/#autoevaluación)

### 6. Conexión, drivers, ODBC y JDBC

Cómo una aplicación llega al motor: driver, ODBC, JDBC, OLE DB, cadena de conexión, protocolos y puerto.

- **Leé:** [Conexión, drivers, ODBC y JDBC](/bbdd-aplicadas/unidad-2/teoria/formatos-conectividad/)
- **Practicá:** ejercicios 53 y 54 incluidos al final de la lección.

### 7. Formatos de intercambio y qué es una API

Los formatos con los que dos sistemas acuerdan cómo escribir un dato (EDI, CSV, ancho fijo, XML, JSON, YAML) y qué es una API.

- **Leé:** [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/) y la sección [Qué es una API](/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql/#qué-es-una-api), la primera de «APIs desde SQL Server» (el resto de esa página es complementario y se ve en la etapa 12).
- **Practicá:** ejercicio 1 de la [Práctica — APIs desde SQL Server](/bbdd-aplicadas/unidad-2/practica/apis/), que es conceptual y corresponde a «Qué es una API».
- **Comprobá:** [autoevaluación de formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/#autoevaluación)

### 8. JSON en SQL Server

Validar, consultar, convertir en filas, modificar y generar JSON desde T-SQL.

- **Leé:** [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/)
- **Practicá:** [Práctica — JSON en SQL Server](/bbdd-aplicadas/unidad-2/practica/json/) (7 ejercicios)
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/#autoevaluación)

### 9. XML en SQL Server

Guardar XML en el tipo `xml`, consultarlo, leerlo con `OPENXML` y generarlo con `FOR XML`.

- **Leé:** [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/)
- **Practicá:** [Práctica — XML en SQL Server](/bbdd-aplicadas/unidad-2/practica/xml/) (7 ejercicios)
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/#autoevaluación)

### 10. Importación de archivos

Cargar CSV, ancho fijo, JSON y XML en tablas, con tablas de staging, validación y control de codificación.

- **Leé:** [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/)
- **Practicá:** [Práctica — Importación de archivos](/bbdd-aplicadas/unidad-2/practica/importacion-archivos/) (6 ejercicios)
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/#autoevaluación)

### 11. Integración: TP 2

Trabajo integrador sobre una red de estaciones de monitoreo (15 ejercicios): collation y sus conflictos, importación de CSV con UTF-8, validación y limpieza, tablas temporales y variables de tabla, y percentiles. Presupone las etapas 3, 4 y 10 (y los formatos de la etapa 7).

- **Practicá:** [Trabajo Práctico 2 — Collation, importación de CSV y tablas temporales](/bbdd-aplicadas/unidad-2/practica/tp2/). El ejercicio 15 necesita permiso `CREATE DATABASE` y dos sesiones (dos ventanas de consulta), y no se probó en un motor.
- **Comprobá:** [autoevaluación del TP 2](/bbdd-aplicadas/unidad-2/practica/tp2/#autoevaluación)

### 12. Invocaciones HTTP desde T-SQL (complementario)

*Complementario: no forma parte del programa 2024; podés saltearlo en una primera lectura.*

- **Leé:** [Procesar la respuesta de una API desde T-SQL](/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql/#procesar-la-respuesta-de-una-api-desde-t-sql) y las secciones siguientes de [APIs desde SQL Server](/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql/).
- **Practicá:** ejercicios 2 a 5 de la [Práctica — APIs desde SQL Server](/bbdd-aplicadas/unidad-2/practica/apis/). El ejercicio 5 usa Ole Automation Procedures: leé antes el aviso de seguridad de la práctica.
- **Comprobá:** [autoevaluación de la lección](/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql/#autoevaluación)

## Ejercicios y laboratorios

- **[Práctica — JSON en SQL Server](/bbdd-aplicadas/unidad-2/practica/json/)** · 7 ejercicios — validación, consulta, modificación y generación de JSON.
- **[Práctica — XML en SQL Server](/bbdd-aplicadas/unidad-2/practica/xml/)** · 7 ejercicios — `FOR XML`, `.nodes()`, `OPENXML` e importación de un archivo XML.
- **[Práctica — Importación de archivos](/bbdd-aplicadas/unidad-2/practica/importacion-archivos/)** · 6 ejercicios — `BULK INSERT` y `OPENROWSET` con CSV y JSON.
- **[Trabajo Práctico 2 — Collation, importación de CSV y tablas temporales](/bbdd-aplicadas/unidad-2/practica/tp2/)** · 15 ejercicios — collation, importación de CSV, validación, temporales y percentiles.
- **[Práctica — BD en memoria (In-Memory OLTP)](/bbdd-aplicadas/unidad-2/practica/bd-en-memoria/)** · 6 ejercicios (complementario).
- **[Práctica — APIs desde SQL Server](/bbdd-aplicadas/unidad-2/practica/apis/)** · 5 ejercicios (el 1 es del programa; del 2 al 5, complementarios).

Ver el [índice de prácticas](/bbdd-aplicadas/unidad-2/practica/).

## Autoevaluación y repaso

Las lecciones terminan en una autoevaluación (enlazadas en la ruta) y el TP 2 también. La unidad no tiene resumen integrador ni guía de examen: el repaso son esas autoevaluaciones y las prácticas.

## Continuar

Cuando puedas resolver las prácticas de JSON, XML e importación y el TP 2 sin mirar la resolución, seguí con la [Unidad 3 — Bases de datos relacionales: aspectos avanzados](/bbdd-aplicadas/unidad-3/teoria/).

:::note[Dónde quedó el resto]
El aislamiento, los bloqueos y los niveles de aislamiento se estudian en la [Unidad 3](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/); data warehouse y data lake, en la [Unidad 4](/bbdd-aplicadas/unidad-4/teoria/datos-data-lake-kdd/); y Always On, en la [Unidad 5](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/).
:::

:::note[Páginas trasladadas]
[Práctica — Transacciones](/bbdd-aplicadas/unidad-2/practica/transacciones/) se conserva para no romper enlaces antiguos: el tema pertenece a la Unidad 3 y se practica en el [Laboratorio TCL](/bbdd-aplicadas/unidad-3/practica/laboratorio-tcl/) y el [Laboratorio de niveles de aislamiento](/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento/).
:::
