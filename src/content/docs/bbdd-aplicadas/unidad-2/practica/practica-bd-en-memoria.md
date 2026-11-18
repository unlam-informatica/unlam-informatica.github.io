---
title: Práctica — BD en memoria (In-Memory OLTP)
slug: bbdd-aplicadas/unidad-2/practica/bd-en-memoria
sidebar:
  order: 6
  label: BD en memoria (In-Memory OLTP)
---

Presupone la lección [BD en memoria](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/). In-Memory OLTP es contenido complementario (no forma parte del programa 2024); los ejercicios se ejecutan sobre SQL Server 2022.

## Preparación

Cada ejercicio parte de una base vacía a la que se le agrega el filegroup `MEMORY_OPTIMIZED_DATA` y su contenedor. Esta preparación se hace una sola vez por base, y el filegroup no se puede quitar sin descartar la base. La ruta del contenedor se arma junto al archivo de datos, para que funcione tanto en Windows como en Linux; en una instalación propia también se puede usar un directorio nuevo como `C:\SQLData\PracticaMem_mem` (no debe existir: SQL Server lo crea).

El ejercicio 41 muestra la preparación completa; en los demás se da por hecha (los scripts de verificación la incluyen).

### Ejercicio 41 · Preparar la base y crear la primera tabla
<!-- ejercicio: U2.41 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Agregá a la base actual un filegroup `MEMORY_OPTIMIZED_DATA` con su contenedor, creá en el esquema `mem` la tabla `Sesion` (clave primaria no agrupada, durabilidad `SCHEMA_AND_DATA`) y comprobá con las vistas de catálogo cuántos filegroups de memoria y cuántas tablas en memoria hay, y qué durabilidad tiene `Sesion`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El filegroup y su archivo se agregan con `ALTER DATABASE CURRENT`. La tabla lleva `MEMORY_OPTIMIZED = ON`. Las comprobaciones salen de `sys.filegroups` (tipo `FX`) y `sys.tables`.

<!-- check: U2.41 -->
```sql
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
CREATE SCHEMA mem;
GO
CREATE TABLE mem.Sesion (
    SesionId INT         NOT NULL,
    Usuario  VARCHAR(40) NOT NULL,
    Activa   BIT         NOT NULL CONSTRAINT DF_Sesion_Activa DEFAULT (1),
    CONSTRAINT PK_Sesion PRIMARY KEY NONCLUSTERED (SesionId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);

SELECT
    (SELECT COUNT(*) FROM sys.filegroups WHERE type = 'FX')                  AS FilegroupsEnMemoria,
    (SELECT COUNT(*) FROM sys.tables WHERE is_memory_optimized = 1)           AS TablasEnMemoria,
    (SELECT durability_desc FROM sys.tables WHERE name = N'Sesion')           AS Durabilidad;
```

**Resultado esperado.**

| FilegroupsEnMemoria | TablasEnMemoria | Durabilidad |
|---:|---:|---|
| 1 | 1 | SCHEMA_AND_DATA |

`sys.filegroups` no tiene columna `database_id`: lista solo los de la base actual, así que no hace falta filtrar por base. Con una clave primaria `CLUSTERED` la creación fallaría.

</details>

### Ejercicio 42 · Elegir la durabilidad según el dato
<!-- ejercicio: U2.42 | nivel: inicial | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Una tienda necesita dos tablas en memoria: una caché de precios (`PrecioCache`), que se puede reconstruir desde la base principal, y las reservas de clientes (`Reserva`), que no pueden perderse. Creá ambas con la durabilidad adecuada y listá su durabilidad.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La caché es derivable: `SCHEMA_ONLY` es suficiente y evita el costo del registro. Las reservas requieren `SCHEMA_AND_DATA`.

<!-- check: U2.42 -->
```sql
CREATE SCHEMA mem;
GO
CREATE TABLE mem.PrecioCache (
    ProductoId INT           NOT NULL,
    Precio     DECIMAL(12,2) NOT NULL,
    CONSTRAINT PK_PrecioCache PRIMARY KEY NONCLUSTERED (ProductoId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_ONLY);

CREATE TABLE mem.Reserva (
    ReservaId INT         NOT NULL,
    Cliente   VARCHAR(40) NOT NULL,
    CONSTRAINT PK_Reserva PRIMARY KEY NONCLUSTERED (ReservaId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);

SELECT t.name AS Tabla, t.durability_desc AS Durabilidad
FROM sys.tables AS t
WHERE t.is_memory_optimized = 1
ORDER BY t.name;
```

