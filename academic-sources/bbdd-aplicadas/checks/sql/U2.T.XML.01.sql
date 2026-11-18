DECLARE @Pedido XML = N'
<pedido numero="1001" estado="abierto">
    <cliente>Ferretería Norte</cliente>
    <linea producto="P001" cantidad="2"><precio>1250.50</precio></linea>
    <linea producto="P003" cantidad="10"><precio>480.25</precio></linea>
</pedido>';

SELECT @Pedido.value('(/pedido/@numero)[1]', 'INT')               AS Numero,
       @Pedido.value('(/pedido/cliente)[1]', 'VARCHAR(40)')       AS Cliente,
       @Pedido.value('count(/pedido/linea)', 'INT')               AS CantidadLineas,
       @Pedido.exist('/pedido/linea[@producto = "P003"]')         AS TieneP003,
       @Pedido.exist('/pedido/linea[@producto = "P999"]')         AS TieneP999,
       @Pedido.query('/pedido/linea[@producto = "P003"]')         AS LineaP003;
