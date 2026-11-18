---
title: Práctica — PIVOT
slug: bbdd-aplicadas/unidad-1/practica/pivot
sidebar:
  label: PIVOT
  order: 3
---

Nueve ejercicios sobre `PIVOT`, `UNPIVOT` y PIVOT dinámico. Presuponen la lección de [PIVOT](/bbdd-aplicadas/unidad-1/teoria/pivot/) y, para el ejercicio 5, [SQL dinámico](/bbdd-aplicadas/unidad-1/teoria/sql-dinamico/). Los datos son propios. El ejercicio 8 es una adaptación con datos propios de un enunciado de estilo parcial.

## Conjunto de datos

Creá una base de prueba (por ejemplo `CREATE DATABASE PracticaPivot;`), cambiá a ella y ejecutá:

<!-- check: U1.43 -->
```sql
CREATE SCHEMA practica;
GO

CREATE TABLE practica.Venta (
    VentaId  INT           NOT NULL IDENTITY(1, 1),
    Vendedor VARCHAR(50)   NOT NULL,
    Mes      VARCHAR(10)   NOT NULL,
    Producto VARCHAR(50)   NOT NULL,
    Monto    DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Venta PRIMARY KEY (VentaId)
);

CREATE TABLE practica.NotaFinal (
    Alumno  VARCHAR(50)   NOT NULL,
    Materia VARCHAR(50)   NOT NULL,
    Nota    DECIMAL(4,1)  NOT NULL,
    CONSTRAINT PK_NotaFinal PRIMARY KEY (Alumno, Materia)
);

CREATE TABLE practica.ResumenTrimestral (
    Departamento VARCHAR(50)   NOT NULL,
    Q1           DECIMAL(10,2) NULL,
    Q2           DECIMAL(10,2) NULL,
    Q3           DECIMAL(10,2) NULL,
    Q4           DECIMAL(10,2) NULL,
    CONSTRAINT PK_ResumenTrimestral PRIMARY KEY (Departamento)
);

CREATE TABLE practica.VentaCiudad (
    VentaId  INT           NOT NULL IDENTITY(1, 1),
    Cantidad INT           NOT NULL,
    Precio   DECIMAL(10,2) NOT NULL,
    Ciudad   VARCHAR(50)   NOT NULL,
    Vendedor VARCHAR(50)   NOT NULL,
    CONSTRAINT PK_VentaCiudad PRIMARY KEY (VentaId)
);
GO

INSERT INTO practica.Venta (Vendedor, Mes, Producto, Monto)
VALUES
    ('Ana', 'Enero', 'Laptop', 1500.00), ('Ana', 'Enero', 'Teclado', 300.00),
    ('Ana', 'Febrero', 'Monitor', 2000.00), ('Ana', 'Marzo', 'Laptop', 1800.00),
    ('Ana', 'Abril', 'Impresora', 2200.00), ('Ana', 'Mayo', 'Laptop', 1600.00),
    ('Ana', 'Junio', 'Monitor', 2500.00),
    ('Luis', 'Enero', 'Teclado', 900.00), ('Luis', 'Febrero', 'Mouse', 1100.00),
    ('Luis', 'Marzo', 'Teclado', 800.00), ('Luis', 'Mayo', 'Mouse', 1200.00),
    ('Luis', 'Junio', 'Teclado', 1400.00),
    ('Marta', 'Enero', 'Monitor', 2100.00), ('Marta', 'Febrero', 'Laptop', 1700.00),
    ('Marta', 'Marzo', 'Monitor', 2300.00), ('Marta', 'Abril', 'Laptop', 1900.00),
    ('Marta', 'Mayo', 'Monitor', 2100.00), ('Marta', 'Junio', 'Laptop', 2800.00),
    ('Carlos', 'Marzo', 'Mouse', 500.00), ('Carlos', 'Abril', 'Mouse', 700.00),
    ('Carlos', 'Mayo', 'Teclado', 600.00);

INSERT INTO practica.NotaFinal (Alumno, Materia, Nota)
VALUES
    ('Juan', 'Matemáticas', 7.0), ('Juan', 'Historia', 9.0), ('Juan', 'Inglés', 8.0),
    ('María', 'Matemáticas', 6.0), ('María', 'Física', 8.0),
    ('Pedro', 'Historia', 10.0), ('Pedro', 'Inglés', 7.0), ('Pedro', 'Física', 9.0),
    ('Laura', 'Matemáticas', 8.0), ('Laura', 'Historia', 8.0), ('Laura', 'Inglés', 9.0), ('Laura', 'Física', 7.0);

INSERT INTO practica.ResumenTrimestral (Departamento, Q1, Q2, Q3, Q4)
VALUES
    ('IT', 120.00, 150.00, 130.00, 200.00),
    ('Ventas', 300.00, 280.00, 320.00, 410.00),
    ('RRHH', 80.00, 95.00, NULL, 110.00);

INSERT INTO practica.VentaCiudad (Cantidad, Precio, Ciudad, Vendedor)
VALUES
    (1, 920.00, 'San Diego', 'Online'), (1, 22.50, 'Seattle', 'Valentina'),
    (2, 18.75, 'San Francisco', 'Sofia'), (1, 215.00, 'Los Angeles', 'Online'),
    (1, 18.75, 'Austin', 'Sofia'), (1, 5.99, 'San Francisco', 'Marcelo'),
    (1, 512.00, 'Los Angeles', 'Marcelo'), (1, 275.00, 'Los Angeles', 'Roberto'),
    (2, 95.00, 'Seattle', 'Sofia'), (1, 140.00, 'Phoenix', 'Roberto'),
    (1, 155.00, 'Phoenix', 'Marcelo'), (1, 88.00, 'Dallas', 'Sofia'),
    (1, 110.00, 'Dallas', 'Roberto'), (1, 220.00, 'Dallas', 'Marcelo'),
    (2, 380.00, 'Seattle', 'Online'), (2, 65.00, 'Los Angeles', 'Valentina'),
    (1, 95.00, 'Phoenix', 'Valentina'), (3, 35.00, 'Dallas', 'Valentina'),
    (1, 175.00, 'Phoenix', 'Sofia'), (1, 95.00, 'Austin', 'Roberto'),
    (2, 45.00, 'Austin', 'Marcelo'), (1, 50.00, 'Austin', 'Valentina'),
    (1, 230.00, 'Dallas', 'Online'), (1, 145.00, 'Phoenix', 'Online'),
    (2, 75.00, 'Seattle', 'Roberto');
GO

SELECT
    (SELECT COUNT(*) FROM practica.Venta)             AS Ventas,
    (SELECT COUNT(*) FROM practica.NotaFinal)         AS Notas,
    (SELECT COUNT(*) FROM practica.ResumenTrimestral) AS Resumenes,
    (SELECT COUNT(*) FROM practica.VentaCiudad)       AS VentasCiudad;
```

