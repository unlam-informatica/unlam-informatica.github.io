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

DECLARE @Candado TABLE (Orden INT, Escenario VARCHAR(30), Recurso VARCHAR(20), Modo VARCHAR(10), Cantidad INT);
DECLARE @Total DECIMAL(12,2);

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Sin índice sobre Saldo: el predicado recorre toda la tabla.
BEGIN TRANSACTION;
    SELECT @Total = SUM(Saldo) FROM banco.Cuenta WHERE Saldo BETWEEN 1000 AND 4000;
    INSERT INTO @Candado
    SELECT 1, 'sin índice sobre Saldo', resource_type, request_mode, COUNT(*) FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type NOT IN ('DATABASE', 'METADATA')
    GROUP BY resource_type, request_mode;
COMMIT TRANSACTION;

CREATE INDEX IX_Cuenta_Saldo ON banco.Cuenta (Saldo);

-- Con índice: se bloquea solo el rango del índice.
BEGIN TRANSACTION;
    SELECT @Total = SUM(Saldo) FROM banco.Cuenta WHERE Saldo BETWEEN 1000 AND 4000;
    INSERT INTO @Candado
    SELECT 2, 'con IX_Cuenta_Saldo', resource_type, request_mode, COUNT(*) FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type NOT IN ('DATABASE', 'METADATA')
    GROUP BY resource_type, request_mode;
COMMIT TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

SELECT Escenario, Recurso, Modo, Cantidad FROM @Candado ORDER BY Orden, Recurso, Modo;
