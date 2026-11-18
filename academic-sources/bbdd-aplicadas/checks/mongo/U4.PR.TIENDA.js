// u4 · práctica: preparación (tienda).
const fs = require("fs");
const dir = "{{FIXTURES}}";   // reemplazá por la carpeta donde guardaste los archivos
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
