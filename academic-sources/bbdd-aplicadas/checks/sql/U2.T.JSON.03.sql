DECLARE @Atributos NVARCHAR(MAX) = N'{"marca":"Zeta","potenciaW":650,"color":"gris","accesorios":["broca","maletin"]}';

SELECT JSON_MODIFY(@Atributos, '$.potenciaW', 750)                  AS Actualiza,
       JSON_MODIFY(@Atributos, '$.garantiaAnios', 2)                AS Agrega,
       JSON_MODIFY(@Atributos, '$.color', NULL)                     AS Elimina,
       JSON_MODIFY(@Atributos, 'append $.accesorios', 'llave')      AS AgregaAlArray;
