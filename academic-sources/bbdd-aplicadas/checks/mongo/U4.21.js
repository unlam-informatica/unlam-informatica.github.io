// u4 · práctica U4.21 (datos propios: archivos/videoclub/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("peliculas");
cargar("socios");
cargar("prestamos");
print("antes: " + db.prestamos.findOne({ numero: 1 }).fechaPrestamo.constructor.name);

db.prestamos.updateMany({}, [
  { $set: {
      fechaPrestamo: { $dateFromString: { dateString: "$fechaPrestamo", format: "%Y-%m-%d" } },
      fechaDevolucion: { $dateFromString: { dateString: "$fechaDevolucion", format: "%Y-%m-%d" } }
  } }
]);

print("despues: " + db.prestamos.findOne({ numero: 1 }).fechaPrestamo.constructor.name);
print("devoluciones nulas: " + db.prestamos.countDocuments({ fechaDevolucion: null }));

mostrar(db.prestamos.find(
  { fechaPrestamo: { $gte: ISODate("2026-02-01T00:00:00Z"), $lt: ISODate("2026-03-01T00:00:00Z") } },
  { _id: 0, numero: 1, fechaPrestamo: 1 }
).sort({ numero: 1 }));
