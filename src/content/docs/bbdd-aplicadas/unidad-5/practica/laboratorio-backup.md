---
title: Laboratorio — Cadena de backup y restauración
slug: bbdd-aplicadas/unidad-5/practica/laboratorio-backup
sidebar:
  order: 2
---

[← Unidad 5](/bbdd-aplicadas/unidad-5/teoria/)

Este laboratorio produce una cadena completo, log, diferencial y log, y recupera otra base hasta un punto anterior a un error. Presupone [el registro de transacciones y los modelos de recuperación](/bbdd-aplicadas/unidad-5/teoria/log-recuperacion/), [backups y restauración](/bbdd-aplicadas/unidad-5/teoria/backup-restauracion/) y [alta disponibilidad](/bbdd-aplicadas/unidad-5/teoria/alta-disponibilidad/). Después del laboratorio hay 17 ejercicios resueltos.

:::caution[No usar sobre una base real]
No uses `WITH REPLACE` sobre una base real. Trabajá con `LaboratorioBackup` (la base de origen) y restaurá como `LaboratorioBackup_Restore`.
:::

## Rutas: Windows y Linux

La **cuenta del servicio de SQL Server** debe poder escribir en las carpetas de backup y de datos. Usá estas rutas según tu instalación:

| Elemento | SQL Server en Windows | SQL Server en Linux o contenedor |
|---|---|---|
| Carpeta de backups | `D:\SQLBackups\` | `/var/opt/mssql/backup/` |
| Carpeta de datos de la base restaurada | `D:\SQLData\` | `/var/opt/mssql/data/` |

En los bloques se muestran las rutas de Windows; reemplazalas por las de Linux si corresponde (por ejemplo, `'/var/opt/mssql/backup/LB_full.bak'`). `COMPRESSION` no existe en todas las ediciones (por ejemplo, no en Express): si falla, quitala. En Linux, el directorio de backups tiene que existir y pertenecer al usuario `mssql`.

## Cómo se verificó

El portal ejecutó este laboratorio completo en una instancia de prueba (SQL Server 2022). Para que el resultado no dependa del reloj, el error lógico se marca con una transacción `WITH MARK` y la restauración se detiene con `STOPBEFOREMARK`. En el paso 8 también se muestra la alternativa con `STOPAT`.

## 1. Preparar la base y el modelo FULL

La base es autocontenida: no depende de otros laboratorios.

<!-- check: U5.LB.R1 -->
```sql
USE master;
GO
CREATE DATABASE LaboratorioBackup;
GO
ALTER DATABASE LaboratorioBackup SET RECOVERY FULL;
GO
USE LaboratorioBackup;
GO
CREATE SCHEMA respaldo;
GO
CREATE TABLE respaldo.Pedido (
    PedidoId  INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Pedido PRIMARY KEY,
    ClienteId INT           NOT NULL,
    Importe   DECIMAL(10,2) NOT NULL,
    Estado    VARCHAR(20)   NOT NULL
);
GO
INSERT respaldo.Pedido (ClienteId, Importe, Estado) VALUES (1, 50, 'P0_EN_FULL');
GO
SELECT name, recovery_model_desc, log_reuse_wait_desc
FROM sys.databases
WHERE name = 'LaboratorioBackup';
```

La fila `P0_EN_FULL` se inserta **antes** del backup completo. Los nombres de los estados indican en qué backup queda cada fila: `P0_EN_FULL` en el completo, `P1_EN_LOG1` en el primer log, `P2_EN_DIFF` en el diferencial, `P3_EN_LOG2` en el segundo log.

## 2. Backup completo

<!-- check: U5.T.BK.13 -->
```sql
BACKUP DATABASE LaboratorioBackup
TO DISK = 'D:\SQLBackups\LB_full.bak'
WITH INIT, COMPRESSION, CHECKSUM, STATS = 10;
GO
USE LaboratorioBackup;
INSERT respaldo.Pedido (ClienteId, Importe, Estado) VALUES (1, 100, 'P1_EN_LOG1');
GO
```

## 3. Primer backup de log

<!-- check: U5.T.BK.13 -->
```sql
BACKUP LOG LaboratorioBackup
TO DISK = 'D:\SQLBackups\LB_log1.trn'
WITH INIT, COMPRESSION, CHECKSUM;
GO
USE LaboratorioBackup;
INSERT respaldo.Pedido (ClienteId, Importe, Estado) VALUES (1, 200, 'P2_EN_DIFF');
GO
```

## 4. Diferencial

<!-- check: U5.T.BK.13 -->
```sql
BACKUP DATABASE LaboratorioBackup
TO DISK = 'D:\SQLBackups\LB_diff.bak'
WITH DIFFERENTIAL, INIT, COMPRESSION, CHECKSUM;
GO
USE LaboratorioBackup;
INSERT respaldo.Pedido (ClienteId, Importe, Estado) VALUES (1, 300, 'P3_EN_LOG2');
GO
```

**Pregunta.** ¿El diferencial contiene `P1_EN_LOG1`, `P2_EN_DIFF`, ambos o ninguno? ¿Y `P0_EN_FULL`?

<details>
<summary>Respuesta</summary>

Contiene **ambos** `P1_EN_LOG1` y `P2_EN_DIFF`: el diferencial guarda todo lo modificado desde el completo (acumulativo), y las dos filas se insertaron después de él, aunque `P1_EN_LOG1` ya estuviera en el primer log. `P0_EN_FULL` no está en el diferencial: ya estaba en el completo.
</details>

## 5. Logs posteriores y error lógico

<!-- check: U5.T.BK.13 -->
```sql
BACKUP LOG LaboratorioBackup
TO DISK = 'D:\SQLBackups\LB_log2.trn'
WITH INIT, COMPRESSION, CHECKSUM;
GO
USE LaboratorioBackup;

