CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (Codigo)
);
GO

INSERT INTO ventas.Producto (Codigo, Nombre, Precio, Stock)
SELECT p.Codigo, p.Nombre, p.Precio, p.Stock
FROM OPENROWSET(BULK '{{FIXTURES}}/producto.json', SINGLE_CLOB) AS archivo
CROSS APPLY OPENJSON(archivo.BulkColumn)
WITH (
    Codigo CHAR(4)       '$.codigo',
    Nombre VARCHAR(40)   '$.nombre',
    Precio DECIMAL(10,2) '$.precio',
    Stock  INT           '$.stock'
) AS p;

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
