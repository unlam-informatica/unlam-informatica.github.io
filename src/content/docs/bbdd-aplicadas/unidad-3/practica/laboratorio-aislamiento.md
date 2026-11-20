---
title: Laboratorio de niveles de aislamiento
slug: bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento
sidebar:
  order: 2
---

[← Concurrencia, bloqueos y transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/)

Este laboratorio recorre los fenómenos de concurrencia y los niveles de aislamiento con **dos ventanas de consulta** (cada ventana es una sesión independiente) y termina con ejercicios de **una sola sesión** sobre locks, versiones de fila y transacciones distribuidas. Presupone la teoría de [Concurrencia, bloqueos y transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/) y de [Control de transacciones (TCL)](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/). Para un escenario con tarjeta de crédito, ver el [laboratorio TCL](/bbdd-aplicadas/unidad-3/practica/laboratorio-tcl/).

:::note[Qué ejemplos podés reproducir tal cual]
El entorno y los ejercicios 13 a 15, 17, 18 y 20 son de una sola sesión: se reproducen en una base de práctica y sus resultados se obtuvieron con SQL Server 2022. Los laboratorios 1 a 5 y los ejercicios 24 y 25 requieren **dos sesiones** y se presentan como guion paso a paso. **No se probaron en un motor**: lo que se indica como resultado de cada sesión es el comportamiento que describe la documentación de SQL Server; comprobalo en tu instalación.
:::

## Cómo trabajar

