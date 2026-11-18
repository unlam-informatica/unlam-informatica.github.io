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

DECLARE @Observacion TABLE (Orden INT, Parametro VARCHAR(60), Valor VARCHAR(20));
DECLARE @PorDefecto INT = @@LOCK_TIMEOUT, @Configurado INT, @Prioridad INT;

SET LOCK_TIMEOUT 5000;
SET @Configurado = @@LOCK_TIMEOUT;

SET DEADLOCK_PRIORITY LOW;
SELECT @Prioridad = deadlock_priority FROM sys.dm_exec_sessions WHERE session_id = @@SPID;

INSERT INTO @Observacion VALUES (1, '@@LOCK_TIMEOUT por defecto', CAST(@PorDefecto AS VARCHAR(20)));
INSERT INTO @Observacion VALUES (2, '@@LOCK_TIMEOUT tras SET LOCK_TIMEOUT 5000', CAST(@Configurado AS VARCHAR(20)));
INSERT INTO @Observacion VALUES (3, 'deadlock_priority tras SET ... LOW', CAST(@Prioridad AS VARCHAR(20)));

SET DEADLOCK_PRIORITY HIGH;
SELECT @Prioridad = deadlock_priority FROM sys.dm_exec_sessions WHERE session_id = @@SPID;
INSERT INTO @Observacion VALUES (4, 'deadlock_priority tras SET ... HIGH', CAST(@Prioridad AS VARCHAR(20)));

SET DEADLOCK_PRIORITY NORMAL;
SET LOCK_TIMEOUT -1;

SELECT Orden, Parametro, Valor FROM @Observacion ORDER BY Orden;
