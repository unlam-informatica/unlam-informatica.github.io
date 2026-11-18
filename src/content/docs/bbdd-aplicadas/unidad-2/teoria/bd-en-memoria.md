---
title: BD en memoria
slug: bbdd-aplicadas/unidad-2/teoria/bd-en-memoria
sidebar:
  order: 3.5
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

Esta página compara el almacenamiento en disco con el almacenamiento en memoria (tema del programa), explica en qué se diferencian las tablas variables, las temporales y las tablas en memoria de SQL Server y, en la segunda parte, desarrolla In-Memory OLTP (contenido complementario). Los ejemplos se ejecutan sobre SQL Server 2022.

## Bases de datos en memoria y en disco

Una **base de datos en memoria** guarda los datos en la memoria principal (RAM) en lugar de en almacenamiento secundario. Cada lectura o escritura se hace directamente en memoria, sin esperar una operación de entrada/salida (E/S) al disco, por lo que es mucho más rápida.

**Para qué se necesita.** Con el Internet de las cosas (IoT) y las soluciones en la nube, las organizaciones deben procesar datos en tiempo real: millones de dispositivos generan datos cada segundo. Las bases en memoria se consideran cuando:

- hay que aprovechar las ventajas de Big Data en tiempo real;
- se recopilan datos periódicamente y se necesita acceder a ellos muy rápido;
- la persistencia de los datos no es la principal preocupación.

| Aspecto | En disco | En memoria |
|---|---|---|
| Operación de lectura o escritura | Requiere E/S contra almacenamiento masivo (lento) | Se hace directamente en memoria (rápido) |
| Persistencia | Los datos no se pierden ante un corte de energía | Son volátiles: necesitan técnicas adicionales para no perderse |
| Estructuras de almacenamiento | Complejas, para lograr un acceso eficiente | Simples, porque el acceso aleatorio en RAM ya es eficiente |
| Dónde corren | Solo en sistemas con almacenamiento secundario | También en la memoria de dispositivos embebidos |
| Tamaño | Grandes volúmenes de datos | Limitado por la memoria disponible |
| Uso típico | Aplicaciones de gestión de clientes y usuarios | Aplicaciones basadas en acceso a internet, datos temporales |

### Durabilidad de una base en memoria

La RAM es volátil. Para conservar la durabilidad de lo confirmado, los sistemas en memoria suelen combinar:

- **Registro de transacciones**: cada cambio se anota en almacenamiento no volátil, y ante una falla permite reconstruir hasta el último `COMMIT`. Agrega E/S y espacio.
- **Instantáneas** (_snapshots_ o puntos de control): copias periódicas del estado en disco. Solas no alcanzan: lo ocurrido después de la última copia se pierde; por eso se combinan con el registro.
- **Memoria no volátil (NVRAM)**: memoria con respaldo que conserva los datos al cortarse la energía. Es una solución de hardware, más cara.

Son técnicas generales de las bases en memoria (ver Silberschatz et al.); cada producto implementa las suyas. SQL Server usa el registro de transacciones y archivos de punto de control en disco.

## Tablas variables, temporales y en memoria

La cátedra pide no confundir estos tres objetos:

| | Variable de tabla | Tabla temporal | Tabla en memoria |
|---|---|---|---|
| Alcance | El módulo en ejecución (lote, procedimiento, disparador) | La sesión (la global `##`, todas mientras se use) | Idéntico a otras tablas |
| Dónde vive | Intenta mantenerse en memoria, pero está en `tempdb` | `tempdb` | En memoria (con el esquema respetado) |
| Cómo se declara | `DECLARE @t TABLE (...)` | `CREATE TABLE #t` o `##t` | `CREATE TABLE` con una cláusula; el nombre no la distingue |
| Su contenido | Se pierde al salir del alcance | Se pierde al cerrarse la sesión | No se pierde (salvo reinicio si no es persistente) |
| Índices y estadísticas | Sin estadísticas; solo los de sus restricciones | Admite índices y estadísticas | Índices no agrupados (no hay índice clúster) |

### Tablas temporales

