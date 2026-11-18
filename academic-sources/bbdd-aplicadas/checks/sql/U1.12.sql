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

INSERT INTO biblioteca.Genero (Nombre)
VALUES ('Novela'), ('Ciencia'), ('Historia'), ('Poesia');

INSERT INTO biblioteca.Socio (Codigo, Nombre, Email, Categoria, FechaAlta, Activo)
VALUES ('S00001', 'Socio Uno',    'socio01@ejemplo.test', 'Estudiante', '2024-03-01', 1),
       ('S00002', 'Socio Dos',    'socio02@ejemplo.test', 'General',    '2024-03-15', 1),
       ('S00003', 'Socio Tres',   'socio03@ejemplo.test', 'Estudiante', '2024-04-02', 1),
       ('S00004', 'Socio Cuatro', NULL,                   'Jubilado',   '2024-04-20', 1),
       ('S00005', 'Socio Cinco',  'socio05@ejemplo.test', 'General',    '2024-05-10', 1),
       ('S00006', 'Socio Seis',   'socio06@ejemplo.test', 'Estudiante', '2024-06-01', 0);

INSERT INTO biblioteca.Libro (Titulo, GeneroId, AnioEdicion, Ejemplares, Precio)
VALUES ('Cuentos del Sur',          1, 2015, 3, 2500.00),
       ('La Ciudad Quieta',         1, 2019, 2, 3200.00),
       ('Orbitas y Mareas',         2, 2020, 4, 4100.00),
       ('Atlas de Particulas',      2, 2018, 1, 5200.00),
       ('Manual de Quimica Basica', 2, 2011, 0, 3000.00),
       ('Cronicas del Litoral',     3, 2008, 2, 2800.00),
       ('Rios y Fronteras',         3, 2021, 3, 3600.00),
       ('Memorias de un Puerto',    3, 2016, 1, 2900.00);

INSERT INTO biblioteca.Prestamo (SocioId, LibroId, FechaPrestamo, FechaDevolucion)
VALUES (1, 1, '2025-03-03', '2025-03-10'),
       (1, 3, '2025-03-12', '2025-03-30'),
       (1, 7, '2025-04-02', NULL),
       (2, 1, '2025-03-05', '2025-03-12'),
       (2, 2, '2025-04-07', NULL),
       (3, 3, '2025-03-20', '2025-04-01'),
       (3, 4, '2025-04-15', '2025-04-20'),
       (3, 7, '2025-05-02', '2025-05-09'),
       (3, 6, '2025-05-10', NULL),
       (4, 6, '2025-04-22', '2025-05-01');

INSERT INTO biblioteca.Resena (LibroId, SocioId, Puntaje, Comentario)
VALUES (1, 5, 5, 'Muy buena'),
       (1, 1, 4, NULL),
       (3, 5, 4, 'Clara y breve'),
       (7, 3, 3, NULL);
GO

CREATE TABLE biblioteca.Bitacora (
    BitacoraId INT IDENTITY(1, 1) NOT NULL,
    Fecha      DATETIME2(0)       NOT NULL CONSTRAINT DF_Bitacora_Fecha DEFAULT (SYSDATETIME()),
    Modulo     VARCHAR(40)        NOT NULL,
    Mensaje    VARCHAR(200)       NOT NULL,
    CONSTRAINT PK_Bitacora PRIMARY KEY CLUSTERED (BitacoraId)
);
GO

CREATE PROCEDURE biblioteca.RegistrarBitacora
    @Modulo     VARCHAR(40),
    @Mensaje    VARCHAR(200) = NULL,
    @BitacoraId INT          = NULL OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    IF NULLIF(LTRIM(RTRIM(@Modulo)), '') IS NULL
        THROW 50001, 'El modulo es obligatorio.', 1;

    INSERT INTO biblioteca.Bitacora (Modulo, Mensaje)
    VALUES (LTRIM(RTRIM(@Modulo)), COALESCE(NULLIF(LTRIM(RTRIM(@Mensaje)), ''), 'Sin detalle'));

    SET @BitacoraId = SCOPE_IDENTITY();
END;
GO

DECLARE @Id INT;

EXEC biblioteca.RegistrarBitacora @Modulo = 'Carga', @Mensaje = 'Inicio de la carga', @BitacoraId = @Id OUTPUT;
EXEC biblioteca.RegistrarBitacora @Modulo = 'Carga', @Mensaje = '   ';
DECLARE @Texto VARCHAR(200) = CONCAT('Primer id: ', @Id);
EXEC biblioteca.RegistrarBitacora @Modulo = 'Prueba', @Mensaje = @Texto;

BEGIN TRY
    EXEC biblioteca.RegistrarBitacora @Modulo = '  ', @Mensaje = 'No deberia guardarse';
END TRY
BEGIN CATCH
    SET @Texto = CONCAT('Numero ', ERROR_NUMBER());
    EXEC biblioteca.RegistrarBitacora @Modulo = 'Error', @Mensaje = @Texto;
END CATCH;

SELECT BitacoraId, Modulo, Mensaje
FROM biblioteca.Bitacora
ORDER BY BitacoraId;
