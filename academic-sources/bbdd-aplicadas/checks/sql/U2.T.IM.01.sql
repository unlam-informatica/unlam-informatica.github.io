-- u2 · In-Memory OLTP: filegroup MEMORY_OPTIMIZED_DATA y su contenedor.
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
