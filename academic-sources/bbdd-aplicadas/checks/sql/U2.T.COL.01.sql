-- u2 · Collation: instancia > base de datos > columna.
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Producto (
    ProductoId  INT          NOT NULL PRIMARY KEY,
    Codigo      VARCHAR(20)  COLLATE Latin1_General_CS_AS NOT NULL,
    Descripcion VARCHAR(100) NOT NULL
);

SELECT Nivel, Intercalacion
FROM (
    SELECT 1 AS Orden, 'instancia' AS Nivel, CAST(SERVERPROPERTY('Collation') AS NVARCHAR(128)) AS Intercalacion
    UNION ALL
    SELECT 2, 'base de datos', collation_name
    FROM sys.databases
    WHERE database_id = DB_ID()
    UNION ALL
    SELECT 3, 'columna ' + name, collation_name
    FROM sys.columns
    WHERE object_id = OBJECT_ID(N'ventas.Producto') AND collation_name IS NOT NULL
) AS n
ORDER BY Orden, Nivel;
