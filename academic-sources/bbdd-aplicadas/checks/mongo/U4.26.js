// u4 · práctica U4.26 (datos propios: archivos/tienda/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("productos");
cargar("clientes");
cargar("pedidos");
cargar("resenas");
mostrar(db.resenas.aggregate([
  { $group: {
      _id: "$sku",
      resenas: { $sum: 1 },
      promedio: { $avg: "$calificacion" },
      votos: { $sum: "$votosUtiles" }
  } },
  { $match: { resenas: { $gte: 2 } } },
  { $lookup: { from: "productos", localField: "_id", foreignField: "sku", as: "producto" } },
  { $unwind: "$producto" },
  { $project: {
      _id: 0, sku: "$_id", categoria: "$producto.categoria",
      resenas: "$resenas", promedio: { $round: ["$promedio", 2] }, votos: "$votos"
  } },
  { $sort: { promedio: -1, sku: 1 } }
]))
