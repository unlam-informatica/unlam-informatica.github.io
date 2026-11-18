// u4 · teoría CRUD: fechas y type bracketing (Date vs String).
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
db.eventos.insertMany([
  { _id: 1, nombre: "alta", fecha: ISODate("2026-01-15T00:00:00Z") },
  { _id: 2, nombre: "baja", fecha: ISODate("2026-02-20T00:00:00Z") },
  { _id: 3, nombre: "texto", fecha: "2026-01-20" }
]);
const ids = (cur) => JSON.stringify(cur.sort({ _id: 1 }).toArray().map(d => d._id));
print("rango con Date: " + ids(db.eventos.find({ fecha: { $gte: ISODate("2026-01-01T00:00:00Z"), $lt: ISODate("2026-02-01T00:00:00Z") } })));
print("rango con String: " + ids(db.eventos.find({ fecha: { $gte: "2026-01-01", $lt: "2026-02-01" } })));
print("tipos: " + JSON.stringify(db.eventos.aggregate([{ $project: { t: { $type: "$fecha" } } }, { $sort: { _id: 1 } }]).toArray().map(d => d.t)));
print("fecha como Date: " + ids(db.eventos.find({ fecha: { $type: "date" } })));
// $toDate convierte el texto y permite comparar
show(db.eventos.aggregate([
  { $addFields: { fechaReal: { $toDate: "$fecha" } } },
  { $match: { fechaReal: { $gte: ISODate("2026-01-01T00:00:00Z"), $lt: ISODate("2026-02-01T00:00:00Z") } } },
  { $project: { _id: 1 } },
  { $sort: { _id: 1 } }
]));
// ISODate y new Date generan el mismo tipo
print(ISODate("2026-01-15T00:00:00Z").getTime() === new Date("2026-01-15T00:00:00Z").getTime());
