---
title: Laboratorio TCL
slug: bbdd-aplicadas/unidad-3/practica/laboratorio-tcl
sidebar:
  order: 1
---

[← Unidad 3](/bbdd-aplicadas/unidad-3/teoria/)

Esta práctica tiene dos partes. La **parte 1** son diez ejercicios de **una sola sesión** sobre el control de transacciones (`BEGIN`, `COMMIT`, `ROLLBACK`, `SAVE TRANSACTION`, `@@TRANCOUNT`, `TRY/CATCH`, `XACT_STATE`, `XACT_ABORT`); todos se ejecutaron en SQL Server 2022 y los resultados esperados son los reales. La **parte 2** es un laboratorio guiado de **dos o tres sesiones** con una tarjeta de crédito: muestra qué ve y qué espera cada sesión según el nivel de aislamiento.

**Teoría previa**: [Control de transacciones (TCL)](/bbdd-aplicadas/unidad-3/teoria/transacciones-y-concurrencia/) para la parte 1 y [Concurrencia, bloqueos y transacciones distribuidas](/bbdd-aplicadas/unidad-3/teoria/transacciones-concurrencia/) para la parte 2.

Los scripts se ejecutan en una **base de pruebas propia** (por ejemplo, una base nueva llamada `LabTransacciones`). Cada ejercicio parte del estado que deja el script de preparación: volvé a ejecutarlo antes de cada uno.

---

## Parte 1. Ejercicios de una sesión

### Preparación

Crea el esquema `banco` con las tablas `Cuenta` y `Movimiento`. Se puede ejecutar las veces que haga falta: borra y vuelve a crear las tablas.

<!-- check: U3.T.TX.13 -->
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

SELECT CuentaId, Titular, Saldo
FROM banco.Cuenta
ORDER BY CuentaId;
```

**Resultado esperado.**

| CuentaId | Titular | Saldo |
|---:|---|---:|
| 1 | Cliente 01 | 5000.00 |
| 2 | Cliente 02 | 3200.00 |
| 3 | Cliente 03 | 800.00 |

En los ejercicios, las observaciones se guardan en una **variable de tabla** (`@Observacion`): a diferencia de una tabla temporal, no se revierte con un `ROLLBACK`, así que sirve para registrar lo que pasa dentro de una transacción. Las variables de sesión como `@@TRANCOUNT` y `XACT_STATE()` se copian primero a una variable porque dentro de un `INSERT` se evalúan en la transacción de esa misma sentencia.

### Nivel inicial

#### Ejercicio 1 · Transferencia confirmada
<!-- ejercicio: U3.01 | nivel: inicial | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Transferí 700 pesos de la cuenta 2 a la cuenta 3 dentro de una transacción explícita. Registrá un movimiento de débito en la cuenta 2 y uno de crédito en la cuenta 3. Al terminar, mostrá por cada cuenta el saldo y la cantidad de movimientos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los dos `UPDATE` y los dos `INSERT` forman una unidad: se encierran entre `BEGIN TRANSACTION` y `COMMIT` para que se confirmen juntos. La consulta final usa `LEFT JOIN` para incluir la cuenta 1, que no tuvo movimientos.

<!-- check: U3.01 -->
```sql
BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo - 700 WHERE CuentaId = 2;
    UPDATE banco.Cuenta SET Saldo = Saldo + 700 WHERE CuentaId = 3;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion)
    VALUES (2, 'D', 700, 'Transferencia a cuenta 3'),
           (3, 'C', 700, 'Transferencia de cuenta 2');
COMMIT TRANSACTION;

SELECT c.CuentaId, c.Saldo, COUNT(m.MovimientoId) AS Movimientos
FROM banco.Cuenta AS c
LEFT JOIN banco.Movimiento AS m ON m.CuentaId = c.CuentaId
GROUP BY c.CuentaId, c.Saldo
ORDER BY c.CuentaId;
```

**Resultado esperado.**

| CuentaId | Saldo | Movimientos |
|---:|---:|---:|
| 1 | 5000.00 | 0 |
| 2 | 2500.00 | 1 |
| 3 | 1500.00 | 1 |

La cuenta 2 queda con 3200 − 700 = 2500 y la 3 con 800 + 700 = 1500, y cada una tiene un movimiento. La cuenta 1 no cambió.
</details>

#### Ejercicio 2 · Modo implícito
<!-- ejercicio: U3.02 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Activá `IMPLICIT_TRANSACTIONS`. Sin escribir `BEGIN TRANSACTION`, sumá 250 al saldo de la cuenta 1 y leé `@@TRANCOUNT` y el saldo. Después hacé `ROLLBACK` y comprobá que el saldo volvió al original. Explicá por qué hay que cerrar también la transacción que abre el `SELECT` posterior.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En modo implícito, el primer `UPDATE` abre la transacción (`@@TRANCOUNT` = 1). El `ROLLBACK` la deshace. Pero en ese modo **cualquier** sentencia posterior que lo requiera abre otra, incluso un `SELECT` sobre una tabla: para no dejarla abierta, se cierra con `COMMIT` antes de desactivar la opción.

<!-- check: U3.02 -->
```sql
DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(50), Trancount INT, SaldoCuenta1 DECIMAL(12,2));
DECLARE @Anidamiento INT, @Saldo DECIMAL(12,2);

SET IMPLICIT_TRANSACTIONS ON;

UPDATE banco.Cuenta SET Saldo = Saldo + 250 WHERE CuentaId = 1;   -- abre la transacción sin BEGIN
SET @Anidamiento = @@TRANCOUNT;
SELECT @Saldo = Saldo FROM banco.Cuenta WHERE CuentaId = 1;
INSERT INTO @Observacion VALUES (1, 'después del UPDATE', @Anidamiento, @Saldo);

ROLLBACK TRANSACTION;

SET @Anidamiento = @@TRANCOUNT;
SELECT @Saldo = Saldo FROM banco.Cuenta WHERE CuentaId = 1;   -- este SELECT abre otra transacción
COMMIT TRANSACTION;
SET IMPLICIT_TRANSACTIONS OFF;
INSERT INTO @Observacion VALUES (2, 'después del ROLLBACK', @Anidamiento, @Saldo);

