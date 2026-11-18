:out /dev/null
CREATE TABLE #Espacio (NombreBase SYSNAME, LogSizeMB FLOAT, LogSpaceUsedPct FLOAT, Status INT);
INSERT #Espacio EXEC ('DBCC SQLPERF(LOGSPACE)');
GO
:out stdout
SELECT 'VLF en la base actual (sys.dm_db_log_info)' AS Concepto, CASE WHEN COUNT(*) >= 1 THEN 'al menos uno' ELSE 'ninguno' END AS Resultado
FROM sys.dm_db_log_info(DB_ID())
UNION ALL
SELECT 'Filas de DBCC SQLPERF para la base', CAST(COUNT(*) AS VARCHAR(10)) FROM #Espacio WHERE NombreBase = DB_NAME()
UNION ALL
SELECT 'Status de la base en SQLPERF', CAST(MAX(Status) AS VARCHAR(10)) FROM #Espacio WHERE NombreBase = DB_NAME()
UNION ALL
SELECT 'Porcentaje usado entre 0 y 100', CASE WHEN MAX(LogSpaceUsedPct) BETWEEN 0 AND 100 THEN 'si' ELSE 'no' END FROM #Espacio WHERE NombreBase = DB_NAME()
UNION ALL
SELECT 'Tamano del log en sys.dm_db_log_space_usage', CASE WHEN total_log_size_in_bytes > 0 THEN 'mayor que cero' ELSE 'cero' END FROM sys.dm_db_log_space_usage
ORDER BY Concepto;
