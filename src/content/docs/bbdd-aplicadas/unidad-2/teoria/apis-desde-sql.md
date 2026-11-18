---
title: APIs desde SQL Server
slug: bbdd-aplicadas/unidad-2/teoria/apis-desde-sql
sidebar:
  order: 10
  badge:
    text: Parte complementaria
    variant: note
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

La primera sección ("Qué es una API") corresponde al programa 2024. Las secciones sobre cómo consumir una API desde T-SQL son **complementarias**.

## Qué es una API

:::note[Definición]
Una **API** (_Application Programming Interface_) es un contrato implementado en software que permite acceder a datos o servicios de un sistema desde otro sistema. Un sistema (el cliente) hace una **solicitud** (_request_) y el otro (el servidor) devuelve una **respuesta** (_response_). La analogía que usa la cátedra es la del mozo: el cliente pide al mozo, el mozo lleva el pedido a la cocina y trae la comida.
:::

Ejemplo de la cátedra: el sistema de una agencia de turismo se comunica con los sistemas de distintas empresas de transporte (terrestre, aéreo, marítimo) para reservar y comprar pasajes, sin conocer cómo funciona cada uno por dentro.

Según quién puede usarlas, las API se clasifican en:

| Tipo | Descripción |
|---|---|
| **Abiertas o públicas** | Disponibles para uso general; algunas exigen una clave (_token_) y pueden limitar las solicitudes según el plan contratado |
| **Internas o privadas** | Se usan dentro de una organización |
| **De socios** | Permiten intercambiar información con proveedores, clientes o socios comerciales |

Los estilos de comunicación mencionados por la cátedra son SOAP, XML-RPC, JSON-RPC y REST. Las API **REST** (o API HTTP) son las más difundidas, y son las que se tratan acá.

### API REST

En una API REST la información se organiza en **recursos** (un producto, un pedido) y cada recurso se identifica con una **URL**. El cliente indica qué quiere hacer con un **verbo HTTP** y el servidor responde con un **código de estado** y, normalmente, un cuerpo en **JSON** (a veces XML).

| Verbo | Uso habitual |
|---|---|
| `GET` | Consultar un recurso o una lista; los parámetros van en la URL |
| `POST` | Crear un recurso; los datos van en el cuerpo de la solicitud |
| `PUT` / `PATCH` | Reemplazar o modificar parcialmente un recurso |
| `DELETE` | Eliminar un recurso |

Los códigos de estado se agrupan por la primera cifra:

| Familia | Significado | Ejemplos |
|---|---|---|
| 2xx | Éxito | `200 OK`, `201 Created` |
| 3xx | Redirección | `301 Moved Permanently` |
| 4xx | Error del cliente | `400 Bad Request`, `401 Unauthorized`, `404 Not Found` |
| 5xx | Error del servidor | `500 Internal Server Error` |

Una consulta y una creación con una API ficticia se ven así (no se ejecuta, es solo ilustración):

```text
GET https://api.ejemplo.test/productos/42
Authorization: Bearer <token>

200 OK
{ "id": 42, "nombre": "Cuaderno rayado", "precio": 1250.50, "stock": 12 }
```

```text
POST https://api.ejemplo.test/ventas
Content-Type: application/json

{ "productoId": 42, "cantidad": 2 }

201 Created
{ "ventaId": 9875 }
```

### Postman

**Postman** es una plataforma para crear y usar API: permite armar solicitudes (verbo, URL, encabezados y cuerpo), enviarlas, ver el código de estado y la respuesta, y organizarlas en colecciones y entornos. Es la herramienta recomendada para explorar una API antes de programar la llamada. Sus recursos de aprendizaje están en Postman Academy.

## Procesar la respuesta de una API desde T-SQL

Sea cual sea la forma de obtener la respuesta, lo que SQL Server hace con ella es siempre lo mismo: es un texto JSON que se valida y se convierte en filas con las funciones de [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/). El siguiente ejemplo usa una respuesta guardada de una API ficticia de cotizaciones, por lo que **no necesita red** y se puede reproducir siempre.

