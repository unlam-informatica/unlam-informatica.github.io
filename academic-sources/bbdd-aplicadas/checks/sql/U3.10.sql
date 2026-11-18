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
CREATE OR ALTER PROCEDURE banco.AcreditarConMovimiento
    @CuentaId INT,
    @Monto    DECIMAL(12, 2)
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @AnidamientoInicial INT = @@TRANCOUNT;

    IF @AnidamientoInicial = 0
        BEGIN TRANSACTION;                       -- el procedimiento es dueño de la transacción
    ELSE
        SAVE TRANSACTION AcreditarConMovimiento; -- participa de la del llamador

    BEGIN TRY
        UPDATE banco.Cuenta SET Saldo = Saldo + @Monto WHERE CuentaId = @CuentaId;
        INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion)
        VALUES (@CuentaId, 'C', @Monto, 'Acreditación');

        IF @AnidamientoInicial = 0
            COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() = -1
            ROLLBACK TRANSACTION;                -- condenada: solo se puede revertir todo
        ELSE IF @AnidamientoInicial = 0
            ROLLBACK TRANSACTION;
        ELSE
            ROLLBACK TRANSACTION AcreditarConMovimiento;  -- deshace solo lo del procedimiento
        THROW;
    END CATCH;
END;
GO
DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(70), Valor VARCHAR(40));

-- 1) Llamada suelta con un monto inválido (el INSERT viola CK_Movimiento_Monto).
BEGIN TRY
    EXEC banco.AcreditarConMovimiento @CuentaId = 1, @Monto = -50;
END TRY
BEGIN CATCH
    INSERT INTO @Observacion VALUES (1, 'llamada suelta: error', CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;
INSERT INTO @Observacion SELECT 2, 'llamada suelta: saldo de la cuenta 1', CAST(Saldo AS VARCHAR(40))
    FROM banco.Cuenta WHERE CuentaId = 1;

-- 2) Llamada dentro de una transacción mayor.
BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;
    BEGIN TRY
        EXEC banco.AcreditarConMovimiento @CuentaId = 1, @Monto = -50;
    END TRY
    BEGIN CATCH
        INSERT INTO @Observacion VALUES (3, 'dentro de la transacción: error', CAST(ERROR_NUMBER() AS VARCHAR(10)));
    END CATCH;
    DECLARE @Estado INT = XACT_STATE();
    INSERT INTO @Observacion VALUES (4, 'XACT_STATE() de la transacción del llamador', CAST(@Estado AS VARCHAR(10)));
    EXEC banco.AcreditarConMovimiento @CuentaId = 1, @Monto = 25;
COMMIT TRANSACTION;

INSERT INTO @Observacion SELECT 5, 'saldo final de la cuenta 1', CAST(Saldo AS VARCHAR(40))
    FROM banco.Cuenta WHERE CuentaId = 1;
INSERT INTO @Observacion SELECT 6, 'movimientos registrados', CAST(COUNT(*) AS VARCHAR(40)) FROM banco.Movimiento;

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