1. Creá una [base de práctica](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos) (por ejemplo, `CREATE DATABASE LabTransacciones;`; si no tenés el permiso `CREATE DATABASE`, pedí una). Abrí **dos ventanas de consulta** (pestañas en SSMS o en VS Code) conectadas al mismo servidor y en **ambas** ejecutá `USE LabTransacciones;`. Una ventana es la sesión A y la otra, la sesión B. Son conexiones independientes: lo que una deja sin confirmar lo ve la otra solo a través de los locks.
2. Ejecutá primero el script de la sección [Entorno](#entorno), en cualquiera de las dos ventanas. Después, cada guion indica en qué sesión se ejecuta cada bloque y cuál va primero. Cuando un bloque tiene un `WAITFOR DELAY`, ejecutá el bloque de la otra sesión **durante** esa espera: conviene dejar el bloque de la otra ventana ya escrito y ejecutarlo apenas arranca el primero.
3. Al final de cada laboratorio hay una **limpieza** o el estado se restablece solo. Si dudás del estado, volvé a ejecutar el script del Entorno.
4. Cerrá las transacciones abiertas antes de pasar al siguiente laboratorio: una sesión con una transacción abierta mantiene sus locks.

## Entorno

Este script se ejecuta en una sola ventana. Crea el esquema `banco` con las tablas `Cuenta` y `Movimiento` y deja la base sin `SNAPSHOT` ni RCSI. Los dos `ALTER DATABASE` esperan a que no haya otras conexiones con transacciones activas en la base; con `WITH ROLLBACK IMMEDIATE` se desconecta a las demás (por ejemplo, una ventana olvidada con una transacción abierta). Es también el script de **reinicio**: volvé a ejecutarlo para restablecer los datos.

<!-- check: U3.T.CC.09 -->
```sql
IF SCHEMA_ID('banco') IS NULL
    EXEC ('CREATE SCHEMA banco');
GO
DROP TABLE IF EXISTS banco.Movimiento;
DROP TABLE IF EXISTS banco.Cuenta;
GO
CREATE TABLE banco.Cuenta (
    CuentaId INT           NOT NULL CONSTRAINT PK_Cuenta PRIMARY KEY,
    Titular  VARCHAR(40)   NOT NULL,
    Saldo    DECIMAL(12,2) NOT NULL CONSTRAINT CK_Cuenta_Saldo CHECK (Saldo >= 0)
);
CREATE TABLE banco.Movimiento (
    MovimientoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Movimiento PRIMARY KEY,
    CuentaId     INT           NOT NULL CONSTRAINT FK_Movimiento_Cuenta REFERENCES banco.Cuenta (CuentaId),
    Tipo         CHAR(1)       NOT NULL CONSTRAINT CK_Movimiento_Tipo CHECK (Tipo IN ('D', 'C')),
    Monto        DECIMAL(12,2) NOT NULL CONSTRAINT CK_Movimiento_Monto CHECK (Monto > 0),
    Descripcion  VARCHAR(100)  NULL
);
GO
INSERT INTO banco.Cuenta (CuentaId, Titular, Saldo) VALUES
    (1, 'Cliente 01', 5000.00),
    (2, 'Cliente 02', 3200.00),
    (3, 'Cliente 03',  800.00);
GO

ALTER DATABASE CURRENT SET READ_COMMITTED_SNAPSHOT OFF WITH ROLLBACK IMMEDIATE;
ALTER DATABASE CURRENT SET ALLOW_SNAPSHOT_ISOLATION OFF;
GO
SELECT is_read_committed_snapshot_on AS Rcsi, snapshot_isolation_state_desc AS Snapshot
FROM sys.databases
WHERE database_id = DB_ID();

SELECT CuentaId, Titular, Saldo FROM banco.Cuenta ORDER BY CuentaId;
```

**Resultado esperado.**

| Rcsi | Snapshot |
|---:|---|
| 0 | OFF |

| CuentaId | Titular | Saldo |
|---:|---|---:|
| 1 | Cliente 01 | 5000.00 |
| 2 | Cliente 02 | 3200.00 |
| 3 | Cliente 03 | 800.00 |

## Laboratorio 1 · Lectura sucia y READ COMMITTED

`READ UNCOMMITTED` lee filas modificadas y no confirmadas. `READ COMMITTED` no: espera a que la otra transacción termine.

**Sesión A** (modifica y espera sin confirmar):

<!-- check: U3.T.CC.10 -->
```sql
BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = 99999 WHERE CuentaId = 1;
    WAITFOR DELAY '00:00:20';
ROLLBACK TRANSACTION;
```

**Sesión B** (ejecutar mientras A espera):

<!-- check: U3.T.CC.10 -->
```sql
-- Primero con READ UNCOMMITTED: no pide lock S.
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT CuentaId, Saldo FROM banco.Cuenta WHERE CuentaId = 1;

-- Después con READ COMMITTED: pide S sobre una fila con X.
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT CuentaId, Saldo FROM banco.Cuenta WHERE CuentaId = 1;
```

**Resultado esperado** (según la documentación; no se probó en un motor):

| Consulta de B | Resultado |
|---|---|
| Primer `SELECT` (`READ UNCOMMITTED`) | Inmediato. `Saldo` = 99999: un dato que A todavía no confirmó y que va a revertir (lectura sucia) |
| Segundo `SELECT` (`READ COMMITTED`) | **Espera** hasta el `ROLLBACK` de A (unos 20 segundos desde que empezó A) |
| Después del `ROLLBACK` | El segundo `SELECT` devuelve `Saldo` = 5000: el valor original |

La sugerencia `WITH (NOLOCK)` en la tabla produce el mismo efecto que `READ UNCOMMITTED` para esa tabla.

## Laboratorio 2 · Lectura no repetible y REPEATABLE READ

Con `READ COMMITTED`, los locks `S` se sueltan al leer: otra transacción puede modificar la fila entre dos lecturas. Con `REPEATABLE READ`, el `S` se mantiene hasta el final y la modificación espera.

**Sesión B, primera corrida** (`READ COMMITTED`):

<!-- check: U3.T.CC.11 -->
```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRANSACTION;
    SELECT Saldo AS PrimeraLectura FROM banco.Cuenta WHERE CuentaId = 1;
    WAITFOR DELAY '00:00:15';
    SELECT Saldo AS SegundaLectura FROM banco.Cuenta WHERE CuentaId = 1;
COMMIT TRANSACTION;
```

**Sesión A** (durante los 15 segundos):

<!-- check: U3.T.CC.11 -->
```sql
UPDATE banco.Cuenta SET Saldo = 1111 WHERE CuentaId = 1;   -- autocommit
```

**Sesión B, segunda corrida**: el mismo bloque con `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;` en la primera línea (antes, restablecé el saldo con `UPDATE banco.Cuenta SET Saldo = 5000 WHERE CuentaId = 1;`). La sesión A ejecuta de nuevo su `UPDATE` durante la espera.

**Resultado esperado** (según la documentación; no se probó en un motor):

| Corrida de B | `PrimeraLectura` | `SegundaLectura` | Sesión A |
|---|---:|---:|---|
| `READ COMMITTED` | 5000 | 1111 (**lectura no repetible**) | Se completa de inmediato |
| `REPEATABLE READ` | 5000 | 5000 | Su `UPDATE` **espera** hasta el `COMMIT` de B y se completa después |

Al terminar, el saldo queda en 1111. Restablecelo con `UPDATE banco.Cuenta SET Saldo = 5000 WHERE CuentaId = 1;`.

## Laboratorio 3 · Fantasma y SERIALIZABLE

`REPEATABLE READ` protege las filas ya leídas, pero no impide que aparezcan filas nuevas que cumplan el criterio. `SERIALIZABLE` toma locks de rango y lo impide.

**Sesión B** (cambiá el nivel para la segunda corrida):

<!-- check: U3.T.CC.12 -->
```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;     -- segunda corrida: SERIALIZABLE
BEGIN TRANSACTION;
    SELECT COUNT(*) AS PrimeraCuenta FROM banco.Cuenta WHERE Saldo >= 1000;
    WAITFOR DELAY '00:00:15';
    SELECT COUNT(*) AS SegundaCuenta FROM banco.Cuenta WHERE Saldo >= 1000;
COMMIT TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**Sesión A** (durante la espera; no borra la fila todavía):

<!-- check: U3.T.CC.12 -->
```sql
INSERT INTO banco.Cuenta (CuentaId, Titular, Saldo) VALUES (4, 'Cliente 04', 2500.00);
```

**Limpieza.** Esperá a que **B termine** y recién entonces ejecutá, en cualquier sesión:

<!-- check: U3.T.CC.12 -->
```sql
DELETE FROM banco.Cuenta WHERE CuentaId = 4;
```

**Resultado esperado** (según la documentación; no se probó en un motor):

| Nivel de B | `PrimeraCuenta` | `SegundaCuenta` | Sesión A |
|---|---:|---:|---|
| `REPEATABLE READ` | 2 | 3 (**fantasma**: apareció la fila de la cuenta 4) | El `INSERT` se completa de inmediato |
| `SERIALIZABLE` | 2 | 2 | El `INSERT` **espera** hasta el `COMMIT` de B |

En el primer caso, el `INSERT` y la limpieza son sentencias separadas **a propósito**: si se ejecutaran de corrido, la fila existiría solo unos milisegundos y B nunca la vería. Como la columna `Saldo` no tiene índice, el rango bloqueado por `SERIALIZABLE` abarca toda la tabla (ver el ejercicio 17); por eso el `INSERT` de la cuenta 4 queda esperando.

## Laboratorio 4 · SNAPSHOT

Con `SNAPSHOT` los lectores no esperan a los escritores y ven la instantánea confirmada al inicio de su transacción.

Habilitá la opción en la base (una sola vez):

<!-- check: U3.T.CC.18 -->
```sql
ALTER DATABASE CURRENT SET ALLOW_SNAPSHOT_ISOLATION ON;
GO
SELECT snapshot_isolation_state_desc AS Snapshot FROM sys.databases WHERE database_id = DB_ID();
```

**Sesión A** (escritura larga sin confirmar):

<!-- check: U3.T.CC.13 -->
```sql
BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = 77777 WHERE CuentaId = 1;
    WAITFOR DELAY '00:00:20';
ROLLBACK TRANSACTION;
```

**Sesión B** (ejecutar mientras A espera):

<!-- check: U3.T.CC.13 -->
```sql
SET TRANSACTION ISOLATION LEVEL SNAPSHOT;
BEGIN TRANSACTION;
    SELECT Saldo AS PrimeraLectura FROM banco.Cuenta WHERE CuentaId = 1;
    WAITFOR DELAY '00:00:25';
    SELECT Saldo AS SegundaLectura FROM banco.Cuenta WHERE CuentaId = 1;
COMMIT TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**Resultado esperado** (según la documentación; no se probó en un motor):

| Consulta de B | Resultado |
|---|---|
| `PrimeraLectura` | Inmediata: 5000. No espera el `X` de A; lee la versión confirmada |
| `SegundaLectura` (después del `ROLLBACK` de A) | 5000: la misma instantánea, y coincide con el valor real porque A revirtió |

Si en lugar de revertir A confirmara, `SegundaLectura` seguiría mostrando 5000: B sigue viendo la instantánea de su inicio.

### Ejercicio 24 · Conflicto de actualización en SNAPSHOT (error 3960)
<!-- ejercicio: U3.24 | nivel: avanzado | tipo: diagnostico | verificacion: revisado -->

:::note[Enunciado]
Con `ALLOW_SNAPSHOT_ISOLATION ON`, una transacción `SNAPSHOT` lee una cuenta y, más tarde, intenta modificarla, pero otra sesión ya la modificó y confirmó en el medio. Escribí el guion de las dos sesiones, indicá qué ocurre en cada una y cómo debe reaccionar la aplicación.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La sesión B abre una transacción `SNAPSHOT` y lee la fila: eso fija su instantánea. Durante su espera, la sesión A modifica la misma fila y confirma. Cuando B intenta modificarla, el motor detecta que la fila cambió **después** de su instantánea y no puede aplicar su cambio sin pisar el de A: aborta la transacción de B con el error 3960. Reiniciá el entorno y habilitá `ALLOW_SNAPSHOT_ISOLATION` antes de empezar.

**Sesión B** (primera; se ejecuta antes que A):

<!-- check: U3.24 -->
```sql
SET TRANSACTION ISOLATION LEVEL SNAPSHOT;

BEGIN TRY
    BEGIN TRANSACTION;
        SELECT Saldo AS SaldoLeido FROM banco.Cuenta WHERE CuentaId = 2;    -- fija la instantánea
        WAITFOR DELAY '00:00:15';                                           -- se ejecuta A
        UPDATE banco.Cuenta SET Saldo = Saldo - 100 WHERE CuentaId = 2;     -- conflicto
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Error, XACT_STATE() AS Estado;
    IF XACT_STATE() <> 0
        ROLLBACK TRANSACTION;
END CATCH;

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**Sesión A** (dentro de los 15 segundos):

<!-- check: U3.24 -->
```sql
UPDATE banco.Cuenta SET Saldo = Saldo + 500 WHERE CuentaId = 2;   -- autocommit: confirma ya
```

**Resultado esperado** (según la documentación; no se probó en un motor):

| Sesión | Resultado |
|---|---|
| B, `SaldoLeido` | 3200 |
| A | Se completa de inmediato: B solo leyó, no tiene locks que esperar. Saldo real = 3700 |
| B, `UPDATE` | Falla con el **error 3960** (*Snapshot isolation transaction aborted due to update conflict*) |
| B, `CATCH` | Devuelve `Error` = 3960; la transacción de B no puede continuar, y se revierte |
| Estado final | Cuenta 2 con saldo 3700: solo quedó el cambio de A |

La aplicación debe **reintentar la transacción completa** de B desde el principio: volverá a leer 3700 y aplicará su débito sobre ese valor. Con `READ COMMITTED` (o RCSI) no habría error: el `UPDATE` de B esperaría el `X` de A y luego restaría 100 sobre el valor ya confirmado.
</details>

## Laboratorio 5 · READ_COMMITTED_SNAPSHOT (RCSI)

RCSI cambia el comportamiento de `READ COMMITTED` para **todas** las conexiones de la base, sin modificar el código: las lecturas usan la versión confirmada al inicio de cada sentencia en lugar de pedir locks `S`.

Activalo (desconecta a las demás sesiones de la base):

<!-- check: U3.T.CC.19 -->
```sql
ALTER DATABASE CURRENT SET READ_COMMITTED_SNAPSHOT ON WITH ROLLBACK IMMEDIATE;
GO
SELECT is_read_committed_snapshot_on AS Rcsi FROM sys.databases WHERE database_id = DB_ID();
```

**Sesión A** (escribe sin confirmar):

<!-- check: U3.T.CC.14 -->
```sql
BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = 55555 WHERE CuentaId = 3;
    WAITFOR DELAY '00:00:20';
ROLLBACK TRANSACTION;
```

**Sesión B** (sin ningún `SET` especial):

<!-- check: U3.T.CC.14 -->
```sql
SELECT CuentaId, Saldo FROM banco.Cuenta WHERE CuentaId = 3;
```

**Resultado esperado** (según la documentación; no se probó en un motor):

| Consulta de B | Resultado |
|---|---|
| `SELECT` | Inmediata: `Saldo` = 800, el último valor **confirmado**. No devuelve 55555 ni espera a A |
| Sin RCSI (para comparar) | La misma consulta **esperaría** el `ROLLBACK` de A |

| | `SNAPSHOT` | RCSI |
|---|---|---|
| Versión que lee | La del inicio de la transacción | La del inicio de cada sentencia |
| Se activa | `SET TRANSACTION ISOLATION LEVEL SNAPSHOT` en cada sesión | `ALTER DATABASE ... READ_COMMITTED_SNAPSHOT ON`, transparente |
| Lecturas repetibles | Sí | No |
| Conflicto de escritura | Error 3960 | Espera el `X` del otro escritor |

RCSI es una opción atractiva para sistemas existentes porque elimina la mayoría de los bloqueos lector-escritor sin cambiar la aplicación, pero tiene costos: usa `tempdb` para las versiones de fila y puede cambiar el comportamiento de código que dependía de que una lectura esperara a un escritor. Conviene medir el uso del *version store* antes de activarlo.

**Restauración.** Al terminar, dejá la base como estaba:

<!-- check: U3.T.CC.20 -->
```sql
ALTER DATABASE CURRENT SET READ_COMMITTED_SNAPSHOT OFF WITH ROLLBACK IMMEDIATE;
ALTER DATABASE CURRENT SET ALLOW_SNAPSHOT_ISOLATION OFF;
GO
SELECT is_read_committed_snapshot_on AS Rcsi, snapshot_isolation_state_desc AS Snapshot
FROM sys.databases WHERE database_id = DB_ID();
```

## Ejercicios

Los ejercicios 11 a 20 se resuelven en **una sola sesión** (o con razonamiento). Ejecutá cada uno en la base de práctica, con los datos que deja el script del [Entorno](#entorno) recién ejecutado.

### Nivel inicial

#### Ejercicio 11 · Planificaciones serie y serializables
<!-- ejercicio: U3.11 | nivel: inicial | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Sean `T1 = R(A) W(A) R(B) W(B)` y `T2 = R(A) W(A)`. Para cada planificación indicá si es **en serie**, **serializable** (equivalente a una serie) o **no serializable**, y justificá con el orden de las operaciones en conflicto.

- `P1`: `R1(A) W1(A) R1(B) W1(B) R2(A) W2(A)`
- `P2`: `R1(A) W1(A) R2(A) W2(A) R1(B) W1(B)`
- `P3`: `R1(A) R2(A) W1(A) W2(A) R1(B) W1(B)`

Para `P3`, indicá qué fenómeno de concurrencia es y qué ocurriría con bloqueos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Dos operaciones están en conflicto si acceden al mismo dato y al menos una escribe. `T2` solo toca `A`, así que los conflictos entre `T1` y `T2` están todos sobre `A`. Se mira, para cada par en conflicto, qué transacción va primero: si todos los pares ordenan a la misma transacción primero, la planificación equivale a esa serie; si unos pares ordenan `T1` primero y otros `T2`, hay un ciclo y no es serializable.

- `P1`: **en serie** (`T1` completa y luego `T2`).
- `P2`: **serializable, no en serie.** Sobre `A`: `W1(A)` va antes que `R2(A)` y `W2(A)`, y `R1(A)` antes que `W2(A)`; siempre va primero `T1`. Es equivalente a `T1; T2`: `T1` termina con `B` después, pero `T2` no toca `B`.
- `P3`: **no serializable.** `R1(A)` va antes de `W2(A)` (`T1` antes que `T2`), pero `R2(A)` va antes de `W1(A)` (`T2` antes que `T1`): ciclo. Es una **actualización perdida**: ambas leen el mismo valor de `A` y ambas escriben a partir de él, de modo que la escritura de `T1` se pierde. Con bloqueos, `W1(A)` pediría un `X` mientras `T2` tiene un `S` sobre `A` (y viceversa): con `REPEATABLE READ` ese cruce es un deadlock de conversión y el motor revierte a una de las dos.
</details>

#### Ejercicio 12 · Verdadero o falso: niveles de aislamiento
<!-- ejercicio: U3.12 | nivel: inicial | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Indicá si cada afirmación es verdadera o falsa.

1. `READ COMMITTED` evita las lecturas no repetibles.
2. `SERIALIZABLE` evita los fantasmas con locks de rango.
3. `SNAPSHOT` evita las lecturas sucias y las no repetibles sin tomar locks `S`.
4. En `READ UNCOMMITTED` una transacción puede leer una fila que otra tiene con lock `X`.
5. Con RCSI activado, dos `SELECT` idénticos dentro de una misma transacción en `READ COMMITTED` siempre devuelven lo mismo.
6. Para usar RCSI hay que cambiar el código de la aplicación.
7. `REPEATABLE READ` evita los fantasmas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se compara cada afirmación con la tabla de niveles.

1. **Falso.** `READ COMMITTED` solo evita la lectura sucia; la no repetible es posible porque el `S` se suelta al leer.
2. **Verdadero.** Los locks de rango impiden insertar filas en el rango leído.
3. **Verdadero.** Lee la versión confirmada al inicio de la transacción, sin pedir `S`.
4. **Verdadero.** `READ UNCOMMITTED` no pide locks `S`, así que no choca con un `X`.
5. **Falso.** RCSI lee la versión confirmada al inicio de **cada sentencia**: si otra transacción confirma entre los dos `SELECT`, el segundo ve el cambio.
6. **Falso.** Se activa en la base con `ALTER DATABASE`; el código existente se beneficia sin cambios (aunque conviene probar el efecto).
7. **Falso.** Evita la no repetible, pero no la fantasma; hace falta `SERIALIZABLE` o `SNAPSHOT`.
</details>

#### Ejercicio 13 · El lock X en READ UNCOMMITTED
<!-- ejercicio: U3.13 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Un compañero sostiene que si una sesión usa `READ UNCOMMITTED`, sus `UPDATE` no toman locks y por eso no bloquean a nadie. Demostrá con `sys.dm_tran_locks` que es falso: modificá una fila en esa sesión y listá los locks que tiene antes de revertir.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El nivel de aislamiento solo cambia cómo se **leen** los datos. Una modificación siempre toma un lock exclusivo, que se mantiene hasta el fin de la transacción. Se hace el `UPDATE` en `READ UNCOMMITTED` y se consulta `sys.dm_tran_locks` filtrando por la sesión actual y excluyendo el lock de la base.

<!-- check: U3.13 -->
```sql
DECLARE @Candado TABLE (Orden INT, Nivel VARCHAR(20), Recurso VARCHAR(20), Modo VARCHAR(10), Cantidad INT);

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 2;
    INSERT INTO @Candado
    SELECT 1, 'READ UNCOMMITTED', resource_type, request_mode, COUNT(*)
    FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type <> 'DATABASE'
    GROUP BY resource_type, request_mode;
ROLLBACK TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

SELECT Nivel, Recurso, Modo, Cantidad FROM @Candado ORDER BY Recurso, Modo;
```

**Resultado esperado.**

| Nivel | Recurso | Modo | Cantidad |
|---|---|---|---:|
| READ UNCOMMITTED | KEY | X | 1 |
| READ UNCOMMITTED | OBJECT | IX | 1 |
| READ UNCOMMITTED | PAGE | IX | 1 |

Hay un lock `X` sobre la fila (`KEY`) y locks de intención `IX` sobre la página y la tabla, igual que en `READ COMMITTED`. Otra sesión que quisiera leer esa fila en `READ COMMITTED` o modificarla tendría que esperar.
</details>

### Nivel intermedio

#### Ejercicio 14 · Activar RCSI y ver las versiones de fila
<!-- ejercicio: U3.14 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Activá `READ_COMMITTED_SNAPSHOT` en la base de pruebas, comprobá la opción en `sys.databases`, modificá una fila dentro de una transacción y verificá con `sys.dm_tran_version_store` que se generó una versión. Dejá la base como estaba.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con RCSI activado, las modificaciones guardan la versión anterior de la fila en el *version store* de `tempdb`, aunque ninguna sesión la esté leyendo todavía: ese es el costo de la opción. La cantidad exacta de versiones depende del motor, así que se verifica que haya al menos una.

<!-- check: U3.14 -->
```sql
DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(60), Valor VARCHAR(40));
DECLARE @Versiones INT;

