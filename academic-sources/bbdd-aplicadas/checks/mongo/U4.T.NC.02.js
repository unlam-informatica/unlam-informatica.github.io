// u4 · conceptos NoSQL: el mismo usuario con dos direcciones como un documento.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.usuarios.insertOne({
  _id: 1,
  nombre: "Lucía",
  direcciones: [
    { ciudad: "Morón", pais: "Argentina" },
    { ciudad: "Montevideo", pais: "Uruguay" }
  ]
});
show(db.usuarios.find({ _id: 1 }));
show(db.usuarios.find({ "direcciones.pais": "Uruguay" }, { _id: 1, nombre: 1 }));
