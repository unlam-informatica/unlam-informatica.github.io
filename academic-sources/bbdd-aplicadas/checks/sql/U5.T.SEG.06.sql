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
-- WITH GRANT OPTION y REVOKE ... CASCADE.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, Importe DECIMAL(10, 2) NOT NULL);
INSERT ventas.Pedido VALUES (1, 100.00);
CREATE USER usr_supervisor WITHOUT LOGIN;
CREATE USER usr_ana WITHOUT LOGIN;
GO
GRANT SELECT ON OBJECT::ventas.Pedido TO usr_supervisor WITH GRANT OPTION;
EXEC dbo.Intentar 'usr_supervisor', '1 supervisor delega SELECT en ana', N'GRANT SELECT ON OBJECT::ventas.Pedido TO usr_ana', 2;
EXEC dbo.Intentar 'usr_ana', '2 ana lee Pedido', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Ejecutar '3 REVOKE sin CASCADE', N'REVOKE SELECT ON OBJECT::ventas.Pedido FROM usr_supervisor';
EXEC dbo.Intentar 'usr_ana', '4 ana lee Pedido tras el error', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Ejecutar '5 REVOKE GRANT OPTION FOR ... CASCADE', N'REVOKE GRANT OPTION FOR SELECT ON OBJECT::ventas.Pedido FROM usr_supervisor CASCADE';
EXEC dbo.Intentar 'usr_ana', '6 ana lee Pedido', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Intentar 'usr_supervisor', '7 supervisor lee Pedido', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Intentar 'usr_supervisor', '8 supervisor delega de nuevo', N'GRANT SELECT ON OBJECT::ventas.Pedido TO usr_ana', 2;
GO
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
