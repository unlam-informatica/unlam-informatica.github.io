// u4 · práctica U4.08 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
mostrar(db.ventas.aggregate([
  { $group: {
      _id: { $dateToString: { format: "%Y-%m", date: "$fecha" } },
      ventas: { $sum: 1 },
      total: { $sum: "$total" },
      promedio: { $avg: "$total" },
      mayor: { $max: "$total" }
  } },
  { $sort: { _id: 1 } },
  { $project: { _id: 0, mes: "$_id", ventas: "$ventas", total: "$total", promedio: { $round: ["$promedio", 2] }, mayor: "$mayor" } }
]))