-- El error: una actualización sin WHERE, en una transacción marcada
BEGIN TRANSACTION ErrorLogico WITH MARK 'actualizacion sin WHERE';
    UPDATE respaldo.Pedido SET Estado = 'ERROR_LOGICO';
COMMIT TRANSACTION;
GO

BACKUP LOG LaboratorioBackup
TO DISK = 'D:\SQLBackups\LB_log3.trn'
WITH INIT, COMPRESSION, CHECKSUM;
```

La marca queda registrada en el log, por lo que no hace falta anotar la hora a mano ni guardar el momento en una variable que se pierde con el `GO`. Si preferís trabajar con el reloj, guardá la hora del servidor en una tabla antes del error: `INSERT respaldo.Momento (Valor) VALUES (SYSDATETIME());`.

## 6. Inspección

<!-- check: U5.T.BK.10 -->
```sql
RESTORE HEADERONLY   FROM DISK = 'D:\SQLBackups\LB_full.bak';
RESTORE FILELISTONLY FROM DISK = 'D:\SQLBackups\LB_full.bak';
RESTORE VERIFYONLY   FROM DISK = 'D:\SQLBackups\LB_full.bak' WITH CHECKSUM;
```

Registrá:

- `FirstLSN`, `LastLSN`, `CheckpointLSN` y `DatabaseBackupLSN` del completo (de `HEADERONLY`);
- los nombres lógicos de datos y de log (de `FILELISTONLY`; son `LaboratorioBackup` y `LaboratorioBackup_log` si no los cambiaste);
- la diferencia entre verificar un archivo y demostrar una restauración.

El historial de lo que se respaldó también está en `msdb`. Resultado del verificador al ejecutar el laboratorio completo:

<!-- check: U5.T.BK.13 -->
```sql
SELECT ROW_NUMBER() OVER (ORDER BY b.backup_set_id) AS Orden,
       CASE b.type WHEN 'D' THEN 'Completo' WHEN 'I' THEN 'Diferencial' ELSE 'Log' END AS Tipo
FROM msdb.dbo.backupset AS b
WHERE b.database_name = 'LaboratorioBackup'
ORDER BY b.backup_set_id;
```

**Resultado esperado.**

| Orden | Tipo |
|---|---|
| 1 | Completo |
| 2 | Log |
| 3 | Diferencial |
| 4 | Log |
| 5 | Log |

## 7. Restaurar el completo y el diferencial

Reemplazá los nombres lógicos por los que obtuviste con `FILELISTONLY`:

<!-- check: U5.T.BK.13 -->
```sql
USE master;
GO
RESTORE DATABASE LaboratorioBackup_Restore
FROM DISK = 'D:\SQLBackups\LB_full.bak'
WITH
    MOVE 'LaboratorioBackup'     TO 'D:\SQLData\LaboratorioBackup_Restore.mdf',
    MOVE 'LaboratorioBackup_log' TO 'D:\SQLData\LaboratorioBackup_Restore.ldf',
    NORECOVERY,
    STATS = 10;
GO

RESTORE DATABASE LaboratorioBackup_Restore
FROM DISK = 'D:\SQLBackups\LB_diff.bak'
WITH NORECOVERY;
GO
```

**Pregunta.** ¿Por qué no hace falta restaurar `LB_log1.trn` si se aplicó el diferencial? ¿Qué logs sí hay que aplicar después?

<details>
<summary>Respuesta</summary>

El diferencial se tomó después del primer log y contiene todos los cambios desde el completo, así que `LB_log1.trn` ya está "incorporado". Los logs que siguen son los **posteriores al diferencial**: `LB_log2.trn` (cuyo rango de LSN cubre el LSN del diferencial) y `LB_log3.trn`. Se comprueba con los LSN que informa `HEADERONLY`.
</details>

## 8. Recuperar hasta antes del error

<!-- check: U5.T.BK.13 -->
```sql
RESTORE LOG LaboratorioBackup_Restore
FROM DISK = 'D:\SQLBackups\LB_log2.trn'
WITH NORECOVERY;
GO

