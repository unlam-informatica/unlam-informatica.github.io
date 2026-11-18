-- SIN-PRELUDE
-- Ejercicio U5.11: el autenticador ata el texto cifrado a su fila.
CREATE SCHEMA salud;
GO
CREATE TABLE salud.Paciente
(
    PacienteId       INT          NOT NULL CONSTRAINT PK_Paciente PRIMARY KEY,
    Documento        VARCHAR(20)  NOT NULL,
    DocumentoCifrado VARBINARY(256) NULL
);
INSERT salud.Paciente (PacienteId, Documento)
VALUES (1, '00000001'), (2, '00000002');
GO
DECLARE @Frase NVARCHAR(128) = N'Frase-didactica-U5-11';

UPDATE salud.Paciente
SET DocumentoCifrado = EncryptByPassPhrase(@Frase, Documento, 1, CONVERT(VARBINARY(128), PacienteId));

-- Alguien copia el texto cifrado del paciente 1 sobre el paciente 2.
UPDATE salud.Paciente
SET DocumentoCifrado = (SELECT DocumentoCifrado FROM salud.Paciente WHERE PacienteId = 1)
WHERE PacienteId = 2;

SELECT PacienteId,
       CONVERT(VARCHAR(20), DecryptByPassPhrase(@Frase, DocumentoCifrado, 1, CONVERT(VARBINARY(128), PacienteId))) AS DocumentoDescifrado
FROM salud.Paciente
ORDER BY PacienteId;
