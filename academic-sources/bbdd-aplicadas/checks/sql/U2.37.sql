DECLARE @Objeto INT;
DECLARE @Numero INT = 0;
DECLARE @Mensaje NVARCHAR(400) = N'';

BEGIN TRY
    EXEC sys.sp_OACreate 'MSXML2.XMLHTTP', @Objeto OUTPUT;
END TRY
BEGIN CATCH
    SET @Numero = ERROR_NUMBER();
    SET @Mensaje = LEFT(ERROR_MESSAGE(), 60);
END CATCH;

SELECT c.name AS Opcion, c.value AS Configurado, c.value_in_use AS EnUso,
       @Numero AS Error, @Mensaje AS Mensaje
FROM sys.configurations AS c
WHERE c.name = 'Ole Automation Procedures';