RESTORE LOG LaboratorioBackup_Restore
FROM DISK = 'D:\SQLBackups\LB_log3.trn'
WITH STOPBEFOREMARK = 'ErrorLogico', RECOVERY;
GO
```

Alternativa con el reloj: en el último `RESTORE LOG`, reemplazar `STOPBEFOREMARK` por `STOPAT = '2026-07-22T14:37:00.000'`, con la hora (literal válido de fecha y hora, en la zona del servidor) anterior al error.

Validá:

<!-- check: U5.T.BK.13 -->
```sql
USE LaboratorioBackup_Restore;
SELECT PedidoId, Importe, Estado FROM respaldo.Pedido ORDER BY PedidoId;
DBCC CHECKDB('LaboratorioBackup_Restore') WITH NO_INFOMSGS;
```

**Resultado esperado.**

| PedidoId | Importe | Estado |
|---|---|---|
| 1 | 50.00 | P0_EN_FULL |
| 2 | 100.00 | P1_EN_LOG1 |
| 3 | 200.00 | P2_EN_DIFF |
| 4 | 300.00 | P3_EN_LOG2 |

`ERROR_LOGICO` no aparece y las cuatro operaciones anteriores sí. `DBCC CHECKDB ... WITH NO_INFOMSGS` no devuelve filas si la base es íntegra: la ausencia de salida es el resultado esperado.

## 9. Copy-only

<!-- check: U5.T.BK.04 -->
```sql
BACKUP DATABASE LaboratorioBackup
TO DISK = 'D:\SQLBackups\LB_copy_only.bak'
WITH COPY_ONLY, INIT, CHECKSUM;
```

Generá después otro diferencial y comprobá, con `RESTORE HEADERONLY` o con `msdb.dbo.backupset`, que su base (`DifferentialBaseLSN`) sigue siendo el completo convencional y no la copia.

## 10. Medición de RPO y RTO

Registrá:

| Métrica | Valor observado |
|---------|-----------------|
| Inicio del incidente simulado | |
| Último punto recuperado | |
| Pérdida temporal real (RPO observado) | |
| Inicio de la restauración | |
| Fin de la validación | |
| Tiempo total (RTO observado) | |

Proponé cambios para cumplir un RPO de 5 minutos y un RTO de 30 minutos con una base cien veces mayor (la resolución de referencia está en el ejercicio 31).

## Desafíos

1. Restaurar sin diferencial, con todos los logs desde el completo (ver ejercicio 26).
2. Provocar una transacción abierta y observar `ACTIVE_TRANSACTION` (ejercicio 37).
3. Comparar el tamaño y la duración con y sin `COMPRESSION`.
4. Diseñar la retención 3-2-1 con una copia inmutable.
5. Documentar un *runbook* que otra persona pueda ejecutar sin conocimiento previo.

## Ejercicios

Los ejercicios con código usan una base de prueba en modelo `FULL` con la tabla `dbo.Reserva (ReservaId INT IDENTITY, Concepto VARCHAR(20))`. Las restauraciones se hacen a una base nueva con `MOVE`, sin tocar la original. Las rutas son las de Windows; en Linux se reemplazan como se indicó arriba. El verificador del portal ejecuta cada resolución en una base descartable y con archivos propios del ejercicio.

---

### Ejercicio 21 · Verdadero o falso sobre el log
<!-- ejercicio: U5.21 | nivel: inicial | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Indicá si cada afirmación es verdadera o falsa y justificá.

1. Al hacer `COMMIT`, la página modificada ya fue escrita en el archivo `.mdf`.
2. Un `CHECKPOINT` hace un backup del log.
3. Truncar el log reduce el tamaño del archivo `.ldf`.
4. En el modelo `SIMPLE` se puede hacer `BACKUP LOG`.
5. En el modelo `FULL`, sin backups de log, el archivo de log puede crecer sin límite aparente.
6. Después de un corte de luz, la recuperación rehace (REDO) las transacciones confirmadas cuyas páginas no llegaron al disco.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada afirmación se contrasta con el principio de registro previo a la escritura y con la tabla de modelos de recuperación.

1. **Falso.** El `COMMIT` exige que el registro de confirmación esté en el log; la página sucia se escribe después (checkpoint, *lazy writer* o presión de memoria).
2. **Falso.** El checkpoint escribe páginas sucias al archivo de datos. No genera ninguna copia.
3. **Falso.** Truncar marca VLF como reutilizables; reducir el archivo requiere `DBCC SHRINKFILE`.
4. **Falso.** En `SIMPLE` el motor rechaza `BACKUP LOG` (error 4208) porque el checkpoint trunca solo.
5. **Verdadero.** Mientras no haya backups de log, `log_reuse_wait_desc` es `LOG_BACKUP` y el motor no reutiliza el espacio.
6. **Verdadero.** Es la fase REDO de la recuperación; las no confirmadas se deshacen (UNDO).
</details>

---

### Ejercicio 22 · RPO y RTO en tres escenarios
<!-- ejercicio: U5.22 | nivel: inicial | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Para cada escenario indicá si el dato dado es un RPO o un RTO y qué mecanismo lo condiciona más.

1. "La tienda en línea puede perder como máximo 5 minutos de pedidos."
2. "Si el servidor se cae, la facturación tiene que volver a andar en menos de una hora."
3. "El sistema de legajos admite perder un día de cambios y estar caído un día."
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El RPO se mide hacia atrás (cuántos datos), el RTO hacia adelante (cuánto tiempo de caída).

1. **RPO de 5 minutos.** Lo condiciona la frecuencia de los backups de log (como mucho cada 5 minutos) o una réplica casi síncrona.
2. **RTO de 1 hora.** Lo condicionan el tamaño de la base, la velocidad de restauración, la automatización del procedimiento y la existencia de un servidor alternativo listo. Un grupo de disponibilidad lo reduce mucho.
3. **RPO de un día y RTO de un día.** Alcanza un completo diario y una restauración manual documentada, sin backups de log.

Un RPO se cumple con la frecuencia de la copia; un RTO solo se demuestra con una restauración medida.
</details>

---

### Ejercicio 23 · ¿Por qué el log no se libera?
<!-- ejercicio: U5.23 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Una base `FULL` con un backup completo ya hecho recibe 20 000 filas y el archivo de log no se libera. Mostrá con `sys.databases` la causa antes y después de hacer un backup de log, y la situación antes del primer backup completo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `log_reuse_wait_desc` informa la causa de la no reutilización. Hace falta que el log ocupe más de un VLF para que se vea `LOG_BACKUP` (el VLF activo no se puede truncar).

<!-- check: U5.23 -->
```sql
ALTER DATABASE CURRENT SET RECOVERY FULL;

