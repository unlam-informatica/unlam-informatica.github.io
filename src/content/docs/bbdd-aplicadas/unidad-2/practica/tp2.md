---
title: Trabajo Práctico 2 — Collation, importación de CSV y tablas temporales
slug: bbdd-aplicadas/unidad-2/practica/tp2
sidebar:
  label: TP 2 — Collation, importación y temporales
  order: 4
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

**Trabajo práctico 2: collation, importación de CSV y tablas temporales.** Es un trabajo original: el dominio es una **red de estaciones de monitoreo de calidad del aire** (ficticia), con cuatro archivos CSV sintéticos y un esquema propio. Cubre los mismos objetivos que un repaso de la unidad: intercalación (servidor, base, columna y expresión) y sus conflictos, importación de CSV con encabezado, separador, comillas y UTF-8, limpieza segura de texto mal codificado, tablas de carga (staging) y validación, tablas temporales locales y globales, variables de tabla, percentiles y una consulta de resumen. Se resuelve en SQL Server 2019 o 2022.

:::note[Qué lecciones presupone]
- [Collation / Intercalación](/bbdd-aplicadas/unidad-2/teoria/collation/): ejercicios 1, 2, 3, 9, 11, 12 y 15.
- [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/): ejercicios 4 a 9.
- [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/): estructura de un CSV (encabezado, separador, comillas) para los ejercicios 4 a 7.
- [Bases de datos en memoria y tablas temporales](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/): ejercicios 5 y 13.
:::

## Los archivos de datos

