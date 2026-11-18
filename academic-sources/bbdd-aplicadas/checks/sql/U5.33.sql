:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_33';
GO
CREATE TABLE dbo.Reserva (ReservaId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Reserva PRIMARY KEY, Concepto VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_33_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Reserva (Concepto) VALUES ('A');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_33_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Reserva (Concepto) VALUES ('B');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_33_log2.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
GO
DROP TABLE IF EXISTS #Archivo; CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_33_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX) = N'RESTORE DATABASE [chk_U5_33_rest] FROM DISK = N''/tmp/U5_33_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_33_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_33_rest.ldf'', NORECOVERY;';
EXEC (@Sql);
CREATE TABLE ##Res (Paso VARCHAR(50), Resultado VARCHAR(60));
BEGIN TRY
    EXEC (N'RESTORE LOG [chk_U5_33_rest] FROM DISK = N''/tmp/U5_33_log2.trn'' WITH NORECOVERY;');
    INSERT ##Res VALUES ('Restaurar log2 sin log1', 'sin error');
END TRY
BEGIN CATCH
    INSERT ##Res VALUES ('Restaurar log2 sin log1', 'rechazada');
END CATCH;
EXEC (N'RESTORE LOG [chk_U5_33_rest] FROM DISK = N''/tmp/U5_33_log1.trn'' WITH NORECOVERY;');
EXEC (N'RESTORE LOG [chk_U5_33_rest] FROM DISK = N''/tmp/U5_33_log2.trn'' WITH RECOVERY;');
INSERT ##Res VALUES ('Orden correcto log1, log2', 'sin error');
GO
:out stdout
SELECT Paso, Resultado FROM ##Res ORDER BY Paso;
SELECT COUNT(*) AS FilasRecuperadas FROM [chk_U5_33_rest].dbo.Reserva;
GO
:out /dev/null
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_33_rest]');
END TRY
BEGIN CATCH
END CATCH;
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_33_rest2]');
END TRY
BEGIN CATCH
END CATCH;
GO
