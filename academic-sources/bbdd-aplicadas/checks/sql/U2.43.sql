-- u2 · Ejercicio U2.43: DML sobre una tabla en memoria con IDENTITY y DEFAULT.
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
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
