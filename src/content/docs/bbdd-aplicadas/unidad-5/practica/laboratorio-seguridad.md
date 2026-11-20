---
title: Laboratorio — Seguridad, roles y permisos
slug: bbdd-aplicadas/unidad-5/practica/laboratorio-seguridad
sidebar:
  order: 1
---

[← Unidad 5](/bbdd-aplicadas/unidad-5/teoria/)

Presupone la lección [Seguridad, usuarios y permisos](/bbdd-aplicadas/unidad-5/teoria/seguridad-permisos/). El objetivo es **comprobar los permisos efectivos**, no limitarse a ejecutar `GRANT`: cada paso trae su resultado esperado.

:::caution[Entorno de laboratorio]
Ejecutá esto únicamente en una instancia de laboratorio: crear logins requiere privilegios de servidor. Las contraseñas de ejemplo son didácticas y no deben reutilizarse. Todo se ejecutó en SQL Server 2022 sobre Linux; para repetirlo, usá una base nueva y, al terminar, la limpieza del final.
:::

Este laboratorio y el de [inyección](/bbdd-aplicadas/unidad-5/practica/laboratorio-inyeccion/) y el de [backup](/bbdd-aplicadas/unidad-5/practica/laboratorio-backup/) comparten la base `LaboratorioU5`. Si ya la creaste, reutilizala eliminando antes los objetos y los esquemas `ventas` y `operaciones`, o empezá con una base nueva.

## Escenario

Una empresa necesita:

- vendedores que consulten clientes visibles y registren pedidos mediante un procedimiento;
- auditores que consulten pedidos pero no los modifiquen, y que **no lean** clientes;
- supervisores que administren los datos del esquema `ventas`;
- ninguna cuenta funcional con `db_owner`.

## Preparación

La base se crea una sola vez. Es una [base de práctica](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos): necesitás el permiso `CREATE DATABASE` o, si no lo tenés, pedí una base y usala con `USE`. Este bloque puntual no se probó en un motor; el resto del laboratorio sí se ejecutó sobre esa base.

<!-- check: U5.LS.R1 -->
```sql
CREATE DATABASE LaboratorioU5;
GO
USE LaboratorioU5;
GO
```

Esquemas, tablas y datos sintéticos:

<!-- check: U5.LS.01 -->
```sql
CREATE SCHEMA ventas AUTHORIZATION dbo;
GO
CREATE SCHEMA operaciones AUTHORIZATION dbo;
GO

CREATE TABLE ventas.Cliente
(
    ClienteId    INT IDENTITY PRIMARY KEY,
    Nombre       NVARCHAR(100)  NOT NULL,
    Email        VARCHAR(256)   NULL,
    LimiteCuenta DECIMAL(18, 2) NOT NULL,
    Pais         CHAR(3)        NOT NULL,
    Activo       BIT            NOT NULL DEFAULT 1
);

CREATE TABLE ventas.Pedido
(
    PedidoId  INT IDENTITY PRIMARY KEY,
    ClienteId INT NOT NULL REFERENCES ventas.Cliente (ClienteId),
    Fecha     DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    Importe   DECIMAL(18, 2) NOT NULL CHECK (Importe > 0),
    Estado    VARCHAR(20) NOT NULL DEFAULT 'NUEVO'
);

INSERT ventas.Cliente (Nombre, Email, LimiteCuenta, Pais)
VALUES (N'Cliente 01', 'cliente01@ejemplo.test', 10000, 'ARG'),
       (N'Cliente 02', 'cliente02@ejemplo.test', 8000, 'ARG'),
       (N'Cliente 03', 'cliente03@ejemplo.test', 6000, 'USA');

INSERT ventas.Pedido (ClienteId, Importe) VALUES (1, 500), (2, 750);
GO
```

## Parte 1 — Login y usuario

<!-- check: U5.LS.01 -->
```sql
CREATE LOGIN login_vendedor_u5 WITH PASSWORD = 'Cambiar_Vendedor_U5_2026!', CHECK_POLICY = ON;
CREATE LOGIN login_auditor_u5 WITH PASSWORD = 'Cambiar_Auditor_U5_2026!', CHECK_POLICY = ON;
CREATE LOGIN login_supervisor_u5 WITH PASSWORD = 'Cambiar_Supervisor_U5_2026!', CHECK_POLICY = ON;
GO

CREATE USER usr_vendedor FOR LOGIN login_vendedor_u5 WITH DEFAULT_SCHEMA = ventas;
CREATE USER usr_auditor FOR LOGIN login_auditor_u5;
CREATE USER usr_supervisor FOR LOGIN login_supervisor_u5;
CREATE USER usr_practicante WITHOUT LOGIN;   -- se usa en la parte 7
GO
```

Preguntas:

1. ¿Puede alguno ejecutar `SELECT * FROM ventas.Cliente` inmediatamente?
2. ¿Qué creó `DEFAULT_SCHEMA` y qué permiso otorgó?
3. ¿En qué catálogos aparecen los logins y los usuarios?

<!-- check: U5.LS.01 -->
```sql
SELECT name, type_desc
FROM sys.server_principals
WHERE name IN ('login_vendedor_u5', 'login_auditor_u5', 'login_supervisor_u5')
ORDER BY name;

SELECT name, type_desc, default_schema_name
FROM sys.database_principals
WHERE name IN ('usr_vendedor', 'usr_auditor', 'usr_supervisor', 'usr_practicante')
ORDER BY name;
```

**Resultado esperado.**

