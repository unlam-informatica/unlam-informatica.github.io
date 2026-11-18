---
title: Importación de archivos
slug: bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos
sidebar:
  order: 9
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

Cómo cargar en tablas de SQL Server los datos de archivos CSV, de ancho fijo, JSON y XML. Los formatos se describen en [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/) y el procesamiento de JSON y XML en [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/) y [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/).

## Para qué sirve

Casi todo dato que llega a una base viene de un archivo: un conjunto de datos abiertos en CSV, un listado bancario de ancho fijo, la respuesta guardada de una API en JSON. Importarlo bien significa cargar rápido y, sobre todo, **no perder ni corromper datos**: comillas, codificación y filas inválidas son los problemas de todos los días.

:::note[Rutas en los ejemplos]
Los ejemplos muestran rutas de Windows como `C:\datos\producto.csv`; reemplazalas por la ruta de tu archivo. La ruta la resuelve **el servidor**, no tu equipo cliente, y la cuenta con la que corre el servicio de SQL Server debe poder leerla. Los ejemplos se verificaron en SQL Server 2022 sobre Linux con archivos de fin de línea LF; ver las notas sobre diferencias.
:::

## Herramientas

| Herramienta | Cuándo se usa |
|---|---|
| `BULK INSERT` | Cargar un archivo de texto (CSV, ancho fijo) directamente en una tabla o vista |
| `OPENROWSET(BULK ...)` | Leer un archivo como un conjunto de filas dentro de una consulta (`SELECT`), con un archivo de formato, o como un único valor (`SINGLE_CLOB`, `SINGLE_NCLOB`, `SINGLE_BLOB`) para JSON y XML |
| `bcp` | Utilidad de línea de comandos para importar y exportar |

**Permisos.** `BULK INSERT` requiere `INSERT` sobre la tabla y el permiso `ADMINISTER BULK OPERATIONS` (rol `bulkadmin`). `OPENROWSET(BULK ...)` requiere el mismo permiso a nivel de servidor.

## BULK INSERT con CSV

<!-- sintaxis -->
```sql
BULK INSERT [esquema.]tabla_o_vista
FROM 'ruta_del_archivo'
WITH (
    FORMAT = 'CSV', FIELDQUOTE = '"', FIRSTROW = 2, ...
);
```

Opciones principales (consultá la [referencia de Microsoft](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql) para el resto):

| Opción | Descripción |
|---|---|
| `FORMAT = 'CSV'` | Interpreta el archivo según RFC 4180: campos entrecomillados, comillas duplicadas, campos vacíos (SQL Server 2017 en adelante) |
| `FIELDQUOTE` | Carácter de comillas; por defecto `"` |
| `FIELDTERMINATOR` | Separador de columnas (por defecto tabulador); con `FORMAT = 'CSV'` es la coma |
| `ROWTERMINATOR` | Separador de filas; el valor por defecto es `\r\n`. Para un archivo LF se usa `'0x0a'` |
| `FIRSTROW` | Primera fila a cargar; `2` salta el encabezado |
| `MAXERRORS` | Cantidad de filas con error toleradas antes de cancelar (por defecto 10) |
| `ERRORFILE` | Archivo donde se copian las filas rechazadas por errores de formato |
| `CHECK_CONSTRAINTS` | Valida `CHECK` y claves foráneas durante la carga (si no, quedan sin validar y no confiables) |
| `BATCHSIZE` | Cantidad de filas por transacción (por defecto, todo el archivo es un lote) |
| `CODEPAGE` | Página de códigos de los datos de tipo `char`; ver "Codificación" |
| `DATAFILETYPE` | `'char'` (por defecto) o `'widechar'` (UTF-16) |

### Ejemplo simple

Archivo `producto.csv` (con fin de línea LF):

```text
codigo,nombre,precio,stock
P001,Cuaderno rayado,1250.50,40
P002,Lapicera azul,300.00,120
P003,Resaltador amarillo,480.25,0
```

<!-- check: U2.T.IMP.01 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NOT NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (Codigo)
);
GO

BULK INSERT ventas.Producto
FROM 'C:\datos\producto.csv'
WITH (
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR   = '0x0a'
);

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Cuaderno rayado | 1250.50 | 40 |
| P002 | Lapicera azul | 300.00 | 120 |
| P003 | Resaltador amarillo | 480.25 | 0 |

