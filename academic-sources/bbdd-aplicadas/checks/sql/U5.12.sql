-- SIN-PRELUDE
-- Ejercicio U5.12: rotación de una clave simétrica.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Tarjeta
(
    TarjetaId     INT           NOT NULL CONSTRAINT PK_Tarjeta PRIMARY KEY,
    Numero        NVARCHAR(30)  NOT NULL,
    NumeroCifrado VARBINARY(256) NULL
);
INSERT ventas.Tarjeta (TarjetaId, Numero) VALUES (1, N'4000-0000-0000-0001'), (2, N'4000-0000-0000-0002');
GO
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Didactica#ClaveMaestra-2026';
CREATE CERTIFICATE CertificadoDatos WITH SUBJECT = 'Protege las claves simetricas';
CREATE SYMMETRIC KEY ClaveTarjetaV1 WITH ALGORITHM = AES_256 ENCRYPTION BY CERTIFICATE CertificadoDatos;
GO
OPEN SYMMETRIC KEY ClaveTarjetaV1 DECRYPTION BY CERTIFICATE CertificadoDatos;
UPDATE ventas.Tarjeta
SET NumeroCifrado = EncryptByKey(KEY_GUID('ClaveTarjetaV1'), Numero, 1, CONVERT(VARBINARY(128), TarjetaId));
CLOSE SYMMETRIC KEY ClaveTarjetaV1;
GO
-- Rotación: nueva clave, re-cifrado y baja de la anterior.
CREATE SYMMETRIC KEY ClaveTarjetaV2 WITH ALGORITHM = AES_256 ENCRYPTION BY CERTIFICATE CertificadoDatos;
GO
OPEN SYMMETRIC KEY ClaveTarjetaV1 DECRYPTION BY CERTIFICATE CertificadoDatos;
OPEN SYMMETRIC KEY ClaveTarjetaV2 DECRYPTION BY CERTIFICATE CertificadoDatos;

UPDATE ventas.Tarjeta
SET NumeroCifrado = EncryptByKey(
        KEY_GUID('ClaveTarjetaV2'),
        DecryptByKey(NumeroCifrado, 1, CONVERT(VARBINARY(128), TarjetaId)),
        1,
        CONVERT(VARBINARY(128), TarjetaId));

CLOSE SYMMETRIC KEY ClaveTarjetaV1;
CLOSE SYMMETRIC KEY ClaveTarjetaV2;
GO
DROP SYMMETRIC KEY ClaveTarjetaV1;
GO
OPEN SYMMETRIC KEY ClaveTarjetaV2 DECRYPTION BY CERTIFICATE CertificadoDatos;
SELECT TarjetaId,
       CONVERT(NVARCHAR(30), DecryptByKey(NumeroCifrado, 1, CONVERT(VARBINARY(128), TarjetaId))) AS Numero
FROM ventas.Tarjeta
ORDER BY TarjetaId;
CLOSE SYMMETRIC KEY ClaveTarjetaV2;
SELECT name FROM sys.symmetric_keys WHERE name LIKE 'ClaveTarjeta%' ORDER BY name;
