---
title: POO y bases de datos
slug: bbdd-aplicadas/unidad-4/teoria/poo-y-bases
sidebar:
  order: 6.5
---

[← Unidad 4](/bbdd-aplicadas/unidad-4/teoria/)

El programa 2024 incluye en la unidad el tema «Relación con POO». La cátedra no desarrolla material propio sobre él, así que esta página se apoya en la documentación oficial de los productos y en la bibliografía. Se limita a tres cosas: la **correspondencia objeto-relacional** (el desajuste de impedancia), la **correspondencia objeto-documental** (documentos embebidos y referencias) y las capas de mapeo **ORM** y **ODM**. No trata patrones de diseño, frameworks en profundidad ni bases de datos orientadas a objetos.

Los ejemplos se comprobaron en SQL Server 2022 (`U4.T.POO.01`) y MongoDB 7.0 (`U4.T.POO.02`). El código de aplicación es una plantilla de sintaxis: no se ejecuta en el portal.

## Para qué sirve

Una aplicación orientada a objetos modela un pedido como un objeto `Pedido` que tiene un `Cliente` y una lista de `LineaPedido`. Al persistirlo hay que decidir cómo se guarda esa estructura de objetos conectados en una base de datos, y cómo se la vuelve a armar al leer. Con tablas, el pedido se reparte en varias filas unidas por claves; con documentos, puede guardarse casi tal como es en memoria. Las diferencias entre ambos mundos tienen un nombre.

## El desajuste de impedancia

:::note[Definición]
El **desajuste de impedancia objeto-relacional** (*object-relational impedance mismatch*) es el conjunto de diferencias conceptuales entre el modelo de objetos de un lenguaje de programación y el modelo relacional de una base de datos, que obligan a traducir en ambos sentidos.
:::

| Aspecto | En el modelo de objetos | En el modelo relacional |
|---|---|---|
| **Identidad** | Cada objeto tiene una identidad propia (dos objetos con los mismos datos son distintos); se compara por referencia o por igualdad definida en la clase | La identidad es el valor de la clave primaria; dos filas con los mismos valores de clave son la misma fila |
| **Herencia** | Una clase hereda atributos y comportamiento de otra; se pueden tratar objetos de las subclases como la superclase (polimorfismo) | No existe: hay que representar la jerarquía con tablas y claves |
| **Asociaciones y colecciones** | Un objeto contiene referencias a otros o colecciones de ellos (`pedido.lineas`) | Las asociaciones se expresan con claves foráneas; una colección es una tabla hija; una relación N:M necesita una tabla intermedia |
| **Navegación** | Se recorre el grafo de objetos siguiendo referencias (`pedido.cliente.nombre`) | Se combinan tablas con `JOIN`; se piensa en conjuntos, no en recorridos |
| **Granularidad y tipos** | Objetos de grano fino (una `Direccion`, un `Dinero`) y tipos propios | Tipos escalares y filas planas; un objeto de grano fino suele aplanarse en columnas o pasar a otra tabla |
| **Estado e integridad** | El encapsulamiento protege el estado; las reglas viven en el código | Las restricciones (`CHECK`, `FOREIGN KEY`) viven en la base y valen para todas las aplicaciones |

La **navegación contra los `JOIN`** merece atención: el código escrito como `pedido.getCliente().getNombre()` parece gratis, pero si cada acceso dispara una consulta (carga perezosa), recorrer una lista de pedidos genera una consulta por cada elemento: el llamado problema de las *N+1 consultas*. En SQL se resuelve con un `JOIN`; en un mapeador, pidiendo la carga anticipada de la asociación.

## Un ejemplo común: el pedido

Las clases de la aplicación (plantilla de sintaxis, en Java):

<!-- sintaxis -->
```java
class Cliente {
    Long id;
    String nombre;
    String localidad;
}

class LineaPedido {
    String producto;
    int cantidad;
    BigDecimal precioUnitario;
}

class Pedido {
    Long id;
    LocalDate fecha;
    Cliente cliente;            // asociación a un objeto
    List<LineaPedido> lineas;   // colección de objetos
}
```

## Correspondencia objeto-relacional

El pedido se reparte en tres tablas: cada clase pasa a ser una tabla, la asociación `Pedido`–`Cliente` es una clave foránea, y la colección `lineas` es una tabla hija con clave compuesta.

