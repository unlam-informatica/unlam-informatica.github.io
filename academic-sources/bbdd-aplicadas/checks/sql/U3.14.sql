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

DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(60), Valor VARCHAR(40));
DECLARE @Versiones INT;

ALTER DATABASE CURRENT SET READ_COMMITTED_SNAPSHOT ON;

INSERT INTO @Observacion
SELECT 1, 'is_read_committed_snapshot_on', CAST(is_read_committed_snapshot_on AS VARCHAR(10))
FROM sys.databases WHERE database_id = DB_ID();
INSERT INTO @Observacion
SELECT 2, 'snapshot_isolation_state_desc', snapshot_isolation_state_desc
FROM sys.databases WHERE database_id = DB_ID();

BEGIN TRANSACTION;                                   -- nivel READ COMMITTED, ya versionado
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;
    SELECT @Versiones = COUNT(*) FROM sys.dm_tran_version_store WHERE database_id = DB_ID();
ROLLBACK TRANSACTION;

INSERT INTO @Observacion VALUES (3, 'versiones de fila tras un UPDATE (>= 1)', IIF(@Versiones >= 1, 'sí', 'no'));

ALTER DATABASE CURRENT SET READ_COMMITTED_SNAPSHOT OFF;
INSERT INTO @Observacion
SELECT 4, 'is_read_committed_snapshot_on tras desactivarla', CAST(is_read_committed_snapshot_on AS VARCHAR(10))
FROM sys.databases WHERE database_id = DB_ID();

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
