-- u1 · repaso: agregados, DISTINCT, WHERE frente a HAVING.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Curso (
    CursoId      INT NOT NULL CONSTRAINT PK_Curso PRIMARY KEY,
    Catedra      VARCHAR(30) NOT NULL,
    Turno        VARCHAR(10) NOT NULL,
    Inscriptos   INT NULL,
    Puntuacion   INT NOT NULL
);
INSERT INTO academia.Curso (CursoId, Catedra, Turno, Inscriptos, Puntuacion) VALUES
    (1, 'Bases de Datos', 'Mañana', 40, 4),
    (2, 'Bases de Datos', 'Noche',  60, 5),
    (3, 'Redes',          'Noche',  30, 2),
    (4, 'Redes',          'Mañana', NULL, 4),
    (5, 'Sistemas',       'Mañana', 50, 5);

SELECT
    Catedra,
    COUNT(*)                AS Cursos,
    COUNT(Inscriptos)       AS ConDato,
    COUNT(DISTINCT Turno)   AS Turnos,
    SUM(Inscriptos)         AS TotalInscriptos,
    AVG(Inscriptos)         AS Promedio
FROM academia.Curso
WHERE Puntuacion > 3
GROUP BY Catedra
HAVING SUM(Inscriptos) > 40
ORDER BY Catedra;
