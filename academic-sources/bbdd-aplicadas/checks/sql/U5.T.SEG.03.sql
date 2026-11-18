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
-- Jerarquía de permisos: seis formas de otorgar SELECT sobre una tabla y su alcance.
CREATE SCHEMA ventas;
GO
CREATE SCHEMA compras;
GO
CREATE TABLE ventas.Cliente (ClienteId INT PRIMARY KEY, Nombre VARCHAR(50) NOT NULL);
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, ClienteId INT NOT NULL, Importe DECIMAL(10, 2) NOT NULL);
CREATE TABLE compras.Proveedor (ProveedorId INT PRIMARY KEY, Nombre VARCHAR(50) NOT NULL);
INSERT ventas.Cliente VALUES (1, 'cliente01'), (2, 'cliente02');
INSERT ventas.Pedido VALUES (1, 1, 100.00), (2, 2, 250.00);
INSERT compras.Proveedor VALUES (1, 'proveedor01');
CREATE USER usr_aza WITHOUT LOGIN;
GO
CREATE PROCEDURE dbo.Alcance @Caso VARCHAR(80)
AS
BEGIN
    DECLARE @C BIT = 0, @P BIT = 0, @V BIT = 0;
    EXECUTE AS USER = 'usr_aza';
    SET @C = HAS_PERMS_BY_NAME('ventas.Cliente', 'OBJECT', 'SELECT');
    SET @P = HAS_PERMS_BY_NAME('ventas.Pedido', 'OBJECT', 'SELECT');
    SET @V = HAS_PERMS_BY_NAME('compras.Proveedor', 'OBJECT', 'SELECT');
    REVERT;
    INSERT dbo.Matriz (Caso, Cliente, Pedido, Proveedor)
    VALUES (@Caso, IIF(@C = 1, 'SI', 'NO'), IIF(@P = 1, 'SI', 'NO'), IIF(@V = 1, 'SI', 'NO'));
END;
GO
CREATE TABLE dbo.Matriz (Orden INT IDENTITY(1, 1), Caso VARCHAR(80), Cliente CHAR(2), Pedido CHAR(2), Proveedor CHAR(2));
GO
EXEC dbo.Alcance 'sin permisos';
GRANT SELECT ON OBJECT::ventas.Cliente TO usr_aza;
EXEC dbo.Alcance 'SELECT sobre ventas.Cliente';
REVOKE SELECT ON OBJECT::ventas.Cliente FROM usr_aza;
GRANT CONTROL ON OBJECT::ventas.Cliente TO usr_aza;
EXEC dbo.Alcance 'CONTROL sobre ventas.Cliente';
REVOKE CONTROL ON OBJECT::ventas.Cliente FROM usr_aza;
GRANT SELECT ON SCHEMA::ventas TO usr_aza;
EXEC dbo.Alcance 'SELECT sobre el esquema ventas';
REVOKE SELECT ON SCHEMA::ventas FROM usr_aza;
GRANT CONTROL ON SCHEMA::ventas TO usr_aza;
EXEC dbo.Alcance 'CONTROL sobre el esquema ventas';
REVOKE CONTROL ON SCHEMA::ventas FROM usr_aza;
GRANT SELECT ON DATABASE::chk_U5_T_SEG_03 TO usr_aza;
EXEC dbo.Alcance 'SELECT sobre la base';
REVOKE SELECT ON DATABASE::chk_U5_T_SEG_03 FROM usr_aza;
GRANT CONTROL ON DATABASE::chk_U5_T_SEG_03 TO usr_aza;
EXEC dbo.Alcance 'CONTROL sobre la base';
GO
SELECT Caso, Cliente, Pedido, Proveedor FROM dbo.Matriz ORDER BY Orden;
