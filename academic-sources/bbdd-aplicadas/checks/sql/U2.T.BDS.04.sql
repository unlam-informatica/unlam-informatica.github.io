-- u2 · tempdb: una tabla temporal vive en tempdb, no en la base actual, y tempdb usa el modelo SIMPLE.
CREATE TABLE #PedidoBds (
    PedidoId INT           NOT NULL PRIMARY KEY,
    Total    DECIMAL(10,2) NOT NULL
);
INSERT #PedidoBds (PedidoId, Total) VALUES (1, 100.00), (2, 250.50);

SELECT
    LEFT(t.name, 10)                         AS Tabla,
    CASE WHEN EXISTS (SELECT 1 FROM sys.tables WHERE name LIKE N'#PedidoBds%') THEN 'sí' ELSE 'no' END AS EnBaseActual,
    d.recovery_model_desc                    AS ModeloDeRecuperacionDeTempdb
FROM tempdb.sys.tables AS t
CROSS JOIN sys.databases AS d
WHERE t.object_id = OBJECT_ID(N'tempdb..#PedidoBds')
  AND d.name = N'tempdb';
