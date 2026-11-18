---
title: XML en SQL Server
slug: bbdd-aplicadas/unidad-2/teoria/xml-en-sql
sidebar:
  order: 8
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

El formato XML se describe en [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/). Acá se trabaja con él desde T-SQL: guardarlo en el tipo `xml`, consultarlo con sus métodos, leerlo con `OPENXML` y generarlo con `FOR XML`.

## Para qué sirve

Muchos sistemas intercambian documentos XML (facturas electrónicas, respuestas de servicios SOAP, archivos de configuración). SQL Server puede almacenar esos documentos, extraer sus datos en filas y generar XML a partir de tablas.

:::note[Definición]
SQL Server tiene un tipo de dato nativo `xml`. Una columna o variable `xml` solo acepta documentos **bien formados** y expone cinco métodos: `.value()`, `.query()`, `.exist()`, `.nodes()` y `.modify()`. Las consultas usan **XPath/XQuery**.
:::

| Método o herramienta | Qué hace |
|---|---|
| `.value(ruta, tipo)` | Devuelve **un** valor escalar convertido al tipo T-SQL indicado |
| `.query(ruta)` | Devuelve un fragmento XML |
| `.exist(ruta)` | Devuelve 1 si la ruta encuentra algo y 0 si no |
| `.nodes(ruta)` | Divide el XML en una fila por cada nodo que coincide con la ruta |
| `OPENXML` | Lee un documento ya preparado con un _handle_ (método clásico) |
| `FOR XML RAW / AUTO / PATH` | Genera XML a partir del resultado de una consulta |

## Consultar con .value, .exist y .query

`.value()` exige que la ruta devuelva un único valor: por eso se escribe `(/pedido/cliente)[1]`, con el índice `[1]`. El segundo argumento es el tipo T-SQL del resultado.

<!-- check: U2.T.XML.01 -->
```sql
DECLARE @Pedido XML = N'
<pedido numero="1001" estado="abierto">
    <cliente>Ferretería Norte</cliente>
    <linea producto="P001" cantidad="2"><precio>1250.50</precio></linea>
    <linea producto="P003" cantidad="10"><precio>480.25</precio></linea>
</pedido>';

SELECT @Pedido.value('(/pedido/@numero)[1]', 'INT')               AS Numero,
       @Pedido.value('(/pedido/cliente)[1]', 'VARCHAR(40)')       AS Cliente,
       @Pedido.value('count(/pedido/linea)', 'INT')               AS CantidadLineas,
       @Pedido.exist('/pedido/linea[@producto = "P003"]')         AS TieneP003,
       @Pedido.exist('/pedido/linea[@producto = "P999"]')         AS TieneP999,
       @Pedido.query('/pedido/linea[@producto = "P003"]')         AS LineaP003;
```

**Resultado esperado.**

| Numero | Cliente | CantidadLineas | TieneP003 | TieneP999 | LineaP003 |
|---:|---|---:|---:|---:|---|
| 1001 | Ferretería Norte | 2 | 1 | 0 | `<linea producto="P003" cantidad="10"><precio>480.25</precio></linea>` |

Los atributos se referencian con `@nombre` y los elementos hijo por su nombre. Los filtros van entre corchetes (`linea[@producto = "P003"]`).

## Convertir XML en filas con .nodes

`.nodes()` devuelve una fila por cada nodo de la ruta, con un alias de tabla y columna (`t(l)`); sobre esa columna se aplica `.value()` con rutas relativas al nodo.

<!-- check: U2.T.XML.02 -->
```sql
DECLARE @Pedido XML = N'
<pedido numero="1001">
    <linea producto="P001" cantidad="2"><precio>1250.50</precio></linea>
    <linea producto="P003" cantidad="10"><precio>480.25</precio></linea>
</pedido>';

SELECT @Pedido.value('(/pedido/@numero)[1]', 'INT') AS Pedido,
       l.value('@producto', 'CHAR(4)')              AS Producto,
       l.value('@cantidad', 'INT')                  AS Cantidad,
       l.value('(precio)[1]', 'DECIMAL(10,2)')      AS Precio
FROM @Pedido.nodes('/pedido/linea') AS t(l)
ORDER BY Producto;
```

**Resultado esperado.**

| Pedido | Producto | Cantidad | Precio |
|---:|---|---:|---:|
| 1001 | P001 | 2 | 1250.50 |
| 1001 | P003 | 10 | 480.25 |

:::tip[Preferí value('(elemento)[1]') a query(...).value('.')]
Encadenar `.query('Nombre').value('.', 'VARCHAR(50)')` funciona, pero construye un fragmento intermedio por cada celda. `.value('(Nombre)[1]', 'VARCHAR(50)')` hace lo mismo en un solo paso.
:::

## OPENXML

