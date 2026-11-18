# Extracción, normalización y validación — Bases de Datos Aplicada (3641)

Fecha: 2026-11-17 · Docling 2.150.1 (OCR RapidOCR, español) · motor propio `plaintext` para `.txt`.

Este informe no reproduce texto de las fuentes ni nombres de estudiantes. Los derivados
(`processed/`) son privados y Git los ignora. Antecedente: `ingest-audit.md`.

## Resultado

| Concepto | Valor |
|---|---|
| Documentos catalogados | 54: 42 PDF, 5 DOCX y 7 TXT |
| Extraídos y normalizados | 51: 45 con Docling y 6 con `plaintext` |
| Omitidos (`skip`) | 3 |
| Fallidos | 0 |
| Páginas extraídas | 802, sin páginas perdidas (`paginas-perdidas`: 0) |
| Texto normalizado | ≈ 1,08 millones de caracteres en 1289 secciones |
| Tablas | 96 |
| Bloques de código | 392 |
| Validación | 0 errores y 119 advertencias, detalladas más abajo |
| Tiempo de extracción | ≈ 18 minutos (CPU/MPS) |

Los tres omitidos son:

- `Instalación MongoDB.pdf`, porque contiene una credencial de terceros.
- `Formularios/1. Formulario.pdf`, un duplicado sin responder de la Autoevaluación 1.
- `Apuntes/7. Apunte.txt`, que solo tiene un enlace a Notion. El enlace no se siguió.

Perfil aplicado: `extraction: {profile: text, picture_text: true}`. A tres documentos se les agregó
`force_ocr: true`: `Apuntes/4. Apunte.pdf`, `Formularios/2. Formulario.pdf` y `Formularios/3. Formulario.pdf`.

## Cambios en el pipeline

Todos tienen tests: `pytest -m "not integration"` da 81 aprobados. No cambian la salida de otras materias.

- **Texto plano (`.txt` → formato `plaintext`).** Se lee sin Docling. Detecta la codificación (BOM,
  UTF-8, cp1252 o latin-1, con advertencia), normaliza saltos de línea y Unicode y no sigue enlaces:
  solo los cuenta (`enlaces-externos-no-seguidos`).
- **`force_ocr`.** Es una opción de perfil que ignora una capa de texto inservible y reconoce cada página como imagen.
- **`picture_text`.** Es una opción de perfil que exporta el texto reconocido dentro de las figuras.
  Está desactivada por defecto.
- **Normalización y validación.** Detectan texto ilegible (`texto-ilegible`: U+FFFD o mojibake) y
  cuentan tablas, bloques de código y bloques "aplanados" (`codigo-sin-saltos`).
- **Catálogo.** El YAML ya no usa anclas (`&id001`). Las entradas no comparten objetos, así que
  corregir una a mano no altera las demás.

## Pruebas de extracción (fase B)

### `Apuntes/4. Apunte.pdf` (capa de texto rota)

| Prueba | U+FFFD | Caracteres acentuados correctos | Bloques de código |
|---|---|---|---|
| Docling con la capa de texto | 67 % de los caracteres, en 35 de 35 páginas | 16 | 26 (el código usa otra fuente y salió legible) |
| Docling con `force_ocr` | 0 | 729 | 27 |

Con OCR forzado, la prosa queda legible. Hay errores residuales en la p. 5: un patrón `LIKE` de una
restricción `CHECK` salió invertido y una viñeta quedó ilegible. En esos fragmentos la capa de texto
original sí es correcta, así que hay que cotejarlos a mano.

### `Apuntes/1. Apunte - Recomendado.pdf` (escaneo de una página de Notion, 24 páginas)

- La prosa, los títulos y las listas salen bien, con los acentos correctos.
- Los bloques de código conservan el contenido, pero pierden los saltos de línea y la indentación y
  tienen errores de puntuación (`},` se lee `'{`).
- Se probó el enriquecimiento de código de Docling (`do_code_enrichment`) en la p. 12 y se descartó:
  - Recupera los saltos de línea y el `---` de YAML.
  - Altera caracteres que el OCR común había leído bien: cambia una clave, inventa dígitos y deforma palabras.
  - Es unas 13 veces más lento (121 s frente a 9,5 s por página).

  Para fuentes académicas, un dato alterado es peor que un salto de línea perdido.

## Calidad de las extracciones (fase C)

### Texto dentro de imágenes

Docling exportaba como `<!-- image -->` el texto reconocido dentro de las figuras, así que se perdía.
Lo detectó la primera validación, que encontró páginas vacías en dos formularios escaneados. El
problema alcanzaba a **35 documentos**. Las mayores pérdidas, medidas como proporción del texto
reconocido que no llegaba al Markdown, eran:

| Documento | Pérdida |
|---|---|
| `Formularios/2. Formulario.pdf` | 91 % |
| `Guia de Ejercicios` de u4 | 60 % |
| `Formularios/3. Formulario.pdf` | 54 % |
| Autoevaluación 3 | 40 % |
| `1. MongoDB` | 37 % |
| `Unidad-5_1` | 28 % |