<!-- check: U4.T.POO.01 -->
```sql
CREATE SCHEMA tienda;
GO

CREATE TABLE tienda.Cliente (
    ClienteId INT         NOT NULL,
    Nombre    VARCHAR(60) NOT NULL,
    Localidad VARCHAR(40) NOT NULL,
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId)
);

CREATE TABLE tienda.Pedido (
    PedidoId  INT  NOT NULL,
    Fecha     DATE NOT NULL,
    ClienteId INT  NOT NULL,
    CONSTRAINT PK_Pedido         PRIMARY KEY CLUSTERED (PedidoId),
    CONSTRAINT FK_Pedido_Cliente FOREIGN KEY (ClienteId) REFERENCES tienda.Cliente (ClienteId)
);

CREATE TABLE tienda.LineaPedido (
    PedidoId       INT           NOT NULL,
    Numero         INT           NOT NULL,
    Producto       VARCHAR(40)   NOT NULL,
    Cantidad       INT           NOT NULL,
    PrecioUnitario DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_LineaPedido        PRIMARY KEY CLUSTERED (PedidoId, Numero),
    CONSTRAINT FK_LineaPedido_Pedido FOREIGN KEY (PedidoId) REFERENCES tienda.Pedido (PedidoId)
);
GO

INSERT INTO tienda.Cliente (ClienteId, Nombre, Localidad) VALUES
    (1, 'Ana', 'Ramos Mejía'),
    (2, 'Bruno', 'Morón');
INSERT INTO tienda.Pedido (PedidoId, Fecha, ClienteId) VALUES
    (101, '2026-03-05', 1),
    (102, '2026-03-18', 2);
INSERT INTO tienda.LineaPedido (PedidoId, Numero, Producto, Cantidad, PrecioUnitario) VALUES
    (101, 1, 'Teclado', 2, 45.00),
    (101, 2, 'Mouse',   1, 20.00),
    (102, 1, 'Monitor', 1, 300.00);
GO

SELECT p.PedidoId, p.Fecha, c.Nombre AS Cliente, l.Numero, l.Producto, l.Cantidad, l.PrecioUnitario
FROM tienda.Pedido AS p
INNER JOIN tienda.Cliente AS c ON c.ClienteId = p.ClienteId
INNER JOIN tienda.LineaPedido AS l ON l.PedidoId = p.PedidoId
WHERE p.PedidoId = 101
ORDER BY l.Numero;
```

**Resultado esperado.**

| PedidoId | Fecha | Cliente | Numero | Producto | Cantidad | PrecioUnitario |
|---:|---|---|---:|---|---:|---:|
| 101 | 2026-03-05 | Ana | 1 | Teclado | 2 | 45.00 |
| 101 | 2026-03-05 | Ana | 2 | Mouse | 1 | 20.00 |

Para reconstruir **un** objeto `Pedido` hacen falta dos `JOIN` y el resultado llega aplanado (una fila por línea, con los datos del pedido repetidos): el código de aplicación debe agruparlo de nuevo en un objeto con su lista.

### La herencia

Si `Pago` es una clase base con las subclases `PagoTarjeta` (cuotas, últimos cuatro dígitos) y `PagoTransferencia` (alias de destino), el modelo relacional ofrece tres estrategias:

| Estrategia | Cómo queda | Ventaja | Costo |
|---|---|---|---|
| **Tabla única** para toda la jerarquía | Una tabla `Pago` con las columnas de todas las subclases y una columna discriminadora; las no aplicables quedan en `NULL` | Consultas sin `JOIN` | Muchas columnas `NULL`; las restricciones `NOT NULL` por subclase no se pueden declarar |
| **Una tabla por subclase** | Tabla `Pago` con lo común y una tabla por subclase con su clave igual a la de `Pago` | Esquema normalizado y restricciones exactas | `JOIN` para leer un pago completo |
| **Una tabla por clase concreta** | Cada subclase concreta tiene su tabla con todos sus atributos, comunes incluidos | Lectura de un tipo sin `JOIN` | Los atributos comunes se repiten; consultar "todos los pagos" exige una unión (`UNION ALL`) |

## Correspondencia objeto-documental

Un documento admite **subdocumentos y arrays**, de modo que un conjunto de objetos conectados puede guardarse como una sola unidad. En términos de diseño, ese conjunto que se lee y se modifica junto es un **agregado** de objetos: el pedido y sus líneas. Para cada asociación hay dos formas de representarla:

- **Embeber**: el objeto relacionado va dentro del documento, como subdocumento o array.
- **Referenciar**: el documento guarda el `_id` del objeto relacionado, que vive en otra colección.

El mismo pedido: las líneas se embeben y el cliente se referencia.

