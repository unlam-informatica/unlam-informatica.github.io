---
title: Repaso de SQL
slug: bbdd-aplicadas/unidad-1/teoria/repaso-sql
sidebar:
  order: 2
---

## Para qué sirve

Las unidades siguientes suponen que ya manejás el SQL básico: crear estructuras, cargar y consultar datos, proteger
la integridad y empaquetar lógica en el servidor. Esta lección lo repasa con un único dominio de ejemplo, un esquema
`academia` con alumnos, materias e inscripciones, y con datos sintéticos. Los resultados se obtuvieron con SQL Server
2022.

Cada bloque de código que crea objetos empieza por `CREATE SCHEMA academia;` y por las tablas y los datos que necesita,
de modo que se puede ejecutar solo: no depende de los bloques anteriores. Justamente por eso **no se pueden ejecutar
dos de esos bloques seguidos en la misma base**: el segundo falla porque el esquema `academia` y sus tablas ya
existen. Para probar cada ejemplo, usá una base de práctica recién creada o borrá antes los objetos y el esquema
`academia` de la ejecución previa. El único bloque que no crea nada es el de `ISNULL`, `COALESCE` y `NULLIF`: solo declara variables y se puede
ejecutar en cualquier base y cuantas veces quieras. Si no sabés qué es una base de práctica, ver
[Cómo estudiar · Antes de ejecutar los ejemplos](/bbdd-aplicadas/como-estudiar/#antes-de-ejecutar-los-ejemplos).

:::note[Convenciones de los ejemplos]
Los ejemplos propios usan tablas en singular y PascalCase (`Alumno`, `Inscripcion`) y un esquema en minúsculas
(`academia`). Los ejercicios de cátedra conservan sus identificadores (esquema `ddbba`). Cada sentencia termina en
`;` y `GO` separa los lotes donde el motor lo exige. Para ver las diferencias entre versiones, consultá la
[documentación de Transact-SQL](https://learn.microsoft.com/es-es/sql/t-sql/language-reference).
:::

## Modelo de datos y restricciones

La **abstracción de datos** oculta los detalles físicos de almacenamiento y expone solo las características
esenciales. Un **modelo de datos** es una colección de conceptos que describen la *estructura* de una base de datos:
los tipos de datos, las relaciones y las restricciones que se aplican sobre ellos. En el modelo relacional, tabla,
fila y columna corresponden a relación, tupla y atributo.

| Tipo de restricción | Descripción | Ejemplo |
|------|-------------|---------|
| **Implícitas** | Inherentes al modelo o impuestas por el tipo de dato | Una columna `INT` solo acepta enteros |
| **Explícitas** | Declaradas en el esquema (PK, FK, `CHECK`, etc.) | "El alumno referenciado debe existir" |
| **Semánticas** | Reglas de negocio que maneja la aplicación | "Una promoción no vale para ciertos proveedores" |

Las implícitas y las explícitas las hace cumplir el RDBMS; las semánticas quedan a cargo de la aplicación (o de
triggers y procedimientos, como veremos).

## Tipos de datos

Hay tipos básicos definidos por el estándar ANSI y otros propios de cada motor. Estos son los de SQL Server.

### Numéricos

<div class="data-type-table">

| Tipo de dato   |              Tamaño | Uso típico                                   |                 Valor mínimo |                Valor máximo |
| -------------- | ------------------: | -------------------------------------------- | ---------------------------: | --------------------------: |
| `BIT`          |        1 bit aprox. | Valores booleanos: activo/inactivo, sí/no    |                          `0` |                         `1` |
| `TINYINT`      |              1 byte | Estados, edades, cantidades muy chicas       |                          `0` |                       `255` |
| `SMALLINT`     |             2 bytes | Cantidades chicas                            |                    `-32.768` |                    `32.767` |
| `INT`          |             4 bytes | IDs, contadores, cantidades generales        |             `-2.147.483.648` |             `2.147.483.647` |
| `BIGINT`       |             8 bytes | IDs enormes, tablas con muchísimos registros | `-9.223.372.036.854.775.808` | `9.223.372.036.854.775.807` |
| `DECIMAL(p,s)` |        5 a 17 bytes | Importes, porcentajes, valores exactos       |               Depende de `p` |              Depende de `p` |
| `NUMERIC(p,s)` |        5 a 17 bytes | Igual que `DECIMAL`                          |               Depende de `p` |              Depende de `p` |
| `SMALLMONEY`   |             4 bytes | Dinero, aunque suele preferirse `DECIMAL`    |              `-214.748,3648` |              `214.748,3647` |
| `MONEY`        |             8 bytes | Dinero, aunque suele preferirse `DECIMAL`    |  `-922.337.203.685.477,5808` |  `922.337.203.685.477,5807` |
| `REAL`         |             4 bytes | Números aproximados                          |           aprox. `-3.40E+38` |           aprox. `3.40E+38` |
| `FLOAT`        | 8 bytes por defecto | Cálculos científicos o aproximados           |          aprox. `-1.79E+308` |          aprox. `1.79E+308` |

</div>

### Fecha y hora

| Tipo | Qué guarda |
|---|---|
| `DATE` | Solo la fecha |
| `TIME(n)` | Solo la hora, con `n` decimales de segundo |
| `DATETIME2(n)` | Fecha y hora con precisión configurable; es el tipo recomendado para código nuevo |
| `DATETIMEOFFSET(n)` | Fecha y hora con desfase respecto de UTC |
| `DATETIME`, `SMALLDATETIME` | Tipos más antiguos, de menor rango y precisión |

### Cadenas de caracteres

| Tipo | Longitud | Unicode | Almacenamiento |
|---|---|---|---|
| `CHAR(n)` | Fija: rellena con espacios hasta `n` | No | `n` bytes |
| `VARCHAR(n)` | Variable hasta `n` | No | Bytes realmente usados (más un pequeño encabezado) |
| `NCHAR(n)` | Fija | Sí | 2 bytes por carácter |
| `NVARCHAR(n)` | Variable hasta `n` | Sí | 2 bytes por carácter usado |
| `VARCHAR(MAX)`, `NVARCHAR(MAX)` | Variable, hasta unos 2 GB | No / Sí | Para textos largos |

`UNIQUEIDENTIFIER` guarda un identificador único global (GUID) de 16 bytes.

<!-- check: U1.T.RS.02 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.EjemploTipo (
    EjemploTipoId INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    Dia           DATE,
    Hora          TIME(0),
    Momento       DATETIME2(3),
    MomentoZona   DATETIMEOFFSET(0),
    CodigoFijo    CHAR(5),
    NombreVar     VARCHAR(5),
    NombreNchar   NCHAR(5),
    NombreNvar    NVARCHAR(5),
    Detalle       VARCHAR(MAX)
);

INSERT INTO academia.EjemploTipo
    (Dia, Hora, Momento, MomentoZona, CodigoFijo, NombreVar, NombreNchar, NombreNvar, Detalle)
VALUES
    ('2026-03-01', '14:30:15', '2026-03-01T14:30:15.1234', '2026-03-01T14:30:15-03:00',
     'AB', 'AB', N'AB', N'AB', REPLICATE(CAST('x' AS VARCHAR(MAX)), 10000));

SELECT
    Dia,
    Hora,
    Momento,
    MomentoZona,
    DATALENGTH(CodigoFijo)  AS BytesChar,
    DATALENGTH(NombreVar)   AS BytesVarchar,
    DATALENGTH(NombreNchar) AS BytesNchar,
    DATALENGTH(NombreNvar)  AS BytesNvarchar,
    LEN(Detalle)            AS LargoDetalle
FROM academia.EjemploTipo;
```

**Resultado esperado.**

| Dia | Hora | Momento | MomentoZona | BytesChar | BytesVarchar | BytesNchar | BytesNvarchar | LargoDetalle |
|---|---|---|---|---:|---:|---:|---:|---:|
| 2026-03-01 | 14:30:15 | 2026-03-01 14:30:15.123 | 2026-03-01 14:30:15 -03:00 | 5 | 2 | 10 | 4 | 10000 |

`CHAR(5)` ocupa 5 bytes aunque guarde `AB`; `VARCHAR(5)` ocupa 2; `NCHAR` y `NVARCHAR` duplican por ser
Unicode. `DATETIME2(3)` descartó el cuarto decimal que le pasamos. Preferí `VARCHAR` sobre `CHAR` cuando la longitud
varía mucho, y `NVARCHAR` cuando el sistema debe manejar caracteres de varios idiomas.

## Catálogos y esquemas

Un **catálogo** es un conjunto de esquemas dentro de un entorno (típicamente una instancia del RDBMS); en SQL
Server se corresponde con una **base de datos**. Un **esquema** es un espacio de nombres que agrupa objetos. El
nombre completo de un objeto es `catálogo.esquema.objeto`, y cada usuario puede tener una base y un esquema
predeterminados.

```text
Catálogo ≈ Base de datos
Esquema  ≈ Espacio de nombres dentro de la base
Tabla    ≈ Objeto dentro de un esquema
```

![db-organization](/bbdd-aplicadas/unidad-1/images/db-organization.png)

`CREATE DATABASE` crea una base nueva; `USE` hace que las sentencias siguientes se ejecuten en ella. La cláusula
`COLLATE` define las reglas de comparación y orden del texto (mayúsculas, acentos). El detalle está en la
[guía de Collation](/bbdd-aplicadas/unidad-2/teoria/collation/).

Los ejemplos de esta lección trabajan dentro de un esquema propio, `academia`. Usarlo tiene tres ventajas: agrupa los
objetos del ejemplo en un espacio de nombres separado, evita depender del esquema `dbo` implícito (en este sitio los
objetos se crean siempre con esquema explícito) y permite eliminar o recrear todo fácilmente. Cada bloque que lo
necesita lo crea con `CREATE SCHEMA academia;`.

Para crear una base hace falta el permiso `CREATE DATABASE`, que tiene un `sysadmin` (por ejemplo, vos en tu
instalación local). El siguiente bloque es un ejemplo de esa sentencia:

<!-- check: U1.T.RS.R1 -->
```sql
CREATE DATABASE Unlam
COLLATE Latin1_General_CI_AS;   -- CI: no distingue mayúsculas; AS: distingue acentos
GO
USE Unlam;
GO
```

Este bloque `CREATE DATABASE` **no se probó en un motor**: es la única parte de esta lección que no se ejecutó. Se
comporta como documenta Microsoft; comprobalo en tu instalación. Si ya tenés una base de práctica, no hace falta crear
otra: cambiá a ella con `USE NombreDeTuBase;`. Los demás ejemplos asumen que estás en una base de práctica donde
todavía no existe el esquema `academia`, y cada uno lo crea junto con sus tablas.

<!-- check: U1.T.RS.01 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT IDENTITY(1, 1) NOT NULL,
    Nombre   VARCHAR(100)       NOT NULL,
    Apellido VARCHAR(100)       NOT NULL,
    Email    VARCHAR(150)       NULL,
    CONSTRAINT PK_Alumno PRIMARY KEY (AlumnoId)
);

CREATE TABLE academia.Materia (
    MateriaId INT IDENTITY(1, 1) NOT NULL,
    Nombre    VARCHAR(100)       NOT NULL,
    Codigo    VARCHAR(20)        NOT NULL,
    CONSTRAINT PK_Materia PRIMARY KEY (MateriaId)
);

CREATE TABLE academia.Inscripcion (
    InscripcionId    INT IDENTITY(1, 1) NOT NULL,
    AlumnoId         INT                NOT NULL,
    MateriaId        INT                NOT NULL,
    FechaInscripcion DATE               NOT NULL,
    CONSTRAINT PK_Inscripcion PRIMARY KEY (InscripcionId),
    CONSTRAINT FK_Inscripcion_Alumno FOREIGN KEY (AlumnoId) REFERENCES academia.Alumno (AlumnoId),
    CONSTRAINT FK_Inscripcion_Materia FOREIGN KEY (MateriaId) REFERENCES academia.Materia (MateriaId)
);

INSERT INTO academia.Alumno (Nombre, Apellido) VALUES ('Ana', 'Prueba');
INSERT INTO academia.Materia (Nombre, Codigo) VALUES ('Bases de Datos', 'BD01');

DECLARE @Error INT = 0;
BEGIN TRY
    INSERT INTO academia.Inscripcion (AlumnoId, MateriaId, FechaInscripcion)
    VALUES (99, 1, '2026-03-01');
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT
    (SELECT COUNT(*) FROM sys.tables WHERE schema_id = SCHEMA_ID('academia')) AS Tablas,
    (SELECT COUNT(*) FROM academia.Inscripcion)                              AS Inscripciones,
    @Error                                                                   AS ErrorFk;
```

**Resultado esperado.**

| Tablas | Inscripciones | ErrorFk |
|---:|---:|---:|
| 3 | 0 | 547 |

El error 547 es la violación de la clave foránea: no existe el alumno 99.

## DDL y DML

| Lenguaje | Sentencias | Opera sobre |
|---|---|---|
| **DDL** (definición) | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | La estructura: bases, tablas, vistas, índices, procedimientos, triggers |
| **DML** (manipulación) | `INSERT`, `UPDATE`, `DELETE`, `MERGE` | Los datos dentro de las estructuras |

`TRUNCATE` vacía la tabla y conserva su estructura. `MERGE` inserta, actualiza o borra según la coincidencia con una
tabla de origen. Los motores modernos no distinguen de forma estricta entre DDL, DML, DQL (consultas), DCL (control
de acceso) y TCL (transacciones): todas son sentencias SQL.

<!-- check: U1.T.RS.22 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Producto (
    ProductoId INT NOT NULL CONSTRAINT PK_Producto PRIMARY KEY,
    Nombre     VARCHAR(30) NOT NULL,
    Precio     DECIMAL(10,2) NOT NULL
);
CREATE TABLE academia.ProductoNovedad (
    ProductoId INT NOT NULL,
    Nombre     VARCHAR(30) NOT NULL,
    Precio     DECIMAL(10,2) NOT NULL
);
CREATE TABLE academia.ProductoTemporal (Nombre VARCHAR(30) NOT NULL);

INSERT INTO academia.Producto (ProductoId, Nombre, Precio) VALUES (1, 'Cuaderno', 100), (2, 'Lapiz', 20), (3, 'Regla', 30);
INSERT INTO academia.ProductoNovedad (ProductoId, Nombre, Precio) VALUES (2, 'Lapiz', 25), (4, 'Goma', 15);
INSERT INTO academia.ProductoTemporal VALUES ('a'), ('b');

UPDATE academia.Producto SET Precio = Precio * 1.10 WHERE ProductoId = 1;
DELETE FROM academia.Producto WHERE ProductoId = 3;

MERGE academia.Producto AS destino
USING academia.ProductoNovedad AS origen ON origen.ProductoId = destino.ProductoId
WHEN MATCHED THEN UPDATE SET Precio = origen.Precio
WHEN NOT MATCHED BY TARGET THEN INSERT (ProductoId, Nombre, Precio) VALUES (origen.ProductoId, origen.Nombre, origen.Precio);

TRUNCATE TABLE academia.ProductoTemporal;

SELECT ProductoId, Nombre, Precio, (SELECT COUNT(*) FROM academia.ProductoTemporal) AS FilasTemporal
FROM academia.Producto
ORDER BY ProductoId;
```

**Resultado esperado.**

| ProductoId | Nombre | Precio | FilasTemporal |
|---:|---|---:|---:|
| 1 | Cuaderno | 110.00 | 0 |
| 2 | Lapiz | 25.00 | 0 |
| 4 | Goma | 15.00 | 0 |

## Integridad referencial, claves y restricciones

La **integridad referencial** es el mecanismo por el que el RDBMS asegura que un valor que aparece en una relación
para ciertos atributos también aparezca en la relación referenciada. Cada inserción, borrado y actualización se
comprueba para no violar esas reglas.

### Clave primaria

- Es el conjunto **mínimo** de columnas que identifica de forma unívoca una fila.
- Es implícitamente `NOT NULL` y única.
- Conviene que sea creciente (por ejemplo, `IDENTITY`) y no modificable.
- Por defecto crea el **índice clúster**, que define el orden físico de las filas. Hay **un solo** índice clúster
  por tabla; si lo necesitás en otra columna, declarás la PK como `NONCLUSTERED`. Los índices se estudian en la
  [Unidad 3](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/) y el clúster en [Índice Clustered](/bbdd-aplicadas/unidad-1/teoria/indice-cluster/).

<!-- check: U1.T.RS.03 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Movimiento (
    MovimientoId INT           NOT NULL CONSTRAINT PK_Movimiento PRIMARY KEY NONCLUSTERED,
    Fecha        DATETIME2(0)  NOT NULL,
    Monto        DECIMAL(10,2) NOT NULL,
    INDEX CIX_Movimiento_Fecha CLUSTERED (Fecha)
);

CREATE TABLE academia.Cuota (
    CuotaId INT NOT NULL CONSTRAINT PK_Cuota PRIMARY KEY,
    Monto   DECIMAL(10,2) NOT NULL
);

SELECT
    OBJECT_NAME(object_id) AS Tabla,
    name                   AS Indice,
    type_desc              AS Tipo,
    is_primary_key         AS EsPk
FROM sys.indexes
WHERE object_id IN (OBJECT_ID('academia.Movimiento'), OBJECT_ID('academia.Cuota'))
ORDER BY Tabla, Indice;
```

**Resultado esperado.**

| Tabla | Indice | Tipo | EsPk |
|---|---|---|---:|
| Cuota | PK_Cuota | CLUSTERED | 1 |
| Movimiento | CIX_Movimiento_Fecha | CLUSTERED | 0 |
| Movimiento | PK_Movimiento | NONCLUSTERED | 1 |

### Clave foránea

- Referencia la clave primaria (o una restricción `UNIQUE`) de otra tabla y registra la relación entre ambas.
- Genera una restricción implícita: no se puede insertar un valor inexistente en la tabla referenciada.
- **No** crea un índice automáticamente; conviene crearlo.
- Las columnas deben tener el mismo tipo de dato que las referenciadas.
- Si es compuesta, debe referenciar **todas** las columnas de una PK o `UNIQUE` de la tabla padre, en el mismo orden de tipos.

<!-- check: U1.T.RS.04 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Comision (
    MateriaId   INT NOT NULL,
    ComisionNro INT NOT NULL,
    Turno       VARCHAR(10) NOT NULL,
    CONSTRAINT PK_Comision PRIMARY KEY (MateriaId, ComisionNro)
);

CREATE TABLE academia.Examen (
    ExamenId    INT IDENTITY(1, 1) NOT NULL,
    MateriaId   INT NOT NULL,
    ComisionNro INT NOT NULL,
    Nota        TINYINT NOT NULL,
    CONSTRAINT PK_Examen PRIMARY KEY (ExamenId),
    CONSTRAINT FK_Examen_Comision
        FOREIGN KEY (MateriaId, ComisionNro)
        REFERENCES academia.Comision (MateriaId, ComisionNro)
        ON DELETE CASCADE
);

INSERT INTO academia.Comision (MateriaId, ComisionNro, Turno)
VALUES (1, 1, 'Mañana'), (1, 2, 'Noche');
INSERT INTO academia.Examen (MateriaId, ComisionNro, Nota)
VALUES (1, 1, 7), (1, 1, 9), (1, 2, 6);

DECLARE @Error INT = 0;
BEGIN TRY
    INSERT INTO academia.Examen (MateriaId, ComisionNro, Nota) VALUES (1, 3, 8);
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

DELETE FROM academia.Comision WHERE MateriaId = 1 AND ComisionNro = 1;

SELECT
    @Error                                  AS ErrorComisionInexistente,
    (SELECT COUNT(*) FROM academia.Comision) AS Comisiones,
    (SELECT COUNT(*) FROM academia.Examen)   AS Examenes;
```

**Resultado esperado.**

| ErrorComisionInexistente | Comisiones | Examenes |
|---:|---:|---:|
| 547 | 1 | 1 |

Al borrar la comisión 1 de la materia 1, `ON DELETE CASCADE` eliminó sus dos exámenes y quedó el de la comisión 2.

### Acciones referenciales

Qué hace el motor cuando se borra (`ON DELETE`) o modifica (`ON UPDATE`) una fila referenciada:

| Acción | Efecto |
|---|---|
| `NO ACTION` (por defecto) | Rechaza la operación si hay filas hijas |
| `CASCADE` | Propaga el borrado o el cambio a las filas hijas |
| `SET NULL` | Pone `NULL` en la FK de las hijas (la columna debe admitirlo) |
| `SET DEFAULT` | Pone el valor `DEFAULT` en la FK de las hijas (ese valor debe existir en el padre) |

<!-- check: U1.T.RS.05 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Categoria (
    CategoriaId INT NOT NULL CONSTRAINT PK_Categoria PRIMARY KEY,
    Nombre      VARCHAR(30) NOT NULL
);

CREATE TABLE academia.ArticuloNoAction (
    ArticuloId  INT NOT NULL PRIMARY KEY,
    CategoriaId INT NOT NULL
        CONSTRAINT FK_ArticuloNoAction_Categoria REFERENCES academia.Categoria (CategoriaId) ON DELETE NO ACTION
);
CREATE TABLE academia.ArticuloCascade (
    ArticuloId  INT NOT NULL PRIMARY KEY,
    CategoriaId INT NOT NULL
        CONSTRAINT FK_ArticuloCascade_Categoria REFERENCES academia.Categoria (CategoriaId) ON DELETE CASCADE
);
CREATE TABLE academia.ArticuloSetNull (
    ArticuloId  INT NOT NULL PRIMARY KEY,
    CategoriaId INT NULL
        CONSTRAINT FK_ArticuloSetNull_Categoria REFERENCES academia.Categoria (CategoriaId) ON DELETE SET NULL
);
CREATE TABLE academia.ArticuloSetDefault (
    ArticuloId  INT NOT NULL PRIMARY KEY,
    CategoriaId INT NOT NULL CONSTRAINT DF_ArticuloSetDefault_Categoria DEFAULT (9)
        CONSTRAINT FK_ArticuloSetDefault_Categoria REFERENCES academia.Categoria (CategoriaId) ON DELETE SET DEFAULT
);

INSERT INTO academia.Categoria (CategoriaId, Nombre)
VALUES (1, 'Libros'), (2, 'Cuadernos'), (3, 'Lapices'), (4, 'Mochilas'), (9, 'Sin clasificar');
INSERT INTO academia.ArticuloNoAction  VALUES (1, 1);
INSERT INTO academia.ArticuloCascade   VALUES (1, 2);
INSERT INTO academia.ArticuloSetNull   VALUES (1, 3);
INSERT INTO academia.ArticuloSetDefault VALUES (1, 4);

DECLARE @ErrorNoAction INT = 0;
BEGIN TRY
    DELETE FROM academia.Categoria WHERE CategoriaId = 1;
END TRY
BEGIN CATCH
    SET @ErrorNoAction = ERROR_NUMBER();
END CATCH;
DELETE FROM academia.Categoria WHERE CategoriaId IN (2, 3, 4);

SELECT 'NO ACTION' AS Accion,
       CAST(@ErrorNoAction AS VARCHAR(10)) AS Resultado
UNION ALL
SELECT 'CASCADE',     CAST(COUNT(*) AS VARCHAR(10)) + ' filas hijas' FROM academia.ArticuloCascade
UNION ALL
SELECT 'SET NULL',    ISNULL(CAST(CategoriaId AS VARCHAR(10)), 'NULL') FROM academia.ArticuloSetNull
UNION ALL
SELECT 'SET DEFAULT', CAST(CategoriaId AS VARCHAR(10)) FROM academia.ArticuloSetDefault;
```

**Resultado esperado.**

| Accion | Resultado |
|---|---|
| NO ACTION | 547 |
| CASCADE | 0 filas hijas |
| SET NULL | NULL |
| SET DEFAULT | 9 |

### Otras restricciones

| Restricción | Efecto |
|---|---|
| `UNIQUE` | Prohíbe duplicados. En SQL Server admite **un solo** `NULL`; otros motores lo tratan distinto |
| `CHECK` | Valida que el valor cumpla una condición |
| `NOT NULL` | Prohíbe nulos |
| `DEFAULT` | Asigna un valor si no se indica ninguno |

Las restricciones nombradas con `CONSTRAINT` se identifican en el catálogo y se pueden modificar o eliminar después.

<!-- check: U1.T.RS.21 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Vehiculo (
    VehiculoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Vehiculo PRIMARY KEY,
    Patente    CHAR(7)     NOT NULL,
    Anio       INT         NOT NULL CONSTRAINT CK_Vehiculo_Anio CHECK (Anio > 1900),
    Estado     VARCHAR(10) NOT NULL CONSTRAINT DF_Vehiculo_Estado DEFAULT ('activo'),
    CONSTRAINT UQ_Vehiculo_Patente UNIQUE (Patente),
    CONSTRAINT CK_Vehiculo_Patente CHECK (
        Patente LIKE '[A-Z][A-Z][0-9][0-9][0-9][A-Z][A-Z]'   -- formato Mercosur
        OR Patente LIKE '[A-Z][A-Z][A-Z][0-9][0-9][0-9]'      -- formato anterior
    )
);

INSERT INTO academia.Vehiculo (Patente, Anio) VALUES ('AB123CD', 2020), ('ABC123', 2010);

DECLARE @ErrorPatente INT = 0, @ErrorAnio INT = 0, @ErrorDuplicada INT = 0;
BEGIN TRY INSERT INTO academia.Vehiculo (Patente, Anio) VALUES ('1234567', 2020); END TRY
BEGIN CATCH SET @ErrorPatente = ERROR_NUMBER(); END CATCH;
BEGIN TRY INSERT INTO academia.Vehiculo (Patente, Anio) VALUES ('ZZ999YY', 1800); END TRY
BEGIN CATCH SET @ErrorAnio = ERROR_NUMBER(); END CATCH;
BEGIN TRY INSERT INTO academia.Vehiculo (Patente, Anio) VALUES ('AB123CD', 2021); END TRY
BEGIN CATCH SET @ErrorDuplicada = ERROR_NUMBER(); END CATCH;

SELECT
    (SELECT COUNT(*) FROM academia.Vehiculo)                           AS Filas,
    (SELECT MIN(Estado) FROM academia.Vehiculo)                        AS EstadoPorDefecto,
    @ErrorPatente AS ErrorPatente, @ErrorAnio AS ErrorAnio, @ErrorDuplicada AS ErrorDuplicada;
```

**Resultado esperado.**

| Filas | EstadoPorDefecto | ErrorPatente | ErrorAnio | ErrorDuplicada |
|---:|---|---:|---:|---:|
| 2 | activo | 547 | 547 | 2627 |

El 547 es una violación de `CHECK` y el 2627, de `UNIQUE`.

## NULL y lógica de tres valores

`NULL` representa un dato ausente, desconocido o no aplicable. Una comparación con `NULL` no da verdadero ni falso:
da **`UNKNOWN`**. `NULL = NULL` es `UNKNOWN`, y un `WHERE` solo conserva las filas cuya condición es verdadera.

| Comportamiento | Detalle |
|----------------|---------|
| `NULL = NULL` | `UNKNOWN` (no verdadero). Se compara con `IS NULL` / `IS NOT NULL` |
| `COUNT(columna)` | No cuenta los `NULL`; `COUNT(*)` sí cuenta las filas |
| `AVG(columna)` | Ignora los `NULL` |
| Concatenación | `'Hola ' + NULL` da `NULL` (con `CONCAT` el `NULL` se trata como cadena vacía) |
| `INNER JOIN` | Las filas con `NULL` en la columna de unión no aparecen |
| `UNIQUE` | En SQL Server, un solo `NULL` |

<!-- check: U1.T.RS.06 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL,
    Email    VARCHAR(100) NULL CONSTRAINT UQ_Alumno_Email UNIQUE,
    Nota     INT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre, Email, Nota) VALUES
    (1, 'Ana',  'ana@ejemplo.test', 8),
    (2, 'Beto', NULL,               NULL),
    (3, 'Cora', 'cora@ejemplo.test', 6);

DECLARE @A INT = NULL, @B INT = NULL, @ErrorUnique INT = 0;
BEGIN TRY
    INSERT INTO academia.Alumno (AlumnoId, Nombre, Email, Nota) VALUES (4, 'Dani', NULL, 5);
END TRY
BEGIN CATCH
    SET @ErrorUnique = ERROR_NUMBER();
END CATCH;

SELECT
    CASE WHEN @A = @B THEN 'VERDADERO'
         WHEN NOT (@A = @B) THEN 'FALSO'
         ELSE 'UNKNOWN' END                                          AS NullIgualNull,
    CASE WHEN @A IS NULL AND @B IS NULL THEN 'VERDADERO' ELSE 'FALSO' END AS IsNull,
    COUNT(*)                                                         AS CuentaFilas,
    COUNT(Nota)                                                      AS CuentaNota,
    AVG(Nota)                                                        AS PromedioNota,
    (SELECT ISNULL('Hola ' + Email, 'NULL') FROM academia.Alumno WHERE AlumnoId = 2) AS ConcatenarNull,
    @ErrorUnique                                                     AS ErrorSegundoNull
FROM academia.Alumno;
```

**Resultado esperado.**

| NullIgualNull | IsNull | CuentaFilas | CuentaNota | PromedioNota | ConcatenarNull | ErrorSegundoNull |
|---|---|---:|---:|---:|---|---:|
| UNKNOWN | VERDADERO | 3 | 2 | 7 | NULL | 2627 |

El promedio es 7 porque suma 8 y 6 y divide por 2, no por 3.

### NOT IN con NULL

Si la subconsulta de un `NOT IN` devuelve aunque sea un `NULL`, el resultado es vacío. Para cada fila, `x NOT IN (1, NULL)`
equivale a `x <> 1 AND x <> NULL`, y la segunda parte es `UNKNOWN`, por lo que la conjunción nunca es verdadera.

<!-- check: U1.T.RS.07 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL
);
CREATE TABLE academia.Inscripcion (
    InscripcionId INT NOT NULL CONSTRAINT PK_Inscripcion PRIMARY KEY,
    AlumnoId      INT NULL,
    Materia       VARCHAR(30) NOT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre) VALUES (1, 'Ana'), (2, 'Beto'), (3, 'Cora');
INSERT INTO academia.Inscripcion (InscripcionId, AlumnoId, Materia) VALUES
    (1, 1,    'Bases de Datos'),
    (2, NULL, 'Redes');

SELECT 'NOT IN' AS Forma, COUNT(*) AS AlumnosSinInscripcion
FROM academia.Alumno
WHERE AlumnoId NOT IN (SELECT AlumnoId FROM academia.Inscripcion)
UNION ALL
SELECT 'NOT EXISTS', COUNT(*)
FROM academia.Alumno AS a
WHERE NOT EXISTS (SELECT 1 FROM academia.Inscripcion AS i WHERE i.AlumnoId = a.AlumnoId)
UNION ALL
SELECT 'NOT IN con filtro IS NOT NULL', COUNT(*)
FROM academia.Alumno
WHERE AlumnoId NOT IN (SELECT AlumnoId FROM academia.Inscripcion WHERE AlumnoId IS NOT NULL);
```

**Resultado esperado.**

| Forma | AlumnosSinInscripcion |
|---|---:|
| NOT IN | 0 |
| NOT EXISTS | 2 |
| NOT IN con filtro IS NOT NULL | 2 |

:::caution[Errores frecuentes]
Usar `NOT IN` sobre una columna que admite `NULL` devuelve **cero filas** sin dar error, como en la primera fila del
resultado. Preferí `NOT EXISTS`, o filtrá `IS NOT NULL` dentro de la subconsulta. Y nunca escribas `= NULL`: usá `IS NULL`.
:::

### ISNULL, COALESCE y NULLIF

| | `ISNULL` | `COALESCE` |
|---|---|---|
| Estándar | Propio de SQL Server | ANSI SQL |
| Parámetros | Exactamente 2 | 2 o más |
| Tipo de retorno | El del **primer** parámetro | El de mayor precedencia entre los argumentos |

`NULLIF(a, b)` devuelve `NULL` si `a = b` y `a` en otro caso; sirve para evitar divisiones por cero.

<!-- check: U1.T.RS.08 -->
```sql
DECLARE @Valor CHAR(3) = NULL;
DECLARE @Total INT = 10, @Cantidad INT = 0;

SELECT
    ISNULL(@Valor, 'valor por defecto')                        AS ConIsnull,
    COALESCE(@Valor, 'valor por defecto')                      AS ConCoalesce,
    COALESCE(NULL, NULL, 'tercero')                            AS PrimerNoNulo,
    @Total / NULLIF(@Cantidad, 0)                              AS DivisionSegura,
    ISNULL(@Total / NULLIF(@Cantidad, 0), -1)                  AS DivisionConDefecto;
```

**Resultado esperado.**

| ConIsnull | ConCoalesce | PrimerNoNulo | DivisionSegura | DivisionConDefecto |
|---|---|---|---|---:|
| val | valor por defecto | tercero | NULL | -1 |

`ISNULL` truncó el reemplazo al tipo `CHAR(3)` de la variable; `COALESCE` no. Preferí `COALESCE` por ser estándar y
más predecible con los tipos.

## Consultas básicas, JOIN y UNION

<!-- sintaxis -->
```sql
SELECT Columna1, Columna2
FROM   esquema.Tabla
WHERE  Condicion
ORDER BY Columna1 ASC;
```

Conceptualmente una consulta se evalúa así: `FROM` (con los `JOIN`), `WHERE`, `GROUP BY`, `HAVING`, `SELECT` y
`ORDER BY`. En realidad el optimizador reordena y paraleliza todo lo posible: SQL es declarativo, indicás *qué*
querés y el motor decide *cómo*. Los planes de ejecución se ven en la [Unidad 3](/bbdd-aplicadas/unidad-3/teoria/indices-y-planes/).

![join-types](/bbdd-aplicadas/unidad-1/images/joins.png)

<!-- check: U1.T.RS.09 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL
);
CREATE TABLE academia.Inscripcion (
    InscripcionId INT NOT NULL CONSTRAINT PK_Inscripcion PRIMARY KEY,
    AlumnoId      INT NOT NULL CONSTRAINT FK_Inscripcion_Alumno REFERENCES academia.Alumno (AlumnoId),
    Materia       VARCHAR(30) NOT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre) VALUES (1, 'Ana'), (2, 'Beto'), (3, 'Cora');
INSERT INTO academia.Inscripcion (InscripcionId, AlumnoId, Materia) VALUES
    (1, 1, 'Bases de Datos'), (2, 1, 'Redes'), (3, 2, 'Bases de Datos');

SELECT a.Nombre, i.Materia, 'INNER' AS Tipo
FROM academia.Alumno AS a
INNER JOIN academia.Inscripcion AS i ON i.AlumnoId = a.AlumnoId
UNION ALL
SELECT a.Nombre, ISNULL(i.Materia, '(sin materia)'), 'LEFT'
FROM academia.Alumno AS a
LEFT JOIN academia.Inscripcion AS i ON i.AlumnoId = a.AlumnoId
WHERE a.AlumnoId = 3
UNION ALL
SELECT a.Nombre, '(anti-join)', 'ANTI'
FROM academia.Alumno AS a
LEFT JOIN academia.Inscripcion AS i ON i.AlumnoId = a.AlumnoId
WHERE i.AlumnoId IS NULL
ORDER BY Tipo, Nombre, Materia;
```

**Resultado esperado.**

| Nombre | Materia | Tipo |
|---|---|---|
| Cora | (anti-join) | ANTI |
| Ana | Bases de Datos | INNER |
| Ana | Redes | INNER |
| Beto | Bases de Datos | INNER |
| Cora | (sin materia) | LEFT |

`LEFT JOIN ... WHERE columna_derecha IS NULL` es el **anti-join**: las filas de la izquierda sin pareja.

- `CROSS JOIN` es el producto cartesiano: todas las combinaciones.
- Un `SELF JOIN` une una tabla consigo misma con alias distintos (por ejemplo, empleado y jefe).
- `UNION` combina resultados y elimina duplicados; `UNION ALL` los conserva y es más rápido.

<!-- check: U1.T.RS.10 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Empleado (
    EmpleadoId INT NOT NULL CONSTRAINT PK_Empleado PRIMARY KEY,
    Nombre     VARCHAR(30) NOT NULL,
    JefeId     INT NULL CONSTRAINT FK_Empleado_Jefe REFERENCES academia.Empleado (EmpleadoId)
);
CREATE TABLE academia.Turno (Nombre VARCHAR(10) NOT NULL);
CREATE TABLE academia.Dia   (Nombre VARCHAR(10) NOT NULL);
INSERT INTO academia.Empleado (EmpleadoId, Nombre, JefeId) VALUES (1, 'Direccion', NULL), (2, 'Ana', 1), (3, 'Beto', 1), (4, 'Cora', 2);
INSERT INTO academia.Turno (Nombre) VALUES ('Mañana'), ('Noche');
INSERT INTO academia.Dia (Nombre) VALUES ('Lunes'), ('Martes'), ('Jueves');

SELECT 'CROSS' AS Consulta, CAST(COUNT(*) AS VARCHAR(10)) AS Resultado
FROM academia.Dia AS d CROSS JOIN academia.Turno AS t
UNION ALL
SELECT 'SELF', STRING_AGG(e.Nombre + ' -> ' + j.Nombre, '; ') WITHIN GROUP (ORDER BY e.EmpleadoId)
FROM academia.Empleado AS e
INNER JOIN academia.Empleado AS j ON j.EmpleadoId = e.JefeId
UNION ALL
SELECT 'UNION', CAST(COUNT(*) AS VARCHAR(10))
FROM (SELECT Nombre FROM academia.Dia UNION SELECT 'Lunes') AS u
UNION ALL
SELECT 'UNION ALL', CAST(COUNT(*) AS VARCHAR(10))
FROM (SELECT Nombre FROM academia.Dia UNION ALL SELECT 'Lunes') AS u;
```

**Resultado esperado.**

| Consulta | Resultado |
|---|---|
| CROSS | 6 |
| SELF | Ana -> Direccion; Beto -> Direccion; Cora -> Ana |
| UNION | 3 |
| UNION ALL | 4 |

## Subconsultas

Una subconsulta es un `SELECT` anidado en otra sentencia. Puede aparecer en el `WHERE`, en el `FROM` (tabla
derivada) y en el `SELECT` (debe devolver un único valor), y también en `UPDATE` y `DELETE`. Es **correlacionada**
si referencia columnas de la consulta externa: se evalúa, conceptualmente, una vez por fila externa.

<!-- check: U1.T.RS.11 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL
);
CREATE TABLE academia.Examen (
    ExamenId INT NOT NULL CONSTRAINT PK_Examen PRIMARY KEY,
    AlumnoId INT NOT NULL CONSTRAINT FK_Examen_Alumno REFERENCES academia.Alumno (AlumnoId),
    Nota     INT NOT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre) VALUES (1, 'Ana'), (2, 'Beto'), (3, 'Cora');
INSERT INTO academia.Examen (ExamenId, AlumnoId, Nota) VALUES
    (1, 1, 9), (2, 1, 7), (3, 2, 4), (4, 2, 6);

-- En WHERE (no correlacionada): alumnos con algún examen de nota mayor a 8.
-- En FROM (tabla derivada): promedio por alumno.
-- En SELECT (correlacionada): mejor nota de cada alumno.
SELECT
    a.Nombre,
    p.Promedio,
    (SELECT MAX(e.Nota) FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId) AS MejorNota,
    CASE WHEN a.AlumnoId IN (SELECT AlumnoId FROM academia.Examen WHERE Nota > 8)
         THEN 'Si' ELSE 'No' END AS TieneMasDeOcho
FROM academia.Alumno AS a
LEFT JOIN (
    SELECT AlumnoId, CAST(AVG(CAST(Nota AS DECIMAL(4,1))) AS DECIMAL(4,1)) AS Promedio
    FROM academia.Examen
    GROUP BY AlumnoId
) AS p ON p.AlumnoId = a.AlumnoId
ORDER BY a.Nombre;
```

**Resultado esperado.**

| Nombre | Promedio | MejorNota | TieneMasDeOcho |
|---|---:|---:|---|
| Ana | 8.0 | 9 | Si |
| Beto | 5.0 | 6 | No |
| Cora | NULL | NULL | No |

`EXISTS` es verdadero si la subconsulta devuelve al menos una fila (no importa qué selecciona). `x < ANY (...)` es
verdadero si se cumple para algún valor; `x > ALL (...)` si se cumple para todos.

<!-- check: U1.T.RS.12 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(50) NOT NULL
);
CREATE TABLE academia.Examen (
    ExamenId INT NOT NULL CONSTRAINT PK_Examen PRIMARY KEY,
    AlumnoId INT NOT NULL CONSTRAINT FK_Examen_Alumno REFERENCES academia.Alumno (AlumnoId),
    Nota     INT NOT NULL
);
INSERT INTO academia.Alumno (AlumnoId, Nombre) VALUES (1, 'Ana'), (2, 'Beto'), (3, 'Cora');
INSERT INTO academia.Examen (ExamenId, AlumnoId, Nota) VALUES
    (1, 1, 9), (2, 1, 7), (3, 2, 4), (4, 2, 6);

