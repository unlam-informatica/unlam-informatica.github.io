-- u2 · Tablas temporales y variables de tabla: dónde viven y quién las ve.
CREATE TABLE #Temporal (Id INT NOT NULL PRIMARY KEY, Texto VARCHAR(10) NOT NULL);
INSERT #Temporal (Id, Texto) VALUES (11, 'Hola');

CREATE TABLE ##TemporalGlobalU2 (Id INT NOT NULL PRIMARY KEY, Texto VARCHAR(20) NOT NULL);
INSERT ##TemporalGlobalU2 (Id, Texto) VALUES (1, 'Compartida');

DECLARE @Variable TABLE (Id INT NOT NULL);
INSERT @Variable (Id) VALUES (1);

SELECT
    CASE WHEN t.name LIKE N'##%' THEN 'global (##)' ELSE 'local (#)' END AS Tipo,
    CASE WHEN t.name LIKE N'##%' THEN t.name ELSE LEFT(t.name, 9) END     AS NombreEnTempdb,
    CASE WHEN EXISTS (SELECT 1 FROM sys.tables WHERE name LIKE N'#Temporal%') THEN 'sí' ELSE 'no' END AS EnLaBaseActual
FROM tempdb.sys.tables AS t
WHERE t.object_id IN (OBJECT_ID(N'tempdb..#Temporal'), OBJECT_ID(N'tempdb..##TemporalGlobalU2'))
ORDER BY t.name;

-- Sea cual sea la base que se escriba delante, la tabla temporal se resuelve en tempdb.
SELECT Id, Texto FROM master.dbo.#Temporal;
GO
DROP TABLE ##TemporalGlobalU2;
