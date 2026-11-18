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
CREATE OR ALTER FUNCTION banco.NivelActual()
RETURNS VARCHAR(20)
AS
BEGIN
    RETURN (SELECT CASE transaction_isolation_level
                       WHEN 1 THEN 'READ UNCOMMITTED' WHEN 2 THEN 'READ COMMITTED'
                       WHEN 3 THEN 'REPEATABLE READ'  WHEN 4 THEN 'SERIALIZABLE'
                       WHEN 5 THEN 'SNAPSHOT'
                   END
            FROM sys.dm_exec_sessions
            WHERE session_id = @@SPID);
END;
GO
CREATE OR ALTER PROCEDURE banco.ContarEnSerializable
    @Nivel VARCHAR(20) OUTPUT
AS
BEGIN
    SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
    SET @Nivel = banco.NivelActual();
END;
GO
DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(50), Nivel VARCHAR(20));
DECLARE @Dentro VARCHAR(20), @Antes VARCHAR(20), @Despues VARCHAR(20);

SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET @Antes = banco.NivelActual();
EXEC banco.ContarEnSerializable @Nivel = @Dentro OUTPUT;
SET @Despues = banco.NivelActual();
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

INSERT INTO @Observacion VALUES (1, 'en el lote, antes de llamar', @Antes);
INSERT INTO @Observacion VALUES (2, 'dentro del procedimiento', @Dentro);
INSERT INTO @Observacion VALUES (3, 'en el lote, después de la llamada', @Despues);

SELECT Orden, Momento, Nivel FROM @Observacion ORDER BY Orden;
