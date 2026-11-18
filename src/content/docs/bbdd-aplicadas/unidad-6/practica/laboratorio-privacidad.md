---
title: Laboratorio — Inventario, minimización y derechos
slug: bbdd-aplicadas/unidad-6/practica/laboratorio-privacidad
sidebar:
  order: 2
---

[← Unidad 6](/bbdd-aplicadas/unidad-6/teoria/)

Laboratorio defensivo sobre un caso ficticio: clasificar datos personales, minimizarlos, protegerlos con seudonimización y enmascaramiento, aplicar una política de retención y atender un derecho de acceso. Las normas se citan con su artículo desde las páginas de la unidad: [Ley 25.326](/bbdd-aplicadas/unidad-6/teoria/ley-25326/), [GDPR (RGPD)](/bbdd-aplicadas/unidad-6/teoria/gdpr/) e [ISO/IEC 25012](/bbdd-aplicadas/unidad-6/teoria/iso-25012/).

:::note[Contenido complementario]
Los controles técnicos (seudonimización con sal, enmascaramiento dinámico, retención y consulta de acceso) y los plazos de retención son elaboración propia para practicar. Ni la Ley 25.326 ni el RGPD prescriben estas técnicas ni estos plazos: exigen resultados (seguridad, minimización, limitación del plazo de conservación). Material académico: no sustituye asesoramiento jurídico.
:::

## Escenario

`SaludEnCasa` es una empresa ficticia que ofrece turnos médicos en Argentina y hace campañas dirigidas a usuarios en España. Hoy guarda en una sola tabla: nombre, DNI, contraseña sin hash, diagnóstico, religión, tarjeta, dirección IP, consentimiento, médico y fecha. Un proveedor de analítica recibe una copia semanal sin plazo de vencimiento.

No uses datos personales reales ni cargues secretos en el repositorio: todos los datos de este laboratorio son sintéticos.

## Qué necesitás saber

- Categorías de datos y principios: [Ley 25.326](/bbdd-aplicadas/unidad-6/teoria/ley-25326/) (arts. 2, 4, 5, 7, 9 y 14 a 16) y [RGPD](/bbdd-aplicadas/unidad-6/teoria/gdpr/) (arts. 3, 4, 5, 9, 12 a 17, 25 y 32).
- [Gobierno, privacidad y calidad desde el diseño](/bbdd-aplicadas/unidad-6/teoria/gobierno-privacidad/) (complementario).
- T-SQL: `HASHBYTES`, `EXECUTE AS`, permisos y `CROSS APPLY`.

## Preparación

Ejecutá el script en una base de laboratorio vacía. Es el modelo mínimo ya separado en entidades; los nombres, DNI y correos son ficticios, y las fechas de corte son fijas para que los resultados se reproduzcan.

