---
title: Laboratorio defensivo — Inyección SQL
slug: bbdd-aplicadas/unidad-5/practica/laboratorio-inyeccion
sidebar:
  order: 2
  badge:
    text: Complementario
    variant: note
---

[← Unidad 5](/bbdd-aplicadas/unidad-5/teoria/)

:::note[Contenido complementario]
La inyección SQL no forma parte del programa 2024; se conserva como práctica complementaria del mínimo privilegio. Presupone la lección [Inyección SQL y programación segura](/bbdd-aplicadas/unidad-5/teoria/inyeccion-sql/) y, para la parte 5, [Seguridad, usuarios y permisos](/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos/).
:::

El objetivo es observar, en una base aislada, cómo la concatenación modifica la consulta y cómo la parametrización conserva la entrada como dato.

:::caution[Entorno de laboratorio]
No pruebes entradas de este tipo contra sistemas ajenos o productivos. El laboratorio no requiere permisos de DDL para la cuenta simulada, no ejecuta borrados y la entrada de prueba solo altera un filtro. Todos los datos son sintéticos.
:::

Todo se ejecutó en SQL Server 2022 sobre Linux. Usá una **base vacía** de laboratorio (por ejemplo, la misma `LaboratorioU5` del [laboratorio de seguridad](/bbdd-aplicadas/unidad-5/practica/laboratorio-seguridad/)). Los scripts crean el esquema `seguridad`: si los repetís, eliminá antes los objetos o usá una base nueva.

## Preparación

<!-- check: U5.LI.01 -->
```sql
CREATE SCHEMA seguridad AUTHORIZATION dbo;
GO

CREATE TABLE seguridad.UsuarioDemo
(
    UsuarioId INT IDENTITY PRIMARY KEY,
    Nombre    NVARCHAR(100) NOT NULL UNIQUE,
    Rol       VARCHAR(20)   NOT NULL
);

INSERT seguridad.UsuarioDemo (Nombre, Rol)
VALUES (N'leia', 'usuario'),
       (N'luke', 'usuario'),
       (N'palpatine', 'admin');
GO
```

No se incluye una contraseña recuperable: la autenticación real requiere un *hashing* adecuado en la capa de identidad.

## Parte 1 — Concatenación vulnerable

<!-- check: U5.LI.01 -->
```sql
CREATE OR ALTER PROCEDURE seguridad.BuscarVulnerable
    @Nombre NVARCHAR(100)
AS
BEGIN
    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT UsuarioId, Nombre, Rol
          FROM seguridad.UsuarioDemo
          WHERE Nombre = ''' + @Nombre + N''';';

    SELECT @Sql AS SqlGenerado; -- observar antes de ejecutar
    EXEC (@Sql);
END;
GO
```

El procedimiento devuelve **dos conjuntos de resultados**: primero el texto SQL generado y después las filas de la consulta.

Prueba normal:

<!-- check: U5.LI.01 -->
```sql
EXEC seguridad.BuscarVulnerable @Nombre = N'leia';
```

El primer conjunto muestra `SELECT ... WHERE Nombre = 'leia';` (con los saltos de línea del texto) y el segundo:

| UsuarioId | Nombre | Rol |
|---|---|---|
| 1 | leia | usuario |

Prueba defensiva controlada, que altera solo el filtro:

<!-- check: U5.LI.01 -->
```sql
EXEC seguridad.BuscarVulnerable @Nombre = N''' OR 1=1--';
```

El SQL generado termina en `WHERE Nombre = '' OR 1=1--';` y la consulta devuelve **las tres filas**:

| UsuarioId | Nombre | Rol |
|---|---|---|
| 1 | leia | usuario |
| 2 | luke | usuario |
| 3 | palpatine | admin |

Analizá el `SqlGenerado` e identificá el cierre de comilla, la condición siempre verdadera y el comentario que anula el resto.

## Parte 2 — `sp_executesql` seguro

<!-- check: U5.LI.01 -->
```sql
CREATE OR ALTER PROCEDURE seguridad.BuscarSeguro
    @Nombre NVARCHAR(100)
AS
BEGIN
    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT UsuarioId, Nombre, Rol
          FROM seguridad.UsuarioDemo
          WHERE Nombre = @PNombre;';

    EXEC sys.sp_executesql
        @stmt = @Sql,
        @params = N'@PNombre NVARCHAR(100)',
        @PNombre = @Nombre;
END;
GO
```

Ejecutá las mismas dos entradas:

<!-- check: U5.LI.01 -->
```sql
EXEC seguridad.BuscarSeguro @Nombre = N'leia';
EXEC seguridad.BuscarSeguro @Nombre = N''' OR 1=1--';
```

