# Guía de producción — Bases de Datos Aplicada (3641)

Contrato común para redactar, revisar e integrar las páginas de `src/content/docs/bbdd-aplicadas/`.
Toda página nueva o reescrita lo cumple. El contrato de trabajo es `reports/content-audit.md`, y las
etapas están en `implementation-plan.md`.

## 0. Decisiones registradas (2026-11-17)

| # | Decisión | Dónde se aplica |
|---|---|---|
| D1 | El programa 2024 (3641) es la referencia principal provisional y el de 2023 es un antecedente. No se supone ni se inventa una actualización 2025/2026 | §1; `curriculum-map.yaml` → `program` |
| D2 | No se incorporan reproducciones nuevas de enunciados de cátedra sin autorización. Los ya publicados se auditan y, cuando corresponda, se proponen reemplazos originales | §6 |
| D3 | La Unidad 6 se sustenta en fuentes primarias oficiales: InfoLEG (legislación argentina), EUR-Lex (RGPD) e información pública de ISO/IEC 25012. No se reproduce material protegido ni se atribuyen contenidos no verificados | §1.1 |
| D4 | POO se limita a la correspondencia objeto-relacional y objeto-documental, ORM y ODM. KDD se desarrolla con las cinco etapas del proceso clásico de Fayyad et al. (1996) | §1.2 |
| D5 | Los contenidos fuera de su unidad se reubican. Los complementarios útiles se conservan, diferenciados del programa obligatorio. No se elimina contenido académico correcto sin justificarlo | §2 |
| D6 | Las pruebas son reproducibles con SQL Server 2022 y MongoDB 7. Se registran por separado los ejemplos ejecutados, los revisados sin ejecución y los pendientes | §7 |
| D7 | QA distingue los operadores de MongoDB de las fórmulas. Los ejemplos SQL propios usan tablas en singular y PascalCase. Hay mínimos de ejercicios por unidad, las resoluciones son completas y no se agregan ejercicios de relleno | §4, §5, §8 |
| D8 | La retirada de los PDF públicos es una corrección de seguridad independiente y no se despliega sin autorización. Queda registrado que la titular de la credencial expuesta debe rotarla | `implementation-plan.md` (pista de seguridad) |

## 1. Alcance y fuentes

- **Referencia curricular provisional: programa analítico 2024** (`bbdd-aplicadas-3d9721081e14`,
  firmado el 07/08/2024). El programa público del DIIT de **2023** es una referencia histórica: no se
  mezclan sus esquemas de evaluación ni su ubicación de temas con la de 2024. La matriz
  `curriculum-map.yaml` registra cada diferencia.
- **No hay una versión posterior verificada.** No se escribe "programa 2025/2026" ni se supone un
  cambio de evaluación: el portal muestra el esquema 2024 (un parcial sobre u1–u4, TP integrador y
  final). Si aparece un programa nuevo, se incorpora como documento fuente y se actualiza la matriz.
- **Jerarquía de fuentes**:
  1. Cátedra (`programa`, `cronograma`, `teoria-catedra`, `guia-practica`).
  2. Documentación oficial de los productos (Microsoft Learn para SQL Server, manual de MongoDB) y
     normativa primaria (InfoLEG, EUR-Lex, ISO).
  3. Bibliografía del programa (Elmasri-Navathe; Silberschatz-Korth-Sudarshan; Gils Carbó).
  4. Material de alumnos (resúmenes, resoluciones, exámenes reconstruidos). Es una referencia
     **no verificada**: sirve para saber qué se evalúa y qué cuesta entender, nunca como fuente de un
     dato, una definición o una solución.
- **Unidad 6**: no hay material de cátedra. Ver §1.1.
- **Excluido**: `Instalación MongoDB.pdf` contiene una credencial de terceros. No se lee, no se cita
  y no se usa como fuente.