<!-- check: U6.P.02 -->
```sql
CREATE SCHEMA privacidad;
GO

CREATE TABLE privacidad.Paciente (
    PacienteId INT           NOT NULL,
    Dni        VARCHAR(20)   NOT NULL,
    Nombre     NVARCHAR(100) NOT NULL,
    Email      VARCHAR(120)  NULL,
    Telefono   VARCHAR(20)   NULL,
    CONSTRAINT PK_Paciente PRIMARY KEY CLUSTERED (PacienteId)
);

CREATE TABLE privacidad.Turno (
    TurnoId      INT           NOT NULL,
    PacienteId   INT           NULL,
    Especialidad VARCHAR(40)   NOT NULL,
    FechaTurno   DATE          NOT NULL,
    Diagnostico  VARCHAR(200)  NULL,
    Medico       NVARCHAR(100) NOT NULL,
    CONSTRAINT PK_Turno PRIMARY KEY CLUSTERED (TurnoId),
    CONSTRAINT FK_Turno_Paciente FOREIGN KEY (PacienteId) REFERENCES privacidad.Paciente (PacienteId)
);

CREATE TABLE privacidad.Consentimiento (
    ConsentimientoId INT         NOT NULL,
    PacienteId       INT         NOT NULL,
    Finalidad        VARCHAR(40) NOT NULL,
    Otorgado         BIT         NOT NULL,
    Fecha            DATE        NOT NULL,
    CONSTRAINT PK_Consentimiento PRIMARY KEY CLUSTERED (ConsentimientoId),
    CONSTRAINT FK_Consentimiento_Paciente FOREIGN KEY (PacienteId) REFERENCES privacidad.Paciente (PacienteId)
);

CREATE TABLE privacidad.ContactoMarketing (
    ContactoId           INT          NOT NULL,
    PacienteId           INT          NULL,
    Email                VARCHAR(120) NOT NULL,
    FechaUltimaActividad DATE         NOT NULL,
    Baja                 BIT          NOT NULL,
    CONSTRAINT PK_ContactoMarketing PRIMARY KEY CLUSTERED (ContactoId),
    CONSTRAINT FK_ContactoMarketing_Paciente FOREIGN KEY (PacienteId) REFERENCES privacidad.Paciente (PacienteId)
);

INSERT INTO privacidad.Paciente (PacienteId, Dni, Nombre, Email, Telefono)
VALUES
    (1, '00000001', N'Paciente Uno',  'paciente01@ejemplo.test', '11-5550-0101'),
    (2, '00000002', N'Paciente Dos',  'paciente02@ejemplo.test', NULL),
    (3, '00000003', N'Paciente Tres', 'paciente03@ejemplo.test', '11-5550-0103');

INSERT INTO privacidad.Turno (TurnoId, PacienteId, Especialidad, FechaTurno, Diagnostico, Medico)
VALUES
    (1, 1, 'Cardiologia',  '2020-03-10', 'Diagnostico ficticio A', N'Medico Alfa'),
    (2, 1, 'Clinica',      '2026-05-20', 'Diagnostico ficticio B', N'Medico Beta'),
    (3, 2, 'Clinica',      '2019-11-05', 'Diagnostico ficticio C', N'Medico Beta'),
    (4, 3, 'Dermatologia', '2026-06-15', 'Diagnostico ficticio D', N'Medico Alfa');

INSERT INTO privacidad.Consentimiento (ConsentimientoId, PacienteId, Finalidad, Otorgado, Fecha)
VALUES
    (1, 1, 'Marketing', 1, '2025-04-01'),
    (2, 2, 'Marketing', 1, '2023-01-15'),
    (3, 3, 'Marketing', 0, '2022-08-30');

INSERT INTO privacidad.ContactoMarketing (ContactoId, PacienteId, Email, FechaUltimaActividad, Baja)
VALUES
    (1, 1,    'paciente01@ejemplo.test',  '2026-04-01', 0),
    (2, 2,    'paciente02@ejemplo.test',  '2023-01-15', 0),
    (3, 3,    'paciente03@ejemplo.test',  '2022-08-30', 1),
    (4, NULL, 'prospecto01@ejemplo.test', '2025-12-01', 0);
GO
```

Para comprobar la carga:

<!-- check: U6.P.02 -->
```sql
SELECT 'ContactoMarketing' AS Tabla, COUNT(*) AS Filas FROM privacidad.ContactoMarketing
UNION ALL
SELECT 'Consentimiento', COUNT(*) FROM privacidad.Consentimiento
UNION ALL
SELECT 'Paciente', COUNT(*) FROM privacidad.Paciente
UNION ALL
SELECT 'Turno', COUNT(*) FROM privacidad.Turno
ORDER BY Tabla;
```

**Resultado esperado.**

| Tabla | Filas |
|---|---:|
| Consentimiento | 3 |
| ContactoMarketing | 4 |
| Paciente | 3 |
| Turno | 4 |

## Ejercicios

### Ejercicio 23 · Inventario y clasificación del escenario
<!-- ejercicio: U6.23 | nivel: inicial | tipo: conceptual | verificacion: razonamiento -->

