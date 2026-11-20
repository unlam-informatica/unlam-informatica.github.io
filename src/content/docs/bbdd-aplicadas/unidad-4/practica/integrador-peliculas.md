---
title: Integrador — Películas y Préstamos
slug: bbdd-aplicadas/unidad-4/practica/integrador-peliculas
sidebar:
  order: 3
---

[← Unidad 4](/bbdd-aplicadas/unidad-4/teoria/)

Práctica integradora sobre un videoclub ficticio: documentos embebidos, arrays, campos ausentes y nulos, conversión de fechas, CRUD, uniones con `$lookup`, controles de integridad, índices y vistas. Los datos y las resoluciones son propios, y los resultados esperados se obtuvieron con MongoDB 7.0.

:::note[Material propio]
Es una práctica propia de estos apuntes, no de la cátedra: los datos están publicados en este sitio y no hace falta descargar nada de fuentes externas.
:::

## Antes de empezar

Presupone las lecciones de [CRUD](/bbdd-aplicadas/unidad-4/teoria/mongodb-crud/) y de [agregación](/bbdd-aplicadas/unidad-4/teoria/mongodb-agregacion/) (con la sección de índices), y un servidor MongoDB con `mongosh` ([instalación](/bbdd-aplicadas/unidad-4/teoria/instalacion-mongodb/)).

## Conjunto de datos

Datos sintéticos (los directores, actores y socios son rótulos, no personas). Descargá los archivos en una carpeta:

- [`peliculas.json`](/bbdd-aplicadas/unidad-4/practica/archivos/videoclub/peliculas.json)
- [`socios.json`](/bbdd-aplicadas/unidad-4/practica/archivos/videoclub/socios.json)
- [`prestamos.json`](/bbdd-aplicadas/unidad-4/practica/archivos/videoclub/prestamos.json)

| Colección | Documentos | Campos principales |
|---|---:|---|
| `peliculas` | 10 | `codigo`, `titulo`, `anio`, `director` (documento embebido con `nombre` y `nacionalidad`), `generos` (array), `reparto` (array), `calificacion` (ausente en una película y `null` en otra), `copias` |
| `socios` | 5 | `codigo`, `nombre`, `alta`, `estado` |
| `prestamos` | 13 | `numero`, `socioCodigo`, `peliculaCodigo`, `fechaPrestamo` y `fechaDevolucion` (texto `AAAA-MM-DD`; `null` si el préstamo sigue abierto) |

Los datos incluyen a propósito tres irregularidades que los ejercicios descubren: un campo ausente, un valor nulo y un préstamo que apunta a una película inexistente (`PEL-99`). Las fechas de `prestamos` están como texto para practicar la conversión.

### Preparación

Trabajá en una base de práctica vacía (por ejemplo, `use videoclub` en `mongosh`; se crea al insertar). El script carga los tres archivos JSON que descargaste: cambiá `dir` por tu carpeta (en macOS o Linux, algo como `/home/usuario/datos/videoclub`; en Windows, con barras normales, como `C:/datos/videoclub`). Si usás el shell integrado de Compass, que puede no permitir leer archivos del disco, importá cada JSON con **ADD DATA → Import JSON or CSV file** en una colección con el mismo nombre del archivo. Cada ejercicio parte de una carga limpia: antes de uno que modifique datos, ejecutá `db.dropDatabase()` y volvé a cargar.

<!-- check: U4.PR.VIDEOCLUB -->
```javascript
const fs = require("fs");
const dir = "C:/datos/videoclub";   // reemplazá por la carpeta donde guardaste los archivos
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));

cargar("peliculas");
cargar("socios");
cargar("prestamos");

print("peliculas: " + db.peliculas.countDocuments() + ", " +
      "socios: " + db.socios.countDocuments() + ", " +
      "prestamos: " + db.prestamos.countDocuments());
```

**Resultado esperado.**

```text
peliculas: 10, socios: 5, prestamos: 13
```