Con `picture_text` se recuperó ese texto: preguntas y opciones de las autoevaluaciones, y código
de las capturas de terminal. Como efecto secundario, las capturas de interfaces (Compass, SSMS)
agregan rótulos de botones y menús. Siempre vienen después de una marca `<!-- image -->`.

### Código

| Origen de los bloques | Cantidad | Fiabilidad |
|---|---|---|
| Capa de texto | 202 | caracteres fiables; se pierden saltos e indentación |
| OCR de capturas o escaneos | 184 | puede haber errores de caracteres |
| Mixto | 4 | — |

Los 392 bloques incluyen 2 sin tokens medibles. En total, 277 de 392 (71 %) quedaron en una sola línea.

- El código de MongoDB de la cátedra es mayormente OCR de capturas:
  - `1. MongoDB`: 61 bloques.
  - `2. MongoDB`: 45.
  - `3. MongoDB`: 15.
- Los demás documentos de cátedra (u1, u2, u3 y u5) son mayormente capa de texto.
- Docling ya pierde los saltos de línea en su modelo interno; no es un problema de la exportación.

### Codificación y OCR

- No queda texto ilegible: `illegible_ratio` es 0 en los 51 documentos.
- Escaneos con OCR: `Apuntes/1`, `Formularios/2–3` y los parciales 1–4.
  - En los parciales, el enunciado impreso y sus tablas se reconocen bien.
  - La resolución manuscrita sale fragmentada y no es fiable.
  - `Parcial/4` no tiene estructura de títulos.
- Hay dos fórmulas no decodificadas, en `Apuntes/2` y `Apuntes/4`. Son símbolos aislados, no matemática.
- **DOCX** (`5. Apunte/*`, `6. Apunte`, la recopilación de parciales): Docling no reconoce sus
  títulos y cada uno queda como una sola sección de 7 a 62 mil caracteres. Probablemente usan negrita
  en lugar de estilos de título. Eso limita la selección de fragmentos por sección de `package`.

### Advertencias de validación

| Código | Cantidad | Lectura |
|---|---|---|
| `formula-dudosa:delimitadores-desbalanceados` | 58 | Ruido: son operadores `$match`, `$group`, `$lookup` de MongoDB, no fórmulas |
| `codigo-sin-saltos` | 26 documentos | Real: hay que cotejar el código con el original |
| `secciones-vacias` | 23 documentos | Mayormente títulos de diapositiva sin cuerpo, o seguidos solo por una imagen |
| `formula-dudosa:glifos-uso-privado` | 5 | Viñetas de Word o PowerPoint |
| `formula-dudosa:formula-no-decodificada` y `formulas-no-decodificadas` | 2 + 2 | Ver arriba |
| `sin-estructura` | 2 | `Formularios/2` y `Parcial/4` |
| `sin-matriz` | 1 | Falta `curriculum-map.yaml` |

## Duplicaciones y versiones

No hay copias exactas. Los casi duplicados se midieron por contención de 7-gramas de palabras sobre
el texto normalizado. No se eliminó ningún documento.

| Contenido | en | Contención | Lectura |
|---|---|---|---|
| `5. Apunte/UNIDAD 5.docx` | `5. Apunte/UNIDAD 4.docx` | 100 % | `UNIDAD 4` es acumulativo (u4 + u5 + versión previa de u6) |
| `Parcial/7. … Recuperatorio.txt` | `Recopilado/Parciales base de datos.docx` | 82 % | El mismo recuperatorio 1C2025, transcripto otra vez |
| `Formularios/3. Formulario.pdf` | `Autoevaluación 3.pdf` | 70 % | Otro intento de la misma autoevaluación |
| `5. Apunte/Unidad 6.docx` | `5. Apunte/UNIDAD 4.docx` | 53 % | Versión previa de u6 dentro de `UNIDAD 4` (67 de 102 párrafos) |
| `RESOLUCION WF.pdf` | `Guia de Ejercicios - Windows Functions.pdf` | 52 % | La resolución copia los enunciados |
| `Unidad 1 - Parte 2` (cátedra) | `Apuntes/4. Apunte.pdf` | 47 % | `4. Apunte` transcribe presentaciones de cátedra |
| `Parcial/3` (foto) | `Recopilado/…docx` | 37 % | Mismo examen 2C2024 T3 |
| `Guia  de Ejercicio 2` (u4) | `RESOLUCION MONGO.pdf` | 34 % | La resolución copia los enunciados |
| `Unidad-2-Guia-Ejercicios` | `Unidad 1/Guia de Ejercicios` | 34 % | Pautas comunes de TP 1 y TP 2 |

`4. Apunte` también reproduce entre el 27 % y el 29 % de `Window Functions`, `Unidad-2-parte-1`,
`Unidad-2-parte-2` y `Unidad-3 Parte 1`. Hay que tratarlo como derivado de la cátedra, no como fuente
independiente.

### Versiones del programa

