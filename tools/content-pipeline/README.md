# content-pipeline

Herramienta local para convertir el material académico de una materia (programas, guías,
apuntes, parciales, libros, imágenes, clases grabadas) en contexto estructurado y trazable para
redactar apuntes, y para controlar la calidad del material publicado. Es independiente del
portal: Astro no la usa ni la necesita para compilar.

Usa [Docling](https://docling-project.github.io/docling/) para la extracción y
[SymPy](https://www.sympy.org/) para la verificación matemática. No usa servicios externos,
bases de datos, colas ni modelos de lenguaje: prepara archivos que después lee quien redacta.

## Arquitectura

```text
academic-sources/<materia>/
├── subject.yaml           reglas de clasificación (versionado)
├── catalog.yaml           inventario con hashes y procedencia (versionado, sin rutas absolutas)
├── curriculum-map.yaml    matriz curricular: programa → temas → fuentes → páginas → ejercicios (versionado)
├── content-guide.md       contrato de redacción de la materia (versionado)
├── checks/*.py            comprobaciones simbólicas de ejemplos y ejercicios (versionado)
├── reports/               evidencia de verificación y control de calidad (versionado)
├── raw/                   documentos originales (privado, ignorado por Git)
└── processed/             derivados (privado, ignorado por Git)
    ├── markdown/<id>.md   texto por página con marcas <!-- page: N -->
    ├── json/<id>.json     sobre con metadatos, páginas y DoclingDocument
    ├── images/<id>/       figuras exportadas
    ├── normalized/<id>.md Markdown normalizado
    ├── index/<id>.json    secciones con título, tipo, páginas y advertencias
    ├── context/<u>/<t>.md paquetes de contexto por tema
    ├── manifest.json      caché de extracción (hash del original + motor + perfil)
    └── reports/           inventario y validación documental
```

| Módulo | Responsabilidad |
|---|---|
| `ingest.py` | Recorre `raw/`, calcula SHA-256, asigna `id = <prefijo>-<sha256[:12]>`, agrupa duplicados, clasifica con `subject.yaml` y actualiza `catalog.yaml` sin pisar correcciones manuales. |
| `extract.py` | Convierte con Docling según un perfil por documento (`full`, `text`, `front-matter`, `asr`, `skip`). Caché por hash: solo reprocesa lo que cambió. Un documento que falla no detiene el lote. |
| `normalize.py` | Quita encabezados y pies repetidos, corrige la jerarquía de títulos, detecta títulos implícitos ("Ejercicio 3"), clasifica secciones (teoría, enunciado, resolución) y marca fórmulas dudosas, sin tocar el interior de las fórmulas. |
| `package.py` | Arma un paquete por tema con objetivos, fragmentos seleccionados por páginas asignadas y palabras clave, bibliografía, ejercicios de referencia, advertencias y faltantes. Sin embeddings ni búsqueda vectorial. |
| `validate.py` | Reporta errores de conversión, páginas perdidas, páginas sin texto, fórmulas dudosas, metadatos faltantes, duplicados, material sin clasificar y referencias inválidas de la matriz curricular. |
| `mathcheck.py` | Registro de comprobaciones (`@check`), igualdad simbólica y álgebra lineal exacta sobre $\mathbb{Z}_p$ (`gf_rref`, `gf_rank`, `gf_nullspace`, distancia de Hamming, etc.). |
| `qa.py` | Control del material publicado: cobertura de la matriz, páginas vacías, texto provisional, enunciados sin resolución, comprobaciones faltantes o fallidas, mínimos por unidad, enlaces internos, fórmulas mal delimitadas, notación prohibida y párrafos duplicados. |
| `cli.py` | Interfaz de línea de comandos. |

## Instalación

Requiere Python 3.10 o posterior. Se recomienda un entorno virtual dentro de esta carpeta
(ignorado por Git).

```sh
cd tools/content-pipeline
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"            # núcleo: PyYAML, SymPy y pytest
.venv/bin/pip install -e ".[dev,extract]"    # además Docling (descarga PyTorch y modelos)
.venv/bin/pip install -e ".[asr]"            # opcional: transcripción de audio y video
```

El extra `asr` necesita `ffmpeg` en el `PATH` (en macOS: `brew install ffmpeg`). La primera
extracción descarga los modelos de Docling; para trabajar sin red, descargarlos antes con
`docling-tools models download` y pasar `--artifacts-path`.

## Uso

Todos los comandos reciben `--subject <materia>` (nombre de la carpeta en `academic-sources/`) y
se ejecutan desde cualquier lugar del repositorio. Opciones comunes: `--sources-root`,
`--log-level`, `--log-format text|json` y `--log-file`.

```sh
alias cp-run='.venv/bin/content-pipeline'
cp-run inventory --subject algebra-ii                 # catálogo, hashes y duplicados
cp-run extract   --subject algebra-ii                 # Docling → Markdown + JSON (con caché)
cp-run normalize --subject algebra-ii                 # Markdown normalizado + índice de secciones
cp-run package   --subject algebra-ii --unit u3       # paquetes de contexto de una unidad
cp-run package   --subject algebra-ii --topic u3-markov
cp-run validate  --subject algebra-ii --strict        # reporte documental y curricular
cp-run run       --subject algebra-ii                 # todo lo anterior en orden
cp-run status    --subject algebra-ii                 # resumen del estado
cp-run verify-math --subject algebra-ii               # ejecuta checks/*.py con SymPy
cp-run qa        --subject algebra-ii                 # controla src/content/docs/algebra-ii
```

| Comando | Opciones propias |
|---|---|
| `inventory` | `--reclassify`: reaplica `subject.yaml` aunque el catálogo tenga correcciones manuales. |
| `extract` | `--ids a,b` · `--profile full\|text\|front-matter\|asr\|skip` · `--no-formulas` · `--force` · `--limit N` · `--device auto\|cpu\|mps\|cuda` · `--artifacts-path DIR` |
| `normalize` | `--ids a,b` · `--force` |
| `package` | `--unit ID` · `--topic ID` · `--budget CARACTERES` (por defecto 24000) |
| `validate` | `--strict` (sale con 1 si hay errores) · `--docs-root DIR` |
| `run` | `--force` · `--limit N` · `--device` · `--artifacts-path` · `--strict` |
| `verify-math` | `--ids a,b` · `--checks DIR` · `--report ARCHIVO` |
| `qa` | `--docs-root DIR` · `--report ARCHIVO` |

Códigos de salida: `0` correcto, `1` errores de validación, verificación o calidad, `2` error de
configuración (materia inexistente, YAML inválido, etc.).

### Agregar una materia

1. Crear `academic-sources/<materia>/raw/` y copiar los documentos (no se versionan).
2. Escribir `subject.yaml` con reglas `match` (comodines sobre la ruta relativa, sin distinguir
   mayúsculas ni acentos; `*` cruza carpetas; las reglas posteriores pisan a las anteriores):

   ```yaml
   id: mi-materia
   defaults: {license: privado-catedra, distribution: privado, extraction: full}
   rules:
     - match: "guias/*"
       doc_type: guia-practica
       source: Cátedra
       units: [u1]
     - match: "libros/*"
       doc_type: bibliografia
       extraction: front-matter
   ```

3. `inventory`, revisar `catalog.yaml` (los campos de clasificación se pueden corregir a mano) y
   `extract`.
4. Escribir `curriculum-map.yaml` (unidades, temas, objetivos, palabras clave, fuentes con
   páginas, página prevista) y generar los paquetes con `package`.

### Perfiles de extracción

| Perfil | Uso | Docling |
|---|---|---|
| `full` | Guías, apuntes, parciales | OCR si hace falta, tablas, fórmulas a LaTeX, figuras |
| `text` | Texto corrido | OCR y tablas, sin fórmulas (más rápido) |
| `front-matter` | Libros con derechos | Solo las primeras 30 páginas (portada, créditos, índice) |
| `asr` | Audio y video | Pipeline ASR (Whisper) |
| `skip` | Material fuera de alcance | No se procesa |

Un perfil también puede ser un mapa: `extraction: {profile: text, max_pages: 10}`.

## Verificación matemática

Cada archivo de `academic-sources/<materia>/checks/` registra funciones con `@check(id, ...)`. El
identificador coincide con el del ejercicio (`<!-- ejercicio: U1.07 | ... -->`) o con el marcador
de un ejemplo (`<!-- check: U1.T03.E2 -->`). Una comprobación falla si lanza una excepción;
`verify-math` escribe el reporte en `academic-sources/<materia>/reports/math-verification.json` y
`qa` exige que todo ejercicio o ejemplo marcado tenga una comprobación aprobada.

```python
import sympy as sp
from content_pipeline.mathcheck import check, require, same, gf_rank

@check("U1.07", "Base de un subespacio de matrices")
def _():
    A = sp.Matrix([[1, 2], [3, 4]])
    same(A.det(), -2, "determinante")
    require(gf_rank([[1, 1], [1, 1]], 2) == 1, "rango en Z2")
```

Las cuentas sobre cuerpos finitos usan aritmética modular exacta. SymPy no valida
demostraciones: las demostraciones se revisan aparte.

## Tests

```sh
.venv/bin/pytest -m "not integration"   # rápidos, sin Docling (los que corre CI)
.venv/bin/pytest -m integration         # extracción real con Docling (local)
```

Los fixtures se generan durante la prueba (un PDF mínimo válido, un DOCX mínimo, Markdown); no
hay documentos de cátedra en el repositorio. Los tests rápidos usan un motor de extracción falso
con la misma interfaz que Docling para cubrir caché, idempotencia y manejo de errores.

## Privacidad

- `raw/` y `processed/` están en `.gitignore`: los originales y todo lo que contiene fragmentos de
  ellos (Markdown, JSON, paquetes de contexto) son privados.
- `catalog.yaml` solo guarda rutas relativas a `raw/`, hashes, tamaños y clasificación. Que un
  archivo esté disponible localmente no implica permiso para publicarlo: la licencia se declara.
- Los reportes versionados (`reports/`) contienen resultados de verificación, no texto de las fuentes.

## Limitaciones conocidas

- La calidad del OCR de manuscritos es baja: las resoluciones escaneadas de alumnos se marcan para
  revisión y no se usan como fuente de resultados.
- El reconocimiento de fórmulas de Docling puede fallar en matrices y fracciones apiladas: esas
  regiones se marcan (`formula-no-decodificada`, `delimitadores-desbalanceados`) y deben
  contrastarse con la página original antes de usar un dato numérico.
- La estimación de páginas de un PDF sin dependencias falla con objetos comprimidos; en ese caso no
  se informa pérdida de páginas.
- La selección de fragmentos es por metadatos y palabras clave: un tema sin páginas asignadas ni
  palabras clave adecuadas puede quedar sin fragmentos (se informa como faltante).
