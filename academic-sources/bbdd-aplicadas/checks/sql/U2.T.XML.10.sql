DECLARE @Xml XML = N'
<f:factura xmlns:f="http://ejemplo.test/factura">
    <f:numero>A-0001</f:numero>
    <f:importe>3000.00</f:importe>
</f:factura>';

-- Sin declarar el espacio de nombres, la ruta no encuentra nada
SELECT @Xml.value('(/factura/numero)[1]', 'VARCHAR(20)') AS SinNamespace;

WITH XMLNAMESPACES ('http://ejemplo.test/factura' AS f)
SELECT @Xml.value('(/f:factura/f:numero)[1]', 'VARCHAR(20)')    AS Numero,
       @Xml.value('(/f:factura/f:importe)[1]', 'DECIMAL(10,2)') AS Importe;