SELECT recovery_model_desc AS Modelo, log_reuse_wait_desc AS Espera      -- antes del primer full
FROM sys.databases WHERE database_id = DB_ID();

BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_23_full.bak' WITH INIT, CHECKSUM;

INSERT dbo.Reserva (Concepto)
SELECT TOP (20000) 'lote' FROM sys.all_objects AS a CROSS JOIN sys.all_objects AS b;
CHECKPOINT;

SELECT recovery_model_desc AS Modelo, log_reuse_wait_desc AS Espera      -- tras el full y los cambios
FROM sys.databases WHERE database_id = DB_ID();

BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_23_log.trn' WITH INIT, CHECKSUM;
CHECKPOINT;

SELECT recovery_model_desc AS Modelo, log_reuse_wait_desc AS Espera      -- tras el backup de log
FROM sys.databases WHERE database_id = DB_ID();
```

**Resultado esperado** (una fila por cada `SELECT`).

| Momento | Modelo | Espera |
|---|---|---|
| FULL sin ningún backup completo | FULL | NOTHING |
| Tras el full y un cambio | FULL | LOG_BACKUP |
| Tras el backup de log | FULL | NOTHING |

Antes del primer completo la base en `FULL` todavía no tiene cadena de log, por eso no espera nada. Después del completo, el log solo se libera con un backup de log, y eso es lo que cambia la última fila.
</details>

---

### Ejercicio 24 · Elegir la herramienta de alta disponibilidad
<!-- ejercicio: U5.24 | nivel: inicial | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Elegí entre grupo de disponibilidad, FCI, replicación y log shipping para cada caso y justificá en una línea.

1. Una sola base crítica con *failover* automático en el mismo centro de datos.
2. Un DR económico en otra ciudad; se acepta *failover* manual y perder unos minutos.
3. Las sucursales deben recibir solo la tabla `Producto` y las filas de su zona.
4. Proteger toda la instancia, incluidos los trabajos de SQL Server Agent y los inicios de sesión.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se identifica la unidad protegida (base, instancia, objetos) y el tipo de *failover*.

1. **Grupo de disponibilidad síncrono con modo automático**: protege la base y permite *failover* automático entre réplicas síncronas.
2. **Log shipping**: backups de log enviados y restaurados en la otra ciudad; es DR, el *failover* es manual y el RPO depende de la frecuencia.
3. **Replicación** (transaccional o de mezcla): permite artículos y filtros de filas y columnas.
4. **FCI**: conmuta la instancia completa, por lo que los trabajos y los inicios de sesión viajan con ella.
</details>

---

### Ejercicio 25 · ¿Esta instancia participa de un grupo de disponibilidad?
<!-- ejercicio: U5.25 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Sin instalar nada, escribí una consulta que diga si Always On está habilitado, si la instancia es de clúster y cuántos grupos y réplicas conoce.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `SERVERPROPERTY` informa si la función está habilitada (`IsHadrEnabled`) y si la instancia es de clúster (`IsClustered`); los catálogos `sys.availability_groups` y `sys.availability_replicas` listan lo configurado.

<!-- check: U5.25 -->
```sql
SELECT CASE WHEN SERVERPROPERTY('IsHadrEnabled') = 1 THEN 'Si' ELSE 'No' END AS AlwaysOnHabilitado,
       CASE WHEN SERVERPROPERTY('IsClustered') = 1 THEN 'Si' ELSE 'No' END AS InstanciaEnCluster,
       (SELECT COUNT(*) FROM sys.availability_groups) AS GruposDeDisponibilidad,
       (SELECT COUNT(*) FROM sys.availability_replicas) AS Replicas;
```

**Resultado esperado** (instancia aislada, sin Always On).

| AlwaysOnHabilitado | InstanciaEnCluster | GruposDeDisponibilidad | Replicas |
|---|---|---|---|
| No | No | 0 | 0 |

En un servidor que sí participa, la primera columna es `Si` y los catálogos muestran el grupo y sus réplicas.
</details>

---

### Ejercicio 26 · Qué restaurar con un diferencial en la cadena
<!-- ejercicio: U5.26 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Hay un completo, un primer log, un diferencial y un segundo log; en cada intervalo se insertó una fila. Restaurá, en otra base y con el **mínimo** de piezas, hasta el final de la cadena, y mostrá las filas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con diferencial, se restaura el completo, el diferencial y solo los logs posteriores a él. El primer log queda incorporado en el diferencial.

<!-- check: U5.26 -->
```sql
-- Cadena (en la base de prueba, cada INSERT precede al backup siguiente)
BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_26_full.bak' WITH INIT, CHECKSUM;
INSERT dbo.Reserva (Concepto) VALUES ('R1_EN_LOG');
BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_26_log1.trn' WITH INIT, CHECKSUM;
INSERT dbo.Reserva (Concepto) VALUES ('R2_EN_DIFF');
BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_26_diff.bak' WITH DIFFERENTIAL, INIT, CHECKSUM;
INSERT dbo.Reserva (Concepto) VALUES ('R3_EN_LOG2');
BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_26_log2.trn' WITH INIT, CHECKSUM;

-- Restauración mínima
RESTORE DATABASE LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_26_full.bak'
    WITH MOVE 'LaboratorioU5' TO 'D:\SQLData\LaboratorioU5_Rest.mdf',
         MOVE 'LaboratorioU5_log' TO 'D:\SQLData\LaboratorioU5_Rest.ldf', NORECOVERY;
RESTORE DATABASE LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_26_diff.bak' WITH NORECOVERY;
RESTORE LOG LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_26_log2.trn' WITH RECOVERY;

