CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NOT NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (Codigo)
);
GO

BULK INSERT ventas.Producto
FROM '{{FIXTURES}}/producto.csv'
WITH (
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR   = '0x0a'
);

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
