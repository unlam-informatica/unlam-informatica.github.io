CREATE SCHEMA practica;
GO

CREATE TABLE practica.Venta (
    VentaId  INT           NOT NULL IDENTITY(1, 1),
    Vendedor VARCHAR(50)   NOT NULL,
    Mes      VARCHAR(10)   NOT NULL,
    Producto VARCHAR(50)   NOT NULL,
    Monto    DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Venta PRIMARY KEY (VentaId)
);

CREATE TABLE practica.NotaFinal (
    Alumno  VARCHAR(50)   NOT NULL,
    Materia VARCHAR(50)   NOT NULL,
    Nota    DECIMAL(4,1)  NOT NULL,
    CONSTRAINT PK_NotaFinal PRIMARY KEY (Alumno, Materia)
);

CREATE TABLE practica.ResumenTrimestral (
    Departamento VARCHAR(50)   NOT NULL,
    Q1           DECIMAL(10,2) NULL,
    Q2           DECIMAL(10,2) NULL,
    Q3           DECIMAL(10,2) NULL,
    Q4           DECIMAL(10,2) NULL,
    CONSTRAINT PK_ResumenTrimestral PRIMARY KEY (Departamento)
);

CREATE TABLE practica.VentaCiudad (
    VentaId  INT           NOT NULL IDENTITY(1, 1),
    Cantidad INT           NOT NULL,
    Precio   DECIMAL(10,2) NOT NULL,
    Ciudad   VARCHAR(50)   NOT NULL,
    Vendedor VARCHAR(50)   NOT NULL,
    CONSTRAINT PK_VentaCiudad PRIMARY KEY (VentaId)
);
GO

INSERT INTO practica.Venta (Vendedor, Mes, Producto, Monto)
VALUES
    ('Ana', 'Enero', 'Laptop', 1500.00), ('Ana', 'Enero', 'Teclado', 300.00),
    ('Ana', 'Febrero', 'Monitor', 2000.00), ('Ana', 'Marzo', 'Laptop', 1800.00),
    ('Ana', 'Abril', 'Impresora', 2200.00), ('Ana', 'Mayo', 'Laptop', 1600.00),
    ('Ana', 'Junio', 'Monitor', 2500.00),
    ('Luis', 'Enero', 'Teclado', 900.00), ('Luis', 'Febrero', 'Mouse', 1100.00),
    ('Luis', 'Marzo', 'Teclado', 800.00), ('Luis', 'Mayo', 'Mouse', 1200.00),
    ('Luis', 'Junio', 'Teclado', 1400.00),
    ('Marta', 'Enero', 'Monitor', 2100.00), ('Marta', 'Febrero', 'Laptop', 1700.00),
    ('Marta', 'Marzo', 'Monitor', 2300.00), ('Marta', 'Abril', 'Laptop', 1900.00),
    ('Marta', 'Mayo', 'Monitor', 2100.00), ('Marta', 'Junio', 'Laptop', 2800.00),
    ('Carlos', 'Marzo', 'Mouse', 500.00), ('Carlos', 'Abril', 'Mouse', 700.00),
    ('Carlos', 'Mayo', 'Teclado', 600.00);

INSERT INTO practica.NotaFinal (Alumno, Materia, Nota)
VALUES
    ('Juan', 'Matemáticas', 7.0), ('Juan', 'Historia', 9.0), ('Juan', 'Inglés', 8.0),
    ('María', 'Matemáticas', 6.0), ('María', 'Física', 8.0),
    ('Pedro', 'Historia', 10.0), ('Pedro', 'Inglés', 7.0), ('Pedro', 'Física', 9.0),
    ('Laura', 'Matemáticas', 8.0), ('Laura', 'Historia', 8.0), ('Laura', 'Inglés', 9.0), ('Laura', 'Física', 7.0);

INSERT INTO practica.ResumenTrimestral (Departamento, Q1, Q2, Q3, Q4)
VALUES
    ('IT', 120.00, 150.00, 130.00, 200.00),
    ('Ventas', 300.00, 280.00, 320.00, 410.00),
    ('RRHH', 80.00, 95.00, NULL, 110.00);

INSERT INTO practica.VentaCiudad (Cantidad, Precio, Ciudad, Vendedor)
VALUES
    (1, 920.00, 'San Diego', 'Online'), (1, 22.50, 'Seattle', 'Valentina'),
    (2, 18.75, 'San Francisco', 'Sofia'), (1, 215.00, 'Los Angeles', 'Online'),
    (1, 18.75, 'Austin', 'Sofia'), (1, 5.99, 'San Francisco', 'Marcelo'),
    (1, 512.00, 'Los Angeles', 'Marcelo'), (1, 275.00, 'Los Angeles', 'Roberto'),
    (2, 95.00, 'Seattle', 'Sofia'), (1, 140.00, 'Phoenix', 'Roberto'),
    (1, 155.00, 'Phoenix', 'Marcelo'), (1, 88.00, 'Dallas', 'Sofia'),
    (1, 110.00, 'Dallas', 'Roberto'), (1, 220.00, 'Dallas', 'Marcelo'),
    (2, 380.00, 'Seattle', 'Online'), (2, 65.00, 'Los Angeles', 'Valentina'),
    (1, 95.00, 'Phoenix', 'Valentina'), (3, 35.00, 'Dallas', 'Valentina'),
    (1, 175.00, 'Phoenix', 'Sofia'), (1, 95.00, 'Austin', 'Roberto'),
    (2, 45.00, 'Austin', 'Marcelo'), (1, 50.00, 'Austin', 'Valentina'),
    (1, 230.00, 'Dallas', 'Online'), (1, 145.00, 'Phoenix', 'Online'),
    (2, 75.00, 'Seattle', 'Roberto');
GO
DECLARE @Columnas NVARCHAR(MAX);
DECLARE @Consulta NVARCHAR(MAX);

SELECT @Columnas = STRING_AGG(QUOTENAME(Mes), N', ') WITHIN GROUP (ORDER BY Orden)
FROM (
    SELECT
        Mes,
        CASE Mes
            WHEN 'Enero'   THEN 1
            WHEN 'Febrero' THEN 2
            WHEN 'Marzo'   THEN 3
            WHEN 'Abril'   THEN 4
            WHEN 'Mayo'    THEN 5
            WHEN 'Junio'   THEN 6
        END AS Orden
    FROM practica.Venta
    GROUP BY Mes
) AS Meses;

SET @Consulta = N'
SELECT Vendedor, ' + @Columnas + N'
FROM (
    SELECT Vendedor, Mes, Monto
    FROM practica.Venta
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Mes IN (' + @Columnas + N')
) AS Pv
ORDER BY Vendedor;';

EXEC sys.sp_executesql @Consulta;