**Resultado esperado.**

| Ventas | Notas | Resumenes | VentasCiudad |
|---:|---:|---:|---:|
| 21 | 12 | 3 | 25 |

## Ejercicios

### Ejercicio 1 · Monto por vendedor y mes
<!-- ejercicio: U1.33 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Obtené el monto total vendido por cada vendedor en cada mes del primer semestre. Las columnas son los meses en orden cronológico. Si un vendedor no vendió en un mes, mostrá `NULL`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `PIVOT` estático con `SUM(Monto)`, `FOR Mes` y la lista de meses escrita en el orden pedido. La subconsulta deja solo `Vendedor`, `Mes` y `Monto`.

<!-- check: U1.33 -->
```sql
SELECT Vendedor, [Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio]
FROM (
    SELECT Vendedor, Mes, Monto
    FROM practica.Venta
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Mes IN ([Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio])
) AS Pv
ORDER BY Vendedor;
```

**Resultado esperado.**

| Vendedor | Enero | Febrero | Marzo | Abril | Mayo | Junio |
|---|---:|---:|---:|---:|---:|---:|
| Ana | 1800.00 | 2000.00 | 1800.00 | 2200.00 | 1600.00 | 2500.00 |
| Carlos | `NULL` | `NULL` | 500.00 | 700.00 | 600.00 | `NULL` |
| Luis | 900.00 | 1100.00 | 800.00 | `NULL` | 1200.00 | 1400.00 |
| Marta | 2100.00 | 1700.00 | 2300.00 | 1900.00 | 2100.00 | 2800.00 |

Ana tuvo dos ventas en enero (1500 + 300) y `SUM` las acumula. Carlos empezó en marzo y Luis no vendió en abril: esas celdas quedan en `NULL`.

</details>

### Ejercicio 2 · Reemplazar los `NULL` por cero
<!-- ejercicio: U1.34 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Repetí el ejercicio 1 mostrando 0 donde no hubo ventas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Mismo `PIVOT`, y en el `SELECT` externo `ISNULL(columna, 0)` con un alias por mes.

