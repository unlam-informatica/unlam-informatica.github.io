# Auditoría de ingesta documental — Bases de Datos Aplicada (3641)

Fecha: 2026-11-17 · Fase: inventario (sin Docling, sin cambios en los apuntes).

> **Actualización (fase de extracción).** Desde la fase de extracción cambiaron cuatro cosas:
> - Los `.txt` ya se catalogan y se extraen (54 documentos; solo el enlace a Notion queda en `skip`).
> - Los dos PDF de cátedra de `public/` se retiraron.
> - `UNIDAD 4.docx` también contiene una versión previa de u6.
> - Se verificó el programa 2023 publicado por el DIIT.
>
> Ver `extraction-report.md`.

Este informe no reproduce texto de las fuentes ni nombres de estudiantes. La clasificación de cada
documento está en `../catalog.yaml` (generado con `content-pipeline inventory`) y sus reglas, en
`../subject.yaml`. El contenido se verificó leyendo la capa de texto de cada PDF/DOCX con
pypdfium2 y python-docx, y mirando páginas renderizadas de los escaneos. El nombre y la carpeta no
se tomaron como evidencia.

## Resumen

| Concepto | Valor |
|---|---|
| Archivos en `raw/` (sin `.DS_Store`) | 54 |
| Inventariados (PDF 42, DOCX 5) | 47, todos con contenido único (sin copias por SHA-256) |
| Omitidos por formato (`.txt`) | 7 |
| Extracción prevista | 45 con perfil `text`, 2 con `skip` |
| Escaneos sin capa de texto (requieren OCR) | 8 |
| Material de cátedra | 20 (programa, presentación, 12 teorías, 5 guías, 1 instructivo) |
| Material de alumnos | 27 (10 apuntes, 3 resoluciones, 6 autoevaluaciones resueltas, 8 exámenes) |

Fuente oficial de referencia: `Programa Analitico.pdf`, programa 2024 firmado por el jefe de
cátedra con seis unidades, que coinciden con las seis del portal.
`Presentación y Cronograma.pdf` (v1.32, agosto de 2025) fija las normas de cursada: un parcial
sobre u1–u4, un TP integrador y un final sobre todas las unidades.

## Clasificación propuesta

### Cátedra

| Documento | Tipo | Unidades | Versión |
|---|---|---|---|
| Programa Analitico.pdf | programa | u1–u6 | 2024 |
| Presentación y Cronograma.pdf | cronograma | u1–u6 | v1.32 (2025-08) |
| Material Teorico/Unidad 1/1. Unidad 1 - Parte 1 | teoria-catedra | u1 | v1.1.0 (2025-03) |
| Material Teorico/Unidad 1/2. Unidad 1 - Parte 2 | teoria-catedra | u1 | v1.0.3 (2024-08) |
| Material Teorico/Unidad 1/3. Window Functions | teoria-catedra | u1 | v1.0 (2024-03) |
| Material Teorico/Unidad 1/Guia de Ejercicios - Windows Functions | guia-practica | u1 | v1.0 (2024-03) |
| Material Teorico/Unidad 1/Guia de Ejercicios (TP 1) | guia-practica | u1 | 2024-03 |
| Material Teorico/Unidad 2/Unidad-2-Guia-Ejercicios (TP 2) | guia-practica | u1, u2 | 2024-04 |
| Material Teorico/Unidad 2/Unidad-2-parte-1 | teoria-catedra | u2, u4 (DWH/Data Lake) | V1.0.1 (2024) |
| Material Teorico/Unidad 2/Unidad-2-parte-2 | teoria-catedra | u2 | v1.0 (2024-04) |
| Material Teorico/Unidad 3/Unidad-3---Parte-1_2 | teoria-catedra | u3 (índices, planes, optimización) | v1.0 (2023-08) |
| Material Teorico/Unidad 3/Unidad-3---Parte-2 | teoria-catedra | u3 (TCL, concurrencia, monitoreo) | v1.0 (2023-08) |
| Material Teorico/Unidad 4/1. MongoDB | teoria-catedra | u4 (CRUD, Compass, Atlas) | V2.0 (2025) |
| Material Teorico/Unidad 4/2. MongoDB | teoria-catedra | u4 (agregaciones, vistas) | v3.0 (2025) |
| Material Teorico/Unidad 4/3. MongoDB | teoria-catedra | u4 (índices) | v1.0 (2024) |
| Material Teorico/Unidad 4/4. MongoDB | teoria-catedra | u4 (NoSQL conceptual) | 2023-07 |
| Material Teorico/Unidad 4/Guia  de Ejercicio 2 | guia-practica | u4 | 2C2025, com. 02-5600 |
| Material Teorico/Unidad 4/Guia de Ejercicios | guia-practica | u4 | 2024-09 |
| Material Teorico/Unidad 4/Instalación MongoDB | instructivo (`skip`) | u4 | 2023-08 |
| Material Teorico/Unidad 5/Unidad-5_1 | teoria-catedra | u5 | v1.1 (2025-06) |

