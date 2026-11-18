---
title: Práctica — Unidad 4 NoSQL / MongoDB
slug: bbdd-aplicadas/unidad-4/practica/ejercicios
sidebar:
  order: 1
  label: Unidad 4 NoSQL / MongoDB
---

[← Unidad 4](/bbdd-aplicadas/unidad-4/teoria/)

Ejercicios de práctica sobre las ventas de una cadena ficticia de ferreterías. Se trabajan operaciones CRUD (con `upsert` y `bulkWrite`), filtros con operadores de arrays y de fechas, proyección y orden, índices con `explain`, agregación (`$group`, `$unwind`, `$lookup`, `$facet`, `$bucket`) y vistas. Todos los ejercicios están resueltos y verificados con MongoDB 7.0.

:::note[Qué cambió en esta práctica]
La versión anterior mezclaba consignas con conjuntos de datos de distinto origen (estrellas, un ejemplo público de alquileres, transacciones con tarjetas y un archivo de ventas coincidente con una guía de cátedra) y con descargas externas. Se reemplazó por ejercicios originales sobre un conjunto de datos propio y publicado, con resolución y resultado esperado. Quedaron resueltos estos defectos: la consulta con `$not` que no filtraba, el ejercicio que reinsertaba documentos ya cargados y la vista creada con un nombre y consultada con otro. Los ejercicios de importación desde Compass, de las colecciones de clima y de tarjetas se retiraron porque dependían de descargas externas o de datos de procedencia no documentada.
:::

## Antes de empezar

Esta práctica presupone las lecciones de [CRUD en MongoDB](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/) y de [agregación](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/), y haber instalado una instancia de MongoDB 7.0 o posterior con `mongosh` ([instalación](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/)).

## Conjunto de datos

Datos sintéticos, escritos para esta práctica. Descargá los archivos (formato JSON extendido, con fechas `Date`) en una carpeta:

- [`ventas.json`](/bbdd-aplicadas/unidad-4/practica/archivos/ventas/ventas.json)
- [`vendedores.json`](/bbdd-aplicadas/unidad-4/practica/archivos/ventas/vendedores.json)

| Colección | Documentos | Contenido |
|---|---:|---|
| `ventas` | 24 | `idVenta`, `fecha`, `sucursal`, `idVendedor`, `medioPago`, `cliente` (documento embebido), `articulos` (array de documentos con `codigo`, `descripcion`, `categoria`, `cantidad`, `precioUnitario`), `total` y, solo en algunas, `descuento` y `etiquetas` |
| `vendedores` | 7 | `idVendedor`, `nombre`, `sucursal`, `zona`, `ingreso` (el vendedor 7 no tiene ventas) |

El campo `total` es el importe bruto de la venta: suma `cantidad * precioUnitario` y no descuenta `descuento`.

### Preparación

Ejecutá este script en `mongosh`, conectado a una base vacía (por ejemplo, `use ferreteria`). Cambiá `dir` por la carpeta donde guardaste los archivos. Cada ejercicio parte de esta carga; si uno modifica datos, volvé a cargar una base vacía antes del siguiente (`db.dropDatabase()` y este script).

<!-- check: U4.PR.VENTAS -->
```javascript
const fs = require("fs");
const dir = "C:/datos/ventas";   // reemplazá por la carpeta donde guardaste los archivos
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));

cargar("ventas");
cargar("vendedores");

print("ventas: " + db.ventas.countDocuments() + ", " +
      "vendedores: " + db.vendedores.countDocuments());
```

**Resultado esperado.**

```text
ventas: 24, vendedores: 7
```

La función `mostrar()` imprime un documento por línea en formato JSON, con las fechas en formato extendido (`{"$date": ...}`). Es lo que se usa en todos los resultados esperados; en `mongosh` podés omitirla y dejar que el cursor se imprima solo.

:::caution[Cada ejercicio parte de datos limpios]
Los ejercicios 4, 6, 7, 10 y 13 crean o modifican colecciones, índices o vistas. Si repetís la carga sin vaciar la base, los documentos se duplican (cada uno recibe un `_id` distinto) y los resultados esperados dejan de coincidir.
:::

## Nivel inicial

