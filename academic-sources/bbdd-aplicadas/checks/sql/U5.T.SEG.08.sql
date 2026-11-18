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
-- Propietarios, encadenamiento de propiedad y ALTER AUTHORIZATION.
CREATE USER usr_ana WITHOUT LOGIN;
CREATE USER usr_fin WITHOUT LOGIN;
GO
CREATE SCHEMA ventas AUTHORIZATION dbo;
GO
CREATE SCHEMA finanzas AUTHORIZATION usr_fin;
GO
CREATE TABLE finanzas.Cuenta (CuentaId INT PRIMARY KEY, Saldo DECIMAL(12, 2) NOT NULL);
INSERT finanzas.Cuenta VALUES (1, 500.00), (2, 800.00);
GO
CREATE VIEW ventas.CuentaVisible AS SELECT CuentaId FROM finanzas.Cuenta;
GO
CREATE PROCEDURE ventas.ListarCuentaEstatico AS SELECT CuentaId FROM finanzas.Cuenta;
GO
CREATE PROCEDURE ventas.ListarCuentaDinamico AS EXEC (N'SELECT CuentaId FROM finanzas.Cuenta');
GO
GRANT SELECT ON OBJECT::ventas.CuentaVisible TO usr_ana;
GRANT EXECUTE ON OBJECT::ventas.ListarCuentaEstatico TO usr_ana;
GRANT EXECUTE ON OBJECT::ventas.ListarCuentaDinamico TO usr_ana;
GO
SELECT s.name AS Esquema, USER_NAME(s.principal_id) AS Propietario
FROM sys.schemas AS s
WHERE s.name IN ('ventas', 'finanzas')
ORDER BY s.name;
GO
EXEC dbo.Intentar 'usr_ana', '1 vista de dbo sobre tabla de usr_fin', N'SELECT * FROM ventas.CuentaVisible';
EXEC dbo.Intentar 'usr_ana', '2 procedimiento estatico, propietarios distintos', N'EXEC ventas.ListarCuentaEstatico', 0;
EXEC dbo.Ejecutar '3 ALTER AUTHORIZATION del esquema finanzas a dbo', N'ALTER AUTHORIZATION ON SCHEMA::finanzas TO dbo';
EXEC dbo.Intentar 'usr_ana', '4 vista, mismo propietario', N'SELECT * FROM ventas.CuentaVisible';
EXEC dbo.Intentar 'usr_ana', '5 procedimiento estatico, mismo propietario', N'EXEC ventas.ListarCuentaEstatico', 0;
EXEC dbo.Intentar 'usr_ana', '6 procedimiento con SQL dinamico, mismo propietario', N'EXEC ventas.ListarCuentaDinamico', 0;
EXEC dbo.Intentar 'usr_ana', '7 SELECT directo sobre la tabla', N'SELECT * FROM finanzas.Cuenta';
EXEC dbo.Ejecutar '8 ALTER AUTHORIZATION a usr_fin', N'ALTER AUTHORIZATION ON SCHEMA::finanzas TO usr_fin';
EXEC dbo.Ejecutar '9 DROP USER del propietario de un esquema', N'DROP USER usr_fin';
EXEC dbo.Ejecutar '10 DENY SELECT al propietario', N'DENY SELECT ON OBJECT::finanzas.Cuenta TO usr_fin';
EXEC dbo.Intentar 'usr_fin', '11 el propietario lee su tabla con DENY', N'SELECT * FROM finanzas.Cuenta';
GO
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
