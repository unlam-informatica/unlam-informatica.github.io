-- U3.44: generado desde la página rendimiento.md
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

CREATE SCHEMA monitoreo;
GO
CREATE TABLE monitoreo.LineaBaseFilas (
    Corte INT          NOT NULL,
    Tabla VARCHAR(60)  NOT NULL,
    Filas BIGINT       NOT NULL,
    CONSTRAINT PK_LineaBaseFilas PRIMARY KEY CLUSTERED (Corte, Tabla)
);
GO
CREATE PROCEDURE monitoreo.TomarCorteDeFilas
    @Corte INT
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO monitoreo.LineaBaseFilas (Corte, Tabla, Filas)
    SELECT @Corte, CONCAT(s.name, '.', t.name), SUM(ps.row_count)
    FROM sys.dm_db_partition_stats AS ps
    INNER JOIN sys.tables  AS t ON t.object_id = ps.object_id
    INNER JOIN sys.schemas AS s ON s.schema_id = t.schema_id
    WHERE ps.index_id IN (0, 1)
      AND s.name = 'taller'
    GROUP BY s.name, t.name;
END;
GO
EXEC monitoreo.TomarCorteDeFilas @Corte = 1;

INSERT INTO taller.Orden (ClienteId, FechaIngreso, Estado, Patente, Total)
SELECT TOP (200) 1, '2025-01-10', 'Abierta', 'BB00000', 100.00
FROM sys.all_columns;

EXEC monitoreo.TomarCorteDeFilas @Corte = 2;
GO
SELECT b2.Tabla,
       b2.Filas - b1.Filas AS Incremento,
       CAST(100.0 * (b2.Filas - b1.Filas) / b1.Filas AS DECIMAL(5, 2)) AS Porcentaje,
       CASE WHEN 100.0 * (b2.Filas - b1.Filas) / b1.Filas > 1 THEN 'ALERTA' ELSE 'normal' END AS Estado
FROM monitoreo.LineaBaseFilas AS b1
INNER JOIN monitoreo.LineaBaseFilas AS b2
    ON b2.Tabla = b1.Tabla AND b2.Corte = b1.Corte + 1
WHERE b1.Corte = 1
ORDER BY b2.Tabla;
