:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_08';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_08_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('A_ANTES');
WAITFOR DELAY '00:00:02';
DECLARE @Momento DATETIME = GETDATE();
WAITFOR DELAY '00:00:02';
INSERT dbo.Pedido (Estado) VALUES ('B_ERROR');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_08_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
CREATE TABLE ##Momento (Valor VARCHAR(30));
INSERT ##Momento VALUES (CONVERT(VARCHAR(30), @Momento, 121));
GO
DROP TABLE IF EXISTS #Archivo; CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_T_BK_08_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX) = N'RESTORE DATABASE [chk_U5_T_BK_08_rest] FROM DISK = N''/tmp/U5_T_BK_08_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_08_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_08_rest.ldf'', NORECOVERY;';
EXEC (@Sql);
DECLARE @T VARCHAR(30) = (SELECT Valor FROM ##Momento);
EXEC (N'RESTORE LOG [chk_U5_T_BK_08_rest] FROM DISK = N''/tmp/U5_T_BK_08_log1.trn'' WITH STOPAT = N''' + @T + N''', RECOVERY;');
GO
:out stdout
SELECT p.Estado FROM [chk_U5_T_BK_08_rest].dbo.Pedido AS p ORDER BY p.PedidoId;
GO
:out /dev/null
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_08_rest]');
END TRY
BEGIN CATCH
END CATCH;
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_08_rest2]');
END TRY
BEGIN CATCH
END CATCH;
GO
