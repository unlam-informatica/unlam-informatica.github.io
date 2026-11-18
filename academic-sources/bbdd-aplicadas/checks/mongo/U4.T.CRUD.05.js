// u4 · teoría CRUD: updateOne/updateMany con $set, $unset, $inc, $mul, $rename, $push, $pull, $addToSet.
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
const r = db.productos.updateOne({ _id: 1 }, { $set: { precio: 50, ultimaRevision: ISODate("2026-07-01T00:00:00Z") } });
print(EJSON.stringify(r, { relaxed: true }));
show(db.productos.find({ _id: 1 }, { _id: 0, nombre: 1, precio: 1, ultimaRevision: 1 }));

print("--- $set con el mismo valor: modifiedCount 0");
print(EJSON.stringify(db.productos.updateOne({ _id: 1 }, { $set: { precio: 50 } }), { relaxed: true }));

print("--- $unset");
db.productos.updateOne({ _id: 1 }, { $unset: { ultimaRevision: "" } });
show(db.productos.find({ _id: 1 }, { _id: 0, nombre: 1, ultimaRevision: 1 }));

print("--- $inc con filtro (updateMany) y $mul");
print(EJSON.stringify(db.productos.updateMany({ categoria: "perifericos" }, { $inc: { stock: -1 } }), { relaxed: true }));
show(db.productos.find({ categoria: "perifericos" }, { _id: 0, nombre: 1, stock: 1 }).sort({ nombre: 1 }));
db.productos.updateOne({ _id: 4 }, { $mul: { precio: 2 } });
print("Notebook x2: " + db.productos.findOne({ _id: 4 }).precio);

print("--- $rename");
db.productos.updateMany({}, { $rename: { etiquetas: "tags" } });
print("campos del _id 2: " + Object.keys(db.productos.findOne({ _id: 2 })).join(","));
db.productos.updateMany({}, { $rename: { tags: "etiquetas" } });

print("--- $push, $addToSet, $pull");
db.productos.updateOne({ _id: 2 }, { $push: { etiquetas: "usb" } });
print("push (permite repetir): " + JSON.stringify(db.productos.findOne({ _id: 2 }).etiquetas));
db.productos.updateOne({ _id: 2 }, { $addToSet: { etiquetas: "usb" } });
print("addToSet (ya existe): " + JSON.stringify(db.productos.findOne({ _id: 2 }).etiquetas));
db.productos.updateOne({ _id: 2 }, { $addToSet: { etiquetas: "gamer" } });
print("addToSet (nuevo): " + JSON.stringify(db.productos.findOne({ _id: 2 }).etiquetas));
db.productos.updateOne({ _id: 2 }, { $pull: { etiquetas: "usb" } });
print("pull (quita todas las coincidencias): " + JSON.stringify(db.productos.findOne({ _id: 2 }).etiquetas));
db.productos.updateOne({ _id: 2 }, { $push: { etiquetas: { $each: ["a", "b"] } } });
print("push con each: " + JSON.stringify(db.productos.findOne({ _id: 2 }).etiquetas));

print("--- Sin filtro que coincida");
print(EJSON.stringify(db.productos.updateOne({ _id: 999 }, { $set: { precio: 1 } }), { relaxed: true }));
print("--- $set condicional con updateMany");
print(EJSON.stringify(db.productos.updateMany({ stock: { $lte: 3 } }, { $set: { reponer: true } }), { relaxed: true }));
