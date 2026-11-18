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
-- Laboratorio de seguridad: preparación y partes 1 a 7 (la base LaboratorioU5 se reemplaza por la base del verificador).
CREATE SCHEMA ventas AUTHORIZATION dbo;
GO
CREATE SCHEMA operaciones AUTHORIZATION dbo;
GO
CREATE TABLE ventas.Cliente
(
    ClienteId    INT IDENTITY PRIMARY KEY,
    Nombre       NVARCHAR(100) NOT NULL,
    Email        VARCHAR(256)  NULL,
    LimiteCuenta DECIMAL(18, 2) NOT NULL,
    Pais         CHAR(3)       NOT NULL,
    Activo       BIT           NOT NULL DEFAULT 1
);
CREATE TABLE ventas.Pedido
(
    PedidoId  INT IDENTITY PRIMARY KEY,
    ClienteId INT NOT NULL REFERENCES ventas.Cliente (ClienteId),
    Fecha     DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    Importe   DECIMAL(18, 2) NOT NULL CHECK (Importe > 0),
    Estado    VARCHAR(20) NOT NULL DEFAULT 'NUEVO'
);
INSERT ventas.Cliente (Nombre, Email, LimiteCuenta, Pais)
VALUES (N'Cliente 01', 'cliente01@ejemplo.test', 10000, 'ARG'),
       (N'Cliente 02', 'cliente02@ejemplo.test', 8000, 'ARG'),
       (N'Cliente 03', 'cliente03@ejemplo.test', 6000, 'USA');
INSERT ventas.Pedido (ClienteId, Importe) VALUES (1, 500), (2, 750);
GO
CREATE LOGIN login_vendedor_u5 WITH PASSWORD = 'Cambiar_Vendedor_U5_2026!', CHECK_POLICY = ON;
CREATE LOGIN login_auditor_u5 WITH PASSWORD = 'Cambiar_Auditor_U5_2026!', CHECK_POLICY = ON;
CREATE LOGIN login_supervisor_u5 WITH PASSWORD = 'Cambiar_Supervisor_U5_2026!', CHECK_POLICY = ON;
GO
CREATE USER usr_vendedor FOR LOGIN login_vendedor_u5 WITH DEFAULT_SCHEMA = ventas;
CREATE USER usr_auditor FOR LOGIN login_auditor_u5;
CREATE USER usr_supervisor FOR LOGIN login_supervisor_u5;
CREATE USER usr_practicante WITHOUT LOGIN;
GO
-- Parte 1
SELECT name, type_desc
FROM sys.server_principals
WHERE name IN ('login_vendedor_u5', 'login_auditor_u5', 'login_supervisor_u5')
ORDER BY name;
SELECT name, type_desc, default_schema_name
FROM sys.database_principals
WHERE name IN ('usr_vendedor', 'usr_auditor', 'usr_supervisor', 'usr_practicante')
ORDER BY name;
EXEC dbo.Intentar 'usr_auditor', 'P1 auditor lee Cliente', N'SELECT * FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_vendedor', 'P1 vendedor lee Cliente', N'SELECT * FROM ventas.Cliente';
GO
-- Parte 2
CREATE ROLE rol_vendedores AUTHORIZATION dbo;
CREATE ROLE rol_auditores AUTHORIZATION dbo;
CREATE ROLE rol_supervisores AUTHORIZATION dbo;
ALTER ROLE rol_vendedores ADD MEMBER usr_vendedor;
ALTER ROLE rol_auditores ADD MEMBER usr_auditor;
ALTER ROLE rol_supervisores ADD MEMBER usr_supervisor;
GRANT SELECT ON OBJECT::ventas.Pedido TO rol_auditores;
GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::ventas TO rol_supervisores;
GO
EXEC dbo.Intentar 'usr_auditor', 'P2 auditor lee Pedido', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Intentar 'usr_auditor', 'P2 auditor lee Cliente', N'SELECT * FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_auditor', 'P2 auditor borra Pedido', N'DELETE ventas.Pedido', 0;
EXEC dbo.Intentar 'usr_supervisor', 'P2 supervisor lee Cliente', N'SELECT * FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_supervisor', 'P2 supervisor borra Pedido', N'DELETE ventas.Pedido', 0;
GO
EXECUTE AS USER = 'usr_auditor';
SELECT entity_name, permission_name FROM fn_my_permissions('ventas.Pedido', 'OBJECT') WHERE subentity_name = '' ORDER BY permission_name;
REVERT;
GO
-- Parte 3
CREATE OR ALTER VIEW ventas.ClientesVisibles
AS
SELECT ClienteId, Nombre, Email, Pais
FROM ventas.Cliente
WHERE Activo = 1 AND Pais <> 'USA';
GO
GRANT SELECT ON OBJECT::ventas.ClientesVisibles TO rol_vendedores;
GO
EXEC dbo.Intentar 'usr_vendedor', 'P3 vendedor lee ClientesVisibles', N'SELECT * FROM ventas.ClientesVisibles';
EXEC dbo.Intentar 'usr_vendedor', 'P3 vendedor lee Cliente', N'SELECT * FROM ventas.Cliente';
GO
-- Parte 4
CREATE OR ALTER PROCEDURE operaciones.RegistrarPedido
    @ClienteId INT,
    @Importe   DECIMAL(18, 2)
