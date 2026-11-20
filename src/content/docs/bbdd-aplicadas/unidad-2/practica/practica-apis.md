---
title: Práctica — APIs desde SQL Server
slug: bbdd-aplicadas/unidad-2/practica/apis
sidebar:
  label: APIs desde SQL Server
  order: 6
  badge:
    text: Complementario
    variant: note
---

:::note[Contenido complementario]
Los ejercicios 2 a 5 trabajan con SQL Server y no forman parte del programa 2024; el ejercicio 1 es conceptual y corresponde a "Qué es una API". Se conservan como práctica complementaria.
:::

Cinco ejercicios sobre API REST y sobre cómo procesar sus respuestas desde T-SQL. Presuponen la lección de [APIs desde SQL Server](/bbdd-aplicadas/unidad-2/teoria/apis-desde-sql/) y [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/). Las respuestas de las API se trabajan **guardadas como texto**, de modo que los ejercicios se pueden reproducir sin red. Los ejercicios 1 a 4 no modifican la configuración del servidor. Creá una base de práctica (por ejemplo `CREATE DATABASE PracticaApis;`, ver [Cómo estudiar · Antes de ejecutar los ejemplos](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos)) y cambiá a ella con `USE PracticaApis;`.

:::danger[Seguridad]
El ejercicio 5 usa `Ole Automation Procedures`. No lo habilites en un servidor compartido ni de producción: amplía la superficie de ataque de la instancia. Si lo probás en una instancia local de práctica, volvé a dejar la opción en 0 al terminar.
:::

---

### Ejercicio 1 · Leer una solicitud REST
<!-- ejercicio: U2.36 | nivel: inicial | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Para cada solicitud a la API ficticia `https://api.ejemplo.test`, indicá el recurso, el verbo HTTP más adecuado y el código de estado que se espera en una respuesta exitosa: (a) obtener los datos del pedido 7; (b) crear un pedido nuevo con los datos en el cuerpo; (c) eliminar el pedido 7; (d) pedir el pedido 9999, que no existe.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El **recurso** se identifica en la URL; el **verbo** indica la operación; el código de estado informa el resultado (2xx éxito, 4xx error del cliente, 5xx error del servidor).

| Caso | Recurso (URL) | Verbo | Respuesta |
|---|---|---|---|
| (a) | `/pedidos/7` | `GET` | `200 OK` con el pedido en JSON |
| (b) | `/pedidos` (los datos van en el cuerpo, `Content-Type: application/json`) | `POST` | `201 Created` con el recurso creado |
| (c) | `/pedidos/7` | `DELETE` | `200 OK` o `204 No Content` (según cómo lo implemente la API) |
| (d) | `/pedidos/9999` | `GET` | `404 Not Found`: es un error del cliente (familia 4xx), no del servidor |

El caso (d) muestra por qué hay que verificar el código de estado antes de procesar el cuerpo: la respuesta existe, pero no contiene el recurso. En Postman se ve el código junto al cuerpo de la respuesta.
</details>

### Ejercicio 2 · Estado de Ole Automation Procedures
<!-- ejercicio: U2.37 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Sin cambiar la configuración, determiná si `Ole Automation Procedures` está habilitada en tu instancia consultando `sys.configurations`, y comprobá qué ocurre al intentar crear el objeto `MSXML2.XMLHTTP`. Capturá el error y mostralo junto con el estado de la opción.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `sys.configurations` tiene el valor configurado (`value`) y el valor en uso (`value_in_use`); `0` significa deshabilitada, el valor por defecto en instancias nuevas. Si está deshabilitada, `sp_OACreate` falla con el error 15281, que se captura con `TRY/CATCH`. No hace falta `sp_configure`.

<!-- check: U2.37 -->
```sql
DECLARE @Objeto INT;
DECLARE @Numero INT = 0;
DECLARE @Mensaje NVARCHAR(400) = N'';

BEGIN TRY
    EXEC sys.sp_OACreate 'MSXML2.XMLHTTP', @Objeto OUTPUT;
END TRY
BEGIN CATCH
    SET @Numero = ERROR_NUMBER();
    SET @Mensaje = LEFT(ERROR_MESSAGE(), 60);
END CATCH;

SELECT c.name AS Opcion, c.value AS Configurado, c.value_in_use AS EnUso,
       @Numero AS Error, @Mensaje AS Mensaje
FROM sys.configurations AS c
WHERE c.name = 'Ole Automation Procedures';
```

