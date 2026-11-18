CREATE SCHEMA privacidad;
GO

CREATE TABLE privacidad.Paciente (
    PacienteId INT           NOT NULL,
    Dni        VARCHAR(20)   NOT NULL,
    Nombre     NVARCHAR(100) NOT NULL,
    Email      VARCHAR(120)  NULL,
    Telefono   VARCHAR(20)   NULL,
    CONSTRAINT PK_Paciente PRIMARY KEY CLUSTERED (PacienteId)
);

CREATE TABLE privacidad.Turno (
    TurnoId      INT           NOT NULL,
    PacienteId   INT           NULL,
    Especialidad VARCHAR(40)   NOT NULL,
    FechaTurno   DATE          NOT NULL,
    Diagnostico  VARCHAR(200)  NULL,
    Medico       NVARCHAR(100) NOT NULL,
    CONSTRAINT PK_Turno PRIMARY KEY CLUSTERED (TurnoId),
    CONSTRAINT FK_Turno_Paciente FOREIGN KEY (PacienteId) REFERENCES privacidad.Paciente (PacienteId)
);

CREATE TABLE privacidad.Consentimiento (
    ConsentimientoId INT         NOT NULL,
    PacienteId       INT         NOT NULL,
    Finalidad        VARCHAR(40) NOT NULL,
    Otorgado         BIT         NOT NULL,
    Fecha            DATE        NOT NULL,
    CONSTRAINT PK_Consentimiento PRIMARY KEY CLUSTERED (ConsentimientoId),
    CONSTRAINT FK_Consentimiento_Paciente FOREIGN KEY (PacienteId) REFERENCES privacidad.Paciente (PacienteId)
);

CREATE TABLE privacidad.ContactoMarketing (
    ContactoId           INT          NOT NULL,
    PacienteId           INT          NULL,
    Email                VARCHAR(120) NOT NULL,
    FechaUltimaActividad DATE         NOT NULL,
    Baja                 BIT          NOT NULL,
    CONSTRAINT PK_ContactoMarketing PRIMARY KEY CLUSTERED (ContactoId),
    CONSTRAINT FK_ContactoMarketing_Paciente FOREIGN KEY (PacienteId) REFERENCES privacidad.Paciente (PacienteId)
);

INSERT INTO privacidad.Paciente (PacienteId, Dni, Nombre, Email, Telefono)
VALUES
    (1, '00000001', N'Paciente Uno',  'paciente01@ejemplo.test', '11-5550-0101'),
    (2, '00000002', N'Paciente Dos',  'paciente02@ejemplo.test', NULL),
    (3, '00000003', N'Paciente Tres', 'paciente03@ejemplo.test', '11-5550-0103');

INSERT INTO privacidad.Turno (TurnoId, PacienteId, Especialidad, FechaTurno, Diagnostico, Medico)
VALUES
    (1, 1, 'Cardiologia',  '2020-03-10', 'Diagnostico ficticio A', N'Medico Alfa'),
    (2, 1, 'Clinica',      '2026-05-20', 'Diagnostico ficticio B', N'Medico Beta'),
    (3, 2, 'Clinica',      '2019-11-05', 'Diagnostico ficticio C', N'Medico Beta'),
    (4, 3, 'Dermatologia', '2026-06-15', 'Diagnostico ficticio D', N'Medico Alfa');

INSERT INTO privacidad.Consentimiento (ConsentimientoId, PacienteId, Finalidad, Otorgado, Fecha)
VALUES
    (1, 1, 'Marketing', 1, '2025-04-01'),
    (2, 2, 'Marketing', 1, '2023-01-15'),
    (3, 3, 'Marketing', 0, '2022-08-30');

INSERT INTO privacidad.ContactoMarketing (ContactoId, PacienteId, Email, FechaUltimaActividad, Baja)
VALUES
    (1, 1,    'paciente01@ejemplo.test',  '2026-04-01', 0),
    (2, 2,    'paciente02@ejemplo.test',  '2023-01-15', 0),
    (3, 3,    'paciente03@ejemplo.test',  '2022-08-30', 1),
    (4, NULL, 'prospecto01@ejemplo.test', '2025-12-01', 0);
GO

DECLARE @Sal VARBINARY(16) = 0x00112233445566778899AABBCCDDEEFF;

SELECT
    LEFT(CONVERT(CHAR(64), h.Valor, 2), 16) AS SeudonimoInicio,
    COUNT(*) AS Turnos
FROM privacidad.Turno AS t
JOIN privacidad.Paciente AS p ON p.PacienteId = t.PacienteId
CROSS APPLY (SELECT HASHBYTES('SHA2_256', @Sal + CONVERT(VARBINARY(20), p.Dni)) AS Valor) AS h
GROUP BY h.Valor
ORDER BY SeudonimoInicio;
GO

DECLARE @Sal VARBINARY(16) = 0x00112233445566778899AABBCCDDEEFF;

WITH Candidato AS (
    SELECT RIGHT(CONCAT('00000000', value), 8) AS Dni
    FROM GENERATE_SERIES(1, 5)
),
Publicado AS (
    SELECT PacienteId,
           HASHBYTES('SHA2_256', Dni)                                AS HashSinSal,
           HASHBYTES('SHA2_256', @Sal + CONVERT(VARBINARY(20), Dni)) AS HashConSal
    FROM privacidad.Paciente
)
SELECT 'Con sal' AS Variante, COUNT(*) AS PacientesRecuperados
FROM Publicado AS pu
JOIN Candidato AS c ON pu.HashConSal = HASHBYTES('SHA2_256', c.Dni)
UNION ALL
SELECT 'Sin sal', COUNT(*)
FROM Publicado AS pu
JOIN Candidato AS c ON pu.HashSinSal = HASHBYTES('SHA2_256', c.Dni)
ORDER BY Variante;