La primera devuelve **una fila** (`leia`). La segunda devuelve **cero filas**: se busca literalmente un nombre que contiene comillas y operadores, y no existe.

## Parte 3 — Consulta estática

<!-- check: U5.LI.01 -->
```sql
CREATE OR ALTER PROCEDURE seguridad.BuscarEstatico
    @Nombre NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT UsuarioId, Nombre, Rol
    FROM seguridad.UsuarioDemo
    WHERE Nombre = @Nombre;
END;
GO

EXEC seguridad.BuscarEstatico @Nombre = N'luke';
```

Devuelve la fila `2 | luke | usuario`. Si no hay estructura dinámica, esta variante es la más simple.

## Parte 4 — Ordenamiento dinámico

Los nombres de columna no aceptan parámetros. Se implementa una lista permitida:

<!-- check: U5.LI.01 -->
```sql
CREATE OR ALTER PROCEDURE seguridad.ListarSeguro
    @Orden SYSNAME
AS
BEGIN
    IF @Orden NOT IN (N'Nombre', N'Rol')
        THROW 50010, 'Orden no permitido.', 1;

    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT UsuarioId, Nombre, Rol
          FROM seguridad.UsuarioDemo
          ORDER BY ' + QUOTENAME(@Orden) + N', UsuarioId;';

    EXEC sys.sp_executesql @Sql;
END;
GO
```

Probalo con `Nombre`, con `Rol` y con un valor no permitido:

<!-- check: U5.LI.01 -->
```sql
EXEC seguridad.ListarSeguro @Orden = N'Nombre';
EXEC seguridad.ListarSeguro @Orden = N'Rol';
EXEC seguridad.ListarSeguro @Orden = N'Clave';
```

| Orden | Filas (`UsuarioId`) |
|---|---|
| `Nombre` | 1 leia, 2 luke, 3 palpatine |
| `Rol` | 3 palpatine (`admin`), 1 leia, 2 luke |
| `Clave` | Error 50010, «Orden no permitido.» |

Explicá la función independiente de la lista permitida y de `QUOTENAME`.

## Parte 5 — Mínimo privilegio

La aplicación solo recibe permiso para **ejecutar** los procedimientos; no tiene `SELECT` sobre la tabla.

<!-- check: U5.LI.P5 -->
```sql
CREATE ROLE rol_consulta_usuario AUTHORIZATION dbo;
GRANT EXECUTE ON OBJECT::seguridad.BuscarEstatico TO rol_consulta_usuario;
GRANT EXECUTE ON OBJECT::seguridad.BuscarSeguro TO rol_consulta_usuario;

CREATE USER app_demo WITHOUT LOGIN;
ALTER ROLE rol_consulta_usuario ADD MEMBER app_demo;
GO
```

Probar como `app_demo`:

<!-- check: U5.LI.P5 -->
```sql
EXECUTE AS USER = 'app_demo';
EXEC seguridad.BuscarEstatico @Nombre = N'leia';
EXEC seguridad.BuscarSeguro @Nombre = N'leia';
SELECT * FROM seguridad.UsuarioDemo;
REVERT;
```

**Resultado esperado**

| Sentencia | Resultado | Por qué |
|---|---|---|
| `BuscarEstatico` | 1 fila | Procedimiento y tabla tienen el mismo propietario (`dbo`): el **encadenamiento de propiedad** omite la comprobación de `SELECT` |
| `BuscarSeguro` | Error 229 (permiso `SELECT` denegado) | `sp_executesql` ejecuta un lote dinámico **fuera** de la cadena de propiedad: se comprueban los permisos de `app_demo`, que no tiene `SELECT` |
| `SELECT` directo | Error 229 | `app_demo` no tiene permiso sobre la tabla |

La parametrización evita la inyección, pero no reemplaza la gestión de permisos: un procedimiento dinámico necesita un mecanismo explícito para acceder a la tabla sin darle `SELECT` al usuario.

### Firmar el procedimiento dinámico

La **firma de módulos** concede el permiso al procedimiento, no al usuario. Se crea un certificado, un
usuario asociado a ese certificado con `SELECT` sobre la tabla, y se firma el procedimiento:

<!-- check: U5.LI.P5 -->
```sql
CREATE CERTIFICATE CertBuscarSeguro
    ENCRYPTION BY PASSWORD = 'Laboratorio-Firma-2026!'
    WITH SUBJECT = 'Firma de seguridad.BuscarSeguro';
CREATE USER UsuarioCertBuscar FROM CERTIFICATE CertBuscarSeguro;
GRANT SELECT ON OBJECT::seguridad.UsuarioDemo TO UsuarioCertBuscar;

ADD SIGNATURE TO seguridad.BuscarSeguro
    BY CERTIFICATE CertBuscarSeguro WITH PASSWORD = 'Laboratorio-Firma-2026!';
GO
```

Al repetir la prueba, `BuscarSeguro` devuelve 1 fila y el `SELECT` directo sigue fallando con el error 229.

:::caution[Errores frecuentes]
- **Usar `DENY SELECT` "para demostrar" el mínimo privilegio.** Un `DENY` sobre el rol del usuario también bloquea el procedimiento firmado (sigue dando error 229). El mínimo privilegio se logra **no otorgando** el permiso, no denegándolo.
- **Modificar el procedimiento.** `ALTER PROCEDURE` elimina la firma: hay que volver a firmarlo.
- **La contraseña del certificado.** La del laboratorio es solo didáctica. En un entorno real se protege el certificado y se lo respalda.
:::

Esto muestra que la parametrización y el mínimo privilegio son capas complementarias.

## Parte 6 — Segundo orden

Se razona sin ejecutar SQL peligroso:

1. Una aplicación guarda un alias recibido externamente.
2. El `INSERT` está parametrizado y es seguro.
3. Un proceso posterior lee el alias y lo concatena en una consulta.
4. El punto vulnerable es ese proceso, porque transformó el dato almacenado en código.