<!-- check: U2.T.API.01 -->
```sql
-- Respuesta guardada de una API ficticia de cotizaciones (el texto llega en @Respuesta)
DECLARE @Respuesta NVARCHAR(MAX) = N'{
    "estado": "ok",
    "consultadoEn": "2026-03-10T12:00:00-03:00",
    "resultado": {
        "moneda": "USD",
        "cotizaciones": [
            { "casa": "mayorista", "compra": 1000.50, "venta": 1010.00 },
            { "casa": "minorista", "compra": 1005.00, "venta": 1030.75 }
        ]
    }
}';

SELECT JSON_VALUE(@Respuesta, '$.estado')                            AS Estado,
       CAST(JSON_VALUE(@Respuesta, '$.consultadoEn') AS DATETIMEOFFSET(0)) AS ConsultadoEn,
       CAST(JSON_VALUE(@Respuesta, '$.consultadoEn') AS DATETIME2(0))      AS SinOffset,
       JSON_VALUE(@Respuesta, '$.resultado.moneda')                  AS Moneda,
       c.Casa, c.Compra, c.Venta
FROM OPENJSON(@Respuesta, '$.resultado.cotizaciones')
WITH (
    Casa   VARCHAR(20)   '$.casa',
    Compra DECIMAL(10,2) '$.compra',
    Venta  DECIMAL(10,2) '$.venta'
) AS c
ORDER BY c.Casa;
```

**Resultado esperado.**

| Estado | ConsultadoEn | SinOffset | Moneda | Casa | Compra | Venta |
|---|---|---|---|---|---:|---:|
| ok | 2026-03-10 12:00:00 -03:00 | 2026-03-10 12:00:00 | USD | mayorista | 1000.50 | 1010.00 |
| ok | 2026-03-10 12:00:00 -03:00 | 2026-03-10 12:00:00 | USD | minorista | 1005.00 | 1030.75 |

La columna `SinOffset` muestra que convertir una fecha ISO 8601 con desfase a `DATETIME2` **descarta el desfase** (no convierte a UTC): si el desfase importa, usá `DATETIMEOFFSET`.

## Llamar a una API desde T-SQL con Ole Automation

:::note[Contenido complementario]
Esta sección y las siguientes no forman parte del programa 2024. Se conservan como primer contacto práctico con las API usando el lenguaje de la materia.
:::

:::danger[Seguridad: no habilitar en producción]
`Ole Automation Procedures` permite que el servidor cree objetos COM arbitrarios desde T-SQL. Está **deshabilitada por defecto** en las instancias nuevas (documentación de Microsoft). Habilitarla **amplía la superficie de ataque** del servidor, porque permite crear objetos COM, que se ejecutan fuera del motor de consultas, y se configura a nivel de instancia (afecta a todas las bases). Además, una llamada HTTP desde el motor deja el hilo de la sesión esperando la red. La alternativa recomendada es **hacer la llamada HTTP en la aplicación** (o en un servicio intermedio) y enviar a SQL Server solo el JSON de la respuesta, que se procesa como en la sección anterior.
:::

Estado de la opción, y qué ocurre en una instancia con la configuración por defecto, donde la llamada a `sp_OACreate` es rechazada con el error 15281:

<!-- check: U2.T.API.02 -->
```sql
DECLARE @Objeto INT;
DECLARE @Numero INT = 0;

BEGIN TRY
    EXEC sys.sp_OACreate 'MSXML2.XMLHTTP', @Objeto OUTPUT;
END TRY
BEGIN CATCH
    SET @Numero = ERROR_NUMBER();
END CATCH;

SELECT name AS Opcion, value_in_use AS ValorEnUso, @Numero AS ErrorAlCrearObjeto
FROM sys.configurations
WHERE name = 'Ole Automation Procedures';
```

**Resultado esperado** (instancia con la configuración por defecto).

| Opcion | ValorEnUso | ErrorAlCrearObjeto |
|---|---:|---:|
| Ole Automation Procedures | 0 | 15281 |

