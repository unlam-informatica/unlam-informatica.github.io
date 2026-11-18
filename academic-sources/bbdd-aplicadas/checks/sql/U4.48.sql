-- u4 · ejercicio U4.48: esquema al leer sobre JSON con array (ELT).
CREATE SCHEMA lago;
GO

CREATE TABLE lago.PedidoCrudo (
    PedidoId  INT           NOT NULL,
    Contenido NVARCHAR(MAX) NOT NULL,
    CONSTRAINT PK_PedidoCrudo PRIMARY KEY CLUSTERED (PedidoId)
);
GO

INSERT INTO lago.PedidoCrudo (PedidoId, Contenido) VALUES
    (1, N'{"cliente":"c1","lineas":[{"prod":"Teclado","cant":2,"precio":45},{"prod":"Mouse","cant":1,"precio":20}]}'),
    (2, N'{"cliente":"c2","lineas":[{"prod":"Monitor","cant":1,"precio":300}]}'),
    (3, N'{"cliente":"c1"}'),
    (4, N'{"cliente":"c1","lineas":[{"prod":"Mouse","cant":3,"precio":"20"}]}');
GO

CREATE VIEW lago.PedidoLinea
AS
SELECT
    p.PedidoId,
    c.Cliente,
    l.Producto,
    l.Cantidad,
    l.Precio
FROM lago.PedidoCrudo AS p
CROSS APPLY OPENJSON(p.Contenido)
    WITH (Cliente VARCHAR(10) '$.cliente', Lineas NVARCHAR(MAX) '$.lineas' AS JSON) AS c
OUTER APPLY OPENJSON(c.Lineas)
    WITH (
        Producto VARCHAR(40)   '$.prod',
        Cantidad INT           '$.cant',
        Precio   DECIMAL(10,2) '$.precio'
    ) AS l;
GO

SELECT Cliente, SUM(Cantidad * Precio) AS Importe, COUNT(Producto) AS Lineas
FROM lago.PedidoLinea
GROUP BY Cliente
ORDER BY Cliente;
