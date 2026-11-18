-- U3.T.MT.02: generado desde la página metricas-de-rendimiento.md
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

CREATE TABLE monitoreo.LineaBaseArchivo (
    MedicionId     INT IDENTITY(1, 1) NOT NULL,
    Momento        DATETIME2          NOT NULL CONSTRAINT DF_LineaBaseArchivo_Momento DEFAULT (SYSDATETIME()),
    ArchivoId      INT                NOT NULL,
    Tipo           VARCHAR(10)        NOT NULL,
    Escrituras     BIGINT             NOT NULL,
    BytesEscritos  BIGINT             NOT NULL,
    CONSTRAINT PK_LineaBaseArchivo PRIMARY KEY CLUSTERED (MedicionId)
);
GO
-- Foto inicial:
INSERT INTO monitoreo.LineaBaseArchivo (ArchivoId, Tipo, Escrituras, BytesEscritos)
SELECT vfs.file_id, mf.type_desc, vfs.num_of_writes, vfs.num_of_bytes_written
FROM sys.dm_io_virtual_file_stats(DB_ID(), NULL) AS vfs
INNER JOIN sys.master_files AS mf
    ON mf.database_id = vfs.database_id AND mf.file_id = vfs.file_id;

-- Actividad: se actualizan 10.000 pedidos.
UPDATE ventas.Pedido SET Importe = Importe + 1 WHERE PedidoId <= 10000;

-- Foto final:
INSERT INTO monitoreo.LineaBaseArchivo (ArchivoId, Tipo, Escrituras, BytesEscritos)
SELECT vfs.file_id, mf.type_desc, vfs.num_of_writes, vfs.num_of_bytes_written
FROM sys.dm_io_virtual_file_stats(DB_ID(), NULL) AS vfs
INNER JOIN sys.master_files AS mf
    ON mf.database_id = vfs.database_id AND mf.file_id = vfs.file_id;
GO
SELECT a.Tipo,
       CASE WHEN b.Escrituras    > a.Escrituras    THEN 'sí' ELSE 'no' END AS AumentaronEscrituras,
       CASE WHEN b.BytesEscritos > a.BytesEscritos THEN 'sí' ELSE 'no' END AS AumentaronBytes
FROM monitoreo.LineaBaseArchivo AS a
INNER JOIN monitoreo.LineaBaseArchivo AS b
    ON b.ArchivoId = a.ArchivoId AND b.MedicionId > a.MedicionId
WHERE a.Tipo = 'LOG';
