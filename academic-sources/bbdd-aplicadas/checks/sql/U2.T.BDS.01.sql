-- u2 · Bases de sistema: las cuatro visibles en sys.databases, y la base de recursos, que no aparece.
SELECT name AS BaseDeDatos, database_id AS Id
FROM sys.databases
WHERE database_id <= 4
ORDER BY database_id;

SELECT
    CASE WHEN DB_ID() > 4 THEN 'usuario' ELSE 'sistema' END AS BaseActual,
    ISNULL(CAST(DB_ID(N'mssqlsystemresource') AS VARCHAR(10)), 'NULL') AS IdBaseDeRecursos;