### Alumnos

| Grupo | Documentos | Unidades | Período |
|---|---|---|---|
| Resúmenes recientes | Apuntes/1, 2, 3 "Recomendado"; Base de Datos Aplicada; Bases de Datos Aplicadas | u1–u4 | 1C2025 a 1C2026 |
| Resumen por clases | Apuntes/4. Apunte | u1–u6 | 2025 |
| Serie histórica (mismo autor) | Apuntes/6. Apunte; 5. Apunte/UNIDAD 4, 5, 6 | u1–u6 | 2C2023 |
| Preguntas con respuestas | Apuntes/10. Apunte (`resolucion-alumno`) | u1–u5 | sin fecha |
| Resoluciones de guías | Ejercicios Resueltos/Z/RESOLUCION WF, RESOLUCION MONGO | u1; u4 | 2025 |
| Autoevaluaciones (MS Forms) | Formularios/1–3 (escaneos); Autoevaluación 1, 3, 4 (texto) | u1–u4 | 2C2024 |
| Exámenes | Parciales Filtrados/Parcial/1, 2, 3, 4, 8, 9, 10; Recopilado | u1–u4 | 2C2023 a 2C2026 |

Comisiones: 5600 corresponde a viernes tarde y 2900 a martes noche. Lo confirman los propios exámenes.

### Omitidos por formato

La ingesta no admite `.txt`. Hay siete archivos en ese formato, todos relatos de alumnos:

- `Apuntes/7. Apunte.txt`: un enlace a Notion. No se siguió.
- `Parciales Filtrados/Final/1–3`: tres finales de 2025.
- `Parciales Filtrados/Parcial/5–7`: dos parciales de 2C2025 y un recuperatorio de 1C2025.

Son la única fuente de finales del lote.

## Requieren revisión humana

`needs_review` del catálogo queda vacío porque todos los documentos tienen tipo, unidad, fuente y
licencia. Los puntos siguientes no los detecta la ingesta automática y figuran en `notes`.

### Privacidad y seguridad

1. **Credencial en texto plano.** `Material Teorico/Unidad 4/Instalación MongoDB.pdf` (p. 6) tiene
   usuario y contraseña de un clúster Atlas de una docente. Quedó con `extraction: skip`. Si se
   extrae, hay que redactar el dato antes de usarlo. Conviene avisar a la cátedra para que rote la
   credencial.
2. **Datos personales.**
   - Las autoevaluaciones con texto (1, 3 y 4) muestran el DNI del alumno.
   - Las fotos de parciales 1 y 3 muestran nombre y DNI; en 2 y 4 están tachados.
   - Los metadatos de varios PDF y DOCX nombran a estudiantes.

   Nada de esto debe llegar al sitio.
3. **PDF de cátedra publicados en un repositorio público.** `public/bbdd-aplicadas/unidad-4/inputs/`
   tiene tres PDF:
   - `MongoDB-Indices.pdf`, idéntico (mismo SHA-256) a `raw/…/3. MongoDB.pdf`.
   - `MongoDB-Agregaciones-2026.pdf`, presentación de cátedra v3.0 de 2026, más nueva que la de `raw/`.
   - `MongoDB no oficial.pdf`, un laboratorio no oficial.

   Ninguna página los enlaza, pero el build los publica y la matriz de migración conserva sus
   rutas. Hay que decidir si se mantienen.

### Rotulado engañoso (ya corregido en la clasificación)

- `4. MongoDB.pdf` no trata MongoDB: es el apunte conceptual de NoSQL.
- `Unidad-2-parte-2.pdf` y `Unidad-3---Parte-2.pdf` tienen títulos de metadatos de otra unidad, y
  varios PDF dicen "Práctica Profesional Supervisada". Son restos de plantilla.
- `Unidad-3---Parte-2` numera su parte de tres formas distintas.
- `5. Apunte/UNIDAD 4.docx` repite completo, desde el párrafo 95, `UNIDAD 5.docx`.
- `10. Apunte.pdf` es una guía de preguntas con respuestas, no un apunte.
- "Formulario" quiere decir autoevaluación, no hoja de fórmulas.
- "Recomendado" no implica aval de la cátedra.
- `Parcial/8` es un recuperatorio aunque el nombre no lo diga.
- `Parcial/1` y `Parcial/4` son el mismo examen del 10/05/2024 en dos temas distintos (T3 y T4).
- En `Parcial/2` y `Parcial/6` (este último, `.txt`), el docente que indica el nombre no consta en el contenido.

