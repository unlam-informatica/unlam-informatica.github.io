-- SIN-PRELUDE
-- Jerarquía de TDE hasta la clave de cifrado de la base (sin activar el cifrado).
-- Crea y elimina objetos en master: clave maestra y certificado del servidor.
DECLARE @CreoClaveMaestra BIT = 0;
BEGIN TRY
    IF NOT EXISTS (SELECT 1 FROM master.sys.symmetric_keys WHERE name = '##MS_DatabaseMasterKey##')
    BEGIN
        EXEC master.sys.sp_executesql N'CREATE MASTER KEY ENCRYPTION BY PASSWORD = ''Didactica#MasterTDE-2026''';
        SET @CreoClaveMaestra = 1;
    END;
    EXEC master.sys.sp_executesql N'CREATE CERTIFICATE CertificadoTdeU5T03 WITH SUBJECT = ''TDE didactico U5T03''';
    EXEC (N'CREATE DATABASE ENCRYPTION KEY WITH ALGORITHM = AES_256 ENCRYPTION BY SERVER CERTIFICATE CertificadoTdeU5T03');
    SELECT DB_NAME(database_id) AS Base, encryption_state AS Estado, key_algorithm AS Algoritmo, key_length AS Largo
    FROM sys.dm_database_encryption_keys
    WHERE database_id = DB_ID();
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorNumero, ERROR_MESSAGE() AS Mensaje;
END CATCH;
-- Limpieza que corre aunque haya fallado lo anterior
BEGIN TRY
    IF EXISTS (SELECT 1 FROM sys.dm_database_encryption_keys WHERE database_id = DB_ID())
        EXEC (N'DROP DATABASE ENCRYPTION KEY');
    IF EXISTS (SELECT 1 FROM master.sys.certificates WHERE name = 'CertificadoTdeU5T03')
        EXEC master.sys.sp_executesql N'DROP CERTIFICATE CertificadoTdeU5T03';
    IF @CreoClaveMaestra = 1
        EXEC master.sys.sp_executesql N'DROP MASTER KEY';
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS ErrorLimpieza, ERROR_MESSAGE() AS MensajeLimpieza;
END CATCH;
SELECT (SELECT COUNT(*) FROM master.sys.certificates WHERE name = 'CertificadoTdeU5T03') AS CertificadosRestantes,
       (SELECT COUNT(*) FROM master.sys.symmetric_keys WHERE name = '##MS_DatabaseMasterKey##') AS ClavesMaestrasEnMaster;
