-- u2 · Ejercicio U2.48: modelo de recuperación de las bases de sistema.
SELECT name AS BaseDeDatos, database_id AS Id, recovery_model_desc AS ModeloDeRecuperacion
FROM sys.databases
WHERE database_id <= 4
ORDER BY database_id;
