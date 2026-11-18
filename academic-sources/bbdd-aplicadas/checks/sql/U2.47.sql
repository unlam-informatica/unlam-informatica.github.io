-- u2 · Ejercicio U2.47: una transferencia entre tres cuentas que falla a mitad de camino se deshace completa.
CREATE SCHEMA banco;
GO
CREATE TABLE banco.Cuenta (
    CuentaId INT           NOT NULL,
    Saldo    DECIMAL(12,2) NOT NULL,
    CONSTRAINT PK_Cuenta PRIMARY KEY (CuentaId),
    CONSTRAINT CK_Cuenta_Saldo CHECK (Saldo >= 0)
);
INSERT banco.Cuenta (CuentaId, Saldo) VALUES (1, 300), (2, 100), (3, 50);

-- Se reparten 200 desde la cuenta 3, que solo tiene 50: la tercera operación viola el CHECK.
BEGIN TRY
    BEGIN TRANSACTION;
        UPDATE banco.Cuenta SET Saldo = Saldo + 100 WHERE CuentaId = 1;
        UPDATE banco.Cuenta SET Saldo = Saldo + 100 WHERE CuentaId = 2;
        UPDATE banco.Cuenta SET Saldo = Saldo - 200 WHERE CuentaId = 3;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
END CATCH;

SELECT CuentaId, Saldo
FROM banco.Cuenta
ORDER BY CuentaId;
