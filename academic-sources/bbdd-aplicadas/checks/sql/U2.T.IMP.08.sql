SELECT p.Codigo, p.Nombre, p.Categoria, LEN(p.Nombre) AS Largo
FROM OPENROWSET(BULK '{{FIXTURES}}/producto_acentos16.json', SINGLE_NCLOB) AS archivo
CROSS APPLY OPENJSON(archivo.BulkColumn)
WITH (
    Codigo    CHAR(4)       '$.codigo',
    Nombre    NVARCHAR(40)  '$.nombre',
    Categoria NVARCHAR(40)  '$.categoria'
) AS p
ORDER BY p.Codigo;
