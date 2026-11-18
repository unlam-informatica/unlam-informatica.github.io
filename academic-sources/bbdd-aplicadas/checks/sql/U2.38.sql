DECLARE @Respuestas TABLE (Llamada INT NOT NULL, Codigo INT NOT NULL, Cuerpo NVARCHAR(MAX) NOT NULL);

INSERT INTO @Respuestas (Llamada, Codigo, Cuerpo)
VALUES (1, 200, N'{"id": 42, "nombre": "Cuaderno rayado", "precio": 1250.50, "stock": 12}'),
       (2, 404, N'{"error": "producto no encontrado", "id": 999}'),
       (3, 200, N'{"id": 43, "nombre": "Lapicera azul", "precio": 300.00, "stock": null}');

SELECT r.Llamada,
       r.Codigo,
       CASE WHEN r.Codigo BETWEEN 200 AND 299 THEN 'procesada' ELSE 'rechazada' END AS Estado,
       p.Id, p.Nombre, p.Precio, p.Stock,
       JSON_VALUE(r.Cuerpo, '$.error') AS MensajeDeError
FROM @Respuestas AS r
OUTER APPLY OPENJSON(CASE WHEN r.Codigo BETWEEN 200 AND 299 THEN r.Cuerpo END)
WITH (
    Id     INT           '$.id',
    Nombre VARCHAR(40)   '$.nombre',
    Precio DECIMAL(10,2) '$.precio',
    Stock  INT           '$.stock'
) AS p
ORDER BY r.Llamada;
