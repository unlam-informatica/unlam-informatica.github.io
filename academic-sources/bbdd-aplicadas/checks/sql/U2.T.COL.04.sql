-- u2 · Collation: conflicto entre una base con otra intercalación y tempdb, y su solución con DATABASE_DEFAULT.
ALTER DATABASE CURRENT COLLATE Modern_Spanish_CI_AS;
GO
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL PRIMARY KEY,
    Nombre    VARCHAR(30) NOT NULL
);
INSERT ventas.Cliente (ClienteId, Nombre) VALUES (1, 'Ana'), (2, 'ANA'), (3, 'Luis');

-- Las tablas temporales viven en tempdb, que usa la intercalación de la instancia.
CREATE TABLE #Excluido (Nombre VARCHAR(30) NOT NULL);
INSERT #Excluido (Nombre) VALUES ('ana');

CREATE TABLE #Resultado (Orden INT NOT NULL, Caso VARCHAR(50) NOT NULL, Resultado VARCHAR(60) NOT NULL);

INSERT #Resultado
SELECT 1, 'ventas.Cliente.Nombre', collation_name
FROM sys.columns WHERE object_id = OBJECT_ID(N'ventas.Cliente') AND name = N'Nombre';
INSERT #Resultado
SELECT 2, '#Excluido.Nombre', collation_name
FROM tempdb.sys.columns WHERE object_id = OBJECT_ID(N'tempdb..#Excluido') AND name = N'Nombre';

BEGIN TRY
    EXEC (N'SELECT c.ClienteId FROM ventas.Cliente AS c INNER JOIN #Excluido AS e ON e.Nombre = c.Nombre');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (3, 'JOIN sin COLLATE', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;
BEGIN TRY
    EXEC (N'SELECT Nombre FROM ventas.Cliente UNION SELECT Nombre FROM #Excluido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (4, 'UNION sin COLLATE', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;
BEGIN TRY
    EXEC (N'SELECT Nombre FROM ventas.Cliente INTERSECT SELECT Nombre FROM #Excluido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (5, 'INTERSECT sin COLLATE', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

INSERT #Resultado
SELECT 6, 'JOIN con DATABASE_DEFAULT', CAST(COUNT(*) AS VARCHAR(10)) + ' fila(s)'
FROM ventas.Cliente AS c
INNER JOIN #Excluido AS e
    ON e.Nombre COLLATE DATABASE_DEFAULT = c.Nombre;
INSERT #Resultado
SELECT 7, 'INTERSECT con DATABASE_DEFAULT', CAST(COUNT(*) AS VARCHAR(10)) + ' fila(s)'
FROM (
    SELECT Nombre FROM ventas.Cliente
    INTERSECT
    SELECT Nombre COLLATE DATABASE_DEFAULT FROM #Excluido
) AS i;

SELECT Caso, Resultado
FROM #Resultado
ORDER BY Orden;