| name | type_desc |
|---|---|
| login_auditor_u5 | SQL_LOGIN |
| login_supervisor_u5 | SQL_LOGIN |
| login_vendedor_u5 | SQL_LOGIN |

| name | type_desc | default_schema_name |
|---|---|---|
| usr_auditor | SQL_USER | dbo |
| usr_practicante | SQL_USER | dbo |
| usr_supervisor | SQL_USER | dbo |
| usr_vendedor | SQL_USER | ventas |

<details>
<summary>Respuestas</summary>

1. **No.** Ni el auditor ni el vendedor pueden leer `ventas.Cliente`: error 229 (permiso `SELECT` denegado). El login solo da acceso al servidor y el usuario no tiene permisos todavía.
2. `DEFAULT_SCHEMA` **no crea nada ni otorga permisos**: solo indica contra qué esquema se resuelven los nombres sin calificar. El esquema `ventas` ya existía.
3. Los logins están en `sys.server_principals`; los usuarios, en `sys.database_principals` de cada base. (Los nombres se filtran con `IN` y no con `LIKE`, porque en `LIKE` el guion bajo es un comodín.)
</details>

## Parte 2 — Roles funcionales

<!-- check: U5.LS.01 -->
```sql
CREATE ROLE rol_vendedores AUTHORIZATION dbo;
CREATE ROLE rol_auditores AUTHORIZATION dbo;
CREATE ROLE rol_supervisores AUTHORIZATION dbo;

ALTER ROLE rol_vendedores ADD MEMBER usr_vendedor;
ALTER ROLE rol_auditores ADD MEMBER usr_auditor;
ALTER ROLE rol_supervisores ADD MEMBER usr_supervisor;

GRANT SELECT ON OBJECT::ventas.Pedido TO rol_auditores;
GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::ventas TO rol_supervisores;
GO
```

Comprobá desde el auditor:

<!-- check: U5.LS.01 -->
```sql
EXECUTE AS USER = 'usr_auditor';
SELECT * FROM ventas.Pedido;        -- permitido
SELECT * FROM ventas.Cliente;       -- debería fallar
DELETE ventas.Pedido;               -- debería fallar
SELECT entity_name, permission_name
FROM fn_my_permissions('ventas.Pedido', 'OBJECT')
WHERE subentity_name = '';
REVERT;
```

**Resultado esperado.**

| Usuario | Sentencia | Resultado |
|---|---|---|
| `usr_auditor` | `SELECT` sobre `ventas.Pedido` | Permitido (2 filas) |
| `usr_auditor` | `SELECT` sobre `ventas.Cliente` | Error 229 |
| `usr_auditor` | `DELETE` sobre `ventas.Pedido` | Error 229 |
| `usr_supervisor` | `SELECT` sobre `ventas.Cliente` | Permitido (3 filas) |
| `usr_supervisor` | `DELETE` sobre `ventas.Pedido` | Permitido |

`fn_my_permissions` devuelve una fila `ventas.Pedido | SELECT`. Cuando una sentencia falla dentro de `EXECUTE AS`, ejecutá `REVERT;` igualmente para volver al contexto original.

## Parte 3 — Vista que oculta datos

<!-- check: U5.LS.01 -->
```sql
CREATE OR ALTER VIEW ventas.ClientesVisibles
AS
SELECT ClienteId, Nombre, Email, Pais
FROM ventas.Cliente
WHERE Activo = 1 AND Pais <> 'USA';
GO

GRANT SELECT ON OBJECT::ventas.ClientesVisibles TO rol_vendedores;
GO
```

<!-- check: U5.LS.01 -->
```sql
EXECUTE AS USER = 'usr_vendedor';
SELECT * FROM ventas.ClientesVisibles;  -- permitido
SELECT * FROM ventas.Cliente;           -- no permitido
REVERT;
```

**Resultado esperado.** La vista devuelve 2 filas (`Cliente 01` y `Cliente 02`); el `SELECT` directo da el error 229.

Explicá:

- qué columnas y filas quedan ocultas (`LimiteCuenta`, `Activo` y el cliente de `USA`);
- por qué funciona el encadenamiento de propiedad (vista y tabla pertenecen a `dbo`);
- por qué esto no equivale a cifrar `LimiteCuenta`: quien tenga permiso sobre la tabla la lee en claro.

## Parte 4 — Procedimiento como interfaz

<!-- check: U5.LS.01 -->
```sql
CREATE OR ALTER PROCEDURE operaciones.RegistrarPedido
    @ClienteId INT,
    @Importe   DECIMAL(18, 2)
AS
BEGIN
    SET NOCOUNT ON;

    IF @Importe <= 0
        THROW 50001, 'El importe debe ser positivo.', 1;

    INSERT ventas.Pedido (ClienteId, Importe)
    VALUES (@ClienteId, @Importe);

    SELECT SCOPE_IDENTITY() AS PedidoId;
END;
GO

GRANT EXECUTE ON OBJECT::operaciones.RegistrarPedido TO rol_vendedores;
GO
```

<!-- check: U5.LS.01 -->
```sql
EXECUTE AS USER = 'usr_vendedor';
EXEC operaciones.RegistrarPedido @ClienteId = 1, @Importe = 1250;                   -- permitido
INSERT ventas.Pedido (ClienteId, Importe) VALUES (1, 999);                          -- debería fallar
EXEC operaciones.RegistrarPedido @ClienteId = 1, @Importe = -5;                     -- error del procedimiento
REVERT;
```

**Resultado esperado.**

| Sentencia | Resultado |
|---|---|
| `EXEC operaciones.RegistrarPedido ... 1250` | Permitido; devuelve el nuevo `PedidoId` (3) |
| `INSERT` directo | Error 229 |
| `EXEC ... @Importe = -5` | Error 50001 «El importe debe ser positivo.» |

