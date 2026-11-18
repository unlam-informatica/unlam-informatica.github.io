// u4 · práctica U4.14 (datos propios: archivos/tienda/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("productos");
cargar("clientes");
cargar("pedidos");
cargar("resenas");
print("antes: " + db.productos.countDocuments());

db.productos.updateMany(
  { categoria: "hogar" },
  [ { $set: { precio: { $round: [{ $multiply: ["$precio", NumberDecimal("1.10")] }, 2] } } } ]
);
mostrar(db.productos.aggregate([
  { $match: { categoria: "hogar" } },
  { $project: { _id: 0, sku: 1, precio: { $toString: "$precio" } } },
  { $sort: { sku: 1 } }
]));

const r = db.productos.deleteMany({ stock: 0, activo: false });
print("borrados: " + r.deletedCount);
print("despues: " + db.productos.countDocuments());
