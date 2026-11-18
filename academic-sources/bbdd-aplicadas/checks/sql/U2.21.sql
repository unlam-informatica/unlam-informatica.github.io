CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Cliente (
    ClienteId INT           NOT NULL,
    Nombre    NVARCHAR(60)  NOT NULL,
    Localidad NVARCHAR(30)  NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE ventas.ClienteContacto (
    ClienteId INT           NOT NULL,
    Email     VARCHAR(80)   NOT NULL,
    CONSTRAINT PK_ClienteContacto PRIMARY KEY CLUSTERED (ClienteId, Email),
    CONSTRAINT FK_ClienteContacto_Cliente FOREIGN KEY (ClienteId) REFERENCES ventas.Cliente (ClienteId)
);

CREATE TABLE ventas.ArchivoCliente (
    Contenido VARCHAR(MAX) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NOT NULL
);
GO

INSERT INTO ventas.ArchivoCliente (Contenido)
SELECT a.BulkColumn
FROM OPENROWSET(BULK '{{FIXTURES}}/cliente_acentos.json', SINGLE_BLOB) AS a;

INSERT INTO ventas.Cliente (ClienteId, Nombre, Localidad)
SELECT c.ClienteId, c.Nombre, c.Localidad
FROM ventas.ArchivoCliente AS f
CROSS APPLY OPENJSON(f.Contenido)
WITH (
    ClienteId INT          '$.clienteId',
    Nombre    NVARCHAR(60) '$.nombre',
    Localidad NVARCHAR(30) '$.localidad'
) AS c;

INSERT INTO ventas.ClienteContacto (ClienteId, Email)
SELECT c.ClienteId, e.[value]
FROM ventas.ArchivoCliente AS f
CROSS APPLY OPENJSON(f.Contenido)
WITH (
    ClienteId INT           '$.clienteId',
    Contactos NVARCHAR(MAX) '$.contactos' AS JSON
) AS c
CROSS APPLY OPENJSON(c.Contactos) AS e;

SELECT c.ClienteId, c.Nombre, c.Localidad, COUNT(k.Email) AS Contactos
FROM ventas.Cliente AS c
LEFT JOIN ventas.ClienteContacto AS k ON k.ClienteId = c.ClienteId
GROUP BY c.ClienteId, c.Nombre, c.Localidad
ORDER BY c.ClienteId;
