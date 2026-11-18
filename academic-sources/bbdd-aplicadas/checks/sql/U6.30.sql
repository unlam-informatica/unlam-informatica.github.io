CREATE SCHEMA comercial;
GO

CREATE TABLE comercial.Cliente (
    ClienteId      INT          NOT NULL,
    Email          VARCHAR(120) NOT NULL,
    AptoMarketing  BIT          NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE comercial.RegistroSupresion (
    ClienteId        INT  NOT NULL,
    FechaSupresion   DATE NOT NULL,
    CONSTRAINT PK_RegistroSupresion PRIMARY KEY CLUSTERED (ClienteId)
);

-- Estado "restaurado" desde una copia antigua: incluye clientes ya suprimidos
INSERT INTO comercial.Cliente (ClienteId, Email, AptoMarketing)
VALUES
    (1, 'cliente01@ejemplo.test', 1),
    (2, 'cliente02@ejemplo.test', 1),
    (3, 'cliente03@ejemplo.test', 1),
    (4, 'cliente04@ejemplo.test', 1),
    (5, 'cliente05@ejemplo.test', 0);

INSERT INTO comercial.RegistroSupresion (ClienteId, FechaSupresion)
VALUES (2, '2026-01-15'), (4, '2026-02-10');
GO

CREATE VIEW comercial.DestinatarioCampana
AS
SELECT c.ClienteId, c.Email
FROM comercial.Cliente AS c
WHERE c.AptoMarketing = 1
  AND NOT EXISTS (SELECT 1 FROM comercial.RegistroSupresion AS r WHERE r.ClienteId = c.ClienteId);
GO

DECLARE @Restaurados INT = (SELECT COUNT(*) FROM comercial.Cliente);
DECLARE @DestinatariosAntes INT = (SELECT COUNT(*) FROM comercial.DestinatarioCampana);
DECLARE @Aplicadas TABLE (ClienteId INT NOT NULL);

DELETE c
OUTPUT deleted.ClienteId INTO @Aplicadas
FROM comercial.Cliente AS c
WHERE EXISTS (SELECT 1 FROM comercial.RegistroSupresion AS r WHERE r.ClienteId = c.ClienteId);

SELECT Orden, Indicador, Valor
FROM (
    SELECT 1 AS Orden, 'Clientes restaurados' AS Indicador, @Restaurados AS Valor
    UNION ALL
    SELECT 2, 'Destinatarios de campaña con el filtro', @DestinatariosAntes
    UNION ALL
    SELECT 3, 'Supresiones reaplicadas', COUNT(*) FROM @Aplicadas
    UNION ALL
    SELECT 4, 'Clientes tras reaplicar', COUNT(*) FROM comercial.Cliente
    UNION ALL
    SELECT 5, 'Reaparecidos (debe ser 0)', COUNT(*)
    FROM comercial.Cliente AS c
    JOIN comercial.RegistroSupresion AS r ON r.ClienteId = c.ClienteId
) AS Control
ORDER BY Orden;
