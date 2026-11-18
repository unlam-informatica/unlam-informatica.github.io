-- u1 · repaso: DML (INSERT, UPDATE, DELETE, MERGE) y TRUNCATE.
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Producto (
    ProductoId INT NOT NULL CONSTRAINT PK_Producto PRIMARY KEY,
    Nombre     VARCHAR(30) NOT NULL,
    Precio     DECIMAL(10,2) NOT NULL
);
CREATE TABLE academia.ProductoNovedad (
    ProductoId INT NOT NULL,
    Nombre     VARCHAR(30) NOT NULL,
    Precio     DECIMAL(10,2) NOT NULL
);
CREATE TABLE academia.ProductoTemporal (Nombre VARCHAR(30) NOT NULL);

INSERT INTO academia.Producto (ProductoId, Nombre, Precio) VALUES (1, 'Cuaderno', 100), (2, 'Lapiz', 20), (3, 'Regla', 30);
INSERT INTO academia.ProductoNovedad (ProductoId, Nombre, Precio) VALUES (2, 'Lapiz', 25), (4, 'Goma', 15);
INSERT INTO academia.ProductoTemporal VALUES ('a'), ('b');

UPDATE academia.Producto SET Precio = Precio * 1.10 WHERE ProductoId = 1;
DELETE FROM academia.Producto WHERE ProductoId = 3;

MERGE academia.Producto AS destino
USING academia.ProductoNovedad AS origen ON origen.ProductoId = destino.ProductoId
WHEN MATCHED THEN UPDATE SET Precio = origen.Precio
WHEN NOT MATCHED BY TARGET THEN INSERT (ProductoId, Nombre, Precio) VALUES (origen.ProductoId, origen.Nombre, origen.Precio);

TRUNCATE TABLE academia.ProductoTemporal;

SELECT ProductoId, Nombre, Precio, (SELECT COUNT(*) FROM academia.ProductoTemporal) AS FilasTemporal
FROM academia.Producto
ORDER BY ProductoId;
