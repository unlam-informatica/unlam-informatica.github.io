-- u4 · POO: un Pedido con cliente y líneas representado en tablas.
CREATE SCHEMA tienda;
GO

CREATE TABLE tienda.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(60) NOT NULL,
    Localidad VARCHAR(40) NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE tienda.Pedido (
    PedidoId  INT  NOT NULL,
    Fecha     DATE NOT NULL,
    ClienteId INT  NOT NULL,
    CONSTRAINT PK_Pedido         PRIMARY KEY CLUSTERED (PedidoId),
    CONSTRAINT FK_Pedido_Cliente FOREIGN KEY (ClienteId) REFERENCES tienda.Cliente (ClienteId)
);

CREATE TABLE tienda.LineaPedido (
    PedidoId       INT           NOT NULL,
    Numero         INT           NOT NULL,
    Producto       VARCHAR(40)   NOT NULL,
    Cantidad       INT           NOT NULL,
    PrecioUnitario DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_LineaPedido        PRIMARY KEY CLUSTERED (PedidoId, Numero),
    CONSTRAINT FK_LineaPedido_Pedido FOREIGN KEY (PedidoId) REFERENCES tienda.Pedido (PedidoId)
);
GO

INSERT INTO tienda.Cliente (ClienteId, Nombre, Localidad) VALUES
    (1, 'Ana', 'Ramos Mejía'),
    (2, 'Bruno', 'Morón');
INSERT INTO tienda.Pedido (PedidoId, Fecha, ClienteId) VALUES
    (101, '2026-03-05', 1),
    (102, '2026-03-18', 2);
INSERT INTO tienda.LineaPedido (PedidoId, Numero, Producto, Cantidad, PrecioUnitario) VALUES
    (101, 1, 'Teclado', 2, 45.00),
    (101, 2, 'Mouse',   1, 20.00),
    (102, 1, 'Monitor', 1, 300.00);
GO

-- Reconstruir el objeto Pedido 101 exige un JOIN por cada asociación
SELECT p.PedidoId, p.Fecha, c.Nombre AS Cliente, l.Numero, l.Producto, l.Cantidad, l.PrecioUnitario
FROM tienda.Pedido AS p
INNER JOIN tienda.Cliente AS c ON c.ClienteId = p.ClienteId
INNER JOIN tienda.LineaPedido AS l ON l.PedidoId = p.PedidoId
WHERE p.PedidoId = 101
ORDER BY l.Numero;
