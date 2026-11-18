:out /dev/null
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'chk_U5_T_BK_11';
GO
CREATE TABLE dbo.Pedido (PedidoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY, Estado VARCHAR(20) NOT NULL);
GO
ALTER DATABASE CURRENT SET RECOVERY FULL;
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_BK_11_full.bak'' WITH INIT, CHECKSUM;';
EXEC (@Sql);
GO
DROP TABLE IF EXISTS #Archivo; CREATE TABLE #Archivo (LogicalName NVARCHAR(128), PhysicalName NVARCHAR(260), Type CHAR(1), FileGroupName NVARCHAR(128), Size NUMERIC(20,0), MaxSize NUMERIC(20,0), FileId BIGINT, CreateLSN NUMERIC(25,0), DropLSN NUMERIC(25,0), UniqueId UNIQUEIDENTIFIER, ReadOnlyLSN NUMERIC(25,0), ReadWriteLSN NUMERIC(25,0), BackupSizeInBytes BIGINT, SourceBlockSize INT, FileGroupId INT, LogGroupGUID UNIQUEIDENTIFIER, DifferentialBaseLSN NUMERIC(25,0), DifferentialBaseGUID UNIQUEIDENTIFIER, IsReadOnly BIT, IsPresent BIT, TDEThumbprint VARBINARY(32), SnapshotUrl NVARCHAR(360));
INSERT #Archivo EXEC (N'RESTORE FILELISTONLY FROM DISK = N''/tmp/U5_T_BK_11_full.bak''');
DECLARE @Datos SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'D');
DECLARE @Registro SYSNAME = (SELECT LogicalName FROM #Archivo WHERE Type = 'L');
DECLARE @Sql NVARCHAR(MAX) = N'RESTORE DATABASE [chk_U5_T_BK_11_rest] FROM DISK = N''/tmp/U5_T_BK_11_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_11_rest.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_11_rest.ldf'', RECOVERY;';
EXEC (@Sql);
CREATE TABLE ##Res (Intento VARCHAR(60), Resultado VARCHAR(60));
-- otra base con el mismo nombre ya existe: la restauración sin REPLACE no debe pisarla
EXEC (N'CREATE DATABASE [chk_U5_T_BK_11_rest2]');
BEGIN TRY
    EXEC (N'RESTORE DATABASE [chk_U5_T_BK_11_rest2] FROM DISK = N''/tmp/U5_T_BK_11_full.bak'' WITH MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_11_rest2.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_11_rest2.ldf'';');
    INSERT ##Res VALUES ('Sin REPLACE sobre otra base', 'sin error');
END TRY
BEGIN CATCH
    INSERT ##Res VALUES ('Sin REPLACE sobre otra base', 'rechazada');
END CATCH;
BEGIN TRY
    EXEC (N'RESTORE DATABASE [chk_U5_T_BK_11_rest2] FROM DISK = N''/tmp/U5_T_BK_11_full.bak'' WITH REPLACE, MOVE N''' + @Datos + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_11_rest2.mdf'', MOVE N''' + @Registro + N''' TO N''/var/opt/mssql/data/chk_U5_T_BK_11_rest2.ldf'';');
    INSERT ##Res VALUES ('Con REPLACE sobre otra base', 'sin error');
END TRY
BEGIN CATCH
    INSERT ##Res VALUES ('Con REPLACE sobre otra base', 'rechazada');
END CATCH;
GO
:out stdout
SELECT Intento, Resultado FROM ##Res ORDER BY Intento;
GO
:out /dev/null
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_11_rest]');
END TRY
BEGIN CATCH
END CATCH;
BEGIN TRY
    EXEC (N'DROP DATABASE [chk_U5_T_BK_11_rest2]');
END TRY
BEGIN CATCH
END CATCH;
GO
