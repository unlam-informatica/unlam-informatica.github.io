-- SIN-PRELUDE
-- Ejercicio U5.13: leer el SQL generado.
CREATE SCHEMA catalogo;
GO
CREATE TABLE catalogo.Producto
(
    ProductoId INT IDENTITY PRIMARY KEY,
    Nombre     NVARCHAR(60) NOT NULL,
    Categoria  VARCHAR(20)  NOT NULL,
    Publicado  BIT          NOT NULL
);
INSERT catalogo.Producto (Nombre, Categoria, Publicado)
VALUES (N'Teclado', 'perifericos', 1), (N'Mouse', 'perifericos', 1), (N'Monitor', 'pantallas', 1), (N'Prototipo', 'pantallas', 0);
GO
CREATE PROCEDURE catalogo.ListarPorCategoria @Categoria NVARCHAR(100)
AS
BEGIN
    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT ProductoId, Nombre FROM catalogo.Producto WHERE Publicado = 1 AND Categoria = ''' + @Categoria + N''';';
    SELECT @Sql AS SqlGenerado;
    EXEC (@Sql);
END;
GO
EXEC catalogo.ListarPorCategoria @Categoria = N'pantallas';
GO
EXEC catalogo.ListarPorCategoria @Categoria = N'pantallas'' OR Publicado = 0--';
GO
CREATE OR ALTER PROCEDURE catalogo.ListarPorCategoria @Categoria NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT ProductoId, Nombre
    FROM catalogo.Producto
    WHERE Publicado = 1 AND Categoria = @Categoria;
END;
GO
EXEC catalogo.ListarPorCategoria @Categoria = N'pantallas'' OR Publicado = 0--';
GO
EXEC catalogo.ListarPorCategoria @Categoria = N'pantallas';
