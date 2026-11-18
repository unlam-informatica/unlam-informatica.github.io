-- SIN-PRELUDE
-- Roles fijos de servidor y de base, roles de servidor definidos por el usuario.
SELECT name
FROM sys.server_principals
WHERE type = 'R' AND is_fixed_role = 1 AND name NOT LIKE '##MS[_]%'
ORDER BY name;
SELECT name
FROM sys.server_principals
WHERE type = 'R' AND is_fixed_role = 1 AND name LIKE '##MS[_]%'
ORDER BY name;
SELECT name
FROM sys.database_principals
WHERE type = 'R' AND is_fixed_role = 1
ORDER BY name;
GO
BEGIN TRY
    EXEC (N'CREATE SERVER ROLE RolServidorU5T07');
    EXEC master.sys.sp_executesql N'GRANT VIEW SERVER STATE TO RolServidorU5T07';
    SELECT r.name AS Rol, p.permission_name AS Permiso, p.state_desc AS Estado
    FROM sys.server_principals AS r
    JOIN sys.server_permissions AS p ON p.grantee_principal_id = r.principal_id
    WHERE r.name = 'RolServidorU5T07' AND p.permission_name = 'VIEW SERVER STATE';
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNumero;
END CATCH;
GO
-- Limpieza de objetos de servidor
IF EXISTS (SELECT 1 FROM sys.server_principals WHERE name = 'RolServidorU5T07')
    DROP SERVER ROLE RolServidorU5T07;
SELECT COUNT(*) AS RolesRestantes FROM sys.server_principals WHERE name = 'RolServidorU5T07';
GO
CREATE TABLE dbo.Dato (DatoId INT PRIMARY KEY);
CREATE ROLE rol_lectura;
CREATE ROLE rol_analistas;
CREATE USER usr_ana WITHOUT LOGIN;
CREATE USER usr_lector WITHOUT LOGIN;
ALTER ROLE rol_lectura ADD MEMBER rol_analistas;
ALTER ROLE rol_analistas ADD MEMBER usr_ana;
GRANT SELECT ON OBJECT::dbo.Dato TO rol_lectura;
ALTER ROLE db_datareader ADD MEMBER usr_lector;
GO
CREATE TABLE dbo.Matriz (Orden INT IDENTITY(1, 1), Caso VARCHAR(80), PuedeLeerDato CHAR(2));
GO
CREATE PROCEDURE dbo.Alcance @Caso VARCHAR(80), @Usuario SYSNAME
AS
BEGIN
    DECLARE @P BIT;
    EXECUTE AS USER = @Usuario;
    SET @P = HAS_PERMS_BY_NAME('dbo.Dato', 'OBJECT', 'SELECT');
    REVERT;
    INSERT dbo.Matriz (Caso, PuedeLeerDato) VALUES (@Caso, IIF(@P = 1, 'SI', 'NO'));
END;
GO
EXEC dbo.Alcance 'usr_ana hereda de rol_lectura por rol_analistas', 'usr_ana';
EXEC dbo.Alcance 'usr_lector en db_datareader', 'usr_lector';
ALTER ROLE db_denydatareader ADD MEMBER usr_lector;
EXEC dbo.Alcance 'usr_lector tambien en db_denydatareader', 'usr_lector';
GO
SELECT Caso, PuedeLeerDato FROM dbo.Matriz ORDER BY Orden;
