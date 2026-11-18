CREATE SCHEMA staging;
GO

CREATE TABLE staging.Producto (
    Codigo    CHAR(4)      NOT NULL,
    Nombre    NVARCHAR(40) NOT NULL,
    Categoria NVARCHAR(40) NOT NULL
);
GO

BULK INSERT staging.Producto
FROM '{{FIXTURES}}/acentos16.csv'
WITH (
    FORMAT       = 'CSV',
    FIRSTROW     = 2,
    DATAFILETYPE = 'widechar'
);

SELECT Codigo, Nombre, Categoria
FROM staging.Producto
ORDER BY Codigo;
