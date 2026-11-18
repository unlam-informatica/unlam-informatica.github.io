// u4 · práctica U4.23 (datos propios: archivos/videoclub/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("peliculas");
cargar("socios");
cargar("prestamos");
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
