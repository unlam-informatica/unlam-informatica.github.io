CREATE SCHEMA tienda;
GO

CREATE TABLE tienda.Producto (
    ProductoId INT IDENTITY(1, 1) NOT NULL,
    Nombre     VARCHAR(60)        NOT NULL,
    Categoria  VARCHAR(30)        NOT NULL,
    Precio     DECIMAL(10,2)      NOT NULL,
    Stock      INT                NOT NULL,
    Atributos  NVARCHAR(MAX)      NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (ProductoId)
);

CREATE TABLE tienda.Pedido (
    PedidoId INT          NOT NULL,
    Cliente  VARCHAR(40)  NOT NULL,
    Fecha    DATE         NOT NULL,
    Detalle  NVARCHAR(MAX) NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId)
);
GO

INSERT INTO tienda.Producto (Nombre, Categoria, Precio, Stock, Atributos)
VALUES ('Notebook 15',    'Computacion', 1299.99, 12, N'{"marca":"Zeta","ramGb":16,"color":"negro"}'),
       ('Mouse inalambrico', 'Perifericos', 29.99, 85, N'{"marca":"Alfa","dpi":1600,"color":"gris"}'),
       ('Monitor 27',    'Computacion',  349.99, 20, N'{"marca":"Zeta","panel":"IPS","hz":144}'),
       ('Teclado mecanico', 'Perifericos', 89.99, 40, N'{"marca":"Alfa","retroiluminado":true,"colores":["rojo","azul"]}');

INSERT INTO tienda.Pedido (PedidoId, Cliente, Fecha, Detalle)
VALUES (1, 'Cliente A', '2026-03-10',
        N'[{"productoId":1,"cantidad":1,"precio":1299.99},{"productoId":2,"cantidad":2,"precio":29.99}]'),
       (2, 'Cliente B', '2026-03-11',
        N'[{"productoId":3,"cantidad":1,"precio":349.99},{"productoId":4,"cantidad":3,"precio":89.99}]'),
       (3, 'Cliente A', '2026-03-12',
        N'[{"productoId":4,"cantidad":2,"precio":89.99}]');
GO

DECLARE @Error INT = 0;

ALTER TABLE tienda.Producto
    ADD CONSTRAINT CK_Producto_Atributos CHECK (Atributos IS NULL OR ISJSON(Atributos) = 1);

BEGIN TRY
    INSERT INTO tienda.Producto (Nombre, Categoria, Precio, Stock, Atributos)
    VALUES ('Producto roto', 'Prueba', 1.00, 0, N'{marca: Zeta');
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT @Error AS NumeroDeError,
       COUNT(*) AS Productos,
       SUM(ISJSON(Atributos)) AS ConJsonValido
FROM tienda.Producto;