ALTER DATABASE CURRENT SET READ_COMMITTED_SNAPSHOT ON;

INSERT INTO @Observacion
SELECT 1, 'is_read_committed_snapshot_on', CAST(is_read_committed_snapshot_on AS VARCHAR(10))
FROM sys.databases WHERE database_id = DB_ID();
INSERT INTO @Observacion
SELECT 2, 'snapshot_isolation_state_desc', snapshot_isolation_state_desc
FROM sys.databases WHERE database_id = DB_ID();

BEGIN TRANSACTION;                                   -- nivel READ COMMITTED, ya versionado
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;
    SELECT @Versiones = COUNT(*) FROM sys.dm_tran_version_store WHERE database_id = DB_ID();
ROLLBACK TRANSACTION;

INSERT INTO @Observacion VALUES (3, 'versiones de fila tras un UPDATE (>= 1)', IIF(@Versiones >= 1, 'sí', 'no'));

ALTER DATABASE CURRENT SET READ_COMMITTED_SNAPSHOT OFF;
INSERT INTO @Observacion
SELECT 4, 'is_read_committed_snapshot_on tras desactivarla', CAST(is_read_committed_snapshot_on AS VARCHAR(10))
FROM sys.databases WHERE database_id = DB_ID();

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Momento | Valor |
|---:|---|---|
| 1 | is_read_committed_snapshot_on | 1 |
| 2 | snapshot_isolation_state_desc | OFF |
| 3 | versiones de fila tras un UPDATE (>= 1) | sí |
| 4 | is_read_committed_snapshot_on tras desactivarla | 0 |

