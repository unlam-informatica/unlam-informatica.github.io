-- U3.T.MT.07: generado desde la página metricas-de-rendimiento.md
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

DECLARE @SoloMiSesion BIT = 1;   -- 0 = todas las sesiones de usuario

SELECT r.session_id           AS SesionId,
       r.blocking_session_id  AS BloqueadaPor,
       DB_NAME(r.database_id) AS BaseDeDatos,
       r.wait_time            AS EsperaMs,
       r.wait_type            AS TipoDeEspera,
       r.command              AS Comando,
       s.login_name           AS Usuario,
       SUBSTRING(t.text, r.statement_start_offset / 2 + 1,
                 (CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.text)
                  ELSE r.statement_end_offset END - r.statement_start_offset) / 2 + 1) AS Sentencia
INTO #EsperasActivas
FROM sys.dm_exec_requests AS r
INNER JOIN sys.dm_exec_sessions AS s ON s.session_id = r.session_id
OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) AS t
WHERE s.is_user_process = 1
  AND (@SoloMiSesion = 0 OR r.session_id = @@SPID);

SELECT COUNT(*) AS Solicitudes,
       MAX(BloqueadaPor) AS BloqueadaPor,
       MAX(Comando) AS Comando
FROM #EsperasActivas;
