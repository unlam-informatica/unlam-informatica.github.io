CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(22)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NOT NULL
);
GO

BULK INSERT ventas.Producto
FROM '{{FIXTURES}}/producto_fijo.txt'
WITH (FORMATFILE = '{{FIXTURES}}/producto_fijo.fmt');

SELECT Codigo, RTRIM(Nombre) AS Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
