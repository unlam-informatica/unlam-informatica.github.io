---
title: Métricas de rendimiento
slug: bbdd-aplicadas/unidad-3/teoria/metricas-de-rendimiento
sidebar:
  order: 5
---

[← Unidad 3](/bbdd-aplicadas/unidad-3/teoria/)

Un servidor "anda lento" cuando algo cambió respecto de cómo anda normalmente. Para saberlo hace falta medir antes: las **métricas de performance** describen cuánto se usa la base de datos y cuántos recursos consume, y sirven para dimensionar el servidor, resolver problemas, detectar *bugs* y anticipar el crecimiento. Esta página reúne las que propone la cátedra (recuento de filas, entrada/salida de archivos, tamaño del backup del log, esperas y bloqueos) y las vistas del sistema para obtenerlas. Cómo interpretar un plan está en [Plan de ejecución y estadísticas](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/) y cómo actuar sobre los índices en [Índices y optimización](/bbdd-aplicadas/unidad-3/teoria/indices-optimizacion/).

:::note[Qué presupone esta lección]
Consultas `SELECT` con `JOIN` ([Unidad 1](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/)) y la noción de archivos de datos y de log de [Unidad 2](/bbdd-aplicadas/unidad-2/teoria/bd-transaccionales/). Los ejemplos se ejecutaron en SQL Server 2022.
:::

## La línea de base

:::note[Definición]
Una **línea de base** (*baseline*) es el conjunto de métricas tomadas con el sistema funcionando con normalidad, discriminado por hora, día o período. Es la referencia que permite decir que un comportamiento es anómalo.
:::

Un valor suelto no dice nada: 500 lecturas por segundo pueden ser mucho o poco. Hay que conocer el sistema y su uso: ¿cuántas transacciones se hacen por hora?, ¿cuántas filas se agregan por día a la tabla de ventas?, ¿a qué ritmo crece la base?, ¿cuánto tarda normalmente una operación crítica? La métrica útil es la **variación** respecto de lo normal. Si una tabla de ventas recibe 5.000 filas por día y un día recibe 20 y otro 200.000, hay algo para investigar (un feriado, una promoción o un error).

Los datos se obtienen de las **vistas de administración dinámica** (DMV): `sys.dm_db_partition_stats` (filas y páginas por partición), `sys.dm_io_virtual_file_stats` (entrada y salida por archivo), `sys.dm_exec_query_stats` (consumo por consulta en caché), `sys.dm_os_wait_stats` (esperas acumuladas) y `sys.dm_os_performance_counters` (contadores). La mayoría acumula desde el último reinicio del servicio: lo que sirve para el baseline es la **diferencia entre dos mediciones**.

## Las métricas de la cátedra

| Métrica | Cómo se obtiene | Ventaja | Limitación |
|---|---|---|---|
| **Recuento de filas** (*row count*) | `sys.dm_db_partition_stats` o `COUNT(*)` | Fácil de medir y efectiva para aplicaciones orientadas a datos; se controla en valores absolutos, porcentajes o ambos | No informa sobre actualizaciones ni lecturas |
| **Entrada/salida de archivos** (*file IO*) | `sys.dm_io_virtual_file_stats` | Cuántos datos se leen y escriben en cada archivo de datos o de log; permite prever si el crecimiento será acompañado por almacenamiento, red y backup | Detecta un problema pero no señala qué tabla u objeto lo causa |
| **Tamaño del backup del log** | `msdb.dbo.backupset` | Se determina sin acceder a la base, solo con los backups; un crecimiento anormal marca más cambios | Solo en modelos `FULL` o `BULK_LOGGED`; resolución limitada por la frecuencia de los backups |
| **Esperas y bloqueos** (*waits*) | `sys.dm_exec_requests`, `sys.dm_os_wait_stats` | Una consulta lenta por esperar a otras apunta a una aplicación a depurar; se asocian a la sesión, al texto y al plan | Hay que muestrear repetidamente: la espera es un estado instantáneo |
| **Hardware y deadlocks** | `sys.dm_os_sys_info`, `sys.dm_os_performance_counters` | CPU, memoria, lecturas y escrituras; el contador de interbloqueos revela conflictos de diseño | Describen el servidor, no una consulta |

## Datos de ejemplo

