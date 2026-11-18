-- u1 · repaso: esquema, tablas, PK/FK y rechazo de una FK inválida.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT IDENTITY(1, 1) NOT NULL,
    Nombre   VARCHAR(100)       NOT NULL,
    Apellido VARCHAR(100)       NOT NULL,
    Email    VARCHAR(150)       NULL,
    CONSTRAINT PK_Alumno PRIMARY KEY (AlumnoId)
);

CREATE TABLE academia.Materia (
    MateriaId INT IDENTITY(1, 1) NOT NULL,
    Nombre    VARCHAR(100)       NOT NULL,
    Codigo    VARCHAR(20)        NOT NULL,
    CONSTRAINT PK_Materia PRIMARY KEY (MateriaId)
);

CREATE TABLE academia.Inscripcion (
    InscripcionId    INT IDENTITY(1, 1) NOT NULL,
    AlumnoId         INT                NOT NULL,
    MateriaId        INT                NOT NULL,
    FechaInscripcion DATE               NOT NULL,
    CONSTRAINT PK_Inscripcion PRIMARY KEY (InscripcionId),
    CONSTRAINT FK_Inscripcion_Alumno FOREIGN KEY (AlumnoId) REFERENCES academia.Alumno (AlumnoId),
    CONSTRAINT FK_Inscripcion_Materia FOREIGN KEY (MateriaId) REFERENCES academia.Materia (MateriaId)
);

INSERT INTO academia.Alumno (Nombre, Apellido) VALUES ('Ana', 'Prueba');
INSERT INTO academia.Materia (Nombre, Codigo) VALUES ('Bases de Datos', 'BD01');

DECLARE @Error INT = 0;
BEGIN TRY
    INSERT INTO academia.Inscripcion (AlumnoId, MateriaId, FechaInscripcion)
    VALUES (99, 1, '2026-03-01');
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT
    (SELECT COUNT(*) FROM sys.tables WHERE schema_id = SCHEMA_ID('academia')) AS Tablas,
    (SELECT COUNT(*) FROM academia.Inscripcion)                              AS Inscripciones,
    @Error                                                                   AS ErrorFk;