SELECT ReservaId, Concepto FROM LaboratorioU5_Rest.dbo.Reserva ORDER BY ReservaId;
```

**Resultado esperado.**

| ReservaId | Concepto |
|---|---|
| 1 | R1_EN_LOG |
| 2 | R2_EN_DIFF |
| 3 | R3_EN_LOG2 |

Las tres filas están: las dos primeras vienen del diferencial (acumulativo desde el completo) y la tercera del segundo log. Aplicar `U5_26_log1.trn` sería innecesario.
</details>

---

### Ejercicio 27 · Ordenar los pasos de una recuperación
<!-- ejercicio: U5.27 | nivel: intermedio | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Se borró una tabla a las 14:37 y hay que recuperar hasta las 14:36. Hay un completo del domingo, un diferencial del miércoles a las 03:00 y logs cada 15 minutos. Ordená los pasos correctos y señalá el paso que **no** corresponde.

- A. Restaurar el diferencial del miércoles con `NORECOVERY`.
- B. Ejecutar `DBCC CHECKDB` y las pruebas funcionales.
- C. Restaurar el completo del domingo con `RECOVERY`.
- D. Respaldar la cola del log (tail-log), si es posible.
- E. Restaurar el completo del domingo con `NORECOVERY`.
- F. Restaurar los logs posteriores al diferencial, en orden, con `NORECOVERY`, salvo el último con `STOPAT` a las 14:36 y `RECOVERY`.
- G. Confirmar el destino para no sobrescribir producción.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Primero se protege lo que falta (cola del log) y se confirma el destino; después se restaura la cadena en orden dejando todas las piezas abiertas salvo la última.

Orden correcto: **G, D, E, A, F, B**. El paso que no corresponde es **C**: restaurar el completo con `RECOVERY` pone la base en línea y cierra la secuencia, y ya no admite el diferencial ni los logs. En el examen alcanza con justificar así: *NORECOVERY en todo salvo en la última pieza*.
</details>

---

### Ejercicio 28 · El copy-only y la base de los diferenciales
<!-- ejercicio: U5.28 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Un compañero hace un completo ad hoc con `COPY_ONLY` entre el completo programado y el diferencial de la noche. ¿Cambia la base del diferencial? Demostralo con `msdb`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El historial `msdb.dbo.backupset` registra, por cada diferencial, el `differential_base_lsn`, que se compara con el `checkpoint_lsn` del completo no copy-only.

<!-- check: U5.28 -->
```sql
BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_28_full.bak' WITH INIT, CHECKSUM;
INSERT dbo.Reserva (Concepto) VALUES ('A');
BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_28_copia.bak' WITH COPY_ONLY, INIT, CHECKSUM;
INSERT dbo.Reserva (Concepto) VALUES ('B');
BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_28_diff.bak' WITH DIFFERENTIAL, INIT, CHECKSUM;

SELECT ROW_NUMBER() OVER (ORDER BY b.backup_set_id) AS Orden,
       CASE WHEN b.is_copy_only = 1 THEN 'Completo copy-only'
            WHEN b.type = 'D' THEN 'Completo'
            ELSE 'Diferencial' END AS TipoBackup,
       CASE WHEN b.type = 'I' AND b.differential_base_lsn =
                 (SELECT f.checkpoint_lsn FROM msdb.dbo.backupset AS f
                  WHERE f.database_name = DB_NAME() AND f.type = 'D' AND f.is_copy_only = 0)
            THEN 'Si' WHEN b.type = 'I' THEN 'No' ELSE '-' END AS BaseEsElCompletoNormal
FROM msdb.dbo.backupset AS b
WHERE b.database_name = DB_NAME()
ORDER BY b.backup_set_id;
```

**Resultado esperado.**

| Orden | TipoBackup | BaseEsElCompletoNormal |
|---|---|---|
| 1 | Completo | - |
| 2 | Completo copy-only | - |
| 3 | Diferencial | Si |

El diferencial sigue basado en el completo programado: el `COPY_ONLY` no la altera. Sin esa opción, el completo ad hoc habría pasado a ser la nueva base.
</details>

---

### Ejercicio 29 · Tail-log antes de restaurar
<!-- ejercicio: U5.29 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Tras el último backup de log se insertó una fila más. Antes de restaurar en otra base hay que capturar la cola. Hacelo, restaurá la cadena completa y mostrá el estado de la base original y las filas recuperadas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `BACKUP LOG ... WITH NORECOVERY` captura la cola y deja la base original en *restoring*; la sesión no puede estar dentro de esa base (`USE master`). Después se restaura completo, log y cola, y la original se vuelve a poner en línea.

<!-- check: U5.29 -->
```sql
BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_29_full.bak' WITH INIT, CHECKSUM;
INSERT dbo.Reserva (Concepto) VALUES ('A');
BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_29_log1.trn' WITH INIT, CHECKSUM;
INSERT dbo.Reserva (Concepto) VALUES ('R2_SIN_RESPALDAR');

USE master;
BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_29_tail.trn' WITH NORECOVERY, INIT, CHECKSUM;
SELECT state_desc FROM sys.databases WHERE name = 'LaboratorioU5';        -- RESTORING

RESTORE DATABASE LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_29_full.bak'
    WITH MOVE 'LaboratorioU5' TO 'D:\SQLData\LaboratorioU5_Rest.mdf',
         MOVE 'LaboratorioU5_log' TO 'D:\SQLData\LaboratorioU5_Rest.ldf', NORECOVERY;
