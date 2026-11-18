// u4 · teoría agregación: $group con acumuladores; operadores de expresión dentro de $group.
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
print("--- acumuladores por estado");
show(db.pedidos.aggregate([
  { $group: {
      _id: "$estado",
      cantidad: { $sum: 1 },
      ingresos: { $sum: "$total" },
      promedio: { $avg: "$total" },
      minimo: { $min: "$total" },
      maximo: { $max: "$total" }
  } },
  { $sort: { _id: 1 } }
]));
print("--- $first/$last dependen del orden: se ordena antes");
show(db.pedidos.aggregate([
  { $sort: { fecha: 1 } },
  { $group: {
      _id: "$clienteId",
      primerPedido: { $first: "$_id" },
      ultimoPedido: { $last: "$_id" },
      pedidos: { $push: "$_id" },
      estados: { $addToSet: "$estado" }
  } },
  { $addFields: { estados: { $sortArray: { input: "$estados", sortBy: 1 } } } },
  { $sort: { _id: 1 } }
]));
print("--- _id: null agrupa toda la coleccion");
show(db.pedidos.aggregate([{ $group: { _id: null, pedidos: { $sum: 1 }, total: { $sum: "$total" } } }]));
print("--- $group por mes con operador de fecha");
show(db.pedidos.aggregate([
  { $group: { _id: { mes: { $month: "$fecha" } }, total: { $sum: "$total" } } },
  { $sort: { "_id.mes": 1 } }
]));
print("--- $multiply, $cmp y $round son operadores de expresion: se usan DENTRO de un acumulador o de $project");
show(db.pedidos.aggregate([
  { $unwind: "$items" },
  { $group: {
      _id: "$estado",
      importe: { $sum: { $multiply: ["$items.cantidad", "$items.precioUnitario"] } },
      promedioItem: { $avg: { $round: [{ $multiply: ["$items.cantidad", "$items.precioUnitario"] }, 0] } }
  } },
  { $sort: { _id: 1 } }
]));
show(db.productos.aggregate([
  { $project: { _id: 1, nombre: 1, frenteA100: { $cmp: ["$precio", 100] } } },
  { $sort: { _id: 1 } },
  { $limit: 4 }
]));
