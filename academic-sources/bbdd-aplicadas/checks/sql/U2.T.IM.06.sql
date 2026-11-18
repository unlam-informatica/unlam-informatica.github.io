-- u2 · In-Memory OLTP: consulta de monitoreo de memoria por tabla.
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