<!-- check: U1.34 -->
```sql
SELECT
    Vendedor,
    ISNULL([Enero],   0) AS Enero,
    ISNULL([Febrero], 0) AS Febrero,
    ISNULL([Marzo],   0) AS Marzo,
    ISNULL([Abril],   0) AS Abril,
    ISNULL([Mayo],    0) AS Mayo,
    ISNULL([Junio],   0) AS Junio
FROM (
    SELECT Vendedor, Mes, Monto
    FROM practica.Venta
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Mes IN ([Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio])
) AS Pv
ORDER BY Vendedor;
```

**Resultado esperado.**

| Vendedor | Enero | Febrero | Marzo | Abril | Mayo | Junio |
|---|---:|---:|---:|---:|---:|---:|
| Ana | 1800.00 | 2000.00 | 1800.00 | 2200.00 | 1600.00 | 2500.00 |
| Carlos | 0.00 | 0.00 | 500.00 | 700.00 | 600.00 | 0.00 |
| Luis | 900.00 | 1100.00 | 800.00 | 0.00 | 1200.00 | 1400.00 |
| Marta | 2100.00 | 1700.00 | 2300.00 | 1900.00 | 2100.00 | 2800.00 |

`ISNULL` se aplica sobre las columnas ya generadas por el `PIVOT`. Los alias son necesarios para que las columnas conserven el nombre del mes.

</details>

### Ejercicio 3 · Cantidad de ventas por vendedor y mes
<!-- ejercicio: U1.35 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
En lugar de sumar montos, contá cuántas ventas hizo cada vendedor por mes.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `COUNT(VentaId)` como agregado: el origen incluye `VentaId` en lugar de `Monto`.

<!-- check: U1.35 -->
```sql
SELECT Vendedor, [Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio]
FROM (
    SELECT Vendedor, Mes, VentaId
    FROM practica.Venta
) AS Origen
PIVOT (
    COUNT(VentaId)
    FOR Mes IN ([Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio])
) AS Pv
ORDER BY Vendedor;
```

**Resultado esperado.**

| Vendedor | Enero | Febrero | Marzo | Abril | Mayo | Junio |
|---|---:|---:|---:|---:|---:|---:|
| Ana | 2 | 1 | 1 | 1 | 1 | 1 |
| Carlos | 0 | 0 | 1 | 1 | 1 | 0 |
| Luis | 1 | 1 | 1 | 0 | 1 | 1 |
| Marta | 1 | 1 | 1 | 1 | 1 | 1 |

`COUNT` devuelve 0 cuando no hay filas, por eso no aparecen `NULL`. Ana tiene 2 ventas en enero.

</details>

### Ejercicio 4 · Notas por alumno y materia
<!-- ejercicio: U1.36 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Mostrá una fila por alumno y una columna por materia con la nota (promedio, si hubiera más de una). Las materias sin nota se muestran con 0, con un decimal.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `PIVOT` con `AVG(Nota)`, y en el `SELECT` externo `CAST(ISNULL(..., 0) AS DECIMAL(4,1))` para conservar un decimal (el promedio de un `DECIMAL(4,1)` tiene escala 6).

<!-- check: U1.36 -->
```sql
SELECT
    Alumno,
    CAST(ISNULL([Matemáticas], 0) AS DECIMAL(4,1)) AS Matematicas,
    CAST(ISNULL([Historia], 0) AS DECIMAL(4,1)) AS Historia,
    CAST(ISNULL([Inglés], 0) AS DECIMAL(4,1)) AS Ingles,
    CAST(ISNULL([Física], 0) AS DECIMAL(4,1)) AS Fisica
FROM (
    SELECT Alumno, Materia, Nota
    FROM practica.NotaFinal
) AS Origen
PIVOT (
    AVG(Nota)
    FOR Materia IN ([Matemáticas], [Historia], [Inglés], [Física])
) AS Pv
ORDER BY Alumno;
```

**Resultado esperado.**

| Alumno | Matematicas | Historia | Ingles | Fisica |
|---|---:|---:|---:|---:|
| Juan | 7.0 | 9.0 | 8.0 | 0.0 |
| Laura | 8.0 | 8.0 | 9.0 | 7.0 |
| María | 6.0 | 0.0 | 0.0 | 8.0 |
| Pedro | 0.0 | 10.0 | 7.0 | 9.0 |

Los encabezados del `PIVOT` son los valores de la columna `Materia` (con tilde: `[Matemáticas]`), y los alias del `SELECT` externo los renombran sin tildes. Un cero no es una nota: solo marca la ausencia de dato.

</details>

