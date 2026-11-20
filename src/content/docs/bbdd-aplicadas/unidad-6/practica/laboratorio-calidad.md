---
title: Laboratorio — Perfilado, reglas y métricas
slug: bbdd-aplicadas/unidad-6/practica/laboratorio-calidad
sidebar:
  order: 1
---

[← Unidad 6](/bbdd-aplicadas/unidad-6/teoria/)

Laboratorio de perfilado y medición de calidad con T-SQL sobre datos que tienen defectos deliberados. Cada defecto se asocia con una característica de [ISO/IEC 25012](/bbdd-aplicadas/unidad-6/teoria/iso-25012/) y, cuando corresponde, con el principio de calidad del artículo 4 de la [Ley 25.326](/bbdd-aplicadas/unidad-6/teoria/ley-25326/).

:::note[Contenido complementario]
Las consultas de perfilado, las métricas y los umbrales de este laboratorio son elaboración propia, pensados para practicar. ISO/IEC 25012 define las características de calidad, no las consultas ni los umbrales; los 365 días de la regla de actualidad son un valor del ejercicio, no un requisito de la norma ni de la ley.
:::

## Qué necesitás saber

- [ISO/IEC 25012](/bbdd-aplicadas/unidad-6/teoria/iso-25012/): completitud, exactitud, consistencia, actualidad y conformidad.
- [Medición y mejora de la calidad](/bbdd-aplicadas/unidad-6/teoria/medicion-calidad/): fórmula, alcance, umbral y controles preventivos, detectivos y correctivos.
- `NULLIF`, `TRY_CONVERT`, `LEFT JOIN`, `GROUP BY` y restricciones `FOREIGN KEY` y `CHECK`.

## Preparación

Ejecutá el script completo en una [base de práctica](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos) nueva y sin otros objetos (`CREATE DATABASE CalidadU6;` y `USE CalidadU6;`; si no tenés el permiso `CREATE DATABASE`, pedí una base y usala con `USE`). Los ejercicios 16 a 20 usan las tablas que crea este script; el 20 agrega restricciones, así que, para repetirlo, volvé a crear la base. Los datos son sintéticos: los DNI (`00000001`, `00000002`, …), los nombres y los correos (`@ejemplo.test`) son evidentemente ficticios. El instante de referencia es fijo (`2026-06-30`) para que los resultados sean reproducibles; en un sistema real usarías la fecha del momento de medir.

