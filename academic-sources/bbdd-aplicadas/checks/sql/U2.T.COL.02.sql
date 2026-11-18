-- u2 · Collation: la misma búsqueda con cuatro sensibilidades distintas.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL PRIMARY KEY,
    Nombre    VARCHAR(30) NOT NULL
);
INSERT ventas.Cliente (ClienteId, Nombre)
VALUES (1, 'Juan'), (2, 'juan'), (3, 'JUAN'), (4, 'juán'), (5, 'Julia');

SELECT Intercalacion, Coincidencias
FROM (
    SELECT 1 AS Orden, 'Modern_Spanish_CI_AS' AS Intercalacion, COUNT(*) AS Coincidencias
    FROM ventas.Cliente WHERE Nombre = 'juan' COLLATE Modern_Spanish_CI_AS
    UNION ALL
    SELECT 2, 'Modern_Spanish_CI_AI', COUNT(*)
    FROM ventas.Cliente WHERE Nombre = 'juan' COLLATE Modern_Spanish_CI_AI
    UNION ALL
    SELECT 3, 'Modern_Spanish_CS_AS', COUNT(*)
    FROM ventas.Cliente WHERE Nombre = 'juan' COLLATE Modern_Spanish_CS_AS
    UNION ALL
    SELECT 4, 'Modern_Spanish_CS_AI', COUNT(*)
    FROM ventas.Cliente WHERE Nombre = 'juan' COLLATE Modern_Spanish_CS_AI
) AS r
ORDER BY Orden;
