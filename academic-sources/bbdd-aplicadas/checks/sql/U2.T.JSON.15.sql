CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    ProductoId INT IDENTITY(1, 1) NOT NULL,
    Nombre     VARCHAR(60)        NOT NULL,
    Atributos  NVARCHAR(MAX)      NOT NULL,
    Marca      AS CAST(JSON_VALUE(Atributos, '$.marca') AS NVARCHAR(40)),
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (ProductoId)
);

CREATE INDEX IX_Producto_Marca ON ventas.Producto (Marca);
GO

INSERT INTO ventas.Producto (Nombre, Atributos)
VALUES ('Taladro',   N'{"marca":"Zeta","potenciaW":650}'),
       ('Martillo',  N'{"marca":"Alfa"}'),
       ('Sierra',    N'{"marca":"Zeta","hojas":3}');

SELECT Nombre, Marca
FROM ventas.Producto
WHERE Marca = N'Zeta'
ORDER BY Nombre;
