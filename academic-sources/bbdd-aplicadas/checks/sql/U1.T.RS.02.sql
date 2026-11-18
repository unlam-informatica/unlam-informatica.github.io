-- u1 · repaso: tipos de fecha/hora y de cadena.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.EjemploTipo (
    EjemploTipoId INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    Dia           DATE,
    Hora          TIME(0),
    Momento       DATETIME2(3),
    MomentoZona   DATETIMEOFFSET(0),
    CodigoFijo    CHAR(5),
    NombreVar     VARCHAR(5),
    NombreNchar   NCHAR(5),
    NombreNvar    NVARCHAR(5),
    Detalle       VARCHAR(MAX)
);

INSERT INTO academia.EjemploTipo
    (Dia, Hora, Momento, MomentoZona, CodigoFijo, NombreVar, NombreNchar, NombreNvar, Detalle)
VALUES
    ('2026-03-01', '14:30:15', '2026-03-01T14:30:15.1234', '2026-03-01T14:30:15-03:00',
     'AB', 'AB', N'AB', N'AB', REPLICATE(CAST('x' AS VARCHAR(MAX)), 10000));

SELECT
    Dia,
    Hora,
    Momento,
    MomentoZona,
    DATALENGTH(CodigoFijo)  AS BytesChar,
    DATALENGTH(NombreVar)   AS BytesVarchar,
    DATALENGTH(NombreNchar) AS BytesNchar,
    DATALENGTH(NombreNvar)  AS BytesNvarchar,
    LEN(Detalle)            AS LargoDetalle
FROM academia.EjemploTipo;
