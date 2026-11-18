---
title: Common Table Expressions
slug: bbdd-aplicadas/unidad-1/teoria/cte
sidebar:
  order: 5
---

Una **common table expression (CTE)** es un resultado con nombre que existe solo durante **una** sentencia. Se declara con `WITH` antes del `SELECT`, `INSERT`, `UPDATE`, `DELETE` o `MERGE` que la usa. Sirve para dar nombre a un paso intermedio, para filtrar por el resultado de una [función de ventana](/bbdd-aplicadas/unidad-1/teoria/window-functions/) y para recorrer jerarquías.

Los ejemplos usan el esquema `ventas` de la página de [window functions](/bbdd-aplicadas/unidad-1/teoria/window-functions/#esquema-de-ejemplo). Se ejecutan sobre una base vacía donde ya se creó ese esquema.

<!-- sintaxis -->
```sql
WITH NombreCte (Columna1, Columna2) AS (
    SELECT ...          -- la lista de columnas es opcional
)
SELECT ... FROM NombreCte;
```

## CTE simple

Los vendedores que cobran más que el promedio de su región. La función de ventana no puede ir en el `WHERE`, así que la calculamos dentro de la CTE y filtramos afuera.

<!-- check: U1.T.CTE.01 -->
```sql
WITH SueldoRegion AS (
    SELECT
        VendedorId,
        Nombre,
        Region,
        Sueldo,
        CAST(AVG(Sueldo) OVER (PARTITION BY Region) AS DECIMAL(10,2)) AS PromedioRegion
    FROM ventas.Vendedor
)
SELECT
    Nombre,
    Region,
    Sueldo,
    PromedioRegion
FROM SueldoRegion
WHERE Sueldo > PromedioRegion
ORDER BY Region, Nombre;
```

| Nombre | Region | Sueldo | PromedioRegion |
|---|---|---:|---:|
| Ana | Norte | 5000.00 | 3800.00 |
| Dario | Sur | 4100.00 | 3300.00 |
| Fede | Sur | 3500.00 | 3300.00 |

## Varias CTE encadenadas

Se separan con coma, con un único `WITH`. Cada una puede usar las anteriores. Acá, el total por vendedor, después su puesto, y al final el cruce con `Vendedor` para mostrar el nombre.

<!-- check: U1.T.CTE.02 -->
```sql
WITH TotalVendedor AS (
    SELECT
        VendedorId,
        COUNT(*)   AS Ventas,
        SUM(Monto) AS Total
    FROM ventas.Venta
    GROUP BY VendedorId
),
Ranking AS (
    SELECT
        VendedorId,
        Ventas,
        Total,
        DENSE_RANK() OVER (ORDER BY Total DESC) AS Puesto
    FROM TotalVendedor
)
SELECT
    v.Nombre,
    r.Ventas,
    r.Total,
    r.Puesto
FROM Ranking AS r
INNER JOIN ventas.Vendedor AS v
    ON v.VendedorId = r.VendedorId
WHERE r.Puesto <= 3
ORDER BY r.Puesto, v.Nombre;
```

| Nombre | Ventas | Total | Puesto |
|---|---:|---:|---:|
| Beto | 4 | 2050.00 | 1 |
| Cora | 3 | 1900.00 | 2 |
| Eva | 3 | 1900.00 | 2 |
| Fede | 3 | 1850.00 | 3 |

## CTE recursiva

Una CTE recursiva se referencia a sí misma. Tiene un **miembro ancla** (el punto de partida), un `UNION ALL` y un **miembro recursivo** que parte de lo que ya se obtuvo. La recursión termina cuando el miembro recursivo no devuelve filas. Es la herramienta para jerarquías, como el organigrama de `Vendedor` (`SupervisorId`).

<!-- check: U1.T.CTE.03 -->
```sql
WITH Organigrama AS (
    -- Caso base: quien no tiene supervisor
    SELECT
        VendedorId,
        Nombre,
        SupervisorId,
        0                          AS Nivel,
        CAST(Nombre AS VARCHAR(200)) AS Camino
    FROM ventas.Vendedor
    WHERE SupervisorId IS NULL

    UNION ALL

    -- Caso recursivo: quienes dependen de alguien que ya está en el resultado
    SELECT
        v.VendedorId,
        v.Nombre,
        v.SupervisorId,
        o.Nivel + 1,
        CAST(o.Camino + ' > ' + v.Nombre AS VARCHAR(200))
    FROM ventas.Vendedor AS v
    INNER JOIN Organigrama AS o
        ON v.SupervisorId = o.VendedorId
)
SELECT
    VendedorId,
    Nombre,
    Nivel,
    Camino
FROM Organigrama
ORDER BY Camino;
```

| VendedorId | Nombre | Nivel | Camino |
|---:|---|---:|---|
| 1 | Ana | 0 | Ana |
| 2 | Beto | 1 | Ana > Beto |
| 3 | Cora | 1 | Ana > Cora |
| 4 | Dario | 1 | Ana > Dario |
| 5 | Eva | 2 | Ana > Dario > Eva |
| 6 | Fede | 2 | Ana > Dario > Fede |
| 7 | Gina | 2 | Ana > Dario > Gina |

El tipo de las columnas del miembro recursivo tiene que coincidir con el del ancla, por eso `Camino` lleva un `CAST` explícito.

### `MAXRECURSION`

SQL Server corta la recursión a los **100 niveles** por defecto (error 530). `OPTION (MAXRECURSION n)` lo cambia, y `0` quita el límite. Un límite alto protege de bucles infinitos, que ocurren si los datos tienen ciclos (por ejemplo un supervisor que se supervisa a sí mismo).

<!-- check: U1.T.CTE.04 -->
```sql
CREATE TABLE #Resultado (Caso VARCHAR(30), Numero INT, Filas INT);
GO

-- Con el límite por defecto (100 niveles) la recursión de 150 pasos falla
BEGIN TRY
    DECLARE @Cantidad INT;
    WITH Numeros AS (
        SELECT 1 AS N
        UNION ALL
        SELECT N + 1 FROM Numeros WHERE N < 150
    )
    SELECT @Cantidad = COUNT(*) FROM Numeros;
END TRY
BEGIN CATCH
    INSERT INTO #Resultado VALUES ('limite por defecto', ERROR_NUMBER(), NULL);
END CATCH;

-- Con OPTION (MAXRECURSION 200) alcanza
WITH Numeros AS (
    SELECT 1 AS N
    UNION ALL
    SELECT N + 1 FROM Numeros WHERE N < 150
)
INSERT INTO #Resultado
SELECT 'MAXRECURSION 200', 0, COUNT(*)
FROM Numeros
OPTION (MAXRECURSION 200);

SELECT Caso, Numero, Filas FROM #Resultado ORDER BY Caso;
```

| Caso | Numero | Filas |
|---|---:|---:|
| limite por defecto | 530 | `NULL` |
| MAXRECURSION 200 | 0 | 150 |

## CTE con `DELETE`, `UPDATE` e `INSERT`

La CTE puede ser el destino de la modificación: el cambio se aplica a la tabla base. Para eso la CTE tiene que apuntar a **una sola tabla** y sus columnas no pueden ser derivadas de un agregado.

El patrón clásico es eliminar duplicados: la CTE numera las copias y el `DELETE` borra las sobrantes. Con `UPDATE` actuamos sobre las filas filtradas por la CTE. Antes se crea una tabla de carga con filas repetidas.

<!-- check: U1.T.CTE.05 -->
```sql
CREATE TABLE ventas.VentaCarga (
    CargaId    INT           NOT NULL IDENTITY(1, 1),
    VendedorId INT           NOT NULL,
    Fecha      DATE          NOT NULL,
    Monto      DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_VentaCarga PRIMARY KEY (CargaId)
);
GO

INSERT INTO ventas.VentaCarga (VendedorId, Fecha, Monto)
VALUES
    (2, '2025-01-10', 200.00),
    (2, '2025-01-10', 200.00),
    (3, '2025-01-15', 500.00),
    (3, '2025-01-15', 500.00),
    (3, '2025-01-15', 500.00),
    (5, '2025-01-30', 200.00);
GO

-- DELETE sobre la CTE: borra de la tabla base las copias sobrantes
WITH Numerada AS (
    SELECT
        ROW_NUMBER() OVER (PARTITION BY VendedorId, Fecha, Monto ORDER BY CargaId) AS Copia
    FROM ventas.VentaCarga
)
DELETE FROM Numerada
WHERE Copia > 1;

-- UPDATE sobre la CTE: aumento del 10 % a la región Sur
WITH Sur AS (
    SELECT Sueldo
    FROM ventas.Vendedor
    WHERE Region = 'Sur'
)
UPDATE Sur
SET Sueldo = Sueldo * 1.10;

SELECT CargaId, VendedorId, Fecha, Monto FROM ventas.VentaCarga ORDER BY CargaId;
SELECT VendedorId, Nombre, Sueldo FROM ventas.Vendedor ORDER BY VendedorId;
```

Primer resultado (`VentaCarga`, quedó una copia por venta):

| CargaId | VendedorId | Fecha | Monto |
|---:|---:|---|---:|
| 1 | 2 | 2025-01-10 | 200.00 |
| 3 | 3 | 2025-01-15 | 500.00 |
| 6 | 5 | 2025-01-30 | 200.00 |

Segundo resultado (`Vendedor`, la región Sur con 10 % de aumento):

| VendedorId | Nombre | Sueldo |
|---:|---|---:|
| 1 | Ana | 5000.00 |
| 2 | Beto | 3200.00 |
| 3 | Cora | 3200.00 |
| 4 | Dario | 4510.00 |
| 5 | Eva | 3080.00 |
| 6 | Fede | 3850.00 |
| 7 | Gina | 3080.00 |

También se puede escribir `WITH ... INSERT INTO destino SELECT ... FROM Cte`, como en el ejemplo de `MAXRECURSION`.

## Punto y coma previo y alcance de una sola sentencia

:::caution[Errores frecuentes]
- **La sentencia anterior debe terminar en `;`.** `WITH` también se usa en otras cláusulas (por ejemplo `WITH (NOLOCK)`), así que SQL Server exige que lo que lo precede esté cerrado (error 319). Por eso la guía de estilo termina siempre con `;` y la que precede a un `WITH`.
- **La CTE no sobrevive a la sentencia.** Una segunda sentencia que la nombre falla con el error 208 (nombre de objeto no válido). Si necesitamos reutilizarla en varias sentencias, usamos una tabla temporal o una vista.
:::

<!-- check: U1.T.CTE.06 -->
```sql
CREATE TABLE #Resultado (Caso VARCHAR(40), Numero INT, Mensaje NVARCHAR(300));
CREATE TABLE #Dato (Dos INT);
GO

-- 1. La sentencia anterior no termina en punto y coma
BEGIN TRY
    EXEC (N'SELECT 1 AS Uno
WITH Unico AS (SELECT 2 AS Dos) INSERT INTO #Dato SELECT Dos FROM Unico');
END TRY
BEGIN CATCH
    INSERT INTO #Resultado VALUES ('sin punto y coma previo', ERROR_NUMBER(), ERROR_MESSAGE());
END CATCH;

-- 2. La CTE solo existe en la sentencia que la sigue
BEGIN TRY
    EXEC (N'WITH Unico AS (SELECT 2 AS Dos) INSERT INTO #Dato SELECT Dos FROM Unico; INSERT INTO #Dato SELECT Dos FROM Unico;');
END TRY
BEGIN CATCH
    INSERT INTO #Resultado VALUES ('segunda sentencia', ERROR_NUMBER(), ERROR_MESSAGE());
END CATCH;

SELECT Caso, Numero, Mensaje FROM #Resultado ORDER BY Caso DESC;
```

| Caso | Numero | Mensaje |
|---|---:|---|
| sin punto y coma previo | 319 | Incorrect syntax near the keyword 'with'. If this statement is a common table expression, an xmlnamespaces clause or a change tracking context clause, the previous statement must be terminated with a semicolon. |
| segunda sentencia | 208 | Invalid object name 'Unico'. |

## CTE, subconsulta, vista y tabla temporal

| | CTE | Subconsulta | Tabla temporal (`#t`) | Vista |
|---|---|---|---|---|
| Legibilidad | Alta: tiene nombre y se define arriba | Baja si está anidada | Alta | Alta |
| Alcance | Una sentencia | Una sentencia | La sesión | Permanente |
| Recursión | Sí | No | No | No |
| Se materializa | No: es una definición | No | Sí, con estadísticas e índices | No (salvo vista indexada) |
| Uso típico | Pasos intermedios, jerarquías, duplicados | Filtros simples | Resultados que se reutilizan | Consulta compartida por muchos |

Limitaciones: una CTE no puede tener `ORDER BY` salvo con `TOP`, no se le pueden crear índices y no persiste. Que se evalúe una o varias veces si se la nombra varias veces depende del plan: normalmente el optimizador la expande en cada referencia, igual que una vista, y no hay garantía de que se calcule una sola vez. Los detalles de planes están en la [Unidad 3](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/).

## Autoevaluación

<details>
<summary>1. ¿Por qué falla `SELECT 1 WITH x AS (...) SELECT * FROM x` sin punto y coma después del primer `SELECT`?</summary>

`WITH` puede ser el comienzo de una CTE o una sugerencia de tabla; SQL Server exige que la sentencia previa esté terminada con `;` para no confundirlos (error 319).
</details>

<details>
<summary>2. ¿Qué pasa si una CTE recursiva tiene datos con un ciclo?</summary>

Recorre el ciclo hasta alcanzar el límite de recursión y da el error 530. Con `MAXRECURSION 0` no se detendría.
</details>

<details>
<summary>3. ¿Se puede usar una CTE en dos sentencias consecutivas?</summary>

No: existe solo para la sentencia que la sigue. La segunda da el error 208.
</details>

:::tip[En resumen]
- La CTE da nombre a un paso intermedio y vive una sola sentencia.
- Varias CTE se encadenan con coma y un único `WITH`.
- La recursiva tiene ancla, `UNION ALL` y miembro recursivo; el límite por defecto es 100 niveles.
- `DELETE`, `UPDATE` e `INSERT` pueden usar una CTE; es el patrón para eliminar duplicados.
- La sentencia previa a `WITH` termina en `;`.
:::

## Fuentes

- Presentación de cátedra, Unidad 1, CTE (2024).
- Microsoft Learn, [WITH common_table_expression (Transact-SQL)](https://learn.microsoft.com/es-es/sql/t-sql/queries/with-common-table-expression-transact-sql).