<!-- check: U3.T.MT.00 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE SCHEMA monitoreo;
GO
CREATE TABLE ventas.Pedido (
    PedidoId  INT IDENTITY(1, 1) NOT NULL,
    ClienteId INT            NOT NULL,
    Estado    VARCHAR(10)    NOT NULL,
    Importe   DECIMAL(10, 2) NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId)
);
CREATE NONCLUSTERED INDEX IX_Pedido_ClienteId ON ventas.Pedido (ClienteId);
GO
WITH n AS (
    SELECT TOP (20000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_columns AS a
    CROSS JOIN sys.all_columns AS b
)
INSERT INTO ventas.Pedido (ClienteId, Estado, Importe)
SELECT n % 500 + 1,
       CASE WHEN n % 100 = 0 THEN 'Anulado' WHEN n % 10 = 0 THEN 'Pendiente' ELSE 'Entregado' END,
       n % 1000 + 0.50
FROM n;
GO
```

## Recuento de filas

`COUNT(*)` es exacto pero lee un índice completo, y cuanto más grande la tabla, mayor el impacto sobre el sistema (si no hay índices, recorre el heap con un *Table Scan*; con ellos, el más angosto disponible). `sys.dm_db_partition_stats` guarda el recuento como metadato de cada partición, sin leer la tabla: se suma `row_count` de las particiones del heap (`index_id = 0`) o del índice clúster (`index_id = 1`). No es un muestreo ni una estimación: es el contador que mantiene el motor, que en condiciones normales coincide con `COUNT(*)`; puede diferir momentáneamente bajo modificaciones concurrentes.

<!-- check: U3.T.MT.01 -->
```sql
SELECT s.name  AS Esquema,
       t.name  AS Tabla,
       SUM(ps.row_count) AS Filas
FROM sys.dm_db_partition_stats AS ps
INNER JOIN sys.tables  AS t ON t.object_id = ps.object_id
INNER JOIN sys.schemas AS s ON s.schema_id = t.schema_id
WHERE ps.index_id IN (0, 1)
GROUP BY s.name, t.name
ORDER BY s.name, t.name;

SELECT COUNT(*) AS FilasConCount FROM ventas.Pedido;
```

**Resultado esperado.**

| Esquema | Tabla | Filas |
|---|---|---:|
| ventas | Pedido | 20000 |

| FilasConCount |
|---:|
| 20000 |

El valor de la vista coincide con `COUNT(*)`, y la consulta lista todas las tablas de usuario de una vez. Filtrando `index_id IN (0, 1)` se evita sumar los índices no clúster, que tienen el mismo número de filas. Para detectar novedades entre muestreos también se puede filtrar por una columna de fecha de modificación: es más liviano que leer toda la tabla y más preciso que una vista de sistema.

## Entrada y salida de archivos

`sys.dm_io_virtual_file_stats(base, archivo)` acumula, **desde el último reinicio del servicio**, las lecturas y escrituras de cada archivo, con la cantidad de operaciones, los bytes y el tiempo de espera de E/S (`io_stall`). Al reiniciar el servicio se pone a cero, de modo que se guarda una *foto* y se calcula la diferencia con la siguiente. Ese patrón es el de un baseline: una tabla de historial y una consulta que mide el delta.

<!-- check: U3.T.MT.02 -->
```sql
CREATE TABLE monitoreo.LineaBaseArchivo (
    MedicionId     INT IDENTITY(1, 1) NOT NULL,
    Momento        DATETIME2          NOT NULL CONSTRAINT DF_LineaBaseArchivo_Momento DEFAULT (SYSDATETIME()),
    ArchivoId      INT                NOT NULL,
    Tipo           VARCHAR(10)        NOT NULL,
    Escrituras     BIGINT             NOT NULL,
    BytesEscritos  BIGINT             NOT NULL,
    CONSTRAINT PK_LineaBaseArchivo PRIMARY KEY CLUSTERED (MedicionId)
);
GO
-- Foto inicial:
INSERT INTO monitoreo.LineaBaseArchivo (ArchivoId, Tipo, Escrituras, BytesEscritos)
SELECT vfs.file_id, mf.type_desc, vfs.num_of_writes, vfs.num_of_bytes_written
FROM sys.dm_io_virtual_file_stats(DB_ID(), NULL) AS vfs
INNER JOIN sys.master_files AS mf
    ON mf.database_id = vfs.database_id AND mf.file_id = vfs.file_id;

-- Actividad: se actualizan 10.000 pedidos.
UPDATE ventas.Pedido SET Importe = Importe + 1 WHERE PedidoId <= 10000;

-- Foto final:
INSERT INTO monitoreo.LineaBaseArchivo (ArchivoId, Tipo, Escrituras, BytesEscritos)
SELECT vfs.file_id, mf.type_desc, vfs.num_of_writes, vfs.num_of_bytes_written
FROM sys.dm_io_virtual_file_stats(DB_ID(), NULL) AS vfs
INNER JOIN sys.master_files AS mf
    ON mf.database_id = vfs.database_id AND mf.file_id = vfs.file_id;
GO
SELECT a.Tipo,
       CASE WHEN b.Escrituras    > a.Escrituras    THEN 'sí' ELSE 'no' END AS AumentaronEscrituras,
       CASE WHEN b.BytesEscritos > a.BytesEscritos THEN 'sí' ELSE 'no' END AS AumentaronBytes
FROM monitoreo.LineaBaseArchivo AS a
INNER JOIN monitoreo.LineaBaseArchivo AS b
    ON b.ArchivoId = a.ArchivoId AND b.MedicionId > a.MedicionId
WHERE a.Tipo = 'LOG';
```

**Resultado esperado.**

| Tipo | AumentaronEscrituras | AumentaronBytes |
|---|---|---|
| LOG | sí | sí |

El archivo de log registró escrituras nuevas durante la actividad. Los **valores absolutos** (cuántas escrituras, cuántos bytes) dependen del equipo, el momento y la caché, y por eso no los mostramos: lo que se compara contra el baseline es el delta por franja horaria. En el archivo de datos, las escrituras pueden aparecer después, cuando el *checkpoint* vuelca las páginas modificadas. Esta métrica sirve para detectar que algo cambió y para prever si el crecimiento de la base acompañará al almacenamiento, la red y los backups; **no** dice qué tabla o consulta lo causó.

## Consumo por consulta y esperas acumuladas

`sys.dm_exec_query_stats` resume, por sentencia en caché, cuántas veces se ejecutó y cuánto consumió; es la vista para encontrar las consultas más costosas (y, al ver la frecuencia, las que más pesan en total). Las esperas del servidor se acumulan en `sys.dm_os_wait_stats`, por tipo de espera.

<!-- check: U3.T.MT.03 -->
```sql
DECLARE @N INT;
SELECT @N = COUNT(*) FROM ventas.Pedido WHERE ClienteId = 7 /*M1*/ OPTION (MAXDOP 1);
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM ventas.Pedido WHERE ClienteId = 7 /*M1*/ OPTION (MAXDOP 1);
GO
DECLARE @N INT;
SELECT @N = COUNT(*) FROM ventas.Pedido WHERE ClienteId = 7 /*M1*/ OPTION (MAXDOP 1);
GO
SELECT SUM(qs.execution_count)                             AS Ejecuciones,
       SUM(qs.total_logical_reads) / SUM(qs.execution_count) AS LecturasPorEjecucion,
       CASE WHEN SUM(qs.total_worker_time) > 0 THEN 'sí' ELSE 'no' END AS ConsumioCpu
FROM sys.dm_exec_query_stats AS qs
CROSS APPLY sys.dm_exec_plan_attributes(qs.plan_handle) AS pa
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) AS t
WHERE pa.attribute = 'dbid' AND CAST(pa.value AS INT) = DB_ID()
  AND t.text LIKE N'%DECLARE @N INT;%/*M1*/%OPTION (MAXDOP 1);%'
  AND t.text NOT LIKE N'%dm_exec_query_stats%';

