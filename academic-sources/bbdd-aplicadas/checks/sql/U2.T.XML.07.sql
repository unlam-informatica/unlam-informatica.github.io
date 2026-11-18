CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    Ciudad    VARCHAR(30) NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE ventas.Pedido (
    PedidoId  INT           NOT NULL,
    ClienteId INT           NOT NULL,
    Fecha     DATE          NOT NULL,
    Total     DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId),
    CONSTRAINT FK_Pedido_Cliente FOREIGN KEY (ClienteId) REFERENCES ventas.Cliente (ClienteId)
);
GO

INSERT INTO ventas.Cliente (ClienteId, Nombre, Ciudad)
VALUES (1, 'Ferretería Norte', 'Rosario'), (2, 'Kiosco Central', NULL);

INSERT INTO ventas.Pedido (PedidoId, ClienteId, Fecha, Total)
VALUES (1001, 1, '2026-03-02', 3000.00),
       (1002, 1, '2026-03-09', 1250.50),
       (1003, 2, '2026-03-10', 480.25);
GO

SELECT c.ClienteId, c.Nombre, p.PedidoId, p.Total
FROM ventas.Cliente AS c
INNER JOIN ventas.Pedido AS p ON p.ClienteId = c.ClienteId
ORDER BY c.ClienteId, p.PedidoId
FOR XML AUTO, ROOT('Ventas');
