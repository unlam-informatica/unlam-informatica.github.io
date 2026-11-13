# Migración a portal unificado

## Arquitectura

Astro 7 y Starlight 0.42 generan HTML estático para el dominio raíz de GitHub Pages.
`src/content/docs/` contiene las tres materias en Markdown. La portada MDX usa
`CardGrid` y `LinkCard` nativos, agrupados según los años del portal anterior.

Starlight gestiona sidebar, índice contextual, paginación, tema, accesibilidad y
menú móvil. Pagefind indexa todas las materias durante el build y busca localmente.
No hay backend, base de datos, CDN de ejecución ni servicios pagos.

KaTeX se ejecuta en el build mediante remark-math/rehype-katex, con CSS y fuentes
locales. Los diagramas siguen editándose como cercos Mermaid y se renderizan con
un bundle local cargado solo en páginas que contienen diagramas. Starlight no
incluye renderizador Mermaid: esa extensión y el aviso no oficial del footer son
las personalizaciones funcionales. El footer delega el resto en el componente
nativo. El CSS solo contiene desbordes de fórmulas y diagramas.

## Procedencia y conservación

`sources.json` registra los commits de origen y hashes SHA-256 de cada página y
recurso. Se importaron 85 páginas de Análisis, 85 de BBDD y 24 de Diseño, además de
50 recursos (imágenes y archivos de trabajo/descarga). No se escribieron cambios
en los repositorios de materias. Los archivos académicos siguen en Markdown;
no se resume ni se reescribe teoría, ejercicios, código o bibliografía.

Se excluyen instrucciones de agentes, README de repositorio, estilos, scripts de
navegación de Jekyll y directorios que el `_config.yml` original excluía. Se
conservan los archivos de entrada publicados, incluso cuando no están enlazados.
El registro de origen permite recuperar exactamente cada original desde su commit.

`node scripts/import-sources.mjs /ruta/a/clones` reproduce la importación desde
copias locales. No es sincronización automática: ejecutarlo sobrescribe páginas
migradas y requiere revisar el diff. Usar los commits registrados para reproducir
la misma versión. No ejecutar sobre clones más nuevos sin revisar cambios.

## Diferencias de Markdown revisadas

- Se reemplaza frontmatter Jekyll por `title`, `slug` y orden de sidebar Starlight.
- El H1 inicial conserva su texto como título de página para evitar duplicarlo.
- Callouts `note`, `important`, `warning`, `enunciado` y `resolucion` se traducen a
  asides nativos con títulos españoles. El texto del bloque se conserva.
- `relative_url` se resuelve al prefijo de materia; `raw`/`endraw` dejan de ser necesarios.
- Atributos Kramdown de presentación se retiran: las tablas e imágenes usan el tema.
- Los delimitadores de fórmulas de bloque `$$` pasan a líneas separadas, como exige
  remark-math. Se adapta el escape de signo monetario sin cambiar su significado.
- Un adaptador de AST corrige el escape Kramdown de separadores de columna en LaTeX
  dentro de tablas, conservando la fuente Markdown.
- Se corrigen enlaces internos heredados sin prefijo de materia y referencias
  relativas que omitían `teoria/`. Se agrega el ancla faltante
  `el-problema-sin-aislamiento` a su texto original, sin cambiar la jerarquía.
- Se cambia `10:00` por `10h00` (y los otros horarios del mismo diagrama) en una
  línea de tiempo: Mermaid interpreta los dos puntos como separadores de eventos.
  Se conservan los horarios y los objetivos RPO/RTO.
- El código inline que menciona Liquid como explicación académica permanece literal.

## Compatibilidad de URLs

`compatibility.md` y `compatibility.json` son la matriz verificable de páginas y
recursos. Los slugs mantienen el prefijo de materia y el permalink anterior,
normalizando a barra final. Las URLs antiguas `.html` tienen archivos HTML de
compatibilidad: canonical, enlace accesible, meta refresh y script que conserva
query y fragmento. GitHub Pages no permite respuestas 301 configurables; por eso
se usan redirecciones estáticas. Las URLs de directorio sin barra final dependen
de la normalización del host. Las imágenes/descargas mantienen sus rutas y bytes.

El chequeo comprueba archivos de salida y fragmentos de enlaces internos. Las
URLs externas no se validan por red. No se garantiza cada fragmento externo
histórico generado por Kramdown: Starlight usa otro generador de IDs. Los enlaces
internos existentes sí se verifican contra los IDs renderizados.

## Validación

```sh
npm ci
npm run build
npm run validate
npx playwright install chromium
npm run test:browser
```

`validation.json` contiene el resultado de enlaces, recursos, rutas únicas,
compatibilidad y errores KaTeX. Playwright prueba escritorio y viewport iPhone 13
con Chromium: portada, navegación, menú móvil, búsqueda de las tres materias,
fórmulas, desborde horizontal, redirecciones y todos los diagramas Mermaid.
La emulación móvil no sustituye una revisión en hardware real con Safari.
Los reportes de navegador se generan en `playwright-report/` y CI los adjunta.

## Despliegue y transición pendiente

La fuente de Pages del portal principal ya está configurada en **GitHub Actions**,
antes del merge. Se verificó que el HTML publicado sigue idéntico al anterior.
Los sitios de materias continúan publicados hasta que el portal nuevo esté listo.
No se ejecutó deploy ni se hizo merge.

Ver la [guía operativa de producción](PRODUCCION.md) para el orden exacto:
revisión/merge por el responsable → despliegue manual desde main → retiro de Pages
de materias → verificación pública de rutas/recursos y revisión en navegador.
La configuración anterior está en `pages-before-cutover.json`; el cambio ya
realizado y su comprobación están en `pages-preparation.json`.

## Riesgos registrados

- La coexistencia con Pages de los repositorios de materias debe resolverse antes
  de afirmar que producción sirve un único portal; requiere coordinación de rollout.
- Mermaid se renderiza con JavaScript: el diagrama conserva su fuente legible sin JS.
  Su bundle genera una advertencia de tamaño de Vite y se carga bajo demanda.
- npm audit detecta cinco avisos de severidad baja en la cadena KaTeX/Mermaid/remark.
  No hay avisos moderados, altos ni críticos en la instalación validada. Actualizar
  la cadena con una revisión específica evita forzar versiones mayores transitivas.
- Revisar visualmente futuros cambios en fórmulas, diagramas y tablas anchas.

Referencias oficiales consultadas: [contenido Markdown](https://starlight.astro.build/guides/authoring-content/),
[sidebar](https://starlight.astro.build/guides/sidebar/) y
[GitHub Pages con Astro](https://docs.astro.build/en/guides/deploy/github/).
