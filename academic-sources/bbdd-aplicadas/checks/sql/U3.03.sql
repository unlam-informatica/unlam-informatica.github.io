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

DECLARE @Observacion TABLE (Orden INT, Instruccion VARCHAR(30), Trancount INT);
DECLARE @N INT;

SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (1, 'al empezar', @N);
BEGIN TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (2, 'BEGIN TRANSACTION', @N);
BEGIN TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (3, 'BEGIN TRANSACTION', @N);
BEGIN TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (4, 'BEGIN TRANSACTION', @N);
COMMIT TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (5, 'COMMIT TRANSACTION', @N);
ROLLBACK TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (6, 'ROLLBACK TRANSACTION', @N);

SELECT Orden, Instruccion, Trancount FROM @Observacion ORDER BY Orden;
