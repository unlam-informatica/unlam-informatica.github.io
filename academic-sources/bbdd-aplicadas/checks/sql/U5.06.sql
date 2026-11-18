-- Auxiliares de comprobación: registran en dbo.Resultado lo que ocurre con cada sentencia.
CREATE TABLE dbo.Resultado (Orden INT IDENTITY(1, 1) PRIMARY KEY, Paso VARCHAR(80) NOT NULL, Resultado VARCHAR(200) NULL);
GO
CREATE PROCEDURE dbo.Ejecutar @Paso VARCHAR(80), @Sql NVARCHAR(MAX)
AS
BEGIN
    BEGIN TRY
        EXEC sys.sp_executesql @Sql;
        INSERT dbo.Resultado (Paso, Resultado) VALUES (@Paso, 'ok');
    END TRY
    BEGIN CATCH
        INSERT dbo.Resultado (Paso, Resultado) VALUES (@Paso, CONCAT('error ', ERROR_NUMBER()));
    END CATCH;
END;
GO
CREATE PROCEDURE dbo.Valor @Paso VARCHAR(80), @Expresion NVARCHAR(MAX)
AS
BEGIN
    DECLARE @V NVARCHAR(200), @Cmd NVARCHAR(MAX) = N'SELECT @V = CAST(' + @Expresion + N' AS NVARCHAR(200));';
    BEGIN TRY
        EXEC sys.sp_executesql @Cmd, N'@V NVARCHAR(200) OUTPUT', @V = @V OUTPUT;
        INSERT dbo.Resultado (Paso, Resultado) VALUES (@Paso, @V);
    END TRY
    BEGIN CATCH
        INSERT dbo.Resultado (Paso, Resultado) VALUES (@Paso, CONCAT('error ', ERROR_NUMBER()));
    END CATCH;
END;
GO
-- Ejecuta como el usuario indicado una consulta (@EsSelect = 1), una sentencia que se deshace (0) o que se conserva (2) y registra SI/NO.
CREATE PROCEDURE dbo.Intentar @Usuario SYSNAME, @Paso VARCHAR(80), @Sql NVARCHAR(MAX), @EsSelect TINYINT = 1
AS
BEGIN
    DECLARE @N INT, @Cmd NVARCHAR(MAX), @Res VARCHAR(80);
    SET @Cmd = CASE WHEN @EsSelect = 1 THEN N'SELECT @N = COUNT(*) FROM (' + @Sql + N') AS q;'
                    ELSE @Sql + N'; SET @N = @@ROWCOUNT;' END;
    BEGIN TRY
        BEGIN TRANSACTION;
        EXECUTE AS USER = @Usuario;
        EXEC sys.sp_executesql @Cmd, N'@N INT OUTPUT', @N = @N OUTPUT;
        REVERT;
        IF @EsSelect = 2 COMMIT TRANSACTION; ELSE ROLLBACK TRANSACTION;
        SET @Res = CONCAT('SI (', @N, ' filas)');
    END TRY
    BEGIN CATCH
        SET @Res = CONCAT('NO (error ', ERROR_NUMBER(), ')');
        REVERT;
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
    END CATCH;
    INSERT dbo.Resultado (Paso, Resultado) VALUES (@Paso, @Res);
END;
GO
-- Ejercicio U5.06: diagnóstico de permisos efectivos con tres roles.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, Importe DECIMAL(10, 2) NOT NULL);
INSERT ventas.Pedido VALUES (1, 100.00);
CREATE ROLE rol_ventas;
CREATE ROLE rol_reportes;
CREATE ROLE rol_externos;
CREATE USER usr_dario WITHOUT LOGIN;
ALTER ROLE rol_ventas ADD MEMBER usr_dario;
ALTER ROLE rol_reportes ADD MEMBER usr_dario;
ALTER ROLE rol_externos ADD MEMBER usr_dario;
GRANT SELECT, INSERT ON OBJECT::ventas.Pedido TO rol_ventas;
GRANT SELECT ON SCHEMA::ventas TO rol_reportes;
DENY INSERT ON OBJECT::ventas.Pedido TO rol_externos;
GRANT UPDATE ON OBJECT::ventas.Pedido TO usr_dario;
GO
EXEC dbo.Intentar 'usr_dario', '1 SELECT', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Intentar 'usr_dario', '2 INSERT', N'INSERT ventas.Pedido (PedidoId, Importe) VALUES (2, 50)', 0;
EXEC dbo.Intentar 'usr_dario', '3 UPDATE', N'UPDATE ventas.Pedido SET Importe = 10', 0;
GO
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
SELECT DISTINCT via.name AS Via, p.state_desc AS Estado, p.permission_name AS Permiso, p.class_desc AS Ambito,
       CASE p.class_desc
         WHEN 'SCHEMA' THEN SCHEMA_NAME(p.major_id)
         ELSE QUOTENAME(OBJECT_SCHEMA_NAME(p.major_id)) + '.' + QUOTENAME(OBJECT_NAME(p.major_id))
       END AS Securable
FROM sys.database_principals AS u
LEFT JOIN sys.database_role_members AS rm ON rm.member_principal_id = u.principal_id
JOIN sys.database_principals AS via ON via.principal_id IN (u.principal_id, rm.role_principal_id)
JOIN sys.database_permissions AS p ON p.grantee_principal_id = via.principal_id
WHERE u.name = 'usr_dario' AND p.class_desc IN ('SCHEMA', 'OBJECT_OR_COLUMN')
ORDER BY via.name, p.permission_name;
