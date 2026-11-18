// u4 · teoría índices: estadísticas de colección e índices ($collStats, $indexStats, collection.stats).
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
const docs = [];
for (let i = 1; i <= 300; i++) docs.push({ _id: i, categoria: "cat" + (i % 5), precio: i });
db.catalogo.insertMany(docs);
db.catalogo.createIndex({ categoria: 1 });
db.catalogo.find({ categoria: "cat1" }).toArray();
db.catalogo.find({ categoria: "cat2" }).toArray();
db.catalogo.find({ precio: 7 }).toArray();

const cs = db.catalogo.aggregate([{ $collStats: { count: {} } }]).toArray()[0];
print("documentos: " + cs.count);

const st = db.catalogo.aggregate([{ $indexStats: {} }, { $project: { _id: 0, name: 1, usos: "$accesses.ops" } }, { $sort: { name: 1 } }]).toArray();
st.forEach(x => print(x.name + ": usos=" + x.usos));

const s = db.catalogo.stats();
print("stats().count=" + s.count + ", nindexes=" + s.nindexes);
print("tiene totalIndexSize: " + (typeof s.totalIndexSize === "number"));
