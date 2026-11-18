---
title: Práctica de rendimiento
slug: bbdd-aplicadas/unidad-3/practica/rendimiento
sidebar:
  order: 3
---

[← Unidad 3](/bbdd-aplicadas/unidad-3/practica/)

Veinte ejercicios sobre índices, plan de ejecución, estadísticas, optimización de consultas, columnstore y métricas. Todos son originales, con datos sintéticos generados por fórmula, y las resoluciones se ejecutaron en SQL Server 2022.

## Qué presupone

- [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/): clúster, no clúster, cobertura, selectividad, fill factor, sargabilidad, columnstore.
- [Plan de ejecución y estadísticas](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/): operadores, plan estimado y real, histograma, actualización.
- [Métricas de rendimiento](/bbdd-aplicadas/unidad-3/teoria/metricas-de-rendimiento/): línea de base, DMV.

## Conjunto de datos

Un taller mecánico: 300 clientes y 15.000 órdenes de trabajo. `Estado` es muy desparejo (85 % `Cerrada`, 14 % `Abierta`, 1 % `Anulada`) y `Patente` es única por orden. Cada resolución se ejecuta sobre una base vacía que primero crea este conjunto, y cuando el ejercicio necesita más tablas, las trae en el enunciado.

Para comparar planes usamos dos funciones auxiliares. `diag.OperadoresDe` devuelve los operadores físicos de una sentencia marcada con un comentario (`/*X*/`) y sus lecturas lógicas (equivalente a `SET STATISTICS IO`); `diag.FilasEstimadasYReales` devuelve las filas estimadas y reales de cada operador. Se explican en [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/#datos-de-ejemplo-y-cómo-medimos) y en [Plan de ejecución y estadísticas](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/#estadísticas-desactualizadas). Los costos y tiempos de ejecución no se usan como evidencia porque cambian de un equipo a otro.

<!-- check: U3.P.RE.00 -->
```sql
CREATE SCHEMA taller;
GO
CREATE SCHEMA diag;
GO
CREATE TABLE taller.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    Ciudad    VARCHAR(20) NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE taller.Orden (
    OrdenId      INT IDENTITY(1, 1) NOT NULL,
    ClienteId    INT                NOT NULL,
    FechaIngreso DATE               NOT NULL,
    Estado       VARCHAR(12)        NOT NULL,
    Patente      VARCHAR(7)         NOT NULL,
    Total        DECIMAL(10, 2)     NOT NULL,
    CONSTRAINT PK_Orden PRIMARY KEY CLUSTERED (OrdenId)
);
GO
WITH n AS (
    SELECT TOP (300) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns
)
INSERT INTO taller.Cliente (ClienteId, Nombre, Ciudad)
SELECT n,
       CONCAT('Cliente ', RIGHT(CONCAT('000', n), 3)),
       CHOOSE(n % 3 + 1, 'La Matanza', 'Moron', 'Lomas')
FROM n;

WITH n AS (
    SELECT TOP (15000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns AS a
    CROSS JOIN sys.all_columns AS b
)
INSERT INTO taller.Orden (ClienteId, FechaIngreso, Estado, Patente, Total)
SELECT n % 300 + 1,
       DATEADD(DAY, n % 1095, '2022-01-01'),
       CASE WHEN n % 100 = 0 THEN 'Anulada' WHEN n % 7 = 0 THEN 'Abierta' ELSE 'Cerrada' END,
       CONCAT('AA', RIGHT(CONCAT('00000', n), 5)),
       n % 500 + 100.00
FROM n;
GO
ALTER DATABASE SCOPED CONFIGURATION SET LAST_QUERY_PLAN_STATS = ON;
GO
CREATE FUNCTION diag.OperadoresDe (@Marca NVARCHAR(40))
RETURNS TABLE
AS RETURN
(
    WITH XMLNAMESPACES (DEFAULT 'http://schemas.microsoft.com/sqlserver/2004/07/showplan')
    SELECT r.o.value('@NodeId', 'INT') AS NodoId,
           CASE WHEN r.o.value('(./*/@Lookup)[1]', 'INT') = 1 THEN N'Key Lookup'
                ELSE r.o.value('@PhysicalOp', 'NVARCHAR(60)') END           AS Operador,
           COALESCE(r.o.value('(./*/Object/@Index)[1]', 'NVARCHAR(128)'),
                    r.o.value('(./*/Object/@Table)[1]', 'NVARCHAR(128)'))   AS Objeto,
           qs.last_logical_reads                                            AS LecturasLogicas
    FROM sys.dm_exec_query_stats AS qs
    CROSS APPLY sys.dm_exec_plan_attributes(qs.plan_handle) AS pa
    CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) AS t
    CROSS APPLY (SELECT SUBSTRING(t.text, qs.statement_start_offset / 2 + 1,
                     (CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(t.text)
                      ELSE qs.statement_end_offset END - qs.statement_start_offset) / 2 + 1) AS Sentencia) AS s
    CROSS APPLY sys.dm_exec_text_query_plan(qs.plan_handle, qs.statement_start_offset, qs.statement_end_offset) AS p
    CROSS APPLY (SELECT CAST(p.query_plan AS XML) AS PlanXml) AS x
    CROSS APPLY x.PlanXml.nodes('//RelOp') AS r(o)
    WHERE pa.attribute = 'dbid' AND CAST(pa.value AS INT) = DB_ID()
      AND s.Sentencia LIKE N'%' + @Marca + N'%'
      AND s.Sentencia NOT LIKE N'%OperadoresDe%'
);
GO
CREATE FUNCTION diag.FilasEstimadasYReales (@Marca NVARCHAR(40))
RETURNS TABLE
AS RETURN
(
    WITH XMLNAMESPACES (DEFAULT 'http://schemas.microsoft.com/sqlserver/2004/07/showplan')
    SELECT r.o.value('@NodeId', 'INT')                                                           AS NodoId,
           r.o.value('@PhysicalOp', 'NVARCHAR(60)')                                              AS Operador,
           CAST(r.o.value('@EstimateRows', 'FLOAT') AS BIGINT)                                   AS FilasEstimadas,
           r.o.value('(./RunTimeInformation/RunTimeCountersPerThread/@ActualRows)[1]', 'BIGINT') AS FilasReales
    FROM sys.dm_exec_query_stats AS qs
    CROSS APPLY sys.dm_exec_plan_attributes(qs.plan_handle) AS pa
    CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) AS t
    CROSS APPLY (SELECT SUBSTRING(t.text, qs.statement_start_offset / 2 + 1,
                     (CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(t.text)
                      ELSE qs.statement_end_offset END - qs.statement_start_offset) / 2 + 1) AS Sentencia) AS s
    CROSS APPLY sys.dm_exec_query_plan_stats(qs.plan_handle) AS p
    CROSS APPLY p.query_plan.nodes('//RelOp') AS r(o)
    WHERE pa.attribute = 'dbid' AND CAST(pa.value AS INT) = DB_ID()
      AND s.Sentencia LIKE N'%' + @Marca + N'%'
      AND s.Sentencia NOT LIKE N'%FilasEstimadasYReales%'
);
GO
```

## Nivel inicial

### Ejercicio 1 · Heap, clúster y no clúster
<!-- ejercicio: U3.26 | nivel: inicial | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Decidí si cada afirmación es verdadera o falsa y justificá.

1. Una tabla puede tener dos índices clúster si se crean sobre columnas distintas.
2. Una tabla sin índice clúster se llama heap y se recorre con un *Table Scan*.
3. Una `PRIMARY KEY` crea siempre un índice clúster, aunque ya exista otro.
4. Un índice no clúster guarda la clave del clúster como localizador de la fila.
5. `INCLUDE` agrega columnas a la clave de búsqueda del índice y las ordena.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Recordar qué contiene cada estructura: el clúster es la tabla ordenada; el no clúster es una copia ordenada de pocas columnas más un localizador.

1. **Falso.** El clúster *es* la tabla, así que solo puede existir uno: las filas se guardan en un único orden.
2. **Verdadero.** Un heap carece de clúster y se recorre completo con *Table Scan*. Recorrer una tabla con clúster completa es un *Clustered Index Scan*.
3. **Falso.** Por defecto una `PRIMARY KEY` crea un clúster, pero si ya hay otro clúster, o si se declara `PRIMARY KEY NONCLUSTERED`, crea un índice no clúster.
4. **Verdadero.** Si la tabla tiene clúster, el localizador es su clave; si es un heap, es un identificador de fila (RID).
5. **Falso.** Las columnas de `INCLUDE` viajan en las hojas pero no forman parte de la clave ni determinan el orden; sirven para cubrir consultas.
</details>

### Ejercicio 2 · Qué índices tiene cada tabla
<!-- ejercicio: U3.27 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Con las tablas siguientes, listá para cada una los índices que tiene (`index_id`, tipo y nombre) y respondé: ¿cuál es un heap? ¿cuál tiene índice clúster? ¿qué `index_id` tiene un índice creado por una `PRIMARY KEY NONCLUSTERED`?

<!-- check: U3.27 -->
```sql
CREATE TABLE taller.Visita (
    VisitaId INT         NOT NULL,
    OrdenId  INT         NOT NULL,
    Nota     VARCHAR(50) NOT NULL
);
CREATE TABLE taller.Repuesto (
    RepuestoId  INT         NOT NULL,
    Descripcion VARCHAR(50) NOT NULL,
    CONSTRAINT PK_Repuesto PRIMARY KEY NONCLUSTERED (RepuestoId)
);
CREATE TABLE taller.Tecnico (
    TecnicoId INT         NOT NULL,
    Nombre    VARCHAR(50) NOT NULL,
    CONSTRAINT PK_Tecnico PRIMARY KEY (TecnicoId)
);
CREATE NONCLUSTERED INDEX IX_Visita_OrdenId ON taller.Visita (OrdenId);
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `sys.indexes` lista todos los índices de un objeto; `index_id` 0 es el heap, 1 el clúster y 2 o más los no clúster.

<!-- check: U3.27 -->
```sql
SELECT OBJECT_NAME(object_id) AS Tabla,
       index_id               AS IndexId,
       type_desc              AS Tipo,
       name                   AS Indice
FROM sys.indexes
WHERE object_id IN (OBJECT_ID('taller.Visita'), OBJECT_ID('taller.Repuesto'), OBJECT_ID('taller.Tecnico'))
ORDER BY Tabla, IndexId;
```

**Resultado esperado.**

| Tabla | IndexId | Tipo | Indice |
|---|---:|---|---|
| Repuesto | 0 | HEAP | NULL |
| Repuesto | 2 | NONCLUSTERED | PK_Repuesto |
| Tecnico | 1 | CLUSTERED | PK_Tecnico |
| Visita | 0 | HEAP | NULL |
| Visita | 2 | NONCLUSTERED | IX_Visita_OrdenId |

`Repuesto` y `Visita` son heaps (fila con `index_id` 0 y `NULL` como nombre): `Repuesto` tiene una `PRIMARY KEY` pero no clúster, así que su índice (`PK_Repuesto`) es no clúster con `index_id` 2; `Visita` tiene un no clúster por `OrdenId`. `Tecnico` es la única con clúster, porque una `PRIMARY KEY` sin más indicaciones crea un clúster (`index_id` 1).
</details>

### Ejercicio 3 · Un índice para buscar por patente
<!-- ejercicio: U3.28 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
En `taller.Orden` se busca seguido una orden por su patente: `WHERE Patente = 'AA00042'`. Mostrá qué operador usa el motor hoy y cuántas páginas lee, creá el índice que corresponde y mostrá cómo cambia.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Medir antes (operador y lecturas), crear un índice no clúster sobre `Patente` y medir después. Cada consulta lleva un marcador para encontrarla en el plan.

<!-- check: U3.28 -->
```sql
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE Patente = 'AA00042' /*A1*/ OPTION (MAXDOP 1);
GO
CREATE NONCLUSTERED INDEX IX_Orden_Patente ON taller.Orden (Patente);
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE Patente = 'AA00042' /*A2*/ OPTION (MAXDOP 1);
GO
SELECT 'Sin índice' AS Momento, Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*A1*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Con índice', Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*A2*/')
WHERE Objeto IS NOT NULL
ORDER BY Momento DESC;
```

**Resultado esperado.**

| Momento | Operador | Objeto | LecturasLogicas |
|---|---|---|---:|
| Sin índice | Clustered Index Scan | [PK_Orden] | 93 |
| Con índice | Index Seek | [IX_Orden_Patente] | 2 |

Sin índice, el motor recorre toda la tabla (`Clustered Index Scan`). Con el índice hace una búsqueda (`Index Seek`) y lee un puñado de páginas: la raíz, el nivel hoja y nada más, porque la consulta solo cuenta y el índice ya contiene la patente.
</details>

### Ejercicio 4 · Predecir el operador
<!-- ejercicio: U3.29 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Sin crear ningún índice más que los de las claves primarias, predecí qué operador usará el motor para cada consulta y después verificalo extrayendo el plan: (a) `WHERE OrdenId = 100`, (b) `WHERE Estado = 'Cerrada'` (contando filas), (c) `WHERE Patente = 'AA00100'`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** (a) usa la clave del clúster: búsqueda. (b) no hay índice por `Estado` y devuelve el 85 % de la tabla: recorrido del clúster. (c) no hay índice por `Patente`: recorrido del clúster, aunque devuelva una sola fila.

<!-- check: U3.29 -->
```sql
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE OrdenId = 100        /*P1*/ OPTION (MAXDOP 1);
SELECT @N = COUNT(*) FROM taller.Orden WHERE Estado = 'Cerrada'   /*P2*/ OPTION (MAXDOP 1);
SELECT @N = COUNT(*) FROM taller.Orden WHERE Patente = 'AA00100'  /*P3*/ OPTION (MAXDOP 1);
GO
SELECT 'a) OrdenId' AS Consulta, Operador, Objeto
FROM diag.OperadoresDe(N'/*P1*/') WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'b) Estado', Operador, Objeto
FROM diag.OperadoresDe(N'/*P2*/') WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'c) Patente', Operador, Objeto
FROM diag.OperadoresDe(N'/*P3*/') WHERE Objeto IS NOT NULL
ORDER BY Consulta;
```

**Resultado esperado.**

| Consulta | Operador | Objeto |
|---|---|---|
| a) OrdenId | Clustered Index Seek | [PK_Orden] |
| b) Estado | Clustered Index Scan | [PK_Orden] |
| c) Patente | Clustered Index Scan | [PK_Orden] |

Solo la primera es una búsqueda. Las otras dos recorren el clúster completo: es la señal de que falta un índice por `Patente` (útil: devuelve una fila) y de que un índice por `Estado` no ayudaría con `'Cerrada'` (devuelve casi todo).
</details>

### Ejercicio 5 · Contar filas sin recorrer la tabla
<!-- ejercicio: U3.30 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
`taller.Orden` tiene un índice no clúster adicional (se crea en el bloque siguiente). Obtené la cantidad de filas de `taller.Orden` y de `taller.Cliente` con `sys.dm_db_partition_stats` y comprobá que coincide con `COUNT(*)`. Cuidado con no contar dos veces.

<!-- check: U3.30 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_ClienteId ON taller.Orden (ClienteId);
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada índice tiene sus propias filas en la vista; se suman solo las del heap (`index_id` 0) o del clúster (`index_id` 1), agrupadas por tabla.

<!-- check: U3.30 -->
```sql
SELECT t.name AS Tabla,
       SUM(ps.row_count) AS ConVista,
       CASE t.name WHEN 'Orden' THEN (SELECT COUNT(*) FROM taller.Orden)
                   WHEN 'Cliente' THEN (SELECT COUNT(*) FROM taller.Cliente) END AS ConCount