`ALLOW_SNAPSHOT_ISOLATION` sigue en `OFF`: RCSI y `SNAPSHOT` son opciones independientes. Al desactivar RCSI la opción vuelve a 0. Si hubiera otras conexiones en la base, el `ALTER DATABASE` esperaría; en ese caso se usa `WITH ROLLBACK IMMEDIATE`.
</details>

#### Ejercicio 15 · Cambiar el nivel a mitad de una transacción
<!-- ejercicio: U3.15 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Dentro de una misma transacción, leé la cuenta 1 en `READ COMMITTED`, cambiá a `REPEATABLE READ` y leé la cuenta 2. Antes del `COMMIT`, listá los locks `KEY` que mantiene la sesión. ¿Cuántos son y de qué cuenta? Relacionalo con la regla de la documentación sobre cambiar el nivel durante una transacción.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Lo leído **antes** del cambio sigue protegido con las reglas del nivel anterior (`READ COMMITTED`: el `S` se soltó al leer). Lo leído **después** se protege con las del nuevo (`REPEATABLE READ`: el `S` se mantiene). Por lo tanto, queda un solo lock `S` y es el de la cuenta 2.

<!-- check: U3.15 -->
```sql
DECLARE @Candado TABLE (Orden INT, Momento VARCHAR(50), Recurso VARCHAR(20), Modo VARCHAR(10), Cantidad INT);
DECLARE @Dato DECIMAL(12,2);

BEGIN TRANSACTION;                                           -- READ COMMITTED
    SELECT @Dato = Saldo FROM banco.Cuenta WHERE CuentaId = 1;

    SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;         -- cambio a mitad de la transacción
    SELECT @Dato = Saldo FROM banco.Cuenta WHERE CuentaId = 2;

    INSERT INTO @Candado
    SELECT 1, 'tras leer las filas 1 (antes) y 2 (después)', resource_type, request_mode, COUNT(*)
    FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type = 'KEY'
    GROUP BY resource_type, request_mode;
COMMIT TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

SELECT Momento, Recurso, Modo, Cantidad FROM @Candado ORDER BY Orden;
```

