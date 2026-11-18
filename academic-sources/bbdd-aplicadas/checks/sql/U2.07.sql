CREATE TABLE dbo.LecturaPrueba (
    Estacion VARCHAR(10), FechaHora VARCHAR(30), Pm25 VARCHAR(30), Observacion VARCHAR(300)
);
GO

-- 1) Con FORMAT = 'CSV', una línea con campos de menos aborta toda la carga
BEGIN TRY
    BULK INSERT dbo.LecturaPrueba
    FROM '{{FIXTURES}}/lecturas-truncada.csv'
    WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ';', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');
END TRY
BEGIN CATCH
    SELECT 'carga CSV' AS Intento, ERROR_NUMBER() AS Error;
END CATCH;
SELECT COUNT(*) AS FilasCargadas FROM dbo.LecturaPrueba;
GO

-- 2) Diagnóstico: cada línea entra entera en una columna (ningún terminador de campo la divide)
CREATE TABLE dbo.LineaCruda (
    NumeroLinea INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    Texto       VARCHAR(500) NULL
);
GO
CREATE VIEW dbo.LineaCrudaTexto AS SELECT Texto FROM dbo.LineaCruda;
GO

BULK INSERT dbo.LineaCrudaTexto
FROM '{{FIXTURES}}/lecturas-truncada.csv'
WITH (FIELDTERMINATOR = '0x1f', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');

SELECT NumeroLinea, Texto, LEN(Texto) - LEN(REPLACE(Texto, ';', '')) AS Separadores
FROM dbo.LineaCruda
WHERE LEN(Texto) - LEN(REPLACE(Texto, ';', '')) <> 3
ORDER BY NumeroLinea;