### Ejercicio 1 · Ventas grandes de una sucursal
<!-- ejercicio: U4.01 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Listá las ventas de la sucursal `Norte` con un `total` de 75000 pesos o más. Mostrá solo `idVenta`, `fecha` y `total`, de la más alta a la más baja; ante un empate, por `idVenta` ascendente.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** El filtro combina dos condiciones con una coma (equivale a un `AND`). El segundo argumento de `find()` es la proyección: se excluye `_id` explícitamente porque se incluye por defecto. El orden va en `sort()` con `-1` para descendente.

<!-- check: U4.01 -->
```javascript
mostrar(db.ventas.find(
  { sucursal: "Norte", total: { $gte: 75000 } },
  { _id: 0, idVenta: 1, fecha: 1, total: 1 }
).sort({ total: -1, idVenta: 1 }))
```

**Resultado esperado.**

```text
{"idVenta":10,"fecha":{"$date":"2025-04-26T00:00:00Z"},"total":158400}
{"idVenta":1,"fecha":{"$date":"2025-01-17T00:00:00Z"},"total":150600}
{"idVenta":13,"fecha":{"$date":"2025-05-29T00:00:00Z"},"total":140000}
{"idVenta":19,"fecha":{"$date":"2025-08-03T00:00:00Z"},"total":99200}
{"idVenta":7,"fecha":{"$date":"2025-03-24T00:00:00Z"},"total":79600}
{"idVenta":22,"fecha":{"$date":"2025-09-05T00:00:00Z"},"total":75200}
```

Hay seis ventas que cumplen las dos condiciones. `$gte` incluye el límite: la venta 22 vale 75200 y entra. En una proyección no se pueden mezclar inclusiones y exclusiones, salvo la exclusión de `_id`.

</details>

### Ejercicio 2 · Ventas de un trimestre pagadas con tarjeta
<!-- ejercicio: U4.02 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Obtené las ventas realizadas en el segundo trimestre de 2025 (abril a junio) cuyo `medioPago` sea `debito` o `credito`. Mostrá `idVenta`, `fecha` y `medioPago`, ordenadas por fecha.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un rango de fechas se expresa con un límite inferior cerrado (`$gte`) y uno superior abierto (`$lt`): así no hace falta calcular el último instante del día. Para elegir entre varios valores del mismo campo se usa `$in`.

<!-- check: U4.02 -->
```javascript
mostrar(db.ventas.find(
  {
    fecha: { $gte: ISODate("2025-04-01T00:00:00Z"), $lt: ISODate("2025-07-01T00:00:00Z") },
    medioPago: { $in: ["debito", "credito"] }
  },
  { _id: 0, idVenta: 1, fecha: 1, medioPago: 1 }
).sort({ fecha: 1 }))
```

**Resultado esperado.**

```text
{"idVenta":10,"fecha":{"$date":"2025-04-26T00:00:00Z"},"medioPago":"credito"}
{"idVenta":11,"fecha":{"$date":"2025-05-07T00:00:00Z"},"medioPago":"debito"}
{"idVenta":14,"fecha":{"$date":"2025-06-09T00:00:00Z"},"medioPago":"credito"}
{"idVenta":15,"fecha":{"$date":"2025-06-20T00:00:00Z"},"medioPago":"debito"}
```

El límite superior es el 1 de julio, que queda afuera. Las fechas son `Date` en UTC; si se compara contra cadenas, el filtro no encuentra nada. Con `$in` evitamos repetir el campo en un `$or`.

</details>

### Ejercicio 3 · Campos ausentes y el operador de negación
<!-- ejercicio: U4.03 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
El campo `descuento` existe solo en algunas ventas. Contá las ventas que cumplen cada una de estas condiciones y explicá por qué los resultados difieren: `descuento < 10`, `descuento` que no sea `>= 10`, sin el campo `descuento`, y con el campo pero que no sea `>= 10`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Comparamos los cuatro filtros con `countDocuments()`. La clave es que los operadores de comparación solo evalúan documentos donde el campo existe, mientras que `$not` invierte el resultado de la condición e incluye también los documentos donde el campo falta.

<!-- check: U4.03 -->
```javascript
const contar = (filtro) => db.ventas.countDocuments(filtro);
print("lt 10:                     " + contar({ descuento: { $lt: 10 } }));
print("not gte 10:                " + contar({ descuento: { $not: { $gte: 10 } } }));
print("sin campo descuento:       " + contar({ descuento: { $exists: false } }));
print("con descuento y not gte 10: " + contar({ descuento: { $exists: true, $not: { $gte: 10 } } }));
```

**Resultado esperado.**

