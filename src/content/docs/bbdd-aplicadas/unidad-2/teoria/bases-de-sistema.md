---
title: Bases de datos de sistema y de usuario
slug: bbdd-aplicadas/unidad-2/teoria/bases-de-sistema
sidebar:
  order: 2
---

[← Unidad 2](/bbdd-aplicadas/unidad-2/teoria/)

Cuando se instala SQL Server, la instancia ya trae un conjunto de bases de datos que el propio motor necesita para funcionar. Saber qué guarda cada una, cuáles no se tocan y por qué una de ellas (`tempdb`) condiciona el almacenamiento es parte de la instalación y de la administración de un motor: lo que importa es qué hace cada una y cómo planificar su ubicación. Los ejemplos se ejecutan sobre SQL Server 2022.

## Bases de sistema y bases de usuario

:::note[Definición]
Las **bases de datos de sistema** son las que crea la instalación y el motor usa para su operación: catálogo de la instancia, plantilla de bases nuevas, tareas programadas y espacio temporal. Las **bases de datos de usuario** son las que se crean para guardar los datos de una aplicación.
:::

| Base | Para qué sirve | Qué no hacer |
|---|---|---|
| `master` | Es el catálogo de la instancia: inicios de sesión, configuración, la lista de bases de datos y la ubicación de sus archivos. Sin ella la instancia no arranca. | No guardar objetos propios; no operar sin un respaldo reciente. |
| `model` | Es la **plantilla** de toda base de usuario nueva. | No agregarle objetos sin querer que se copien a cada base y a `tempdb`. |
| `msdb` | La usa SQL Server Agent: trabajos programados (_jobs_), alertas, y el historial de respaldos y restauraciones. | No borrar el historial a ciegas. |
| `tempdb` | Espacio temporal compartido por toda la instancia: tablas temporales, variables de tabla, ordenamientos y resultados intermedios. Se vuelve a crear cada vez que se inicia el servicio. | No guardar datos que deban persistir. |
| `mssqlsystemresource` (_resource_) | Base de solo lectura y oculta con el código y los objetos de sistema que vienen con el motor. | No intentar abrirla ni modificarla. |

Las cuatro primeras se ven en `sys.databases`. La base de recursos no se lista ahí:

<!-- check: U2.T.BDS.01 -->
```sql
SELECT name AS BaseDeDatos, database_id AS Id
FROM sys.databases
WHERE database_id <= 4
ORDER BY database_id;

SELECT
    CASE WHEN DB_ID() > 4 THEN 'usuario' ELSE 'sistema' END AS BaseActual,
    ISNULL(CAST(DB_ID(N'mssqlsystemresource') AS VARCHAR(10)), 'NULL') AS IdBaseDeRecursos;
```

| BaseDeDatos | Id |
|---|---:|
| master | 1 |
| tempdb | 2 |
| model | 3 |
| msdb | 4 |

| BaseActual | IdBaseDeRecursos |
|---|---|
| usuario | NULL |

Las bases de usuario reciben identificadores desde el 5. `DB_ID(N'mssqlsystemresource')` devuelve `NULL`: el motor la usa, pero no se puede consultar como una base común.

## Los archivos de cada base

Cada base de sistema tiene sus archivos de datos y de log, como cualquier otra. `sys.master_files` los lista para toda la instancia:

<!-- check: U2.T.BDS.02 -->
```sql
SELECT
    DB_NAME(database_id) AS BaseDeDatos,
    name                 AS NombreLogico,
    type_desc            AS Tipo
FROM sys.master_files
WHERE database_id IN (1, 3, 4)
ORDER BY database_id, file_id;

SELECT
    CASE WHEN SUM(CASE WHEN type_desc = 'ROWS' THEN 1 ELSE 0 END) >= 1 THEN 'sí' ELSE 'no' END AS TieneArchivosDeDatos,
    SUM(CASE WHEN type_desc = 'LOG'  THEN 1 ELSE 0 END)       AS ArchivosDeLog
FROM sys.master_files
WHERE database_id = 2;
```

| BaseDeDatos | NombreLogico | Tipo |
|---|---|---|
| master | master | ROWS |
| master | mastlog | LOG |
| model | modeldev | ROWS |
| model | modellog | LOG |
| msdb | MSDBData | ROWS |
| msdb | MSDBLog | LOG |

| TieneArchivosDeDatos | ArchivosDeLog |
|---|---:|
| sí | 1 |

De `tempdb` no listamos los archivos de datos porque su cantidad depende de la instalación: el instalador puede crear varios según los núcleos de CPU.

## `model` es la plantilla

Al ejecutar `CREATE DATABASE`, el motor copia `model` y le cambia el nombre. Por eso la base nueva hereda sus propiedades: intercalación, modelo de recuperación, nivel de compatibilidad, tamaño y crecimiento inicial de los archivos, y los objetos que `model` tuviera. El script siguiente se ejecuta en una base recién creada y la compara con `model`:

