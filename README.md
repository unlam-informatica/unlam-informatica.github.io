# Ingeniería en Informática — UNLaM

Portal comunitario no oficial vinculado a la carrera Ingeniería en Informática de la UNLaM.

No pertenece a la Universidad Nacional de La Matanza ni representa comunicación institucional. Su objetivo es centralizar accesos a sitios de materias publicados en GitHub Pages dentro de la organización [`unlam-informatica`](https://github.com/unlam-informatica).

## Objetivo

Este repositorio no contiene el material completo de las materias. Funciona como índice principal para entrar rápidamente al sitio propio de cada materia.

Cada materia mantiene sus apuntes, prácticas y recursos en su repositorio correspondiente.

## Estructura

- **`index.md`** — página principal con las tarjetas de materias disponibles.
- **`_config.yml`** — configuración de Jekyll, GitHub Pages y just-the-docs.
- **`_sass/custom/`** — estilos propios del sitio.
- **`_includes/head_custom.html`** — include reservado para personalizaciones del `<head>`.
- **`assets/favicon/`** — favicons del sitio.

## Agregar una materia

Editar `index.md` y agregar una tarjeta dentro de `.subject-grid`:

```html
<a class="subject-card" href="https://unlam-informatica.github.io/nombre-del-sitio/">
	<span class="subject-card-kicker">1er año</span>
	<span class="subject-card-title">Nombre de la materia</span>
	<span class="subject-card-text">Descripción breve del material disponible.</span>
</a>
```

Usar URLs absolutas al sitio GitHub Pages de la materia y mantener descripciones breves.

## Desarrollo local

Instalar dependencias:

```bash
bundle install
```

Levantar el sitio:

```bash
bundle exec jekyll serve
```

URL local:

```text
http://localhost:4000/
```

## Publicación

El sitio se publica con GitHub Pages desde la rama `main`.

Al hacer push a `main`, GitHub Pages construye el sitio desde la raíz del repositorio.
