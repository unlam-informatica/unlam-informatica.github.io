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

DECLARE @Observacion TABLE (Orden INT, Variante VARCHAR(70), Detalle VARCHAR(80));
DECLARE @Salto BIT = 0;

-- Variante original: el CHECK falla antes del IF, así que el ROLLBACK TO nunca se ejecuta.
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo - 200 WHERE CuentaId = 1;
    SAVE TRANSACTION AntesDeB;
    UPDATE banco.Cuenta SET Saldo = Saldo - 9999 WHERE CuentaId = 1;   -- error 547: no hay IF que lo vea
    IF (SELECT Saldo FROM banco.Cuenta WHERE CuentaId = 1) < 0
    BEGIN
        SET @Salto = 1;
        ROLLBACK TRANSACTION AntesDeB;
    END;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    DECLARE @Error INT = ERROR_NUMBER(), @Estado INT = XACT_STATE();
    INSERT INTO @Observacion VALUES (1, 'sin XACT_ABORT: ¿se ejecutó el ROLLBACK TO?', IIF(@Salto = 1, 'sí', 'no'));
    INSERT INTO @Observacion VALUES (2, 'sin XACT_ABORT: error y XACT_STATE()', CONCAT(@Error, ' / ', @Estado));
    -- XACT_STATE() = 1: se puede volver al savepoint y confirmar lo anterior.
    IF @Estado = 1
    BEGIN
        ROLLBACK TRANSACTION AntesDeB;
        COMMIT TRANSACTION;
    END;
END CATCH;

INSERT INTO @Observacion SELECT 3, 'saldo de la cuenta 1 tras la variante corregida', CAST(Saldo AS VARCHAR(20))
    FROM banco.Cuenta WHERE CuentaId = 1;

SELECT Orden, Variante, Detalle FROM @Observacion ORDER BY Orden;
