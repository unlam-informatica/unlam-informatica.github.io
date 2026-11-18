// u4 · práctica U4.04 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
db.createCollection("gastos", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["descripcion", "monto"],
      properties: {
        descripcion: { bsonType: "string", minLength: 3 },
        monto: { bsonType: ["int", "long", "double", "decimal"], minimum: 0 }
      }
    }
  },
  validationAction: "error"
});

db.gastos.insertOne({ descripcion: "Flete", monto: 12500 });

try {
  db.gastos.insertOne({ descripcion: "Bolsas", monto: -50 });
} catch (e) {
  print("rechazado, codigo " + e.code);
}
try {
  db.gastos.insertOne({ monto: 300 });
} catch (e) {
  print("rechazado, codigo " + e.code);
}
print("documentos guardados: " + db.gastos.countDocuments());
