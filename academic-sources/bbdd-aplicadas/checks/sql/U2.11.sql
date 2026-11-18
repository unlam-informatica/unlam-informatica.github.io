CREATE SCHEMA prueba;
GO

CREATE TABLE prueba.BarrioFlexible (Nombre NVARCHAR(40) COLLATE Latin1_General_CI_AI NOT NULL);
CREATE TABLE prueba.BarrioEstricto (Nombre NVARCHAR(40) COLLATE Latin1_General_CS_AS NOT NULL);
GO

INSERT INTO prueba.BarrioFlexible (Nombre) VALUES (N'San José'), (N'Villa Ocampo'), (N'Nuñez');
INSERT INTO prueba.BarrioEstricto (Nombre) VALUES (N'San Jose'), (N'Villa Ocampo'), (N'Nuñez');
GO

-- 1) Sin resolver: cada operación falla con el error 468 (se ejecuta con EXEC para poder capturarlo:
--    el conflicto se detecta al compilar la sentencia)
BEGIN TRY
    EXEC (N'SELECT f.Nombre FROM prueba.BarrioFlexible AS f JOIN prueba.BarrioEstricto AS e ON e.Nombre = f.Nombre;');
END TRY
BEGIN CATCH
    SELECT 'JOIN' AS Operacion, ERROR_NUMBER() AS Error;
END CATCH;

BEGIN TRY
    EXEC (N'SELECT Nombre FROM prueba.BarrioFlexible INTERSECT SELECT Nombre FROM prueba.BarrioEstricto;');
END TRY
BEGIN CATCH
    SELECT 'INTERSECT' AS Operacion, ERROR_NUMBER() AS Error;
END CATCH;
GO

-- 2) Resuelto: la collation de la comparación se elige con COLLATE, y cambia el resultado
SELECT Nombre FROM prueba.BarrioFlexible
INTERSECT
SELECT Nombre COLLATE Latin1_General_CI_AI FROM prueba.BarrioEstricto
ORDER BY Nombre;

SELECT Nombre COLLATE Latin1_General_CS_AS AS Nombre FROM prueba.BarrioFlexible
INTERSECT
SELECT Nombre FROM prueba.BarrioEstricto
ORDER BY Nombre;
