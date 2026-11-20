---
title: Práctica — JSON en SQL Server
slug: bbdd-aplicadas/unidad-2/practica/json
sidebar:
  label: JSON en SQL Server
  order: 1
---

Siete ejercicios de validación, consulta, modificación y generación de JSON. Presuponen la lección de [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/). Los datos son propios y no hacen falta archivos externos.

## Conjunto de datos

Creá una base de práctica (por ejemplo `CREATE DATABASE PracticaJson;`; necesitás el permiso `CREATE DATABASE` o una base que te hayan dado, ver [Cómo estudiar · Antes de ejecutar los ejemplos](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos)), cambiá a ella con `USE PracticaJson;` y ejecutá este script una sola vez:

<!-- check: U2.22 -->
```sql
CREATE SCHEMA tienda;
GO

CREATE TABLE tienda.Producto (
    ProductoId INT IDENTITY(1, 1) NOT NULL,
    Nombre     VARCHAR(60)        NOT NULL,
    Categoria  VARCHAR(30)        NOT NULL,
    Precio     DECIMAL(10,2)      NOT NULL,
    Stock      INT                NOT NULL,
    Atributos  NVARCHAR(MAX)      NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (ProductoId)
);

CREATE TABLE tienda.Pedido (
    PedidoId INT          NOT NULL,
    Cliente  VARCHAR(40)  NOT NULL,
    Fecha    DATE         NOT NULL,
    Detalle  NVARCHAR(MAX) NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId)
);
GO

INSERT INTO tienda.Producto (Nombre, Categoria, Precio, Stock, Atributos)
VALUES ('Notebook 15',    'Computacion', 1299.99, 12, N'{"marca":"Zeta","ramGb":16,"color":"negro"}'),
       ('Mouse inalambrico', 'Perifericos', 29.99, 85, N'{"marca":"Alfa","dpi":1600,"color":"gris"}'),
       ('Monitor 27',    'Computacion',  349.99, 20, N'{"marca":"Zeta","panel":"IPS","hz":144}'),
       ('Teclado mecanico', 'Perifericos', 89.99, 40, N'{"marca":"Alfa","retroiluminado":true,"colores":["rojo","azul"]}');

INSERT INTO tienda.Pedido (PedidoId, Cliente, Fecha, Detalle)
VALUES (1, 'Cliente A', '2026-03-10',
        N'[{"productoId":1,"cantidad":1,"precio":1299.99},{"productoId":2,"cantidad":2,"precio":29.99}]'),
       (2, 'Cliente B', '2026-03-11',
        N'[{"productoId":3,"cantidad":1,"precio":349.99},{"productoId":4,"cantidad":3,"precio":89.99}]'),
       (3, 'Cliente A', '2026-03-12',
        N'[{"productoId":4,"cantidad":2,"precio":89.99}]');
GO
```

Cada resolución parte de este conjunto de datos recién creado.

---

### Ejercicio 1 · Exigir JSON válido en una columna
<!-- ejercicio: U2.22 | nivel: inicial | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
La columna `Atributos` acepta cualquier texto. Agregá una restricción que exija JSON válido (o `NULL`), intentá insertar un producto con el texto `{marca: Zeta` y mostrá el número de error, la cantidad de productos y cuántos tienen JSON válido.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Una restricción `CHECK` con `ISJSON(Atributos) = 1` rechaza el texto inválido con el error 547. Como `ISJSON(NULL)` devuelve `NULL`, la condición admite explícitamente `NULL`. El error se captura con `TRY/CATCH`.

<!-- check: U2.22 -->
```sql
DECLARE @Error INT = 0;

ALTER TABLE tienda.Producto
    ADD CONSTRAINT CK_Producto_Atributos CHECK (Atributos IS NULL OR ISJSON(Atributos) = 1);

BEGIN TRY
    INSERT INTO tienda.Producto (Nombre, Categoria, Precio, Stock, Atributos)
    VALUES ('Producto roto', 'Prueba', 1.00, 0, N'{marca: Zeta');
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT @Error AS NumeroDeError,
       COUNT(*) AS Productos,
       SUM(ISJSON(Atributos)) AS ConJsonValido
FROM tienda.Producto;
```

**Resultado esperado.**

| NumeroDeError | Productos | ConJsonValido |
|---:|---:|---:|
| 547 | 4 | 4 |

El producto roto no se insertó: quedan los 4 originales, todos con JSON válido.
</details>

### Ejercicio 2 · Extraer valores y fragmentos
<!-- ejercicio: U2.23 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Listá los productos de la marca `Alfa` con su nombre, marca, color y la lista de colores (un arreglo). Cuando una propiedad no existe, el resultado debe ser `NULL` y no un error. Ordenalos por nombre.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `marca` y `color` son escalares: `JSON_VALUE`. `colores` es un arreglo: `JSON_QUERY` (con `JSON_VALUE` daría `NULL`). Por defecto las rutas son `lax`, así que una propiedad inexistente da `NULL`. El filtro puede usar `JSON_VALUE` en el `WHERE`.

