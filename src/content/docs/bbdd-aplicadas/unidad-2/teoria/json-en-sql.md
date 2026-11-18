---
title: JSON en SQL Server
slug: bbdd-aplicadas/unidad-2/teoria/json-en-sql
sidebar:
  order: 7
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

El formato JSON se describe en [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/). Acá se trabaja con él desde T-SQL: validarlo, extraer valores, convertirlo en filas, modificarlo y generarlo a partir de consultas.

## Para qué sirve

Las API web devuelven JSON, muchas aplicaciones guardan atributos variables como JSON y algunos archivos de intercambio lo usan. Con las funciones JSON de SQL Server se puede consultar ese texto con SQL, sin pasar por la aplicación.

:::note[Definición]
SQL Server 2022 **no tiene un tipo de dato `json`**: el JSON se guarda en columnas de texto (`NVARCHAR(MAX)` es lo habitual) y las funciones lo interpretan cada vez que se las invoca. Las funciones JSON requieren nivel de compatibilidad 130 o superior (SQL Server 2016 en adelante).
:::

Resumen de las herramientas, con la documentación de Microsoft como referencia:

| Herramienta | Qué hace |
|---|---|
| `ISJSON(texto)` | Devuelve 1 si el texto es JSON válido y 0 si no |
| `JSON_VALUE(texto, ruta)` | Extrae un valor **escalar** (cadena, número, booleano) como texto |
| `JSON_QUERY(texto, ruta)` | Extrae un **objeto o arreglo** como JSON |
| `JSON_MODIFY(texto, ruta, valor)` | Devuelve el JSON con un valor actualizado, agregado o eliminado |
| `OPENJSON(texto [, ruta])` | Convierte JSON en filas, con o sin esquema (`WITH`) |
| `FOR JSON PATH` / `FOR JSON AUTO` | Genera JSON a partir del resultado de una consulta |
| `JSON_OBJECT`, `JSON_ARRAY` | Construyen JSON a partir de valores (SQL Server 2022) |

Las rutas empiezan con `$` (la raíz): `$.direccion.ciudad` para una propiedad anidada y `$.etiquetas[0]` para un elemento de un arreglo (los índices empiezan en 0).

## ISJSON, JSON_VALUE y JSON_QUERY

`JSON_VALUE` devuelve siempre texto (hasta 4000 caracteres) y solo para valores escalares: si la ruta apunta a un objeto o arreglo, en modo `lax` devuelve `NULL`. Para objetos y arreglos se usa `JSON_QUERY`.

<!-- check: U2.T.JSON.01 -->
```sql
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
       JSON_QUERY(@Json, '$.etiquetas')        AS ArregloConJsonQuery,
       JSON_VALUE(@Json, '$.inexistente')      AS Inexistente;
```

**Resultado esperado.**

| Cliente | Activo | Limite | Ciudad | SegundaEtiqueta | ObjetoConJsonValue | ObjetoConJsonQuery | ArregloConJsonQuery | Inexistente |
|---|---|---|---|---|---|---|---|---|
| Ferretería Norte | true | 25000.50 | Rosario | frecuente | NULL | `{ "ciudad": "Rosario", "cp": "S2000" }` | `["mayorista", "frecuente"]` | NULL |

Para usar un valor como número hay que convertirlo (`CAST(JSON_VALUE(...) AS DECIMAL(10,2))`). Una ruta inexistente devuelve `NULL` y no un error, salvo que se use el modo `strict` (más abajo).

`ISJSON` sirve para validar antes de procesar, y para impedir que una columna guarde texto inválido con una restricción `CHECK`:

<!-- check: U2.T.JSON.02 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    ProductoId INT IDENTITY(1, 1) NOT NULL,
    Nombre     VARCHAR(60)        NOT NULL,
    Atributos  NVARCHAR(MAX)      NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (ProductoId),
    CONSTRAINT CK_Producto_Atributos CHECK (Atributos IS NULL OR ISJSON(Atributos) = 1)
);
GO