## Parte 5 — `REVOKE` y `DENY`

Se otorga el mismo acceso por dos rutas (rol y esquema) para ver qué hace cada sentencia. **Al final se revierte todo**: si quedara un `SELECT` de esquema para el auditor, terminaría leyendo `ventas.Cliente`, algo que el escenario no le permite.

<!-- check: U5.LS.01 -->
```sql
GRANT SELECT ON OBJECT::ventas.Cliente TO rol_auditores;
GRANT SELECT ON SCHEMA::ventas TO usr_auditor;

REVOKE SELECT ON OBJECT::ventas.Cliente FROM rol_auditores;   -- (a)
DENY SELECT ON OBJECT::ventas.Cliente TO usr_auditor;         -- (b)
REVOKE SELECT ON OBJECT::ventas.Cliente FROM usr_auditor;     -- (c) quita el DENY
REVOKE SELECT ON SCHEMA::ventas FROM usr_auditor;             -- (d) revierte el permiso de esquema
```

Después de cada paso, probá `SELECT * FROM ventas.Cliente` como `usr_auditor`:

| Después de | ¿Lee `ventas.Cliente`? | Por qué |
|---|---|---|
| (a) | SI | El `REVOKE` quitó el permiso del rol, pero el `GRANT` de esquema sigue dando acceso |
| (b) | NO | El `DENY` explícito sobre la tabla gana |
| (c) | SI | `REVOKE` eliminó el `DENY`; no concedió nada, vuelve a valer el permiso de esquema |
| (d) | **NO** | Se revirtió el permiso de esquema: el auditor vuelve al estado del escenario |

Tras (d), `usr_auditor` sigue leyendo `ventas.Pedido` (2 filas) por `rol_auditores`.

## Parte 6 — Auditoría

Tres consultas para revisar el estado:

<!-- check: U5.LS.01 -->
```sql
-- 1. Membresías de los roles funcionales
SELECT rol.name AS Rol, miembro.name AS Miembro
FROM sys.database_role_members AS drm
JOIN sys.database_principals AS rol ON rol.principal_id = drm.role_principal_id
JOIN sys.database_principals AS miembro ON miembro.principal_id = drm.member_principal_id
WHERE rol.name LIKE 'rol[_]%'
ORDER BY rol.name, miembro.name;

-- 2. Permisos de los roles, en las tres clases (base, esquema, objeto)
SELECT p.state_desc, p.permission_name, p.class_desc,
       USER_NAME(p.grantee_principal_id) AS principal,
       CASE p.class_desc
         WHEN 'DATABASE' THEN DB_NAME()
         WHEN 'SCHEMA' THEN SCHEMA_NAME(p.major_id)
         WHEN 'OBJECT_OR_COLUMN'
           THEN QUOTENAME(OBJECT_SCHEMA_NAME(p.major_id)) + '.' + QUOTENAME(OBJECT_NAME(p.major_id))
       END AS securable
FROM sys.database_permissions AS p
WHERE USER_NAME(p.grantee_principal_id) LIKE 'rol[_]%'
ORDER BY principal, p.class_desc, securable, p.permission_name;

-- 3. Propietarios de los esquemas
SELECT s.name AS esquema, USER_NAME(s.principal_id) AS propietario
FROM sys.schemas AS s
WHERE s.name IN ('ventas', 'operaciones')
ORDER BY s.name;
```

**Resultado esperado.**

| Rol | Miembro |
|---|---|
| rol_auditores | usr_auditor |
| rol_supervisores | usr_supervisor |
| rol_vendedores | usr_vendedor |

| state_desc | permission_name | class_desc | principal | securable |
|---|---|---|---|---|
| GRANT | SELECT | OBJECT_OR_COLUMN | rol_auditores | [ventas].[Pedido] |
| GRANT | DELETE | SCHEMA | rol_supervisores | ventas |
| GRANT | INSERT | SCHEMA | rol_supervisores | ventas |
| GRANT | SELECT | SCHEMA | rol_supervisores | ventas |
| GRANT | UPDATE | SCHEMA | rol_supervisores | ventas |
| GRANT | EXECUTE | OBJECT_OR_COLUMN | rol_vendedores | [operaciones].[RegistrarPedido] |
| GRANT | SELECT | OBJECT_OR_COLUMN | rol_vendedores | [ventas].[ClientesVisibles] |

| esquema | propietario |
|---|---|
| operaciones | dbo |
| ventas | dbo |

Se usa `LIKE 'rol[_]%'` con el guion bajo entre corchetes para que sea literal. Para la comprobación puntual, `HAS_PERMS_BY_NAME('ventas.Cliente', 'OBJECT', 'SELECT')` bajo `EXECUTE AS` da el permiso efectivo de cada usuario.

Por qué consultar solo `sys.database_permissions` no entrega siempre el permiso efectivo completo: no incluye lo que se hereda por membresía de roles (incluidos los anidados), por la jerarquía (base y esquema), por la propiedad (el propietario no necesita permisos), ni por la pertenencia a roles de servidor como `sysadmin`.

## Parte 7 — Delegación controlada

El supervisor recibe `SELECT` con `GRANT OPTION` y lo delega en el practicante (`usr_practicante`, creado en la parte 1):