```text
lt 10:                     3
not gte 10:                21
sin campo descuento:       18
con descuento y not gte 10: 3
```

`{ descuento: { $lt: 10 } }` devuelve 3 documentos (los que tienen descuento de 5). `$not: { $gte: 10 }` devuelve 21 porque suma los 3 anteriores y las 18 ventas sin el campo; el total de 24 se completa con las 3 que tienen descuento de 10. Para quedarse solo con los documentos que tienen el campo hay que agregar `$exists: true`. Un filtro de negación que no cambia el resultado respecto de otro suele indicar que no se está evaluando lo que se cree.

</details>

### Ejercicio 4 · Validación de esquema al crear una colección
<!-- ejercicio: U4.04 | nivel: inicial | tipo: mql | verificacion: motor -->

:::note[Enunciado]
MongoDB no define columnas al crear una colección, pero permite exigir reglas con un validador. Creá la colección `gastos` que exija `descripcion` (cadena de al menos 3 caracteres) y `monto` (numérico, no negativo). Insertá un gasto válido y comprobá que se rechazan uno con monto negativo y otro sin `descripcion`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se usa `createCollection()` con la opción `validator` y un `$jsonSchema`. Con `validationAction: "error"` los documentos inválidos se rechazan. Capturamos el error con `try/catch` y mostramos su código.

<!-- check: U4.04 -->
```javascript
db.createCollection("gastos", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["descripcion", "monto"],
      properties: {
        descripcion: { bsonType: "string", minLength: 3 },
        monto: { bsonType: ["int", "long", "double", "decimal"], minimum: 0 }
      }
    }
  },
  validationAction: "error"
});

db.gastos.insertOne({ descripcion: "Flete", monto: 12500 });

try {
  db.gastos.insertOne({ descripcion: "Bolsas", monto: -50 });
} catch (e) {
  print("rechazado, codigo " + e.code);
}
try {
  db.gastos.insertOne({ monto: 300 });
} catch (e) {
  print("rechazado, codigo " + e.code);
}
print("documentos guardados: " + db.gastos.countDocuments());
```

**Resultado esperado.**

```text
rechazado, codigo 121
rechazado, codigo 121
documentos guardados: 1
```

El código 121 corresponde a `DocumentValidationFailure`. La colección termina con un solo documento. Los tipos se declaran con nombres BSON (`string`, `int`, `double`, `decimal`); aceptar varios tipos numéricos evita rechazar un monto entero o decimal. El validador controla las inserciones y las modificaciones; los documentos que ya existían en una colección no se revisan hasta que se modifican.

</details>

## Nivel intermedio

### Ejercicio 5 · Consultas sobre arrays
<!-- ejercicio: U4.05 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Resolvé estas cuatro consultas sobre `ventas`: (A) ventas con un artículo de la categoría `electricidad` y cantidad de 3 o más en ese mismo artículo; (B) ventas que tengan algún artículo de `electricidad` y algún artículo (cualquiera) con cantidad de 3 o más; (C) ventas con las etiquetas `promo` y `web`; (D) ventas con exactamente tres artículos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `$elemMatch` exige que todas las condiciones las cumpla un mismo elemento del array. Si las condiciones se escriben por separado con notación de punto, cada una puede cumplirla un elemento distinto. `$all` pide que el array contenga todos los valores indicados y `$size` compara la longitud.

<!-- check: U4.05 -->
```javascript
print("A) electricidad con cantidad >= 3 en el mismo articulo");
mostrar(db.ventas.find(
  { articulos: { $elemMatch: { categoria: "electricidad", cantidad: { $gte: 3 } } } },
  { _id: 0, idVenta: 1 }
).sort({ idVenta: 1 }));

print("B) las dos condiciones pueden cumplirlas articulos distintos");
mostrar(db.ventas.find(
  { "articulos.categoria": "electricidad", "articulos.cantidad": { $gte: 3 } },
  { _id: 0, idVenta: 1 }
).sort({ idVenta: 1 }));

print("C) etiquetas con promo y web");
mostrar(db.ventas.find({ etiquetas: { $all: ["promo", "web"] } }, { _id: 0, idVenta: 1, etiquetas: 1 }).sort({ idVenta: 1 }));

print("D) ventas con exactamente tres articulos");
mostrar(db.ventas.find({ articulos: { $size: 3 } }, { _id: 0, idVenta: 1 }).sort({ idVenta: 1 }));
```

**Resultado esperado.**

