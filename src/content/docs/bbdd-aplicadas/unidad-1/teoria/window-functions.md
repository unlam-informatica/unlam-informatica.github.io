---
title: Window Functions
slug: bbdd-aplicadas/unidad-1/teoria/window-functions
sidebar:
  order: 3
---

Las funciones de ventana (*window functions*) calculan un valor para cada fila a partir de un conjunto de filas relacionadas con ella, **sin colapsar el resultado** como hace `GROUP BY`. Sirven para rankear, acumular, comparar con la fila anterior o calcular porcentajes sin perder el detalle.

Presuponen [repaso de SQL](/bbdd-aplicadas/unidad-1/teoria/repaso-sql/) (`JOIN`, `GROUP BY`). Las páginas de [CTE](/bbdd-aplicadas/unidad-1/teoria/cte/), [PIVOT](/bbdd-aplicadas/unidad-1/teoria/pivot/) y [SQL dinámico](/bbdd-aplicadas/unidad-1/teoria/sql-dinamico/) usan el mismo esquema de ejemplo.

## Esquema de ejemplo

Todas las páginas de SQL avanzado de la unidad usan el esquema `ventas`: siete vendedores en dos regiones, con un supervisor opcional, y dieciséis ventas entre enero y abril de 2025. Hay empates de sueldo y de monto a propósito, porque son los casos límite que distinguen una función de otra.

<!-- check: U1.T.WF.01 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Vendedor (
    VendedorId   INT           NOT NULL,
    Nombre       VARCHAR(30)   NOT NULL,
    Region       VARCHAR(10)   NOT NULL,
    SupervisorId INT           NULL,
    Sueldo       DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Vendedor PRIMARY KEY (VendedorId),
    CONSTRAINT FK_Vendedor_Supervisor FOREIGN KEY (SupervisorId) REFERENCES ventas.Vendedor (VendedorId)
);

CREATE TABLE ventas.Venta (
    VentaId    INT           NOT NULL,
    VendedorId INT           NOT NULL,
    Fecha      DATE          NOT NULL,
    Producto   VARCHAR(20)   NOT NULL,
    Monto      DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Venta PRIMARY KEY (VentaId),
    CONSTRAINT FK_Venta_Vendedor FOREIGN KEY (VendedorId) REFERENCES ventas.Vendedor (VendedorId)
);

INSERT INTO ventas.Vendedor (VendedorId, Nombre, Region, SupervisorId, Sueldo)
VALUES
    (1, 'Ana',  'Norte', NULL, 5000.00),
    (2, 'Beto', 'Norte', 1,    3200.00),
    (3, 'Cora', 'Norte', 1,    3200.00),
    (4, 'Dario','Sur',   1,    4100.00),
    (5, 'Eva',  'Sur',   4,    2800.00),
    (6, 'Fede', 'Sur',   4,    3500.00),
    (7, 'Gina', 'Sur',   4,    2800.00);

INSERT INTO ventas.Venta (VentaId, VendedorId, Fecha, Producto, Monto)
VALUES
    (1,  2, '2025-01-10', 'Teclado',  200.00),
    (2,  3, '2025-01-15', 'Monitor',  500.00),
    (3,  2, '2025-01-28', 'Monitor',  500.00),
    (4,  5, '2025-01-30', 'Teclado',  200.00),
    (5,  6, '2025-02-05', 'Notebook', 1200.00),
    (6,  2, '2025-02-12', 'Teclado',  150.00),
    (7,  3, '2025-02-20', 'Notebook', 1200.00),
    (8,  5, '2025-02-25', 'Monitor',  500.00),
    (9,  7, '2025-02-27', 'Teclado',  200.00),
    (10, 3, '2025-03-03', 'Teclado',  200.00),
    (11, 6, '2025-03-10', 'Monitor',  500.00),
    (12, 5, '2025-03-18', 'Notebook', 1200.00),
    (13, 7, '2025-03-22', 'Monitor',  500.00),
    (14, 2, '2025-04-02', 'Notebook', 1200.00),
    (15, 6, '2025-04-15', 'Teclado',  150.00),
    (16, 4, '2025-04-20', 'Monitor',  500.00);
GO

SELECT
    (SELECT COUNT(*) FROM ventas.Vendedor) AS Vendedores,
    (SELECT COUNT(*) FROM ventas.Venta)    AS Ventas;
