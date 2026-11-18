// u4 · práctica U4.01 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
mostrar(db.ventas.find(
  { sucursal: "Norte", total: { $gte: 75000 } },
  { _id: 0, idVenta: 1, fecha: 1, total: 1 }
).sort({ total: -1, idVenta: 1 }))
