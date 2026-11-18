// u4 · ejercicio U4.45: curso con docente por referencia e inscripciones embebidas.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.docentes.insertMany([
  { _id: "d1", nombre: "Marta Ríos" },
  { _id: "d2", nombre: "Hugo Paz" }
]);
db.cursos.insertMany([
  { _id: "BD1", nombre: "Bases de datos I", docenteId: "d1",
    inscripciones: [{ alumno: "a01", nota: 8 }, { alumno: "a02", nota: 6 }, { alumno: "a03", nota: 9 }] },
  { _id: "RED", nombre: "Redes", docenteId: "d2", inscripciones: [{ alumno: "a02", nota: 7 }] },
  { _id: "SO", nombre: "Sistemas operativos", docenteId: "d1", inscripciones: [] }
]);
show(db.cursos.aggregate([
  { $lookup: { from: "docentes", localField: "docenteId", foreignField: "_id", as: "docente" } },
  { $unwind: "$docente" },
  { $project: { _id: 1, docente: "$docente.nombre", inscriptos: { $size: "$inscripciones" }, promedio: { $avg: "$inscripciones.nota" } } },
  { $sort: { _id: 1 } }
]));
print("--");
db.docentes.updateOne({ _id: "d1" }, { $set: { nombre: "Marta Ríos Vega" } });
show(db.cursos.aggregate([
  { $lookup: { from: "docentes", localField: "docenteId", foreignField: "_id", as: "docente" } },
  { $unwind: "$docente" },
  { $match: { docenteId: "d1" } },
  { $project: { _id: 1, docente: "$docente.nombre" } },
  { $sort: { _id: 1 } }
]));
