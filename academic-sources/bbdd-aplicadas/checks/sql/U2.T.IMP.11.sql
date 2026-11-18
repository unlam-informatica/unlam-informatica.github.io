SELECT d.Codigo,
       RTRIM(d.Nombre)                   AS Nombre,
       CAST(d.Precio AS DECIMAL(10,2))   AS Precio,
       CAST(d.Stock AS INT)              AS Stock
FROM OPENROWSET(
    BULK '{{FIXTURES}}/producto_fijo.txt',
    FORMATFILE = '{{FIXTURES}}/producto_fijo.fmt'
) AS d
ORDER BY d.Codigo;
