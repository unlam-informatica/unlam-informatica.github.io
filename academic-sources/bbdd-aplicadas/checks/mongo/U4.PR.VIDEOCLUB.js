// u4 · práctica: preparación (videoclub).
const fs = require("fs");
const dir = "{{FIXTURES}}";   // reemplazá por la carpeta donde guardaste los archivos
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));

cargar("peliculas");
cargar("socios");
cargar("prestamos");

print("peliculas: " + db.peliculas.countDocuments() + ", " +
      "socios: " + db.socios.countDocuments() + ", " +
      "prestamos: " + db.prestamos.countDocuments());
