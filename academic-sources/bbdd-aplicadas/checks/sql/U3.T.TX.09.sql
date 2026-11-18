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

DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(60), Valor VARCHAR(80));
DECLARE @Estado INT, @Error INT;

SET XACT_ABORT ON;
BEGIN TRY
    BEGIN TRANSACTION;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion) VALUES (1, 'C', 10, 'válido');
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion) VALUES (99, 'C', 10, 'cuenta inexistente');
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    SET @Estado = XACT_STATE();
    SET @Error = ERROR_NUMBER();
    INSERT INTO @Observacion VALUES (1, 'error original', CAST(@Error AS VARCHAR(10)));
    INSERT INTO @Observacion VALUES (2, 'XACT_STATE()', CAST(@Estado AS VARCHAR(10)));

    -- Con XACT_STATE() = -1 la transacción no admite COMMIT ni escrituras.
    BEGIN TRY
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        INSERT INTO @Observacion VALUES (3, 'COMMIT sobre transacción condenada', CAST(ERROR_NUMBER() AS VARCHAR(10)));
    END CATCH;

    IF XACT_STATE() = -1
        ROLLBACK TRANSACTION;
    INSERT INTO @Observacion VALUES (4, 'movimientos después del ROLLBACK',
        CAST((SELECT COUNT(*) FROM banco.Movimiento) AS VARCHAR(10)));
END CATCH;
SET XACT_ABORT OFF;

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
