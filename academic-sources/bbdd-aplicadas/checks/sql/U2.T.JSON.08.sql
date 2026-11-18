DECLARE @Json NVARCHAR(MAX) = N'{"producto": "P001", "cantidad": 2}';
DECLARE @Error INT = 0;
DECLARE @Mensaje NVARCHAR(200) = N'';

BEGIN TRY
    SELECT Producto, Descuento
    FROM OPENJSON(@Json)
    WITH (
        Producto  CHAR(4) '$.producto',
        Descuento INT     'strict $.descuento'
    );
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    SET @Mensaje = ERROR_MESSAGE();
END CATCH;

SELECT @Error AS NumeroDeError, @Mensaje AS Mensaje,
       JSON_VALUE(@Json, 'lax $.descuento') AS ConLax;