```text
A) electricidad con cantidad >= 3 en el mismo articulo
{"idVenta":2}
{"idVenta":4}
{"idVenta":15}
{"idVenta":17}
{"idVenta":22}
B) las dos condiciones pueden cumplirlas articulos distintos
{"idVenta":2}
{"idVenta":4}
{"idVenta":5}
{"idVenta":7}
{"idVenta":14}
{"idVenta":15}
{"idVenta":17}
{"idVenta":22}
C) etiquetas con promo y web
{"idVenta":3,"etiquetas":["promo","web"]}
{"idVenta":9,"etiquetas":["promo","web"]}
{"idVenta":15,"etiquetas":["promo","web"]}
D) ventas con exactamente tres articulos
{"idVenta":2}
{"idVenta":5}
{"idVenta":8}
{"idVenta":11}
{"idVenta":14}
{"idVenta":17}
{"idVenta":20}
{"idVenta":23}
```

La consulta A devuelve 5 ventas y la B, 8: la diferencia son ventas donde la cantidad alta está en un artículo y la categoría `electricidad` en otro. `$all` no exige un orden ni que no haya otras etiquetas. `$size` solo admite un número exacto; para rangos de longitud se usa una expresión en `$expr` o en una agregación.

</details>

### Ejercicio 6 · Actualizaciones con operadores
<!-- ejercicio: U4.06 | nivel: intermedio | tipo: mql | verificacion: motor -->

:::note[Enunciado]
Sobre `ventas`: (1) agregá la etiqueta `revisada` a las ventas de la sucursal `Sur` con total de 100000 o más, de modo que repetir la operación no duplique la etiqueta; (2) quitá `descuento` de las ventas con descuento de 5 y registrá `descuentoAplicado: false`; (3) sumá una unidad a la cantidad del primer artículo de la venta 1. Comprobá los resultados.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `$addToSet` agrega un valor a un array solo si no está, y crea el array si el campo no existe. `$unset` y `$set` se pueden combinar en una misma actualización. Para un elemento de array por posición se usa la notación `articulos.0.cantidad` con `$inc`. Ejecutar la actualización 1 dos veces muestra que es idempotente.

<!-- check: U4.06 -->
```javascript
const filtro = { sucursal: "Sur", total: { $gte: 100000 } };
const r1 = db.ventas.updateMany(filtro, { $addToSet: { etiquetas: "revisada" } });
print("primera vez: " + r1.matchedCount + " encontradas, " + r1.modifiedCount + " modificadas");
const r2 = db.ventas.updateMany(filtro, { $addToSet: { etiquetas: "revisada" } });
print("segunda vez: " + r2.matchedCount + " encontradas, " + r2.modifiedCount + " modificadas");

const r3 = db.ventas.updateMany({ descuento: 5 }, { $unset: { descuento: "" }, $set: { descuentoAplicado: false } });
print("sin descuento de 5: " + r3.modifiedCount + " modificadas");

const r4 = db.ventas.updateOne({ idVenta: 1 }, { $inc: { "articulos.0.cantidad": 1 } });
print("articulo 0 de la venta 1: " + r4.modifiedCount + " modificada");

mostrar(db.ventas.find({ etiquetas: "revisada" }, { _id: 0, idVenta: 1, etiquetas: 1 }).sort({ idVenta: 1 }));
mostrar(db.ventas.find({ idVenta: 1 }, { _id: 0, idVenta: 1, "articulos.codigo": 1, "articulos.cantidad": 1 }));
print("descuentoAplicado: " + db.ventas.countDocuments({ descuentoAplicado: false }));
```

**Resultado esperado.**

```text
primera vez: 5 encontradas, 5 modificadas
segunda vez: 5 encontradas, 0 modificadas
sin descuento de 5: 3 modificadas
articulo 0 de la venta 1: 1 modificada
{"idVenta":5,"etiquetas":["revisada"]}
{"idVenta":11,"etiquetas":["revisada"]}
{"idVenta":14,"etiquetas":["web","revisada"]}
{"idVenta":17,"etiquetas":["revisada"]}
{"idVenta":23,"etiquetas":["revisada"]}
{"idVenta":1,"articulos":[{"codigo":"PIN-04","cantidad":3},{"codigo":"CAN-08","cantidad":4}]}
descuentoAplicado: 3
```

