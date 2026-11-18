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
-- Ejercicio U5.05: secuencia de GRANT, DENY y REVOKE sobre un rol y dos usuarios.
CREATE SCHEMA ventas;
GO
CREATE SCHEMA compras;
GO
CREATE TABLE ventas.Cliente (ClienteId INT PRIMARY KEY, Nombre VARCHAR(50) NOT NULL);
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, ClienteId INT NOT NULL, Estado VARCHAR(20) NOT NULL);
CREATE TABLE compras.Proveedor (ProveedorId INT PRIMARY KEY, Nombre VARCHAR(50) NOT NULL);
INSERT ventas.Cliente VALUES (1, 'cliente01');
INSERT ventas.Pedido VALUES (1, 1, 'NUEVO');
INSERT compras.Proveedor VALUES (1, 'proveedor01');
CREATE ROLE rol_comercial;
CREATE USER usr_ana WITHOUT LOGIN;
CREATE USER usr_beto WITHOUT LOGIN;
CREATE USER usr_carla WITHOUT LOGIN;
ALTER ROLE rol_comercial ADD MEMBER usr_ana;
ALTER ROLE rol_comercial ADD MEMBER usr_beto;
GO
GRANT SELECT ON SCHEMA::ventas TO rol_comercial;
GRANT INSERT ON OBJECT::ventas.Pedido TO rol_comercial;
DENY SELECT ON OBJECT::ventas.Cliente TO usr_beto;
GRANT SELECT ON OBJECT::compras.Proveedor TO rol_comercial;
DENY SELECT ON OBJECT::compras.Proveedor TO usr_ana;
GRANT UPDATE ON OBJECT::ventas.Pedido TO usr_beto;
REVOKE SELECT ON SCHEMA::ventas FROM rol_comercial;
GRANT SELECT ON OBJECT::ventas.Pedido TO usr_ana;
GO
CREATE TABLE dbo.Tabla (Orden INT IDENTITY(1, 1), Consulta VARCHAR(60), Ana VARCHAR(20), Beto VARCHAR(20), Carla VARCHAR(20));
GO
CREATE PROCEDURE dbo.Fila @Consulta VARCHAR(60), @Sql NVARCHAR(MAX), @Modo TINYINT
AS
BEGIN
    DELETE dbo.Resultado;
    EXEC dbo.Intentar 'usr_ana', 'a', @Sql, @Modo;
    EXEC dbo.Intentar 'usr_beto', 'b', @Sql, @Modo;
    EXEC dbo.Intentar 'usr_carla', 'c', @Sql, @Modo;
    INSERT dbo.Tabla (Consulta, Ana, Beto, Carla)
    SELECT @Consulta,
           MAX(CASE WHEN Paso = 'a' THEN LEFT(Resultado, 2) ELSE '' END),
           MAX(CASE WHEN Paso = 'b' THEN LEFT(Resultado, 2) ELSE '' END),
           MAX(CASE WHEN Paso = 'c' THEN LEFT(Resultado, 2) ELSE '' END)
    FROM dbo.Resultado;
END;
GO
EXEC dbo.Fila '1 SELECT * FROM ventas.Cliente', N'SELECT * FROM ventas.Cliente', 1;
EXEC dbo.Fila '2 SELECT * FROM ventas.Pedido', N'SELECT * FROM ventas.Pedido', 1;
EXEC dbo.Fila '3 INSERT en ventas.Pedido', N'INSERT ventas.Pedido (PedidoId, ClienteId, Estado) VALUES (9, 1, ''NUEVO'')', 0;
EXEC dbo.Fila '4 UPDATE ventas.Pedido SET Estado', N'UPDATE ventas.Pedido SET Estado = ''ENVIADO''', 0;
EXEC dbo.Fila '5 SELECT * FROM compras.Proveedor', N'SELECT * FROM compras.Proveedor', 1;
GO
SELECT Consulta, Ana, Beto, Carla FROM dbo.Tabla ORDER BY Orden;
