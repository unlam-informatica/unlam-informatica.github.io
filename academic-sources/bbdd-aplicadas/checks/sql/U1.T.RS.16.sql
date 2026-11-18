-- u1 · repaso: procedimiento almacenado con parámetro OUTPUT, coherente con las tablas del repaso.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL
);
CREATE TABLE academia.Materia (
    MateriaId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Materia PRIMARY KEY,
    Nombre    VARCHAR(100) NOT NULL,
    Codigo    VARCHAR(20)  NOT NULL
);
CREATE TABLE academia.Inscripcion (
    InscripcionId    INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Inscripcion PRIMARY KEY,
    AlumnoId         INT  NOT NULL CONSTRAINT FK_Inscripcion_Alumno REFERENCES academia.Alumno (AlumnoId),
    MateriaId        INT  NOT NULL CONSTRAINT FK_Inscripcion_Materia REFERENCES academia.Materia (MateriaId),
    FechaInscripcion DATE NOT NULL,
    CONSTRAINT UQ_Inscripcion_Alumno_Materia UNIQUE (AlumnoId, MateriaId)
);
INSERT INTO academia.Alumno (Nombre, Apellido) VALUES ('Ana', 'Prueba');
INSERT INTO academia.Materia (Nombre, Codigo) VALUES ('Bases de Datos', 'BD01');
GO
CREATE OR ALTER PROCEDURE academia.InscribirAlumno
    @AlumnoId  INT,
    @MateriaId INT,
    @Resultado INT = 0 OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM academia.Alumno WHERE AlumnoId = @AlumnoId)
        SET @Resultado = -1;          -- el alumno no existe
    ELSE IF EXISTS (SELECT 1 FROM academia.Inscripcion
                    WHERE AlumnoId = @AlumnoId AND MateriaId = @MateriaId)
        SET @Resultado = -2;          -- ya estaba inscripto
    ELSE
    BEGIN
        INSERT INTO academia.Inscripcion (AlumnoId, MateriaId, FechaInscripcion)
        VALUES (@AlumnoId, @MateriaId, CAST(GETDATE() AS DATE));
        SET @Resultado = 1;
    END;
END;
GO
DECLARE @R1 INT, @R2 INT, @R3 INT;
EXEC academia.InscribirAlumno @AlumnoId = 1,  @MateriaId = 1, @Resultado = @R1 OUTPUT;
EXEC academia.InscribirAlumno @AlumnoId = 1,  @MateriaId = 1, @Resultado = @R2 OUTPUT;
EXEC academia.InscribirAlumno @AlumnoId = 99, @MateriaId = 1, @Resultado = @R3 OUTPUT;

SELECT
    @R1 AS PrimeraVez,
    @R2 AS Repetida,
    @R3 AS AlumnoInexistente,
    (SELECT COUNT(*) FROM academia.Inscripcion) AS Inscripciones;
