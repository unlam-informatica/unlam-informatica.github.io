# Auditoría de ingesta — Análisis Matemático I

Fecha: 2026-11-20 y 2026-11-21. Fuente de verdad: el contenido actual de `raw/` (privado, no versionado). Los
derivados de `processed/` también son privados.

## Inventario

`content-pipeline inventory --subject analisis-matematico-i`: **10 archivos, 9 documentos únicos, 1 duplicado exacto**
(mismo SHA-256). Clasificación hecha por el contenido (portadas, encabezados y texto de las primeras páginas), no por
el nombre del archivo. Ningún documento contiene datos personales de estudiantes; los autores que figuran son docentes
de la cátedra.

| Documento (id) | Tipo | Contenido verificado | Unidades | Confiabilidad |
|---|---|---|---|---|
| Consideraciones generales 2C2026 (`…-5ccac17bb05e`) | programa | Programa analítico, metodología, cronograma 2C2026, régimen de acreditación y bibliografía | u1–u4 | Alta: documento oficial de la cátedra, el más reciente |
| Apuntes de clase, Unidad 1 (`…-cf66ddbbbcbd`) | teoría de cátedra | Williner (2016), funciones; 38 p. | u1 | Alta (citado como bibliografía por el programa) |
| Apuntes de clase, Unidad 2 (`…-378ec9f8def6`) | teoría de cátedra | Límite funcional y continuidad; 56 p. | u2 | Alta |
| Apuntes de clase, Unidad 3 (`…-54ca5de3f6da`) | teoría de cátedra | Derivada y diferencial; 48 p. | u3 | Alta |
| Apuntes de clase, Unidad 4 (`…-62bdddb361bc`) | teoría de cátedra | Polinomios de Taylor; 19 p. | u4 | Alta |
| Guía de Trabajos Prácticos 2026 (`…-20099881563a`) | guía práctica | Prácticas 1 a 4, ejercicios adicionales y respuestas; 46 p. | u1–u4 | Alta; las respuestas tienen erratas puntuales (ver `content-audit.md`) |
| Actividad de autoaprendizaje de Continuidad (`…-315ad3f8bf01`) | guía de estudio | Consignas y recursos (videos) para estudiar Continuidad en forma autónoma; 4 p. | u2 | Alta |
| Práctica para el primer parcial (`…-441038ce6982`) | práctica de examen | Ejercicios de práctica, algunos tomados en parciales anteriores; 7 p. Dos archivos idénticos (`…(1).pdf` y `…(1)_1.pdf`) | u1–u2 | Alta |
| Ejercicios de repaso del segundo parcial (`…-00eed4030c1f`) | práctica de examen | 15 ejercicios de repaso; 3 p. | u2–u4 | Alta |

No hay resoluciones oficiales completas, exámenes reconstruidos por alumnos ni libros entre las fuentes locales. La
bibliografía del programa no está disponible localmente.

### Documento retirado (2026-11-21)

`Ingenieria-2024-COMPLETO-(SIN-ISBN).pdf` (`analisis-matematico-i-6822a8f21bf1`, 537 páginas) era el **Manual para el
Curso de Ingreso 2024** de la UNLaM (comprensión de textos y matemática de ingreso), no material de la materia. Ya
estaba clasificado como bibliografía con derechos reservados y con extracción limitada a las primeras 30 páginas
(`front-matter`). El responsable lo quitó de `raw/`. Al reinventariar se detectó como faltante y:

- se eliminaron sus derivados (`processed/markdown/…-6822a8f21bf1.md`, `processed/json/…-6822a8f21bf1.json` y su
  entrada del manifiesto); no tenía imágenes ni otros derivados;
- se quitó del catálogo y su regla de `subject.yaml` (queda un comentario de registro);
- se retiraron de la matriz curricular y de la guía de contenido las referencias a sus módulos.

## Extracción (Docling 2.150)

Pruebas previas sobre documentos representativos:

