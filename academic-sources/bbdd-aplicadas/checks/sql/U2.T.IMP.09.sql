DECLARE @Documento XML = (
    SELECT CAST(archivo.BulkColumn AS XML)
    FROM OPENROWSET(BULK '{{FIXTURES}}/producto.xml', SINGLE_BLOB) AS archivo
);

SELECT n.value('@codigo', 'CHAR(4)')                 AS Codigo,
       n.value('(Nombre)[1]', 'NVARCHAR(40)')        AS Nombre,
       n.value('(Precio)[1]', 'DECIMAL(10,2)')       AS Precio,
       n.value('(Stock)[1]', 'INT')                  AS Stock
FROM @Documento.nodes('/Productos/Producto') AS t(n)
ORDER BY Codigo;