:::caution[Fin de línea: CRLF y LF]
`ROWTERMINATOR = '\n'` en `BULK INSERT` se interpreta como el par CRLF en Windows, según la documentación de Microsoft. Un archivo creado en Linux o macOS termina en LF solo: en Windows usá `'0x0a'`. Un archivo de Windows (CRLF) se lee con `'\n'` o con `'0x0d0a'`. Si el terminador no coincide, la última columna se carga con el carácter de control o la fila no se separa.
:::

### Campos entrecomillados: FORMAT = 'CSV'

Cuando un campo contiene la coma, el CSV lo entrecomilla. `FIELDTERMINATOR = ','` no entiende las comillas; `FORMAT = 'CSV'` sí. El archivo `producto_comillas.csv`:

```text
codigo,nombre,precio,stock
P001,"Cuaderno, rayado",1250.50,40
P002,"Lapicera ""Trazo"" azul",300.00,120
P003,Resaltador amarillo,480.25,
```

<!-- check: U2.T.IMP.02 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (Codigo)
);
GO

BULK INSERT ventas.Producto
FROM 'C:\datos\producto_comillas.csv'
WITH (
    FORMAT     = 'CSV',
    FIELDQUOTE = '"',
    FIRSTROW   = 2
);

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---|
| P001 | Cuaderno, rayado | 1250.50 | 40 |
| P002 | Lapicera "Trazo" azul | 300.00 | 120 |
| P003 | Resaltador amarillo | 480.25 | NULL |

La coma interna se conserva, las comillas dobles duplicadas pasan a una comilla y el campo vacío del final es `NULL`.

Con el mismo archivo y solo `FIELDTERMINATOR = ','` (sin `FORMAT = 'CSV'`), la primera fila no se puede convertir (su tercera "columna" es `rayado"`) y se descarta con el error 4864 de conversión, y la segunda se carga con las comillas literales:

<!-- check: U2.T.IMP.03 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NULL
);
GO

DECLARE @Error INT = 0;

BEGIN TRY
    BULK INSERT ventas.Producto
    FROM 'C:\datos\producto_comillas.csv'
    WITH (
        FIRSTROW        = 2,
        FIELDTERMINATOR = ',',
        ROWTERMINATOR   = '0x0a'
    );
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---|
| P002 | `"Lapicera ""Trazo"" azul"` | 300.00 | 120 |
| P003 | Resaltador amarillo | 480.25 | NULL |

Así se pierde una fila y se ensucia otra sin que el script se detenga en el entorno de prueba (en SSMS aparece el mensaje de error 4864 para la fila descartada). Por eso conviene verificar siempre la cantidad de filas cargadas.

## Staging, validación y carga final

Cargar directo a la tabla final tiene un problema: si una sola fila viola un tipo, una restricción o una clave, `BULK INSERT` la descarta o aborta, y el motivo no queda registrado. El patrón recomendado es:

1. Cargar el archivo **tal cual** en una tabla de **staging**, con todas las columnas como texto y sin restricciones.
2. **Validar** con `TRY_CONVERT` y consultas: tipos, rangos, duplicados, claves foráneas.
3. Insertar en la tabla final solo las filas válidas, y guardar las rechazadas con su motivo.

`BULK INSERT` puede cargar en una **vista**; así la tabla de staging puede tener una columna de identidad con el orden de llegada, que el archivo no trae. En el archivo de ejemplo hay un precio no numérico (`abc`), un stock negativo y un código repetido:

```text
codigo,nombre,precio,stock
P001,Cuaderno rayado,1250.50,40
P002,Lapicera azul,abc,120
P003,Resaltador amarillo,480.25,-5
P001,Cuaderno duplicado,999.00,1
P004,Goma de borrar,150.00,60
```

