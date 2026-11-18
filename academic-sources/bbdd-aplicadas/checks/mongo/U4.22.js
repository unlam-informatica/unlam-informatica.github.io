// u4 · práctica U4.22 (datos propios: archivos/videoclub/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("peliculas");
cargar("socios");
cargar("prestamos");
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