**Resultado esperado.**

| Tabla | Durabilidad |
|---|---|
| PrecioCache | SCHEMA_ONLY |
| Reserva | SCHEMA_AND_DATA |

Con `SCHEMA_ONLY`, después de reiniciar el servicio la tabla `PrecioCache` existe pero está vacía. Las reservas se recuperan del registro de transacciones y de los archivos de punto de control.

</details>

### Ejercicio 43 · DML con IDENTITY y DEFAULT
<!-- ejercicio: U2.43 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Creá `mem.Tarea` con una columna `IDENTITY(1, 1)` y un estado cuyo valor por defecto sea `'pendiente'`. Insertá cuatro tareas, marcá una como `'hecha'`, eliminá otra y mostrá el resultado.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las tablas en memoria admiten `IDENTITY` (con semilla e incremento 1) y `DEFAULT`, y las sentencias DML habituales.

<!-- check: U2.43 -->
```sql
CREATE SCHEMA mem;
GO
CREATE TABLE mem.Tarea (
    TareaId     INT IDENTITY(1, 1) NOT NULL,
    Descripcion VARCHAR(60)        NOT NULL,
    Estado      VARCHAR(10)        NOT NULL CONSTRAINT DF_Tarea_Estado DEFAULT ('pendiente'),
    CONSTRAINT PK_Tarea PRIMARY KEY NONCLUSTERED (TareaId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_ONLY);

INSERT mem.Tarea (Descripcion) VALUES ('Armar informe'), ('Revisar índice'), ('Cerrar caja'), ('Archivar legajo');
UPDATE mem.Tarea SET Estado = 'hecha' WHERE Descripcion = 'Revisar índice';
DELETE FROM mem.Tarea WHERE Descripcion = 'Archivar legajo';

SELECT TareaId, Descripcion, Estado
FROM mem.Tarea
ORDER BY TareaId;
```

**Resultado esperado.**

| TareaId | Descripcion | Estado |
|---:|---|---|
| 1 | Armar informe | pendiente |
| 2 | Revisar índice | hecha |
| 3 | Cerrar caja | pendiente |

La tarea 4 se eliminó, pero su número de `IDENTITY` no se reutiliza: la próxima fila recibiría el 5.

</details>

### Ejercicio 44 · Claves foráneas y ALTER TABLE
<!-- ejercicio: U2.44 | nivel: intermedio | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Creá `mem.Cliente` y `mem.Pedido` (con una clave foránea entre ambas) y una tabla de disco `dbo.Region`. Agregá una columna `RegionId` a `mem.Cliente`. Comprobá qué pasa al insertar un pedido de un cliente que no existe y al intentar una clave foránea desde `mem.Cliente` hacia `dbo.Region`, y cuántas columnas tiene `mem.Cliente` al final. Corregí la premisa errónea de que `ALTER TABLE` no se admite en tablas en memoria.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las claves foráneas entre tablas en memoria se verifican como siempre (error 547). Hacia una tabla de disco no se admiten. `ALTER TABLE ... ADD` sí se admite desde SQL Server 2016.

<!-- check: U2.44 -->
```sql
CREATE SCHEMA mem;
GO
CREATE TABLE mem.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    CONSTRAINT PK_MemCliente PRIMARY KEY NONCLUSTERED (ClienteId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);
CREATE TABLE mem.Pedido (
    PedidoId  INT NOT NULL,
    ClienteId INT NOT NULL,
    CONSTRAINT PK_MemPedido PRIMARY KEY NONCLUSTERED (PedidoId),
    CONSTRAINT FK_MemPedido_MemCliente FOREIGN KEY (ClienteId) REFERENCES mem.Cliente (ClienteId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);
CREATE TABLE dbo.Region (RegionId INT NOT NULL PRIMARY KEY);
GO
INSERT mem.Cliente (ClienteId, Nombre) VALUES (1, 'Cliente 01');
INSERT mem.Pedido (PedidoId, ClienteId) VALUES (10, 1);
ALTER TABLE mem.Cliente ADD RegionId INT NULL;

CREATE TABLE #Resultado (Orden INT NOT NULL, Caso VARCHAR(60) NOT NULL, Resultado VARCHAR(30) NOT NULL);

BEGIN TRY
    INSERT mem.Pedido (PedidoId, ClienteId) VALUES (11, 99);
    INSERT #Resultado VALUES (1, 'Pedido de un cliente inexistente', 'aceptado');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (1, 'Pedido de un cliente inexistente', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cliente ADD CONSTRAINT FK_MemCliente_Region FOREIGN KEY (RegionId) REFERENCES dbo.Region (RegionId)');
    INSERT #Resultado VALUES (2, 'FOREIGN KEY de una tabla en memoria hacia una de disco', 'aceptado');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (2, 'FOREIGN KEY de una tabla en memoria hacia una de disco', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

INSERT #Resultado
SELECT 3, 'Columnas de mem.Cliente tras el ALTER TABLE', CAST(COUNT(*) AS VARCHAR(10))
FROM sys.columns
WHERE object_id = OBJECT_ID(N'mem.Cliente');

SELECT Caso, Resultado
FROM #Resultado
ORDER BY Orden;
```

