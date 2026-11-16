# Plan de implementación — Pipeline académico y Álgebra II

Documento de seguimiento. Rama de trabajo: `feat/algebra-ii-pipeline`.
Última actualización: 2026-11-16 (sesión 1, segunda parte).

## Objetivos

- **A.** Pipeline Python reutilizable (`tools/content-pipeline/`) con Docling: ingesta,
  extracción, normalización, paquetes de contexto, validación, verificación matemática, QA y CLI.
- **B.** Materia completa de Álgebra y Geometría Analítica II (3645) en
  `src/content/docs/algebra-ii/`, integrada al portal.

## Estado por fase

| Fase | Estado | Detalle |
|------|--------|---------|
| 1. Auditoría | Hecha | Repo, tests, validaciones, fuentes y programa revisados. |
| 2. Pipeline | Código y tests escritos; **sin ejecutar** | Falta instalar dependencias (bloqueo 1) para correr pytest. |
| 3. Procesamiento | Bloqueada | Docling no se puede instalar (bloqueo 1). Lectura directa de fuentes en digestos privados como alternativa. |
| 4. Diseño de Álgebra II | Hecha | `content-guide.md`, `curriculum-map.yaml`, `subject.yaml`, estructura de slugs y navegación. |
| 5. Generación académica | En curso | Páginas generales escritas; teoría de repaso y unidades 1–4 en redacción; práctica y simulacros pendientes. |
| 6. Integración web | En curso | Sidebar, navegación superior, portada y estilos de figuras listos; tests de navegador pendientes. |
| 7. Auditoría final | No iniciada | |

## Archivos principales

- Pipeline: `tools/content-pipeline/` (`src/content_pipeline/{config,io_utils,logging_utils,ingest,extract,normalize,package,validate,mathcheck,qa,cli}.py`, `tests/`, `README.md`).
- Materia: `academic-sources/algebra-ii/{subject.yaml,curriculum-map.yaml,content-guide.md,checks/}`.
- Sitio: `src/content/docs/algebra-ii/`, `src/config/sidebar.mjs`, `astro.config.mjs`,
  `src/content/docs/index.mdx`, `src/styles/custom.css`.
- CI: job `pipeline` en `.github/workflows/validate.yml` (pytest rápido, verify-math, qa).

## Hallazgos verificados

- **Programa vigente:** 2023 (PDF del DIIT, modificado el 30/10/2023; es el único de la ficha oficial).
- **Ubicación:** 3er año, 1er cuatrimestre (Plan 2023), correlativa 3627.
- **Fuentes:** 64 PDF, 4 DOCX, 5 JPG, 6 MP4 (431 MB). Duplicados exactos: 6 pares (ver catálogo
  cuando se genere). Los tres `EDA*.docx` son fotos de resoluciones manuscritas de alumnos.
- **Huecos de las fuentes de cátedra:** cadenas de Markov, producto en ℤ₂ⁿ y códigos autoduales no
  aparecen en ninguna guía; se redactan desde la bibliografía (Poole 3.ª ed.).
- **Bibliografía local:** Poole 3.ª ed. (el programa pide la 4.ª); Lay no está disponible.

## Decisiones

- Docling como extra opcional `extract`; CI instala solo PyYAML, SymPy y pytest.
- Notación de la cátedra en todo el sitio, con equivalencias de libros en `/algebra-ii/notacion/`.
- Resoluciones plegadas con `<details>` (probado: KaTeX y avisos renderizan dentro).
- Figuras en SVG en línea con colores por clase (`.math-figure` en `custom.css`), claro y oscuro.
- Producción paralela por agentes con propiedad exclusiva de archivos; checks SymPy por archivo.

## Bloqueos

1. **PyPI inaccesible.** El DNS del proveedor resuelve `files.pythonhosted.org` a `127.9.9.9`
   (walled garden). El responsable eligió corregir la red; no se esquivó el bloqueo. Sin esto no se
   pueden instalar Docling, SymPy, PyYAML ni pytest.
2. Sin `ffmpeg` no se pueden transcribir los MP4.

## Próxima acción exacta

1. Al resolverse el bloqueo 1: en `tools/content-pipeline/`,
   `python3 -m venv .venv && .venv/bin/pip install -e ".[dev,extract]"`, correr pytest,
   `content-pipeline run --subject algebra-ii`, revisar catálogo y paquetes.
2. Integrar la teoría de los agentes, lanzar prácticas y simulacros, `verify-math`, `qa`, build y tests.
