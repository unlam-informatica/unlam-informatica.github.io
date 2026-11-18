-- u1 · repaso: trigger AFTER UPDATE con inserted y deleted (varias filas).
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Examen (
    ExamenId INT NOT NULL CONSTRAINT PK_Examen PRIMARY KEY,
    Alumno   VARCHAR(30) NOT NULL,
    Nota     INT NOT NULL
);
CREATE TABLE academia.ExamenAuditoria (
    AuditoriaId  INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_ExamenAuditoria PRIMARY KEY,
    ExamenId     INT NOT NULL,
    NotaAnterior INT NOT NULL,
    NotaNueva    INT NOT NULL,
    Fecha        DATETIME2(0) NOT NULL CONSTRAINT DF_ExamenAuditoria_Fecha DEFAULT (SYSDATETIME())
);
INSERT INTO academia.Examen (ExamenId, Alumno, Nota) VALUES (1, 'Ana', 6), (2, 'Beto', 4), (3, 'Cora', 8);
GO
CREATE OR ALTER TRIGGER academia.TrgExamenAuditoria
ON academia.Examen
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO academia.ExamenAuditoria (ExamenId, NotaAnterior, NotaNueva)
    SELECT i.ExamenId, d.Nota, i.Nota
    FROM inserted AS i
    INNER JOIN deleted AS d ON d.ExamenId = i.ExamenId
    WHERE i.Nota <> d.Nota;
END;
GO
UPDATE academia.Examen SET Nota = Nota + 1 WHERE ExamenId IN (1, 2);
UPDATE academia.Examen SET Alumno = 'Cora M.' WHERE ExamenId = 3;   -- no cambia la nota

SELECT ExamenId, NotaAnterior, NotaNueva
FROM academia.ExamenAuditoria
ORDER BY ExamenId;
