:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_13';
GO
CREATE SCHEMA respaldo;
GO
CREATE TABLE respaldo.Pedido (
    PedidoId  INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY,
    ClienteId INT           NOT NULL,
    Importe   DECIMAL(10,2) NOT NULL,
    Estado    VARCHAR(20)   NOT NULL
);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
INSERT respaldo.Pedido (ClienteId, Importe, Estado) VALUES (1, 50, 'P0_EN_FULL');
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_13_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT respaldo.Pedido (ClienteId, Importe, Estado) VALUES (1, 100, 'P1_EN_LOG1');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_13_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT respaldo.Pedido (ClienteId, Importe, Estado) VALUES (1, 200, 'P2_EN_DIFF');
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_13_diff.bak'' WITH INIT, CHECKSUM, DIFFERENTIAL;';
EXEC (@Sql);
INSERT respaldo.Pedido (ClienteId, Importe, Estado) VALUES (1, 300, 'P3_EN_LOG2');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_13_log2.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
BEGIN TRANSACTION ErrorLogico WITH MARK 'actualizacion sin WHERE';
    UPDATE respaldo.Pedido SET Estado = 'ERROR_LOGICO';
COMMIT TRANSACTION;
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_13_log3.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
GO
DROP TABLE IF EXISTS #Archivo; CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_T_BK_13_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX) = N'RESTORE DATABASE [chk_U5_T_BK_13_rest] FROM DISK = N''/tmp/U5_T_BK_13_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_13_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_13_rest.ldf'', NORECOVERY;';
EXEC (@Sql);
EXEC (N'RESTORE DATABASE [chk_U5_T_BK_13_rest] FROM DISK = N''/tmp/U5_T_BK_13_diff.bak'' WITH NORECOVERY;');
EXEC (N'RESTORE LOG [chk_U5_T_BK_13_rest] FROM DISK = N''/tmp/U5_T_BK_13_log2.trn'' WITH NORECOVERY;');
EXEC (N'RESTORE LOG [chk_U5_T_BK_13_rest] FROM DISK = N''/tmp/U5_T_BK_13_log3.trn'' WITH STOPBEFOREMARK = N''ErrorLogico'', RECOVERY;');
GO
:out stdout
SELECT p.PedidoId, p.Importe, p.Estado FROM [chk_U5_T_BK_13_rest].respaldo.Pedido AS p ORDER BY p.PedidoId;
SELECT ROW_NUMBER() OVER (ORDER BY b.backup_set_id) AS Orden,
       CASE b.type WHEN 'D' THEN 'Completo' WHEN 'I' THEN 'Diferencial' ELSE 'Log' END AS Tipo
FROM msdb.dbo.backupset AS b WHERE b.database_name = N'chk_U5_T_BK_13' ORDER BY b.backup_set_id;
GO
:out /dev/null
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_13_rest]');
END TRY
BEGIN CATCH
END CATCH;
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_13_rest2]');
END TRY
BEGIN CATCH
END CATCH;
GO
