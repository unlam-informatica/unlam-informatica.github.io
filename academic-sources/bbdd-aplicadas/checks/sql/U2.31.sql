CREATE SCHEMA rrhh;
GO

CREATE TABLE rrhh.Departamento (
    DepartamentoId INT         NOT NULL,
    Nombre         VARCHAR(40) NOT NULL,
    CONSTRAINT PK_Departamento PRIMARY KEY CLUSTERED (DepartamentoId)
);

CREATE TABLE rrhh.Empleado (
    EmpleadoId     INT           NOT NULL,
    DepartamentoId INT           NOT NULL,
    Nombre         VARCHAR(40)   NOT NULL,
    Cargo          VARCHAR(40)   NOT NULL,
    Salario        DECIMAL(10,2) NOT NULL,
    Email          VARCHAR(80)   NULL,
    CONSTRAINT PK_Empleado PRIMARY KEY CLUSTERED (EmpleadoId),
    CONSTRAINT FK_Empleado_Departamento FOREIGN KEY (DepartamentoId) REFERENCES rrhh.Departamento (DepartamentoId)
);
GO

INSERT INTO rrhh.Departamento (DepartamentoId, Nombre)
VALUES (1, 'Ingenieria'), (2, 'Administracion');

INSERT INTO rrhh.Empleado (EmpleadoId, DepartamentoId, Nombre, Cargo, Salario, Email)
VALUES (1, 1, 'Empleado 01', 'Desarrollo',  120000.00, 'e01@ejemplo.test'),
       (2, 1, 'Empleado 02', 'Operaciones',  98000.00, NULL),
       (3, 2, 'Empleado 03', 'Contaduria',   82000.00, 'e03@ejemplo.test');
GO

SELECT d.DepartamentoId, d.Nombre AS Departamento, e.EmpleadoId, e.Nombre AS Empleado
FROM rrhh.Departamento AS d
INNER JOIN rrhh.Empleado AS e ON e.DepartamentoId = d.DepartamentoId
WHERE d.DepartamentoId = 1
ORDER BY d.DepartamentoId, e.EmpleadoId
FOR XML AUTO, ROOT('Empresa');

SELECT e.EmpleadoId, e.Nombre AS Empleado, d.DepartamentoId, d.Nombre AS Departamento
FROM rrhh.Empleado AS e
INNER JOIN rrhh.Departamento AS d ON d.DepartamentoId = e.DepartamentoId
WHERE d.DepartamentoId = 1
ORDER BY e.EmpleadoId
FOR XML AUTO, ROOT('Empresa');
