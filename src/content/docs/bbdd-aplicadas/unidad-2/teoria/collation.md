---
title: Collation / Intercalación
slug: bbdd-aplicadas/unidad-2/teoria/collation
sidebar:
  order: 3
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

La **intercalación** (_collation_) decide cómo se guardan, comparan y ordenan los textos. Es una propiedad que se elige al instalar y que, mal configurada, produce comparaciones que no funcionan como se pensó o directamente errores. Los resultados se obtuvieron con SQL Server 2022; los ejemplos se ejecutan en una base de práctica (ver [Cómo estudiar · Antes de ejecutar los ejemplos](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos)).

:::note[Definición]
La intercalación determina dos cosas: **cómo se representan los caracteres** (qué patrón de bits o página de códigos corresponde a cada uno) y **cómo se comparan y ordenan** (si `'a'` y `'A'` son iguales, si `'a'` y `'á'` son iguales, y en qué orden aparecen con `ORDER BY`).
:::

## Nomenclatura

El nombre sigue el patrón `Idioma_Sensibilidades`. Por ejemplo, `Modern_Spanish_CI_AI` es español moderno, insensible a mayúsculas y a acentos.

| Código | Significado | Efecto |
|---|---|---|
| `CI` | _Case insensitive_ | `'a'` = `'A'` |
| `CS` | _Case sensitive_ | `'a'` ≠ `'A'` |
| `AI` | _Accent insensitive_ | `'a'` = `'á'` |
| `AS` | _Accent sensitive_ | `'a'` ≠ `'á'` |
| `KS` | _Kana sensitive_ | distingue Hiragana de Katakana (idiomas asiáticos) |
| `WS` | _Width sensitive_ | distingue caracteres de ancho completo y medio |
| `BIN`, `BIN2` | Binarias | comparan por el valor binario del carácter, sin reglas de idioma |
| `UTF8` | Sufijo | usa UTF-8 como codificación (SQL Server 2019 o posterior) |

La intercalación predeterminada depende de la configuración regional del sistema donde se instala. `SQL_Latin1_General_CP1_CI_AS` corresponde a la configuración en inglés de Estados Unidos; con otra región el instalador propone otra. La cátedra señala que elegirla es un punto crítico del despliegue.

## Niveles

```
Instancia      → base de sistema y valor por defecto de las bases nuevas
  └── Base de datos → valor por defecto de las tablas y columnas nuevas
        └── Columna → puede fijar la suya propia
```

Una tabla o columna nueva que no indica intercalación toma la de la base de datos. Se consulta en cada nivel:

<!-- check: U2.T.COL.01 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Producto (
    ProductoId  INT          NOT NULL PRIMARY KEY,
    Codigo      VARCHAR(20)  COLLATE Latin1_General_CS_AS NOT NULL,
    Descripcion VARCHAR(100) NOT NULL
);

SELECT Nivel, Intercalacion
FROM (
    SELECT 1 AS Orden, 'instancia' AS Nivel, CAST(SERVERPROPERTY('Collation') AS NVARCHAR(128)) AS Intercalacion
    UNION ALL
    SELECT 2, 'base de datos', collation_name
    FROM sys.databases
    WHERE database_id = DB_ID()
    UNION ALL
    SELECT 3, 'columna ' + name, collation_name
    FROM sys.columns
    WHERE object_id = OBJECT_ID(N'ventas.Producto') AND collation_name IS NOT NULL
) AS n
ORDER BY Orden, Nivel;
```

| Nivel | Intercalacion |
|---|---|
| instancia | SQL_Latin1_General_CP1_CI_AS |
| base de datos | SQL_Latin1_General_CP1_CI_AS |
| columna Codigo | Latin1_General_CS_AS |
| columna Descripcion | SQL_Latin1_General_CP1_CI_AS |

`Descripcion` heredó la de la base; `Codigo` la fijó la columna. Para definirla en otros niveles:

<!-- sintaxis -->
```sql
CREATE DATABASE <NombreBase> COLLATE <Intercalacion>;

ALTER TABLE <esquema>.<Tabla>
    ALTER COLUMN <Columna> VARCHAR(20) COLLATE <Intercalacion> NOT NULL;
