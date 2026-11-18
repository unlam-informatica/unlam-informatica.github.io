// u4 · teoría Compass: los campos Filter, Project, Sort, Skip, Limit y Collation, su equivalente en shell, índice con nombre y explain.
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
const ids = (cur) => JSON.stringify(cur.toArray().map(d => d._id));
print("Filter { categoria: 'audio' }: " + ids(db.productos.find({ categoria: "audio" }).sort({ _id: 1 })));
print("Filter + Sort + Limit: " + ids(db.productos.find({ precio: { $gt: 40 } }).sort({ precio: -1 }).limit(2)));
print("Filter con $or: " + ids(db.productos.find({ $or: [{ categoria: "audio", precio: { $gt: 70 } }, { stock: 0 }] }).sort({ _id: 1 })));
show(db.productos.find({ categoria: "perifericos" }, { _id: 0, nombre: 1, precio: 1 }).sort({ nombre: 1 }).skip(1).limit(1));

// Collation: strength 1 ignora mayusculas y acentos
db.localidades.insertMany([{ _id: 1, nombre: "Morón" }, { _id: 2, nombre: "moron" }, { _id: 3, nombre: "MORON" }, { _id: 4, nombre: "Haedo" }]);
print("sin collation: " + ids(db.localidades.find({ nombre: "moron" })));
print("collation es strength 1: " + ids(db.localidades.find({ nombre: "moron" }).collation({ locale: "es", strength: 1 }).sort({ _id: 1 })));
// numericOrdering
db.codigos.insertMany([{ _id: 1, c: "10" }, { _id: 2, c: "2" }, { _id: 3, c: "1" }]);
print("orden textual: " + JSON.stringify(db.codigos.find().sort({ c: 1 }).toArray().map(d => d.c)));
print("numericOrdering: " + JSON.stringify(db.codigos.find().sort({ c: 1 }).collation({ locale: "es", numericOrdering: true }).toArray().map(d => d.c)));

// la tilde importa en un filtro sin collation
db.clientes.insertOne({ _id: "c4", nombre: "Dora", localidad: "Ramos Mejía" });
print("'Ramos Mejia' sin tilde: " + db.clientes.countDocuments({ localidad: "Ramos Mejia" }));
print("'Ramos Mejía' con tilde: " + db.clientes.countDocuments({ localidad: "Ramos Mejía" }));

// indice con nombre propio
print(db.productos.createIndex({ categoria: 1 }, { name: "categoria_indx" }));
print(JSON.stringify(db.productos.getIndexes().map(i => i.name)));
db.productos.dropIndex("categoria_indx");

// campos que muestra la pestana Explain
const e = db.productos.find({ categoria: "audio" }).explain("executionStats");
print("nReturned=" + e.executionStats.nReturned + " totalKeysExamined=" + e.executionStats.totalKeysExamined + " totalDocsExamined=" + e.executionStats.totalDocsExamined + " stage=" + e.queryPlanner.winningPlan.stage);