<!-- check: U4.T.POO.02 -->
```javascript
db.clientes.insertMany([
  { _id: 1, nombre: "Ana", localidad: "Ramos Mejía" },
  { _id: 2, nombre: "Bruno", localidad: "Morón" }
]);

db.pedidos.insertMany([
  { _id: 101, fecha: ISODate("2026-03-05T00:00:00Z"), clienteId: 1,
    lineas: [
      { producto: "Teclado", cantidad: 2, precioUnitario: 45 },
      { producto: "Mouse", cantidad: 1, precioUnitario: 20 }
    ] },
  { _id: 102, fecha: ISODate("2026-03-18T00:00:00Z"), clienteId: 2,
    lineas: [{ producto: "Monitor", cantidad: 1, precioUnitario: 300 }] }
]);

// Una lectura devuelve el pedido con sus líneas
db.pedidos.find({ _id: 101 });

// El cliente va por referencia: hace falta una segunda lectura o un $lookup
db.pedidos.aggregate([
  { $match: { _id: 101 } },
  { $lookup: { from: "clientes", localField: "clienteId", foreignField: "_id", as: "cliente" } },
  { $unwind: "$cliente" },
  { $project: { _id: 1, cliente: "$cliente.nombre", cantidadLineas: { $size: "$lineas" } } }
]);

// Cambiar el precio de una línea embebida es una sola actualización
db.pedidos.updateOne({ _id: 101, "lineas.producto": "Mouse" }, { $set: { "lineas.$.precioUnitario": 25 } });
db.pedidos.find({ _id: 101 }, { _id: 0, lineas: 1 });
```

**Resultado esperado.**

1. La primera lectura devuelve el documento 101 completo, con las dos líneas dentro y `clienteId: 1`.
2. El `$lookup` devuelve `{ _id: 101, cliente: "Ana", cantidadLineas: 2 }`.
3. Después de la actualización, la línea del mouse tiene `precioUnitario: 25` y la del teclado queda igual (`modifiedCount` es 1).

### ¿Embeber o referenciar?

| Conviene **embeber** cuando… | Conviene **referenciar** cuando… |
|---|---|
| El objeto relacionado se lee casi siempre junto con el principal | El objeto relacionado se consulta o actualiza por su cuenta |
| Pertenece a un único propietario (una línea solo existe dentro de su pedido) | Lo comparten muchos documentos (un cliente con muchos pedidos) |
| Su cantidad es acotada | Su cantidad crece sin límite |
| Se quiere actualizar todo con una sola operación sobre un documento | Hay que mantener un dato en un solo lugar, para que un cambio no obligue a modificar muchos documentos |

El tamaño máximo de un documento BSON es de 16 MiB: un array que crece sin control termina en un límite duro. Una referencia, en cambio, obliga a una consulta adicional o a un `$lookup`, y la base **no verifica** que el `_id` referenciado exista (no hay claves foráneas). En un diseño documental, la forma de los documentos sale de las **consultas** de la aplicación, no de las entidades.

### La herencia en documentos

Un documento puede tener campos distintos de otro de la misma colección, así que una jerarquía de clases se guarda en **una sola colección** con un campo discriminador (por ejemplo `tipo`). Cada subclase aporta sus campos propios; no hay columnas `NULL` que rellenar. El ejercicio 49 lo desarrolla.

## ORM y ODM: capas de mapeo

Escribir a mano la traducción entre objetos y filas (o documentos) es repetitivo y propenso a errores. Las capas de mapeo la automatizan:

- **ORM** (*Object-Relational Mapping*): mapea clases a tablas y objetos a filas. Genera el SQL y arma de nuevo los objetos al leer. Ejemplos: Hibernate/JPA (Java), Entity Framework (.NET; funciona con SQL Server), SQLAlchemy (Python).
- **ODM** (*Object-Document Mapping*): mapea clases a documentos de una colección. Ejemplos: Mongoose (Node.js), Spring Data MongoDB (Java), MongoEngine (Python).

| Qué hacen | Qué no hacen por sí solas |
|---|---|
| Declarar la correspondencia entre clases y tablas o colecciones | Decidir el diseño: embeber o referenciar, o cómo representar la herencia, lo decide quien modela |
| Generar las operaciones de lectura y escritura | Garantizar buen rendimiento: la carga perezosa puede producir el problema de las N+1 consultas |
| Seguir los cambios de los objetos para guardarlos | Dar integridad referencial en MongoDB: una referencia sigue sin verificarse |
| Validar o convertir tipos según el esquema declarado en la aplicación | Reemplazar a las restricciones de la base, que valen para todas las aplicaciones |

Una capa de mapeo es una **comodidad**, no una excusa para no entender qué consultas ejecuta: conviene mirar el SQL o las operaciones que genera.

## Errores frecuentes