La primera ejecución modifica 5 documentos y la segunda, ninguno, aunque encuentra los mismos 5: `matchedCount` cuenta coincidencias del filtro y `modifiedCount` cambios efectivos. La venta 14 ya tenía `["web"]` y recibió `revisada` al final. Usar la posición fija `0` es frágil si cambia el orden del array; con `arrayFilters` se puede apuntar a un elemento por su contenido.

</details>

### Ejercicio 7 · Upsert y operaciones en lote
<!-- ejercicio: U4.07 | nivel: intermedio | tipo: mql | verificacion: motor -->

:::note[Enunciado]
Creá la colección `stock` con tres documentos. Hacé un `upsert` que registre un mínimo para el código `TAL-01` en la sucursal `Sur` y ejecutalo dos veces. Luego, con un único `bulkWrite()` ordenado, descontá una unidad de `TAL-01` en `Centro`, fijá en 6 la cantidad de `MAR-02` en `Norte` (creándolo si falta), insertá `CAN-08` en `Sur` y borrá `TAL-01` en `Norte`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `updateOne()` con `upsert: true` inserta un documento nuevo cuando el filtro no coincide; `$setOnInsert` define campos que se escriben solo en ese caso. `bulkWrite()` agrupa operaciones heterogéneas en una sola llamada y devuelve los totales por tipo.

<!-- check: U4.07 -->
```javascript
db.stock.insertMany([
  { sucursal: "Centro", codigo: "TAL-01", cantidad: 4 },
  { sucursal: "Centro", codigo: "MAR-02", cantidad: 10 },
  { sucursal: "Norte", codigo: "TAL-01", cantidad: 2 }
]);

const reponer = () => db.stock.updateOne(
  { sucursal: "Sur", codigo: "TAL-01" },
  { $set: { minimo: 3 }, $setOnInsert: { cantidad: 0 } },
  { upsert: true }
);
const a = reponer();
print("upsert 1: encontradas " + a.matchedCount + ", insertadas " + a.upsertedCount);
const b = reponer();
print("upsert 2: encontradas " + b.matchedCount + ", insertadas " + b.upsertedCount + ", modificadas " + b.modifiedCount);

const lote = db.stock.bulkWrite([
  { updateOne: { filter: { sucursal: "Centro", codigo: "TAL-01" }, update: { $inc: { cantidad: -1 } } } },
  { updateOne: { filter: { sucursal: "Norte", codigo: "MAR-02" }, update: { $set: { cantidad: 6 } }, upsert: true } },
  { insertOne: { document: { sucursal: "Sur", codigo: "CAN-08", cantidad: 9 } } },
  { deleteOne: { filter: { sucursal: "Norte", codigo: "TAL-01" } } }
], { ordered: true });
print("insertados " + lote.insertedCount + ", encontrados " + lote.matchedCount + ", modificados " + lote.modifiedCount +
      ", upsert " + lote.upsertedCount + ", borrados " + lote.deletedCount);

mostrar(db.stock.aggregate([
  { $sort: { sucursal: 1, codigo: 1 } },
  { $project: { _id: 0, sucursal: "$sucursal", codigo: "$codigo", cantidad: "$cantidad", minimo: "$minimo" } }
]));
```

**Resultado esperado.**

```text
upsert 1: encontradas 0, insertadas 1
upsert 2: encontradas 1, insertadas 0, modificadas 0
insertados 1, encontrados 1, modificados 1, upsert 1, borrados 1
{"sucursal":"Centro","codigo":"MAR-02","cantidad":10}
{"sucursal":"Centro","codigo":"TAL-01","cantidad":3}
{"sucursal":"Norte","codigo":"MAR-02","cantidad":6}
{"sucursal":"Sur","codigo":"CAN-08","cantidad":9}
{"sucursal":"Sur","codigo":"TAL-01","cantidad":0,"minimo":3}
```

La primera llamada inserta (`upsertedCount: 1`) y la segunda encuentra el documento y no cambia nada: el upsert con `$set` y `$setOnInsert` es idempotente. En el lote, cada operación afecta a un documento distinto; con `ordered: true` se detendría ante el primer error. El upsert de `MAR-02` crea el documento con los campos del filtro más los de `$set`. Para mostrar el resultado se usa `$project` con expresiones: el orden de los campos de un documento creado por `upsert` puede variar, y así la salida queda fija.

</details>

