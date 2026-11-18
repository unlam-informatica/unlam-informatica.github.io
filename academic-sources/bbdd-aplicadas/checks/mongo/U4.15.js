// u4 · práctica U4.15 (datos propios: archivos/tienda/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("productos");
cargar("clientes");
cargar("pedidos");
cargar("resenas");
mostrar(db.productos.find(
  {
    activo: true,
    etiquetas: "oficina",
    precio: { $lt: NumberDecimal("20000") }
  },
  { _id: 0, sku: 1, nombre: 1, etiquetas: 1 }
).sort({ sku: 1 }));

mostrar(db.productos.find(
  { "especificaciones.color": "negro" },
  { _id: 0, sku: 1, "especificaciones.color": 1 }
).sort({ sku: 1 }));