:::note[Enunciado]
Clasificá cada atributo de la tabla original de `SaludEnCasa` (nombre, DNI, contraseña, diagnóstico, religión, tarjeta, dirección IP, consentimiento, médico, fecha del turno) como dato personal, dato sensible según la Ley 25.326 o categoría especial según el RGPD, o ninguno, citando el artículo. Indicá además (a) si la campaña a España activa el RGPD, (b) si el proveedor de analítica es encargado o responsable y (c) qué atributos eliminarías por minimización.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para cada atributo se pregunta: ¿identifica o hace identificable a una persona (art. 2 Ley; art. 4.1 RGPD)?, ¿pertenece a una categoría sensible (art. 2 y 7 Ley) o especial (art. 9.1 RGPD)? y ¿para qué finalidad se necesita (art. 4.1 Ley; art. 5.1.c RGPD)?

| Atributo | Clasificación | Fundamento | Finalidad / decisión |
|---|---|---|---|
| Nombre, DNI | Dato personal | Ley art. 2; RGPD art. 4.1. Nombre y DNI figuran entre los datos del art. 5.2.c de la Ley que no requieren consentimiento | Necesarios para gestionar el turno |
| Diagnóstico | Sensible (salud) y categoría especial | Ley art. 2 y 7 (los establecimientos sanitarios pueden tratar los datos de sus pacientes con secreto profesional: art. 8); RGPD art. 9.1 y excepción del art. 9.2 (asistencia sanitaria) | Solo para atención clínica; no para analítica ni marketing |
| Religión | Sensible y categoría especial | Ley art. 2 y 7.1 (nadie puede ser obligado a proporcionarlos); RGPD art. 9.1 | No hay finalidad que lo justifique para turnos: **eliminar** (minimización, Ley art. 4.1; RGPD art. 5.1.c) |
| Contraseña sin hash | No es sensible, pero su almacenamiento en claro incumple la seguridad | Ley art. 9.1; RGPD art. 32.1 y 5.1.f | Guardar solo un derivado con sal en el componente de identidad; **no** conservar la contraseña |
| Tarjeta | Dato personal (financiero); no sensible | Ley art. 2 y 9; RGPD art. 4.1 y 32 | Solo en el sistema de cobro; no en la base clínica. Afecta la **confidencialidad** (ISO/IEC 25012) |
| Dirección IP | Dato personal cuando permite identificar o hacer identificable a una persona | Ley art. 2 ("determinables"); RGPD art. 4.1 (identificador en línea) | Conservar solo para seguridad, con plazo corto |
| Consentimiento | Dato personal asociado (evidencia) | Ley art. 5.1; RGPD art. 5.2 (poder demostrar el cumplimiento) | Conservar con fecha y finalidad |
| Médico | Dato personal del profesional; junto con el paciente revela información de salud | Ley art. 2; RGPD art. 4.1 y 9.1 | Acceso restringido |
| Fecha del turno | No es sensible por sí sola; en este contexto revela una consulta de salud | Ley art. 2 y 7; RGPD art. 9.1 (por inferencia) | Misma restricción que el diagnóstico |

(a) **Sí, probablemente.** El RGPD se aplica si se ofrecen servicios a personas que están en la Unión (art. 3.2.a), aunque la empresa no tenga establecimiento allí. Importan la oferta dirigida y el lugar donde está el titular; no su ciudadanía ni que el sitio sea accesible (considerando 23). La ley argentina sigue rigiendo el tratamiento realizado en el país.

(b) Depende de quién **determina los fines y medios** (RGPD art. 4.7 y 4.8). Si el proveedor solo trata la copia por cuenta de `SaludEnCasa` y según sus instrucciones, es encargado y necesita el contrato del art. 28.3; si decide usarla para sus propios fines, pasa a ser responsable de ese tratamiento (art. 28.10). En la Ley 25.326, quien presta servicios por cuenta de terceros no puede aplicar los datos a un fin distinto del contrato ni cederlos, y cumplido el contrato debe destruirlos (art. 25). La decisión que falta conocer: qué hace el proveedor con la copia y por cuánto tiempo.

(c) Eliminar la **religión** (sin finalidad) y la **contraseña en claro**; separar **tarjeta**, **diagnóstico** y **médico** de la copia analítica; reducir la **IP** a lo necesario para seguridad; y pasar el proveedor a datos agregados o seudonimizados (ejercicio 24).
</details>

