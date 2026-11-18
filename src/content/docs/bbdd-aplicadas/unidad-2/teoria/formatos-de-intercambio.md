---
title: Formatos de intercambio
slug: bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio
sidebar:
  order: 6
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

Esta es la única página de la unidad que describe los **formatos** de intercambio de datos: EDI, CSV, ancho fijo, XML, JSON y YAML. Cómo leer y generar XML y JSON desde T-SQL está en [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/) y [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/); cómo cargar archivos en una tabla, en [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/).

## Para qué sirve

Dos sistemas que no comparten base de datos necesitan acordar cómo se escribe un dato en un archivo o en un mensaje. Un **formato de intercambio** es ese acuerdo: un estándar de texto con reglas de sintaxis. Al adherir a un estándar no hace falta conocer de antemano quién va a usar los datos, y casi siempre existen bibliotecas que los generan o los interpretan.

:::note[Definición]
Un **formato de intercambio** es una convención de texto con estructura y sintaxis propias para almacenar y compartir información entre sistemas. En la materia se estudian EDI, CSV (y TSV), ancho fijo, XML, JSON y YAML.
:::

Un mismo dato puede viajar en cualquiera de ellos. Los datos de ejemplo de esta página son siempre los mismos, tres productos de una librería ficticia:

| Código | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Cuaderno rayado | 1250,50 | 40 |
| P002 | Lapicera azul | 300,00 | 120 |
| P003 | Resaltador amarillo | 480,25 | 0 |

## EDI (Electronic Data Interchange)

EDI es un formato de texto pensado para el intercambio entre computadoras (_computer-to-computer_) de documentos comerciales como facturas u órdenes de compra. No existe un único EDI: hay varios estándares, cada uno con múltiples versiones, por ejemplo ANSI X12, EANCOM, HIPAA, ODETTE y SWIFT. En cada intercambio se informa a qué estándar y versión se adhiere, y el estándar detalla cómo interpretar números, fechas y códigos.

Una factura ANSI X12 simplificada, con datos ficticios, se ve así:

```text
ST*810*0001~
BIG*20260310*FAC0001*20260301*OC0001*1001~
N1*ST*EMPRESA EJEMPLO SA*9*123456789~
N3*CALLE FICTICIA 100~
N4*ROSARIO*SF*S2000~
TDS*14400~
SE*6*0001~
```

| Segmento | Significado |
|---|---|
| `ST*810*0001~` | Inicio de la transacción tipo 810 (factura), con número de control 0001 |
| `BIG*...` | Datos generales: fecha de la factura, número de factura, fecha y número de la orden de compra |
| `N1*ST*...` | Identificación del destinatario (_ship to_) |
| `N3*...` / `N4*...` | Dirección; ciudad, provincia y código postal |
| `TDS*14400~` | Total del documento. Por la convención del segmento `TDS`, el importe se escribe sin separador decimal y con dos decimales implícitos: 14400 equivale a 144,00 |
| `SE*6*0001~` | Fin de la transacción: cantidad de segmentos y número de control |

SQL Server no lee EDI directamente. En la práctica se usa un traductor que convierte el EDI a otro formato (por ejemplo XML) antes de cargarlo.

## CSV y TSV

**CSV** (_Comma-Separated Values_) es un formato de texto tabular: cada línea es un registro y las columnas se separan con un delimitador, en general la coma o el punto y coma. **TSV** es lo mismo con el carácter tabulador como delimitador.

Reglas habituales (RFC 4180 describe la variante más difundida):

- La primera línea puede tener los nombres de las columnas.
- Todos los registros tienen la misma cantidad de campos.
- Un campo vacío se escribe con dos delimitadores contiguos: `P003,Resaltador amarillo,480.25,`.
- Si el delimitador forma parte del dato, el campo se entrecomilla con comillas dobles: `"Cuaderno, rayado"`. Dentro de un campo entrecomillado, una comilla se duplica: `"Lapicera ""Trazo"" azul"`.
- En países que usan la coma como separador decimal se usa `;` como delimitador.

```text
codigo,nombre,precio,stock
P001,"Cuaderno, rayado",1250.50,40
P002,"Lapicera ""Trazo"" azul",300.00,120
P003,Resaltador amarillo,480.25,
```

Para cargar un CSV en una tabla (`BULK INSERT` con `FORMAT = 'CSV'`) mirá [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/).

## Ancho fijo

