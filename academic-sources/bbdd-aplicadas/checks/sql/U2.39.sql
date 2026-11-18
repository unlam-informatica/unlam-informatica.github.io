CREATE SCHEMA mercado;
GO

CREATE TABLE mercado.Cotizacion (
    Moneda     CHAR(3)       NOT NULL,
    Casa       VARCHAR(20)   NOT NULL,
    Compra     DECIMAL(10,2) NOT NULL,
    Venta      DECIMAL(10,2) NOT NULL,
    Actualizado DATETIMEOFFSET(0) NOT NULL,
    CONSTRAINT PK_Cotizacion PRIMARY KEY CLUSTERED (Moneda, Casa)
);
GO

CREATE PROCEDURE mercado.CargarCotizaciones
    @Respuesta NVARCHAR(MAX)
AS
BEGIN
    SET NOCOUNT ON;

    IF ISJSON(@Respuesta) = 0 OR JSON_VALUE(@Respuesta, '$.estado') <> 'ok'
        THROW 50001, 'La respuesta no es valida o no tiene estado ok.', 1;

    MERGE mercado.Cotizacion AS destino
    USING (
        SELECT JSON_VALUE(@Respuesta, '$.resultado.moneda') AS Moneda,
               c.Casa, c.Compra, c.Venta,
               CAST(JSON_VALUE(@Respuesta, '$.consultadoEn') AS DATETIMEOFFSET(0)) AS Actualizado
        FROM OPENJSON(@Respuesta, '$.resultado.cotizaciones')
        WITH (
            Casa   VARCHAR(20)   '$.casa',
            Compra DECIMAL(10,2) '$.compra',
            Venta  DECIMAL(10,2) '$.venta'
        ) AS c
    ) AS origen
    ON destino.Moneda = origen.Moneda AND destino.Casa = origen.Casa
    WHEN MATCHED THEN
        UPDATE SET Compra = origen.Compra, Venta = origen.Venta, Actualizado = origen.Actualizado
    WHEN NOT MATCHED THEN
        INSERT (Moneda, Casa, Compra, Venta, Actualizado)
        VALUES (origen.Moneda, origen.Casa, origen.Compra, origen.Venta, origen.Actualizado);
END;
GO

EXEC mercado.CargarCotizaciones N'{"estado":"ok","consultadoEn":"2026-03-10T12:00:00-03:00",
  "resultado":{"moneda":"USD","cotizaciones":[
    {"casa":"mayorista","compra":1000.50,"venta":1010.00},
    {"casa":"minorista","compra":1005.00,"venta":1030.75}]}}';

-- Segunda consulta: cambia una casa, aparece otra y la primera se repite
EXEC mercado.CargarCotizaciones N'{"estado":"ok","consultadoEn":"2026-03-10T15:30:00-03:00",
  "resultado":{"moneda":"USD","cotizaciones":[
    {"casa":"mayorista","compra":1000.50,"venta":1010.00},
    {"casa":"minorista","compra":1010.00,"venta":1040.00},
    {"casa":"turista","compra":1090.00,"venta":1100.00}]}}';

DECLARE @Error INT = 0;
BEGIN TRY
    EXEC mercado.CargarCotizaciones N'{"estado":"error","mensaje":"limite de consultas"}';
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT Moneda, Casa, Compra, Venta, Actualizado, @Error AS ErrorUltimaRespuesta
FROM mercado.Cotizacion
ORDER BY Casa;
