-- SIN-PRELUDE
-- Concatenación frente a parámetros, en lotes completos.
CREATE SCHEMA seguridad;
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
-- Incorrecto: concatena la entrada. Entrada normal.
DECLARE @Nombre NVARCHAR(100) = N'leia';
DECLARE @Sql NVARCHAR(MAX) =
    N'SELECT UsuarioId, Nombre, Rol FROM seguridad.UsuarioDemo WHERE Rol = ''usuario'' AND Nombre = ''' + @Nombre + N''';';
SELECT @Sql AS SqlGenerado;
EXEC (@Sql);
GO
-- Incorrecto: la entrada cambia la estructura del filtro.
DECLARE @Nombre NVARCHAR(100) = N''' OR Rol = ''admin''--';
DECLARE @Sql NVARCHAR(MAX) =
    N'SELECT UsuarioId, Nombre, Rol FROM seguridad.UsuarioDemo WHERE Rol = ''usuario'' AND Nombre = ''' + @Nombre + N''';';
SELECT @Sql AS SqlGenerado;
EXEC (@Sql);
GO
-- Correcto: la misma entrada viaja como parámetro tipado.
DECLARE @Nombre NVARCHAR(100) = N''' OR Rol = ''admin''--';
DECLARE @Sql NVARCHAR(MAX) =
    N'SELECT UsuarioId, Nombre, Rol FROM seguridad.UsuarioDemo WHERE Rol = ''usuario'' AND Nombre = @PNombre;';
EXEC sys.sp_executesql @stmt = @Sql, @params = N'@PNombre NVARCHAR(100)', @PNombre = @Nombre;
SELECT @@ROWCOUNT AS FilasConParametro;
GO
-- Identificador dinámico con lista permitida.
CREATE PROCEDURE seguridad.ListarOrdenado @Columna SYSNAME
AS
BEGIN
    IF @Columna NOT IN (N'Nombre', N'Rol')
        THROW 50001, 'Columna no permitida.', 1;

    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT UsuarioId, Nombre, Rol FROM seguridad.UsuarioDemo ORDER BY ' + QUOTENAME(@Columna) + N', UsuarioId;';
    EXEC sys.sp_executesql @Sql;
END;
GO
EXEC seguridad.ListarOrdenado @Columna = N'Rol';
GO
BEGIN TRY
    EXEC seguridad.ListarOrdenado @Columna = N'Rol, (SELECT 1)';
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Error, ERROR_MESSAGE() AS Mensaje;
END CATCH;