Habilitar la opción requiere permiso de administrador y deja `show advanced options` activada. Este bloque no se ejecuta en el entorno de pruebas porque modifica la configuración de la instancia:

<!-- check: U2.T.API.R1 -->
```sql
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
GO

EXEC sp_configure 'Ole Automation Procedures', 1;
RECONFIGURE;
GO

-- Para volver al estado seguro, cuando termine la práctica:
EXEC sp_configure 'Ole Automation Procedures', 0;
RECONFIGURE;
GO
```

### Patrón de una llamada GET

Las llamadas HTTP con Ole Automation usan el objeto COM `MSXML2.XMLHTTP`, siempre con la misma secuencia: crear el objeto, abrir la solicitud, enviarla, leer el estado y el texto de la respuesta, y **destruir el objeto**. Si no se llama a `sp_OADestroy`, el objeto COM queda reservado en memoria hasta que termina la sesión.

| Procedimiento | Rol |
|---|---|
| `sp_OACreate` | Crea una instancia del objeto COM |
| `sp_OAMethod` | Llama a un método (`open`, `send`, `setRequestHeader`) |
| `sp_OAGetProperty` | Lee una propiedad (`status`, `responseText`) |
| `sp_OAGetErrorInfo` | Obtiene el detalle del error de una llamada anterior |
| `sp_OADestroy` | Libera el objeto |

Todos los procedimientos devuelven 0 si salieron bien. El siguiente ejemplo consulta una API ficticia (`api.ejemplo.test` no existe: reemplazala por una API real y revisá sus condiciones de uso), verifica el estado HTTP, procesa el JSON y siempre libera el objeto:

<!-- check: U2.T.API.R2 -->
```sql
DECLARE @Url       NVARCHAR(400) = N'https://api.ejemplo.test/cotizaciones';
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

    SELECT @Estado AS EstadoHttp, JSON_VALUE(@Respuesta, '$.estado') AS Estado;
END TRY
BEGIN CATCH
    DECLARE @Origen VARCHAR(255), @Descripcion VARCHAR(255);
    EXEC sys.sp_OAGetErrorInfo @Objeto, @Origen OUTPUT, @Descripcion OUTPUT;
    SELECT ERROR_MESSAGE() AS Error, @Origen AS Origen, @Descripcion AS Descripcion;
END CATCH;

EXEC sys.sp_OADestroy @Objeto;
```

Una llamada **POST** cambia `'GET'` por `'POST'`, agrega el encabezado `Content-Type: application/json` con `setRequestHeader` y pasa el cuerpo como argumento de `send`:

<!-- check: U2.T.API.R2 -->
```sql
DECLARE @Cuerpo NVARCHAR(MAX) = N'{"productoId": 42, "cantidad": 2}';

EXEC sys.sp_OAMethod @Objeto, 'open', NULL, 'POST', @Url, 'false';
EXEC sys.sp_OAMethod @Objeto, 'setRequestHeader', NULL, 'Content-Type', 'application/json';
EXEC sys.sp_OAMethod @Objeto, 'send', NULL, @Cuerpo;
```

| | GET | POST |
|---|---|---|
| Datos | En la URL (`?parametro=valor`) | En el cuerpo de la solicitud |
| Método en `open` | `'GET'` | `'POST'` |
| Encabezado `Content-Type` | No hace falta | `application/json` |
| `send` | Sin argumentos | Con el cuerpo |

:::caution[Codificación de la URL]
Los parámetros de la URL no pueden llevar espacios ni caracteres como `|`, `&` o `?` sin codificar: se escriben en _porcentaje_ (`%20` para el espacio, `%7C` para `|`). T-SQL no tiene una función para codificar URL; una frase con espacios en la URL puede ser rechazada por el objeto HTTP.
:::

:::note[Estado de la verificación]
Los bloques de llamadas HTTP con Ole Automation están **pendientes de verificación específica**: requieren red externa, habilitar la opción en una instancia de SQL Server para Windows (los objetos COM no existen en la edición para Linux del entorno de pruebas) y servicios que pueden cambiar o dejar de existir. Lo que sí se verificó en el motor es el procesamiento de la respuesta.
:::

