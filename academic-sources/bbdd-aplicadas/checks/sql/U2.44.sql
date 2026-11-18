-- u2 · Ejercicio U2.44: claves foráneas y ALTER TABLE en tablas en memoria.
ALTER DATABASE CURRENT ADD FILEGROUP FgMemoria CONTAINS MEMORY_OPTIMIZED_DATA;
GO
-- El directorio no debe existir: SQL Server lo crea. Se arma junto al archivo de datos para que funcione en Windows y en Linux.
DECLARE @Ruta NVARCHAR(400) = REPLACE((SELECT TOP (1) physical_name FROM sys.database_files WHERE type = 0), N'.mdf', N'_mem');
DECLARE @Sql  NVARCHAR(MAX) = N'ALTER DATABASE CURRENT ADD FILE (NAME = N''ArchivoMemoria'', FILENAME = N''' + @Ruta + N''') TO FILEGROUP FgMemoria;';
EXEC (@Sql);
GO
CREATE SCHEMA mem;
GO
CREATE TABLE mem.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    CONSTRAINT PK_MemCliente PRIMARY KEY NONCLUSTERED (ClienteId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);
CREATE TABLE mem.Pedido (
    PedidoId  INT NOT NULL,
    ClienteId INT NOT NULL,
    CONSTRAINT PK_MemPedido PRIMARY KEY NONCLUSTERED (PedidoId),
    CONSTRAINT FK_MemPedido_MemCliente FOREIGN KEY (ClienteId) REFERENCES mem.Cliente (ClienteId)
) WITH (MEMORY_OPTIMIZED = ON, DURABILITY = SCHEMA_AND_DATA);
CREATE TABLE dbo.Region (RegionId INT NOT NULL PRIMARY KEY);
GO
INSERT mem.Cliente (ClienteId, Nombre) VALUES (1, 'Cliente 01');
INSERT mem.Pedido (PedidoId, ClienteId) VALUES (10, 1);
ALTER TABLE mem.Cliente ADD RegionId INT NULL;

CREATE TABLE #Resultado (Orden INT NOT NULL, Caso VARCHAR(60) NOT NULL, Resultado VARCHAR(30) NOT NULL);

BEGIN TRY
    INSERT mem.Pedido (PedidoId, ClienteId) VALUES (11, 99);
    INSERT #Resultado VALUES (1, 'Pedido de un cliente inexistente', 'aceptado');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (1, 'Pedido de un cliente inexistente', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

BEGIN TRY
    EXEC (N'ALTER TABLE mem.Cliente ADD CONSTRAINT FK_MemCliente_Region FOREIGN KEY (RegionId) REFERENCES dbo.Region (RegionId)');
    INSERT #Resultado VALUES (2, 'FOREIGN KEY de una tabla en memoria hacia una de disco', 'aceptado');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (2, 'FOREIGN KEY de una tabla en memoria hacia una de disco', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

INSERT #Resultado
SELECT 3, 'Columnas de mem.Cliente tras el ALTER TABLE', CAST(COUNT(*) AS VARCHAR(10))
FROM sys.columns
WHERE object_id = OBJECT_ID(N'mem.Cliente');

SELECT Caso, Resultado
FROM #Resultado
ORDER BY Orden;
