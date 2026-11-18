-- SIN-PRELUDE
-- Laboratorio de inyección, preparación y partes 1 a 4.
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
CREATE OR ALTER PROCEDURE seguridad.BuscarVulnerable
    @Nombre NVARCHAR(100)
AS
BEGIN
    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT UsuarioId, Nombre, Rol
          FROM seguridad.UsuarioDemo
          WHERE Nombre = ''' + @Nombre + N''';';

    SELECT @Sql AS SqlGenerado;
    EXEC (@Sql);
END;
GO
EXEC seguridad.BuscarVulnerable @Nombre = N'leia';
GO
EXEC seguridad.BuscarVulnerable @Nombre = N''' OR 1=1--';
GO
CREATE OR ALTER PROCEDURE seguridad.BuscarSeguro
    @Nombre NVARCHAR(100)
AS
BEGIN
    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT UsuarioId, Nombre, Rol
          FROM seguridad.UsuarioDemo
          WHERE Nombre = @PNombre;';

    EXEC sys.sp_executesql
        @stmt = @Sql,
        @params = N'@PNombre NVARCHAR(100)',
        @PNombre = @Nombre;
END;
GO
EXEC seguridad.BuscarSeguro @Nombre = N'leia';
GO
EXEC seguridad.BuscarSeguro @Nombre = N''' OR 1=1--';
GO
CREATE OR ALTER PROCEDURE seguridad.BuscarEstatico
    @Nombre NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT UsuarioId, Nombre, Rol
    FROM seguridad.UsuarioDemo
    WHERE Nombre = @Nombre;
END;
GO
EXEC seguridad.BuscarEstatico @Nombre = N'luke';
GO
CREATE OR ALTER PROCEDURE seguridad.ListarSeguro
    @Orden SYSNAME
AS
BEGIN
    IF @Orden NOT IN (N'Nombre', N'Rol')
        THROW 50010, 'Orden no permitido.', 1;

    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT UsuarioId, Nombre, Rol
          FROM seguridad.UsuarioDemo
          ORDER BY ' + QUOTENAME(@Orden) + N', UsuarioId;';

    EXEC sys.sp_executesql @Sql;
END;
GO
EXEC seguridad.ListarSeguro @Orden = N'Nombre';
GO
EXEC seguridad.ListarSeguro @Orden = N'Rol';
GO
BEGIN TRY
    EXEC seguridad.ListarSeguro @Orden = N'Clave';
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Error, ERROR_MESSAGE() AS Mensaje;
END CATCH;
