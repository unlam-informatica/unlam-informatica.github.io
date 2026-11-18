import { test, expect } from '@playwright/test';
import { load } from 'cheerio';
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const subjects = ['analisis-matematico-i', 'bbdd-aplicadas', 'diseno-de-software', 'algebra-ii'];
const walk = (dir: string): string[] => readdirSync(dir, { withFileTypes: true }).flatMap(entry =>
  entry.isDirectory() ? walk(join(dir, entry.name)) : [join(dir, entry.name)]);
const destinations = new Set(walk('dist').filter(file => file.endsWith('/index.html') && load(readFileSync(file, 'utf8'))('[data-pagefind-body]').length)
  .map(file => file === 'dist/index.html' ? '/' : '/' + file.slice(5)));

test('todas las páginas se alcanzan siguiendo enlaces desde la portada', async ({ request, baseURL }) => {
  test.setTimeout(120000);
  const reached = new Set(['/']);
  const queue = ['/'];
  while (queue.length) {
    const current = queue.shift()!;
    const response = await request.get(current, { headers: { 'Accept-Encoding': 'gzip' } });
    expect(response.status(), current).toBe(200);
    const $ = load(await response.text());
    expect($('meta[name="generator"][content^="Starlight"]').length, current).toBe(1);
    for (const element of $('a[href]').toArray()) {
      const url = new URL($(element).attr('href')!, new URL(current, baseURL));
      if (url.origin !== new URL(baseURL!).origin || !destinations.has(url.pathname)) continue;
      if (!reached.has(url.pathname)) {
        reached.add(url.pathname);
        queue.push(url.pathname);
      }
    }
  }
  expect([...destinations].filter(url => !reached.has(url))).toEqual([]);
});

test.describe('navegación con 404 de directorio en caché', () => {
  test.beforeEach(async ({ page }) => {
    await page.route(url => subjects.some(subject => url.pathname.startsWith('/' + subject + '/')) && url.pathname.endsWith('/'),
      route => route.fulfill({ status: 404, contentType: 'text/html', body: '<h1>404</h1>' }));
  });

  test('tarjetas, unidades, paginación y menú funcionan en las cuatro materias', async ({ page, isMobile }) => {
    for (const subject of subjects) {
      const unitPath = `/${subject}/unidad-1/${subject === 'bbdd-aplicadas' ? 'teoria/' : ''}index.html`;
      await page.goto('/');
      await page.locator(`.sl-markdown-content a[href="/${subject}/index.html"]`).first().click();
      await expect(page).toHaveURL(`/${subject}/index.html`);
      await page.locator(`.sl-markdown-content a[href="${unitPath}"]`).first().click();
      await expect(page).toHaveURL(unitPath);
      await expect(page.locator('meta[name="generator"][content^="Starlight"]')).toHaveCount(1);
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
      const next = page.locator('a[rel="next"]');
      const nextHref = await next.getAttribute('href');
      await next.click();
      await expect(page).toHaveURL(nextHref!);
      await expect(page.locator('h1').first()).not.toHaveText('404');
      if (!isMobile) {
        const current = page.locator('.sidebar a[aria-current="page"]');
        await expect(current).toHaveAttribute('href', nextHref!);
        const groups = page.locator('.sidebar details').filter({ has: page.locator(`a[href="${unitPath}"]`) });
        for (const group of await groups.all()) {
          if (await group.getAttribute('open') === null) await group.locator(':scope > summary').click();
        }
        await page.locator(`.sidebar a[href="${unitPath}"]`).click();
        await expect(page).toHaveURL(unitPath);
      }
      if (isMobile) {
        await page.getByRole('button', { name: 'Menú de materias', exact: true }).click();
        await page.locator('#drawer a[href="/"]').first().click();
      } else {
        await page.locator('.nav-bar a[href="/"]').click();
      }
      await expect(page).toHaveURL('/');
    }
  });

  test('búsqueda y redirecciones históricas evitan los directorios', async ({ page }) => {
    for (const term of ['derivada', 'transacciones', 'patrones', 'autovalores']) {
      await page.goto('/');
      await page.getByRole('button', { name: 'Buscar', exact: true }).click();
      await page.locator('.pagefind-ui__search-input').fill(term);
      const result = page.locator('.pagefind-ui__result-link').first();
      await expect(result).toHaveAttribute('href', /\/index\.html(?:#.*)?$/);
      await result.click();
      await expect(page.locator('meta[name="generator"][content^="Starlight"]')).toHaveCount(1);
    }
    await page.goto('/diseno-de-software/diagramas.html?origen=legacy#uml-vs-mermaid');
    await expect(page).toHaveURL('/diseno-de-software/diagramas/index.html?origen=legacy#uml-vs-mermaid');
    await expect(page.locator('#uml-vs-mermaid')).toBeVisible();
  });

  test('las descargas migradas conservan rutas y bytes originales', async ({ request }) => {
    const response = await request.get('/bbdd-aplicadas/unidad-2/practica/archivos/starwars.json');
    expect(response.status()).toBe(200);
    expect(await response.body()).toEqual(readFileSync('public/bbdd-aplicadas/unidad-2/practica/archivos/starwars.json'));
  });

  test('los recursos retirados ya no se publican', async ({ request }) => {
    // migration/withdrawn.json registra su procedencia; npm run validate exige que no estén en public/ ni dist/.
    const withdrawn = JSON.parse(readFileSync('migration/withdrawn.json', 'utf8')).assets;
    for (const asset of withdrawn) {
      const response = await request.get('/' + asset.output.slice('public/'.length));
      expect(response.status(), asset.output).toBe(404);
    }
  });
});