SELECT 'EXISTS' AS Consulta, a.Nombre
FROM academia.Alumno AS a
WHERE EXISTS (SELECT 1 FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId)
UNION ALL
SELECT 'NOT EXISTS', a.Nombre
FROM academia.Alumno AS a
WHERE NOT EXISTS (SELECT 1 FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId)
UNION ALL
SELECT 'ANY (algun examen mayor a 8)', a.Nombre
FROM academia.Alumno AS a
WHERE 8 < ANY (SELECT e.Nota FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId)
UNION ALL
SELECT 'ALL (todos los examenes menores a 7)', a.Nombre
FROM academia.Alumno AS a
WHERE 7 > ALL (SELECT e.Nota FROM academia.Examen AS e WHERE e.AlumnoId = a.AlumnoId)
ORDER BY Consulta, Nombre;
```

**Resultado esperado.**

| Consulta | Nombre |
|---|---|
| ALL (todos los examenes menores a 7) | Beto |
| ALL (todos los examenes menores a 7) | Cora |
| ANY (algun examen mayor a 8) | Ana |
| EXISTS | Ana |
| EXISTS | Beto |
| NOT EXISTS | Cora |

:::caution[Errores frecuentes]
Cora aparece en el `ALL` aunque no rindió ningún examen: `ALL` sobre un conjunto vacío es verdadero. Si ese no es el
resultado buscado, agregá `AND EXISTS (...)`.
:::

## Funciones de agregado

Las funciones de agregado resumen un grupo de filas en un valor: `COUNT`, `SUM`, `AVG`, `MIN` y `MAX`. Se indica el criterio de agrupado con
`GROUP BY`. `COUNT` devuelve un entero; las demás respetan el tipo de la columna (el `AVG` de un `INT` es entero).
`WHERE` filtra filas **antes** de agrupar; `HAVING` filtra grupos **después** de agregar. `COUNT(DISTINCT col)`
cuenta valores distintos.

<!-- check: U1.T.RS.13 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Curso (
    CursoId      INT NOT NULL CONSTRAINT PK_Curso PRIMARY KEY,
    Catedra      VARCHAR(30) NOT NULL,
    Turno        VARCHAR(10) NOT NULL,
    Inscriptos   INT NULL,
    Puntuacion   INT NOT NULL
);
INSERT INTO academia.Curso (CursoId, Catedra, Turno, Inscriptos, Puntuacion) VALUES
    (1, 'Bases de Datos', 'Mañana', 40, 4),
    (2, 'Bases de Datos', 'Noche',  60, 5),
    (3, 'Redes',          'Noche',  30, 2),
    (4, 'Redes',          'Mañana', NULL, 4),
    (5, 'Sistemas',       'Mañana', 50, 5);

SELECT
    Catedra,
    COUNT(*)                AS Cursos,
    COUNT(Inscriptos)       AS ConDato,
    COUNT(DISTINCT Turno)   AS Turnos,
    SUM(Inscriptos)         AS TotalInscriptos,
    AVG(Inscriptos)         AS Promedio
FROM academia.Curso
WHERE Puntuacion > 3
GROUP BY Catedra
HAVING SUM(Inscriptos) > 40
ORDER BY Catedra;
```