- Los derivados de `processed/` contienen datos personales de estudiantes. Solo se leen o se pasan a
  un modelo a través de un corpus anonimizado: sin nombres, DNI, correos ni datos de contacto.

### 1.1 Fuentes de la Unidad 6 (D3)

| Tema | Fuente primaria | Uso permitido |
|---|---|---|
| Ley 25.326 | Texto actualizado en InfoLEG (Ley 25.326 y su Decreto Reglamentario 1558/2001) | Citar artículos con número y parafrasear. Las citas textuales deben ser breves y llevar referencia |
| RGPD (GDPR) | Reglamento (UE) 2016/679 en EUR-Lex, versión en español | Ídem. Citar artículo y considerando |
| ISO/IEC 25012 | Solo información pública: la página oficial de la norma en iso.org y su resumen público | No se reproduce el texto de la norma, que es paga. Las 15 características y su clasificación se presentan con definiciones propias y la cita de la fuente pública consultada |

- Cada afirmación normativa (artículo, plazo, monto, característica) lleva su cita. Si no se pudo
  verificar contra la fuente primaria, no se publica.
- No se atribuyen frases a personas ni instituciones sin fuente verificable. Por ejemplo, la cita
  atribuida a Henry Ford que hoy aparece en u6 se elimina si no se encuentra su origen.
- Los apuntes de alumnos sobre u6 sirven solo para saber qué se evalúa.

### 1.2 Alcance de temas sin desarrollo de cátedra (D4)

- **Relación con POO (`u4-poo`)**: correspondencia objeto-relacional (desajuste de impedancia),
  correspondencia objeto-documental (documentos embebidos y referencias frente a agregados de
  objetos), ORM y ODM como capas de mapeo, con un ejemplo comparativo breve. No se desarrollan
  patrones de diseño, frameworks concretos en profundidad ni bases orientadas a objetos.
- **KDD (`u4-kdd`)**: las cinco etapas de Fayyad, Piatetsky-Shapiro y Smyth (1996): selección,
  preprocesamiento, transformación, minería de datos e interpretación/evaluación. La minería de
  datos se presenta como una etapa del proceso. Las variantes de 7 etapas no se usan.

## 2. Rutas, slugs y navegación

- **Se conservan las URL actuales.** Cada `.md` tiene un `slug` explícito, y el slug no se cambia
  aunque cambie el nombre del archivo.
- Si una página se mueve, se fusiona o se elimina:
  - se mantiene la ruta anterior (redirección) y se actualiza la matriz de `migration/`, según `migration/README.md`;
  - `npm run validate` tiene que pasar.
- Cada unidad mantiene `teoria/` y `practica/`, con un `index.md` que presenta la unidad.
  El `index.md` de `teoria/` es la **presentación y ruta** de la unidad (objetivos, antes de comenzar,
  ruta de aprendizaje con «Leé / Practicá / Comprobá» por etapa, ejercicios y laboratorios,
  autoevaluación y repaso, continuar) y el de `practica/` es el índice de prácticas con lo que cada una
  requiere. El `sidebar.order` de lecciones y prácticas sigue el orden de la ruta. Una lección nueva se
  agrega también a la ruta de su unidad (`tests/sidebar.spec.ts` lo comprueba). La guía general está en
  `como-estudiar.md`.
- Una página trata un tema del programa. Las páginas integradoras ("apunte completo") resumen
  temas y enlazan a ellos; no duplican su desarrollo.
- **Reubicación (D5).** El contenido fuera de su unidad se traslada a la página de la unidad que
  corresponde según el programa 2024. En el lugar de origen queda, como mucho, un párrafo puente con
  el enlace. Si una página entera cambia de unidad, se conserva su URL (redirección y `migration/`).
- **Contenido complementario (D5).** Lo correcto y útil que no está en el programa 2024 se conserva y
  se rotula así:
  - en el frontmatter, `sidebar: { badge: { text: Complementario, variant: note } }`;
  - al comienzo de la página o de la sección, `:::note[Contenido complementario]` con una línea que
    diga que no forma parte del programa 2024.

  Las guías de parcial no lo incluyen.
