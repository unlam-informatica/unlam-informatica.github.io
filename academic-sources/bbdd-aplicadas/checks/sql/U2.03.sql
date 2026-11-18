CREATE SCHEMA aire;
GO

CREATE TABLE aire.Zona (
    ZonaId        INT IDENTITY(1, 1) NOT NULL,
    NombreFlexible NVARCHAR(40) COLLATE Latin1_General_CI_AI NOT NULL,
    NombreEstricto NVARCHAR(40) COLLATE Latin1_General_CS_AS NOT NULL,
    CONSTRAINT PK_Zona PRIMARY KEY CLUSTERED (ZonaId),
    CONSTRAINT UQ_Zona_NombreFlexible UNIQUE (NombreFlexible),
    CONSTRAINT UQ_Zona_NombreEstricto UNIQUE (NombreEstricto)
);
GO

INSERT INTO aire.Zona (NombreFlexible, NombreEstricto) VALUES (N'Ñandú', N'Ñandú');

BEGIN TRY
    INSERT INTO aire.Zona (NombreFlexible, NombreEstricto) VALUES (N'NANDU', N'Ñandú2');
END TRY
BEGIN CATCH
    SELECT 'NombreFlexible' AS Columna, ERROR_NUMBER() AS Error;
END CATCH;

BEGIN TRY
    INSERT INTO aire.Zona (NombreFlexible, NombreEstricto) VALUES (N'Otra', N'ñandú');
    SELECT 'NombreEstricto' AS Columna, 0 AS Error;
END TRY
BEGIN CATCH
    SELECT 'NombreEstricto' AS Columna, ERROR_NUMBER() AS Error;
END CATCH;

SELECT ZonaId, NombreFlexible, NombreEstricto FROM aire.Zona ORDER BY ZonaId;
