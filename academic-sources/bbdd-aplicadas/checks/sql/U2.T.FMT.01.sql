DECLARE @Json NVARCHAR(MAX) = N'[
  {"codigo": "P001", "nombre": "Cuaderno rayado", "precio": 1250.50, "stock": 40},
  {"codigo": "P002", "nombre": "Lapicera azul",   "precio": 300.00,  "stock": 120}
]';

DECLARE @Xml XML = N'
<productos>
  <producto codigo="P001">
    <nombre>Cuaderno rayado</nombre>
    <precio>1250.50</precio>
    <stock>40</stock>
  </producto>
  <producto codigo="P002">
    <nombre>Lapicera azul</nombre>
    <precio>300.00</precio>
    <stock>120</stock>
  </producto>
</productos>';

SELECT 'JSON' AS Origen, Codigo, Nombre, Precio, Stock
FROM OPENJSON(@Json)
WITH (
    Codigo CHAR(4)       '$.codigo',
    Nombre VARCHAR(40)   '$.nombre',
    Precio DECIMAL(10,2) '$.precio',
    Stock  INT           '$.stock'
)
UNION ALL
SELECT 'XML',
       n.value('@codigo', 'CHAR(4)'),
       n.value('(nombre)[1]', 'VARCHAR(40)'),
       n.value('(precio)[1]', 'DECIMAL(10,2)'),
       n.value('(stock)[1]', 'INT')
FROM @Xml.nodes('/productos/producto') AS t(n)
ORDER BY Codigo, Origen;