AS
BEGIN
    SET NOCOUNT ON;

    IF @Importe <= 0
        THROW 50001, 'El importe debe ser positivo.', 1;

    INSERT ventas.Pedido (ClienteId, Importe)
    VALUES (@ClienteId, @Importe);

    SELECT SCOPE_IDENTITY() AS PedidoId;
END;
GO
GRANT EXECUTE ON OBJECT::operaciones.RegistrarPedido TO rol_vendedores;
GO
EXEC dbo.Intentar 'usr_vendedor', 'P4 vendedor registra un pedido', N'EXEC operaciones.RegistrarPedido @ClienteId = 1, @Importe = 1250', 0;
EXEC dbo.Intentar 'usr_vendedor', 'P4 vendedor inserta directo', N'INSERT ventas.Pedido (ClienteId, Importe) VALUES (1, 999)', 0;
EXEC dbo.Intentar 'usr_vendedor', 'P4 importe negativo', N'EXEC operaciones.RegistrarPedido @ClienteId = 1, @Importe = -5', 0;
GO
-- Parte 5 (corregida: se revierte el permiso de esquema)
GRANT SELECT ON OBJECT::ventas.Cliente TO rol_auditores;
GRANT SELECT ON SCHEMA::ventas TO usr_auditor;
REVOKE SELECT ON OBJECT::ventas.Cliente FROM rol_auditores;
EXEC dbo.Intentar 'usr_auditor', 'P5 a REVOKE del rol, queda el permiso de esquema', N'SELECT * FROM ventas.Cliente';
DENY SELECT ON OBJECT::ventas.Cliente TO usr_auditor;
EXEC dbo.Intentar 'usr_auditor', 'P5 b DENY sobre la tabla', N'SELECT * FROM ventas.Cliente';
REVOKE SELECT ON OBJECT::ventas.Cliente FROM usr_auditor;
EXEC dbo.Intentar 'usr_auditor', 'P5 c REVOKE del DENY, sigue el esquema', N'SELECT * FROM ventas.Cliente';
REVOKE SELECT ON SCHEMA::ventas FROM usr_auditor;
EXEC dbo.Intentar 'usr_auditor', 'P5 d REVOKE del esquema: Cliente', N'SELECT * FROM ventas.Cliente';
EXEC dbo.Intentar 'usr_auditor', 'P5 d REVOKE del esquema: Pedido', N'SELECT * FROM ventas.Pedido';
GO
-- Parte 6
SELECT rol.name AS Rol, miembro.name AS Miembro
FROM sys.database_role_members AS drm
JOIN sys.database_principals AS rol ON rol.principal_id = drm.role_principal_id
JOIN sys.database_principals AS miembro ON miembro.principal_id = drm.member_principal_id
WHERE rol.name LIKE 'rol[_]%'
ORDER BY rol.name, miembro.name;
SELECT p.state_desc, p.permission_name, p.class_desc,
       USER_NAME(p.grantee_principal_id) AS principal,
       CASE p.class_desc
         WHEN 'DATABASE' THEN DB_NAME()
         WHEN 'SCHEMA' THEN SCHEMA_NAME(p.major_id)
         WHEN 'OBJECT_OR_COLUMN' THEN QUOTENAME(OBJECT_SCHEMA_NAME(p.major_id)) + '.' + QUOTENAME(OBJECT_NAME(p.major_id))
       END AS securable
FROM sys.database_permissions AS p
WHERE USER_NAME(p.grantee_principal_id) LIKE 'rol[_]%'
ORDER BY principal, p.class_desc, securable, p.permission_name;
SELECT s.name AS esquema, USER_NAME(s.principal_id) AS propietario
FROM sys.schemas AS s
WHERE s.name IN ('ventas', 'operaciones')
ORDER BY s.name;
GO
-- Parte 7
GRANT SELECT ON OBJECT::ventas.Pedido TO usr_supervisor WITH GRANT OPTION;
EXEC dbo.Intentar 'usr_supervisor', 'P7 supervisor delega en el practicante', N'GRANT SELECT ON OBJECT::ventas.Pedido TO usr_practicante', 2;
EXEC dbo.Intentar 'usr_practicante', 'P7 practicante lee Pedido', N'SELECT * FROM ventas.Pedido';
EXEC dbo.Ejecutar 'P7 REVOKE sin CASCADE', N'REVOKE SELECT ON OBJECT::ventas.Pedido FROM usr_supervisor';
EXEC dbo.Ejecutar 'P7 REVOKE con CASCADE', N'REVOKE SELECT ON OBJECT::ventas.Pedido FROM usr_supervisor CASCADE';
EXEC dbo.Intentar 'usr_practicante', 'P7 practicante lee Pedido tras CASCADE', N'SELECT * FROM ventas.Pedido';
GO
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
GO
-- Limpieza de logins (objetos de servidor)
BEGIN TRY
    DROP LOGIN login_vendedor_u5;
    DROP LOGIN login_auditor_u5;
    DROP LOGIN login_supervisor_u5;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorLimpieza;
END CATCH;
SELECT COUNT(*) AS LoginsRestantes FROM sys.server_principals WHERE name LIKE 'login[_]%[_]u5';