SELECT Orden, Momento, Trancount, SaldoCuenta1 FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Momento | Trancount | SaldoCuenta1 |
|---:|---|---:|---:|
| 1 | después del UPDATE | 1 | 5250.00 |
| 2 | después del ROLLBACK | 0 | 5000.00 |

El `SELECT` que lee el saldo después del `ROLLBACK` mostró `@@TRANCOUNT` = 0 justo antes de ejecutarse y abrió una transacción nueva; si no se cierra, queda con sus locks.
</details>

#### Ejercicio 3 · Contador de transacciones
<!-- ejercicio: U3.03 | nivel: inicial | tipo: conceptual | verificacion: motor -->

:::note[Enunciado]
Abrí tres transacciones anidadas con `BEGIN TRANSACTION`, ejecutá un `COMMIT` y después un `ROLLBACK` sin nombre. Registrá el valor de `@@TRANCOUNT` en cada paso y explicá la última lectura.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Cada `BEGIN TRANSACTION` suma 1 y cada `COMMIT` resta 1. Un `ROLLBACK` sin nombre ignora el anidamiento: va directo a 0.

<!-- check: U3.03 -->
```sql
DECLARE @Observacion TABLE (Orden INT, Instruccion VARCHAR(30), Trancount INT);
DECLARE @N INT;

SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (1, 'al empezar', @N);
BEGIN TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (2, 'BEGIN TRANSACTION', @N);
BEGIN TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (3, 'BEGIN TRANSACTION', @N);
BEGIN TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (4, 'BEGIN TRANSACTION', @N);
COMMIT TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (5, 'COMMIT TRANSACTION', @N);
ROLLBACK TRANSACTION;
SET @N = @@TRANCOUNT;
INSERT INTO @Observacion VALUES (6, 'ROLLBACK TRANSACTION', @N);

SELECT Orden, Instruccion, Trancount FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Instruccion | Trancount |
|---:|---|---:|
| 1 | al empezar | 0 |
| 2 | BEGIN TRANSACTION | 1 |
| 3 | BEGIN TRANSACTION | 2 |
| 4 | BEGIN TRANSACTION | 3 |
| 5 | COMMIT TRANSACTION | 2 |
| 6 | ROLLBACK TRANSACTION | 0 |

Tras el `COMMIT` el contador baja a 2 y no se confirmó nada en disco. El `ROLLBACK` lo lleva a 0 y deshace todas las modificaciones hechas desde el primer `BEGIN`.
</details>

#### Ejercicio 4 · Verdadero o falso: TCL y ACID
<!-- ejercicio: U3.04 | nivel: inicial | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Indicá si cada afirmación es verdadera o falsa y justificá.

1. En autocommit, un `UPDATE` que modifica 100 filas y falla en la fila 60 deja las primeras 59 modificadas.
2. Con `@@TRANCOUNT` = 3, un `ROLLBACK TRANSACTION` sin nombre deja `@@TRANCOUNT` en 0.
3. El `COMMIT` de una transacción anidada hace durables sus cambios.
4. Si `XACT_STATE()` vale −1 y no hubo más sentencias, un `COMMIT` es válido.
5. Con `IMPLICIT_TRANSACTIONS ON`, un `SELECT` sobre una tabla abre una transacción.
6. La consistencia la garantiza el motor sin que el programador tenga que hacer nada.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se revisa cada afirmación contra el comportamiento de `@@TRANCOUNT`, `XACT_STATE()` y los modos de transacción.

1. **Falso.** Cada sentencia es atómica: si falla, el motor deshace los cambios que había hecho esa sentencia y ninguna de las 59 filas queda modificada. Lo que no es atómico en autocommit es **el conjunto** de dos sentencias distintas.
2. **Verdadero.** Un `ROLLBACK` sin nombre deshace todo y lleva el contador a 0 (ejercicio 3).
3. **Falso.** Solo baja `@@TRANCOUNT`. Los cambios se confirman con el `COMMIT` que lo lleva a 0.
4. **Falso.** Con `XACT_STATE() = -1` la transacción está condenada: un `COMMIT` da el error 3930 y solo se puede hacer `ROLLBACK`.
5. **Verdadero.** Se comprobó en el ejemplo de modos de transacción: el `SELECT` dejó `@@TRANCOUNT` = 1.
6. **Falso.** El motor verifica las restricciones declaradas (`CHECK`, `FOREIGN KEY`, etc.); las reglas de negocio que no están declaradas son responsabilidad de quien programa la transacción.
</details>

### Nivel intermedio

#### Ejercicio 5 · TRY/CATCH con una violación de restricción
<!-- ejercicio: U3.05 | nivel: intermedio | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Intentá debitar 6000 pesos de la cuenta 3 (saldo 800), que tiene `CHECK (Saldo >= 0)`. Dentro de un `TRY/CATCH`, capturá el número de error, la restricción involucrada y `XACT_STATE()`, hacé `ROLLBACK` y comprobá que el saldo no cambió. Respondé: ¿qué número devuelve `ERROR_NUMBER()`? ¿Qué pasaría si el `CATCH` hiciera `ROLLBACK` sin comprobar que hay una transacción?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El `UPDATE` viola `CK_Cuenta_Saldo`, el motor cancela la sentencia y salta al `CATCH`. Con `XACT_ABORT OFF` la transacción sigue abierta (`XACT_STATE()` = 1); el `CATCH` la revierte.

<!-- check: U3.05 -->
```sql
DECLARE @Observacion TABLE (Orden INT, Pregunta VARCHAR(60), Respuesta VARCHAR(80));

BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo - 6000 WHERE CuentaId = 3;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion) VALUES (3, 'D', 6000, 'Débito grande');
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    DECLARE @Numero INT = ERROR_NUMBER(), @Estado INT = XACT_STATE(), @Mensaje NVARCHAR(200) = ERROR_MESSAGE();
    INSERT INTO @Observacion VALUES (1, 'ERROR_NUMBER()', CAST(@Numero AS VARCHAR(10)));
    INSERT INTO @Observacion VALUES (2, 'restricción nombrada en el mensaje',
        IIF(@Mensaje LIKE '%CK_Cuenta_Saldo%', 'CK_Cuenta_Saldo', 'otra'));
    INSERT INTO @Observacion VALUES (3, 'XACT_STATE() antes del ROLLBACK', CAST(@Estado AS VARCHAR(10)));
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;
END CATCH;

