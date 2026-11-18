// u4 · práctica U4.07 (datos propios: archivos/ventas/).
const fs = require("fs");
const dir = "{{FIXTURES}}";
const cargar = (coleccion) => db[coleccion].insertMany(EJSON.parse(fs.readFileSync(dir + "/" + coleccion + ".json", "utf8")));
const mostrar = (cursor) => cursor.forEach(d => print(EJSON.stringify(d, { relaxed: true })));
cargar("ventas");
cargar("vendedores");
db.stock.insertMany([
  { sucursal: "Centro", codigo: "TAL-01", cantidad: 4 },
  { sucursal: "Centro", codigo: "MAR-02", cantidad: 10 },
  { sucursal: "Norte", codigo: "TAL-01", cantidad: 2 }
]);

const reponer = () => db.stock.updateOne(
  { sucursal: "Sur", codigo: "TAL-01" },
  { $set: { minimo: 3 }, $setOnInsert: { cantidad: 0 } },
  { upsert: true }
);
const a = reponer();
print("upsert 1: encontradas " + a.matchedCount + ", insertadas " + a.upsertedCount);
const b = reponer();
print("upsert 2: encontradas " + b.matchedCount + ", insertadas " + b.upsertedCount + ", modificadas " + b.modifiedCount);

const lote = db.stock.bulkWrite([
  { updateOne: { filter: { sucursal: "Centro", codigo: "TAL-01" }, update: { $inc: { cantidad: -1 } } } },
  { updateOne: { filter: { sucursal: "Norte", codigo: "MAR-02" }, update: { $set: { cantidad: 6 } }, upsert: true } },
  { insertOne: { document: { sucursal: "Sur", codigo: "CAN-08", cantidad: 9 } } },
  { deleteOne: { filter: { sucursal: "Norte", codigo: "TAL-01" } } }
], { ordered: true });
print("insertados " + lote.insertedCount + ", encontrados " + lote.matchedCount + ", modificados " + lote.modifiedCount +
      ", upsert " + lote.upsertedCount + ", borrados " + lote.deletedCount);

mostrar(db.stock.aggregate([
  { $sort: { sucursal: 1, codigo: 1 } },
  { $project: { _id: 0, sucursal: "$sucursal", codigo: "$codigo", cantidad: "$cantidad", minimo: "$minimo" } }
]));
