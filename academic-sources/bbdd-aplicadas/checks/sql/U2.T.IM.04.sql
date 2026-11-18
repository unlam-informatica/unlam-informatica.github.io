-- u2 · In-Memory OLTP: índice hash, índice no clúster, secuencia y procedimiento compilado de forma nativa.
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
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
