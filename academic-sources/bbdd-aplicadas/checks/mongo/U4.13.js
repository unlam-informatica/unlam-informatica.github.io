// u4 · práctica U4.13 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
db.createView("ventasConVendedor", "ventas", [
  { $match: { fecha: { $gte: ISODate("2025-07-01T00:00:00Z") } } },
  { $lookup: { from: "vendedores", localField: "idVendedor", foreignField: "idVendedor", as: "vendedor" } },
  { $unwind: "$vendedor" },
  { $project: { _id: 0, idVenta: 1, fecha: 1, total: 1, vendedor: "$vendedor.nombre", zona: "$vendedor.zona" } }
]);

mostrar(db.ventasConVendedor.find({ zona: "Oeste" }).sort({ idVenta: 1 }));
mostrar(db.ventasConVendedor.aggregate([
  { $group: { _id: "$zona", ventas: { $sum: 1 }, total: { $sum: "$total" } } },
  { $sort: { _id: 1 } }
]));

const info = db.getCollectionInfos({ name: "ventasConVendedor" })[0];
print(info.type + " sobre " + info.options.viewOn);
db.ventas.insertOne({ idVenta: 99, fecha: ISODate("2025-10-01T00:00:00Z"), idVendedor: 1, total: 1000 });
print("la vista refleja el alta: " + (db.ventasConVendedor.countDocuments({ idVenta: 99 }) === 1));
