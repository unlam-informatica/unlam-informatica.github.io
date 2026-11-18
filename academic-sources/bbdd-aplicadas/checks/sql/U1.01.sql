CREATE SCHEMA biblioteca;
GO

CREATE TABLE biblioteca.Genero (
    GeneroId INT IDENTITY(1, 1) NOT NULL,
    Nombre   VARCHAR(40)        NOT NULL,
    CONSTRAINT PK_Genero        PRIMARY KEY CLUSTERED (GeneroId),
    CONSTRAINT UQ_Genero_Nombre UNIQUE (Nombre)
);

CREATE TABLE biblioteca.Socio (
    SocioId   INT IDENTITY(1, 1) NOT NULL,
    Codigo    CHAR(6)            NOT NULL,
    Nombre    VARCHAR(60)        NOT NULL,
    Email     VARCHAR(100)       NULL,
    Categoria VARCHAR(10)        NOT NULL CONSTRAINT DF_Socio_Categoria DEFAULT ('General'),
    FechaAlta DATE               NOT NULL CONSTRAINT DF_Socio_FechaAlta DEFAULT (CAST(GETDATE() AS DATE)),
    Activo    BIT                NOT NULL CONSTRAINT DF_Socio_Activo DEFAULT (1),
    CONSTRAINT PK_Socio           PRIMARY KEY CLUSTERED (SocioId),
    CONSTRAINT UQ_Socio_Codigo    UNIQUE (Codigo),
    CONSTRAINT UQ_Socio_Email     UNIQUE (Email),
    CONSTRAINT CK_Socio_Codigo    CHECK (Codigo LIKE 'S[0-9][0-9][0-9][0-9][0-9]'),
    CONSTRAINT CK_Socio_Categoria CHECK (Categoria IN ('Estudiante', 'General', 'Jubilado'))
);

SELECT TABLE_NAME AS Tabla,
       COLUMN_NAME AS Columna,
       DATA_TYPE AS Tipo,
       IS_NULLABLE AS AdmiteNulos
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'biblioteca'
ORDER BY TABLE_NAME, ORDINAL_POSITION;