<!-- check: U6.P.01 -->
```sql
CREATE SCHEMA calidad;
GO

CREATE TABLE calidad.Cliente (
    ClienteId            INT           NOT NULL,
    Dni                  VARCHAR(20)   NULL,
    Nombre               NVARCHAR(100) NULL,
    Email                VARCHAR(256)  NULL,
    PaisCodigo           CHAR(3)       NULL,
    FechaNacimientoTexto VARCHAR(20)   NULL,
    FechaAlta            DATE          NOT NULL,
    FechaActualizacion   DATE          NOT NULL,
    Activo               BIT           NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE calidad.Pedido (
    PedidoId       INT           NOT NULL,
    ClienteId      INT           NULL,
    FechaPedido    DATE          NOT NULL,
    FechaEntrega   DATE          NULL,
    TotalDeclarado DECIMAL(12, 2) NOT NULL,
    CONSTRAINT PK_Pedido PRIMARY KEY CLUSTERED (PedidoId)
);

CREATE TABLE calidad.ItemPedido (
    PedidoId       INT            NOT NULL,
    Renglon        INT            NOT NULL,
    Cantidad       INT            NOT NULL,
    PrecioUnitario DECIMAL(12, 2) NOT NULL,
    CONSTRAINT PK_ItemPedido PRIMARY KEY CLUSTERED (PedidoId, Renglon)
);

INSERT INTO calidad.Cliente
    (ClienteId, Dni, Nombre, Email, PaisCodigo, FechaNacimientoTexto, FechaAlta, FechaActualizacion, Activo)
VALUES
    (1, '00000001', N'Cliente Uno',    'cliente01@ejemplo.test', 'ARG', '1990-02-10', '2025-01-10', '2026-05-20', 1),
    (2, '00000001', N'Cliente Dos',    'cliente02@ejemplo.test', 'ARG', '1990-02-10', '2025-01-10', '2025-03-15', 1),
    (3, NULL,       N'Cliente Tres',   '',                       'AR ', '31/02/1995', '2025-03-01', '2026-06-10', 1),
    (4, '00000004', NULL,              'cliente04@ejemplo.test', 'URY', '1985-05-20', '2025-04-01', '2026-06-01', 1),
    (5, '00000005', N'Cliente Cinco',  'cliente05@ejemplo.test', 'ZZZ', '1977-09-08', '2024-02-01', '2024-11-02', 0),
    (6, '00000006', N'Cliente Seis',   NULL,                     'BRA', '2000-01-31', '2025-05-05', '2026-01-15', 1),
    (7, '00000007', N'Cliente Siete',  '   ',                    'ARG', NULL,         '2024-08-08', '2025-01-20', 1),
    (8, '00000008', N'Cliente Ocho',   'cliente08@ejemplo.test', 'ARG', '1999-12-01', '2025-06-01', '2026-03-03', 1),
    (9, '00000009', N'Cliente Nueve',  'CLIENTE01@EJEMPLO.TEST', 'URY', '1988-07-07', '2026-01-02', '2026-06-29', 1);

INSERT INTO calidad.Pedido (PedidoId, ClienteId, FechaPedido, FechaEntrega, TotalDeclarado)
VALUES
    (101, 1,  '2026-06-01', '2026-05-31', 150.00),
    (102, 3,  '2026-06-02', NULL,         200.00),
    (103, 99, '2026-06-03', NULL,          50.00);

INSERT INTO calidad.ItemPedido (PedidoId, Renglon, Cantidad, PrecioUnitario)
VALUES
    (101, 1, 1, 100.00),
    (101, 2, 1,  40.00),
    (102, 1, 2, 100.00),
    (103, 1, 1,  50.00);
GO
```

Para comprobar que la carga fue correcta:

<!-- check: U6.P.01 -->
```sql
SELECT 'Cliente' AS Tabla, COUNT(*) AS Filas FROM calidad.Cliente
UNION ALL
SELECT 'ItemPedido', COUNT(*) FROM calidad.ItemPedido
UNION ALL
SELECT 'Pedido', COUNT(*) FROM calidad.Pedido
ORDER BY Tabla;
```

**Resultado esperado.**

| Tabla | Filas |
|---|---:|
| Cliente | 9 |
| ItemPedido | 4 |
| Pedido | 3 |

Los defectos que sembramos, para que sepas qué buscar: un DNI repetido (clientes 1 y 2), un DNI ausente (3), un nombre ausente (4), correos `NULL`, vacío o con espacios (3, 6, 7), un país fuera de catálogo (3 y 5), una fecha de nacimiento textual imposible (3), clientes sin verificar hace más de un año (2 y 7), un correo que coincide con otro salvo por mayúsculas (9), un pedido sin cliente existente (103), una entrega anterior al pedido (101) y un total declarado que no coincide con los renglones (101).

## Ejercicios

### Ejercicio 16 · Perfil de completitud
<!-- ejercicio: U6.16 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con `calidad.Cliente`, calculá en una sola consulta el total de filas, cuántas no tienen DNI, nombre ni correo con valor real (tratá la cadena vacía y los espacios como ausentes) y el porcentaje de completitud del correo **solo entre los clientes activos**. Indicá qué característica de ISO/IEC 25012 mide cada indicador.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Normalizar cada columna con `NULLIF(LTRIM(RTRIM(...)), '')` para que vacío y espacios cuenten como ausentes, contar con `SUM(CASE ...)` y dividir por un denominador explícito (los clientes activos), protegido con `NULLIF` contra la división por cero.