### Ejercicio 24 · Seudonimización con sal y por qué la sal importa
<!-- ejercicio: U6.24 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Para la copia analítica, reemplazá el DNI por un seudónimo calculado con `HASHBYTES('SHA2_256', ...)` y una sal, y contá turnos por seudónimo. Luego mostrá que el mismo hash **sin sal** sobre DNI de 8 dígitos se revierte probando candidatos, y que con sal no. Explicá qué sigue siendo la copia desde el punto de vista legal.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El seudónimo es `SHA2_256(sal + DNI)`: determinista (la misma persona produce siempre el mismo valor, así el análisis puede agrupar) pero imposible de recalcular sin la sal. La sal de este laboratorio (`0x0011...EEFF`) es un valor ficticio; en un sistema real se genera aleatoria, se guarda separada de la copia analítica, con acceso restringido, y no va en el código ni en el repositorio.

Parte A: turnos por seudónimo (se muestran los primeros 16 caracteres del hash).

<!-- check: U6.24 -->
```sql
DECLARE @Sal VARBINARY(16) = 0x00112233445566778899AABBCCDDEEFF;

SELECT
    LEFT(CONVERT(CHAR(64), h.Valor, 2), 16) AS SeudonimoInicio,
    COUNT(*) AS Turnos
FROM privacidad.Turno AS t
JOIN privacidad.Paciente AS p ON p.PacienteId = t.PacienteId
CROSS APPLY (SELECT HASHBYTES('SHA2_256', @Sal + CONVERT(VARBINARY(20), p.Dni)) AS Valor) AS h
GROUP BY h.Valor
ORDER BY SeudonimoInicio;
GO
```

**Resultado esperado (parte A).**

| SeudonimoInicio | Turnos |
|---|---:|
| 84A608E4E302CBE7 | 2 |
| 8652D331B11148FE | 1 |
| 89229A290DAE678A | 1 |

Parte B: un atacante conoce el formato (8 dígitos) y prueba candidatos. Con `GENERATE_SERIES` (SQL Server 2022; en 2019 se reemplaza por una tabla de números) probamos del 1 al 5, que cubre los tres DNI de la tabla. En la realidad el espacio es del orden de 10^8 candidatos, que se recorre en poco tiempo con hardware común.

<!-- check: U6.24 -->
```sql
DECLARE @Sal VARBINARY(16) = 0x00112233445566778899AABBCCDDEEFF;

WITH Candidato AS (
    SELECT RIGHT(CONCAT('00000000', value), 8) AS Dni
    FROM GENERATE_SERIES(1, 5)
),
Publicado AS (
    SELECT PacienteId,
           HASHBYTES('SHA2_256', Dni)                                AS HashSinSal,
           HASHBYTES('SHA2_256', @Sal + CONVERT(VARBINARY(20), Dni)) AS HashConSal
    FROM privacidad.Paciente
)
SELECT 'Con sal' AS Variante, COUNT(*) AS PacientesRecuperados
FROM Publicado AS pu
JOIN Candidato AS c ON pu.HashConSal = HASHBYTES('SHA2_256', c.Dni)
UNION ALL
SELECT 'Sin sal', COUNT(*)
FROM Publicado AS pu
JOIN Candidato AS c ON pu.HashSinSal = HASHBYTES('SHA2_256', c.Dni)
ORDER BY Variante;
```

**Resultado esperado (parte B).**

| Variante | PacientesRecuperados |
|---|---:|
| Con sal | 0 |
| Sin sal | 3 |

Sin sal, el hash de un identificador de espacio pequeño es reversible por diccionario: no protege. Con una sal secreta, el atacante no puede reproducir el hash.

**Qué es la copia.** Seguirá siendo **dato personal**: el RGPD define la seudonimización como un tratamiento tras el cual los datos no se atribuyen a una persona sin información adicional que se mantiene por separado (art. 4.5), y el considerando 26 aclara que los datos seudonimizados siguen siendo información sobre una persona identificable. Es una medida de seguridad y minimización (art. 25 y 32.1), no anonimización. La Ley 25.326 solo exceptúa de ciertos deberes la **disociación** (art. 2): un tratamiento tras el cual la información no se puede asociar a persona determinada o determinable. Mientras `SaludEnCasa` conserve la sal y el DNI, puede reidentificar, de modo que no hay disociación. Característica ISO/IEC 25012 protegida: **confidencialidad**; costo: se pierde **comprensibilidad** para quien necesite saber quién es.
</details>

