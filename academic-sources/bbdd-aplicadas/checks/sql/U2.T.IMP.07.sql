CREATE SCHEMA staging;
GO

-- La columna VARCHAR con collation UTF8 interpreta los bytes del archivo como UTF-8
CREATE TABLE staging.Documento (
    Contenido VARCHAR(MAX) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NOT NULL
);
GO

INSERT INTO staging.Documento (Contenido)
SELECT archivo.BulkColumn
FROM OPENROWSET(BULK '{{FIXTURES}}/producto_acentos.json', SINGLE_BLOB) AS archivo;

SELECT p.Codigo, p.Nombre, p.Categoria, LEN(p.Nombre) AS Largo
FROM staging.Documento AS d
CROSS APPLY OPENJSON(d.Contenido)
WITH (
    Codigo    CHAR(4)       '$.codigo',
    Nombre    NVARCHAR(40)  '$.nombre',
    Categoria NVARCHAR(40)  '$.categoria'
) AS p
ORDER BY p.Codigo;