### Ejercicio 5 · PIVOT dinámico en orden cronológico
<!-- ejercicio: U1.37 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Repetí el ejercicio 1 armando la lista de meses a partir de los datos. Si mañana se cargan ventas de julio, la consulta tiene que incluirlas sin modificarse, y las columnas siguen en orden cronológico.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Armamos la lista con `STRING_AGG(QUOTENAME(Mes), ', ') WITHIN GROUP (ORDER BY Orden)` y ejecutamos con `sp_executesql`, todo en un único lote.

<!-- check: U1.37 -->
```sql
DECLARE @Columnas NVARCHAR(MAX);
DECLARE @Consulta NVARCHAR(MAX);

SELECT @Columnas = STRING_AGG(QUOTENAME(Mes), N', ') WITHIN GROUP (ORDER BY Orden)
FROM (
    SELECT
        Mes,
        CASE Mes
            WHEN 'Enero'   THEN 1
            WHEN 'Febrero' THEN 2
            WHEN 'Marzo'   THEN 3
            WHEN 'Abril'   THEN 4
            WHEN 'Mayo'    THEN 5
            WHEN 'Junio'   THEN 6
        END AS Orden
    FROM practica.Venta
    GROUP BY Mes
) AS Meses;

SET @Consulta = N'
SELECT Vendedor, ' + @Columnas + N'
FROM (
    SELECT Vendedor, Mes, Monto
    FROM practica.Venta
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Mes IN (' + @Columnas + N')
) AS Pv
ORDER BY Vendedor;';

EXEC sys.sp_executesql @Consulta;
```

**Resultado esperado.**

| Vendedor | Enero | Febrero | Marzo | Abril | Mayo | Junio |
|---|---:|---:|---:|---:|---:|---:|
| Ana | 1800.00 | 2000.00 | 1800.00 | 2200.00 | 1600.00 | 2500.00 |
| Carlos | `NULL` | `NULL` | 500.00 | 700.00 | 600.00 | `NULL` |
| Luis | 900.00 | 1100.00 | 800.00 | `NULL` | 1200.00 | 1400.00 |
| Marta | 2100.00 | 1700.00 | 2300.00 | 1900.00 | 2100.00 | 2800.00 |

**Dos correcciones frente a la versión anterior del ejercicio.** (1) Un `GO` entre armar `@Columnas` y armar `@Consulta` terminaba el lote y las variables dejaban de existir (error 137). (2) `ORDER BY` fuera del `STRING_AGG` es inválido: el orden dentro de la lista se pide con `WITHIN GROUP (ORDER BY ...)`. El orden cronológico viene de un `CASE` que asigna un número a cada mes, porque alfabéticamente `Abril` precede a `Enero`. Para meses nuevos hay que ampliar el `CASE`.

</details>

### Ejercicio 6 · UNPIVOT de un resumen trimestral
<!-- ejercicio: U1.38 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
`ResumenTrimestral` tiene una columna por trimestre. Pasala a formato vertical: una fila por departamento y trimestre.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `UNPIVOT (Monto FOR Trimestre IN (Q1, Q2, Q3, Q4))`.

<!-- check: U1.38 -->
```sql
SELECT Departamento, Trimestre, Monto
FROM practica.ResumenTrimestral
UNPIVOT (
    Monto FOR Trimestre IN (Q1, Q2, Q3, Q4)
) AS Un
ORDER BY Departamento, Trimestre;
```

**Resultado esperado.**

| Departamento | Trimestre | Monto |
|---|---|---:|
| IT | Q1 | 120.00 |
| IT | Q2 | 150.00 |
| IT | Q3 | 130.00 |
| IT | Q4 | 200.00 |
| RRHH | Q1 | 80.00 |
| RRHH | Q2 | 95.00 |
| RRHH | Q4 | 110.00 |
| Ventas | Q1 | 300.00 |
| Ventas | Q2 | 280.00 |
| Ventas | Q3 | 320.00 |
| Ventas | Q4 | 410.00 |

`UNPIVOT` descarta las filas con `NULL`: RRHH no tiene fila para Q3. Las columnas listadas tienen el mismo tipo (`DECIMAL(10,2)`), requisito del operador.

</details>

### Ejercicio 7 · Filtrar el resultado del PIVOT
<!-- ejercicio: U1.39 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con el `PIVOT` del ejercicio 1, mostrá solo a los vendedores cuyo total de marzo supera 1500, ordenados de mayor a menor por ese monto.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El `WHERE` y el `ORDER BY` se escriben después del `PIVOT`, sobre las columnas generadas (`[Marzo]`).

