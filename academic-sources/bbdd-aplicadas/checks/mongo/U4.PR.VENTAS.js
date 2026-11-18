// u4 · práctica: preparación (ventas).
const fs = require("fs");
const dir = "{{FIXTURES}}";   // reemplazá por la carpeta donde guardaste los archivos
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));

cargar("ventas");
cargar("vendedores");

print("ventas: " + db.ventas.countDocuments() + ", " +
      "vendedores: " + db.vendedores.countDocuments());
