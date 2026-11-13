---
title: Bases de Datos Aplicadas — UNLaM
slug: bbdd-aplicadas
sidebar:
  order: 1
  label: Bases de Datos Aplicadas
---


Apuntes, guías de referencia y ejercicios prácticos de la cursada, organizados por unidad.

:::note[Nota]
Este sitio usa una estructura de documentación navegable con búsqueda, anclas por encabezado, tabla de contenidos lateral en páginas extensas y soporte para diagramas Mermaid y fórmulas TeX.
:::

## Contenido

### [Unidad 1 — Conceptos básicos. Repaso SQL](/bbdd-aplicadas/unidad-1/)
DDL, DML, constraints, NULL, JOINs, vistas, procedimientos almacenados, triggers, funciones de usuario, window functions, CTE, SQL dinámico, PIVOT.

### [Unidad 2 — BD Transaccionales: aspectos básicos](/bbdd-aplicadas/unidad-2/)
Arquitectura de SQL Server, instalación, ODBC/JDBC, collation.

### [Unidad 3 — BD Transaccionales: aspectos avanzados](/bbdd-aplicadas/unidad-3/)
Transacciones, ACID, concurrencia, bloqueos, índices, optimización de consultas.

### [Unidad 4 — BD No Transaccionales (NoSQL)](/bbdd-aplicadas/unidad-4/)
NoSQL, MongoDB, MongoDB Query Language, Data Lakes, KDD.

### [Unidad 5 — Protección de los datos](/bbdd-aplicadas/unidad-5/)
Seguridad, DCL, roles, backups, alta disponibilidad, réplicas.

### [Unidad 6 — Calidad en bases de datos](/bbdd-aplicadas/unidad-6/)
Calidad de datos, ISO/IEC 25012, GDPR, gobierno de datos.

## Mapa de cursada

```mermaid
flowchart LR
    U1["Unidad 1<br/>SQL y bases"] --> U2["Unidad 2<br/>Aspectos transaccionales básicos"]
    U2 --> U3["Unidad 3<br/>Transacciones, índices y optimización"]
    U3 --> U4["Unidad 4<br/>NoSQL y MongoDB"]
    U4 --> U5["Unidad 5<br/>Protección de datos"]
    U5 --> U6["Unidad 6<br/>Calidad y gobierno"]
```

---

## Bibliografía

- Elmasri, Navathe — *Fundamentos de Sistemas de Bases de Datos* · Pearson · 5ta ed. · 2007
- Silberschatz, Korth, Sudarshan — *Fundamentos de Bases de Datos* · McGraw-Hill · 4ta ed. · 2002

**Recursos online**
- [Microsoft Learn — Modern Data Warehouse](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/)
- [Microsoft Learn — Azure Data Lake Storage](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-data-lake-storage/)
- [MongoDB University — Introduction to MongoDB](https://learn.mongodb.com/learning-paths/introduction-to-mongodb)
