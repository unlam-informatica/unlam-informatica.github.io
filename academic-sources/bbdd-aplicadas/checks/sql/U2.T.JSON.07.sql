DECLARE @Json NVARCHAR(MAX) = N'{
    "pedido": 1001,
    "lineas": [
        { "producto": "P001", "cantidad": 2 },
        { "producto": "P003", "cantidad": 10 }
    ]
}';

SELECT Producto, Cantidad, Descuento
FROM OPENJSON(@Json, '$.lineas')
WITH (
    Producto  CHAR(4) '$.producto',
    Cantidad  INT     '$.cantidad',
    Descuento INT     '$.descuento'
)
ORDER BY Producto;
