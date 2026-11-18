-- U3.31: generado desde la página rendimiento.md
CREATE SCHEMA taller;
GO
CREATE SCHEMA diag;
GO
CREATE TABLE taller.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    Ciudad    VARCHAR(20) NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE taller.Orden (
    OrdenId      INT IDENTITY(1, 1) NOT NULL,
    ClienteId    INT                NOT NULL,
    FechaIngreso DATE               NOT NULL,
    Estado       VARCHAR(12)        NOT NULL,
    Patente      VARCHAR(7)         NOT NULL,
    Total        DECIMAL(10, 2)     NOT NULL,
    CONSTRAINT PK_Orden PRIMARY KEY CLUSTERED (OrdenId)
);
GO
WITH n AS (
    SELECT TOP (300) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns
)
INSERT INTO taller.Cliente (ClienteId, Nombre, Ciudad)
SELECT n,
       CONCAT('Cliente ', RIGHT(CONCAT('000', n), 3)),
       CHOOSE(n % 3 + 1, 'La Matanza', 'Moron', 'Lomas')
FROM n;

WITH n AS (
    SELECT TOP (15000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns AS a
    CROSS JOIN sys.all_columns AS b
)
INSERT INTO taller.Orden (ClienteId, FechaIngreso, Estado, Patente, Total)
SELECT n % 300 + 1,
       DATEADD(DAY, n % 1095, '2022-01-01'),
       CASE WHEN n % 100 = 0 THEN 'Anulada' WHEN n % 7 = 0 THEN 'Abierta' ELSE 'Cerrada' END,
       CONCAT('AA', RIGHT(CONCAT('00000', n), 5)),
       n % 500 + 100.00
FROM n;
GO
ALTER DATABASE SCOPED CONFIGURATION SET LAST_QUERY_PLAN_STATS = ON;
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
CREATE FUNCTION diag.FilasEstimadasYReales (@Marca NVARCHAR(40))
RETURNS TABLE
AS RETURN
(
    WITH XMLNAMESPACES (DEFAULT 'http://schemas.microsoft.com/sqlserver/2004/07/showplan')
    SELECT r.o.value('@NodeId', 'INT')                                                           AS NodoId,
           r.o.value('@PhysicalOp', 'NVARCHAR(60)')                                              AS Operador,
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

CREATE NONCLUSTERED INDEX IX_Orden_Estado ON taller.Orden (Estado);
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM taller.Orden WHERE Estado = 'Abierta' /*H1*/ OPTION (MAXDOP 1);
GO
SELECT h.range_high_key AS Valor, CAST(h.equal_rows AS INT) AS FilasConEseValor
FROM sys.dm_db_stats_histogram(OBJECT_ID('taller.Orden'),
         (SELECT stats_id FROM sys.stats WHERE object_id = OBJECT_ID('taller.Orden') AND name = 'IX_Orden_Estado')) AS h
ORDER BY h.range_high_key;

SELECT FilasEstimadas, FilasReales
FROM diag.FilasEstimadasYReales(N'/*H1*/')
WHERE Operador = 'Index Seek';
