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

DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(60), Trancount INT, SaldoCuenta3 DECIMAL(12,2));

BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 100 WHERE CuentaId = 3;
    SAVE TRANSACTION PuntoA;
    UPDATE banco.Cuenta SET Saldo = Saldo + 200 WHERE CuentaId = 3;
    SAVE TRANSACTION PuntoB;
    UPDATE banco.Cuenta SET Saldo = Saldo + 9999 WHERE CuentaId = 3;
    INSERT INTO @Observacion SELECT 1, 'antes del ROLLBACK a PuntoB', @@TRANCOUNT, Saldo
        FROM banco.Cuenta WHERE CuentaId = 3;

    ROLLBACK TRANSACTION PuntoB;
    INSERT INTO @Observacion SELECT 2, 'después del ROLLBACK a PuntoB', @@TRANCOUNT, Saldo
        FROM banco.Cuenta WHERE CuentaId = 3;
COMMIT TRANSACTION;

INSERT INTO @Observacion SELECT 3, 'después del COMMIT', @@TRANCOUNT, Saldo
    FROM banco.Cuenta WHERE CuentaId = 3;

SELECT Orden, Momento, Trancount, SaldoCuenta3 FROM @Observacion ORDER BY Orden;