### Ejercicio 25 · Enmascaramiento dinámico de datos
<!-- ejercicio: U6.25 | nivel: intermedio | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Configurá Dynamic Data Masking sobre `Dni` (mostrar solo los últimos 4 dígitos), `Email` (función de correo) y `Telefono` (función por defecto) de `privacidad.Paciente`. Creá un usuario `AnalistaMascara` sin inicio de sesión y con `SELECT` sobre el esquema, sin `UNMASK`, y compará qué ve él con lo que ve el propietario. Comprobá en el catálogo qué columnas están enmascaradas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `ALTER COLUMN ... ADD MASKED WITH (FUNCTION = ...)` define la máscara; el dato **no cambia** en disco, solo lo que devuelve la consulta a quienes no tienen el permiso `UNMASK`. El propietario de la base (`dbo`) lo tiene implícitamente. Para ver el efecto sin crear un inicio de sesión se usa `CREATE USER ... WITHOUT LOGIN` y `EXECUTE AS USER`.

<!-- check: U6.25 -->
```sql
ALTER TABLE privacidad.Paciente ALTER COLUMN Dni      ADD MASKED WITH (FUNCTION = 'partial(0, "XXXX", 4)');
ALTER TABLE privacidad.Paciente ALTER COLUMN Email    ADD MASKED WITH (FUNCTION = 'email()');
ALTER TABLE privacidad.Paciente ALTER COLUMN Telefono ADD MASKED WITH (FUNCTION = 'default()');
GO

CREATE USER AnalistaMascara WITHOUT LOGIN;
GRANT SELECT ON SCHEMA::privacidad TO AnalistaMascara;
GO
```

Ahora se consulta como propietario, como `AnalistaMascara` y se revisa el catálogo:

<!-- check: U6.25 -->
```sql
SELECT PacienteId, Dni, Email, Telefono
FROM privacidad.Paciente
ORDER BY PacienteId;

EXECUTE AS USER = 'AnalistaMascara';

SELECT PacienteId, Dni, Email, Telefono
FROM privacidad.Paciente
ORDER BY PacienteId;

REVERT;

SELECT c.name AS Columna, mc.masking_function AS Funcion
FROM sys.masked_columns AS mc
JOIN sys.columns AS c ON c.object_id = mc.object_id AND c.column_id = mc.column_id
WHERE mc.object_id = OBJECT_ID('privacidad.Paciente')
ORDER BY c.name;
```

**Resultado esperado.**

Como propietario (sin máscara):

| PacienteId | Dni | Email | Telefono |
|---:|---|---|---|
| 1 | 00000001 | paciente01@ejemplo.test | 11-5550-0101 |
| 2 | 00000002 | paciente02@ejemplo.test | NULL |
| 3 | 00000003 | paciente03@ejemplo.test | 11-5550-0103 |

Como `AnalistaMascara` (sin `UNMASK`):

| PacienteId | Dni | Email | Telefono |
|---:|---|---|---|
| 1 | XXXX0001 | pXXX@XXXX.com | xxxx |
| 2 | XXXX0002 | pXXX@XXXX.com | NULL |
| 3 | XXXX0003 | pXXX@XXXX.com | xxxx |

Catálogo:

| Columna | Funcion |
|---|---|
| Dni | partial(0, "XXXX", 4) |
| Email | email() |
| Telefono | default() |

El enmascaramiento reduce la exposición accidental en las consultas de quien no necesita el dato completo (**confidencialidad**, ISO/IEC 25012; minimización del acceso, art. 25 del RGPD). Observá que el `NULL` no se enmascara: la máscara no oculta que el dato está ausente.
</details>