**Resultado esperado.**

| Momento | Recurso | Modo | Cantidad |
|---|---|---|---:|
| tras leer las filas 1 (antes) y 2 (después) | KEY | S | 1 |

Un único `KEY` con modo `S`: el de la fila de la cuenta 2. La cuenta 1, leída antes del cambio, no quedó protegida.
</details>

#### Ejercicio 16 · Compatibilidad de locks
<!-- ejercicio: U3.16 | nivel: intermedio | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Con la matriz de compatibilidad de la teoría, decidí en cada caso si la solicitud se concede o espera.

1. La sesión A tiene un `S` sobre una fila y la B pide un `U` sobre la misma fila.
2. La sesión A tiene un `U` sobre una fila y la B pide un `U` sobre la misma fila.
3. La sesión A modifica una fila (tiene `IX` sobre la tabla) y la B pide un `S` sobre **toda la tabla**.
4. La sesión A tiene un `X` sobre una fila y la B lee esa fila en `READ UNCOMMITTED`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se busca el lock concedido en las filas de la matriz y el solicitado en las columnas.

1. **Se concede.** `U` es compatible con un `S` ya concedido. Por eso un `UPDATE` puede empezar a leer una fila que otra sesión está leyendo.
2. **Espera.** `U` no es compatible con `U`. Eso evita el deadlock de conversión de dos sesiones que leen para actualizar: la segunda espera desde el principio, no después de haber leído.
3. **Espera.** `S` sobre la tabla no es compatible con `IX`. Un `SELECT` que necesita bloquear la tabla entera (por ejemplo, un escaneo con un hint `TABLOCK`) espera a que termine la transacción que modifica filas.
4. **Se concede.** `READ UNCOMMITTED` no pide locks `S`, así que no hay solicitud incompatible: la lectura es inmediata y puede ser sucia.
</details>

