---
title: PIVOT
slug: bbdd-aplicadas/unidad-1/teoria/pivot
sidebar:
  order: 5
---

`PIVOT` convierte **valores de una columna en columnas**: pasamos de una tabla "larga" (una fila por hecho) a una tabla "ancha" (un valor por columna), útil para reportes y comparaciones. `UNPIVOT` hace el camino inverso.

Los ejemplos usan el esquema `ventas` de la página de [window functions](/bbdd-aplicadas/unidad-1/teoria/window-functions/#esquema-de-ejemplo), en una base vacía donde ya se creó ese esquema.

## PIVOT estático

<!-- sintaxis -->
```sql
SELECT <columnas fijas>, [valor1], [valor2], ...
FROM ( <consulta de origen> ) AS Origen
PIVOT (
    FUNCION_DE_AGREGADO(columna_a_agregar)
    FOR columna_cuyos_valores_pasan_a_columnas
    IN ([valor1], [valor2], ...)
) AS Pv;
```

| Componente | Qué define |
|---|---|
| Función de agregado | Cómo combinar los valores que caen en la misma celda: `SUM`, `COUNT`, `AVG`, `MIN`, `MAX` |
| `FOR columna` | La columna cuyos **valores** se convierten en encabezados |
| `IN (...)` | Los valores concretos que serán columnas, escritos a mano |

Monto vendido por vendedor y producto:

<!-- check: U1.T.PV.01 -->
```sql
SELECT
    Nombre,
    [Teclado],
    [Monitor],
    [Notebook]
FROM (
    SELECT
        v.Nombre,
        ve.Producto,
        ve.Monto
    FROM ventas.Venta AS ve
    INNER JOIN ventas.Vendedor AS v
        ON v.VendedorId = ve.VendedorId
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Producto IN ([Teclado], [Monitor], [Notebook])
) AS Pv
ORDER BY Nombre;
```

| Nombre | Teclado | Monitor | Notebook |
|---|---:|---:|---:|
| Beto | 350.00 | 500.00 | 1200.00 |
| Cora | 200.00 | 500.00 | 1200.00 |
| Dario | `NULL` | 500.00 | `NULL` |
| Eva | 200.00 | 500.00 | 1200.00 |
| Fede | 150.00 | 500.00 | 1200.00 |
| Gina | 200.00 | 500.00 | `NULL` |

Beto vendió dos teclados (200 + 150) y `SUM` los acumula en una celda. Ana no aparece porque no tiene ventas.

### Celdas `NULL`

Si no hay filas para una combinación, la celda queda en `NULL`. Con `ISNULL` o `COALESCE` se reemplaza por 0:

<!-- check: U1.T.PV.02 -->
```sql
SELECT
    Nombre,
    ISNULL([Teclado],  0) AS Teclado,
    ISNULL([Monitor],  0) AS Monitor,
    ISNULL([Notebook], 0) AS Notebook
FROM (
    SELECT
        v.Nombre,
        ve.Producto,
        ve.Monto
    FROM ventas.Venta AS ve
    INNER JOIN ventas.Vendedor AS v
        ON v.VendedorId = ve.VendedorId
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Producto IN ([Teclado], [Monitor], [Notebook])
) AS Pv
ORDER BY Nombre;
```

| Nombre | Teclado | Monitor | Notebook |
|---|---:|---:|---:|
| Beto | 350.00 | 500.00 | 1200.00 |
| Cora | 200.00 | 500.00 | 1200.00 |
| Dario | 0.00 | 500.00 | 0.00 |
| Eva | 200.00 | 500.00 | 1200.00 |
| Fede | 150.00 | 500.00 | 1200.00 |
| Gina | 200.00 | 500.00 | 0.00 |

Con `COUNT` no hace falta: cuando no hay filas devuelve 0.

<!-- check: U1.T.PV.03 -->
```sql
SELECT
    Nombre,
    [Teclado],
    [Monitor],
    [Notebook]
FROM (
    SELECT
        v.Nombre,
        ve.Producto,
        ve.VentaId
    FROM ventas.Venta AS ve
    INNER JOIN ventas.Vendedor AS v
        ON v.VendedorId = ve.VendedorId
) AS Origen
PIVOT (
    COUNT(VentaId)
    FOR Producto IN ([Teclado], [Monitor], [Notebook])
) AS Pv
ORDER BY Nombre;
```

| Nombre | Teclado | Monitor | Notebook |
|---|---:|---:|---:|
| Beto | 2 | 1 | 1 |
| Cora | 1 | 1 | 1 |
| Dario | 0 | 1 | 0 |
| Eva | 1 | 1 | 1 |
| Fede | 1 | 1 | 1 |
| Gina | 1 | 1 | 0 |

### La subconsulta de origen no es opcional

`PIVOT` agrupa por **todas las columnas del origen que no participan** en la agregación ni en `FOR`. Si apuntamos directo a `ventas.Venta`, `VentaId`, `VendedorId` y `Fecha` también agrupan, y obtenemos una fila por venta en lugar de una por vendedor. La subconsulta elige exactamente qué columnas entran.

<!-- check: U1.T.PV.04 -->
```sql
SELECT
    (SELECT COUNT(*)
     FROM ventas.Venta
     PIVOT (SUM(Monto) FOR Producto IN ([Teclado], [Monitor], [Notebook])) AS Pv) AS FilasSinSubconsulta,
    (SELECT COUNT(*)
     FROM (SELECT VendedorId, Producto, Monto FROM ventas.Venta) AS Origen
     PIVOT (SUM(Monto) FOR Producto IN ([Teclado], [Monitor], [Notebook])) AS Pv) AS FilasConSubconsulta;
```

| FilasSinSubconsulta | FilasConSubconsulta |
|---:|---:|
| 16 | 6 |

:::note[Regla práctica]
El `SELECT` externo decide qué columnas se muestran; la subconsulta decide qué columnas participan en el giro.
:::

### Alternativa manual con `CASE`

El mismo resultado se obtiene con `GROUP BY` y agregados condicionales. Es más largo, pero permite varios agregados y expresiones, que `PIVOT` no admite.

<!-- check: U1.T.PV.05 -->
```sql
SELECT
    v.Nombre,
    SUM(CASE WHEN ve.Producto = 'Teclado'  THEN ve.Monto END) AS Teclado,
    SUM(CASE WHEN ve.Producto = 'Monitor'  THEN ve.Monto END) AS Monitor,
    SUM(CASE WHEN ve.Producto = 'Notebook' THEN ve.Monto END) AS Notebook
FROM ventas.Venta AS ve
INNER JOIN ventas.Vendedor AS v
    ON v.VendedorId = ve.VendedorId
GROUP BY v.Nombre
ORDER BY v.Nombre;
```

(El resultado es el del primer ejemplo, con los mismos `NULL`.)

## PIVOT dinámico

Si los valores de `IN` cambian con los datos, la lista se arma en tiempo de ejecución con [SQL dinámico](/bbdd-aplicadas/unidad-1/teoria/sql-dinamico/): se leen los valores distintos, se concatenan con `QUOTENAME` y se ejecuta con `sp_executesql`. Todo ocurre en **un único lote**: un `GO` en el medio destruiría las variables.

<!-- check: U1.T.PV.06 -->
```sql
DECLARE @Columnas NVARCHAR(MAX);
DECLARE @Consulta NVARCHAR(MAX);

SELECT @Columnas = STRING_AGG(QUOTENAME(Producto), N', ') WITHIN GROUP (ORDER BY Producto)
FROM (SELECT DISTINCT Producto FROM ventas.Venta) AS Productos;

SET @Consulta = N'
SELECT Nombre, ' + @Columnas + N'
FROM (
    SELECT v.Nombre, ve.Producto, ve.Monto
    FROM ventas.Venta AS ve
    INNER JOIN ventas.Vendedor AS v
        ON v.VendedorId = ve.VendedorId
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Producto IN (' + @Columnas + N')
) AS Pv
ORDER BY Nombre;';

EXEC sys.sp_executesql @Consulta;
```

| Nombre | Monitor | Notebook | Teclado |
|---|---:|---:|---:|
| Beto | 500.00 | 1200.00 | 350.00 |
| Cora | 500.00 | 1200.00 | 200.00 |
| Dario | 500.00 | `NULL` | `NULL` |
| Eva | 500.00 | 1200.00 | 200.00 |
| Fede | 500.00 | 1200.00 | 150.00 |
| Gina | 500.00 | `NULL` | 200.00 |

El orden de las columnas lo fija el `WITHIN GROUP (ORDER BY ...)` de `STRING_AGG` (2017 o posterior).

| | Estático | Dinámico |
|---|---|---|
| Cuándo | Los valores son fijos y conocidos (trimestres, meses) | Los valores cambian (productos, etiquetas) |
| Ventaja | Simple y fácil de depurar | Se adapta a los datos |
| Desventaja | Falla en silencio si aparece un valor nuevo: no figura en el resultado | Más difícil de leer; hay que cuidar la inyección |

## UNPIVOT

Para ver `UNPIVOT` armamos una tabla ancha con el resultado de un `PIVOT`: `SELECT ... INTO` guarda las ventas por vendedor y mes.

<!-- check: U1.T.PV.07 -->
```sql
SELECT VendedorId, Ene, Feb, Mar, Abr
FROM ventas.ResumenMensual
ORDER BY VendedorId;
```

| VendedorId | Ene | Feb | Mar | Abr |
|---:|---:|---:|---:|---:|
| 2 | 700.00 | 150.00 | `NULL` | 1200.00 |
| 3 | 500.00 | 1200.00 | 200.00 | `NULL` |
| 4 | `NULL` | `NULL` | `NULL` | 500.00 |
| 5 | 200.00 | 500.00 | 1200.00 | `NULL` |
| 6 | `NULL` | 1200.00 | 500.00 | 150.00 |
| 7 | `NULL` | 200.00 | 500.00 | `NULL` |

`UNPIVOT` vuelve a filas. Las columnas listadas deben tener el mismo tipo, y **descarta las filas con `NULL`**:

<!-- check: U1.T.PV.08 -->
```sql
SELECT VendedorId, Mes, Monto
FROM ventas.ResumenMensual
UNPIVOT (
    Monto FOR Mes IN (Ene, Feb, Mar, Abr)
) AS Un
ORDER BY VendedorId,
    CASE Mes WHEN 'Ene' THEN 1 WHEN 'Feb' THEN 2 WHEN 'Mar' THEN 3 ELSE 4 END;
```

| VendedorId | Mes | Monto |
|---:|---|---:|
| 2 | Ene | 700.00 |
| 2 | Feb | 150.00 |
| 2 | Abr | 1200.00 |
| 3 | Ene | 500.00 |
| 3 | Feb | 1200.00 |
| 3 | Mar | 200.00 |
| 4 | Abr | 500.00 |
| 5 | Ene | 200.00 |
| 5 | Feb | 500.00 |
| 5 | Mar | 1200.00 |
| 6 | Feb | 1200.00 |
| 6 | Mar | 500.00 |
| 6 | Abr | 150.00 |
| 7 | Feb | 200.00 |
| 7 | Mar | 500.00 |

Quedan 15 filas: los 9 `NULL` de la tabla ancha desaparecen. Para **conservarlos**, usamos `CROSS APPLY` con `VALUES` (aquí, para los vendedores 2 y 4):

<!-- check: U1.T.PV.09 -->
```sql
SELECT
    r.VendedorId,
    m.Mes,
    m.Monto
FROM ventas.ResumenMensual AS r
CROSS APPLY (VALUES
    ('Ene', r.Ene),
    ('Feb', r.Feb),
    ('Mar', r.Mar),
    ('Abr', r.Abr)
) AS m (Mes, Monto)
WHERE r.VendedorId IN (2, 4)
ORDER BY r.VendedorId,
    CASE m.Mes WHEN 'Ene' THEN 1 WHEN 'Feb' THEN 2 WHEN 'Mar' THEN 3 ELSE 4 END;
```

| VendedorId | Mes | Monto |
|---:|---|---:|
| 2 | Ene | 700.00 |
| 2 | Feb | 150.00 |
| 2 | Mar | `NULL` |
| 2 | Abr | 1200.00 |
| 4 | Ene | `NULL` |
| 4 | Feb | `NULL` |
| 4 | Mar | `NULL` |
| 4 | Abr | 500.00 |

## Limitaciones y errores frecuentes

:::caution[Errores frecuentes]
- **Valores de `IN` que no existen o están mal escritos**: la columna sale vacía o no sale. Los valores que no figuran en `IN` desaparecen **sin error**. Conviene contrastar con `SELECT DISTINCT`.
- **Columnas extra en el origen**: generan filas repetidas por vendedor (ejemplo de las 16 filas).
- **Un único agregado y un único `FOR`**: dos agregados dan el error 102; para eso usamos `CASE`.
- **`IN` no admite una subconsulta**: da el error 156. Para listas variables, SQL dinámico.
- **`STRING_AGG` requiere SQL Server 2017**. En versiones anteriores se arma la lista con `STUFF` y `FOR XML PATH`.
:::

<!-- check: U1.T.PV.10 -->
```sql
CREATE TABLE #Resultado (Caso VARCHAR(40), Numero INT, Mensaje NVARCHAR(300));
GO

-- 1. IN no admite una subconsulta
BEGIN TRY
    EXEC (N'SELECT * FROM (SELECT Producto, Monto FROM ventas.Venta) AS Origen
            PIVOT (SUM(Monto) FOR Producto IN (SELECT DISTINCT Producto FROM ventas.Venta)) AS Pv');
END TRY
BEGIN CATCH
    INSERT INTO #Resultado VALUES ('IN con subconsulta', ERROR_NUMBER(), ERROR_MESSAGE());
END CATCH;

-- 2. Solo se admite un agregado
BEGIN TRY
    EXEC (N'SELECT * FROM (SELECT Producto, Monto FROM ventas.Venta) AS Origen
            PIVOT (SUM(Monto), COUNT(Monto) FOR Producto IN ([Teclado])) AS Pv');
END TRY
BEGIN CATCH
    INSERT INTO #Resultado VALUES ('dos agregados', ERROR_NUMBER(), ERROR_MESSAGE());
END CATCH;

SELECT Caso, Numero, Mensaje FROM #Resultado ORDER BY Caso;
```

| Caso | Numero | Mensaje |
|---|---:|---|
| IN con subconsulta | 156 | Incorrect syntax near the keyword 'SELECT'. |
| dos agregados | 102 | Incorrect syntax near ','. |

## Autoevaluación

<details>
<summary>1. ¿Qué diferencia hay entre `PIVOT` con `COUNT` y con `SUM` en las celdas sin datos?</summary>

`COUNT` devuelve 0; `SUM` devuelve `NULL`.
</details>

<details>
<summary>2. ¿Por qué se usa una subconsulta como origen?</summary>

Porque `PIVOT` agrupa por todas las columnas del origen que no son la agregada ni la del `FOR`. La subconsulta deja solo las necesarias.
</details>

<details>
<summary>3. ¿Cómo se conservan los `NULL` al despivotar?</summary>

Con `CROSS APPLY (VALUES ...)`, porque `UNPIVOT` los elimina.
</details>

:::tip[En resumen]
- `PIVOT` rota valores en columnas con un único agregado; `UNPIVOT` rota columnas en filas y descarta `NULL`.
- Siempre con una subconsulta de origen con solo las columnas necesarias.
- La lista de `IN` es fija; para listas variables se usa SQL dinámico en un solo lote.
:::

:::tip[Para seguir]
Practicá con la [Práctica — PIVOT](/bbdd-aplicadas/unidad-1/practica/pivot/) y después seguí con [SQL Dinámico](/bbdd-aplicadas/unidad-1/teoria/sql-dinamico/), que completa el PIVOT dinámico.
:::

## Fuentes

- Presentación de cátedra, Unidad 1, PIVOT (2024).
- Microsoft Learn, [FROM - PIVOT y UNPIVOT](https://learn.microsoft.com/es-es/sql/t-sql/queries/from-using-pivot-and-unpivot).