**Resultado esperado** (instancia con la configuración por defecto).

| Opcion | Configurado | EnUso | Error | Mensaje |
|---|---:|---:|---:|---|
| Ole Automation Procedures | 0 | 0 | 15281 | SQL Server blocked access to procedure 'sys.sp_OACreate' of |

El mensaje se recorta a 60 caracteres y su idioma depende de la instalación. Si en tu instancia la opción está en 1, `Error` es 0 (y en Windows se habría creado el objeto, que en este ejercicio no se libera: por eso conviene no habilitarla).
</details>

### Ejercicio 3 · Procesar respuestas, incluidos los errores
<!-- ejercicio: U2.38 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Tres llamadas a una API de productos devolvieron estas respuestas: (1) código 200 con un producto; (2) código 404 con `{"error": "producto no encontrado", "id": 999}`; (3) código 200 con un producto cuyo `stock` es `null`. Guardalas en una variable de tabla y devolvé, para cada llamada, si fue procesada o rechazada, los datos del producto (cuando corresponda) y el mensaje de error.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se evalúa el código de estado antes de abrir el cuerpo: solo las respuestas 2xx se pasan a `OPENJSON`. Con `OUTER APPLY` las respuestas rechazadas siguen apareciendo en el resultado con columnas `NULL`; un `CASE` que devuelve `NULL` para las rechazadas evita parsear JSON que no tiene la forma esperada. El mensaje de error se saca con `JSON_VALUE`.

<!-- check: U2.38 -->
```sql
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
```

**Resultado esperado.**

| Llamada | Codigo | Estado | Id | Nombre | Precio | Stock | MensajeDeError |
|---:|---:|---|---:|---|---:|---:|---|
| 1 | 200 | procesada | 42 | Cuaderno rayado | 1250.50 | 12 | NULL |
| 2 | 404 | rechazada | NULL | NULL | NULL | NULL | producto no encontrado |
| 3 | 200 | procesada | 43 | Lapicera azul | 300.00 | NULL | NULL |

La respuesta 3 muestra la diferencia entre una propiedad con valor `null` (stock `NULL`) y una respuesta rechazada.
</details>

### Ejercicio 4 · Persistir cotizaciones de una respuesta
<!-- ejercicio: U2.39 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Una API ficticia de cotizaciones devuelve `{"estado": "ok", "consultadoEn": "...", "resultado": {"moneda": "USD", "cotizaciones": [{"casa": ..., "compra": ..., "venta": ...}]}}`. Escribí el procedimiento `mercado.CargarCotizaciones`, que recibe el texto de la respuesta, lanza un error si no es JSON válido o si `estado` no es `ok`, y carga la tabla `mercado.Cotizacion` (clave: moneda y casa) **sin duplicar**: inserta las casas nuevas y actualiza las existentes. Probalo con tres respuestas: la primera, una segunda con una casa modificada y otra nueva, y una con `estado: error`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** (1) La validación va primero: `ISJSON` y el estado, con `THROW`. (2) La respuesta se convierte en filas con `OPENJSON(@Respuesta, '$.resultado.cotizaciones')`; la moneda y la fecha, que están fuera del arreglo, se leen con `JSON_VALUE` y se repiten en cada fila. La fecha ISO con desfase se convierte a `DATETIMEOFFSET`. (3) `MERGE` hace el insertar o actualizar en una sola sentencia y la hace repetible: volver a cargar la misma respuesta no duplica filas. (4) Después de la respuesta con error, la tabla queda como estaba.

