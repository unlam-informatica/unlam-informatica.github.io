:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_26';
GO
CREATE TABLE dbo.Reserva (ReservaId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Reserva PRIMARY KEY, Concepto VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_26_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Reserva (Concepto) VALUES ('R1_EN_LOG');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_26_log1.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Reserva (Concepto) VALUES ('R2_EN_DIFF');
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_26_diff.bak'' WITH DIFFERENTIAL, INIT, CHECKSUM;';
EXEC (@Sql);
INSERT dbo.Reserva (Concepto) VALUES ('R3_EN_LOG2');
SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_26_log2.trn'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
GO
CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_26_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'RESTORE DATABASE [chk_U5_26_rest] FROM DISK = N''/tmp/U5_26_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_26_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_26_rest.ldf'', NORECOVERY;';
EXEC (@Sql);
EXEC (N'RESTORE DATABASE [chk_U5_26_rest] FROM DISK = N''/tmp/U5_26_diff.bak'' WITH NORECOVERY;');
EXEC (N'RESTORE LOG [chk_U5_26_rest] FROM DISK = N''/tmp/U5_26_log2.trn'' WITH RECOVERY;');
GO
:out stdout
SELECT p.ReservaId, p.Concepto FROM [chk_U5_26_rest].dbo.Reserva AS p ORDER BY p.ReservaId;
GO
:out /dev/null
BEGIN TRY
    IF DB_ID(N'chk_U5_26_rest') IS NOT NULL
    BEGIN
        EXEC (N'DROP DATABASE [chk_U5_26_rest]');
    END;
END TRY
BEGIN CATCH
END CATCH;
GO
