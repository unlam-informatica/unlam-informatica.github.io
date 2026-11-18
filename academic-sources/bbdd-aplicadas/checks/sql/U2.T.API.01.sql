-- Respuesta guardada de una API ficticia de cotizaciones (el texto llega en @Respuesta)
DECLARE @Respuesta NVARCHAR(MAX) = N'{
    "estado": "ok",
    "consultadoEn": "2026-03-10T12:00:00-03:00",
    "resultado": {
        "moneda": "USD",
        "cotizaciones": [
            { "casa": "mayorista", "compra": 1000.50, "venta": 1010.00 },
            { "casa": "minorista", "compra": 1005.00, "venta": 1030.75 }
        ]
    }
}';

SELECT JSON_VALUE(@Respuesta, '$.estado')                            AS Estado,
       CAST(JSON_VALUE(@Respuesta, '$.consultadoEn') AS DATETIMEOFFSET(0)) AS ConsultadoEn,
       CAST(JSON_VALUE(@Respuesta, '$.consultadoEn') AS DATETIME2(0))      AS SinOffset,
       JSON_VALUE(@Respuesta, '$.resultado.moneda')                  AS Moneda,
       c.Casa, c.Compra, c.Venta
FROM OPENJSON(@Respuesta, '$.resultado.cotizaciones')
WITH (
    Casa   VARCHAR(20)   '$.casa',
    Compra DECIMAL(10,2) '$.compra',
    Venta  DECIMAL(10,2) '$.venta'
) AS c
ORDER BY c.Casa;