INSERT INTO @Observacion SELECT 4, 'saldo de la cuenta 3', CAST(Saldo AS VARCHAR(20)) FROM banco.Cuenta WHERE CuentaId = 3;

SELECT Orden, Pregunta, Respuesta FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Pregunta | Respuesta |
|---:|---|---|
| 1 | ERROR_NUMBER() | 547 |
| 2 | restricción nombrada en el mensaje | CK_Cuenta_Saldo |
| 3 | XACT_STATE() antes del ROLLBACK | 1 |
| 4 | saldo de la cuenta 3 | 800.00 |

`ERROR_NUMBER()` devuelve **547** (conflicto con una restricción `CHECK` o `FOREIGN KEY`). Respecto de la segunda pregunta: en este caso el `ROLLBACK` incondicional funcionaría porque la transacción existe, pero si el error ocurre **antes** del `BEGIN TRANSACTION` (por ejemplo, una validación previa), el `ROLLBACK` falla con el error 3903 y tapa el error original; se muestra en el ejercicio 8.
</details>

#### Ejercicio 6 · SAVE TRANSACTION: el ROLLBACK TO que nunca se ejecutaba
<!-- ejercicio: U3.06 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Un compañero escribió una transacción con un savepoint: debita 200 pesos de la cuenta 1, guarda un savepoint `AntesDeB`, debita 9999 (más que el saldo) y, **después**, controla `IF saldo < 0 ROLLBACK TRANSACTION AntesDeB`. La cuenta tiene `CHECK (Saldo >= 0)`. Ejecutalo y explicá por qué el `ROLLBACK TO` nunca corre. Después corregilo para que se conserve el primer débito y se descarte el segundo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La restricción `CHECK` falla **durante** el `UPDATE`, antes de que llegue la sentencia `IF`: el motor cancela la sentencia (error 547) y salta al `CATCH`. El saldo nunca llega a ser negativo, así que la condición `saldo < 0` no se evalúa ni se cumple. La corrección es resolver el caso en el `CATCH`: con `XACT_STATE() = 1` la transacción sigue siendo confirmable, se vuelve al savepoint y se confirma.

<!-- check: U3.06 -->
```sql
DECLARE @Observacion TABLE (Orden INT, Variante VARCHAR(70), Detalle VARCHAR(80));
DECLARE @Salto BIT = 0;

-- Variante original: el CHECK falla antes del IF, así que el ROLLBACK TO nunca se ejecuta.
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo - 200 WHERE CuentaId = 1;
    SAVE TRANSACTION AntesDeB;
    UPDATE banco.Cuenta SET Saldo = Saldo - 9999 WHERE CuentaId = 1;   -- error 547: no hay IF que lo vea
    IF (SELECT Saldo FROM banco.Cuenta WHERE CuentaId = 1) < 0
    BEGIN
        SET @Salto = 1;
        ROLLBACK TRANSACTION AntesDeB;
    END;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    DECLARE @Error INT = ERROR_NUMBER(), @Estado INT = XACT_STATE();
    INSERT INTO @Observacion VALUES (1, 'sin XACT_ABORT: ¿se ejecutó el ROLLBACK TO?', IIF(@Salto = 1, 'sí', 'no'));
    INSERT INTO @Observacion VALUES (2, 'sin XACT_ABORT: error y XACT_STATE()', CONCAT(@Error, ' / ', @Estado));
    -- XACT_STATE() = 1: se puede volver al savepoint y confirmar lo anterior.
    IF @Estado = 1
    BEGIN
        ROLLBACK TRANSACTION AntesDeB;
        COMMIT TRANSACTION;
    END;
END CATCH;

INSERT INTO @Observacion SELECT 3, 'saldo de la cuenta 1 tras la variante corregida', CAST(Saldo AS VARCHAR(20))
    FROM banco.Cuenta WHERE CuentaId = 1;

SELECT Orden, Variante, Detalle FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Variante | Detalle |
|---:|---|---|
| 1 | sin XACT_ABORT: ¿se ejecutó el ROLLBACK TO? | no |
| 2 | sin XACT_ABORT: error y XACT_STATE() | 547 / 1 |
| 3 | saldo de la cuenta 1 tras la variante corregida | 4800.00 |

El `ROLLBACK TRANSACTION AntesDeB` del `IF` no se ejecutó (fila 1), el error fue 547 con `XACT_STATE()` = 1 (fila 2), y tras volver al savepoint y confirmar, el saldo es 5000 − 200 = 4800: se conservó el primer débito y se descartó el segundo. El error de un enunciado anterior de esta práctica era justamente este: el resultado coincidía por casualidad, pero la demostración del savepoint no era correcta.
</details>

#### Ejercicio 7 · XACT_ABORT con una clave foránea
<!-- ejercicio: U3.07 | nivel: intermedio | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Sumá 10 pesos a la cuenta 1 e insertá un movimiento para la cuenta 999, que no existe (viola la clave foránea). Hacelo dos veces dentro de `TRY/CATCH`: con `XACT_ABORT OFF` y con `XACT_ABORT ON`. Registrá el error, `XACT_STATE()` y el saldo de la cuenta 1. Respondé: ¿cuándo conviene combinar `XACT_ABORT ON` con `TRY/CATCH`?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Con `OFF`, el error termina solo el `INSERT` y la transacción sigue confirmable (`XACT_STATE()` = 1): si el `CATCH` la confirma, el `+10` queda. Con `ON` el mismo error condena la transacción (`-1`) y solo se puede revertir.

<!-- check: U3.07 -->
```sql
DECLARE @Observacion TABLE (Orden INT, XactAbort VARCHAR(3), Error INT, Estado INT, SaldoCuenta1 DECIMAL(12,2));
DECLARE @Error INT, @Estado INT, @Saldo DECIMAL(12,2);

-- XACT_ABORT OFF: el INSERT con FK inválida falla pero la transacción sigue abierta.
SET XACT_ABORT OFF;
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo + 10 WHERE CuentaId = 1;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto) VALUES (999, 'C', 10);
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    SET @Estado = XACT_STATE();
    SELECT @Saldo = Saldo FROM banco.Cuenta WHERE CuentaId = 1;
    INSERT INTO @Observacion VALUES (1, 'OFF', @Error, @Estado, @Saldo);
    IF @Estado = 1 COMMIT TRANSACTION;     -- lo que sí se ejecutó queda confirmado
    IF @Estado = -1 ROLLBACK TRANSACTION;