`OPENXML` es el método clásico. Primero se **prepara** el documento con `sp_xml_preparedocument`, que devuelve un _handle_; después se consulta con `OPENXML(handle, ruta)`; y al final se **libera** con `sp_xml_removedocument`. El documento preparado ocupa memoria del servidor hasta que se libera o termina la sesión, por eso nunca hay que omitir el último paso.

<!-- check: U2.T.XML.03 -->
```sql
DECLARE @Xml XML = N'
<clientes>
    <cliente id="1"><nombre>Ferretería Norte</nombre><limite>25000.50</limite></cliente>
    <cliente id="2"><nombre>Kiosco Central</nombre><limite>8000.00</limite></cliente>
</clientes>';

DECLARE @Handle INT;

EXEC sys.sp_xml_preparedocument @Handle OUTPUT, @Xml;

SELECT Id, Nombre, Limite
FROM OPENXML(@Handle, '/clientes/cliente')
WITH (
    Id     INT           '@id',
    Nombre VARCHAR(40)   'nombre',
    Limite DECIMAL(10,2) 'limite'
)
ORDER BY Id;

EXEC sys.sp_xml_removedocument @Handle;
```

**Resultado esperado.**

| Id | Nombre | Limite |
|---:|---|---:|
| 1 | Ferretería Norte | 25000.50 |
| 2 | Kiosco Central | 8000.00 |

Hoy se prefiere `.nodes()` + `.value()`, que no necesita _handle_; `OPENXML` sigue siendo útil en código existente y con documentos grandes que se consultan muchas veces.

## Namespaces y validación con XSD

Si el documento declara un espacio de nombres (`xmlns`), las rutas deben declararlo con `WITH XMLNAMESPACES`; si no, no encuentran nada y devuelven `NULL`:

<!-- check: U2.T.XML.10 -->
```sql
DECLARE @Xml XML = N'
<f:factura xmlns:f="http://ejemplo.test/factura">
    <f:numero>A-0001</f:numero>
    <f:importe>3000.00</f:importe>
</f:factura>';

-- Sin declarar el espacio de nombres, la ruta no encuentra nada
SELECT @Xml.value('(/factura/numero)[1]', 'VARCHAR(20)') AS SinNamespace;

WITH XMLNAMESPACES ('http://ejemplo.test/factura' AS f)
SELECT @Xml.value('(/f:factura/f:numero)[1]', 'VARCHAR(20)')    AS Numero,
       @Xml.value('(/f:factura/f:importe)[1]', 'DECIMAL(10,2)') AS Importe;
```

**Resultado esperado.**

| SinNamespace |
|---|
| NULL |

| Numero | Importe |
|---|---:|
| A-0001 | 3000.00 |

Para exigir que el XML cumpla un esquema, se crea una **colección de esquemas XML** y se tipa la columna o variable con ella (`XML(dbo.EsquemaProducto)`). Un documento que no cumple el esquema se rechaza al asignarlo:

<!-- check: U2.T.XML.11 -->
```sql
CREATE XML SCHEMA COLLECTION dbo.EsquemaProducto AS N'
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="producto">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="nombre" type="xs:string"/>
                <xs:element name="precio" type="xs:decimal"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>';
GO

DECLARE @Valido   XML(dbo.EsquemaProducto) = N'<producto><nombre>Cuaderno</nombre><precio>1250.50</precio></producto>';
DECLARE @Error INT = 0;

BEGIN TRY
    DECLARE @Invalido XML(dbo.EsquemaProducto) = N'<producto><nombre>Cuaderno</nombre><precio>caro</precio></producto>';
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT @Valido.value('(/producto/precio)[1]', 'DECIMAL(10,2)') AS PrecioValido,
       @Error AS NumeroDeErrorConPrecioInvalido;
```

**Resultado esperado.**

| PrecioValido | NumeroDeErrorConPrecioInvalido |
|---:|---:|
| 1250.50 | 6926 |

## Generar XML con FOR XML

`FOR XML` se agrega al final de un `SELECT`. Hay cuatro modos: `RAW`, `AUTO`, `PATH` y `EXPLICIT` (este último, muy engorroso, queda fuera de esta unidad). Los ejemplos usan estas tablas:

<!-- check: U2.T.XML.04 -->
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

Cada bloque siguiente se ejecuta con ese juego de datos ya cargado.

### FOR XML RAW

Cada fila se convierte en un elemento `<row>` y cada columna en un atributo. Una columna `NULL` no aparece.

<!-- check: U2.T.XML.04 -->
```sql
SELECT ClienteId, Nombre, Ciudad
FROM ventas.Cliente
ORDER BY ClienteId
FOR XML RAW;
```

**Resultado esperado.**

```xml
<row ClienteId="1" Nombre="Ferretería Norte" Ciudad="Rosario"/><row ClienteId="2" Nombre="Kiosco Central"/>
```

