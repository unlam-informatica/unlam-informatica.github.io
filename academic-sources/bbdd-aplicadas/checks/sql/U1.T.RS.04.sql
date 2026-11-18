-- u1 · repaso: FK compuesta hacia una PK compuesta, con borrado en cascada.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Comision (
    MateriaId   INT NOT NULL,
    ComisionNro INT NOT NULL,
    Turno       VARCHAR(10) NOT NULL,
    CONSTRAINT PK_Comision PRIMARY KEY (MateriaId, ComisionNro)
);

CREATE TABLE academia.Examen (
    ExamenId    INT IDENTITY(1, 1) NOT NULL,
    MateriaId   INT NOT NULL,
    ComisionNro INT NOT NULL,
    Nota        TINYINT NOT NULL,
    CONSTRAINT PK_Examen PRIMARY KEY (ExamenId),
    CONSTRAINT FK_Examen_Comision
        FOREIGN KEY (MateriaId, ComisionNro)
        REFERENCES academia.Comision (MateriaId, ComisionNro)
        ON DELETE CASCADE
);

INSERT INTO academia.Comision (MateriaId, ComisionNro, Turno)
VALUES (1, 1, 'Mañana'), (1, 2, 'Noche');
INSERT INTO academia.Examen (MateriaId, ComisionNro, Nota)
VALUES (1, 1, 7), (1, 1, 9), (1, 2, 6);

DECLARE @Error INT = 0;
BEGIN TRY
    INSERT INTO academia.Examen (MateriaId, ComisionNro, Nota) VALUES (1, 3, 8);
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

DELETE FROM academia.Comision WHERE MateriaId = 1 AND ComisionNro = 1;

SELECT
    @Error                                  AS ErrorComisionInexistente,
    (SELECT COUNT(*) FROM academia.Comision) AS Comisiones,
    (SELECT COUNT(*) FROM academia.Examen)   AS Examenes;
