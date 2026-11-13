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