INSERT INTO ventas.Producto (Nombre, Atributos)
VALUES ('Taladro', N'{"marca":"Zeta","potenciaW":650}');

DECLARE @Error INT = 0;
BEGIN TRY
    INSERT INTO ventas.Producto (Nombre, Atributos)
    VALUES ('Martillo', N'{"marca":"Zeta", potencia: }');
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT @Error AS NumeroDeError,
       (SELECT COUNT(*) FROM ventas.Producto) AS FilasGuardadas,
       ISJSON(N'{"a":1}') AS EsJson1,
       ISJSON(N'{a:1}')   AS EsJson2,
       ISJSON(N'[1,2,3]') AS EsJson3,
       ISJSON(N'texto')   AS EsJson4;
```

**Resultado esperado.**

| NumeroDeError | FilasGuardadas | EsJson1 | EsJson2 | EsJson3 | EsJson4 |
|---:|---:|---:|---:|---:|---:|
| 547 | 1 | 1 | 0 | 1 | 0 |

El error 547 es la violación del `CHECK`. Las claves sin comillas (`{a:1}`) no son JSON válido.

## JSON_MODIFY

`JSON_MODIFY` no cambia el texto original: **devuelve un JSON nuevo** que hay que asignar (por ejemplo con `UPDATE`). Actualiza si la propiedad existe, la agrega si no existe, la elimina si el valor es `NULL` y agrega un elemento a un arreglo con el prefijo `append`.

<!-- check: U2.T.JSON.03 -->
```sql
DECLARE @Atributos NVARCHAR(MAX) = N'{"marca":"Zeta","potenciaW":650,"color":"gris","accesorios":["broca","maletin"]}';

SELECT JSON_MODIFY(@Atributos, '$.potenciaW', 750)                  AS Actualiza,
       JSON_MODIFY(@Atributos, '$.garantiaAnios', 2)                AS Agrega,
       JSON_MODIFY(@Atributos, '$.color', NULL)                     AS Elimina,
       JSON_MODIFY(@Atributos, 'append $.accesorios', 'llave')      AS AgregaAlArreglo;
```

**Resultado esperado.**

| Actualiza | Agrega | Elimina | AgregaAlArreglo |
|---|---|---|---|
| `{"marca":"Zeta","potenciaW":750,"color":"gris","accesorios":["broca","maletin"]}` | `{"marca":"Zeta","potenciaW":650,"color":"gris","accesorios":["broca","maletin"],"garantiaAnios":2}` | `{"marca":"Zeta","potenciaW":650,"accesorios":["broca","maletin"]}` | `{"marca":"Zeta","potenciaW":650,"color":"gris","accesorios":["broca","maletin","llave"]}` |

Para insertar un fragmento JSON (un objeto o arreglo) y no una cadena, hay que envolverlo en `JSON_QUERY(...)`; si no, se guarda como texto escapado.

## OPENJSON sin esquema

Sin cláusula `WITH`, `OPENJSON` devuelve una fila por cada propiedad del nivel indicado, con tres columnas: `key`, `value` y `type`.

<!-- check: U2.T.JSON.04 -->
```sql
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
```

**Resultado esperado.**

| Clave | Valor | Tipo |
|---|---|---:|
| codigo | P001 | 1 |
| nombre | Cuaderno rayado | 1 |
| precio | 1250.50 | 2 |
| activo | true | 3 |
| etiquetas | `["escolar", "papeleria"]` | 4 |
| proveedor | `{ "nombre": "Papelera Sur" }` | 5 |
| descuento | NULL | 0 |

La propiedad `descuento` es `null` en el JSON y `value` es un `NULL` de SQL (no el texto `null`). El orden de las filas es el del documento.

| `type` | Tipo JSON |
|---:|---|
| 0 | null |
| 1 | cadena |
| 2 | número |
| 3 | booleano |
| 4 | arreglo |
| 5 | objeto |

## OPENJSON con esquema (WITH)

La cláusula `WITH` define las columnas de salida: nombre, tipo T-SQL y ruta. Las propiedades que faltan dan `NULL`.

<!-- check: U2.T.JSON.05 -->
```sql
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
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock | Proveedor | Descuento |
|---|---|---:|---:|---|---|
| P001 | Cuaderno rayado | 1250.50 | 40 | Papelera Sur | NULL |

