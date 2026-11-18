:out stdout
SELECT 'IsHadrEnabled' AS Propiedad, CAST(SERVERPROPERTY('IsHadrEnabled') AS VARCHAR(10)) AS Valor
UNION ALL SELECT 'IsClustered', CAST(SERVERPROPERTY('IsClustered') AS VARCHAR(10))
UNION ALL SELECT 'Grupos en sys.availability_groups', CAST(COUNT(*) AS VARCHAR(10)) FROM sys.availability_groups
UNION ALL SELECT 'Replicas en sys.availability_replicas', CAST(COUNT(*) AS VARCHAR(10)) FROM sys.availability_replicas
ORDER BY Propiedad;
