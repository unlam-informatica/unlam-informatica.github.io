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

DECLARE @Observacion TABLE (Orden INT, Variante VARCHAR(40), ErrorVisible INT);

-- CATCH ingenuo: ROLLBACK sin comprobar si hay transacción. El error ocurre antes del BEGIN TRANSACTION.
BEGIN TRY
    IF NOT EXISTS (SELECT 1 FROM banco.Cuenta WHERE CuentaId = 99)
        THROW 50010, 'La cuenta no existe.', 1;
    BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 99;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    BEGIN TRY
        ROLLBACK TRANSACTION;                -- no hay transacción abierta
    END TRY
    BEGIN CATCH
        INSERT INTO @Observacion VALUES (1, 'ROLLBACK sin comprobar', ERROR_NUMBER());
    END CATCH;
END CATCH;

-- CATCH correcto: se comprueba XACT_STATE() y se conserva el error original.
BEGIN TRY
    IF NOT EXISTS (SELECT 1 FROM banco.Cuenta WHERE CuentaId = 99)
        THROW 50010, 'La cuenta no existe.', 1;
    BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 99;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    DECLARE @Original INT = ERROR_NUMBER();
    IF XACT_STATE() <> 0
        ROLLBACK TRANSACTION;
    INSERT INTO @Observacion VALUES (2, 'con XACT_STATE()', @Original);
END CATCH;

SELECT Orden, Variante, ErrorVisible FROM @Observacion ORDER BY Orden;