### Ejercicio 8 · Ventas por mes
<!-- ejercicio: U4.08 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Calculá, para cada mes de 2025, la cantidad de ventas, el total facturado, el promedio (redondeado a dos decimales) y la venta de mayor importe. Ordená por mes.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se agrupa con `$group` usando como clave el mes, que se obtiene con `$dateToString` y el formato `%Y-%m`. Los acumuladores `$sum`, `$avg` y `$max` calculan las métricas; `$sort` ordena por la clave y `$project` renombra `_id` y redondea con `$round`.

<!-- check: U4.08 -->
```javascript
mostrar(db.ventas.aggregate([
  { $group: {
      _id: { $dateToString: { format: "%Y-%m", date: "$fecha" } },
      ventas: { $sum: 1 },
      total: { $sum: "$total" },
      promedio: { $avg: "$total" },
      mayor: { $max: "$total" }
  } },
  { $sort: { _id: 1 } },
  { $project: { _id: 0, mes: "$_id", ventas: "$ventas", total: "$total", promedio: { $round: ["$promedio", 2] }, mayor: "$mayor" } }
]))
```

**Resultado esperado.**

```text
{"mes":"2025-01","ventas":2,"total":247300,"promedio":123650,"mayor":150600}
{"mes":"2025-02","ventas":2,"total":55100,"promedio":27550,"mayor":36500}
{"mes":"2025-03","ventas":3,"total":220050,"promedio":73350,"mayor":137200}
{"mes":"2025-04","ventas":3,"total":227750,"promedio":75916.67,"mayor":158400}
{"mes":"2025-05","ventas":3,"total":344700,"promedio":114900,"mayor":195800}
{"mes":"2025-06","ventas":2,"total":293400,"promedio":146700,"mayor":183800}
{"mes":"2025-07","ventas":3,"total":187250,"promedio":62416.67,"mayor":134400}
{"mes":"2025-08","ventas":3,"total":234950,"promedio":78316.67,"mayor":99200}
{"mes":"2025-09","ventas":3,"total":254200,"promedio":84733.33,"mayor":169200}
```

El mes se calcula en UTC. El orden de los grupos de `$group` no está garantizado, por eso el `$sort` va después. Marzo tiene 3 ventas por 220050 pesos, un promedio de 73350.

</details>

### Ejercicio 9 · Artículos más vendidos
<!-- ejercicio: U4.09 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Obtené los cinco artículos con más unidades vendidas, junto con lo facturado por cada uno (cantidad por precio unitario). Ante un empate de unidades, ordená por código.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los artículos están dentro de un array, así que primero `$unwind` genera un documento por artículo. Después `$group` por código acumula las unidades y el importe calculado con `$multiply`; `$sort` y `$limit` arman el ranking.

<!-- check: U4.09 -->
```javascript
mostrar(db.ventas.aggregate([
  { $unwind: "$articulos" },
  { $group: {
      _id: "$articulos.codigo",
      unidades: { $sum: "$articulos.cantidad" },
      facturado: { $sum: { $multiply: ["$articulos.cantidad", "$articulos.precioUnitario"] } }
  } },
  { $sort: { unidades: -1, _id: 1 } },
  { $limit: 5 }
]))
```

**Resultado esperado.**

```text
{"_id":"SIL-10","unidades":26,"facturado":80600}
{"_id":"ROD-05","unidades":21,"facturado":90300}
{"_id":"CAN-08","unidades":16,"facturado":347200}
{"_id":"CIN-09","unidades":16,"facturado":10400}
{"_id":"PIN-04","unidades":16,"facturado":510400}
```

Tres artículos empatan con 16 unidades (`CAN-08`, `CIN-09` y `PIN-04`) y quedan ordenados por código; sin el segundo criterio de orden, el empate se resolvería de forma arbitraria. Notá que el más vendido en unidades (`SIL-10`) no es el que más factura: el ranking cambia según la métrica.

</details>

### Ejercicio 10 · Índice compuesto y plan de ejecución
<!-- ejercicio: U4.10 | nivel: intermedio | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
Para la consulta que busca las ventas de la sucursal `Norte` ordenadas por `fecha` descendente, comparé el plan de ejecución antes y después de crear un índice compuesto. Informá las etapas, los documentos devueltos y los examinados.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un índice compuesto `{ sucursal: 1, fecha: -1 }` sirve al filtro por igualdad en el primer campo y al orden por el segundo. Con `explain("executionStats")` se leen las etapas del plan ganador y las cifras de ejecución. Se resumen solo valores estables, sin tiempos.