<!-- check: U6.16 -->
```sql
SELECT
    COUNT(*) AS Filas,
    SUM(CASE WHEN NULLIF(LTRIM(RTRIM(Dni)), '') IS NULL THEN 1 ELSE 0 END)    AS DniFaltante,
    SUM(CASE WHEN NULLIF(LTRIM(RTRIM(Nombre)), '') IS NULL THEN 1 ELSE 0 END) AS NombreFaltante,
    SUM(CASE WHEN NULLIF(LTRIM(RTRIM(Email)), '') IS NULL THEN 1 ELSE 0 END)  AS EmailFaltante,
    CAST(
        100.0 * SUM(CASE WHEN Activo = 1 AND NULLIF(LTRIM(RTRIM(Email)), '') IS NOT NULL THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN Activo = 1 THEN 1 ELSE 0 END), 0)
        AS DECIMAL(5, 2)) AS CompletitudEmailActivosPct
FROM calidad.Cliente;
```

**Resultado esperado.**

| Filas | DniFaltante | NombreFaltante | EmailFaltante | CompletitudEmailActivosPct |
|---:|---:|---:|---:|---:|
| 9 | 1 | 1 | 3 | 62.50 |

Los tres primeros indicadores miden **completitud** (valores presentes para los atributos esperados). Hay 8 clientes activos y 5 tienen un correo con valor (1, 2, 4, 8 y 9), de modo que la completitud del correo es 5 / 8 = 62,50 %. Si el denominador fueran las 9 filas, el resultado sería 55,56 %: por eso hay que declarar la población.
</details>

### Ejercicio 17 · Duplicados, dominios y formato
<!-- ejercicio: U6.17 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Listá en un único resultado, con una fila por hallazgo, (a) los DNI repetidos, (b) los clientes con un código de país que no pertenece al catálogo `ARG`, `URY`, `BRA` y (c) las fechas de nacimiento textuales que no se pueden interpretar como fecha `AAAA-MM-DD`. Clasificá cada regla según ISO/IEC 25012.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Una consulta por regla, unidas con `UNION ALL` y con la misma forma de salida (regla, cliente, valor). Para el formato se usa `TRY_CONVERT(DATE, ..., 23)`, que devuelve `NULL` si el texto no es una fecha válida en ese estilo; el `NULL` de origen se excluye antes, porque ya es un problema de completitud, no de formato.

<!-- check: U6.17 -->
```sql
SELECT Regla, ClienteId, Valor
FROM (
    SELECT 'DNI repetido' AS Regla, c.ClienteId, CAST(c.Dni AS VARCHAR(30)) AS Valor
    FROM calidad.Cliente AS c
    WHERE c.Dni IN (
        SELECT Dni
        FROM calidad.Cliente
        WHERE Dni IS NOT NULL
        GROUP BY Dni
        HAVING COUNT(*) > 1
    )

    UNION ALL

    SELECT 'País fuera de catálogo', ClienteId, CAST(PaisCodigo AS VARCHAR(30))
    FROM calidad.Cliente
    WHERE PaisCodigo NOT IN ('ARG', 'URY', 'BRA')

    UNION ALL

    SELECT 'Fecha de nacimiento inválida', ClienteId, FechaNacimientoTexto
    FROM calidad.Cliente
    WHERE FechaNacimientoTexto IS NOT NULL
      AND TRY_CONVERT(DATE, FechaNacimientoTexto, 23) IS NULL
) AS Hallazgo
ORDER BY Regla, ClienteId;
```

**Resultado esperado.**

| Regla | ClienteId | Valor |
|---|---:|---|
| DNI repetido | 1 | 00000001 |
| DNI repetido | 2 | 00000001 |
| Fecha de nacimiento inválida | 3 | 31/02/1995 |
| País fuera de catálogo | 3 | AR |
| País fuera de catálogo | 5 | ZZZ |

El DNI repetido es un problema de **consistencia** (la misma identidad en dos filas) y, según el caso, de exactitud. El país fuera de catálogo y la fecha mal formada son problemas de **conformidad** y de **exactitud sintáctica**. Observá que `'AR '` (con espacio) no es un código del catálogo aunque "parezca" Argentina: el control es sobre el valor almacenado, no sobre lo que el usuario quiso escribir. En la salida de `sqlcmd` el valor `AR ` se muestra sin el espacio final.
</details>

