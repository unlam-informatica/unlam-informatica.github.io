-- u2 · Collation: el orden de ORDER BY cambia con la intercalación (diccionario frente a binario).
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Etiqueta (Texto VARCHAR(10) NOT NULL);
INSERT ventas.Etiqueta (Texto) VALUES ('a'), ('B'), ('C'), ('d');

SELECT
    'Latin1_General_CI_AS' AS Intercalacion,
    STRING_AGG(Texto, ' ') WITHIN GROUP (ORDER BY Texto COLLATE Latin1_General_CI_AS) AS Orden
FROM ventas.Etiqueta
UNION ALL
SELECT
    'Latin1_General_BIN2',
    STRING_AGG(Texto, ' ') WITHIN GROUP (ORDER BY Texto COLLATE Latin1_General_BIN2)
FROM ventas.Etiqueta;
