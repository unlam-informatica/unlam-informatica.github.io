-- u1 · repaso: SCHEMABINDING impide cambios que romperían la vista.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Curso (
    CursoId    INT NOT NULL CONSTRAINT PK_Curso PRIMARY KEY,
    Catedra    VARCHAR(30) NOT NULL,
    Inscriptos INT NOT NULL,
    Puntuacion INT NOT NULL
);
INSERT INTO academia.Curso VALUES (1, 'Bases de Datos', 40, 4), (2, 'Bases de Datos', 60, 5), (3, 'Redes', 30, 2);
GO
CREATE OR ALTER VIEW academia.CursoDestacado
WITH SCHEMABINDING
AS
    SELECT Catedra, SUM(Inscriptos) AS TotalInscriptos, COUNT_BIG(*) AS Cursos
    FROM academia.Curso
    WHERE Puntuacion > 3
    GROUP BY Catedra;
GO
DECLARE @ErrorAlter INT = 0, @ErrorDrop INT = 0;
BEGIN TRY
    ALTER TABLE academia.Curso DROP COLUMN Inscriptos;
END TRY
BEGIN CATCH
    SET @ErrorAlter = ERROR_NUMBER();
END CATCH;
BEGIN TRY
    DROP TABLE academia.Curso;
END TRY
BEGIN CATCH
    SET @ErrorDrop = ERROR_NUMBER();
END CATCH;

SELECT Catedra, TotalInscriptos, @ErrorAlter AS ErrorAlterColumna, @ErrorDrop AS ErrorDropTabla
FROM academia.CursoDestacado;
