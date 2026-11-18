// u4 · práctica U4.16 (datos propios: archivos/tienda/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("productos");
cargar("clientes");
cargar("pedidos");
cargar("resenas");
mostrar(db.clientes.aggregate([
  { $lookup: {
      from: "pedidos",
      localField: "codigo",
      foreignField: "clienteCodigo",
      pipeline: [ { $match: { estado: { $ne: "cancelado" } } } ],
      as: "pedidos"
  } },
  { $project: {
      _id: 0, codigo: 1, plan: 1,
      cantidadPedidos: { $size: "$pedidos" },
      gasto: { $toString: { $sum: "$pedidos.total" } }
  } },
  { $sort: { cantidadPedidos: -1, codigo: 1 } }
]))
