// u4 · práctica U4.05 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
print("A) electricidad con cantidad >= 3 en el mismo articulo");
mostrar(db.ventas.find(
  { articulos: { $elemMatch: { categoria: "electricidad", cantidad: { $gte: 3 } } } },
  { _id: 0, idVenta: 1 }
).sort({ idVenta: 1 }));

print("B) las dos condiciones pueden cumplirlas articulos distintos");
mostrar(db.ventas.find(
  { "articulos.categoria": "electricidad", "articulos.cantidad": { $gte: 3 } },
  { _id: 0, idVenta: 1 }
).sort({ idVenta: 1 }));

print("C) etiquetas con promo y web");
mostrar(db.ventas.find({ etiquetas: { $all: ["promo", "web"] } }, { _id: 0, idVenta: 1, etiquetas: 1 }).sort({ idVenta: 1 }));

print("D) ventas con exactamente tres articulos");
mostrar(db.ventas.find({ articulos: { $size: 3 } }, { _id: 0, idVenta: 1 }).sort({ idVenta: 1 }));
