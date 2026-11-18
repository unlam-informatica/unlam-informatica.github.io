// u4 · práctica U4.25 (datos propios: archivos/videoclub/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("peliculas");
cargar("socios");
cargar("prestamos");
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
