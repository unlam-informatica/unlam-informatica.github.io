DECLARE @Catalogo XML = N'
<catalogo>
    <producto codigo="P001" categoria="Escolar">
        <nombre>Cuaderno rayado</nombre>
        <precio>1250.50</precio>
        <stock>40</stock>
    </producto>
    <producto codigo="P002" categoria="Escolar">
        <nombre>Lapicera azul</nombre>
        <precio>300.00</precio>
        <stock>0</stock>
    </producto>
    <producto codigo="P003" categoria="Oficina">
        <nombre>Resma A4</nombre>
        <precio>9800.00</precio>
        <stock>15</stock>
    </producto>
</catalogo>';

SELECT p.value('@codigo', 'CHAR(4)')            AS Codigo,
       p.value('(nombre)[1]', 'VARCHAR(40)')     AS Nombre,
       p.value('(precio)[1]', 'DECIMAL(10,2)')   AS Precio,
       p.value('(stock)[1]', 'INT')              AS Stock
FROM @Catalogo.nodes('/catalogo/producto[@categoria = "Escolar"]') AS t(p)
WHERE p.exist('stock[. > 0]') = 1
ORDER BY Codigo;
