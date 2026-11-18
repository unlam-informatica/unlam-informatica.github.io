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

DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(60), Trancount INT, Detalle VARCHAR(80));

BEGIN TRANSACTION TxExterna;
    INSERT INTO @Observacion VALUES (1, 'BEGIN TRANSACTION TxExterna', @@TRANCOUNT, NULL);
    UPDATE banco.Cuenta SET Saldo = Saldo + 10 WHERE CuentaId = 1;

    BEGIN TRANSACTION TxInterna;
        INSERT INTO @Observacion VALUES (2, 'BEGIN TRANSACTION TxInterna', @@TRANCOUNT, NULL);
        UPDATE banco.Cuenta SET Saldo = Saldo + 20 WHERE CuentaId = 2;

        BEGIN TRY
            ROLLBACK TRANSACTION TxInterna;   -- no es un savepoint: error 6401
        END TRY
        BEGIN CATCH
            INSERT INTO @Observacion VALUES (3, 'ROLLBACK TRANSACTION TxInterna', @@TRANCOUNT,
                CONCAT('error ', ERROR_NUMBER()));
        END CATCH;
    COMMIT TRANSACTION TxInterna;
    INSERT INTO @Observacion VALUES (4, 'COMMIT de la interna', @@TRANCOUNT, 'no confirma nada todavía');
ROLLBACK TRANSACTION TxExterna;
INSERT INTO @Observacion VALUES (5, 'ROLLBACK TRANSACTION TxExterna', @@TRANCOUNT, 'revierte las dos');

INSERT INTO @Observacion
SELECT 6, 'saldos finales', @@TRANCOUNT, CONCAT('cuenta 1 = ', c1.Saldo, ', cuenta 2 = ', c2.Saldo)
FROM banco.Cuenta AS c1
JOIN banco.Cuenta AS c2 ON c2.CuentaId = 2
WHERE c1.CuentaId = 1;

SELECT Orden, Momento, Trancount, Detalle FROM @Observacion ORDER BY Orden;
