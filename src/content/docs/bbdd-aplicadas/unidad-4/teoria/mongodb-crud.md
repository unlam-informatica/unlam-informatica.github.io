---
title: MongoDB — CRUD y consultas
slug: bbdd-aplicadas/unidad-4/teoria/mongodb-crud
sidebar:
  order: 4
---

[← Unidad 4](/bbdd-aplicadas/unidad-4/teoria/)

Operaciones de MongoDB Query Language (MQL) sobre colecciones: insertar, consultar con `find()` y sus operadores, actualizar (incluido `upsert`), reemplazar, eliminar y combinar varias escrituras con `bulkWrite()`. Presupone [MongoDB — Introducción](/bbdd-aplicadas/unidad-4/teoria/mongodb-introduccion/).

Todos los resultados de la página se obtuvieron con MongoDB 7.0 y `mongosh` 2.x. Para reproducirlos, abrí `mongosh`, elegí una base de práctica (por ejemplo, `use practica`; se crea al insertar el primer documento) y cargá los datos de la sección siguiente.

## Para qué sirve

Una tienda registra productos y pedidos. Hay que cargarlos, buscar los que cumplen una condición, corregir un precio, reponer el stock de varios a la vez y borrar los que se discontinuaron. Son las cuatro operaciones CRUD (*Create, Read, Update, Delete*). Se ejecutan sobre una colección, y si esta no existe, las inserciones la crean.

| Operación | Método MongoDB | Equivalente SQL |
|---|---|---|
| Create | `insertOne()`, `insertMany()` | `INSERT` |
| Read | `find()`, `findOne()`, `countDocuments()`, `distinct()` | `SELECT` |
| Update | `updateOne()`, `updateMany()`, `replaceOne()` | `UPDATE` |
| Delete | `deleteOne()`, `deleteMany()` | `DELETE` |
| Varias a la vez | `bulkWrite()` | un lote de sentencias |

## Datos de los ejemplos

Las consultas de lectura y de actualización usan una colección `productos` con 8 documentos. Cargala con el script siguiente en una base vacía. Los ejemplos de inserción (`socios`) y de fechas (`eventos`) crean su propia colección en el bloque. Cada sección parte de este estado inicial; si ya ejecutaste actualizaciones o borrados y querés repetir un ejemplo, ejecutá `db.productos.drop()` y volvé a cargar el script. Dentro de las secciones de `upsert`, `replaceOne()` y `delete`, los bloques son consecutivos (usan el documento `_id: 20` que crea el primer `upsert`), y los dos bloques de `bulkWrite()` también:

<!-- check: U4.T.CRUD.02 -->
```javascript
db.productos.insertMany([
  { _id: 1, nombre: "Teclado",     categoria: "perifericos",  precio: 45,  stock: 12, etiquetas: ["usb", "oficina"] },
  { _id: 2, nombre: "Mouse",       categoria: "perifericos",  precio: 20,  stock: 30, etiquetas: ["usb"] },
  { _id: 3, nombre: "Monitor",     categoria: "pantallas",    precio: 300, stock: 5,  etiquetas: ["hdmi", "oficina"] },
  { _id: 4, nombre: "Notebook",    categoria: "computadoras", precio: 900, stock: 3,  etiquetas: ["portatil"] },
  { _id: 5, nombre: "Auriculares", categoria: "audio",        precio: 60,  stock: 0,  etiquetas: ["usb", "audio"] },
  { _id: 6, nombre: "Parlante",    categoria: "audio",        precio: 85,  stock: 8,  etiquetas: ["audio", "bluetooth"] },
  { _id: 7, nombre: "Webcam",      categoria: "perifericos",  precio: 55,  stock: 14, etiquetas: ["usb", "video"] },
  { _id: 8, nombre: "Impresora",   categoria: "impresion",    precio: 210, stock: 2,  etiquetas: ["oficina"] }
]);
```