**Resultado esperado.**

| Catedra | Cursos | ConDato | Turnos | TotalInscriptos | Promedio |
|---|---:|---:|---:|---:|---:|
| Bases de Datos | 2 | 2 | 2 | 100 | 50 |
| Sistemas | 1 | 1 | 1 | 50 | 50 |

Redes quedó afuera por dos motivos: su curso con 2 puntos no pasó el `WHERE` y el otro tiene `NULL`, con lo que su
suma es `NULL` y no cumple el `HAVING`.

## Vistas

Una vista es una tabla virtual: guarda solo su consulta, no datos. Se usa para simplificar consultas, limitar el
acceso a columnas o filas y mantener la compatibilidad cuando cambia la estructura de las tablas.

**¿Qué DML admite?** Una vista admite `INSERT`, `UPDATE` y `DELETE` si cada fila de la vista se corresponde con una
fila de una tabla base. Puede estar definida sobre **varias tablas**, siempre que cada modificación afecte columnas
de **una sola** tabla base. No admiten DML las vistas con `GROUP BY`, `DISTINCT`, agregados o `UNION`, porque sus filas
son derivadas.

<!-- check: U1.T.RS.14 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Departamento (
    DepartamentoId INT NOT NULL CONSTRAINT PK_Departamento PRIMARY KEY,
    Nombre         VARCHAR(30) NOT NULL
);
CREATE TABLE academia.Empleado (
    EmpleadoId     INT NOT NULL CONSTRAINT PK_Empleado PRIMARY KEY,
    Nombre         VARCHAR(30) NOT NULL,
    DepartamentoId INT NOT NULL CONSTRAINT FK_Empleado_Departamento REFERENCES academia.Departamento (DepartamentoId),
    Sueldo         DECIMAL(10,2) NOT NULL
);
INSERT INTO academia.Departamento VALUES (1, 'Sistemas'), (2, 'Ventas');
INSERT INTO academia.Empleado VALUES (1, 'Ana', 1, 1000), (2, 'Beto', 2, 800);
GO
CREATE VIEW academia.EmpleadoDetalle
AS
    SELECT e.EmpleadoId, e.Nombre, d.Nombre AS Departamento, e.Sueldo
    FROM academia.Empleado AS e
    INNER JOIN academia.Departamento AS d ON d.DepartamentoId = e.DepartamentoId;
