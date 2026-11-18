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
-- Ejercicio U5.07: delegación en dos niveles y REVOKE ... CASCADE.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, Importe DECIMAL(10, 2) NOT NULL);
INSERT ventas.Pedido VALUES (1, 100.00);
CREATE USER usr_gerente WITHOUT LOGIN;
CREATE USER usr_jefe WITHOUT LOGIN;
CREATE USER usr_analista WITHOUT LOGIN;
GO
GRANT SELECT ON OBJECT::ventas.Pedido TO usr_gerente WITH GRANT OPTION;
EXEC dbo.Intentar 'usr_gerente', '1 gerente delega a jefe con GRANT OPTION', N'GRANT SELECT ON OBJECT::ventas.Pedido TO usr_jefe WITH GRANT OPTION', 2;
EXEC dbo.Intentar 'usr_jefe', '2 jefe delega a analista', N'GRANT SELECT ON OBJECT::ventas.Pedido TO usr_analista', 2;
EXEC dbo.Intentar 'usr_analista', '3 analista lee Pedido', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Ejecutar '4 REVOKE GRANT OPTION FOR sin CASCADE', N'REVOKE GRANT OPTION FOR SELECT ON OBJECT::ventas.Pedido FROM usr_gerente';
EXEC dbo.Ejecutar '5 REVOKE GRANT OPTION FOR con CASCADE', N'REVOKE GRANT OPTION FOR SELECT ON OBJECT::ventas.Pedido FROM usr_gerente CASCADE';
EXEC dbo.Intentar 'usr_gerente', '6 gerente lee Pedido', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Intentar 'usr_jefe', '7 jefe lee Pedido', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Intentar 'usr_analista', '8 analista lee Pedido', N'SELECT * FROM ventas.Pedido';
GO
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
