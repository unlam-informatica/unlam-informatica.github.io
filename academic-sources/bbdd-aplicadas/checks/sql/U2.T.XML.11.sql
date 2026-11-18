CREATE XML SCHEMA COLLECTION dbo.EsquemaProducto AS N'
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="producto">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="nombre" type="xs:string"/>
                <xs:element name="precio" type="xs:decimal"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>';
GO

DECLARE @Valido   XML(dbo.EsquemaProducto) = N'<producto><nombre>Cuaderno</nombre><precio>1250.50</precio></producto>';
DECLARE @Error INT = 0;

BEGIN TRY
    DECLARE @Invalido XML(dbo.EsquemaProducto) = N'<producto><nombre>Cuaderno</nombre><precio>caro</precio></producto>';
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT @Valido.value('(/producto/precio)[1]', 'DECIMAL(10,2)') AS PrecioValido,
       @Error AS NumeroDeErrorConPrecioInvalido;