GO
CREATE VIEW academia.SueldoPorDepartamento
AS
    SELECT DepartamentoId, SUM(Sueldo) AS Total
    FROM academia.Empleado
    GROUP BY DepartamentoId;
GO
DECLARE @ErrorDosTablas INT = 0, @ErrorAgregado INT = 0;

-- Actualizar columnas de UNA sola tabla base a traves de una vista de varias tablas: permitido.
UPDATE academia.EmpleadoDetalle SET Sueldo = 1100 WHERE EmpleadoId = 1;

-- Un UPDATE que toca columnas de dos tablas base a la vez: rechazado.
BEGIN TRY
    EXEC (N'UPDATE academia.EmpleadoDetalle SET Sueldo = 900, Departamento = ''Soporte'' WHERE EmpleadoId = 2;');
END TRY
BEGIN CATCH
    SET @ErrorDosTablas = ERROR_NUMBER();
END CATCH;

-- Vista con GROUP BY: no admite UPDATE.
BEGIN TRY
    EXEC (N'UPDATE academia.SueldoPorDepartamento SET Total = 0 WHERE DepartamentoId = 1;');
END TRY
BEGIN CATCH
    SET @ErrorAgregado = ERROR_NUMBER();
END CATCH;

SELECT
    (SELECT Sueldo FROM academia.Empleado WHERE EmpleadoId = 1) AS SueldoAna,
    @ErrorDosTablas AS ErrorDosTablas,
    @ErrorAgregado  AS ErrorAgregado;