En el formato de **ancho fijo** no hay delimitadores: cada campo ocupa siempre la misma cantidad de caracteres y cada registro tiene la misma longitud total. Hay que definir el carácter de relleno, típicamente espacios para el texto y ceros a la izquierda para los números. Es habitual en sistemas heredados, archivos bancarios y organismos públicos.

Especificación del ejemplo: código (4), nombre (22), precio (10) y stock (4), 40 caracteres por línea.

```text
P001Cuaderno rayado       0001250.500040
P002Lapicera azul         0000300.000120
P003Resaltador amarillo   0000480.250000
```

Hay dos formas de leerlo en SQL Server. La primera es cargar cada línea completa en una sola columna y cortarla con `SUBSTRING`. El archivo del ejemplo tiene fin de línea LF, por eso se usa `ROWTERMINATOR = '0x0a'`. En una ruta de Windows se reemplaza el ejemplo `C:\datos\producto_fijo.txt` por la ruta propia.

<!-- check: U2.T.FMT.02 -->
```sql
CREATE SCHEMA staging;
GO

-- Cada línea del archivo mide 40 caracteres
CREATE TABLE staging.LineaProducto (
    Linea CHAR(40) NOT NULL
);
GO

BULK INSERT staging.LineaProducto
FROM 'C:\datos\producto_fijo.txt'
WITH (ROWTERMINATOR = '0x0a');

SELECT SUBSTRING(Linea, 1, 4)                              AS Codigo,
       RTRIM(SUBSTRING(Linea, 5, 22))                      AS Nombre,
       CAST(SUBSTRING(Linea, 27, 10) AS DECIMAL(10,2))     AS Precio,
       CAST(SUBSTRING(Linea, 37, 4)  AS INT)               AS Stock
FROM staging.LineaProducto
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Cuaderno rayado | 1250.50 | 40 |
| P002 | Lapicera azul | 300.00 | 120 |
| P003 | Resaltador amarillo | 480.25 | 0 |

La segunda forma es un **archivo de formato** (`.fmt`) que describe cada campo, su longitud y sus terminadores. Con él, `BULK INSERT` carga cada campo en su columna.

```text
14.0
4
1  SQLCHAR  0  4   ""    1  Codigo  ""
2  SQLCHAR  0  22  ""    2  Nombre  ""
3  SQLCHAR  0  10  ""    3  Precio  ""
4  SQLCHAR  0  4   "\n"  4  Stock   ""
```

La primera línea es la versión del formato (14.0 corresponde a SQL Server 2017; las versiones posteriores lo leen), la segunda la cantidad de campos. Cada línea siguiente indica, en orden: número de campo en el archivo, tipo de dato en el archivo, prefijo (0 = sin prefijo), longitud, terminador, número de columna de la tabla, nombre de la columna y _collation_. Los campos de ancho fijo llevan terminador vacío (`""`); el último lleva el fin de línea.

<!-- check: U2.T.FMT.03 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Producto (
    Codigo CHAR(4)       NOT NULL,
    Nombre VARCHAR(22)   NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock  INT           NOT NULL
);
GO

BULK INSERT ventas.Producto
FROM 'C:\datos\producto_fijo.txt'
WITH (FORMATFILE = 'C:\datos\producto_fijo.fmt');

SELECT Codigo, RTRIM(Nombre) AS Nombre, Precio, Stock
FROM ventas.Producto
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Cuaderno rayado | 1250.50 | 40 |
| P002 | Lapicera azul | 300.00 | 120 |
| P003 | Resaltador amarillo | 480.25 | 0 |

:::caution[Fin de línea en el archivo de formato]
El terminador `"\n"` del archivo de formato y el `ROWTERMINATOR = '0x0a'` suponen líneas terminadas en LF. Los archivos generados en Windows suelen terminar en CRLF: en ese caso el terminador es `"\r\n"` (o `0x0d0a`). Si no coincide, la última columna incluye el retorno de carro y la conversión falla.
:::

## XML (Extensible Markup Language)

XML es un lenguaje de marcado, similar a HTML pero sin etiquetas predefinidas. Es **autodescriptivo**: cada dato se delimita con etiquetas (`<etiqueta>dato</etiqueta>`), la estructura es un árbol de elementos anidados y los elementos pueden tener atributos. Se puede validar contra un esquema (DTD o XSD) y es muy usado en formatos de archivo y en servicios SOAP. Es verboso, pero expresivo.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<productos>
  <producto codigo="P001">
    <nombre>Cuaderno rayado</nombre>
    <precio>1250.50</precio>
    <stock>40</stock>
  </producto>
  <producto codigo="P002">
    <nombre>Lapicera azul</nombre>
    <precio>300.00</precio>
    <stock>120</stock>
  </producto>
</productos>
```

