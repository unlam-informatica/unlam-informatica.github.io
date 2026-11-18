---
title: Práctica — XML en SQL Server
slug: bbdd-aplicadas/unidad-2/practica/xml
sidebar:
  order: 5
  label: XML en SQL Server
---

Siete ejercicios para generar XML con `FOR XML`, consultarlo con `.nodes()` y `.value()`, leerlo con `OPENXML` e importarlo desde un archivo. Presuponen la lección de [XML en SQL Server](/bbdd-aplicadas/unidad-2/teoria/xml-en-sql/). Los datos son propios. El ejercicio 7 usa el archivo [empleado.xml](/bbdd-aplicadas/unidad-2/practica/archivos/empleado.xml), que debe estar en una carpeta del servidor (por ejemplo `C:\Importar\`).

## Conjunto de datos

Creá una base de prueba (por ejemplo `CREATE DATABASE PracticaXml;`), cambiá a ella y ejecutá:

<!-- check: U2.29 -->
```sql
CREATE SCHEMA rrhh;
GO

CREATE TABLE rrhh.Departamento (
    DepartamentoId INT         NOT NULL,
    Nombre         VARCHAR(40) NOT NULL,
    CONSTRAINT PK_Departamento PRIMARY KEY CLUSTERED (DepartamentoId)
);

CREATE TABLE rrhh.Empleado (
    EmpleadoId     INT           NOT NULL,
    DepartamentoId INT           NOT NULL,
    Nombre         VARCHAR(40)   NOT NULL,
    Cargo          VARCHAR(40)   NOT NULL,
    Salario        DECIMAL(10,2) NOT NULL,
    Email          VARCHAR(80)   NULL,
    CONSTRAINT PK_Empleado PRIMARY KEY CLUSTERED (EmpleadoId),
    CONSTRAINT FK_Empleado_Departamento FOREIGN KEY (DepartamentoId) REFERENCES rrhh.Departamento (DepartamentoId)
);
GO

INSERT INTO rrhh.Departamento (DepartamentoId, Nombre)
VALUES (1, 'Ingenieria'), (2, 'Administracion');

INSERT INTO rrhh.Empleado (EmpleadoId, DepartamentoId, Nombre, Cargo, Salario, Email)
VALUES (1, 1, 'Empleado 01', 'Desarrollo',  120000.00, 'e01@ejemplo.test'),
       (2, 1, 'Empleado 02', 'Operaciones',  98000.00, NULL),
       (3, 2, 'Empleado 03', 'Contaduria',   82000.00, 'e03@ejemplo.test');
GO
```

Los ejercicios 1, 2, 3 y 6 parten de este conjunto de datos. Los ejercicios 4 y 5 usan XML en una variable y el 7 crea su propia tabla.

---

### Ejercicio 1 · Modos de FOR XML RAW
<!-- ejercicio: U2.29 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Exportá `EmpleadoId`, `Nombre` y `Cargo` de `rrhh.Empleado` en tres versiones: (a) `FOR XML RAW` simple; (b) con elemento de fila `Empleado` y raíz `Empleados`; (c) con las columnas como elementos hijo (para (c) mostrá solo los empleados 1 y 2).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `RAW` genera un elemento por fila con las columnas como atributos. `RAW('Empleado')` cambia el nombre del elemento, `ROOT('Empleados')` agrega la raíz (necesaria para obtener un documento) y `ELEMENTS` convierte las columnas en elementos hijo.

<!-- check: U2.29 -->
```sql
SELECT EmpleadoId, Nombre, Cargo
FROM rrhh.Empleado
ORDER BY EmpleadoId
FOR XML RAW;

SELECT EmpleadoId, Nombre, Cargo
FROM rrhh.Empleado
ORDER BY EmpleadoId
FOR XML RAW('Empleado'), ROOT('Empleados');

SELECT EmpleadoId, Nombre, Cargo
FROM rrhh.Empleado
WHERE EmpleadoId <= 2
ORDER BY EmpleadoId
FOR XML RAW('Empleado'), ROOT('Empleados'), ELEMENTS;
```

**Resultado esperado.** (a):

```xml
<row EmpleadoId="1" Nombre="Empleado 01" Cargo="Desarrollo"/><row EmpleadoId="2" Nombre="Empleado 02" Cargo="Operaciones"/><row EmpleadoId="3" Nombre="Empleado 03" Cargo="Contaduria"/>
```

(b):

```xml
<Empleados><Empleado EmpleadoId="1" Nombre="Empleado 01" Cargo="Desarrollo"/><Empleado EmpleadoId="2" Nombre="Empleado 02" Cargo="Operaciones"/><Empleado EmpleadoId="3" Nombre="Empleado 03" Cargo="Contaduria"/></Empleados>
```

(c):

```xml
<Empleados><Empleado><EmpleadoId>1</EmpleadoId><Nombre>Empleado 01</Nombre><Cargo>Desarrollo</Cargo></Empleado><Empleado><EmpleadoId>2</EmpleadoId><Nombre>Empleado 02</Nombre><Cargo>Operaciones</Cargo></Empleado></Empleados>
```
</details>

### Ejercicio 2 · Valores NULL: ELEMENTS y XSINIL
<!-- ejercicio: U2.30 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
El empleado 2 no tiene `Email`. Generá XML con `EmpleadoId` y `Email` para los empleados 1 y 2, primero con `ELEMENTS` y después con `ELEMENTS XSINIL`. ¿Por qué `XSINIL` puede ser importante para quien consume el XML?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con `ELEMENTS` un `NULL` no genera el elemento: el consumidor no puede distinguir "no tiene correo" de "el sistema no informa el correo". Con `ELEMENTS XSINIL` el elemento aparece vacío con `xsi:nil="true"`, que es la forma estándar de XML Schema para expresar "valor nulo".

<!-- check: U2.30 -->
```sql
SELECT EmpleadoId, Email
FROM rrhh.Empleado
WHERE EmpleadoId <= 2
ORDER BY EmpleadoId
FOR XML RAW('Empleado'), ROOT('Empleados'), ELEMENTS;

SELECT EmpleadoId, Email
FROM rrhh.Empleado
WHERE EmpleadoId <= 2
ORDER BY EmpleadoId
FOR XML RAW('Empleado'), ROOT('Empleados'), ELEMENTS XSINIL;
```

**Resultado esperado.** Con `ELEMENTS`:

```xml
<Empleados><Empleado><EmpleadoId>1</EmpleadoId><Email>e01@ejemplo.test</Email></Empleado><Empleado><EmpleadoId>2</EmpleadoId></Empleado></Empleados>
```

Con `ELEMENTS XSINIL`:

```xml
<Empleados xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><Empleado><EmpleadoId>1</EmpleadoId><Email>e01@ejemplo.test</Email></Empleado><Empleado><EmpleadoId>2</EmpleadoId><Email xsi:nil="true"/></Empleado></Empleados>
```

Una aplicación que valida contra un esquema XSD con un elemento obligatorio pero que admite `nil` solo acepta el segundo formato.
</details>

### Ejercicio 3 · Jerarquía de FOR XML AUTO
<!-- ejercicio: U2.31 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Unir `rrhh.Departamento` con `rrhh.Empleado` y generar XML con `FOR XML AUTO` y raíz `Empresa` para el departamento 1: (a) con las columnas del departamento antes que las del empleado; (b) con las columnas del empleado primero. Observá cómo cambia el anidamiento.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `AUTO` crea un elemento por tabla y anida según el orden en que aparecen las tablas en el `SELECT`: la primera tabla es la más externa. En (a) el departamento contiene a sus empleados; en (b), cada empleado contiene a su departamento. Los elementos se llaman como el alias de la tabla (`d`, `e`).

<!-- check: U2.31 -->
```sql
SELECT d.DepartamentoId, d.Nombre AS Departamento, e.EmpleadoId, e.Nombre AS Empleado
FROM rrhh.Departamento AS d
INNER JOIN rrhh.Empleado AS e ON e.DepartamentoId = d.DepartamentoId
WHERE d.DepartamentoId = 1
ORDER BY d.DepartamentoId, e.EmpleadoId
FOR XML AUTO, ROOT('Empresa');

SELECT e.EmpleadoId, e.Nombre AS Empleado, d.DepartamentoId, d.Nombre AS Departamento
FROM rrhh.Empleado AS e
INNER JOIN rrhh.Departamento AS d ON d.DepartamentoId = e.DepartamentoId
WHERE d.DepartamentoId = 1
ORDER BY e.EmpleadoId
FOR XML AUTO, ROOT('Empresa');
```

**Resultado esperado.** (a):

```xml
<Empresa><d DepartamentoId="1" Departamento="Ingenieria"><e EmpleadoId="1" Empleado="Empleado 01"/><e EmpleadoId="2" Empleado="Empleado 02"/></d></Empresa>
```

(b):

```xml
<Empresa><e EmpleadoId="1" Empleado="Empleado 01"><d DepartamentoId="1" Departamento="Ingenieria"/></e><e EmpleadoId="2" Empleado="Empleado 02"><d DepartamentoId="1" Departamento="Ingenieria"/></e></Empresa>
```

En (b) el departamento se repite dentro de cada empleado: el orden de las columnas decide la jerarquía.
</details>

### Ejercicio 4 · .nodes() y .value() con un filtro
<!-- ejercicio: U2.32 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Dado el catálogo XML del script, devolvé en filas el código, el nombre, el precio y el stock de los productos de la categoría `Escolar` que tienen stock mayor que 0.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La ruta de `.nodes()` puede filtrar por atributo (`[@categoria = "Escolar"]`). La condición de stock se aplica con `.exist('stock[. > 0]')` en el `WHERE`, que equivale a "existe un elemento `stock` con valor mayor que 0". El resto son `.value()` con `[1]`.

<!-- check: U2.32 -->
```sql
DECLARE @Catalogo XML = N'
<catalogo>
    <producto codigo="P001" categoria="Escolar">
        <nombre>Cuaderno rayado</nombre>
        <precio>1250.50</precio>
        <stock>40</stock>
    </producto>
    <producto codigo="P002" categoria="Escolar">
        <nombre>Lapicera azul</nombre>
        <precio>300.00</precio>
        <stock>0</stock>
    </producto>
    <producto codigo="P003" categoria="Oficina">
        <nombre>Resma A4</nombre>
        <precio>9800.00</precio>
        <stock>15</stock>
    </producto>
</catalogo>';

SELECT p.value('@codigo', 'CHAR(4)')            AS Codigo,
       p.value('(nombre)[1]', 'VARCHAR(40)')     AS Nombre,
       p.value('(precio)[1]', 'DECIMAL(10,2)')   AS Precio,
       p.value('(stock)[1]', 'INT')              AS Stock
FROM @Catalogo.nodes('/catalogo/producto[@categoria = "Escolar"]') AS t(p)
WHERE p.exist('stock[. > 0]') = 1
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Cuaderno rayado | 1250.50 | 40 |

La lapicera tiene stock 0 y la resma es de otra categoría.
</details>

### Ejercicio 5 · OPENXML con atributos
<!-- ejercicio: U2.33 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Leé con `OPENXML` el XML de productos del script, que guarda los datos en atributos. Uno de los productos se llama `Monitor 27"` (27 pulgadas). Escribí el XML correctamente, liberá el documento al final y explicá qué pasa si el nombre se escribe con la comilla sin escapar.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un valor de atributo delimitado por comillas dobles no puede contener una comilla doble: debe escribirse `&quot;`. Una forma como `"Monitor 27"""` (comillas duplicadas al estilo de SQL) no es XML válido, porque en XML las comillas no se escapan duplicándolas, y la conversión a `xml` falla por documento mal formado. Con el XML bien formado, `sp_xml_preparedocument` devuelve un _handle_, `OPENXML` lee los atributos con `@nombre` y `sp_xml_removedocument` libera la memoria.

<!-- check: U2.33 -->
```sql
DECLARE @Xml XML = N'
<Productos>
    <Producto Codigo="P001" Nombre="Notebook 15"      Precio="1299.99" Stock="12"/>
    <Producto Codigo="P002" Nombre="Mouse inalambrico" Precio="29.99"   Stock="85"/>
    <Producto Codigo="P003" Nombre="Monitor 27&quot;"  Precio="349.99"  Stock="20"/>
</Productos>';

DECLARE @Handle INT;

EXEC sys.sp_xml_preparedocument @Handle OUTPUT, @Xml;

SELECT Codigo, Nombre, Precio, Stock
FROM OPENXML(@Handle, '/Productos/Producto')
WITH (
    Codigo VARCHAR(10)   '@Codigo',
    Nombre VARCHAR(60)   '@Nombre',
    Precio DECIMAL(10,2) '@Precio',
    Stock  INT           '@Stock'
)
ORDER BY Codigo;

EXEC sys.sp_xml_removedocument @Handle;
```

**Resultado esperado.**

| Codigo | Nombre | Precio | Stock |
|---|---|---:|---:|
| P001 | Notebook 15 | 1299.99 | 12 |
| P002 | Mouse inalambrico | 29.99 | 85 |
| P003 | Monitor 27" | 349.99 | 20 |

Otra forma de evitar el problema es delimitar el atributo con comillas simples (`Nombre='Monitor 27"'`).
</details>

### Ejercicio 6 · Departamentos con sus empleados anidados
<!-- ejercicio: U2.34 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Generá, para el departamento 1, un XML con raíz `empresa` donde cada `departamento` (atributos `id` y `nombre`) contenga un elemento `empleados` con un `empleado` por fila (atributos `id`, `nombre` y `salario`).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `FOR XML PATH` con alias que empiezan con `@` produce atributos. Los empleados se obtienen con una subconsulta correlacionada `FOR XML PATH('empleado'), TYPE` en una columna con alias `empleados`; `TYPE` hace que el resultado se incruste como XML y no como texto escapado. El alias de columna `empleados` da nombre al elemento contenedor.

<!-- check: U2.34 -->
```sql
SELECT d.DepartamentoId AS [@id],
       d.Nombre         AS [@nombre],
       (SELECT e.EmpleadoId AS [@id],
               e.Nombre     AS [@nombre],
               e.Salario    AS [@salario]
        FROM rrhh.Empleado AS e
        WHERE e.DepartamentoId = d.DepartamentoId
        ORDER BY e.EmpleadoId
        FOR XML PATH('empleado'), TYPE) AS [empleados]
FROM rrhh.Departamento AS d
WHERE d.DepartamentoId = 1
ORDER BY d.DepartamentoId
FOR XML PATH('departamento'), ROOT('empresa');
```

**Resultado esperado.**

```xml
<empresa><departamento id="1" nombre="Ingenieria"><empleados><empleado id="1" nombre="Empleado 01" salario="120000.00"/><empleado id="2" nombre="Empleado 02" salario="98000.00"/></empleados></departamento></empresa>
```
</details>

### Ejercicio 7 · Importar un archivo XML
<!-- ejercicio: U2.35 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
`empleado.xml` (UTF-8) tiene departamentos con empleados: el nombre del departamento es un atributo del elemento padre, `legajo` y `cargo` son atributos del empleado y `Salario` y `Email` (opcional) son elementos hijo. Importalo en `rrhh.EmpleadoImportado` (`Legajo`, `Departamento`, `Cargo`, `Salario`, `Email`) y comprobá además con `.exist()` que el documento contiene el departamento `Ingeniería`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `OPENROWSET(BULK ..., SINGLE_BLOB)` lee los bytes del archivo y `CAST(... AS XML)` respeta la codificación declarada en el documento, así que las tildes se conservan. `.nodes('/Empresa/Departamento/Empleado')` da una fila por empleado; el departamento se alcanza con `../@nombre` (el padre) y el correo, que es opcional, da `NULL` cuando falta.

<!-- check: U2.35 -->
```sql
CREATE SCHEMA rrhh;
GO

CREATE TABLE rrhh.EmpleadoImportado (
    Legajo       CHAR(4)       NOT NULL,
    Departamento NVARCHAR(40)  NOT NULL,
    Cargo        VARCHAR(40)   NOT NULL,
    Salario      DECIMAL(10,2) NOT NULL,
    Email        VARCHAR(80)   NULL,
    CONSTRAINT PK_EmpleadoImportado PRIMARY KEY CLUSTERED (Legajo)
);
GO

DECLARE @Documento XML = (
    SELECT CAST(a.BulkColumn AS XML)
    FROM OPENROWSET(BULK 'C:\Importar\empleado.xml', SINGLE_BLOB) AS a
);

INSERT INTO rrhh.EmpleadoImportado (Legajo, Departamento, Cargo, Salario, Email)
SELECT e.value('@legajo', 'CHAR(4)'),
       e.value('../@nombre', 'NVARCHAR(40)'),
       e.value('@cargo', 'VARCHAR(40)'),
       e.value('(Salario)[1]', 'DECIMAL(10,2)'),
       e.value('(Email)[1]', 'VARCHAR(80)')
FROM @Documento.nodes('/Empresa/Departamento/Empleado') AS t(e);

SELECT Legajo, Departamento, Cargo, Salario, Email,
       @Documento.exist('/Empresa/Departamento[@nombre = "Ingeniería"]') AS HayIngenieria
FROM rrhh.EmpleadoImportado
ORDER BY Legajo;
```

**Resultado esperado.**

| Legajo | Departamento | Cargo | Salario | Email | HayIngenieria |
|---|---|---|---:|---|---:|
| E001 | Ingeniería | Desarrollo | 120000.00 | NULL | 1 |
| E002 | Ingeniería | Operaciones | 98000.00 | NULL | 1 |
| E003 | Administración | Contaduría | 82000.00 | e003@ejemplo.test | 1 |
</details>
