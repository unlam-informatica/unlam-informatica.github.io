// u4 · teoría introducción: fechas, esquema flexible, documento completo y errInfo de la validación.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
print(typeof new Date().getTime() + " " + (new Date("1995-12-17T03:24:00Z").getTime() === ISODate("1995-12-17T03:24:00Z").getTime()));

db.contactos.insertMany([
  { nombre: "Juan", edad: 30 },
  { nombre: "Ana", email: "ana@ejemplo.test", activo: true },
  { nombre: "Carlos", direccion: { ciudad: "Buenos Aires", calle: "Corrientes" }, telefonos: ["1111-1111", "2222-2222"] }
]);
print("contactos: " + db.contactos.countDocuments());
print("campos distintos: " + JSON.stringify(db.contactos.find().sort({ nombre: 1 }).toArray().map(d => Object.keys(d).filter(k => k !== "_id").join("+"))));

const r = db.clientes.insertOne({
  nombre: "Pedro Gómez",
  fechaNacimiento: new Date("1990-07-12T00:00:00Z"),
  activo: true,
  saldo: NumberDecimal("2500.50"),
  direccion: { calle: "Avenida Siempre Viva", numero: 742 },
  documentos: ["DNI", "Licencia"],
  fechaRegistro: new Date()
});
print("acknowledged: " + r.acknowledged + ", insertedId es ObjectId: " + (r.insertedId instanceof ObjectId));

db.createCollection("v", { validator: { $jsonSchema: { bsonType: "object", required: ["edad"], properties: { edad: { bsonType: "int", minimum: 18 } } } } });
try {
  db.v.insertOne({ edad: 15 });
} catch (e) {
  print("errInfo: " + JSON.stringify(e.errInfo.details.schemaRulesNotSatisfied[0].propertiesNotSatisfied[0].propertyName)
    + " " + JSON.stringify(e.errInfo.details.schemaRulesNotSatisfied[0].propertiesNotSatisfied[0].details[0].operatorName));
}

// prueba de conexion del laboratorio (instalacion)
db.prueba.insertOne({ mensaje: "conexión correcta", fecha: new Date() });
print("prueba: " + JSON.stringify(db.prueba.find({}, { _id: 0, mensaje: 1 }).toArray()));
print("colecciones: " + JSON.stringify(db.getCollectionNames().includes("prueba")));