<!-- check: U5.LS.01 -->
```sql
GRANT SELECT ON OBJECT::ventas.Pedido TO usr_supervisor WITH GRANT OPTION;

-- Como usr_supervisor:
--   GRANT SELECT ON OBJECT::ventas.Pedido TO usr_practicante;

REVOKE SELECT ON OBJECT::ventas.Pedido FROM usr_supervisor;            -- error 4611
REVOKE SELECT ON OBJECT::ventas.Pedido FROM usr_supervisor CASCADE;    -- revoca también al practicante
```

**Resultado esperado.**

| Paso | Resultado |
|---|---|
| El supervisor delega en el practicante | Permitido; el practicante lee `ventas.Pedido` (2 filas) |
| `REVOKE` sin `CASCADE` | Error 4611: el permiso fue delegado |
| `REVOKE ... CASCADE` | Se revoca al supervisor y al practicante |
| El practicante lee `ventas.Pedido` | Error 229 |

Antes de usar `CASCADE`, documentá a quién se le revoca.

## Limpieza

Los logins son objetos de servidor: hay que eliminarlos explícitamente. Para borrar la base (desde otra base, por ejemplo `master`), `DROP DATABASE LaboratorioU5;`.

<!-- check: U5.LS.01 -->
```sql
DROP LOGIN login_vendedor_u5;
DROP LOGIN login_auditor_u5;
DROP LOGIN login_supervisor_u5;
```

## Desafíos

