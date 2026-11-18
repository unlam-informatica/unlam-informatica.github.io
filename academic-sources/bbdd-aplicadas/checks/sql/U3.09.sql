IF SCHEMA_ID('banco') IS NULL
    EXEC ('CREATE SCHEMA banco');
GO
DROP TABLE IF EXISTS banco.Movimiento;
DROP TABLE IF EXISTS banco.Cuenta;
GO
CREATE TABLE banco.Cuenta (
    CuentaId INT           NOT NULL CONSTRAINT PK_Cuenta PRIMARY KEY,
    Titular  VARCHAR(40)   NOT NULL,
    Saldo    DECIMAL(12,2) NOT NULL CONSTRAINT CK_Cuenta_Saldo CHECK (Saldo >= 0)
);
CREATE TABLE banco.Movimiento (
    MovimientoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Movimiento PRIMARY KEY,
    CuentaId     INT           NOT NULL CONSTRAINT FK_Movimiento_Cuenta REFERENCES banco.Cuenta (CuentaId),
    Tipo         CHAR(1)       NOT NULL CONSTRAINT CK_Movimiento_Tipo CHECK (Tipo IN ('D', 'C')),
    Monto        DECIMAL(12,2) NOT NULL CONSTRAINT CK_Movimiento_Monto CHECK (Monto > 0),
    Descripcion  VARCHAR(100)  NULL
);
GO
INSERT INTO banco.Cuenta (CuentaId, Titular, Saldo) VALUES
    (1, 'Cliente 01', 5000.00),
    (2, 'Cliente 02', 3200.00),
    (3, 'Cliente 03',  800.00);
GO

GO
DROP PROCEDURE IF EXISTS banco.TransferirLote;
DROP TYPE IF EXISTS banco.TransferenciaTipo;
GO
CREATE TYPE banco.TransferenciaTipo AS TABLE
(
    Origen  INT           NOT NULL,
    Destino INT           NOT NULL,
    Monto   DECIMAL(12,2) NOT NULL CHECK (Monto > 0)
);
GO
CREATE OR ALTER PROCEDURE banco.TransferirLote
    @Lote banco.TransferenciaTipo READONLY
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        UPDATE c
        SET c.Saldo = c.Saldo + n.Neto
        FROM banco.Cuenta AS c
        JOIN (SELECT CuentaId, SUM(Monto) AS Neto
              FROM (SELECT Origen AS CuentaId, -Monto AS Monto FROM @Lote
                    UNION ALL
                    SELECT Destino, Monto FROM @Lote) AS m
              GROUP BY CuentaId) AS n ON n.CuentaId = c.CuentaId;

        INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion)
        SELECT Origen, 'D', Monto, CONCAT('Lote: a cuenta ', Destino) FROM @Lote
        UNION ALL
        SELECT Destino, 'C', Monto, CONCAT('Lote: de cuenta ', Origen) FROM @Lote;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0
            ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
GO
DECLARE @Valido banco.TransferenciaTipo, @Invalido banco.TransferenciaTipo;
INSERT INTO @Valido VALUES (1, 2, 300), (2, 3, 100);
INSERT INTO @Invalido VALUES (1, 2, 300), (3, 1, 1000);   -- la cuenta 3 queda con solo 900

DECLARE @Observacion TABLE (Orden INT, Lote VARCHAR(10), Error INT);
EXEC banco.TransferirLote @Valido;
INSERT INTO @Observacion VALUES (1, 'válido', 0);
BEGIN TRY
    EXEC banco.TransferirLote @Invalido;
END TRY
BEGIN CATCH
    INSERT INTO @Observacion VALUES (2, 'inválido', ERROR_NUMBER());
END CATCH;

SELECT Orden, Lote, Error FROM @Observacion ORDER BY Orden;
SELECT CuentaId, Saldo FROM banco.Cuenta ORDER BY CuentaId;
SELECT COUNT(*) AS Movimientos FROM banco.Movimiento;
