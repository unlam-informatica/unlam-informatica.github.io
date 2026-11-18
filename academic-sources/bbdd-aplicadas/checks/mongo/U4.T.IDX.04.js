// u4 · teoría índices: covered query, hint, getIndexes y dropIndex.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
const docs = [];
for (let i = 1; i <= 500; i++) {
  docs.push({ _id: i, categoria: "cat" + (i % 10), precio: i, nombre: "producto" + i });
}
db.catalogo.insertMany(docs);
print("--- indice simple y sobre campo embebido");
print(db.catalogo.createIndex({ "proveedor.nombre": 1 }));
print(db.catalogo.createIndex({ "proveedor.nombre": 1 }) + " (repetirlo no hace nada)");
print(JSON.stringify(db.catalogo.getIndexes().map(i => i.name)));
db.catalogo.dropIndex({ "proveedor.nombre": 1 });
db.catalogo.createIndex({ categoria: 1, precio: 1 });
const m = (e) => { const s = e.executionStats; const st = []; let n = e.queryPlanner.winningPlan; while (n) { st.push(n.stage); n = n.inputStage; }
  print("  " + st.join(" > ") + " | nReturned=" + s.nReturned + " keysExamined=" + s.totalKeysExamined + " docsExamined=" + s.totalDocsExamined); };

print("consulta que pide nombre (hay que leer el documento):");
m(db.catalogo.find({ categoria: "cat3" }, { _id: 0, categoria: 1, precio: 1, nombre: 1 }).explain("executionStats"));
print("covered query (solo campos del indice, sin _id):");
m(db.catalogo.find({ categoria: "cat3" }, { _id: 0, categoria: 1, precio: 1 }).explain("executionStats"));
print("con _id en la proyeccion deja de estar cubierta:");
m(db.catalogo.find({ categoria: "cat3" }, { categoria: 1, precio: 1 }).explain("executionStats"));

print("--- hint");
db.catalogo.createIndex({ precio: 1 });
print("sin hint el planificador elige uno; con hint se fuerza:");
m(db.catalogo.find({ categoria: "cat3", precio: { $gt: 100 } }).hint({ precio: 1 }).explain("executionStats"));
m(db.catalogo.find({ categoria: "cat3", precio: { $gt: 100 } }).hint({ categoria: 1, precio: 1 }).explain("executionStats"));
m(db.catalogo.find({ categoria: "cat3" }).hint({ $natural: 1 }).explain("executionStats"));

print("--- getIndexes / dropIndex");
show(db.catalogo.getIndexes().map(i => ({ name: i.name, key: i.key })));
print(EJSON.stringify(db.catalogo.dropIndex("precio_1"), { relaxed: true }));
try {
  db.catalogo.dropIndex("categoria_hashed");
} catch (e) {
  print("dropIndex de un indice que no existe -> " + e.codeName);
}
try {
  db.catalogo.dropIndex("_id_");
} catch (e) {
  print("dropIndex del _id -> " + e.codeName);
}
print(EJSON.stringify(db.catalogo.dropIndexes(), { relaxed: true }));
show(db.catalogo.getIndexes().map(i => i.name));