SELECT COUNT(*) AS ColumnasDeEsperas
FROM sys.all_columns
WHERE object_id = OBJECT_ID('sys.dm_os_wait_stats')
  AND name IN ('wait_type', 'waiting_tasks_count', 'wait_time_ms', 'signal_wait_time_ms');
```

**Resultado esperado.**

| Ejecuciones | LecturasPorEjecucion | ConsumioCpu |
|---:|---:|---|
| 3 | 2 | sí |

| ColumnasDeEsperas |
|---:|
| 4 |

La sentencia se ejecutó tres veces (se suman las entradas porque cada lote con texto distinto genera la suya) y cada ejecución leyó 2 páginas (una búsqueda en el índice por `ClienteId`). En un servidor real se ordena por `total_logical_reads`, `total_worker_time` o `total_elapsed_time` para ver las consultas que más pesan, y se mira `execution_count` para no confundir una consulta lenta y rara con una rápida y muy frecuente. `sys.dm_os_wait_stats` cuenta cuántas veces esperó cada tipo (`waiting_tasks_count`), cuánto esperó en total (`wait_time_ms`) y cuánto de eso fue esperar CPU (`signal_wait_time_ms`); como acumula desde el arranque, se toma una foto y se compara con otra, igual que con los archivos. Interpretar cada tipo de espera (por ejemplo, de disco o de bloqueos) se amplía en [Concurrencia, bloqueos y transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/).

## Modelo de recuperación

El **modelo de recuperación** es una propiedad de la base de datos que controla cómo se mantiene el registro de transacciones: cuándo se registra, si es obligatorio respaldarlo y qué restauraciones están disponibles. Hay tres, y se puede cambiar en cualquier momento:

| | `SIMPLE` | `FULL` | `BULK_LOGGED` |
|---|---|---|---|
| **Backup del log** | No existe | Necesario | Necesario |
| **Liberación del log** | Al completarse las transacciones (con el *checkpoint*) | Al respaldarlo; si no se respalda crece sin límite | Al respaldarlo |
| **Restauración** | Solo a un backup completo o diferencial | A cualquier punto en el tiempo | A un punto en el tiempo, salvo en intervalos con operaciones masivas |
| **Cargas masivas** | Registro mínimo | Se registran completas | Registro mínimo de ciertas operaciones masivas (`BULK INSERT`, `SELECT INTO`, creación de índices) |
| **No admite** | AlwaysOn, *mirroring*, *log shipping*, restauración a un punto en el tiempo | | |
| **Uso típico** | Desarrollo, bases no críticas | Producción | Cargas masivas temporales dentro de una base `FULL` |

`BULK_LOGGED` reduce el volumen de log en cargas masivas a cambio de perder la restauración a un punto en el tiempo dentro del intervalo afectado. El detalle de cómo funcionan el log, los checkpoints y los backups está en [Registro de transacciones y modelos de recuperación](/bbdd-aplicadas/unidad-5/teoria/log-recuperacion/) y en [Backups y restauración](/bbdd-aplicadas/unidad-5/teoria/backup-restauracion/) (Unidad 5). Para esta página importa el modelo porque determina qué métricas existen: sin backups de log no hay tamaño de backup de log que medir. Una base nueva hereda el modelo de `model` (en esta instancia, `FULL`), y se cambia con `ALTER DATABASE`:

<!-- check: U3.T.MT.04 -->
```sql
SELECT 'Inicial' AS Momento, recovery_model_desc AS Modelo
FROM sys.databases WHERE name = DB_NAME();

