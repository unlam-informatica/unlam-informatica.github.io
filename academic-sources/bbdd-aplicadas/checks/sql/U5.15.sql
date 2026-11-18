-- SIN-PRELUDE
-- Ejercicio U5.15: inyección de segundo orden.
CREATE SCHEMA seguridad;
GO
CREATE TABLE seguridad.Alias
(
    AliasId INT IDENTITY PRIMARY KEY,
    Texto   NVARCHAR(100) NOT NULL
);
CREATE TABLE seguridad.Mensaje
(
    MensajeId INT IDENTITY PRIMARY KEY,
    Autor     NVARCHAR(100) NOT NULL,
    Privado   BIT NOT NULL
);
INSERT seguridad.Mensaje (Autor, Privado)
VALUES (N'ana', 0), (N'ana', 1), (N'beto', 0), (N'beto', 1);
GO
-- El alta es segura: parámetros.
CREATE PROCEDURE seguridad.RegistrarAlias @Texto NVARCHAR(100)
AS
BEGIN
    INSERT seguridad.Alias (Texto) VALUES (@Texto);
END;
GO
EXEC seguridad.RegistrarAlias @Texto = N'ana';
EXEC seguridad.RegistrarAlias @Texto = N''' OR Privado = 1--';
GO
-- El proceso posterior concatena el valor guardado.
CREATE PROCEDURE seguridad.ResumenAlias
AS
BEGIN
    DECLARE @Texto NVARCHAR(100), @Sql NVARCHAR(MAX);
    DECLARE Alias CURSOR LOCAL FAST_FORWARD FOR SELECT Texto FROM seguridad.Alias ORDER BY AliasId;
    OPEN Alias;
    FETCH NEXT FROM Alias INTO @Texto;
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @Sql = N'SELECT COUNT(*) AS Mensajes FROM seguridad.Mensaje WHERE Privado = 0 AND Autor = ''' + @Texto + N''';';
        EXEC (@Sql);
        FETCH NEXT FROM Alias INTO @Texto;
    END;
    CLOSE Alias;
    DEALLOCATE Alias;
END;
GO
EXEC seguridad.ResumenAlias;
GO
-- Corrección: el proceso posterior no concatena nada.
CREATE OR ALTER PROCEDURE seguridad.ResumenAlias
AS
BEGIN
    SET NOCOUNT ON;
    SELECT a.Texto AS Alias, COUNT(m.MensajeId) AS Mensajes
    FROM seguridad.Alias AS a
    LEFT JOIN seguridad.Mensaje AS m ON m.Autor = a.Texto AND m.Privado = 0
    GROUP BY a.AliasId, a.Texto
    ORDER BY a.AliasId;
END;
GO
EXEC seguridad.ResumenAlias;
