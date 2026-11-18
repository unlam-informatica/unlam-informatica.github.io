-- u1 · repaso: NOT IN con NULL en la subconsulta frente a NOT EXISTS.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL
);
CREATE TABLE academia.Inscripcion (
    InscripcionId INT NOT NULL CONSTRAINT PK_Inscripcion PRIMARY KEY,
    AlumnoId      INT NULL,
    Materia       VARCHAR(30) NOT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre) VALUES (1, 'Ana'), (2, 'Beto'), (3, 'Cora');
INSERT INTO academia.Inscripcion (InscripcionId, AlumnoId, Materia) VALUES
    (1, 1,    'Bases de Datos'),
    (2, NULL, 'Redes');

SELECT 'NOT IN' AS Forma, COUNT(*) AS AlumnosSinInscripcion
FROM academia.Alumno
WHERE AlumnoId NOT IN (SELECT AlumnoId FROM academia.Inscripcion)
UNION ALL
SELECT 'NOT EXISTS', COUNT(*)
FROM academia.Alumno AS a
WHERE NOT EXISTS (SELECT 1 FROM academia.Inscripcion AS i WHERE i.AlumnoId = a.AlumnoId)
UNION ALL
SELECT 'NOT IN con filtro IS NOT NULL', COUNT(*)
FROM academia.Alumno
WHERE AlumnoId NOT IN (SELECT AlumnoId FROM academia.Inscripcion WHERE AlumnoId IS NOT NULL);
