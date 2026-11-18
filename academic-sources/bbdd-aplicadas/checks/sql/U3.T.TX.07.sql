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

DECLARE @EstadoInicial INT = XACT_STATE();   -- se lee en una variable: dentro de un INSERT ya hay una transacción
INSERT INTO @Observacion VALUES (1, 'XACT_STATE() sin transacción', CAST(@EstadoInicial AS VARCHAR(10)));

BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo - 6000 WHERE CuentaId = 3;   -- viola CK_Cuenta_Saldo
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion) VALUES (3, 'D', 6000, 'Débito grande');
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    DECLARE @Estado INT = XACT_STATE(), @Error INT = ERROR_NUMBER(), @Severidad INT = ERROR_SEVERITY(),
            @Anidamiento INT = @@TRANCOUNT;
    INSERT INTO @Observacion VALUES (2, 'ERROR_NUMBER()', CAST(@Error AS VARCHAR(10)));
    INSERT INTO @Observacion VALUES (3, 'ERROR_SEVERITY()', CAST(@Severidad AS VARCHAR(10)));
    INSERT INTO @Observacion VALUES (4, 'XACT_STATE() dentro del CATCH', CAST(@Estado AS VARCHAR(10)));
    INSERT INTO @Observacion VALUES (5, '@@TRANCOUNT dentro del CATCH', CAST(@Anidamiento AS VARCHAR(10)));
    IF @Estado <> 0
        ROLLBACK TRANSACTION;
END CATCH;

INSERT INTO @Observacion VALUES (6, '@@TRANCOUNT al final', CAST(@@TRANCOUNT AS VARCHAR(10)));
INSERT INTO @Observacion SELECT 7, 'saldo de la cuenta 3', CAST(Saldo AS VARCHAR(20)) FROM banco.Cuenta WHERE CuentaId = 3;
INSERT INTO @Observacion SELECT 8, 'movimientos registrados', CAST(COUNT(*) AS VARCHAR(10)) FROM banco.Movimiento;

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