Una tabla temporal **local** (`#`) es visible solo en la sesión que la crea, y la **global** (`##`) en todas las sesiones activas. Ambas se guardan en `tempdb`; a la local el motor le agrega un sufijo único, para que varias sesiones puedan tener su propia `#Temporal` a la vez, y la global conserva el nombre exacto, por lo que no puede haber dos iguales.

<!-- check: U2.T.IM.05 -->
```sql
CREATE TABLE #Temporal (Id INT NOT NULL PRIMARY KEY, Texto VARCHAR(10) NOT NULL);
INSERT #Temporal (Id, Texto) VALUES (11, 'Hola');

CREATE TABLE ##TemporalGlobalU2 (Id INT NOT NULL PRIMARY KEY, Texto VARCHAR(20) NOT NULL);
INSERT ##TemporalGlobalU2 (Id, Texto) VALUES (1, 'Compartida');

DECLARE @Variable TABLE (Id INT NOT NULL);
INSERT @Variable (Id) VALUES (1);

SELECT
    CASE WHEN t.name LIKE N'##%' THEN 'global (##)' ELSE 'local (#)' END AS Tipo,
    CASE WHEN t.name LIKE N'##%' THEN t.name ELSE LEFT(t.name, 9) END     AS NombreEnTempdb,
    CASE WHEN EXISTS (SELECT 1 FROM sys.tables WHERE name LIKE N'#Temporal%') THEN 'sí' ELSE 'no' END AS EnLaBaseActual
FROM tempdb.sys.tables AS t
WHERE t.object_id IN (OBJECT_ID(N'tempdb..#Temporal'), OBJECT_ID(N'tempdb..##TemporalGlobalU2'))
ORDER BY t.name;

-- Sea cual sea la base que se escriba delante, la tabla temporal se resuelve en tempdb.
SELECT Id, Texto FROM master.dbo.#Temporal;
GO
DROP TABLE ##TemporalGlobalU2;
```