Los caracteres `<`, `>`, `&`, `'` y `"` no pueden aparecer tal cual en el contenido o en un valor de atributo: se escriben como `&lt;`, `&gt;`, `&amp;`, `&apos;` y `&quot;`. Un documento con estructura mal cerrada o con un carácter sin escapar está **mal formado** y el motor lo rechaza.

SQL Server tiene un tipo de dato `xml` y métodos para consultarlo y generarlo; todo eso está en [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/).

## JSON (JavaScript Object Notation)

JSON es un formato de texto liviano basado en pares clave-valor, muy usado por las API web. Sus construcciones son:

| Construcción | Sintaxis | Ejemplo |
|---|---|---|
| Objeto | `{ "clave": valor, ... }` | `{"codigo": "P001", "stock": 40}` |
| Arreglo | `[ valor, valor, ... ]` | `[1, 2, 3]` o `[{...}, {...}]` |
| Cadena | entre comillas dobles | `"Cuaderno rayado"` |
| Número | sin comillas | `42`, `1250.50` |
| Booleano | sin comillas | `true`, `false` |
| Nulo | sin comillas | `null` |

```json
[
  { "codigo": "P001", "nombre": "Cuaderno rayado", "precio": 1250.50, "stock": 40 },
  { "codigo": "P002", "nombre": "Lapicera azul",   "precio": 300.00,  "stock": 120 }
]
```

Las claves y las cadenas van siempre entre comillas dobles; no se admiten comentarios ni comas finales. SQL Server no tiene un tipo `json` propio en SQL Server 2022: guarda JSON en columnas de texto (`NVARCHAR`) y lo procesa con funciones. Mirá [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/).

## El mismo dato en XML y en JSON

Para ver que el formato cambia pero el dato no, el siguiente ejemplo lee dos productos escritos en JSON y los mismos dos escritos en XML, y los devuelve con las mismas columnas. Los métodos usados se explican en las dos páginas de T-SQL.

<!-- check: U2.T.FMT.01 -->
```sql
DECLARE @Json NVARCHAR(MAX) = N'[
  {"codigo": "P001", "nombre": "Cuaderno rayado", "precio": 1250.50, "stock": 40},
  {"codigo": "P002", "nombre": "Lapicera azul",   "precio": 300.00,  "stock": 120}
]';

DECLARE @Xml XML = N'
<productos>
  <producto codigo="P001">
    <nombre>Cuaderno rayado</nombre>
    <precio>1250.50</precio>
    <stock>40</stock>
  </producto>
  <producto codigo="P002">
    <nombre>Lapicera azul</nombre>
    <precio>300.00</precio>
    <stock>120</stock>
  </producto>
</productos>';

SELECT 'JSON' AS Origen, Codigo, Nombre, Precio, Stock
FROM OPENJSON(@Json)
WITH (
    Codigo CHAR(4)       '$.codigo',
    Nombre VARCHAR(40)   '$.nombre',
    Precio DECIMAL(10,2) '$.precio',
    Stock  INT           '$.stock'
)
UNION ALL
SELECT 'XML',
       n.value('@codigo', 'CHAR(4)'),
       n.value('(nombre)[1]', 'VARCHAR(40)'),
       n.value('(precio)[1]', 'DECIMAL(10,2)'),
       n.value('(stock)[1]', 'INT')
FROM @Xml.nodes('/productos/producto') AS t(n)
ORDER BY Codigo, Origen;
```

**Resultado esperado.**

| Origen | Codigo | Nombre | Precio | Stock |
|---|---|---|---:|---:|
| JSON | P001 | Cuaderno rayado | 1250.50 | 40 |
| XML | P001 | Cuaderno rayado | 1250.50 | 40 |
| JSON | P002 | Lapicera azul | 300.00 | 120 |
| XML | P002 | Lapicera azul | 300.00 | 120 |

## YAML (YAML Ain't Markup Language)

YAML es un formato de serialización pensado para que lo lean y escriban personas. Se lo considera, en la práctica, un superconjunto de JSON. Sus reglas básicas:

- La jerarquía se marca con sangría de **espacios** (nunca tabuladores).
- Los pares clave-valor se escriben `clave: valor`, sin comillas salvo que el valor tenga caracteres especiales.
- Los elementos de una lista empiezan con `- `.
- Un documento puede comenzar con `---`.
- Los comentarios empiezan con `#`.

