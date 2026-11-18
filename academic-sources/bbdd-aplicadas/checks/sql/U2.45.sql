-- u2 · Ejercicio U2.45: índice hash, índice por rango y procedimiento nativo con secuencia.
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
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
