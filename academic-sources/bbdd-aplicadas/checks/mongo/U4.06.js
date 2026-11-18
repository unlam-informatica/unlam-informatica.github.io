// u4 · práctica U4.06 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
const filtro = { sucursal: "Sur", total: { $gte: 100000 } };
const r1 = db.ventas.updateMany(filtro, { $addToSet: { etiquetas: "revisada" } });
print("primera vez: " + r1.matchedCount + " encontradas, " + r1.modifiedCount + " modificadas");
const r2 = db.ventas.updateMany(filtro, { $addToSet: { etiquetas: "revisada" } });
print("segunda vez: " + r2.matchedCount + " encontradas, " + r2.modifiedCount + " modificadas");

const r3 = db.ventas.updateMany({ descuento: 5 }, { $unset: { descuento: "" }, $set: { descuentoAplicado: false } });
print("sin descuento de 5: " + r3.modifiedCount + " modificadas");

const r4 = db.ventas.updateOne({ idVenta: 1 }, { $inc: { "articulos.0.cantidad": 1 } });
print("articulo 0 de la venta 1: " + r4.modifiedCount + " modificada");

mostrar(db.ventas.find({ etiquetas: "revisada" }, { _id: 0, idVenta: 1, etiquetas: 1 }).sort({ idVenta: 1 }));
mostrar(db.ventas.find({ idVenta: 1 }, { _id: 0, idVenta: 1, "articulos.codigo": 1, "articulos.cantidad": 1 }));
print("descuentoAplicado: " + db.ventas.countDocuments({ descuentoAplicado: false }));
