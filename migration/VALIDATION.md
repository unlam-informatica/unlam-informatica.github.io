# Validaciones ejecutadas

- `npm run build`: exitoso, 196 páginas generadas (195 de contenido + 404).
- `npm run validate`: 195 rutas de contenido únicas; 212 HTML incluyendo aliases;
  47.645 referencias internas; 245 entradas de compatibilidad; 50 recursos con
  SHA-256 conservado. Sin enlaces rotos, fragmentos internos faltantes ni errores KaTeX.
- `npm run test:browser`: **10 pruebas exitosas**, Chromium, escritorio e iPhone 13
  emulado. Portada, navegación por materia/unidad, menú móvil, búsqueda por materia,
  fórmulas, ancho responsive, redirección con query/fragmento y todos los diagramas.
- Capturas de portada en ambos tamaños revisadas visualmente.
- `git diff --check`: exitoso.
- `npm audit`: 5 avisos bajos, 0 moderados/altos/críticos (cadena KaTeX/Mermaid/remark).

Entorno local: Node 26.13.0, npm 11.20.0. CI usa Node 22 LTS. Las pruebas móviles
son emuladas en Chromium; no se ejecutaron en un dispositivo real ni en Safari.
No se ejecutó despliegue ni se validó el enrutamiento sobre producción.

Ver `README.md` de este directorio para problemas detectados, adaptaciones del
Markdown y condiciones necesarias para la transición de GitHub Pages.

La importación verifica automáticamente los 942 bloques de código contra los originales;
solo permite la adaptación documentada de horarios en Mermaid.

Preparación de producción: se cambió únicamente la fuente de Pages del portal
principal a GitHub Actions. HTTP 200 y SHA-256 del HTML idénticos antes y después;
registro en `pages-preparation.json`. Las publicaciones de materias se conservaron.

`node scripts/verify-production.mjs http://127.0.0.1:4322`: **357 comprobaciones
exitosas**, contra el build local servido con `python3 -m http.server` (redirección
de directorios como Pages). Comprueba rutas antiguas y canónicas, generador
Starlight, canonical, bytes de recursos y módulo Pagefind. No es una validación
del nuevo portal en producción: su despliegue sigue pendiente.

Tema Lucode: build de producción exitoso, 195 rutas únicas y 47.938 referencias
internas verificadas sin errores; matriz de 245 entradas y 50 recursos conservados.
Las 12 pruebas Playwright pasan en escritorio y móvil, incluyendo cambio de tema,
persistencia al recargar, navegación, búsqueda, fórmulas, todos los diagramas y
redirecciones. Capturas de portada y apunte en modo oscuro revisadas visualmente.
