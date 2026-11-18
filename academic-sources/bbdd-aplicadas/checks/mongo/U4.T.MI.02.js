// u4 · teoría introducción: colecciones, creación implícita/explícita y validación $jsonSchema.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.createCollection("empleados", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["nombre", "edad"],
      properties: {
        nombre: { bsonType: "string", description: "cadena obligatoria" },
        edad: { bsonType: ["int", "long", "double"], minimum: 18, maximum: 70, description: "numero entre 18 y 70" }
      }
    }
  }
});
db.empleados.insertOne({ nombre: "Ana", edad: 30 });
db.empleados.insertOne({ nombre: "Bruno", edad: 41.0 });
try {
  db.empleados.insertOne({ nombre: "Carla", edad: 15 });
} catch (e) {
  print("edad 15 -> codigo " + e.code + ": " + e.message);
}
try {
  db.empleados.insertOne({ nombre: "Diego" });
} catch (e) {
  print("sin edad -> codigo " + e.code + ": " + e.message);
}
try {
  db.empleados.insertOne({ nombre: "Eva", edad: "treinta" });
} catch (e) {
  print("edad texto -> codigo " + e.code);
}
print("empleados: " + db.empleados.countDocuments());

// Con bsonType "int" a secas, un double entero (30.0) falla
db.createCollection("solo_int", { validator: { $jsonSchema: { bsonType: "object", properties: { edad: { bsonType: "int" } } } } });
db.solo_int.insertOne({ edad: 30 });
try {
  db.solo_int.insertOne({ edad: 30.5 });
} catch (e) {
  print("solo_int 30.5 -> " + e.code);
}
db.solo_int.insertOne({ edad: NumberInt(31) });
show(db.solo_int.aggregate([{ $project: { _id: 0, edad: 1, t: { $type: "$edad" } } }, { $sort: { edad: 1 } }]));

// Creacion implicita
db.nueva.insertOne({ x: 1 });
print(JSON.stringify(db.getCollectionNames().sort()));
print("drop existente: " + db.nueva.drop());
print("drop inexistente: " + db.nueva.drop());
print(JSON.stringify(db.getCollectionNames().sort()));