Con `RAW('nombre')` se cambia el nombre del elemento, con `ROOT('nombre')` se agrega una raíz (sin ella el resultado no es un documento, sino un fragmento con varios elementos) y con `ELEMENTS` las columnas pasan a ser elementos hijo:

<!-- check: U2.T.XML.05 -->
```sql
SELECT ClienteId, Nombre, Ciudad
FROM ventas.Cliente
ORDER BY ClienteId
FOR XML RAW('Cliente'), ROOT('Clientes'), ELEMENTS;
```

**Resultado esperado.**

```xml
<Clientes><Cliente><ClienteId>1</ClienteId><Nombre>Ferretería Norte</Nombre><Ciudad>Rosario</Ciudad></Cliente><Cliente><ClienteId>2</ClienteId><Nombre>Kiosco Central</Nombre></Cliente></Clientes>
```

Con `ELEMENTS` los `NULL` se omiten. Con `ELEMENTS XSINIL` aparecen como elementos vacíos con `xsi:nil="true"`, lo que le permite al consumidor distinguir "sin dato" de "elemento ausente":

<!-- check: U2.T.XML.06 -->
```sql
SELECT ClienteId, Ciudad
FROM ventas.Cliente
ORDER BY ClienteId
FOR XML RAW('Cliente'), ROOT('Clientes'), ELEMENTS XSINIL;
```

**Resultado esperado.**

```xml
<Clientes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><Cliente><ClienteId>1</ClienteId><Ciudad>Rosario</Ciudad></Cliente><Cliente><ClienteId>2</ClienteId><Ciudad xsi:nil="true"/></Cliente></Clientes>
```

`XMLSCHEMA` agrega al resultado el esquema XSD inferido (`FOR XML RAW, ELEMENTS, XMLSCHEMA`).

### FOR XML AUTO

Deduce la estructura de los alias de tabla de la consulta: un `JOIN` genera un elemento por cada tabla, anidado según el **orden de las columnas en el `SELECT`**. Con alias `c` y `p` los elementos se llaman `c` y `p`.

<!-- check: U2.T.XML.07 -->
```sql
SELECT c.ClienteId, c.Nombre, p.PedidoId, p.Total
FROM ventas.Cliente AS c
INNER JOIN ventas.Pedido AS p ON p.ClienteId = c.ClienteId
ORDER BY c.ClienteId, p.PedidoId
FOR XML AUTO, ROOT('Ventas');
```

**Resultado esperado.**

```xml
<Ventas><c ClienteId="1" Nombre="Ferretería Norte"><p PedidoId="1001" Total="3000.00"/><p PedidoId="1002" Total="1250.50"/></c><c ClienteId="2" Nombre="Kiosco Central"><p PedidoId="1003" Total="480.25"/></c></Ventas>
```

Si se invierte el orden de las columnas (primero las de `Pedido`), la jerarquía se invierte: cada pedido contiene a su cliente. El ejercicio 3 de la [práctica](/bbdd-aplicadas/unidad-2/practica/xml/) lo comprueba.

### FOR XML PATH

Da control total: el alias de cada columna es una ruta XPath. `@nombre` produce un atributo y `a/b` elementos anidados. El nombre del elemento de fila se pasa en `PATH('...')`.

<!-- check: U2.T.XML.08 -->
```sql
SELECT c.ClienteId AS [@id],
       c.Nombre    AS [nombre],
       c.Ciudad    AS [direccion/ciudad]
FROM ventas.Cliente AS c
ORDER BY c.ClienteId
FOR XML PATH('cliente'), ROOT('clientes');
```

**Resultado esperado.**

```xml
<clientes><cliente id="1"><nombre>Ferretería Norte</nombre><direccion><ciudad>Rosario</ciudad></direccion></cliente><cliente id="2"><nombre>Kiosco Central</nombre></cliente></clientes>
```

### Relaciones con subconsultas y TYPE

Para anidar los pedidos de cada cliente con la forma deseada se usa una subconsulta `FOR XML ... TYPE` en una columna. `TYPE` hace que la subconsulta devuelva el tipo `xml` y no texto; sin él, el XML interno se escaparía (`&lt;`) como si fuera una cadena. El ejemplo se limita al cliente 1 para que el resultado sea corto.

<!-- check: U2.T.XML.09 -->
```sql
SELECT c.ClienteId AS [@id],
       c.Nombre    AS [nombre],
       (SELECT p.PedidoId AS [@numero], p.Total AS [total]
        FROM ventas.Pedido AS p
        WHERE p.ClienteId = c.ClienteId
        ORDER BY p.PedidoId
        FOR XML PATH('pedido'), TYPE) AS [pedidos]
FROM ventas.Cliente AS c
WHERE c.ClienteId = 1
ORDER BY c.ClienteId
FOR XML PATH('cliente'), ROOT('clientes');
```

