DECLARE @Json NVARCHAR(MAX) = N'{
    "codigo": "P001",
    "nombre": "Cuaderno rayado",
    "precio": 1250.50,
    "stock": 40,
    "proveedor": { "nombre": "Papelera Sur", "pais": "AR" }
}';

SELECT *
FROM OPENJSON(@Json)
WITH (
    Codigo    CHAR(4)       '$.codigo',
    Nombre    VARCHAR(40)   '$.nombre',
    Precio    DECIMAL(10,2) '$.precio',
    Stock     INT           '$.stock',
    Proveedor VARCHAR(40)   '$.proveedor.nombre',
    Descuento DECIMAL(5,2)  '$.descuento'
);
