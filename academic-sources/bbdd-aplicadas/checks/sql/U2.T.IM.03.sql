-- u2 · In-Memory OLTP: qué se admite y qué no (SQL Server 2022). Cada caso se prueba por separado.
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
CREATE SCHEMA mem;
GO
CREATE TABLE mem.Cuenta (
    CuentaId INT          NOT NULL,
    Titular  VARCHAR(40)  NOT NULL,
    Saldo    DECIMAL(12,2) NOT NULL,
    Nota     VARCHAR(100) NULL,                  -- columna que admite NULL
    CONSTRAINT PK_MemCuenta PRIMARY KEY NONCLUSTERED (CuentaId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);
CREATE TABLE dbo.DiscoCuenta (CuentaId INT NOT NULL PRIMARY KEY);

CREATE TABLE #Resultado (Orden INT NOT NULL, Caso VARCHAR(60) NOT NULL, Resultado VARCHAR(30) NOT NULL);

BEGIN TRY
    EXEC (N'CREATE TABLE mem.Movimiento (
                MovimientoId INT NOT NULL PRIMARY KEY NONCLUSTERED,
                CuentaId INT NOT NULL,
                CONSTRAINT FK_MemMovimiento_MemCuenta FOREIGN KEY (CuentaId) REFERENCES mem.Cuenta (CuentaId)
            ) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA)');
    INSERT #Resultado VALUES (1, 'FOREIGN KEY entre dos tablas en memoria', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (1, 'FOREIGN KEY entre dos tablas en memoria', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'CREATE TABLE mem.Auxiliar (
                Id INT NOT NULL PRIMARY KEY NONCLUSTERED,
                CuentaId INT NOT NULL,
                CONSTRAINT FK_MemAuxiliar_DiscoCuenta FOREIGN KEY (CuentaId) REFERENCES dbo.DiscoCuenta (CuentaId)
            ) WITH (MEMORY_OPTIMIZED = ON)');
    INSERT #Resultado VALUES (2, 'FOREIGN KEY hacia una tabla en disco', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (2, 'FOREIGN KEY hacia una tabla en disco', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'CREATE TABLE mem.Agrupada (Id INT NOT NULL PRIMARY KEY CLUSTERED) WITH (MEMORY_OPTIMIZED = ON)');
    INSERT #Resultado VALUES (3, 'PRIMARY KEY CLUSTERED', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (3, 'PRIMARY KEY CLUSTERED', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'TRUNCATE TABLE mem.Cuenta');
    INSERT #Resultado VALUES (4, 'TRUNCATE TABLE', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (4, 'TRUNCATE TABLE', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cuenta ADD Moneda CHAR(3) NOT NULL CONSTRAINT DF_MemCuenta_Moneda DEFAULT (''ARS'')');
    INSERT #Resultado VALUES (5, 'ALTER TABLE ... ADD', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (5, 'ALTER TABLE ... ADD', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cuenta ADD NotaLarga VARCHAR(MAX) NULL');
    INSERT #Resultado VALUES (6, 'Columna VARCHAR(MAX)', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (6, 'Columna VARCHAR(MAX)', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cuenta ADD SaldoDoble AS (Saldo * 2)');
    INSERT #Resultado VALUES (7, 'Columna calculada con una operación aritmética', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (7, 'Columna calculada con una operación aritmética', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cuenta ADD TitularMayuscula AS (UPPER(Titular))');
    INSERT #Resultado VALUES (8, 'Columna calculada con UPPER', 'admitido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (8, 'Columna calculada con UPPER', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

SELECT Caso, Resultado
FROM #Resultado
ORDER BY Orden;
