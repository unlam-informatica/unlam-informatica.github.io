CREATE SCHEMA staging;
GO
CREATE SCHEMA ventas;
GO

-- Staging: todo como texto, más una columna con el orden de llegada
CREATE TABLE staging.Producto (
    FilaId INT IDENTITY(1, 1) NOT NULL,
    Codigo VARCHAR(20)  NULL,
    Nombre VARCHAR(100) NULL,
    Precio VARCHAR(30)  NULL,
    Stock  VARCHAR(30)  NULL,
    CONSTRAINT PK_StagingProducto PRIMARY KEY CLUSTERED (FilaId)
);
GO

-- Vista sin la columna de identidad: es el destino de BULK INSERT
CREATE VIEW staging.ProductoCarga
AS
SELECT Codigo, Nombre, Precio, Stock FROM staging.Producto;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NOT NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (Codigo),
    CONSTRAINT CK_Producto_Precio CHECK (Precio > 0),
    CONSTRAINT CK_Producto_Stock CHECK (Stock >= 0)
);
GO

BULK INSERT staging.ProductoCarga
FROM '{{FIXTURES}}/producto_sucio.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2);
GO

-- Validación: una fila es válida si convierte bien, cumple las reglas y es la primera de su código
WITH Validada AS (
    SELECT FilaId, Codigo, Nombre,
           TRY_CONVERT(DECIMAL(10,2), Precio) AS PrecioNum,
           TRY_CONVERT(INT, Stock)            AS StockNum,
           ROW_NUMBER() OVER (PARTITION BY Codigo ORDER BY FilaId) AS Orden
    FROM staging.Producto
)
INSERT INTO ventas.Producto (Codigo, Nombre, Precio, Stock)
SELECT Codigo, Nombre, PrecioNum, StockNum
FROM Validada
WHERE PrecioNum > 0
  AND StockNum >= 0
  AND Orden = 1;

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
