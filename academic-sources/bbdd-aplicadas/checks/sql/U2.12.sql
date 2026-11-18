CREATE SCHEMA prueba;
GO

CREATE TABLE prueba.BarrioCarga (
    Codigo VARCHAR(10) NULL,
    Barrio VARCHAR(60) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    Zona   VARCHAR(10) NULL
);
GO

BULK INSERT prueba.BarrioCarga
FROM '{{FIXTURES}}/barrios-mojibake.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');

-- Secuencias dañadas: Ã + otro carácter (UTF-8 leído como Windows-1252).
-- Reparación ingenua (collation CI_AI) frente a reparación segura (comparación binaria)
WITH Texto AS (
    SELECT Codigo, CAST(Barrio AS NVARCHAR(60)) AS Original FROM prueba.BarrioCarga
)
SELECT t.Codigo,
       t.Original,
       i.Ingenua,
       s.Segura
FROM Texto AS t
CROSS APPLY (
    SELECT REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(t.Original COLLATE Latin1_General_CI_AI,
           NCHAR(195) + NCHAR(161),  N'á'),
           NCHAR(195) + NCHAR(169),  N'é'),
           NCHAR(195) + NCHAR(179),  N'ó'),
           NCHAR(195) + NCHAR(186),  N'ú'),
           NCHAR(195) + NCHAR(177),  N'ñ'),
           NCHAR(195) + NCHAR(8216), N'Ñ') AS Ingenua
) AS i
CROSS APPLY (
    SELECT REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(t.Original COLLATE Latin1_General_100_BIN2,
           NCHAR(195) + NCHAR(161),  N'á'),
           NCHAR(195) + NCHAR(169),  N'é'),
           NCHAR(195) + NCHAR(179),  N'ó'),
           NCHAR(195) + NCHAR(186),  N'ú'),
           NCHAR(195) + NCHAR(177),  N'ñ'),
           NCHAR(195) + NCHAR(8216), N'Ñ') AS Segura
) AS s
ORDER BY t.Codigo;

-- Control posterior: ninguna fila reparada conserva la letra Ã (código 195)
SELECT COUNT(*) AS FilasConResiduo
FROM prueba.BarrioCarga
WHERE CHARINDEX(NCHAR(195),
      REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(CAST(Barrio AS NVARCHAR(60)) COLLATE Latin1_General_100_BIN2,
      NCHAR(195) + NCHAR(161),  N'á'),
      NCHAR(195) + NCHAR(169),  N'é'),
      NCHAR(195) + NCHAR(179),  N'ó'),
      NCHAR(195) + NCHAR(186),  N'ú'),
      NCHAR(195) + NCHAR(177),  N'ñ'),
      NCHAR(195) + NCHAR(8216), N'Ñ') COLLATE Latin1_General_100_BIN2) > 0;
