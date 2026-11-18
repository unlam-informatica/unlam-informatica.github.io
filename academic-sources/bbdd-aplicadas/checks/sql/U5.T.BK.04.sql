:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_04';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_04_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('A');
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_04_copia.bak'' WITH COPY_ONLY, INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('B');
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_04_diff.bak'' WITH INIT, CHECKSUM, DIFFERENTIAL;';
EXEC (@Sql);
GO
:out stdout
SELECT ROW_NUMBER() OVER (ORDER BY b.backup_set_id) AS Orden,
       CASE WHEN b.is_copy_only = 1 THEN 'Completo copy-only'
            WHEN b.type = 'D' THEN 'Completo'
            ELSE 'Diferencial' END AS TipoBackup,
       CASE WHEN b.type = 'I' AND b.differential_base_lsn = (SELECT f.checkpoint_lsn FROM msdb.dbo.backupset AS f WHERE f.database_name = DB_NAME() AND f.type = 'D' AND f.is_copy_only = 0) THEN 'Si' WHEN b.type = 'I' THEN 'No' ELSE '-' END AS BaseEsElCompletoNormal
FROM msdb.dbo.backupset AS b
WHERE b.database_name = DB_NAME()
ORDER BY b.backup_set_id;
