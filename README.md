# Apuntes de Informática — UNLaM

Portal personal de apuntes, teoría y ejercicios. **No es un sitio oficial de la Universidad Nacional de La Matanza.**

Destino: https://unlam-informatica.github.io/

- 1er año: Análisis Matemático I.
- 2do año: Bases de Datos Aplicadas.
- 3er año: Diseño de Software.

Astro Starlight con el tema [Lucode](https://lucas-labs.github.io/lucode-starlight-theme/)
genera un sitio estático con búsqueda global Pagefind, navegación
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
`public/`. La portada usa tarjetas nativas de Starlight y el contenedor de Lucode. Mermaid se sirve localmente
y KaTeX genera las fórmulas en el build.

Ver [arquitectura, migración y transición](migration/README.md),
[guía de producción](migration/PRODUCCION.md),
[matriz de URLs](migration/compatibility.md) e [informe de validación](migration/validation.json).

## Publicación controlada

Los PR ejecutan validaciones sin desplegar. `Deploy portal (manual)` solo se puede
ejecutar sobre `main`. Pages del portal ya está preparado para GitHub Actions.
Después del primer
despliegue hay que retirar las publicaciones anteriores de materias que comparten
prefijos; consultar la guía de producción. Sus archivos e historial se conservan.

## Tema visual

[Lucode Starlight](https://lucas-labs.github.io/lucode-starlight-theme/) se integra
como plugin en `astro.config.mjs`. Se usa su apariencia predeterminada, navegación
superior por materia, portada `banner` y modos claro/oscuro. El esquema de contenido
extiende `ExtendDocsSchema`, como indica la documentación del tema.

El footer local delega su aspecto y paginación al componente de Lucode. Solo agrega
el aviso de sitio no oficial en los apuntes y conserva la carga local de Mermaid;
el aviso de la portada se configura mediante `footerText`. Los estilos propios
siguen limitados a contener contenido académico ancho y presentar ese aviso.
