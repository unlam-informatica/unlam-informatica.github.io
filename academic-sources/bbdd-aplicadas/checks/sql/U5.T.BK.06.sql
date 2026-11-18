:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_06';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_06_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('A');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_06_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('B_SIN_RESPALDAR');
GO
USE master;
GO
DECLARE @Base SYSNAME = N'chk_U5_T_BK_06';
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_06_tail.trn'' WITH NORECOVERY, INIT, CHECKSUM;';
EXEC (@Sql);
DECLARE @EstadoOrigen NVARCHAR(60) = (SELECT state_desc FROM sys.databases WHERE name = @Base);
CREATE TABLE ##Est (Concepto VARCHAR(40), Valor NVARCHAR(60));
INSERT ##Est VALUES ('Base origen tras el tail-log', @EstadoOrigen);
GO
DROP TABLE IF EXISTS #Archivo; CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_T_BK_06_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX) = N'RESTORE DATABASE [chk_U5_T_BK_06_rest] FROM DISK = N''/tmp/U5_T_BK_06_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_06_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_06_rest.ldf'', NORECOVERY;';
EXEC (@Sql);
EXEC (N'RESTORE LOG [chk_U5_T_BK_06_rest] FROM DISK = N''/tmp/U5_T_BK_06_log1.trn'' WITH NORECOVERY;');
EXEC (N'RESTORE LOG [chk_U5_T_BK_06_rest] FROM DISK = N''/tmp/U5_T_BK_06_tail.trn'' WITH RECOVERY;');
GO
EXEC (N'RESTORE DATABASE chk_U5_T_BK_06 WITH RECOVERY');
GO
:out stdout
SELECT Concepto, Valor FROM ##Est
UNION ALL
SELECT 'Fila restaurada ' + CAST(p.PedidoId AS VARCHAR(5)), p.Estado FROM [chk_U5_T_BK_06_rest].dbo.Pedido AS p
ORDER BY Concepto;
GO
:out /dev/null
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_06_rest]');
END TRY
BEGIN CATCH
END CATCH;
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_06_rest2]');
END TRY
BEGIN CATCH
END CATCH;
GO
