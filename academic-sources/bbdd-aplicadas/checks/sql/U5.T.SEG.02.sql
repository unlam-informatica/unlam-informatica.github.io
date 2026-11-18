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
-- Formas de usuario de base de datos que se pueden crear sin dominio de Windows.
CREATE LOGIN LoginU5T02 WITH PASSWORD = 'Didactica#2026d', CHECK_POLICY = ON;
GO
BEGIN TRY
    EXEC (N'CREATE USER UsuarioLogin FOR LOGIN LoginU5T02');
    EXEC (N'CREATE USER UsuarioSinLogin WITHOUT LOGIN');
    EXEC (N'CREATE CERTIFICATE CertU5T02 ENCRYPTION BY PASSWORD = ''Didactica#Cert-2026'' WITH SUBJECT = ''Certificado didactico''');
    EXEC (N'CREATE USER UsuarioCertificado FROM CERTIFICATE CertU5T02');
    EXEC (N'CREATE ASYMMETRIC KEY ClaveU5T02 WITH ALGORITHM = RSA_2048 ENCRYPTION BY PASSWORD = ''Didactica#Clave-2026''');
    EXEC (N'CREATE USER UsuarioClave FROM ASYMMETRIC KEY ClaveU5T02');
    EXEC (N'CREATE USER OtroUsuario FOR LOGIN LoginU5T02');
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorSegundoUsuarioDelLogin;
END CATCH;
SELECT name, type_desc, authentication_type_desc
FROM sys.database_principals
WHERE name IN ('UsuarioLogin', 'UsuarioSinLogin', 'UsuarioCertificado', 'UsuarioClave', 'OtroUsuario')
ORDER BY name;
GO
DROP LOGIN LoginU5T02;
SELECT COUNT(*) AS LoginsRestantes FROM sys.server_principals WHERE name = 'LoginU5T02';
