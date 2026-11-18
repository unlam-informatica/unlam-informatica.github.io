:out /dev/null
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY SIMPLE;
GO
CREATE TABLE ##Res (Orden INT, Momento VARCHAR(70), Espera VARCHAR(40));
BEGIN TRANSACTION;
INSERT dbo.Pedido (Estado) SELECT TOP (20000) 'masivo' FROM sys.all_objects AS a CROSS JOIN sys.all_objects AS b;
CHECKPOINT;
INSERT ##Res SELECT 1, 'Transaccion abierta y CHECKPOINT', log_reuse_wait_desc FROM sys.databases WHERE database_id = DB_ID();
COMMIT TRANSACTION;
CHECKPOINT;
INSERT ##Res SELECT 2, 'Tras el COMMIT y otro CHECKPOINT', log_reuse_wait_desc FROM sys.databases WHERE database_id = DB_ID();
GO
:out stdout
SELECT Momento, Espera FROM ##Res ORDER BY Orden;
