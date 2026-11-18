// u4 · práctica U4.18 (datos propios: archivos/tienda/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("productos");
cargar("clientes");
cargar("pedidos");
cargar("resenas");
mostrar(db.pedidos.aggregate([
  { $facet: {
      porEstado: [
        { $group: { _id: "$estado", pedidos: { $sum: 1 } } },
        { $sort: { _id: 1 } }
      ],
      masVendidos: [
        { $unwind: "$items" },
        { $group: { _id: "$items.sku", unidades: { $sum: "$items.cantidad" } } },
        { $sort: { unidades: -1, _id: 1 } },
        { $limit: 3 }
      ],
      porTamanio: [
        { $bucket: {
            groupBy: { $toDouble: "$total" },
            boundaries: [0, 50000, 150000, 1000000],
            output: { pedidos: { $sum: 1 } }
        } }
      ]
  } }
]))
