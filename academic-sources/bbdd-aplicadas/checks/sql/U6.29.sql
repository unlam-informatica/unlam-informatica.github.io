CREATE SCHEMA pulsera;
GO

CREATE TABLE pulsera.Usuario (
    UsuarioId INT         NOT NULL,
    Zona      VARCHAR(10) NOT NULL,
    RangoEdad VARCHAR(10) NOT NULL,
    PasosDia  INT         NOT NULL,
    CONSTRAINT PK_Usuario PRIMARY KEY CLUSTERED (UsuarioId)
);

INSERT INTO pulsera.Usuario (UsuarioId, Zona, RangoEdad, PasosDia)
VALUES
    (1,  'Zona A', '20-29', 6000),
    (2,  'Zona A', '20-29', 8000),
    (3,  'Zona A', '20-29', 7000),
    (4,  'Zona A', '20-29', 9000),
    (5,  'Zona A', '30-39', 5000),
    (6,  'Zona A', '30-39', 6000),
    (7,  'Zona A', '30-39', 7000),
    (8,  'Zona B', '20-29', 4000),
    (9,  'Zona B', '20-29', 12000),
    (10, 'Zona B', '60-69', 3000);
GO

DECLARE @MinimoPorGrupo INT = 3;

SELECT
    Zona,
    RangoEdad,
    COUNT(*) AS Usuarios,
    CASE WHEN COUNT(*) >= @MinimoPorGrupo
         THEN CAST(AVG(1.0 * PasosDia) AS DECIMAL(8, 1)) END AS PasosPromedio,
    CASE WHEN COUNT(*) >= @MinimoPorGrupo THEN 'Publicar' ELSE 'Suprimir' END AS Decision
FROM pulsera.Usuario
GROUP BY Zona, RangoEdad
ORDER BY Zona, RangoEdad;