```

:::caution[Cambiar la de una columna]
Cambiar la intercalación de una columna con índices o restricciones que la referencian falla: hay que eliminarlos y recrearlos. Cambiar la de la **instancia** es una operación avanzada y de alto riesgo (se reconstruyen las bases de sistema), que no se hace en producción sin planificación.
:::

## Cláusula `COLLATE` en una consulta

Se puede forzar la intercalación en una expresión sin tocar la definición de la tabla. La misma búsqueda de `'juan'` da resultados distintos según la sensibilidad:

<!-- check: U2.T.COL.02 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL PRIMARY KEY,
    Nombre    VARCHAR(30) NOT NULL
);
INSERT ventas.Cliente (ClienteId, Nombre)
VALUES (1, 'Juan'), (2, 'juan'), (3, 'JUAN'), (4, 'juán'), (5, 'Julia');

SELECT Intercalacion, Coincidencias
FROM (
    SELECT 1 AS Orden, 'Modern_Spanish_CI_AS' AS Intercalacion, COUNT(*) AS Coincidencias
    FROM ventas.Cliente WHERE Nombre = 'juan' COLLATE Modern_Spanish_CI_AS
    UNION ALL
    SELECT 2, 'Modern_Spanish_CI_AI', COUNT(*)
    FROM ventas.Cliente WHERE Nombre = 'juan' COLLATE Modern_Spanish_CI_AI
    UNION ALL
    SELECT 3, 'Modern_Spanish_CS_AS', COUNT(*)
    FROM ventas.Cliente WHERE Nombre = 'juan' COLLATE Modern_Spanish_CS_AS
    UNION ALL
    SELECT 4, 'Modern_Spanish_CS_AI', COUNT(*)
    FROM ventas.Cliente WHERE Nombre = 'juan' COLLATE Modern_Spanish_CS_AI
) AS r
ORDER BY Orden;
```

| Intercalacion | Coincidencias |
|---|---:|
| Modern_Spanish_CI_AS | 3 |
| Modern_Spanish_CI_AI | 4 |
| Modern_Spanish_CS_AS | 1 |
| Modern_Spanish_CS_AI | 2 |

`CI_AS` ignora las mayúsculas (`Juan`, `juan`, `JUAN`) pero distingue `juán`; `CI_AI` iguala los cuatro; `CS_AS` solo encuentra la cadena exacta y `CS_AI` encuentra `juan` y `juán`.

## Orden: diccionario y binario

`ORDER BY` también obedece a la intercalación. Las binarias ordenan por el código del carácter (todas las mayúsculas antes que las minúsculas); las de diccionario, por las reglas del idioma.

<!-- check: U2.T.COL.03 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Etiqueta (Texto VARCHAR(10) NOT NULL);
INSERT ventas.Etiqueta (Texto) VALUES ('a'), ('B'), ('C'), ('d');

SELECT
    'Latin1_General_CI_AS' AS Intercalacion,
    STRING_AGG(Texto, ' ') WITHIN GROUP (ORDER BY Texto COLLATE Latin1_General_CI_AS) AS Orden
FROM ventas.Etiqueta
UNION ALL
SELECT
    'Latin1_General_BIN2',
    STRING_AGG(Texto, ' ') WITHIN GROUP (ORDER BY Texto COLLATE Latin1_General_BIN2)
FROM ventas.Etiqueta;
```

| Intercalacion | Orden |
|---|---|
| Latin1_General_CI_AS | a B C d |
| Latin1_General_BIN2 | B C a d |

Las binarias son las más rápidas y exactas, pero no respetan acentos ni mayúsculas al ordenar. Se usan cuando se quiere una comparación literal (por ejemplo, para códigos técnicos). `BIN2` es la binaria recomendada frente a la antigua `BIN`.

## Conflictos entre intercalaciones

Cuando una comparación, un `JOIN`, un `UNION`, `INTERSECT` o `EXCEPT` combina columnas con intercalaciones distintas, el motor no sabe cuál aplicar y lanza el **error 468** («Cannot resolve the collation conflict»). El conflicto aparece con frecuencia entre una tabla de la base y una **tabla temporal**: las temporales viven en `tempdb`, que usa la intercalación de la **instancia** y no la de la base de datos de trabajo.

Se reproduce con una base cuya intercalación difiere de la de la instancia. El primer comando del bloque siguiente, `ALTER DATABASE CURRENT COLLATE`, cambia la intercalación de la base actual y necesita acceso exclusivo a ella: ejecutalo solo en una base de práctica. La tabla de resultados que sigue supone una instancia con `SQL_Latin1_General_CP1_CI_AS`; si la tuya usa otra, el segundo renglón y la presencia del conflicto pueden cambiar. La solución es `COLLATE DATABASE_DEFAULT`, que traduce la expresión a la intercalación de la base actual (`CATALOG_DEFAULT` hace lo mismo con la del catálogo):

<!-- check: U2.T.COL.04 -->
```sql
ALTER DATABASE CURRENT COLLATE Modern_Spanish_CI_AS;
GO
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL PRIMARY KEY,
    Nombre    VARCHAR(30) NOT NULL
);
INSERT ventas.Cliente (ClienteId, Nombre) VALUES (1, 'Ana'), (2, 'ANA'), (3, 'Luis');

