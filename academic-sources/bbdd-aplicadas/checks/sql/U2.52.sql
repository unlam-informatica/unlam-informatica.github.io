-- u2 · Ejercicio U2.52: una tabla temporal con la intercalación de la base evita los conflictos.
ALTER DATABASE CURRENT COLLATE Modern_Spanish_CI_AS;
GO
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Producto (
    ProductoId INT         NOT NULL PRIMARY KEY,
    Rubro      VARCHAR(20) NOT NULL
);
INSERT ventas.Producto (ProductoId, Rubro) VALUES (1, 'Limpieza'), (2, 'Bazar'), (3, 'LIMPIEZA');

-- Sin COLLATE, esta tabla usaría la intercalación de tempdb y la comparación daría el error 468.
CREATE TABLE #RubroActivo (Rubro VARCHAR(20) COLLATE DATABASE_DEFAULT NOT NULL);
INSERT #RubroActivo (Rubro) VALUES ('limpieza');

SELECT
    p.ProductoId,
    p.Rubro,
    (SELECT collation_name FROM tempdb.sys.columns
     WHERE object_id = OBJECT_ID(N'tempdb..#RubroActivo') AND name = N'Rubro') AS IntercalacionTemporal
FROM ventas.Producto AS p
INNER JOIN #RubroActivo AS r
    ON r.Rubro = p.Rubro
ORDER BY p.ProductoId;
