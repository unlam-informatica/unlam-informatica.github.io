---
title: Unidad 2 — Teoría
slug: bbdd-aplicadas/unidad-2/teoria
sidebar:
  order: 0
  label: Presentación
---
Resúmenes teóricos y guías de referencia de la Unidad 2.

## Bases de datos relacionales: aspectos básicos

Bases de datos transaccionales (OLTP), propiedades ACID a nivel conceptual y commit/rollback. Arquitectura de un motor relacional (instancia, servicios, archivos) y arquitectura distribuida y clústeres. Bases de datos de sistema y de usuario (`master`, `model`, `msdb`, `tempdb`). Instalación de SQL Server: análisis previo, ubicación de archivos, memoria, Configuration Manager, conexión remota y autenticación. Collation / intercalación. Almacenamiento en disco y en memoria (In-Memory OLTP, complementario). Conexión, drivers, ODBC y JDBC. Formatos de intercambio (EDI, CSV, XML, JSON, YAML), importación de archivos y APIs.

:::note[Dónde quedó el resto]
El aislamiento, los bloqueos y los niveles de aislamiento se estudian en la [Unidad 3](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/); data warehouse y data lake, en la [Unidad 4](/bbdd-aplicadas/unidad-4/teoria/datos-data-lake-kdd/); y Always On, en la [Unidad 5](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/).
:::

## Teoría

| Apunte | Tema |
|---------|------|
| [Arquitectura e instalación de un motor relacional](/bbdd-aplicadas/unidad-2/teoria/bd-transaccionales/) | OLTP, ACID conceptual, commit y rollback, instancia y archivos, clústeres, instalación, memoria, conexión remota, autenticación |
| [Bases de datos de sistema y de usuario](/bbdd-aplicadas/unidad-2/teoria/bases-de-sistema/) | master, model, msdb, tempdb y la base de recursos; `model` como plantilla; planificación de `tempdb` |
| [Collation / Intercalación](/bbdd-aplicadas/unidad-2/teoria/collation/) | Sensibilidades, niveles, cláusula `COLLATE`, conflictos (error 468), `DATABASE_DEFAULT`, `tempdb`, UTF-8 |
| [BD en memoria](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/) | Disco frente a memoria, tablas temporales; In-Memory OLTP (complementario) |
| [Conexión, drivers, ODBC y JDBC](/bbdd-aplicadas/unidad-2/teoria/formatos-conectividad/) | Driver, ODBC, JDBC, OLE DB, cadenas de conexión, protocolos y puerto |
| [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/) | EDI, CSV, ancho fijo, XML, JSON, YAML |
| [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/) | OPENJSON, FOR JSON, JSON_VALUE/QUERY/MODIFY: parseo y generación de JSON |
| [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/) | Importar XML con OPENROWSET + .nodes(), OPENXML y exportar con FOR XML |
| [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/) | BULK INSERT (CSV) y OPENROWSET + OPENJSON (JSON): sintaxis y opciones |
| [APIs desde SQL Server](/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql/) | Llamadas HTTP desde T-SQL con Ole Automation Procedures: GET y POST |


## Práctica

[Ir a los ejercicios y laboratorios de la unidad](/bbdd-aplicadas/unidad-2/practica/).