RESTORE LOG LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_29_log1.trn' WITH NORECOVERY;
RESTORE LOG LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_29_tail.trn' WITH RECOVERY;

SELECT ReservaId, Concepto FROM LaboratorioU5_Rest.dbo.Reserva ORDER BY ReservaId;
RESTORE DATABASE LaboratorioU5 WITH RECOVERY;                              -- la original vuelve a línea
```

**Resultado esperado.**

| Concepto | Valor |
|---|---|
| Base origen tras el tail-log | RESTORING |
| Fila restaurada 1 | A |
| Fila restaurada 2 | R2_SIN_RESPALDAR |

Sin el tail-log, la segunda fila (posterior al último log) se habría perdido.
</details>

---

### Ejercicio 30 · Volver a antes de una carga marcada
<!-- ejercicio: U5.30 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Antes de un cierre mensual se abre una transacción marcada `CierreMensual`. Después del cierre se inserta una fila más. Restaurá una copia que vuelva a **antes** del cierre y otra que lo **incluya**, y comparalas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `WITH MARK` deja un nombre en el log. `STOPBEFOREMARK` recupera hasta justo antes de esa transacción; `STOPATMARK`, hasta incluirla. Se restauran dos bases desde el mismo completo y el mismo log.

<!-- check: U5.30 -->
```sql
INSERT dbo.Reserva (Concepto) VALUES ('R0_ANTES');
BEGIN TRANSACTION CierreMensual WITH MARK 'cierre del mes';
    INSERT dbo.Reserva (Concepto) VALUES ('R1_CIERRE');
COMMIT TRANSACTION;
INSERT dbo.Reserva (Concepto) VALUES ('R2_DESPUES');
BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_30_log1.trn' WITH INIT, CHECKSUM;

-- Base 1: completo NORECOVERY + log hasta justo antes de la marca
RESTORE LOG LaboratorioU5_Rest1 FROM DISK = 'D:\SQLBackups\U5_30_log1.trn'
    WITH STOPBEFOREMARK = 'CierreMensual', RECOVERY;
-- Base 2: completo NORECOVERY + log hasta incluir la transacción marcada
RESTORE LOG LaboratorioU5_Rest2 FROM DISK = 'D:\SQLBackups\U5_30_log1.trn'
    WITH STOPATMARK = 'CierreMensual', RECOVERY;

SELECT 'STOPBEFOREMARK' AS Opcion, Concepto FROM LaboratorioU5_Rest1.dbo.Reserva
UNION ALL
SELECT 'STOPATMARK', Concepto FROM LaboratorioU5_Rest2.dbo.Reserva
ORDER BY Opcion, Concepto;
```

**Resultado esperado** (se asume que el completo se restauró antes con `NORECOVERY` en ambas bases).

| Opcion | Concepto |
|---|---|
| STOPATMARK | R0_ANTES |
| STOPATMARK | R1_CIERRE |
| STOPBEFOREMARK | R0_ANTES |

`R2_DESPUES` no aparece en ninguna, porque ocurrió después de la marca. La diferencia entre las dos está en `R1_CIERRE`, que pertenece a la transacción marcada.
</details>

---

### Ejercicio 31 · Diseñar la estrategia para un RPO y un RTO
<!-- ejercicio: U5.31 | nivel: intermedio | tipo: diseno | verificacion: razonamiento -->

:::note[Enunciado]
Una base de 600 GB debe cumplir un RPO de 5 minutos y un RTO de 30 minutos. Restaurar un completo tarda 90 minutos, un diferencial 25 minutos y cada log unos 20 segundos. Diseñá la estrategia y decidí si los backups solos alcanzan.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se calcula el peor caso de restauración sumando las piezas y se lo compara con el RTO.

- **RPO de 5 minutos.** Backups de log cada 5 minutos (modelo `FULL`). Con intervalos de 5 minutos, a lo sumo se pierde lo ocurrido desde el último log.
- **Peor caso de restauración desde backups.** Completo (90 min) + diferencial (25 min) + hasta 288 logs diarios, aunque con un diferencial cada 6 horas bastan unos 72 logs × 20 s = 24 min. Total estimado: unos 139 minutos, mucho más que los 30 del RTO.
- **Conclusión.** Los backups **no alcanzan** para el RTO: cumplen el RPO pero no el tiempo de restauración. Hace falta una réplica lista (grupo de disponibilidad síncrono para la HA local, o al menos un secundario con log shipping y restauración continua), de modo que el *failover* dure segundos o minutos.
- **Los backups siguen siendo necesarios** para volver atrás ante un error lógico y para la retención 3-2-1.
</details>

---

### Ejercicio 32 · Recuperar a una hora con STOPAT
<!-- ejercicio: U5.32 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Se insertó una fila buena, pasaron unos segundos, se tomó una hora de referencia y, más tarde, se insertó una fila errónea; después se respaldó el log. Restaurá la base hasta la hora de referencia y mostrá que la fila errónea no está.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se guarda la hora del servidor (`GETDATE()`) antes del error, con unos segundos de margen a cada lado para no depender de la precisión del reloj, y se usa en `STOPAT`. Como el valor debe estar en el literal del `RESTORE`, el verificador lo arma con SQL dinámico; a mano se escribe la hora.

<!-- check: U5.32 -->
```sql
BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_32_full.bak' WITH INIT, CHECKSUM;
INSERT dbo.Reserva (Concepto) VALUES ('R0_ANTES');
WAITFOR DELAY '00:00:02';
DECLARE @Momento DATETIME = GETDATE();      -- hora de referencia (anotala)
WAITFOR DELAY '00:00:02';
INSERT dbo.Reserva (Concepto) VALUES ('R9_ERROR');
BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_32_log1.trn' WITH INIT, CHECKSUM;

