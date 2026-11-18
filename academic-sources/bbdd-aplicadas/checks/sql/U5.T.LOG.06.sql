-- u5 · log-recuperacion: consulta de cantidad y tamaño promedio de VLF por base (código de la página).
-- La salida depende de la instancia; se guarda en una tabla temporal y se verifica que la consulta
-- compila, devuelve la base actual y que cada base tiene al menos un VLF.
CREATE TABLE #Vlf (name SYSNAME, CantidadVlf INT, PromedioMb DECIMAL(12, 2));
INSERT #Vlf
SELECT d.name,
       COUNT(*) AS CantidadVlf,
       CONVERT(DECIMAL(12, 2), AVG(v.vlf_size_mb)) AS PromedioMb
FROM sys.databases AS d
CROSS APPLY sys.dm_db_log_info(d.database_id) AS v
GROUP BY d.name
ORDER BY CantidadVlf DESC;
SELECT IIF(EXISTS (SELECT 1 FROM #Vlf WHERE name = DB_NAME()), 'base actual presente', 'falta la base actual') AS Control
UNION ALL
SELECT IIF(NOT EXISTS (SELECT 1 FROM #Vlf WHERE CantidadVlf < 1), 'toda base tiene al menos un VLF', 'hay bases sin VLF');
