-- u1 · repaso: qué DML admite una vista (una tabla base afectada; con agregados no).
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Departamento (
    DepartamentoId INT NOT NULL CONSTRAINT PK_Departamento PRIMARY KEY,
    Nombre         VARCHAR(30) NOT NULL
);
CREATE TABLE academia.Empleado (
    EmpleadoId     INT NOT NULL CONSTRAINT PK_Empleado PRIMARY KEY,
    Nombre         VARCHAR(30) NOT NULL,
    DepartamentoId INT NOT NULL CONSTRAINT FK_Empleado_Departamento REFERENCES academia.Departamento (DepartamentoId),
    Sueldo         DECIMAL(10,2) NOT NULL
);
INSERT INTO academia.Departamento VALUES (1, 'Sistemas'), (2, 'Ventas');
INSERT INTO academia.Empleado VALUES (1, 'Ana', 1, 1000), (2, 'Beto', 2, 800);
GO
CREATE VIEW academia.EmpleadoDetalle
AS
    SELECT e.EmpleadoId, e.Nombre, d.Nombre AS Departamento, e.Sueldo
    FROM academia.Empleado AS e
    INNER JOIN academia.Departamento AS d ON d.DepartamentoId = e.DepartamentoId;
GO
CREATE VIEW academia.SueldoPorDepartamento
AS
    SELECT DepartamentoId, SUM(Sueldo) AS Total
    FROM academia.Empleado
    GROUP BY DepartamentoId;
GO
DECLARE @ErrorDosTablas INT = 0, @ErrorAgregado INT = 0;

-- Actualizar columnas de UNA sola tabla base a traves de una vista de varias tablas: permitido.
UPDATE academia.EmpleadoDetalle SET Sueldo = 1100 WHERE EmpleadoId = 1;

-- Un UPDATE que toca columnas de dos tablas base a la vez: rechazado.
BEGIN TRY
    EXEC (N'UPDATE academia.EmpleadoDetalle SET Sueldo = 900, Departamento = ''Soporte'' WHERE EmpleadoId = 2;');
END TRY
BEGIN CATCH
    SET @ErrorDosTablas = ERROR_NUMBER();
END CATCH;

-- Vista con GROUP BY: no admite UPDATE.
BEGIN TRY
    EXEC (N'UPDATE academia.SueldoPorDepartamento SET Total = 0 WHERE DepartamentoId = 1;');
END TRY
BEGIN CATCH
    SET @ErrorAgregado = ERROR_NUMBER();
END CATCH;

SELECT
    (SELECT Sueldo FROM academia.Empleado WHERE EmpleadoId = 1) AS SueldoAna,
    @ErrorDosTablas AS ErrorDosTablas,
    @ErrorAgregado  AS ErrorAgregado;