:::caution[Errores frecuentes]
- Embeber una colección que crece sin límite (por ejemplo, todos los comentarios históricos de una publicación) y chocar con el límite de 16 MiB.
- Referenciar todo por costumbre relacional y terminar leyendo cada documento con un `$lookup` o con consultas adicionales.
- Duplicar un dato en varios documentos (el nombre de un cliente dentro de cada pedido) sin prever cómo se mantiene al cambiar.
- Creer que el ODM da integridad referencial: elimina un cliente y sus pedidos siguen apuntando a un `_id` que ya no existe.
- Mapear una jerarquía en una tabla única y dejar de poder declarar `NOT NULL` en los campos propios de cada subclase.
- Asumir que "sin esquema" significa "sin diseño": el esquema pasa a vivir en la aplicación.
:::

## Ejercicios

### Ejercicio 45 · Embeber o referenciar
<!-- ejercicio: U4.45 | nivel: intermedio | tipo: diseno | verificacion: motor -->

:::note[Enunciado]
Una facultad guarda cursos. Cada curso tiene un docente (que dicta varios cursos) y una lista de inscripciones (alumno y nota) de a lo sumo cuarenta alumnos, que siempre se muestran junto con el curso. (a) Decidí qué se embebe y qué se referencia, y justificalo. (b) Implementalo en MongoDB con tres cursos y dos docentes y mostrá por curso: el nombre del docente, la cantidad de inscriptos y el promedio de notas. (c) Cambiá el nombre de un docente y comprobá cuántos cursos reflejan el cambio sin tocarlos.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** Las inscripciones pertenecen a un solo curso, son pocas y se leen siempre con él: se **embeben**. El docente lo comparten varios cursos y puede cambiar su nombre: se **referencia**, así el dato vive en un solo lugar.

<!-- check: U4.45 -->
```javascript
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

db.cursos.aggregate([
  { $lookup: { from: "docentes", localField: "docenteId", foreignField: "_id", as: "docente" } },
  { $unwind: "$docente" },
  { $project: { _id: 1, docente: "$docente.nombre", inscriptos: { $size: "$inscripciones" }, promedio: { $avg: "$inscripciones.nota" } } },
  { $sort: { _id: 1 } }
]);

db.docentes.updateOne({ _id: "d1" }, { $set: { nombre: "Marta Ríos Vega" } });

db.cursos.aggregate([
  { $lookup: { from: "docentes", localField: "docenteId", foreignField: "_id", as: "docente" } },
  { $unwind: "$docente" },
  { $match: { docenteId: "d1" } },
  { $project: { _id: 1, docente: "$docente.nombre" } },
  { $sort: { _id: 1 } }
]);
```

**Resultado esperado.** Primera consulta:

| _id | docente | inscriptos | promedio |
|---|---|---:|---:|
| BD1 | Marta Ríos | 3 | 7.666666666666667 |
| RED | Hugo Paz | 1 | 7 |
| SO | Marta Ríos | 0 | null |

Segunda consulta (tras cambiar el nombre):

| _id | docente |
|---|---|
| BD1 | Marta Ríos Vega |
| SO | Marta Ríos Vega |

Un solo `updateOne` sobre `docentes` se refleja en los dos cursos del docente. Si el nombre estuviera embebido, habría que actualizar cada curso. El promedio de un array vacío es `null`, no 0: conviene tenerlo en cuenta al mostrarlo.

</details>

### Ejercicio 49 · Una jerarquía de clases en una colección
<!-- ejercicio: U4.49 | nivel: avanzado | tipo: diseno | verificacion: motor -->

:::note[Enunciado]
La clase abstracta `Pago` (con `monto`) tiene dos subclases: `PagoTarjeta` (`cuotas`, `ultimos4`) y `PagoTransferencia` (`aliasDestino`). (a) Elegí una de las tres estrategias relacionales y señalá qué se pierde con ella. (b) Guardá cuatro pagos (dos de cada tipo) en una única colección de MongoDB con un campo discriminador. (c) Calculá el total y la cantidad por tipo, buscá los pagos en más de una cuota y listá los que no son de tarjeta sin usar el discriminador.
:::

<details>
<summary>Resolución</summary>

**Estrategia.** (a) Con tabla única, la consulta sobre todos los pagos es simple, pero `cuotas` y `aliasDestino` quedan en `NULL` según el tipo y no se puede exigir `NOT NULL` a los campos de cada subclase; con tabla por subclase se conserva la integridad a costa de un `JOIN`. En (b) y (c) el documento absorbe la diferencia: cada pago tiene solo sus campos.

