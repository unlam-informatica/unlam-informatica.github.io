-- u4 · conceptos NoSQL: alta de un usuario con dos direcciones en el modelo relacional.
CREATE SCHEMA agenda;
GO

CREATE TABLE agenda.Usuario (
    UsuarioId INT         NOT NULL,
    Nombre    VARCHAR(60) NOT NULL,
    CONSTRAINT PK_Usuario PRIMARY KEY CLUSTERED (UsuarioId)
);

CREATE TABLE agenda.Direccion (
    DireccionId INT         NOT NULL,
    UsuarioId   INT         NOT NULL,
    Ciudad      VARCHAR(60) NOT NULL,
    Pais        VARCHAR(60) NOT NULL,
    CONSTRAINT PK_Direccion         PRIMARY KEY CLUSTERED (DireccionId),
    CONSTRAINT FK_Direccion_Usuario FOREIGN KEY (UsuarioId) REFERENCES agenda.Usuario (UsuarioId)
);
GO

BEGIN TRANSACTION;
INSERT INTO agenda.Usuario (UsuarioId, Nombre) VALUES (1, 'Lucía');
INSERT INTO agenda.Direccion (DireccionId, UsuarioId, Ciudad, Pais) VALUES
    (1, 1, 'Morón', 'Argentina'),
    (2, 1, 'Montevideo', 'Uruguay');
COMMIT TRANSACTION;

SELECT u.UsuarioId, u.Nombre, d.Ciudad, d.Pais
FROM agenda.Usuario AS u
INNER JOIN agenda.Direccion AS d ON d.UsuarioId = u.UsuarioId
ORDER BY d.DireccionId;
