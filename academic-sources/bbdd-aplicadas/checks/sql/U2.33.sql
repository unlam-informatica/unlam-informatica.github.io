DECLARE @Xml XML = N'
<Productos>
    <Producto Codigo="P001" Nombre="Notebook 15"      Precio="1299.99" Stock="12"/>
    <Producto Codigo="P002" Nombre="Mouse inalambrico" Precio="29.99"   Stock="85"/>
    <Producto Codigo="P003" Nombre="Monitor 27&quot;"  Precio="349.99"  Stock="20"/>
</Productos>';

DECLARE @Handle INT;

EXEC sys.sp_xml_preparedocument @Handle OUTPUT, @Xml;

SELECT Codigo, Nombre, Precio, Stock
FROM OPENXML(@Handle, '/Productos/Producto')
WITH (
    Codigo VARCHAR(10)   '@Codigo',
    Nombre VARCHAR(60)   '@Nombre',
    Precio DECIMAL(10,2) '@Precio',
    Stock  INT           '@Stock'
)
ORDER BY Codigo;

EXEC sys.sp_xml_removedocument @Handle;