FROM sys.dm_db_partition_stats AS ps
INNER JOIN sys.tables AS t ON t.object_id = ps.object_id
WHERE ps.index_id IN (0, 1)
GROUP BY t.name
ORDER BY Tabla;
```

**Resultado esperado.**

| Tabla | ConVista | ConCount |
|---|---:|---:|
| Cliente | 300 | 300 |
| Orden | 15000 | 15000 |

Las dos formas coinciden. Sin el filtro `index_id IN (0, 1)`, `Orden` aparecería con 30.000 filas porque el índice no clúster tiene tantas filas como la tabla. La vista no lee la tabla: es un metadato, por eso sirve para medir el crecimiento sin costo.
</details>

### Ejercicio 6 · Leer un histograma
<!-- ejercicio: U3.31 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Creá un índice sobre `Estado`. Obtené su histograma (valor, filas con ese valor exacto) y comprobá que el optimizador estima, para `Estado = 'Abierta'`, la cantidad de filas que figura en el histograma. Mostrá estimadas contra reales.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `sys.dm_db_stats_histogram` devuelve el histograma como filas; `equal_rows` es `EQ_ROWS`. Para las estimaciones se usa el plan real más reciente.

<!-- check: U3.31 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_Estado ON taller.Orden (Estado);
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE Estado = 'Abierta' /*H1*/ OPTION (MAXDOP 1);
GO
SELECT h.range_high_key AS Valor, CAST(h.equal_rows AS INT) AS FilasConEseValor
FROM sys.dm_db_stats_histogram(OBJECT_ID('taller.Orden'),
         (SELECT stats_id FROM sys.stats WHERE object_id = OBJECT_ID('taller.Orden') AND name = 'IX_Orden_Estado')) AS h
ORDER BY h.range_high_key;

SELECT FilasEstimadas, FilasReales
FROM diag.FilasEstimadasYReales(N'/*H1*/')
WHERE Operador = 'Index Seek';
```

