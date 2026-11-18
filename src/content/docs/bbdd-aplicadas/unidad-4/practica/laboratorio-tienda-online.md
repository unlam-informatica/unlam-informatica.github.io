---
title: Laboratorio Práctico — tienda_online
slug: bbdd-aplicadas/unidad-4/practica/laboratorio-tienda-online
sidebar:
  order: 2
  label: Laboratorio — Tienda online
---

[← Unidad 4](/bbdd-aplicadas/unidad-4/teoria/)

Laboratorio sobre una tienda en línea ficticia. Combina CRUD con tipos exactos (`Decimal128`), consultas sobre arrays y documentos embebidos, uniones con `$lookup`, resúmenes con `$facet` y `$bucket`, e índices único, compuesto y TTL. Los datos y las resoluciones son propios y están verificados con MongoDB 7.0.

:::note[Material propio]
Este laboratorio es una elaboración de este portal, no de la cátedra. Reemplaza al laboratorio anterior, que dependía de scripts que no estaban publicados y de una API externa.
:::

## Antes de empezar

Presupone las lecciones de [CRUD](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/) y de [agregación](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/). Conviene haber hecho antes la [práctica de ventas](/bbdd-aplicadas/unidad-4/practica/ejercicios/).

## Conjunto de datos

Datos sintéticos; los correos usan el dominio reservado `ejemplo.test`. Descargá los archivos en una carpeta:

- [`productos.json`](/bbdd-aplicadas/unidad-4/practica/archivos/tienda/productos.json)
- [`clientes.json`](/bbdd-aplicadas/unidad-4/practica/archivos/tienda/clientes.json)
- [`pedidos.json`](/bbdd-aplicadas/unidad-4/practica/archivos/tienda/pedidos.json)
- [`resenas.json`](/bbdd-aplicadas/unidad-4/practica/archivos/tienda/resenas.json)

| Colección | Documentos | Campos principales |
|---|---:|---|
| `productos` | 10 | `sku`, `nombre`, `categoria`, `precio` (`Decimal128`), `stock`, `activo`, `etiquetas` (array), `especificaciones` (documento embebido) |
| `clientes` | 6 | `codigo`, `email`, `plan`, `ciudad`, `alta`, `preferencias` (documento embebido) |
| `pedidos` | 10 | `numero`, `clienteCodigo`, `fecha`, `estado`, `items` (array de documentos con `sku`, `cantidad`, `precioUnitario`), `total`, `envio` (documento embebido) |
| `resenas` | 8 | `sku`, `clienteCodigo`, `calificacion`, `titulo`, `votosUtiles` |

Las relaciones se guardan por código (`clienteCodigo`, `sku`), no por `_id`, para que los resultados no dependan de identificadores generados.

### Preparación

Cargá una base vacía (por ejemplo, `use tienda`) con este script, cambiando `dir` por tu carpeta. Cada ejercicio parte de una carga limpia: antes de uno que modifique datos, ejecutá `db.dropDatabase()` y volvé a cargar.

<!-- check: U4.PR.TIENDA -->
```javascript
const fs = require("fs");
const dir = "C:/datos/tienda";   // reemplazá por la carpeta donde guardaste los archivos
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));

cargar("productos");
cargar("clientes");
cargar("pedidos");
cargar("resenas");

print("productos: " + db.productos.countDocuments() + ", " +
      "clientes: " + db.clientes.countDocuments() + ", " +
      "pedidos: " + db.pedidos.countDocuments() + ", " +
      "resenas: " + db.resenas.countDocuments());
```

**Resultado esperado.**

```text
productos: 10, clientes: 6, pedidos: 10, resenas: 8
```

