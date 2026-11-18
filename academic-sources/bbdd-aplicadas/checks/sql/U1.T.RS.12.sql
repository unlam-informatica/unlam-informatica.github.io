-- u1 · repaso: EXISTS, NOT EXISTS, ANY y ALL.
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

SELECT 'EXISTS' AS Consulta, a.Nombre
FROM academia.Alumno AS a
WHERE EXISTS (SELECT 1 FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId)
UNION ALL
SELECT 'NOT EXISTS', a.Nombre
FROM academia.Alumno AS a
WHERE NOT EXISTS (SELECT 1 FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId)
UNION ALL
SELECT 'ANY (algun examen mayor a 8)', a.Nombre
FROM academia.Alumno AS a
WHERE 8 < ANY (SELECT e.Nota FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId)
UNION ALL
SELECT 'ALL (todos los examenes menores a 7)', a.Nombre
FROM academia.Alumno AS a
WHERE 7 > ALL (SELECT e.Nota FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId)
ORDER BY Consulta, Nombre;
