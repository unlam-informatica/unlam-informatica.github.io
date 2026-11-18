:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_34';
GO
CREATE TABLE dbo.Reserva (ReservaId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Reserva PRIMARY KEY, Concepto VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_34_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
GO
DROP TABLE IF EXISTS #Archivo; CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_34_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX) = N'RESTORE DATABASE [chk_U5_34_rest] FROM DISK = N''/tmp/U5_34_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_34_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_34_rest.ldf'', NORECOVERY;';
EXEC (@Sql);
CREATE TABLE ##Res (Paso VARCHAR(60), Concepto VARCHAR(30), EnStandby BIT, Filas INT);
INSERT ##Res SELECT '1 secundaria tras restaurar el full', state_desc, is_in_standby, NULL FROM sys.databases WHERE name = N'chk_U5_34_rest';
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
INSERT dbo.Reserva (Concepto) VALUES ('A');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_34_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
EXEC (N'RESTORE LOG [chk_U5_34_rest] FROM DISK = N''/tmp/U5_34_log1.trn'' WITH STANDBY = N''/var/opt/mssql/data/chk_U5_34_rest.undo'';');
DECLARE @F1 INT;
EXEC sp_executesql N'SELECT @C = COUNT(*) FROM [chk_U5_34_rest].dbo.Reserva', N'@C INT OUTPUT', @C = @F1 OUTPUT;
INSERT ##Res SELECT '2 tras aplicar el log 1 con STANDBY', state_desc, is_in_standby, @F1 FROM sys.databases WHERE name = N'chk_U5_34_rest';
INSERT dbo.Reserva (Concepto) VALUES ('B');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_34_log2.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
EXEC (N'RESTORE LOG [chk_U5_34_rest] FROM DISK = N''/tmp/U5_34_log2.trn'' WITH STANDBY = N''/var/opt/mssql/data/chk_U5_34_rest.undo'';');
DECLARE @F2 INT;
EXEC sp_executesql N'SELECT @C = COUNT(*) FROM [chk_U5_34_rest].dbo.Reserva', N'@C INT OUTPUT', @C = @F2 OUTPUT;
INSERT ##Res SELECT '3 tras aplicar el log 2 con STANDBY', state_desc, is_in_standby, @F2 FROM sys.databases WHERE name = N'chk_U5_34_rest';
EXEC (N'RESTORE DATABASE [chk_U5_34_rest] WITH RECOVERY;');
DECLARE @F3 INT;
EXEC sp_executesql N'SELECT @C = COUNT(*) FROM [chk_U5_34_rest].dbo.Reserva', N'@C INT OUTPUT', @C = @F3 OUTPUT;
INSERT ##Res SELECT '4 failover manual: RECOVERY', state_desc, is_in_standby, @F3 FROM sys.databases WHERE name = N'chk_U5_34_rest';
GO
:out stdout
SELECT Paso, Concepto, EnStandby, Filas FROM ##Res ORDER BY Paso;
GO
:out /dev/null
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_34_rest]');
END TRY
BEGIN CATCH
END CATCH;
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_34_rest2]');
END TRY
BEGIN CATCH
END CATCH;
GO