END CATCH;

-- XACT_ABORT ON: el mismo error condena la transacción.
SET XACT_ABORT ON;
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE banco.Cuenta SET Saldo = Saldo + 10 WHERE CuentaId = 1;
    INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto) VALUES (999, 'C', 10);
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
    SET @Estado = XACT_STATE();
    IF @Estado = 1 COMMIT TRANSACTION;
    IF @Estado = -1 ROLLBACK TRANSACTION;
    SELECT @Saldo = Saldo FROM banco.Cuenta WHERE CuentaId = 1;
    INSERT INTO @Observacion VALUES (2, 'ON', @Error, @Estado, @Saldo);
END CATCH;
SET XACT_ABORT OFF;

SELECT Orden, XactAbort, Error, Estado, SaldoCuenta1 FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | XactAbort | Error | Estado | SaldoCuenta1 |
|---:|---|---:|---:|---:|
| 1 | OFF | 547 | 1 | 5010.00 |
| 2 | ON | 547 | -1 | 5010.00 |

Con `OFF` el `CATCH` confirmó el `+10` (saldo 5010). Con `ON` revirtió: el saldo se mantuvo en 5010, es decir, el segundo `+10` no quedó.

**Respuesta.** Siempre que una transacción vive dentro de un procedimiento. `XACT_ABORT ON` garantiza que ningún error la deje abierta y con locks a medio camino, y el `TRY/CATCH` permite decidir qué hacer (revertir, registrar, relanzar con `THROW`). Sin `TRY/CATCH`, el error corta el lote y llega al cliente.
</details>

#### Ejercicio 8 · ROLLBACK sin transacción (error 3903)
<!-- ejercicio: U3.08 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Un procedimiento valida que la cuenta exista y, si no existe, lanza un error con `THROW` **antes** de abrir la transacción. Su `CATCH` hace `ROLLBACK TRANSACTION` directamente. Mostrá qué error se ve en lugar del original y corregí el `CATCH` para que conserve el error original.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Si el `THROW` ocurre antes de `BEGIN TRANSACTION`, no hay transacción que revertir y el `ROLLBACK` falla. La corrección es comprobar `XACT_STATE() <> 0` y guardar `ERROR_NUMBER()` antes de cualquier otra sentencia.

<!-- check: U3.08 -->
```sql
DECLARE @Observacion TABLE (Orden INT, Variante VARCHAR(40), ErrorVisible INT);

-- CATCH ingenuo: ROLLBACK sin comprobar si hay transacción. El error ocurre antes del BEGIN TRANSACTION.
BEGIN TRY
    IF NOT EXISTS (SELECT 1 FROM banco.Cuenta WHERE CuentaId = 99)
        THROW 50010, 'La cuenta no existe.', 1;
    BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 99;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    BEGIN TRY
        ROLLBACK TRANSACTION;                -- no hay transacción abierta
    END TRY
    BEGIN CATCH
        INSERT INTO @Observacion VALUES (1, 'ROLLBACK sin comprobar', ERROR_NUMBER());
    END CATCH;
END CATCH;

-- CATCH correcto: se comprueba XACT_STATE() y se conserva el error original.
BEGIN TRY
    IF NOT EXISTS (SELECT 1 FROM banco.Cuenta WHERE CuentaId = 99)
        THROW 50010, 'La cuenta no existe.', 1;
    BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 99;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    DECLARE @Original INT = ERROR_NUMBER();
    IF XACT_STATE() <> 0
        ROLLBACK TRANSACTION;
    INSERT INTO @Observacion VALUES (2, 'con XACT_STATE()', @Original);
END CATCH;

SELECT Orden, Variante, ErrorVisible FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Variante | ErrorVisible |
|---:|---|---:|
| 1 | ROLLBACK sin comprobar | 3903 |
| 2 | con XACT_STATE() | 50010 |

El `ROLLBACK` sin comprobar produce el error **3903** (*The ROLLBACK TRANSACTION request has no corresponding BEGIN TRANSACTION*), que reemplaza al error 50010 que se quería informar. Con `XACT_STATE()` el `CATCH` se salta el `ROLLBACK` y el error original (50010) se conserva.
</details>

### Nivel avanzado

#### Ejercicio 9 · Lote de transferencias todo o nada
<!-- ejercicio: U3.09 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Escribí un procedimiento `banco.TransferirLote` que reciba un conjunto de transferencias (origen, destino, monto) y las aplique **todas o ninguna**. Usá un tipo de tabla como parámetro, un solo `UPDATE` que aplique el neto por cuenta y los movimientos correspondientes. Probalo con un lote válido y con uno en el que una cuenta quedaría con saldo negativo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un tipo de tabla (`CREATE TYPE ... AS TABLE`) permite pasar varias filas como parámetro de solo lectura. El `UPDATE` calcula, por cuenta, el neto del lote (créditos menos débitos) y lo aplica de una vez; si el saldo resultante de **cualquier** cuenta es negativo, el `CHECK` hace fallar la sentencia, `XACT_ABORT ON` condena la transacción y el `CATCH` la revierte, con lo que no queda ninguna transferencia del lote. Al aplicar el neto, el orden de las transferencias dentro del lote no importa.

<!-- check: U3.09 -->
```sql
DROP PROCEDURE IF EXISTS banco.TransferirLote;
DROP TYPE IF EXISTS banco.TransferenciaTipo;
GO
CREATE TYPE banco.TransferenciaTipo AS TABLE
(
    Origen  INT           NOT NULL,
    Destino INT           NOT NULL,
    Monto   DECIMAL(12,2) NOT NULL CHECK (Monto > 0)
);
GO
CREATE OR ALTER PROCEDURE banco.TransferirLote
    @Lote banco.TransferenciaTipo READONLY
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        UPDATE c
        SET c.Saldo = c.Saldo + n.Neto
        FROM banco.Cuenta AS c
        JOIN (SELECT CuentaId, SUM(Monto) AS Neto
              FROM (SELECT Origen AS CuentaId, -Monto AS Monto FROM @Lote
                    UNION ALL
                    SELECT Destino, Monto FROM @Lote) AS m
              GROUP BY CuentaId) AS n ON n.CuentaId = c.CuentaId;

        INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion)
        SELECT Origen, 'D', Monto, CONCAT('Lote: a cuenta ', Destino) FROM @Lote
        UNION ALL
        SELECT Destino, 'C', Monto, CONCAT('Lote: de cuenta ', Origen) FROM @Lote;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0
            ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
