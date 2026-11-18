-- u4 · Data Lake: carga cruda (EL) y esquema al leer (schema on read) con OPENJSON.
CREATE SCHEMA lago;
GO

CREATE TABLE lago.EventoCrudo (
    EventoId  INT           NOT NULL,
    Contenido NVARCHAR(MAX) NOT NULL,
    CONSTRAINT PK_EventoCrudo PRIMARY KEY CLUSTERED (EventoId)
);
GO

-- Carga: se guarda lo que llega, sin validar la forma
INSERT INTO lago.EventoCrudo (EventoId, Contenido) VALUES
    (1, N'{"sensor":"S1","temp":21.5,"ts":"2026-05-01T10:00:00"}'),
    (2, N'{"sensor":"S2","temp":"19.0","ts":"2026-05-01T10:05:00","bateria":80}'),
    (3, N'{"sensor":"S1","ts":"2026-05-01T10:10:00"}'),
    (4, N'esto no es JSON');
GO

-- Esquema al leer: cada consumidor decide tipos y campos
SELECT e.EventoId, j.Sensor, j.Temp, j.Ts
FROM lago.EventoCrudo AS e
CROSS APPLY OPENJSON(e.Contenido)
    WITH (
        Sensor VARCHAR(10)   '$.sensor',
        Temp   DECIMAL(5, 1) '$.temp',
        Ts     DATETIME2(0)  '$.ts'
    ) AS j
WHERE ISJSON(e.Contenido) = 1
ORDER BY e.EventoId;
GO

-- Lo que no es JSON válido hace fallar la lectura: el control de calidad no desaparece
BEGIN TRY
    SELECT j.Sensor
    FROM lago.EventoCrudo AS e
    CROSS APPLY OPENJSON(e.Contenido) WITH (Sensor VARCHAR(10) '$.sensor') AS j
    WHERE e.EventoId = 4;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Numero, ERROR_MESSAGE() AS Mensaje;
END CATCH;
