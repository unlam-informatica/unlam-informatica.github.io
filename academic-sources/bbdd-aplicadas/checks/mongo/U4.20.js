// u4 · práctica U4.20 (datos propios: archivos/videoclub/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("peliculas");
cargar("socios");
cargar("prestamos");
const contar = (filtro) => db.peliculas.countDocuments(filtro);
print("calificacion: null           -> " + contar({ calificacion: null }));
print("calificacion $exists: false  -> " + contar({ calificacion: { $exists: false } }));
print("calificacion $type: null     -> " + contar({ calificacion: { $type: "null" } }));

mostrar(db.peliculas.find({ generos: { $all: ["drama", "misterio"] } }, { _id: 0, codigo: 1, generos: 1 }).sort({ codigo: 1 }));
mostrar(db.peliculas.find({ reparto: { $size: 3 } }, { _id: 0, codigo: 1, reparto: 1 }).sort({ codigo: 1 }));
mostrar(db.peliculas.find({ "director.nacionalidad": "Argentina", anio: { $gte: 2010 } }, { _id: 0, codigo: 1, titulo: 1 }).sort({ codigo: 1 }));
