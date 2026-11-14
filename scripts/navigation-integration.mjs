import fs from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { load } from 'cheerio';
import * as pagefind from 'pagefind';
import { navigationHref, navigationPath } from './navigation.mjs';

export default function navigationIntegration() {
  let config;
  return {
    name: 'portal-navigation',
    hooks: {
      'astro:config:done': ({ config: resolved }) => { config = resolved; },
      'astro:build:done': async ({ dir, logger }) => {
        const matrix = JSON.parse(await fs.readFile(new URL('migration/compatibility.json', config.root), 'utf8'));
        const files = (await fs.readdir(dir, { recursive: true })).filter(file => file.endsWith('.html'));
        const routes = new Map();
        const searchPages = [];
        for (const file of files.filter(file => file.endsWith('index.html'))) {
          const canonical = '/' + file.slice(0, -'index.html'.length);
          routes.set(canonical, navigationPath(canonical));
          routes.set(canonical.replace(/\/$/, ''), navigationPath(canonical));
        }
        for (const entry of matrix.filter(entry => entry.kind === 'page')) {
          const destination = navigationPath(entry.canonical);
          for (const route of [entry.old, entry.canonical, entry.canonical.replace(/\/$/, '')]) {
            routes.set(route, destination);
          }
        }
        for (const file of files) {
          const location = new URL(file, dir);
          const html = await fs.readFile(location, 'utf8');
          const $ = load(html);
          const base = new URL(file.replace(/index\.html$/, ''), config.site);
          let changed = false;
          $('a[href]').each((_, element) => {
            const before = $(element).attr('href');
            const after = navigationHref(before, base, routes);
            if (after !== before) {
              $(element).attr('href', after);
              changed = true;
            }
          });
          // Legacy .html redirects must also avoid a cached directory 404.
          const refresh = $('meta[http-equiv="refresh"]');
          if (refresh.length) {
            const canonical = $('link[rel="canonical"]').attr('href');
            const destination = navigationHref(canonical, base, routes);
            refresh.attr('content', '0;url=' + destination);
            let script = $('script').first();
            if (!script.length) script = $('<script>').appendTo('body');
            script.text(`location.replace(${JSON.stringify(destination)}+location.search+location.hash)`);
            $('html').attr('lang', 'es');
            $('title').text('Página trasladada');
            $('a').first().text('Continuar al apunte');
            $('html').attr('data-pagefind-ignore', 'all');
            changed = true;
          }
          if (changed) await fs.writeFile(location, $.html());
          if (file.endsWith('index.html') && $('[data-pagefind-body]').length) {
            searchPages.push({ url: '/' + file, content: changed ? $.html() : html });
          }
        }
        // Starlight's search UI is retained. Its built-in indexer does not expose
        // keepIndexUrl, so build the index once here with Pagefind's native option.
        const check = response => {
          if (response.errors.length) throw new Error(response.errors.join('\n'));
          return response;
        };
        try {
          const { index } = check(await pagefind.createIndex({ keepIndexUrl: true }));
          // Index real notes only; unit directory redirects must not appear as
          // duplicate search results after their content has been consolidated.
          for (const page of searchPages) check(await index.addHTMLFile(page));
          check(await index.writeFiles({ outputPath: fileURLToPath(new URL('pagefind/', dir)) }));
          logger.info(`Navigation prepared; ${searchPages.length} pages indexed with explicit index.html URLs.`);
        } finally {
          await pagefind.close();
        }
      },
    },
  };
}
