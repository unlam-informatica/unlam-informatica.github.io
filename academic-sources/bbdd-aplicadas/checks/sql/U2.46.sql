-- u2 · Ejercicio U2.46: carga repetida en una tabla de disco y en una en memoria (se verifica la cantidad de filas, no los tiempos).
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
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
