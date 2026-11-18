CREATE TABLE #Parcial (Estacion CHAR(3) NOT NULL, Pm25 DECIMAL(5, 1) NOT NULL);
DECLARE @Parcial TABLE (Estacion CHAR(3) NOT NULL, Pm25 DECIMAL(5, 1) NOT NULL);

INSERT INTO #Parcial  (Estacion, Pm25) VALUES ('E01', 12.5), ('E01', 15.0);
INSERT INTO @Parcial  (Estacion, Pm25) VALUES ('E01', 12.5), ('E01', 15.0);

SELECT 'mismo lote' AS Donde,
       (SELECT COUNT(*) FROM #Parcial) AS FilasTemporal,
       (SELECT COUNT(*) FROM @Parcial) AS FilasVariable;
GO

-- Lote nuevo: la tabla temporal sigue en la sesión; la variable ya no existe
SELECT 'lote siguiente' AS Donde, COUNT(*) AS FilasTemporal FROM #Parcial;

BEGIN TRY
    EXEC (N'SELECT COUNT(*) FROM @Parcial;');
END TRY
BEGIN CATCH
    SELECT 'variable en otro lote' AS Intento, ERROR_NUMBER() AS Error;
END CATCH;

-- El SQL dinámico es un ámbito hijo: ve la tabla temporal local de quien lo invoca
EXEC (N'SELECT ''dinámico'' AS Donde, COUNT(*) AS FilasTemporal FROM #Parcial;');

DROP TABLE #Parcial;
