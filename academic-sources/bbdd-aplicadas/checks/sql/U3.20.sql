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

DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(50), Valor VARCHAR(80));
DECLARE @Anidamiento INT, @Error INT, @Mensaje NVARCHAR(200);

BEGIN TRY
    BEGIN DISTRIBUTED TRANSACTION TransferenciaEntreNodos;
    SET @Anidamiento = @@TRANCOUNT;
    INSERT INTO @Observacion VALUES (1, '@@TRANCOUNT tras BEGIN DISTRIBUTED', CAST(@Anidamiento AS VARCHAR(10)));
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;
    COMMIT TRANSACTION;
    INSERT INTO @Observacion VALUES (2, 'COMMIT', 'confirmada');
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    SET @Mensaje = ERROR_MESSAGE();
    IF XACT_STATE() <> 0 ROLLBACK TRANSACTION;
    INSERT INTO @Observacion VALUES (3, 'error', CAST(@Error AS VARCHAR(10)));
    INSERT INTO @Observacion VALUES (4, 'mensaje', LEFT(@Mensaje, 80));
END CATCH;

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