:::tip[Códigos con ceros a la izquierda]
Si un identificador es `"02"` y se lo declara `INT`, se pierde el cero. Cuando el valor es un código y no un número, declaralo como `CHAR` o `VARCHAR`.
:::

## AS JSON: objetos y arreglos anidados

Cuando una propiedad es un objeto o un arreglo, `WITH` no puede devolverla como columna escalar. Se declara la columna como `NVARCHAR(MAX)` y se agrega `AS JSON`: así se obtiene el fragmento como texto JSON, que se puede volver a abrir con otro `OPENJSON` mediante `CROSS APPLY`.

:::caution[Regla de AS JSON]
`AS JSON` solo se admite con una columna de tipo `NVARCHAR(MAX)` y siempre con una ruta. No es una forma de calcular una columna: `subtotal AS JSON` sin tipo ni ruta es un error de sintaxis. Los cálculos se hacen fuera del `WITH`.
:::

<!-- check: U2.T.JSON.06 -->
```sql
DECLARE @Json NVARCHAR(MAX) = N'{
    "pedido": 1001,
    "cliente": "Ferretería Norte",
    "lineas": [
        { "producto": "P001", "cantidad": 2, "precio": 1250.50 },
        { "producto": "P003", "cantidad": 10, "precio": 480.25 }
    ]
}';

-- AS JSON conserva el arreglo como texto JSON; el segundo OPENJSON lo despliega en filas
SELECT c.Pedido, c.Cliente, l.Producto, l.Cantidad, l.Precio
FROM OPENJSON(@Json)
WITH (
    Pedido  INT           '$.pedido',
    Cliente VARCHAR(40)   '$.cliente',
    Lineas  NVARCHAR(MAX) '$.lineas' AS JSON
) AS c
CROSS APPLY OPENJSON(c.Lineas)
WITH (
    Producto CHAR(4)       '$.producto',
    Cantidad INT           '$.cantidad',
    Precio   DECIMAL(10,2) '$.precio'
) AS l
ORDER BY l.Producto;
```

**Resultado esperado.**

| Pedido | Cliente | Producto | Cantidad | Precio |
|---:|---|---|---:|---:|
| 1001 | Ferretería Norte | P001 | 2 | 1250.50 |
| 1001 | Ferretería Norte | P003 | 10 | 480.25 |

## Ruta como segundo argumento y modos lax y strict

Si solo interesa el arreglo, se puede pasar su ruta como segundo argumento de `OPENJSON` y evitar el primer `WITH`:

<!-- check: U2.T.JSON.07 -->
```sql
DECLARE @Json NVARCHAR(MAX) = N'{
    "pedido": 1001,
    "lineas": [
        { "producto": "P001", "cantidad": 2 },
        { "producto": "P003", "cantidad": 10 }
    ]
}';

SELECT Producto, Cantidad, Descuento
FROM OPENJSON(@Json, '$.lineas')
WITH (
    Producto  CHAR(4) '$.producto',
    Cantidad  INT     '$.cantidad',
    Descuento INT     '$.descuento'
)
ORDER BY Producto;
```

**Resultado esperado.**

| Producto | Cantidad | Descuento |
|---|---:|---|
| P001 | 2 | NULL |
| P003 | 10 | NULL |

Por defecto las rutas usan el modo **lax**: una propiedad inexistente devuelve `NULL`. Con el prefijo `strict` la propiedad faltante es un error (13608):

<!-- check: U2.T.JSON.08 -->
```sql
DECLARE @Json NVARCHAR(MAX) = N'{"producto": "P001", "cantidad": 2}';
DECLARE @Error INT = 0;
DECLARE @Mensaje NVARCHAR(200) = N'';

BEGIN TRY
    SELECT Producto, Descuento
    FROM OPENJSON(@Json)
    WITH (
        Producto  CHAR(4) '$.producto',
        Descuento INT     'strict $.descuento'
    );
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    SET @Mensaje = ERROR_MESSAGE();
END CATCH;

SELECT @Error AS NumeroDeError, @Mensaje AS Mensaje,
       JSON_VALUE(@Json, 'lax $.descuento') AS ConLax;
```

