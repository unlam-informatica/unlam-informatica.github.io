// u4 · conceptos NoSQL: modelo de texto, índice de texto y búsqueda de texto completo.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.articulos.insertMany([
  { _id: 1, titulo: "Replicación en MongoDB", cuerpo: "Un conjunto de réplicas mantiene copias de los datos en varios nodos." },
  { _id: 2, titulo: "Índices compuestos", cuerpo: "El orden de los campos del índice cambia las consultas que puede resolver." },
  { _id: 3, titulo: "Consistencia eventual", cuerpo: "Las réplicas convergen cuando cesan las escrituras." },
  { _id: 4, titulo: "Grafos y recomendaciones", cuerpo: "Las relaciones entre personas se recorren sin joins." }
]);
db.articulos.createIndex({ titulo: "text", cuerpo: "text" }, { default_language: "spanish", name: "IX_articulos_texto" });
show(db.articulos.find({ $text: { $search: "replica" } }, { _id: 1 }).sort({ _id: 1 }));
print("--");
show(db.articulos.find({ $text: { $search: "índice recorren" } }, { _id: 1 }).sort({ _id: 1 }));
print("--");
show(db.articulos.find({ $text: { $search: "réplicas -eventual" } }, { _id: 1 }).sort({ _id: 1 }));
