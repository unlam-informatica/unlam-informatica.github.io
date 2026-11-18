// u4 · guía de parcial: un pipeline con $match, $group, $project y $sort, y dos consultas equivalentes.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.ventas.insertMany([
  { _id: 1, localidad: "Morón", estado: "pagada", importe: 400 },
  { _id: 2, localidad: "Morón", estado: "pagada", importe: 600 },
  { _id: 3, localidad: "Haedo", estado: "pagada", importe: 250 },
  { _id: 4, localidad: "Haedo", estado: "anulada", importe: 900 },
  { _id: 5, localidad: "Ramos Mejía", estado: "pagada", importe: 700 }
]);
show(db.ventas.aggregate([
  { $match: { estado: "pagada" } },
  { $group: { _id: "$localidad", total: { $sum: "$importe" }, cantidad: { $sum: 1 } } },
  { $project: { _id: 0, localidad: "$_id", total: 1, cantidad: 1 } },
  { $sort: { total: -1 } }
]));
print("--");
// Dos consultas equivalentes: la coma equivale a $and, y $in a varios $or de igualdad
const a = db.ventas.find({ estado: "pagada", localidad: { $in: ["Morón", "Haedo"] } }, { _id: 1 }).sort({ _id: 1 }).toArray().map(d => d._id);
const b = db.ventas.find({ $and: [{ estado: "pagada" }, { $or: [{ localidad: "Morón" }, { localidad: "Haedo" }] }] }, { _id: 1 }).sort({ _id: 1 }).toArray().map(d => d._id);
print(JSON.stringify(a) + " " + JSON.stringify(b));
