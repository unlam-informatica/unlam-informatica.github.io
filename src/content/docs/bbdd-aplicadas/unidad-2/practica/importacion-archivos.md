---
title: Práctica — Importación de archivos
slug: bbdd-aplicadas/unidad-2/practica/importacion-archivos
sidebar:
  order: 2
  label: Importación de archivos
---

Seis ejercicios de importación de archivos CSV y JSON con `BULK INSERT` y `OPENROWSET`. Presuponen la lección de [Importación de archivos](/bbdd-aplicadas/unidad-2/teoria/importacion-de-archivos/) y, para los formatos, [Formatos de intercambio](/bbdd-aplicadas/unidad-2/teoria/formatos-de-intercambio/).

## Archivos

Descargá los archivos y copialos en una carpeta del **servidor** de SQL Server (por ejemplo `C:\Importar\`). Los ejemplos usan esa carpeta: si usás otra, reemplazá la ruta. Antes de cada ejercicio, creá una base de prueba (por ejemplo `CREATE DATABASE PracticaImportacion;`) y cambiá a ella.

| Archivo | Descripción | Ejercicios |
|---|---|---|
| [viajerosgalicia.csv](/bbdd-aplicadas/unidad-2/practica/archivos/viajerosgalicia.csv) | Viajeros por estación y tramo horario (datos abiertos): 465 filas, CSV con fin de línea CRLF | 1 |
| [SalarioMensualMedio.csv](/bbdd-aplicadas/unidad-2/practica/archivos/SalarioMensualMedio.csv) | Mediana del salario mensual por sector (datos abiertos): 17255 filas, CRLF | 2 |
| [cliente_comillas.csv](/bbdd-aplicadas/unidad-2/practica/archivos/cliente_comillas.csv) | Clientes ficticios con comas y comillas dentro de los campos; fin de línea LF | 3 |
| [starwars.json](/bbdd-aplicadas/unidad-2/practica/archivos/starwars.json) | Personajes de la saga, arreglo JSON de 25 objetos, en UTF-8 y con una letra con tilde | 4 |
| [venta_sucia.csv](/bbdd-aplicadas/unidad-2/practica/archivos/venta_sucia.csv) | Ventas ficticias con errores de datos; fin de línea LF | 5 |
| [cliente_acentos.json](/bbdd-aplicadas/unidad-2/practica/archivos/cliente_acentos.json) | Clientes ficticios con tildes y un arreglo anidado, en UTF-8 | 6 |

:::note[Verificación]
Las resoluciones se ejecutaron en SQL Server 2022 sobre Linux, con los archivos en una carpeta del contenedor. La ruta `C:\Importar\...` de los enunciados es un ejemplo: en tu equipo se reemplaza por la propia. Los archivos CRLF se cargan con `ROWTERMINATOR = '0x0d0a'` y los LF con `'0x0a'`.
:::

---

### Ejercicio 1 · Viajeros por estación
<!-- ejercicio: U2.16 | nivel: inicial | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Importá `viajerosgalicia.csv` en una tabla `transporte.Viajero` con las columnas `Id`, `CodigoEstacion`, `NombreEstacion`, `NucleoCercanias`, `TramoHorario`, `ViajerosSubidos` y `ViajerosBajados`. Verificá la carga con la cantidad de filas, la cantidad de estaciones distintas y los totales de subidos y bajados.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El archivo tiene una fila de encabezado (`FIRSTROW = 2`), no tiene comillas y termina cada línea en CRLF. Las columnas de texto se declaran más largas que los datos y los números como `INT`. Después se comprueba la carga: el archivo tiene 466 líneas, es decir, 465 filas de datos.

<!-- check: U2.16 -->
```sql
CREATE SCHEMA transporte;
GO

CREATE TABLE transporte.Viajero (
    Id              INT           NOT NULL,
    CodigoEstacion  VARCHAR(10)   NOT NULL,
    NombreEstacion  VARCHAR(60)   NOT NULL,
    NucleoCercanias VARCHAR(40)   NOT NULL,
    TramoHorario    VARCHAR(20)   NOT NULL,
    ViajerosSubidos INT           NOT NULL,
    ViajerosBajados INT           NOT NULL
);
GO

BULK INSERT transporte.Viajero
FROM 'C:\Importar\viajerosgalicia.csv'
WITH (
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR   = '0x0d0a'
);

SELECT COUNT(*) AS Filas,
       COUNT(DISTINCT CodigoEstacion) AS Estaciones,
       SUM(ViajerosSubidos) AS TotalSubidos,
       SUM(ViajerosBajados) AS TotalBajados
FROM transporte.Viajero;
```

**Resultado esperado.**

| Filas | Estaciones | TotalSubidos | TotalBajados |
|---:|---:|---:|---:|
| 465 | 24 | 279 | 279 |

Una cantidad distinta de filas indica que el terminador de fila no coincide con el del archivo.
</details>

### Ejercicio 2 · Salario mensual por sector
<!-- ejercicio: U2.17 | nivel: inicial | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
El archivo `SalarioMensualMedio.csv` tiene las columnas `fecha`, `clae2` y `w_median`. Importalo en `empleo.SalarioMensual` y verificá la carga con la cantidad de filas, la primera y la última fecha y la cantidad de sectores (`clae2`) distintos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Es el mismo patrón que el ejercicio 1. La columna del archivo se llama `clae2`; la tabla conserva ese nombre para que el origen y el destino coincidan (con otra denominación, el resultado esperado cambia de encabezado pero no de datos). Como el orden de las columnas de la tabla es el del archivo, no hace falta archivo de formato.

<!-- check: U2.17 -->
```sql
CREATE SCHEMA empleo;
GO

CREATE TABLE empleo.SalarioMensual (
    Fecha   DATE NOT NULL,
    Clae2   INT  NOT NULL,
    Mediana INT  NOT NULL
);
GO

BULK INSERT empleo.SalarioMensual
FROM 'C:\Importar\SalarioMensualMedio.csv'
WITH (
    FIRSTROW        = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR   = '0x0d0a'
);

SELECT COUNT(*) AS Filas,
       MIN(Fecha) AS PrimeraFecha,
       MAX(Fecha) AS UltimaFecha,
       COUNT(DISTINCT Clae2) AS Sectores
FROM empleo.SalarioMensual;
```

**Resultado esperado.**

| Filas | PrimeraFecha | UltimaFecha | Sectores |
|---:|---|---|---:|
| 17255 | 2007-01-01 | 2023-11-01 | 85 |

Las fechas con formato `AAAA-MM-DD` se convierten sin ambigüedad a `DATE`.
</details>

### Ejercicio 3 · Campos con comas y comillas
<!-- ejercicio: U2.18 | nivel: intermedio | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
`cliente_comillas.csv` tiene nombres con comas (`"Ferreteria Lopez, Hnos."`), comillas dobles duplicadas (`"Kiosco ""La Esquina"""`) y campos vacíos. Importalo en `ventas.Cliente` (`ClienteId`, `Nombre`, `Localidad`, `Observacion`; las dos últimas admiten `NULL`) y explicá por qué con `FIELDTERMINATOR = ','` solo no alcanza.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `FORMAT = 'CSV'` aplica las reglas de RFC 4180: un campo entre comillas puede contener el delimitador, `""` representa una comilla y un campo vacío es `NULL`. Con solo `FIELDTERMINATOR` cada coma separaría una columna y las filas 1, 3 y 4 tendrían más columnas de las esperadas.

<!-- check: U2.18 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Cliente (
    ClienteId   INT          NOT NULL,
    Nombre      VARCHAR(60)  NOT NULL,
    Localidad   VARCHAR(30)  NULL,
    Observacion VARCHAR(80)  NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);
GO

BULK INSERT ventas.Cliente
FROM 'C:\Importar\cliente_comillas.csv'
WITH (
    FORMAT     = 'CSV',
    FIELDQUOTE = '"',
    FIRSTROW   = 2
);

SELECT ClienteId, Nombre, Localidad, Observacion
FROM ventas.Cliente
ORDER BY ClienteId;
```

**Resultado esperado.**

| ClienteId | Nombre | Localidad | Observacion |
|---:|---|---|---|
| 1 | Ferreteria Lopez, Hnos. | Rosario | NULL |
| 2 | Kiosco "La Esquina" | Cordoba | Paga al contado |
| 3 | Almacen Norte | Salta | Entrega por la manana, sin firma |
| 4 | Distribuidora Sur, S.A. | NULL | NULL |

Las comas internas se conservan, `""` pasa a `"` y los campos vacíos son `NULL`.
</details>

### Ejercicio 4 · Personajes en JSON con tilde
<!-- ejercicio: U2.19 | nivel: intermedio | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
Importá `starwars.json` (UTF-8) en `cine.Personaje` (`PersonajeId`, `Personaje`, `Actor`, `Pelicula`, `Anio`) sin perder la tilde de `Padmé Amidala`. Mostrá cuántos personajes hay por película y comprobá el largo del nombre `Padm%`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `SINGLE_CLOB` interpretaría los bytes UTF-8 con la página de códigos de la base y deformaría la `é` (ocuparía dos caracteres corruptos). Se leen los bytes con `SINGLE_BLOB` y se guardan en una columna `VARCHAR(MAX)` con _collation_ UTF-8, que los interpreta correctamente; después `OPENJSON` extrae las propiedades del arreglo (la propiedad del año se llama `anio_pelicula`). "Padmé Amidala" tiene 13 caracteres.

<!-- check: U2.19 -->
```sql
CREATE SCHEMA cine;
GO

CREATE TABLE cine.Personaje (
    PersonajeId INT           NOT NULL,
    Personaje   NVARCHAR(100) NOT NULL,
    Actor       NVARCHAR(100) NOT NULL,
    Pelicula    NVARCHAR(100) NOT NULL,
    Anio        INT           NOT NULL,
    CONSTRAINT PK_Personaje PRIMARY KEY CLUSTERED (PersonajeId)
);

CREATE TABLE cine.Archivo (
    Contenido VARCHAR(MAX) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NOT NULL
);
GO

-- El archivo está en UTF-8: se lee como bytes y se guarda en una columna con collation UTF8
INSERT INTO cine.Archivo (Contenido)
SELECT a.BulkColumn
FROM OPENROWSET(BULK 'C:\Importar\starwars.json', SINGLE_BLOB) AS a;

INSERT INTO cine.Personaje (PersonajeId, Personaje, Actor, Pelicula, Anio)
SELECT p.PersonajeId, p.Personaje, p.Actor, p.Pelicula, p.Anio
FROM cine.Archivo AS f
CROSS APPLY OPENJSON(f.Contenido)
WITH (
    PersonajeId INT           '$.id',
    Personaje   NVARCHAR(100) '$.personaje',
    Actor       NVARCHAR(100) '$.actor',
    Pelicula    NVARCHAR(100) '$.pelicula',
    Anio        INT           '$.anio_pelicula'
) AS p;

SELECT Anio, Pelicula, COUNT(*) AS Personajes
FROM cine.Personaje
GROUP BY Anio, Pelicula
ORDER BY Anio, Pelicula;

SELECT DISTINCT Personaje, LEN(Personaje) AS Largo
FROM cine.Personaje
WHERE Personaje LIKE N'Padm%';
```

**Resultado esperado.** Primero la cantidad de personajes por película:

| Anio | Pelicula | Personajes |
|---:|---|---:|
| 1977 | Star Wars: Episode IV - A New Hope | 8 |
| 1980 | Star Wars: Episode V - The Empire Strikes Back | 3 |
| 1983 | Star Wars: Episode VI - Return of the Jedi | 2 |
| 1999 | Star Wars: Episode I - The Phantom Menace | 6 |
| 2002 | Star Wars: Episode II - Attack of the Clones | 2 |
| 2005 | Star Wars: Episode III - Revenge of the Sith | 4 |

y después el nombre con tilde:

| Personaje | Largo |
|---|---:|
| Padmé Amidala | 13 |

Los 25 personajes se cargan sin errores. Si el nombre no tuviera la tilde correcta, el largo no daría 13.
</details>

### Ejercicio 5 · Carga con validación y rechazos
<!-- ejercicio: U2.20 | nivel: avanzado | tipo: programabilidad | verificacion: motor -->

:::note[Enunciado]
`venta_sucia.csv` (`VentaId`, `Fecha`, `ClienteId`, `Importe`) tiene filas con errores: una fecha inexistente, un cliente que no existe, un importe negativo, un importe vacío y un `VentaId` repetido. Dados los clientes 1 y 2 en `ventas.Cliente`, cargá el archivo en una tabla de staging y volcá a `ventas.Venta` solo las filas válidas. Registrá cada fila rechazada, con su número de orden de llegada y el motivo, en `staging.VentaRechazada`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** (1) Staging con columnas de texto y una columna `Fila` (identidad) que registra el orden de llegada; como el archivo no trae esa columna, se carga a través de una vista que no la incluye. (2) Se analiza cada fila con `TRY_CONVERT` (el estilo 23 de `DATE` exige `AAAA-MM-DD` y rechaza el 30 de febrero) y se cuenta con `ROW_NUMBER` el orden de cada `VentaId` para detectar repetidos: se conserva la primera aparición. (3) Se insertan en las rechazadas las filas con un motivo (en orden de prioridad) y en `ventas.Venta` las demás.

<!-- check: U2.20 -->
```sql
CREATE SCHEMA ventas;
GO
CREATE SCHEMA staging;
GO

CREATE TABLE ventas.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(40) NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

INSERT INTO ventas.Cliente (ClienteId, Nombre) VALUES (1, 'Cliente Uno'), (2, 'Cliente Dos');

CREATE TABLE ventas.Venta (
    VentaId   INT           NOT NULL,
    Fecha     DATE          NOT NULL,
    ClienteId INT           NOT NULL,
    Importe   DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Venta PRIMARY KEY CLUSTERED (VentaId),
    CONSTRAINT FK_Venta_Cliente FOREIGN KEY (ClienteId) REFERENCES ventas.Cliente (ClienteId),
    CONSTRAINT CK_Venta_Importe CHECK (Importe > 0)
);

CREATE TABLE staging.Venta (
    Fila      INT IDENTITY(1, 1) NOT NULL,
    VentaId   VARCHAR(20) NULL,
    Fecha     VARCHAR(20) NULL,
    ClienteId VARCHAR(20) NULL,
    Importe   VARCHAR(20) NULL,
    CONSTRAINT PK_StagingVenta PRIMARY KEY CLUSTERED (Fila)
);

CREATE TABLE staging.VentaRechazada (
    Fila   INT         NOT NULL,
    Motivo VARCHAR(40) NOT NULL
);
GO

CREATE VIEW staging.VentaCarga
AS
SELECT VentaId, Fecha, ClienteId, Importe FROM staging.Venta;
GO

BULK INSERT staging.VentaCarga
FROM 'C:\Importar\venta_sucia.csv'
WITH (FORMAT = 'CSV', FIRSTROW = 2);
GO

WITH Analizada AS (
    SELECT s.Fila,
           TRY_CONVERT(INT, s.VentaId)            AS VentaId,
           TRY_CONVERT(DATE, s.Fecha, 23)         AS Fecha,
           TRY_CONVERT(INT, s.ClienteId)          AS ClienteId,
           TRY_CONVERT(DECIMAL(10,2), s.Importe)  AS Importe,
           ROW_NUMBER() OVER (PARTITION BY s.VentaId ORDER BY s.Fila) AS Orden
    FROM staging.Venta AS s
)
INSERT INTO staging.VentaRechazada (Fila, Motivo)
SELECT a.Fila,
       CASE
           WHEN a.Fecha IS NULL                                       THEN 'fecha invalida'
           WHEN a.Importe IS NULL                                     THEN 'importe vacio o invalido'
           WHEN a.Importe <= 0                                        THEN 'importe no positivo'
           WHEN NOT EXISTS (SELECT 1 FROM ventas.Cliente AS c
                            WHERE c.ClienteId = a.ClienteId)          THEN 'cliente inexistente'
           ELSE 'venta duplicada'
       END
FROM Analizada AS a
WHERE a.Fecha IS NULL
   OR a.Importe IS NULL
   OR a.Importe <= 0
   OR NOT EXISTS (SELECT 1 FROM ventas.Cliente AS c WHERE c.ClienteId = a.ClienteId)
   OR a.Orden > 1;

INSERT INTO ventas.Venta (VentaId, Fecha, ClienteId, Importe)
SELECT TRY_CONVERT(INT, s.VentaId), TRY_CONVERT(DATE, s.Fecha, 23),
       TRY_CONVERT(INT, s.ClienteId), TRY_CONVERT(DECIMAL(10,2), s.Importe)
FROM staging.Venta AS s
WHERE NOT EXISTS (SELECT 1 FROM staging.VentaRechazada AS r WHERE r.Fila = s.Fila);

SELECT Fila, Motivo FROM staging.VentaRechazada ORDER BY Fila;

SELECT VentaId, Fecha, ClienteId, Importe FROM ventas.Venta ORDER BY VentaId;
```

**Resultado esperado.** Filas rechazadas:

| Fila | Motivo |
|---:|---|
| 3 | fecha invalida |
| 4 | cliente inexistente |
| 5 | importe no positivo |
| 6 | venta duplicada |
| 7 | importe vacio o invalido |

y ventas cargadas:

| VentaId | Fecha | ClienteId | Importe |
|---:|---|---:|---:|
| 1 | 2026-03-01 | 1 | 1500.00 |
| 2 | 2026-03-02 | 2 | 820.50 |
| 7 | 2026-03-08 | 2 | 1200.25 |

Las 8 filas del archivo se reparten en 3 válidas y 5 rechazadas, y cada rechazo es trazable a su posición en el archivo. Cargar directo a `ventas.Venta` habría cancelado o descartado las filas sin dejar el motivo.
</details>

### Ejercicio 6 · JSON UTF-8 con un arreglo anidado
<!-- ejercicio: U2.21 | nivel: avanzado | tipo: ddl | verificacion: motor -->

:::note[Enunciado]
`cliente_acentos.json` contiene tres clientes con tildes (`Ferretería Peña`, `Almacén Ñandú`) y cada uno con un arreglo `contactos` de correos (uno de ellos vacío). Cargalos en `ventas.Cliente` y `ventas.ClienteContacto` (una fila por correo) y mostrá cuántos contactos tiene cada cliente, incluyendo el que no tiene ninguno.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El archivo está en UTF-8: se lee con `SINGLE_BLOB` hacia una columna `VARCHAR(MAX)` con _collation_ UTF-8 (ejercicio 4). Luego se hacen dos pasadas con `OPENJSON`: la primera extrae los datos del cliente; la segunda trae `contactos` con `AS JSON` y lo despliega con un segundo `OPENJSON`, que sin `WITH` devuelve cada elemento en la columna `value`. Para contar los contactos incluido el cliente sin ninguno se usa `LEFT JOIN`.

<!-- check: U2.21 -->
```sql
CREATE SCHEMA ventas;
GO

CREATE TABLE ventas.Cliente (
    ClienteId INT           NOT NULL,
    Nombre    NVARCHAR(60)  NOT NULL,
    Localidad NVARCHAR(30)  NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE ventas.ClienteContacto (
    ClienteId INT           NOT NULL,
    Email     VARCHAR(80)   NOT NULL,
    CONSTRAINT PK_ClienteContacto PRIMARY KEY CLUSTERED (ClienteId, Email),
    CONSTRAINT FK_ClienteContacto_Cliente FOREIGN KEY (ClienteId) REFERENCES ventas.Cliente (ClienteId)
);

CREATE TABLE ventas.ArchivoCliente (
    Contenido VARCHAR(MAX) COLLATE Latin1_General_100_CI_AS_SC_UTF8 NOT NULL
);
GO

INSERT INTO ventas.ArchivoCliente (Contenido)
SELECT a.BulkColumn
FROM OPENROWSET(BULK 'C:\Importar\cliente_acentos.json', SINGLE_BLOB) AS a;

INSERT INTO ventas.Cliente (ClienteId, Nombre, Localidad)
SELECT c.ClienteId, c.Nombre, c.Localidad
FROM ventas.ArchivoCliente AS f
CROSS APPLY OPENJSON(f.Contenido)
WITH (
    ClienteId INT          '$.clienteId',
    Nombre    NVARCHAR(60) '$.nombre',
    Localidad NVARCHAR(30) '$.localidad'
) AS c;

INSERT INTO ventas.ClienteContacto (ClienteId, Email)
SELECT c.ClienteId, e.[value]
FROM ventas.ArchivoCliente AS f
CROSS APPLY OPENJSON(f.Contenido)
WITH (
    ClienteId INT           '$.clienteId',
    Contactos NVARCHAR(MAX) '$.contactos' AS JSON
) AS c
CROSS APPLY OPENJSON(c.Contactos) AS e;

SELECT c.ClienteId, c.Nombre, c.Localidad, COUNT(k.Email) AS Contactos
FROM ventas.Cliente AS c
LEFT JOIN ventas.ClienteContacto AS k ON k.ClienteId = c.ClienteId
GROUP BY c.ClienteId, c.Nombre, c.Localidad
ORDER BY c.ClienteId;
```

**Resultado esperado.**

| ClienteId | Nombre | Localidad | Contactos |
|---:|---|---|---:|
| 1 | Ferretería Peña | Córdoba | 2 |
| 2 | Almacén Ñandú | Rosario | 1 |
| 3 | Kiosco Sol | Salta | 0 |

El cliente 3 tiene un arreglo vacío: el segundo `OPENJSON` no devuelve filas, por eso no aparece en `ClienteContacto` y el `LEFT JOIN` lo cuenta como 0.
</details>
