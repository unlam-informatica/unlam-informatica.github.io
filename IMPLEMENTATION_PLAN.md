# Plan de implementación — Pipeline académico y Álgebra II

Documento de seguimiento. Rama: `feat/algebra-ii-pipeline`. Última actualización: 2026-11-17.

## Objetivos

- **A.** Pipeline Python reutilizable (`tools/content-pipeline/`) con Docling: ingesta,
  extracción, normalización, paquetes de contexto, validación, verificación matemática, QA y CLI.
- **B.** Materia completa de Álgebra y Geometría Analítica II (3645) en
  `src/content/docs/algebra-ii/`, integrada al portal.

## Estado por fase

| Fase | Estado |
|------|--------|
| 1. Auditoría | Hecha |
| 2. Pipeline | Hecha: 53 tests rápidos y 1 de integración con Docling pasan |
| 3. Procesamiento | Hecha con limitaciones (ver abajo): 57 documentos extraídos y normalizados, 41 paquetes |
| 4. Diseño | Hecha: `content-guide.md`, `curriculum-map.yaml`, `subject.yaml` |
| 5. Generación académica | Hecha: 69 páginas, 154 ejercicios, 2 simulacros |
| 6. Integración web | Hecha: sidebar, navegación superior, portada (3er año), laboratorio interactivo |
| 7. Auditoría final | Hecha: build, validate, Playwright, SymPy y QA en verde |

## Resultados verificados (2026-11-17)

- `npm run build`: 259 páginas. `npm run validate`: 258 páginas de contenido alcanzables desde la
  portada, 149 097 enlaces y recursos revisados, 0 errores.
- `npm run test:browser`: 32/32 (escritorio y móvil).
- `pytest -m "not integration"`: 53/53. `pytest -m integration` (Docling 2.150.1): 1/1.
- `content-pipeline verify-math --subject algebra-ii`: 328/328 comprobaciones (SymPy 1.14).
- `content-pipeline qa --subject algebra-ii`: 69 páginas, 154 ejercicios, 0 errores; 10 advertencias
  de notación, todas en avisos de equivalencia con la notación de los libros (permitidos).
- `content-pipeline validate --subject algebra-ii`: 0 errores; 547 advertencias, casi todas fórmulas
  no decodificadas por la pasada sin el modelo de fórmulas.
- Revisión de los 108 enunciados de teoremas, propiedades, lemas y corolarios: sin observaciones.

## Contenido

| Sección | Páginas | Ejercicios |
|---|---|---|
| Generales (presentación, programa, cómo estudiar, notación, laboratorio, bibliografía) | 6 | — |
| Repaso de Álgebra I | 6 | 20 |
| Unidad 1 (10 lecciones + presentación + 4 de práctica) | 15 | 30 |
| Unidad 2 (8 + 1 + 4) | 13 | 32 |
| Unidad 3 (8 + 1 + 4) | 13 | 31 |
| Unidad 4 (8 + 1 + 4) | 13 | 32 |
| Integradores y simulacros | 3 | 9 |

## Decisiones

- Programa 2023 (único publicado por el DIIT); materia de 3er año, 1er cuatrimestre.
- Notación de la cátedra con tabla de equivalencias con Poole y Lay.
- Resoluciones plegadas con `<details>`; fórmulas nunca dentro de etiquetas HTML.
- Figuras SVG en línea con colores por tokens de tema; un componente interactivo sin dependencias.
- Docling como extra opcional; CI corre los tests rápidos, `verify-math` y `qa`.
- Producción con subagentes: primero Opus, luego Sonnet (por indicación del responsable), con
  archivos exclusivos por agente e integración y revisión centralizadas.

## Limitaciones y pendientes reales

1. **Reconocimiento de fórmulas de Docling**: en esta máquina tarda más de 10 minutos para 22 páginas;
   el corpus se procesó con `--no-formulas`. Para los documentos clave: `content-pipeline extract
   --subject algebra-ii --ids <id>` sin la opción.
2. **Clases grabadas**: los MP4 fueron quitados de `raw/` (quedan registrados como ausentes); su
   transcripción requiere `ffmpeg` y el extra `asr`.
3. Los digestos privados de "otras fuentes" y de bibliografía quedaron parciales (prácticas resueltas
   de años anteriores y el mapa de Nakos y Joyner sin relevar).
4. Lay (5.ª ed.) no está disponible localmente: se cita sin secciones ni páginas. Poole se citó con la
   3.ª ed. (el programa pide la 4.ª).
5. El job `pipeline` de CI no se ejecutó todavía en GitHub Actions.
6. Merge y despliegue: fuera del alcance autorizado.