```

**Resultado esperado.**

| SueldoAna | ErrorDosTablas | ErrorAgregado |
|---:|---:|---:|
| 1100.00 | 4405 | 4406 |

:::note[Por qué usamos EXEC]
Esos dos errores se producen al compilar la sentencia, y `TRY...CATCH` no captura errores de compilación del propio
lote. Por eso la sentencia se ejecuta como cadena con `EXEC`, solo para poder mostrar el número de error.
:::

`WITH SCHEMABINDING` vincula la vista a las tablas: el motor impide cambios (quitar una columna, borrar la tabla)
que la dejarían inválida. Exige nombres de dos partes, y una vista con `GROUP BY` e índice debe incluir `COUNT_BIG(*)`.

<!-- check: U1.T.RS.15 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Curso (
    CursoId    INT NOT NULL CONSTRAINT PK_Curso PRIMARY KEY,
    Catedra    VARCHAR(30) NOT NULL,
    Inscriptos INT NOT NULL,
    Puntuacion INT NOT NULL
);
INSERT INTO academia.Curso VALUES (1, 'Bases de Datos', 40, 4), (2, 'Bases de Datos', 60, 5), (3, 'Redes', 30, 2);
GO
CREATE OR ALTER VIEW academia.CursoDestacado
WITH SCHEMABINDING
AS
    SELECT Catedra, SUM(Inscriptos) AS TotalInscriptos, COUNT_BIG(*) AS Cursos
    FROM academia.Curso
    WHERE Puntuacion > 3
    GROUP BY Catedra;
GO
DECLARE @ErrorAlter INT = 0, @ErrorDrop INT = 0;
BEGIN TRY
    ALTER TABLE academia.Curso DROP COLUMN Inscriptos;
END TRY
BEGIN CATCH
    SET @ErrorAlter = ERROR_NUMBER();
END CATCH;
BEGIN TRY
    DROP TABLE academia.Curso;
END TRY
BEGIN CATCH
    SET @ErrorDrop = ERROR_NUMBER();
END CATCH;

SELECT Catedra, TotalInscriptos, @ErrorAlter AS ErrorAlterColumna, @ErrorDrop AS ErrorDropTabla
FROM academia.CursoDestacado;
```