<!-- check: U4.10 -->
```javascript
const resumen = (plan) => {
  let nodo = plan.queryPlanner.winningPlan;
  const etapas = [];
  let indice = null;
  while (nodo) {
    etapas.push(nodo.stage);
    if (nodo.stage === "IXSCAN") indice = nodo.indexName;
    nodo = nodo.inputStage;
  }
  const e = plan.executionStats;
  return { etapas: etapas.join(" > "), indice: indice, devueltos: e.nReturned, examinados: e.totalDocsExamined };
};
const consulta = () => db.ventas.find({ sucursal: "Norte" }).sort({ fecha: -1 });

print("sin indice: " + JSON.stringify(resumen(consulta().explain("executionStats"))));
db.ventas.createIndex({ sucursal: 1, fecha: -1 }, { name: "ixSucursalFecha" });
print("con indice: " + JSON.stringify(resumen(consulta().explain("executionStats"))));
```

**Resultado esperado.**

```text
sin indice: {"etapas":"SORT > COLLSCAN","indice":null,"devueltos":8,"examinados":24}
con indice: {"etapas":"FETCH > IXSCAN","indice":"ixSucursalFecha","devueltos":8,"examinados":8}
```

Sin índice el plan es `SORT > COLLSCAN`: recorre las 24 ventas y ordena en memoria para devolver 8. Con el índice es `FETCH > IXSCAN`: examina solo 8 entradas y no necesita ordenar, porque el índice ya entrega las claves en el orden pedido. Con tan pocos documentos la diferencia de tiempo es irrelevante; la cantidad de documentos examinados es la medida que escala.

</details>

## Nivel avanzado

### Ejercicio 11 · Ventas por vendedor, incluso sin ventas
<!-- ejercicio: U4.11 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Listá todos los vendedores con su zona, la cantidad de ventas y lo facturado, incluidos los que no vendieron. Ordená por facturación descendente.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se parte de `vendedores` y se une con `ventas` mediante `$lookup`; así el vendedor sin ventas queda con un array vacío en lugar de desaparecer, como ocurriría si se partiera de `ventas`. `$size` cuenta las ventas y `$sum` sobre la ruta `$ventas.total` suma los importes del array.

<!-- check: U4.11 -->
```javascript
mostrar(db.vendedores.aggregate([
  { $lookup: { from: "ventas", localField: "idVendedor", foreignField: "idVendedor", as: "ventas" } },
  { $project: {
      _id: 0, idVendedor: 1, zona: 1,
      cantidadVentas: { $size: "$ventas" },
      facturado: { $sum: "$ventas.total" }
  } },
  { $sort: { facturado: -1, idVendedor: 1 } }
]))
```

**Resultado esperado.**

```text
{"idVendedor":2,"zona":"Norte","cantidadVentas":4,"facturado":636600}
{"idVendedor":6,"zona":"Sur","cantidadVentas":4,"facturado":469400}
{"idVendedor":5,"zona":"Norte","cantidadVentas":4,"facturado":378400}
{"idVendedor":3,"zona":"Sur","cantidadVentas":4,"facturado":301450}
{"idVendedor":4,"zona":"Oeste","cantidadVentas":4,"facturado":235400}
{"idVendedor":1,"zona":"Oeste","cantidadVentas":4,"facturado":43450}
{"idVendedor":7,"zona":"Oeste","cantidadVentas":0,"facturado":0}
```

El vendedor 7 aparece con 0 ventas y 0 facturado. En SQL equivale a un `LEFT JOIN` con `GROUP BY`. Cuando el `$lookup` trae muchos documentos por cada uno de origen, conviene resumirlos con un `pipeline` dentro del propio `$lookup` en lugar de materializar el array completo.

</details>

### Ejercicio 12 · Varios resúmenes en una sola consulta
<!-- ejercicio: U4.12 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con una única agregación sobre `ventas`, devolvé: la cantidad de ventas por medio de pago, la cantidad de ventas por rango de total (0 a 19999, 20000 a 99999 y 100000 a 199999, con una categoría para el resto) y los totales generales.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `$facet` ejecuta varios sub-pipelines sobre los mismos documentos de entrada y devuelve un único documento con un array por cada uno. `$bucket` agrupa por rangos definidos en `boundaries`: cada rango incluye el límite inferior y excluye el superior.

