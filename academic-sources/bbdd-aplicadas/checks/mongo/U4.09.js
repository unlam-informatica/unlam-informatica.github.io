// u4 · práctica U4.09 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
mostrar(db.ventas.aggregate([
  { $unwind: "$articulos" },
  { $group: {
      _id: "$articulos.codigo",
      unidades: { $sum: "$articulos.cantidad" },
      facturado: { $sum: { $multiply: ["$articulos.cantidad", "$articulos.precioUnitario"] } }
  } },
  { $sort: { unidades: -1, _id: 1 } },
  { $limit: 5 }
]))
