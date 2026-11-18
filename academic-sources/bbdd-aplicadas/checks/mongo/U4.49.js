// u4 · ejercicio U4.49: jerarquía de clases de pago en una única colección polimórfica.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.pagos.insertMany([
  { _id: 1, tipo: "tarjeta", monto: 1200, cuotas: 3, ultimos4: "4242" },
  { _id: 2, tipo: "transferencia", monto: 800, aliasDestino: "tienda.demo" },
  { _id: 3, tipo: "tarjeta", monto: 300, cuotas: 1, ultimos4: "1111" },
  { _id: 4, tipo: "transferencia", monto: 500, aliasDestino: "tienda.demo" }
]);
show(db.pagos.aggregate([
  { $group: { _id: "$tipo", total: { $sum: "$monto" }, cantidad: { $sum: 1 } } },
  { $sort: { _id: 1 } }
]));
print("--");
show(db.pagos.find({ cuotas: { $gt: 1 } }, { _id: 1, tipo: 1, cuotas: 1 }));
print("--");
show(db.pagos.find({ cuotas: { $exists: false } }, { _id: 1 }).sort({ _id: 1 }));