<!-- check: U1.39 -->
```sql
SELECT Vendedor, [Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio]
FROM (
    SELECT Vendedor, Mes, Monto
    FROM practica.Venta
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Mes IN ([Enero], [Febrero], [Marzo], [Abril], [Mayo], [Junio])
) AS Pv
WHERE [Marzo] > 1500
ORDER BY [Marzo] DESC;
```

**Resultado esperado.**

| Vendedor | Enero | Febrero | Marzo | Abril | Mayo | Junio |
|---|---:|---:|---:|---:|---:|---:|
| Marta | 2100.00 | 1700.00 | 2300.00 | 1900.00 | 2100.00 | 2800.00 |
| Ana | 1800.00 | 2000.00 | 1800.00 | 2200.00 | 1600.00 | 2500.00 |

Las columnas del `PIVOT` se usan como columnas comunes. Carlos (500) y Luis (800) quedan afuera; Marta (2300) precede a Ana (1800).

</details>

### Ejercicio 8 · Venta máxima por vendedor y ciudad
<!-- ejercicio: U1.40 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
A partir de `VentaCiudad` (cantidad, precio, ciudad, vendedor), mostrá por vendedor la venta de mayor monto en cada una de estas ciudades: Los Angeles, Seattle, Austin, Phoenix y Dallas. El monto de una venta es `Cantidad * Precio`. Hay que usar `PIVOT`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El monto se calcula en la subconsulta, porque `PIVOT` solo agrega una columna existente. El filtro de ciudades va en esa misma subconsulta. El agregado es `MAX`.

<!-- check: U1.40 -->
```sql
SELECT
    Vendedor,
    [Los Angeles], [Seattle], [Austin], [Phoenix], [Dallas]
FROM (
    SELECT
        Vendedor,
        Ciudad,
        Cantidad * Precio AS Monto
    FROM practica.VentaCiudad
    WHERE Ciudad IN ('Los Angeles', 'Seattle', 'Austin', 'Phoenix', 'Dallas')
) AS Origen
PIVOT (
    MAX(Monto)
    FOR Ciudad IN ([Los Angeles], [Seattle], [Austin], [Phoenix], [Dallas])
) AS Pv
ORDER BY Vendedor;
```

**Resultado esperado.**

| Vendedor | Los Angeles | Seattle | Austin | Phoenix | Dallas |
|---|---:|---:|---:|---:|---:|
| Marcelo | 512.00 | `NULL` | 90.00 | 155.00 | 220.00 |
| Online | 215.00 | 760.00 | `NULL` | 145.00 | 230.00 |
| Roberto | 275.00 | 150.00 | 95.00 | 140.00 | 110.00 |
| Sofia | `NULL` | 190.00 | 18.75 | 175.00 | 88.00 |
| Valentina | 130.00 | 22.50 | 50.00 | 95.00 | 105.00 |

Este ejercicio es la versión integradora de un enunciado inspirado en un parcial, con datos y ciudades propios. Por ejemplo, Online en Seattle tiene 2 × 380 = 760 y Marcelo en Austin 2 × 45 = 90. Las ciudades sin ventas de un vendedor quedan en `NULL`, y las que no están en la lista (San Diego, San Francisco) no aparecen como columnas.

</details>

### Ejercicio 9 · Despivotar conservando los `NULL`
<!-- ejercicio: U1.41 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Mostrá el resumen trimestral de RRHH en formato vertical **incluyendo** el trimestre sin dato (Q3).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `UNPIVOT` descartaría la fila; usamos `CROSS APPLY (VALUES ...)` para generar una fila por trimestre aunque el valor sea `NULL`.

<!-- check: U1.41 -->
```sql
SELECT
    r.Departamento,
    t.Trimestre,
    t.Monto
FROM practica.ResumenTrimestral AS r
CROSS APPLY (VALUES
    ('Q1', r.Q1),
    ('Q2', r.Q2),
    ('Q3', r.Q3),
    ('Q4', r.Q4)
) AS t (Trimestre, Monto)
WHERE r.Departamento = 'RRHH'
ORDER BY r.Departamento, t.Trimestre;
```

**Resultado esperado.**

| Departamento | Trimestre | Monto |
|---|---|---:|
| RRHH | Q1 | 80.00 |
| RRHH | Q2 | 95.00 |
| RRHH | Q3 | `NULL` |
| RRHH | Q4 | 110.00 |

`CROSS APPLY` con `VALUES` genera cuatro filas por cada departamento, con o sin dato. Es la alternativa cuando el `NULL` tiene significado.

</details>
