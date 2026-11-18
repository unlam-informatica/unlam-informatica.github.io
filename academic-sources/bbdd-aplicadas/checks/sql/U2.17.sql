CREATE SCHEMA empleo;
GO

CREATE TABLE empleo.SalarioMensual (
    Fecha   DATE NOT NULL,
    Clae2   INT  NOT NULL,
    Mediana INT  NOT NULL
);
GO

BULK INSERT empleo.SalarioMensual
FROM '{{FIXTURES}}/SalarioMensualMedio.csv'
WITH (
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR   = '0x0d0a'
);

SELECT COUNT(*) AS Filas,
       MIN(Fecha) AS PrimeraFecha,
       MAX(Fecha) AS UltimaFecha,
       COUNT(DISTINCT Clae2) AS Sectores
FROM empleo.SalarioMensual;