### Ejercicio 26 · El enmascaramiento no es control de acceso
<!-- ejercicio: U6.26 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Con el enmascaramiento del ejercicio 25, `AnalistaMascara` conoce el DNI de una persona (`00000002`) y quiere confirmar si es paciente. Mostrá que puede hacerlo filtrando por la columna enmascarada y proponé un control que lo impida. Verificá que el control funciona.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** La máscara se aplica al *resultado* y no al predicado: `WHERE Dni = '00000002'` se evalúa con el valor real, así que el conteo revela si existe. El control correcto es de acceso: denegar `SELECT` sobre la columna sensible a quien no la necesita. Se parte de la configuración del ejercicio 25.

<!-- check: U6.26 -->
```sql
DECLARE @Bitacora TABLE (Paso INT NOT NULL, Intento VARCHAR(60) NOT NULL, Resultado VARCHAR(40) NOT NULL);

EXECUTE AS USER = 'AnalistaMascara';

INSERT INTO @Bitacora
SELECT 1, 'Filtrar por DNI con máscara', CONCAT(COUNT(*), ' coincidencia(s)')
FROM privacidad.Paciente
WHERE Dni = '00000002';

REVERT;

DENY SELECT ON privacidad.Paciente (Dni) TO AnalistaMascara;

EXECUTE AS USER = 'AnalistaMascara';

BEGIN TRY
    INSERT INTO @Bitacora
    SELECT 2, 'Filtrar por DNI tras DENY', CONCAT(COUNT(*), ' coincidencia(s)')
    FROM privacidad.Paciente
    WHERE Dni = '00000002';
END TRY
BEGIN CATCH
    INSERT INTO @Bitacora VALUES (2, 'Filtrar por DNI tras DENY', CONCAT('Error ', ERROR_NUMBER()));
END CATCH;

REVERT;

SELECT Paso, Intento, Resultado
FROM @Bitacora
ORDER BY Paso;
```

**Resultado esperado.**

| Paso | Intento | Resultado |
|---:|---|---|
| 1 | Filtrar por DNI con máscara | 1 coincidencia(s) |
| 2 | Filtrar por DNI tras DENY | Error 230 |

Con la máscara, el analista no ve el DNI pero **infiere** que existe (y, probando valores, podría reconstruirlo). Tras `DENY SELECT` sobre la columna, el motor rechaza la consulta (error 230). Conclusión: el enmascaramiento dinámico es una capa de reducción de exposición, no un reemplazo del control de acceso ni del cifrado. Es una medida de seguridad apropiada al riesgo (Ley art. 9.1; RGPD art. 32.1), pero por sí sola no alcanza para datos de salud o identificadores.
</details>

### Ejercicio 27 · Retención: borrar y anonimizar por vencimiento
<!-- ejercicio: U6.27 | nivel: intermedio | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
Política del ejercicio (plazos ficticios, no legales): los contactos de marketing se borran si dieron de baja o llevan más de 24 meses sin actividad; los turnos de más de 5 años se conservan para estadística pero se anonimizan (se quitan el paciente y el diagnóstico). Con fecha de corte `2026-06-30`, aplicá la política y mostrá cuántas filas se vieron afectadas y cuántas quedan identificables.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Fijar la fecha de corte en una variable, capturar `@@ROWCOUNT` justo después de cada sentencia y resumir. Borrar cuando el dato ya no es necesario (Ley art. 4, inciso 7; RGPD art. 5.1.e); anonimizar cuando se necesita el hecho estadístico pero no la identidad.

<!-- check: U6.27 -->
```sql
DECLARE @FechaCorte DATE = '2026-06-30';
DECLARE @ContactosBorrados INT, @TurnosAnonimizados INT;

DELETE FROM privacidad.ContactoMarketing
WHERE Baja = 1
   OR FechaUltimaActividad < DATEADD(MONTH, -24, @FechaCorte);
SET @ContactosBorrados = @@ROWCOUNT;

UPDATE privacidad.Turno
SET PacienteId = NULL,
    Diagnostico = NULL
WHERE FechaTurno < DATEADD(YEAR, -5, @FechaCorte);
SET @TurnosAnonimizados = @@ROWCOUNT;

SELECT Dataset, Accion, Filas
FROM (
    SELECT 'Contactos de marketing' AS Dataset, 'Borrados' AS Accion, @ContactosBorrados AS Filas
    UNION ALL
    SELECT 'Contactos de marketing', 'Conservados', COUNT(*) FROM privacidad.ContactoMarketing
    UNION ALL
    SELECT 'Turnos', 'Anonimizados', @TurnosAnonimizados
    UNION ALL
    SELECT 'Turnos', 'Con paciente identificable', COUNT(*) FROM privacidad.Turno WHERE PacienteId IS NOT NULL
) AS Resumen
ORDER BY Dataset, Accion;
```