GO
DECLARE @Valido banco.TransferenciaTipo, @Invalido banco.TransferenciaTipo;
INSERT INTO @Valido VALUES (1, 2, 300), (2, 3, 100);
INSERT INTO @Invalido VALUES (1, 2, 300), (3, 1, 1000);   -- la cuenta 3 queda con solo 900

DECLARE @Observacion TABLE (Orden INT, Lote VARCHAR(10), Error INT);
EXEC banco.TransferirLote @Valido;
INSERT INTO @Observacion VALUES (1, 'válido', 0);
BEGIN TRY
    EXEC banco.TransferirLote @Invalido;
END TRY
BEGIN CATCH
    INSERT INTO @Observacion VALUES (2, 'inválido', ERROR_NUMBER());
END CATCH;

SELECT Orden, Lote, Error FROM @Observacion ORDER BY Orden;
SELECT CuentaId, Saldo FROM banco.Cuenta ORDER BY CuentaId;
SELECT COUNT(*) AS Movimientos FROM banco.Movimiento;
```

**Resultado esperado.**

Resultado de cada lote (0 es éxito, 547 es la violación de `CK_Cuenta_Saldo`):

| Orden | Lote | Error |
|---:|---|---:|
| 1 | válido | 0 |
| 2 | inválido | 547 |

Saldos finales:

| CuentaId | Saldo |
|---:|---:|
| 1 | 4700.00 |
| 2 | 3400.00 |
| 3 | 900.00 |

Cantidad de movimientos:

| Movimientos |
|---:|
| 4 |

El lote válido movió 300 de la cuenta 1 a la 2 y 100 de la 2 a la 3 (4 movimientos). En el lote inválido, la cuenta 3 (900) quedaría en −100 (900 − 1000), por lo que el lote entero se revirtió: ni siquiera la primera transferencia, que sí era válida, quedó aplicada.
</details>

#### Ejercicio 10 · Procedimiento que participa de una transacción mayor
<!-- ejercicio: U3.10 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Escribí un procedimiento `banco.AcreditarConMovimiento` que acredite un monto y registre el movimiento, y que funcione **tanto** si se lo llama solo **como** si se lo llama dentro de una transacción abierta por otro código. Si falla, debe deshacer solo lo suyo cuando lo llaman dentro de una transacción mayor y la transacción entera cuando es dueño de ella. Probalo con un monto inválido (−50) solo y dentro de una transacción mayor, y después con uno válido.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Al entrar se lee `@@TRANCOUNT`. Si es 0, el procedimiento abre su transacción y es responsable de confirmarla o revertirla. Si no, crea un **savepoint** y, ante un error, vuelve a él: el trabajo del llamador queda intacto y el llamador decide qué hacer. Si `XACT_STATE() = -1`, la transacción está condenada y solo queda `ROLLBACK` completo. Un `ROLLBACK` incondicional en un procedimiento anidado revertiría también el trabajo del llamador.

<!-- check: U3.10 -->
```sql
CREATE OR ALTER PROCEDURE banco.AcreditarConMovimiento
    @CuentaId INT,
    @Monto    DECIMAL(12, 2)
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @AnidamientoInicial INT = @@TRANCOUNT;

    IF @AnidamientoInicial = 0
        BEGIN TRANSACTION;                       -- el procedimiento es dueño de la transacción
    ELSE
        SAVE TRANSACTION AcreditarConMovimiento; -- participa de la del llamador

    BEGIN TRY
        UPDATE banco.Cuenta SET Saldo = Saldo + @Monto WHERE CuentaId = @CuentaId;
        INSERT INTO banco.Movimiento (CuentaId, Tipo, Monto, Descripcion)
        VALUES (@CuentaId, 'C', @Monto, 'Acreditación');

        IF @AnidamientoInicial = 0
            COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() = -1
            ROLLBACK TRANSACTION;                -- condenada: solo se puede revertir todo
        ELSE IF @AnidamientoInicial = 0
            ROLLBACK TRANSACTION;
        ELSE
            ROLLBACK TRANSACTION AcreditarConMovimiento;  -- deshace solo lo del procedimiento
        THROW;
    END CATCH;
END;
GO
DECLARE @Observacion TABLE (Orden INT, Momento VARCHAR(70), Valor VARCHAR(40));

-- 1) Llamada suelta con un monto inválido (el INSERT viola CK_Movimiento_Monto).
BEGIN TRY
    EXEC banco.AcreditarConMovimiento @CuentaId = 1, @Monto = -50;
END TRY
BEGIN CATCH
    INSERT INTO @Observacion VALUES (1, 'llamada suelta: error', CAST(ERROR_NUMBER() AS VARCHAR(10)));
END CATCH;
INSERT INTO @Observacion SELECT 2, 'llamada suelta: saldo de la cuenta 1', CAST(Saldo AS VARCHAR(40))
    FROM banco.Cuenta WHERE CuentaId = 1;

-- 2) Llamada dentro de una transacción mayor.
BEGIN TRANSACTION;
    UPDATE banco.Cuenta SET Saldo = Saldo + 1 WHERE CuentaId = 1;
    BEGIN TRY
        EXEC banco.AcreditarConMovimiento @CuentaId = 1, @Monto = -50;
    END TRY
    BEGIN CATCH
        INSERT INTO @Observacion VALUES (3, 'dentro de la transacción: error', CAST(ERROR_NUMBER() AS VARCHAR(10)));
    END CATCH;
    DECLARE @Estado INT = XACT_STATE();
    INSERT INTO @Observacion VALUES (4, 'XACT_STATE() de la transacción del llamador', CAST(@Estado AS VARCHAR(10)));
    EXEC banco.AcreditarConMovimiento @CuentaId = 1, @Monto = 25;
COMMIT TRANSACTION;

