// u4 · práctica U4.02 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
mostrar(db.ventas.find(
  {
    fecha: { $gte: ISODate("2025-04-01T00:00:00Z"), $lt: ISODate("2025-07-01T00:00:00Z") },
    medioPago: { $in: ["debito", "credito"] }
  },
  { _id: 0, idVenta: 1, fecha: 1, medioPago: 1 }
).sort({ fecha: 1 }))
