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
-- Ejercicio U5.08: encadenamiento de propiedad roto por un esquema con otro propietario.
CREATE USER usr_ana WITHOUT LOGIN;
CREATE USER usr_tesoreria WITHOUT LOGIN;
GO
CREATE SCHEMA ventas AUTHORIZATION dbo;
GO
CREATE SCHEMA tesoreria AUTHORIZATION usr_tesoreria;
GO
CREATE TABLE tesoreria.Caja (CajaId INT PRIMARY KEY, Saldo DECIMAL(12, 2) NOT NULL);
INSERT tesoreria.Caja VALUES (1, 1000.00), (2, 2500.00);
GO
CREATE VIEW ventas.CajaResumen AS SELECT COUNT(*) AS Cajas, SUM(Saldo) AS Total FROM tesoreria.Caja;
GO
GRANT SELECT ON OBJECT::ventas.CajaResumen TO usr_ana;
GO
EXEC dbo.Intentar 'usr_ana', '1 vista con propietarios distintos', N'SELECT * FROM ventas.CajaResumen';
SELECT s.name AS Esquema, USER_NAME(s.principal_id) AS Propietario FROM sys.schemas AS s WHERE s.name IN ('ventas', 'tesoreria') ORDER BY s.name;
ALTER AUTHORIZATION ON SCHEMA::tesoreria TO dbo;
EXEC dbo.Intentar 'usr_ana', '2 vista tras ALTER AUTHORIZATION', N'SELECT * FROM ventas.CajaResumen';
EXEC dbo.Intentar 'usr_ana', '3 tabla directa', N'SELECT * FROM tesoreria.Caja';
GO
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
SELECT * FROM ventas.CajaResumen;