INSERT INTO @Observacion SELECT 5, 'saldo final de la cuenta 1', CAST(Saldo AS VARCHAR(40))
    FROM banco.Cuenta WHERE CuentaId = 1;
INSERT INTO @Observacion SELECT 6, 'movimientos registrados', CAST(COUNT(*) AS VARCHAR(40)) FROM banco.Movimiento;

SELECT Orden, Momento, Valor FROM @Observacion ORDER BY Orden;
```

**Resultado esperado.**

| Orden | Momento | Valor |
|---:|---|---|
| 1 | llamada suelta: error | 547 |
| 2 | llamada suelta: saldo de la cuenta 1 | 5000.00 |
| 3 | dentro de la transacción: error | 547 |
| 4 | XACT_STATE() de la transacción del llamador | 1 |
| 5 | saldo final de la cuenta 1 | 5026.00 |
| 6 | movimientos registrados | 1 |

Llamado solo, el error 547 revirtió su propia transacción (saldo sin cambios en 5000). Dentro de la transacción mayor, el procedimiento volvió a su savepoint: la transacción del llamador siguió confirmable (`XACT_STATE()` = 1) y su `+1` se conservó. El crédito válido de 25 se sumó y el `COMMIT` dejó 5000 + 1 + 25 = 5026, con un solo movimiento registrado (el del crédito válido).
</details>

---

## Parte 2. Laboratorio guiado: tarjeta de crédito

Escenario: una tabla de tarjetas con su límite de crédito disponible y una tabla de transacciones (ventas `V` y reversiones `R`). Cada venta descuenta el límite; cada reversión lo repone. Los experimentos muestran qué ve y qué espera cada sesión según el nivel de aislamiento.

:::note[Cómo leer los experimentos]
El **experimento 0** usa una sola sesión y se ejecutó en el motor. Los experimentos 1 a 3 necesitan **dos o tres ventanas de consulta** (cada una es una sesión independiente) y no se ejecutan en la verificación automática: el "resultado esperado" es lo que garantiza el motor según la documentación de SQL Server, y quedan registrados como pendientes de verificación específica. Se ejecuta la sesión A y, **dentro de la espera de la sesión A**, la B (y la C). Las esperas con `WAITFOR DELAY` están calculadas para darte tiempo.
:::

### Entorno

Crea las tablas `banco.TarjetaCredito` y `banco.TransaccionTarjeta` con cuatro tarjetas de ejemplo. El índice sobre `NroTarjeta` hace que los bloqueos de rango del experimento 3 queden acotados a esa tarjeta. Es también el script de **reinicio**: se lo vuelve a ejecutar antes de cada experimento.

<!-- check: U3.T.TX.11 -->
```sql
IF SCHEMA_ID('banco') IS NULL
    EXEC ('CREATE SCHEMA banco');
GO
DROP TABLE IF EXISTS banco.TransaccionTarjeta;
DROP TABLE IF EXISTS banco.TarjetaCredito;
GO
CREATE TABLE banco.TarjetaCredito (
    NroTarjeta    BIGINT        NOT NULL CONSTRAINT PK_TarjetaCredito PRIMARY KEY,
    Ciudad        VARCHAR(50)   NOT NULL,
    LimiteCredito DECIMAL(12,2) NOT NULL
);
CREATE TABLE banco.TransaccionTarjeta (
    TransaccionId        INT           NOT NULL CONSTRAINT PK_TransaccionTarjeta PRIMARY KEY,
    NroTarjeta           BIGINT        NOT NULL CONSTRAINT FK_TransaccionTarjeta_Tarjeta
                                       REFERENCES banco.TarjetaCredito (NroTarjeta),
    Fecha                DATETIME      NOT NULL,
    Monto                DECIMAL(12,2) NOT NULL,
    TransaccionOrigenId  INT           NULL CONSTRAINT FK_TransaccionTarjeta_Origen
                                       REFERENCES banco.TransaccionTarjeta (TransaccionId),
    Tipo                 CHAR(1)       NOT NULL CONSTRAINT CK_TransaccionTarjeta_Tipo CHECK (Tipo IN ('V', 'R'))
);
CREATE INDEX IX_TransaccionTarjeta_NroTarjeta ON banco.TransaccionTarjeta (NroTarjeta);
GO
INSERT INTO banco.TarjetaCredito (NroTarjeta, Ciudad, LimiteCredito) VALUES
    (1000000000000001, 'Ciudad A',  6000.00),
    (1000000000000002, 'Ciudad B', 16000.00),
    (1000000000000003, 'Ciudad C', 14000.00),
    (1000000000000004, 'Ciudad D', 18000.00);
GO

SELECT NroTarjeta, Ciudad, LimiteCredito FROM banco.TarjetaCredito ORDER BY NroTarjeta;
SELECT COUNT(*) AS Transacciones FROM banco.TransaccionTarjeta;
```

**Resultado esperado.**

| NroTarjeta | Ciudad | LimiteCredito |
|---:|---|---:|
| 1000000000000001 | Ciudad A | 6000.00 |
| 1000000000000002 | Ciudad B | 16000.00 |
| 1000000000000003 | Ciudad C | 14000.00 |
| 1000000000000004 | Ciudad D | 18000.00 |

| Transacciones |
|---:|
| 0 |

### Experimento 0 · Compra atómica (una sesión)

El cliente compra por 500 pesos. Si el límite disponible alcanza (incluso si es exactamente igual al monto), se registra la venta y se descuenta el límite, todo en una transacción.

<!-- check: U3.T.TX.12 -->
```sql
DECLARE @TransaccionId INT = 1001,
        @NroTarjeta    BIGINT = 1000000000000001,
        @Monto         DECIMAL(12,2) = 500.00,
        @LimiteActual  DECIMAL(12,2);

BEGIN TRANSACTION;
    SELECT @LimiteActual = LimiteCredito
    FROM banco.TarjetaCredito
    WHERE NroTarjeta = @NroTarjeta;

    IF @LimiteActual >= @Monto
    BEGIN
        INSERT INTO banco.TransaccionTarjeta (TransaccionId, NroTarjeta, Fecha, Monto, TransaccionOrigenId, Tipo)
        VALUES (@TransaccionId, @NroTarjeta, '2026-03-01T10:00:00', @Monto, NULL, 'V');

        UPDATE banco.TarjetaCredito
        SET LimiteCredito = LimiteCredito - @Monto
        WHERE NroTarjeta = @NroTarjeta;
    END;
