-- u1 · repaso: funciones escalar, de tabla inline y de tabla multi-statement.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId        INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre          VARCHAR(30) NOT NULL,
    FechaNacimiento DATE NOT NULL
);
CREATE TABLE academia.Examen (
    ExamenId INT NOT NULL CONSTRAINT PK_Examen PRIMARY KEY,
    AlumnoId INT NOT NULL CONSTRAINT FK_Examen_Alumno REFERENCES academia.Alumno (AlumnoId),
    Nota     INT NOT NULL
);
INSERT INTO academia.Alumno VALUES (1, 'Ana', '2000-05-20'), (2, 'Beto', '1999-12-31');
INSERT INTO academia.Examen VALUES (1, 1, 9), (2, 1, 7), (3, 2, 4);
GO
-- Escalar
CREATE OR ALTER FUNCTION academia.ObtenerEdad (@FechaNacimiento DATE, @FechaReferencia DATE)
RETURNS INT
AS
BEGIN
    RETURN DATEDIFF(YEAR, @FechaNacimiento, @FechaReferencia)
         - CASE WHEN MONTH(@FechaNacimiento) * 100 + DAY(@FechaNacimiento)
                     > MONTH(@FechaReferencia) * 100 + DAY(@FechaReferencia)
                THEN 1 ELSE 0 END;
END;
GO
-- De tabla inline: un único SELECT
CREATE OR ALTER FUNCTION academia.ExamenPorAlumno (@AlumnoId INT)
RETURNS TABLE
AS
RETURN
    SELECT ExamenId, Nota
    FROM academia.Examen
    WHERE AlumnoId = @AlumnoId;
GO
-- De tabla multi-statement: declara la tabla de retorno y la llena con varias sentencias
CREATE OR ALTER FUNCTION academia.ResumenAlumno (@AlumnoId INT)
RETURNS @Resumen TABLE (Nombre VARCHAR(30), Examenes INT, Promedio DECIMAL(4,1))
AS
BEGIN
    INSERT INTO @Resumen (Nombre, Examenes, Promedio)
    SELECT a.Nombre, COUNT(e.ExamenId), CAST(AVG(CAST(e.Nota AS DECIMAL(4,1))) AS DECIMAL(4,1))
    FROM academia.Alumno AS a
    LEFT JOIN academia.Examen AS e ON e.AlumnoId = a.AlumnoId
    WHERE a.AlumnoId = @AlumnoId
    GROUP BY a.Nombre;
    RETURN;
END;
GO
SELECT
    a.Nombre,
    academia.ObtenerEdad(a.FechaNacimiento, '2026-03-01') AS Edad,
    r.Examenes,
    r.Promedio,
    (SELECT MAX(x.Nota) FROM academia.ExamenPorAlumno(a.AlumnoId) AS x) AS MejorNota
FROM academia.Alumno AS a
CROSS APPLY academia.ResumenAlumno(a.AlumnoId) AS r
ORDER BY a.Nombre;
