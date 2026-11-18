CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Vendedor (
    VendedorId   INT           NOT NULL,
    Nombre       VARCHAR(30)   NOT NULL,
    Region       VARCHAR(10)   NOT NULL,
    SupervisorId INT           NULL,
    Sueldo       DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Vendedor PRIMARY KEY (VendedorId),
    CONSTRAINT FK_Vendedor_Supervisor FOREIGN KEY (SupervisorId) REFERENCES ventas.Vendedor (VendedorId)
);

CREATE TABLE ventas.Venta (
    VentaId    INT           NOT NULL,
    VendedorId INT           NOT NULL,
    Fecha      DATE          NOT NULL,
    Producto   VARCHAR(20)   NOT NULL,
    Monto      DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Venta PRIMARY KEY (VentaId),
    CONSTRAINT FK_Venta_Vendedor FOREIGN KEY (VendedorId) REFERENCES ventas.Vendedor (VendedorId)
);

INSERT INTO ventas.Vendedor (VendedorId, Nombre, Region, SupervisorId, Sueldo)
VALUES
    (1, 'Ana',  'Norte', NULL, 5000.00),
    (2, 'Beto', 'Norte', 1,    3200.00),
    (3, 'Cora', 'Norte', 1,    3200.00),
    (4, 'Dario','Sur',   1,    4100.00),
    (5, 'Eva',  'Sur',   4,    2800.00),
    (6, 'Fede', 'Sur',   4,    3500.00),
    (7, 'Gina', 'Sur',   4,    2800.00);

INSERT INTO ventas.Venta (VentaId, VendedorId, Fecha, Producto, Monto)
VALUES
    (1,  2, '2025-01-10', 'Teclado',  200.00),
    (2,  3, '2025-01-15', 'Monitor',  500.00),
    (3,  2, '2025-01-28', 'Monitor',  500.00),
    (4,  5, '2025-01-30', 'Teclado',  200.00),
    (5,  6, '2025-02-05', 'Notebook', 1200.00),
    (6,  2, '2025-02-12', 'Teclado',  150.00),
    (7,  3, '2025-02-20', 'Notebook', 1200.00),
    (8,  5, '2025-02-25', 'Monitor',  500.00),
    (9,  7, '2025-02-27', 'Teclado',  200.00),
    (10, 3, '2025-03-03', 'Teclado',  200.00),
    (11, 6, '2025-03-10', 'Monitor',  500.00),
    (12, 5, '2025-03-18', 'Notebook', 1200.00),
    (13, 7, '2025-03-22', 'Monitor',  500.00),
    (14, 2, '2025-04-02', 'Notebook', 1200.00),
    (15, 6, '2025-04-15', 'Teclado',  150.00),
    (16, 4, '2025-04-20', 'Monitor',  500.00);
GO
DECLARE @Region VARCHAR(10) = 'Sur';

-- El código dinámico se ejecuta en su propio ámbito: no ve las variables de quien lo llama
BEGIN TRY
    EXEC (N'SELECT COUNT(*) FROM ventas.Vendedor WHERE Region = @Region');
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Numero, ERROR_MESSAGE() AS Mensaje;
END CATCH;