### Calidad de extracción

- **Escaneos que dependen de OCR.**
  - `Apuntes/1` (Notion impreso, con código recortado).
  - `Formularios/1–3`.
  - Parciales 1–4: enunciado impreso y resolución manuscrita. El OCR del manuscrito no es fiable.
- **Mojibake en `Apuntes/4. Apunte.pdf`.** La capa de texto tiene "Û" por "ó". Puede que Docling
  la herede. El pipeline no tiene una opción para forzar OCR.
- **Errores en las resoluciones de alumnos.** RESOLUCION MONGO (ejercicio 8), `Parcial/3` y la
  recopilación (salario mal transcripto) tienen errores. Ninguna resolución del lote es de la
  cátedra.

### Vigencia

- El programa es de 2024; las presentaciones van de 2023 a 2025.
- La propia cátedra advierte que corrige el material cada cuatrimestre.
- Hay que confirmar qué versión se considera vigente, sobre todo para u3 (2023) y u4 (existe una
  v3.0 de 2026 fuera de `raw/`).

## Cobertura de las fuentes por unidad

| Unidad | Cátedra | Alumnos | Faltante |
|---|---|---|---|
| u1 | 3 teorías y 2 guías | resúmenes, resolución WF, autoevaluación, todos los exámenes | — |
| u2 | 2 teorías y 1 guía | resúmenes, autoevaluación 2 (escaneo) | — |
| u3 | 2 teorías (2023) | resúmenes, autoevaluación 3, exámenes | no hay guía de cátedra |
| u4 | 4 teorías, 2 guías y 1 instructivo | resúmenes, resolución Mongo, autoevaluación 4, exámenes | KDD figura en el programa (u4 y contenidos mínimos), pero ningún documento lo desarrolla |
| u5 | 1 teoría | apunte 2025, serie 2023, finales (`.txt`) | no hay guía ni laboratorio de cátedra |
| u6 | ninguna | `4. Apunte` (2025), `Unidad 6.docx` (2023), finales (`.txt`) | no hay material de cátedra |

## Estructura actual del portal

- 79 páginas: portada, más `teoria/` y `practica/` por unidad, con un índice en cada una.
- Teoría y práctica por unidad: u1 7 y 3, u2 9 y 7, u3 5 y 2, u4 9 y 3, u5 8 y 3, u6 7 y 3.

Observaciones para la fase de revisión (no se modificó nada):

- Los títulos de u2, u3 y u4 usan "BD Transaccionales" y "No Transaccionales". El programa 2024
  dice "Bases de datos relacionales" (aspectos básicos y avanzados) y "no relacionales".
- Los índices de u4, u5 y u6 dicen "2do parcial". El programa y la presentación prevén un solo
  parcial (u1–u4); u5 y u6 se evalúan en el TP y el final. El nombre "Parcial 1" de 2C2026 sugiere
  que esto pudo cambiar: hay que confirmarlo.
- Hay temas fuera de la unidad del programa:
  - `unidad-1/teoria/indice-cluster` trata índices clúster, que el programa ubica en u3.
  - `unidad-2/practica/transacciones` y la página `bd-transaccionales` (OLTP, aislamiento)
    adelantan temas de u3. La cátedra presenta "transaccionales" en u2 y TCL y concurrencia en u3.
- Hay pares con solapamiento probable:
  - u3: `transacciones-concurrencia` y `transacciones-y-concurrencia`.
  - u3: `indices-optimizacion` e `indices-y-planes`.
  - u2: `formatos-conectividad` y `formatos-de-intercambio`.
- Ninguna página cita sus fuentes. `datos-data-lake-kdd` (u4) desarrolla KDD sin respaldo en `raw/`.
- u5 y u6 tienen mucho desarrollo (laboratorios, guías de parcial) con poca o ninguna fuente de
  cátedra que lo respalde.

## Próximos pasos sugeridos

1. Decidir sobre la credencial, los PDF de `public/…/inputs/` y la vigencia de las versiones.
2. Decidir qué hacer con los `.txt`: agregar soporte de texto plano al pipeline (ingesta y
   extracción sin Docling) o convertirlos a mano a Markdown con la leyenda de reconstrucción no oficial.
3. Para la extracción, probar primero `Apuntes/4. Apunte.pdf` y un escaneo (`Formularios/2`) con
   `--limit` o `--ids`, para medir la calidad del OCR antes de procesar el lote.
4. Redactar `curriculum-map.yaml` y una `content-guide.md` de la materia.