#### Ejercicio 19 · Commit en dos fases
<!-- ejercicio: U3.19 | nivel: intermedio | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Una transacción distribuida involucra a tres instancias, `P1`, `P2` y `P3`, coordinadas por MS DTC. Respondé: (a) ¿qué pasa si `P3` responde que no puede prepararse en la fase 1? (b) ¿Qué estado tiene `P1` si el coordinador deja de responder justo después de que `P1` dijo que estaba listo? (c) ¿Por qué `SNAPSHOT` no se puede usar en una transacción distribuida?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se razona con las dos fases: preparación (cada participante deja sus cambios durables en su log y responde) y confirmación (el coordinador decide).

- **(a)** El coordinador recibe un "no" y ordena `ROLLBACK` a todos, incluidos `P1` y `P2`, que ya habían dicho "listo". La transacción se revierte en las tres instancias: es lo que garantiza la atomicidad entre nodos.
- **(b)** `P1` queda **en duda** (*in-doubt*): respondió "listo", tiene sus cambios en el log y sus locks tomados, y no puede decidir solo si confirmar o revertir, porque el resultado depende de lo que haya decidido el coordinador. Debe esperar a que se restablezca la comunicación. Mientras tanto, los datos bloqueados siguen inaccesibles para otras sesiones.
- **(c)** Según la documentación de SQL Server, el aislamiento `SNAPSHOT` no admite transacciones distribuidas.
</details>

#### Ejercicio 20 · BEGIN DISTRIBUTED TRANSACTION en una instancia
<!-- ejercicio: U3.20 | nivel: intermedio | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Sin servidor vinculado, comprobá la sintaxis: abrí una transacción con `BEGIN DISTRIBUTED TRANSACTION` y un nombre, leé `@@TRANCOUNT`, modificá una fila local, confirmá y registrá lo que pasó. Indicá qué **no** demuestra este ejercicio.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con una sola instancia no hay participantes remotos, pero la instrucción se acepta y se comporta como una transacción explícita: suma 1 a `@@TRANCOUNT` y se cierra con `COMMIT`. Se captura cualquier error en un `TRY/CATCH` y se lo registra.

