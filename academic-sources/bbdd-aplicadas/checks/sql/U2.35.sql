CREATE SCHEMA rrhh;
GO

CREATE TABLE rrhh.EmpleadoImportado (
    Legajo       CHAR(4)       NOT NULL,
    Departamento NVARCHAR(40)  NOT NULL,
    Cargo        VARCHAR(40)   NOT NULL,
    Salario      DECIMAL(10,2) NOT NULL,
    Email        VARCHAR(80)   NULL,
    CONSTRAINT PK_EmpleadoImportado PRIMARY KEY CLUSTERED (Legajo)
);
GO

DECLARE @Documento XML = (
    SELECT CAST(a.BulkColumn AS XML)
    FROM OPENROWSET(BULK '{{FIXTURES}}/empleado.xml', SINGLE_BLOB) AS a
);

INSERT INTO rrhh.EmpleadoImportado (Legajo, Departamento, Cargo, Salario, Email)
SELECT e.value('@legajo', 'CHAR(4)'),
       e.value('../@nombre', 'NVARCHAR(40)'),
       e.value('@cargo', 'VARCHAR(40)'),
       e.value('(Salario)[1]', 'DECIMAL(10,2)'),
       e.value('(Email)[1]', 'VARCHAR(80)')
FROM @Documento.nodes('/Empresa/Departamento/Empleado') AS t(e);

SELECT Legajo, Departamento, Cargo, Salario, Email,
       @Documento.exist('/Empresa/Departamento[@nombre = "Ingeniería"]') AS HayIngenieria
FROM rrhh.EmpleadoImportado
ORDER BY Legajo;
