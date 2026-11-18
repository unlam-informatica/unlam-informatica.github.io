CREATE SCHEMA transporte;
GO

CREATE TABLE transporte.Viajero (
    Id              INT           NOT NULL,
    CodigoEstacion  VARCHAR(10)   NOT NULL,
    NombreEstacion  VARCHAR(60)   NOT NULL,
    NucleoCercanias VARCHAR(40)   NOT NULL,
    TramoHorario    VARCHAR(20)   NOT NULL,
    ViajerosSubidos INT           NOT NULL,
    ViajerosBajados INT           NOT NULL
);
GO

BULK INSERT transporte.Viajero
FROM '{{FIXTURES}}/viajerosgalicia.csv'
WITH (
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR   = '0x0d0a'
);

SELECT COUNT(*) AS Filas,
       COUNT(DISTINCT CodigoEstacion) AS Estaciones,
       SUM(ViajerosSubidos) AS TotalSubidos,
       SUM(ViajerosBajados) AS TotalBajados
FROM transporte.Viajero;
