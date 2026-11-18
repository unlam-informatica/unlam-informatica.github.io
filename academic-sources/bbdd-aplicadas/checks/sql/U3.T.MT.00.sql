-- U3.T.MT.00: generado desde la página metricas-de-rendimiento.md
CREATE SCHEMA ventas;
GO
CREATE SCHEMA monitoreo;
GO
CREATE TABLE ventas.Pedido (
    PedidoId  INT IDENTITY(1, 1) NOT NULL,
    ClienteId INT            NOT NULL,
    Estado    VARCHAR(10)    NOT NULL,
    Importe   DECIMAL(10, 2) NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId)
);
CREATE NONCLUSTERED INDEX IX_Pedido_ClienteId ON ventas.Pedido (ClienteId);
GO
WITH n AS (
    SELECT TOP (20000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns AS a
    CROSS JOIN sys.all_columns AS b
)
INSERT INTO ventas.Pedido (ClienteId, Estado, Importe)
SELECT n % 500 + 1,
       CASE WHEN n % 100 = 0 THEN 'Anulado' WHEN n % 10 = 0 THEN 'Pendiente' ELSE 'Entregado' END,
       n % 1000 + 0.50
FROM n;
GO