<!-- check: U2.T.IMP.04 -->
```sql
CREATE SCHEMA staging;
GO
CREATE SCHEMA ventas;
GO

-- Staging: todo como texto, más una columna con el orden de llegada
CREATE TABLE staging.Producto (
    FilaId INT IDENTITY(1, 1) NOT NULL,
    Codigo VARCHAR(20)  NULL,
    Nombre VARCHAR(100) NULL,
    Precio VARCHAR(30)  NULL,
    Stock  VARCHAR(30)  NULL,
    CONSTRAINT PK_StagingProducto PRIMARY KEY CLUSTERED (FilaId)
);
GO

-- Vista sin la columna de identidad: es el destino de BULK INSERT
CREATE VIEW staging.ProductoCarga
AS
SELECT Codigo, Nombre, Precio, Stock FROM staging.Producto;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NOT NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (Codigo),
    CONSTRAINT CK_Producto_Precio CHECK (Precio > 0),
    CONSTRAINT CK_Producto_Stock CHECK (Stock >= 0)
);
GO

BULK INSERT staging.ProductoCarga
FROM 'C:\datos\producto_sucio.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2);
GO

-- Validación: una fila es válida si convierte bien, cumple las reglas y es la primera de su código
WITH Validada AS (
    SELECT FilaId, Codigo, Nombre,
           TRY_CONVERT(DECIMAL(10,2), Precio) AS PrecioNum,
           TRY_CONVERT(INT, Stock)            AS StockNum,
           ROW_NUMBER() OVER (PARTITION BY Codigo ORDER BY FilaId) AS Orden
    FROM staging.Producto
)
INSERT INTO ventas.Producto (Codigo, Nombre, Precio, Stock)
SELECT Codigo, Nombre, PrecioNum, StockNum
FROM Validada
WHERE PrecioNum > 0
  AND StockNum >= 0
  AND Orden = 1;

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Cuaderno rayado | 1250.50 | 40 |
| P004 | Goma de borrar | 150.00 | 60 |

`TRY_CONVERT` devuelve `NULL` si la conversión falla (en vez de un error) y `NULL > 0` no es verdadero, así que las filas con precio no numérico quedan fuera. En una carga real se agrega una tabla de rechazos con el motivo, como en el ejercicio 5 de la [práctica](/bbdd-aplicadas/unidad-2/practica/importacion-archivos/).

### ERRORFILE y MAXERRORS

Si se carga directo con tipos estrictos, `ERRORFILE` guarda las filas que no se pudieron convertir y `MAXERRORS` fija cuántas se toleran. El archivo de errores **no debe existir** antes de la carga (si existe, el comando falla); además se crea un archivo de control con extensión `.Error.Txt` con el diagnóstico de cada fila.

<!-- check: U2.T.IMP.05 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NOT NULL
);
GO

DECLARE @Error INT = 0;

BEGIN TRY
    BULK INSERT ventas.Producto
    FROM 'C:\datos\producto_errores.csv'
    WITH (
        FIRSTROW        = 2,
        FIELDTERMINATOR = ',',
        ROWTERMINATOR   = '0x0a',
        MAXERRORS       = 10,
        ERRORFILE       = 'C:\datos\rechazadas.csv'
    );
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;

SELECT d.BulkColumn AS FilasRechazadas
FROM OPENROWSET(BULK 'C:\datos\rechazadas.csv', SINGLE_CLOB) AS d;
```

**Resultado esperado.** Primero las filas cargadas:

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Cuaderno rayado | 1250.50 | 40 |
| P003 | Resaltador amarillo | 480.25 | 0 |

y después el contenido del archivo de rechazos (dos filas copiadas tal cual):

```text
P002,Lapicera azul,xx,120
P004,Goma de borrar,yy,60
```

## Codificación

Un archivo de texto es una secuencia de bytes; para saber qué letra es cada uno hay que conocer la **codificación**. Los portales de datos abiertos suelen publicar en **UTF-8** y Windows guarda muchos archivos en **UTF-16** ("Unicode"). Si la codificación declarada al cargar no es la real, las letras con tilde y la `ñ` se corrompen (por ejemplo `Ã±` en lugar de `ñ`).

| Codificación del archivo | Cómo cargarlo |
|---|---|
| ASCII (sin tildes ni `ñ`) | No hay problema con ninguna opción |
| UTF-8, en Windows | `CODEPAGE = '65001'` en `BULK INSERT` |
| UTF-16 (little endian) | `DATAFILETYPE = 'widechar'` con columnas `NVARCHAR` (verificado) |
| UTF-8, en cualquier plataforma | Leer los bytes con `SINGLE_BLOB` y guardarlos en una columna `VARCHAR` con _collation_ UTF-8 (SQL Server 2019 o posterior) (verificado para JSON, abajo) |

