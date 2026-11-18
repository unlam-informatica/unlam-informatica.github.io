CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    ProductoId INT IDENTITY(1, 1) NOT NULL,
    Nombre     VARCHAR(60)        NOT NULL,
    Atributos  NVARCHAR(MAX)      NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (ProductoId),
    CONSTRAINT CK_Producto_Atributos CHECK (Atributos IS NULL OR ISJSON(Atributos) = 1)
);
GO

INSERT INTO ventas.Producto (Nombre, Atributos)
VALUES ('Taladro', N'{"marca":"Zeta","potenciaW":650}');

DECLARE @Error INT = 0;
BEGIN TRY
    INSERT INTO ventas.Producto (Nombre, Atributos)
    VALUES ('Martillo', N'{"marca":"Zeta", potencia: }');
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT @Error AS NumeroDeError,
       (SELECT COUNT(*) FROM ventas.Producto) AS FilasGuardadas,
       ISJSON(N'{"a":1}') AS EsJson1,
       ISJSON(N'{a:1}')   AS EsJson2,
       ISJSON(N'[1,2,3]') AS EsJson3,
       ISJSON(N'texto')   AS EsJson4;
