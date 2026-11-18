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
-- Autenticación y directivas de contraseña (sección «Autenticación»).
SELECT SERVERPROPERTY('IsIntegratedSecurityOnly') AS SoloWindows;
GO
EXEC dbo.Ejecutar 'corta-con-politica', N'CREATE LOGIN LoginU5T01Corta WITH PASSWORD = ''Ab1!'', CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'sin-complejidad', N'CREATE LOGIN LoginU5T01Simple WITH PASSWORD = ''abcdefgh'', CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'cumple-y-debe-cambiar', N'CREATE LOGIN LoginU5T01Ana WITH PASSWORD = ''Didactica#2026a'' MUST_CHANGE, CHECK_EXPIRATION = ON, CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'sin-politica', N'CREATE LOGIN LoginU5T01Libre WITH PASSWORD = ''abc'', CHECK_POLICY = OFF';
EXEC dbo.Ejecutar 'vencimiento-sin-politica', N'CREATE LOGIN LoginU5T01Venc WITH PASSWORD = ''Didactica#2026b'', CHECK_EXPIRATION = ON, CHECK_POLICY = OFF';
EXEC dbo.Ejecutar 'cambio-sin-vencimiento', N'CREATE LOGIN LoginU5T01Cambio WITH PASSWORD = ''Didactica#2026e'' MUST_CHANGE, CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'con-vencimiento', N'CREATE LOGIN LoginU5T01Venc3 WITH PASSWORD = ''Didactica#2026f'', CHECK_EXPIRATION = ON, CHECK_POLICY = ON';
EXEC dbo.Ejecutar 'valores-por-defecto', N'CREATE LOGIN LoginU5T01Def WITH PASSWORD = ''Didactica#2026c''';
SELECT Paso, Resultado FROM dbo.Resultado ORDER BY Orden;
GO
SELECT name, is_policy_checked AS Politica, is_expiration_checked AS Vencimiento,
       LOGINPROPERTY(name, 'IsMustChange') AS DebeCambiar
FROM sys.sql_logins
WHERE name LIKE 'LoginU5T01%'
ORDER BY name;
SELECT PWDCOMPARE(N'Didactica#2026c', password_hash) AS Exacta,
       PWDCOMPARE(N'didactica#2026c', password_hash) AS OtraCapitalizacion
FROM sys.sql_logins
WHERE name = 'LoginU5T01Def';
ALTER LOGIN LoginU5T01Def DISABLE;
SELECT name, is_disabled FROM sys.sql_logins WHERE name = 'LoginU5T01Def';
SELECT LOGINPROPERTY('LoginU5T01Venc3', 'DaysUntilExpiration') AS DiasParaVencer;
GO
-- Limpieza de objetos de servidor
DECLARE @Login SYSNAME;
DECLARE Pendientes CURSOR LOCAL FAST_FORWARD FOR SELECT name FROM sys.server_principals WHERE name LIKE 'LoginU5T01%';
OPEN Pendientes;
FETCH NEXT FROM Pendientes INTO @Login;
WHILE @@FETCH_STATUS = 0
BEGIN
    EXEC (N'DROP LOGIN ' + @Login);
    FETCH NEXT FROM Pendientes INTO @Login;
END;
CLOSE Pendientes;
DEALLOCATE Pendientes;
SELECT COUNT(*) AS LoginsRestantes FROM sys.server_principals WHERE name LIKE 'LoginU5T01%';
