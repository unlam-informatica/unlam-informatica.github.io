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
-- Ejercicio U5.02: contraseñas y directivas.
EXEC dbo.Ejecutar 'A Primavera', N'CREATE LOGIN LoginU502A WITH PASSWORD = ''Primavera'', CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'B Pri2026', N'CREATE LOGIN LoginU502B WITH PASSWORD = ''Pri2026'', CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'C Primavera2026', N'CREATE LOGIN LoginU502C WITH PASSWORD = ''Primavera2026'', CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'D primavera_2026', N'CREATE LOGIN LoginU502D WITH PASSWORD = ''primavera_2026'', CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'E Primavera con politica apagada', N'CREATE LOGIN LoginU502E WITH PASSWORD = ''Primavera'', CHECK_POLICY = OFF';
EXEC dbo.Ejecutar 'F MUST_CHANGE sin vencimiento', N'CREATE LOGIN LoginU502F WITH PASSWORD = ''Primavera2026'' MUST_CHANGE, CHECK_POLICY = ON';
GO
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
SELECT name, is_policy_checked AS Politica, is_expiration_checked AS Vencimiento
FROM sys.sql_logins
WHERE name LIKE 'LoginU502%'
ORDER BY name;
GO
-- Limpieza de objetos de servidor
DECLARE @Login SYSNAME;
DECLARE Pendientes CURSOR LOCAL FAST_FORWARD FOR SELECT name FROM sys.server_principals WHERE name LIKE 'LoginU502%';
OPEN Pendientes;
FETCH NEXT FROM Pendientes INTO @Login;
WHILE @@FETCH_STATUS = 0
BEGIN
    EXEC (N'DROP LOGIN ' + @Login);
    FETCH NEXT FROM Pendientes INTO @Login;
END;
CLOSE Pendientes;
DEALLOCATE Pendientes;
SELECT COUNT(*) AS LoginsRestantes FROM sys.server_principals WHERE name LIKE 'LoginU502%';