COMMIT TRANSACTION;

SELECT t.TransaccionId, t.NroTarjeta, t.Monto, t.Tipo, c.LimiteCredito
FROM banco.TransaccionTarjeta AS t
JOIN banco.TarjetaCredito AS c ON c.NroTarjeta = t.NroTarjeta
ORDER BY t.TransaccionId;
```

**Resultado esperado.**

| TransaccionId | NroTarjeta | Monto | Tipo | LimiteCredito |
|---:|---:|---:|---|---:|
| 1001 | 1000000000000001 | 500.00 | V | 5500.00 |

La condición es `>=`: una compra por exactamente el límite disponible es válida. Como el experimento deja la venta 1001 registrada y el límite en 5500, **reiniciá el entorno** antes del siguiente.

### Experimento 1 · READ UNCOMMITTED: lectura sucia con consecuencias
<!-- ejercicio: U3.21 | nivel: intermedio | tipo: diagnostico | verificacion: revisado -->

:::note[Enunciado]
El banco prepara un cambio del límite de la tarjeta 1000000000000001 a 76000 en una transacción larga que, finalmente, se revierte. Mientras tanto, un cliente compra por 20000 con su sesión en `READ UNCOMMITTED`. Predecí qué lee el cliente, qué pasa con su `UPDATE`, y cómo queda la base cuando todo termina. Después repetí el experimento con `READ COMMITTED` y explicá la diferencia.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reiniciá el entorno (límite 6000). Ejecutá la sesión A y, dentro de sus 20 segundos de espera, la sesión B. En `READ UNCOMMITTED` la lectura de B **no pide lock `S`**, así que no espera el `X` de A y ve 76000, un dato que nunca se confirmará. El `UPDATE` de B, en cambio, necesita un `X` sobre la fila: queda esperando hasta que A haga `ROLLBACK`, y recién entonces ejecuta `LimiteCredito - 20000` sobre el valor original (6000).

**Sesión A** (banco: transacción larga que se revierte):

<!-- check: U3.21 -->
```sql
BEGIN TRANSACTION;
    UPDATE banco.TarjetaCredito
    SET LimiteCredito = 76000.00
    WHERE NroTarjeta = 1000000000000001;

    WAITFOR DELAY '00:00:20';      -- da tiempo a ejecutar la sesión B
ROLLBACK TRANSACTION;
```

**Sesión B** (cliente, `READ UNCOMMITTED`; se ejecuta mientras A espera):

<!-- check: U3.21 -->
```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

DECLARE @Limite DECIMAL(12,2);

BEGIN TRANSACTION;
    SELECT @Limite = LimiteCredito
    FROM banco.TarjetaCredito
    WHERE NroTarjeta = 1000000000000001;        -- devuelve 76000 sin esperar

    SELECT @Limite AS LimiteLeido;

    IF @Limite >= 20000.00
    BEGIN
        UPDATE banco.TarjetaCredito                -- espera el X de A hasta su ROLLBACK
        SET LimiteCredito = LimiteCredito - 20000.00
        WHERE NroTarjeta = 1000000000000001;

        INSERT INTO banco.TransaccionTarjeta (TransaccionId, NroTarjeta, Fecha, Monto, TransaccionOrigenId, Tipo)
        VALUES (1002, 1000000000000001, '2026-03-01T10:05:00', 20000.00, NULL, 'V');
    END;
COMMIT TRANSACTION;

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

SELECT NroTarjeta, LimiteCredito FROM banco.TarjetaCredito WHERE NroTarjeta = 1000000000000001;
```

**Resultado esperado** (según la documentación; no verificado en esta edición):

| Momento | Qué ocurre |
|---|---|
| B, `SELECT` | Devuelve `LimiteLeido` = 76000 de inmediato |
| B, `UPDATE` | Espera hasta que A termine su espera y haga `ROLLBACK` (unos 20 segundos desde que empezó A) |
| Después del `ROLLBACK` de A | El `UPDATE` de B se ejecuta sobre 6000 |
| Estado final | `LimiteCredito` = −14000 y la venta 1002 por 20000 registrada |

El límite queda **negativo**: B autorizó una compra sobre un dato (76000) que nunca existió, y la tabla no tiene una restricción que lo impida. Si la tabla tuviera `CHECK (LimiteCredito >= 0)`, el `UPDATE` de B fallaría con el error 547 y habría que decidir qué hacer con la venta ya insertada; el aislamiento no reemplaza a las restricciones.

**Con `READ COMMITTED`** (reiniciá el entorno y cambiá la primera línea de la sesión B por `SET TRANSACTION ISOLATION LEVEL READ COMMITTED;`): el `SELECT` de B pide un `S` sobre una fila que A tiene con `X` y **espera** hasta el `ROLLBACK`; lee entonces 6000, la condición `6000 >= 20000` es falsa y la compra no se registra. El estado final es el original (límite 6000, sin venta 1002).
</details>

### Experimento 2 · REPEATABLE READ: tres sesiones sobre la misma fila
<!-- ejercicio: U3.22 | nivel: intermedio | tipo: diagnostico | verificacion: revisado -->

:::note[Enunciado]
Un cliente consulta el límite de su tarjeta en `REPEATABLE READ` y lo mantiene abierto mientras decide. Al mismo tiempo, un empleado intenta cambiar el límite (sesión B) y otro cambia la ciudad (sesión C). Predecí cuándo terminan B y C y qué pasaría si, además, el cliente intentara modificar esa fila antes de confirmar.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reiniciá el entorno. `REPEATABLE READ` mantiene el lock `S` de la fila leída hasta el final de la transacción de A. Las modificaciones de B y de C necesitan un `X` sobre esa misma fila (los locks son por fila, no por columna: la sesión C cambia una columna distinta y igual espera). Ninguna avanza hasta que A confirme.

**Sesión A** (cliente):

<!-- check: U3.22 -->
```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

DECLARE @Limite DECIMAL(12,2);

