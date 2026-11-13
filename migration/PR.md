El portal Jekyll enlazaba tres sitios separados. Esta migración reúne sus apuntes en un único sitio estático Astro Starlight, con portada por año, búsqueda global, navegación por materia/unidad y aviso visible de sitio personal no oficial de la UNLaM.

## Arquitectura y cambios

- 194 páginas académicas importadas (85 Análisis, 85 BBDD, 24 Diseño), más portada MDX, conservando Markdown y los prefijos públicos de cada materia.
- 50 recursos originales preservados byte a byte: imágenes, PDF, ZIP, SQL, CSV y JSON. Commits de origen y hashes en `migration/sources.json`.
- Starlight nativo para tarjetas, sidebar, índice contextual, menú móvil, temas, búsqueda Pagefind y asides.
- Fórmulas con KaTeX durante build; Mermaid local bajo demanda. Se retiran configuración, estilos e includes Jekyll.
- Matriz de 245 rutas de páginas/recursos y aliases estáticos para URLs `.html`, conservando consultas y fragmentos.
- GitHub Actions valida PRs y prepara despliegue Pages **manual, exclusivamente desde main**. No se ejecutó ningún deploy. Como preparación posterior, Pages del portal se cambió a GitHub Actions antes del merge; su HTML publicado se verificó idéntico.
- Se actualizan README y AGENTS.md al nuevo alcance. Importador reproducible que solo lee clones de las materias.

## Validaciones ejecutadas

- Build de producción exitoso: 196 páginas (195 contenido + 404).
- Sin rutas duplicadas, enlaces internos rotos ni errores KaTeX. 47.645 referencias verificadas.
- Matriz completa comprobada contra salida estática; 50 recursos con hashes idénticos en origen/importación/build.
- **10 pruebas Playwright exitosas** en escritorio y viewport iPhone 13 con Chromium: navegación, menú móvil, búsqueda de las tres materias, fórmulas, overflow, aliases con query/fragmento y renderizado de todos los Mermaid.
- Capturas de portada revisadas en escritorio y móvil; `git diff --check` exitoso.
- Entorno local Node 26.13.0/npm 11.20.0; CI configurado con Node 22 LTS. La ejecución remota de CI queda visible en este PR.

## Problemas detectados y resueltos

- Enlaces heredados sin prefijo de materia o con rutas relativas incompletas; ancla faltante en BBDD.
- Sintaxis Liquid y atributos Kramdown reemplazados por mecanismos Starlight.
- Diferencias MathJax/remark-math: bloques `$$` en líneas separadas, signo monetario y escape de separador de columnas LaTeX en tablas.
- Línea de tiempo Mermaid con horarios `10:00` interpretados como separadores de eventos: se usa `10h00`, conservando horarios y objetivos RPO/RTO.
- No se cambian resoluciones académicas, fórmulas, código de ejercicios ni bibliografía. La revisión de diferencias de Markdown está documentada en `migration/README.md`.

## Riesgos y transición pendiente

- Los Pages de los repositorios de materias todavía pueden tener prioridad sobre los mismos prefijos del sitio raíz. Antes de producción hace falta coordinar su configuración de publicación en una acción posterior autorizada. **No se modificó ninguno de esos repositorios.**
- Pages del portal ya está configurado en GitHub Actions. Tras el merge por el responsable, ejecutar el despliegue manual y recién después desactivar los Pages anteriores de materias. Ver `migration/PRODUCCION.md`. No se hizo merge ni se ejecutó despliegue.
- Fragmentos externos históricos Kramdown no conocidos no tienen garantía exhaustiva; todos los fragmentos de enlaces internos sí se comprobaron. Las URLs externas no se verificaron por red.
- Redirecciones estáticas con meta refresh/script: GitHub Pages no ofrece 301 configurables. La normalización de directorios sin barra final depende del host.
- npm audit informa 5 avisos bajos en la cadena KaTeX/Mermaid/remark; sin avisos moderados, altos ni críticos. Mermaid produce advertencia de bundle grande, cargado solo en páginas con diagramas.
- Móvil probado por emulación Chromium; Safari/hardware real y verificación final sobre el dominio quedan pendientes de la transición.

Documentación detallada: `migration/README.md`, `migration/compatibility.md`, `migration/validation.json` y `migration/VALIDATION.md`.

La importación verifica automáticamente los 942 bloques de código contra los originales;
solo permite la adaptación documentada de horarios en Mermaid.

Guía operativa y comandos de verificación/reversión: `migration/PRODUCCION.md`. Estado anterior y preparación realizada: `migration/pages-before-cutover.json` y `migration/pages-preparation.json`.

El verificador público `scripts/verify-production.mjs` se ensayó contra el build local con normalización de directorios: 357 comprobaciones sin errores. No se ejecutó el despliegue del portal nuevo.