**Resultado esperado.**

| Dataset | Accion | Filas |
|---|---|---:|
| Contactos de marketing | Borrados | 2 |
| Contactos de marketing | Conservados | 2 |
| Turnos | Anonimizados | 2 |
| Turnos | Con paciente identificable | 2 |

Se borraron el contacto 3 (baja) y el 2 (última actividad en 2023, anterior al `2024-06-30`); se anonimizaron los turnos 1 (2020) y 3 (2019).

:::caution[Límites de la política]
- Los plazos son un ejemplo. El plazo real de cada dataset lo fija la finalidad y la normativa aplicable (por ejemplo, la sanitaria para la historia clínica, que este apunte no desarrolla).
- Un turno "anonimizado" que conserva especialidad, fecha y médico puede seguir siendo reidentificable en un servicio chico: si no se puede garantizar la disociación (Ley art. 2), no se lo debe llamar anónimo.
- Borrar en producción no borra las copias de seguridad: la política debe contemplar su vencimiento por rotación y qué pasa al restaurar (ver el [caso 5](/bbdd-aplicadas/unidad-6/practica/casos-integradores/)).
:::
</details>

### Ejercicio 28 · Atender un derecho de acceso
<!-- ejercicio: U6.28 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
`Paciente Uno` (DNI `00000001`) ejerce su derecho de acceso y pide una copia completa de sus datos. Escribí una consulta que reúna, en un solo resultado legible, todo lo que la base operativa guarda sobre esa persona, sin incluir datos de terceros. Indicá los plazos de la Ley 25.326 y del RGPD y qué otras fuentes habría que revisar.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Parametrizar el DNI (ya verificado la identidad por el canal autenticado), llevar cada origen a la forma común *origen, dato, valor* con `CROSS APPLY (VALUES ...)` para el perfil y consultas por tabla para el resto, y ordenar por origen. **No** se incluye el nombre del médico: es información de un tercero (la ley indica que la respuesta nunca puede revelar datos de terceros, art. 15); en un caso real se decide con asesoramiento qué parte de la historia incluye el derecho de acceso.

<!-- check: U6.28 -->
```sql
DECLARE @Dni VARCHAR(20) = '00000001';

SELECT Origen, Dato, Valor
FROM (
    SELECT 1 AS Orden, 'Paciente' AS Origen, v.Dato, v.Valor
    FROM privacidad.Paciente AS p
    CROSS APPLY (VALUES
        ('Dni', CAST(p.Dni AS NVARCHAR(200))),
        ('Nombre', CAST(p.Nombre AS NVARCHAR(200))),
        ('Email', CAST(p.Email AS NVARCHAR(200))),
        ('Telefono', CAST(p.Telefono AS NVARCHAR(200)))
    ) AS v (Dato, Valor)
    WHERE p.Dni = @Dni

    UNION ALL

    SELECT 2, 'Turno',
           CONCAT('Turno ', t.TurnoId, ' (', t.Especialidad, ', ', CONVERT(VARCHAR(10), t.FechaTurno, 23), ')'),
           t.Diagnostico
    FROM privacidad.Turno AS t
    JOIN privacidad.Paciente AS p ON p.PacienteId = t.PacienteId
    WHERE p.Dni = @Dni

    UNION ALL

    SELECT 3, 'Consentimiento', c.Finalidad,
           CONCAT(CASE c.Otorgado WHEN 1 THEN 'otorgado' ELSE 'no otorgado' END,
                  ' el ', CONVERT(VARCHAR(10), c.Fecha, 23))
    FROM privacidad.Consentimiento AS c
    JOIN privacidad.Paciente AS p ON p.PacienteId = c.PacienteId
    WHERE p.Dni = @Dni

    UNION ALL

    SELECT 4, 'ContactoMarketing', x.Dato, x.Valor
    FROM privacidad.ContactoMarketing AS m
    JOIN privacidad.Paciente AS p ON p.PacienteId = m.PacienteId
    CROSS APPLY (VALUES
        ('Email', CAST(m.Email AS NVARCHAR(200))),
        ('UltimaActividad', CONVERT(NVARCHAR(10), m.FechaUltimaActividad, 23))
    ) AS x (Dato, Valor)
    WHERE p.Dni = @Dni
) AS Copia
ORDER BY Orden, Dato;
```

