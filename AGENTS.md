# AGENTS.md

Portal personal de apuntes de Ingeniería en Informática — UNLaM. **No oficial**.

## Arquitectura

Astro Starlight, salida estática, sin backend. Contenido en español en
`src/content/docs/{materia}/`, Markdown para apuntes y MDX para la portada.
Recursos descargables e imágenes en `public/{materia}/`, con rutas conservadas.

## Edición

- Preservar contenido académico, fórmulas, código y bibliografía.
- Mantener los prefijos `analisis-matematico-i`, `bbdd-aplicadas` y `diseno-de-software`.
- Preferir componentes, navegación, búsqueda y configuración nativos de Starlight.
- Consultar https://starlight.astro.build/ antes de personalizar comportamientos.
- Callouts nativos: `:::note`, `:::tip`, `:::caution`, `:::danger` con título en español.
- Fórmulas inline `$...$`; bloques con `$$` en líneas separadas. Mermaid en cercos `mermaid`.
- No agregar imágenes decorativas ni inventar materias, años o material académico.
- Mantener visible el aviso de sitio personal y no oficial.
- No modificar los repositorios de origen para sincronizar este portal.

## Validación

```sh
npm ci
npm run build
npm run validate
npx playwright install chromium
npm run test:browser
```

`migration/` registra procedencia, hashes y compatibilidad. Al cambiar una ruta,
actualizar la matriz y conservar la ruta antigua. La importación es una herramienta
puntual: no reimportar sin revisar cambios locales.

## Publicación

GitHub Actions valida los PR. El despliegue es **manual**, solo desde `main`, con
`deploy.yml`; requiere Pages con fuente GitHub Actions. No publicar ni hacer merge
sin autorización explícita. Revisar el plan de transición en `migration/README.md`.
