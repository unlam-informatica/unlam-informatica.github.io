-- u2 · Ejercicio U2.50: una columna sensible a mayúsculas y otra que no.
CREATE SCHEMA inventario;
GO
CREATE TABLE inventario.Articulo (
    ArticuloId INT         NOT NULL PRIMARY KEY,
    Codigo     VARCHAR(10) COLLATE Latin1_General_CS_AS NOT NULL,
    Etiqueta   VARCHAR(10) COLLATE Latin1_General_CI_AS NOT NULL
);
INSERT inventario.Articulo (ArticuloId, Codigo, Etiqueta)
VALUES (1, 'ab-1', 'ab-1'), (2, 'AB-1', 'AB-1'), (3, 'Ab-1', 'Ab-1');

SELECT
    (SELECT COUNT(*) FROM inventario.Articulo WHERE Codigo   = 'ab-1') AS PorCodigo,
    (SELECT COUNT(*) FROM inventario.Articulo WHERE Etiqueta = 'ab-1') AS PorEtiqueta;
