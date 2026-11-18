-- u1 · repaso: INSTEAD OF INSERT sobre una vista con join.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Departamento (
    DepartamentoId INT NOT NULL CONSTRAINT PK_Departamento PRIMARY KEY,
    Nombre         VARCHAR(30) NOT NULL
);
CREATE TABLE academia.Empleado (
    EmpleadoId     INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Empleado PRIMARY KEY,
    Nombre         VARCHAR(30) NOT NULL,
    DepartamentoId INT NOT NULL CONSTRAINT FK_Empleado_Departamento REFERENCES academia.Departamento (DepartamentoId)
);
INSERT INTO academia.Departamento VALUES (1, 'Sistemas'), (2, 'Ventas');
GO
CREATE VIEW academia.EmpleadoDetalle
AS
    SELECT e.Nombre, d.Nombre AS Departamento
    FROM academia.Empleado AS e
    INNER JOIN academia.Departamento AS d ON d.DepartamentoId = e.DepartamentoId;
GO
CREATE TRIGGER academia.TrgEmpleadoDetalleInsert
ON academia.EmpleadoDetalle
INSTEAD OF INSERT
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO academia.Empleado (Nombre, DepartamentoId)
    SELECT i.Nombre, d.DepartamentoId
    FROM inserted AS i
    INNER JOIN academia.Departamento AS d ON d.Nombre = i.Departamento;
END;
GO
INSERT INTO academia.EmpleadoDetalle (Nombre, Departamento) VALUES ('Ana', 'Ventas'), ('Beto', 'Sistemas');

SELECT Nombre, Departamento
FROM academia.EmpleadoDetalle
ORDER BY Nombre;
