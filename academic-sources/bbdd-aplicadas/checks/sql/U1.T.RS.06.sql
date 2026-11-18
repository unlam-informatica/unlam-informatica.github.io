-- u1 · repaso: lógica de tres valores, agregados y concatenación con NULL, UNIQUE y NULL.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL,
    Email    VARCHAR(100) NULL CONSTRAINT UQ_Alumno_Email UNIQUE,
    Nota     INT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre, Email, Nota) VALUES
    (1, 'Ana',  'ana@ejemplo.test', 8),
    (2, 'Beto', NULL,               NULL),
    (3, 'Cora', 'cora@ejemplo.test', 6);

DECLARE @A INT = NULL, @B INT = NULL, @ErrorUnique INT = 0;
BEGIN TRY
    INSERT INTO academia.Alumno (AlumnoId, Nombre, Email, Nota) VALUES (4, 'Dani', NULL, 5);
END TRY
BEGIN CATCH
    SET @ErrorUnique = ERROR_NUMBER();
END CATCH;

SELECT
    CASE WHEN @A = @B THEN 'VERDADERO'
         WHEN NOT (@A = @B) THEN 'FALSO'
         ELSE 'UNKNOWN' END                                          AS NullIgualNull,
    CASE WHEN @A IS NULL AND @B IS NULL THEN 'VERDADERO' ELSE 'FALSO' END AS IsNull,
    COUNT(*)                                                         AS CuentaFilas,
    COUNT(Nota)                                                      AS CuentaNota,
    AVG(Nota)                                                        AS PromedioNota,
    (SELECT ISNULL('Hola ' + Email, 'NULL') FROM academia.Alumno WHERE AlumnoId = 2) AS ConcatenarNull,
    @ErrorUnique                                                     AS ErrorSegundoNull
FROM academia.Alumno;
