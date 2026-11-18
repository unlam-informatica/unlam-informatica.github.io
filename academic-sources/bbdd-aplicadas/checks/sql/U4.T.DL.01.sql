-- u4 · DWH: modelo en estrella mínimo cargado con ETL desde una tabla de origen.
CREATE SCHEMA oltp;
GO
CREATE SCHEMA dwh;
GO

-- Origen transaccional (normalizado, reducido a lo necesario)
CREATE TABLE oltp.VentaOrigen (
    VentaId    INT           NOT NULL,
    Fecha      DATE          NOT NULL,
    ClienteId  INT           NOT NULL,
    Localidad  VARCHAR(40)   NOT NULL,
    Producto   VARCHAR(40)   NOT NULL,
    Categoria  VARCHAR(40)   NOT NULL,
    Cantidad   INT           NOT NULL,
    PrecioUnit DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_VentaOrigen PRIMARY KEY CLUSTERED (VentaId)
);
INSERT INTO oltp.VentaOrigen (VentaId, Fecha, ClienteId, Localidad, Producto, Categoria, Cantidad, PrecioUnit) VALUES
    (1, '2026-03-05', 10, 'Morón',  'Teclado', 'perifericos', 2, 45.00),
    (2, '2026-03-18', 11, 'Haedo',  'Mouse',   'perifericos', 1, 20.00),
    (3, '2026-04-02', 10, 'Morón',  'Monitor', 'pantallas',   1, 300.00),
    (4, '2026-04-20', 12, 'Ramos Mejía', 'Teclado', 'perifericos', 1, 45.00),
    (5, '2026-04-21', 11, 'Haedo',  'Monitor', 'pantallas',   2, 300.00);
GO

-- Dimensiones y tabla de hechos
CREATE TABLE dwh.DimCliente (
    ClienteKey INT IDENTITY(1, 1) NOT NULL,
    ClienteId  INT                NOT NULL,
    Localidad  VARCHAR(40)        NOT NULL,
    CONSTRAINT PK_DimCliente PRIMARY KEY CLUSTERED (ClienteKey),
    CONSTRAINT UQ_DimCliente_ClienteId UNIQUE (ClienteId)
);
CREATE TABLE dwh.DimProducto (
    ProductoKey INT IDENTITY(1, 1) NOT NULL,
    Producto    VARCHAR(40)        NOT NULL,
    Categoria   VARCHAR(40)        NOT NULL,
    CONSTRAINT PK_DimProducto PRIMARY KEY CLUSTERED (ProductoKey),
    CONSTRAINT UQ_DimProducto_Producto UNIQUE (Producto)
);
CREATE TABLE dwh.DimTiempo (
    TiempoKey INT      NOT NULL,
    Fecha     DATE     NOT NULL,
    Anio      SMALLINT NOT NULL,
    Mes       TINYINT  NOT NULL,
    CONSTRAINT PK_DimTiempo PRIMARY KEY CLUSTERED (TiempoKey)
);
CREATE TABLE dwh.FactVenta (
    TiempoKey   INT           NOT NULL,
    ClienteKey  INT           NOT NULL,
    ProductoKey INT           NOT NULL,
    Cantidad    INT           NOT NULL,
    Importe     DECIMAL(12,2) NOT NULL,
    CONSTRAINT FK_FactVenta_DimTiempo   FOREIGN KEY (TiempoKey)   REFERENCES dwh.DimTiempo (TiempoKey),
    CONSTRAINT FK_FactVenta_DimCliente  FOREIGN KEY (ClienteKey)  REFERENCES dwh.DimCliente (ClienteKey),
    CONSTRAINT FK_FactVenta_DimProducto FOREIGN KEY (ProductoKey) REFERENCES dwh.DimProducto (ProductoKey)
);
GO

-- ETL: extraer del origen, transformar (claves sustitutas, fecha desglosada, importe calculado) y cargar
INSERT INTO dwh.DimCliente (ClienteId, Localidad)
SELECT DISTINCT ClienteId, Localidad FROM oltp.VentaOrigen;

INSERT INTO dwh.DimProducto (Producto, Categoria)
SELECT DISTINCT Producto, Categoria FROM oltp.VentaOrigen;

INSERT INTO dwh.DimTiempo (TiempoKey, Fecha, Anio, Mes)
SELECT DISTINCT
    YEAR(Fecha) * 10000 + MONTH(Fecha) * 100 + DAY(Fecha),
    Fecha,
    YEAR(Fecha),
    MONTH(Fecha)
FROM oltp.VentaOrigen;

INSERT INTO dwh.FactVenta (TiempoKey, ClienteKey, ProductoKey, Cantidad, Importe)
SELECT
    YEAR(v.Fecha) * 10000 + MONTH(v.Fecha) * 100 + DAY(v.Fecha),
    c.ClienteKey,
    p.ProductoKey,
    v.Cantidad,
    v.Cantidad * v.PrecioUnit
FROM oltp.VentaOrigen AS v
INNER JOIN dwh.DimCliente  AS c ON c.ClienteId = v.ClienteId
INNER JOIN dwh.DimProducto AS p ON p.Producto  = v.Producto;
GO

-- Consulta analítica: ventas por mes y categoría
SELECT
    t.Anio,
    t.Mes,
    p.Categoria,
    SUM(f.Importe)  AS ImporteTotal,
    SUM(f.Cantidad) AS Unidades
FROM dwh.FactVenta AS f
INNER JOIN dwh.DimTiempo   AS t ON t.TiempoKey   = f.TiempoKey
INNER JOIN dwh.DimProducto AS p ON p.ProductoKey = f.ProductoKey
GROUP BY t.Anio, t.Mes, p.Categoria
ORDER BY t.Anio, t.Mes, p.Categoria;