**Resultado esperado.**

| Catedra | TotalInscriptos | ErrorAlterColumna | ErrorDropTabla |
|---|---:|---:|---:|
| Bases de Datos | 100 | 4922 | 3729 |

## Procedimientos almacenados

Un procedimiento es un módulo de programa almacenado en la base y ejecutado por el motor. Normaliza el acceso a
datos desde distintas aplicaciones, reduce el tráfico cliente-servidor, admite parámetros de entrada y salida
(`OUTPUT`) y permite dar permiso al procedimiento en lugar de a las tablas. En SQL Server se compila y se guarda su
plan en caché la primera vez que se ejecuta, no al crearlo.

<!-- check: U1.T.RS.16 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre   VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL
);
CREATE TABLE academia.Materia (
    MateriaId INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Materia PRIMARY KEY,
    Nombre    VARCHAR(100) NOT NULL,
    Codigo    VARCHAR(20)  NOT NULL
);
CREATE TABLE academia.Inscripcion (
    InscripcionId    INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Inscripcion PRIMARY KEY,
    AlumnoId         INT  NOT NULL CONSTRAINT FK_Inscripcion_Alumno REFERENCES academia.Alumno (AlumnoId),
    MateriaId        INT  NOT NULL CONSTRAINT FK_Inscripcion_Materia REFERENCES academia.Materia (MateriaId),
    FechaInscripcion DATE NOT NULL,
    CONSTRAINT UQ_Inscripcion_Alumno_Materia UNIQUE (AlumnoId, MateriaId)
);
INSERT INTO academia.Alumno (Nombre, Apellido) VALUES ('Ana', 'Prueba');
INSERT INTO academia.Materia (Nombre, Codigo) VALUES ('Bases de Datos', 'BD01');
GO
CREATE OR ALTER PROCEDURE academia.InscribirAlumno
    @AlumnoId  INT,
    @MateriaId INT,
    @Resultado INT = 0 OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM academia.Alumno WHERE AlumnoId = @AlumnoId)
        SET @Resultado = -1;          -- el alumno no existe
    ELSE IF EXISTS (SELECT 1 FROM academia.Inscripcion
                    WHERE AlumnoId = @AlumnoId AND MateriaId = @MateriaId)
        SET @Resultado = -2;          -- ya estaba inscripto
    ELSE
    BEGIN
        INSERT INTO academia.Inscripcion (AlumnoId, MateriaId, FechaInscripcion)
        VALUES (@AlumnoId, @MateriaId, CAST(GETDATE() AS DATE));
        SET @Resultado = 1;
    END;
