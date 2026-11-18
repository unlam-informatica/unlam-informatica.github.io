CREATE SCHEMA ventas;
GO
CREATE SCHEMA staging;
GO

CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

INSERT INTO ventas.Cliente (ClienteId, Nombre) VALUES (1, 'Cliente Uno'), (2, 'Cliente Dos');

CREATE TABLE ventas.Venta (
    VentaId   INT           NOT NULL,
    Fecha     DATE          NOT NULL,
    ClienteId INT           NOT NULL,
    Importe   DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Venta PRIMARY KEY CLUSTERED (VentaId),
    CONSTRAINT FK_Venta_Cliente FOREIGN KEY (ClienteId) REFERENCES ventas.Cliente (ClienteId),
    CONSTRAINT CK_Venta_Importe CHECK (Importe > 0)
);

CREATE TABLE staging.Venta (
    Fila      INT IDENTITY(1, 1) NOT NULL,
    VentaId   VARCHAR(20) NULL,
    Fecha     VARCHAR(20) NULL,
    ClienteId VARCHAR(20) NULL,
    Importe   VARCHAR(20) NULL,
    CONSTRAINT PK_StagingVenta PRIMARY KEY CLUSTERED (Fila)
);

CREATE TABLE staging.VentaRechazada (
    Fila   INT         NOT NULL,
    Motivo VARCHAR(40) NOT NULL
);
GO

CREATE VIEW staging.VentaCarga
AS
SELECT VentaId, Fecha, ClienteId, Importe FROM staging.Venta;
GO

BULK INSERT staging.VentaCarga
FROM '{{FIXTURES}}/venta_sucia.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2);
GO

WITH Analizada AS (
    SELECT s.Fila,
           TRY_CONVERT(INT, s.VentaId)            AS VentaId,
           TRY_CONVERT(DATE, s.Fecha, 23)         AS Fecha,
           TRY_CONVERT(INT, s.ClienteId)          AS ClienteId,
           TRY_CONVERT(DECIMAL(10,2), s.Importe)  AS Importe,
           ROW_NUMBER() OVER (PARTITION BY s.VentaId ORDER BY s.Fila) AS Orden
    FROM staging.Venta AS s
)
INSERT INTO staging.VentaRechazada (Fila, Motivo)
SELECT a.Fila,
       CASE
           WHEN a.Fecha IS NULL                                       THEN 'fecha invalida'
           WHEN a.Importe IS NULL                                     THEN 'importe vacio o invalido'
           WHEN a.Importe <= 0                                        THEN 'importe no positivo'
           WHEN NOT EXISTS (SELECT 1 FROM ventas.Cliente AS c
                            WHERE c.ClienteId = a.ClienteId)          THEN 'cliente inexistente'
           ELSE 'venta duplicada'
       END
FROM Analizada AS a
WHERE a.Fecha IS NULL
   OR a.Importe IS NULL
   OR a.Importe <= 0
   OR NOT EXISTS (SELECT 1 FROM ventas.Cliente AS c WHERE c.ClienteId = a.ClienteId)
   OR a.Orden > 1;

INSERT INTO ventas.Venta (VentaId, Fecha, ClienteId, Importe)
SELECT TRY_CONVERT(INT, s.VentaId), TRY_CONVERT(DATE, s.Fecha, 23),
       TRY_CONVERT(INT, s.ClienteId), TRY_CONVERT(DECIMAL(10,2), s.Importe)
FROM staging.Venta AS s
WHERE NOT EXISTS (SELECT 1 FROM staging.VentaRechazada AS r WHERE r.Fila = s.Fila);

SELECT Fila, Motivo FROM staging.VentaRechazada ORDER BY Fila;

SELECT VentaId, Fecha, ClienteId, Importe FROM ventas.Venta ORDER BY VentaId;
