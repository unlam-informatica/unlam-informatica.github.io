---
title: SQL Dinámico
slug: bbdd-aplicadas/unidad-1/teoria/sql-dinamico
sidebar:
  order: 6
---

El **SQL dinámico** arma una sentencia como cadena de texto y la ejecuta en tiempo de ejecución. Se usa cuando no se conoce de antemano un nombre de columna o de tabla, o la lista de valores de un [PIVOT](/bbdd-aplicadas/unidad-1/teoria/pivot/). Es potente y peligroso: una cadena armada con datos externos es una puerta para la inyección.

Los ejemplos usan el esquema `ventas` de la página de [window functions](/bbdd-aplicadas/unidad-1/teoria/window-functions/#esquema-de-ejemplo).

## `EXEC` frente a `sp_executesql`

| | `EXEC (@cadena)` | `sp_executesql` |
|---|---|---|
| Parámetros tipados | No: todo se concatena | Sí, con `OUTPUT` |
| Valores de datos | Dentro del texto (riesgo de inyección) | Viajan como parámetros |
| Plan de ejecución | Se cachea por texto exacto: cada valor distinto es otro texto | Un único texto parametrizado reutiliza el plan |
| Cadena | `VARCHAR` o `NVARCHAR` | Debe ser `NVARCHAR` |

La diferencia no es que `EXEC` "no cachee": también cachea planes ad hoc, pero solo si el texto coincide letra por letra. La ventaja de `sp_executesql` es la parametrización.

<!-- check: U1.T.SD.01 -->
```sql
DECLARE @Region VARCHAR(10) = 'Sur';
DECLARE @Sentencia NVARCHAR(MAX);

-- EXEC: la cadena se arma por concatenación
SET @Sentencia = N'SELECT Nombre, Sueldo FROM ventas.Vendedor WHERE Region = ''' + @Region + N''' ORDER BY VendedorId';
SELECT @Sentencia AS Cadena;
EXEC (@Sentencia);

-- sp_executesql: el valor viaja como parámetro tipado
SET @Sentencia = N'SELECT Nombre, Sueldo FROM ventas.Vendedor WHERE Region = @Region ORDER BY VendedorId';
EXEC sys.sp_executesql @Sentencia, N'@Region VARCHAR(10)', @Region = @Region;
```

Ambas variantes devuelven lo mismo, pero la primera arma un texto distinto por cada región:

| Cadena |
|---|
| SELECT Nombre, Sueldo FROM ventas.Vendedor WHERE Region = 'Sur' ORDER BY VendedorId |

| Nombre | Sueldo |
|---|---:|
| Dario | 4100.00 |
| Eva | 2800.00 |
| Fede | 3500.00 |
| Gina | 2800.00 |

(La tabla se imprime dos veces: una por cada ejecución.)

## Ámbito: el código dinámico no ve tus variables

El texto se ejecuta en un ámbito propio. Las variables del llamador no existen ahí: hay que pasarlas como parámetros de `sp_executesql`.

<!-- check: U1.T.SD.06 -->
```sql
DECLARE @Region VARCHAR(10) = 'Sur';

-- El código dinámico se ejecuta en su propio ámbito: no ve las variables de quien lo llama
BEGIN TRY
    EXEC (N'SELECT COUNT(*) FROM ventas.Vendedor WHERE Region = @Region');
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Numero, ERROR_MESSAGE() AS Mensaje;
END CATCH;
```

| Numero | Mensaje |
|---:|---|
| 137 | Must declare the scalar variable "@Region". |

## `OUTPUT`

<!-- check: U1.T.SD.04 -->
```sql
DECLARE @Region   VARCHAR(10) = 'Sur';
DECLARE @Cantidad INT;
DECLARE @Sentencia NVARCHAR(MAX) = N'SELECT @Cantidad = COUNT(*) FROM ventas.Vendedor WHERE Region = @Region';

EXEC sys.sp_executesql
    @Sentencia,
    N'@Region VARCHAR(10), @Cantidad INT OUTPUT',
    @Region   = @Region,
    @Cantidad = @Cantidad OUTPUT;

SELECT @Cantidad AS VendedoresSur;
```

| VendedoresSur |
|---:|
| 4 |

## Inyección SQL

Concatenar una entrada del usuario convierte los datos en código. Con la entrada `' OR '1'='1`, el filtro por nombre devuelve **todos** los vendedores. Con `sp_executesql` la misma entrada es un dato y no coincide con ningún nombre.

<!-- check: U1.T.SD.02 -->
```sql
DECLARE @Entrada   VARCHAR(50) = ''' OR ''1''=''1';
DECLARE @Sentencia NVARCHAR(MAX);

-- Vulnerable: la entrada se convierte en código
SET @Sentencia = N'SELECT Nombre FROM ventas.Vendedor WHERE Nombre = ''' + @Entrada + N'''';
SELECT @Sentencia AS Cadena;
EXEC (@Sentencia);

-- Seguro: la entrada viaja como dato
SET @Sentencia = N'SELECT Nombre FROM ventas.Vendedor WHERE Nombre = @Nombre';
EXEC sys.sp_executesql @Sentencia, N'@Nombre VARCHAR(50)', @Nombre = @Entrada;
```

| Cadena construida |
|---|
| SELECT Nombre FROM ventas.Vendedor WHERE Nombre = '' OR '1'='1' |

La versión vulnerable devuelve los 7 nombres (Ana, Beto, Cora, Dario, Eva, Fede, Gina); la parametrizada, ninguna fila. El laboratorio completo, con la corrección, está en [inyección SQL](/bbdd-aplicadas/unidad-5/practica/laboratorio-inyeccion/).

## `QUOTENAME`: nombres de objetos

Un nombre de tabla o columna **no se puede parametrizar**. Se lo valida y se lo protege con `QUOTENAME`, que lo envuelve entre corchetes y duplica los `]` internos. Así, un nombre hostil se convierte en un identificador inexistente, no en código.

<!-- check: U1.T.SD.03 -->
```sql
DECLARE @Columna  SYSNAME = N'Sueldo';
DECLARE @Hostil   SYSNAME = N'Sueldo; DROP TABLE ventas.Venta; --';
DECLARE @Sentencia NVARCHAR(MAX);

SELECT QUOTENAME(@Columna) AS Normal, QUOTENAME(@Hostil) AS Hostil;

-- Uso correcto: ordenar por una columna elegida en tiempo de ejecución
SET @Sentencia = N'SELECT TOP (3) Nombre, Sueldo FROM ventas.Vendedor ORDER BY ' + QUOTENAME(@Columna) + N' DESC, VendedorId';
EXEC sys.sp_executesql @Sentencia;

-- El nombre hostil queda como un identificador inexistente: error, no ejecución
BEGIN TRY
    SET @Sentencia = N'SELECT Nombre FROM ventas.Vendedor ORDER BY ' + QUOTENAME(@Hostil);
    EXEC sys.sp_executesql @Sentencia;
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Numero, ERROR_MESSAGE() AS Mensaje;
END CATCH;

SELECT COUNT(*) AS VentasIntactas FROM ventas.Venta;
```

| Normal | Hostil |
|---|---|
| [Sueldo] | [Sueldo; DROP TABLE ventas.Venta; --] |

El `ORDER BY` correcto devuelve:

| Nombre | Sueldo |
|---|---:|
| Ana | 5000.00 |
| Dario | 4100.00 |
| Fede | 3500.00 |

Y el hostil falla sin ejecutar nada: error 207 (`Invalid column name 'Sueldo; DROP TABLE ventas.Venta; --'`) y las 16 ventas siguen en su lugar.

Regla: valores de datos, parámetros de `sp_executesql`; nombres de objetos, `QUOTENAME` (y, mejor, una lista blanca contra el catálogo).

## Ejemplo: PIVOT dinámico, sin `GO`

Los meses se leen de los datos y se arman como columnas.

:::caution[El `GO` rompe el PIVOT dinámico]
`GO` no es una sentencia de T-SQL: es un separador de lotes de las herramientas (`sqlcmd`, SSMS). Si se pone entre el `SELECT @Columnas = ...` y el `SET @Consulta = ...`, las variables dejan de existir y el segundo lote falla con el error 137 (`Must declare the scalar variable "@Columnas"`). Todo el armado y el `EXEC sp_executesql` tienen que estar en un único lote.
:::

<!-- check: U1.T.SD.05 -->
```sql
DECLARE @Columnas NVARCHAR(MAX);
DECLARE @Consulta NVARCHAR(MAX);

-- Sin GO entre los pasos: @Columnas y @Consulta viven en un único lote
SELECT @Columnas = STRING_AGG(QUOTENAME(Mes), N', ') WITHIN GROUP (ORDER BY Mes)
FROM (SELECT DISTINCT CONVERT(CHAR(7), Fecha, 126) AS Mes FROM ventas.Venta) AS Meses;

SET @Consulta = N'
SELECT VendedorId, ' + @Columnas + N'
FROM (
    SELECT VendedorId, CONVERT(CHAR(7), Fecha, 126) AS Mes, Monto
    FROM ventas.Venta
) AS Origen
PIVOT (
    SUM(Monto)
    FOR Mes IN (' + @Columnas + N')
) AS Pv
ORDER BY VendedorId;';

EXEC sys.sp_executesql @Consulta;
```

| VendedorId | 2025-01 | 2025-02 | 2025-03 | 2025-04 |
|---:|---:|---:|---:|---:|
| 2 | 700.00 | 150.00 | `NULL` | 1200.00 |
| 3 | 500.00 | 1200.00 | 200.00 | `NULL` |
| 4 | `NULL` | `NULL` | `NULL` | 500.00 |
| 5 | 200.00 | 500.00 | 1200.00 | `NULL` |
| 6 | `NULL` | 1200.00 | 500.00 | 150.00 |
| 7 | `NULL` | 200.00 | 500.00 | `NULL` |

## Ejemplo: filas por tabla de un esquema

Se arma un `UNION ALL` con una subconsulta por cada tabla del catálogo.

<!-- check: U1.T.SD.07 -->
```sql
DECLARE @Consulta NVARCHAR(MAX);

SELECT @Consulta = STRING_AGG(
        CAST(N'SELECT ' + QUOTENAME(t.name, '''') + N' AS Tabla, COUNT(*) AS Filas FROM '
             + QUOTENAME(s.name) + N'.' + QUOTENAME(t.name) AS NVARCHAR(MAX)),
        N' UNION ALL ')
FROM sys.tables AS t
INNER JOIN sys.schemas AS s
    ON s.schema_id = t.schema_id
WHERE s.name = N'ventas';

SET @Consulta = N'SELECT Tabla, Filas FROM (' + @Consulta + N') AS Conteo ORDER BY Tabla;';
EXEC sys.sp_executesql @Consulta;
```

| Tabla | Filas |
|---|---:|
| Vendedor | 7 |
| Venta | 16 |

## Depuración y permisos

- Mostrar la cadena antes de ejecutarla: `PRINT` muestra hasta 4000 caracteres si es `NVARCHAR` y 8000 si es `VARCHAR`; para cadenas más largas, `SELECT @Consulta`.
- Permisos: el código dinámico se ejecuta con los permisos de quien lo llama, y el encadenamiento de propietarios no se aplica al texto dinámico. Quien ejecuta un procedimiento que usa SQL dinámico necesita permisos sobre los objetos que toca. Ver [documentación de Microsoft](https://learn.microsoft.com/es-es/sql/relational-databases/security/ownership-and-user-schema-separation).

## Autoevaluación

<details>
<summary>1. ¿Por qué `sp_executesql` evita la inyección de valores?</summary>

Porque el valor se pasa como parámetro tipado y nunca se interpreta como parte del texto de la consulta.
</details>

<details>
<summary>2. ¿Por qué falla un PIVOT dinámico con `GO` entre sus pasos?</summary>

`GO` termina el lote y las variables locales se destruyen; el segundo lote no las ve (error 137).
</details>

<details>
<summary>3. ¿Cómo se protege un nombre de columna recibido por parámetro?</summary>

Con `QUOTENAME` y, de preferencia, validándolo contra el catálogo.
</details>

:::tip[En resumen]
- Dinámico = cadena + ejecución; usar `sp_executesql` con parámetros para los valores.
- Nombres de objetos: `QUOTENAME` y lista blanca.
- El código dinámico no ve las variables del llamador y todo el armado va en un único lote, sin `GO`.
:::

:::tip[Para seguir]
Resolvé el ejercicio 5 de la [Práctica — PIVOT](/bbdd-aplicadas/unidad-1/practica/pivot/) (PIVOT dinámico).
:::

## Fuentes

- Presentación de cátedra, Unidad 1, SQL dinámico (2024).
- Microsoft Learn, [sp_executesql](https://learn.microsoft.com/es-es/sql/relational-databases/system-stored-procedures/sp-executesql-transact-sql) y [QUOTENAME](https://learn.microsoft.com/es-es/sql/t-sql/functions/quotename-transact-sql).