El ejemplo de `$elemMatch` usa además una colección `pedidos` (con los ítems embebidos) y existe `clientes`: ambas se cargan con el script de [Aggregation Pipeline · Datos de los ejemplos](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#datos-de-los-ejemplos), que también incluye `productos`; cargá ese script en lugar de este si vas a usar `pedidos`.

## Create: insertar documentos

### `insertOne()` e `insertMany()`

<!-- check: U4.T.CRUD.01 -->
```javascript
db.socios.insertOne({ _id: 1, nombre: "Ana", edad: 28 });
db.socios.insertMany([
  { _id: 2, nombre: "Bruno", edad: 34 },
  { _id: 3, nombre: "Carla", edad: 23 }
]);
```

Las respuestas son:

```text
{ acknowledged: true, insertedId: 1 }
{ acknowledged: true, insertedIds: { '0': 2, '1': 3 } }
```

Si no se indica `_id`, `insertedId` es el `ObjectId` generado. Con `insertMany()`, `insertedIds` asocia la posición de cada documento del array con su `_id`.

### Inserción en lote con duplicados: `ordered`

Por defecto `insertMany()` es **ordenada** (`ordered: true`): se detiene en el primer error y los documentos que venían después no se insertan. Con `{ ordered: false }` el motor sigue con el resto y reporta todos los errores al final.

<!-- check: U4.T.CRUD.01 -->
```javascript
// ordered: true (por defecto). El _id 2 ya existe.
try {
  db.socios.insertMany([
    { _id: 4, nombre: "Diego" },
    { _id: 2, nombre: "Duplicado" },
    { _id: 5, nombre: "Elena" }
  ]);
} catch (e) {
  print(e.code, e.result.insertedCount);   // 11000, 1
}

// ordered: false. Se insertan el 6 y el 7, y falla solo el duplicado.
try {
  db.socios.insertMany([
    { _id: 6, nombre: "Fabi" },
    { _id: 2, nombre: "Duplicado" },
    { _id: 7, nombre: "Gaby" }
  ], { ordered: false });
} catch (e) {
  print(e.code, e.result.insertedCount, e.writeErrors.length);   // 11000, 2, 1
}
```

**Resultado esperado.**

| Caso | Código | Documentos insertados | `_id` que quedan en la colección |
|---|---:|---:|---|
| `ordered: true` | 11000 | 1 (el 4) | 1, 2, 3, 4 (el 5 no se intentó) |
| `ordered: false` | 11000 | 2 (el 6 y el 7) | 1, 2, 3, 4, 6, 7 |

El mensaje del error empieza con `E11000 duplicate key error collection: …`. El código 11000 corresponde a una clave duplicada, ya sea en `_id` o en un índice único. Un `insertMany()` **no es una transacción**: lo que se insertó antes del error permanece.

## Read: `find()`

<!-- sintaxis -->
```javascript
// forma general
db.coleccion.find(<filtro>, <proyección>).sort(<orden>).skip(n).limit(n)
```

Se escribe como una plantilla; el filtro `{}` (o ninguno) devuelve todos los documentos. Equivale a `SELECT * FROM tabla`.

### Equivalencias SQL ↔ MongoDB

| Operación | SQL Server | MongoDB |
|---|---|---|
| Todos los documentos | `SELECT * FROM productos` | `db.productos.find()` |
| Campos específicos | `SELECT nombre, precio FROM productos` | `db.productos.find({}, { nombre: 1, precio: 1 })` |
| Con filtro | `WHERE categoria = 'audio'` | `db.productos.find({ categoria: "audio" })` |
| Filtro y proyección | `SELECT nombre, precio FROM productos WHERE categoria = 'audio'` | `db.productos.find({ categoria: "audio" }, { nombre: 1, precio: 1, _id: 0 })` |
| Patrón | `WHERE nombre LIKE 'M%'` | `db.productos.find({ nombre: /^M/ })` |
| Orden ascendente | `ORDER BY precio ASC` | `db.productos.find().sort({ precio: 1 })` |
| Limitar | `SELECT TOP 3 *` | `db.productos.find().limit(3)` |

### Operadores de comparación

| Operador | Significado |
|---|---|
| `$eq`, `$ne` | Igual, distinto |
| `$gt`, `$gte` | Mayor, mayor o igual |
| `$lt`, `$lte` | Menor, menor o igual |
| `$in`, `$nin` | Igual a alguno de una lista, a ninguno |

<!-- check: U4.T.CRUD.02 -->
```javascript
db.productos.find({ precio: { $gt: 100 } })                              // _id 3, 4, 8
db.productos.find({ precio: { $gte: 45, $lte: 85 } })                    // _id 1, 5, 6, 7
db.productos.find({ categoria: { $in: ["audio", "pantallas"] } })        // _id 3, 5, 6
db.productos.find({ categoria: { $nin: ["perifericos", "audio"] } })     // _id 3, 4, 8
```

Dos condiciones sobre campos distintos dentro del mismo filtro se combinan con **AND** implícito:

<!-- check: U4.T.CRUD.02 -->
```javascript
db.productos.find({ categoria: "perifericos", precio: { $lt: 50 } })     // _id 1, 2
```

Estas tres formas son equivalentes: `{ categoria: "audio" }`, `{ categoria: { $eq: "audio" } }` y `{ categoria: { $in: ["audio"] } }`.

### Operadores lógicos

| Operador | Significado |
|---|---|
| `$and` | Se cumplen todas las condiciones |
| `$or` | Se cumple al menos una |
| `$nor` | No se cumple ninguna |
| `$not` | Niega el operador que lo sigue (se usa dentro de un campo) |

<!-- check: U4.T.CRUD.02 -->
```javascript
db.productos.find({ $or: [{ stock: 0 }, { precio: { $gte: 900 } }] })                  // _id 4, 5
db.productos.find({ $nor: [{ categoria: "perifericos" }, { categoria: "audio" }] })    // _id 3, 4, 8
db.productos.find({ precio: { $not: { $gt: 60 } } })                                   // _id 1, 2, 5, 7
```

`$and` explícito hace falta cuando se repite el mismo campo o el mismo operador en dos condiciones (un objeto JavaScript no admite claves repetidas):

<!-- sintaxis -->
```javascript
{ $and: [ { $or: [<cond1>, <cond2>] }, { $or: [<cond3>, <cond4>] } ] }
```

### Operadores de arrays

| Operador | Significado |
|---|---|
| `{ campo: "valor" }` | El array contiene el valor |
| `$all` | El array contiene **todos** los valores indicados |
| `$size` | El array tiene exactamente esa cantidad de elementos |
| `$elemMatch` | Un **mismo** elemento cumple todas las condiciones |
| `"campo.0"` | Acceso por posición (base 0) |

<!-- check: U4.T.CRUD.02 -->
```javascript
db.productos.find({ etiquetas: "usb" })                            // _id 1, 2, 5, 7
db.productos.find({ etiquetas: { $all: ["usb", "oficina"] } })     // _id 1
db.productos.find({ etiquetas: { $size: 2 } })                     // _id 1, 3, 5, 6, 7
db.productos.find({ "etiquetas.0": "audio" })                      // _id 6
```

`$elemMatch` exige que las condiciones recaigan sobre **el mismo** elemento del array. Si se buscan pedidos con una línea de producto 2 y cantidad de al menos 2:

<!-- check: U4.T.CRUD.02 -->
```javascript
db.pedidos.find({ items: { $elemMatch: { productoId: 2, cantidad: { $gte: 2 } } } })     // pedidos 103, 106, 108
db.pedidos.find({ "items.productoId": 2, "items.cantidad": { $gte: 2 } })                // pedidos 101, 103, 106, 108
```

El segundo filtro también devuelve el pedido 101, que tiene un ítem del producto 2 con cantidad 1 y otro ítem (producto 1) con cantidad 2: las condiciones se cumplen en elementos distintos. Para que valgan juntas hay que usar `$elemMatch`.

### Operadores de elementos y de evaluación

| Operador | Significado |
|---|---|
| `$exists` | El campo existe (`true`) o no (`false`) |
| `$type` | El campo tiene ese tipo BSON |
| `$regex` | Coincide con una expresión regular |
| `$expr` | Usa expresiones de agregación, por ejemplo para comparar dos campos |
| `$mod` | Resto de una división |
| `$text` | Búsqueda con un índice de texto (ver [índices](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#índice-de-texto)) |
| `$where` | Ejecuta JavaScript por documento |

<!-- check: U4.T.CRUD.02 -->
```javascript
db.productos.insertOne({ _id: 9, nombre: "Cable", precio: "15" });   // precio guardado como texto

db.productos.find({ stock: { $exists: false } })             // _id 9
db.productos.find({ precio: { $type: "string" } })           // _id 9
db.productos.find({ precio: { $type: "number" } })           // _id 1 a 8
db.productos.find({ nombre: { $regex: "^m", $options: "i" } })   // _id 2, 3 (Mouse, Monitor)
```

El documento 9 guarda `precio` como texto. Por eso `{ precio: { $gt: 100 } }` sigue devolviendo solo los documentos 3, 4 y 8: ver [type bracketing](#fechas-y-type-bracketing).

`$expr` compara campos del mismo documento (`{ $expr: { $gt: ["$precio", "$stock"] } }`). `$where` ejecuta JavaScript por documento, impide el uso de índices y es un riesgo si se arma con entrada externa: se prefiere `$expr` u otros operadores.

### Fechas y type bracketing

En los operadores de comparación (`$gt`, `$gte`, `$lt`, `$lte`, `$eq`) MongoDB aplica el *type bracketing*: **solo compara valores del mismo tipo**. Un `Date` solo se compara con `Date`; un `String`, con `String`. Un documento cuyo campo tiene otro tipo no es "menor" ni "mayor": simplemente **no coincide**. Por eso comparar un campo `Date` con un texto no falla y devuelve cero documentos.

<!-- check: U4.T.CRUD.04 -->
```javascript
db.eventos.insertMany([
  { _id: 1, nombre: "alta",  fecha: ISODate("2026-01-15T00:00:00Z") },
  { _id: 2, nombre: "baja",  fecha: ISODate("2026-02-20T00:00:00Z") },
  { _id: 3, nombre: "texto", fecha: "2026-01-20" }
]);

// Límites Date: encuentra solo los documentos con fecha de tipo Date
db.eventos.find({ fecha: { $gte: ISODate("2026-01-01T00:00:00Z"), $lt: ISODate("2026-02-01T00:00:00Z") } })   // _id 1

// Límites String: encuentra solo los documentos cuya fecha es un String
db.eventos.find({ fecha: { $gte: "2026-01-01", $lt: "2026-02-01" } })                                        // _id 3
```

Cada filtro ve únicamente los documentos del tipo de sus límites. Así, un campo de fecha guardado como texto queda fuera de los rangos de fechas y nadie recibe un error. Para detectar el problema se usa `$type`:

<!-- check: U4.T.CRUD.04 -->
```javascript
db.eventos.find({ fecha: { $type: "date" } })       // _id 1, 2
db.eventos.find({ fecha: { $type: "string" } })     // _id 3
```

La solución definitiva es **guardar las fechas como `Date`**. Si ya están como texto, se las convierte en una agregación con `$toDate` (o `$dateFromString` cuando el formato es particular):

<!-- check: U4.T.CRUD.04 -->
```javascript
db.eventos.aggregate([
  { $addFields: { fechaReal: { $toDate: "$fecha" } } },
  { $match: { fechaReal: { $gte: ISODate("2026-01-01T00:00:00Z"), $lt: ISODate("2026-02-01T00:00:00Z") } } },
  { $project: { _id: 1 } },
  { $sort: { _id: 1 } }
])
// _id 1 y 3: ahora el texto "2026-01-20" también entra en el rango
```

:::note[Las comparaciones de rangos en `sort()` son distintas]
El orden entre tipos distintos (un `Number` antes que un `String`, un `String` antes que un `Date`, etc.) existe y se usa al **ordenar**, pero no en los operadores de comparación de `find()`. Son dos mecanismos diferentes.
:::

### Proyección

El segundo argumento de `find()` define qué campos se devuelven:

- `1` incluye el campo y `0` lo excluye.
- `_id` se incluye siempre, salvo que se escriba `_id: 0`.
- No se mezclan inclusiones y exclusiones en una proyección (la excepción es `_id`).

<!-- check: U4.T.CRUD.03 -->
```javascript
db.productos.find({ categoria: "perifericos" }, { _id: 0, nombre: 1, precio: 1 }).sort({ precio: -1 })
db.productos.find({ _id: 1 }, { etiquetas: 0, stock: 0 })
```

**Resultado esperado.**

| nombre | precio |
|---|---:|
| Webcam | 55 |
| Teclado | 45 |
| Mouse | 20 |

La segunda consulta devuelve `{ _id: 1, nombre: "Teclado", categoria: "perifericos", precio: 45 }`.

### `sort()`, `skip()` y `limit()`

`sort()` ordena (`1` ascendente, `-1` descendente, con varios campos en orden de prioridad), `skip(n)` omite los primeros `n` documentos y `limit(n)` devuelve como máximo `n`. Para una paginación estable se ordena siempre por un campo único (por ejemplo `_id`), porque sin orden explícito el resultado no está garantizado:

<!-- check: U4.T.CRUD.03 -->
```javascript
// Página 2, de 3 productos por página
db.productos.find({}, { nombre: 1 }).sort({ _id: 1 }).skip(3).limit(3)
```

**Resultado esperado.** `Notebook` (`_id` 4), `Auriculares` (5) y `Parlante` (6). Sin importar el orden en que se escriban los métodos, MongoDB aplica primero `sort`, luego `skip` y luego `limit`. En colecciones grandes `skip()` es costoso porque recorre los documentos omitidos; se prefiere paginar por rango de `_id`.

### `findOne()`, `countDocuments()` y `distinct()`

<!-- check: U4.T.CRUD.03 -->
```javascript
db.productos.findOne({ stock: 0 }, { _id: 0, nombre: 1 })         // { nombre: 'Auriculares' }
db.productos.findOne({ precio: { $gt: 5000 } })                   // null (no hay coincidencia)
db.productos.countDocuments()                                      // 8
db.productos.countDocuments({ precio: { $gt: 100 } })              // 3
db.productos.distinct("categoria")                                 // [ 'audio', 'computadoras', 'impresion', 'pantallas', 'perifericos' ]
db.productos.distinct("etiquetas")                                 // los valores individuales de los arrays
```

`findOne()` devuelve un documento (o `null`), no un cursor. `countDocuments()` cuenta con un filtro; `estimatedDocumentCount()` usa metadatos y es más rápida, pero no admite filtro. `distinct()` sobre un campo array devuelve cada valor individual sin repetir.

## Update: modificar documentos

<!-- sintaxis -->
```javascript
db.coleccion.updateOne(<filtro>, <actualización>, <opciones>)
db.coleccion.updateMany(<filtro>, <actualización>, <opciones>)
```

`updateOne()` modifica el primer documento que coincide; `updateMany()`, todos. La actualización usa **operadores**; si se pasa un documento sin operadores, el motor lo rechaza (para reemplazar el documento completo existe `replaceOne()`).

| Operador | Efecto |
|---|---|
| `$set` | Asigna un valor; crea el campo si no existe |
| `$unset` | Elimina un campo |
| `$inc` | Suma (o resta, con negativo) un número |
| `$mul` | Multiplica |
| `$rename` | Renombra un campo |
| `$push` | Agrega un elemento al final de un array (admite repetidos); `$each` agrega varios |
| `$addToSet` | Agrega solo si no está ya presente |
| `$pull` | Quita **todos** los elementos que coinciden |

<!-- check: U4.T.CRUD.05 -->
```javascript
db.productos.updateOne({ _id: 1 }, { $set: { precio: 50, ultimaRevision: ISODate("2026-07-01T00:00:00Z") } });
```

La respuesta es:

```text
{ acknowledged: true, insertedId: null, matchedCount: 1, modifiedCount: 1, upsertedCount: 0 }
```

`matchedCount` cuenta los documentos que coincidieron con el filtro y `modifiedCount`, los que cambiaron: repetir el mismo `$set` da `matchedCount: 1` y `modifiedCount: 0`. Un filtro sin coincidencias da `0` en ambos y no es un error.

### `$unset`, `$inc` y `$mul`

<!-- check: U4.T.CRUD.05 -->
```javascript
db.productos.updateOne({ _id: 1 }, { $unset: { ultimaRevision: "" } });       // el valor "" se ignora
db.productos.updateMany({ categoria: "perifericos" }, { $inc: { stock: -1 } }); // matchedCount 3, modifiedCount 3
db.productos.updateOne({ _id: 4 }, { $mul: { precio: 2 } });                    // precio: 1800
db.productos.updateMany({ stock: { $lte: 3 } }, { $set: { reponer: true } });   // marca los productos con poco stock
```

Tras el `$inc`, Mouse queda con 29 de stock, Teclado con 11 y Webcam con 13.

### Arrays: `$push`, `$addToSet` y `$pull`

El campo `etiquetas` del producto 2 parte de `["usb"]`:

<!-- check: U4.T.CRUD.05 -->
```javascript
db.productos.updateOne({ _id: 2 }, { $push: { etiquetas: "usb" } });         // ["usb", "usb"]       (permite repetir)
db.productos.updateOne({ _id: 2 }, { $addToSet: { etiquetas: "usb" } });     // ["usb", "usb"]       (ya estaba: no agrega)
db.productos.updateOne({ _id: 2 }, { $addToSet: { etiquetas: "gamer" } });   // ["usb", "usb", "gamer"]
db.productos.updateOne({ _id: 2 }, { $pull: { etiquetas: "usb" } });         // ["gamer"]            (quita las dos)
db.productos.updateOne({ _id: 2 }, { $push: { etiquetas: { $each: ["a", "b"] } } });   // ["gamer", "a", "b"]
```

`$set`, `$inc` y los demás actúan sobre campos anidados con notación de punto (`{ $set: { "direccion.ciudad": "Morón" } }`). `$rename` cambia el nombre de un campo en todos los documentos que lo tienen.

### `upsert`: actualizar o insertar

Con la opción `{ upsert: true }`, si **ningún documento** coincide con el filtro, el motor **inserta uno nuevo** construido con los campos de igualdad del filtro más la actualización. Si hay coincidencia, actualiza como siempre. `$setOnInsert` define campos que se asignan solo cuando se inserta.

<!-- check: U4.T.CRUD.06 -->
```javascript
// 1) No existe el _id 20: se inserta
db.productos.updateOne(
  { _id: 20 },
  { $set: { nombre: "Hub USB", precio: 25 }, $setOnInsert: { stock: 0 } },
  { upsert: true }
);

// 2) Ahora existe: se actualiza y $setOnInsert se ignora
db.productos.updateOne(
  { _id: 20 },
  { $set: { nombre: "Hub USB", precio: 30 }, $setOnInsert: { stock: 99 } },
  { upsert: true }
);
```

**Resultado esperado.**

| Llamada | `matchedCount` | `modifiedCount` | `upsertedCount` | Id del documento insertado | Documento resultante |
|---|---:|---:|---:|---|---|
| 1 | 0 | 0 | 1 | `20` | `{ _id: 20, nombre: "Hub USB", precio: 25, stock: 0 }` |
| 2 | 1 | 1 | 0 | (ninguno) | `{ _id: 20, nombre: "Hub USB", precio: 30, stock: 0 }` |

:::note[Dónde aparece el `_id` insertado]
En el resultado de `updateOne()` en `mongosh` 2.x el `_id` del documento insertado figura en **`insertedId`** (con `upsertedCount: 1`), y vale `null` cuando no hubo inserción; los drivers lo llaman `upsertedId`. En el resultado de `bulkWrite()` aparece como `upsertedIds`, un objeto que asocia la posición de la operación con el `_id`. En las dos formas, `upsertedCount` es la señal confiable de que se insertó.
:::

Cuando el filtro no fija el `_id`, MongoDB genera un `ObjectId`:

<!-- check: U4.T.CRUD.06 -->
```javascript
db.productos.updateOne({ nombre: "Cargador" }, { $inc: { stock: 5 } }, { upsert: true });
// upsertedCount: 1; el documento nuevo es { _id: ObjectId('…'), nombre: "Cargador", stock: 5 }
```

Observá que el documento nuevo tomó `nombre: "Cargador"` del filtro de igualdad y `stock: 5` del `$inc` aplicado a un campo inexistente.

:::caution[Upsert y duplicados]
Un `upsert` con un filtro poco selectivo, ejecutado en paralelo por dos clientes, puede insertar dos documentos si no hay un índice único sobre los campos del filtro. Se garantiza la unicidad con un índice único (ver [índices](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/#índice-único)).
:::

### `replaceOne()` y `findOneAndUpdate()`

`replaceOne()` reemplaza **todo** el documento (salvo `_id`) por el nuevo, sin operadores: los campos que no se repiten desaparecen.

<!-- check: U4.T.CRUD.06 -->
```javascript
db.productos.replaceOne({ _id: 20 }, { nombre: "Hub USB 3.0", precio: 35 });   // queda { _id: 20, nombre: "Hub USB 3.0", precio: 35 } (sin stock)
db.productos.findOneAndUpdate({ _id: 20 }, { $inc: { precio: 5 } }, { returnDocument: "after" });   // devuelve el documento ya modificado
```

`findOneAndUpdate()` modifica y devuelve el documento en una sola operación atómica, útil para contadores o colas.

## Delete: eliminar documentos

<!-- check: U4.T.CRUD.06 -->
```javascript
db.productos.deleteOne({ _id: 20 });                  // { acknowledged: true, deletedCount: 1 }
db.productos.deleteOne({ _id: 20 });                  // { acknowledged: true, deletedCount: 0 }   (ya no existe)
db.productos.deleteMany({ stock: { $lte: 3 } });      // elimina todos los que coinciden
```

`deleteOne()` elimina solo el primer documento que coincide aunque haya varios; `deleteMany({})` con filtro vacío **vacía la colección** (los índices permanecen); `drop()` elimina la colección y sus índices.

:::caution[`remove()` está obsoleto]
`db.coleccion.remove()` es el método heredado: en `mongosh` muestra `DeprecationWarning: Collection.remove() is deprecated. Use deleteOne, deleteMany, findOneAndDelete, or bulkWrite.` Se lo ve en código y en apuntes antiguos; en código nuevo se usa `deleteOne()` o `deleteMany()`. Lo mismo vale para `insert()` y `update()`, reemplazados por `insertOne()`/`insertMany()` y `updateOne()`/`updateMany()`.
:::

## `bulkWrite()`: varias escrituras en una llamada

`bulkWrite()` envía un conjunto de operaciones de distinto tipo en un solo viaje al servidor. Cada elemento es un documento con el tipo de operación como clave: `insertOne`, `updateOne`, `updateMany`, `replaceOne`, `deleteOne` o `deleteMany`.

<!-- check: U4.T.CRUD.07 -->
```javascript
const r = db.productos.bulkWrite([
  { insertOne: { document: { _id: 30, nombre: "Soporte", categoria: "accesorios", precio: 18, stock: 40 } } },
  { updateOne: { filter: { _id: 1 }, update: { $inc: { stock: 10 } } } },
  { updateMany: { filter: { categoria: "audio" }, update: { $set: { promo: true } } } },
  { replaceOne: { filter: { _id: 8 }, replacement: { nombre: "Impresora laser", categoria: "impresion", precio: 250, stock: 2 } } },
  { updateOne: { filter: { _id: 31 }, update: { $set: { nombre: "Funda", precio: 12 } }, upsert: true } },
  { deleteOne: { filter: { _id: 7 } } },
  { deleteMany: { filter: { precio: { $gt: 800 } } } }
]);
```

**Resultado esperado.**

| Campo | Valor | Origen |
|---|---:|---|
| `insertedCount` | 1 | el `insertOne` |
| `matchedCount` | 4 | un `updateOne` (1), el `updateMany` de audio (2) y el `replaceOne` (1) |
| `modifiedCount` | 4 | los mismos cuatro |
| `upsertedCount` | 1 | el `updateOne` con `upsert` (`upsertedIds: { '4': 31 }`, la posición 4 de la lista) |
| `deletedCount` | 2 | el `deleteOne` (Webcam) y el `deleteMany` (Notebook) |

Como `insertMany()`, `bulkWrite()` es **ordenada** por defecto y se detiene en el primer error. Con `{ ordered: false }` ejecuta el resto y reporta los errores al final, y el motor puede reordenar las operaciones para ser más eficiente:

<!-- check: U4.T.CRUD.07 -->
```javascript
try {
  db.productos.bulkWrite([
    { insertOne: { document: { _id: 30, nombre: "Repetido" } } },   // _id repetido: falla
    { insertOne: { document: { _id: 32, nombre: "Nuevo" } } }       // se inserta igual
  ], { ordered: false });
} catch (e) {
  print(e.code, e.result.insertedCount);    // 11000, 1
}
```

Si las operaciones tienen que ser todo o nada, se necesita una **transacción** (MongoDB las admite en conjuntos de réplicas y clústeres; ver [Transacciones](/bbdd-aplicadas/unidad-2/practica/transacciones/) para el concepto); `bulkWrite()` por sí solo no lo garantiza.

## Errores frecuentes

:::caution[Errores frecuentes]
- Escribir `updateOne({ _id: 1 }, { precio: 50 })` sin `$set`: el motor lo rechaza porque la actualización no usa operadores. Para reemplazar el documento se usa `replaceOne()`.
- Comparar un campo de fecha guardado como texto con límites `Date`: no hay error, simplemente no devuelve esos documentos.
- Usar `$and` con la misma clave repetida en un objeto literal: la segunda clave pisa a la primera.
- Esperar que `{ "items.productoId": 2, "items.cantidad": { $gte: 2 } }` evalúe ambas condiciones sobre el mismo ítem: para eso se usa `$elemMatch`.
- Paginar con `skip()` sin `sort()`: el orden del resultado no está garantizado.
- Ejecutar `deleteMany({})` creyendo que elimina la colección: solo vacía los documentos.
:::

## Autoevaluación

<details>
<summary>1. ¿Qué diferencia hay entre `insertMany()` con `ordered: true` y con `ordered: false` cuando el segundo de tres documentos es un duplicado?</summary>

Con `ordered: true` se inserta el primero, falla el segundo (E11000) y el tercero no se intenta. Con `ordered: false` se insertan el primero y el tercero, y se informa un error. En ninguno de los dos casos se deshace el primer documento.

</details>

<details>
<summary>2. Un `updateOne()` con `upsert: true` devuelve `matchedCount: 0` y `upsertedCount: 1`. ¿Qué pasó?</summary>

Ningún documento coincidía con el filtro, así que el motor insertó uno nuevo, armado con el filtro de igualdad y la actualización.

</details>

<details>
<summary>3. Un campo fecha contiene tanto valores Date como textos. Una consulta de rango con un límite Date, ¿qué devuelve?</summary>

Por ejemplo, `{ fecha: { $gte: ISODate("2026-01-01") } }`.

Solo los documentos cuyo `fecha` es un `Date`, porque los operadores de comparación solo comparan valores del mismo tipo (type bracketing). Los textos no coinciden y no se informa ningún error.

</details>

:::tip[En resumen]
- `insertMany()` y `bulkWrite()` son ordenadas por defecto; `ordered: false` continúa tras un error. Ninguna es una transacción.
- `find()` combina filtro, proyección, `sort`, `skip` y `limit`; `$elemMatch` evalúa varias condiciones sobre el mismo elemento de un array.
- Los operadores de comparación solo comparan valores del mismo tipo (type bracketing): una fecha como texto queda fuera de los rangos de `Date`.
- `updateOne()` y `updateMany()` usan operadores (`$set`, `$unset`, `$inc`, `$push`, `$addToSet`, `$pull`); `upsert: true` inserta si no hay coincidencia.
- `deleteOne()` y `deleteMany()` reemplazan al obsoleto `remove()`.
:::

:::tip[Para seguir]
- Practicá con los ejercicios 1 a 7 de la [Práctica — Unidad 4 NoSQL / MongoDB](/bbdd-aplicadas/unidad-4/practica/ejercicios/) y después seguí con [Aggregation Pipeline, índices y vistas](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/).
:::

## Fuentes

- Presentación de cátedra, Unidad 4, parte 1 (MQL, CRUD) y guía de trabajos prácticos de MongoDB.
- MongoDB Manual 7.0, *CRUD Operations*, *Query and Projection Operators*, *Update Operators*, *Bulk Write Operations* y *Comparison/Sort Order*: https://www.mongodb.com/docs/manual/.