### Ejercicio 18 · Reglas entre tablas
<!-- ejercicio: U6.18 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Detectá, en un único resultado, los pedidos que (a) referencian un cliente inexistente, (b) tienen la fecha de entrega anterior a la fecha del pedido y (c) tienen un total declarado distinto de la suma de `Cantidad * PrecioUnitario` de sus renglones. Para cada regla, indicá si una `FOREIGN KEY` o un `CHECK` podría haberla evitado por completo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** (a) `LEFT JOIN` contra `Cliente` y filtrar los que no tienen par; (b) comparación de dos columnas de la misma fila; (c) agregación de los renglones y comparación con el total, que obliga a unir con otra tabla.

<!-- check: U6.18 -->
```sql
SELECT Regla, PedidoId, Detalle
FROM (
    SELECT 'Cliente inexistente' AS Regla, p.PedidoId,
           CONCAT('ClienteId ', p.ClienteId) AS Detalle
    FROM calidad.Pedido AS p
    LEFT JOIN calidad.Cliente AS c ON c.ClienteId = p.ClienteId
    WHERE p.ClienteId IS NOT NULL
      AND c.ClienteId IS NULL

    UNION ALL

    SELECT 'Entrega anterior al pedido', PedidoId,
           CONCAT(CONVERT(VARCHAR(10), FechaEntrega, 23), ' < ', CONVERT(VARCHAR(10), FechaPedido, 23))
    FROM calidad.Pedido
    WHERE FechaEntrega < FechaPedido

    UNION ALL

    SELECT 'Total no reconciliado', p.PedidoId,
           CONCAT('declarado ', p.TotalDeclarado, ' / calculado ', SUM(i.Cantidad * i.PrecioUnitario))
    FROM calidad.Pedido AS p
    JOIN calidad.ItemPedido AS i ON i.PedidoId = p.PedidoId
    GROUP BY p.PedidoId, p.TotalDeclarado
    HAVING p.TotalDeclarado <> SUM(i.Cantidad * i.PrecioUnitario)
) AS Hallazgo
ORDER BY Regla, PedidoId;
```

**Resultado esperado.**

| Regla | PedidoId | Detalle |
|---|---:|---|
| Cliente inexistente | 103 | ClienteId 99 |
| Entrega anterior al pedido | 101 | 2026-05-31 < 2026-06-01 |
| Total no reconciliado | 101 | declarado 150.00 / calculado 140.00 |

Las tres son **consistencia**. Una `FOREIGN KEY` previene por completo la regla (a): el motor rechaza un `ClienteId` que no existe. Un `CHECK (FechaEntrega IS NULL OR FechaEntrega >= FechaPedido)` previene la regla (b), porque compara columnas de la misma fila. La regla (c) depende de filas de otra tabla: un `CHECK` no puede consultarla, de modo que hace falta un disparador, una columna calculada o un control detectivo como esta consulta. Nada de esto prueba que la fecha o el total sean *verdaderos*, solo que no se contradicen.
</details>

### Ejercicio 19 · Actualidad con instante fijo
<!-- ejercicio: U6.19 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Regla del laboratorio: un cliente activo debe haber sido verificado en los 365 días previos a la fecha de corte `2026-06-30`. Calculá cuántos clientes activos se evalúan, cuántos cumplen la regla y el porcentaje de actualidad. Documentá alcance, numerador, denominador, instante, umbral propuesto y responsable.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Fijar el instante de medición en una variable (así el resultado no depende del reloj), delimitar la población (`Activo = 1`) y contar con `SUM(CASE ...)`. Un cliente cumple si `FechaActualizacion >= DATEADD(DAY, -365, @FechaCorte)`.

<!-- check: U6.19 -->
```sql
DECLARE @FechaCorte DATE = '2026-06-30';

SELECT
    COUNT(*) AS ActivosEvaluados,
    SUM(CASE WHEN FechaActualizacion >= DATEADD(DAY, -365, @FechaCorte) THEN 1 ELSE 0 END) AS Vigentes,
    CAST(
        100.0 * SUM(CASE WHEN FechaActualizacion >= DATEADD(DAY, -365, @FechaCorte) THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0)
        AS DECIMAL(5, 2)) AS ActualidadPct
FROM calidad.Cliente
WHERE Activo = 1;
```