<!-- check: U2.T.IMP.R1 -->
```sql
BULK INSERT ventas.Producto
FROM 'C:\datos\producto_acentos.csv'
WITH (
    FORMAT   = 'CSV',
    FIRSTROW = 2,
    CODEPAGE = '65001'    -- UTF-8
);
```

:::note[CODEPAGE en SQL Server sobre Linux]
`CODEPAGE = '65001'` es la forma habitual en Windows, pero no se pudo comprobar en el entorno de pruebas de esta materia: SQL Server 2022 sobre Linux rechaza la opción con el error 16202 (`Keyword or statement option 'CODEPAGE' is not supported on the 'Linux' platform`), y la documentación de Microsoft indica que no es una opción soportada en Linux. Este bloque queda registrado como pendiente de verificación específica en Windows.
:::

Un CSV en UTF-16 se carga con `DATAFILETYPE = 'widechar'` en columnas `NVARCHAR`. El archivo `acentos16.csv` tiene este contenido, guardado como UTF-16 con marca de orden de bytes:

```text
codigo,nombre,categoria
P010,Lápiz de grafito,Librería
P011,"Pegamento, en barra",Papelería
P012,Cartulina ñandú,Librería
```

<!-- check: U2.T.IMP.10 -->
```sql
CREATE SCHEMA staging;
GO

CREATE TABLE staging.Producto (
    Codigo    CHAR(4)      NOT NULL,
    Nombre    NVARCHAR(40) NOT NULL,
    Categoria NVARCHAR(40) NOT NULL
);
GO

BULK INSERT staging.Producto
FROM 'C:\datos\acentos16.csv'
WITH (
    FORMAT       = 'CSV',
    FIRSTROW     = 2,
    DATAFILETYPE = 'widechar'
);

SELECT Codigo, Nombre, Categoria
FROM staging.Producto
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Categoria |
|---|---|---|
| P010 | Lápiz de grafito | Librería |
| P011 | Pegamento, en barra | Papelería |
| P012 | Cartulina ñandú | Librería |

## Importar un archivo de ancho fijo

Se carga con un archivo de formato, como en [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/#ancho-fijo), o se lee como un conjunto de filas con `OPENROWSET(BULK ..., FORMATFILE = ...)`. Con este último método el archivo de formato declara todo como texto, así que hay que convertir:

<!-- check: U2.T.IMP.11 -->
```sql
SELECT d.Codigo,
       RTRIM(d.Nombre)                   AS Nombre,
       CAST(d.Precio AS DECIMAL(10,2))   AS Precio,
       CAST(d.Stock AS INT)              AS Stock
FROM OPENROWSET(
    BULK 'C:\datos\producto_fijo.txt',
    FORMATFILE = 'C:\datos\producto_fijo.fmt'
) AS d
ORDER BY d.Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Cuaderno rayado | 1250.50 | 40 |
| P002 | Lapicera azul | 300.00 | 120 |
| P003 | Resaltador amarillo | 480.25 | 0 |

## Importar JSON con OPENROWSET

Un archivo JSON se lee entero con `OPENROWSET(BULK ..., SINGLE_CLOB)`, que lo entrega como **un único valor de texto** en la columna `BulkColumn`; después `OPENJSON` lo convierte en filas. `SINGLE_CLOB` lee el archivo como `varchar` con la página de códigos de la base, por eso solo es seguro con archivos sin tildes. El archivo `producto.json`:

```json
[
  {"codigo": "P001", "nombre": "Cuaderno rayado",    "precio": 1250.50, "stock": 40},
  {"codigo": "P002", "nombre": "Lapicera azul",      "precio": 300.00,  "stock": 120},
  {"codigo": "P003", "nombre": "Resaltador amarillo", "precio": 480.25,  "stock": null}
]
```

<!-- check: U2.T.IMP.06 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(40)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NULL,
    CONSTRAINT PK_Producto PRIMARY KEY CLUSTERED (Codigo)
);
GO

INSERT INTO ventas.Producto (Codigo, Nombre, Precio, Stock)
SELECT p.Codigo, p.Nombre, p.Precio, p.Stock
FROM OPENROWSET(BULK 'C:\datos\producto.json', SINGLE_CLOB) AS archivo
CROSS APPLY OPENJSON(archivo.BulkColumn)
WITH (
    Codigo CHAR(4)       '$.codigo',
    Nombre VARCHAR(40)   '$.nombre',
    Precio DECIMAL(10,2) '$.precio',
    Stock  INT           '$.stock'
) AS p;

