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

-- Se agrega una columna de versión de fila para detectar la modificación concurrente.
ALTER TABLE banco.Cuenta ADD Version ROWVERSION;
GO
DECLARE @Observacion TABLE (Orden INT, Paso VARCHAR(70), Valor VARCHAR(40));
DECLARE @SaldoLeidoA DECIMAL(12,2), @VersionA BINARY(8), @Filas INT;

-- El cajero A lee el saldo y la versión.
SELECT @SaldoLeidoA = Saldo, @VersionA = Version FROM banco.Cuenta WHERE CuentaId = 1;

-- Mientras tanto el cajero B retira 4000 y confirma (otra "sesión", simulada con una sentencia propia).
UPDATE banco.Cuenta SET Saldo = Saldo - 4000 WHERE CuentaId = 1;

-- El cajero A intenta retirar 700 a partir de lo que leyó: la condición sobre la versión falla.
UPDATE banco.Cuenta SET Saldo = @SaldoLeidoA - 700
WHERE CuentaId = 1 AND Version = @VersionA;
SET @Filas = @@ROWCOUNT;

INSERT INTO @Observacion VALUES (1, 'saldo que leyó A', CAST(@SaldoLeidoA AS VARCHAR(20)));
INSERT INTO @Observacion VALUES (2, 'filas modificadas por la actualización de A', CAST(@Filas AS VARCHAR(10)));
INSERT INTO @Observacion SELECT 3, 'saldo final en la tabla', CAST(Saldo AS VARCHAR(20)) FROM banco.Cuenta WHERE CuentaId = 1;

SELECT Orden, Paso, Valor FROM @Observacion ORDER BY Orden;
