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

DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(70), Valor VARCHAR(60));
DECLARE @Dato DECIMAL(12,2), @Error INT, @Versiones INT, @Activas INT, @Anidamiento INT;

-- 1) Sin ALLOW_SNAPSHOT_ISOLATION, el primer acceso a datos falla.
SET TRANSACTION ISOLATION LEVEL SNAPSHOT;
BEGIN TRY
    BEGIN TRANSACTION;
    SELECT @Dato = Saldo FROM banco.Cuenta WHERE CuentaId = 1;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    IF XACT_STATE() <> 0 ROLLBACK TRANSACTION;
END CATCH;
INSERT INTO @Observacion VALUES (1, 'SNAPSHOT con la opción en OFF: error', CAST(@Error AS VARCHAR(10)));
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- 2) Se habilita la opción en la base.
ALTER DATABASE CURRENT SET ALLOW_SNAPSHOT_ISOLATION ON;

INSERT INTO @Observacion
SELECT 2, 'snapshot_isolation_state_desc', snapshot_isolation_state_desc
FROM sys.databases WHERE database_id = DB_ID();

-- 3) Ahora la transacción SNAPSHOT funciona y su modificación genera una versión de la fila.
SET TRANSACTION ISOLATION LEVEL SNAPSHOT;
BEGIN TRANSACTION;
    SELECT @Dato = Saldo FROM banco.Cuenta WHERE CuentaId = 1;        -- fija el momento de la instantánea
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;

    SELECT @Activas = COUNT(*) FROM sys.dm_tran_active_snapshot_database_transactions WHERE session_id = @@SPID;
    SELECT @Versiones = COUNT(*) FROM sys.dm_tran_version_store WHERE database_id = DB_ID();
    SET @Anidamiento = @@TRANCOUNT;
COMMIT TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

INSERT INTO @Observacion VALUES (3, 'transacciones SNAPSHOT activas de esta sesión', CAST(@Activas AS VARCHAR(10)));
INSERT INTO @Observacion VALUES (4, 'versiones de fila en el version store (>= 1)', IIF(@Versiones >= 1, 'sí', 'no'));
INSERT INTO @Observacion VALUES (5, 'saldo leído al empezar la transacción', CAST(@Dato AS VARCHAR(20)));

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