BEGIN TRANSACTION;
    SELECT @Limite = LimiteCredito
    FROM banco.TarjetaCredito
    WHERE NroTarjeta = 1000000000000001;     -- el lock S se mantiene hasta el COMMIT

    SELECT @Limite AS LimiteLeido;

    WAITFOR DELAY '00:00:20';                -- se ejecutan B y C

    SELECT LimiteCredito AS LimiteRelectura  -- sigue siendo el mismo valor
    FROM banco.TarjetaCredito
    WHERE NroTarjeta = 1000000000000001;
COMMIT TRANSACTION;

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**Sesión B** (empleado 1; dentro de los 20 segundos):

<!-- check: U3.22 -->
```sql
UPDATE banco.TarjetaCredito
SET LimiteCredito = 5800.00
WHERE NroTarjeta = 1000000000000001;
```

**Sesión C** (empleado 2; dentro de los 20 segundos):

<!-- check: U3.22 -->
```sql
UPDATE banco.TarjetaCredito
SET Ciudad = 'Ciudad X'
WHERE NroTarjeta = 1000000000000001;
```

**Resultado esperado** (según la documentación; no verificado en esta edición):

| Sesión | Resultado |
|---|---|
| A, `LimiteLeido` | 6000 |
| B y C | Quedan esperando mientras A está abierta |
| A, `LimiteRelectura` | 6000: la lectura es repetible porque nadie pudo modificar la fila |
| Después del `COMMIT` de A | B y C se completan; el estado final es límite 5800 y ciudad `Ciudad X` |

Se puede ver la espera desde otra ventana con `sys.dm_tran_locks` y `sys.dm_exec_requests`: A figura con `S` en la `KEY` y B y C aparecen con `blocking_session_id` apuntando a A.

**Variante con riesgo de deadlock.** Si A, antes de confirmar, intentara modificar la fila que leyó, convertiría su `S` en `X`. Un `UPDATE` toma primero un lock de actualización (`U`), que es compatible con el `S` de A: B lo obtiene y queda esperando para convertirlo a `X`. Entonces A espera el `X` (incompatible con el `U` de B) y B espera que A suelte el `S`: es un ciclo, un **deadlock de conversión**, y el motor elige una víctima y le devuelve el error 1205. La forma de evitarlo es que A lea con `UPDLOCK` (`SELECT ... FROM banco.TarjetaCredito WITH (UPDLOCK)`), que toma el `U` desde la lectura y deja a B esperando antes de que el ciclo se forme.
</details>

### Experimento 3 · SERIALIZABLE: sin fantasmas en el historial de una tarjeta
<!-- ejercicio: U3.23 | nivel: avanzado | tipo: diagnostico | verificacion: revisado -->

:::note[Enunciado]
Un proceso de conciliación cuenta las transacciones de una tarjeta, hace otras tareas y vuelve a contarlas dentro de la misma transacción. Mientras tanto, otra sesión registra una venta nueva de esa tarjeta. Compará lo que ve la conciliación con `REPEATABLE READ` y con `SERIALIZABLE`, y explicá qué lock lo explica.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Ejecutá antes el experimento 0 (deja la venta 1001, por lo que el historial tiene una fila). Corré la sesión A con `REPEATABLE READ` y después con `SERIALIZABLE`; en ambos casos, la sesión B inserta durante la espera. `REPEATABLE READ` solo protege las **filas ya leídas**: no impide insertar filas nuevas que cumplen el criterio. `SERIALIZABLE` toma locks de rango sobre el índice `IX_TransaccionTarjeta_NroTarjeta`, que cubren las filas de esa tarjeta y la clave siguiente, y bloquea las inserciones en ese rango.

**Sesión A** (conciliación; cambiá el nivel para cada corrida):

<!-- check: U3.23 -->
```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;      -- segunda corrida: SERIALIZABLE

BEGIN TRANSACTION;
    SELECT COUNT(*) AS PrimeraCuenta
    FROM banco.TransaccionTarjeta
    WHERE NroTarjeta = 1000000000000001;

    WAITFOR DELAY '00:00:20';                         -- se ejecuta B

    SELECT COUNT(*) AS SegundaCuenta
    FROM banco.TransaccionTarjeta
    WHERE NroTarjeta = 1000000000000001;
COMMIT TRANSACTION;

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**Sesión B** (venta nueva; dentro de los 20 segundos):

<!-- check: U3.23 -->
```sql
INSERT INTO banco.TransaccionTarjeta (TransaccionId, NroTarjeta, Fecha, Monto, TransaccionOrigenId, Tipo)
VALUES (1004, 1000000000000001, '2026-03-01T11:00:00', 100.00, NULL, 'V');
```

**Resultado esperado** (según la documentación; no verificado en esta edición):

| Nivel de A | `PrimeraCuenta` | `SegundaCuenta` | Sesión B |
|---|---:|---:|---|
| `REPEATABLE READ` | 1 | 2 (aparece un **fantasma**) | Se completa de inmediato |
| `SERIALIZABLE` | 1 | 1 | Espera hasta el `COMMIT` de A y recién entonces inserta |

Después de cada corrida borrá la fila insertada con `DELETE FROM banco.TransaccionTarjeta WHERE TransaccionId = 1004;` o reiniciá el entorno, y repetí el experimento 0 si hace falta.

El `SERIALIZABLE` es más caro: los locks de rango pueden bloquear también inserciones de tarjetas vecinas en el orden del índice, y mantienen los locks hasta el final de la transacción. Se lo reserva para operaciones donde un fantasma sería incorrecto, como una conciliación.
</details>

### Resumen de los experimentos

| Experimento | Nivel de A | Sesiones | Fenómeno | Verificación |
|---|---|---:|---|---|
| 0 | `READ COMMITTED` (por defecto) | 1 | Compra atómica con `BEGIN TRANSACTION` | Ejecutado |
| 1 | `READ UNCOMMITTED` en el cliente | 2 | Lectura sucia | Guion (dos sesiones) |
| 2 | `REPEATABLE READ` | 3 | Locks `S` que bloquean escrituras | Guion (tres sesiones) |
| 3 | `REPEATABLE READ` y `SERIALIZABLE` | 2 | Fantasma y locks de rango | Guion (dos sesiones) |

Para el recorrido sistemático por nivel (con una sola tabla y resultados por sesión), seguí con el [laboratorio de aislamiento](/bbdd-aplicadas/unidad-3/practica/laboratorio-aislamiento/).
