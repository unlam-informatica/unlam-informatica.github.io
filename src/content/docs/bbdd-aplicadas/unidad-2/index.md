---
title: Unidad 2
slug: bbdd-aplicadas/unidad-2
sidebar:
  order: 3
---

## BD Transaccionales: aspectos básicos · 1er parcial

Bases de datos transaccionales (OLTP), propiedades ACID, commit/rollback, OLTP vs OLAP. BD vs Data Warehouse vs Data Lake. Arquitectura distribuida y clústeres. Motor SQL Server: instalación, SSMS, Configuration Manager, conexión remota, autenticación. Collation / intercalación. BD en memoria (In-Memory OLTP). ODBC y JDBC. Formatos de intercambio: EDI, CSV, XML, JSON, YAML. APIs REST.

## Teoría

| Archivo | Tema |
|---------|------|
| [bd-transaccionales](/bbdd-aplicadas/unidad-2/teoria/bd-transaccionales/) | OLTP, ACID, concurrencia, niveles de aislamiento, OLAP, DWH, SQL Server motor |
| [bd-en-memoria](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/) | Tablas en memoria (In-Memory OLTP): configuración, índices, comparativa |
| [collation](/bbdd-aplicadas/unidad-2/teoria/collation/) | Collation en SQL Server: sensibilidades, niveles, consultas y cláusula COLLATE |
| [formatos-conectividad](/bbdd-aplicadas/unidad-2/teoria/formatos-conectividad/) | ODBC/JDBC, formatos EDI/CSV/XML/JSON/YAML, APIs REST |
| [formatos-de-intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/) | EDI, CSV, XML, JSON, YAML: ejemplos y operaciones T-SQL |
| [json-en-sql](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/) | OPENJSON, FOR JSON, JSON_VALUE/QUERY/MODIFY: parseo y generación de JSON |
| [xml-en-sql](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/) | Importar XML con OPENROWSET + .nodes(), OPENXML y exportar con FOR XML |
| [importacion-de-archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/) | BULK INSERT (CSV) y OPENROWSET + OPENJSON (JSON): sintaxis y opciones |
| [apis-desde-sql](/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql/) | Llamadas HTTP desde T-SQL con Ole Automation Procedures: GET y POST |

## Práctica

| Archivo | Tema |
|---------|------|
| [importacion-archivos](/bbdd-aplicadas/unidad-2/practica/importacion-archivos/) | 4 ejercicios de importación: 3 CSV (datos abiertos) + 1 JSON |
| [tp2](/bbdd-aplicadas/unidad-2/practica/tp2/) | TP2: collation, importación de CSVs, percentiles, tablas temporales globales |
| [transacciones](/bbdd-aplicadas/unidad-2/practica/transacciones/) | BEGIN/COMMIT/ROLLBACK, TRY/CATCH, SAVEPOINT, XACT_ABORT, aislamiento |
| [json](/bbdd-aplicadas/unidad-2/practica/json/) | OPENJSON, JSON_VALUE/QUERY/MODIFY, FOR JSON PATH/AUTO |
| [xml](/bbdd-aplicadas/unidad-2/practica/xml/) | FOR XML RAW/AUTO, .nodes()/.value(), OPENXML, subconsultas anidadas |
| [bd-en-memoria](/bbdd-aplicadas/unidad-2/practica/bd-en-memoria/) | Crear filegroup, tablas MEMORY_OPTIMIZED, comparativa disco vs. memoria |
| [apis](/bbdd-aplicadas/unidad-2/practica/apis/) | GET/POST con sp_OACreate, parseo de respuestas JSON, persistir resultados |
