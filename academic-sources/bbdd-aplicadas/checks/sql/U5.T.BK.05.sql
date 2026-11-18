:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_05';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_05_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('A_DIA1');
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_05_diff1.bak'' WITH INIT, CHECKSUM, DIFFERENTIAL;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('B_DIA2');
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_05_diff2.bak'' WITH INIT, CHECKSUM, DIFFERENTIAL;';
EXEC (@Sql);
GO
DROP TABLE IF EXISTS #Archivo; CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_T_BK_05_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX) = N'RESTORE DATABASE [chk_U5_T_BK_05_rest] FROM DISK = N''/tmp/U5_T_BK_05_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_05_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_05_rest.ldf'', NORECOVERY;';
EXEC (@Sql);
EXEC (N'RESTORE DATABASE [chk_U5_T_BK_05_rest] FROM DISK = N''/tmp/U5_T_BK_05_diff2.bak'' WITH RECOVERY;');
GO
:out stdout
SELECT 'Filas tras full + diff2' AS Concepto, COUNT(*) AS Valor FROM [chk_U5_T_BK_05_rest].dbo.Pedido
UNION ALL
SELECT 'Diferenciales con la misma base', COUNT(DISTINCT differential_base_lsn) FROM msdb.dbo.backupset WHERE database_name = DB_NAME() AND type = 'I'
ORDER BY Concepto;
GO
:out /dev/null
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_05_rest]');
END TRY
BEGIN CATCH
END CATCH;
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_05_rest2]');
END TRY
BEGIN CATCH
END CATCH;
GO