SELECT Codigo, Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---|
| P001 | Cuaderno rayado | 1250.50 | 40 |
| P002 | Lapicera azul | 300.00 | 120 |
| P003 | Resaltador amarillo | 480.25 | NULL |

### JSON con tildes: UTF-8 y UTF-16

Con `producto_acentos.json` guardado en UTF-8, `SINGLE_CLOB` lo leería con la página de códigos equivocada y `Lápiz` quedaría como `LÃ¡piz`. Hay dos soluciones verificadas.

**UTF-8:** leer los bytes con `SINGLE_BLOB` y guardarlos en una columna `VARCHAR(MAX)` con _collation_ UTF-8, que interpreta los bytes como UTF-8. Después se pasa a `NVARCHAR` al leerlo con `OPENJSON`.

<!-- check: U2.T.IMP.07 -->
```sql
CREATE SCHEMA staging;
GO

-- La columna VARCHAR con collation UTF8 interpreta los bytes del archivo como UTF-8
CREATE TABLE staging.Documento (
    Contenido VARCHAR(MAX) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NOT NULL
);
GO

INSERT INTO staging.Documento (Contenido)
SELECT archivo.BulkColumn
FROM OPENROWSET(BULK 'C:\datos\producto_acentos.json', SINGLE_BLOB) AS archivo;

SELECT p.Codigo, p.Nombre, p.Categoria, LEN(p.Nombre) AS Largo
FROM staging.Documento AS d
CROSS APPLY OPENJSON(d.Contenido)
WITH (
    Codigo    CHAR(4)       '$.codigo',
    Nombre    NVARCHAR(40)  '$.nombre',
    Categoria NVARCHAR(40)  '$.categoria'
) AS p
ORDER BY p.Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Categoria | Largo |
|---|---|---|---:|
| P010 | Lápiz de grafito | Librería | 16 |
| P011 | Pegamento en barra | Papelería | 18 |
| P012 | Cartulina ñandú | Librería | 15 |

**UTF-16:** si el archivo está guardado como Unicode (UTF-16), `SINGLE_NCLOB` lo lee directamente como `NVARCHAR(MAX)`. Con un archivo que no sea UTF-16, `SINGLE_NCLOB` falla con el error 4809 (`SINGLE_NCLOB requires a UNICODE (widechar) input file`).

<!-- check: U2.T.IMP.08 -->
```sql
SELECT p.Codigo, p.Nombre, p.Categoria, LEN(p.Nombre) AS Largo
FROM OPENROWSET(BULK 'C:\datos\producto_acentos16.json', SINGLE_NCLOB) AS archivo
CROSS APPLY OPENJSON(archivo.BulkColumn)
WITH (
    Codigo    CHAR(4)       '$.codigo',
    Nombre    NVARCHAR(40)  '$.nombre',
    Categoria NVARCHAR(40)  '$.categoria'
) AS p
ORDER BY p.Codigo;
```

**Resultado esperado.** El mismo de la tabla anterior.

:::caution[Marca de orden de bytes (BOM)]
Si un archivo UTF-8 empieza con la marca `EF BB BF`, el texto que se obtiene tiene un carácter inicial inesperado y `OPENJSON` rechaza el documento (error 13609, `Unexpected character 'ï' is found at position 0`). Guardá el archivo UTF-8 sin BOM o quitalo antes de procesar.
:::

## Importar XML con OPENROWSET

Para XML se usa `SINGLE_BLOB`: lee los bytes sin convertirlos y, al convertir a `xml`, el motor respeta la codificación que declara el propio documento (`encoding="utf-8"`). Después se aplican `.nodes()` y `.value()`. El archivo `producto.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Productos>
  <Producto codigo="P001">
    <Nombre>Cuaderno rayado</Nombre>
    <Precio>1250.50</Precio>
    <Stock>40</Stock>
  </Producto>
  <Producto codigo="P002">
    <Nombre>Lápiz de grafito</Nombre>
    <Precio>300.00</Precio>
    <Stock>120</Stock>
  </Producto>
  <Producto codigo="P003">
    <Nombre>Resaltador amarillo</Nombre>
    <Precio>480.25</Precio>
  </Producto>
