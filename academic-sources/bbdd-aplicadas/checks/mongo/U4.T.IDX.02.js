// u4 · teoría índices: único, multikey (array), parcial y sparse.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
const stagesDe = (e) => { const st = []; let n = e.queryPlanner.winningPlan; while (n) { st.push(n.stage); n = n.inputStage; } return st.join(" > "); };

print("--- unico");
db.usuarios.createIndex({ email: 1 }, { unique: true });
db.usuarios.insertOne({ _id: 1, email: "ana@ejemplo.test" });
try {
  db.usuarios.insertOne({ _id: 2, email: "ana@ejemplo.test" });
} catch (e) {
  print("duplicado -> " + e.code + " " + e.errmsg.split(" collection:")[0]);
}
// sin email: el valor ausente cuenta como null, y solo cabe uno
db.usuarios.insertOne({ _id: 3 });
try {
  db.usuarios.insertOne({ _id: 4 });
} catch (e) {
  print("dos documentos sin email -> " + e.code);
}

print("--- multikey (array)");
db.articulos.insertMany([
  { _id: 1, titulo: "A", etiquetas: ["bd", "mongo"] },
  { _id: 2, titulo: "B", etiquetas: ["sql", "bd"] },
  { _id: 3, titulo: "C", etiquetas: ["redes"] }
]);
db.articulos.createIndex({ etiquetas: 1 });
const e1 = db.articulos.find({ etiquetas: "bd" }).explain("executionStats");
print(stagesDe(e1) + " | isMultiKey=" + e1.queryPlanner.winningPlan.inputStage.isMultiKey + " nReturned=" + e1.executionStats.nReturned);

print("--- sparse: solo documentos que tienen el campo");
db.contactos.insertMany([
  { _id: 1, nombre: "Ana", telefono: "1111" },
  { _id: 2, nombre: "Bruno" },
  { _id: 3, nombre: "Carla", telefono: null }
]);
db.contactos.createIndex({ telefono: 1 }, { sparse: true });
print("recorriendo el indice sparse: " + JSON.stringify(db.contactos.find().hint({ telefono: 1 }).sort({ _id: 1 }).toArray().map(d => d._id)));
print("find({ telefono: null }): " + JSON.stringify(db.contactos.find({ telefono: null }).sort({ _id: 1 }).toArray().map(d => d._id)));

print("--- parcial");
db.ventas.insertMany([
  { _id: 1, estado: "activa", total: 50 },
  { _id: 2, estado: "activa", total: 700 },
  { _id: 3, estado: "baja", total: 900 },
  { _id: 4, estado: "activa", total: 1200 }
]);
db.ventas.createIndex({ total: 1 }, { partialFilterExpression: { estado: "activa" } });
const conFiltro = db.ventas.find({ estado: "activa", total: { $gt: 500 } }).explain("executionStats");
print("consulta que incluye el filtro del indice: " + stagesDe(conFiltro));
const sinFiltro = db.ventas.find({ total: { $gt: 500 } }).explain("executionStats");
print("consulta que NO lo incluye: " + stagesDe(sinFiltro));