`mostrar()` imprime un documento por línea, igual que en la [práctica de MongoDB](/bbdd-aplicadas/unidad-4/practica/ejercicios/#conjunto-de-datos), donde se explica su formato.

## SQL y MongoDB, lado a lado

| Concepto | SQL / relacional | MongoDB / documental |
|---|---|---|
| Estructura | Tablas y filas con columnas fijas | Colecciones y documentos BSON |
| Esquema | Definido de antemano con DDL | Flexible; se puede exigir con un validador (`$jsonSchema`) |
| Relaciones | `JOIN` entre tablas | Documentos embebidos o referencias con `$lookup` |
| Arrays | Tabla intermedia y `JOIN` | Array dentro del documento |
| Escalado | Principalmente vertical; también horizontal con particionado y réplicas | Horizontal con sharding, además de réplicas |
| Transacciones | ACID | ACID, también entre varios documentos (requiere replica set o clúster) |
| Consultas | SQL | MQL y pipeline de agregación |

Correspondencia de operaciones del laboratorio:

| SQL | MQL |
|---|---|
| `UPDATE productos SET precio = precio * 1.10 WHERE categoria = 'hogar'` | `updateMany({ categoria: "hogar" }, [ { $set: ... } ])` |
| `DELETE FROM productos WHERE stock = 0 AND activo = 0` | `deleteMany({ stock: 0, activo: false })` |
| `SELECT ... FROM clientes LEFT JOIN pedidos ... GROUP BY ...` | `aggregate([ { $lookup }, { $project } ])` desde `clientes` |
| `SELECT estado, COUNT(*) ... GROUP BY estado` | `aggregate([ { $group } ])` |

## Nivel inicial

### Ejercicio 14 · Ajuste de precios y limpieza con decimales exactos
<!-- ejercicio: U4.14 | nivel: inicial | tipo: mql | verificacion: motor -->

:::note[Enunciado]
En `productos`, aumentá un 10 % los precios de la categoría `hogar` sin perder exactitud, y eliminá los productos sin stock que estén inactivos. Verificá los precios resultantes y las cantidades de documentos antes y después.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los precios están en `Decimal128`, que representa decimales exactos; con `Double` un incremento como 1.10 arrastraría errores de redondeo binario. Se usa una actualización con pipeline (MongoDB 4.2 o posterior) para calcular el nuevo precio a partir del anterior con `$multiply` y `$round` a dos decimales. `deleteMany()` informa cuántos borró.

<!-- check: U4.14 -->
```javascript
print("antes: " + db.productos.countDocuments());

db.productos.updateMany(
  { categoria: "hogar" },
  [ { $set: { precio: { $round: [{ $multiply: ["$precio", NumberDecimal("1.10")] }, 2] } } } ]
);
mostrar(db.productos.aggregate([
  { $match: { categoria: "hogar" } },
  { $project: { _id: 0, sku: 1, precio: { $toString: "$precio" } } },
  { $sort: { sku: 1 } }
]));

const r = db.productos.deleteMany({ stock: 0, activo: false });
print("borrados: " + r.deletedCount);
print("despues: " + db.productos.countDocuments());
```

**Resultado esperado.**

```text
antes: 10
{"sku":"P-004","precio":"49720.00"}
{"sku":"P-005","precio":"26180.00"}
{"sku":"P-006","precio":"13970.99"}
borrados: 2
despues: 8
```

El precio se muestra con `$toString` para ver el valor exacto. Se borran 2 productos (`P-005`, que ya había recibido el aumento, y `P-008`), así que quedan 8. Antes de un `deleteMany()` conviene ejecutar el mismo filtro con `find()` o `countDocuments()`. Con `Double`, `12700.9 * 1.1` da 13970.990000000002 en JavaScript.

</details>

### Ejercicio 15 · Filtrar por etiquetas y especificaciones
<!-- ejercicio: U4.15 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Mostrá los productos activos con la etiqueta `oficina` y precio menor a 20000 pesos, y por separado los productos de color negro (campo `especificaciones.color`).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Para un array, la condición `etiquetas: "oficina"` busca ese valor entre los elementos. Los campos de un documento embebido se alcanzan con notación de punto, entre comillas. El precio es `Decimal128`, así que se compara con `NumberDecimal`.

<!-- check: U4.15 -->
```javascript
mostrar(db.productos.find(
  {
    activo: true,
    etiquetas: "oficina",
    precio: { $lt: NumberDecimal("20000") }
  },
  { _id: 0, sku: 1, nombre: 1, etiquetas: 1 }
).sort({ sku: 1 }));

mostrar(db.productos.find(
  { "especificaciones.color": "negro" },
  { _id: 0, sku: 1, "especificaciones.color": 1 }
).sort({ sku: 1 }));
```

**Resultado esperado.**

```text
{"sku":"P-006","nombre":"Lampara de escritorio","etiquetas":["iluminacion","oficina"]}
{"sku":"P-010","nombre":"Soporte para notebook","etiquetas":["oficina","perifericos"]}
{"sku":"P-001","especificaciones":{"color":"negro"}}
{"sku":"P-002","especificaciones":{"color":"negro"}}
```

Los productos `P-006` y `P-010` cumplen las tres condiciones. La comparación de un `Decimal128` con un número del mismo valor funciona entre tipos numéricos, pero el literal `NumberDecimal("20000")` evita ambigüedades. La proyección `especificaciones.color: 1` devuelve el subdocumento solo con ese campo.

</details>

## Nivel intermedio

### Ejercicio 16 · Gasto por cliente, incluso sin compras
<!-- ejercicio: U4.16 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Calculá la cantidad de pedidos no cancelados y el gasto total de cada cliente, incluidos los que no compraron. Ordená por cantidad de pedidos descendente y luego por código.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Partimos de `clientes` para no perder a los que no compraron. El `$lookup` con `pipeline` filtra los pedidos no cancelados dentro de la propia unión (se pueden combinar `localField` y `foreignField` con `pipeline` desde MongoDB 5.0). `$sum` sobre `$pedidos.total` suma los importes.

<!-- check: U4.16 -->
```javascript
mostrar(db.clientes.aggregate([
  { $lookup: {
      from: "pedidos",
      localField: "codigo",
      foreignField: "clienteCodigo",
      pipeline: [ { $match: { estado: { $ne: "cancelado" } } } ],
      as: "pedidos"
  } },
  { $project: {
      _id: 0, codigo: 1, plan: 1,
      cantidadPedidos: { $size: "$pedidos" },
      gasto: { $toString: { $sum: "$pedidos.total" } }
  } },
  { $sort: { cantidadPedidos: -1, codigo: 1 } }
]))
```

**Resultado esperado.**

```text
{"codigo":"C-01","plan":"premium","cantidadPedidos":3,"gasto":"172671.80"}
{"codigo":"C-03","plan":"premium","cantidadPedidos":3,"gasto":"296590.50"}
{"codigo":"C-06","plan":"premium","cantidadPedidos":2,"gasto":"304503.20"}
{"codigo":"C-04","plan":"basico","cantidadPedidos":1,"gasto":"27600.00"}
{"codigo":"C-02","plan":"basico","cantidadPedidos":0,"gasto":"0"}
{"codigo":"C-05","plan":"basico","cantidadPedidos":0,"gasto":"0"}
```

`C-02` tiene un único pedido, pero estaba cancelado, así que cuenta 0 igual que `C-05`, que nunca compró. El gasto de un cliente sin pedidos queda en el entero 0, sin escala decimal, porque la suma de un conjunto vacío no es un `Decimal128`. Con un filtro posterior al `$lookup` en lugar de uno dentro, se habrían traído los pedidos cancelados antes de descartarlos.

</details>

### Ejercicio 17 · Facturación por categoría
<!-- ejercicio: U4.17 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Calculá, por categoría de producto, las unidades vendidas y lo facturado en pedidos que no estén cancelados.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Los pedidos guardan solo el `sku`; la categoría está en `productos`. Se filtra con `$match` al inicio para reducir los documentos, se expande `items` con `$unwind`, se une con `productos` mediante `$lookup`, se aplana el resultado y se agrupa por categoría.

<!-- check: U4.17 -->
```javascript
mostrar(db.pedidos.aggregate([
  { $match: { estado: { $ne: "cancelado" } } },
  { $unwind: "$items" },
  { $lookup: { from: "productos", localField: "items.sku", foreignField: "sku", as: "producto" } },
  { $unwind: "$producto" },
  { $group: {
      _id: "$producto.categoria",
      unidades: { $sum: "$items.cantidad" },
      facturado: { $sum: { $multiply: ["$items.cantidad", "$items.precioUnitario"] } }
  } },
  { $project: { _id: 0, categoria: "$_id", unidades: "$unidades", facturado: { $toString: "$facturado" } } },
  { $sort: { categoria: 1 } }
]))
```

**Resultado esperado.**

```text
{"categoria":"accesorios","unidades":6,"facturado":"125700.00"}
{"categoria":"electronica","unidades":8,"facturado":"520761.00"}
{"categoria":"hogar","unidades":6,"facturado":"108704.50"}
{"categoria":"libros","unidades":3,"facturado":"46200.00"}
```

El `$match` temprano deja afuera el pedido cancelado antes de hacer la unión. El importe usa el `precioUnitario` guardado en el ítem, no el precio actual del producto: así la facturación histórica no cambia si el precio se actualiza (esa copia de datos es una decisión de modelado habitual en documentos). El resultado de la suma es `Decimal128` y se muestra como texto.

</details>

## Nivel avanzado

### Ejercicio 18 · Panel de resumen con `$facet` y `$bucket`
<!-- ejercicio: U4.18 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Con una sola agregación sobre `pedidos`, obtené la cantidad de pedidos por estado, los tres productos más vendidos en unidades y la distribución de los pedidos por tamaño de total (menos de 50000, de 50000 a 149999 y de 150000 a 999999).
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se usa `$facet` con tres sub-pipelines. En el segundo se expande `items` antes de agrupar. En el tercero, el total se convierte a `double` con `$toDouble` para poder usarlo como clave de `$bucket`, cuyos límites son numéricos.

<!-- check: U4.18 -->
```javascript
mostrar(db.pedidos.aggregate([
  { $facet: {
      porEstado: [
        { $group: { _id: "$estado", pedidos: { $sum: 1 } } },
        { $sort: { _id: 1 } }
      ],
      masVendidos: [
        { $unwind: "$items" },
        { $group: { _id: "$items.sku", unidades: { $sum: "$items.cantidad" } } },
        { $sort: { unidades: -1, _id: 1 } },
        { $limit: 3 }
      ],
      porTamanio: [
        { $bucket: {
            groupBy: { $toDouble: "$total" },
            boundaries: [0, 50000, 150000, 1000000],
            output: { pedidos: { $sum: 1 } }
        } }
      ]
  } }
]))
```

**Resultado esperado.**

```text
{"porEstado":[{"_id":"cancelado","pedidos":1},{"_id":"entregado","pedidos":6},{"_id":"enviado","pedidos":2},{"_id":"pendiente","pedidos":1}],"masVendidos":[{"_id":"P-006","unidades":5},{"_id":"P-001","unidades":4},{"_id":"P-007","unidades":3}],"porTamanio":[{"_id":0,"pedidos":4},{"_id":50000,"pedidos":4},{"_id":150000,"pedidos":2}]}
```

Hay 6 pedidos entregados, 2 enviados, 1 cancelado y 1 pendiente. Los más vendidos son `P-006` (5 unidades), `P-001` (4) y `P-007` (3). Los rangos dan 4, 4 y 2 pedidos. Si un valor quedara fuera de todos los rangos y no hubiera `default`, `$bucket` fallaría.

</details>

### Ejercicio 19 · Índices único, compuesto y TTL
<!-- ejercicio: U4.19 | nivel: avanzado | tipo: diagnostico | verificacion: motor -->

:::note[Enunciado]
(1) Garantizá que no se repitan los correos en `clientes` y comprobá el rechazo de un duplicado. (2) Compará el plan de `pedidos` para los pedidos `entregado` ordenados por fecha descendente antes y después de crear un índice compuesto. (3) Definí un índice TTL que expire las sesiones 30 minutos después de `creadaEn` y comprobalo con la lista de índices.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un índice con `unique: true` rechaza claves repetidas con el error 11000. El índice `{ estado: 1, fecha: -1 }` cubre el filtro y el orden. Un índice TTL se define sobre un campo de fecha con `expireAfterSeconds`; se verifica leyendo `getIndexes()`, sin esperar a que el proceso de limpieza actúe.

<!-- check: U4.19 -->
```javascript
db.clientes.createIndex({ email: 1 }, { unique: true, name: "uxEmail" });
try {
  db.clientes.insertOne({ codigo: "C-99", email: "cliente01@ejemplo.test", plan: "basico" });
} catch (e) {
  print("duplicado rechazado, codigo " + e.code);
}

const resumen = (plan) => {
  let nodo = plan.queryPlanner.winningPlan;
  const etapas = [];
  while (nodo) { etapas.push(nodo.stage); nodo = nodo.inputStage; }
  const e = plan.executionStats;
  return { etapas: etapas.join(" > "), devueltos: e.nReturned, examinados: e.totalDocsExamined };
};
const consulta = () => db.pedidos.find({ estado: "entregado" }).sort({ fecha: -1 });
print("sin indice: " + JSON.stringify(resumen(consulta().explain("executionStats"))));
db.pedidos.createIndex({ estado: 1, fecha: -1 }, { name: "ixEstadoFecha" });
print("con indice: " + JSON.stringify(resumen(consulta().explain("executionStats"))));

db.sesiones.createIndex({ creadaEn: 1 }, { name: "ttlSesiones", expireAfterSeconds: 1800 });
const ttl = db.sesiones.getIndexes().find(i => i.name === "ttlSesiones");
print("TTL: " + JSON.stringify({ clave: ttl.key, expireAfterSeconds: ttl.expireAfterSeconds }));
```

**Resultado esperado.**

```text
duplicado rechazado, codigo 11000
sin indice: {"etapas":"SORT > COLLSCAN","devueltos":6,"examinados":10}
con indice: {"etapas":"FETCH > IXSCAN","devueltos":6,"examinados":6}
TTL: {"clave":{"creadaEn":1},"expireAfterSeconds":1800}
```

El duplicado falla con código 11000. Sin índice, el plan es `SORT > COLLSCAN` y examina los 10 pedidos para devolver 6; con índice, `FETCH > IXSCAN` examina solo esos 6. El índice TTL se aplica a la colección `sesiones`: los documentos cuyo `creadaEn` sea un `Date` anterior al límite se borran automáticamente en un proceso de fondo que corre periódicamente, por eso no es un plazo exacto. Un índice TTL sobre una colección real puede eliminar datos sin aviso: probalo siempre en una colección de prueba.

</details>

### Ejercicio 26 · Calificación promedio por producto
<!-- ejercicio: U4.26 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Calculá la calificación promedio y los votos útiles de los productos con al menos dos reseñas, junto con su categoría. Ordená por promedio descendente y por `sku`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se agrupa primero `resenas` por `sku` (cantidad, promedio y suma de votos). Con `$match` se descartan los productos con menos de dos reseñas y luego se completa la categoría con `$lookup` sobre `productos`.

<!-- check: U4.26 -->
```javascript
mostrar(db.resenas.aggregate([
  { $group: {
      _id: "$sku",
      resenas: { $sum: 1 },
      promedio: { $avg: "$calificacion" },
      votos: { $sum: "$votosUtiles" }
  } },
  { $match: { resenas: { $gte: 2 } } },
  { $lookup: { from: "productos", localField: "_id", foreignField: "sku", as: "producto" } },
  { $unwind: "$producto" },
  { $project: {
      _id: 0, sku: "$_id", categoria: "$producto.categoria",
      resenas: "$resenas", promedio: { $round: ["$promedio", 2] }, votos: "$votos"
  } },
  { $sort: { promedio: -1, sku: 1 } }
]))
```

**Resultado esperado.**

```text
{"sku":"P-001","categoria":"electronica","resenas":2,"promedio":4.5,"votos":15}
{"sku":"P-007","categoria":"libros","resenas":2,"promedio":4.5,"votos":26}
```

Solo `P-001` y `P-007` tienen dos o más reseñas, ambos con promedio de 4.5, y se desempatan por `sku`. Filtrar con `$match` antes del `$lookup` reduce el trabajo de la unión: primero se resume y luego se enriquece.

</details>

## Fuera del alcance: consumo de una API externa

El laboratorio anterior incluía un ejercicio que importaba libros desde una API pública con un script de Node. No se incorporó a esta versión porque requiere acceso a la red y el servicio externo puede cambiar, así que no es reproducible. Si querés practicar el consumo de una API, usá la [práctica de APIs desde SQL](/bbdd-aplicadas/unidad-2/practica/apis/) de la Unidad 2, que queda pendiente de verificación específica por el mismo motivo.

## Tipos de índices vistos

| Tipo | Ejemplo | Dónde se usó |
|---|---|---|
| Simple | `{ estado: 1 }` | |
| Único | `{ email: 1 }` con `unique: true` | ejercicio 19 |
| Compuesto | `{ estado: 1, fecha: -1 }` | ejercicio 19 |
| Multiclave (sobre un array) | `{ generos: 1 }` indexa cada elemento | [integrador de películas](/bbdd-aplicadas/unidad-4/practica/integrador-peliculas/) |
| TTL | `{ creadaEn: 1 }` con `expireAfterSeconds` | ejercicio 19 |
