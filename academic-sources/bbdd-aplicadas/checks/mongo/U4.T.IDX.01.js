// u4 · teoría índices: explain('executionStats'), COLLSCAN vs IXSCAN, índice simple y compuesto (ESR).
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
const docs = [];
const estados = ["pendiente", "entregado", "cancelado", "entregado"];
for (let i = 1; i <= 1000; i++) {
  docs.push({ _id: i, cliente: "c" + (i % 50), estado: estados[i % 4], total: (i * 7) % 500, fecha: new Date(Date.UTC(2026, 0, 1) + i * 86400000) });
}
db.ordenes.insertMany(docs);
const resumen = (e) => {
  const s = e.executionStats;
  const stages = [];
  let n = e.queryPlanner.winningPlan;
  while (n) { stages.push(n.stage); n = n.inputStage; }
  print("  etapas: " + stages.join(" > ") + " | nReturned=" + s.nReturned + " keysExamined=" + s.totalKeysExamined + " docsExamined=" + s.totalDocsExamined);
};
print("Sin indice:");
resumen(db.ordenes.find({ cliente: "c7" }).explain("executionStats"));
db.ordenes.createIndex({ cliente: 1 });
print("Con indice simple en cliente:");
resumen(db.ordenes.find({ cliente: "c7" }).explain("executionStats"));

// compuesto: igualdad, ordenamiento, rango
print("Filtro estado (igualdad) + total (rango), ordenado por fecha:");
db.ordenes.createIndex({ estado: 1, total: 1, fecha: 1 });
resumen(db.ordenes.find({ estado: "entregado", total: { $gte: 400 } }).sort({ fecha: 1 }).explain("executionStats"));
db.ordenes.dropIndex({ estado: 1, total: 1, fecha: 1 });
db.ordenes.createIndex({ estado: 1, fecha: 1, total: 1 });
print("Con el orden E-S-R (igualdad, sort, rango):");
resumen(db.ordenes.find({ estado: "entregado", total: { $gte: 400 } }).sort({ fecha: 1 }).explain("executionStats"));

// explain de un aggregate: el $match inicial puede usar el indice
const ea = db.ordenes.explain("executionStats").aggregate([
  { $match: { cliente: "c7" } },
  { $group: { _id: "$estado", total: { $sum: "$total" } } }
]);
const plan = ea.stages[0].$cursor;
print("aggregate: " + plan.queryPlanner.winningPlan.inputStage.inputStage.stage + " | docsExamined=" + plan.executionStats.totalDocsExamined);
