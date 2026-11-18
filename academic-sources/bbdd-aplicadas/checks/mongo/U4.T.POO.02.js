// u4 · POO: el mismo Pedido como documento (líneas embebidas, cliente por referencia).
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.clientes.insertMany([
  { _id: 1, nombre: "Ana", localidad: "Ramos Mejía" },
  { _id: 2, nombre: "Bruno", localidad: "Morón" }
]);
db.pedidos.insertMany([
  { _id: 101, fecha: ISODate("2026-03-05T00:00:00Z"), clienteId: 1,
    lineas: [
      { producto: "Teclado", cantidad: 2, precioUnitario: 45 },
      { producto: "Mouse", cantidad: 1, precioUnitario: 20 }
    ] },
  { _id: 102, fecha: ISODate("2026-03-18T00:00:00Z"), clienteId: 2,
    lineas: [{ producto: "Monitor", cantidad: 1, precioUnitario: 300 }] }
]);
// Una lectura devuelve el pedido completo, con sus líneas
show(db.pedidos.find({ _id: 101 }));
print("--");
// El cliente va por referencia: para traerlo se hace una segunda lectura o un $lookup
show(db.pedidos.aggregate([
  { $match: { _id: 101 } },
  { $lookup: { from: "clientes", localField: "clienteId", foreignField: "_id", as: "cliente" } },
  { $unwind: "$cliente" },
  { $project: { _id: 1, cliente: "$cliente.nombre", cantidadLineas: { $size: "$lineas" } } }
]));
print("--");
// Cambiar el precio de una línea embebida es una sola actualización sobre un documento
const r = db.pedidos.updateOne({ _id: 101, "lineas.producto": "Mouse" }, { $set: { "lineas.$.precioUnitario": 25 } });
print("modificados: " + r.modifiedCount);
show(db.pedidos.find({ _id: 101 }, { _id: 0, lineas: 1 }));
