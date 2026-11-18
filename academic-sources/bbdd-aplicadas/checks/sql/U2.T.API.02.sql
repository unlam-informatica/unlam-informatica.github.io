DECLARE @Objeto INT;
DECLARE @Numero INT = 0;

BEGIN TRY
    EXEC sys.sp_OACreate 'MSXML2.XMLHTTP', @Objeto OUTPUT;
END TRY
BEGIN CATCH
    SET @Numero = ERROR_NUMBER();
END CATCH;

SELECT name AS Opcion, value_in_use AS ValorEnUso, @Numero AS ErrorAlCrearObjeto
FROM sys.configurations
WHERE name = 'Ole Automation Procedures';