-- Las tablas temporales viven en tempdb, que usa la intercalación de la instancia.
CREATE TABLE #Excluido (Nombre VARCHAR(30) NOT NULL);
INSERT #Excluido (Nombre) VALUES ('ana');

CREATE TABLE #Resultado (Orden INT NOT NULL, Caso VARCHAR(50) NOT NULL, Resultado VARCHAR(60) NOT NULL);

INSERT #Resultado
SELECT 1, 'ventas.Cliente.Nombre', collation_name
FROM sys.columns WHERE object_id = OBJECT_ID(N'ventas.Cliente') AND name = N'Nombre';
INSERT #Resultado
SELECT 2, '#Excluido.Nombre', collation_name
FROM tempdb.sys.columns WHERE object_id = OBJECT_ID(N'tempdb..#Excluido') AND name = N'Nombre';

BEGIN TRY
    EXEC (N'SELECT c.ClienteId FROM ventas.Cliente AS c INNER JOIN #Excluido AS e ON e.Nombre = c.Nombre');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (3, 'JOIN sin COLLATE', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;
BEGIN TRY
    EXEC (N'SELECT Nombre FROM ventas.Cliente UNION SELECT Nombre FROM #Excluido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (4, 'UNION sin COLLATE', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;
BEGIN TRY
    EXEC (N'SELECT Nombre FROM ventas.Cliente INTERSECT SELECT Nombre FROM #Excluido');
END TRY
BEGIN CATCH
    INSERT #Resultado VALUES (5, 'INTERSECT sin COLLATE', 'error ' + CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;

INSERT #Resultado
SELECT 6, 'JOIN con DATABASE_DEFAULT', CAST(COUNT(*) AS VARCHAR(10)) + ' fila(s)'
FROM ventas.Cliente AS c
INNER JOIN #Excluido AS e
    ON e.Nombre COLLATE DATABASE_DEFAULT = c.Nombre;
INSERT #Resultado
SELECT 7, 'INTERSECT con DATABASE_DEFAULT', CAST(COUNT(*) AS VARCHAR(10)) + ' fila(s)'
FROM (
    SELECT Nombre FROM ventas.Cliente
    INTERSECT
    SELECT Nombre COLLATE DATABASE_DEFAULT FROM #Excluido
) AS i;

SELECT Caso, Resultado
FROM #Resultado
ORDER BY Orden;
```

| Caso | Resultado |
|---|---|
| ventas.Cliente.Nombre | Modern_Spanish_CI_AS |
| #Excluido.Nombre | SQL_Latin1_General_CP1_CI_AS |
| JOIN sin COLLATE | error 468 |
| UNION sin COLLATE | error 468 |
| INTERSECT sin COLLATE | error 468 |
| JOIN con DATABASE_DEFAULT | 2 fila(s) |
| INTERSECT con DATABASE_DEFAULT | 1 fila(s) |

Los `EXEC` están porque el error 468 se produce al compilar la sentencia: sin ejecutarla como texto, el `TRY...CATCH` del mismo lote no alcanza a capturarlo. En una instalación donde la base y la instancia comparten intercalación, el conflicto no se ve, y por eso es un error que aparece recién al pasar de un entorno a otro.

Otra forma de evitarlo es crear la tabla temporal con la intercalación de la base: `CREATE TABLE #T (Col VARCHAR(20) COLLATE DATABASE_DEFAULT)`. Y para comparar columnas de bases distintas, la cátedra recomienda hacer explícita la intercalación con el sufijo `COLLATE` (por ejemplo, `WHERE campo1 = campo2 COLLATE Modern_Spanish_CS_AI`).

## Intercalaciones UTF-8

Desde SQL Server 2019 existen intercalaciones con sufijo `_UTF8`: permiten guardar texto Unicode en columnas `VARCHAR` y `CHAR` con UTF-8 (página de códigos 65001), en lugar de usar `NVARCHAR`.

<!-- check: U2.T.COL.05 -->
```sql
SELECT
    'Latin1_General_CI_AS'               AS Intercalacion,
    COLLATIONPROPERTY('Latin1_General_CI_AS', 'CodePage') AS PaginaDeCodigos
UNION ALL
SELECT
    'Latin1_General_100_CI_AS_SC_UTF8',
    COLLATIONPROPERTY('Latin1_General_100_CI_AS_SC_UTF8', 'CodePage');
```

| Intercalacion | PaginaDeCodigos |
|---|---:|
| Latin1_General_CI_AS | 1252 |
| Latin1_General_100_CI_AS_SC_UTF8 | 65001 |

## Qué intercalación elegir

No hay una única recomendación; depende del uso:

| Situación | Criterio |
|---|---|
| Búsquedas en español para usuarios finales | Una `CI_AI` evita que el usuario deba acertar mayúsculas y tildes |
| Códigos o identificadores donde la diferencia importa | `CS_AS` o binaria (`BIN2`) |
| Comparaciones literales, sin reglas de idioma | Binaria (`BIN2`) |
| Datos de varios idiomas | Considerar `NVARCHAR` o una intercalación UTF-8 |
| Bases que se van a comparar o unir | Usar la misma en todas, para evitar conflictos |

:::caution[Errores frecuentes]
- Suponer que la intercalación de la base es la de la instancia: `ALTER DATABASE ... COLLATE` la cambia sin tocar la instancia.
- Comparar con una tabla temporal sin tener en cuenta que usa la intercalación de `tempdb`.
- Cambiar la intercalación de una columna indexada sin eliminar antes el índice.
- Pasar un script de un entorno a otro con intercalaciones distintas: el error 468 aparece en el destino.
:::

## Autoevaluación

**1. ¿De dónde toma su intercalación una tabla temporal `#T`?**

<details>
<summary>Respuesta</summary>

De `tempdb`, que usa la de la instancia, y no de la base desde la que se crea.
</details>

**2. ¿Qué diferencia hay entre `CI_AI` y `CS_AS` al comparar `'Ana'` con `'ána'`?**

<details>
<summary>Respuesta</summary>

Con `CI_AI` son iguales (ignora mayúsculas y acentos); con `CS_AS` son distintas.
</details>

## Ejercicios

### Ejercicio 50 · Una columna sensible a mayúsculas y otra que no
<!-- ejercicio: U2.50 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Una tabla de artículos tiene `Codigo` con intercalación `Latin1_General_CS_AS` y `Etiqueta` con `Latin1_General_CI_AS`. Se cargan tres filas cuyo valor es `ab-1`, `AB-1` y `Ab-1` en ambas columnas. Contá cuántas filas encuentra el filtro `= 'ab-1'` en cada columna.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada columna aplica su propia intercalación en la comparación: la `CS` solo encuentra la cadena exacta y la `CI`, las tres variantes.

<!-- check: U2.50 -->
```sql
CREATE SCHEMA inventario;
GO
CREATE TABLE inventario.Articulo (
    ArticuloId INT         NOT NULL PRIMARY KEY,
    Codigo     VARCHAR(10) COLLATE Latin1_General_CS_AS NOT NULL,
    Etiqueta   VARCHAR(10) COLLATE Latin1_General_CI_AS NOT NULL
);
INSERT inventario.Articulo (ArticuloId, Codigo, Etiqueta)
VALUES (1, 'ab-1', 'ab-1'), (2, 'AB-1', 'AB-1'), (3, 'Ab-1', 'Ab-1');

SELECT
    (SELECT COUNT(*) FROM inventario.Articulo WHERE Codigo   = 'ab-1') AS PorCodigo,
    (SELECT COUNT(*) FROM inventario.Articulo WHERE Etiqueta = 'ab-1') AS PorEtiqueta;
```

**Resultado esperado.**

| PorCodigo | PorEtiqueta |
|---:|---:|
| 1 | 3 |

El literal `'ab-1'` no tiene intercalación propia (toma la de la columna), así que cada comparación usa la de su columna.
</details>

### Ejercicio 51 · La ñ y el orden
<!-- ejercicio: U2.51 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con las palabras `cano`, `caña`, `cana` y `canal`, mostrá el orden que devuelven `Modern_Spanish_CI_AS` y `Latin1_General_CI_AS`. ¿En qué se diferencian?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se concatena cada lista con `STRING_AGG` ordenando con una `COLLATE` distinta en cada consulta.

<!-- check: U2.51 -->
```sql
CREATE SCHEMA diccionario;
GO
CREATE TABLE diccionario.Palabra (Texto VARCHAR(10) NOT NULL);
INSERT diccionario.Palabra (Texto) VALUES ('cano'), ('caña'), ('cana'), ('canal');

SELECT 'Modern_Spanish_CI_AS' AS Intercalacion,
       STRING_AGG(Texto, ' ') WITHIN GROUP (ORDER BY Texto COLLATE Modern_Spanish_CI_AS) AS Orden
FROM diccionario.Palabra
UNION ALL
SELECT 'Latin1_General_CI_AS',
       STRING_AGG(Texto, ' ') WITHIN GROUP (ORDER BY Texto COLLATE Latin1_General_CI_AS)
FROM diccionario.Palabra;
```

**Resultado esperado.**

| Intercalacion | Orden |
|---|---|
| Modern_Spanish_CI_AS | cana canal cano caña |
| Latin1_General_CI_AS | cana caña canal cano |

El español moderno trata la `ñ` como una letra propia, posterior a la `n`, así que `caña` va al final. La intercalación general la trata como una `n` con diacrítico y la ubica junto a `cana`.
</details>

### Ejercicio 52 · Una temporal sin conflictos
<!-- ejercicio: U2.52 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
En una base de práctica con intercalación `Modern_Spanish_CI_AS` (distinta de la de la instancia, que se supone `SQL_Latin1_General_CP1_CI_AS`; el bloque de la resolución la cambia con `ALTER DATABASE CURRENT`), un procedimiento compara una tabla de productos con una tabla temporal de rubros activos y falla con el error 468. Reescribí la creación de la tabla temporal para que la comparación funcione sin tocar el `JOIN`, y comprobá la intercalación resultante.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El error se debe a que la columna de la temporal toma la intercalación de `tempdb`. Se declara la columna con `COLLATE DATABASE_DEFAULT`: queda con la de la base y el `JOIN` no cambia.

<!-- check: U2.52 -->
```sql
ALTER DATABASE CURRENT COLLATE Modern_Spanish_CI_AS;
GO
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Producto (
    ProductoId INT         NOT NULL PRIMARY KEY,
    Rubro      VARCHAR(20) NOT NULL
);
INSERT ventas.Producto (ProductoId, Rubro) VALUES (1, 'Limpieza'), (2, 'Bazar'), (3, 'LIMPIEZA');

-- Sin COLLATE, esta tabla usaría la intercalación de tempdb y la comparación daría el error 468.
CREATE TABLE #RubroActivo (Rubro VARCHAR(20) COLLATE DATABASE_DEFAULT NOT NULL);
INSERT #RubroActivo (Rubro) VALUES ('limpieza');

SELECT
    p.ProductoId,
    p.Rubro,
    (SELECT collation_name FROM tempdb.sys.columns
     WHERE object_id = OBJECT_ID(N'tempdb..#RubroActivo') AND name = N'Rubro') AS IntercalacionTemporal
FROM ventas.Producto AS p
INNER JOIN #RubroActivo AS r
    ON r.Rubro = p.Rubro
ORDER BY p.ProductoId;
```

**Resultado esperado.**

| ProductoId | Rubro | IntercalacionTemporal |
|---:|---|---|
| 1 | Limpieza | Modern_Spanish_CI_AS |
| 3 | LIMPIEZA | Modern_Spanish_CI_AS |

La comparación es insensible a mayúsculas (`CI`) y devuelve las dos filas de «limpieza». La solución en el origen evita repetir `COLLATE` en cada consulta que use la tabla.
</details>

:::tip[En resumen]
- La intercalación define cómo se comparan y ordenan los textos; se hereda de la instancia a la base y de la base a la columna.
- `CI/CS` y `AI/AS` controlan mayúsculas y acentos; las `BIN2` comparan por código.
- Combinar columnas con intercalaciones distintas da el error 468 en `JOIN`, `UNION`, `INTERSECT` y `EXCEPT`; se resuelve con `COLLATE`, por ejemplo `DATABASE_DEFAULT`.
- Las tablas temporales usan la intercalación de `tempdb`, que es la de la instancia.
- Desde SQL Server 2019 hay intercalaciones UTF-8.
:::

:::tip[Para seguir]
Las collations se aplican en el [Trabajo práctico 2](/bbdd-aplicadas/unidad-2/practica/tp2/) (ejercicios 1, 2, 3, 9, 11, 12 y 15), que conviene resolver después de ver la importación de archivos. Seguí con [BD en memoria](/bbdd-aplicadas/unidad-2/teoria/bd-en-memoria/).
:::

## Fuentes

- Presentación de cátedra, Unidad 2, parte 1: intercalación (patrón de bits, sensibilidades, comparación entre bases con `COLLATE`).
- Microsoft Learn, documentación de SQL Server: [compatibilidad con la intercalación y Unicode](https://learn.microsoft.com/es-es/sql/relational-databases/collations/collation-and-unicode-support) y [cláusula COLLATE](https://learn.microsoft.com/es-es/sql/t-sql/statements/collations).