ALTER DATABASE CURRENT SET RECOVERY BULK_LOGGED;
SELECT 'Tras BULK_LOGGED' AS Momento, recovery_model_desc AS Modelo
FROM sys.databases WHERE name = DB_NAME();

ALTER DATABASE CURRENT SET RECOVERY SIMPLE;
SELECT 'Tras SIMPLE' AS Momento, recovery_model_desc AS Modelo
FROM sys.databases WHERE name = DB_NAME();
```

**Resultado esperado.**

| Momento | Modelo |
|---|---|
| Inicial | FULL |
| Tras BULK_LOGGED | BULK_LOGGED |
| Tras SIMPLE | SIMPLE |

### Tamaño del backup del log

En `FULL` o `BULK_LOGGED`, los cambios en la base se reflejan en el tamaño de los backups del log. Si se toman cada hora y tienen un tamaño habitual, un crecimiento anormal indica una situación a investigar. La ventaja es que se determina **sin acceder a la base**, solo con los backups. `msdb` guarda el historial de cada backup en `dbo.backupset` (tipo `D` = completo, `L` = log) con su tamaño y duración. La retención del historial depende del mantenimiento de `msdb` (`sp_delete_backuphistory`). La ruta de los archivos del ejemplo es del servidor de la instancia: reemplazala por una propia.

<!-- check: U3.T.MT.05 -->
```sql
DECLARE @Base SYSNAME = DB_NAME();
DECLARE @Sql  NVARCHAR(MAX);