**Resultado esperado.**

| ActivosEvaluados | Vigentes | ActualidadPct |
|---:|---:|---:|
| 8 | 6 | 75.00 |

La actualidad es del 75,00 % (6 de 8): los clientes 2 (`2025-03-15`) y 7 (`2025-01-20`) superan la ventana de 365 días. El cliente 5 no entra en el denominador porque está inactivo. La ficha de la regla queda así (los valores son una propuesta de este ejercicio):

| Elemento | Valor |
|---|---|
| Alcance | clientes con `Activo = 1` |
| Numerador | activos con `FechaActualizacion` dentro de los 365 días previos al corte |
| Denominador | clientes activos al corte |
| Instante | fecha de corte explícita (`2026-06-30`) |
| Umbral | advertencia por debajo de 90 %, rechazo por debajo de 75 % (propuesta del ejercicio) |
| Responsable | quien decide el significado de "cliente verificado" (owner) y quien opera la medición (steward) |
</details>

### Ejercicio 20 · Endurecer el esquema sin inventar datos
<!-- ejercicio: U6.20 | nivel: avanzado | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Intentá agregar `FK_Pedido_Cliente` y `CK_Pedido_Fechas` sobre `calidad.Pedido` mientras existen los defectos del laboratorio y registrá qué ocurre. Luego, sin modificar ningún valor, apartá a una tabla de cuarentena los pedidos que violan las reglas, repetí los dos comandos y comprobá que ahora se aceptan. Explicá por qué no se corrigieron los datos con un `UPDATE`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los dos `ALTER TABLE ... WITH CHECK` validan los datos existentes y, mientras haya defectos, fallan con el error 547 (conflicto con una restricción). Se capturan con `TRY...CATCH` y se registran en una variable de tabla, de modo que el script no se corta. La cuarentena traslada las filas defectuosas con su evidencia; después de ese paso, los mismos comandos se aceptan.

<!-- check: U6.20 -->
```sql
DECLARE @Bitacora TABLE (Paso INT NOT NULL, Accion VARCHAR(60) NOT NULL, Resultado VARCHAR(30) NOT NULL);

CREATE TABLE calidad.PedidoCuarentena (
    PedidoId       INT            NOT NULL,
    ClienteId      INT            NULL,
    FechaPedido    DATE           NOT NULL,
    FechaEntrega   DATE           NULL,
    TotalDeclarado DECIMAL(12, 2) NOT NULL,
    Motivo         VARCHAR(60)    NOT NULL,
    CONSTRAINT PK_PedidoCuarentena PRIMARY KEY CLUSTERED (PedidoId)
);

BEGIN TRY
    ALTER TABLE calidad.Pedido WITH CHECK
        ADD CONSTRAINT FK_Pedido_Cliente FOREIGN KEY (ClienteId) REFERENCES calidad.Cliente (ClienteId);
    INSERT INTO @Bitacora VALUES (1, 'FK antes de la cuarentena', 'OK');
END TRY
BEGIN CATCH
    INSERT INTO @Bitacora VALUES (1, 'FK antes de la cuarentena', CONCAT('Error ', ERROR_NUMBER()));
END CATCH;

BEGIN TRY
    ALTER TABLE calidad.Pedido WITH CHECK
        ADD CONSTRAINT CK_Pedido_Fechas CHECK (FechaEntrega IS NULL OR FechaEntrega >= FechaPedido);
    INSERT INTO @Bitacora VALUES (2, 'CHECK antes de la cuarentena', 'OK');
END TRY
BEGIN CATCH
    INSERT INTO @Bitacora VALUES (2, 'CHECK antes de la cuarentena', CONCAT('Error ', ERROR_NUMBER()));
END CATCH;

INSERT INTO calidad.PedidoCuarentena (PedidoId, ClienteId, FechaPedido, FechaEntrega, TotalDeclarado, Motivo)
SELECT p.PedidoId, p.ClienteId, p.FechaPedido, p.FechaEntrega, p.TotalDeclarado,
       CASE WHEN c.ClienteId IS NULL THEN 'Cliente inexistente' ELSE 'Entrega anterior al pedido' END
FROM calidad.Pedido AS p
LEFT JOIN calidad.Cliente AS c ON c.ClienteId = p.ClienteId
WHERE (p.ClienteId IS NOT NULL AND c.ClienteId IS NULL)
   OR p.FechaEntrega < p.FechaPedido;

INSERT INTO @Bitacora VALUES (3, 'Pedidos a cuarentena', CONCAT(@@ROWCOUNT, ' filas'));

DELETE p
FROM calidad.Pedido AS p
WHERE EXISTS (SELECT 1 FROM calidad.PedidoCuarentena AS q WHERE q.PedidoId = p.PedidoId);

BEGIN TRY
    ALTER TABLE calidad.Pedido WITH CHECK
        ADD CONSTRAINT FK_Pedido_Cliente FOREIGN KEY (ClienteId) REFERENCES calidad.Cliente (ClienteId);
    INSERT INTO @Bitacora VALUES (4, 'FK después de la cuarentena', 'OK');
END TRY
BEGIN CATCH
    INSERT INTO @Bitacora VALUES (4, 'FK después de la cuarentena', CONCAT('Error ', ERROR_NUMBER()));
END CATCH;

BEGIN TRY
    ALTER TABLE calidad.Pedido WITH CHECK
        ADD CONSTRAINT CK_Pedido_Fechas CHECK (FechaEntrega IS NULL OR FechaEntrega >= FechaPedido);
    INSERT INTO @Bitacora VALUES (5, 'CHECK después de la cuarentena', 'OK');
END TRY
BEGIN CATCH
    INSERT INTO @Bitacora VALUES (5, 'CHECK después de la cuarentena', CONCAT('Error ', ERROR_NUMBER()));
END CATCH;

SELECT Paso, Accion, Resultado
FROM @Bitacora
ORDER BY Paso;
```

