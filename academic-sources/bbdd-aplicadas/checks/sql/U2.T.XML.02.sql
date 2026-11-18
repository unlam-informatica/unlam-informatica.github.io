DECLARE @Pedido XML = N'
<pedido numero="1001">
    <linea producto="P001" cantidad="2"><precio>1250.50</precio></linea>
    <linea producto="P003" cantidad="10"><precio>480.25</precio></linea>
</pedido>';

SELECT @Pedido.value('(/pedido/@numero)[1]', 'INT') AS Pedido,
       l.value('@producto', 'CHAR(4)')              AS Producto,
       l.value('@cantidad', 'INT')                  AS Cantidad,
       l.value('(precio)[1]', 'DECIMAL(10,2)')      AS Precio
FROM @Pedido.nodes('/pedido/linea') AS t(l)
ORDER BY Producto;
