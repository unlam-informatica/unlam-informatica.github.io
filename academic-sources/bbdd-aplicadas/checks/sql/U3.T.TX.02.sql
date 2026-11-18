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

-- Autocommit: cada sentencia es su propia transacción.
DECLARE @Observacion TABLE (Orden INT, Paso VARCHAR(50), Trancount INT, ImplicitasActivas VARCHAR(3));

UPDATE banco.Cuenta SET Saldo = Saldo + 10 WHERE CuentaId = 1;
INSERT INTO @Observacion VALUES (1, 'después de un UPDATE en autocommit', @@TRANCOUNT,
    IIF(@@OPTIONS & 2 = 2, 'ON', 'OFF'));

-- Modo implícito: hasta un SELECT sobre una tabla abre la transacción.
SET IMPLICIT_TRANSACTIONS ON;
DECLARE @Filas INT, @Dentro INT, @Opcion VARCHAR(3);
SELECT @Filas = COUNT(*) FROM banco.Cuenta;
SET @Dentro = @@TRANCOUNT;
SET @Opcion = IIF(@@OPTIONS & 2 = 2, 'ON', 'OFF');
COMMIT TRANSACTION;
DECLARE @Despues INT = @@TRANCOUNT;
SET IMPLICIT_TRANSACTIONS OFF;

INSERT INTO @Observacion VALUES (2, 'después de un SELECT con IMPLICIT_TRANSACTIONS ON', @Dentro, @Opcion);
INSERT INTO @Observacion VALUES (3, 'después del COMMIT', @Despues, 'ON');
INSERT INTO @Observacion VALUES (4, 'con IMPLICIT_TRANSACTIONS OFF', @@TRANCOUNT, IIF(@@OPTIONS & 2 = 2, 'ON', 'OFF'));

SELECT Orden, Paso, Trancount, ImplicitasActivas FROM @Observacion ORDER BY Orden;
