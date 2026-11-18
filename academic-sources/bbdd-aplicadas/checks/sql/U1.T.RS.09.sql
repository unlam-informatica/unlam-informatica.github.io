-- u1 · repaso: INNER JOIN, LEFT JOIN y anti-join.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL
);
CREATE TABLE academia.Inscripcion (
    InscripcionId INT NOT NULL CONSTRAINT PK_Inscripcion PRIMARY KEY,
    AlumnoId      INT NOT NULL CONSTRAINT FK_Inscripcion_Alumno REFERENCES academia.Alumno (AlumnoId),
    Materia       VARCHAR(30) NOT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre) VALUES (1, 'Ana'), (2, 'Beto'), (3, 'Cora');
INSERT INTO academia.Inscripcion (InscripcionId, AlumnoId, Materia) VALUES
    (1, 1, 'Bases de Datos'), (2, 1, 'Redes'), (3, 2, 'Bases de Datos');

SELECT a.Nombre, i.Materia, 'INNER' AS Tipo
FROM academia.Alumno AS a
INNER JOIN academia.Inscripcion AS i ON i.AlumnoId = a.AlumnoId
UNION ALL
SELECT a.Nombre, ISNULL(i.Materia, '(sin materia)'), 'LEFT'
FROM academia.Alumno AS a
LEFT JOIN academia.Inscripcion AS i ON i.AlumnoId = a.AlumnoId
WHERE a.AlumnoId = 3
UNION ALL
SELECT a.Nombre, '(anti-join)', 'ANTI'
FROM academia.Alumno AS a
LEFT JOIN academia.Inscripcion AS i ON i.AlumnoId = a.AlumnoId
WHERE i.AlumnoId IS NULL
ORDER BY Tipo, Nombre, Materia;
