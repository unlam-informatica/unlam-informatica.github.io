// u4 · teoría índices: TTL y texto.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.sesiones.createIndex({ creada: 1 }, { expireAfterSeconds: 3600 });
db.sesiones.insertMany([
  { _id: 1, usuario: "u1", creada: new Date() },
  { _id: 2, usuario: "u2", creada: new Date(Date.now() - 2 * 3600 * 1000) }
]);
const idx = db.sesiones.getIndexes().find(i => i.name === "creada_1");
print("TTL: " + JSON.stringify({ name: idx.name, key: idx.key, expireAfterSeconds: idx.expireAfterSeconds }));
print("los documentos siguen hasta que corre el proceso de fondo (cada 60 s): " + db.sesiones.countDocuments());

print("--- texto");
db.apuntes.insertMany([
  { _id: 1, titulo: "Indices en MongoDB", cuerpo: "Un indice evita recorrer toda la coleccion" },
  { _id: 2, titulo: "Agregacion", cuerpo: "El pipeline procesa documentos por etapas" },
  { _id: 3, titulo: "Transacciones", cuerpo: "ACID y sesiones en MongoDB" }
]);
db.apuntes.createIndex({ titulo: "text", cuerpo: "text" });
print("mongodb:"); show(db.apuntes.find({ $text: { $search: "mongodb" } }, { _id: 1 }).sort({ _id: 1 }));
print("pipeline etapas (cualquiera de los terminos):"); show(db.apuntes.find({ $text: { $search: "pipeline etapas" } }, { _id: 1 }));
print("mongodb sin transacciones:"); show(db.apuntes.find({ $text: { $search: "mongodb -transacciones" } }, { _id: 1 }));
print("frase exacta:"); show(db.apuntes.find({ $text: { $search: "\"por etapas\"" } }, { _id: 1 }));
try {
  db.apuntes.createIndex({ cuerpo: "text" });
} catch (e) {
  print("segundo indice de texto -> " + e.codeName);
}