| Tipo | NombreEnTempdb | EnLaBaseActual |
|---|---|---|
| global (##) | ##TemporalGlobalU2 | no |
| local (#) | #Temporal | no |

| Id | Texto |
|---:|---|
| 11 | Hola |

Con la última consulta el motor muestra el aviso `Database name 'master' ignored, referencing object in tempdb.`: ignora el nombre de la base y usa `tempdb`. Dos detalles:

- Una tabla global se elimina cuando se cierra la sesión que la creó **y** ninguna otra la está usando; si otra sesión tiene una transacción abierta sobre ella, la eliminación espera.
- Como viven en `tempdb`, su intercalación es la de la instancia: puede causar conflictos al combinarlas con tablas de la base ([collation](/bbdd-aplicadas/unidad-2/teoria/collation/#conflictos-entre-intercalaciones)).

## In-Memory OLTP

:::note[Contenido complementario]
Esta parte no forma parte del programa 2024: la cátedra solo menciona que SQL Server permite tablas en memoria y remite a una guía. Se conserva, actualizada, como ampliación.
:::

**In-Memory OLTP** (nombre anterior, _Hekaton_) es la tecnología de SQL Server para **tablas optimizadas para memoria**. Los datos residen en RAM y el motor trabaja sin bloqueos tradicionales (con versionado de filas). Conviene en cargas OLTP de alta concurrencia con baja latencia, y se desempeña mejor con más escrituras que lecturas: colas, tablas de sesión, cachés, datos de sensores. Existe desde SQL Server 2014 y desde SQL Server 2016 SP1 está disponible en todas las ediciones. Las restricciones que se describen se verificaron en SQL Server 2022.

### Preparar la base

La base necesita un filegroup de tipo `MEMORY_OPTIMIZED_DATA`, que se puede agregar al crearla o después, y un contenedor (un directorio, que SQL Server crea). Una vez agregado, el filegroup no se puede quitar sin descartar la base. En el código siguiente la ruta se arma junto al archivo de datos para que funcione tanto en Windows como en Linux; en una instalación propia se puede usar un directorio como `C:\datos\MiBase_mem`, que no debe existir.

<!-- check: U2.T.IM.01 -->
```sql
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
SELECT
    fg.name      AS Filegroup,
    fg.type_desc AS TipoFilegroup,
    f.type_desc  AS TipoArchivo
FROM sys.filegroups AS fg
INNER JOIN sys.database_files AS f
    ON f.data_space_id = fg.data_space_id
WHERE fg.type = 'FX';
```

| Filegroup | TipoFilegroup | TipoArchivo |
|---|---|---|
| FgMemoria | MEMORY_OPTIMIZED_DATA_FILEGROUP | FILESTREAM |

El «archivo» del filegroup es en realidad un contenedor (un directorio); por eso su tipo figura como `FILESTREAM`. `sys.filegroups` no tiene columna `database_id`: lista los de la base actual.

### Crear las tablas y modos de durabilidad

Se crean con `MEMORY_OPTIMIZED = ON`, una `PRIMARY KEY` obligatoriamente **no agrupada** (no hay índice clúster) y el modo de durabilidad:

| Modo | Qué persiste |
|---|---|
| `SCHEMA_AND_DATA` | El esquema y los datos; usa el registro de transacciones y archivos de punto de control. |
| `SCHEMA_ONLY` | Solo el esquema; los datos se pierden al reiniciar. Útil para cachés, staging y datos de sesión. |

<!-- check: U2.T.IM.02 -->
```sql
CREATE SCHEMA mem;
GO
CREATE TABLE mem.Inventario (
    ProductoId  INT            NOT NULL,
    Descripcion NVARCHAR(100)  NOT NULL,
    Stock       INT            NOT NULL CONSTRAINT DF_Inventario_Stock DEFAULT (0),
    CONSTRAINT PK_Inventario PRIMARY KEY NONCLUSTERED (ProductoId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);

CREATE TABLE mem.SesionActiva (
    SesionId INT          NOT NULL,
    Usuario  VARCHAR(40)  NOT NULL,
    Inicio   DATETIME2    NOT NULL CONSTRAINT DF_SesionActiva_Inicio DEFAULT (SYSDATETIME()),
    CONSTRAINT PK_SesionActiva PRIMARY KEY NONCLUSTERED (SesionId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_ONLY);

INSERT mem.Inventario (ProductoId, Descripcion, Stock) VALUES (1, N'Teclado', 50), (2, N'Mouse', 0);
UPDATE mem.Inventario SET Stock = Stock - 1 WHERE ProductoId = 1;
INSERT mem.SesionActiva (SesionId, Usuario) VALUES (1, 'usuario01');

SELECT
    SCHEMA_NAME(t.schema_id) AS Esquema,
    t.name                   AS Tabla,
    t.durability_desc        AS Durabilidad
FROM sys.tables AS t
WHERE t.is_memory_optimized = 1
ORDER BY t.name;
```

| Esquema | Tabla | Durabilidad |
|---|---|---|
| mem | Inventario | SCHEMA_AND_DATA |
| mem | SesionActiva | SCHEMA_ONLY |

El `INSERT`, el `UPDATE` y el `SELECT` son los de siempre. Internamente un `UPDATE` se registra como un borrado y una inserción, con una versión nueva de la fila.

### Qué se admite y qué no

Varias restricciones que se mencionaban en versiones antiguas ya no existen. Resultado en SQL Server 2022:

<!-- check: U2.T.IM.03 -->
```sql
CREATE SCHEMA mem;
GO
CREATE TABLE mem.Cuenta (
    CuentaId INT          NOT NULL,
    Titular  VARCHAR(40)  NOT NULL,
    Saldo    DECIMAL(12,2) NOT NULL,
    Nota     VARCHAR(100) NULL,                  -- columna que admite NULL
    CONSTRAINT PK_MemCuenta PRIMARY KEY NONCLUSTERED (CuentaId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);
CREATE TABLE dbo.DiscoCuenta (CuentaId INT NOT NULL PRIMARY KEY);

CREATE TABLE #Resultado (Orden INT NOT NULL, Caso VARCHAR(60) NOT NULL, Resultado VARCHAR(30) NOT NULL);

BEGIN TRY
    EXEC (N'CREATE TABLE mem.Movimiento (
                MovimientoId INT NOT NULL PRIMARY KEY NONCLUSTERED,
                CuentaId INT NOT NULL,
                CONSTRAINT FK_MemMovimiento_MemCuenta FOREIGN KEY (CuentaId) REFERENCES mem.Cuenta (CuentaId)
            ) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA)');
    INSERT #Resultado VALUES (1, 'FOREIGN KEY entre dos tablas en memoria', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (1, 'FOREIGN KEY entre dos tablas en memoria', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'CREATE TABLE mem.Auxiliar (
                Id INT NOT NULL PRIMARY KEY NONCLUSTERED,
                CuentaId INT NOT NULL,
                CONSTRAINT FK_MemAuxiliar_DiscoCuenta FOREIGN KEY (CuentaId) REFERENCES dbo.DiscoCuenta (CuentaId)
            ) WITH (MEMORY_OPTIMIZED = ON)');
    INSERT #Resultado VALUES (2, 'FOREIGN KEY hacia una tabla en disco', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (2, 'FOREIGN KEY hacia una tabla en disco', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'CREATE TABLE mem.Agrupada (Id INT NOT NULL PRIMARY KEY CLUSTERED) WITH (MEMORY_OPTIMIZED = ON)');
    INSERT #Resultado VALUES (3, 'PRIMARY KEY CLUSTERED', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (3, 'PRIMARY KEY CLUSTERED', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'TRUNCATE TABLE mem.Cuenta');
    INSERT #Resultado VALUES (4, 'TRUNCATE TABLE', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (4, 'TRUNCATE TABLE', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cuenta ADD Moneda CHAR(3) NOT NULL CONSTRAINT DF_MemCuenta_Moneda DEFAULT (''ARS'')');
    INSERT #Resultado VALUES (5, 'ALTER TABLE ... ADD', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (5, 'ALTER TABLE ... ADD', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cuenta ADD NotaLarga VARCHAR(MAX) NULL');
    INSERT #Resultado VALUES (6, 'Columna VARCHAR(MAX)', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (6, 'Columna VARCHAR(MAX)', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cuenta ADD SaldoDoble AS (Saldo * 2)');
    INSERT #Resultado VALUES (7, 'Columna calculada con una operación aritmética', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (7, 'Columna calculada con una operación aritmética', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cuenta ADD TitularMayuscula AS (UPPER(Titular))');
    INSERT #Resultado VALUES (8, 'Columna calculada con UPPER', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (8, 'Columna calculada con UPPER', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

SELECT Caso, Resultado
FROM #Resultado
ORDER BY Orden;
```

| Caso | Resultado |
|---|---|
| FOREIGN KEY entre dos tablas en memoria | admitido |
| FOREIGN KEY hacia una tabla en disco | error 1750 |
| PRIMARY KEY CLUSTERED | error 12317 |
| TRUNCATE TABLE | error 10794 |
| ALTER TABLE ... ADD | admitido |
| Columna VARCHAR(MAX) | admitido |
| Columna calculada con una operación aritmética | admitido |
| Columna calculada con UPPER | error 10794 |

- **Claves foráneas**: se admiten entre tablas en memoria (desde SQL Server 2016); no hacia una tabla en disco. El error 1750 es el envoltorio; el motor informa antes el 10778 («Foreign key relationships between memory optimized tables and non-memory optimized tables are not supported»).
- **Columnas `NULL`**: se admiten desde SQL Server 2016, así que no es obligatorio `NOT NULL` ni un valor por defecto.
- **`ALTER TABLE`**: se admite desde 2016 (agregar, modificar o eliminar columnas e índices, con la tabla reconstruida en memoria).
- **Columnas calculadas**: se admiten desde SQL Server 2017, pero no cualquier función dentro de ellas (`UPPER` falla con el error 10794).
- **Tipos grandes**: `VARCHAR(MAX)` se admite en columnas (almacenado fuera de la fila), aunque no sirve como clave de índice.
- **Sin índice clúster ni `TRUNCATE TABLE`**: se usa `PRIMARY KEY NONCLUSTERED` y `DELETE`.

### Índices

Hay dos tipos de índice, y siempre deben declararse al crear la tabla o con `ALTER TABLE`:

- **Hash**: óptimo para búsquedas por igualdad exacta (`WHERE Id = 5`); no sirve para rangos. Requiere `BUCKET_COUNT`: la cantidad de cubetas. Una referencia habitual es acercarla a una o dos veces la cantidad de valores distintos esperados (es una heurística, no una regla).
- **No agrupado (_range_)**: sirve para rangos, `BETWEEN` y `ORDER BY`. En las tablas en memoria usa una estructura llamada Bw-tree (no el árbol B+ de las tablas en disco).

### Procedimientos compilados de forma nativa

Un procedimiento con `NATIVE_COMPILATION` se compila a código máquina al crearse. Tiene restricciones: requiere `SCHEMABINDING` y un bloque `BEGIN ATOMIC`, y **no admite `NEXT VALUE FOR`**. La secuencia se consulta fuera del procedimiento y se pasa por parámetro. Tampoco se puede usar la secuencia como `DEFAULT` de una columna de una tabla en memoria.

<!-- check: U2.T.IM.04 -->
```sql
CREATE SCHEMA mem;
GO
CREATE SEQUENCE mem.SecuenciaEvento AS BIGINT START WITH 1;
GO
CREATE TABLE mem.Evento (
    EventoId BIGINT        NOT NULL,
    Fecha    DATETIME2     NOT NULL,
    Importe  DECIMAL(12,2) NOT NULL,
    CONSTRAINT PK_Evento PRIMARY KEY NONCLUSTERED HASH (EventoId) WITH (BUCKET_COUNT = 1024),
    INDEX IX_Evento_Fecha NONCLUSTERED (Fecha)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);
GO
CREATE PROCEDURE mem.RegistrarEvento
    @EventoId BIGINT,
    @Fecha    DATETIME2,
    @Importe  DECIMAL(12,2)
WITH NATIVE_COMPILATION, SCHEMABINDING
AS
BEGIN ATOMIC WITH (TRANSACTION ISOLATION LEVEL = SNAPSHOT, LANGUAGE = N'us_english')
    INSERT INTO mem.Evento (EventoId, Fecha, Importe)
    VALUES (@EventoId, @Fecha, @Importe);
END;
GO
-- NEXT VALUE FOR no se admite dentro del módulo nativo: el número se pide afuera y se pasa por parámetro.
DECLARE @Id BIGINT = NEXT VALUE FOR mem.SecuenciaEvento;
EXEC mem.RegistrarEvento @Id, '2026-03-01T10:00:00', 150.00;
SET @Id = NEXT VALUE FOR mem.SecuenciaEvento;
EXEC mem.RegistrarEvento @Id, '2026-03-02T11:30:00', 75.50;

SELECT
    i.name      AS Indice,
    i.type_desc AS Tipo
FROM sys.indexes AS i
WHERE i.object_id = OBJECT_ID(N'mem.Evento')
  AND i.type > 0
ORDER BY i.name;

SELECT EventoId, Fecha, Importe
FROM mem.Evento
ORDER BY EventoId;
```

| Indice | Tipo |
|---|---|
| IX_Evento_Fecha | NONCLUSTERED |
| PK_Evento | NONCLUSTERED HASH |

| EventoId | Fecha | Importe |
|---:|---|---:|
| 1 | 2026-03-01 10:00:00.0000000 | 150.00 |
| 2 | 2026-03-02 11:30:00.0000000 | 75.50 |

Fuera del módulo nativo (con T-SQL interpretado) las tablas en memoria se usan con las mismas sentencias que las demás.

### Almacenamiento interno: disco y memoria

| Categoría | Tabla en disco | Tabla en memoria |
|---|---|---|
| Estructura | Filas en páginas de 8 KB | Filas sin estructura de páginas |
| Índices | Almacenados en páginas, junto con los datos | Residen en memoria y se reconstruyen al iniciar la base |
| Operaciones | Se carga la página en el _buffer pool_ (E/S) y se modifica | Los datos ya están en RAM; un proceso en segundo plano persiste en archivos de datos y de cambios |
| `UPDATE` | Modifica en el lugar (o borra e inserta si cambia la clave) | Se registra como borrado más inserción: genera otra versión de la fila |
| Fragmentación | Las páginas se fragmentan: `REBUILD` / `REORGANIZE` | No hay páginas fragmentadas; un proceso de fondo (`MERGE`) compacta los archivos |

### Monitoreo

<!-- check: U2.T.IM.06 -->
```sql
CREATE SCHEMA mem;
GO
CREATE TABLE mem.Inventario (
    ProductoId  INT           NOT NULL,
    Descripcion NVARCHAR(100) NOT NULL,
    CONSTRAINT PK_Inventario PRIMARY KEY NONCLUSTERED (ProductoId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);
INSERT mem.Inventario (ProductoId, Descripcion) VALUES (1, N'Teclado'), (2, N'Mouse');

SELECT
    t.name                                     AS Tabla,
    t.durability_desc                          AS Durabilidad,
    CASE WHEN s.memory_allocated_for_table_kb > 0 THEN 'sí' ELSE 'no' END AS UsaMemoria
FROM sys.tables AS t
INNER JOIN sys.dm_db_xtp_table_memory_stats AS s
    ON s.object_id = t.object_id
WHERE t.is_memory_optimized = 1
ORDER BY t.name;
```

| Tabla | Durabilidad | UsaMemoria |
|---|---|---|
| Inventario | SCHEMA_AND_DATA | sí |

(El motor agrega un aviso sobre el orden del `JOIN`, porque la vista de gestión usa una sugerencia interna.) Para saber cuántos kilobytes ocupa cada tabla, se consulta la columna `memory_allocated_for_table_kb`.

:::caution[Errores frecuentes]
- Repetir que las tablas en memoria no admiten claves foráneas, columnas `NULL`, `ALTER TABLE` o columnas calculadas: eso era cierto en SQL Server 2014 y ya no.
- Usar `NEXT VALUE FOR` dentro de un procedimiento nativo o como `DEFAULT` de una tabla en memoria.
- Elegir `SCHEMA_ONLY` para datos que no pueden perderse en un reinicio.
- Crear la tabla sin el filegroup `MEMORY_OPTIMIZED_DATA`, o con una `PRIMARY KEY CLUSTERED`.
:::

## Autoevaluación

**1. ¿Por qué una base en memoria necesita técnicas adicionales de durabilidad?**

<details>
<summary>Respuesta</summary>

Porque la RAM es volátil: ante un corte de energía se pierde su contenido. Se combinan registro de transacciones, instantáneas o memoria no volátil.
</details>

**2. ¿Qué diferencia hay entre una variable de tabla, una tabla temporal y una tabla en memoria en cuanto a alcance y duración?**

<details>
<summary>Respuesta</summary>

La variable vive en el módulo en ejecución; la temporal, en la sesión (la global, mientras la usen); la tabla en memoria tiene el mismo alcance que cualquier tabla y, con `SCHEMA_AND_DATA`, sobrevive al reinicio.
</details>

:::tip[En resumen]
- Una base en memoria evita la E/S de disco, pero es volátil y está limitada por la RAM.
- No hay que confundir variable de tabla, tabla temporal (en `tempdb`) y tabla en memoria.
- In-Memory OLTP (complementario) requiere un filegroup `MEMORY_OPTIMIZED_DATA`, una `PRIMARY KEY` no agrupada y elegir `SCHEMA_AND_DATA` o `SCHEMA_ONLY`.
- Desde 2016/2017 se admiten claves foráneas entre tablas en memoria, columnas `NULL`, `ALTER TABLE` y columnas calculadas.
:::

## Fuentes

- Presentación de cátedra, Unidad 2, parte 1: bases de datos en memoria, comparación con disco, tablas variables, temporales y en memoria.
- Microsoft Learn: [Descripción general de In-Memory OLTP](https://learn.microsoft.com/es-es/sql/relational-databases/in-memory-oltp/overview-and-usage-scenarios), [transact-SQL compatible con In-Memory OLTP](https://learn.microsoft.com/es-es/sql/relational-databases/in-memory-oltp/transact-sql-support-for-in-memory-oltp) y [tablas temporales](https://learn.microsoft.com/es-es/sql/t-sql/statements/create-table-transact-sql).
- Silberschatz, Korth y Sudarshan, _Fundamentos de bases de datos_: bases de datos en memoria principal.