SET @Sql = N'BACKUP DATABASE ' + QUOTENAME(@Base) + N' TO DISK = N''/var/opt/mssql/data/u3_metricas.bak'' WITH INIT;';
EXEC (@Sql);

INSERT INTO ventas.Pedido (ClienteId, Estado, Importe) VALUES (1, 'Pendiente', 99.00);

SET @Sql = N'BACKUP LOG ' + QUOTENAME(@Base) + N' TO DISK = N''/var/opt/mssql/data/u3_metricas.trn'' WITH INIT;';
EXEC (@Sql);

SELECT bs.type AS Tipo,
       CASE WHEN bs.backup_size > 0 THEN 'sí' ELSE 'no' END AS TieneTamano,
       bs.recovery_model AS Modelo
FROM msdb.dbo.backupset AS bs
WHERE bs.database_name = @Base
ORDER BY bs.backup_set_id;
```

**Resultado esperado.**

| Tipo | TieneTamano | Modelo |
|---|---|---|
| D | sí | FULL |
| L | sí | FULL |

Con la columna `backup_size` (en bytes) se arma la serie histórica: por ejemplo, `CAST(bs.backup_size / 1048576.0 AS DECIMAL(18, 2))` en megabytes, y `bs.backup_finish_date - bs.backup_start_date` para la duración. Para saber cuántos cambios generó una operación, `sys.dm_tran_database_transactions` informa los registros de log de la transacción abierta. La cátedra señala que un `UPDATE` que fija el mismo valor que ya tenía la fila igual genera entradas en el log. Lo probamos con una transacción que se revierte:

<!-- check: U3.T.MT.06 -->
```sql
BEGIN TRANSACTION;
UPDATE ventas.Pedido SET Estado = Estado WHERE ClienteId = 7;
SELECT 'Mismo valor' AS Caso, database_transaction_log_record_count AS RegistrosDeLog
FROM sys.dm_tran_database_transactions
WHERE transaction_id = (SELECT transaction_id FROM sys.dm_tran_current_transaction)
  AND database_id = DB_ID();
ROLLBACK;

BEGIN TRANSACTION;
UPDATE ventas.Pedido SET Importe = Importe + 1 WHERE ClienteId = 7;
SELECT 'Valor nuevo' AS Caso, database_transaction_log_record_count AS RegistrosDeLog
FROM sys.dm_tran_database_transactions
WHERE transaction_id = (SELECT transaction_id FROM sys.dm_tran_current_transaction)
  AND database_id = DB_ID();
ROLLBACK;
```

**Resultado esperado.**

| Caso | RegistrosDeLog |
|---|---:|
| Mismo valor | 1 |
| Valor nuevo | 41 |

En SQL Server 2022 y con esta tabla (sin triggers, replicación ni otras opciones), el `UPDATE` que no cambia el valor registra un único registro de log (el inicio de la transacción) y **no** las 40 filas, mientras que el que cambia el importe registra 41. La afirmación de la cátedra, entonces, no se cumple en este caso: el motor detecta que la fila no cambia y no la modifica. Puede variar con otras configuraciones (triggers, captura de datos modificados, columnas de distinto tipo), por lo que conviene medir antes de asumir en cualquiera de los dos sentidos.

## Esperas y bloqueos activos

`sys.dm_exec_requests` muestra, por cada solicitud en curso, si está esperando (`wait_type`, `wait_time`, `wait_resource`) y quién la bloquea (`blocking_session_id`, que vale `0` cuando nadie). Combinada con `sys.dm_exec_sessions` (usuario, programa, equipo) y `sys.dm_exec_sql_text` (la sentencia) permite ver qué espera, por qué y qué ejecuta. La consulta sigue el esquema de la cátedra; la variable `@SoloMiSesion` permite probarla sin ver las demás sesiones del servidor:

<!-- check: U3.T.MT.07 -->
```sql
DECLARE @SoloMiSesion BIT = 1;   -- 0 = todas las sesiones de usuario

SELECT r.session_id           AS SesionId,
       r.blocking_session_id  AS BloqueadaPor,
       DB_NAME(r.database_id) AS BaseDeDatos,
       r.wait_time            AS EsperaMs,
       r.wait_type            AS TipoDeEspera,
       r.command              AS Comando,
       s.login_name           AS Usuario,
       SUBSTRING(t.text, r.statement_start_offset / 2 + 1,
                 (CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.text)
                  ELSE r.statement_end_offset END - r.statement_start_offset) / 2 + 1) AS Sentencia
