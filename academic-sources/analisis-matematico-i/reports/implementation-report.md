# Informe de implementación — Análisis Matemático I

Fechas: 2026-11-20 y 2026-11-21. Rama de trabajo `feat/analisis-matematico-i` (sin commits). Referencia curricular:
programa analítico 2C2026 de la cátedra. Contrato de redacción: `content-guide.md`. Matriz: `curriculum-map.yaml`.

## 1. Fuentes y procesamiento

- **Documentos:** 9 únicos (10 archivos, uno duplicado) después de retirar el manual del curso de ingreso, que no era
  material de la materia. Detalle, perfiles de extracción y calidad: `ingest-audit.md`.
- **Extracción:** 9 documentos convertidos con Docling. Cinco con reconocimiento de fórmulas (`full`): guía de TP, apunte
  de la Unidad 4, autoaprendizaje y las dos prácticas de parcial. Cuatro con `text`: apuntes de las Unidades 1 a 3 y
  consideraciones generales. En los apuntes de Word, la capa de texto conserva las ecuaciones en Unicode.
- **Problemas de OCR y de fuentes:**
  - la capa de texto de los PDF de pdfTeX pierde exponentes, índices de raíces y fracciones en línea;
  - el modelo de fórmulas pierde el «=», confunde primas y desordena ecuaciones en línea de Word, y solo corre en CPU (≈30 a 36 s por fórmula).

  Por eso los enunciados de la guía se leyeron siempre en el PDF renderizado.

## 2. Programa y matriz curricular

- El programa 2C2026 coincide con la organización del portal: 4 unidades y **31 temas** curriculares (9, 9, 8 y 5).
  No hay programas anteriores entre las fuentes para contrastar.
- Decisiones D1–D5 en la matriz:
  - D1: programa de referencia;
  - D2: atribución de las prácticas existentes, sin reproducciones nuevas;
  - D3: las páginas de teoría pasan a ser resúmenes integradores;
  - D4: el diferencial es complementario y los teoremas de funciones continuas se incluyen en «Propiedades»;
  - D5: la razón de cambio media aparece en la Unidad 1.
- **Cobertura:** los 31 temas pasan a estado `completo` (`coverage_after`), con `production: redactado` y `validation: verificado`.

## 3. Páginas

| | Cantidad | Detalle |
|---|---:|---|
| Antes | 85 | — |
| Después | 110 | Todas las URL anteriores se conservan |
| Creadas | 25 | 20 lecciones, 4 páginas de integradores, guía «Cómo estudiar» |
| Modificadas | 18 | Las 18 son páginas migradas, registradas en `migration/revisions.json` (etapa AM1) |
| Conservadas sin cambios | 67 | — |

Las 18 modificadas son:

- la portada;
- 4 presentaciones de unidad, reescritas con la ruta de aprendizaje y las tablas de temas conservadas;
- 4 resúmenes integradores (las páginas de teoría originales, con su contenido íntegro);
- 4 índices de práctica, con atribución;
- 4 correcciones matemáticas en prácticas: U1 ejercicio-9 y adicionales, U2 ejercicio-16 y ejercicio-25;
- la página de GeoGebra de derivada.

Las prácticas 3 y 4 también se corrigieron; cuentan entre los índices de práctica.

**Lecciones por unidad** (cada una con objetivos, prerrequisitos, definiciones, interpretación geométrica, teoremas con
hipótesis y contraejemplos, demostraciones rotuladas, ejemplos resueltos, errores frecuentes, ejercicios,
autoevaluación, resumen y enlace al tema siguiente):

- **U1:** Funciones y modelos · Ceros, signo, paridad y acotación · Funciones elementales · Álgebra de funciones y
  transformaciones · Funciones biyectivas y función inversa.
- **U2:** Entornos y límite finito · Límites laterales y propiedades · Infinitésimos · Límites infinitos y en el infinito
  · Cálculo de límites e indeterminaciones · Asíntotas · Continuidad y discontinuidades (autocontenida, porque en 2C2026
  el tema se estudia de forma autónoma).
