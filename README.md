# Apuntes de Informática — UNLaM

Portal personal de apuntes, teoría y ejercicios. **No es un sitio oficial de la Universidad Nacional de La Matanza.**

Destino: https://unlam-informatica.github.io/

- 1er año: Análisis Matemático I.
- 2do año: Bases de Datos Aplicadas.
- 3er año: Diseño de Software.

Astro Starlight genera un sitio estático con búsqueda global Pagefind, navegación
contextual, modo claro/oscuro y menú móvil. No requiere backend ni servicios pagos.

## Desarrollo

Node.js 22.23.4+ y npm. Las versiones resueltas están fijadas en `package-lock.json`.

```sh
npm ci
npm run dev -- --foreground
npm run build
npm run validate
npx playwright install chromium
npm run test:browser
```

La documentación está en `src/content/docs/`; los recursos se conservan bajo
`public/`. La portada usa tarjetas nativas de Starlight. Mermaid se sirve localmente
y KaTeX genera las fórmulas en el build.

Ver [arquitectura, migración y transición](migration/README.md),
[matriz de URLs](migration/compatibility.md) e [informe de validación](migration/validation.json).

## Publicación controlada

Los PR ejecutan validaciones sin desplegar. `Deploy portal (manual)` solo se puede
ejecutar sobre `main`. Antes del primer despliegue hay que configurar Pages para
GitHub Actions y resolver los sitios de proyecto que comparten prefijos; consultar
el plan de transición. Esta migración no publica ni modifica los repositorios de materias.
