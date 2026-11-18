:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_LOG_01';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
CREATE TABLE ##Res (Orden INT, Momento VARCHAR(60), Modelo VARCHAR(20), Espera VARCHAR(40));
INSERT ##Res SELECT 1, 'FULL sin ningun backup completo', recovery_model_desc, log_reuse_wait_desc FROM sys.databases WHERE database_id = DB_ID();
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_LOG_01_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) SELECT TOP (20000) 'masivo' FROM sys.all_objects AS a CROSS JOIN sys.all_objects AS b;
CHECKPOINT;
INSERT ##Res SELECT 2, 'Tras el full y un cambio', recovery_model_desc, log_reuse_wait_desc FROM sys.databases WHERE database_id = DB_ID();
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_LOG_01_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
CHECKPOINT;
INSERT ##Res SELECT 3, 'Tras el backup de log', recovery_model_desc, log_reuse_wait_desc FROM sys.databases WHERE database_id = DB_ID();
GO
:out stdout
SELECT Momento, Modelo, Espera FROM ##Res ORDER BY Orden;
