CREATE SCHEMA carrera;
GO

CREATE TABLE carrera.Corredor (
    CorredorId INT         NOT NULL,
    Nombre     VARCHAR(30) NOT NULL,
    Categoria  VARCHAR(10) NOT NULL,
    CONSTRAINT PK_Corredor PRIMARY KEY (CorredorId),
    CONSTRAINT CK_Corredor_Categoria CHECK (Categoria IN ('Elite', 'Amateur'))
);

CREATE TABLE carrera.Etapa (
    EtapaId INT         NOT NULL,
    Nombre  VARCHAR(30) NOT NULL,
    Km      INT         NOT NULL,
    CONSTRAINT PK_Etapa PRIMARY KEY (EtapaId),
    CONSTRAINT CK_Etapa_Km CHECK (Km > 0)
);

CREATE TABLE carrera.Tiempo (
    CorredorId INT NOT NULL,
    EtapaId    INT NOT NULL,
    Minutos    INT NOT NULL,
    CONSTRAINT PK_Tiempo PRIMARY KEY (CorredorId, EtapaId),
    CONSTRAINT FK_Tiempo_Corredor FOREIGN KEY (CorredorId) REFERENCES carrera.Corredor (CorredorId),
    CONSTRAINT FK_Tiempo_Etapa FOREIGN KEY (EtapaId) REFERENCES carrera.Etapa (EtapaId),
    CONSTRAINT CK_Tiempo_Minutos CHECK (Minutos > 0)
);

INSERT INTO carrera.Corredor (CorredorId, Nombre, Categoria)
VALUES
    (1, 'Lola',  'Elite'),
    (2, 'Mateo', 'Elite'),
    (3, 'Nora',  'Elite'),
    (4, 'Omar',  'Elite'),
    (5, 'Pia',   'Amateur'),
    (6, 'Rafa',  'Amateur'),
    (7, 'Sol',   'Amateur'),
    (8, 'Tito',  'Amateur');

INSERT INTO carrera.Etapa (EtapaId, Nombre, Km)
VALUES
    (1, 'Llano',        40),
    (2, 'Montana',      55),
    (3, 'Contrarreloj', 20),
    (4, 'Sierras',      65),
    (5, 'Final',        30);

-- Tito abandona antes de la etapa 4: no tiene tiempos en las etapas 4 y 5
INSERT INTO carrera.Tiempo (CorredorId, EtapaId, Minutos)
VALUES
    (1, 1, 62), (2, 1, 64), (3, 1, 64), (4, 1, 66), (5, 1, 70), (6, 1, 69), (7, 1, 72), (8, 1, 72),
    (1, 2, 90), (2, 2, 88), (3, 2, 91), (4, 2, 91), (5, 2, 99), (6, 2, 97), (7, 2, 97), (8, 2, 104),
    (1, 3, 30), (2, 3, 31), (3, 3, 29), (4, 3, 31), (5, 3, 36), (6, 3, 35), (7, 3, 33), (8, 3, 38),
    (1, 4, 98), (2, 4, 101), (3, 4, 96), (4, 4, 100), (5, 4, 112), (6, 4, 108), (7, 4, 110),
    (1, 5, 47), (2, 5, 45), (3, 5, 49), (4, 5, 48), (5, 5, 55), (6, 5, 52), (7, 5, 50);
GO
SELECT
    ROW_NUMBER() OVER (ORDER BY t.Minutos, t.CorredorId) AS NroLlegada,
    c.Nombre,
    t.Minutos
FROM carrera.Tiempo AS t
INNER JOIN carrera.Corredor AS c
    ON c.CorredorId = t.CorredorId
WHERE t.EtapaId = 1
ORDER BY NroLlegada;