**Resultado esperado.**

| Valor | FilasConEseValor |
|---|---:|
| Abierta | 2121 |
| Anulada | 150 |
| Cerrada | 12729 |

| FilasEstimadas | FilasReales |
|---:|---:|
| 2121 | 2121 |

El histograma tiene un paso por valor, y como `'Abierta'` es un `RANGE_HI_KEY`, el optimizador estima exactamente su `EQ_ROWS`, que coincide con la cantidad real.
</details>

### Ejercicio 7 · Plan, estadísticas y caché
<!-- ejercicio: U3.32 | nivel: inicial | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Decidí si cada afirmación es verdadera o falsa y justificá.

1. El plan de ejecución estimado y el real muestran costos distintos, porque el real los mide.
2. Dos consultas ad hoc que difieren solo en un literal comparten el mismo plan en caché.
3. Un `Index Seek` siempre es mejor que un `Index Scan`.
4. Las estadísticas de una tabla se actualizan solas cuando cambian lo suficiente, si `AUTO_UPDATE_STATISTICS` está activo.
5. Un plan sale de la caché si se crea un índice nuevo sobre una de las tablas que usa.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Separar lo que es estimación (costos, filas estimadas) de lo que es medición (filas reales, tiempos) y recordar cómo se identifica un plan en caché.

1. **Falso.** Los costos son los mismos: son estimaciones del optimizador. Lo que agrega el plan real son las filas reales, los tiempos y la memoria usada.
2. **Falso.** El caché se indexa por el texto de la consulta: cada literal distinto genera su propia entrada (salvo parametrización). Con consultas parametrizadas se reutiliza el plan.
3. **Falso.** Si hay que leer la mayor parte de las filas, un recorrido puede ser más barato que miles de búsquedas; lo que importa es que el operador sea el adecuado para la cantidad de filas.
4. **Verdadero.** Se actualizan al superar un umbral de modificaciones, de manera sincrónica por defecto.
5. **Verdadero.** Un cambio de estructura invalida los planes que dependen de la tabla; la próxima ejecución recompila.
</details>

## Nivel intermedio

### Ejercicio 8 · Cubrir una consulta
<!-- ejercicio: U3.33 | nivel: intermedio | tipo: diseno | verificacion: motor -->

:::note[Enunciado]
La consulta frecuente es `SELECT FechaIngreso, Total FROM taller.Orden WHERE ClienteId = 17 AND Estado = 'Abierta'`. Hay un índice por `ClienteId` (se crea abajo), pero no cubre la consulta. Mostrá qué operador usa hoy, diseñá un índice de cobertura que reemplace al existente y mostrá cómo cambian el operador y las lecturas.

<!-- check: U3.33 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_ClienteId ON taller.Orden (ClienteId);
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las columnas del predicado de igualdad (`ClienteId`, `Estado`) van en la clave; las columnas que solo se devuelven (`FechaIngreso`, `Total`) van en `INCLUDE`. Se reemplaza el índice con `DROP_EXISTING`.

<!-- check: U3.33 -->
```sql
DECLARE @Fecha DATE, @Total DECIMAL(10, 2);
SELECT @Fecha = FechaIngreso, @Total = Total
FROM taller.Orden
WHERE ClienteId = 17 AND Estado = 'Abierta' /*C1*/
OPTION (MAXDOP 1);
GO
CREATE NONCLUSTERED INDEX IX_Orden_ClienteId ON taller.Orden (ClienteId, Estado)
    INCLUDE (FechaIngreso, Total)
    WITH (DROP_EXISTING = ON);
GO
DECLARE @Fecha DATE, @Total DECIMAL(10, 2);
SELECT @Fecha = FechaIngreso, @Total = Total
FROM taller.Orden
WHERE ClienteId = 17 AND Estado = 'Abierta' /*C2*/
OPTION (MAXDOP 1);
GO
SELECT 'Antes' AS Momento, Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*C1*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Después', Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*C2*/')
WHERE Objeto IS NOT NULL
ORDER BY Momento, Operador;
```

**Resultado esperado.**

| Momento | Operador | Objeto | LecturasLogicas |
|---|---|---|---:|
| Antes | Clustered Index Scan | [PK_Orden] | 93 |
| Después | Index Seek | [IX_Orden_ClienteId] | 2 |

Antes, el índice por `ClienteId` no contiene `Estado`, `FechaIngreso` ni `Total`: usarlo costaría un `Key Lookup` por cada orden del cliente (unas 50), más que las páginas del clúster, y el optimizador prefiere recorrer la tabla. Después, el índice contiene todo lo que la consulta necesita y se resuelve con una única búsqueda de pocas páginas. El costo: el índice es más ancho y se actualiza cuando cambia `Total`, `FechaIngreso` o `Estado`.
</details>