- **U3:** Razón de cambio y derivada · La derivada como función · Reglas de derivación · Regla de la cadena e inversa ·
  Derivación implícita y logarítmica.
- **U4:** Orden de contacto · Polinomio de Taylor y de Mac Laurin · Término complementario.

**Navegación** (`src/config/sidebar.mjs`): «Presentación», «Cómo estudiar» y, por unidad, «Presentación y ruta», Teoría,
Práctica y «Resumen integrador». El orden del menú es el pedagógico, así que la paginación recorre la ruta.

**Figuras:** 31 SVG generados desde las fórmulas por `figures/u<n>_figuras.py` con `figures/svgplot.py` (Python estándar).
Tienen texto alternativo y fondo propio en tema claro u oscuro.

## 4. Ejercicios y verificación

| Unidad | Ejercicios originales | Inicial | Intermedio | Avanzado | SymPy | Razonamiento | Mínimo |
|---|---:|---:|---:|---:|---:|---:|---|
| U1 | 25 | 6 | 9 | 10 | 23 | 2 | 12 (≥3 por nivel) |
| U2 | 31 | 9 | 10 | 12 | 25 | 6 | 15 (≥4) |
| U3 | 22 | 6 | 8 | 8 | 21 | 1 | 15 (≥4) |
| U4 | 17 | 4 | 6 | 7 | 15 | 2 | 12 (≥3) |
| **Total** | **95** | 25 | 33 | 37 | **84** | **11** | todos cumplidos |

- Los 95 tienen enunciado y resolución completa (estrategia, desarrollo y resultado).
- Incluyen 15 integradores de estilo parcial, con ítems de opción múltiple justificados y con GeoGebra (y resolución analítica).
- Todos son originales. Las prácticas de la guía de la cátedra (≈150 ejercicios) se conservan aparte, con atribución.

**`content-pipeline verify-math`** (SymPy 1.14): **430 comprobaciones, 430 aprobadas**.

| Grupo | Comprobaciones | Qué verifican |
|---|---:|---|
| Teoría | 170 | Cada ejemplo resuelto marcado en las lecciones: el resultado y los pasos intermedios publicados |
| Práctica | 85 | Los 84 ejercicios `sympy`, más una comprobación parcial de la demostración `U3.07` |
| Auditoría | 175 | Resultados de las prácticas existentes recalculados y contrastados con las respuestas oficiales, y regresiones de cada corrección |

Distinción del estado de cada resultado:

- **Comprobado simbólicamente** (exacto): los ejercicios `sympy` y los ejemplos con marcador.
- **Comprobado numéricamente bajo condiciones explícitas:** las aproximaciones decimales y las cotas de error, que se
  contrastaron con aritmética racional o con 30 dígitos. Siempre acompañan un resultado exacto.
- **Demostración revisada sin cálculo:** los 11 ejercicios `razonamiento` y las demostraciones de las lecciones (unicidad
  del límite, intercalación, derivable implica continua, reglas del producto, cociente y cadena, coeficientes de Taylor,
  resto de Lagrange). Las revisó la coordinación; SymPy no las demuestra.
- **No verificado:** los comandos de GeoGebra (no se pueden ejecutar en este entorno) y los ejercicios de la guía que
  dependen de leer un gráfico.

**Advertencia técnica:** SymPy 1.14 calcula mal algunos límites laterales de potencias. Por ejemplo,
`limit(3**(1/x), x, 0, dir="-")` devuelve `oo` en lugar de `0`. Las comprobaciones reescriben esas potencias como
`exp(log(base)·exponente)` y contrastan numéricamente.

## 5. Correcciones a los apuntes anteriores

Detalle en `content-audit.md`. En resumen:

- **Errores matemáticos corregidos, con su regresión:**
  - U1: adicional 1c (dominio) y 9l (enunciado mal transcripto).
  - U2: 16e (enunciado mal transcripto: es una potencia, no un producto), 25a y 25c.
  - U3: ejercicio 14 (ordenada), 42d (contraejemplo inválido), 42 (borrador) y 5c (cúspide con tangente vertical).
  - U4: 15b, y 3b y adicional 4 (discrepancias espurias).
- **Respuestas oficiales de la guía con errores** (evidencia en el PDF y en SymPy): U1 9j y 9k (intercambiadas); U2 2b y 25c; U3 6e y 42k; U4 15b.
- **Presentación de la Unidad 2:** decía que Continuidad se evalúa en el segundo parcial; según 2C2026 es en el primero.
- **Residuos de la migración** («1. TOC» de Jekyll) y la frase «copiado literal del PDF» retirados.

## 6. Resultado de las pruebas

| Control | Resultado |
|---|---|
| `content-pipeline inventory` / `normalize` / `validate` | 9 documentos extraídos y normalizados; 0 errores, 137 advertencias explicadas en `ingest-audit.md` |
| `content-pipeline verify-math` | 430/430 |
| `content-pipeline qa` | Análisis: 0 errores, 0 advertencias (110 páginas, 95 ejercicios completos). Álgebra II y BBDD sin cambios ni errores |
| `pytest` (pipeline) | 108 aprobados, 1 omitido (requiere los contenedores de motores) |
| `npm run build` | correcto |
| `npm run validate` | 0 errores; 287 páginas, todas alcanzables desde la portada; 227 revisiones encadenadas |
| `npm run test:browser` | 56 aprobadas, 6 omitidas (escritorio y móvil) |
| `git diff --check` | limpio |

Pruebas de navegador nuevas o actualizadas:

- estructura del menú de Análisis;
- orden de la teoría según la ruta de cada unidad;
- renderizado de una lección por unidad: KaTeX sin errores, figuras cargadas con texto alternativo, resoluciones plegadas y sin desborde en móvil;
- desborde de «Cómo estudiar» y de una presentación de unidad;
- la prueba de Diseño de Software separada de la de Análisis.

## 7. Limitaciones conocidas

- **Figuras:** son imágenes SVG cuyo tema sigue la preferencia del sistema operativo, no el selector claro/oscuro del
  sitio. Siempre son legibles porque tienen fondo propio. Una mejora futura es generarlas como SVG en línea con las
  clases `.math-figure` que ya usa Álgebra II.
- **GeoGebra:** los comandos de las lecciones y de la sección de GeoGebra no se ejecutaron en GeoGebra.
- **Apuntes sin fórmulas en LaTeX:** los de las Unidades 1 a 3 no tienen sus fórmulas extraídas en LaTeX (decisión de
  costo). No afecta el contenido publicado.
- **Ejercicios con gráficos:** los de la guía que dependen de leer un gráfico (U2 ej. 1, 4, 22, 23, 27, entre otros) se
  revisaron sin recálculo.
- **Resúmenes integradores:** conservan su notación original ($V(a,\delta)$, `\sin`), equivalente a la de las lecciones.

## 8. Decisiones pendientes (requieren a la cátedra o al responsable del sitio)

1. **Autorización para reproducir enunciados de la Guía de TP 2026** en las prácticas existentes (D2). Hoy se conservan
   con atribución y no se agregaron reproducciones nuevas.
2. **Comunicar a la cátedra las erratas** encontradas en las respuestas oficiales (sección 5).
3. **Reprocesar los apuntes de las Unidades 1 a 3** con fórmulas (≈5 h de CPU), si se necesitan en LaTeX.
4. **Tratamiento de los temas fuera del programa:**
   - si se quiere desarrollar el diferencial (hoy es una nota complementaria);
   - si los teoremas de Bolzano, del valor intermedio y de Weierstrass deben ir con demostración formal;
   - si la sección de optimización de GeoGebra se mantiene.