**Resultado esperado.**

| NumeroDeError | Mensaje | ConLax |
|---:|---|---|
| 13608 | Property cannot be found on the specified JSON path. | NULL |

El texto del mensaje depende del idioma de la instalación.

## Generar JSON con FOR JSON

`FOR JSON` convierte el resultado de una consulta en JSON. Con `PATH` el nombre de cada columna define la estructura; con `AUTO` la estructura se deduce de las tablas de la consulta. Los ejemplos usan estas tablas:

<!-- check: U2.T.JSON.09 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    Ciudad    VARCHAR(30) NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE ventas.Pedido (
    PedidoId  INT           NOT NULL,
    ClienteId INT           NOT NULL,
    Fecha     DATE          NOT NULL,
    Total     DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId),
    CONSTRAINT FK_Pedido_Cliente FOREIGN KEY (ClienteId) REFERENCES ventas.Cliente (ClienteId)
);
GO

INSERT INTO ventas.Cliente (ClienteId, Nombre, Ciudad)
VALUES (1, 'Ferretería Norte', 'Rosario'), (2, 'Kiosco Central', NULL);

INSERT INTO ventas.Pedido (PedidoId, ClienteId, Fecha, Total)
VALUES (1001, 1, '2026-03-02', 3000.00),
       (1002, 1, '2026-03-09', 1250.50),
       (1003, 2, '2026-03-10', 480.25);
GO
```

Cada bloque de esta sección usa ese juego de datos y se ejecuta justo después de él. Por defecto, las columnas `NULL` se omiten del resultado.

<!-- check: U2.T.JSON.09 -->
```sql
SELECT ClienteId, Nombre, Ciudad
FROM ventas.Cliente
ORDER BY ClienteId
FOR JSON PATH;
```

**Resultado esperado.**

```json
[{"ClienteId":1,"Nombre":"Ferretería Norte","Ciudad":"Rosario"},{"ClienteId":2,"Nombre":"Kiosco Central"}]
```

Con alias que contienen puntos se anidan objetos; `ROOT` agrega un objeto raíz e `INCLUDE_NULL_VALUES` conserva los nulos:

<!-- check: U2.T.JSON.10 -->
```sql
SELECT ClienteId AS [id],
       Nombre    AS [datos.nombre],
       Ciudad    AS [datos.ciudad]
FROM ventas.Cliente
ORDER BY ClienteId
FOR JSON PATH, ROOT('clientes'), INCLUDE_NULL_VALUES;
```

**Resultado esperado.**

```json
{"clientes":[{"id":1,"datos":{"nombre":"Ferretería Norte","ciudad":"Rosario"}},{"id":2,"datos":{"nombre":"Kiosco Central","ciudad":null}}]}
```

Con `AUTO`, un `JOIN` produce un arreglo anidado por cada tabla (el alias de la tabla interna, `p`, pasa a ser el nombre del arreglo):

<!-- check: U2.T.JSON.11 -->
```sql
SELECT c.ClienteId, c.Nombre, p.PedidoId, p.Total
FROM ventas.Cliente AS c
INNER JOIN ventas.Pedido AS p ON p.ClienteId = c.ClienteId
ORDER BY c.ClienteId, p.PedidoId
FOR JSON AUTO;
```

**Resultado esperado.**

```json
[{"ClienteId":1,"Nombre":"Ferretería Norte","p":[{"PedidoId":1001,"Total":3000.00},{"PedidoId":1002,"Total":1250.50}]},{"ClienteId":2,"Nombre":"Kiosco Central","p":[{"PedidoId":1003,"Total":480.25}]}]
```

Para controlar los nombres, se usa una subconsulta con `FOR JSON PATH` en una columna con alias; el motor la incrusta como JSON y no como texto:

<!-- check: U2.T.JSON.12 -->
```sql
SELECT c.ClienteId AS [id],
       c.Nombre    AS [nombre],
       (SELECT p.PedidoId AS [pedido], p.Total AS [total]
        FROM ventas.Pedido AS p
        WHERE p.ClienteId = c.ClienteId
        ORDER BY p.PedidoId
        FOR JSON PATH) AS [pedidos]
