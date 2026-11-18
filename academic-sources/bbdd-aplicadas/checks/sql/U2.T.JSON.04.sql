DECLARE @Json NVARCHAR(MAX) = N'{
    "codigo": "P001",
    "nombre": "Cuaderno rayado",
    "precio": 1250.50,
    "activo": true,
    "etiquetas": ["escolar", "papeleria"],
    "proveedor": { "nombre": "Papelera Sur" },
    "descuento": null
}';

SELECT [key] AS Clave, [value] AS Valor, [type] AS Tipo
FROM OPENJSON(@Json)
ORDER BY (SELECT NULL);