`mostrar()` imprime un documento por línea, igual que en la [práctica de MongoDB](/bbdd-aplicadas/unidad-4/practica/ejercicios/#conjunto-de-datos), donde se explica su formato.

## Nivel inicial

### Ejercicio 20 · Campo ausente, campo nulo y arrays
<!-- ejercicio: U4.20 | nivel: inicial | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
En `peliculas`, contá cuántas tienen `calificacion` igual a `null`, cuántas no tienen el campo y cuántas tienen el valor `null` explícito. Después buscá las películas de los géneros `drama` y `misterio` a la vez, las que tienen tres actores y las argentinas desde 2010.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** En MongoDB, `{ campo: null }` coincide con el valor nulo y también con el campo ausente. `$exists: false` detecta solo la ausencia y `$type: "null"` detecta solo el nulo explícito. Para arrays, `$all` y `$size`; para el documento embebido `director`, notación de punto.

<!-- check: U4.20 -->
```javascript
const contar = (filtro) => db.peliculas.countDocuments(filtro);
print("calificacion: null           -> " + contar({ calificacion: null }));
print("calificacion $exists: false  -> " + contar({ calificacion: { $exists: false } }));
print("calificacion $type: null     -> " + contar({ calificacion: { $type: "null" } }));

mostrar(db.peliculas.find({ generos: { $all: ["drama", "misterio"] } }, { _id: 0, codigo: 1, generos: 1 }).sort({ codigo: 1 }));
mostrar(db.peliculas.find({ reparto: { $size: 3 } }, { _id: 0, codigo: 1, reparto: 1 }).sort({ codigo: 1 }));
mostrar(db.peliculas.find({ "director.nacionalidad": "Argentina", anio: { $gte: 2010 } }, { _id: 0, codigo: 1, titulo: 1 }).sort({ codigo: 1 }));
```

**Resultado esperado.**

```text
calificacion: null           -> 2
calificacion $exists: false  -> 1
calificacion $type: null     -> 1
{"codigo":"PEL-01","generos":["drama","misterio"]}
{"codigo":"PEL-10","generos":["misterio","drama"]}
{"codigo":"PEL-01","reparto":["Actor 1","Actor 2","Actor 3"]}
{"codigo":"PEL-05","reparto":["Actor 4","Actor 7","Actor 8"]}
{"codigo":"PEL-07","reparto":["Actor 2","Actor 9","Actor 10"]}
{"codigo":"PEL-01","titulo":"La ciudad dormida"}
{"codigo":"PEL-09","titulo":"Orbita"}
```

Dos películas coinciden con `{ calificacion: null }`: `PEL-03` (nulo explícito) y `PEL-08` (campo ausente). `$exists: false` encuentra una y `$type: "null"`, la otra. `$all` es independiente del orden de los elementos, por eso `PEL-10` (con `misterio` antes que `drama`) también aparece.

</details>

### Ejercicio 21 · Convertir fechas de texto a Date
<!-- ejercicio: U4.21 | nivel: inicial | tipo: mql | verificacion: motor -->

:::note[Enunciado]
En `prestamos`, las fechas están guardadas como texto (`AAAA-MM-DD`) y `fechaDevolucion` es `null` cuando el préstamo sigue abierto. Convertí ambos campos a `Date` con una sola actualización, verificá el tipo resultante y consultá los préstamos de febrero de 2026.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Una actualización con pipeline permite calcular el nuevo valor de cada campo con `$dateFromString`. Si `dateString` es `null`, la función devuelve `null` (opción `onNull`), así que las devoluciones pendientes se conservan sin lógica adicional.

<!-- check: U4.21 -->
```javascript
print("antes: " + db.prestamos.findOne({ numero: 1 }).fechaPrestamo.constructor.name);

db.prestamos.updateMany({}, [
  { $set: {
      fechaPrestamo: { $dateFromString: { dateString: "$fechaPrestamo", format: "%Y-%m-%d" } },
      fechaDevolucion: { $dateFromString: { dateString: "$fechaDevolucion", format: "%Y-%m-%d" } }
  } }
]);

print("despues: " + db.prestamos.findOne({ numero: 1 }).fechaPrestamo.constructor.name);
print("devoluciones nulas: " + db.prestamos.countDocuments({ fechaDevolucion: null }));

mostrar(db.prestamos.find(
  { fechaPrestamo: { $gte: ISODate("2026-02-01T00:00:00Z"), $lt: ISODate("2026-03-01T00:00:00Z") } },
  { _id: 0, numero: 1, fechaPrestamo: 1 }
).sort({ numero: 1 }));
```

**Resultado esperado.**

```text
antes: String
despues: Date
devoluciones nulas: 5
{"numero":1,"fechaPrestamo":{"$date":"2026-02-02T00:00:00Z"}}
{"numero":2,"fechaPrestamo":{"$date":"2026-02-20T00:00:00Z"}}
{"numero":3,"fechaPrestamo":{"$date":"2026-02-10T00:00:00Z"}}
{"numero":12,"fechaPrestamo":{"$date":"2026-02-25T00:00:00Z"}}
```

Después de la conversión el tipo cambia de `String` a `Date` y los 5 préstamos abiertos mantienen `fechaDevolucion: null`. Con fechas reales, el filtro por rango funciona y devuelve los préstamos 1, 2, 3 y 12. Con texto `AAAA-MM-DD`, la comparación habría funcionado por orden alfabético, pero no se podrían hacer cálculos de fechas. Requiere MongoDB 4.2 o posterior.

</details>

## Nivel intermedio

### Ejercicio 22 · Préstamos con retraso
<!-- ejercicio: U4.22 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
El plazo de préstamo es de 3 días. Con fecha de corte `2026-03-20`, listá los préstamos que siguen abiertos y están retrasados, con los días transcurridos y los días de retraso. Ordená de mayor a menor retraso.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se filtran los préstamos con `fechaDevolucion: null`. `$dateDiff` calcula los días entre el préstamo (convertido con `$dateFromString` dentro de la misma consulta, así no depende de la conversión del ejercicio anterior) y la fecha de corte. El retraso es la diferencia con el plazo, con piso en cero mediante `$max`.

<!-- check: U4.22 -->
```javascript
mostrar(db.prestamos.aggregate([
  { $match: { fechaDevolucion: null } },
  { $set: {
      dias: { $dateDiff: {
          startDate: { $dateFromString: { dateString: "$fechaPrestamo" } },
          endDate: ISODate("2026-03-20T00:00:00Z"),
          unit: "day"
      } }
  } },
  { $set: { diasDeRetraso: { $max: [0, { $subtract: ["$dias", 3] }] } } },
  { $match: { diasDeRetraso: { $gt: 0 } } },
  { $project: { _id: 0, numero: 1, socioCodigo: 1, peliculaCodigo: 1, dias: 1, diasDeRetraso: 1 } },
  { $sort: { diasDeRetraso: -1, numero: 1 } }
]))
```

**Resultado esperado.**

```text
{"numero":5,"socioCodigo":"S-03","peliculaCodigo":"PEL-09","dias":17,"diasDeRetraso":14}
{"numero":8,"socioCodigo":"S-05","peliculaCodigo":"PEL-05","dias":15,"diasDeRetraso":12}
{"numero":9,"socioCodigo":"S-05","peliculaCodigo":"PEL-09","dias":8,"diasDeRetraso":5}
```

Hay 5 préstamos abiertos, pero solo 3 están retrasados: el 13 se prestó el 19 de marzo (1 día) y el 11, el 18 (2 días), así que ambos están dentro del plazo. `$dateDiff` requiere MongoDB 5.0 o posterior. La fecha de corte se fija en el ejercicio para que el resultado sea reproducible; en una aplicación sería la fecha actual.

</details>

### Ejercicio 23 · Referencias que no encuentran destino
<!-- ejercicio: U4.23 | nivel: intermedio | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Detectá dos problemas de integridad: (A) las películas que nunca se prestaron y (B) los préstamos cuya película no existe en el catálogo.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** MongoDB no impone integridad referencial, así que las referencias por código se verifican a mano. Para A se une desde `peliculas` hacia `prestamos` y se queda con los arrays vacíos. Para B se une desde `prestamos` hacia `peliculas`, se aplana con `$unwind` y `preserveNullAndEmptyArrays: true`, y se buscan los documentos sin el campo `pelicula`.

<!-- check: U4.23 -->
```javascript
print("A) peliculas que nunca se prestaron");
mostrar(db.peliculas.aggregate([
  { $lookup: { from: "prestamos", localField: "codigo", foreignField: "peliculaCodigo", as: "prestamos" } },
  { $match: { prestamos: { $size: 0 } } },
  { $project: { _id: 0, codigo: 1, titulo: 1 } },
  { $sort: { codigo: 1 } }
]));

print("B) prestamos cuya pelicula no existe");
mostrar(db.prestamos.aggregate([
  { $lookup: { from: "peliculas", localField: "peliculaCodigo", foreignField: "codigo", as: "pelicula" } },
  { $unwind: { path: "$pelicula", preserveNullAndEmptyArrays: true } },
  { $match: { pelicula: { $exists: false } } },
  { $project: { _id: 0, numero: 1, socioCodigo: 1, peliculaCodigo: 1 } },
  { $sort: { numero: 1 } }
]));
```

**Resultado esperado.**

```text
A) peliculas que nunca se prestaron
{"codigo":"PEL-03","titulo":"El ultimo tren"}
{"codigo":"PEL-06","titulo":"Taller de sueños"}
{"codigo":"PEL-08","titulo":"Mapa de sal"}
{"codigo":"PEL-10","titulo":"Sombras del puerto"}
B) prestamos cuya pelicula no existe
{"numero":13,"socioCodigo":"S-04","peliculaCodigo":"PEL-99"}
```

Cuatro películas nunca se prestaron. El préstamo 13 referencia a `PEL-99`, que no existe. Sin `preserveNullAndEmptyArrays`, el `$unwind` descartaría justamente ese préstamo y el problema quedaría oculto. En un modelo relacional una clave foránea lo habría impedido; acá es responsabilidad de la aplicación o de un proceso de control.

</details>

## Nivel avanzado

### Ejercicio 24 · Géneros más prestados
<!-- ejercicio: U4.24 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Calculá, para cada género, cuántos préstamos tuvo y cuántos socios distintos los realizaron. Ordená por cantidad de préstamos y, ante empate, por género.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Se une cada préstamo con su película y se aplana. Como `generos` es un array, un segundo `$unwind` genera una fila por género. Después se agrupa por género, contando préstamos y juntando los socios con `$addToSet`, cuyo tamaño da los socios distintos.

<!-- check: U4.24 -->
```javascript
mostrar(db.prestamos.aggregate([
  { $lookup: { from: "peliculas", localField: "peliculaCodigo", foreignField: "codigo", as: "pelicula" } },
  { $unwind: "$pelicula" },
  { $unwind: "$pelicula.generos" },
  { $group: {
      _id: "$pelicula.generos",
      prestamos: { $sum: 1 },
      socios: { $addToSet: "$socioCodigo" }
  } },
  { $project: { _id: 0, genero: "$_id", prestamos: 1, sociosDistintos: { $size: "$socios" } } },
  { $sort: { prestamos: -1, genero: 1 } }
]))
```

**Resultado esperado.**

```text
{"prestamos":8,"genero":"aventura","sociosDistintos":4}
{"prestamos":5,"genero":"drama","sociosDistintos":4}
{"prestamos":3,"genero":"ciencia ficcion","sociosDistintos":3}
{"prestamos":3,"genero":"familiar","sociosDistintos":3}
{"prestamos":3,"genero":"misterio","sociosDistintos":2}
{"prestamos":1,"genero":"comedia","sociosDistintos":1}
{"prestamos":1,"genero":"suspenso","sociosDistintos":1}
```

Un préstamo de una película con dos géneros se cuenta una vez por cada género, por eso la suma de préstamos por género supera la cantidad de préstamos con película válida. El préstamo 13 no aparece: su película no existe y el `$unwind` lo descarta. `aventura` lidera con 8 préstamos de 4 socios distintos.

</details>

### Ejercicio 25 · Índices y vista del videoclub
<!-- ejercicio: U4.25 | nivel: avanzado | tipo: mql | verificacion: motor -->

:::note[Enunciado]
(1) Hacé único el código de las películas y probá el rechazo de un duplicado. (2) Creá un índice sobre `generos` y comprobá que se usa y que es multiclave. (3) Creá la vista `vwPrestamosDetalle` con el título de la película y consultala para el socio `S-03`; compará la cantidad de documentos de la vista con la de `prestamos`.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un índice sobre un campo array es multiclave: indexa cada elemento. Para leer el plan se recorre `winningPlan` hasta la etapa `IXSCAN`. La vista usa `$lookup` y `$unwind` (sin conservar los huérfanos) para completar cada préstamo con el título.

<!-- check: U4.25 -->
```javascript
db.peliculas.createIndex({ codigo: 1 }, { unique: true, name: "uxCodigo" });
try {
  db.peliculas.insertOne({ codigo: "PEL-01", titulo: "Copia" });
} catch (e) {
  print("duplicado rechazado, codigo " + e.code);
}

db.peliculas.createIndex({ generos: 1 }, { name: "ixGeneros" });
const plan = db.peliculas.find({ generos: "drama" }).explain("executionStats");
let nodo = plan.queryPlanner.winningPlan;
while (nodo.stage !== "IXSCAN") nodo = nodo.inputStage;
print("indice " + nodo.indexName + ", multikey " + nodo.isMultiKey + ", devueltos " + plan.executionStats.nReturned +
      ", examinados " + plan.executionStats.totalDocsExamined);

db.createView("vwPrestamosDetalle", "prestamos", [
  { $lookup: { from: "peliculas", localField: "peliculaCodigo", foreignField: "codigo", as: "pelicula" } },
  { $unwind: "$pelicula" },
  { $project: { _id: 0, numero: 1, socioCodigo: 1, titulo: "$pelicula.titulo", fechaPrestamo: 1, fechaDevolucion: 1 } }
]);
mostrar(db.vwPrestamosDetalle.find({ socioCodigo: "S-03" }).sort({ numero: 1 }));
print("prestamos: " + db.prestamos.countDocuments() + ", en la vista: " + db.vwPrestamosDetalle.countDocuments());
```

**Resultado esperado.**

```text
duplicado rechazado, codigo 11000
indice ixGeneros, multikey true, devueltos 5, examinados 5
{"numero":5,"socioCodigo":"S-03","fechaPrestamo":"2026-03-03","fechaDevolucion":null,"titulo":"Orbita"}
{"numero":6,"socioCodigo":"S-03","fechaPrestamo":"2026-03-10","fechaDevolucion":"2026-03-12","titulo":"Ruta al sur"}
{"numero":12,"socioCodigo":"S-03","fechaPrestamo":"2026-02-25","fechaDevolucion":"2026-02-27","titulo":"Cielo abierto"}
prestamos: 13, en la vista: 12
```

El índice único devuelve el error 11000 ante `PEL-01` repetido. El plan usa `ixGeneros`, con `isMultiKey: true`, y examina solo las 5 entradas de `drama`. La vista muestra 12 préstamos frente a 13 en la colección: falta el que apunta a `PEL-99`. Las vistas no se materializan; cada consulta ejecuta el pipeline completo, y pueden apoyarse en los índices de la colección de origen.

</details>

### Ejercicio 27 · Película más prestada, con empates
<!-- ejercicio: U4.27 | nivel: avanzado | tipo: consulta | verificacion: motor -->

:::note[Enunciado]
Obtené la película con más préstamos. Si hay empate en el primer puesto, deben aparecer todas las empatadas.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Un `$limit: 1` descartaría a las empatadas. En su lugar se cuenta por película, se asigna una posición con `$setWindowFields` y la función `$rank` (empatadas comparten posición) y se queda con la posición 1.

<!-- check: U4.27 -->
```javascript
mostrar(db.prestamos.aggregate([
  { $group: { _id: "$peliculaCodigo", prestamos: { $sum: 1 } } },
  { $setWindowFields: { sortBy: { prestamos: -1 }, output: { posicion: { $rank: {} } } } },
  { $match: { posicion: 1 } },
  { $sort: { _id: 1 } }
]))
```

**Resultado esperado.**

```text
{"_id":"PEL-05","prestamos":3,"posicion":1}
{"_id":"PEL-09","prestamos":3,"posicion":1}
```

`PEL-05` y `PEL-09` tienen 3 préstamos cada una, así que ambas reciben la posición 1. `$setWindowFields` y `$rank` están disponibles desde MongoDB 5.0.

</details>