- **No se elimina** contenido académico correcto sin justificarlo en el registro de la etapa
  (`implementation-plan.md`). Lo incorrecto se corrige; lo redundante se fusiona.

## 3. Frontmatter

```yaml
---
title: Window functions
slug: bbdd-aplicadas/unidad-1/teoria/window-functions
sidebar:
  order: 30
---
```

Los títulos van en español, sin el nombre de la unidad y sin marcas de parcial ("2do parcial").

## 4. Convenciones de T-SQL (SQL Server)

Valen para todo ejemplo **propio**. Los ejercicios de cátedra reproducidos siguen la sección 6.

| Elemento | Convención | Ejemplo |
|---|---|---|
| Tablas | Singular y PascalCase | `Cliente`, `DetalleFactura` |
| Columnas | PascalCase | `ClienteId`, `FechaAlta`, `ImporteTotal` |
| Variables y parámetros | `@` + PascalCase | `@FechaDesde`, `@ClienteId` |
| Procedimientos, funciones, vistas y triggers | PascalCase, con verbo para los procedimientos | `RegistrarVenta`, `ObtenerSaldo`, `VentaMensual`, `TrgFacturaAuditoria` |
| Restricciones | Prefijo + tabla (+ columna o referencia) | `PK_Cliente`, `FK_Factura_Cliente`, `CK_Producto_Precio`, `UQ_Cliente_Email`, `DF_Factura_Fecha` |
| Índices | `IX_` (no clúster), `CIX_` (clúster) + tabla + columnas | `IX_Factura_ClienteId_Fecha` |
| Palabras reservadas, funciones del sistema y tipos de datos | MAYÚSCULAS | `SELECT`, `ROW_NUMBER()`, `OVER`, `VARCHAR(50)` |

Además:

- **Identificadores.** Van en español, sin espacios, tildes ni `ñ`, sin corchetes salvo que sean
  imprescindibles y sin abreviaturas crípticas.
- **Prefijo `sp_`.** No se usa en procedimientos propios: SQL Server lo reserva para los
  procedimientos del sistema.
- **Esquema.** Siempre explícito (`ventas.Cliente`), nunca `dbo` implícito. Los esquemas propios
  van en minúsculas y con un nombre de dominio (`ventas`, `rrhh`, `seguridad`). La cátedra usa
  `ddbba`, que se conserva en sus ejercicios.
- **Formato de las sentencias.**
  - Cada sentencia termina en `;` y la que precede a un `WITH` también.
  - Se usa `GO` donde el lote lo exige (`CREATE PROCEDURE`, `CREATE VIEW`, `CREATE TRIGGER`).
  - Una cláusula por línea, con sangría de 4 espacios; las columnas de `SELECT` van una por línea
    cuando son más de tres.
- **Versión objetivo.** SQL Server 2019 o 2022, como en las guías de cátedra. Si una
  característica requiere una versión posterior (por ejemplo `GREATEST`, `STRING_SPLIT` con ordinal
  o `GENERATE_SERIES`, de 2022), se indica en un `:::note`.

```sql
CREATE TABLE ventas.Cliente (
    ClienteId   INT IDENTITY(1, 1) NOT NULL,
    Nombre      VARCHAR(80)        NOT NULL,
    Email       VARCHAR(120)       NULL,
    FechaAlta   DATE               NOT NULL CONSTRAINT DF_Cliente_FechaAlta DEFAULT (CAST(GETDATE() AS DATE)),
    CONSTRAINT PK_Cliente PRIMARY KEY CLUSTERED (ClienteId),
    CONSTRAINT UQ_Cliente_Email UNIQUE (Email)
);
```

## 5. Convenciones de MongoDB (MQL)

- **Sintaxis.** Se usa `mongosh`, con MongoDB 7.0 o posterior. Si una característica depende de la
  versión, se indica.
