CREATE SCHEMA aire;
GO

-- Tablas de carga (staging): todo texto, columnas con collation UTF-8
CREATE TABLE aire.EstacionCarga (
    Codigo  VARCHAR(10)                                      NULL,
    Nombre  VARCHAR(100) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    Barrio  VARCHAR(60)  COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    AlturaM VARCHAR(10)                                      NULL
);

CREATE TABLE aire.LecturaCarga (
    Estacion    VARCHAR(10)                                       NULL,
    FechaHora   VARCHAR(30)                                       NULL,
    Pm25        VARCHAR(30)                                       NULL,
    Observacion VARCHAR(300) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL
);

-- Tablas definitivas
CREATE TABLE aire.Estacion (
    Codigo  CHAR(3)      NOT NULL,
    Nombre  NVARCHAR(80) NOT NULL,
    Barrio  NVARCHAR(40) NOT NULL,
    AlturaM SMALLINT     NOT NULL,
    CONSTRAINT PK_Estacion        PRIMARY KEY CLUSTERED (Codigo),
    CONSTRAINT CK_Estacion_Codigo CHECK (Codigo LIKE 'E[0-9][0-9]'),
    CONSTRAINT CK_Estacion_Altura CHECK (AlturaM BETWEEN 0 AND 500)
);

CREATE TABLE aire.Lectura (
    Estacion    CHAR(3)      NOT NULL,
    FechaHora   DATETIME2(0) NOT NULL,
    Pm25        DECIMAL(5,1) NOT NULL,
    Observacion NVARCHAR(200) NULL,
    CONSTRAINT PK_Lectura PRIMARY KEY CLUSTERED (Estacion, FechaHora),
    CONSTRAINT FK_Lectura_Estacion FOREIGN KEY (Estacion) REFERENCES aire.Estacion (Codigo),
    CONSTRAINT CK_Lectura_Pm25 CHECK (Pm25 >= 0)
);

CREATE TABLE aire.LecturaRechazada (
    RechazoId   INT IDENTITY(1, 1) NOT NULL,
    Estacion    VARCHAR(10)  NULL,
    FechaHora   VARCHAR(30)  NULL,
    Pm25        VARCHAR(30)  NULL,
    Motivo      VARCHAR(40)  NOT NULL,
    CONSTRAINT PK_LecturaRechazada PRIMARY KEY CLUSTERED (RechazoId)
);
GO
SELECT CAST(SERVERPROPERTY('Collation') AS VARCHAR(60))              AS CollationServidor,
       CAST(DATABASEPROPERTYEX(DB_NAME(), 'Collation') AS VARCHAR(60)) AS CollationBase,
       (SELECT catalog_collation_type_desc FROM sys.databases WHERE database_id = DB_ID()) AS CollationCatalogo;

SELECT t.name AS Tabla, c.name AS Columna, c.collation_name AS Collation
FROM sys.columns AS c
JOIN sys.tables  AS t ON t.object_id = c.object_id
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
WHERE s.name = 'aire'
  AND t.name IN ('EstacionCarga', 'Estacion')
  AND c.collation_name IS NOT NULL
ORDER BY t.name, c.column_id;
