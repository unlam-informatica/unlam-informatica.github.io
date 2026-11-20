---
title: MongoDB Compass
slug: bbdd-aplicadas/unidad-4/teoria/mongodb-compass
sidebar:
  order: 6
---

[← Unidad 4](/bbdd-aplicadas/unidad-4/teoria/)

Guía de uso de la interfaz gráfica oficial de MongoDB. Cada operación de la interfaz tiene su equivalente en el shell, que se explica en [CRUD y consultas](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/) y en [Aggregation Pipeline, índices y vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/). La instalación y la conexión a Atlas están en [Instalación y conexión](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/).

:::note[Sobre las descripciones de pantalla]
Esta página describe la interfaz con **texto**, sin capturas. Los nombres de botones y pestañas (en inglés) corresponden a las versiones recientes de Compass y pueden cambiar entre versiones. Los filtros, las proyecciones, el índice y el plan que se muestran tienen su equivalente en `mongosh`, con resultados obtenidos con MongoDB 7.0; los pasos dentro de la interfaz gráfica, en cambio, no se probaron en cada versión de Compass, así que si un botón o una pestaña no coincide con lo que ves, guiate por la documentación de tu versión.
:::

## Para qué sirve

Compass permite explorar una base, probar una consulta, armar un pipeline etapa por etapa con vista previa y ver el plan de ejecución, sin escribir los comandos completos. Sirve para **aprender y diagnosticar**; el trabajo repetible se escribe como script de `mongosh`.

## ¿Qué es MongoDB Compass?

**MongoDB Compass** es el cliente gráfico (GUI) oficial de MongoDB, disponible para Windows, macOS y Linux. Es gratuito. Su código fuente es público en el repositorio oficial de MongoDB, con la licencia *Server Side Public License* (SSPL), que no está aprobada como de código abierto por la *Open Source Initiative*: se lo describe como de código disponible y no sin más "de código abierto". La licencia vigente figura en el repositorio.

**Funciones principales:**

- Conectarse a instancias locales o remotas (Atlas).
- Crear y eliminar bases y colecciones.
- Insertar, importar, modificar y eliminar documentos.
- Filtrar documentos con la sintaxis de `find()`.
- Construir pipelines de agregación de forma visual.
- Administrar índices y ver el plan de ejecución (*Explain*).
- Un shell integrado (`mongosh`) para ejecutar comandos.

## Conexión

Compass pide una **cadena de conexión** (URI) en **New Connection**. Para un servidor local, con los valores por defecto:

```text
mongodb://localhost:27017/
```

Para un clúster de Atlas, se pega la cadena que genera Atlas (**Connect → Compass**), con marcadores en lugar de credenciales:

<!-- sintaxis -->
```text
mongodb+srv://<usuario>:<contraseña>@<cluster>/
```