## Alternativas

- **Llamar a la API desde la aplicación** (o desde un proceso programado) y guardar la respuesta: es la opción recomendada.
- **`sp_invoke_external_rest_endpoint`**: un procedimiento del sistema que invoca un endpoint REST HTTPS directamente desde T-SQL. Según la documentación de Microsoft está disponible en SQL Server 2025, Azure SQL Database, Azure SQL Managed Instance y la base de datos SQL de Fabric; en SQL Server 2025 está deshabilitado por defecto (`external rest endpoint enabled`) y requiere el permiso `EXECUTE ANY EXTERNAL ENDPOINT`. No existe en SQL Server 2022. En Azure SQL Database solo admite un conjunto de servicios de Azure permitidos. Devuelve el código HTTP y la respuesta en un parámetro de salida.

<!-- check: U2.T.API.R3 -->
```sql
DECLARE @Codigo INT, @Respuesta NVARCHAR(MAX);

EXEC @Codigo = sys.sp_invoke_external_rest_endpoint
    @url      = N'https://<aplicacion>.azurewebsites.net/api/cotizaciones',
    @method   = 'GET',
    @response = @Respuesta OUTPUT;

SELECT @Codigo AS Codigo, JSON_VALUE(@Respuesta, '$.response.status.http.code') AS CodigoHttp;
```

Este bloque queda pendiente de verificación: requiere SQL Server 2025 o Azure SQL y un servicio externo.

## Errores frecuentes

:::caution[Errores frecuentes]
- Dejar `Ole Automation Procedures` habilitada después de la práctica.
- No llamar a `sp_OADestroy` (objeto COM sin liberar) ni a `sp_OAGetErrorInfo` ante un error.
- Procesar el cuerpo sin verificar el código de estado: una respuesta 404 o 500 también es "una respuesta".
- Suponer que la API existe y responde siempre: los servicios gratuitos cambian, limitan solicitudes o desaparecen.
- Poner claves (_tokens_) dentro de scripts que se guardan o comparten.
:::

## Autoevaluación

<details>
<summary>1. ¿Qué verbo HTTP se usa para consultar un recurso y cuál para crearlo?</summary>

`GET` para consultar y `POST` para crear.
</details>

<details>
<summary>2. Una API responde `404`. ¿Es un error del cliente o del servidor?</summary>

Del cliente (familia 4xx): el recurso solicitado no existe. Los errores del servidor son 5xx.
</details>

<details>
<summary>3. ¿Por qué se desaconseja habilitar Ole Automation Procedures en un servidor de producción?</summary>

Porque amplía la superficie de ataque: permite crear objetos COM desde T-SQL a nivel de toda la instancia. Es preferible hacer la llamada en la aplicación y enviar a la base solo el JSON de la respuesta.
</details>

## En resumen

:::tip[En resumen]
- Una API REST expone recursos con URL, se usa con verbos HTTP, responde con un código de estado y un cuerpo (JSON); Postman sirve para explorarla.
- Desde SQL Server la respuesta es un texto JSON que se procesa con `ISJSON`, `JSON_VALUE` y `OPENJSON`.
- Llamar a una API con Ole Automation es posible pero desaconsejado por seguridad; la alternativa recomendada es llamar desde la aplicación.
:::

:::tip[Para seguir]
Practicá con la [Práctica — APIs desde SQL Server](/bbdd-aplicadas/unidad-2/practica/apis/): el ejercicio 1 es del programa y los ejercicios 2 a 5 son complementarios.
:::

## Fuentes

- Presentación de cátedra, Unidad 2, parte 2 (Formatos de intercambio), diapositivas 23 a 26 (API y Postman).
- Microsoft Learn, [Ole Automation Procedures (opción de configuración)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/ole-automation-procedures-server-configuration-option), [sp_invoke_external_rest_endpoint](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql).
- Postman, documentación y Postman Academy.