- **Ejercicios del segundo parcial** (pdfTeX, perfil `full`, 3 p., ≈6 min). Las fórmulas en bloque salen bien, incluidas
  las funciones por tramos con `cases`. Errores: «si x ≠ 0» reconocido como `\sin(x \neq 0)`, un enunciado de verdadero
  o falso entero metido dentro de una fórmula. **En la capa de texto de los PDF de pdfTeX se pierden exponentes,
  índices de raíces y fracciones en línea** (`(g(x))x` por `(g(x))^x`, `e3x+18`, `x2 16 + y2 4`) y las tildes salen
  separadas («ecuaci´on»).
- **Apunte de la Unidad 4** (Word): con `text` las fórmulas quedan como `formula-not-decoded`; con `full`, 115 fórmulas
  decodificadas en 69 minutos, con la estructura bien (fracciones, potencias, sistemas) pero con errores sistemáticos:
  el signo «=» se pierde, las primas se confunden ($f'$ por $f''$) y las ecuaciones en línea de Word se desordenan.
- El modelo de fórmulas **no admite aceleración MPS** en este equipo (solo CPU, unos 30 a 36 s por fórmula). Una
  primera corrida de todos los documentos se interrumpió por falta de memoria con otros procesos en paralelo; la
  extracción se retomó documento por documento, aprovechando la caché.

Perfiles aplicados:

| Documento | Perfil | Páginas | Tablas | Figuras | Fórmulas (sin decodificar) |
|---|---|---:|---:|---:|---|
| Consideraciones generales | `text` (sin fórmulas) | 5 | 1 | 0 | — |
| Apunte U1 | `text` | 38 | 6 | 50 | 87 (87) |
| Apunte U2 | `text` | 56 | 14 | 60 | 210 (210) |
| Apunte U3 | `text` | 48 | 13 | 42 | 218 (217) |
| Apunte U4 | `full` | 19 | 3 | 12 | 115 (0) |
| Autoaprendizaje Continuidad | `full` | 4 | 0 | 27 | 0 |
| Práctica primer parcial | `full` | 7 | 2 | 16 | 11 (0) |
| Repaso segundo parcial | `full` | 3 | 0 | 0 | 10 (0) |
| Guía de TP 2026 | `full` (≈57 min) | 46 | 20 | 13 | 106 (0) |

**Decisión:** en los apuntes de las Unidades 1 a 3 (PDF de Word), la capa de texto conserva las ecuaciones como caracteres
matemáticos Unicode y fue suficiente para auditar temas, notación y nivel. El reconocimiento de fórmulas con `full`
costaría unas 5 horas de CPU (514 fórmulas) y, por lo visto en la Unidad 4, no sería confiable sin revisión. Queda como
reproceso opcional (`content-pipeline extract --subject analisis-matematico-i --profile full --force --ids …`).

**Para leer enunciados** de la guía se usó el **PDF renderizado** (imagen de la página), porque ni la capa de texto ni
la extracción garantizan el alcance de raíces, exponentes y fracciones. Así se detectaron dos enunciados mal transcriptos
en el portal (ver `content-audit.md`).

## Normalización y validación documental

`content-pipeline normalize` normalizó los 9 documentos. `validate --subject analisis-matematico-i`: **0 errores**, 137
advertencias y 1 información:

- 104 «fórmula no decodificada» y 3 «fórmulas no decodificadas»: son los marcadores de los apuntes de las Unidades 1 a 3
  procesados con `text` (decisión de costo, ver arriba);
- 16 «glifos de uso privado» y 9 «delimitadores desbalanceados»: símbolos de las tipografías de Word y de pdfTeX que el
  extractor no traduce (por ejemplo, los encabezados de sección de la guía). Afectan solo al texto extraído, que no se
  publica;
- 5 «secciones vacías»: títulos sin texto propio (portadas e índices);
- 1 información: el duplicado exacto de la práctica para el primer parcial.

La extracción completa de los 9 documentos insumió unas 2 h 30 min de CPU, sobre todo por el reconocimiento de
fórmulas de la guía y del apunte de la Unidad 4.

## Pendientes

- Reprocesar con `full` los apuntes de las Unidades 1 a 3 si se necesitan sus fórmulas en LaTeX (opcional).
- La bibliografía del programa no está disponible localmente: se cita sin páginas.