<!-- check: U2.23 -->
```sql
SELECT Nombre,
       JSON_VALUE(Atributos, '$.marca')  AS Marca,
       JSON_VALUE(Atributos, '$.color')  AS Color,
       JSON_QUERY(Atributos, '$.colores') AS Colores
FROM tienda.Producto
WHERE JSON_VALUE(Atributos, '$.marca') = 'Alfa'
ORDER BY Nombre;
```

**Resultado esperado.**

| Nombre | Marca | Color | Colores |
|---|---|---|---|
| Mouse inalambrico | Alfa | gris | NULL |
| Teclado mecanico | Alfa | NULL | `["rojo","azul"]` |

El mouse no tiene `colores` y el teclado no tiene `color`: ambos dan `NULL`.
</details>

### Ejercicio 3 · Total de cada pedido
<!-- ejercicio: U2.24 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Cada pedido guarda sus líneas en `Detalle`, un arreglo JSON con `productoId`, `cantidad` y `precio`. Calculá el total de cada pedido (suma de cantidad por precio), con el número de pedido y el cliente.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `CROSS APPLY OPENJSON(p.Detalle) WITH (...)` convierte el arreglo de cada pedido en filas con tipos; después se agrupa por pedido y se suma. Los precios se declaran `DECIMAL(10,2)` para evitar errores de redondeo.

<!-- check: U2.24 -->
```sql
SELECT p.PedidoId,
       p.Cliente,
       SUM(l.Cantidad * l.Precio) AS Total
FROM tienda.Pedido AS p
CROSS APPLY OPENJSON(p.Detalle)
WITH (
    ProductoId INT           '$.productoId',
    Cantidad   INT           '$.cantidad',
    Precio     DECIMAL(10,2) '$.precio'
) AS l
GROUP BY p.PedidoId, p.Cliente
ORDER BY p.PedidoId;
```

**Resultado esperado.**

| PedidoId | Cliente | Total |
|---:|---|---:|
| 1 | Cliente A | 1359.97 |
| 2 | Cliente B | 619.96 |
| 3 | Cliente A | 179.98 |
</details>

### Ejercicio 4 · Modificar propiedades con JSON_MODIFY
<!-- ejercicio: U2.25 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
En el producto `Notebook 15`: cambiá `ramGb` a 32, agregá `garantiaAnios` con valor 2 y eliminá `color`. En el `Teclado mecanico`: agregá `verde` al arreglo `colores`. Mostrá los `Atributos` resultantes de ambos productos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `JSON_MODIFY` devuelve un JSON nuevo, así que hay que asignarlo con `UPDATE`. Para varios cambios se anidan las llamadas: la salida de una es la entrada de la siguiente. Asignar `NULL` elimina la propiedad y el prefijo `append` agrega un elemento a un arreglo.

<!-- check: U2.25 -->
```sql
UPDATE tienda.Producto
SET Atributos = JSON_MODIFY(
                    JSON_MODIFY(
                        JSON_MODIFY(Atributos, '$.ramGb', 32),
                        '$.garantiaAnios', 2),
                    '$.color', NULL)
WHERE Nombre = 'Notebook 15';

UPDATE tienda.Producto
SET Atributos = JSON_MODIFY(Atributos, 'append $.colores', 'verde')
WHERE Nombre = 'Teclado mecanico';

SELECT Nombre, Atributos
FROM tienda.Producto
WHERE Nombre IN ('Notebook 15', 'Teclado mecanico')
ORDER BY Nombre;
```

**Resultado esperado.**

| Nombre | Atributos |
|---|---|
| Notebook 15 | `{"marca":"Zeta","ramGb":32,"garantiaAnios":2}` |
| Teclado mecanico | `{"marca":"Alfa","retroiluminado":true,"colores":["rojo","azul","verde"]}` |
</details>

### Ejercicio 5 · Catálogo con objetos anidados
<!-- ejercicio: U2.26 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Generá un JSON con la raíz `catalogo` con los productos de la categoría `Perifericos`. Cada producto debe tener `id`, `nombre`, `precio` y un objeto `detalle` con `marca` (sacada de `Atributos`) y `stock`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `FOR JSON PATH` usa los alias como rutas: un punto crea un objeto anidado (`detalle.marca`, `detalle.stock`). `ROOT('catalogo')` agrega la raíz. La marca se extrae con `JSON_VALUE` dentro del `SELECT`.

<!-- check: U2.26 -->
```sql
SELECT ProductoId AS [id],
       Nombre     AS [nombre],
       Precio     AS [precio],
       JSON_VALUE(Atributos, '$.marca') AS [detalle.marca],
       Stock      AS [detalle.stock]
FROM tienda.Producto
WHERE Categoria = 'Perifericos'
ORDER BY ProductoId
FOR JSON PATH, ROOT('catalogo');
```

**Resultado esperado.**

