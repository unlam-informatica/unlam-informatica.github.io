# Plan de implementación — Pipeline académico y Álgebra II

Documento de seguimiento. Rama de trabajo: `feat/algebra-ii-pipeline`.
Última actualización: 2026-11-16 (sesión 1, interrumpida por límite de uso).

## Objetivos

- **A.** Pipeline Python reutilizable (`tools/content-pipeline/`) con Docling: ingesta,
  extracción, normalización, paquetes de contexto, validación y CLI.
- **B.** Materia completa de Álgebra y Geometría Analítica II (3645) en
  `src/content/docs/algebra-ii/`, integrada al portal.

## Estado por fase

| Fase | Estado | Detalle |
|------|--------|---------|
| 1. Auditoría | Hecha | Repo, tests, validaciones, fuentes y programa revisados. |
| 2. Pipeline | Iniciada | Solo `pyproject.toml` y `.gitignore`. Falta todo el código. |
| 3. Procesamiento | Bloqueada | Depende de instalar Docling (ver Bloqueos). |
| 4. Diseño de Álgebra II | No iniciada | Digestos de fuentes en curso (pueden estar incompletos). |
| 5. Generación académica | No iniciada | Ninguna página escrita. |
| 6. Integración web | No iniciada | Sidebar, navLinks, portada y tests sin tocar. |
| 7. Auditoría final | No iniciada | Sin PR. |

## Hallazgos verificados

- **Programa vigente:** `661_3645_AlgebrayGeometriaAnaliticaII.pdf`, año académico 2023,
  Dra. Marcela Falsetti. La ficha oficial de la materia ofrece un único programa
  (última modificación del PDF: 30/10/2023). No se encontró versión posterior.
- **Año de la materia:** el Plan 2023 ubica 3645 en **tercer año, primer cuatrimestre**
  (correlativa 3627). Debe agruparse bajo "3er año" en portada y sidebar.
- **Unidades del programa:** 1 Espacios vectoriales (incluye $\mathbb{Z}_2^n$, rango,
  códigos $(n,k)$, matriz de paridad); 2 Transformaciones lineales (incluye teorema
  fundamental); 3 Autovalores, semejanza, diagonalización, Markov y recurrencias;
  4 Espacios euclídeos (Gram-Schmidt, complemento ortogonal, proyecciones, producto
  interno en $\mathbb{Z}_2^n$, códigos autoduales, Hamming, cuadrados mínimos).
- **Bibliografía oficial:** Poole (4ta, 2017) y Lay (5ta, 2016) obligatorias; Grossman,
  Anton y Strang complementarias; Nakos–Joyner para códigos.
- **Fuentes en `academic-sources/algebra-ii/raw/`:** 64 PDF (incluido el programa
  descargado en `raw/programa/`), 4 DOCX, 5 JPG y 6 MP4; 431 MB. Hay material de un
  plan anterior (cónicas, ecuaciones diferenciales, matrices simétricas) fuera del
  programa 2023.
- **Convenciones del portal:** todo Markdown necesita `slug` explícito
  (`scripts/validate.mjs`); enunciados en `:::note[Enunciado]` y resoluciones en
  `:::tip[Resolución]`; los tests de Playwright tienen las materias fijas en arreglos
  que hay que ampliar.

## Decisiones arquitectónicas tomadas

- Docling como extra opcional `extract`; CI instala solo PyYAML, SymPy y pytest.
- Una entrada de catálogo por hash SHA-256 único; los duplicados se listan como rutas.
- Motor de extracción detrás de una interfaz para probar caché e idempotencia sin
  Docling; tests de integración reales marcados `integration`.
- Verificaciones SymPy por unidad en `academic-sources/algebra-ii/checks/`, con
  identificador por ejercicio y reporte versionado.

## Bloqueos

1. **PyPI inaccesible en esta red.** El DNS del proveedor resuelve
   `files.pythonhosted.org` a `127.9.9.9` (walled garden). No se pudo instalar Docling,
   SymPy, PyYAML ni pytest. No se esquivó el bloqueo: requiere decisión del responsable
   (cambiar DNS, o autorizar una resolución o índice alternativo).
2. Sin `ffmpeg` no se pueden transcribir los 6 MP4.

## Trabajo pendiente

Todo el código del pipeline, sus tests y README; procesamiento de fuentes; catálogo y
`curriculum-map.yaml`; las páginas de Álgebra II (repaso, cuatro unidades, guías,
simulacros); integración web; verificación matemática; CI de Python; Pull Request.

## Próxima acción exacta

1. Resolver el bloqueo 1 y ejecutar en `tools/content-pipeline/`:
   `uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python -e ".[dev,extract]"`.
2. Revisar `academic-sources/algebra-ii/processed/digests/` (digestos privados de
   lectura directa; verificar que estén completos antes de usarlos).
3. Implementar `ingest.py` y generar `catalog.yaml`.
