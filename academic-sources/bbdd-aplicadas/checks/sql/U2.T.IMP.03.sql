CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NULL
);
GO

DECLARE @Error INT = 0;

BEGIN TRY
    BULK INSERT ventas.Producto
    FROM '{{FIXTURES}}/producto_comillas.csv'
    WITH (
        FIRSTROW        = 2,
        FIELDTERMINATOR = ',',
        ROWTERMINATOR   = '0x0a'
    );
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
