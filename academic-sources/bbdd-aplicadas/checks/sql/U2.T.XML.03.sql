DECLARE @Xml XML = N'
<clientes>
    <cliente id="1"><nombre>Ferretería Norte</nombre><limite>25000.50</limite></cliente>
    <cliente id="2"><nombre>Kiosco Central</nombre><limite>8000.00</limite></cliente>
</clientes>';

DECLARE @Handle INT;

EXEC sys.sp_xml_preparedocument @Handle OUTPUT, @Xml;

SELECT Id, Nombre, Limite
FROM OPENXML(@Handle, '/clientes/cliente')
WITH (
    Id     INT           '@id',
    Nombre VARCHAR(40)   'nombre',
    Limite DECIMAL(10,2) 'limite'
)
ORDER BY Id;

EXEC sys.sp_xml_removedocument @Handle;
