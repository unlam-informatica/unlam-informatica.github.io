// u4 · ejercicio U4.46: índice de texto y búsqueda de texto completo sobre tickets.
const show = (x) => { const a = (x && typeof x.toArray === "function") ? x.toArray() : (Array.isArray(x) ? x : [x]); a.forEach(d => print(EJSON.stringify(d, { relaxed: true }))); };
db.tickets.insertMany([
  { _id: 1, asunto: "Factura duplicada", detalle: "Me llegó dos veces la factura de marzo." },
  { _id: 2, asunto: "No puedo ingresar", detalle: "La clave no funciona desde ayer." },
  { _id: 3, asunto: "Facturación incorrecta", detalle: "El importe de la factura no coincide con el plan." },
  { _id: 4, asunto: "Baja del servicio", detalle: "Quiero dar de baja el servicio por mudanza." },
  { _id: 5, asunto: "Consulta de plan", detalle: "¿Cuál es el costo del plan básico?" }
]);
db.tickets.createIndex({ asunto: "text", detalle: "text" }, { default_language: "spanish", name: "IX_tickets_texto" });
show(db.tickets.find({ $text: { $search: "factura" } }, { _id: 1 }).sort({ _id: 1 }));
print("--");
show(db.tickets.find({ $text: { $search: "factura -duplicada" } }, { _id: 1 }).sort({ _id: 1 }));
print("--");
show(db.tickets.find({ $text: { $search: "\"dar de baja\"" } }, { _id: 1 }).sort({ _id: 1 }));
print("--");
show(db.tickets.find({ $text: { $search: "plan" } }, { _id: 1 }).sort({ _id: 1 }));
