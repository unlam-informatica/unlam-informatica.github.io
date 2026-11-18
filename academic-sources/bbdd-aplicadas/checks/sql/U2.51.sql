-- u2 · Ejercicio U2.51: la ñ se ordena distinto según la intercalación.
CREATE SCHEMA diccionario;
GO
CREATE TABLE diccionario.Palabra (Texto VARCHAR(10) NOT NULL);
INSERT diccionario.Palabra (Texto) VALUES ('cano'), ('caña'), ('cana'), ('canal');

SELECT 'Modern_Spanish_CI_AS' AS Intercalacion,
       STRING_AGG(Texto, ' ') WITHIN GROUP (ORDER BY Texto COLLATE Modern_Spanish_CI_AS) AS Orden
FROM diccionario.Palabra
UNION ALL
SELECT 'Latin1_General_CI_AS',
       STRING_AGG(Texto, ' ') WITHIN GROUP (ORDER BY Texto COLLATE Latin1_General_CI_AS)
FROM diccionario.Palabra;