```json
{"catalogo":[{"id":2,"nombre":"Mouse inalambrico","precio":29.99,"detalle":{"marca":"Alfa","stock":85}},{"id":4,"nombre":"Teclado mecanico","precio":89.99,"detalle":{"marca":"Alfa","stock":40}}]}
```
</details>

### Ejercicio 6 · Subtotal por línea y la línea completa
<!-- ejercicio: U2.27 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Para el pedido 2, mostrá una fila por línea con el producto, el subtotal (cantidad por precio) y el texto JSON de la línea completa. Un compañero lo intentó agregando al `WITH` una columna `subtotal AS JSON`; explicá por qué eso es inválido y cómo resolverlo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `AS JSON` solo se admite en una columna `NVARCHAR(MAX)` con una ruta: sirve para **extraer un fragmento JSON** (objeto o arreglo), no para calcular valores. `subtotal AS JSON` carece de tipo y de ruta (y `subtotal` no existe en el documento), por lo que es un error de sintaxis. La solución son dos pasos: la línea completa se obtiene con la ruta `'$'` (el propio elemento) y el cálculo se hace en el `SELECT`, fuera del `WITH`.

<!-- check: U2.27 -->
```sql
-- Subtotal por línea y la línea completa como JSON
SELECT p.PedidoId,
       l.ProductoId,
       l.Cantidad * l.Precio AS Subtotal,
       l.Linea
FROM tienda.Pedido AS p
CROSS APPLY OPENJSON(p.Detalle)
WITH (
    ProductoId INT           '$.productoId',
    Cantidad   INT           '$.cantidad',
    Precio     DECIMAL(10,2) '$.precio',
    Linea      NVARCHAR(MAX) '$' AS JSON
) AS l
WHERE p.PedidoId = 2
ORDER BY l.ProductoId;
```

**Resultado esperado.**

| PedidoId | ProductoId | Subtotal | Linea |
|---:|---:|---:|---|
| 2 | 3 | 349.99 | `{"productoId":3,"cantidad":1,"precio":349.99}` |
| 2 | 4 | 269.97 | `{"productoId":4,"cantidad":3,"precio":89.99}` |
</details>

### Ejercicio 7 · FOR JSON AUTO y FOR JSON PATH
<!-- ejercicio: U2.28 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Creá la tabla `tienda.Categoria` (`Categoria`, `Rubro`) con las categorías `Computacion` y `Perifericos` (rubro `Tecnologia`). Uní las categorías con sus productos y generá el resultado para `Perifericos` con `FOR JSON AUTO` y con `FOR JSON PATH`. ¿En qué se diferencian los resultados?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con `AUTO` el motor deduce la estructura a partir de las tablas de la consulta: las columnas de la primera tabla forman el objeto exterior y las de la segunda un arreglo anidado, que lleva por nombre el alias de la tabla (`p`). Con `PATH` y nombres de columna sin puntos, el resultado es una lista **plana** de filas. En `AUTO` el orden de las columnas del `SELECT` importa: las de una tabla deben estar juntas.

<!-- check: U2.28 -->
```sql
CREATE TABLE tienda.Categoria (
    Categoria VARCHAR(30) NOT NULL,
    Rubro     VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Categoria PRIMARY KEY CLUSTERED (Categoria)
);

INSERT INTO tienda.Categoria (Categoria, Rubro)
VALUES ('Computacion', 'Tecnologia'), ('Perifericos', 'Tecnologia');
GO

-- 1) FOR JSON AUTO: anida la tabla de la derecha dentro de la de la izquierda
SELECT c.Categoria, c.Rubro, p.Nombre, p.Precio
FROM tienda.Categoria AS c
INNER JOIN tienda.Producto AS p ON p.Categoria = c.Categoria
WHERE c.Categoria = 'Perifericos'
ORDER BY c.Categoria, p.Nombre
FOR JSON AUTO;

-- 2) FOR JSON PATH: devuelve filas planas
SELECT c.Categoria, c.Rubro, p.Nombre, p.Precio
FROM tienda.Categoria AS c
INNER JOIN tienda.Producto AS p ON p.Categoria = c.Categoria
WHERE c.Categoria = 'Perifericos'
ORDER BY c.Categoria, p.Nombre
FOR JSON PATH;
```

**Resultado esperado.** Con `AUTO`:

```json
[{"Categoria":"Perifericos","Rubro":"Tecnologia","p":[{"Nombre":"Mouse inalambrico","Precio":29.99},{"Nombre":"Teclado mecanico","Precio":89.99}]}]
```

Con `PATH`:

```json
[{"Categoria":"Perifericos","Rubro":"Tecnologia","Nombre":"Mouse inalambrico","Precio":29.99},{"Categoria":"Perifericos","Rubro":"Tecnologia","Nombre":"Teclado mecanico","Precio":89.99}]
```

`AUTO` evita repetir los datos de la categoría; `PATH` los repite en cada fila pero da control sobre los nombres y la forma.
</details>
