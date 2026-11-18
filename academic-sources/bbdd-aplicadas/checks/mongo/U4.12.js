// u4 · práctica U4.12 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
mostrar(db.ventas.aggregate([
  { $facet: {
      porMedioPago: [
        { $group: { _id: "$medioPago", ventas: { $sum: 1 } } },
        { $sort: { _id: 1 } }
      ],
      porRangoDeTotal: [
        { $bucket: {
            groupBy: "$total",
            boundaries: [0, 20000, 100000, 200000],
            default: "200000 o mas",
            output: { ventas: { $sum: 1 } }
        } }
      ],
      totalGeneral: [
        { $group: { _id: null, ventas: { $sum: 1 }, facturado: { $sum: "$total" } } },
        { $project: { _id: 0 } }
      ]
  } }
]))