**Resultado esperado.**

| Caso | Resultado |
|---|---|
| Pedido de un cliente inexistente | error 547 |
| FOREIGN KEY de una tabla en memoria hacia una de disco | error 1750 |
| Columnas de mem.Cliente tras el ALTER TABLE | 3 |

El `ALTER TABLE` funcionó: la tabla pasó de dos a tres columnas. Lo no admitido es la clave foránea entre una tabla en memoria y una de disco (el motor informa antes el error 10778; aquí se ve el 1750, que lo envuelve).

</details>

### Ejercicio 45 · Índices y un procedimiento nativo con secuencia
<!-- ejercicio: U2.45 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Creá `mem.Lectura` (sensor, fecha, valor) con una clave hash sobre el identificador y un índice por rango sobre la fecha, y un procedimiento compilado de forma nativa que inserte una lectura. El identificador debe salir de una secuencia. Registrá cuatro lecturas y mostrá las que ocurrieron entre el 1 de mayo a las 08:30 y el 3 de mayo a las 00:00.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `NEXT VALUE FOR` no se admite dentro de un módulo nativo, así que el número se pide afuera y se pasa por parámetro. El índice por rango resuelve el filtro por fecha.

<!-- check: U2.45 -->
```sql
CREATE SCHEMA mem;
GO
CREATE SEQUENCE mem.SecuenciaLectura AS INT START WITH 1;
GO
CREATE TABLE mem.Lectura (
    LecturaId INT           NOT NULL,
    SensorId  INT           NOT NULL,
    Fecha     DATETIME2     NOT NULL,
    Valor     DECIMAL(8,2)  NOT NULL,
    CONSTRAINT PK_Lectura PRIMARY KEY NONCLUSTERED HASH (LecturaId) WITH (BUCKET_COUNT = 1024),
    INDEX IX_Lectura_Fecha NONCLUSTERED (Fecha)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_ONLY);
GO
CREATE PROCEDURE mem.RegistrarLectura
    @LecturaId INT,
    @SensorId  INT,
    @Fecha     DATETIME2,
    @Valor     DECIMAL(8,2)
WITH NATIVE_COMPILATION, SCHEMABINDING
AS
BEGIN ATOMIC WITH (TRANSACTION ISOLATION LEVEL = SNAPSHOT, LANGUAGE = N'us_english')
    INSERT INTO mem.Lectura (LecturaId, SensorId, Fecha, Valor)
    VALUES (@LecturaId, @SensorId, @Fecha, @Valor);
END;
GO
DECLARE @Id INT;

SET @Id = NEXT VALUE FOR mem.SecuenciaLectura;
EXEC mem.RegistrarLectura @Id, 7, '2026-05-01T08:00:00', 21.50;
SET @Id = NEXT VALUE FOR mem.SecuenciaLectura;
EXEC mem.RegistrarLectura @Id, 7, '2026-05-01T09:00:00', 22.00;
SET @Id = NEXT VALUE FOR mem.SecuenciaLectura;
EXEC mem.RegistrarLectura @Id, 8, '2026-05-02T08:00:00', 19.25;
SET @Id = NEXT VALUE FOR mem.SecuenciaLectura;
EXEC mem.RegistrarLectura @Id, 8, '2026-05-03T08:00:00', 18.75;

SELECT LecturaId, SensorId, Fecha, Valor
FROM mem.Lectura
WHERE Fecha >= '2026-05-01T08:30:00' AND Fecha < '2026-05-03T00:00:00'
ORDER BY Fecha;
```

