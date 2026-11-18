// u4 · práctica U4.24 (datos propios: archivos/videoclub/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("peliculas");
cargar("socios");
cargar("prestamos");
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
