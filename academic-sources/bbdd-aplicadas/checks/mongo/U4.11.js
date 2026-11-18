// u4 · práctica U4.11 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
mostrar(db.vendedores.aggregate([
  { $lookup: { from: "ventas", localField: "idVendedor", foreignField: "idVendedor", as: "ventas" } },
  { $project: {
      _id: 0, idVendedor: 1, zona: 1,
      cantidadVentas: { $size: "$ventas" },
      facturado: { $sum: "$ventas.total" }
  } },
  { $sort: { facturado: -1, idVendedor: 1 } }
]))