1. Creá `rol_operador_backup` y decidí si usar un rol fijo (`db_backupoperator`) o permisos granulares.
2. Construí la matriz de acceso final del escenario y demostrá cada celda con una prueba.
3. Investigá cómo firmar un procedimiento que necesita permisos adicionales sin otorgárselos a quien lo llama (la [parte 5 del laboratorio de inyección](/bbdd-aplicadas/unidad-5/practica/laboratorio-inyeccion/#parte-5--mínimo-privilegio) lo resuelve).

## Ejercicios

### Ejercicio 1 · Clasificar cuentas y asignar privilegios
<!-- ejercicio: U5.01 | nivel: inicial | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Una clínica tiene un sistema con la base `Turnos`. Hay cinco cuentas: (1) la aplicación de recepción, que registra turnos; (2) el equipo de reportes, que arma estadísticas sin ver datos personales; (3) el DBA; (4) una auditora externa que revisa quién modificó qué; (5) un desarrollador que mantiene el esquema en el ambiente de pruebas. Clasificá cada cuenta y proponé el acceso mínimo. Indicá una cuenta que **no** deba tener `db_owner` y por qué.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Aplicar el principio del mínimo privilegio: para cada cuenta, la operación estrictamente necesaria, a través de un rol, y el objeto más específico posible.

| Cuenta | Clase | Acceso mínimo |
|---|---|---|
| Aplicación de recepción | Aplicación | `EXECUTE` sobre procedimientos como `RegistrarTurno`; sin permisos directos sobre las tablas |
| Equipo de reportes | Usuarios finales | `SELECT` sobre vistas que excluyen los datos personales (o permisos de columna) |
| DBA | Administrador | Rol de servidor o `db_owner` con cuenta nominal; separado de las cuentas de aplicación |
| Auditora externa | Auditor | Solo lectura sobre el registro de cambios y sobre los datos que audita; sin `INSERT`/`UPDATE`/`DELETE` |
| Desarrollador | Desarrollador | Permisos de definición (DDL) únicamente en la base de **pruebas**, no en producción |

La aplicación de recepción no debe ser `db_owner`: una inyección SQL o una credencial filtrada daría control total sobre la base. Con `EXECUTE` sobre procedimientos, el daño posible se limita a lo que esos procedimientos hacen.
</details>

### Ejercicio 2 · Predecir qué contraseñas acepta el motor
<!-- ejercicio: U5.02 | nivel: inicial | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Para cada intento, predecí si `CREATE LOGIN` funciona y, si falla, qué regla se incumple.

1. `'Primavera'` con `CHECK_POLICY = ON`.
2. `'Pri2026'` con `CHECK_POLICY = ON`.
3. `'Primavera2026'` con `CHECK_POLICY = ON`.
4. `'primavera_2026'` con `CHECK_POLICY = ON`.
5. `'Primavera'` con `CHECK_POLICY = OFF`.
6. `'Primavera2026' MUST_CHANGE` con `CHECK_POLICY = ON` y sin `CHECK_EXPIRATION`.

Luego verificalo y mostrá las banderas de política que quedaron en los logins creados.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Aplicar las reglas: 8 caracteres como mínimo y tres de cuatro categorías (mayúsculas, minúsculas, dígitos, símbolos); `MUST_CHANGE` exige `CHECK_EXPIRATION = ON`.

<!-- check: U5.02 -->
```sql
CREATE LOGIN LoginU502A WITH PASSWORD = 'Primavera', CHECK_POLICY = ON;
CREATE LOGIN LoginU502B WITH PASSWORD = 'Pri2026', CHECK_POLICY = ON;
CREATE LOGIN LoginU502C WITH PASSWORD = 'Primavera2026', CHECK_POLICY = ON;
CREATE LOGIN LoginU502D WITH PASSWORD = 'primavera_2026', CHECK_POLICY = ON;
CREATE LOGIN LoginU502E WITH PASSWORD = 'Primavera', CHECK_POLICY = OFF;
CREATE LOGIN LoginU502F WITH PASSWORD = 'Primavera2026' MUST_CHANGE, CHECK_POLICY = ON;

SELECT name, is_policy_checked AS Politica, is_expiration_checked AS Vencimiento
FROM sys.sql_logins
WHERE name LIKE 'LoginU502%'
ORDER BY name;
```

**Resultado esperado.**

| Intento | Resultado | Regla |
|---|---|---|
| 1 | Error 33064 | Tiene 9 caracteres, pero solo 2 categorías de 4 (mayúsculas y minúsculas) |
| 2 | Error 33062 | Tiene 7 caracteres: menos del mínimo de 8 |
| 3 | Creado | Mayúscula, minúscula y dígitos: 3 de 4 |
| 4 | Creado | Minúsculas, dígitos y símbolo: 3 de 4 |
| 5 | Creado | Sin `CHECK_POLICY` no se valida |
| 6 | Error 15099 | `MUST_CHANGE` exige `CHECK_EXPIRATION = ON` |

| name | Politica | Vencimiento |
|---|---|---|
| LoginU502C | 1 | 0 |
| LoginU502D | 1 | 0 |
| LoginU502E | 0 | 0 |

El intento 1 no tiene dígitos ni símbolos, por eso cuenta solo 2 categorías. Al terminar, eliminá los logins de práctica con `DROP LOGIN` si ya no los necesitás.
</details>

### Ejercicio 3 · Verdadero o falso sobre DCL, roles y propietarios
<!-- ejercicio: U5.03 | nivel: inicial | tipo: verdadero-falso | verificacion: razonamiento -->

:::note[Enunciado]
Decidí y justificá:

1. `REVOKE SELECT` sobre un usuario impide que lea una tabla si pertenece a un rol que tiene `GRANT SELECT`.
2. Un `DENY` heredado de un rol anula un `GRANT` directo al usuario.
3. Un `GRANT SELECT ON SCHEMA::ventas` alcanza también a las tablas que se creen después en ese esquema.
4. Se puede eliminar un usuario que es propietario de un esquema sin reasignarlo antes.
5. Un login con `DEFAULT_DATABASE = Ventas` puede leer tablas de `Ventas`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para cada punto, recordar qué sentencia actúa sobre qué fila de permiso y desde qué ruta llega el acceso.

1. **Falso.** `REVOKE` solo quita el permiso de ese principal; el `GRANT` del rol sigue vigente (paso 3 y 4 de la tabla de precedencia de la lección). Para impedirlo hay que usar `DENY`.
2. **Verdadero.** `DENY` gana sobre cualquier `GRANT`, aunque venga de otra ruta (se ve en el paso 3: el `GRANT` directo no levantó el `DENY` del rol).
3. **Verdadero.** El permiso de esquema incluye los objetos presentes y futuros (lo indica la cátedra y se muestra en la lección).
4. **Falso.** El motor responde el error 15138; primero hay que reasignar el esquema con `ALTER AUTHORIZATION`.
5. **Falso.** `DEFAULT_DATABASE` solo indica adónde se conecta; hace falta un usuario en la base y permisos.
</details>

### Ejercicio 4 · Permisos de columna
<!-- ejercicio: U5.04 | nivel: intermedio | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
`ventas.Cliente (ClienteId, Nombre, Email, LimiteCuenta)`. El usuario `usr_soporte` debe ver `ClienteId`, `Nombre` y `Email`, pero **no** `LimiteCuenta`. (a) Otorgá el permiso con granularidad de columna. (b) Probá cinco consultas (`SELECT` de las tres columnas, `SELECT *`, solo `LimiteCuenta`, `COUNT(*)` y filtrar por `LimiteCuenta`). (c) Denegá `Email` y mostrá qué sigue pudiendo leer. (d) Listá sus permisos de columna con `fn_my_permissions`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `GRANT SELECT (columnas) ON OBJECT::...` y `DENY SELECT (columna)`. Un permiso de columna no cubre `*` ni las columnas que se usan en un filtro.

<!-- check: U5.04 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Cliente
(
    ClienteId    INT IDENTITY PRIMARY KEY,
    Nombre       NVARCHAR(100)  NOT NULL,
    Email        VARCHAR(256)   NULL,
    LimiteCuenta DECIMAL(18, 2) NOT NULL
);
INSERT ventas.Cliente (Nombre, Email, LimiteCuenta)
VALUES (N'Cliente 01', 'cliente01@ejemplo.test', 10000), (N'Cliente 02', 'cliente02@ejemplo.test', 8000);
CREATE USER usr_soporte WITHOUT LOGIN;
GO
GRANT SELECT (ClienteId, Nombre, Email) ON OBJECT::ventas.Cliente TO usr_soporte;
GO
-- (b) Como usr_soporte: SELECT ClienteId, Nombre, Email ...; SELECT * ...; SELECT LimiteCuenta ...;
--     SELECT COUNT(*) ...; SELECT Nombre ... WHERE LimiteCuenta > 9000.
DENY SELECT (Email) ON OBJECT::ventas.Cliente TO usr_soporte;
GO
EXECUTE AS USER = 'usr_soporte';
SELECT subentity_name AS Columna, permission_name
FROM fn_my_permissions('ventas.Cliente', 'OBJECT')
WHERE subentity_name <> ''
ORDER BY subentity_name;
REVERT;
```

**Resultado esperado.**

| Consulta como `usr_soporte` | Resultado |
|---|---|
| `SELECT ClienteId, Nombre, Email` | Permitido (2 filas) |
| `SELECT *` | Error 230 (permiso denegado sobre la columna `LimiteCuenta`) |
| `SELECT LimiteCuenta` | Error 230 |
| `SELECT COUNT(*)` | Error 230 |
| `Nombre ... WHERE LimiteCuenta > 9000` | Error 230: filtrar también lee la columna |
| `SELECT Email` (tras el `DENY`) | Error 230 |
| `SELECT Nombre` (tras el `DENY`) | Permitido (2 filas) |

| Columna | permission_name |
|---|---|
| ClienteId | SELECT |
| Nombre | SELECT |

Con permisos de columna, hay que listar las columnas explícitamente. Que `COUNT(*)` falle es un caso límite para tener presente: sin `SELECT` de tabla completa, el motor no permite esa forma.
</details>

### Ejercicio 5 · Examen: secuencia de GRANT, DENY y REVOKE
<!-- ejercicio: U5.05 | nivel: intermedio | tipo: conceptual | verificacion: motor -->

:::note[Enunciado]
Un rol `rol_comercial` tiene como miembros a `usr_ana` y `usr_beto`. `usr_carla` no pertenece a ningún rol. Las tablas son `ventas.Cliente`, `ventas.Pedido` y `compras.Proveedor`. Se ejecuta, en este orden:

1. `GRANT SELECT ON SCHEMA::ventas TO rol_comercial;`
2. `GRANT INSERT ON OBJECT::ventas.Pedido TO rol_comercial;`
3. `DENY SELECT ON OBJECT::ventas.Cliente TO usr_beto;`
4. `GRANT SELECT ON OBJECT::compras.Proveedor TO rol_comercial;`
5. `DENY SELECT ON OBJECT::compras.Proveedor TO usr_ana;`
6. `GRANT UPDATE ON OBJECT::ventas.Pedido TO usr_beto;`
7. `REVOKE SELECT ON SCHEMA::ventas FROM rol_comercial;`
8. `GRANT SELECT ON OBJECT::ventas.Pedido TO usr_ana;`

Completá con SI o NO si cada usuario puede ejecutar cada consulta **al terminar la secuencia**: (1) `SELECT` de `ventas.Cliente`; (2) `SELECT` de `ventas.Pedido`; (3) `INSERT` en `ventas.Pedido`; (4) `UPDATE ventas.Pedido SET Estado = 'ENVIADO'`; (5) `SELECT` de `compras.Proveedor`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para cada usuario, juntar sus permisos directos y los de su rol, y aplicar: un `DENY` gana sobre cualquier `GRANT`; `REVOKE` solo quita la fila del principal indicado. Después se comprobó cada celda ejecutando la consulta con `EXECUTE AS USER` en SQL Server; podés repetir la comprobación del mismo modo.

<!-- check: U5.05 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE SCHEMA compras;
GO
CREATE TABLE ventas.Cliente (ClienteId INT PRIMARY KEY, Nombre VARCHAR(50) NOT NULL);
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, ClienteId INT NOT NULL, Estado VARCHAR(20) NOT NULL);
CREATE TABLE compras.Proveedor (ProveedorId INT PRIMARY KEY, Nombre VARCHAR(50) NOT NULL);
INSERT ventas.Cliente VALUES (1, 'cliente01');
INSERT ventas.Pedido VALUES (1, 1, 'NUEVO');
INSERT compras.Proveedor VALUES (1, 'proveedor01');
CREATE ROLE rol_comercial;
CREATE USER usr_ana WITHOUT LOGIN;
CREATE USER usr_beto WITHOUT LOGIN;
CREATE USER usr_carla WITHOUT LOGIN;
ALTER ROLE rol_comercial ADD MEMBER usr_ana;
ALTER ROLE rol_comercial ADD MEMBER usr_beto;
GO
GRANT SELECT ON SCHEMA::ventas TO rol_comercial;
GRANT INSERT ON OBJECT::ventas.Pedido TO rol_comercial;
DENY SELECT ON OBJECT::ventas.Cliente TO usr_beto;
GRANT SELECT ON OBJECT::compras.Proveedor TO rol_comercial;
DENY SELECT ON OBJECT::compras.Proveedor TO usr_ana;
GRANT UPDATE ON OBJECT::ventas.Pedido TO usr_beto;
REVOKE SELECT ON SCHEMA::ventas FROM rol_comercial;
GRANT SELECT ON OBJECT::ventas.Pedido TO usr_ana;
GO
-- Cada consulta se ejecutó como cada usuario, por ejemplo:
EXECUTE AS USER = 'usr_ana';
SELECT HAS_PERMS_BY_NAME('ventas.Pedido', 'OBJECT', 'SELECT') AS PuedeLeerPedido;
REVERT;
```

**Resultado esperado.**

| Consulta | `usr_ana` | `usr_beto` | `usr_carla` |
|---|:---:|:---:|:---:|
| 1. `SELECT` de `ventas.Cliente` | NO | NO | NO |
| 2. `SELECT` de `ventas.Pedido` | SI | NO | NO |
| 3. `INSERT` en `ventas.Pedido` | SI | SI | NO |
| 4. `UPDATE` de `ventas.Pedido` | NO | SI | NO |
| 5. `SELECT` de `compras.Proveedor` | NO | SI | NO |

Razonamiento:

- **Consulta 1.** El paso 7 quitó el `SELECT` de esquema del rol y nadie más lo tiene: todos en NO (el `DENY` de Beto ya no cambia nada).
- **Consulta 2.** Ana tiene `SELECT` directo (paso 8); Beto solo lo tenía por el rol y se revocó.
- **Consulta 3.** El `INSERT` viene del rol (paso 2) y no se revocó: Ana y Beto. Carla no pertenece al rol.
- **Consulta 4.** El `UPDATE` es un permiso directo de Beto (paso 6).
- **Consulta 5.** Beto lo hereda del rol; Ana tiene un `DENY` directo (paso 5), que gana sobre el `GRANT` del rol.
</details>

### Ejercicio 6 · Diagnóstico de permisos efectivos
<!-- ejercicio: U5.06 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
`usr_dario` pertenece a `rol_ventas`, `rol_reportes` y `rol_externos`, y además tiene un permiso directo. Nadie recuerda qué se otorgó. Escribí una consulta que liste, para ese usuario, **desde qué principal (él o cada rol)** llega cada permiso sobre `ventas.Pedido` y sobre el esquema `ventas`, e indicá si puede hacer `SELECT`, `INSERT` y `UPDATE`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Unir el usuario con las membresías de roles y con `sys.database_permissions` de él y de sus roles. `DISTINCT` evita duplicar la fila directa por cada rol. Después se prueban las operaciones con `EXECUTE AS`.

<!-- check: U5.06 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, Importe DECIMAL(10, 2) NOT NULL);
INSERT ventas.Pedido VALUES (1, 100.00);
CREATE ROLE rol_ventas;
CREATE ROLE rol_reportes;
CREATE ROLE rol_externos;
CREATE USER usr_dario WITHOUT LOGIN;
ALTER ROLE rol_ventas ADD MEMBER usr_dario;
ALTER ROLE rol_reportes ADD MEMBER usr_dario;
ALTER ROLE rol_externos ADD MEMBER usr_dario;
GRANT SELECT, INSERT ON OBJECT::ventas.Pedido TO rol_ventas;
GRANT SELECT ON SCHEMA::ventas TO rol_reportes;
DENY INSERT ON OBJECT::ventas.Pedido TO rol_externos;
GRANT UPDATE ON OBJECT::ventas.Pedido TO usr_dario;
GO
SELECT DISTINCT via.name AS Via, p.state_desc AS Estado, p.permission_name AS Permiso, p.class_desc AS Ambito,
       CASE p.class_desc
         WHEN 'SCHEMA' THEN SCHEMA_NAME(p.major_id)
         ELSE QUOTENAME(OBJECT_SCHEMA_NAME(p.major_id)) + '.' + QUOTENAME(OBJECT_NAME(p.major_id))
       END AS Securable
FROM sys.database_principals AS u
LEFT JOIN sys.database_role_members AS rm ON rm.member_principal_id = u.principal_id
JOIN sys.database_principals AS via ON via.principal_id IN (u.principal_id, rm.role_principal_id)
JOIN sys.database_permissions AS p ON p.grantee_principal_id = via.principal_id
WHERE u.name = 'usr_dario' AND p.class_desc IN ('SCHEMA', 'OBJECT_OR_COLUMN')
ORDER BY via.name, p.permission_name;
```

**Resultado esperado.**

| Via | Estado | Permiso | Ambito | Securable |
|---|---|---|---|---|
| rol_externos | DENY | INSERT | OBJECT_OR_COLUMN | [ventas].[Pedido] |
| rol_reportes | GRANT | SELECT | SCHEMA | ventas |
| rol_ventas | GRANT | INSERT | OBJECT_OR_COLUMN | [ventas].[Pedido] |
| rol_ventas | GRANT | SELECT | OBJECT_OR_COLUMN | [ventas].[Pedido] |
| usr_dario | GRANT | UPDATE | OBJECT_OR_COLUMN | [ventas].[Pedido] |

Probadas como `usr_dario`: `SELECT` permitido (llega por `rol_ventas` y por `rol_reportes`), `INSERT` **denegado** con el error 229 (el `DENY` de `rol_externos` gana sobre el `GRANT` de `rol_ventas`) y `UPDATE` permitido (permiso directo). La consulta no resuelve por sí sola la precedencia: muestra los orígenes y se aplica la regla de que `DENY` gana.
</details>

### Ejercicio 7 · Delegación en dos niveles
<!-- ejercicio: U5.07 | nivel: avanzado | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
`usr_gerente` recibe `SELECT` sobre `ventas.Pedido` con `GRANT OPTION`. Delega con `GRANT OPTION` en `usr_jefe`, y este delega (sin `GRANT OPTION`) en `usr_analista`. (a) Verificá que `usr_analista` lee la tabla. (b) Quitá a `usr_gerente` **la capacidad de delegar**, pero no su acceso. Mostrá qué pasa si falta `CASCADE` y quién conserva acceso al final.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `REVOKE GRANT OPTION FOR ... CASCADE` retira la facultad de delegar y arrastra lo delegado a partir de ella, sin tocar el `SELECT` propio de quien la tenía. Sin `CASCADE`, el motor rechaza la sentencia (4611).

<!-- check: U5.07 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE TABLE ventas.Pedido (PedidoId INT PRIMARY KEY, Importe DECIMAL(10, 2) NOT NULL);
INSERT ventas.Pedido VALUES (1, 100.00);
CREATE USER usr_gerente WITHOUT LOGIN;
CREATE USER usr_jefe WITHOUT LOGIN;
CREATE USER usr_analista WITHOUT LOGIN;
GO
GRANT SELECT ON OBJECT::ventas.Pedido TO usr_gerente WITH GRANT OPTION;
-- Como usr_gerente: GRANT SELECT ON OBJECT::ventas.Pedido TO usr_jefe WITH GRANT OPTION;
-- Como usr_jefe:    GRANT SELECT ON OBJECT::ventas.Pedido TO usr_analista;

REVOKE GRANT OPTION FOR SELECT ON OBJECT::ventas.Pedido FROM usr_gerente;           -- error 4611
REVOKE GRANT OPTION FOR SELECT ON OBJECT::ventas.Pedido FROM usr_gerente CASCADE;
```

**Resultado esperado.**

| Paso | Resultado |
|---|---|
| Gerente delega en jefe; jefe delega en analista | Permitido |
| `usr_analista` lee `ventas.Pedido` | SI (1 fila) |
| `REVOKE GRANT OPTION FOR` sin `CASCADE` | Error 4611 |
| `REVOKE GRANT OPTION FOR ... CASCADE` | Correcto |
| `usr_gerente` lee `ventas.Pedido` | SI (conserva el `SELECT`) |
| `usr_jefe` lee `ventas.Pedido` | NO (error 229) |
| `usr_analista` lee `ventas.Pedido` | NO (error 229) |

El `CASCADE` recorre la cadena: el jefe recibió el permiso gracias a la facultad del gerente, y el analista gracias a la del jefe; ambos pierden el acceso. Solo el gerente lo conserva, sin poder delegar.
</details>

### Ejercicio 8 · Una vista que deja de funcionar
<!-- ejercicio: U5.08 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
`usr_ana` tiene `SELECT` sobre la vista `ventas.CajaResumen` (propietario `dbo`), que resume `tesoreria.Caja`. El esquema `tesoreria` pertenece a `usr_tesoreria`. Ana recibe el error 229. (a) Diagnosticá la causa con una consulta de catálogo. (b) Corregí **sin** darle `SELECT` sobre `tesoreria.Caja`. (c) Verificá que Ana sigue sin leer la tabla directamente.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Comparar los propietarios de los esquemas de la vista y de la tabla: si difieren, se rompe el encadenamiento de propiedad y se evalúan los permisos de Ana sobre la tabla. Se unifica el propietario con `ALTER AUTHORIZATION` (otra opción es firmar un procedimiento).

<!-- check: U5.08 -->
```sql
CREATE USER usr_ana WITHOUT LOGIN;
CREATE USER usr_tesoreria WITHOUT LOGIN;
GO
CREATE SCHEMA ventas AUTHORIZATION dbo;
GO
CREATE SCHEMA tesoreria AUTHORIZATION usr_tesoreria;
GO
CREATE TABLE tesoreria.Caja (CajaId INT PRIMARY KEY, Saldo DECIMAL(12, 2) NOT NULL);
INSERT tesoreria.Caja VALUES (1, 1000.00), (2, 2500.00);
GO
CREATE VIEW ventas.CajaResumen AS SELECT COUNT(*) AS Cajas, SUM(Saldo) AS Total FROM tesoreria.Caja;
GO
GRANT SELECT ON OBJECT::ventas.CajaResumen TO usr_ana;
GO
-- (a) Diagnóstico
SELECT s.name AS Esquema, USER_NAME(s.principal_id) AS Propietario
FROM sys.schemas AS s
WHERE s.name IN ('ventas', 'tesoreria')
ORDER BY s.name;

-- (b) Corrección
ALTER AUTHORIZATION ON SCHEMA::tesoreria TO dbo;

-- (c) Como usr_ana: SELECT * FROM ventas.CajaResumen   y   SELECT * FROM tesoreria.Caja
```

**Resultado esperado.** El diagnóstico muestra propietarios distintos:

| Esquema | Propietario |
|---|---|
| tesoreria | usr_tesoreria |
| ventas | dbo |

Como `usr_ana`: antes de la corrección, la vista da el error 229 (cadena rota); después de `ALTER AUTHORIZATION`, la vista devuelve una fila (`2 | 3500.00`), y el `SELECT` directo sobre `tesoreria.Caja` sigue fallando con el error 229.

La corrección conviene si el cambio de propietario es coherente con el diseño. Si `usr_tesoreria` debe seguir siendo el propietario, la alternativa es exponer los datos con un procedimiento firmado con certificado.
</details>

## Autoevaluación

<details>
<summary>1. ¿Por qué la parte 5 termina con un <code>REVOKE</code> de esquema?</summary>

Porque el `GRANT SELECT ON SCHEMA` al auditor era solo para demostrar la diferencia entre `REVOKE` y `DENY`. Si no se revierte, el auditor termina leyendo `ventas.Cliente`, que el escenario le prohíbe.
</details>

<details>
<summary>2. ¿Por qué la vista de la parte 3 funciona aunque el vendedor no tenga <code>SELECT</code> sobre la tabla?</summary>

Por el encadenamiento de propiedad: la vista y la tabla son de `dbo`, así que basta el permiso sobre la vista.
</details>

:::tip[En resumen]
- Probá siempre el permiso efectivo con `EXECUTE AS` y `HAS_PERMS_BY_NAME`, no solo el `GRANT` que escribiste.
- `REVOKE` no equivale a `DENY`; revertí lo que otorgaste solo para demostrar.
- Los roles, los esquemas, las vistas y los procedimientos permiten dar acceso sin tocar las tablas.
- Los logins son objetos de servidor: se eliminan al terminar.
:::

## Fuentes

- Presentación de cátedra, Unidad 5, "Permisos, usuarios y roles" (UNLaM, DIIT).
- Microsoft Learn, [Introducción a los permisos del motor de base de datos](https://learn.microsoft.com/es-es/sql/relational-databases/security/authentication-access/getting-started-with-database-engine-permissions), [GRANT](https://learn.microsoft.com/es-es/sql/t-sql/statements/grant-transact-sql), [DENY](https://learn.microsoft.com/es-es/sql/t-sql/statements/deny-transact-sql), [REVOKE](https://learn.microsoft.com/es-es/sql/t-sql/statements/revoke-transact-sql), [Encadenamiento de propiedad](https://learn.microsoft.com/es-es/sql/relational-databases/security/ownership-chains).