<!-- check: U2.39 -->
```sql
CREATE SCHEMA mercado;
GO

CREATE TABLE mercado.Cotizacion (
    Moneda     CHAR(3)       NOT NULL,
    Casa       VARCHAR(20)   NOT NULL,
    Compra     DECIMAL(10,2) NOT NULL,
    Venta      DECIMAL(10,2) NOT NULL,
    Actualizado DATETIMEOFFSET(0) NOT NULL,
    CONSTRAINT PK_Cotizacion PRIMARY KEY CLUSTERED (Moneda, Casa)
);
GO

CREATE PROCEDURE mercado.CargarCotizaciones
    @Respuesta NVARCHAR(MAX)
AS
BEGIN
    SET NOCOUNT ON;

    IF ISJSON(@Respuesta) = 0 OR JSON_VALUE(@Respuesta, '$.estado') <> 'ok'
        THROW 50001, 'La respuesta no es valida o no tiene estado ok.', 1;

    MERGE mercado.Cotizacion AS destino
    USING (
        SELECT JSON_VALUE(@Respuesta, '$.resultado.moneda') AS Moneda,
               c.Casa, c.Compra, c.Venta,
               CAST(JSON_VALUE(@Respuesta, '$.consultadoEn') AS DATETIMEOFFSET(0)) AS Actualizado
        FROM OPENJSON(@Respuesta, '$.resultado.cotizaciones')
        WITH (
            Casa   VARCHAR(20)   '$.casa',
            Compra DECIMAL(10,2) '$.compra',
            Venta  DECIMAL(10,2) '$.venta'
        ) AS c
    ) AS origen
    ON destino.Moneda = origen.Moneda AND destino.Casa = origen.Casa
    WHEN MATCHED THEN
        UPDATE SET Compra = origen.Compra, Venta = origen.Venta, Actualizado = origen.Actualizado
    WHEN NOT MATCHED THEN
        INSERT (Moneda, Casa, Compra, Venta, Actualizado)
        VALUES (origen.Moneda, origen.Casa, origen.Compra, origen.Venta, origen.Actualizado);
END;
GO

EXEC mercado.CargarCotizaciones N'{"estado":"ok","consultadoEn":"2026-03-10T12:00:00-03:00",
  "resultado":{"moneda":"USD","cotizaciones":[
    {"casa":"mayorista","compra":1000.50,"venta":1010.00},
    {"casa":"minorista","compra":1005.00,"venta":1030.75}]}}';

-- Segunda consulta: cambia una casa, aparece otra y la primera se repite
EXEC mercado.CargarCotizaciones N'{"estado":"ok","consultadoEn":"2026-03-10T15:30:00-03:00",
  "resultado":{"moneda":"USD","cotizaciones":[
    {"casa":"mayorista","compra":1000.50,"venta":1010.00},
    {"casa":"minorista","compra":1010.00,"venta":1040.00},
    {"casa":"turista","compra":1090.00,"venta":1100.00}]}}';

DECLARE @Error INT = 0;
BEGIN TRY
    EXEC mercado.CargarCotizaciones N'{"estado":"error","mensaje":"limite de consultas"}';
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT Moneda, Casa, Compra, Venta, Actualizado, @Error AS ErrorUltimaRespuesta
FROM mercado.Cotizacion
ORDER BY Casa;
```

**Resultado esperado.**

| Moneda | Casa | Compra | Venta | Actualizado | ErrorUltimaRespuesta |
|---|---|---:|---:|---|---:|
| USD | mayorista | 1000.50 | 1010.00 | 2026-03-10 15:30:00 -03:00 | 50001 |
| USD | minorista | 1010.00 | 1040.00 | 2026-03-10 15:30:00 -03:00 | 50001 |
| USD | turista | 1090.00 | 1100.00 | 2026-03-10 15:30:00 -03:00 | 50001 |

Tras dos cargas quedan 3 filas (no 5): `minorista` fue actualizada y `turista` insertada. La tercera respuesta fue rechazada con el error 50001 y no cambió nada.
</details>

### Ejercicio 5 · Una llamada GET real con manejo de errores
<!-- ejercicio: U2.40 | nivel: avanzado | tipo: programabilidad | verificacion: revisado -->

