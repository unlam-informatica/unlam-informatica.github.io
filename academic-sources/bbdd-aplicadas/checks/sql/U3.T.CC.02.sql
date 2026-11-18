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

DECLARE @Candado TABLE (Orden INT, Nivel VARCHAR(20), Recurso VARCHAR(20), Modo VARCHAR(10), Cantidad INT);
DECLARE @Total DECIMAL(12,2);

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRANSACTION;
    SELECT @Total = SUM(Saldo) FROM banco.Cuenta WHERE CuentaId BETWEEN 1 AND 2;
    INSERT INTO @Candado
    SELECT 1, 'READ COMMITTED', resource_type, request_mode, COUNT(*) FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type <> 'DATABASE'
    GROUP BY resource_type, request_mode;
COMMIT TRANSACTION;

SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRANSACTION;
    SELECT @Total = SUM(Saldo) FROM banco.Cuenta WHERE CuentaId BETWEEN 1 AND 2;
    INSERT INTO @Candado
    SELECT 2, 'REPEATABLE READ', resource_type, request_mode, COUNT(*) FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type <> 'DATABASE'
    GROUP BY resource_type, request_mode;
COMMIT TRANSACTION;

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
    SELECT @Total = SUM(Saldo) FROM banco.Cuenta WHERE CuentaId BETWEEN 1 AND 2;
    INSERT INTO @Candado
    SELECT 3, 'SERIALIZABLE', resource_type, request_mode, COUNT(*) FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type <> 'DATABASE'
    GROUP BY resource_type, request_mode;
COMMIT TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

IF NOT EXISTS (SELECT 1 FROM @Candado WHERE Orden = 1)
    INSERT INTO @Candado VALUES (1, 'READ COMMITTED', '(ninguno)', '', 0);

SELECT Nivel, Recurso, Modo, Cantidad FROM @Candado ORDER BY Orden, Recurso, Modo;