END;
GO
DECLARE @R1 INT, @R2 INT, @R3 INT;
EXEC academia.InscribirAlumno @AlumnoId = 1,  @MateriaId = 1, @Resultado = @R1 OUTPUT;
EXEC academia.InscribirAlumno @AlumnoId = 1,  @MateriaId = 1, @Resultado = @R2 OUTPUT;
EXEC academia.InscribirAlumno @AlumnoId = 99, @MateriaId = 1, @Resultado = @R3 OUTPUT;

SELECT
    @R1 AS PrimeraVez,
    @R2 AS Repetida,
    @R3 AS AlumnoInexistente,
    (SELECT COUNT(*) FROM academia.Inscripcion) AS Inscripciones;
```

**Resultado esperado.**

| PrimeraVez | Repetida | AlumnoInexistente | Inscripciones |
|---:|---:|---:|---:|
| 1 | -2 | -1 | 1 |

`SET NOCOUNT ON` suprime los mensajes de filas afectadas. Los códigos de retorno (1, -1, -2) son una convención propia
de este ejemplo.

## Triggers

Un trigger es un procedimiento especial que el motor ejecuta automáticamente ante un evento DML (`INSERT`,
`UPDATE`, `DELETE`) o DDL. No recibe parámetros: dentro de él existen las pseudotablas `inserted` (filas nuevas) y
`deleted` (filas viejas). En un `UPDATE`, `deleted` tiene los valores previos e `inserted` los nuevos. SQL Server
dispara un trigger **por sentencia**, no por fila (no tiene `FOR EACH ROW`), de modo que siempre hay que escribirlo
para varias filas.

| Momento | Descripción |
|---------|-------------|
| `AFTER` (o `FOR`) | Se ejecuta después de aplicar la operación |
| `INSTEAD OF` | Reemplaza la operación original; es el único que admiten las vistas |

<!-- check: U1.T.RS.17 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Examen (
    ExamenId INT NOT NULL CONSTRAINT PK_Examen PRIMARY KEY,
    Alumno   VARCHAR(30) NOT NULL,
    Nota     INT NOT NULL
);
CREATE TABLE academia.ExamenAuditoria (
    AuditoriaId  INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_ExamenAuditoria PRIMARY KEY,
    ExamenId     INT NOT NULL,
    NotaAnterior INT NOT NULL,
    NotaNueva    INT NOT NULL,
    Fecha        DATETIME2(0) NOT NULL CONSTRAINT DF_ExamenAuditoria_Fecha DEFAULT (SYSDATETIME())
);
INSERT INTO academia.Examen (ExamenId, Alumno, Nota) VALUES (1, 'Ana', 6), (2, 'Beto', 4), (3, 'Cora', 8);
GO
CREATE OR ALTER TRIGGER academia.TrgExamenAuditoria
ON academia.Examen
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO academia.ExamenAuditoria (ExamenId, NotaAnterior, NotaNueva)
    SELECT i.ExamenId, d.Nota, i.Nota
    FROM inserted AS i
    INNER JOIN deleted AS d ON d.ExamenId = i.ExamenId
    WHERE i.Nota <> d.Nota;
END;
GO
UPDATE academia.Examen SET Nota = Nota + 1 WHERE ExamenId IN (1, 2);
UPDATE academia.Examen SET Alumno = 'Cora M.' WHERE ExamenId = 3;   -- no cambia la nota

SELECT ExamenId, NotaAnterior, NotaNueva
FROM academia.ExamenAuditoria
ORDER BY ExamenId;
```

**Resultado esperado.**

| ExamenId | NotaAnterior | NotaNueva |
|---:|---:|---:|
| 1 | 6 | 7 |
| 2 | 4 | 5 |

El segundo `UPDATE` cambia una columna distinta de `Nota` y no genera auditoría.

Un trigger `INSTEAD OF` permite hacer DML sobre una vista que no lo admitiría por sí sola:

<!-- check: U1.T.RS.18 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Departamento (
    DepartamentoId INT NOT NULL CONSTRAINT PK_Departamento PRIMARY KEY,
    Nombre         VARCHAR(30) NOT NULL
);
CREATE TABLE academia.Empleado (
    EmpleadoId     INT IDENTITY(1, 1) NOT NULL CONSTRAINT PK_Empleado PRIMARY KEY,
    Nombre         VARCHAR(30) NOT NULL,
    DepartamentoId INT NOT NULL CONSTRAINT FK_Empleado_Departamento REFERENCES academia.Departamento (DepartamentoId)
);
INSERT INTO academia.Departamento VALUES (1, 'Sistemas'), (2, 'Ventas');
GO
CREATE VIEW academia.EmpleadoDetalle
AS
    SELECT e.Nombre, d.Nombre AS Departamento
    FROM academia.Empleado AS e
    INNER JOIN academia.Departamento AS d ON d.DepartamentoId = e.DepartamentoId;
GO
CREATE TRIGGER academia.TrgEmpleadoDetalleInsert
ON academia.EmpleadoDetalle
INSTEAD OF INSERT
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO academia.Empleado (Nombre, DepartamentoId)
    SELECT i.Nombre, d.DepartamentoId
    FROM inserted AS i
    INNER JOIN academia.Departamento AS d ON d.Nombre = i.Departamento;
END;
GO
INSERT INTO academia.EmpleadoDetalle (Nombre, Departamento) VALUES ('Ana', 'Ventas'), ('Beto', 'Sistemas');

SELECT Nombre, Departamento
FROM academia.EmpleadoDetalle
ORDER BY Nombre;
```

**Resultado esperado.**

| Nombre | Departamento |
|---|---|
| Ana | Ventas |
| Beto | Sistemas |

Un **DDL trigger** actúa sobre la base de datos y sirve para auditar o impedir cambios estructurales:

<!-- check: U1.T.RS.19 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (AlumnoId INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY);
GO
CREATE TRIGGER TrgNoDropTable
ON DATABASE
FOR DROP_TABLE
AS
BEGIN
    PRINT 'No se permite eliminar tablas.';
    ROLLBACK;
END;
GO
DECLARE @Error INT = 0;
BEGIN TRY
    DROP TABLE academia.Alumno;
END TRY
BEGIN CATCH
    SET @Error = ERROR_NUMBER();
END CATCH;

SELECT
    @Error AS Error,
    CASE WHEN OBJECT_ID('academia.Alumno') IS NOT NULL THEN 'existe' ELSE 'eliminada' END AS Tabla;
GO
DROP TRIGGER TrgNoDropTable ON DATABASE;
```

**Resultado esperado.**

```text
No se permite eliminar tablas.
```

| Error | Tabla |
|---:|---|
| 3609 | existe |

El `ROLLBACK` deshizo el `DROP TABLE`; el 3609 indica que la transacción terminó dentro del trigger. El bloque termina eliminando el trigger con `DROP TRIGGER`: si lo interrumpís antes, ejecutá esa última sentencia a mano, porque mientras exista impide borrar tablas en esa base. También existe el
**logon trigger**, a nivel de instancia, que se dispara al iniciar sesión (por ejemplo, para limitar conexiones).

## Funciones de usuario

Una función retorna un valor, escalar o tabla, y se usa dentro de una consulta (`SELECT`, `FROM`, `WHERE`). Solo
tiene parámetros de entrada. Hay tres formas:

- **Escalar**: devuelve un único valor.
- **De tabla *inline***: un único `SELECT` que se comporta como una vista con parámetros. Suele ser la más eficiente.
- **De tabla *multi-statement***: declara una tabla de retorno y la llena con varias sentencias.