**Resultado esperado.**

```xml
<clientes><cliente id="1"><nombre>Ferretería Norte</nombre><pedidos><pedido numero="1001"><total>3000.00</total></pedido><pedido numero="1002"><total>1250.50</total></pedido></pedidos></cliente></clientes>
```

La misma idea con `AUTO`:

<!-- check: U2.T.XML.12 -->
```sql
SELECT c.ClienteId,
       c.Nombre,
       (SELECT p.PedidoId, p.Total
        FROM ventas.Pedido AS p
        WHERE p.ClienteId = c.ClienteId
        ORDER BY p.PedidoId
        FOR XML AUTO, TYPE, ELEMENTS) AS Pedidos
FROM ventas.Cliente AS c
WHERE c.ClienteId = 1
ORDER BY c.ClienteId
FOR XML AUTO, ROOT('Clientes');
```

**Resultado esperado.**

```xml
<Clientes><c ClienteId="1" Nombre="Ferretería Norte"><Pedidos><p><PedidoId>1001</PedidoId><Total>3000.00</Total></p><p><PedidoId>1002</PedidoId><Total>1250.50</Total></p></Pedidos></c></Clientes>
```

## Leer un archivo XML

Para cargar un archivo `.xml` en tablas se lee el archivo con `OPENROWSET(BULK ..., SINGLE_BLOB)`, se convierte a `xml` y se aplica `.nodes()`. El patrón completo está en [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/). Se usa `SINGLE_BLOB` para que el motor respete la codificación declarada en el propio XML.

## Errores frecuentes

:::caution[Errores frecuentes]
- **XML mal formado.** Un `&` o un `<` sin escapar, o una comilla doble dentro de un atributo delimitado por comillas dobles, hace fallar la conversión. `Monitor 27"` en un atributo se escribe `Monitor 27&quot;`.
- **Olvidar `sp_xml_removedocument`.** El documento queda en memoria hasta cerrar la sesión.
- **Rutas con namespace sin declararlo.** Devuelven `NULL` sin error (ver el ejemplo de `WITH XMLNAMESPACES`).
- **`.value()` sin `[1]`.** Falla si la ruta puede devolver más de un valor.
- **Subconsulta `FOR XML` sin `TYPE`.** El XML anidado sale como texto escapado.
:::

## Autoevaluación

<details>
<summary>1. ¿Qué diferencia hay entre `.value()` y `.query()`?</summary>

`.value()` devuelve un escalar convertido a un tipo T-SQL; `.query()` devuelve un fragmento XML.
</details>

<details>
<summary>2. ¿Por qué `FOR XML RAW` con una columna `NULL` omite el atributo y cómo se evita?</summary>

Porque un atributo o elemento ausente representa el `NULL`. Con `ELEMENTS XSINIL` el valor nulo se escribe como un elemento con `xsi:nil="true"`.
</details>

<details>
<summary>3. ¿Cuándo hace falta `TYPE` en una subconsulta `FOR XML`?</summary>

Cuando se la incrusta en la consulta externa como una columna: sin `TYPE` el resultado es texto y se escapa; con `TYPE` es XML y se anida correctamente.
</details>

## En resumen

:::tip[En resumen]
- El tipo `xml` guarda documentos bien formados y se consulta con `.value()`, `.query()`, `.exist()` y `.nodes()`.
- `OPENXML` necesita `sp_xml_preparedocument` y siempre `sp_xml_removedocument`.
- `FOR XML RAW`, `AUTO` y `PATH` generan XML; `ELEMENTS`, `ROOT`, `XSINIL` y `TYPE` ajustan el resultado.
- Los namespaces se declaran con `WITH XMLNAMESPACES` y la validación se hace con una colección de esquemas XSD.
:::

:::tip[Para seguir]
Practicá con la [Práctica — XML en SQL Server](/bbdd-aplicadas/unidad-2/practica/xml/) y después seguí con [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/).
:::

## Fuentes

- Presentación de cátedra, Unidad 2, parte 2 (Formatos de intercambio), diapositivas 12 a 14 (formato XML).
- Microsoft Learn, [Tipo de datos xml](https://learn.microsoft.com/en-us/sql/t-sql/xml/xml-transact-sql), [método nodes()](https://learn.microsoft.com/en-us/sql/t-sql/xml/nodes-method-xml-data-type), [método value()](https://learn.microsoft.com/en-us/sql/t-sql/xml/value-method-xml-data-type), [método exist()](https://learn.microsoft.com/en-us/sql/t-sql/xml/exist-method-xml-data-type), [OPENXML](https://learn.microsoft.com/en-us/sql/t-sql/functions/openxml-transact-sql), [FOR XML](https://learn.microsoft.com/en-us/sql/relational-databases/xml/for-xml-sql-server).
