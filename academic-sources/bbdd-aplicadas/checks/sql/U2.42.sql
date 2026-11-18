-- u2 · Ejercicio U2.42: elegir la durabilidad según el dato.
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
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