<!-- check: U1.T.RS.20 -->
```sql
CREATE SCHEMA academia;
GO
CREATE TABLE academia.Alumno (
    AlumnoId        INT NOT NULL CONSTRAINT PK_Alumno PRIMARY KEY,
    Nombre          VARCHAR(30) NOT NULL,
    FechaNacimiento DATE NOT NULL
);
CREATE TABLE academia.Examen (
    ExamenId INT NOT NULL CONSTRAINT PK_Examen PRIMARY KEY,
    AlumnoId INT NOT NULL CONSTRAINT FK_Examen_Alumno REFERENCES academia.Alumno (AlumnoId),
    Nota     INT NOT NULL
);
INSERT INTO academia.Alumno VALUES (1, 'Ana', '2000-05-20'), (2, 'Beto', '1999-12-31');
INSERT INTO academia.Examen VALUES (1, 1, 9), (2, 1, 7), (3, 2, 4);
GO
-- Escalar
CREATE OR ALTER FUNCTION academia.ObtenerEdad (@FechaNacimiento DATE, @FechaReferencia DATE)
RETURNS INT
AS
BEGIN
    RETURN DATEDIFF(YEAR, @FechaNacimiento, @FechaReferencia)
         - CASE WHEN MONTH(@FechaNacimiento) * 100 + DAY(@FechaNacimiento)
                     > MONTH(@FechaReferencia) * 100 + DAY(@FechaReferencia)
                THEN 1 ELSE 0 END;
END;
GO
-- De tabla inline: un único SELECT
CREATE OR ALTER FUNCTION academia.ExamenPorAlumno (@AlumnoId INT)
RETURNS TABLE
AS
RETURN
    SELECT ExamenId, Nota
    FROM academia.Examen
    WHERE AlumnoId = @AlumnoId;
GO
-- De tabla multi-statement: declara la tabla de retorno y la llena con varias sentencias
CREATE OR ALTER FUNCTION academia.ResumenAlumno (@AlumnoId INT)
RETURNS @Resumen TABLE (Nombre VARCHAR(30), Examenes INT, Promedio DECIMAL(4,1))
AS
BEGIN
    INSERT INTO @Resumen (Nombre, Examenes, Promedio)
    SELECT a.Nombre, COUNT(e.ExamenId), CAST(AVG(CAST(e.Nota AS DECIMAL(4,1))) AS DECIMAL(4,1))
    FROM academia.Alumno AS a
    LEFT JOIN academia.Examen AS e ON e.AlumnoId = a.AlumnoId
    WHERE a.AlumnoId = @AlumnoId
    GROUP BY a.Nombre;
    RETURN;
END;
GO
SELECT
    a.Nombre,
    academia.ObtenerEdad(a.FechaNacimiento, '2026-03-01') AS Edad,
    r.Examenes,
    r.Promedio,
    (SELECT MAX(x.Nota) FROM academia.ExamenPorAlumno(a.AlumnoId) AS x) AS MejorNota
FROM academia.Alumno AS a
CROSS APPLY academia.ResumenAlumno(a.AlumnoId) AS r
ORDER BY a.Nombre;
```

**Resultado esperado.**

| Nombre | Edad | Examenes | Promedio | MejorNota |
|---|---:|---:|---:|---:|
| Ana | 25 | 2 | 8.0 | 9 |
| Beto | 26 | 1 | 4.0 | 4 |

La edad recibe la fecha de referencia como parámetro en lugar de usar `GETDATE()`, para que el resultado sea
reproducible.

| | Función | Procedimiento |
|---|---------|---------------|
| Salida | Valor de retorno (escalar o tabla) | Parámetros `OUTPUT` y conjuntos de resultados |
| Se usa en `SELECT`, `FROM` o `WHERE` | Sí | No (se invoca con `EXEC`) |
| Modifica datos permanentes | No: no puede modificar tablas permanentes | Sí |

## Resumen de objetos de una base

| Objeto | Para qué sirve |
|--------|----------------|
| **Tabla** | Almacena datos persistentes |
| **Vista** | Consulta con nombre (tabla virtual) |
| **Procedimiento** | Lógica ejecutable en el servidor, con parámetros |
| **Función** | Retorna un valor o una tabla y se usa dentro de consultas |
| **Trigger** | Se dispara ante eventos DML o DDL |
| **Índice** | Acelera búsquedas; el clúster define el orden físico |
| **Restricción** | Regla de integridad (PK, FK, `UNIQUE`, `CHECK`, `DEFAULT`) |

## Temas con guía propia

| Tema | Guía |
|------|------|
| Window functions | [Window Functions](/bbdd-aplicadas/unidad-1/teoria/window-functions/) |
| Common Table Expressions | [CTE](/bbdd-aplicadas/unidad-1/teoria/cte/) |
| SQL dinámico | [SQL Dinámico](/bbdd-aplicadas/unidad-1/teoria/sql-dinamico/) |
| PIVOT y UNPIVOT | [PIVOT](/bbdd-aplicadas/unidad-1/teoria/pivot/) |
| Índice clúster | [Índice Clustered](/bbdd-aplicadas/unidad-1/teoria/indice-cluster/) |

## Autoevaluación

<details>
<summary>1. ¿Por qué <code>WHERE x NOT IN (SELECT y FROM t)</code> puede devolver cero filas aunque haya datos que cumplen?</summary>

Porque si `y` contiene un `NULL`, la comparación de `x` con ese `NULL` es `UNKNOWN` y la conjunción de todas las
comparaciones nunca es verdadera. Se resuelve con `NOT EXISTS` o filtrando `IS NOT NULL` en la subconsulta.
</details>

<details>
<summary>2. ¿Qué pasa con las filas hijas al borrar una fila padre con cada acción referencial?</summary>

`NO ACTION` rechaza el borrado; `CASCADE` borra las hijas; `SET NULL` pone `NULL` en la FK; `SET DEFAULT` pone el valor
por defecto, que debe existir en la tabla padre.
</details>

<details>
<summary>3. ¿Se puede hacer <code>UPDATE</code> sobre una vista que une dos tablas?</summary>

Sí, mientras la modificación afecte columnas de una sola tabla base. Si toca columnas de ambas, el motor la rechaza.
Con `GROUP BY` o agregados, no se puede modificar.
</details>

<details>
<summary>4. ¿Qué diferencia hay entre una función de tabla inline y una multi-statement?</summary>

La inline es un único `SELECT` que el optimizador expande como una vista; la multi-statement declara una tabla de
retorno y la llena con varias sentencias, lo que da menos información al optimizador.
</details>

## En resumen

:::tip[En resumen]
- Las restricciones implícitas y explícitas las aplica el motor; las semánticas, la aplicación.
- Elegí tipos acordes: `DATETIME2` para fecha y hora, `VARCHAR`/`NVARCHAR` según el idioma, `DECIMAL` para dinero.
- `NULL` introduce lógica de tres valores: `NULL = NULL` es `UNKNOWN`; evitá `NOT IN` con columnas nulas.
- Las acciones referenciales (`NO ACTION`, `CASCADE`, `SET NULL`, `SET DEFAULT`) definen qué pasa con las hijas.
- Una subconsulta puede ir en `WHERE`, `FROM` y `SELECT`; `EXISTS` suele ser la forma más segura.
- Las vistas admiten DML si cada modificación afecta una sola tabla base; los triggers usan `inserted` y `deleted`.
- Las funciones se usan dentro de consultas; los procedimientos, con `EXEC`.
:::

:::tip[Para seguir]
Practicá con el [Trabajo Práctico 1 — Repaso de SQL](/bbdd-aplicadas/unidad-1/practica/tp1/) y después seguí con [Window Functions](/bbdd-aplicadas/unidad-1/teoria/window-functions/).
:::

## Fuentes

- Presentación de cátedra, Unidad 1, parte 2: Repaso de SQL (v1.1.0, 2025).
- Microsoft Learn, [Tipos de datos (Transact-SQL)](https://learn.microsoft.com/es-es/sql/t-sql/data-types/data-types-transact-sql).
- Microsoft Learn, [CREATE TABLE](https://learn.microsoft.com/es-es/sql/t-sql/statements/create-table-transact-sql) y
  [Restricciones de clave externa](https://learn.microsoft.com/es-es/sql/relational-databases/tables/create-foreign-key-relationships).
- Microsoft Learn, [NULL y UNKNOWN](https://learn.microsoft.com/es-es/sql/t-sql/language-elements/null-and-unknown-transact-sql),
  [COALESCE](https://learn.microsoft.com/es-es/sql/t-sql/language-elements/coalesce-transact-sql) y
  [NULLIF](https://learn.microsoft.com/es-es/sql/t-sql/language-elements/nullif-transact-sql).
- Microsoft Learn, [Subconsultas](https://learn.microsoft.com/es-es/sql/relational-databases/performance/subqueries),
  [CREATE VIEW](https://learn.microsoft.com/es-es/sql/t-sql/statements/create-view-transact-sql),
  [CREATE PROCEDURE](https://learn.microsoft.com/es-es/sql/t-sql/statements/create-procedure-transact-sql),
  [CREATE TRIGGER](https://learn.microsoft.com/es-es/sql/t-sql/statements/create-trigger-transact-sql) y
  [CREATE FUNCTION](https://learn.microsoft.com/es-es/sql/t-sql/statements/create-function-transact-sql).