</Productos>
```

<!-- check: U2.T.IMP.09 -->
```sql
DECLARE @Documento XML = (
    SELECT CAST(archivo.BulkColumn AS XML)
    FROM OPENROWSET(BULK 'C:\datos\producto.xml', SINGLE_BLOB) AS archivo
);

SELECT n.value('@codigo', 'CHAR(4)')                 AS Codigo,
       n.value('(Nombre)[1]', 'NVARCHAR(40)')        AS Nombre,
       n.value('(Precio)[1]', 'DECIMAL(10,2)')       AS Precio,
       n.value('(Stock)[1]', 'INT')                  AS Stock
FROM @Documento.nodes('/Productos/Producto') AS t(n)
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---|
| P001 | Cuaderno rayado | 1250.50 | 40 |
| P002 | Lápiz de grafito | 300.00 | 120 |
| P003 | Resaltador amarillo | 480.25 | NULL |

Un elemento ausente (`Stock` del producto P003) da `NULL`. La instrucción `OPENROWSET(BULK ...)` funciona en el entorno de pruebas sin configuración adicional; no se necesitó habilitar ninguna opción del servidor, solo el permiso de operaciones masivas.

## YAML

SQL Server no lee YAML. Se convierte el archivo a JSON con una herramienta externa y después se aplica lo visto para JSON.

## Errores frecuentes

:::caution[Errores frecuentes]
- **Cargar un CSV con comas internas sin `FORMAT = 'CSV'`**: se pierden o se ensucian filas (ver el ejemplo `U2.T.IMP.03`).
- **Terminador de fila incorrecto**: la última columna llega con un carácter de control o la carga falla.
- **Codificación equivocada**: tildes corruptas. Comprobá con una consulta por una palabra con tilde.
- **Cargar sin verificar**: comparar siempre la cantidad de filas del archivo con la de la tabla.
- **Tabla de destino con tipos estrictos y datos sucios**: usá staging.
- **`ERRORFILE` ya existente**: el comando falla; usá un nombre nuevo en cada carga.
- **Ruta del cliente en vez del servidor**: el archivo debe ser visible desde el servidor.
:::

## Autoevaluación

<details>
<summary>1. ¿Por qué conviene cargar a una tabla de staging antes de la tabla final?</summary>

Porque permite cargar todo sin que los tipos ni las restricciones rechacen filas, validar con `TRY_CONVERT` y consultas, y registrar por qué se descartó cada fila.
</details>

<details>
<summary>2. ¿Qué opción hace que `BULK INSERT` entienda un campo `"Gómez, Ana"`?</summary>

`FORMAT = 'CSV'` (con `FIELDQUOTE` si las comillas son otro carácter).
</details>

<details>
<summary>3. Un JSON en UTF-8 con tildes se lee con `SINGLE_CLOB` y aparecen caracteres raros. ¿Cómo se corrige?</summary>

Leyendo los bytes con `SINGLE_BLOB` hacia una columna `VARCHAR(MAX)` con _collation_ UTF-8 (o guardando el archivo como UTF-16 y usando `SINGLE_NCLOB`).
</details>

## En resumen

:::tip[En resumen]
- `BULK INSERT` carga CSV y ancho fijo; `FORMAT = 'CSV'` maneja comillas, `ERRORFILE` y `MAXERRORS` el manejo de errores.
- `OPENROWSET(BULK ...)` lee archivos JSON y XML como un único valor para procesarlos con `OPENJSON` y `.nodes()`.
- Cargá con staging, validá con `TRY_CONVERT` y conservá las filas rechazadas con su motivo.
- La codificación del archivo (UTF-8, UTF-16) importa tanto como el formato.
:::

:::tip[Para seguir]
Practicá con la [Práctica — Importación de archivos](/bbdd-aplicadas/unidad-2/practica/importacion-archivos/) y después integrá todo en el [Trabajo práctico 2](/bbdd-aplicadas/unidad-2/practica/tp2/).
:::

## Fuentes

- Guía de trabajo práctico de cátedra, TP 2 (objetivos de importación de archivos CSV), y presentación de cátedra, Unidad 2, parte 2, diapositivas 8 a 11.
- Microsoft Learn, [BULK INSERT](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql), [OPENROWSET (BULK)](https://learn.microsoft.com/en-us/sql/t-sql/functions/openrowset-bulk-transact-sql), [Archivos de formato no XML](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/non-xml-format-files-sql-server).