:::note[Enunciado]
En una instancia local de práctica de SQL Server para Windows (**no** en un servidor compartido) y con una API pública que elijas y cuyas condiciones de uso respetes, escribí un script que: (a) crea el objeto `MSXML2.XMLHTTP`; (b) hace un `GET` con el encabezado `Accept: application/json`; (c) lee el código de estado y el cuerpo; (d) lanza un error si el estado no es 200 o el cuerpo no es JSON; (e) ante cualquier error informa el origen y la descripción con `sp_OAGetErrorInfo`; (f) **siempre** libera el objeto con `sp_OADestroy`. Antes de empezar, indicá cómo habilitar la opción y, al terminar, cómo volver a deshabilitarla.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Habilitar la opción (`sp_configure`, con `show advanced options`), ejecutar el script y deshabilitarla. El script crea el objeto, abre la solicitud, la envía y verifica el estado y la validez del JSON **antes** de procesar el cuerpo. La liberación con `sp_OADestroy` va fuera del `TRY`, para que se ejecute siempre. Reemplazá la URL del ejemplo por la de la API elegida (ya codificada: sin espacios ni `|` sin convertir a `%20` y `%7C`).

<!-- check: U2.40 -->
```sql
-- 1) Habilitar (requiere permisos de administrador; solo en una instancia local de práctica)
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'Ole Automation Procedures', 1;
RECONFIGURE;
GO

-- 2) Llamada
DECLARE @Url       NVARCHAR(400) = N'https://api.ejemplo.test/cotizaciones';  -- reemplazar
DECLARE @Objeto    INT;
DECLARE @Resultado INT;
DECLARE @Estado    INT;
DECLARE @Respuesta NVARCHAR(MAX);
DECLARE @Texto     TABLE (Cuerpo NVARCHAR(MAX));

EXEC @Resultado = sys.sp_OACreate 'MSXML2.XMLHTTP', @Objeto OUTPUT;
IF @Resultado <> 0 THROW 50010, 'No se pudo crear el objeto HTTP.', 1;

BEGIN TRY
    EXEC @Resultado = sys.sp_OAMethod @Objeto, 'open', NULL, 'GET', @Url, 'false';
    IF @Resultado <> 0 THROW 50011, 'No se pudo abrir la solicitud.', 1;

    EXEC sys.sp_OAMethod @Objeto, 'setRequestHeader', NULL, 'Accept', 'application/json';
    EXEC @Resultado = sys.sp_OAMethod @Objeto, 'send';
    IF @Resultado <> 0 THROW 50012, 'Falló el envío de la solicitud.', 1;

    EXEC sys.sp_OAGetProperty @Objeto, 'status', @Estado OUTPUT;

    INSERT INTO @Texto (Cuerpo)
    EXEC sys.sp_OAGetProperty @Objeto, 'responseText';
    SELECT @Respuesta = Cuerpo FROM @Texto;

    IF @Estado <> 200 OR ISJSON(@Respuesta) = 0
        THROW 50013, 'La API no devolvió un JSON con estado 200.', 1;

    SELECT @Estado AS EstadoHttp, @Respuesta AS Respuesta;
END TRY
BEGIN CATCH
    DECLARE @Origen VARCHAR(255), @Descripcion VARCHAR(255);
    EXEC sys.sp_OAGetErrorInfo @Objeto, @Origen OUTPUT, @Descripcion OUTPUT;
    SELECT ERROR_MESSAGE() AS Error, @Origen AS Origen, @Descripcion AS Descripcion;
END CATCH;

EXEC sys.sp_OADestroy @Objeto;
GO

-- 3) Volver al estado seguro
EXEC sp_configure 'Ole Automation Procedures', 0;
RECONFIGURE;
GO
```

**Resultado esperado.** Con una API que responde 200 con JSON, una fila con `EstadoHttp = 200` y el texto de la respuesta; con una URL inexistente o una respuesta 404, una fila con el mensaje `La API no devolvió un JSON con estado 200.` (o el error del objeto HTTP, con su origen y descripción). El resultado exacto depende de la API elegida.

**Qué necesitás para ejecutarlo.** Este ejercicio **no se probó en un motor**: requiere acceso a internet, una instancia de SQL Server para Windows con la opción habilitada y permisos de administrador (el objeto COM no existe en SQL Server para Linux) y un servicio externo cuyo comportamiento no controlamos. Para procesar la respuesta una vez guardada, ver el ejercicio 4, que se puede reproducir sin red.
</details>
