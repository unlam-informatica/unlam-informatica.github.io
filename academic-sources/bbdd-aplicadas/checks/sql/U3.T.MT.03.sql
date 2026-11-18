-- U3.T.MT.03: generado desde la página metricas-de-rendimiento.md
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

DECLARE @N INT;
SELECT @N = COUNT(*) FROM ventas.Pedido WHERE ClienteId = 7 /*M1*/ OPTION (MAXDOP 1);
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM ventas.Pedido WHERE ClienteId = 7 /*M1*/ OPTION (MAXDOP 1);
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM ventas.Pedido WHERE ClienteId = 7 /*M1*/ OPTION (MAXDOP 1);
GO
SELECT SUM(qs.execution_count)                             AS Ejecuciones,
       SUM(qs.total_logical_reads) / SUM(qs.execution_count) AS LecturasPorEjecucion,
       CASE WHEN SUM(qs.total_worker_time) > 0 THEN 'sí' ELSE 'no' END AS ConsumioCpu
FROM sys.dm_exec_query_stats AS qs
CROSS APPLY sys.dm_exec_plan_attributes(qs.plan_handle) AS pa
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) AS t
WHERE pa.attribute = 'dbid' AND CAST(pa.value AS INT) = DB_ID()
  AND t.text LIKE N'%DECLARE @N INT;%/*M1*/%OPTION (MAXDOP 1);%'
  AND t.text NOT LIKE N'%dm_exec_query_stats%';

SELECT COUNT(*) AS ColumnasDeEsperas
FROM sys.all_columns
WHERE object_id = OBJECT_ID('sys.dm_os_wait_stats')
  AND name IN ('wait_type', 'waiting_tasks_count', 'wait_time_ms', 'signal_wait_time_ms');