INTO #EsperasActivas
FROM sys.dm_exec_requests AS r
INNER JOIN sys.dm_exec_sessions AS s ON s.session_id = r.session_id
OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) AS t
WHERE s.is_user_process = 1
  AND (@SoloMiSesion = 0 OR r.session_id = @@SPID);

SELECT COUNT(*) AS Solicitudes,
       MAX(BloqueadaPor) AS BloqueadaPor,
       MAX(Comando) AS Comando
FROM #EsperasActivas;
```

**Resultado esperado.**

| Solicitudes | BloqueadaPor | Comando |
|---:|---:|---|
| 1 | 0 | SELECT INTO |

Con una sola sesión hay una solicitud (la propia consulta, un `SELECT`) y nadie la bloquea. En un sistema real se filtra por un umbral de `wait_time`, por `blocking_session_id <> 0`, se excluyen los procesos que no interesan (`command` de backup, `wait_type` benignos) y se muestrea repetidamente, porque la espera es un estado instantáneo. Las esperas pueden asociarse al identificador de sesión, al texto de la consulta y al plan en XML (`sys.dm_exec_query_plan(r.plan_handle)`), lo que las vuelve muy útiles cuando hay que investigar más. Producir un bloqueo requiere dos sesiones y se practica en el [laboratorio de niveles de aislamiento](/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento/).

## Hardware y deadlocks

La cátedra incluye entre las métricas las estadísticas de hardware (consumo de CPU, memoria, lecturas y escrituras) y los *deadlocks*. Algunas fuentes:

<!-- check: U3.T.MT.08 -->
```sql
SELECT CASE WHEN cpu_count > 0 THEN 'sí' ELSE 'no' END               AS TieneNucleos,
       CASE WHEN physical_memory_kb > 0 THEN 'sí' ELSE 'no' END      AS TieneMemoria
FROM sys.dm_os_sys_info;

SELECT RTRIM(counter_name) AS Contador, RTRIM(instance_name) AS Instancia
FROM sys.dm_os_performance_counters
WHERE counter_name LIKE N'Number of Deadlocks/sec%'
  AND instance_name = N'_Total';
