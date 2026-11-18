-- u2 · Ejercicio U2.49: la base nueva nace con el tamaño y el crecimiento de los archivos de model.
SELECT
    mf.type_desc AS Tipo,
    CASE WHEN mf.size = f.size THEN 'sí' ELSE 'no' END AS MismoTamanio,
    CASE WHEN mf.growth = f.growth AND mf.is_percent_growth = f.is_percent_growth THEN 'sí' ELSE 'no' END AS MismoCrecimiento
FROM sys.master_files AS mf
INNER JOIN sys.database_files AS f
    ON f.type = mf.type
WHERE mf.database_id = DB_ID(N'model')
ORDER BY mf.type;