<!-- check: U3.20 -->
```sql
DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(50), Valor VARCHAR(80));
DECLARE @Anidamiento INT, @Error INT, @Mensaje NVARCHAR(200);

BEGIN TRY
    BEGIN DISTRIBUTED TRANSACTION TransferenciaEntreNodos;
    SET @Anidamiento = @@TRANCOUNT;
    INSERT INTO @Observacion VALUES (1, '@@TRANCOUNT tras BEGIN DISTRIBUTED', CAST(@Anidamiento AS VARCHAR(10)));
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;
    COMMIT TRANSACTION;
    INSERT INTO @Observacion VALUES (2, 'COMMIT', 'confirmada');
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    SET @Mensaje = ERROR_MESSAGE();
    IF XACT_STATE() <> 0 ROLLBACK TRANSACTION;
    INSERT INTO @Observacion VALUES (3, 'error', CAST(@Error AS VARCHAR(10)));
    INSERT INTO @Observacion VALUES (4, 'mensaje', LEFT(@Mensaje, 80));
END CATCH;

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Momento | Valor |
|---:|---|---|
| 1 | @@TRANCOUNT tras BEGIN DISTRIBUTED | 1 |
| 2 | COMMIT | confirmada |

Esto comprueba la sintaxis y el manejo de `@@TRANCOUNT`, no la **participación remota**: la coordinación con otras instancias exige un servidor vinculado y MS DTC configurado entre equipos, algo que este ejercicio no ejecuta (el ejemplo de la teoría tampoco se probó en un motor: necesita esa infraestructura).
</details>

### Nivel avanzado

#### Ejercicio 17 · Rango bloqueado con y sin índice
<!-- ejercicio: U3.17 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
En `SERIALIZABLE`, leé las cuentas con `Saldo BETWEEN 1000 AND 4000` primero **sin** índice sobre `Saldo` y después **con** `IX_Cuenta_Saldo`. Listá los locks `KEY` de cada caso. ¿Cuántos son y qué rango cubre cada uno? ¿Qué consecuencia tiene para otras sesiones?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para evitar fantasmas, `SERIALIZABLE` bloquea el **rango de claves** del índice que recorre. Sin índice sobre `Saldo` el motor recorre el índice clúster entero (por `CuentaId`): bloquea todas sus claves y el final de la tabla. Con el índice sobre `Saldo`, hace una búsqueda de rango y bloquea solo las claves del rango y la siguiente.

<!-- check: U3.17 -->
```sql
DECLARE @Candado TABLE (Orden INT, Escenario VARCHAR(30), Recurso VARCHAR(20), Modo VARCHAR(10), Cantidad INT);
DECLARE @Total DECIMAL(12,2);

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Sin índice sobre Saldo: el predicado recorre toda la tabla.
BEGIN TRANSACTION;
    SELECT @Total = SUM(Saldo) FROM banco.Cuenta WHERE Saldo BETWEEN 1000 AND 4000;
    INSERT INTO @Candado
    SELECT 1, 'sin índice sobre Saldo', resource_type, request_mode, COUNT(*) FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type NOT IN ('DATABASE', 'METADATA')
    GROUP BY resource_type, request_mode;
COMMIT TRANSACTION;

CREATE INDEX IX_Cuenta_Saldo ON banco.Cuenta (Saldo);

-- Con índice: se bloquea solo el rango del índice.
BEGIN TRANSACTION;
    SELECT @Total = SUM(Saldo) FROM banco.Cuenta WHERE Saldo BETWEEN 1000 AND 4000;
    INSERT INTO @Candado
    SELECT 2, 'con IX_Cuenta_Saldo', resource_type, request_mode, COUNT(*) FROM sys.dm_tran_locks
    WHERE request_session_id = @@SPID AND resource_database_id = DB_ID() AND resource_type NOT IN ('DATABASE', 'METADATA')
    GROUP BY resource_type, request_mode;
COMMIT TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

SELECT Escenario, Recurso, Modo, Cantidad FROM @Candado ORDER BY Orden, Recurso, Modo;
```

**Resultado esperado.**

| Escenario | Recurso | Modo | Cantidad |
|---|---|---|---:|
| sin índice sobre Saldo | KEY | RangeS-S | 4 |
| sin índice sobre Saldo | OBJECT | IS | 1 |
| sin índice sobre Saldo | PAGE | IS | 1 |
| con IX_Cuenta_Saldo | KEY | RangeS-S | 2 |
| con IX_Cuenta_Saldo | OBJECT | IS | 1 |
| con IX_Cuenta_Saldo | PAGE | IS | 1 |

Sin índice hay 4 locks `RangeS-S` (las tres filas y el final del índice): ninguna otra sesión puede insertar una cuenta nueva, aunque su saldo no esté en el rango. Con el índice solo hay 2 (la fila con saldo 3200, que está en el rango, y la clave siguiente, 5000, que marca su límite): únicamente las inserciones con saldo en ese rango quedarían esperando. Un índice adecuado reduce el alcance de los locks.
</details>

#### Ejercicio 18 · Actualización perdida y control optimista
<!-- ejercicio: U3.18 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Dos cajeros operan la cuenta 1 (saldo 5000). El cajero A lee el saldo y la versión de la fila; mientras tanto el cajero B retira 4000 y confirma; después A intenta retirar 700 a partir de lo que leyó. Implementá un **control optimista** con una columna `ROWVERSION` que impida la actualización perdida y mostrá qué ocurre con la actualización de A. La simulación se hace con una sola sesión: las dos "sesiones" son sentencias consecutivas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se agrega una columna `Version ROWVERSION`, que el motor cambia con cada modificación de la fila. A guarda el saldo y la versión que leyó y condiciona su `UPDATE` con `WHERE Version = @VersionA`. Si B modificó la fila entre la lectura y la escritura, la versión cambió, el `WHERE` no encuentra la fila y el `UPDATE` afecta 0 filas: la aplicación detecta el conflicto con `@@ROWCOUNT` y reintenta con el valor actual, en lugar de pisar el cambio de B.

<!-- check: U3.18 -->
```sql
-- Se agrega una columna de versión de fila para detectar la modificación concurrente.
ALTER TABLE banco.Cuenta ADD Version ROWVERSION;
GO
DECLARE @Observacion TABLE (Orden INT, Paso VARCHAR(70), Valor VARCHAR(40));
DECLARE @SaldoLeidoA DECIMAL(12,2), @VersionA BINARY(8), @Filas INT;