### Ejercicio 9 · Un predicado no sargable
<!-- ejercicio: U3.34 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Un reporte suma el `Total` de las órdenes de mayo de 2023 con `WHERE YEAR(FechaIngreso) = 2023 AND MONTH(FechaIngreso) = 5`. Hay un índice por `FechaIngreso` que incluye `Total` (se crea abajo). Reescribí el predicado para que use una búsqueda, mostrá los dos planes con sus lecturas y comprobá que el resultado no cambia.

<!-- check: U3.34 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_FechaIngreso ON taller.Orden (FechaIngreso) INCLUDE (Total);
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Aplicar `YEAR`/`MONTH` a la columna impide navegar el índice. Se reemplaza por un rango semiabierto sobre la columna: `>= '2023-05-01' AND < '2023-06-01'`.

<!-- check: U3.34 -->
```sql
DECLARE @Original DECIMAL(18, 2), @Reescrita DECIMAL(18, 2);

SELECT @Original = SUM(Total)
FROM taller.Orden
WHERE YEAR(FechaIngreso) = 2023 AND MONTH(FechaIngreso) = 5 /*Y1*/
OPTION (MAXDOP 1);

SELECT @Reescrita = SUM(Total)
FROM taller.Orden
WHERE FechaIngreso >= '2023-05-01' AND FechaIngreso < '2023-06-01' /*Y2*/
OPTION (MAXDOP 1);

SELECT CASE WHEN @Original = @Reescrita THEN 'sí' ELSE 'no' END AS MismoResultado;
GO
SELECT 'Con YEAR y MONTH' AS Version, Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*Y1*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Con rango', Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*Y2*/')
WHERE Objeto IS NOT NULL
ORDER BY Version;
```

**Resultado esperado.**

| MismoResultado |
|---|
| sí |

| Version | Operador | Objeto | LecturasLogicas |
|---|---|---|---:|
| Con rango | Index Seek | [IX_Orden_FechaIngreso] | 3 |
| Con YEAR y MONTH | Index Scan | [IX_Orden_FechaIngreso] | 43 |

El resultado es idéntico, pero la versión original recorre todas las hojas del índice y la reescrita navega directamente hasta el rango de mayo. Se mueve el cálculo del lado de la columna al de las constantes.
</details>

### Ejercicio 10 · La conversión implícita escondida
<!-- ejercicio: U3.35 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Una aplicación busca órdenes por patente y envía el parámetro como `NVARCHAR`. Hay un índice por `Patente` (se crea abajo). Mostrá que el motor recorre el índice en lugar de buscar, explicá por qué y corregí la consulta sin tocar el índice.

<!-- check: U3.35 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_Patente ON taller.Orden (Patente);
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `Patente` es `VARCHAR` y el parámetro `NVARCHAR`: el tipo de menor precedencia (`VARCHAR`) se convierte al de mayor (`NVARCHAR`), es decir, se convierte la columna. Se corrige declarando el parámetro del mismo tipo que la columna.

<!-- check: U3.35 -->
```sql
DECLARE @PatenteUnicode NVARCHAR(7) = N'AA00500';
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE Patente = @PatenteUnicode /*V1*/ OPTION (MAXDOP 1);
GO
DECLARE @PatenteVarchar VARCHAR(7) = 'AA00500';
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE Patente = @PatenteVarchar /*V2*/ OPTION (MAXDOP 1);
GO
SELECT 'Parámetro NVARCHAR' AS Version, Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*V1*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Parámetro VARCHAR', Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*V2*/')
WHERE Objeto IS NOT NULL
ORDER BY Version DESC;
```

**Resultado esperado.**

| Version | Operador | Objeto | LecturasLogicas |
|---|---|---|---:|
| Parámetro VARCHAR | Index Seek | [IX_Orden_Patente] | 2 |
| Parámetro NVARCHAR | Index Scan | [IX_Orden_Patente] | 41 |

Con el parámetro Unicode hay un `Index Scan`: el motor tiene que convertir cada patente antes de compararla. Con el tipo correcto, una búsqueda. Este problema es típico de los ORM que declaran todas las cadenas como Unicode.
</details>

### Ejercicio 11 · Cuánto cuesta el fill factor
<!-- ejercicio: U3.36 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Cargá 8.000 filas de 100 bytes en tres tablas idénticas cuyo índice clúster tiene fill factor 100, 80 y 60. Mostrá cuántas páginas hoja ocupa cada una y cuánto más grande (en porcentaje) es respecto de la de 100.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El fill factor se aplica al crear o reconstruir el índice, así que se hace `REBUILD` después de la carga. Las páginas se leen de `sys.dm_db_index_physical_stats` en modo `DETAILED`.

<!-- check: U3.36 -->
```sql
CREATE TABLE taller.Bitacora100 (BitacoraId INT NOT NULL, Detalle CHAR(100) NOT NULL DEFAULT 'x',
    CONSTRAINT PK_Bitacora100 PRIMARY KEY CLUSTERED (BitacoraId) WITH (FILLFACTOR = 100));
CREATE TABLE taller.Bitacora80  (BitacoraId INT NOT NULL, Detalle CHAR(100) NOT NULL DEFAULT 'x',
    CONSTRAINT PK_Bitacora80  PRIMARY KEY CLUSTERED (BitacoraId) WITH (FILLFACTOR = 80));
CREATE TABLE taller.Bitacora60  (BitacoraId INT NOT NULL, Detalle CHAR(100) NOT NULL DEFAULT 'x',
    CONSTRAINT PK_Bitacora60  PRIMARY KEY CLUSTERED (BitacoraId) WITH (FILLFACTOR = 60));
GO
WITH n AS (
    SELECT TOP (8000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns AS a CROSS JOIN sys.all_columns AS b
)
INSERT INTO taller.Bitacora100 (BitacoraId) SELECT n FROM n;
INSERT INTO taller.Bitacora80  (BitacoraId) SELECT BitacoraId FROM taller.Bitacora100;
INSERT INTO taller.Bitacora60  (BitacoraId) SELECT BitacoraId FROM taller.Bitacora100;

ALTER INDEX PK_Bitacora100 ON taller.Bitacora100 REBUILD;
ALTER INDEX PK_Bitacora80  ON taller.Bitacora80  REBUILD;
ALTER INDEX PK_Bitacora60  ON taller.Bitacora60  REBUILD;
GO
WITH p AS (
    SELECT OBJECT_NAME(object_id) AS Tabla, page_count AS Paginas
    FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'DETAILED')
    WHERE index_level = 0 AND OBJECT_NAME(object_id) LIKE 'Bitacora%'
)
SELECT p.Tabla,
       p.Paginas,
       CAST(100.0 * (p.Paginas - b.Paginas) / b.Paginas AS DECIMAL(5, 1)) AS PctMasQueFF100
FROM p
CROSS JOIN (SELECT Paginas FROM p WHERE Tabla = 'Bitacora100') AS b
ORDER BY p.Paginas;
```

**Resultado esperado.**

| Tabla | Paginas | PctMasQueFF100 |
|---|---:|---:|
| Bitacora100 | 113 | 0.0 |
| Bitacora80 | 138 | 22.1 |
| Bitacora60 | 187 | 65.5 |

