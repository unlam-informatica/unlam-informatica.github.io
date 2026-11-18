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

DECLARE @Observacion TABLE (Orden INT, XactAbort VARCHAR(3), Error INT, Estado INT, SaldoCuenta1 DECIMAL(12,2));
DECLARE @Error INT, @Estado INT, @Saldo DECIMAL(12,2);

-- XACT_ABORT OFF: el INSERT con FK inválida falla pero la transacción sigue abierta.
SET XACT_ABORT OFF;
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo + 10 WHERE CuentaId = 1;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto) VALUES (999, 'C', 10);
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    SET @Estado = XACT_STATE();
    SELECT @Saldo = Saldo FROM banco.Cuenta WHERE CuentaId = 1;
    INSERT INTO @Observacion VALUES (1, 'OFF', @Error, @Estado, @Saldo);
    IF @Estado = 1 COMMIT TRANSACTION;     -- lo que sí se ejecutó queda confirmado
    IF @Estado = -1 ROLLBACK TRANSACTION;
END CATCH;

-- XACT_ABORT ON: el mismo error condena la transacción.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo + 10 WHERE CuentaId = 1;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto) VALUES (999, 'C', 10);
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    SET @Estado = XACT_STATE();
    IF @Estado = 1 COMMIT TRANSACTION;
    IF @Estado = -1 ROLLBACK TRANSACTION;
    SELECT @Saldo = Saldo FROM banco.Cuenta WHERE CuentaId = 1;
    INSERT INTO @Observacion VALUES (2, 'ON', @Error, @Estado, @Saldo);
END CATCH;
SET XACT_ABORT OFF;

SELECT Orden, XactAbort, Error, Estado, SaldoCuenta1 FROM @Observacion ORDER BY Orden;
