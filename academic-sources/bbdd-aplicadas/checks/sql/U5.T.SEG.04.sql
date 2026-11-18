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
-- Ejecuta una consulta (@EsSelect = 1) o una sentencia como el usuario indicado y registra SI/NO.
CREATE PROCEDURE dbo.Intentar @Usuario SYSNAME, @Paso VARCHAR(80), @Sql NVARCHAR(MAX), @EsSelect BIT = 1
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
        ROLLBACK TRANSACTION;
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
-- Precedencia de DENY, REVOKE y permisos heredados de un rol.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Cliente (ClienteId INT PRIMARY KEY, Nombre VARCHAR(50) NOT NULL);
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, ClienteId INT NOT NULL);
INSERT ventas.Cliente VALUES (1, 'cliente01');
INSERT ventas.Pedido VALUES (1, 1);
CREATE ROLE rol_ventas;
CREATE USER usr_ana WITHOUT LOGIN;
ALTER ROLE rol_ventas ADD MEMBER usr_ana;
CREATE USER usr_dueno WITHOUT LOGIN;
ALTER ROLE db_owner ADD MEMBER usr_dueno;
GO
CREATE TABLE dbo.Matriz (Orden INT IDENTITY(1, 1), Paso VARCHAR(90), Cliente CHAR(2), Pedido CHAR(2));
GO
CREATE PROCEDURE dbo.Alcance @Paso VARCHAR(90), @Usuario SYSNAME = 'usr_ana'
AS
BEGIN
    DECLARE @C BIT, @P BIT;
    EXECUTE AS USER = @Usuario;
    SET @C = HAS_PERMS_BY_NAME('ventas.Cliente', 'OBJECT', 'SELECT');
    SET @P = HAS_PERMS_BY_NAME('ventas.Pedido', 'OBJECT', 'SELECT');
    REVERT;
    INSERT dbo.Matriz (Paso, Cliente, Pedido) VALUES (@Paso, IIF(@C = 1, 'SI', 'NO'), IIF(@P = 1, 'SI', 'NO'));
END;
GO
GRANT SELECT ON SCHEMA::ventas TO rol_ventas;
EXEC dbo.Alcance '1 GRANT SELECT esquema ventas al rol';
DENY SELECT ON OBJECT::ventas.Cliente TO rol_ventas;
EXEC dbo.Alcance '2 DENY SELECT ventas.Cliente al rol';
GRANT SELECT ON OBJECT::ventas.Cliente TO usr_ana;
EXEC dbo.Alcance '3 GRANT SELECT ventas.Cliente a ana (el DENY es del rol)';
REVOKE SELECT ON OBJECT::ventas.Cliente FROM rol_ventas;
EXEC dbo.Alcance '4 REVOKE SELECT ventas.Cliente al rol (quita el DENY)';
DENY SELECT ON SCHEMA::ventas TO usr_ana;
EXEC dbo.Alcance '5 DENY SELECT esquema ventas a ana';
REVOKE SELECT ON SCHEMA::ventas FROM usr_ana;
EXEC dbo.Alcance '6 REVOKE SELECT esquema ventas a ana (quita el DENY)';
REVOKE SELECT ON OBJECT::ventas.Cliente FROM usr_ana;
DENY SELECT ON OBJECT::ventas.Cliente TO usr_dueno;
EXEC dbo.Alcance '7 DENY SELECT ventas.Cliente a un miembro de db_owner', 'usr_dueno';
GO
SELECT Paso, Cliente, Pedido FROM dbo.Matriz ORDER BY Orden;
EXEC dbo.Intentar 'usr_dueno', 'SELECT real de usr_dueno', N'SELECT * FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_ana', 'SELECT real de ana a Pedido', N'SELECT * FROM ventas.Pedido';
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
