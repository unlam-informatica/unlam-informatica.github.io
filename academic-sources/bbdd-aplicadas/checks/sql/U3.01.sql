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

BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo - 700 WHERE CuentaId = 2;
    UPDATE banco.Cuenta SET Saldo = Saldo + 700 WHERE CuentaId = 3;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion)
    VALUES (2, 'D', 700, 'Transferencia a cuenta 3'),
           (3, 'C', 700, 'Transferencia de cuenta 2');
COMMIT TRANSACTION;

SELECT c.CuentaId, c.Saldo, COUNT(m.MovimientoId) AS Movimientos
FROM banco.Cuenta AS c
LEFT JOIN banco.Movimiento AS m ON m.CuentaId = c.CuentaId
GROUP BY c.CuentaId, c.Saldo
ORDER BY c.CuentaId;