- **Nombres.** Colecciones en minúsculas y en plural (`clientes`, `ventas`); campos en camelCase
  (`fechaAlta`, `importeTotal`). Es la convención habitual de MongoDB, y los ejercicios de cátedra
  conservan sus nombres.
- **Operadores (`$match`, `$group`, `$lookup`, `$set`).** Siempre van como código en línea, también
  en títulos y tablas. Un `$` suelto en la prosa lo interpreta KaTeX como fórmula; ya pasa en
  `mongodb-agregacion` y en la práctica de transacciones. `qa` informa el operador sin formato como
  `operador-mongodb-sin-codigo`, separado de los errores de fórmulas.
- **Montos en pesos.** En la prosa se escriben como `$ 500` dentro de código, o como "500 pesos", nunca `$500` suelto.
- **Cadenas de conexión.** Llevan marcadores (`mongodb+srv://<usuario>:<contraseña>@<cluster>/`),
  nunca credenciales reales ni nombres de clústeres existentes.

## 6. Ejercicios de cátedra reproducidos

- Se **preservan los identificadores originales**: esquema, tablas, columnas, colecciones, nombres
  de archivos de datos y numeración de consignas. Las convenciones de las secciones 4 y 5 no se
  aplican a ellos.
- **No se incorporan reproducciones nuevas de enunciados de cátedra sin autorización (D2).**
- **Enunciados ya publicados.** Hay reproducciones o adaptaciones de cátedra en:
  - `unidad-1/practica/tp1`;
  - `unidad-1/practica/window-functions`;
  - `unidad-2/practica/tp2`;
  - las prácticas de MongoDB de u4.

  Se auditan, cada uno con su veredicto en `implementation-plan.md`:
  - **conservar con atribución**: está corregido y completo;
  - **reemplazar por un original equivalente**: mismo objetivo de aprendizaje, nivel y tipo de
    consigna, con datos e identificadores propios.

  El reemplazo es la opción por defecto cuando hay que reescribir las soluciones. La página conserva su URL.
- Mientras un enunciado reproducido siga publicado, lleva atribución: "Fuente: guía de cátedra, TP N
  (versión o cuatrimestre)". No se copian presentaciones, figuras ni párrafos teóricos.
- La resolución es propia y completa, y cumple la sección 7. Si se corrige un error del enunciado
  original, se aclara en un `:::caution`.
- Los exámenes reconstruidos por alumnos no se presentan como enunciados oficiales. Pueden inspirar
  ejercicios propios ("estilo parcial") con datos e identificadores nuevos.

## 7. Ejemplos y soluciones propios

- **Originales.** No se reutilizan datos ni enunciados de fuentes privadas.
- **Completos.** Cada ejemplo ejecutable incluye, en este orden:
  1. el DDL (con `DROP TABLE IF EXISTS` o esquema propio para que sea repetible);
  2. los datos (`INSERT` explícitos, pocos y elegidos para ilustrar el caso límite);
  3. la consulta;
  4. el **resultado esperado** como tabla Markdown.
- **Verificables.** Los resultados no dependen del orden físico: siempre hay `ORDER BY` cuando se
  muestran filas. No hay fechas relativas sin fijar (`GETDATE()` solo en `DEFAULT`) ni
  aleatoriedad. Los planes de ejecución y los tiempos se describen cualitativamente o con la versión
  y el volumen de datos usados.
- **Datos sintéticos.** Nada de DNI, CUIT, correos o nombres de personas reales. Se usan valores
  evidentemente ficticios (`cliente01@ejemplo.test`).
