DECLARE @Json NVARCHAR(MAX) = N'{
    "cliente": "Ferretería Norte",
    "activo": true,
    "limite": 25000.50,
    "direccion": { "ciudad": "Rosario", "cp": "S2000" },
    "etiquetas": ["mayorista", "frecuente"]
}';

SELECT JSON_VALUE(@Json, '$.cliente')          AS Cliente,
       JSON_VALUE(@Json, '$.activo')           AS Activo,
       JSON_VALUE(@Json, '$.limite')           AS Limite,
       JSON_VALUE(@Json, '$.direccion.ciudad') AS Ciudad,
       JSON_VALUE(@Json, '$.etiquetas[1]')     AS SegundaEtiqueta,
       JSON_VALUE(@Json, '$.direccion')        AS ObjetoConJsonValue,
       JSON_QUERY(@Json, '$.direccion')        AS ObjetoConJsonQuery,
       JSON_QUERY(@Json, '$.etiquetas')        AS ArrayConJsonQuery,
       JSON_VALUE(@Json, '$.inexistente')      AS Inexistente;
