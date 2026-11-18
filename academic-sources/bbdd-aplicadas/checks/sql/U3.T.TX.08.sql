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
CREATE OR ALTER PROCEDURE banco.TransferirSaldo
    @Origen  INT,
    @Destino INT,
    @Monto   DECIMAL(12, 2)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    IF @Monto <= 0
        THROW 50001, 'El monto debe ser mayor que cero.', 1;

    BEGIN TRY
        BEGIN TRANSACTION;

        IF NOT EXISTS (SELECT 1 FROM banco.Cuenta WHERE CuentaId = @Destino)
            THROW 50002, 'La cuenta destino no existe.', 1;

        IF (SELECT Saldo FROM banco.Cuenta WITH (UPDLOCK) WHERE CuentaId = @Origen) < @Monto
            THROW 50003, 'Saldo insuficiente en la cuenta origen.', 1;

        UPDATE banco.Cuenta SET Saldo = Saldo - @Monto WHERE CuentaId = @Origen;
        UPDATE banco.Cuenta SET Saldo = Saldo + @Monto WHERE CuentaId = @Destino;

        INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion)
        VALUES (@Origen, 'D', @Monto, CONCAT('Transferencia a cuenta ', @Destino)),
               (@Destino, 'C', @Monto, CONCAT('Transferencia de cuenta ', @Origen));

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0
            ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
GO
DROP TABLE IF EXISTS banco.Resultado;
GO
CREATE TABLE banco.Resultado (Orden INT, Llamada VARCHAR(40), Error INT, Trancount INT);
GO
CREATE OR ALTER PROCEDURE banco.Probar @Orden INT, @Llamada VARCHAR(40), @Origen INT, @Destino INT, @Monto DECIMAL(12, 2)
AS
BEGIN
    DECLARE @Error INT = 0, @Anidamiento INT;
    BEGIN TRY
        EXEC banco.TransferirSaldo @Origen, @Destino, @Monto;
    END TRY
    BEGIN CATCH
        SET @Error = ERROR_NUMBER();
    END CATCH;
    SET @Anidamiento = @@TRANCOUNT;   -- se lee antes del INSERT
    INSERT INTO banco.Resultado VALUES (@Orden, @Llamada, @Error, @Anidamiento);
END;
GO
EXEC banco.Probar 1, 'cuenta 1 a 2, 200',      1, 2, 200;
EXEC banco.Probar 2, 'cuenta 3 a 1, 5000',     3, 1, 5000;
EXEC banco.Probar 3, 'cuenta 1 a 99, 100',     1, 99, 100;
EXEC banco.Probar 4, 'cuenta 1 a 2, monto -50', 1, 2, -50;

SELECT Orden, Llamada, Error, Trancount FROM banco.Resultado ORDER BY Orden;

SELECT CuentaId, Saldo FROM banco.Cuenta ORDER BY CuentaId;

SELECT COUNT(*) AS Movimientos FROM banco.Movimiento;
