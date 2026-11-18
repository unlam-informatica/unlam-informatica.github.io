-- u2 · model es la plantilla: la base nueva (la del script) hereda sus propiedades.
SELECT
    p.Propiedad,
    p.Modelo,
    p.BaseNueva,
    CASE WHEN p.Modelo = p.BaseNueva THEN 'sí' ELSE 'no' END AS Coincide
FROM (
    SELECT 1 AS Orden, N'Intercalación' COLLATE DATABASE_DEFAULT AS Propiedad,
           CAST(m.collation_name AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT AS Modelo, CAST(n.collation_name AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT AS BaseNueva
    FROM sys.databases AS m CROSS JOIN sys.databases AS n
    WHERE m.name = N'model' AND n.database_id = DB_ID()
    UNION ALL
    SELECT 2, N'Modelo de recuperación', CAST(m.recovery_model_desc AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT, CAST(n.recovery_model_desc AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT
    FROM sys.databases AS m CROSS JOIN sys.databases AS n
    WHERE m.name = N'model' AND n.database_id = DB_ID()
    UNION ALL
    SELECT 3, N'Nivel de compatibilidad', CAST(m.compatibility_level AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT, CAST(n.compatibility_level AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT
    FROM sys.databases AS m CROSS JOIN sys.databases AS n
    WHERE m.name = N'model' AND n.database_id = DB_ID()
) AS p
ORDER BY p.Orden;
