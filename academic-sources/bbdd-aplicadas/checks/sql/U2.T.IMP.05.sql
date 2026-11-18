CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NOT NULL
);
GO

DECLARE @Error INT = 0;

BEGIN TRY
    BULK INSERT ventas.Producto
    FROM '{{FIXTURES}}/producto_errores.csv'
    WITH (
        FIRSTROW        = 2,
        FIELDTERMINATOR = ',',
        ROWTERMINATOR   = '0x0a',
        MAXERRORS       = 10,
        ERRORFILE       = '{{FIXTURES}}/rechazadas.csv'
    );
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;

SELECT d.BulkColumn AS FilasRechazadas
FROM OPENROWSET(BULK '{{FIXTURES}}/rechazadas.csv', SINGLE_CLOB) AS d;
