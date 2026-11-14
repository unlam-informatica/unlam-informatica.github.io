---
title: Unidad 2 — Teoría
slug: bbdd-aplicadas/unidad-2/teoria
sidebar:
  order: 0
  label: Presentación
---
Resúmenes teóricos y guías de referencia de la Unidad 2.

## BD Transaccionales: aspectos básicos · 1er parcial

Bases de datos transaccionales (OLTP), propiedades ACID, commit/rollback, OLTP vs OLAP. BD vs Data Warehouse vs Data Lake. Arquitectura distribuida y clústeres. Motor SQL Server: instalación, SSMS, Configuration Manager, conexión remota, autenticación. Collation / intercalación. BD en memoria (In-Memory OLTP). ODBC y JDBC. Formatos de intercambio: EDI, CSV, XML, JSON, YAML. APIs REST.


## Teoría

| Apunte | Tema |
|---------|------|
| [Bases de datos transaccionales (OLTP)](/bbdd-aplicadas/unidad-2/teoria/bd-transaccionales/) | OLTP, ACID, concurrencia, niveles de aislamiento, OLAP, DWH, SQL Server motor |
| [BD en memoria](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/) | Tablas en memoria (In-Memory OLTP): configuración, índices, comparativa |
| [Collation / Intercalación](/bbdd-aplicadas/unidad-2/teoria/collation/) | Collation en SQL Server: sensibilidades, niveles, consultas y cláusula COLLATE |
| [Formatos y Conectividad](/bbdd-aplicadas/unidad-2/teoria/formatos-conectividad/) | ODBC/JDBC, formatos EDI/CSV/XML/JSON/YAML, APIs REST |
| [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/) | EDI, CSV, XML, JSON, YAML: ejemplos y operaciones T-SQL |
| [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/) | OPENJSON, FOR JSON, JSON_VALUE/QUERY/MODIFY: parseo y generación de JSON |
| [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/) | Importar XML con OPENROWSET + .nodes(), OPENXML y exportar con FOR XML |
| [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/) | BULK INSERT (CSV) y OPENROWSET + OPENJSON (JSON): sintaxis y opciones |
| [APIs desde SQL Server](/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql/) | Llamadas HTTP desde T-SQL con Ole Automation Procedures: GET y POST |


## Práctica

[Ir a los ejercicios y laboratorios de la unidad](/bbdd-aplicadas/unidad-2/practica/).
