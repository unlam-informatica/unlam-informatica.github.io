-- u1 · repaso: CROSS JOIN, SELF JOIN, UNION y UNION ALL.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Empleado (
    EmpleadoId INT NOT NULL CONSTRAINT PK_Empleado PRIMARY KEY,
    Nombre     VARCHAR(30) NOT NULL,
    JefeId     INT NULL CONSTRAINT FK_Empleado_Jefe REFERENCES academia.Empleado (EmpleadoId)
);
CREATE TABLE academia.Turno (Nombre VARCHAR(10) NOT NULL);
CREATE TABLE academia.Dia   (Nombre VARCHAR(10) NOT NULL);
INSERT INTO academia.Empleado (EmpleadoId, Nombre, JefeId) VALUES (1, 'Direccion', NULL), (2, 'Ana', 1), (3, 'Beto', 1), (4, 'Cora', 2);
INSERT INTO academia.Turno (Nombre) VALUES ('Mañana'), ('Noche');
INSERT INTO academia.Dia (Nombre) VALUES ('Lunes'), ('Martes'), ('Jueves');

SELECT 'CROSS' AS Consulta, CAST(COUNT(*) AS VARCHAR(10)) AS Resultado
FROM academia.Dia AS d CROSS JOIN academia.Turno AS t
UNION ALL
SELECT 'SELF', STRING_AGG(e.Nombre + ' -> ' + j.Nombre, '; ') WITHIN GROUP (ORDER BY e.EmpleadoId)
FROM academia.Empleado AS e
INNER JOIN academia.Empleado AS j ON j.EmpleadoId = e.JefeId
UNION ALL
SELECT 'UNION', CAST(COUNT(*) AS VARCHAR(10))
FROM (SELECT Nombre FROM academia.Dia UNION SELECT 'Lunes') AS u
UNION ALL
SELECT 'UNION ALL', CAST(COUNT(*) AS VARCHAR(10))
FROM (SELECT Nombre FROM academia.Dia UNION ALL SELECT 'Lunes') AS u;