Cada fila de 100 bytes más el encabezado entra unas 70 por página con fill factor 100; bajar a 80 y a 60 deja 20 % y 40 % libre, y las tablas crecen en proporción. Ese espacio libre es el precio de absorber inserciones sin partir páginas: más memoria, más lecturas, backups más pesados. Por eso no se baja sin haber medido fragmentación.
</details>

### Ejercicio 12 · ¿Vale la pena el índice?
<!-- ejercicio: U3.37 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Se evalúa un índice por `Estado` (se crea abajo) para la consulta `SELECT SUM(Total) FROM taller.Orden WHERE Estado = @valor`. Para cada uno de los tres valores, informá cuántas filas devuelve (y el porcentaje) y qué operador usa el motor. Después ajustá el índice para que el valor menos frecuente use una búsqueda.

<!-- check: U3.37 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_Estado ON taller.Orden (Estado);
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Contar filas por valor da la selectividad. Luego se mide el operador de cada valor; para que el índice sirva, debe cubrir la consulta (`INCLUDE (Total)`) y así evitar el lookup por fila.

<!-- check: U3.37 -->
```sql
DECLARE @T DECIMAL(18, 2);
SELECT @T = SUM(Total) FROM taller.Orden WHERE Estado = 'Anulada' /*S1*/ OPTION (MAXDOP 1);
SELECT @T = SUM(Total) FROM taller.Orden WHERE Estado = 'Abierta' /*S2*/ OPTION (MAXDOP 1);
SELECT @T = SUM(Total) FROM taller.Orden WHERE Estado = 'Cerrada' /*S3*/ OPTION (MAXDOP 1);
GO
SELECT o.Estado,
       COUNT(*) AS Filas,
       CAST(100.0 * COUNT(*) / (SELECT COUNT(*) FROM taller.Orden) AS DECIMAL(5, 1)) AS Porcentaje
FROM taller.Orden AS o
GROUP BY o.Estado
ORDER BY Filas;

SELECT 'Anulada' AS Valor, Operador FROM diag.OperadoresDe(N'/*S1*/') WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Abierta', Operador FROM diag.OperadoresDe(N'/*S2*/') WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Cerrada', Operador FROM diag.OperadoresDe(N'/*S3*/') WHERE Objeto IS NOT NULL
ORDER BY Valor;
GO
CREATE NONCLUSTERED INDEX IX_Orden_Estado ON taller.Orden (Estado) INCLUDE (Total) WITH (DROP_EXISTING = ON);
GO
DECLARE @T DECIMAL(18, 2);
SELECT @T = SUM(Total) FROM taller.Orden WHERE Estado = 'Anulada' /*S4*/ OPTION (MAXDOP 1);
GO
SELECT 'Anulada con INCLUDE' AS Valor, Operador, Objeto
FROM diag.OperadoresDe(N'/*S4*/')
WHERE Objeto IS NOT NULL;
```

**Resultado esperado.**

| Estado | Filas | Porcentaje |
|---|---:|---:|
| Anulada | 150 | 1.0 |
| Abierta | 2121 | 14.1 |
| Cerrada | 12729 | 84.9 |

| Valor | Operador |
|---|---|
| Abierta | Clustered Index Scan |
| Anulada | Clustered Index Scan |
| Cerrada | Clustered Index Scan |

| Valor | Operador | Objeto |
|---|---|---|
| Anulada con INCLUDE | Index Seek | [IX_Orden_Estado] |

Con el índice original ningún valor usa una búsqueda: aun `'Anulada'` (1 %) necesita un lookup por fila, más caro que leer la tabla. Cuando el índice cubre la consulta no hay lookups y el valor poco frecuente se resuelve con una búsqueda. Para `'Cerrada'` (85 %) ningún índice ayuda.
</details>

### Ejercicio 13 · Un índice filtrado
<!-- ejercicio: U3.38 | nivel: intermedio | tipo: diseno | verificacion: motor -->

:::note[Enunciado]
Casi todas las consultas operativas miran solo las órdenes abiertas: `SELECT SUM(Total) FROM taller.Orden WHERE Estado = 'Abierta' AND FechaIngreso >= '2024-01-01' AND FechaIngreso < '2024-04-01'`. Creá un índice filtrado para ellas y comparalo, en páginas y en lecturas de la consulta, con un índice completo equivalente.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El filtro (`WHERE Estado = 'Abierta'`) deja afuera el 86 % de las filas: el índice resulta más chico. La consulta repite el predicado, así que el optimizador puede usarlo.

<!-- check: U3.38 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_Fecha_Completo ON taller.Orden (FechaIngreso) INCLUDE (Estado, Total);
CREATE NONCLUSTERED INDEX IX_Orden_Abiertas_Fecha ON taller.Orden (FechaIngreso) INCLUDE (Total)
    WHERE Estado = 'Abierta';
GO
DECLARE @T DECIMAL(18, 2);
SELECT @T = SUM(Total)
FROM taller.Orden WITH (INDEX (IX_Orden_Fecha_Completo))
WHERE Estado = 'Abierta'
  AND FechaIngreso >= '2024-01-01' AND FechaIngreso < '2024-04-01' /*F1*/
OPTION (MAXDOP 1);

SELECT @T = SUM(Total)
FROM taller.Orden WITH (INDEX (IX_Orden_Abiertas_Fecha))
WHERE Estado = 'Abierta'
  AND FechaIngreso >= '2024-01-01' AND FechaIngreso < '2024-04-01' /*F2*/
OPTION (MAXDOP 1);
GO
SELECT i.name AS Indice, ps.used_page_count AS Paginas
FROM sys.indexes AS i
INNER JOIN sys.dm_db_partition_stats AS ps
    ON ps.object_id = i.object_id AND ps.index_id = i.index_id
WHERE i.object_id = OBJECT_ID('taller.Orden') AND i.index_id > 1
ORDER BY i.name;