```

**Resultado esperado.**

| TieneNucleos | TieneMemoria |
|---|---|
| sí | sí |

| Contador | Instancia |
|---|---|
| Number of Deadlocks/sec | _Total |

`sys.dm_os_sys_info` informa los núcleos y la memoria del equipo; `sys.dm_os_performance_counters` expone los contadores de rendimiento de SQL Server, entre ellos los interbloqueos por segundo (acumulado, hay que comparar dos fotos) y, por ejemplo, las solicitudes de lote por segundo. Los deadlocks también quedan registrados en la sesión de eventos `system_health`.

## Activity Monitor

El **Monitor de actividad** de SSMS (clic derecho sobre la instancia, *Activity Monitor*) es el "ECG de SQL Server": un panel en tiempo real que se actualiza cada pocos segundos y que resume, en gráficos y listas, lo que las DMV exponen por separado. Muestra el tiempo de procesador (% *Processor Time*), las tareas en espera (*Waiting Tasks*), la E/S de la base de datos (*Database I/O*) y las solicitudes por lote por segundo (*Batch Requests/sec*), y debajo, paneles expandibles:

| Panel | Qué muestra | Se corresponde con |
|---|---|---|
| **Processes** | Sesiones activas, qué ejecutan, bloqueos | `sys.dm_exec_sessions`, `sys.dm_exec_requests` |
| **Resource Waits** | Esperas por categoría | `sys.dm_os_wait_stats` |
| **Data File I/O** | Lecturas y escrituras por archivo de datos y de log, con el tiempo de respuesta | `sys.dm_io_virtual_file_stats` |
| **Recent Expensive Queries** / **Active Expensive Queries** | Las consultas más costosas de la historia reciente y las que se ejecutan ahora | `sys.dm_exec_query_stats`, `sys.dm_exec_requests` |

Sirve para un diagnóstico puntual y en vivo, pero no guarda historia: no es un baseline.

## Cómo obtener y analizar las métricas

1. **Ejecución manual de scripts.** Útil para un diagnóstico puntual; sin historial no constituye un baseline.
2. **Trabajos programados.** Un trabajo del Agente de SQL Server ejecuta los scripts periódicamente y guarda los resultados en tablas de historial (como `monitoreo.LineaBaseArchivo`).
3. **Avisos y paneles.** Envío de correo ante un umbral, o un tablero personalizado sobre las tablas de historial para ver tendencias.
4. **Software especializado de terceros.** Herramientas de monitoreo que almacenan el historial y comparan contra la línea de base.

Los valores fuera de lo normal pueden indicar problemas a resolver; la comparación siempre es contra el baseline.

:::caution[Errores frecuentes]
- **Tomar un valor instantáneo como diagnóstico.** `sys.dm_io_virtual_file_stats` y `sys.dm_os_wait_stats` acumulan desde el reinicio: sin una segunda foto, el número no significa nada.
- **Hacer `COUNT(*)` periódico sobre tablas enormes** para medir el crecimiento. Es costoso: se usa `sys.dm_db_partition_stats` (sumando `index_id` 0 y 1) o una columna de fecha.
- **Sumar todas las filas de `sys.dm_db_partition_stats`.** Con índices no clúster o particiones, el total se duplica; hay que filtrar por `index_id IN (0, 1)` y agrupar por tabla.
- **Esperar que el tamaño del backup del log exista en `SIMPLE`.** En ese modelo no hay backups de log.
- **Confiar en `sys.dm_db_index_usage_stats` o en los contadores tras un reinicio.** Se ponen a cero con el servicio.
:::

## Autoevaluación

<details>
<summary>1. ¿Por qué la cantidad de lecturas del archivo de datos, por sí sola, no permite decidir si hay un problema?</summary>

Porque la vista acumula desde el reinicio y no hay referencia: hay que comparar la diferencia entre dos fotos contra el comportamiento normal (línea de base) para esa franja horaria.
</details>

<details>
<summary>2. ¿Qué dos limitaciones tiene la métrica de entrada/salida de archivos?</summary>

Sirve para detectar que hay un problema pero no para saber qué tabla u objeto lo causa, y los valores dependen del equipo y se reinician con el servicio.
</details>

<details>
<summary>3. ¿Qué ventaja tiene medir el tamaño de los backups del log, y en qué modelos de recuperación se puede?</summary>

Se puede medir sin acceder a la base, solo con el historial de los backups, y un crecimiento anormal revela más cambios. Requiere `FULL` o `BULK_LOGGED`; en `SIMPLE` no hay backups de log.
</details>

<details>
<summary>4. ¿Qué indica <code>blocking_session_id</code> distinto de cero en <code>sys.dm_exec_requests</code>?</summary>

Que la solicitud está esperando a la sesión con ese identificador, que mantiene un bloqueo sobre el recurso que necesita.
</details>

:::tip[En resumen]
- Sin línea de base no se puede decir qué es anormal: se mide la variación.
- Las métricas de la cátedra: recuento de filas, E/S de archivos, tamaño del backup del log, esperas y bloqueos, más hardware y deadlocks.
- Las DMV acumulan desde el reinicio: se toma una foto, se espera y se calcula la diferencia.
- `SIMPLE`, `FULL` y `BULK_LOGGED` determinan qué se puede respaldar y restaurar; el desarrollo está en la Unidad 5.
- El Monitor de actividad es el panel en vivo de las mismas DMV; el historial se arma con trabajos programados o herramientas de terceros.
:::

:::tip[Para seguir]
Practicá con los ejercicios 5 y 19 de la [Práctica de rendimiento](/bbdd-aplicadas/unidad-3/practica/rendimiento/).
:::

## Fuentes

- Presentación de cátedra, Unidad 3, parte 2 (v1.0, 2023): monitoreo y métricas de performance.
- Microsoft Learn: [Modelos de recuperación](https://learn.microsoft.com/es-es/sql/relational-databases/backup-restore/recovery-models-sql-server), `sys.dm_db_partition_stats`, `sys.dm_io_virtual_file_stats`, `sys.dm_exec_query_stats`, `sys.dm_os_wait_stats`, `sys.dm_exec_requests` y [Monitor de actividad](https://learn.microsoft.com/es-es/sql/relational-databases/performance-monitor/open-activity-monitor-sql-server-management-studio).