La corrección es parametrizar en el momento de la ejecución. Se resuelve con datos en el [ejercicio 15](#ejercicio-15--segundo-orden).

## Cuestionario

<details>
<summary>1. ¿Por qué duplicar comillas manualmente es una defensa frágil?</summary>

Porque exige cubrir todos los contextos y codificaciones sin olvidar ninguno. Con parámetros, el dato nunca se interpreta como sintaxis.
</details>

<details>
<summary>2. ¿Un procedimiento almacenado impide la inyección automáticamente?</summary>

No. Si el procedimiento concatena sus parámetros en SQL dinámico, es vulnerable (`BuscarVulnerable`). Es seguro si usa consultas estáticas o parámetros.
</details>

<details>
<summary>3. ¿Qué parte puede parametrizarse y cuál necesita lista permitida?</summary>

Los valores se parametrizan; los nombres de columna o tabla y la dirección de orden usan lista permitida y `QUOTENAME`.
</details>

<details>
<summary>4. ¿Por qué una cuenta <code>db_owner</code> aumenta el impacto?</summary>

Porque una consulta alterada corre con los permisos de la cuenta y con `db_owner` puede leer y modificar toda la base.
</details>

<details>
<summary>5. ¿Qué cambia si el dato vulnerable proviene de una cookie o de otra tabla?</summary>

Nada en el mecanismo: toda fuente externa o almacenada es no confiable y se parametriza en el punto de ejecución.
</details>

<details>
<summary>6. ¿Qué eventos registrarías sin guardar el payload completo ni secretos?</summary>

Rechazos de la lista permitida, errores de sintaxis repetidos, intentos desde un mismo origen, y el procedimiento y el usuario involucrados, con la entrada truncada o sin datos personales.
</details>

## Ejercicios

### Ejercicio 13 · Leer el SQL generado
<!-- ejercicio: U5.13 | nivel: inicial | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
La tabla `catalogo.Producto (ProductoId, Nombre, Categoria, Publicado)` tiene cuatro productos; el último (`Prototipo`, categoría `pantallas`) **no está publicado**. El procedimiento `catalogo.ListarPorCategoria` arma el filtro `Publicado = 1 AND Categoria = '<entrada>'` por concatenación. (a) Escribí el SQL generado y las filas para la entrada `pantallas' OR Publicado = 0--`. (b) Corregí el procedimiento y mostrá que esa entrada ya no trae nada.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Reconstruir el texto final, aplicando la precedencia de `AND` sobre `OR`. Después, reemplazar la concatenación por un filtro estático con parámetro.

<!-- check: U5.13 -->
```sql
CREATE SCHEMA catalogo;
GO
CREATE TABLE catalogo.Producto
(
    ProductoId INT IDENTITY PRIMARY KEY,
    Nombre     NVARCHAR(60) NOT NULL,
    Categoria  VARCHAR(20)  NOT NULL,
    Publicado  BIT          NOT NULL
);
INSERT catalogo.Producto (Nombre, Categoria, Publicado)
VALUES (N'Teclado', 'perifericos', 1), (N'Mouse', 'perifericos', 1), (N'Monitor', 'pantallas', 1), (N'Prototipo', 'pantallas', 0);
GO
CREATE PROCEDURE catalogo.ListarPorCategoria @Categoria NVARCHAR(100)
AS
BEGIN
    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT ProductoId, Nombre FROM catalogo.Producto WHERE Publicado = 1 AND Categoria = ''' + @Categoria + N''';';
    SELECT @Sql AS SqlGenerado;
    EXEC (@Sql);
END;
GO
EXEC catalogo.ListarPorCategoria @Categoria = N'pantallas';
GO
EXEC catalogo.ListarPorCategoria @Categoria = N'pantallas'' OR Publicado = 0--';
GO
CREATE OR ALTER PROCEDURE catalogo.ListarPorCategoria @Categoria NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT ProductoId, Nombre
    FROM catalogo.Producto
    WHERE Publicado = 1 AND Categoria = @Categoria;
END;
GO
EXEC catalogo.ListarPorCategoria @Categoria = N'pantallas'' OR Publicado = 0--';
GO
EXEC catalogo.ListarPorCategoria @Categoria = N'pantallas';
```

**Resultado esperado.** La entrada normal devuelve `3 | Monitor`. Con la entrada alterada, el SQL generado es

```text
SELECT ProductoId, Nombre FROM catalogo.Producto WHERE Publicado = 1 AND Categoria = 'pantallas' OR Publicado = 0--';
```

| ProductoId | Nombre |
|---|---|
| 3 | Monitor |
| 4 | Prototipo |

(`AND` se evalúa primero; el `OR Publicado = 0` agrega los no publicados.) Con el procedimiento corregido, la misma entrada devuelve cero filas y la entrada normal vuelve a dar `3 | Monitor`.

El parámetro `@Categoria` es `NVARCHAR(100)`: con una longitud demasiado corta (por ejemplo 20) la entrada se **trunca** y el SQL queda con una comilla sin cerrar, es decir, un error de sintaxis en lugar de la alteración. Truncar no es una defensa.
</details>

### Ejercicio 14 · Orden y dirección permitidos
<!-- ejercicio: U5.14 | nivel: intermedio | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Escribí `catalogo.ListarOrdenado @Columna, @Direccion` sobre `catalogo.Producto (ProductoId, Nombre, Precio)`. Solo se admiten las columnas `Nombre` y `Precio` y las direcciones `ASC` y `DESC` (por defecto `ASC`). Cualquier otra entrada debe rechazarse con un error propio (50020 para la columna, 50021 para la dirección). Mostrá el orden por precio descendente, por nombre y el rechazo de una dirección alterada.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La dirección tampoco se parametriza: se valida contra una lista y se concatena solo un valor que ya está permitido. La columna, además, se delimita con `QUOTENAME`. Se agrega `ProductoId` como desempate para que el orden sea determinista.

<!-- check: U5.14 -->
```sql
CREATE SCHEMA catalogo;
GO
CREATE TABLE catalogo.Producto
(
    ProductoId INT IDENTITY PRIMARY KEY,
    Nombre     NVARCHAR(60)   NOT NULL,
    Precio     DECIMAL(10, 2) NOT NULL
);
INSERT catalogo.Producto (Nombre, Precio) VALUES (N'Teclado', 30), (N'Mouse', 12), (N'Monitor', 150);
GO
CREATE PROCEDURE catalogo.ListarOrdenado @Columna SYSNAME, @Direccion VARCHAR(4) = 'ASC'
AS
BEGIN
    IF @Columna NOT IN (N'Nombre', N'Precio')
        THROW 50020, 'Columna no permitida.', 1;
    IF @Direccion NOT IN ('ASC', 'DESC')
        THROW 50021, 'Direccion no permitida.', 1;

    DECLARE @Sql NVARCHAR(MAX) =
        N'SELECT ProductoId, Nombre, Precio FROM catalogo.Producto ORDER BY '
        + QUOTENAME(@Columna) + N' ' + @Direccion + N', ProductoId;';
    EXEC sys.sp_executesql @Sql;
END;
GO
EXEC catalogo.ListarOrdenado @Columna = N'Precio', @Direccion = 'DESC';
GO
EXEC catalogo.ListarOrdenado @Columna = N'Nombre';
GO
BEGIN TRY
    EXEC catalogo.ListarOrdenado @Columna = N'Precio', @Direccion = 'ASC, Nombre';
END TRY
BEGIN CATCH
    SELECT ERROR_NUMBER() AS Error, ERROR_MESSAGE() AS Mensaje;
END CATCH;
```

**Resultado esperado.**

| ProductoId | Nombre | Precio |
|---|---|---|
| 3 | Monitor | 150.00 |
| 1 | Teclado | 30.00 |
| 2 | Mouse | 12.00 |

| ProductoId | Nombre | Precio |
|---|---|---|
| 3 | Monitor | 150.00 |
| 2 | Mouse | 12.00 |
| 1 | Teclado | 30.00 |

| Error | Mensaje |
|---|---|
| 50021 | Direccion no permitida. |
</details>

### Ejercicio 15 · Segundo orden
<!-- ejercicio: U5.15 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
La aplicación registra alias con un `INSERT` parametrizado en `seguridad.Alias`. Un proceso posterior, `seguridad.ResumenAlias`, cuenta los mensajes **públicos** (`Privado = 0`) de cada alias recorriéndolos con un cursor y concatenando el alias en SQL dinámico. Se registran los alias `ana` y `' OR Privado = 1--` (un texto, para el laboratorio). Mostrá qué devuelve el proceso, explicá cuál de las dos operaciones es vulnerable y reescribilo sin SQL dinámico.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El alta es segura porque guarda el valor como dato. El proceso posterior vuelve a convertirlo en código al concatenarlo. La corrección no es "limpiar" el alias al guardarlo, sino no concatenar nunca: una sola consulta con `JOIN`.

<!-- check: U5.15 -->
```sql
CREATE SCHEMA seguridad;
GO
CREATE TABLE seguridad.Alias
(
    AliasId INT IDENTITY PRIMARY KEY,
    Texto   NVARCHAR(100) NOT NULL
);
CREATE TABLE seguridad.Mensaje
(
    MensajeId INT IDENTITY PRIMARY KEY,
    Autor     NVARCHAR(100) NOT NULL,
    Privado   BIT NOT NULL
);
INSERT seguridad.Mensaje (Autor, Privado)
VALUES (N'ana', 0), (N'ana', 1), (N'beto', 0), (N'beto', 1);
GO
-- El alta es segura: parámetros.
CREATE PROCEDURE seguridad.RegistrarAlias @Texto NVARCHAR(100)
AS
BEGIN
    INSERT seguridad.Alias (Texto) VALUES (@Texto);
END;
GO
EXEC seguridad.RegistrarAlias @Texto = N'ana';
EXEC seguridad.RegistrarAlias @Texto = N''' OR Privado = 1--';
GO
-- El proceso posterior concatena el valor guardado.
CREATE PROCEDURE seguridad.ResumenAlias
AS
BEGIN
    DECLARE @Texto NVARCHAR(100), @Sql NVARCHAR(MAX);
    DECLARE Alias CURSOR LOCAL FAST_FORWARD FOR SELECT Texto FROM seguridad.Alias ORDER BY AliasId;
    OPEN Alias;
    FETCH NEXT FROM Alias INTO @Texto;
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @Sql = N'SELECT COUNT(*) AS Mensajes FROM seguridad.Mensaje WHERE Privado = 0 AND Autor = ''' + @Texto + N''';';
        EXEC (@Sql);
        FETCH NEXT FROM Alias INTO @Texto;
    END;
    CLOSE Alias;
    DEALLOCATE Alias;
END;
GO
EXEC seguridad.ResumenAlias;
GO
-- Corrección: el proceso posterior no concatena nada.
CREATE OR ALTER PROCEDURE seguridad.ResumenAlias
AS
BEGIN
    SET NOCOUNT ON;
    SELECT a.Texto AS Alias, COUNT(m.MensajeId) AS Mensajes
    FROM seguridad.Alias AS a
    LEFT JOIN seguridad.Mensaje AS m ON m.Autor = a.Texto AND m.Privado = 0
    GROUP BY a.AliasId, a.Texto
    ORDER BY a.AliasId;
END;
GO
EXEC seguridad.ResumenAlias;
```

**Resultado esperado.** El proceso vulnerable devuelve un conjunto por alias: `1` para `ana`, y **`2`** para el segundo alias, que contó los mensajes privados (el SQL generado fue `... Privado = 0 AND Autor = '' OR Privado = 1--'`). La versión corregida:

| Alias | Mensajes |
|---|---|
| ana | 1 |
| ' OR Privado = 1-- | 0 |

La operación vulnerable es el proceso posterior, no el alta. El dato era inofensivo mientras estuvo almacenado como dato; el daño aparece cuando otro código lo concatena. Por eso se parametriza (o se evita el SQL dinámico) **en cada punto de ejecución**.
</details>
