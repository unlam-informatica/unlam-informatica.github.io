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

DECLARE @Observacion TABLE (Orden INT, Pregunta VARCHAR(60), Respuesta VARCHAR(80));

BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo - 6000 WHERE CuentaId = 3;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion) VALUES (3, 'D', 6000, 'Débito grande');
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    DECLARE @Numero INT = ERROR_NUMBER(), @Estado INT = XACT_STATE(), @Mensaje NVARCHAR(200) = ERROR_MESSAGE();
    INSERT INTO @Observacion VALUES (1, 'ERROR_NUMBER()', CAST(@Numero AS VARCHAR(10)));
    INSERT INTO @Observacion VALUES (2, 'restricción nombrada en el mensaje',
        IIF(@Mensaje LIKE '%CK_Cuenta_Saldo%', 'CK_Cuenta_Saldo', 'otra'));
    INSERT INTO @Observacion VALUES (3, 'XACT_STATE() antes del ROLLBACK', CAST(@Estado AS VARCHAR(10)));
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;
END CATCH;

INSERT INTO @Observacion SELECT 4, 'saldo de la cuenta 3', CAST(Saldo AS VARCHAR(20)) FROM banco.Cuenta WHERE CuentaId = 3;

SELECT Orden, Pregunta, Respuesta FROM @Observacion ORDER BY Orden;
