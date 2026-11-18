-- U3.T.IX.04: generado desde la página indices-optimizacion.md
CREATE SCHEMA ventas;
GO
CREATE SCHEMA diag;
GO
CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    Provincia VARCHAR(20) NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE ventas.Pedido (
    PedidoId  INT IDENTITY(1, 1) NOT NULL,
    ClienteId INT                NOT NULL,
    Fecha     DATE               NOT NULL,
    Estado    VARCHAR(10)        NOT NULL,
    Codigo    VARCHAR(12)        NOT NULL,
    Importe   DECIMAL(10, 2)     NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId)
);
GO
WITH n AS (
    SELECT TOP (520) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns
)
INSERT INTO ventas.Cliente (ClienteId, Nombre, Provincia)
SELECT n,
       CONCAT('Cliente ', RIGHT(CONCAT('000', n), 3)),
       CHOOSE(n % 4 + 1, 'Buenos Aires', 'Cordoba', 'Santa Fe', 'Mendoza')
FROM n;

WITH n AS (
    SELECT TOP (20000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns AS a
    CROSS JOIN sys.all_columns AS b
)
INSERT INTO ventas.Pedido (ClienteId, Fecha, Estado, Codigo, Importe)
SELECT n % 500 + 1,
       DATEADD(DAY, n % 730, '2023-01-01'),
       CASE WHEN n % 100 = 0 THEN 'Anulado' WHEN n % 10 = 0 THEN 'Pendiente' ELSE 'Entregado' END,
       CONCAT('P', RIGHT(CONCAT('00000000', n), 8)),
       n % 1000 + 0.50
FROM n;
GO

CREATE FUNCTION diag.OperadoresDe (@Marca NVARCHAR(40))
RETURNS TABLE
AS RETURN
(
    WITH XMLNAMESPACES (DEFAULT 'http://schemas.microsoft.com/sqlserver/2004/07/showplan')
    SELECT r.o.value('@NodeId', 'INT') AS NodoId,
           CASE WHEN r.o.value('(./*/@Lookup)[1]', 'INT') = 1 THEN N'Key Lookup'
                ELSE r.o.value('@PhysicalOp', 'NVARCHAR(60)') END           AS Operador,
           COALESCE(r.o.value('(./*/Object/@Index)[1]', 'NVARCHAR(128)'),
                    r.o.value('(./*/Object/@Table)[1]', 'NVARCHAR(128)'))   AS Objeto,
           qs.last_logical_reads                                            AS LecturasLogicas
    FROM sys.dm_exec_query_stats AS qs
    CROSS APPLY sys.dm_exec_plan_attributes(qs.plan_handle) AS pa
    CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) AS t
    CROSS APPLY (SELECT SUBSTRING(t.text, qs.statement_start_offset / 2 + 1,
                     (CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(t.text)
                      ELSE qs.statement_end_offset END - qs.statement_start_offset) / 2 + 1) AS Sentencia) AS s
    CROSS APPLY sys.dm_exec_text_query_plan(qs.plan_handle, qs.statement_start_offset, qs.statement_end_offset) AS p
    CROSS APPLY (SELECT CAST(p.query_plan AS XML) AS PlanXml) AS x
    CROSS APPLY x.PlanXml.nodes('//RelOp') AS r(o)
    WHERE pa.attribute = 'dbid' AND CAST(pa.value AS INT) = DB_ID()
      AND s.Sentencia LIKE N'%' + @Marca + N'%'
      AND s.Sentencia NOT LIKE N'%OperadoresDe%'
);
GO

CREATE VIEW diag.EstadoIndice
AS
SELECT OBJECT_NAME(ips.object_id) AS Tabla,
       i.name                     AS Indice,
       ips.page_count             AS Paginas,
       CAST(ips.avg_page_space_used_in_percent AS DECIMAL(5, 1)) AS PctLleno,
       CAST(ips.avg_fragmentation_in_percent  AS DECIMAL(5, 1)) AS PctFragmentacion
FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'DETAILED') AS ips
INNER JOIN sys.indexes AS i
    ON i.object_id = ips.object_id
   AND i.index_id  = ips.index_id
WHERE ips.index_level = 0;
GO

ALTER DATABASE SCOPED CONFIGURATION SET LAST_QUERY_PLAN_STATS = ON;
GO
CREATE FUNCTION diag.FilasEstimadasYReales (@Marca NVARCHAR(40))
RETURNS TABLE
AS RETURN
(
    WITH XMLNAMESPACES (DEFAULT 'http://schemas.microsoft.com/sqlserver/2004/07/showplan')
    SELECT r.o.value('@NodeId', 'INT')                                                           AS NodoId,
           r.o.value('@PhysicalOp', 'NVARCHAR(60)')                                              AS Operador,
           COALESCE(r.o.value('(./*/Object/@Index)[1]', 'NVARCHAR(128)'),
                    r.o.value('(./*/Object/@Table)[1]', 'NVARCHAR(128)'))                        AS Objeto,
           CAST(r.o.value('@EstimateRows', 'FLOAT') AS BIGINT)                                   AS FilasEstimadas,
           r.o.value('(./RunTimeInformation/RunTimeCountersPerThread/@ActualRows)[1]', 'BIGINT') AS FilasReales
    FROM sys.dm_exec_query_stats AS qs
    CROSS APPLY sys.dm_exec_plan_attributes(qs.plan_handle) AS pa
    CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) AS t
    CROSS APPLY (SELECT SUBSTRING(t.text, qs.statement_start_offset / 2 + 1,
                     (CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(t.text)
                      ELSE qs.statement_end_offset END - qs.statement_start_offset) / 2 + 1) AS Sentencia) AS s
    CROSS APPLY sys.dm_exec_query_plan_stats(qs.plan_handle) AS p
    CROSS APPLY p.query_plan.nodes('//RelOp') AS r(o)
    WHERE pa.attribute = 'dbid' AND CAST(pa.value AS INT) = DB_ID()
      AND s.Sentencia LIKE N'%' + @Marca + N'%'
      AND s.Sentencia NOT LIKE N'%FilasEstimadasYReales%'
);
GO

DECLARE @N INT;
SELECT @N = COUNT(*) FROM ventas.Pedido WHERE ClienteId = 42 /*A1*/ OPTION (MAXDOP 1);
GO
CREATE NONCLUSTERED INDEX IX_Pedido_ClienteId ON ventas.Pedido (ClienteId);
GO
DECLARE @Total DECIMAL(18, 2);
DECLARE @N INT;
SELECT @Total = SUM(Importe) FROM ventas.Pedido WHERE ClienteId = 42 /*A2*/ OPTION (MAXDOP 1);
SELECT @N     = COUNT(*)     FROM ventas.Pedido WHERE ClienteId = 42 /*A3*/ OPTION (MAXDOP 1);
GO
SELECT 'Sin índice' AS Caso, Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*A1*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Con índice, pide Importe', Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*A2*/')
WHERE Objeto IS NOT NULL
UNION ALL
SELECT 'Con índice, solo cuenta', Operador, Objeto, LecturasLogicas
FROM diag.OperadoresDe(N'/*A3*/')
WHERE Objeto IS NOT NULL
ORDER BY Caso, Operador;