Descargá los cuatro archivos y copialos a una carpeta del servidor (los ejemplos usan `C:\datos\tp2\`; reemplazá la ruta por la propia, y recordá que la ruta la resuelve el **servidor**, no el cliente).

| Archivo | Contenido | Casos difíciles a propósito |
|---|---|---|
| [`estaciones.csv`](/bbdd-aplicadas/unidad-2/practica/archivos/tp2/estaciones.csv) | 5 estaciones (`Codigo,Nombre,Barrio,Altura_m`), separador coma | Encabezado; tildes y `Ñ` en UTF-8; coma dentro de un campo entre comillas; comillas dobles escapadas (`""`) |
| [`lecturas.csv`](/bbdd-aplicadas/unidad-2/practica/archivos/tp2/lecturas.csv) | 24 lecturas de PM2,5 (`Estacion;FechaHora;Pm25;Observacion`), separador punto y coma | Punto y coma dentro de un campo entre comillas; comillas escapadas; valor `s/d`; una fecha en la columna de la medición; una estación inexistente; una lectura duplicada |
| [`lecturas-truncada.csv`](/bbdd-aplicadas/unidad-2/practica/archivos/tp2/lecturas-truncada.csv) | Un lote de 4 lecturas | Una línea con un campo de menos |
| [`barrios-mojibake.csv`](/bbdd-aplicadas/unidad-2/practica/archivos/tp2/barrios-mojibake.csv) | 9 barrios (`Codigo,Barrio,Zona`) | Texto ya dañado en origen (`JosÃ©` en lugar de `José`) y un nombre sano que parece dañado (`Sao Pedro`) |

Los archivos terminan las líneas con LF (`0x0a`), por eso los ejemplos usan `ROWTERMINATOR = '0x0a'`. Si tu editor los guarda con CRLF, cambiá el terminador a `'0x0d0a'`. Todos los nombres y valores son ficticios.

:::caution[Qué se usa y qué no según el sistema operativo]
Los ejemplos de esta práctica se ejecutaron en SQL Server 2022 sobre Linux. La opción `CODEPAGE = 'RAW'` (sin conversión de bytes) funciona en Windows y en Linux. En cambio `CODEPAGE = '65001'` (UTF-8) es de Windows: en Linux el motor responde con el error 16202. Por eso la técnica elegida acá es **leer los bytes sin convertir y guardarlos en una columna `VARCHAR` con una collation UTF-8** (ejercicios 4 y 9). Con `65001` el resultado es el mismo en Windows.
:::

## Script de preparación

Los ejercicios 1 y 4 a 8 construyen este esquema paso a paso. El script reúne esas soluciones: ejecutalo en una base de práctica (ver [Cómo estudiar · Antes de ejecutar los ejemplos](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos)) para saltear los ejercicios 4 a 8 y resolver el resto. Crea las tablas de carga (`EstacionCarga`, `LecturaCarga`, todo texto, con columnas UTF-8), las tablas definitivas y la tabla de rechazos, importa los dos archivos y valida las lecturas.

<!-- check: U2.TP2.00 -->

```sql
CREATE SCHEMA aire;
GO

-- Tablas de carga (staging): todo texto, columnas con collation UTF-8
CREATE TABLE aire.EstacionCarga (
    Codigo  VARCHAR(10)                                           NULL,
    Nombre  VARCHAR(100) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    Barrio  VARCHAR(60)  COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    AlturaM VARCHAR(10)                                           NULL
);

CREATE TABLE aire.LecturaCarga (
    Estacion    VARCHAR(10)                                           NULL,
    FechaHora   VARCHAR(30)                                           NULL,
    Pm25        VARCHAR(30)                                           NULL,
    Observacion VARCHAR(300) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL
);

-- Tablas definitivas
CREATE TABLE aire.Estacion (
    Codigo  CHAR(3)      NOT NULL,
    Nombre  NVARCHAR(80) NOT NULL,
    Barrio  NVARCHAR(40) NOT NULL,
    AlturaM SMALLINT     NOT NULL,
    CONSTRAINT PK_Estacion        PRIMARY KEY CLUSTERED (Codigo),
    CONSTRAINT CK_Estacion_Codigo CHECK (Codigo LIKE 'E[0-9][0-9]'),
    CONSTRAINT CK_Estacion_Altura CHECK (AlturaM BETWEEN 0 AND 500)
);

CREATE TABLE aire.Lectura (
    Estacion    CHAR(3)       NOT NULL,
    FechaHora   DATETIME2(0)  NOT NULL,
    Pm25        DECIMAL(5, 1) NOT NULL,
    Observacion NVARCHAR(200) NULL,
    CONSTRAINT PK_Lectura PRIMARY KEY CLUSTERED (Estacion, FechaHora),
    CONSTRAINT FK_Lectura_Estacion FOREIGN KEY (Estacion) REFERENCES aire.Estacion (Codigo),
    CONSTRAINT CK_Lectura_Pm25 CHECK (Pm25 >= 0)
);

CREATE TABLE aire.LecturaRechazada (
    RechazoId INT IDENTITY(1, 1) NOT NULL,
    Estacion  VARCHAR(10) NULL,
    FechaHora VARCHAR(30) NULL,
    Pm25      VARCHAR(30) NULL,
    Motivo    VARCHAR(40) NOT NULL,
    CONSTRAINT PK_LecturaRechazada PRIMARY KEY CLUSTERED (RechazoId)
);
GO

-- Estaciones: coma como separador, encabezado, campos entre comillas, UTF-8
BULK INSERT aire.EstacionCarga
FROM 'C:\datos\tp2\estaciones.csv'
WITH (
    FORMAT          = 'CSV',
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    FIELDQUOTE      = '"',
    ROWTERMINATOR   = '0x0a',
    CODEPAGE        = 'RAW'
);

INSERT INTO aire.Estacion (Codigo, Nombre, Barrio, AlturaM)
SELECT Codigo, Nombre, Barrio, CAST(AlturaM AS SMALLINT)
FROM aire.EstacionCarga;
GO

-- Lecturas: punto y coma como separador
BULK INSERT aire.LecturaCarga
FROM 'C:\datos\tp2\lecturas.csv'
WITH (
    FORMAT          = 'CSV',
    FIRSTROW        = 2,
    FIELDTERMINATOR = ';',
    FIELDQUOTE      = '"',
    ROWTERMINATOR   = '0x0a',
    CODEPAGE        = 'RAW'
);

-- Validación: cada fila inválida recibe un único motivo
WITH Marcada AS (
    SELECT c.Estacion, c.FechaHora, c.Pm25,
           ROW_NUMBER() OVER (PARTITION BY c.Estacion, c.FechaHora ORDER BY c.Pm25) AS Orden,
           CASE
               WHEN e.Codigo IS NULL                               THEN 'Estación inexistente'
               WHEN TRY_CONVERT(DATETIME2(0), c.FechaHora) IS NULL THEN 'Fecha inválida'
               WHEN TRY_CONVERT(DECIMAL(5, 1), c.Pm25) IS NULL     THEN 'Pm25 no numérico'
           END AS Motivo
    FROM aire.LecturaCarga AS c
    LEFT JOIN aire.Estacion AS e ON e.Codigo = c.Estacion
)
INSERT INTO aire.LecturaRechazada (Estacion, FechaHora, Pm25, Motivo)
SELECT Estacion, FechaHora, Pm25, COALESCE(Motivo, 'Duplicada')
FROM Marcada
WHERE Motivo IS NOT NULL OR Orden > 1;

INSERT INTO aire.Lectura (Estacion, FechaHora, Pm25, Observacion)
SELECT c.Estacion, CONVERT(DATETIME2(0), c.FechaHora), CONVERT(DECIMAL(5, 1), c.Pm25), c.Observacion
FROM (
    SELECT c.*, ROW_NUMBER() OVER (PARTITION BY c.Estacion, c.FechaHora ORDER BY c.Pm25) AS Orden
    FROM aire.LecturaCarga AS c
) AS c
JOIN aire.Estacion AS e ON e.Codigo = c.Estacion
WHERE c.Orden = 1
  AND TRY_CONVERT(DATETIME2(0), c.FechaHora) IS NOT NULL
  AND TRY_CONVERT(DECIMAL(5, 1), c.Pm25) IS NOT NULL;
GO

SELECT 'estaciones' AS Tabla, COUNT(*) AS Filas FROM aire.Estacion
UNION ALL SELECT 'lecturas', COUNT(*) FROM aire.Lectura
UNION ALL SELECT 'rechazadas', COUNT(*) FROM aire.LecturaRechazada
ORDER BY Tabla;

SELECT Estacion, FechaHora, Pm25, Motivo FROM aire.LecturaRechazada ORDER BY Estacion, FechaHora;
```

**Resultado esperado.**

| Tabla | Filas |
|---|---:|
| estaciones | 5 |
| lecturas | 20 |
| rechazadas | 4 |

| Estacion | FechaHora | Pm25 | Motivo |
|---|---|---|---|
| E01 | 2026-03-01 12:00 | 30.5 | Duplicada |
| E03 | 2026-03-01 08:00 | s/d | Pm25 no numérico |
| E04 | 2026-03-01 10:00 | 31/03/2026 | Pm25 no numérico |
| E09 | 2026-03-01 08:00 | 25.0 | Estación inexistente |

## Nivel inicial

### Ejercicio 1 · ¿Qué collation tiene cada nivel?
<!-- ejercicio: U2.01 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con el esquema `aire` creado, averiguá la collation de la instancia, la de la base actual y la de su catálogo, y listá la collation de cada columna de texto de `aire.EstacionCarga` y `aire.Estacion`. ¿Qué columnas difieren de la de la base y por qué?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La collation del servidor se lee con `SERVERPROPERTY('Collation')` y la de la base con `DATABASEPROPERTYEX(..., 'Collation')`. La del catálogo (nombres de objetos) está en `sys.databases`. La de cada columna está en `sys.columns.collation_name`, que es `NULL` para las columnas que no son de texto.

<!-- check: U2.01 -->

```sql
SELECT CAST(SERVERPROPERTY('Collation') AS VARCHAR(60))                AS CollationServidor,
       CAST(DATABASEPROPERTYEX(DB_NAME(), 'Collation') AS VARCHAR(60)) AS CollationBase,
       (SELECT catalog_collation_type_desc FROM sys.databases WHERE database_id = DB_ID()) AS CollationCatalogo;

SELECT t.name AS Tabla, c.name AS Columna, c.collation_name AS Collation
FROM sys.columns AS c
JOIN sys.tables  AS t ON t.object_id = c.object_id
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
WHERE s.name = 'aire'
  AND t.name IN ('EstacionCarga', 'Estacion')
  AND c.collation_name IS NOT NULL
ORDER BY t.name, c.column_id;
```

**Resultado esperado** (instalación de SQL Server 2022 con la collation por defecto `SQL_Latin1_General_CP1_CI_AS`; en otra instalación el servidor y la base pueden mostrar otra, por ejemplo `Modern_Spanish_CI_AS`).

| CollationServidor | CollationBase | CollationCatalogo |
|---|---|---|
| SQL_Latin1_General_CP1_CI_AS | SQL_Latin1_General_CP1_CI_AS | DATABASE_DEFAULT |

| Tabla | Columna | Collation |
|---|---|---|
| Estacion | Codigo | SQL_Latin1_General_CP1_CI_AS |
| Estacion | Nombre | SQL_Latin1_General_CP1_CI_AS |
| Estacion | Barrio | SQL_Latin1_General_CP1_CI_AS |
| EstacionCarga | Codigo | SQL_Latin1_General_CP1_CI_AS |
| EstacionCarga | Nombre | Latin1_General_100_CI_AS_SC_UTF8 |
| EstacionCarga | Barrio | Latin1_General_100_CI_AS_SC_UTF8 |
| EstacionCarga | AlturaM | SQL_Latin1_General_CP1_CI_AS |

**Explicación.** Una columna sin `COLLATE` hereda la de la base; la base, la del servidor al crearse. Solo `Nombre` y `Barrio` de la tabla de carga declaran otra (UTF-8) a propósito, para poder recibir los bytes del CSV tal como vienen (ejercicio 4). El catálogo `DATABASE_DEFAULT` indica que los nombres de objetos usan la collation de la base.

</details>

### Ejercicio 2 · Qué distingue cada sufijo
<!-- ejercicio: U2.02 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Sin crear tablas, comprobá cuándo `N'Ñandú'` se considera igual a `N'nandu'` y a `N'Nandu'` según la collation de la comparación: insensible o sensible a mayúsculas (`CI`/`CS`), insensible o sensible a acentos (`AI`/`AS`) y binaria. Explicá cada resultado.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La cláusula `COLLATE` aplicada a una expresión cambia la collation con la que se hace esa comparación, sin tocar ningún dato.

<!-- check: U2.02 -->

```sql
SELECT CASE WHEN N'Ñandú' COLLATE Latin1_General_CI_AI = N'nandu' THEN 'iguales' ELSE 'distintas' END AS CI_AI_nandu,
       CASE WHEN N'Ñandú' COLLATE Latin1_General_CI_AS = N'nandu' THEN 'iguales' ELSE 'distintas' END AS CI_AS_nandu,
       CASE WHEN N'Ñandú' COLLATE Latin1_General_CS_AI = N'nandu' THEN 'iguales' ELSE 'distintas' END AS CS_AI_nandu,
       CASE WHEN N'Ñandú' COLLATE Latin1_General_CS_AI = N'Nandu' THEN 'iguales' ELSE 'distintas' END AS CS_AI_Nandu,
       CASE WHEN N'Ñandú' COLLATE Latin1_General_100_BIN2 = N'Nandu' THEN 'iguales' ELSE 'distintas' END AS BIN2_Nandu;
```

**Resultado esperado.**

| CI_AI_nandu | CI_AS_nandu | CS_AI_nandu | CS_AI_Nandu | BIN2_Nandu |
|---|---|---|---|---|
| iguales | distintas | distintas | iguales | distintas |

**Explicación.** Con `CI_AI` se ignoran mayúsculas y acentos, así que `Ñ` equivale a `n` y todo coincide. Con `CI_AS` el acento (`Ñ` frente a `n`) separa las cadenas. Con `CS_AI` la `n` minúscula difiere de la `Ñ` mayúscula, pero `Nandu` solo se distingue en acentos, que se ignoran. La collation binaria compara code points y no considera iguales a letras distintas.

</details>

### Ejercicio 3 · La collation de una columna decide qué es un duplicado
<!-- ejercicio: U2.03 | nivel: inicial | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Creá `aire.Zona` con dos columnas `NVARCHAR(40)` con restricción `UNIQUE`: `NombreFlexible` con collation `Latin1_General_CI_AI` y `NombreEstricto` con `Latin1_General_CS_AS`. Insertá `Ñandú` en ambas y probá insertar `NANDU` en la flexible y `ñandú` en la estricta. Mostrá qué inserción falla y con qué error.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un índice único compara con la collation de la columna. Las inserciones que fallan se capturan con `TRY...CATCH` para informar `ERROR_NUMBER()`.

<!-- check: U2.03 -->

```sql
CREATE SCHEMA aire;
GO

CREATE TABLE aire.Zona (
    ZonaId         INT IDENTITY(1, 1) NOT NULL,
    NombreFlexible NVARCHAR(40) COLLATE Latin1_General_CI_AI NOT NULL,
    NombreEstricto NVARCHAR(40) COLLATE Latin1_General_CS_AS NOT NULL,
    CONSTRAINT PK_Zona PRIMARY KEY CLUSTERED (ZonaId),
    CONSTRAINT UQ_Zona_NombreFlexible UNIQUE (NombreFlexible),
    CONSTRAINT UQ_Zona_NombreEstricto UNIQUE (NombreEstricto)
);
GO

INSERT INTO aire.Zona (NombreFlexible, NombreEstricto) VALUES (N'Ñandú', N'Ñandú');

BEGIN TRY
    INSERT INTO aire.Zona (NombreFlexible, NombreEstricto) VALUES (N'NANDU', N'Ñandú2');
END TRY
BEGIN CATCH
    SELECT 'NombreFlexible' AS Columna, ERROR_NUMBER() AS Error;
END CATCH;

BEGIN TRY
    INSERT INTO aire.Zona (NombreFlexible, NombreEstricto) VALUES (N'Otra', N'ñandú');
    SELECT 'NombreEstricto' AS Columna, 0 AS Error;
END TRY
BEGIN CATCH
    SELECT 'NombreEstricto' AS Columna, ERROR_NUMBER() AS Error;
END CATCH;

SELECT ZonaId, NombreFlexible, NombreEstricto FROM aire.Zona ORDER BY ZonaId;
```

**Resultado esperado.**

| Columna | Error |
|---|---:|
| NombreFlexible | 2627 |
| NombreEstricto | 0 |

| ZonaId | NombreFlexible | NombreEstricto |
|---:|---|---|
| 1 | Ñandú | Ñandú |
| 3 | Otra | ñandú |

**Explicación.** `NANDU` es duplicado de `Ñandú` para `CI_AI` (error 2627, violación de la restricción única), pero `ñandú` es distinto de `Ñandú` para `CS_AS`. El identificador 2 no aparece: la inserción fallida consumió el valor de `IDENTITY` aunque no guardó la fila.

</details>

### Ejercicio 4 · Importar las estaciones
<!-- ejercicio: U2.04 | nivel: inicial | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Importá `estaciones.csv` a una tabla de carga, respetando el encabezado, las comas dentro de campos entre comillas, las comillas escapadas y las tildes. Verificá que la estación `E02` conserva su coma y que `E04` conserva sus comillas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `FORMAT = 'CSV'` interpreta las comillas (`FIELDQUOTE`), `FIRSTROW = 2` saltea el encabezado y `CODEPAGE = 'RAW'` evita toda conversión de bytes. La columna que recibe el texto es `VARCHAR` con una collation UTF-8, que guarda los bytes como UTF-8. La tabla de carga (`aire.EstacionCarga`) es la del script de preparación.

<!-- check: U2.04 -->

```sql
BULK INSERT aire.EstacionCarga
FROM 'C:\datos\tp2\estaciones.csv'
WITH (
    FORMAT          = 'CSV',
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    FIELDQUOTE      = '"',
    ROWTERMINATOR   = '0x0a',
    CODEPAGE        = 'RAW'
);

SELECT Codigo, Nombre, Barrio, AlturaM, LEN(Nombre) AS LongitudNombre
FROM aire.EstacionCarga
ORDER BY Codigo;
```

**Resultado esperado.**

| Codigo | Nombre | Barrio | AlturaM | LongitudNombre |
|---|---|---|---|---:|
| E01 | Plaza Ñandú | Villa Ocampo | 25 | 11 |
| E02 | Parque Lineal, sector norte | Paso del Rey | 31 | 27 |
| E03 | Estación Ferrocarril | San José | 28 | 20 |
| E04 | Escuela "Paulo Freire" | Los Álamos | 40 | 22 |
| E05 | Mercado Cooperativo | Villa Ocampo | 22 | 19 |

**Explicación.** Las cinco filas llegan completas: la coma de `E02` no parte el campo y las comillas dobles de `E04` se reducen a un par de comillas simples dentro del texto. Todas las columnas de la carga son texto: la conversión a tipos definitivos (`AlturaM` a `SMALLINT`) va en un paso posterior y validado. En Windows también podés escribir `CODEPAGE = '65001'` con una columna `NVARCHAR`.

</details>

### Ejercicio 5 · Ámbito de una temporal local y de una variable de tabla
<!-- ejercicio: U2.05 | nivel: inicial | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
En un mismo lote, creá una tabla temporal local `#Parcial` y una variable de tabla `@Parcial` con las mismas columnas y cargales dos filas. Luego, en el lote siguiente (después de `GO`), comprobá si siguen disponibles. Probá también si un fragmento de SQL dinámico las ve.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Una tabla `#` vive hasta que termina la sesión (o hasta que se elimina) y la ven los ámbitos que la sesión invoca, como el SQL dinámico. Una variable de tabla vive solo en el lote donde se declara. El intento de usar la variable desde otro lote se ejecuta con `EXEC` dentro de `TRY...CATCH`, porque el error se produce al compilar.

<!-- check: U2.05 -->

```sql
CREATE TABLE #Parcial (Estacion CHAR(3) NOT NULL, Pm25 DECIMAL(5, 1) NOT NULL);
DECLARE @Parcial TABLE (Estacion CHAR(3) NOT NULL, Pm25 DECIMAL(5, 1) NOT NULL);

INSERT INTO #Parcial (Estacion, Pm25) VALUES ('E01', 12.5), ('E01', 15.0);
INSERT INTO @Parcial (Estacion, Pm25) VALUES ('E01', 12.5), ('E01', 15.0);

SELECT 'mismo lote' AS Donde,
       (SELECT COUNT(*) FROM #Parcial) AS FilasTemporal,
       (SELECT COUNT(*) FROM @Parcial) AS FilasVariable;
GO

-- Lote nuevo: la tabla temporal sigue en la sesión; la variable ya no existe
SELECT 'lote siguiente' AS Donde, COUNT(*) AS FilasTemporal FROM #Parcial;

BEGIN TRY
    EXEC (N'SELECT COUNT(*) FROM @Parcial;');
END TRY
BEGIN CATCH
    SELECT 'variable en otro lote' AS Intento, ERROR_NUMBER() AS Error;
END CATCH;

-- El SQL dinámico es un ámbito hijo: ve la tabla temporal local de quien lo invoca
EXEC (N'SELECT ''dinámico'' AS Donde, COUNT(*) AS FilasTemporal FROM #Parcial;');

DROP TABLE #Parcial;
```

**Resultado esperado.**

| Donde | FilasTemporal | FilasVariable |
|---|---:|---:|
| mismo lote | 2 | 2 |

| Donde | FilasTemporal |
|---|---:|
| lote siguiente | 2 |

| Intento | Error |
|---|---:|
| variable en otro lote | 1087 |

| Donde | FilasTemporal |
|---|---:|
| dinámico | 2 |

**Explicación.** El error 1087 (`Must declare the table variable`) confirma que la variable no existe fuera de su lote. Las tablas temporales locales (`#`) pertenecen a la sesión: sobreviven a `GO` y las ven los procedimientos y el SQL dinámico invocados desde ella. Las globales (`##`) las ven todas las sesiones (ejercicio 13).

</details>

## Nivel intermedio

### Ejercicio 6 · Cargar las lecturas con separador `;` y comillas
<!-- ejercicio: U2.06 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Importá `lecturas.csv` a `aire.LecturaCarga` (separador punto y coma). Comprobá cuántas filas entraron, cuántas observaciones traen un `;` dentro del campo, cuántas traen comillas y cuántas quedaron vacías, y mostrá esas filas con texto especial.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con `FIELDTERMINATOR = ';'` y `FORMAT = 'CSV'`, el `;` dentro de un campo entre comillas no es separador. Las comillas dobles escapadas llegan como una sola. Los campos vacíos llegan como `NULL`.

<!-- check: U2.06 -->

```sql
BULK INSERT aire.LecturaCarga
FROM 'C:\datos\tp2\lecturas.csv'
WITH (
    FORMAT          = 'CSV',
    FIRSTROW        = 2,
    FIELDTERMINATOR = ';',
    FIELDQUOTE      = '"',
    ROWTERMINATOR   = '0x0a',
    CODEPAGE        = 'RAW'
);

SELECT COUNT(*) AS Filas,
       SUM(CASE WHEN Observacion LIKE '%;%' THEN 1 ELSE 0 END) AS ConSeparadorEnCampo,
       SUM(CASE WHEN Observacion LIKE '%"%' THEN 1 ELSE 0 END) AS ConComillas,
       SUM(CASE WHEN Observacion IS NULL    THEN 1 ELSE 0 END) AS SinObservacion
FROM aire.LecturaCarga;

SELECT Estacion, FechaHora, Pm25, Observacion
FROM aire.LecturaCarga
WHERE Observacion LIKE '%;%' OR Observacion LIKE '%"%'
ORDER BY Estacion, FechaHora;
```

**Resultado esperado.**

| Filas | ConSeparadorEnCampo | ConComillas | SinObservacion |
|---:|---:|---:|---:|
| 24 | 2 | 2 | 17 |

| Estacion | FechaHora | Pm25 | Observacion |
|---|---|---|---|
| E01 | 2026-03-01 09:00 | 15.0 | Viento del sur; sin lluvia |
| E01 | 2026-03-01 12:00 | 30.5 | Quema de pastizales "cercana" |
| E01 | 2026-03-01 12:00 | 30.5 | Quema de pastizales "cercana" |
| E03 | 2026-03-01 09:00 | 41.0 | Tránsito pesado; hora pico |

**Explicación.** Las 24 líneas de datos entran todas, incluidas las que luego se rechazarán por su contenido: la tabla de carga no valida, solo recibe. Sin `FORMAT = 'CSV'` (o con otro `FIELDQUOTE`), las comillas quedarían dentro del texto y los `;` internos partirían los campos.

</details>

### Ejercicio 7 · Un lote con una línea truncada
<!-- ejercicio: U2.07 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
`lecturas-truncada.csv` trae una línea con un campo de menos. Intentá importarlo con `FORMAT = 'CSV'` y capturá el error; verificá que no quedó ninguna fila cargada. Después diagnosticá cuál es la línea defectuosa leyendo el archivo como líneas de texto y contando separadores.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `FORMAT = 'CSV'` es estricto: una línea que no tiene el número de campos de la tabla aborta la carga completa. Para encontrar la línea, se importa cada línea entera a una única columna (un terminador de campo que no aparece en el archivo, como `0x1f`) y se cuentan los `;`. Como `BULK INSERT` no devuelve el número de línea, la tabla tiene una columna `IDENTITY` y se carga a través de una vista que solo expone el texto.

<!-- check: U2.07 -->

```sql
CREATE TABLE dbo.LecturaPrueba (
    Estacion VARCHAR(10), FechaHora VARCHAR(30), Pm25 VARCHAR(30), Observacion VARCHAR(300)
);
GO

-- 1) Con FORMAT = 'CSV', una línea con campos de menos aborta toda la carga
BEGIN TRY
    BULK INSERT dbo.LecturaPrueba
    FROM 'C:\datos\tp2\lecturas-truncada.csv'
    WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ';', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');
END TRY
BEGIN CATCH
    SELECT 'carga CSV' AS Intento, ERROR_NUMBER() AS Error;
END CATCH;
SELECT COUNT(*) AS FilasCargadas FROM dbo.LecturaPrueba;
GO

-- 2) Diagnóstico: cada línea entra entera en una columna
CREATE TABLE dbo.LineaCruda (
    NumeroLinea INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    Texto       VARCHAR(500) NULL
);
GO
CREATE VIEW dbo.LineaCrudaTexto AS SELECT Texto FROM dbo.LineaCruda;
GO

BULK INSERT dbo.LineaCrudaTexto
FROM 'C:\datos\tp2\lecturas-truncada.csv'
WITH (FIELDTERMINATOR = '0x1f', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');

SELECT NumeroLinea, Texto, LEN(Texto) - LEN(REPLACE(Texto, ';', '')) AS Separadores
FROM dbo.LineaCruda
WHERE LEN(Texto) - LEN(REPLACE(Texto, ';', '')) <> 3
ORDER BY NumeroLinea;
```

**Resultado esperado.**

| Intento | Error |
|---|---:|
| carga CSV | 7330 |

| FilasCargadas |
|---:|
| 0 |

| NumeroLinea | Texto | Separadores |
|---:|---|---:|
| 3 | E01;2026-03-02 09:00;13.5 | 2 |

**Explicación.** En SQL Server 2022 sobre Linux la carga falla con el error 7330 (el mensaje 4879 que lo acompaña indica la fila y la columna del problema) y no queda ninguna fila: es una carga todo o nada. La línea 3 del archivo (el encabezado es la 1) tiene 2 separadores en lugar de 3. Este conteo de `;` sirve solo para archivos cuyos campos no llevan `;` entre comillas, como este. Sin `FORMAT = 'CSV'`, `MAXERRORS` permitiría seguir, pero el motor no entiende comillas y la línea truncada se fusiona con la siguiente: se pierden datos sin aviso. Conviene devolver el archivo a quien lo generó.

</details>

### Ejercicio 8 · Validar la carga y registrar los rechazos
<!-- ejercicio: U2.08 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con `aire.LecturaCarga` cargada, pasá a `aire.Lectura` solo las filas válidas y guardá las rechazadas en `aire.LecturaRechazada` con un motivo único: estación inexistente, fecha inválida, `Pm25` no numérico o duplicada. Informá cuántas filas se rechazaron por cada motivo y comprobá que todo se contabiliza.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `TRY_CONVERT` devuelve `NULL` en lugar de un error cuando el valor no se puede convertir, por lo que sirve para clasificar. El orden de las condiciones en el `CASE` define cuál es el motivo cuando una fila falla por varios. Las duplicadas se detectan con `ROW_NUMBER()` sobre la clave de la tabla definitiva. Las filas válidas son las que no tienen motivo y tienen número 1. El bloque completo está en el script de preparación; acá se muestra el control posterior.

<!-- check: U2.08 -->

```sql
SELECT Motivo, COUNT(*) AS Filas
FROM aire.LecturaRechazada
GROUP BY Motivo
ORDER BY Motivo;

SELECT (SELECT COUNT(*) FROM aire.LecturaCarga)     AS EnStaging,
       (SELECT COUNT(*) FROM aire.Lectura)          AS Aceptadas,
       (SELECT COUNT(*) FROM aire.LecturaRechazada) AS Rechazadas;
```

**Resultado esperado.**

| Motivo | Filas |
|---|---:|
| Duplicada | 1 |
| Estación inexistente | 1 |
| Pm25 no numérico | 2 |

| EnStaging | Aceptadas | Rechazadas |
|---:|---:|---:|
| 24 | 20 | 4 |

**Explicación.** 24 = 20 + 4: ninguna fila se pierde ni se cuenta dos veces. Las dos filas de `Pm25 no numérico` son `s/d` (valor ausente) y `31/03/2026` (una fecha cargada en la columna equivocada). La duplicada es la segunda copia de la lectura de `E01` de las 12:00, que se rechaza para respetar la clave primaria. Si el proceso se vuelve a ejecutar, hay que vaciar antes la tabla de carga y la de rechazos para no duplicarlas.

</details>

### Ejercicio 9 · Elegir la collation de la columna de carga
<!-- ejercicio: U2.09 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Importá `estaciones.csv` dos veces: a una columna `VARCHAR` con la collation de la base (página de códigos 1252) y a otra con una collation UTF-8, ambas con `CODEPAGE = 'RAW'`. Mostrá en qué estaciones el texto difiere, y explicá por qué.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El archivo está en UTF-8: `Ñ` ocupa 2 bytes. Con `RAW` los bytes llegan sin conversión. Si la columna interpreta esos bytes como Windows-1252, cada byte es un carácter y aparece el texto dañado (`Ã‘`). Si la columna es UTF-8, los interpreta bien. Comparar `LEN` de ambas revela cuáles filas tienen caracteres fuera de ASCII.

<!-- check: U2.09 -->

```sql
CREATE SCHEMA prueba;
GO

CREATE TABLE prueba.CargaBase (
    Codigo  VARCHAR(10)  NULL,
    Nombre  VARCHAR(100) NULL,   -- collation de la base: página de códigos 1252
    Barrio  VARCHAR(60)  NULL,
    AlturaM VARCHAR(10)  NULL
);

CREATE TABLE prueba.CargaUtf8 (
    Codigo  VARCHAR(10)  NULL,
    Nombre  VARCHAR(100) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    Barrio  VARCHAR(60)  COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    AlturaM VARCHAR(10)  NULL
);
GO

BULK INSERT prueba.CargaBase
FROM 'C:\datos\tp2\estaciones.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');

BULK INSERT prueba.CargaUtf8
FROM 'C:\datos\tp2\estaciones.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');

SELECT b.Codigo,
       b.Nombre AS ColumnaBase,
       u.Nombre AS ColumnaUtf8,
       LEN(b.Nombre) AS LongitudBase,
       LEN(u.Nombre) AS LongitudUtf8
FROM prueba.CargaBase AS b
JOIN prueba.CargaUtf8 AS u ON u.Codigo = b.Codigo
WHERE LEN(b.Nombre) <> LEN(u.Nombre)
ORDER BY b.Codigo;
```

**Resultado esperado.**

| Codigo | ColumnaBase | ColumnaUtf8 | LongitudBase | LongitudUtf8 |
|---|---|---|---:|---:|
| E01 | Plaza Ã‘andÃº | Plaza Ñandú | 13 | 11 |
| E03 | EstaciÃ³n Ferrocarril | Estación Ferrocarril | 21 | 20 |

**Explicación.** Las dos filas muestran el defecto típico del mojibake: cada carácter acentuado de 2 bytes se lee como 2 caracteres. E02, E04 y E05 no difieren porque su nombre no tiene acentos (los de `E04` están en `Barrio`, que no se comparó). Elegir bien la collation de la columna de carga evita corregir después. Si el texto llega ya dañado en origen, hace falta una limpieza (ejercicio 12).

</details>

### Ejercicio 10 · Mediana y percentil 90 por estación
<!-- ejercicio: U2.10 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con `aire.Lectura` ya cargada, calculá por estación la cantidad de lecturas, la mediana y el percentil 90 de `Pm25` con `PERCENTILE_CONT` y con `PERCENTILE_DISC`. Explicá en qué filas difieren y por qué.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Ambas funciones son de ventana: se escriben con `WITHIN GROUP (ORDER BY ...) OVER (PARTITION BY ...)`, repiten el valor en cada fila de la partición y por eso se agrega `DISTINCT`. `PERCENTILE_CONT` interpola entre valores y devuelve un número de coma flotante: se convierte a `DECIMAL` para mostrarlo sin ruido. `PERCENTILE_DISC` devuelve un valor existente de la serie.

<!-- check: U2.10 -->

```sql
SELECT DISTINCT
       Estacion,
       COUNT(*) OVER (PARTITION BY Estacion) AS Lecturas,
       CAST(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Pm25) OVER (PARTITION BY Estacion) AS DECIMAL(6, 2)) AS MedianaCont,
       PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY Pm25) OVER (PARTITION BY Estacion) AS MedianaDisc,
       CAST(PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY Pm25) OVER (PARTITION BY Estacion) AS DECIMAL(6, 2)) AS P90Cont,
       PERCENTILE_DISC(0.9) WITHIN GROUP (ORDER BY Pm25) OVER (PARTITION BY Estacion) AS P90Disc
FROM aire.Lectura
ORDER BY Estacion;
```

**Resultado esperado.**

| Estacion | Lecturas | MedianaCont | MedianaDisc | P90Cont | P90Disc |
|---|---:|---:|---:|---:|---:|
| E01 | 5 | 18.50 | 18.5 | 27.10 | 30.5 |
| E02 | 5 | 10.50 | 10.5 | 15.32 | 18.2 |
| E03 | 4 | 51.75 | 48.0 | 58.65 | 60.0 |
| E04 | 4 | 18.00 | 16.5 | 19.85 | 20.0 |
| E05 | 2 | 30.25 | 27.0 | 32.85 | 33.5 |

**Explicación.** Con una cantidad impar de lecturas (E01, E02) la mediana coincide en ambas funciones, porque cae sobre un valor. Con cantidad par (E03, E04, E05) la mediana continua es el promedio de los dos centrales (para E03, 48.0 y 55.5 dan 51.75), mientras que la discreta devuelve el primer valor de la serie ordenada cuya posición relativa alcanza el 50 % (48.0). En el percentil 90 de E01 con 5 valores, la posición es 0,9 × 4 = 3,6: la continua interpola entre el cuarto (22.0) y el quinto (30.5) valor, 27,1; la discreta devuelve el primero que alcanza el 90 %, 30.5.

</details>

## Nivel avanzado

### Ejercicio 11 · Conflicto de collation en JOIN e INTERSECT
<!-- ejercicio: U2.11 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Creá dos tablas de barrios cuyas columnas tienen distinta collation (`Latin1_General_CI_AI` y `Latin1_General_CS_AS`). Mostrá que un `JOIN` y un `INTERSECT` entre ellas fallan, y resolvelo con `COLLATE` de dos maneras que dan resultados distintos. Explicá por qué la elección de la collation cambia la respuesta.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dos columnas con collations explícitas distintas no se pueden comparar: el motor no elige y da el error 468. Como el conflicto se detecta al compilar la sentencia, para capturarlo con `TRY...CATCH` hay que ejecutarla con `EXEC`. La solución es declarar con `COLLATE` cuál rige, y esa elección define qué es "igual". El error es el mismo con `UNION` y `EXCEPT`.

<!-- check: U2.11 -->

```sql
CREATE SCHEMA prueba;
GO

CREATE TABLE prueba.BarrioFlexible (Nombre NVARCHAR(40) COLLATE Latin1_General_CI_AI NOT NULL);
CREATE TABLE prueba.BarrioEstricto (Nombre NVARCHAR(40) COLLATE Latin1_General_CS_AS NOT NULL);
GO

INSERT INTO prueba.BarrioFlexible (Nombre) VALUES (N'San José'), (N'Villa Ocampo'), (N'Nuñez');
INSERT INTO prueba.BarrioEstricto (Nombre) VALUES (N'San Jose'), (N'Villa Ocampo'), (N'Nuñez');
GO

-- 1) Sin resolver: cada operación falla con el error 468 (se ejecuta con EXEC para poder capturarlo:
--    el conflicto se detecta al compilar la sentencia)
BEGIN TRY
    EXEC (N'SELECT f.Nombre FROM prueba.BarrioFlexible AS f JOIN prueba.BarrioEstricto AS e ON e.Nombre = f.Nombre;');
END TRY
BEGIN CATCH
    SELECT 'JOIN' AS Operacion, ERROR_NUMBER() AS Error;
END CATCH;

BEGIN TRY
    EXEC (N'SELECT Nombre FROM prueba.BarrioFlexible INTERSECT SELECT Nombre FROM prueba.BarrioEstricto;');
END TRY
BEGIN CATCH
    SELECT 'INTERSECT' AS Operacion, ERROR_NUMBER() AS Error;
END CATCH;
GO

-- 2) Resuelto: la collation de la comparación se elige con COLLATE, y cambia el resultado
SELECT Nombre FROM prueba.BarrioFlexible
INTERSECT
SELECT Nombre COLLATE Latin1_General_CI_AI FROM prueba.BarrioEstricto
ORDER BY Nombre;

SELECT Nombre COLLATE Latin1_General_CS_AS AS Nombre FROM prueba.BarrioFlexible
INTERSECT
SELECT Nombre FROM prueba.BarrioEstricto
ORDER BY Nombre;
```

**Resultado esperado.**

| Operacion | Error |
|---|---:|
| JOIN | 468 |

| Operacion | Error |
|---|---:|
| INTERSECT | 468 |

Con `CI_AI` (tres filas):

| Nombre |
|---|
| Nuñez |
| San José |
| Villa Ocampo |

Con `CS_AS` (dos filas):

| Nombre |
|---|
| Nuñez |
| Villa Ocampo |

**Explicación.** Con `CI_AI`, `San José` y `San Jose` son la misma cadena, así que la intersección tiene tres filas. Con `CS_AS` son distintas y quedan dos. La collation no es un detalle de formato: decide el resultado. Para comparar columnas de bases con distinta collation, `COLLATE DATABASE_DEFAULT` toma la de la base donde corre la consulta (ejercicio 15).

</details>

### Ejercicio 12 · Limpieza segura de texto mal codificado
<!-- ejercicio: U2.12 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
`barrios-mojibake.csv` llegó con el texto ya dañado (`San JosÃ©`). Importalo y corregí los barrios reemplazando las secuencias dañadas más comunes por su carácter correcto. Compará una reparación con la collation `Latin1_General_CI_AI` con otra de comparación binaria y mostrá por qué la primera es peligrosa. Verificá al final que no quede ningún residuo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El texto dañado es UTF-8 interpretado como Windows-1252 y vuelto a guardar: `é` (2 bytes) se transformó en `Ã©` (2 caracteres). Se reemplaza cada secuencia por la letra original. `REPLACE` usa la collation de la expresión para decidir qué coincide: con una collation insensible a acentos, el patrón `Ãº` (el dañado de `ú`) coincide con `ao`, porque `º` se considera una `o` y `Ã` una `a`. Con una collation binaria solo coincide la secuencia exacta. Los patrones se arman con `NCHAR` para que ningún editor los altere.

<!-- check: U2.12 -->

```sql
CREATE SCHEMA prueba;
GO

CREATE TABLE prueba.BarrioCarga (
    Codigo VARCHAR(10) NULL,
    Barrio VARCHAR(60) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NULL,
    Zona   VARCHAR(10) NULL
);
GO

BULK INSERT prueba.BarrioCarga
FROM 'C:\datos\tp2\barrios-mojibake.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2, FIELDTERMINATOR = ',', ROWTERMINATOR = '0x0a', CODEPAGE = 'RAW');

-- Secuencias dañadas: Ã + otro carácter (UTF-8 leído como Windows-1252).
-- Reparación ingenua (collation CI_AI) frente a reparación segura (comparación binaria)
WITH Texto AS (
    SELECT Codigo, CAST(Barrio AS NVARCHAR(60)) AS Original FROM prueba.BarrioCarga
)
SELECT t.Codigo,
       t.Original,
       i.Ingenua,
       s.Segura
FROM Texto AS t
CROSS APPLY (
    SELECT REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(t.Original COLLATE Latin1_General_CI_AI,
           NCHAR(195) + NCHAR(161),  N'á'),
           NCHAR(195) + NCHAR(169),  N'é'),
           NCHAR(195) + NCHAR(179),  N'ó'),
           NCHAR(195) + NCHAR(186),  N'ú'),
           NCHAR(195) + NCHAR(177),  N'ñ'),
           NCHAR(195) + NCHAR(8216), N'Ñ') AS Ingenua
) AS i
CROSS APPLY (
    SELECT REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(t.Original COLLATE Latin1_General_100_BIN2,
           NCHAR(195) + NCHAR(161),  N'á'),
           NCHAR(195) + NCHAR(169),  N'é'),
           NCHAR(195) + NCHAR(179),  N'ó'),
           NCHAR(195) + NCHAR(186),  N'ú'),
           NCHAR(195) + NCHAR(177),  N'ñ'),
           NCHAR(195) + NCHAR(8216), N'Ñ') AS Segura
) AS s
ORDER BY t.Codigo;

-- Control posterior: ninguna fila reparada conserva la letra Ã (código 195)
SELECT COUNT(*) AS FilasConResiduo
FROM prueba.BarrioCarga
WHERE CHARINDEX(NCHAR(195),
      REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(CAST(Barrio AS NVARCHAR(60)) COLLATE Latin1_General_100_BIN2,
      NCHAR(195) + NCHAR(161),  N'á'),
      NCHAR(195) + NCHAR(169),  N'é'),
      NCHAR(195) + NCHAR(179),  N'ó'),
      NCHAR(195) + NCHAR(186),  N'ú'),
      NCHAR(195) + NCHAR(177),  N'ñ'),
      NCHAR(195) + NCHAR(8216), N'Ñ') COLLATE Latin1_General_100_BIN2) > 0;
```

**Resultado esperado.**

| Codigo | Original | Ingenua | Segura |
|---|---|---|---|
| B01 | Villa Ocampo | Villa Ocampo | Villa Ocampo |
| B02 | San JosÃ© | San José | San José |
| B03 | NuÃ±ez Chico | Nuñez Chico | Nuñez Chico |
| B04 | ConstituciÃ³n | Constitución | Constitución |
| B05 | Paso del Rey | Paso del Rey | Paso del Rey |
| B06 | PeÃ±a y Lillo | Peña y Lillo | Peña y Lillo |
| B07 | Sao Pedro | **Sú Pedro** | Sao Pedro |
| B08 | Avenida Ã‘andÃº | Avenida Ñandú | Avenida Ñandú |
| B09 | Bajo Hondo | Bajo Hondo | Bajo Hondo |

| FilasConResiduo |
|---:|
| 0 |

**Explicación.** Las dos reparaciones coinciden salvo en `Sao Pedro`, un nombre sano que la reparación ingenua convierte en `Sú Pedro` porque `ao` es "igual" a `Ãº` bajo `CI_AI`. Ese es el tipo de error silencioso que hace insegura esta limpieza en una base con collation insensible a acentos. La regla: reparar con comparación binaria, listar las secuencias conocidas, revisar antes y después (acá, con el control del residuo) y, si se puede, volver a importar con la codificación correcta en lugar de parchar.

</details>

### Ejercicio 13 · Temporales locales y globales, procedimientos y vistas
<!-- ejercicio: U2.13 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Escribí `aire.PrepararResumen`, un procedimiento que crea una tabla temporal local `#Interna` y una global `##ResumenEstacion` con la cantidad de lecturas y el máximo por estación. Mostrá desde fuera del procedimiento cuál de las dos sigue existiendo. Escribí `aire.ContarParcial`, que lee una `#Parcial` que no crea, y mostrá que funciona si el llamador la creó. Probá crear una vista sobre `##ResumenEstacion` y proponé la alternativa válida.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Una tabla `#` creada dentro de un procedimiento se elimina al terminar este; una `##` sigue visible. En sentido inverso, un procedimiento ve las `#` del código que lo invoca (por eso conviene documentar la dependencia). Una vista no puede definirse sobre una tabla temporal, local ni global (error 4508): la alternativa es definirla sobre las tablas permanentes, o materializar el resultado en una tabla permanente.

<!-- check: U2.13 -->

```sql
CREATE PROCEDURE aire.PrepararResumen
AS
BEGIN
    SET NOCOUNT ON;

    CREATE TABLE #Interna (N INT NOT NULL);          -- local: muere al terminar el procedimiento

    IF OBJECT_ID('tempdb..##ResumenEstacion') IS NOT NULL
        DROP TABLE ##ResumenEstacion;

    SELECT Estacion, COUNT(*) AS Lecturas, MAX(Pm25) AS Maximo
    INTO ##ResumenEstacion                           -- global: visible para toda la instancia
    FROM aire.Lectura
    GROUP BY Estacion;
END;
GO

CREATE PROCEDURE aire.ContarParcial
AS
    SELECT COUNT(*) AS FilasDelLlamador FROM #Parcial;   -- usa la temporal local del código que lo invoca
GO

EXEC aire.PrepararResumen;

-- La global sigue existiendo fuera del procedimiento; la local ya no
SELECT Estacion, Lecturas, Maximo FROM ##ResumenEstacion ORDER BY Estacion;
SELECT CASE WHEN OBJECT_ID('tempdb..#Interna') IS NULL THEN 'ya no existe' ELSE 'existe' END AS TablaInterna;

CREATE TABLE #Parcial (Estacion CHAR(3) NOT NULL);
INSERT INTO #Parcial (Estacion) VALUES ('E01'), ('E02'), ('E03');
EXEC aire.ContarParcial;
GO

-- Una vista no puede apoyarse en una tabla temporal (local o global)
BEGIN TRY
    EXEC (N'CREATE VIEW aire.VistaResumen AS SELECT Estacion, Lecturas, Maximo FROM ##ResumenEstacion;');
END TRY
BEGIN CATCH
    SELECT 'vista sobre ##ResumenEstacion' AS Intento, ERROR_NUMBER() AS Error;
END CATCH;
GO

-- Alternativa: la vista se define sobre las tablas permanentes
CREATE VIEW aire.VistaResumen
AS
SELECT Estacion, COUNT(*) AS Lecturas, MAX(Pm25) AS Maximo
FROM aire.Lectura
GROUP BY Estacion;
GO

SELECT Estacion, Lecturas, Maximo FROM aire.VistaResumen ORDER BY Estacion;

DROP TABLE ##ResumenEstacion;
DROP TABLE #Parcial;
```

**Resultado esperado.**

| Estacion | Lecturas | Maximo |
|---|---:|---:|
| E01 | 5 | 30.5 |
| E02 | 5 | 18.2 |
| E03 | 4 | 60.0 |
| E04 | 4 | 20.0 |
| E05 | 2 | 33.5 |

| TablaInterna |
|---|
| ya no existe |

| FilasDelLlamador |
|---:|
| 3 |

| Intento | Error |
|---|---:|
| vista sobre ##ResumenEstacion | 4508 |

La última consulta (`aire.VistaResumen`) repite la primera tabla.

**Explicación.** Las tres reglas de ámbito: la local del procedimiento desaparece con él, la global sobrevive hasta que se elimina o se cierra la última sesión que la usa, y las locales del llamador son visibles para los procedimientos que invoca. Que una `##` sea visible para *otras* sesiones no se puede mostrar en una sola conexión: el ejercicio 15 lo plantea con dos sesiones.

</details>

### Ejercicio 14 · Consulta de resumen por estación
<!-- ejercicio: U2.14 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Producí un resumen por estación con su barrio, la cantidad de lecturas válidas, la cantidad de lecturas rechazadas, el promedio, la mediana y el percentil 90 de `Pm25`, y un puesto según el percentil 90 (de mayor a menor, con empates compartiendo puesto).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dos CTE separan los cálculos: las estadísticas por estación (con las funciones de ventana y `DISTINCT`) y los rechazos agrupados. La consulta final une con `aire.Estacion` y aplica `RANK()` sobre el resultado de la CTE, no sobre las filas originales. El rechazo de la estación inexistente `E09` no aparece porque no hay estación a la cual asignarlo.

<!-- check: U2.14 -->

```sql
WITH Estadistica AS (
    SELECT DISTINCT
           Estacion,
           COUNT(*) OVER (PARTITION BY Estacion) AS Lecturas,
           CAST(AVG(Pm25) OVER (PARTITION BY Estacion) AS DECIMAL(5, 1)) AS Promedio,
           CAST(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Pm25) OVER (PARTITION BY Estacion) AS DECIMAL(5, 1)) AS Mediana,
           CAST(PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY Pm25) OVER (PARTITION BY Estacion) AS DECIMAL(5, 1)) AS P90
    FROM aire.Lectura
),
Rechazo AS (
    SELECT Estacion, COUNT(*) AS Rechazadas
    FROM aire.LecturaRechazada
    GROUP BY Estacion
)
SELECT RANK() OVER (ORDER BY s.P90 DESC) AS Puesto,
       e.Codigo,
       e.Barrio,
       s.Lecturas,
       COALESCE(r.Rechazadas, 0) AS Rechazadas,
       s.Promedio,
       s.Mediana,
       s.P90
FROM aire.Estacion AS e
JOIN Estadistica   AS s ON s.Estacion = e.Codigo
LEFT JOIN Rechazo  AS r ON r.Estacion = e.Codigo
ORDER BY Puesto, e.Codigo;
```

**Resultado esperado.**

| Puesto | Codigo | Barrio | Lecturas | Rechazadas | Promedio | Mediana | P90 |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | E03 | San José | 4 | 1 | 51.1 | 51.8 | 58.7 |
| 2 | E05 | Villa Ocampo | 2 | 0 | 30.3 | 30.3 | 32.9 |
| 3 | E01 | Villa Ocampo | 5 | 1 | 19.7 | 18.5 | 27.1 |
| 4 | E04 | Los Álamos | 4 | 1 | 17.5 | 18.0 | 19.9 |
| 5 | E02 | Paso del Rey | 5 | 0 | 11.4 | 10.5 | 15.3 |

**Explicación.** Los valores con un decimal salen de redondear al convertir: la mediana de E03 es 51,75 y se muestra 51.8; la de E05 es 30,25 y se muestra 30.3. El puesto se calcula sobre el resultado ya agrupado: un `RANK` aplicado a las lecturas individuales ordenaría lecturas y no estaciones. E05 tiene solo dos lecturas: un percentil sobre tan pocos valores es poco confiable, y un reporte real debería mostrar la cantidad como aquí.

</details>

### Ejercicio 15 · Bases con otra collation, `tempdb` y dos sesiones
<!-- ejercicio: U2.15 | nivel: avanzado | tipo: diagnostico | verificacion: revisado -->

:::note[Enunciado]
(a) Creá dos bases, `AireCsAs` (`Latin1_General_100_CS_AS`) y `AireCiAi` (`Latin1_General_100_CI_AI`), con una tabla `dbo.Barrio` en cada una. Mostrá que un `INTERSECT` entre ellas falla con el error 468 y resolvelo con `COLLATE DATABASE_DEFAULT`. (b) Comprobá qué collation toma una columna de tabla temporal y cómo evitar el conflicto. (c) Verificá con dos sesiones que una tabla temporal global es visible para otras conexiones y que desaparece cuando termina la que la creó.
:::

:::caution[No probado en un motor]
Este ejercicio necesita el permiso `CREATE DATABASE` (para crear las dos bases) y dos sesiones, es decir, dos ventanas de consulta conectadas a la misma instancia (ver [Cómo estudiar · Antes de ejecutar los ejemplos](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos)). Los resultados de (a) y (b) se obtuvieron con SQL Server 2022; el paso (c), que usa las dos sesiones, no se probó en un motor y el resultado es el que describe la documentación de Microsoft: comprobalo en tu instalación.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada base fija la collation por defecto de sus columnas, así que una consulta que cruza ambas mezcla dos collations explícitas (error 468). `COLLATE DATABASE_DEFAULT` usa la de la base donde corre la consulta. Una tabla temporal vive en `tempdb`, que toma la collation de la instancia: una columna sin `COLLATE` en una base con otra collation puede entrar en conflicto con las columnas de esa base. En (c), una tabla `##` pertenece a la sesión que la crea y se elimina cuando esa sesión termina y ninguna otra la está usando.

<!-- check: U2.15 -->

```sql
CREATE DATABASE AireCsAs COLLATE Latin1_General_100_CS_AS;
GO
CREATE DATABASE AireCiAi COLLATE Latin1_General_100_CI_AI;
GO

SELECT name, collation_name
FROM sys.databases
WHERE name IN ('AireCsAs', 'AireCiAi')
ORDER BY name;
GO

USE AireCsAs;
GO
CREATE TABLE dbo.Barrio (Nombre NVARCHAR(40) NOT NULL);
INSERT INTO dbo.Barrio (Nombre) VALUES (N'San José'), (N'Villa Ocampo');
GO

USE AireCiAi;
GO
CREATE TABLE dbo.Barrio (Nombre NVARCHAR(40) NOT NULL);
INSERT INTO dbo.Barrio (Nombre) VALUES (N'SAN JOSE'), (N'Villa Ocampo');
GO

-- Entre bases con distinta collation, el cruce falla (error 468) hasta que se fija la collation
BEGIN TRY
    EXEC (N'SELECT Nombre FROM AireCsAs.dbo.Barrio INTERSECT SELECT Nombre FROM AireCiAi.dbo.Barrio;');
END TRY
BEGIN CATCH
    SELECT 'cruce entre bases' AS Intento, ERROR_NUMBER() AS Error;
END CATCH;

SELECT Nombre COLLATE DATABASE_DEFAULT AS Nombre FROM AireCsAs.dbo.Barrio
INTERSECT
SELECT Nombre COLLATE DATABASE_DEFAULT FROM AireCiAi.dbo.Barrio
ORDER BY Nombre;

-- La columna de una tabla temporal toma la collation de tempdb, no la de la base actual
CREATE TABLE #Parcial (Nombre NVARCHAR(40) NOT NULL);
SELECT CAST(DATABASEPROPERTYEX('tempdb', 'Collation') AS VARCHAR(60)) AS CollationTempdb,
       CAST(DATABASEPROPERTYEX(DB_NAME(), 'Collation') AS VARCHAR(60)) AS CollationBaseActual,
       (SELECT collation_name FROM tempdb.sys.columns
        WHERE object_id = OBJECT_ID('tempdb..#Parcial') AND name = 'Nombre') AS CollationColumna;
DROP TABLE #Parcial;

CREATE TABLE #ParcialBase (Nombre NVARCHAR(40) COLLATE DATABASE_DEFAULT NOT NULL);
SELECT collation_name AS CollationColumna
FROM tempdb.sys.columns
WHERE object_id = OBJECT_ID('tempdb..#ParcialBase') AND name = 'Nombre';
DROP TABLE #ParcialBase;
GO

USE master;
GO
DROP DATABASE AireCsAs;
DROP DATABASE AireCiAi;
GO
```

Para (c), abrí dos ventanas de consulta conectadas a la misma instancia (dos conexiones independientes). Ejecutá cada paso en la ventana que indica el comentario; la sesión A es la ventana donde creás `##Compartida`, y «cerrar la sesión A» significa cerrar esa ventana o desconectarla:

<!-- check: U2.15 -->

```sql
-- Sesión A
CREATE TABLE ##Compartida (Estacion CHAR(3) NOT NULL);
INSERT INTO ##Compartida (Estacion) VALUES ('E01');

-- Sesión B (mientras A sigue abierta)
SELECT Estacion FROM ##Compartida;      -- devuelve una fila

-- Cerrá la sesión A y volvé a ejecutar en la sesión B
SELECT Estacion FROM ##Compartida;      -- error 208: el nombre de objeto no es válido
```

**Resultado esperado** de (a) y (b), obtenido con SQL Server 2022 (el nombre de la collation de la instancia depende de cómo esté instalada):

| name | collation_name |
|---|---|
| AireCiAi | Latin1_General_100_CI_AI |
| AireCsAs | Latin1_General_100_CS_AS |

| Intento | Error |
|---|---:|
| cruce entre bases | 468 |

| Nombre |
|---|
| San José |
| Villa Ocampo |

| CollationTempdb | CollationBaseActual | CollationColumna |
|---|---|---|
| SQL_Latin1_General_CP1_CI_AS | Latin1_General_100_CI_AI | SQL_Latin1_General_CP1_CI_AS |

| CollationColumna |
|---|
| Latin1_General_100_CI_AI |

**Explicación.** Con `COLLATE DATABASE_DEFAULT` la comparación se hace con la collation de la base activa (`CI_AI` en este caso), y `SAN JOSE` coincide con `San José`. La columna temporal sin `COLLATE` toma la de `tempdb`, distinta de la de la base: al compararla con columnas de la base daría el mismo error 468; con `COLLATE DATABASE_DEFAULT` se evita. La visibilidad de `##` entre sesiones y su eliminación al cerrarse la sesión creadora son comportamiento documentado de SQL Server; para observarlos hacen falta las dos conexiones del paso (c), cuyo resultado es el que indican los comentarios del bloque.

</details>

## Autoevaluación

<details>
<summary>¿Por qué `BULK INSERT` con `FORMAT = 'CSV'` falla en una línea truncada pero sin ese formato "funciona"?</summary>

Con `FORMAT = 'CSV'` el motor exige que cada línea tenga todos los campos y aborta ante una que no los tiene. Sin ese formato, solo cuenta terminadores: una línea corta se une con la siguiente, y la carga "funciona" con filas corruptas. Fallar es preferible a cargar datos corruptos.
</details>

<details>
<summary>¿Qué diferencia hay entre `#Parcial`, `##Parcial` y `@Parcial`?</summary>

`#Parcial` es de la sesión (y visible para lo que ella invoca), `##Parcial` es visible para todas las sesiones hasta que termina la que la creó y nadie más la usa, y `@Parcial` existe solo en el lote donde se declara. Ninguna admite una vista.
</details>

<details>
<summary>¿Por qué conviene reparar texto dañado con una comparación binaria?</summary>

Porque las collations insensibles a acentos consideran iguales caracteres distintos (`º` y `o`, `Ã` y `a`), y `REPLACE` puede modificar texto sano. La comparación binaria solo reemplaza la secuencia exacta.
</details>

:::tip[En resumen]
- La collation se hereda del servidor a la base y de esta a la columna, y se puede fijar por columna o por expresión con `COLLATE`; dos collations explícitas distintas dan el error 468.
- Un CSV se importa con `FORMAT = 'CSV'`, `FIRSTROW`, el separador y el terminador correctos, y los bytes sin convertir hacia una columna UTF-8.
- Se carga todo como texto, se valida con `TRY_CONVERT` y se separan las filas rechazadas con su motivo.
- El texto dañado se limpia con reemplazos de comparación binaria, antes y después verificados.
- Las temporales locales, globales y las variables de tabla tienen alcances distintos, y una vista no puede apoyarse en ninguna temporal.
- `PERCENTILE_CONT` interpola; `PERCENTILE_DISC` devuelve un valor de la serie.
:::

## Fuentes

- Documentación de Microsoft Learn de SQL Server: `BULK INSERT` (opciones `FORMAT`, `FIELDQUOTE`, `FIRSTROW`, `CODEPAGE`), collation y compatibilidad de Unicode, `COLLATE`, `PERCENTILE_CONT` y `PERCENTILE_DISC`, `CREATE TABLE` (tablas temporales), `TRY_CONVERT`.
- Presentaciones de cátedra de la Unidad 2 (collation, importación de datos y tablas temporales), como referencia de los temas; el enunciado, los datos, los archivos y los ejemplos de esta práctica son originales.