<!-- check: U4.12 -->
```javascript
mostrar(db.ventas.aggregate([
  { $facet: {
      porMedioPago: [
        { $group: { _id: "$medioPago", ventas: { $sum: 1 } } },
        { $sort: { _id: 1 } }
      ],
      porRangoDeTotal: [
        { $bucket: {
            groupBy: "$total",
            boundaries: [0, 20000, 100000, 200000],
            default: "200000 o mas",
            output: { ventas: { $sum: 1 } }
        } }
      ],
      totalGeneral: [
        { $group: { _id: null, ventas: { $sum: 1 }, facturado: { $sum: "$total" } } },
        { $project: { _id: 0 } }
      ]
  } }
]))
```

**Resultado esperado.**

```text
{"porMedioPago":[{"_id":"credito","ventas":6},{"_id":"debito","ventas":6},{"_id":"efectivo","ventas":6},{"_id":"transferencia","ventas":6}],"porRangoDeTotal":[{"_id":0,"ventas":4},{"_id":20000,"ventas":11},{"_id":100000,"ventas":9}],"totalGeneral":[{"ventas":24,"facturado":2064700}]}
```

El resultado es un solo documento. Cada medio de pago tiene 6 ventas. En `porRangoDeTotal`, la clave `_id` es el límite inferior del rango: 4 ventas en el primero, 11 en el segundo y 9 en el tercero; ninguna llega a 200000, por lo que la categoría `default` no aparece. El documento resultante tiene que entrar en el límite de tamaño de un documento BSON (16 MB), lo que condiciona el uso de `$facet` con resultados grandes.

</details>

### Ejercicio 13 · Una vista con datos del vendedor
<!-- ejercicio: U4.13 | nivel: avanzado | tipo: mql | verificacion: motor -->

:::note[Enunciado]
Creá la vista `ventasConVendedor` con las ventas desde julio de 2025, el nombre y la zona del vendedor. Consultala por zona, agrupala por zona y comprobá que refleja una venta insertada después de crearla.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** `createView()` recibe el nombre de la vista, la colección de origen y el pipeline. La vista no guarda datos: ejecuta el pipeline cada vez que se consulta, y se la consulta con el mismo nombre con que se creó.

<!-- check: U4.13 -->
```javascript
db.createView("ventasConVendedor", "ventas", [
  { $match: { fecha: { $gte: ISODate("2025-07-01T00:00:00Z") } } },
  { $lookup: { from: "vendedores", localField: "idVendedor", foreignField: "idVendedor", as: "vendedor" } },
  { $unwind: "$vendedor" },
  { $project: { _id: 0, idVenta: 1, fecha: 1, total: 1, vendedor: "$vendedor.nombre", zona: "$vendedor.zona" } }
]);

mostrar(db.ventasConVendedor.find({ zona: "Oeste" }).sort({ idVenta: 1 }));
mostrar(db.ventasConVendedor.aggregate([
  { $group: { _id: "$zona", ventas: { $sum: 1 }, total: { $sum: "$total" } } },
  { $sort: { _id: 1 } }
]));

const info = db.getCollectionInfos({ name: "ventasConVendedor" })[0];
print(info.type + " sobre " + info.options.viewOn);
db.ventas.insertOne({ idVenta: 99, fecha: ISODate("2025-10-01T00:00:00Z"), idVendedor: 1, total: 1000 });
print("la vista refleja el alta: " + (db.ventasConVendedor.countDocuments({ idVenta: 99 }) === 1));
```

**Resultado esperado.**

```text
{"idVenta":18,"fecha":{"$date":"2025-07-23T00:00:00Z"},"total":21500,"vendedor":"Vendedor 01","zona":"Oeste"}
{"idVenta":21,"fecha":{"$date":"2025-08-25T00:00:00Z"},"total":63800,"vendedor":"Vendedor 04","zona":"Oeste"}
{"idVenta":24,"fecha":{"$date":"2025-09-27T00:00:00Z"},"total":9800,"vendedor":"Vendedor 01","zona":"Oeste"}
{"_id":"Norte","ventas":3,"total":375550}
{"_id":"Oeste","ventas":3,"total":95100}
{"_id":"Sur","ventas":3,"total":205750}
view sobre ventas
la vista refleja el alta: true
```

La vista se consulta con `find()` y `aggregate()` como una colección más; `getCollectionInfos()` informa su tipo y su origen. La venta 99 se agrega a `ventas` y aparece de inmediato en la vista, porque no hay copia almacenada. Es una vista de solo lectura: para cambiar su definición hay que eliminarla y volver a crearla, o usar `collMod`.

</details>