- **Verificación en motor (D6).**
  - **Entorno.** SQL Server 2022 y MongoDB 7.0 en contenedores efímeros, sin puertos publicados y
    con imágenes fijadas por digest. Lo levanta y usa `content-pipeline verify-code`.
  - **Marcador.** Cada ejemplo o resolución ejecutable lleva `<!-- check: ID -->` antes de su
    bloque de código.
  - **Plantillas de sintaxis.** Un bloque que solo muestra la forma general (`SELECT ... FROM <tabla>`)
    va precedido de `<!-- sintaxis -->`. No es pendiente ni verificado. `verify-code` lo cuenta aparte y
    marca como sospechoso un bloque así que parezca una sentencia completa sin marcadores de posición.
  - **Script de comprobación.** Está en `academic-sources/bbdd-aplicadas/checks/sql/ID.sql` o
    `checks/mongo/ID.js`, con el mismo identificador.
  - **Salida esperada.** Va en `ID.expected` y es la salida exacta del último conjunto de resultados.
  - **Salida no determinista del motor.** Si un mensaje informativo no depende del contenido (por ejemplo, los de
    `ALTER DATABASE ... WITH ROLLBACK IMMEDIATE`), el script lo declara con `-- verify: ignorar-salida <regex>` y
    esas líneas se excluyen de la comparación. Nunca se usa para ocultar resultados.
  - **Equivalencia.** Un bloque ilustrativo (rutas de Windows, bases con nombre fijo) puede llevar el ID de una
    comprobación que ejecuta las **mismas sentencias** adaptadas a la base de prueba y a rutas del contenedor. Si
    ninguna comprobación las cubre, el bloque es pendiente de verificación específica, no se marca como verificado.
- **Tres registros separados** en `reports/code-verification.md`:
  - **ejecutados**: tienen un script de comprobación y su resultado (aprobado o fallido);
  - **pendientes de verificación específica**: están listados en `checks/reviewed.yaml` con el motivo
    (dos sesiones concurrentes, un clúster o alta disponibilidad, red externa, una edición
    Enterprise, permisos administrativos de servidor o creación de bases), quién los revisó y la
    fecha. Se revisaron sin ejecutar y **nunca cuentan como verificados**: un tema con ítems en esta
    categoría no pasa a `validation: verificado` en la matriz;
  - **pendientes**: todo bloque `sql` o `js`/`javascript` de las páginas que no está en los
    registros anteriores.
- Un ejemplo pendiente no bloquea la publicación de una página existente. Una página **reescrita**
  no puede tener ejemplos pendientes.
- **Código extraído de fuentes.** Nunca se publica tal como salió de la extracción. 277 bloques
  perdieron los saltos de línea y 184 provienen de OCR de capturas. Se reconstruye a mano contra el
  original y se ejecuta.

## 8. Estructura pedagógica

### Lección de teoría

Se usan las partes que el tema necesite, en este orden:

