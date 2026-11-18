CREATE SCHEMA staging;
GO

-- Cada línea del archivo mide 40 caracteres
CREATE TABLE staging.LineaProducto (
    Linea CHAR(40) NOT NULL
);
GO

BULK INSERT staging.LineaProducto
FROM '{{FIXTURES}}/producto_fijo.txt'
WITH (ROWTERMINATOR = '0x0a');

SELECT SUBSTRING(Linea, 1, 4)                              AS Codigo,
       RTRIM(SUBSTRING(Linea, 5, 22))                      AS Nombre,
       CAST(SUBSTRING(Linea, 27, 10) AS DECIMAL(10,2))     AS Precio,
       CAST(SUBSTRING(Linea, 37, 4)  AS INT)               AS Stock
FROM staging.LineaProducto
ORDER BY Codigo;