```yaml
# Los mismos productos, en YAML
productos:
  - codigo: P001
    nombre: Cuaderno rayado
    precio: 1250.50
    stock: 40
  - codigo: P002
    nombre: Lapicera azul
    precio: 300.00
    stock: 120
```

Es muy común en archivos de configuración; por ejemplo, el archivo `mongod.conf` de MongoDB está escrito en YAML. SQL Server no tiene soporte nativo para YAML. El camino habitual es convertir el archivo a JSON con una herramienta externa (hay conversores en línea y utilidades de línea de comandos) y luego usar `OPENJSON`.

## Comparación

| Formato | Estructura | Verbosidad | Legibilidad | Uso típico |
|---|---|---|---|---|
| EDI | Segmentos con delimitadores | Alta | Baja | Intercambio entre empresas (facturas, órdenes de compra) |
| CSV / TSV | Tabular plana | Baja | Alta | Conjuntos de datos abiertos, carga masiva |
| Ancho fijo | Tabular plana, por posición | Nula | Muy baja | Sistemas bancarios y heredados |
| XML | Árbol de elementos | Muy alta | Media | Documentos, configuración, servicios SOAP |
| JSON | Clave-valor jerárquico | Media | Alta | API REST, bases de datos documentales |
| YAML | Clave-valor jerárquico | Baja | Muy alta | Configuración de herramientas |

Los formatos con estructura jerárquica (XML, JSON, YAML) representan anidamiento natural, como un pedido con sus líneas. Los tabulares (CSV, ancho fijo) son planos: para representar relaciones hay que usar varios archivos.

## Errores frecuentes

:::caution[Errores frecuentes]
- **Suponer que un CSV no tiene comillas.** Un nombre con coma parte la fila en más columnas de las esperadas. Hay que leerlo con un lector de CSV real (`FORMAT = 'CSV'`).
- **Confundir el fin de línea.** LF y CRLF son distintos; el archivo de ancho fijo con CRLF tiene 41 caracteres por línea y no 40.
- **Olvidar la codificación.** Un archivo con tildes en UTF-8 leído como página de códigos de Windows muestra caracteres corruptos. Ver [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/).
- **Escribir JSON con comillas simples o comas finales.** No es JSON válido: `ISJSON` devuelve 0.
:::

## Autoevaluación

<details>
<summary>1. ¿Qué diferencia hay entre CSV y ancho fijo al momento de leer un registro?</summary>

En CSV las columnas se separan con un delimitador y cada campo puede tener un largo distinto; en ancho fijo no hay delimitadores y cada campo se ubica por su posición y su largo, que están definidos de antemano.
</details>

<details>
<summary>2. ¿Por qué XML y JSON se prestan mejor que CSV para representar un pedido con varias líneas?</summary>

Porque admiten anidamiento: las líneas del pedido pueden ir dentro del pedido. En CSV hay que repetir los datos del pedido en cada línea o usar dos archivos y relacionarlos por un código.
</details>

<details>
<summary>3. Un archivo YAML con una lista de clientes, ¿cómo se carga en SQL Server?</summary>

Se convierte primero a JSON con una herramienta externa y luego se lee con `OPENJSON`, porque SQL Server no interpreta YAML.
</details>

## En resumen

:::tip[En resumen]
- Un formato de intercambio es un estándar de texto con sintaxis propia; adherir a uno evita acuerdos particulares entre sistemas.
- CSV y ancho fijo son tabulares; XML, JSON y YAML son jerárquicos. EDI está orientado a documentos comerciales entre empresas.
- En SQL Server, XML y JSON tienen soporte propio (tipo `xml`, `OPENJSON`, `FOR JSON`, `FOR XML`); CSV y ancho fijo se cargan con `BULK INSERT`; YAML requiere convertirlo a JSON.
:::

:::tip[Para seguir]
Seguí con [JSON en SQL Server](/bbdd-aplicadas/unidad-2/teoria/json-en-sql/) y [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/).
:::

## Fuentes

- Presentación de cátedra, Unidad 2, parte 2 (Formatos de intercambio), diapositivas 4 a 22.
- Microsoft Learn, [Create a format file with bcp](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/create-a-format-file-sql-server), [BULK INSERT](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql).
- IETF, [RFC 4180: formato CSV](https://www.rfc-editor.org/rfc/rfc4180); [RFC 8259: JSON](https://www.rfc-editor.org/rfc/rfc8259).
- W3C, [Extensible Markup Language (XML) 1.0](https://www.w3.org/TR/xml/); YAML, [especificación](https://yaml.org/spec/).
