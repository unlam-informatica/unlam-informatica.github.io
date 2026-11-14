import { test, expect, type Locator, type Page } from '@playwright/test';
import { readdirSync, readFileSync } from 'node:fs';

async function openParents(scope: Locator, page: Page, href: string) {
  const groups = scope.locator('details').filter({ has: page.locator(`a[href="${href}"]`) });
  for (const group of await groups.all()) {
    if (await group.getAttribute('open') === null) await group.locator(':scope > summary').click();
  }
}

test('las seis unidades de BBDD solo contienen Teoría y Práctica', async ({ page }) => {
  for (let number = 1; number <= 6; number++) {
    const entries = readdirSync(`src/content/docs/bbdd-aplicadas/unidad-${number}`, { withFileTypes: true });
    expect(entries.every(entry => entry.isDirectory())).toBeTruthy();
    expect(entries.map(entry => entry.name).sort()).toEqual(['practica', 'teoria']);
  }
  await page.goto('/bbdd-aplicadas/index.html');
  const subject = page.locator('.sidebar .container-sidebar-entry').filter({
    has: page.getByRole('heading', { name: '2do año · BBDD Aplicadas', exact: true, includeHidden: true }),
  });
  const units = subject.locator(':scope > .container-group-link > details');
  await expect(units).toHaveCount(6);
  for (let index = 0; index < 6; index++) {
    const unit = units.nth(index);
    await expect(unit.locator(':scope > summary')).toHaveText(`Unidad ${index + 1}`);
    await expect(unit.locator(':scope > .container-group-link > a')).toHaveCount(0);
    const sections = unit.locator(':scope > .container-group-link > details > summary');
    await expect(sections).toHaveText(['Teoría', 'Práctica']);
  }
  const labels = await page.locator('.sidebar summary').allTextContents();
  expect(labels.some(label => /^(?:unidad-\d+|teoria|practica|geogebra)$/.test(label.trim()))).toBeFalsy();
});

test('cada unidad de BBDD permite abrir Teoría y Práctica desde el menú', async ({ page, isMobile }) => {
  await page.goto('/');
  for (let number = 1; number <= 6; number++) {
    for (const [section, label] of [['teoria', 'Teoría'], ['practica', 'Práctica']]) {
      if (isMobile) await page.getByRole('button', { name: 'Menú de materias', exact: true }).click();
      // Start on the homepage to exercise the mobile drawer even on splash pages.
      if (!isMobile && number === 1 && section === 'teoria') await page.goto('/bbdd-aplicadas/index.html');
      const menu = page.locator(isMobile ? '#drawer nav[aria-label="Materias y unidades"]' : '.sidebar');
      const href = `/bbdd-aplicadas/unidad-${number}/${section}/index.html`;
      await openParents(menu, page, href);
      await menu.locator(`a[href="${href}"]`).click();
      await expect(page).toHaveURL(href);
      await expect(page.locator('h1').first()).toHaveText(`Unidad ${number} — ${label}`);
      await expect(page.locator('meta[name="generator"][content^="Starlight"]')).toHaveCount(1);
    }
  }
});

test('las rutas anteriores de las unidades redirigen conservando consulta y ancla', async ({ page }) => {
  // Astro preview applies config redirects before serving files. GitHub Pages
  // serves the emitted HTML instead, so load those exact artifacts here.
  await page.route(url => /^\/bbdd-aplicadas\/unidad-\d+\/(?:index\.html)?$/.test(url.pathname), route => {
    const pathname = new URL(route.request().url()).pathname;
    const file = 'dist' + pathname + (pathname.endsWith('/') ? 'index.html' : '');
    return route.fulfill({ status: 200, contentType: 'text/html', body: readFileSync(file) });
  });
  for (let number = 1; number <= 6; number++) {
    for (const suffix of ['', 'index.html']) {
      await page.goto(`/bbdd-aplicadas/unidad-${number}/${suffix}?origen=legacy#teoría`);
      await expect(page).toHaveURL(`/bbdd-aplicadas/unidad-${number}/teoria/index.html?origen=legacy#teor%C3%ADa`);
      await expect(page.locator('#teoría')).toBeVisible();
    }
  }
});

test('Análisis y Diseño tienen unidades legibles y en orden', async ({ page }) => {
  await page.goto('/analisis-matematico-i/index.html');
  for (const [name, count] of [['1er año · Análisis Matemático I', 4], ['3er año · Diseño de Software', 6]] as const) {
    const subject = page.locator('.sidebar .container-sidebar-entry').filter({
      has: page.getByRole('heading', { name, exact: true, includeHidden: true }),
    });
    const units = subject.locator(':scope > .container-group-link > details > summary').filter({ hasText: /^Unidad / });
    await expect(units).toHaveText(Array.from({ length: count }, (_, index) => `Unidad ${index + 1}`));
  }
});