```

**Resultado esperado.**

| Vendedores | Ventas |
|---:|---:|
| 7 | 16 |

Ejecutá primero el bloque anterior en una base de práctica (ver [Cómo estudiar · Antes de ejecutar los ejemplos](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos)): crea el esquema `ventas` y carga los datos. Los ejemplos que siguen, en esta y en las otras páginas de SQL avanzado, usan esas tablas y no las vuelven a crear. Valen para SQL Server 2019 o 2022; los resultados se obtuvieron con SQL Server 2022.

## Para qué sirve

Con `GROUP BY` obtenemos un total por región, pero perdemos a los vendedores:

<!-- check: U1.T.WF.02 -->
```sql
SELECT
    Region,
    SUM(Sueldo) AS TotalRegion
FROM ventas.Vendedor
GROUP BY Region
ORDER BY Region;
```

| Region | TotalRegion |
|---|---:|
| Norte | 11400.00 |
| Sur | 13200.00 |

Con una función de ventana el total por región aparece **en cada fila** y conservamos el detalle. Además podemos calcular, en la misma consulta, qué porcentaje representa cada sueldo:

<!-- check: U1.T.WF.03 -->
```sql
SELECT
    Nombre,
    Region,
    Sueldo,
    SUM(Sueldo) OVER (PARTITION BY Region) AS TotalRegion,
    CAST(Sueldo * 100.0 / SUM(Sueldo) OVER (PARTITION BY Region) AS DECIMAL(5,1)) AS PorcentajeRegion
