CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Cliente (
    ClienteId   INT          NOT NULL,
    Nombre      VARCHAR(60)  NOT NULL,
    Localidad   VARCHAR(30)  NULL,
    Observacion VARCHAR(80)  NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);
GO

BULK INSERT ventas.Cliente
FROM '{{FIXTURES}}/cliente_comillas.csv'
WITH (
    FORMAT     = 'CSV',
    FIELDQUOTE = '"',
    FIRSTROW   = 2
);

SELECT ClienteId, Nombre, Localidad, Observacion
FROM ventas.Cliente
ORDER BY ClienteId;
