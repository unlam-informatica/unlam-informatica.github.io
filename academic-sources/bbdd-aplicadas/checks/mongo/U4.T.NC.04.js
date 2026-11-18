// u4 · conceptos NoSQL: modelo jerárquico como documento anidado.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.organigrama.insertOne({
  _id: "org",
  nombre: "Departamento de Sistemas",
  areas: [
    { nombre: "Desarrollo", equipos: [{ nombre: "Web", integrantes: 4 }, { nombre: "Móvil", integrantes: 3 }] },
    { nombre: "Infraestructura", equipos: [{ nombre: "Redes", integrantes: 2 }] }
  ]
});
show(db.organigrama.find({ "areas.equipos.nombre": "Redes" }, { _id: 0, nombre: 1 }));
show(db.organigrama.aggregate([
  { $unwind: "$areas" },
  { $unwind: "$areas.equipos" },
  { $group: { _id: "$areas.nombre", integrantes: { $sum: "$areas.equipos.integrantes" } } },
  { $sort: { _id: 1 } }
]));