-- El cajero A lee el saldo y la versión.
SELECT @SaldoLeidoA = Saldo, @VersionA = Version FROM banco.Cuenta WHERE CuentaId = 1;

-- Mientras tanto el cajero B retira 4000 y confirma (otra "sesión", simulada con una sentencia propia).
UPDATE banco.Cuenta SET Saldo = Saldo - 4000 WHERE CuentaId = 1;

-- El cajero A intenta retirar 700 a partir de lo que leyó: la condición sobre la versión falla.
UPDATE banco.Cuenta SET Saldo = @SaldoLeidoA - 700
WHERE CuentaId = 1 AND Version = @VersionA;
SET @Filas = @@ROWCOUNT;

INSERT INTO @Observacion VALUES (1, 'saldo que leyó A', CAST(@SaldoLeidoA AS VARCHAR(20)));
INSERT INTO @Observacion VALUES (2, 'filas modificadas por la actualización de A', CAST(@Filas AS VARCHAR(10)));
INSERT INTO @Observacion SELECT 3, 'saldo final en la tabla', CAST(Saldo AS VARCHAR(20)) FROM banco.Cuenta WHERE CuentaId = 1;

SELECT Orden, Paso, Valor FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Paso | Valor |
|---:|---|---|
| 1 | saldo que leyó A | 5000.00 |
| 2 | filas modificadas por la actualización de A | 0 |
| 3 | saldo final en la tabla | 1000.00 |

A leyó 5000, B dejó la cuenta en 1000 y el `UPDATE` de A modificó 0 filas: el saldo final es 1000, el de B. Sin el control, A habría escrito 5000 − 700 = 4300 y habría perdido el retiro de B. Con dos sesiones reales, la alternativa pesimista es leer con `UPDLOCK` dentro de una transacción, y la de `SNAPSHOT`, que da el error 3960 en lugar de perder la actualización.
</details>

#### Ejercicio 25 · Deadlock con víctima conocida
<!-- ejercicio: U3.25 | nivel: avanzado | tipo: diagnostico | verificacion: revisado -->

:::note[Enunciado]
Provocá un deadlock entre dos sesiones que actualizan las cuentas 1 y 2 en orden inverso. Hacé que la sesión A sea siempre la víctima con `SET DEADLOCK_PRIORITY`, capturá el error 1205 en un `CATCH` y mostrá el estado final. Explicá cómo se evitaría el deadlock.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada sesión toma un `X` sobre su primera fila, espera con `WAITFOR` para asegurar el cruce, y pide la fila de la otra. Como A tiene `DEADLOCK_PRIORITY LOW` y B tiene `HIGH`, el monitor de deadlocks elige a A como víctima sin importar el costo de reversión. Reiniciá el entorno antes de empezar.

**Sesión A** (se ejecuta primero):

<!-- check: U3.25 -->
```sql
SET DEADLOCK_PRIORITY LOW;
SET XACT_ABORT ON;

BEGIN TRY
    BEGIN TRANSACTION;
        UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;
        WAITFOR DELAY '00:00:10';
        UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 2;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Error, XACT_STATE() AS Estado;
    IF XACT_STATE() <> 0
        ROLLBACK TRANSACTION;
END CATCH;
```

**Sesión B** (dentro de los 10 segundos de A):

<!-- check: U3.25 -->
```sql
SET DEADLOCK_PRIORITY HIGH;

BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 2;
    WAITFOR DELAY '00:00:05';
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;
COMMIT TRANSACTION;

SELECT CuentaId, Saldo FROM banco.Cuenta WHERE CuentaId IN (1, 2) ORDER BY CuentaId;
```

**Resultado esperado** (según la documentación; no se probó en un motor):

| Sesión | Resultado |
|---|---|
| A | Su segundo `UPDATE` queda esperando la fila 2 (tomada por B); B pide la fila 1 (tomada por A): ciclo. El monitor elige a A (prioridad `LOW`) y su `CATCH` devuelve `Error` = 1205; la transacción de A se revierte |
| B | Su segundo `UPDATE` se completa cuando A libera la fila 1 y su `COMMIT` confirma |
| Estado final (`SELECT` de B) | Cuenta 1 = 5001 y cuenta 2 = 3201: solo quedaron los cambios de B |

El deadlock se evitaría haciendo que **ambas** sesiones accedan a las filas en el mismo orden (por ejemplo, siempre la cuenta de menor `CuentaId` primero): la segunda sesión esperaría la primera fila sin haber tomado nada y no habría ciclo. La aplicación debería, además, **reintentar** la transacción de A (ver el procedimiento con reintentos de la teoría).
</details>

## Fuentes

- Presentación de cátedra, Unidad 3, control de concurrencia y transacciones distribuidas, v1.0, 2023.
- Microsoft Learn: [SET TRANSACTION ISOLATION LEVEL](https://learn.microsoft.com/es-es/sql/t-sql/statements/set-transaction-isolation-level-transact-sql), [Guía de bloqueo de transacciones y versiones de fila](https://learn.microsoft.com/es-es/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide), [sys.dm_tran_locks](https://learn.microsoft.com/es-es/sql/relational-databases/system-dynamic-management-views/sys-dm-tran-locks-transact-sql), [Isolation levels in the Database Engine](https://learn.microsoft.com/es-es/sql/t-sql/statements/set-transaction-isolation-level-transact-sql#arguments).
