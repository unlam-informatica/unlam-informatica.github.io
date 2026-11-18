-- SIN-PRELUDE
-- Jerarquía de claves dentro de una base: clave maestra de la base, certificado y clave simétrica.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Tarjeta
(
    TarjetaId     INT           NOT NULL CONSTRAINT PK_Tarjeta PRIMARY KEY,
    Numero        NVARCHAR(30)  NOT NULL,
    NumeroCifrado VARBINARY(256) NULL
);
INSERT ventas.Tarjeta (TarjetaId, Numero)
VALUES (1, N'4000-0000-0000-0001'), (2, N'4000-0000-0000-0002');
GO
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Didactica#ClaveMaestra-2026';
CREATE CERTIFICATE CertificadoDatos WITH SUBJECT = 'Protege la clave simetrica de tarjetas';
CREATE SYMMETRIC KEY ClaveTarjeta
    WITH ALGORITHM = AES_256
    ENCRYPTION BY CERTIFICATE CertificadoDatos;
GO
OPEN SYMMETRIC KEY ClaveTarjeta DECRYPTION BY CERTIFICATE CertificadoDatos;

UPDATE ventas.Tarjeta
SET NumeroCifrado = EncryptByKey(KEY_GUID('ClaveTarjeta'), Numero, 1, CONVERT(VARBINARY(128), TarjetaId));

SELECT TarjetaId,
       CONVERT(NVARCHAR(30), DecryptByKey(NumeroCifrado, 1, CONVERT(VARBINARY(128), TarjetaId))) AS Numero
FROM ventas.Tarjeta
ORDER BY TarjetaId;

CLOSE SYMMETRIC KEY ClaveTarjeta;

SELECT TarjetaId,
       CONVERT(NVARCHAR(30), DecryptByKey(NumeroCifrado, 1, CONVERT(VARBINARY(128), TarjetaId))) AS NumeroSinAbrirLaClave
FROM ventas.Tarjeta
ORDER BY TarjetaId;
