CREATE SCHEMA biblioteca;
GO

CREATE TABLE biblioteca.SocioImportado (
    Fila   INT IDENTITY(1, 1) NOT NULL,
    Nombre VARCHAR(60)        NOT NULL,
    Email  VARCHAR(100)       NOT NULL
);

INSERT INTO biblioteca.SocioImportado (Nombre, Email)
VALUES ('Socio A',  'socio01@ejemplo.test'),
       ('Socio A',  'SOCIO01@ejemplo.test '),
       ('Socio B',  'socio02@ejemplo.test'),
       ('Socio C',  'socio03@ejemplo.test'),
       ('Socio C',  ' Socio03@Ejemplo.Test'),
       ('Socio C2', 'socio03@ejemplo.test'),
       ('Socio D',  'socio04@ejemplo.test');

WITH Numerado AS (
    SELECT Fila,
           ROW_NUMBER() OVER (
               PARTITION BY LOWER(LTRIM(RTRIM(Email)))
               ORDER BY Fila
           ) AS Orden
    FROM biblioteca.SocioImportado
)
DELETE FROM Numerado
WHERE Orden > 1;

SELECT Fila, Nombre, Email
FROM biblioteca.SocioImportado
ORDER BY Fila;