<!-- check: U2.T.BDS.03 -->
```sql
SELECT
    p.Propiedad,
    p.Modelo,
    p.BaseNueva,
    CASE WHEN p.Modelo = p.BaseNueva THEN 'sí' ELSE 'no' END AS Coincide
FROM (
    SELECT 1 AS Orden, N'Intercalación' COLLATE DATABASE_DEFAULT AS Propiedad,
           CAST(m.collation_name AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT AS Modelo, CAST(n.collation_name AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT AS BaseNueva
    FROM sys.databases AS m CROSS JOIN sys.databases AS n
    WHERE m.name = N'model' AND n.database_id = DB_ID()
    UNION ALL
    SELECT 2, N'Modelo de recuperación', CAST(m.recovery_model_desc AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT, CAST(n.recovery_model_desc AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT
    FROM sys.databases AS m CROSS JOIN sys.databases AS n
    WHERE m.name = N'model' AND n.database_id = DB_ID()
    UNION ALL
    SELECT 3, N'Nivel de compatibilidad', CAST(m.compatibility_level AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT, CAST(n.compatibility_level AS NVARCHAR(128)) COLLATE DATABASE_DEFAULT
    FROM sys.databases AS m CROSS JOIN sys.databases AS n
    WHERE m.name = N'model' AND n.database_id = DB_ID()
) AS p
ORDER BY p.Orden;
```

| Propiedad | Modelo | BaseNueva | Coincide |
|---|---|---|---|
| Intercalación | SQL_Latin1_General_CP1_CI_AS | SQL_Latin1_General_CP1_CI_AS | sí |
| Modelo de recuperación | FULL | FULL | sí |
| Nivel de compatibilidad | 160 | 160 | sí |

