-- Cadena full -> log -> diferencial -> log sobre la base de prueba; resultado: lo que registra msdb.
:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_01';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX) = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_01_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('A_LOG1');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_01_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('B_DIFF');
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_01_diff.bak'' WITH DIFFERENTIAL, INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('C_LOG2');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_01_log2.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
GO
:out stdout
SELECT ROW_NUMBER() OVER (ORDER BY backup_set_id) AS Orden,
       type AS Tipo,
       CASE type WHEN 'D' THEN 'Completo' WHEN 'I' THEN 'Diferencial' WHEN 'L' THEN 'Log' END AS Descripcion,
       is_copy_only AS SoloCopia
FROM msdb.dbo.backupset
WHERE database_name = DB_NAME()
ORDER BY backup_set_id;
