-- u2 · In-Memory OLTP: tablas con las dos durabilidades y DML habitual.
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
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
