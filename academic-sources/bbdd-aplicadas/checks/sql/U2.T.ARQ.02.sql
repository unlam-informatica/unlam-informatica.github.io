-- u2 · Transacción: COMMIT confirma las dos operaciones; el error en la segunda deshace también la primera.
CREATE SCHEMA banco;
GO
CREATE TABLE banco.Cuenta (
    CuentaId INT           NOT NULL,
    Titular  VARCHAR(40)   NOT NULL,
    Saldo    DECIMAL(12,2) NOT NULL,
    CONSTRAINT PK_Cuenta PRIMARY KEY (CuentaId),
    CONSTRAINT CK_Cuenta_Saldo CHECK (Saldo >= 0)
);
INSERT banco.Cuenta (CuentaId, Titular, Saldo)
VALUES (1, 'Cuenta de prueba A', 1000), (2, 'Cuenta de prueba B', 200);

-- Transferencia de 500 de A hacia B: las dos operaciones se confirman juntas.
BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo - 500 WHERE CuentaId = 1;
    UPDATE banco.Cuenta SET Saldo = Saldo + 500 WHERE CuentaId = 2;
COMMIT TRANSACTION;

-- Transferencia de 900 de B hacia A: B queda sin fondos y el CHECK rechaza la segunda operación.
BEGIN TRY
    BEGIN TRANSACTION;
        UPDATE banco.Cuenta SET Saldo = Saldo + 900 WHERE CuentaId = 1;
        UPDATE banco.Cuenta SET Saldo = Saldo - 900 WHERE CuentaId = 2;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
END CATCH;

SELECT CuentaId, Titular, Saldo
FROM banco.Cuenta
ORDER BY CuentaId;
