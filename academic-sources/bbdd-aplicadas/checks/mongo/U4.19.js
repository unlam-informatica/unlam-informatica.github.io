// u4 · práctica U4.19 (datos propios: archivos/tienda/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("productos");
cargar("clientes");
cargar("pedidos");
cargar("resenas");
db.clientes.createIndex({ email: 1 }, { unique: true, name: "uxEmail" });
try {
  db.clientes.insertOne({ codigo: "C-99", email: "cliente01@ejemplo.test", plan: "basico" });
} catch (e) {
  print("duplicado rechazado, codigo " + e.code);
}

const resumen = (plan) => {
  let nodo = plan.queryPlanner.winningPlan;
  const etapas = [];
  while (nodo) { etapas.push(nodo.stage); nodo = nodo.inputStage; }
  const e = plan.executionStats;
  return { etapas: etapas.join(" > "), devueltos: e.nReturned, examinados: e.totalDocsExamined };
};
const consulta = () => db.pedidos.find({ estado: "entregado" }).sort({ fecha: -1 });
print("sin indice: " + JSON.stringify(resumen(consulta().explain("executionStats"))));
db.pedidos.createIndex({ estado: 1, fecha: -1 }, { name: "ixEstadoFecha" });
print("con indice: " + JSON.stringify(resumen(consulta().explain("executionStats"))));

db.sesiones.createIndex({ creadaEn: 1 }, { name: "ttlSesiones", expireAfterSeconds: 1800 });
const ttl = db.sesiones.getIndexes().find(i => i.name === "ttlSesiones");
print("TTL: " + JSON.stringify({ clave: ttl.key, expireAfterSeconds: ttl.expireAfterSeconds }));