**Resultado esperado.**

| Origen | Dato | Valor |
|---|---|---|
| Paciente | Dni | 00000001 |
| Paciente | Email | paciente01@ejemplo.test |
| Paciente | Nombre | Paciente Uno |
| Paciente | Telefono | 11-5550-0101 |
| Turno | Turno 1 (Cardiologia, 2020-03-10) | Diagnostico ficticio A |
| Turno | Turno 2 (Clinica, 2026-05-20) | Diagnostico ficticio B |
| Consentimiento | Marketing | otorgado el 2025-04-01 |
| ContactoMarketing | Email | paciente01@ejemplo.test |
| ContactoMarketing | UltimaActividad | 2026-04-01 |

**Plazos y alcance.**

- Ley 25.326: 10 días corridos desde la intimación fehaciente (art. 14); gratuito a intervalos no inferiores a seis meses salvo interés legítimo; la información debe ser clara y abarcar todo el registro (art. 15).
- RGPD: un mes desde la recepción, prorrogable dos meses más en casos complejos (art. 12.3); el derecho de acceso es el del art. 15. Si ambas normas fueran aplicables, responder dentro del plazo más corto cumple los dos.
- La consulta cubre solo la base operativa. El flujo real debe revisar también los logs, las copias en el proveedor de analítica, los archivos exportados y las copias de seguridad, por eso importan el inventario y el linaje (ver [gobierno de datos](/bbdd-aplicadas/unidad-6/teoria/gobierno-privacidad/)).
- El acceso supone verificar la identidad de forma proporcional y registrar la solicitud, la fecha y la respuesta como evidencia (RGPD art. 5.2).
</details>

## Actividad integradora (sin resolución única)

Esta actividad cierra el laboratorio como trabajo de diseño; no tiene una resolución verificable en el motor.

1. **Matriz normativa por finalidad.** Para turnos, atención clínica, facturación, analítica y marketing, indicá base o habilitación (y la condición adicional para datos de salud), la información que recibe el titular, el dato mínimo, el plazo de conservación y su evento inicial, los controles de seguridad y el contrato con el proveedor. No respondas "consentimiento para todo": analizá cada finalidad por separado (Ley art. 5, 6 y 7; RGPD art. 6 y 9).
2. **Incidente.** Un bucket del proveedor estuvo público durante 36 horas. Armá la línea de tiempo (detección, contención, evidencia, evaluación de riesgo, comunicación) y señalá qué exige el RGPD (notificación a la autoridad a más tardar 72 horas después de tener constancia, art. 33, y comunicación a los interesados si hay alto riesgo, art. 34). La Ley 25.326 impone el deber de seguridad (art. 9) pero su texto no fija un plazo de notificación. Características de ISO/IEC 25012 afectadas: confidencialidad, conformidad, credibilidad y trazabilidad.

## Fuentes

- Ley 25.326 y Decreto 1558/2001: [InfoLEG](https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm), consultados el 2026-11-17.
- Reglamento (UE) 2016/679: [EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679), consultado el 2026-11-17.
- Resumen público de ISO/IEC 25012: [iso25000.com](https://iso25000.com/index.php/normas-iso-25000/iso-25012).
- Dynamic Data Masking, `HASHBYTES` y `EXECUTE AS`: documentación de [SQL Server en Microsoft Learn](https://learn.microsoft.com/es-es/sql/relational-databases/security/dynamic-data-masking).
