# AGENTS.md

Guía para agentes que trabajen en este repositorio.

## Qué es este proyecto

Sitio web base de la carrera **Ingeniería en Informática — UNLaM**, publicado con **GitHub Pages** usando el tema **just-the-docs** (vía `remote_theme`).

El objetivo del sitio es funcionar como **portal de acceso centralizado** a los sitios propios de cada materia de la carrera, también publicados como GitHub Pages dentro de la organización `unlam-informatica`.

- Sitio publicado: `https://unlam-informatica.github.io/`
- Organización GitHub: `https://github.com/unlam-informatica`
- El contenido está en **español**.
- Este repositorio no contiene los apuntes completos de cada materia: solo enlaza a sus sitios específicos.

## Alcance del contenido

Este sitio debe mantenerse simple y orientado a navegación:

- Página principal con accesos claros a las materias disponibles.
- Cada materia debe enlazar a su propio sitio GitHub Pages.
- El texto de cada materia debe describir brevemente qué se encuentra en ese sitio, sin duplicar sus contenidos.
- Si una materia todavía no tiene sitio publicado, no agregarla como enlace activo salvo que se indique explícitamente.

No usar este repositorio para desarrollar teoría, prácticas, programas analíticos o material detallado de materias. Ese contenido corresponde al repositorio específico de cada materia.

## Materias enlazadas

Al agregar o modificar una materia, mantener consistencia con el patrón actual de tarjetas en `index.md`:

```html
<a class="subject-card" href="https://unlam-informatica.github.io/nombre-del-sitio/">
	<span class="subject-card-kicker">1er año</span>
	<span class="subject-card-title">Nombre de la materia</span>
	<span class="subject-card-text">Descripción breve del material disponible.</span>
</a>
```

Criterios:

- Usar el nombre oficial o más reconocible de la materia.
- Indicar el año o trayecto de forma breve en `subject-card-kicker`.
- Usar URLs absolutas a GitHub Pages.
- Mantener barras finales en URLs cuando el sitio las use.
- No inventar materias, años, códigos ni URLs si no están presentes en el repo o no fueron provistos por el usuario.

## Estructura del sitio

```text
_config.yml                         # Config Jekyll/just-the-docs
index.md                            # Home con tarjetas de materias
README.md                           # Descripción del portal
_sass/custom/*.scss                 # Overrides de estilo del tema
_includes/head_custom.html          # Include reservado para personalizaciones del head
assets/favicon/                     # Favicons del sitio
```

Este sitio no usa carpetas `unidad-N/`, `practicas/` ni `reference/` como los sitios de materias. Si aparecen en el futuro, revisar si realmente corresponden a este portal o si deberían vivir en otro repositorio.

## Cambios de sitio, layout y estilos

Antes de implementar cambios ad hoc sobre **layout, estilos, navegación, componentes, configuración del tema, Mermaid, callouts, tablas, código, búsqueda o cualquier comportamiento propio del sitio**, verificar primero si **Just the Docs** ya ofrece una forma oficial de hacerlo.

- Documentación oficial: <https://just-the-docs.com/>
- Preferir configuración del tema, includes documentados, variables Sass, componentes y extensiones soportadas por Just the Docs.
- Usar CSS o JavaScript propio solo cuando la documentación oficial no cubra el caso, cuando el mecanismo documentado no alcance, o cuando el cambio sea específico del sitio y esté justificado.
- Si se agrega una solución propia, mantenerla acotada, documentar brevemente por qué existe y evitar duplicar una capacidad nativa del tema.

## Navegación

- El **home** vive en `index.md` y usa `layout: minimal` para no mostrar sidebars.
- Mantener `nav_order: 1` para el home.
- Mantener `nav_enabled: false`, `search_enabled: false` y `AGENTS.md` dentro de `exclude` en `_config.yml`.
- Este portal debería tener muy pocas páginas. Evitar crear secciones internas salvo que agreguen valor real al índice de materias.
- Si se agregan páginas nuevas, usar frontmatter compatible con Just the Docs y mantener títulos en español.

## Diagramas e imágenes

- No agregar imágenes decorativas.
- Usar imágenes solo si ayudan a identificar la carrera, la universidad o la estructura de navegación.
- Si se necesita un diagrama o esquema editable, preferir Mermaid.
- Si Mermaid no aplica, usar SVG simple en `assets/img/` y referenciarlo desde Markdown.

## Convenciones de contenido

- **Idioma:** español.
- **Tono:** claro, directo y orientado a estudiantes.
- **Extensión:** breve. Este sitio es un índice, no un apunte.
- **Consistencia:** mantener nombres, años y descripciones con el mismo estilo entre materias.
- **Accesibilidad:** los enlaces deben tener texto descriptivo; evitar "clic acá" o URLs sueltas como texto principal.
- **No duplicar contenido:** cualquier explicación extensa de una materia debe ir en el sitio propio de esa materia.

## Callouts disponibles

Definidos en `_config.yml`: `note`, `important`, `warning`, `enunciado` y `resolucion`.

Para este portal, usar callouts con moderación. Los callouts `enunciado` y `resolucion` están disponibles en la configuración, pero normalmente corresponden mejor a sitios de materias o prácticas.

Uso:

```markdown
{: .note }
> Texto del callout.
```

## Desarrollo local

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000/
```

Publicación: push a `main`; GitHub Pages buildea desde la raíz.
