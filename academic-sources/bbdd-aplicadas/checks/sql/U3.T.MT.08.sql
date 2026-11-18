-- U3.T.MT.08: generado desde la página metricas-de-rendimiento.md
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

SELECT CASE WHEN cpu_count > 0 THEN 'sí' ELSE 'no' END               AS TieneNucleos,
       CASE WHEN physical_memory_kb > 0 THEN 'sí' ELSE 'no' END      AS TieneMemoria
FROM sys.dm_os_sys_info;

SELECT RTRIM(counter_name) AS Contador, RTRIM(instance_name) AS Instancia
FROM sys.dm_os_performance_counters
WHERE counter_name LIKE N'Number of Deadlocks/sec%'
  AND instance_name = N'_Total';
