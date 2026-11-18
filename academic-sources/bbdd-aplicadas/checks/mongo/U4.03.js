// u4 · práctica U4.03 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
const contar = (filtro) => db.ventas.countDocuments(filtro);
print("lt 10:                     " + contar({ descuento: { $lt: 10 } }));
print("not gte 10:                " + contar({ descuento: { $not: { $gte: 10 } } }));
print("sin campo descuento:       " + contar({ descuento: { $exists: false } }));
print("con descuento y not gte 10: " + contar({ descuento: { $exists: true, $not: { $gte: 10 } } }));