RESTORE DATABASE LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_32_full.bak'
    WITH MOVE 'LaboratorioU5' TO 'D:\SQLData\LaboratorioU5_Rest.mdf',
         MOVE 'LaboratorioU5_log' TO 'D:\SQLData\LaboratorioU5_Rest.ldf', NORECOVERY;
RESTORE LOG LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_32_log1.trn'
    WITH STOPAT = '2026-07-22T14:37:00.000', RECOVERY;     -- la hora de referencia anotada

SELECT Concepto FROM LaboratorioU5_Rest.dbo.Reserva ORDER BY ReservaId;
```

**Resultado esperado.**

| Concepto |
|---|
| R0_ANTES |

`R9_ERROR`, posterior a la hora de referencia, no está. La hora es la del servidor: hay que verificar la zona horaria y, si es posible, preferir marcas, que no dependen del reloj (ejercicio 30).
</details>

---

### Ejercicio 33 · La cadena rota
<!-- ejercicio: U5.33 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Un operador restauró el completo y quiso aplicar el segundo log sin haber aplicado el primero. ¿Qué pasa? Demostralo, corregí el orden y contá las filas recuperadas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada backup de log cubre un rango de LSN y el siguiente debe empezar donde terminó el anterior; si hay un hueco, el motor rechaza la restauración. Como una base en *restoring* sigue aceptando piezas, se puede aplicar el log faltante y continuar. El primer `RESTORE LOG` va en un `TRY`/`CATCH`.

<!-- check: U5.33 -->
```sql
RESTORE DATABASE LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_33_full.bak'
    WITH MOVE 'LaboratorioU5' TO 'D:\SQLData\LaboratorioU5_Rest.mdf',
         MOVE 'LaboratorioU5_log' TO 'D:\SQLData\LaboratorioU5_Rest.ldf', NORECOVERY;

BEGIN TRY
    RESTORE LOG LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_33_log2.trn' WITH NORECOVERY;  -- salta log1
END TRY
BEGIN CATCH
    SELECT 'Restaurar log2 sin log1' AS Paso, 'rechazada' AS Resultado;
END CATCH;

RESTORE LOG LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_33_log1.trn' WITH NORECOVERY;
RESTORE LOG LaboratorioU5_Rest FROM DISK = 'D:\SQLBackups\U5_33_log2.trn' WITH RECOVERY;

SELECT COUNT(*) AS FilasRecuperadas FROM LaboratorioU5_Rest.dbo.Reserva;
```

**Resultado esperado** (el verificador junta el aviso del `CATCH` y el orden correcto en una tabla; al final hay 2 filas).

| Paso | Resultado |
|---|---|
| Orden correcto log1, log2 | sin error |
| Restaurar log2 sin log1 | rechazada |

`FilasRecuperadas` = 2. La base no se perdió por el error: siguió en *restoring* y aceptó los logs en el orden correcto. Para elegir el log siguiente se comparan los LSN de `RESTORE HEADERONLY` (`FirstLSN` y `LastLSN`).
</details>

---

### Ejercicio 34 · Log shipping simulado con STANDBY
<!-- ejercicio: U5.34 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Simulá en una instancia el flujo de un log shipping: un completo restaurado en `NORECOVERY` en la secundaria y, por cada ciclo, un backup de log de la primaria restaurado con `STANDBY`. Mostrá el estado de la secundaria y cuántas filas se pueden leer en cada paso, y hacé el *failover* manual al final.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los tres trabajos de log shipping (backup, copia, restauración) equivalen a `BACKUP LOG` y `RESTORE LOG ... WITH STANDBY`. Con `STANDBY` la secundaria es legible entre restauraciones (`is_in_standby = 1`). El *failover* manual es un `RESTORE ... WITH RECOVERY`.

<!-- check: U5.34 -->
```sql
BACKUP DATABASE LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_34_full.bak' WITH INIT, CHECKSUM;
RESTORE DATABASE LaboratorioU5_Sec FROM DISK = 'D:\SQLBackups\U5_34_full.bak'
    WITH MOVE 'LaboratorioU5' TO 'D:\SQLData\LaboratorioU5_Sec.mdf',
         MOVE 'LaboratorioU5_log' TO 'D:\SQLData\LaboratorioU5_Sec.ldf', NORECOVERY;

INSERT dbo.Reserva (Concepto) VALUES ('A');                      -- ciclo 1
BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_34_log1.trn' WITH INIT, CHECKSUM;
RESTORE LOG LaboratorioU5_Sec FROM DISK = 'D:\SQLBackups\U5_34_log1.trn'
    WITH STANDBY = 'D:\SQLData\LaboratorioU5_Sec.undo';
SELECT state_desc, is_in_standby, (SELECT COUNT(*) FROM LaboratorioU5_Sec.dbo.Reserva) AS Filas
FROM sys.databases WHERE name = 'LaboratorioU5_Sec';

INSERT dbo.Reserva (Concepto) VALUES ('B');                      -- ciclo 2 (igual)
BACKUP LOG LaboratorioU5 TO DISK = 'D:\SQLBackups\U5_34_log2.trn' WITH INIT, CHECKSUM;
RESTORE LOG LaboratorioU5_Sec FROM DISK = 'D:\SQLBackups\U5_34_log2.trn'
    WITH STANDBY = 'D:\SQLData\LaboratorioU5_Sec.undo';