<!-- check: U4.49 -->
```javascript
db.pagos.insertMany([
  { _id: 1, tipo: "tarjeta", monto: 1200, cuotas: 3, ultimos4: "4242" },
  { _id: 2, tipo: "transferencia", monto: 800, aliasDestino: "tienda.demo" },
  { _id: 3, tipo: "tarjeta", monto: 300, cuotas: 1, ultimos4: "1111" },
  { _id: 4, tipo: "transferencia", monto: 500, aliasDestino: "tienda.demo" }
]);

db.pagos.aggregate([
  { $group: { _id: "$tipo", total: { $sum: "$monto" }, cantidad: { $sum: 1 } } },
  { $sort: { _id: 1 } }
]);

db.pagos.find({ cuotas: { $gt: 1 } }, { _id: 1, tipo: 1, cuotas: 1 });

db.pagos.find({ cuotas: { $exists: false } }, { _id: 1 }).sort({ _id: 1 });
```

**Resultado esperado.**

| _id (tipo) | total | cantidad |
|---|---:|---:|
| tarjeta | 1500 | 2 |
| transferencia | 1300 | 2 |

La búsqueda de más de una cuota devuelve solo `{ _id: 1, tipo: "tarjeta", cuotas: 3 }`, y los pagos sin `cuotas` son los `_id` 2 y 4.

Los documentos de las dos subclases conviven en la misma colección y se consultan juntos (polimorfismo). A cambio, nada impide que se inserte un pago de tarjeta sin `cuotas`: esa regla pasa a la aplicación, o a un validador `$jsonSchema` (ver [MongoDB — Introducción](/bbdd-aplicadas/unidad-4/teoria/mongodb-introduccion/)). Que un campo no exista (`$exists: false`) no es lo mismo que valga `null`.

</details>

## Autoevaluación

<details>
<summary>1. ¿Qué es el desajuste de impedancia y cuáles son sus cuatro manifestaciones principales?</summary>

Es la diferencia entre el modelo de objetos y el relacional que obliga a traducir entre ambos. Se manifiesta en la identidad (referencia contra clave primaria), la herencia (no existe en tablas), las asociaciones y colecciones (claves foráneas y tablas hijas) y la navegación (recorrer referencias contra combinar tablas con `JOIN`).

</details>

<details>
<summary>2. ¿Por qué un documento reduce el desajuste, y qué problema nuevo plantea?</summary>

Porque un agregado de objetos (pedido y líneas) se guarda como una unidad, con una estructura parecida a la del objeto. El problema nuevo es diseñar qué se embebe y qué se referencia: un array sin cota choca con el límite de 16 MiB y una referencia no tiene integridad verificada por la base.

</details>

<details>
<summary>3. ¿Qué diferencia hay entre un ORM y un ODM?</summary>

El ORM traduce entre objetos y tablas de una base relacional (generando SQL); el ODM, entre objetos y documentos de una base documental. Ambos son capas de mapeo que no reemplazan el diseño de datos.

</details>

<details>
<summary>4. Un `Cliente` tiene miles de `Pedido`. ¿Se embeben los pedidos dentro del cliente?</summary>

No: la cantidad crece sin límite, los pedidos se consultan por su cuenta y el documento del cliente crecería hasta el tope de tamaño. Se referencia al cliente desde cada pedido.

</details>

:::tip[En resumen]
- El **desajuste de impedancia** reúne las diferencias entre objetos y tablas: identidad, herencia, asociaciones y colecciones, y navegación.
- En el modelo relacional, cada clase es una tabla, las asociaciones son claves foráneas y reconstruir un objeto exige `JOIN`. La herencia tiene tres estrategias con costos distintos.
- En el modelo documental, un agregado de objetos puede guardarse como un documento: se **embebe** lo que se lee junto y es acotado, y se **referencia** lo compartido o ilimitado.
- ORM y ODM automatizan la traducción, pero el diseño y el rendimiento siguen siendo responsabilidad de quien modela.
:::

## Fuentes

- Programa analítico 2024 de la asignatura (Unidad 4: «Relación con POO»). No hay presentación de cátedra sobre el tema.
- Ireland, C., Bowers, D., Newton, M. y Waugh, K. (2009), "A Classification of Object-Relational Impedance Mismatch", *First International Conference on Advances in Databases, Knowledge, and Data Applications*.
- MongoDB Manual 7.0: *Data Modeling*, *Embedded Data Models*, *Model Relationships Between Documents* y *Schema Validation*: https://www.mongodb.com/docs/manual/.
- Microsoft Learn, *Entity Framework Core* (visión general): https://learn.microsoft.com/ef/core/. Hibernate ORM, *User Guide*: https://hibernate.org/orm/documentation/. Mongoose, *Documentation*: https://mongoosejs.com/docs/.
