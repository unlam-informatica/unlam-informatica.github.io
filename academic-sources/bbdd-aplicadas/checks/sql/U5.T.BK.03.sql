:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_03';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_03_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('A_LOG1');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_03_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Pedido (Estado) VALUES ('B_LOG2');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_03_log2.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
GO
CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_T_BK_03_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'RESTORE DATABASE [chk_U5_T_BK_03_rest] FROM DISK = N''/tmp/U5_T_BK_03_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_03_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_03_rest.ldf'', NORECOVERY;';
EXEC (@Sql);
EXEC (N'RESTORE LOG [chk_U5_T_BK_03_rest] FROM DISK = N''/tmp/U5_T_BK_03_log1.trn'' WITH NORECOVERY;');
DECLARE @Estado NVARCHAR(60) = (SELECT state_desc FROM sys.databases WHERE name = N'chk_U5_T_BK_03_rest');
EXEC (N'RESTORE LOG [chk_U5_T_BK_03_rest] FROM DISK = N''/tmp/U5_T_BK_03_log2.trn'' WITH RECOVERY;');
CREATE TABLE ##Est (Etapa VARCHAR(40), Estado NVARCHAR(60));
INSERT ##Est VALUES ('Tras el primer log', @Estado), ('Tras el ultimo log', (SELECT state_desc FROM sys.databases WHERE name = N'chk_U5_T_BK_03_rest'));
GO
:out stdout
SELECT Etapa, Estado FROM ##Est ORDER BY Etapa DESC;
SELECT p.Estado FROM [chk_U5_T_BK_03_rest].dbo.Pedido AS p ORDER BY p.PedidoId;
GO
:out /dev/null
BEGIN TRY
    IF DB_ID(N'chk_U5_T_BK_03_rest') IS NOT NULL
    BEGIN
        EXEC (N'DROP DATABASE [chk_U5_T_BK_03_rest]');
    END;
END TRY
BEGIN CATCH
END CATCH;
GO
