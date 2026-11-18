// u4 · guía de parcial: lectura de una consulta MQL con filtro, $or, fecha, proyección, orden y límite.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.ventas.insertMany([
  { _id: 1, fecha: ISODate("2025-02-10T00:00:00Z"), cliente: { nombre: "Ana", localidad: "Ramos Mejía" }, importe: 400 },
  { _id: 2, fecha: ISODate("2025-03-01T00:00:00Z"), cliente: { nombre: "Bruno", localidad: "Morón" }, importe: 1500 },
  { _id: 3, fecha: ISODate("2024-12-20T00:00:00Z"), cliente: { nombre: "Carla", localidad: "Haedo" }, importe: 2000 },
  { _id: 4, fecha: ISODate("2025-04-15T00:00:00Z"), cliente: { nombre: "Diego", localidad: "Morón" }, importe: 90 },
  { _id: 5, fecha: ISODate("2025-05-02T00:00:00Z"), cliente: { nombre: "Eva", localidad: "Ramos Mejía" }, importe: 1100 }
]);
show(db.ventas.find(
  {
    fecha: { $gte: ISODate("2025-01-01T00:00:00Z") },
    $or: [
      { "cliente.localidad": "Ramos Mejía" },
      { importe: { $gt: 1000 } }
    ]
  },
  { _id: 0, fecha: 1, "cliente.nombre": 1, importe: 1 }
).sort({ importe: -1 }).limit(2));
