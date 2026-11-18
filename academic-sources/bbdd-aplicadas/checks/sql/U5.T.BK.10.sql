:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_10';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_10_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
GO
CREATE TABLE #H (BackupName NVARCHAR(128), BackupDescription NVARCHAR(255), BackupType SMALLINT, ExpirationDate DATETIME, Compressed BIT, Position SMALLINT, DeviceType TINYINT, UserName NVARCHAR(128), ServerName NVARCHAR(128), DatabaseName NVARCHAR(128), DatabaseVersion INT, DatabaseCreationDate DATETIME, BackupSize NUMERIC(20,0), FirstLSN NUMERIC(25,0), LastLSN NUMERIC(25,0), CheckpointLSN NUMERIC(25,0), DatabaseBackupLSN NUMERIC(25,0), BackupStartDate DATETIME, BackupFinishDate DATETIME, SortOrder SMALLINT, CodePage SMALLINT, UnicodeLocaleId INT, UnicodeComparisonStyle INT, CompatibilityLevel TINYINT, SoftwareVendorId INT, SoftwareVersionMajor INT, SoftwareVersionMinor INT, SoftwareVersionBuild INT, MachineName NVARCHAR(128), Flags INT, BindingID UNIQUEIDENTIFIER, RecoveryForkID UNIQUEIDENTIFIER, Collation NVARCHAR(128), FamilyGUID UNIQUEIDENTIFIER, HasBulkLoggedData BIT, IsSnapshot BIT, IsReadOnly BIT, IsSingleUser BIT, HasBackupChecksums BIT, IsDamaged BIT, BeginsLogChain BIT, HasIncompleteMetaData BIT, IsForceOffline BIT, IsCopyOnly BIT, FirstRecoveryForkID UNIQUEIDENTIFIER, ForkPointLSN NUMERIC(25,0), RecoveryModel NVARCHAR(60), DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, BackupTypeDescription NVARCHAR(60), BackupSetGUID UNIQUEIDENTIFIER, CompressedBackupSize BIGINT, containment TINYINT, KeyAlgorithm NVARCHAR(32), EncryptorThumbprint VARBINARY(32), EncryptorType NVARCHAR(32), LastValidRestoreTime DATETIME, TimeZone INT, CompressionAlgorithm NVARCHAR(32));
INSERT #H EXEC (N'RESTORE HEADERONLY FROM DISK = N''/tmp/U5_T_BK_10_full.bak''');
DROP TABLE IF EXISTS #Archivo; CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_T_BK_10_full.bak''');
CREATE TABLE ##Res (Concepto VARCHAR(40), Valor VARCHAR(60));
INSERT ##Res SELECT 'HEADERONLY BackupType', CAST(BackupType AS VARCHAR(5)) FROM #H;
INSERT ##Res SELECT 'HEADERONLY RecoveryModel', RecoveryModel FROM #H;
INSERT ##Res SELECT 'HEADERONLY HasBackupChecksums', CAST(HasBackupChecksums AS VARCHAR(5)) FROM #H;
INSERT ##Res SELECT 'FILELISTONLY archivos tipo ' + Type, '1' FROM #Archivo;
BEGIN TRY
    EXEC (N'RESTORE VERIFYONLY FROM DISK = N''/tmp/U5_T_BK_10_full.bak'' WITH CHECKSUM');
    INSERT ##Res VALUES ('VERIFYONLY del archivo', 'valido');
END TRY
BEGIN CATCH
    INSERT ##Res VALUES ('VERIFYONLY del archivo', 'rechazada');
END CATCH;
BEGIN TRY
    EXEC (N'RESTORE VERIFYONLY FROM DISK = N''/tmp/U5_T_BK_10_no_existe.bak''');
    INSERT ##Res VALUES ('VERIFYONLY de un archivo inexistente', 'valido');
END TRY
BEGIN CATCH
    INSERT ##Res VALUES ('VERIFYONLY de un archivo inexistente', 'rechazada');
END CATCH;
GO
:out stdout
SELECT Concepto, Valor FROM ##Res ORDER BY Concepto;
