-- u2 · Arquitectura: una base de datos de usuario son (al menos) un archivo de datos y uno de log.
SELECT
    file_id    AS ArchivoId,
    type_desc  AS Tipo,
    RIGHT(physical_name, 4) AS Extension
FROM sys.database_files
ORDER BY file_id;
