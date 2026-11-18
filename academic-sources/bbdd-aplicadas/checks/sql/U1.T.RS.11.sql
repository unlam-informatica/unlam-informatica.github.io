-- u1 · repaso: subconsultas en WHERE, FROM y SELECT; correlacionada.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL
);
CREATE TABLE academia.Examen (
    ExamenId INT NOT NULL CONSTRAINT PK_Examen PRIMARY KEY,
    AlumnoId INT NOT NULL CONSTRAINT FK_Examen_Alumno REFERENCES academia.Alumno (AlumnoId),
    Nota     INT NOT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre) VALUES (1, 'Ana'), (2, 'Beto'), (3, 'Cora');
INSERT INTO academia.Examen (ExamenId, AlumnoId, Nota) VALUES
    (1, 1, 9), (2, 1, 7), (3, 2, 4), (4, 2, 6);

-- En WHERE (no correlacionada): alumnos con algún examen de nota mayor a 8.
-- En FROM (tabla derivada): promedio por alumno.
-- En SELECT (correlacionada): mejor nota de cada alumno.
SELECT
    a.Nombre,
    p.Promedio,
    (SELECT MAX(e.Nota) FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId) AS MejorNota,
    CASE WHEN a.AlumnoId IN (SELECT AlumnoId FROM academia.Examen WHERE Nota > 8)
         THEN 'Si' ELSE 'No' END AS TieneMasDeOcho
FROM academia.Alumno AS a
LEFT JOIN (
    SELECT AlumnoId, CAST(AVG(CAST(Nota AS DECIMAL(4,1))) AS DECIMAL(4,1)) AS Promedio
    FROM academia.Examen
    GROUP BY AlumnoId
) AS p ON p.AlumnoId = a.AlumnoId
ORDER BY a.Nombre;
