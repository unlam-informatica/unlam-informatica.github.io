-- u2 · Bases de sistema: archivos de master, model y msdb; tempdb tiene datos y un único log.
SELECT
    DB_NAME(database_id) AS BaseDeDatos,
    name                 AS NombreLogico,
    type_desc            AS Tipo
FROM sys.master_files
WHERE database_id IN (1, 3, 4)
ORDER BY database_id, file_id;

SELECT
    CASE WHEN SUM(CASE WHEN type_desc = 'ROWS' THEN 1 ELSE 0 END) >= 1 THEN 'sí' ELSE 'no' END AS TieneArchivosDeDatos,
    SUM(CASE WHEN type_desc = 'LOG'  THEN 1 ELSE 0 END)       AS ArchivosDeLog
FROM sys.master_files
WHERE database_id = 2;
