// u4 · práctica U4.17 (datos propios: archivos/tienda/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("productos");
cargar("clientes");
cargar("pedidos");
cargar("resenas");
mostrar(db.pedidos.aggregate([
  { $match: { estado: { $ne: "cancelado" } } },
  { $unwind: "$items" },
  { $lookup: { from: "productos", localField: "items.sku", foreignField: "sku", as: "producto" } },
  { $unwind: "$producto" },
  { $group: {
      _id: "$producto.categoria",
      unidades: { $sum: "$items.cantidad" },
      facturado: { $sum: { $multiply: ["$items.cantidad", "$items.precioUnitario"] } }
  } },
  { $project: { _id: 0, categoria: "$_id", unidades: "$unidades", facturado: { $toString: "$facturado" } } },
  { $sort: { categoria: 1 } }
]))
