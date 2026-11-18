CREATE SCHEMA aire;
GO

-- Tablas de carga (staging): todo texto, columnas con collation UTF-8
CREATE TABLE aire.EstacionCarga (
    Codigo  VARCHAR(10)                                      NULL,
    Nombre  VARCHAR(100) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    Barrio  VARCHAR(60)  COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    AlturaM VARCHAR(10)                                      NULL
);

CREATE TABLE aire.LecturaCarga (
    Estacion    VARCHAR(10)                                       NULL,
    FechaHora   VARCHAR(30)                                       NULL,
    Pm25        VARCHAR(30)                                       NULL,
    Observacion VARCHAR(300) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL
);

-- Tablas definitivas
CREATE TABLE aire.Estacion (
    Codigo  CHAR(3)      NOT NULL,
    Nombre  NVARCHAR(80) NOT NULL,
    Barrio  NVARCHAR(40) NOT NULL,
    AlturaM SMALLINT     NOT NULL,
    CONSTRAINT PK_Estacion        PRIMARY KEY CLUSTERED (Codigo),
    CONSTRAINT CK_Estacion_Codigo CHECK (Codigo LIKE 'E[0-9][0-9]'),
    CONSTRAINT CK_Estacion_Altura CHECK (AlturaM BETWEEN 0 AND 500)
);

CREATE TABLE aire.Lectura (
    Estacion    CHAR(3)      NOT NULL,
    FechaHora   DATETIME2(0) NOT NULL,
    Pm25        DECIMAL(5,1) NOT NULL,
    Observacion NVARCHAR(200) NULL,
    CONSTRAINT PK_Lectura PRIMARY KEY CLUSTERED (Estacion, FechaHora),
    CONSTRAINT FK_Lectura_Estacion FOREIGN KEY (Estacion) REFERENCES aire.Estacion (Codigo),
    CONSTRAINT CK_Lectura_Pm25 CHECK (Pm25 >= 0)
);

CREATE TABLE aire.LecturaRechazada (
    RechazoId   INT IDENTITY(1, 1) NOT NULL,
    Estacion    VARCHAR(10)  NULL,
    FechaHora   VARCHAR(30)  NULL,
    Pm25        VARCHAR(30)  NULL,
    Motivo      VARCHAR(40)  NOT NULL,
    CONSTRAINT PK_LecturaRechazada PRIMARY KEY CLUSTERED (RechazoId)
);
GO

-- Estaciones: coma como separador, encabezado, campos entre comillas, UTF-8
BULK INSERT aire.EstacionCarga
FROM '{{FIXTURES}}/estaciones.csv'
WITH (
    FORMAT          = 'CSV',
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    FIELDQUOTE      = '"',
    ROWTERMINATOR   = '0x0a',
    CODEPAGE        = 'RAW'
);

INSERT INTO aire.Estacion (Codigo, Nombre, Barrio, AlturaM)
SELECT Codigo, Nombre, Barrio, CAST(AlturaM AS SMALLINT)
FROM aire.EstacionCarga;
GO

-- Lecturas: punto y coma como separador
BULK INSERT aire.LecturaCarga
FROM '{{FIXTURES}}/lecturas.csv'
WITH (
    FORMAT          = 'CSV',
    FIRSTROW        = 2,
    FIELDTERMINATOR = ';',
    FIELDQUOTE      = '"',
    ROWTERMINATOR   = '0x0a',
    CODEPAGE        = 'RAW'
);

-- Validación: cada fila inválida recibe un único motivo
WITH Marcada AS (
    SELECT c.Estacion, c.FechaHora, c.Pm25,
           ROW_NUMBER() OVER (PARTITION BY c.Estacion, c.FechaHora ORDER BY c.Pm25) AS Orden,
           CASE
               WHEN e.Codigo IS NULL                            THEN 'Estación inexistente'
               WHEN TRY_CONVERT(DATETIME2(0), c.FechaHora) IS NULL THEN 'Fecha inválida'
               WHEN TRY_CONVERT(DECIMAL(5, 1), c.Pm25) IS NULL  THEN 'Pm25 no numérico'
           END AS Motivo
    FROM aire.LecturaCarga AS c
    LEFT JOIN aire.Estacion AS e ON e.Codigo = c.Estacion
)
INSERT INTO aire.LecturaRechazada (Estacion, FechaHora, Pm25, Motivo)
SELECT Estacion, FechaHora, Pm25, COALESCE(Motivo, 'Duplicada')
FROM Marcada
WHERE Motivo IS NOT NULL OR Orden > 1;

INSERT INTO aire.Lectura (Estacion, FechaHora, Pm25, Observacion)
SELECT c.Estacion, CONVERT(DATETIME2(0), c.FechaHora), CONVERT(DECIMAL(5, 1), c.Pm25), c.Observacion
FROM (
    SELECT c.*, ROW_NUMBER() OVER (PARTITION BY c.Estacion, c.FechaHora ORDER BY c.Pm25) AS Orden
    FROM aire.LecturaCarga AS c
) AS c
JOIN aire.Estacion AS e ON e.Codigo = c.Estacion
WHERE c.Orden = 1
  AND TRY_CONVERT(DATETIME2(0), c.FechaHora) IS NOT NULL
  AND TRY_CONVERT(DECIMAL(5, 1), c.Pm25) IS NOT NULL;
GO
CREATE PROCEDURE aire.PrepararResumen
AS
BEGIN
    SET NOCOUNT ON;

    CREATE TABLE #Interna (N INT NOT NULL);          -- local: muere al terminar el procedimiento

    IF OBJECT_ID('tempdb..##ResumenEstacion') IS NOT NULL
        DROP TABLE ##ResumenEstacion;

    SELECT Estacion, COUNT(*) AS Lecturas, MAX(Pm25) AS Maximo
    INTO ##ResumenEstacion                           -- global: visible para toda la instancia
    FROM aire.Lectura
    GROUP BY Estacion;
END;
GO

CREATE PROCEDURE aire.ContarParcial
AS
    SELECT COUNT(*) AS FilasDelLlamador FROM #Parcial;   -- usa la temporal local del código que lo invoca
GO

EXEC aire.PrepararResumen;

-- La global sigue existiendo fuera del procedimiento; la local ya no
SELECT Estacion, Lecturas, Maximo FROM ##ResumenEstacion ORDER BY Estacion;
SELECT CASE WHEN OBJECT_ID('tempdb..#Interna') IS NULL THEN 'ya no existe' ELSE 'existe' END AS TablaInterna;

CREATE TABLE #Parcial (Estacion CHAR(3) NOT NULL);
INSERT INTO #Parcial (Estacion) VALUES ('E01'), ('E02'), ('E03');
EXEC aire.ContarParcial;
GO

-- Una vista no puede apoyarse en una tabla temporal (local o global)
BEGIN TRY
    EXEC (N'CREATE VIEW aire.VistaResumen AS SELECT Estacion, Lecturas, Maximo FROM ##ResumenEstacion;');
END TRY
BEGIN CATCH
    SELECT 'vista sobre ##ResumenEstacion' AS Intento, ERROR_NUMBER() AS Error;
END CATCH;
GO

-- Alternativa: la vista se define sobre las tablas permanentes
CREATE VIEW aire.VistaResumen
AS
SELECT Estacion, COUNT(*) AS Lecturas, MAX(Pm25) AS Maximo
FROM aire.Lectura
GROUP BY Estacion;
GO

SELECT Estacion, Lecturas, Maximo FROM aire.VistaResumen ORDER BY Estacion;

DROP TABLE ##ResumenEstacion;
DROP TABLE #Parcial;
