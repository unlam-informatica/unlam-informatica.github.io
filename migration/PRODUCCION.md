# Publicación del portal unificado

El contenido ya está integrado en `unlam-informatica/unlam-informatica.github.io`.
Los repositorios de materias se conservan como historial; el portal no los consulta
al compilar ni al navegar.

## Preparación realizada

- PR [#1](https://github.com/unlam-informatica/unlam-informatica.github.io/pull/1)
  en draft, rama `feat/unified-starlight-portal`.
- Build, validación de enlaces/rutas/recursos y pruebas de navegador exitosos.
- Configuración y commits anteriores registrados en `pages-before-cutover.json`.
- Fuente de Pages del portal principal cambiada de `legacy` (Jekyll desde `main`)
  a `workflow` (GitHub Actions), antes del merge. Consultar `pages-preparation.json`
  para el resultado de la operación y la comprobación de disponibilidad.
- No se hizo merge, no se ejecutó deploy y no se desactivaron las materias.

## 1. Revisar y mergear el PR

Verificar el último CI verde y revisar los cambios académicos y la matriz
`compatibility.md`. Marcar el PR como listo y hacer merge cuando se apruebe.
Esta acción sigue reservada al responsable del repositorio.

La fuente de Pages debe permanecer en **GitHub Actions**. No volver a
`Deploy from a branch`: el contenido nuevo requiere el build de Astro.

El merge no publica el portal: el workflow de despliegue solo acepta ejecución manual.

## 2. Desplegar desde main

En el repositorio principal:

1. Abrir **Actions → Deploy portal (manual) → Run workflow**.
2. Seleccionar **main**.
3. Esperar que los jobs `build` y `deploy` terminen correctamente.
4. Si `github-pages` requiere aprobación, revisar y aprobar ese deployment.
5. Abrir https://unlam-informatica.github.io/ y confirmar la portada nueva.

Alternativa con GitHub CLI, después del merge:

```sh
gh workflow run deploy.yml --repo unlam-informatica/unlam-informatica.github.io --ref main
gh run list --repo unlam-informatica/unlam-informatica.github.io --workflow deploy.yml --limit 3
```

Revisar la ejecución creada en el paso anterior. Si falla, conservar las publicaciones
de materias mientras se resuelve. No retirarlas antes de un deployment raíz exitoso.

## 3. Retirar las publicaciones anteriores de materias

Hacerlo después del deployment raíz exitoso, dentro de la misma ventana de transición.
Hasta entonces puede verse una mezcla del portal nuevo y sitios anteriores.

Abrir **Settings → Pages** en cada uno:

- https://github.com/unlam-informatica/analisis-matematico-i/settings/pages
- https://github.com/unlam-informatica/bbdd-aplicadas/settings/pages
- https://github.com/unlam-informatica/diseno-de-software/settings/pages

En sitios publicados desde rama, seleccionar **Source → Deploy from a branch →
Branch: None → Save**, para deshabilitar Pages. Si la interfaz ofrece únicamente
**Unpublish site**, recordar que despublicar conserva la configuración y un push
posterior podría volver a publicarlo: también hay que desactivar la fuente.

Alternativa por API para deshabilitar la configuración del sitio Pages:

```sh
gh api --method DELETE repos/unlam-informatica/analisis-matematico-i/pages
gh api --method DELETE repos/unlam-informatica/bbdd-aplicadas/pages
gh api --method DELETE repos/unlam-informatica/diseno-de-software/pages
```

Estos endpoints eliminan el sitio/configuración de Pages, **no el repositorio,
los archivos ni el historial Git**. Revisar antes que no haya workflows de esos
repositorios que creen o desplieguen Pages por su cuenta. Esta migración no agrega
ninguno en ellos.

Comprobar que `gh api repos/unlam-informatica/NOMBRE/pages` devuelve `404` tras
deshabilitar Pages; debe hacerse con la misma cuenta que antes podía consultarlo,
para distinguir ausencia de sitio de un problema de permisos.

La propagación de cambios puede demorar; una respuesta vieja inmediatamente después
de la operación no implica necesariamente que falló. No borrar los repositorios.

## 4. Verificar producción

Desde el checkout del portal, con dependencias instaladas:

```sh
node scripts/verify-production.mjs
```

El verificador comprueba cada página con `Accept-Encoding: identity` y `gzip` e
incluye los destinos `index.html` registrados en la matriz. Informa `x-cache`,
`age` y el nodo de caché al fallar, para detectar respuestas diferentes como el
404 de BBDD del 13 de noviembre de 2026. Una respuesta 200 sin compresión no basta
para dar una ruta por verificada.

Para verificar solo los destinos usados por el portal, recursos y búsqueda,
sin incluir las direcciones antiguas que puedan seguir retenidas en caché:

```sh
npm run verify:production -- --navigation-only
```

El modo predeterminado sigue siendo estricto e incluye las rutas antiguas y
canónicas. Los cambios en una rama no alteran producción: requieren revisión,
merge autorizado y despliegue manual desde `main`.

El comando solo lee el sitio público. Recorre las rutas antiguas y canónicas de la
matriz, comprueba que las páginas canónicas sirven Starlight, sus enlaces canonical,
los hashes SHA-256 de los recursos originales y la disponibilidad del módulo de
búsqueda Pagefind. Sale con error si detecta diferencias. No crea archivos remotos.

Para ensayarlo localmente, servir `dist/` con un servidor estático que redirija
directorios sin barra final, como GitHub Pages. El preview de Astro con
`trailingSlash: always` responde 404 a esas rutas y no reproduce esa normalización.

Completar la revisión en navegador:

- Portada con tres materias y aviso visible de sitio personal no oficial.
- Cada materia abre Starlight, con navegación por unidades/temas y menú móvil.
- Buscar `derivada`, `transacciones` y `patrones`; abrir sus resultados.
- Comprobar fórmulas de Análisis y diagramas de BBDD/Diseño.
- Descargar un PDF y un archivo de práctica.
- Abrir una URL antigua `.html` con query/fragmento y verificar que se conserva.
- Revisar al menos un teléfono real/Safari además de las pruebas emuladas.

Registrar el deployment y los resultados. Las anclas históricas externas no
inventariadas y enlaces externos siguen siendo los límites documentados del chequeo.

## Reversión

**Si aún no se hizo merge:** restaurar Pages del portal a `legacy`, rama `main`,
raíz `/`, con la configuración registrada en `pages-before-cutover.json`.

```sh
gh api --method PUT repos/unlam-informatica/unlam-informatica.github.io/pages \
  -f build_type=legacy -f 'source[branch]=main' -f 'source[path]=/'
```

**Si ya se hizo merge/despliegue:** no configurar Jekyll sobre el `main` migrado.
Crear una rama de recuperación desde el commit previo del portal registrado en
`pages-before-cutover.json`, y configurar Pages con `build_type=legacy`, esa rama y
ruta `/`. Así se recupera el sitio anterior sin reescribir `main`. Otra alternativa
es revertir el PR mediante el flujo normal de revisión antes de restaurar la fuente.

Para recuperar Pages de una materia cuya configuración se eliminó, crear el sitio
con sus valores previos (`legacy`, `main`, `/` en el registro actual):

```sh
# Sustituir NOMBRE por el repositorio que se quiera restaurar.
gh api --method POST repos/unlam-informatica/NOMBRE/pages \
  -f build_type=legacy -f 'source[branch]=main' -f 'source[path]=/'
```

Restaurar su publicación desde Settings o mediante un nuevo build Jekyll si es
necesario. Confirmar su URL antes de dar la reversión por terminada.

## Referencias oficiales

- [Configurar la fuente de publicación](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [API de Pages: cambiar fuente o eliminar un sitio](https://docs.github.com/en/rest/pages/pages)
- [Despublicación y reactivación](https://docs.github.com/en/pages/getting-started-with-github-pages/unpublishing-a-github-pages-site)
