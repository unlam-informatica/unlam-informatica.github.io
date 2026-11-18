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

DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(50), Trancount INT, SaldoCuenta1 DECIMAL(12,2));
DECLARE @Anidamiento INT, @Saldo DECIMAL(12,2);

SET IMPLICIT_TRANSACTIONS ON;

UPDATE banco.Cuenta SET Saldo = Saldo + 250 WHERE CuentaId = 1;   -- abre la transacción sin BEGIN
SET @Anidamiento = @@TRANCOUNT;
SELECT @Saldo = Saldo FROM banco.Cuenta WHERE CuentaId = 1;
INSERT INTO @Observacion VALUES (1, 'después del UPDATE', @Anidamiento, @Saldo);

ROLLBACK TRANSACTION;

SET @Anidamiento = @@TRANCOUNT;
SELECT @Saldo = Saldo FROM banco.Cuenta WHERE CuentaId = 1;   -- este SELECT abre otra transacción
COMMIT TRANSACTION;
SET IMPLICIT_TRANSACTIONS OFF;
INSERT INTO @Observacion VALUES (2, 'después del ROLLBACK', @Anidamiento, @Saldo);

SELECT Orden, Momento, Trancount, SaldoCuenta1 FROM @Observacion ORDER BY Orden;
