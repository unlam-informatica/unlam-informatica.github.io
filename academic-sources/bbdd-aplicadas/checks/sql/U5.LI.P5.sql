-- Laboratorio defensivo de inyección (u5), Parte 5: mínimo privilegio con SQL estático y dinámico.
-- Comprueba qué puede ejecutar un usuario que solo tiene EXECUTE sobre los procedimientos.
CREATE SCHEMA seguridad AUTHORIZATION dbo;
GO
CREATE TABLE seguridad.UsuarioDemo
(
    UsuarioId INT IDENTITY PRIMARY KEY,
    Nombre    NVARCHAR(100) NOT NULL UNIQUE,
    Rol       VARCHAR(20)   NOT NULL
);
INSERT seguridad.UsuarioDemo (Nombre, Rol)
VALUES (N'leia', 'usuario'), (N'luke', 'usuario'), (N'palpatine', 'admin');
GO
CREATE PROCEDURE seguridad.BuscarSeguro
    @Nombre NVARCHAR(100)
AS
BEGIN
    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT UsuarioId, Nombre, Rol FROM seguridad.UsuarioDemo WHERE Nombre = @PNombre;';
    EXEC sys.sp_executesql @stmt = @Sql, @params = N'@PNombre NVARCHAR(100)', @PNombre = @Nombre;
END;
GO
CREATE PROCEDURE seguridad.BuscarEstatico
    @Nombre NVARCHAR(100)
AS
BEGIN
    SELECT UsuarioId, Nombre, Rol FROM seguridad.UsuarioDemo WHERE Nombre = @Nombre;
END;
GO
CREATE ROLE rol_consulta_usuario AUTHORIZATION dbo;
GRANT EXECUTE ON OBJECT::seguridad.BuscarSeguro TO rol_consulta_usuario;
GRANT EXECUTE ON OBJECT::seguridad.BuscarEstatico TO rol_consulta_usuario;
CREATE USER app_demo WITHOUT LOGIN;
ALTER ROLE rol_consulta_usuario ADD MEMBER app_demo;
GO
CREATE TABLE dbo.Resultado (Orden INT IDENTITY, Escenario VARCHAR(30), Caso VARCHAR(20), Salida VARCHAR(40));
GRANT INSERT ON dbo.Resultado TO app_demo;
GO
-- Prueba los tres accesos como app_demo y registra filas devueltas o número de error.
CREATE PROCEDURE dbo.Probar
    @Escenario VARCHAR(30)
AS
BEGIN
    DECLARE @Filas TABLE (UsuarioId INT, Nombre NVARCHAR(100), Rol VARCHAR(20));
    DECLARE @N INT;
    EXECUTE AS USER = 'app_demo';
    BEGIN TRY
        INSERT @Filas EXEC seguridad.BuscarEstatico @Nombre = N'leia';
        SET @N = @@ROWCOUNT;
        INSERT dbo.Resultado VALUES (@Escenario, 'estatico', CONCAT('filas ', @N));
    END TRY
    BEGIN CATCH
        INSERT dbo.Resultado VALUES (@Escenario, 'estatico', CONCAT('error ', ERROR_NUMBER()));
    END CATCH;
    DELETE @Filas;
    BEGIN TRY
        INSERT @Filas EXEC seguridad.BuscarSeguro @Nombre = N'leia';
        SET @N = @@ROWCOUNT;
        INSERT dbo.Resultado VALUES (@Escenario, 'dinamico', CONCAT('filas ', @N));
    END TRY
    BEGIN CATCH
        INSERT dbo.Resultado VALUES (@Escenario, 'dinamico', CONCAT('error ', ERROR_NUMBER()));
    END CATCH;
    DELETE @Filas;
    BEGIN TRY
        -- SQL dinámico: corta el encadenamiento de propiedad de dbo.Probar y evalúa los permisos de app_demo.
        INSERT @Filas EXEC (N'SELECT UsuarioId, Nombre, Rol FROM seguridad.UsuarioDemo;');
        SET @N = @@ROWCOUNT;
        INSERT dbo.Resultado VALUES (@Escenario, 'select-directo', CONCAT('filas ', @N));
    END TRY
    BEGIN CATCH
        INSERT dbo.Resultado VALUES (@Escenario, 'select-directo', CONCAT('error ', ERROR_NUMBER()));
    END CATCH;
    REVERT;
END;
GO
GRANT EXECUTE ON dbo.Probar TO app_demo;
GO
EXEC dbo.Probar 'sin-select';
GO
DENY SELECT ON OBJECT::seguridad.UsuarioDemo TO rol_consulta_usuario;
GO
EXEC dbo.Probar 'deny-select';
GO
-- Remedio: firmar el procedimiento dinámico con un certificado cuyo usuario tiene SELECT.
REVOKE SELECT ON OBJECT::seguridad.UsuarioDemo FROM rol_consulta_usuario;
CREATE CERTIFICATE CertBuscarSeguro
    ENCRYPTION BY PASSWORD = 'Laboratorio-Firma-2026!'
    WITH SUBJECT = 'Firma de seguridad.BuscarSeguro';
CREATE USER UsuarioCertBuscar FROM CERTIFICATE CertBuscarSeguro;
GRANT SELECT ON OBJECT::seguridad.UsuarioDemo TO UsuarioCertBuscar;
ADD SIGNATURE TO seguridad.BuscarSeguro
    BY CERTIFICATE CertBuscarSeguro WITH PASSWORD = 'Laboratorio-Firma-2026!';
GO
EXEC dbo.Probar 'firmado';
GO
DENY SELECT ON OBJECT::seguridad.UsuarioDemo TO rol_consulta_usuario;
GO
EXEC dbo.Probar 'firmado-con-deny';
GO
SELECT Escenario, Caso, Salida FROM dbo.Resultado ORDER BY Orden;