FROM ventas.Vendedor
ORDER BY Region, VendedorId;
```

| Nombre | Region | Sueldo | TotalRegion | PorcentajeRegion |
|---|---|---:|---:|---:|
| Ana | Norte | 5000.00 | 11400.00 | 43.9 |
| Beto | Norte | 3200.00 | 11400.00 | 28.1 |
| Cora | Norte | 3200.00 | 11400.00 | 28.1 |
| Dario | Sur | 4100.00 | 13200.00 | 31.1 |
| Eva | Sur | 2800.00 | 13200.00 | 21.2 |
| Fede | Sur | 3500.00 | 13200.00 | 26.5 |
| Gina | Sur | 2800.00 | 13200.00 | 21.2 |

## Anatomía de `OVER`

<!-- sintaxis -->
```sql
FUNCION(...) OVER (
    PARTITION BY columnas          -- divide las filas en grupos independientes
    ORDER BY columnas [ASC|DESC]   -- ordena las filas dentro de cada grupo
    ROWS | RANGE BETWEEN ... AND ... -- marco: qué filas de la partición ve cada fila
)
```

:::note[Definición]
La **ventana** de una fila es el conjunto de filas que la función puede ver cuando calcula esa fila. `PARTITION BY` reparte las filas en particiones; `ORDER BY` las ordena dentro de cada partición; el **marco** (*frame*) recorta la partición alrededor de la fila actual.
:::

| Cláusula | Qué hace | Cuándo es obligatoria |
|---|---|---|
| `PARTITION BY` | Parte la tabla en grupos. Si se omite, toda la tabla es una única partición | Nunca |
| `ORDER BY` | Ordena dentro de la partición | Siempre en ranking, `NTILE`, `LAG`/`LEAD`, `FIRST_VALUE`/`LAST_VALUE`, `PERCENT_RANK` y `CUME_DIST`, y siempre que haya marco |
| Marco (`ROWS`/`RANGE`) | Define qué filas entran en el cálculo | Nunca; si hay `ORDER BY` y se omite, rige el marco por defecto |

Las funciones de ventana solo se pueden escribir en el `SELECT` y en el `ORDER BY`. Para filtrar por su resultado hay que envolver la consulta en una [CTE](/bbdd-aplicadas/unidad-1/teoria/cte/) o una subconsulta.

## Funciones de agregado con `OVER`

`SUM`, `AVG`, `COUNT`, `MIN` y `MAX` aceptan `OVER`. Sin `ORDER BY` calculan sobre toda la partición (como en el ejemplo anterior). Con `ORDER BY` calculan un valor **acumulado** hasta la fila actual.

Los totales por mes salen de un `GROUP BY`; encima aplicamos ventanas sobre esos totales ya agregados (por eso aparece `SUM(SUM(Monto))`):

<!-- check: U1.T.WF.04 -->
```sql
SELECT
    MONTH(Fecha)                                          AS Mes,
    SUM(Monto)                                            AS TotalMes,
    SUM(SUM(Monto)) OVER (ORDER BY MONTH(Fecha)
                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS Acumulado,
    CAST(AVG(SUM(Monto)) OVER (ORDER BY MONTH(Fecha)
                          ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS DECIMAL(10,2)) AS MediaMovil2
FROM ventas.Venta
GROUP BY MONTH(Fecha)
ORDER BY Mes;
```

| Mes | TotalMes | Acumulado | MediaMovil2 |
|---:|---:|---:|---:|
| 1 | 1400.00 | 1400.00 | 1400.00 |
| 2 | 3250.00 | 4650.00 | 2325.00 |
| 3 | 2400.00 | 7050.00 | 2825.00 |
| 4 | 1850.00 | 8900.00 | 2125.00 |

`MediaMovil2` promedia la fila actual y la anterior (`1 PRECEDING`). En enero solo existe la fila actual, y por eso el promedio es 1400.

## Funciones de ranking

Devuelven una posición dentro de la partición y **exigen `ORDER BY`**. No admiten marco.

| Función | Empates | Numeración |
|---|---|---|
| `ROW_NUMBER()` | Los desempata arbitrariamente (conviene agregar una columna de desempate) | 1, 2, 3, 4 |
| `RANK()` | Mismo puesto, y luego **salta** | 1, 2, 2, 4 |
| `DENSE_RANK()` | Mismo puesto, **sin saltos** | 1, 2, 2, 3 |
| `NTILE(n)` | Reparte las filas en `n` grupos de tamaño casi igual | 1, 1, 2, 2 |

<!-- check: U1.T.WF.05 -->
```sql
SELECT
    Nombre,
    Region,
    Sueldo,
    ROW_NUMBER() OVER (PARTITION BY Region ORDER BY Sueldo DESC, Nombre) AS NroFila,
    RANK()       OVER (PARTITION BY Region ORDER BY Sueldo DESC)         AS PuestoRank,
    DENSE_RANK() OVER (PARTITION BY Region ORDER BY Sueldo DESC)         AS PuestoDenso,
    NTILE(2)     OVER (PARTITION BY Region ORDER BY Sueldo DESC, Nombre) AS Mitad
FROM ventas.Vendedor
ORDER BY Region, NroFila;
```

| Nombre | Region | Sueldo | NroFila | PuestoRank | PuestoDenso | Mitad |
|---|---|---:|---:|---:|---:|---:|
| Ana | Norte | 5000.00 | 1 | 1 | 1 | 1 |
| Beto | Norte | 3200.00 | 2 | 2 | 2 | 1 |
| Cora | Norte | 3200.00 | 3 | 2 | 2 | 2 |
| Dario | Sur | 4100.00 | 1 | 1 | 1 | 1 |
| Fede | Sur | 3500.00 | 2 | 2 | 2 | 1 |
| Eva | Sur | 2800.00 | 3 | 3 | 3 | 2 |
| Gina | Sur | 2800.00 | 4 | 3 | 3 | 2 |

En Norte, Beto y Cora empatan en 3200: `RANK` y `DENSE_RANK` les dan el puesto 2, y `ROW_NUMBER` les da 2 y 3 (el desempate por nombre lo decidimos nosotros). En Sur, Eva y Gina empatan en el puesto 3. Como los empates están al final no se ve el salto de `RANK`: aparecería si el empate fuera en el primer puesto (1, 1, 3) y `DENSE_RANK` seguiría con 1, 1, 2.

`NTILE` con una cantidad de filas no divisible: cuando las filas no se reparten en partes iguales, los grupos **más grandes van primero**. Norte tiene 3 filas y `NTILE(2)` forma un grupo de 2 y otro de 1.

## `LAG` y `LEAD`

`LAG(expresión, desplazamiento, valor_por_defecto)` lee una fila anterior de la partición y `LEAD` una posterior. El desplazamiento es 1 por defecto y el valor por defecto es `NULL`. Reemplazan al auto-`JOIN` para comparar filas consecutivas.

<!-- check: U1.T.WF.06 -->
```sql
WITH TotalMensual AS (
    SELECT
        MONTH(Fecha) AS Mes,
        SUM(Monto)   AS Total
    FROM ventas.Venta
    GROUP BY MONTH(Fecha)
)
SELECT
    Mes,
    Total,
    LAG(Total, 1, 0)  OVER (ORDER BY Mes) AS MesAnterior,
    Total - LAG(Total, 1, 0) OVER (ORDER BY Mes) AS Variacion,
    LEAD(Total)       OVER (ORDER BY Mes) AS MesSiguiente
FROM TotalMensual
ORDER BY Mes;
```

| Mes | Total | MesAnterior | Variacion | MesSiguiente |
|---:|---:|---:|---:|---:|
| 1 | 1400.00 | 0.00 | 1400.00 | 3250.00 |
| 2 | 3250.00 | 1400.00 | 1850.00 | 2400.00 |
| 3 | 2400.00 | 3250.00 | -850.00 | 1850.00 |
| 4 | 1850.00 | 2400.00 | -550.00 | `NULL` |

Con el valor por defecto 0, la variación de enero es el total completo. Si lo omitimos, `MesAnterior` y `Variacion` serían `NULL` en la primera fila, que suele ser lo correcto cuando "no hay mes anterior" no equivale a "vendió cero".

## `FIRST_VALUE` y `LAST_VALUE`, y el marco por defecto

`FIRST_VALUE` y `LAST_VALUE` devuelven el valor de la primera y de la última fila **del marco**. Aquí aparece el error clásico.

:::caution[El marco por defecto hace "fallar" LAST_VALUE]
Cuando la ventana tiene `ORDER BY` y no se escribe marco, SQL Server usa `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`: desde el comienzo de la partición **hasta la fila actual** (y sus empates). La última fila de ese marco es la fila actual, así que `LAST_VALUE` devuelve el valor de la propia fila. Para ver el final de la partición hay que pedir el marco completo: `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.
:::

<!-- check: U1.T.WF.07 -->
```sql
SELECT
    Nombre,
    Region,
    Sueldo,
    FIRST_VALUE(Nombre) OVER (PARTITION BY Region ORDER BY Sueldo DESC, Nombre) AS MejorPago,
    LAST_VALUE(Nombre)  OVER (PARTITION BY Region ORDER BY Sueldo DESC, Nombre) AS UltimoMarcoPorDefecto,
    LAST_VALUE(Nombre)  OVER (PARTITION BY Region ORDER BY Sueldo DESC, Nombre
                              ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS MenosPago
FROM ventas.Vendedor
ORDER BY Region, Sueldo DESC, Nombre;
```

| Nombre | Region | Sueldo | MejorPago | UltimoMarcoPorDefecto | MenosPago |
|---|---|---:|---|---|---|
| Ana | Norte | 5000.00 | Ana | Ana | Cora |
| Beto | Norte | 3200.00 | Ana | Beto | Cora |
| Cora | Norte | 3200.00 | Ana | Cora | Cora |
| Dario | Sur | 4100.00 | Dario | Dario | Gina |
| Fede | Sur | 3500.00 | Dario | Fede | Gina |
| Eva | Sur | 2800.00 | Dario | Eva | Gina |
| Gina | Sur | 2800.00 | Dario | Gina | Gina |

`FIRST_VALUE` no tiene el problema porque la primera fila siempre está dentro del marco por defecto.

## `PERCENT_RANK` y `CUME_DIST`

Ubican una fila entre 0 y 1 dentro de la partición. Sea `RANK` el puesto de la fila con `RANK()`, `n` la cantidad de filas de la partición y `c` la cantidad de filas cuyo valor es **menor o igual** que el de la fila actual (todas las empatadas cuentan):

| Función | Fórmula | Mínimo | Máximo |
|---|---|---|---|
| `PERCENT_RANK()` | $(RANK - 1) / (n - 1)$ | 0 | 1 |
| `CUME_DIST()` | $c / n$ | $1/n$ | 1 |

`CUME_DIST` **no** es `RANK / n`: con empates, difiere. En el ejemplo, los dos sueldos más bajos (2800) están empatados en el puesto 1: `RANK / n` daría 0,25 y `CUME_DIST` da 0,5, porque ambas filas tienen valor menor o igual.

<!-- check: U1.T.WF.08 -->
```sql
SELECT
    Nombre,
    Sueldo,
    RANK()         OVER (ORDER BY Sueldo) AS Puesto,
    CAST(PERCENT_RANK() OVER (ORDER BY Sueldo) AS DECIMAL(5,3)) AS PercentRank,
    CAST(CUME_DIST()    OVER (ORDER BY Sueldo) AS DECIMAL(5,3)) AS CumeDist
FROM ventas.Vendedor
WHERE Region = 'Sur'
ORDER BY Sueldo, Nombre;
```

| Nombre | Sueldo | Puesto | PercentRank | CumeDist |
|---|---:|---:|---:|---:|
| Eva | 2800.00 | 1 | 0.000 | 0.500 |
| Gina | 2800.00 | 1 | 0.000 | 0.500 |
| Fede | 3500.00 | 3 | 0.667 | 0.750 |
| Dario | 4100.00 | 4 | 1.000 | 1.000 |

## Marcos: `ROWS` y `RANGE`

| Delimitador | Significado |
|---|---|
| `UNBOUNDED PRECEDING` | Desde la primera fila de la partición |
| `N PRECEDING` | `N` filas antes de la actual (solo en `ROWS`) |
| `CURRENT ROW` | La fila actual |
| `N FOLLOWING` | `N` filas después de la actual (solo en `ROWS`) |
| `UNBOUNDED FOLLOWING` | Hasta la última fila de la partición |

- `ROWS` cuenta **filas físicas**: la fila actual y las `N` de al lado.
- `RANGE` trabaja con **valores**: incluye a todos los pares (filas con el mismo valor de `ORDER BY`) de la fila actual. En SQL Server solo admite `UNBOUNDED` y `CURRENT ROW`.

Los empates marcan la diferencia. Tomamos las ventas de enero ordenadas por monto, con dos ventas de 200 y dos de 500:

<!-- check: U1.T.WF.09 -->
```sql
SELECT
    VentaId,
    Monto,
    SUM(Monto) OVER (ORDER BY Monto)                                  AS PorDefecto,
    SUM(Monto) OVER (ORDER BY Monto RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS ConRange,
    SUM(Monto) OVER (ORDER BY Monto ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)  AS ConRows
FROM ventas.Venta
WHERE Fecha < '2025-02-01'
ORDER BY Monto, VentaId;
```

| VentaId | Monto | PorDefecto | ConRange | ConRows |
|---:|---:|---:|---:|---:|
| 1 | 200.00 | 400.00 | 400.00 | 200.00 |
| 4 | 200.00 | 400.00 | 400.00 | 400.00 |
| 2 | 500.00 | 1400.00 | 1400.00 | 900.00 |
| 3 | 500.00 | 1400.00 | 1400.00 | 1400.00 |

`PorDefecto` y `ConRange` coinciden: el marco por defecto **es** `RANGE`. Por eso, un acumulado con empates en el `ORDER BY` repite el valor para los pares. Para un acumulado fila a fila hay que escribir `ROWS`, y conviene ordenar por una columna única.

## Errores frecuentes

:::caution[Errores frecuentes]
- **Marco sin `ORDER BY`.** `ROWS` y `RANGE` requieren `ORDER BY`, incluso con `UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`. Sin él, SQL Server devuelve el error 10756. Para sumar toda la partición alcanza con `SUM(...) OVER (PARTITION BY ...)`, sin marco.
- **Ranking sin `ORDER BY`.** `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, `LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE`, `PERCENT_RANK` y `CUME_DIST` dan el error 4112.
- **Marco en una función que no lo admite.** `LAG`, `LEAD` y las de ranking dan el error 10752.
- **Filtrar con una función de ventana en `WHERE`.** Da el error 4108: hay que usar una CTE.
- **`RANGE` con desplazamiento numérico.** Error 4194.
:::

Para ver los cinco errores en una sola tabla, el script del recuadro siguiente ejecuta cada consulta defectuosa como texto con `EXEC`, dentro de un `TRY ... CATCH`, y reúne el número y el mensaje de cada error en una tabla temporal. Si ejecutás cada consulta por separado, el error aparece en el panel de mensajes. El idioma de los mensajes depende de la instalación:

| Caso | Número | Mensaje |
|---:|---:|---|
| 1 | 10756 | Window frame with ROWS or RANGE must have an ORDER BY clause. |
| 2 | 4112 | The function 'ROW_NUMBER' must have an OVER clause with ORDER BY. |
| 3 | 10752 | The function 'LAG' may not have a window frame. |
| 4 | 4194 | RANGE is only supported with UNBOUNDED and CURRENT ROW window frame delimiters. |
| 5 | 4108 | Windowed functions can only appear in the SELECT or ORDER BY clauses. |

<details>
<summary>Script que produce esa tabla</summary>

<!-- check: U1.T.WF.10 -->
```sql
DECLARE @Consulta NVARCHAR(MAX);
DECLARE @Casos TABLE (Caso INT, Consulta NVARCHAR(MAX));

INSERT INTO @Casos (Caso, Consulta)
VALUES
    (1, N'SELECT SUM(Monto) OVER (PARTITION BY VendedorId ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM ventas.Venta'),
    (2, N'SELECT ROW_NUMBER() OVER (PARTITION BY VendedorId) FROM ventas.Venta'),
    (3, N'SELECT LAG(Monto) OVER (ORDER BY Fecha ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) FROM ventas.Venta'),
    (4, N'SELECT SUM(Monto) OVER (ORDER BY Fecha RANGE BETWEEN 1 PRECEDING AND CURRENT ROW) FROM ventas.Venta'),
    (5, N'SELECT VentaId FROM ventas.Venta WHERE ROW_NUMBER() OVER (ORDER BY Monto) = 1');

CREATE TABLE #Resultado (Caso INT, Numero INT, Mensaje NVARCHAR(200));

DECLARE @Caso INT = 1;
WHILE @Caso <= 5
BEGIN
    SELECT @Consulta = Consulta FROM @Casos WHERE Caso = @Caso;
    BEGIN TRY
        EXEC (@Consulta);
    END TRY
    BEGIN CATCH
        INSERT INTO #Resultado VALUES (@Caso, ERROR_NUMBER(), ERROR_MESSAGE());
    END CATCH;
    SET @Caso += 1;
END;

SELECT Caso, Numero, Mensaje FROM #Resultado ORDER BY Caso;
```

</details>

## Rendimiento

Una ventana con `PARTITION BY` y `ORDER BY` obliga a ordenar los datos; un índice no clúster sobre `(columnas de partición, columnas de orden)` puede evitar esa ordenación. Los detalles de planes e índices están en la [Unidad 3](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/).

## Autoevaluación

<details>
<summary>1. ¿Por qué `LAST_VALUE(x) OVER (ORDER BY y)` devuelve el valor de la propia fila?</summary>

Porque con `ORDER BY` y sin marco explícito el marco es `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, y la última fila de ese marco es la fila actual (o la última de sus empates). Se corrige con `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.
</details>

<details>
<summary>2. Cuatro filas con valores 10, 10, 20, 30: ¿cuánto vale `CUME_DIST` en las dos primeras?</summary>

0,5: dos de las cuatro filas tienen un valor menor o igual a 10. `PERCENT_RANK` vale 0 en las dos primeras.
</details>

<details>
<summary>3. ¿Se puede escribir `SUM(Monto) OVER (PARTITION BY VendedorId ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)`?</summary>

No: falta `ORDER BY` (error 10756). Es innecesario: `SUM(Monto) OVER (PARTITION BY VendedorId)` ya suma toda la partición.
</details>

:::tip[En resumen]
- Una ventana calcula sobre un conjunto de filas sin colapsar el resultado.
- Ranking, `NTILE`, `LAG`/`LEAD`, `FIRST_VALUE`/`LAST_VALUE`, `PERCENT_RANK` y `CUME_DIST` necesitan `ORDER BY`; el marco también.
- El marco por defecto con `ORDER BY` es `RANGE ... UNBOUNDED PRECEDING AND CURRENT ROW`: explica el acumulado con empates y el fallo de `LAST_VALUE`.
- `CUME_DIST` es la proporción de filas con valor menor o igual; `PERCENT_RANK` es `(RANK - 1) / (n - 1)`.
:::

:::tip[Para seguir]
Practicá con la [Práctica — Window Functions](/bbdd-aplicadas/unidad-1/practica/window-functions/) y después seguí con [Common Table Expressions](/bbdd-aplicadas/unidad-1/teoria/cte/).
:::

## Fuentes

- Presentación de cátedra, Unidad 1, funciones de ventana (v1.0, 2024).
- Microsoft Learn, [SELECT - cláusula OVER (Transact-SQL)](https://learn.microsoft.com/es-es/sql/t-sql/queries/select-over-clause-transact-sql).
- Microsoft Learn, [CUME_DIST](https://learn.microsoft.com/es-es/sql/t-sql/functions/cume-dist-transact-sql) y [PERCENT_RANK](https://learn.microsoft.com/es-es/sql/t-sql/functions/percent-rank-transact-sql).
