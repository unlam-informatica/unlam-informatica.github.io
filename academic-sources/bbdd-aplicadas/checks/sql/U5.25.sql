:out stdout
SELECT CASE WHEN SERVERPROPERTY('IsHadrEnabled') = 1 THEN 'Si' ELSE 'No' END AS AlwaysOnHabilitado,
       CASE WHEN SERVERPROPERTY('IsClustered') = 1 THEN 'Si' ELSE 'No' END AS InstanciaEnCluster,
       (SELECT COUNT(*) FROM sys.availability_groups) AS GruposDeDisponibilidad,
       (SELECT COUNT(*) FROM sys.availability_replicas) AS Replicas;
