CREATE SCHEMA cine;
GO

CREATE TABLE cine.Personaje (
    PersonajeId INT           NOT NULL,
    Personaje   NVARCHAR(100) NOT NULL,
    Actor       NVARCHAR(100) NOT NULL,
    Pelicula    NVARCHAR(100) NOT NULL,
    Anio        INT           NOT NULL,
    CONSTRAINT PK_Personaje PRIMARY KEY CLUSTERED (PersonajeId)
);

CREATE TABLE cine.Archivo (
    Contenido VARCHAR(MAX) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NOT NULL
);
GO

-- El archivo está en UTF-8: se lee como bytes y se guarda en una columna con collation UTF8
INSERT INTO cine.Archivo (Contenido)
SELECT a.BulkColumn
FROM OPENROWSET(BULK '{{FIXTURES}}/starwars.json', SINGLE_BLOB) AS a;

INSERT INTO cine.Personaje (PersonajeId, Personaje, Actor, Pelicula, Anio)
SELECT p.PersonajeId, p.Personaje, p.Actor, p.Pelicula, p.Anio
FROM cine.Archivo AS f
CROSS APPLY OPENJSON(f.Contenido)
WITH (
    PersonajeId INT           '$.id',
    Personaje   NVARCHAR(100) '$.personaje',
    Actor       NVARCHAR(100) '$.actor',
    Pelicula    NVARCHAR(100) '$.pelicula',
    Anio        INT           '$.anio_pelicula'
) AS p;

SELECT Anio, Pelicula, COUNT(*) AS Personajes
FROM cine.Personaje
GROUP BY Anio, Pelicula
ORDER BY Anio, Pelicula;

SELECT DISTINCT Personaje, LEN(Personaje) AS Largo
FROM cine.Personaje
WHERE Personaje LIKE N'Padm%';