**Resultado esperado.**

| Paso | Accion | Resultado |
|---:|---|---|
| 1 | FK antes de la cuarentena | Error 547 |
| 2 | CHECK antes de la cuarentena | Error 547 |
| 3 | Pedidos a cuarentena | 2 filas |
| 4 | FK después de la cuarentena | OK |
| 5 | CHECK después de la cuarentena | OK |

Los dos primeros intentos fallan porque la base heredada **no cumple todavía** las reglas: el rechazo es información útil, no un obstáculo. Se apartaron los pedidos 101 (entrega anterior) y 103 (cliente inexistente) con su motivo, y a partir de ahí el motor garantiza ambas reglas en la captura (control **preventivo**). No se hizo un `UPDATE` porque la fecha de entrega o el cliente correctos no se pueden deducir de los datos: corregir exige una fuente autorizada. El pedido 101 sigue en cuarentena también por el total no reconciliado (ejercicio 18), que ningún `CHECK` cubre.

:::caution[Errores frecuentes]
Agregar la restricción con `WITH NOCHECK` "para que pase" deja datos que violan la regla y una restricción que el optimizador no considera confiable; crea una confianza falsa. Si hace falta usarla de forma transitoria, hay que registrar el plazo para validar y volver a habilitarla con `WITH CHECK`.
:::
</details>

### Ejercicio 21 · ¿DNI repetido significa dos personas iguales?
<!-- ejercicio: U6.21 | nivel: intermedio | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Los clientes 1 y 2 tienen el mismo DNI `00000001`, la misma fecha de nacimiento y correos distintos. (a) ¿Alcanza para afirmar que son la misma persona? (b) ¿Qué característica de ISO/IEC 25012 está comprometida? (c) ¿Qué principio del artículo 4 de la Ley 25.326 se relaciona y qué debe hacer el responsable? (d) ¿Por qué `LIKE '%@%'` sobre el correo no demuestra exactitud?
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Separar lo que la consulta *muestra* (dos filas con el mismo valor) de lo que *prueba* (nada sobre las personas) y asociar cada hallazgo con la característica y el artículo correspondientes.