SELECT DISTINCT 'Completo' AS Indice, Operador, LecturasLogicas
FROM diag.OperadoresDe(N'/*F1*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT DISTINCT 'Filtrado', Operador, LecturasLogicas
FROM diag.OperadoresDe(N'/*F2*/')
WHERE Objeto IS NOT NULL
ORDER BY Indice;
```

**Resultado esperado.**

| Indice | Paginas |
|---|---:|
| IX_Orden_Abiertas_Fecha | 8 |
| IX_Orden_Fecha_Completo | 64 |

| Indice | Operador | LecturasLogicas |
|---|---|---:|
| Completo | Index Seek | 8 |
| Filtrado | Index Seek | 4 |

El filtrado ocupa 8 páginas contra 64 del completo (guarda solo las abiertas y una columna menos) y la consulta lee la mitad de páginas. Forzamos cada índice con `INDEX(...)` para compararlos; sin la pista, en una tabla tan chica el optimizador puede elegir cualquiera de los dos, porque ambos son baratos. La ventaja se acentúa con el volumen: menos espacio, menos costo de mantenimiento en cada escritura sobre filas que no son abiertas. La contrapartida es que solo sirve a consultas cuyo predicado implique `Estado = 'Abierta'`.
</details>

### Ejercicio 14 · Columnstore sobre una tabla de mediciones
<!-- ejercicio: U3.39 | nivel: intermedio | tipo: diseno | verificacion: motor -->

:::note[Enunciado]
Se carga una tabla `taller.Medicion` con 200.000 filas (abajo). Convertila a almacenamiento por columna con un índice columnstore clúster y mostrá: el operador de una agregación por sensor antes y después, el estado de sus grupos de filas, y qué ocurre con tres filas nuevas.

<!-- check: U3.39 -->
```sql
CREATE TABLE taller.Medicion (
    MedicionId INT            NOT NULL,
    SensorId   INT            NOT NULL,
    Valor      DECIMAL(10, 2) NOT NULL,
    Dia        DATE           NOT NULL
);
GO
WITH n AS (
    SELECT TOP (200000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns AS a CROSS JOIN sys.all_columns AS b
)
INSERT INTO taller.Medicion (MedicionId, SensorId, Valor, Dia)
SELECT n, n % 50 + 1, n % 90 + 0.25, DATEADD(DAY, n % 365, '2024-01-01')
FROM n;
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La tabla es un heap: antes, la agregación hace un `Table Scan`. `CREATE CLUSTERED COLUMNSTORE INDEX` convierte la tabla; después el operador es un recorrido del columnstore. Las filas nuevas van al delta store.

<!-- check: U3.39 -->
```sql
DECLARE @T DECIMAL(18, 2);
SELECT @T = SUM(Valor) FROM (SELECT SensorId, SUM(Valor) AS Valor FROM taller.Medicion GROUP BY SensorId) AS x /*K1*/ OPTION (MAXDOP 1);
GO
CREATE CLUSTERED COLUMNSTORE INDEX CCI_Medicion ON taller.Medicion WITH (MAXDOP = 1);
GO
DECLARE @T DECIMAL(18, 2);
SELECT @T = SUM(Valor) FROM (SELECT SensorId, SUM(Valor) AS Valor FROM taller.Medicion GROUP BY SensorId) AS x /*K2*/ OPTION (MAXDOP 1);
GO
SELECT 'Heap' AS Momento, Operador, Objeto FROM diag.OperadoresDe(N'/*K1*/') WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Columnstore', Operador, Objeto FROM diag.OperadoresDe(N'/*K2*/') WHERE Objeto IS NOT NULL
ORDER BY Momento;

SELECT state_description AS Estado, total_rows AS Filas
FROM sys.column_store_row_groups
WHERE object_id = OBJECT_ID('taller.Medicion')
ORDER BY row_group_id;

INSERT INTO taller.Medicion (MedicionId, SensorId, Valor, Dia)
VALUES (200001, 1, 1.00, '2025-01-01'), (200002, 2, 2.00, '2025-01-02'), (200003, 3, 3.00, '2025-01-03');

SELECT state_description AS Estado, total_rows AS Filas
FROM sys.column_store_row_groups
WHERE object_id = OBJECT_ID('taller.Medicion')
ORDER BY row_group_id;
```

**Resultado esperado.** SQL Server puede mostrar la advertencia sobre una pista de combinación al consultar `sys.column_store_row_groups`; es inofensiva.

| Momento | Operador | Objeto |
|---|---|---|
| Columnstore | Clustered Index Scan | [CCI_Medicion] |
| Heap | Table Scan | [Medicion] |

| Estado | Filas |
|---|---:|
| COMPRESSED | 200000 |

| Estado | Filas |
|---|---:|
| COMPRESSED | 200000 |
| OPEN | 3 |

Las 200.000 filas quedan comprimidas en un solo grupo de filas. Las tres nuevas se acumulan en un grupo `OPEN` (delta store), sin comprimir, hasta que el *tuple mover* las comprime. Por eso el columnstore rinde mejor en tablas de solo consulta o cargadas por lotes grandes.
</details>

## Nivel avanzado

### Ejercicio 15 · Estimaciones que no coinciden
<!-- ejercicio: U3.40 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Un proceso carga 3.000 órdenes con fecha de ingreso `2025-06-15` y la consulta `WHERE FechaIngreso = '2025-06-15'` empieza a recibir estimaciones muy bajas. La base tiene desactivada la actualización automática de estadísticas (se configura abajo). Mostrá estimadas contra reales, diagnosticá la causa con `sys.dm_db_stats_properties`, corregila y mostrá la estimación nueva.

<!-- check: U3.40 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_FechaIngreso ON taller.Orden (FechaIngreso);
ALTER DATABASE CURRENT SET AUTO_UPDATE_STATISTICS OFF;
GO
INSERT INTO taller.Orden (ClienteId, FechaIngreso, Estado, Patente, Total)
SELECT TOP (3000) 1, '2025-06-15', 'Abierta', 'ZZ00000', 100.00
FROM sys.all_columns;
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** (1) Medir estimadas y reales. (2) Mirar cuántas modificaciones tiene la estadística desde su última actualización. (3) Actualizarla y volver a medir.

<!-- check: U3.40 -->
```sql
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE FechaIngreso = '2025-06-15' /*E1*/ OPTION (MAXDOP 1);
GO
SELECT sp.rows AS FilasEnLaEstadistica, sp.modification_counter AS ModificacionesPendientes
FROM sys.stats AS s
CROSS APPLY sys.dm_db_stats_properties(s.object_id, s.stats_id) AS sp
WHERE s.object_id = OBJECT_ID('taller.Orden') AND s.name = 'IX_Orden_FechaIngreso';

UPDATE STATISTICS taller.Orden IX_Orden_FechaIngreso WITH FULLSCAN;
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE FechaIngreso = '2025-06-15' /*E2*/ OPTION (MAXDOP 1);
GO
SELECT 'Antes' AS Momento, FilasEstimadas, FilasReales
FROM diag.FilasEstimadasYReales(N'/*E1*/')
WHERE Operador = 'Index Seek'
UNION ALL
SELECT 'Después', FilasEstimadas, FilasReales
FROM diag.FilasEstimadasYReales(N'/*E2*/')
WHERE Operador = 'Index Seek'
ORDER BY Momento;
```

**Resultado esperado.**

| FilasEnLaEstadistica | ModificacionesPendientes |
|---:|---:|
| 15000 | 3000 |

| Momento | FilasEstimadas | FilasReales |
|---|---:|---:|
| Antes | 1 | 3000 |
| Después | 3000 | 3000 |

La estadística sigue describiendo las 15.000 filas anteriores y acumula 3.000 modificaciones pendientes: el valor nuevo cae fuera del histograma y el optimizador estima poco. Con 3.000 cambios no se llegó al umbral de actualización automática (500 más el 20 % de las filas), y de todos modos la opción estaba desactivada. Después de `UPDATE STATISTICS` la estimación coincide con lo real. Con tablas de mayor volumen y consultas con `JOIN`, la misma desviación cambia el algoritmo y la memoria reservada.
</details>

### Ejercicio 16 · Qué índices sobran
<!-- ejercicio: U3.41 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
`taller.Orden` tiene los cuatro índices del bloque siguiente. Se ejecuta una carga de trabajo (también abajo). Con `sys.dm_db_index_usage_stats`, listá cada índice con sus búsquedas, recorridos, lookups y actualizaciones, e indicá cuáles son candidatos a eliminarse y por qué. Uno se elimina por no usarse; otro por ser redundante.

<!-- check: U3.41 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_ClienteId        ON taller.Orden (ClienteId);
CREATE NONCLUSTERED INDEX IX_Orden_ClienteId_Estado ON taller.Orden (ClienteId, Estado);
CREATE NONCLUSTERED INDEX IX_Orden_Total            ON taller.Orden (Total);
CREATE NONCLUSTERED INDEX IX_Orden_FechaIngreso     ON taller.Orden (FechaIngreso);
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE ClienteId = 5 AND Estado = 'Abierta' OPTION (MAXDOP 1);
SELECT @N = COUNT(*) FROM taller.Orden WHERE ClienteId = 6 AND Estado = 'Cerrada' OPTION (MAXDOP 1);
SELECT @N = COUNT(*) FROM taller.Orden WHERE ClienteId = 7 OPTION (MAXDOP 1);
SELECT @N = COUNT(*) FROM taller.Orden WHERE FechaIngreso >= '2024-02-01' AND FechaIngreso < '2024-02-08' OPTION (MAXDOP 1);
UPDATE taller.Orden SET Total = Total + 1 WHERE OrdenId <= 50;
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los contadores de uso dicen qué se leyó y qué solo se mantuvo. Un índice con actualizaciones y sin lecturas no se usa. Un índice cuya clave es prefijo de otro (`ClienteId` frente a `ClienteId, Estado`) es candidato a redundante.

<!-- check: U3.41 -->
```sql
SELECT i.name                    AS Indice,
       ISNULL(s.user_seeks, 0)   AS Busquedas,
       ISNULL(s.user_scans, 0)   AS Recorridos,
       ISNULL(s.user_lookups, 0) AS Lookups,
       ISNULL(s.user_updates, 0) AS Actualizaciones
FROM sys.indexes AS i
LEFT JOIN sys.dm_db_index_usage_stats AS s
    ON s.object_id = i.object_id AND s.index_id = i.index_id AND s.database_id = DB_ID()
WHERE i.object_id = OBJECT_ID('taller.Orden') AND i.index_id > 1
ORDER BY i.name;
```

**Resultado esperado.**

| Indice | Busquedas | Recorridos | Lookups | Actualizaciones |
|---|---:|---:|---:|---:|
| IX_Orden_ClienteId | 0 | 0 | 0 | 0 |
| IX_Orden_ClienteId_Estado | 3 | 0 | 0 | 0 |
| IX_Orden_FechaIngreso | 1 | 0 | 0 | 0 |
| IX_Orden_Total | 0 | 0 | 0 | 1 |

`IX_Orden_Total` nunca se leyó y solo cuesta: se actualizó con el `UPDATE` (no usado). `IX_Orden_ClienteId_Estado` resolvió las tres consultas por cliente, incluida la que solo filtra por `ClienteId` (su clave empieza por esa columna), y `IX_Orden_ClienteId` no se usó nunca: es redundante respecto del compuesto y se puede eliminar. Antes de eliminar, hay que observar un período representativo, porque estos contadores se reinician con el servicio y un cierre de mes puede usar índices que la semana pasada no se tocaron.
</details>

### Ejercicio 17 · El orden de las columnas de un índice compuesto
<!-- ejercicio: U3.42 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Para la consulta `SELECT SUM(Total) FROM taller.Orden WHERE Estado = 'Abierta' AND FechaIngreso >= '2024-01-01' AND FechaIngreso < '2024-02-01'` se proponen dos índices: `(Estado, FechaIngreso)` y `(FechaIngreso, Estado)`, ambos con `INCLUDE (Total)`. Compará las lecturas de cada uno forzándolo con `INDEX(...)` y explicá la regla que se desprende.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Crear los dos, forzar cada uno con una pista (solo para comparar) y medir las lecturas. Las columnas con igualdad conviene ponerlas antes que las del rango.

<!-- check: U3.42 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_Estado_Fecha ON taller.Orden (Estado, FechaIngreso) INCLUDE (Total);
CREATE NONCLUSTERED INDEX IX_Orden_Fecha_Estado ON taller.Orden (FechaIngreso, Estado) INCLUDE (Total);
GO
DECLARE @T DECIMAL(18, 2);
SELECT @T = SUM(Total)
FROM taller.Orden WITH (INDEX (IX_Orden_Estado_Fecha))
WHERE Estado = 'Abierta' AND FechaIngreso >= '2024-01-01' AND FechaIngreso < '2024-02-01' /*O1*/
OPTION (MAXDOP 1);

SELECT @T = SUM(Total)
FROM taller.Orden WITH (INDEX (IX_Orden_Fecha_Estado))
WHERE Estado = 'Abierta' AND FechaIngreso >= '2024-01-01' AND FechaIngreso < '2024-02-01' /*O2*/
OPTION (MAXDOP 1);
GO
SELECT '(Estado, FechaIngreso)' AS Indice, Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*O1*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT '(FechaIngreso, Estado)', Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*O2*/')
WHERE Objeto IS NOT NULL
ORDER BY Indice DESC;
```

**Resultado esperado.**

| Indice | Operador | Objeto | LecturasLogicas |
|---|---|---|---:|
| (FechaIngreso, Estado) | Index Seek | [IX_Orden_Fecha_Estado] | 5 |
| (Estado, FechaIngreso) | Index Seek | [IX_Orden_Estado_Fecha] | 3 |

Con `(Estado, FechaIngreso)` el motor baja a las abiertas y dentro de ellas lee un rango contiguo de fechas: toca solo las filas que cumplen (3 lecturas). Con `(FechaIngreso, Estado)` lee todo el rango de fechas, con todos los estados mezclados, y descarta las que no son abiertas (5 lecturas). Con 15.000 filas la diferencia es chica; crece con el volumen. Regla: primero las columnas con igualdad, después la del rango. Las pistas `INDEX(...)` sirven para experimentar; en producción se deja que el optimizador elija.
</details>

### Ejercicio 18 · NOT IN y los NULL
<!-- ejercicio: U3.43 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Se quiere listar los técnicos sin ninguna asignación. Con los datos siguientes (una asignación sin técnico informado), escribí la consulta con `NOT IN` y con `NOT EXISTS`, compará los resultados y explicá la diferencia.

<!-- check: U3.43 -->
```sql
CREATE TABLE taller.Mecanico (MecanicoId INT NOT NULL PRIMARY KEY, Nombre VARCHAR(30) NOT NULL);
CREATE TABLE taller.Asignacion (AsignacionId INT NOT NULL PRIMARY KEY, MecanicoId INT NULL);

INSERT INTO taller.Mecanico (MecanicoId, Nombre) VALUES (1, 'Mecanico 1'), (2, 'Mecanico 2'), (3, 'Mecanico 3');
INSERT INTO taller.Asignacion (AsignacionId, MecanicoId) VALUES (1, 1), (2, NULL), (3, 1);
```
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `x NOT IN (..., NULL)` es desconocido para todo `x` que no esté en la lista, de modo que el `WHERE` nunca es verdadero. `NOT EXISTS` compara fila a fila y no se ve afectado por el `NULL`.

<!-- check: U3.43 -->
```sql
SELECT 'NOT IN' AS Version, m.MecanicoId
FROM taller.Mecanico AS m
WHERE m.MecanicoId NOT IN (SELECT a.MecanicoId FROM taller.Asignacion AS a)
UNION ALL
SELECT 'NOT EXISTS', m.MecanicoId
FROM taller.Mecanico AS m
WHERE NOT EXISTS (SELECT 1 FROM taller.Asignacion AS a WHERE a.MecanicoId = m.MecanicoId)
ORDER BY Version DESC, MecanicoId;
```

**Resultado esperado.**

| Version | MecanicoId |
|---|---:|
| NOT EXISTS | 2 |
| NOT EXISTS | 3 |

`NOT IN` no devuelve ninguna fila (por eso no aparece en la tabla), aunque los mecánicos 2 y 3 no tienen asignaciones; `NOT EXISTS` devuelve los dos. En consultas sobre índices equivalentes, los planes de ambas formas suelen ser iguales: se elige por la semántica ante `NULL`, no por rendimiento. Si la columna admite `NULL`, `NOT IN` debe acompañarse de `WHERE a.MecanicoId IS NOT NULL` dentro de la subconsulta, o reemplazarse por `NOT EXISTS`.
</details>

### Ejercicio 19 · Una línea de base de filas
<!-- ejercicio: U3.44 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Armá una tabla de historial que guarde, por tabla y por corte (`Corte` 1, 2, ...), su cantidad de filas tomada de `sys.dm_db_partition_stats`. Tomá un corte inicial, insertá 200 órdenes, tomá un segundo corte y escribí la consulta que informa por tabla el incremento y el porcentaje, marcando `ALERTA` cuando supere el 1 %.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un procedimiento guarda una foto con el número de corte; una consulta compara cortes consecutivos por tabla. Se suma `row_count` de `index_id` 0 y 1.

<!-- check: U3.44 -->
```sql
CREATE SCHEMA monitoreo;
GO
CREATE TABLE monitoreo.LineaBaseFilas (
    Corte INT          NOT NULL,
    Tabla VARCHAR(60)  NOT NULL,
    Filas BIGINT       NOT NULL,
    CONSTRAINT PK_LineaBaseFilas PRIMARY KEY CLUSTERED (Corte, Tabla)
);
GO
CREATE PROCEDURE monitoreo.TomarCorteDeFilas
    @Corte INT
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO monitoreo.LineaBaseFilas (Corte, Tabla, Filas)
    SELECT @Corte, CONCAT(s.name, '.', t.name), SUM(ps.row_count)
    FROM sys.dm_db_partition_stats AS ps
    INNER JOIN sys.tables  AS t ON t.object_id = ps.object_id
    INNER JOIN sys.schemas AS s ON s.schema_id = t.schema_id
    WHERE ps.index_id IN (0, 1)
      AND s.name = 'taller'
    GROUP BY s.name, t.name;
END;
GO
EXEC monitoreo.TomarCorteDeFilas @Corte = 1;

INSERT INTO taller.Orden (ClienteId, FechaIngreso, Estado, Patente, Total)
SELECT TOP (200) 1, '2025-01-10', 'Abierta', 'BB00000', 100.00
FROM sys.all_columns;

EXEC monitoreo.TomarCorteDeFilas @Corte = 2;
GO
SELECT b2.Tabla,
       b2.Filas - b1.Filas AS Incremento,
       CAST(100.0 * (b2.Filas - b1.Filas) / b1.Filas AS DECIMAL(5, 2)) AS Porcentaje,
       CASE WHEN 100.0 * (b2.Filas - b1.Filas) / b1.Filas > 1 THEN 'ALERTA' ELSE 'normal' END AS Estado
FROM monitoreo.LineaBaseFilas AS b1
INNER JOIN monitoreo.LineaBaseFilas AS b2
    ON b2.Tabla = b1.Tabla AND b2.Corte = b1.Corte + 1
WHERE b1.Corte = 1
ORDER BY b2.Tabla;
```

**Resultado esperado.**

| Tabla | Incremento | Porcentaje | Estado |
|---|---:|---:|---|
| taller.Cliente | 0 | 0.00 | normal |
| taller.Orden | 200 | 1.33 | ALERTA |

`taller.Orden` creció un 1,33 % entre cortes y supera el umbral; `taller.Cliente` no cambió. En producción el procedimiento lo ejecuta un trabajo del Agente cada cierto tiempo, y el umbral se calibra con el historial (el baseline), no con un valor fijo. Medir con `sys.dm_db_partition_stats` evita el costo de `COUNT(*)` sobre tablas grandes.
</details>

### Ejercicio 20 · Diseñar los índices de una carga de trabajo
<!-- ejercicio: U3.45 | nivel: avanzado | tipo: diseno | verificacion: motor -->

:::note[Enunciado]
`taller.Orden` solo tiene su clave primaria. La carga de trabajo son tres consultas frecuentes: (1) órdenes abiertas de un cliente, con fecha y total; (2) total mensual de las órdenes de 2023; (3) búsqueda de una orden por patente para obtener su cliente y total. Proponé como máximo tres índices, cada uno con su justificación, y mostrá que cada consulta se resuelve con una búsqueda y sin `Key Lookup`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un índice por consulta, con la clave en las columnas de igualdad o de rango y `INCLUDE` en las que solo se devuelven: (1) `(ClienteId, Estado)` incluyendo `FechaIngreso` y `Total`; (2) `(FechaIngreso)` incluyendo `Total`, con el filtro como rango; (3) `(Patente)` incluyendo `ClienteId` y `Total`.

<!-- check: U3.45 -->
```sql
CREATE NONCLUSTERED INDEX IX_Orden_Cliente_Estado ON taller.Orden (ClienteId, Estado) INCLUDE (FechaIngreso, Total);
CREATE NONCLUSTERED INDEX IX_Orden_FechaIngreso   ON taller.Orden (FechaIngreso) INCLUDE (Total);
CREATE NONCLUSTERED INDEX IX_Orden_Patente        ON taller.Orden (Patente) INCLUDE (ClienteId, Total);
GO
DECLARE @Fecha DATE, @Total DECIMAL(18, 2), @Cliente INT, @Mes INT;

SELECT @Fecha = FechaIngreso, @Total = Total
FROM taller.Orden
WHERE ClienteId = 17 AND Estado = 'Abierta' /*D1*/
OPTION (MAXDOP 1);

SELECT @Mes = MONTH(FechaIngreso), @Total = SUM(Total)
FROM taller.Orden
WHERE FechaIngreso >= '2023-01-01' AND FechaIngreso < '2024-01-01' /*D2*/
GROUP BY MONTH(FechaIngreso)
OPTION (MAXDOP 1);

SELECT @Cliente = ClienteId, @Total = Total
FROM taller.Orden
WHERE Patente = 'AA01234' /*D3*/
OPTION (MAXDOP 1);
GO
SELECT 'Consulta 1' AS Consulta, Operador, Objeto
FROM diag.OperadoresDe(N'/*D1*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Consulta 2', Operador, Objeto
FROM diag.OperadoresDe(N'/*D2*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Consulta 3', Operador, Objeto
FROM diag.OperadoresDe(N'/*D3*/')
WHERE Objeto IS NOT NULL
ORDER BY Consulta;
```

**Resultado esperado.**

| Consulta | Operador | Objeto |
|---|---|---|
| Consulta 1 | Index Seek | [IX_Orden_Cliente_Estado] |
| Consulta 2 | Index Seek | [IX_Orden_FechaIngreso] |
| Consulta 3 | Index Seek | [IX_Orden_Patente] |

Las tres consultas usan un `Index Seek` sobre su propio índice, sin `Key Lookup`. El costo de los tres índices es de escritura y de espacio: cada alta o cambio de `Total` actualiza los tres. Por eso se justifican con consultas frecuentes y se vigilan después con `sys.dm_db_index_usage_stats`. Un cuarto índice para `Estado` solo no se propone: no es selectivo.
</details>

## Fuentes

- Presentación de cátedra, Unidad 3, parte 1 (v1.0, agosto 2023) y parte 2 (v1.0, 2023).
- Microsoft Learn: documentación de índices, estadísticas y vistas de administración dinámica de SQL Server.
