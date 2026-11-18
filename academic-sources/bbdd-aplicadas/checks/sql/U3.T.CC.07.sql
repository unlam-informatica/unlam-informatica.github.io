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
CREATE OR ALTER PROCEDURE banco.AcreditarConReintento
    @CuentaId INT,
    @Monto    DECIMAL(12, 2),
    @Intentos INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;
    DECLARE @Maximo INT = 3;
    SET @Intentos = 0;

    WHILE @Intentos < @Maximo
    BEGIN
        SET @Intentos += 1;
        BEGIN TRY
            BEGIN TRANSACTION;
                UPDATE banco.Cuenta SET Saldo = Saldo + @Monto WHERE CuentaId = @CuentaId;
            COMMIT TRANSACTION;
            RETURN;                                   -- terminó bien
        END TRY
        BEGIN CATCH
            IF XACT_STATE() <> 0
                ROLLBACK TRANSACTION;

            IF ERROR_NUMBER() = 1205 AND @Intentos < @Maximo   -- fue víctima de un deadlock
                WAITFOR DELAY '00:00:00.100';             -- pausa breve y reintento
            ELSE
                THROW;                                    -- otro error, o se agotaron los intentos
        END CATCH;
    END;
END;
GO
DECLARE @Intentos INT;
EXEC banco.AcreditarConReintento @CuentaId = 1, @Monto = 10, @Intentos = @Intentos OUTPUT;

SELECT @Intentos AS Intentos, Saldo FROM banco.Cuenta WHERE CuentaId = 1;