(a) No alcanza. Dos filas con el mismo identificador pueden ser un duplicado por doble alta, una carga con un identificador mal escrito o un dato que pertenece a otra persona. La consulta detecta una **sospecha**; resolverla exige una fuente de referencia (por ejemplo, el documento presentado al dar el alta).

(b) La **consistencia**: dos filas contradicen la regla de que un identificador corresponde a una única persona. Si uno de los DNI fuera de otra persona, también habría un problema de **exactitud semántica** (el valor tiene formato válido pero no representa la realidad), y la fuente podría cuestionarse por **credibilidad**.

(c) El artículo 4 exige que los datos sean exactos y se actualicen cuando sea necesario (inciso 4), y que, si son inexactos o incompletos, se supriman, sustituyan o completen cuando el responsable toma conocimiento del error (inciso 5). El responsable debe investigar con la fuente, corregir o fusionar y propagar la corrección, y conservar evidencia. La ley no habla de "duplicados": es una consecuencia de esos incisos.

(d) `LIKE '%@%'` verifica una forma (hay un arroba) y, por lo tanto, solo la **exactitud sintáctica** y la conformidad. Que `cliente02@ejemplo.test` tenga forma de correo no demuestra que exista ni que pertenezca al cliente: eso es exactitud semántica y solo se comprueba contra la realidad (por ejemplo, con un mensaje de confirmación).
</details>

### Ejercicio 22 · Lo que el SQL no puede probar
<!-- ejercicio: U6.22 | nivel: avanzado | tipo: diagnostico | verificacion: razonamiento -->

:::note[Enunciado]
Un informe reporta "calidad de clientes: 100 %" porque todas las filas pasan las reglas de formato (DNI de 8 dígitos, país del catálogo, correo con arroba, fecha válida). Señalá tres defectos que ese informe no detectaría, la característica de ISO/IEC 25012 de cada uno y el control (preventivo, detectivo o correctivo) que propondrías.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Buscar defectos que la validación de formato no puede ver y asociar cada uno con la característica que lo describe y con el momento en que conviene controlarlo.

| Defecto invisible al formato | Característica | Control propuesto |
|---|---|---|
| El DNI tiene 8 dígitos pero pertenece a otra persona | Exactitud semántica | Detectivo: contraste periódico con una fuente autorizada; correctivo: corregir con evidencia y propagar |
| El domicilio es válido pero la persona se mudó hace años | Actualidad | Detectivo: medir antigüedad de la última verificación (como en el ejercicio 19); preventivo: pedir reconfirmación en cada interacción |
| Dos filas con el mismo cliente escrito distinto (`Cliente Uno` y `Cliente Uno S.`) | Consistencia | Detectivo: clave de comparación normalizada; preventivo: búsqueda de similares al dar de alta |
| Todos los datos son correctos pero un analista ve datos que no necesita | Confidencialidad | Preventivo: permisos por rol (el control de calidad de formato no lo mide) |

Un 100 % de conformidad de formato no es "calidad total": mide una sola característica sobre una población. La medición con SQL prueba que los datos *cumplen reglas expresadas en SQL*, no que sean verdaderos.
</details>

## Entregable

Un informe breve con:

1. el perfil y la evidencia SQL de los ejercicios 16 a 19;
2. la característica ISO de cada hallazgo;
3. cinco reglas formalizadas con la ficha del ejercicio 19;
4. métrica y umbral de tres reglas, aclarando que los umbrales son propuestas;
5. causa raíz probable y controles preventivo, detectivo y correctivo;
6. los límites de la medición, con el ejercicio 22.

## Fuentes

- Resumen público de ISO/IEC 25012: [iso25000.com](https://iso25000.com/index.php/normas-iso-25000/iso-25012), consultado el 2026-11-17. Las consultas, métricas y umbrales son elaboración propia.
- Ley 25.326, art. 4: [InfoLEG](https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm), consultada el 2026-11-17.
- Restricciones `FOREIGN KEY` y `CHECK`, `TRY_CONVERT` y `TRY...CATCH`: documentación de [SQL Server en Microsoft Learn](https://learn.microsoft.com/es-es/sql/t-sql/).