FROM ventas.Cliente AS c
ORDER BY c.ClienteId
FOR JSON PATH;
```

**Resultado esperado.**

```json
[{"id":1,"nombre":"Ferretería Norte","pedidos":[{"pedido":1001,"total":3000.00},{"pedido":1002,"total":1250.50}]},{"id":2,"nombre":"Kiosco Central","pedidos":[{"pedido":1003,"total":480.25}]}]
```

`WITHOUT_ARRAY_WRAPPER` quita los corchetes cuando se espera un único objeto:

<!-- check: U2.T.JSON.13 -->
```sql
SELECT ClienteId, Nombre
FROM ventas.Cliente
WHERE ClienteId = 1
FOR JSON PATH, WITHOUT_ARRAY_WRAPPER;
```

**Resultado esperado.**

```json
{"ClienteId":1,"Nombre":"Ferretería Norte"}
```

## JSON_OBJECT y JSON_ARRAY

:::note[SQL Server 2022]
`JSON_OBJECT` y `JSON_ARRAY` están disponibles desde SQL Server 2022. Si el servidor es anterior, hay que armar el texto con `FOR JSON` o concatenando.
:::

`JSON_OBJECT` se escribe como `'clave': valor` y `JSON_ARRAY` como una lista de valores. En el objeto, `NULL ON NULL` (por defecto) conserva los nulos y `ABSENT ON NULL` los omite; en el arreglo es al revés: por defecto se omiten.

<!-- check: U2.T.JSON.14 -->
```sql
SELECT JSON_OBJECT('codigo': 'P001', 'precio': 1250.50, 'stock': NULL)                AS ObjetoPorDefecto,
       JSON_OBJECT('codigo': 'P001', 'precio': 1250.50, 'stock': NULL ABSENT ON NULL) AS ObjetoSinNulos,
       JSON_ARRAY('azul', 'rojo', NULL)                                                AS ArregloPorDefecto,
       JSON_ARRAY('azul', 'rojo', NULL NULL ON NULL)                                   AS ArregloConNulos,
       JSON_OBJECT('lineas': JSON_ARRAY(1, 2, 3))                                      AS Anidado;
```

**Resultado esperado.**

| ObjetoPorDefecto | ObjetoSinNulos | ArregloPorDefecto | ArregloConNulos | Anidado |
|---|---|---|---|---|
| `{"codigo":"P001","precio":1250.50,"stock":null}` | `{"codigo":"P001","precio":1250.50}` | `["azul","rojo"]` | `["azul","rojo",null]` | `{"lineas":[1,2,3]}` |

## Rendimiento: consultar una propiedad con un índice

Filtrar con `JSON_VALUE` en el `WHERE` obliga a leer y analizar el JSON de cada fila. Para buscar por una propiedad con frecuencia, se crea una **columna calculada** con `JSON_VALUE` y un índice sobre ella. El motor puede usar el índice cuando la consulta compara contra esa columna.

<!-- check: U2.T.JSON.15 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    ProductoId INT IDENTITY(1, 1) NOT NULL,
    Nombre     VARCHAR(60)        NOT NULL,
    Atributos  NVARCHAR(MAX)      NOT NULL,
    Marca      AS CAST(JSON_VALUE(Atributos, '$.marca') AS NVARCHAR(40)),
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (ProductoId)
);

CREATE INDEX IX_Producto_Marca ON ventas.Producto (Marca);
GO

INSERT INTO ventas.Producto (Nombre, Atributos)
VALUES ('Taladro',  N'{"marca":"Zeta","potenciaW":650}'),
       ('Martillo', N'{"marca":"Alfa"}'),
       ('Sierra',   N'{"marca":"Zeta","hojas":3}');

SELECT Nombre, Marca
FROM ventas.Producto
WHERE Marca = N'Zeta'
ORDER BY Nombre;
```

