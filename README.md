# Apuntes de Informática — UNLaM

Portal personal de apuntes, teoría y ejercicios. **No es un sitio oficial de la Universidad Nacional de La Matanza.**

Destino: https://unlam-informatica.github.io/

- 1er año: Análisis Matemático I.
- 2do año: Bases de Datos Aplicadas.
- 3er año: Diseño de Software.

Astro Starlight con el tema [Lucode](https://lucas-labs.github.io/lucode-starlight-theme/)
genera un sitio estático con búsqueda global Pagefind, navegación
contextual, modo claro/oscuro y menú móvil. No requiere backend ni servicios pagos.

La navegación enlaza los archivos `index.html` de cada apunte para evitar respuestas
404 de directorio retenidas por la caché de GitHub Pages. Se conservan las URLs
canónicas con barra final y las rutas históricas. Búsqueda, tarjetas y menús usan
el mismo destino; no hay que modificar los enlaces de los Markdown académicos.

Los menús usan nombres legibles y unidades en orden numérico. Cada unidad de BBDD
contiene solo las carpetas `teoria/` y `practica/`, con una presentación e índices
de apuntes en cada sección. El menú móvil también permite abrir los grupos
anidados de las tres materias; las rutas anteriores de BBDD se conservan.

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
