-- u2 · Ejercicio U2.41: preparar una base para In-Memory OLTP y comprobar el filegroup.
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
