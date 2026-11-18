-- SIN-PRELUDE
-- Ejercicio U5.14: ordenamiento dinámico con columna y dirección permitidas.
CREATE SCHEMA catalogo;
GO
CREATE TABLE catalogo.Producto
(
    ProductoId INT IDENTITY PRIMARY KEY,
    Nombre     NVARCHAR(60)   NOT NULL,
    Precio     DECIMAL(10, 2) NOT NULL
);
INSERT catalogo.Producto (Nombre, Precio) VALUES (N'Teclado', 30), (N'Mouse', 12), (N'Monitor', 150);
GO
CREATE PROCEDURE catalogo.ListarOrdenado @Columna SYSNAME, @Direccion VARCHAR(4) = 'ASC'
AS
BEGIN
    IF @Columna NOT IN (N'Nombre', N'Precio')
        THROW 50020, 'Columna no permitida.', 1;
    IF @Direccion NOT IN ('ASC', 'DESC')
        THROW 50021, 'Direccion no permitida.', 1;

    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT ProductoId, Nombre, Precio FROM catalogo.Producto ORDER BY '
        + QUOTENAME(@Columna) + N' ' + @Direccion + N', ProductoId;';
    EXEC sys.sp_executesql @Sql;
END;
GO
EXEC catalogo.ListarOrdenado @Columna = N'Precio', @Direccion = 'DESC';
GO
EXEC catalogo.ListarOrdenado @Columna = N'Nombre';
GO
BEGIN TRY
    EXEC catalogo.ListarOrdenado @Columna = N'Precio', @Direccion = 'ASC, Nombre';
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Error, ERROR_MESSAGE() AS Mensaje;
END CATCH;
