-- u3 · XACT_ABORT: estado de una transacción explícita después de distintos errores.
-- En cada caso se inserta una fila válida, se provoca un error dentro de TRY y en el CATCH se
-- registra XACT_STATE(): 1 = la transacción sigue y puede confirmarse; -1 = solo puede revertirse.
CREATE TABLE dbo.Cuenta
(
    CuentaId INT          NOT NULL PRIMARY KEY,
    Saldo    DECIMAL(9,2) NOT NULL CONSTRAINT CK_Cuenta_Saldo CHECK (Saldo >= 0),
    Nivel    TINYINT      NULL,
    Caso     VARCHAR(20)  NOT NULL
);
CREATE TABLE dbo.Observacion
(
    Caso VARCHAR(20), XactAbort VARCHAR(3), Error INT, XactState INT, FilaValidaConfirmada INT
);
GO
CREATE PROCEDURE dbo.Probar
    @Caso VARCHAR(20),
    @XactAbort BIT
AS
BEGIN
    IF @XactAbort = 1 SET XACT_ABORT ON ELSE SET XACT_ABORT OFF;
    BEGIN TRY
        BEGIN TRANSACTION;
        INSERT dbo.Cuenta VALUES (1, 100, NULL, @Caso);
        IF @Caso = 'restriccion' INSERT dbo.Cuenta VALUES (2, -5, NULL, @Caso);
        IF @Caso = 'desbordamiento' INSERT dbo.Cuenta VALUES (2, 100, 300, @Caso);
        IF @Caso = 'conversion' INSERT dbo.Cuenta VALUES (CAST('ocho' AS INT), 100, NULL, @Caso);
        COMMIT;
    END TRY
    BEGIN CATCH
        DECLARE @Estado INT = XACT_STATE(), @Error INT = ERROR_NUMBER();
        IF @Estado = 1 COMMIT;      -- la fila válida se confirma
        IF @Estado = -1 ROLLBACK;   -- transacción condenada: solo se puede revertir
        INSERT dbo.Observacion (Caso, XactAbort, Error, XactState)
        VALUES (@Caso, IIF(@XactAbort = 1, 'ON', 'OFF'), @Error, @Estado);
    END CATCH;
    UPDATE dbo.Observacion
    SET FilaValidaConfirmada = (SELECT COUNT(*) FROM dbo.Cuenta WHERE Caso = @Caso)
    WHERE Caso = @Caso AND XactAbort = IIF(@XactAbort = 1, 'ON', 'OFF');
    DELETE dbo.Cuenta;
END;
GO
EXEC dbo.Probar 'restriccion', 0;
EXEC dbo.Probar 'restriccion', 1;
EXEC dbo.Probar 'desbordamiento', 0;
EXEC dbo.Probar 'desbordamiento', 1;
EXEC dbo.Probar 'conversion', 0;
EXEC dbo.Probar 'conversion', 1;
GO
SELECT Caso, XactAbort, Error, XactState, FilaValidaConfirmada
FROM dbo.Observacion
ORDER BY Caso, XactAbort;
