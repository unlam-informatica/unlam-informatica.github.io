CREATE SCHEMA calidad;
GO

CREATE TABLE calidad.Cliente (
    ClienteId            INT           NOT NULL,
    Dni                  VARCHAR(20)   NULL,
    Nombre               NVARCHAR(100) NULL,
    Email                VARCHAR(256)  NULL,
    PaisCodigo           CHAR(3)       NULL,
    FechaNacimientoTexto VARCHAR(20)   NULL,
    FechaAlta            DATE          NOT NULL,
    FechaActualizacion   DATE          NOT NULL,
    Activo               BIT           NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE calidad.Pedido (
    PedidoId       INT           NOT NULL,
    ClienteId      INT           NULL,
    FechaPedido    DATE          NOT NULL,
    FechaEntrega   DATE          NULL,
    TotalDeclarado DECIMAL(12, 2) NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId)
);

CREATE TABLE calidad.ItemPedido (
    PedidoId       INT            NOT NULL,
    Renglon        INT            NOT NULL,
    Cantidad       INT            NOT NULL,
    PrecioUnitario DECIMAL(12, 2) NOT NULL,
    CONSTRAINT PK_ItemPedido PRIMARY KEY CLUSTERED (PedidoId, Renglon)
);

INSERT INTO calidad.Cliente
    (ClienteId, Dni, Nombre, Email, PaisCodigo, FechaNacimientoTexto, FechaAlta, FechaActualizacion, Activo)
VALUES
    (1, '00000001', N'Cliente Uno',    'cliente01@ejemplo.test', 'ARG', '1990-02-10', '2025-01-10', '2026-05-20', 1),
    (2, '00000001', N'Cliente Dos',    'cliente02@ejemplo.test', 'ARG', '1990-02-10', '2025-01-10', '2025-03-15', 1),
    (3, NULL,       N'Cliente Tres',   '',                       'AR ', '31/02/1995', '2025-03-01', '2026-06-10', 1),
    (4, '00000004', NULL,              'cliente04@ejemplo.test', 'URY', '1985-05-20', '2025-04-01', '2026-06-01', 1),
    (5, '00000005', N'Cliente Cinco',  'cliente05@ejemplo.test', 'ZZZ', '1977-09-08', '2024-02-01', '2024-11-02', 0),
    (6, '00000006', N'Cliente Seis',   NULL,                     'BRA', '2000-01-31', '2025-05-05', '2026-01-15', 1),
    (7, '00000007', N'Cliente Siete',  '   ',                    'ARG', NULL,         '2024-08-08', '2025-01-20', 1),
    (8, '00000008', N'Cliente Ocho',   'cliente08@ejemplo.test', 'ARG', '1999-12-01', '2025-06-01', '2026-03-03', 1),
    (9, '00000009', N'Cliente Nueve',  'CLIENTE01@EJEMPLO.TEST', 'URY', '1988-07-07', '2026-01-02', '2026-06-29', 1);

INSERT INTO calidad.Pedido (PedidoId, ClienteId, FechaPedido, FechaEntrega, TotalDeclarado)
VALUES
    (101, 1,  '2026-06-01', '2026-05-31', 150.00),
    (102, 3,  '2026-06-02', NULL,         200.00),
    (103, 99, '2026-06-03', NULL,          50.00);

INSERT INTO calidad.ItemPedido (PedidoId, Renglon, Cantidad, PrecioUnitario)
VALUES
    (101, 1, 1, 100.00),
    (101, 2, 1,  40.00),
    (102, 1, 2, 100.00),
    (103, 1, 1,  50.00);
GO

SELECT 'Cliente' AS Tabla, COUNT(*) AS Filas FROM calidad.Cliente
UNION ALL
SELECT 'ItemPedido', COUNT(*) FROM calidad.ItemPedido
UNION ALL
SELECT 'Pedido', COUNT(*) FROM calidad.Pedido
ORDER BY Tabla;
