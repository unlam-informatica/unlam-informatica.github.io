// u4 · teoría CRUD: find con operadores de comparación, lógicos, de arrays y de elementos.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.productos.insertMany([
  { _id: 1, nombre: "Teclado",    categoria: "perifericos",  precio: 45,  stock: 12, etiquetas: ["usb", "oficina"] },
  { _id: 2, nombre: "Mouse",      categoria: "perifericos",  precio: 20,  stock: 30, etiquetas: ["usb"] },
  { _id: 3, nombre: "Monitor",    categoria: "pantallas",    precio: 300, stock: 5,  etiquetas: ["hdmi", "oficina"] },
  { _id: 4, nombre: "Notebook",   categoria: "computadoras", precio: 900, stock: 3,  etiquetas: ["portatil"] },
  { _id: 5, nombre: "Auriculares", categoria: "audio",       precio: 60,  stock: 0,  etiquetas: ["usb", "audio"] },
  { _id: 6, nombre: "Parlante",   categoria: "audio",        precio: 85,  stock: 8,  etiquetas: ["audio", "bluetooth"] },
  { _id: 7, nombre: "Webcam",     categoria: "perifericos",  precio: 55,  stock: 14, etiquetas: ["usb", "video"] },
  { _id: 8, nombre: "Impresora",  categoria: "impresion",    precio: 210, stock: 2,  etiquetas: ["oficina"] }
]);
db.clientes.insertMany([
  { _id: "c1", nombre: "Ana",   localidad: "Ramos Mejía" },
  { _id: "c2", nombre: "Bruno", localidad: "Morón" },
  { _id: "c3", nombre: "Carla", localidad: "Haedo" }
]);
db.pedidos.insertMany([
  { _id: 101, fecha: ISODate("2026-03-05T00:00:00Z"), estado: "entregado", clienteId: "c1", total: 110,
    items: [{ productoId: 1, cantidad: 2, precioUnitario: 45 }, { productoId: 2, cantidad: 1, precioUnitario: 20 }] },
  { _id: 102, fecha: ISODate("2026-03-18T00:00:00Z"), estado: "entregado", clienteId: "c2", total: 300,
    items: [{ productoId: 3, cantidad: 1, precioUnitario: 300 }] },
  { _id: 103, fecha: ISODate("2026-04-02T00:00:00Z"), estado: "pendiente", clienteId: "c1", total: 940,
    items: [{ productoId: 4, cantidad: 1, precioUnitario: 900 }, { productoId: 2, cantidad: 2, precioUnitario: 20 }] },
  { _id: 104, fecha: ISODate("2026-04-20T00:00:00Z"), estado: "cancelado", clienteId: "c3", total: 60,
    items: [{ productoId: 5, cantidad: 1, precioUnitario: 60 }] },
  { _id: 105, fecha: ISODate("2026-05-11T00:00:00Z"), estado: "entregado", clienteId: "c2", total: 185,
    items: [{ productoId: 1, cantidad: 1, precioUnitario: 45 }, { productoId: 7, cantidad: 1, precioUnitario: 55 }, { productoId: 6, cantidad: 1, precioUnitario: 85 }] },
  { _id: 106, fecha: ISODate("2026-05-30T00:00:00Z"), estado: "entregado", clienteId: "c3", total: 60,
    items: [{ productoId: 2, cantidad: 3, precioUnitario: 20 }] },
  { _id: 107, fecha: ISODate("2026-06-14T00:00:00Z"), estado: "pendiente", clienteId: "c1", total: 210,
    items: [{ productoId: 8, cantidad: 1, precioUnitario: 210 }] },
  { _id: 108, fecha: ISODate("2026-06-20T00:00:00Z"), estado: "entregado", clienteId: "c9", total: 40,
    items: [{ productoId: 2, cantidad: 2, precioUnitario: 20 }] }
]);
const ids = (cur) => JSON.stringify(cur.sort({ _id: 1 }).toArray().map(d => d._id));
print("precio > 100: " + ids(db.productos.find({ precio: { $gt: 100 } })));
print("precio entre 45 y 85: " + ids(db.productos.find({ precio: { $gte: 45, $lte: 85 } })));
print("categoria $in: " + ids(db.productos.find({ categoria: { $in: ["audio", "pantallas"] } })));
print("categoria $nin: " + ids(db.productos.find({ categoria: { $nin: ["perifericos", "audio"] } })));
print("$and implicito: " + ids(db.productos.find({ categoria: "perifericos", precio: { $lt: 50 } })));
print("$or: " + ids(db.productos.find({ $or: [{ stock: 0 }, { precio: { $gte: 900 } }] })));
print("$nor: " + ids(db.productos.find({ $nor: [{ categoria: "perifericos" }, { categoria: "audio" }] })));
print("$not: " + ids(db.productos.find({ precio: { $not: { $gt: 60 } } })));
print("$all: " + ids(db.productos.find({ etiquetas: { $all: ["usb", "oficina"] } })));
print("etiqueta usb (array): " + ids(db.productos.find({ etiquetas: "usb" })));
print("$size 2: " + ids(db.productos.find({ etiquetas: { $size: 2 } })));
print("etiquetas.0 = audio: " + ids(db.productos.find({ "etiquetas.0": "audio" })));
print("$elemMatch: " + ids(db.pedidos.find({ items: { $elemMatch: { productoId: 2, cantidad: { $gte: 2 } } } })));
print("sin elemMatch: " + ids(db.pedidos.find({ "items.productoId": 2, "items.cantidad": { $gte: 2 } })));
db.productos.insertOne({ _id: 9, nombre: "Cable", precio: "15" });
print("$exists stock: " + ids(db.productos.find({ stock: { $exists: false } })));
print("$type string: " + ids(db.productos.find({ precio: { $type: "string" } })));
print("$type number: " + ids(db.productos.find({ precio: { $type: "number" } })));
print("precio > 100 con cadena en la coleccion: " + ids(db.productos.find({ precio: { $gt: 100 } })));
print("$regex: " + ids(db.productos.find({ nombre: { $regex: "^m", $options: "i" } })));
