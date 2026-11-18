IF SCHEMA_ID('banco') IS NULL
    EXEC ('CREATE SCHEMA banco');
GO
DROP TABLE IF EXISTS banco.TransaccionTarjeta;
DROP TABLE IF EXISTS banco.TarjetaCredito;
GO
CREATE TABLE banco.TarjetaCredito (
    NroTarjeta    BIGINT        NOT NULL CONSTRAINT PK_TarjetaCredito PRIMARY KEY,
    Ciudad        VARCHAR(50)   NOT NULL,
    LimiteCredito DECIMAL(12,2) NOT NULL
);
CREATE TABLE banco.TransaccionTarjeta (
    TransaccionId        INT           NOT NULL CONSTRAINT PK_TransaccionTarjeta PRIMARY KEY,
    NroTarjeta           BIGINT        NOT NULL CONSTRAINT FK_TransaccionTarjeta_Tarjeta
                                       REFERENCES banco.TarjetaCredito (NroTarjeta),
    Fecha                DATETIME      NOT NULL,
    Monto                DECIMAL(12,2) NOT NULL,
    TransaccionOrigenId  INT           NULL CONSTRAINT FK_TransaccionTarjeta_Origen
                                       REFERENCES banco.TransaccionTarjeta (TransaccionId),
    Tipo                 CHAR(1)       NOT NULL CONSTRAINT CK_TransaccionTarjeta_Tipo CHECK (Tipo IN ('V', 'R'))
);
CREATE INDEX IX_TransaccionTarjeta_NroTarjeta ON banco.TransaccionTarjeta (NroTarjeta);
GO
INSERT INTO banco.TarjetaCredito (NroTarjeta, Ciudad, LimiteCredito) VALUES
    (1000000000000001, 'Ciudad A',  6000.00),
    (1000000000000002, 'Ciudad B', 16000.00),
    (1000000000000003, 'Ciudad C', 14000.00),
    (1000000000000004, 'Ciudad D', 18000.00);
GO
DECLARE @TransaccionId INT = 1001,
        @NroTarjeta    BIGINT = 1000000000000001,
        @Monto         DECIMAL(12,2) = 500.00,
        @LimiteActual  DECIMAL(12,2);

BEGIN TRANSACTION;
    SELECT @LimiteActual = LimiteCredito
    FROM banco.TarjetaCredito
    WHERE NroTarjeta = @NroTarjeta;

    IF @LimiteActual >= @Monto
    BEGIN
        INSERT INTO banco.TransaccionTarjeta (TransaccionId, NroTarjeta, Fecha, Monto, TransaccionOrigenId, Tipo)
        VALUES (@TransaccionId, @NroTarjeta, '2026-03-01T10:00:00', @Monto, NULL, 'V');

        UPDATE banco.TarjetaCredito
        SET LimiteCredito = LimiteCredito - @Monto
        WHERE NroTarjeta = @NroTarjeta;
    END;
COMMIT TRANSACTION;

SELECT t.TransaccionId, t.NroTarjeta, t.Monto, t.Tipo, c.LimiteCredito
FROM banco.TransaccionTarjeta AS t
JOIN banco.TarjetaCredito AS c ON c.NroTarjeta = t.NroTarjeta
ORDER BY t.TransaccionId;
