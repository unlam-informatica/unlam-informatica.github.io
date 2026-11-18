// u4 · práctica U4.27 (datos propios: archivos/videoclub/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("peliculas");
cargar("socios");
cargar("prestamos");
mostrar(db.prestamos.aggregate([
  { $group: { _id: "$peliculaCodigo", prestamos: { $sum: 1 } } },
  { $setWindowFields: { sortBy: { prestamos: -1 }, output: { posicion: { $rank: {} } } } },
  { $match: { posicion: 1 } },
  { $sort: { _id: 1 } }
]))