El `COLLATE DATABASE_DEFAULT` es necesario porque las vistas de catálogo y la base actual pueden tener intercalaciones distintas (ver [collation](/bbdd-aplicadas/unidad-2/teoria/collation/#conflictos-entre-intercalaciones)). Los valores concretos dependen de la instalación.

:::caution[`model` también afecta a `tempdb`]
Como `tempdb` se recrea en cada inicio a partir de `model`, un objeto agregado a `model` aparece en `tempdb` después de reiniciar. Modificar `model` es una decisión de administración con efecto en todas las bases futuras: no es un lugar para pruebas.
:::

## `tempdb`: qué guarda y cómo planificarlo

Toda tabla temporal (`#t`, `##t`) y toda tabla de variable (`@t`) vive en `tempdb`, igual que los ordenamientos y las operaciones intermedias que no entran en memoria. Se comparte entre todas las sesiones de la instancia y se recrea en cada inicio, vacía. Por eso su rendimiento afecta a todas las bases, y por eso la cátedra pide para ella el almacenamiento más rápido y planificar su ubicación y su parámetro de crecimiento.

<!-- check: U2.T.BDS.04 -->
```sql
CREATE TABLE #PedidoBds (
    PedidoId INT           NOT NULL PRIMARY KEY,
    Total    DECIMAL(10,2) NOT NULL
);
INSERT #PedidoBds (PedidoId, Total) VALUES (1, 100.00), (2, 250.50);

SELECT
    LEFT(t.name, 10)                         AS Tabla,
    CASE WHEN EXISTS (SELECT 1 FROM sys.tables WHERE name LIKE N'#PedidoBds%') THEN 'sí' ELSE 'no' END AS EnBaseActual,
    d.recovery_model_desc                    AS ModeloDeRecuperacionDeTempdb
FROM tempdb.sys.tables AS t
CROSS JOIN sys.databases AS d
WHERE t.object_id = OBJECT_ID(N'tempdb..#PedidoBds')
  AND d.name = N'tempdb';
```

| Tabla | EnBaseActual | ModeloDeRecuperacionDeTempdb |
|---|---|---|
| #PedidoBds | no | SIMPLE |

La tabla está en `tempdb` y no en la base actual. `tempdb` usa el modelo de recuperación `SIMPLE` porque sus datos no se recuperan después de un reinicio.

Criterios de planificación:

- **Ubicación.** En almacenamiento rápido (la cátedra dice «rapidísimo»), separado de los discos de las bases de usuario si es posible.
- **Tamaño y crecimiento.** Dimensionar el tamaño inicial para la carga esperada y fijar un crecimiento por incrementos de tamaño fijo, de modo que no crezca muchas veces pequeño ni llene el disco.
- **Cantidad de archivos.** Puede tener varios archivos de datos; el instalador propone una cantidad según los núcleos.
- **Intercalación.** `tempdb` toma la de la instancia, no la de la base de usuario: puede causar conflictos al comparar columnas con tablas temporales ([ver el caso](/bbdd-aplicadas/unidad-2/teoria/collation/#conflictos-entre-intercalaciones)).

## Qué no tocar

- No guardar objetos de aplicación en `master`, `model`, `msdb` ni `tempdb`.
- No borrar ni mover archivos de las bases de sistema sin seguir el procedimiento documentado.
- Respaldar `master` y `msdb`: sin ellas se pierden los inicios de sesión, la configuración y los trabajos programados.
- Dejar que las bases de usuario crezcan fuera de la partición del sistema.

:::caution[Errores frecuentes]
- Crear tablas de aplicación en `master` porque «ya estaba seleccionada» (`USE` olvidado).
- Esperar que una tabla temporal sobreviva al cierre de la sesión, o que los datos de `tempdb` persistan tras un reinicio.
- Suponer que `sys.databases` muestra todas las bases de sistema: la de recursos no aparece.
:::

## Autoevaluación

**1. ¿Qué pasa con una tabla creada en `tempdb` después de reiniciar el servicio?**

<details>
<summary>Respuesta</summary>

Desaparece: `tempdb` se recrea vacía a partir de `model` en cada inicio. Por eso no se guardan allí datos persistentes.
</details>

**2. Se crea una base nueva con `CREATE DATABASE` sin opciones. ¿De dónde salen su intercalación y el tamaño de sus archivos?**

<details>
<summary>Respuesta</summary>

De `model`, que es la plantilla de las bases de usuario.
</details>

## Ejercicios

### Ejercicio 48 · Modelo de recuperación de las bases de sistema
<!-- ejercicio: U2.48 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Listá las cuatro bases de sistema visibles con su identificador y su modelo de recuperación. ¿Cuál es la diferencia con las bases de usuario nuevas?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `sys.databases` tiene `recovery_model_desc`. Las bases de sistema son las de `database_id` del 1 al 4.

<!-- check: U2.48 -->
```sql
SELECT name AS BaseDeDatos, database_id AS Id, recovery_model_desc AS ModeloDeRecuperacion
FROM sys.databases
WHERE database_id <= 4
ORDER BY database_id;
```

**Resultado esperado.**

| BaseDeDatos | Id | ModeloDeRecuperacion |
|---|---:|---|
| master | 1 | SIMPLE |
| tempdb | 2 | SIMPLE |
| model | 3 | FULL |
| msdb | 4 | SIMPLE |

`model` tiene el modelo `FULL`, y una base de usuario nueva lo hereda (`FULL`), mientras que `master`, `msdb` y `tempdb` usan `SIMPLE`. Una base nueva nace con `FULL` porque es el de la plantilla, no porque sea el de las demás bases de sistema.
</details>

### Ejercicio 49 · La base nueva nace con el tamaño de `model`
<!-- ejercicio: U2.49 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Comprobá, para el archivo de datos y el de log, si la base actual (recién creada) tiene el mismo tamaño y el mismo crecimiento que los archivos de `model`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se cruzan `sys.master_files` (filtrada a `model`) con `sys.database_files` (la base actual) por tipo de archivo, y se comparan `size`, `growth` e `is_percent_growth`.

<!-- check: U2.49 -->
```sql
SELECT
    mf.type_desc AS Tipo,
    CASE WHEN mf.size = f.size THEN 'sí' ELSE 'no' END AS MismoTamanio,
    CASE WHEN mf.growth = f.growth AND mf.is_percent_growth = f.is_percent_growth THEN 'sí' ELSE 'no' END AS MismoCrecimiento
FROM sys.master_files AS mf
INNER JOIN sys.database_files AS f
    ON f.type = mf.type
WHERE mf.database_id = DB_ID(N'model')
ORDER BY mf.type;
```

**Resultado esperado.**

| Tipo | MismoTamanio | MismoCrecimiento |
|---|---|---|
| ROWS | sí | sí |
| LOG | sí | sí |

La base nueva copia el tamaño y el crecimiento de `model`. Si se hubiera agrandado `model`, todas las bases nuevas nacerían más grandes. La comparación solo es cierta si al crear la base no se indicaron tamaños propios.
</details>

:::tip[En resumen]
- Las bases de sistema son `master` (catálogo), `model` (plantilla), `msdb` (Agent y respaldos), `tempdb` (espacio temporal) y la base de recursos (oculta, de solo lectura).
- Toda base de usuario nueva es una copia de `model`.
- `tempdb` se recrea en cada inicio y la comparten todas las sesiones: se planifica con almacenamiento rápido y crecimiento controlado.
- Respaldá `master` y `msdb`, y no guardes objetos de aplicación en las bases de sistema.
:::

## Fuentes

- Presentación de cátedra, Unidad 2, parte 1: aspectos clave de la instalación (ubicación de bases de usuario, de sistema y temporal).
- Microsoft Learn, documentación de SQL Server: [bases de datos del sistema](https://learn.microsoft.com/es-es/sql/relational-databases/databases/system-databases) y [base de datos tempdb](https://learn.microsoft.com/es-es/sql/relational-databases/databases/tempdb-database).
