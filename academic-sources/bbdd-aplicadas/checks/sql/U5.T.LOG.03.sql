:out /dev/null
CREATE TABLE ##Res (Orden INT, Situacion VARCHAR(70), Resultado VARCHAR(40));
GO
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql NVARCHAR(MAX);
ALTER DATABASE CURRENT SET RECOVERY SIMPLE;
BEGIN TRY
    SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_LOG_03_a.trn'' WITH INIT;';
    EXEC (@Sql);
    INSERT ##Res VALUES (1, 'BACKUP LOG en SIMPLE', 'permitido');
END TRY
BEGIN CATCH
    INSERT ##Res VALUES (1, 'BACKUP LOG en SIMPLE', 'rechazado');
END CATCH;
ALTER DATABASE CURRENT SET RECOVERY FULL;
BEGIN TRY
    SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_LOG_03_b.trn'' WITH INIT;';
    EXEC (@Sql);
    INSERT ##Res VALUES (2, 'BACKUP LOG en FULL sin backup completo previo', 'permitido');
END TRY
BEGIN CATCH
    INSERT ##Res VALUES (2, 'BACKUP LOG en FULL sin backup completo previo', 'rechazado');
END CATCH;
SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_LOG_03_full.bak'' WITH INIT;';
EXEC (@Sql);
BEGIN TRY
    SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/tmp/U5_T_LOG_03_c.trn'' WITH INIT;';
    EXEC (@Sql);
    INSERT ##Res VALUES (3, 'BACKUP LOG en FULL con backup completo previo', 'permitido');
END TRY
BEGIN CATCH
    INSERT ##Res VALUES (3, 'BACKUP LOG en FULL con backup completo previo', 'rechazado');
END CATCH;
ALTER DATABASE CURRENT SET RECOVERY BULK_LOGGED;
INSERT ##Res SELECT 4, 'Modelo tras ALTER DATABASE ... BULK_LOGGED', recovery_model_desc FROM sys.databases WHERE database_id = DB_ID();
GO
:out stdout
SELECT Situacion, Resultado FROM ##Res ORDER BY Orden;