RESTORE DATABASE LaboratorioU5_Sec WITH RECOVERY;                -- failover manual
```

**Resultado esperado** (el verificador consulta el estado tras cada paso).

| Paso | Estado | EnStandby | Filas |
|---|---|---|---|
| 1 secundaria tras restaurar el full | RESTORING | 0 | NULL |
| 2 tras aplicar el log 1 con STANDBY | ONLINE | 1 | 1 |
| 3 tras aplicar el log 2 con STANDBY | ONLINE | 1 | 2 |
| 4 failover manual: RECOVERY | ONLINE | 0 | 2 |

La secundaria es de solo lectura mientras sigue recibiendo logs; después de `RECOVERY` es escribible y deja de aceptar más logs. Ese paso es todo el *failover*: por eso en log shipping es manual.
</details>

---

### Ejercicio 35 · Session timeout y failover automático
<!-- ejercicio: U5.35 | nivel: avanzado | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Un grupo de disponibilidad tiene una primaria y dos secundarias: **S1** síncrona con *failover* automático y **S2** asíncrona. Durante 25 segundos se corta la red hacia S1. (a) ¿Se bloquean los commits en la primaria? (b) Si en ese lapso falla la primaria, ¿puede haber *failover* automático a S1 sin pérdida de datos? (c) ¿Y a S2?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se aplican las reglas del modo de disponibilidad y el comportamiento ante `SESSION_TIMEOUT` (10 segundos por defecto).

- **(a)** No de forma indefinida. Vencido el `SESSION_TIMEOUT`, la primaria deja de esperar a S1 y confirma de forma asíncrona para esa réplica hasta que se restablezca y se ponga al día.
- **(b)** No sin pérdida. Mientras S1 no está sincronizada, no cumple la condición de estado sincronizado que exige el *failover* automático; un *failover* en ese estado solo es posible de forma forzada, con posible pérdida de las transacciones que no recibió.
- **(c)** Tampoco de forma automática. S2 es asíncrona: el *failover* automático solo existe entre réplicas síncronas. Con S2 solo hay *failover* manual forzado, con posible pérdida.

La lección: el modo síncrono reduce el RPO solo mientras la réplica está sincronizada.
</details>

---

### Ejercicio 36 · Un DELETE descubierto tres días después
<!-- ejercicio: U5.36 | nivel: avanzado | tipo: diseno | verificacion: razonamiento -->

:::note[Enunciado]
Un grupo de disponibilidad síncrono protege una base. Tres días después alguien descubre que un trabajo borró por error las facturas de un mes. (a) ¿La réplica sirve para recuperarlas? (b) ¿Qué estrategia de backups lo permite? (c) ¿Y si además la cuenta administrativa fue comprometida por *ransomware*?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se distingue disponibilidad (el estado actual) de recuperación histórica (estados pasados) y se agrega aislamiento de las copias.

- **(a)** No. La réplica síncrona aplicó el `DELETE` casi al instante; también tiene las facturas borradas. La HA no reemplaza al backup.
- **(b)** Hace falta una cadena `FULL` con completos, diferenciales y logs retenidos por más de tres días. Se restaura a otra base hasta justo antes del borrado (`STOPAT` o una marca), se extraen las facturas y se reinsertan en producción. Se valida con `CHECKDB` y pruebas funcionales.
- **(c)** Las copias no deben compartir credenciales con producción: se agrega una copia externa e inmutable (regla 3-2-1), con retención que un atacante no pueda borrar, y se prueban restauraciones periódicas.
</details>

---

### Ejercicio 37 · Una transacción abierta retiene el log
<!-- ejercicio: U5.37 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
En una base en modelo `SIMPLE`, un proceso abre una transacción que inserta 20 000 filas y no la cierra. Mostrá qué dice `log_reuse_wait_desc` mientras la transacción está abierta y después de confirmarla.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El checkpoint de `SIMPLE` trunca el log, pero no puede liberar el espacio que una transacción activa todavía necesita. Se mide con y sin la transacción abierta. En un modelo `FULL`, la causa también sería `ACTIVE_TRANSACTION` mientras dure, y además `LOG_BACKUP` hasta el próximo backup de log (un `BACKUP` no puede ejecutarse dentro de una transacción, por eso el ejercicio usa `SIMPLE`).

<!-- check: U5.37 -->
```sql
ALTER DATABASE CURRENT SET RECOVERY SIMPLE;

BEGIN TRANSACTION;
    INSERT dbo.Reserva (Concepto)
    SELECT TOP (20000) 'lote' FROM sys.all_objects AS a CROSS JOIN sys.all_objects AS b;
    CHECKPOINT;
    SELECT 'Transaccion abierta y CHECKPOINT' AS Momento, log_reuse_wait_desc AS Espera
    FROM sys.databases WHERE database_id = DB_ID();
COMMIT TRANSACTION;

CHECKPOINT;
SELECT 'Tras el COMMIT y otro CHECKPOINT' AS Momento, log_reuse_wait_desc AS Espera
FROM sys.databases WHERE database_id = DB_ID();
```

**Resultado esperado.**

| Momento | Espera |
|---|---|
| Transacción abierta y CHECKPOINT | ACTIVE_TRANSACTION |
| Tras el COMMIT y otro CHECKPOINT | NOTHING |

Para encontrar al culpable en un sistema real se usan `DBCC OPENTRAN` o `sys.dm_tran_active_transactions`. La solución es cerrar o acortar la transacción, no achicar el archivo.
</details>