1. **Para qué sirve.** El problema concreto que resuelve, en un sistema real.
2. **Conceptos.** Definiciones en `:::note[Definición]` y comparación con lo ya conocido.
3. **Sintaxis.** La forma general, con la referencia a la documentación oficial de la versión.
4. **Ejemplo guiado.** Un caso completo según la sección 7.
5. **Variantes y casos límite.** `NULL`, empates, conjuntos vacíos, concurrencia.
6. **Rendimiento y buenas prácticas.** Cuando corresponda: índices, plan, bloqueos.
7. **Errores frecuentes.** En `:::caution[Errores frecuentes]`, con un contraejemplo ejecutable.
8. **Autoevaluación.** De 2 a 4 preguntas con la respuesta en `<details>`.
9. **En resumen.** `:::tip[En resumen]`.
10. **Fuentes.** Las de cátedra descriptas sin rutas privadas (por ejemplo, "Presentación de
    cátedra, Unidad 3, parte 1, v1.0, 2023"), la documentación oficial y la bibliografía.

Se escribe en español de Argentina, en primera persona del plural y con voseo cuando se interpela
al lector. Sin relleno.

### Práctica

1. Qué lecciones presupone, con enlaces.
2. El conjunto de datos, enlazado a `public/bbdd-aplicadas/unidad-N/practica/archivos/`, o un DDL
   completo.
3. Ejercicios ordenados por nivel.

Cada ejercicio usa el marcador que lee `qa`:

~~~markdown
### Ejercicio 7 · Ranking de vendedores por mes
<!-- ejercicio: U1.07 | nivel: intermedio | tipo: consulta | verificacion: razonamiento -->

:::note[Enunciado]
…
:::

<details>
<summary>Resolución</summary>

**Estrategia.** …

```sql
…
```

**Resultado esperado.**

| … |

</details>
~~~

- **Identificadores.** `U1.01`… por unidad, únicos en toda la materia.
- **`nivel`.** `inicial`, `intermedio` o `avanzado`.
- **`tipo`.** `consulta`, `ddl`, `programabilidad`, `diagnostico` (planes, bloqueos), `diseno`,
  `conceptual`, `verdadero-falso` o `mql`.
- **`verificacion`.**
  - `motor`: la resolución tiene código con `<!-- check: ID -->` y su comprobación aprobada en
    `reports/code-verification.json`.
  - `revisado`: el código está en `checks/reviewed.yaml` porque no se puede ejecutar en el entorno
    (requiere dos sesiones, un clúster, red o una edición Enterprise).
  - `razonamiento`: el ejercicio no tiene código.
  - `sympy` no se usa en esta materia.
- **Resolución completa (D7).** Tiene estrategia y desarrollo. Si tiene código, incluye además el
  bloque completo (sin cuerpos vacíos ni `…`) y el **resultado esperado**. En un V/F o un ejercicio
  conceptual, incluye la justificación. `qa` rechaza las resoluciones ausentes, los bloques de
  código vacíos y los ejercicios `motor` sin comprobación aprobada.
- **Mínimos por unidad (D7).** Solo cuentan los ejercicios con resolución completa. No se agregan
  ejercicios de relleno para alcanzarlos: si un tema no da para más, se registra en el plan.

  | Unidad | Mínimo de ejercicios | Por nivel (inicial, intermedio, avanzado) |
  |---|---:|---:|
  | u1 | 15 | ≥ 3 cada uno |
  | u2 | 12 | ≥ 3 cada uno |
  | u3 | 12 | ≥ 3 cada uno |
  | u4 | 15 | ≥ 3 cada uno |
  | u5 | 8 | ≥ 2 cada uno |
  | u6 | 6 | ≥ 2 cada uno |

### Guía de parcial

Sigue el esquema de evaluación **2024**: un parcial sobre u1–u4, más el TP integrador y el final.
No se rotula ninguna unidad como "2do parcial". Las guías de u5 y u6 se orientan al TP y al final.

## 9. Formato

- Callouts nativos con título en español: `:::note[…]`, `:::tip[…]`, `:::caution[…]`, `:::danger[…]`.
- Diagramas en cercos `mermaid`, en lugar de imágenes decorativas.
- No hace falta notación matemática. Si se usa, va `$...$` en línea y `$$` en líneas propias.

## 10. Privacidad y seguridad

- No se publican nombres, DNI, legajos, correos ni otros datos de estudiantes, tampoco en ejemplos.
- No se publican originales de cátedra (presentaciones o PDF) en `public/`. Los retirados están en
  `migration/withdrawn.json`.
- No se publican credenciales, cadenas de conexión reales ni nombres de clústeres.
- Los laboratorios de seguridad son defensivos: muestran la vulnerabilidad en un entorno local
  controlado y siempre la corrección. No incluyen cargas útiles contra sistemas de terceros.

## 11. Prohibido

- Inventar artículos de ley, multas, fechas, características ISO o comportamientos de un motor sin fuente.
- Publicar código extraído sin reconstruir y ejecutar.
- Presentar material de alumnos o exámenes reconstruidos como oficiales.
- Mezclar los esquemas de evaluación de 2023 y 2024.
- Cambiar una URL sin redirección y sin actualizar `migration/`.
