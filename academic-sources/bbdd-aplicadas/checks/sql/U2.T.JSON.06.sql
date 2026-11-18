DECLARE @Json NVARCHAR(MAX) = N'{
    "pedido": 1001,
    "cliente": "Ferretería Norte",
    "lineas": [
        { "producto": "P001", "cantidad": 2, "precio": 1250.50 },
        { "producto": "P003", "cantidad": 10, "precio": 480.25 }
    ]
}';

-- AS JSON conserva el array como texto JSON; el segundo OPENJSON lo despliega en filas
SELECT c.Pedido, c.Cliente, l.Producto, l.Cantidad, l.Precio
FROM OPENJSON(@Json)
WITH (
    Pedido  INT           '$.pedido',
    Cliente VARCHAR(40)   '$.cliente',
    Lineas  NVARCHAR(MAX) '$.lineas' AS JSON
) AS c
CROSS APPLY OPENJSON(c.Lineas)
WITH (
    Producto CHAR(4)       '$.producto',
    Cantidad INT           '$.cantidad',
    Precio   DECIMAL(10,2) '$.precio'
) AS l
ORDER BY l.Producto;
