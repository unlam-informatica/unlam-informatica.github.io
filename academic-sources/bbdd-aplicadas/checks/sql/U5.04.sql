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
-- Ejercicio U5.04: permisos de columna.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Cliente
(
    ClienteId    INT IDENTITY PRIMARY KEY,
    Nombre       NVARCHAR(100)  NOT NULL,
    Email        VARCHAR(256)   NULL,
    LimiteCuenta DECIMAL(18, 2) NOT NULL
);
INSERT ventas.Cliente (Nombre, Email, LimiteCuenta)
VALUES (N'Cliente 01', 'cliente01@ejemplo.test', 10000), (N'Cliente 02', 'cliente02@ejemplo.test', 8000);
CREATE USER usr_soporte WITHOUT LOGIN;
GO
GRANT SELECT (ClienteId, Nombre, Email) ON OBJECT::ventas.Cliente TO usr_soporte;
GO
EXEC dbo.Intentar 'usr_soporte', '1 columnas permitidas', N'SELECT ClienteId, Nombre, Email FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_soporte', '2 SELECT *', N'SELECT * FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_soporte', '3 columna LimiteCuenta', N'SELECT LimiteCuenta FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_soporte', '4 COUNT(*) sin columnas', N'SELECT COUNT(*) AS Filas FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_soporte', '5 filtrar por LimiteCuenta', N'SELECT Nombre FROM ventas.Cliente WHERE LimiteCuenta > 9000';
GO
DENY SELECT (Email) ON OBJECT::ventas.Cliente TO usr_soporte;
GO
EXEC dbo.Intentar 'usr_soporte', '6 Email tras DENY de columna', N'SELECT Email FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_soporte', '7 Nombre tras DENY de Email', N'SELECT Nombre FROM ventas.Cliente';
GO
EXECUTE AS USER = 'usr_soporte';
SELECT subentity_name AS Columna, permission_name
FROM fn_my_permissions('ventas.Cliente', 'OBJECT')
WHERE subentity_name <> ''
ORDER BY subentity_name;
REVERT;
GO
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