| Programa | Unidades 2, 3 y 4 | Parciales | KDD y Data Mining |
|---|---|---|---|
| 2023, publicado en el sitio del DIIT ([PDF](https://ingenieria.unlam.edu.ar/descargas/656_3641-BasesdeDatosAplicada.pdf), creado el 2023-09-04) | "transaccionales" y "no transaccionales" | dos: u1–u3 y u4–u6 | en u4 |
| 2024, en `raw/` (firmado el 07/08/2024) | "relacionales" y "no relacionales" | uno: u1–u4; u5 y u6 se evalúan en el TP y el final | en u4 (corregido; ver nota) |

> **Corrección (fase curricular).** Este informe decía antes que el programa 2024 había quitado
> KDD y Data Mining de u4. Es un error: la página renderizada del programa 2024 (p. 3) termina la
> u4 con "Data Lakes. Introducción al Data Mining. Knowledge Discovery in Databases.". pypdfium2 no
> extrae esa última línea de la celda; Docling sí. El contenido de u3 a u6 es igual en ambas versiones.

- La terminología del portal y su "2do parcial" siguen el programa de 2023.
- Los exámenes del lote (2024–2026) evalúan solo u1–u4, lo que concuerda con el de 2024.
- El sitio oficial no publica una versión posterior a 2023 y no hay evidencia de una posterior a 2024.
- Se mantiene el de 2024 como referencia provisional.

### Versiones de presentaciones de cátedra

- u3 está en una versión de 2023.
- La presentación de agregaciones de u4 en `raw/` es v3.0 de 2025. Existía una v3.0 de 2026, que es
  la que se retiró de `public/`.

## Seguridad y privacidad pendientes

1. **Credencial.** Hay que notificar a la titular de la credencial de Atlas que aparece en
   `Instalación MongoDB.pdf`, para que la revoque o la cambie. El documento sigue con `skip`, no se
   extrajo y no se reprodujo la credencial en ningún archivo.
2. **PDF de cátedra.** Los dos PDF se quitaron de `public/` y se registraron en `migration/withdrawn.json`.
   - `npm run validate` exige que no se publiquen.
   - `verify-production.mjs` exige un 404.
   - El importador no los vuelve a copiar.

   Siguen publicados en producción hasta el próximo despliegue, que requiere autorización. La caché
   de Pages puede servirlos un tiempo más. También siguen en el historial de Git.
3. **Datos personales en los derivados privados.** `processed/` contiene DNI, nombres y correos de
   estudiantes: autoevaluaciones, fotos de parciales, metadatos y un correo en `Apuntes/10`. Nada de
   eso es versionable. Los paquetes de contexto que se generen con `package` también los pueden
   arrastrar: hay que anonimizarlos antes de usarlos para publicar.
4. **`MongoDB no oficial.pdf`.** Sigue publicado. No es material de cátedra, no tiene credenciales y
   su único correo es de ejemplo.

## Recomendaciones

### `curriculum-map.yaml`

1. Usar la estructura de Álgebra II: `program`, `units`, `topics`, con `sources: {doc, pages}`,
   `page`, `production` y `validation`. Declarar el programa 2024 (`bbdd-aplicadas-3d9721081e14`)
   como referencia y registrar en `program` la discrepancia con el de 2023 del sitio oficial.
2. Usar los temas del programa 2024 como `topics`, uno por ítem. Para u6, basarse en la Ley 25.326, GDPR e ISO/IEC 25012.
3. Priorizar las fuentes de cátedra (`teoria-catedra` y `guia-practica`) con sus páginas. Usar los
   apuntes de alumnos solo como apoyo. Fuentes por unidad:
   - u3: las dos presentaciones de 2023.
   - u4: las partes 1–3 de MongoDB y el apunte NoSQL.
   - u5: `Unidad-5_1`.
   - u6: no hay fuente de cátedra. Usar `Unidad 6.docx` y `4. Apunte` marcados como alumno, y la normativa primaria.
4. Registrar los exámenes como `exercises` de referencia de cada tema. Pivot, window functions, CTE,
   índices, aislamiento, CAP/BASE, MQL y APIs aparecen en casi todos los parciales.
5. Agregar `keywords` en inglés y en español (`window`, `pivot`, `$lookup`, `collation`). La selección
   de fragmentos es léxica.
6. Antes de `package`, conviene desactivar o filtrar en esta materia el control de fórmulas, por los
   58 falsos positivos de `$`, y decidir cómo seccionar los DOCX sin títulos.

### Auditoría de los apuntes del portal

1. Contrastar cada página con la matriz:
   - temas del programa 2024 sin página;
   - páginas sin fuente de contenido, como KDD en u4: figura en ambos programas, pero ningún documento lo desarrolla;
   - temas fuera de su unidad, como el índice clúster en u1 o las transacciones en u2.
2. Revisar los pares que se solapan: transacciones (2) e índices (2) en u3, y formatos (2) en u2.
3. Decidir con la cátedra la terminología (programa 2023 o 2024) y el esquema de parciales antes de
   cambiar títulos. Si cambian rutas, actualizar la matriz de migración y conservar las antiguas.
4. Cotejar todo bloque SQL o MQL tomado de las fuentes con la página original, en especial el código
   OCR de MongoDB y los 277 bloques aplanados.
5. Mantener los nombres de docentes solo donde ya consten en documentos públicos. No usar nada de
   autoevaluaciones ni fotos de exámenes sin anonimizar.
