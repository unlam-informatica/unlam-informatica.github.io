CREATE SCHEMA prueba;
GO

CREATE TABLE prueba.CargaBase (
    Codigo  VARCHAR(10)  NULL,
    Nombre  VARCHAR(100) NULL,   -- collation de la base: página de códigos 1252
    Barrio  VARCHAR(60)  NULL,
    AlturaM VARCHAR(10)  NULL
);

CREATE TABLE prueba.CargaUtf8 (
    Codigo  VARCHAR(10)  NULL,
    Nombre  VARCHAR(100) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    Barrio  VARCHAR(60)  COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    AlturaM VARCHAR(10)  NULL
);
GO

BULK INSERT prueba.CargaBase
FROM '{{FIXTURES}}/estaciones.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');

BULK INSERT prueba.CargaUtf8
FROM '{{FIXTURES}}/estaciones.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');

SELECT b.Codigo,
       b.Nombre AS ColumnaBase,
       u.Nombre AS ColumnaUtf8,
       LEN(b.Nombre) AS LongitudBase,
       LEN(u.Nombre) AS LongitudUtf8
FROM prueba.CargaBase AS b
JOIN prueba.CargaUtf8 AS u ON u.Codigo = b.Codigo
WHERE LEN(b.Nombre) <> LEN(u.Nombre)
ORDER BY b.Codigo;