**Resultado esperado.**

| LecturaId | SensorId | Fecha | Valor |
|---:|---:|---|---:|
| 2 | 7 | 2026-05-01 09:00:00.0000000 | 22.00 |
| 3 | 8 | 2026-05-02 08:00:00.0000000 | 19.25 |

Las dos lecturas del 1 de mayo a las 08:00 y del 3 de mayo a las 08:00 quedan fuera del intervalo. La consulta usa el índice por rango; el hash solo sirve para igualdad.

</details>

### Ejercicio 46 · Carga repetida en disco y en memoria
<!-- ejercicio: U2.46 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Insertá 5000 filas, una por una, en una tabla de disco y en una tabla en memoria `SCHEMA_ONLY`, midiendo el tiempo de cada carga. Verificá que ambas terminaron con 5000 filas. ¿Por qué el resultado de la comparación no es concluyente con una sola sesión?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se mide cada bucle con `SYSDATETIME()` y `DATEDIFF`. Los milisegundos cambian de una ejecución a otra: lo verificable es la cantidad de filas.

<!-- check: U2.46 -->
```sql
CREATE SCHEMA carga;
GO
CREATE TABLE carga.RegistroDisco (
    RegistroId INT         NOT NULL CONSTRAINT PK_RegistroDisco PRIMARY KEY,
    Usuario    VARCHAR(30) NOT NULL
);
CREATE TABLE carga.RegistroMemoria (
    RegistroId INT         NOT NULL,
    Usuario    VARCHAR(30) NOT NULL,
    CONSTRAINT PK_RegistroMemoria PRIMARY KEY NONCLUSTERED (RegistroId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_ONLY);
GO
DECLARE @Filas INT = 5000;
DECLARE @Inicio DATETIME2;
DECLARE @Contador INT;
DECLARE @MsDisco INT, @MsMemoria INT;

SET @Inicio = SYSDATETIME();
SET @Contador = 1;
WHILE @Contador <= @Filas
BEGIN
    INSERT carga.RegistroDisco (RegistroId, Usuario) VALUES (@Contador, 'usuario' + CAST(@Contador AS VARCHAR(10)));
    SET @Contador += 1;
END;
SET @MsDisco = DATEDIFF(MILLISECOND, @Inicio, SYSDATETIME());

SET @Inicio = SYSDATETIME();
SET @Contador = 1;
WHILE @Contador <= @Filas
BEGIN
    INSERT carga.RegistroMemoria (RegistroId, Usuario) VALUES (@Contador, 'usuario' + CAST(@Contador AS VARCHAR(10)));
    SET @Contador += 1;
END;
SET @MsMemoria = DATEDIFF(MILLISECOND, @Inicio, SYSDATETIME());

-- Los milisegundos cambian en cada ejecución: lo que se puede verificar es que ambas cargas terminaron.
SELECT
    (SELECT COUNT(*) FROM carga.RegistroDisco)   AS FilasDisco,
    (SELECT COUNT(*) FROM carga.RegistroMemoria) AS FilasMemoria,
    CASE WHEN @MsDisco >= 0 AND @MsMemoria >= 0 THEN 'sí' ELSE 'no' END AS TiemposMedidos;
```

**Resultado esperado.**

| FilasDisco | FilasMemoria | TiemposMedidos |
|---:|---:|---|
| 5000 | 5000 | sí |

Con una sola sesión el costo del bucle de T-SQL, que es el mismo en los dos casos, domina el tiempo; la ventaja de las tablas en memoria se nota con muchas sesiones concurrentes escribiendo a la vez. Para comparar, aumentá `@Filas` a 100000 y mirá `@MsDisco` y `@MsMemoria` (agregá `PRINT` o `SELECT` de las variables).

</details>

:::tip[En resumen]
- Preparar la base: filegroup `MEMORY_OPTIMIZED_DATA` y su contenedor.
- Elegir `SCHEMA_ONLY` solo si el dato se puede perder.
- Se admiten claves foráneas entre tablas en memoria y `ALTER TABLE`; no hacia tablas de disco.
- `NEXT VALUE FOR` no entra en un procedimiento nativo: se pasa el valor por parámetro.
:::