**Resultado esperado.**

| Nombre | Marca |
|---|---|
| Sierra | Zeta |
| Taladro | Zeta |

## Leer un archivo JSON

Para cargar un archivo `.json` del disco en tablas se combina `OPENROWSET(BULK ...)` con `OPENJSON`. Ese patrón, con su problema de codificación, está en [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/).

## Errores frecuentes

:::caution[Errores frecuentes]
- **Usar `JSON_VALUE` para un objeto o un arreglo.** Devuelve `NULL` en modo lax; hay que usar `JSON_QUERY`.
- **Olvidar que `JSON_MODIFY` no modifica la variable.** Devuelve un texto nuevo: `SET @Json = JSON_MODIFY(@Json, ...)`.
- **Comparar números como texto.** `JSON_VALUE` devuelve `NVARCHAR`; `'9' > '10'` es verdadero como texto. Convertí con `CAST`.
- **Esperar un error ante una propiedad inexistente.** En modo lax da `NULL`; si el dato es obligatorio, usá `strict`.
- **Escribir `columna AS JSON` sin tipo ni ruta** (ver el recuadro de la sección AS JSON).
:::

## Autoevaluación

<details>
<summary>1. ¿Qué devuelve `JSON_VALUE` cuando la ruta apunta a una propiedad que es un objeto?</summary>

`NULL` en modo lax (y un error en modo `strict`). Para un objeto se usa `JSON_QUERY`.
</details>

<details>
<summary>2. ¿Cómo se despliega en filas un arreglo anidado dentro de cada fila de una tabla?</summary>

Con `CROSS APPLY OPENJSON(columna) WITH (...)`; si el arreglo está en una propiedad, se la extrae con `AS JSON` o se pasa la ruta como segundo argumento.
</details>

<details>
<summary>3. ¿Qué diferencia hay entre `FOR JSON AUTO` y `FOR JSON PATH` en una consulta con `JOIN`?</summary>

`AUTO` anida cada tabla como un arreglo dentro de la anterior y no permite elegir los nombres; `PATH` devuelve filas planas, salvo que los alias tengan puntos o se usen subconsultas, y da control total sobre la estructura.
</details>

## En resumen

:::tip[En resumen]
- SQL Server guarda JSON como texto; `ISJSON` lo valida y se puede exigir con un `CHECK`.
- `JSON_VALUE` extrae escalares, `JSON_QUERY` fragmentos y `JSON_MODIFY` devuelve un JSON modificado.
- `OPENJSON` convierte JSON en filas (con o sin `WITH`; `AS JSON` y `CROSS APPLY` para anidados).
- `FOR JSON PATH/AUTO` genera JSON; `JSON_OBJECT` y `JSON_ARRAY` lo construyen en SQL Server 2022.
:::

:::tip[Para seguir]
Practicá con la [Práctica — JSON en SQL Server](/bbdd-aplicadas/unidad-2/practica/json/) y después seguí con [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/).
:::

## Fuentes

- Presentación de cátedra, Unidad 2, parte 2 (Formatos de intercambio), diapositivas 15 a 18 (formato JSON).
- Microsoft Learn, [Datos JSON en SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server), [OPENJSON](https://learn.microsoft.com/en-us/sql/t-sql/functions/openjson-transact-sql), [JSON_VALUE](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-value-transact-sql), [JSON_QUERY](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-query-transact-sql), [JSON_MODIFY](https://learn.microsoft.com/en-us/sql/t-sql/functions/json-modify-transact-sql), [ISJSON](https://learn.microsoft.com/en-us/sql/t-sql/functions/isjson-transact-sql), [FOR JSON](https://learn.microsoft.com/en-us/sql/relational-databases/json/format-query-results-as-json-with-for-json-sql-server).
