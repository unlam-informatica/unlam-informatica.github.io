// u4 · práctica U4.10 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
const resumen = (plan) => {
  let nodo = plan.queryPlanner.winningPlan;
  const etapas = [];
  let indice = null;
  while (nodo) {
    etapas.push(nodo.stage);
    if (nodo.stage === "IXSCAN") indice = nodo.indexName;
    nodo = nodo.inputStage;
  }
  const e = plan.executionStats;
  return { etapas: etapas.join(" > "), indice: indice, devueltos: e.nReturned, examinados: e.totalDocsExamined };
};
const consulta = () => db.ventas.find({ sucursal: "Norte" }).sort({ fecha: -1 });

print("sin indice: " + JSON.stringify(resumen(consulta().explain("executionStats"))));
db.ventas.createIndex({ sucursal: 1, fecha: -1 }, { name: "ixSucursalFecha" });
print("con indice: " + JSON.stringify(resumen(consulta().explain("executionStats"))));
