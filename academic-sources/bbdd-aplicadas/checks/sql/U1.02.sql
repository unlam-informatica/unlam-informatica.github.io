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
GO

CREATE TABLE biblioteca.Libro (
    LibroId     INT IDENTITY(1, 1) NOT NULL,
    Titulo      VARCHAR(100)       NOT NULL,
    GeneroId    INT                NOT NULL,
    AnioEdicion SMALLINT           NOT NULL,
    Ejemplares  INT                NOT NULL CONSTRAINT DF_Libro_Ejemplares DEFAULT (1),
    Precio      DECIMAL(10, 2)     NOT NULL,
    CONSTRAINT PK_Libro            PRIMARY KEY CLUSTERED (LibroId),
    CONSTRAINT FK_Libro_Genero     FOREIGN KEY (GeneroId) REFERENCES biblioteca.Genero (GeneroId),
    CONSTRAINT CK_Libro_Anio       CHECK (AnioEdicion BETWEEN 1900 AND 2100),
    CONSTRAINT CK_Libro_Ejemplares CHECK (Ejemplares >= 0),
    CONSTRAINT CK_Libro_Precio     CHECK (Precio > 0)
);

CREATE TABLE biblioteca.Prestamo (
    PrestamoId      INT IDENTITY(1, 1) NOT NULL,
    SocioId         INT                NOT NULL,
    LibroId         INT                NOT NULL,
    FechaPrestamo   DATE               NOT NULL,
    FechaDevolucion DATE               NULL,
    CONSTRAINT PK_Prestamo        PRIMARY KEY CLUSTERED (PrestamoId),
    CONSTRAINT FK_Prestamo_Socio  FOREIGN KEY (SocioId) REFERENCES biblioteca.Socio (SocioId),
    CONSTRAINT FK_Prestamo_Libro  FOREIGN KEY (LibroId) REFERENCES biblioteca.Libro (LibroId),
    CONSTRAINT CK_Prestamo_Fechas CHECK (FechaDevolucion IS NULL OR FechaDevolucion >= FechaPrestamo)
);

CREATE TABLE biblioteca.Resena (
    ResenaId   INT IDENTITY(1, 1) NOT NULL,
    LibroId    INT                NOT NULL,
    SocioId    INT                NULL,
    Puntaje    TINYINT            NOT NULL,
    Comentario VARCHAR(200)       NULL,
    CONSTRAINT PK_Resena       PRIMARY KEY CLUSTERED (ResenaId),
    CONSTRAINT FK_Resena_Libro FOREIGN KEY (LibroId) REFERENCES biblioteca.Libro (LibroId)
        ON DELETE CASCADE,
    CONSTRAINT FK_Resena_Socio FOREIGN KEY (SocioId) REFERENCES biblioteca.Socio (SocioId)
        ON DELETE SET NULL,
    CONSTRAINT CK_Resena_Puntaje CHECK (Puntaje BETWEEN 1 AND 5)
);

INSERT INTO biblioteca.Genero (Nombre) VALUES ('Novela'), ('Poesia');
INSERT INTO biblioteca.Socio (Codigo, Nombre, Email) VALUES ('S00001', 'Socio Uno', 'socio01@ejemplo.test');
INSERT INTO biblioteca.Libro (Titulo, GeneroId, AnioEdicion, Precio)
VALUES ('Cuentos del Sur', 1, 2015, 2500.00), ('La Ciudad Quieta', 1, 2019, 3200.00);
INSERT INTO biblioteca.Resena (LibroId, SocioId, Puntaje)
VALUES (1, 1, 5), (2, 1, 4);

DECLARE @Resultado TABLE (Orden INT, Caso VARCHAR(60), Resultado VARCHAR(30));

BEGIN TRY
    DELETE FROM biblioteca.Genero WHERE Nombre = 'Novela';
    INSERT INTO @Resultado VALUES (1, 'Borrar genero con libros', 'ok');
END TRY
BEGIN CATCH
    INSERT INTO @Resultado VALUES (1, 'Borrar genero con libros', CONCAT('error ', ERROR_NUMBER()));
END CATCH;

DELETE FROM biblioteca.Libro WHERE Titulo = 'Cuentos del Sur';
INSERT INTO @Resultado
SELECT 2, 'Resenas tras borrar el libro 1', CAST(COUNT(*) AS VARCHAR(30))
FROM biblioteca.Resena;

DELETE FROM biblioteca.Socio WHERE Codigo = 'S00001';
INSERT INTO @Resultado
SELECT 3, 'Resenas con SocioId NULL tras borrar el socio', CAST(COUNT(*) AS VARCHAR(30))
FROM biblioteca.Resena
WHERE SocioId IS NULL;

SELECT Caso, Resultado FROM @Resultado ORDER BY Orden;
