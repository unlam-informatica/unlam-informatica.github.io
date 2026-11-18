// u4 · teoría CRUD: insertOne, insertMany ordered true/false con un duplicado.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
const r1 = db.socios.insertOne({ _id: 1, nombre: "Ana", edad: 28 });
print("insertOne: " + EJSON.stringify(r1, { relaxed: true }));

const r2 = db.socios.insertMany([
  { _id: 2, nombre: "Bruno", edad: 34 },
  { _id: 3, nombre: "Carla", edad: 23 }
]);
print("insertMany: " + EJSON.stringify(r2, { relaxed: true }));

// ordered: true (por defecto): se detiene en el primer error
try {
  db.socios.insertMany([
    { _id: 4, nombre: "Diego" },
    { _id: 2, nombre: "Duplicado" },
    { _id: 5, nombre: "Elena" }
  ]);
} catch (e) {
  print("ordered:true -> codigo " + e.code + ", insertados: " + e.result.insertedCount);
  print("mensaje: " + e.writeErrors[0].errmsg.split(" collection:")[0]);
}
print("socios tras ordered:true -> " + JSON.stringify(db.socios.find({}, { _id: 1 }).sort({ _id: 1 }).toArray().map(d => d._id)));

// ordered: false: sigue con el resto
try {
  db.socios.insertMany([
    { _id: 6, nombre: "Fabi" },
    { _id: 2, nombre: "Duplicado" },
    { _id: 7, nombre: "Gaby" }
  ], { ordered: false });
} catch (e) {
  print("ordered:false -> codigo " + e.code + ", insertados: " + e.result.insertedCount + ", errores: " + e.writeErrors.length);
}
print("socios tras ordered:false -> " + JSON.stringify(db.socios.find({}, { _id: 1 }).sort({ _id: 1 }).toArray().map(d => d._id)));