El panel izquierdo muestra las bases y colecciones de la conexión; la pestaña de **My Queries** guarda consultas y pipelines para reutilizarlos. El paso a paso para Atlas (clúster, usuario de base de datos, lista de acceso de red) está en [Instalación y conexión](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/#conexión-a-atlas). Los usuarios y las contraseñas no se guardan en capturas ni en apuntes.

## Vistas de datos

Dentro de una colección, la pestaña **Documents** ofrece tres formas de ver los documentos:

| Vista | Descripción |
|---|---|
| **Lista** | Un documento por bloque, con los campos y su tipo |
| **JSON** | Los documentos como JSON completo |
| **Tabla** | Una fila por documento y una columna por campo; útil para comparar valores |

## Crear una base y una colección

1. En el panel izquierdo, botón **+** junto a **Databases** (o **Create database**).
2. Completar **Database Name** y **Collection Name**.
3. Confirmar con **Create Database**.

A diferencia del shell, Compass **sí crea** la base y la colección vacías de inmediato.

## Insertar documentos

1. Seleccionar la colección.
2. **ADD DATA → Insert document**.
3. Escribir el documento en JSON (o en la vista de campos) y confirmar con **Insert**.

```json
{
  "nombre": "Pedro Gómez",
  "activo": true,
  "saldo": { "$numberDecimal": "2500.50" },
  "direccion": { "calle": "Avenida Siempre Viva", "numero": 742 },
  "documentos": ["DNI", "Licencia"]
}
```

El cuadro acepta Extended JSON, así que `"$numberDecimal"` se guarda como `Decimal128`. Para insertar **varios** documentos, se pega un array JSON (`[ {...}, {...} ]`). El equivalente en el shell es `insertOne()` o `insertMany()`.

## Importar documentos

**ADD DATA → Import JSON or CSV file** abre el asistente de importación.

- **JSON**: acepta un array de documentos o un documento por línea (NDJSON). Los tipos que JSON no tiene (`Date`, `ObjectId`) se importan correctamente solo si están escritos en Extended JSON; de lo contrario quedan como texto.
- **CSV**: se elige el delimitador y **se indica el tipo de cada columna** (`String`, `Int32`, `Double`, `Date`, `Boolean`...).

:::caution[Los tipos de una importación CSV]
Si no se cambia el tipo de una columna de fechas a `Date`, queda como `String` y las consultas por rango de fechas no encuentran esos documentos (ver [type bracketing](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/#fechas-y-type-bracketing)). Se verifica con un filtro `{ fecha: { $type: "string" } }` luego de importar. Un número con decimales quedaría como `Double` y un entero como `Int32`.
:::

La alternativa de línea de comandos es `mongoimport`, que es una herramienta externa y no un comando de `mongosh`:

<!-- sintaxis -->
```text
mongoimport --db=<base> --collection=<coleccion> --file=<archivo>.json --jsonArray
mongoimport --db=<base> --collection=<coleccion> --type=csv --headerline --file=<archivo>.csv
```

## Filtrar documentos

La barra **Filter** acepta el documento de filtro de `find()`; las otras opciones del panel corresponden al resto de la consulta:

| Campo de Compass | Equivalente en el shell |
|---|---|
| **Filter** | primer argumento de `find()` |
| **Project** | segundo argumento (proyección) |
| **Sort** | `.sort()` |
| **Skip**, **Limit** | `.skip()`, `.limit()` |
| **Collation** | `.collation()` |

Los filtros se escriben tal cual en la barra. Sobre la colección `productos` de [CRUD](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/#datos-de-los-ejemplos) (cargala antes en tu base de práctica; el ejemplo de la tilde usa también `clientes`, del script de [Aggregation Pipeline](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#datos-de-los-ejemplos)):

```text
{ categoria: "audio" }
{ precio: { $gt: 40 } }
{ $or: [ { categoria: "audio", precio: { $gt: 70 } }, { stock: 0 } ] }
```

<!-- check: U4.T.CRUD.08 -->
```javascript
db.productos.find({ categoria: "audio" })                                               // _id 5, 6
db.productos.find({ precio: { $gt: 40 } }).sort({ precio: -1 }).limit(2)                // Notebook, Monitor (_id 4, 3)
db.productos.find({ $or: [{ categoria: "audio", precio: { $gt: 70 } }, { stock: 0 }] })  // _id 5, 6
db.productos.find({ categoria: "perifericos" }, { _id: 0, nombre: 1, precio: 1 }).sort({ nombre: 1 }).skip(1).limit(1)
// { nombre: 'Teclado', precio: 45 }  (el segundo por nombre: Mouse, Teclado, Webcam)
```

Los valores de texto **distinguen mayúsculas y tildes**: `{ localidad: "Ramos Mejia" }` (sin tilde) no devuelve los documentos que tienen `"Ramos Mejía"`, y no se informa ningún error. Con los datos de ejemplo, la consulta sin tilde cuenta 0 y la correcta cuenta 2.

### Collation

La **collation** define cómo se comparan y ordenan los textos. Se escribe como un documento (`{ locale: "es", strength: 1 }`):

| Opción | Función |
|---|---|
| `locale` | Reglas del idioma, por ejemplo `es`, `en`, `fr` |
| `strength` | Nivel de diferencias que se consideran. `1` ignora mayúsculas y acentos; `2` ignora solo mayúsculas |
| `caseLevel` | Agrega la comparación de mayúsculas cuando corresponde |
| `caseFirst` | Mayúsculas primero, minúsculas primero o valor predeterminado |
| `numericOrdering` | Ordena cadenas numéricas por valor (`"2"` antes que `"10"`) |

<!-- check: U4.T.CRUD.08 -->
```javascript
db.localidades.find({ nombre: "moron" })                                               // solo "moron" (_id 2)
db.localidades.find({ nombre: "moron" }).collation({ locale: "es", strength: 1 })      // Morón, moron y MORON (_id 1, 2, 3)
db.codigos.find().sort({ c: 1 })                                                       // "1", "10", "2" (orden textual)
db.codigos.find().sort({ c: 1 }).collation({ locale: "es", numericOrdering: true })   // "1", "2", "10"
```

La collation cambia comparación y orden; para que un índice sirva a una consulta con collation, el índice debe haberse creado con la misma collation.

## Modificar documentos

1. Pasar el cursor sobre el documento y hacer clic en el ícono de **lápiz** (*Edit document*), o hacer doble clic en un campo.
2. Cambiar el valor. A la derecha de cada campo se ve su **tipo BSON** (String, Int32, Date...), que se puede cambiar.
3. Confirmar con **Update**.

Esta edición actualiza **un documento**. Para modificar muchos a la vez, se usa `updateMany()` en el shell integrado.

## Eliminar y clonar documentos

- **Eliminar**: ícono de **papelera**; el documento se marca como *flagged for deletion* (en rojo) y se confirma con **Delete**.
- **Clonar**: ícono de **clonar**; abre el cuadro *Insert Document* con los mismos campos, que se editan antes de confirmar con **Insert**. Si el `_id` se deja igual, la inserción falla con `E11000`: hay que cambiarlo o quitarlo.

## Aggregation Pipeline visual

1. Seleccionar la colección y abrir la pestaña **Aggregations**.
2. **Add Stage** y elegir una etapa en el menú (`$match`, `$group`, `$project`, `$lookup`, `$unwind`, `$sort`, `$limit`, `$skip`, `$replaceRoot`, `$out`...).
3. Completar el cuerpo de la etapa. A la derecha, una **vista previa** muestra los primeros documentos que salen de esa etapa (con un muestreo de la colección).
4. Agregar más etapas con **Add Stage**, reordenarlas o activarlas y desactivarlas.

La vista previa de cada etapa ayuda a depurar un pipeline paso a paso. Se puede exportar el pipeline a un lenguaje de programación, y **Save → Create view** crea una [vista](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#vistas); el panel izquierdo la muestra con la marca de solo lectura.

## Índices

La pestaña **Indexes** lista los índices de la colección con su nombre, definición, tipo, tamaño y la cantidad de usos. **Create Index** permite elegir los campos y el orden (`1` ascendente, `-1` descendente), y las opciones (único, parcial, TTL, collation, nombre).

El equivalente en el shell, con un nombre propio:

<!-- check: U4.T.CRUD.08 -->
```javascript
db.productos.createIndex({ categoria: 1 }, { name: "categoria_indx" })   // devuelve 'categoria_indx'
db.productos.getIndexes()                                                // _id_ y categoria_indx
db.productos.dropIndex("categoria_indx")
```

Los tipos de índice y su efecto están en [Índices y estadísticas de ejecución](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#índices-y-estadísticas-de-ejecución).

## Explain Plan

El botón **Explain** (junto a **Find**, con un filtro cargado) ejecuta `explain("executionStats")` y lo presenta en forma gráfica. Los campos del panel de resumen son:

| Campo mostrado | Significado |
|---|---|
| **Documents Returned** | `nReturned` |
| **Documents Examined** | `totalDocsExamined` |
| **Index Keys Examined** | `totalKeysExamined` |
| **Actual Query Execution Time** | `executionTimeMillis` |
| **Query used the following index** / **No index available for this query** | Se usó un índice, o la consulta es un `COLLSCAN` |
| **Sorted in memory** | El orden se hizo en memoria (`SORT`) y no con un índice |

Debajo del resumen se ven las etapas del plan (`COLLSCAN`, `IXSCAN`, `FETCH`, `SORT`) y hay una vista **Raw JSON** con la salida completa de `explain()`. Los mismos números se obtienen en el shell:

<!-- check: U4.T.CRUD.08 -->
```javascript
db.productos.find({ categoria: "audio" }).explain("executionStats")
// nReturned: 2, totalKeysExamined: 0, totalDocsExamined: 8, etapa: COLLSCAN
```

La consulta devuelve 2 documentos y examina los 8 de la colección: no hay índice sobre `categoria`. Con `createIndex({ categoria: 1 })`, `Documents Examined` baja a 2.

## Asistente de IA

Las versiones recientes de Compass incorporan un asistente que genera consultas y pipelines a partir de una descripción en lenguaje natural (por ejemplo, "productos de la categoría audio con precio mayor a 70"). Es una herramienta de ayuda y su disponibilidad depende de la versión y de la configuración. Toda consulta generada se revisa antes de usarla: el asistente puede equivocarse en nombres de campos o en el operador. Esta función no forma parte del programa de la materia.

## Errores frecuentes

:::caution[Errores frecuentes]
- Importar un CSV sin cambiar el tipo de las columnas de fecha: quedan como `String`.
- Filtrar `"Ramos Mejia"` sin tilde: no devuelve nada y no da error.
- Usar el ícono de lápiz esperando modificar muchos documentos: edita uno solo.
- Confiar en la vista previa de una etapa como resultado final: es una muestra de la colección.
- Dejar usuario y contraseña en una captura o en un apunte compartido.
:::

## Autoevaluación

<details>
<summary>1. Importé un CSV con una columna fecha sin cambiar el tipo y una consulta de rango con límite Date no devuelve nada. ¿Por qué?</summary>

La consulta es `{ fecha: { $gte: ISODate("2026-01-01") } }`.

La columna quedó como `String` y los operadores de comparación solo comparan valores del mismo tipo. Se vuelve a importar con el tipo `Date`, o se convierte con `$toDate` en un pipeline.

</details>

<details>
<summary>2. ¿Qué campo de Compass equivale a `.skip()` del shell? ¿Y a `explain("executionStats")`?</summary>

El campo **Skip** del panel de consulta, y el botón **Explain**.

</details>

:::tip[En resumen]
- Compass es la interfaz gráfica; cada acción tiene su comando de `mongosh`.
- Filter, Project, Sort, Skip, Limit y Collation corresponden a las partes de `find()`.
- Al importar un CSV se eligen los tipos de las columnas; las fechas deben ser `Date`.
- Explain muestra `nReturned`, claves y documentos examinados, y si hubo `COLLSCAN` o `IXSCAN`.
:::

## Fuentes

- Presentación de cátedra, Unidad 4, parte 1 (MongoDB Compass) y agregaciones.
- MongoDB Compass Documentation: https://www.mongodb.com/docs/compass/.
