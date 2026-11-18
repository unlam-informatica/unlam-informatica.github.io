// u4 · teoría introducción: tipos BSON, números en mongosh y estructura del ObjectId.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.personas.insertOne({
  _id: 1,
  nombre: "Pedro",
  edad: 30,
  altura: 1.75,
  entero: 30.0,
  grande: 3000000000,
  forzado: Double(30),
  visitas: NumberLong("9999999999"),
  saldo: NumberDecimal("2500.50"),
  activo: true,
  segundoNombre: null,
  hobbies: ["leer", "viajar"],
  nacimiento: ISODate("1990-07-12T00:00:00Z"),
  direccion: { calle: "Avenida Siempre Viva", numero: 742 },
  ref: ObjectId("507f1f77bcf86cd799439011")
});
const campos = ["nombre", "edad", "altura", "entero", "grande", "forzado", "visitas", "saldo", "activo", "segundoNombre", "hobbies", "nacimiento", "direccion", "ref"];
const proy = {};
campos.forEach(c => { proy[c] = { $type: "$" + c }; });
show(db.personas.aggregate([{ $project: Object.assign({ _id: 0 }, proy) }]));

// Estructura del ObjectId
const oid = ObjectId("507f1f77bcf86cd799439011");
print("hex: " + oid.toString());
print("timestamp: " + oid.getTimestamp().toISOString());
print("bytes de tiempo (4): " + oid.toString().substring(0, 8));
print("valor aleatorio (5 bytes): " + oid.toString().substring(8, 18));
print("contador (3 bytes): " + oid.toString().substring(18));
print("longitud hex: " + oid.toString().length);

// Un ObjectId generado automaticamente conserva el momento de creacion
const r = db.personas.insertOne({ nombre: "Ana" });
const ahora = Math.floor(Date.now() / 1000);
print("insertedId es ObjectId: " + (r.insertedId instanceof ObjectId));
print("creado hace menos de 60 s: " + (ahora - Math.floor(r.insertedId.getTimestamp().getTime() / 1000) < 60));

// _id propio y _id repetido
db.personas.insertOne({ _id: "p-100", nombre: "Luis" });
try {
  db.personas.insertOne({ _id: "p-100", nombre: "Otro" });
} catch (e) {
  print("_id repetido -> " + e.code);
}
