-- SIN-PRELUDE
-- Cifrado de una columna con frase de paso y autenticador.
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
DECLARE @Frase NVARCHAR(128) = N'Frase-didactica-no-usar-en-produccion';

UPDATE ventas.Tarjeta
SET NumeroCifrado = EncryptByPassPhrase(@Frase, Numero, 1, CONVERT(VARBINARY(128), TarjetaId));

SELECT TarjetaId,
       CONVERT(NVARCHAR(30), DecryptByPassPhrase(@Frase, NumeroCifrado, 1, CONVERT(VARBINARY(128), TarjetaId))) AS Numero,
       CONVERT(VARCHAR(30), DecryptByPassPhrase(@Frase, NumeroCifrado, 1, CONVERT(VARBINARY(128), TarjetaId))) AS ComoVarchar,
       DecryptByPassPhrase(@Frase, NumeroCifrado, 1, CONVERT(VARBINARY(128), TarjetaId + 1)) AS AutenticadorErroneo,
       DecryptByPassPhrase(N'otra frase', NumeroCifrado, 1, CONVERT(VARBINARY(128), TarjetaId)) AS FraseErronea
FROM ventas.Tarjeta
ORDER BY TarjetaId;
