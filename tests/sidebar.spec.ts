import { test, expect, type Locator, type Page } from '@playwright/test';
import { readdirSync, readFileSync } from 'node:fs';

async function openParents(scope: Locator, page: Page, href: string) {
  const groups = scope.locator('details').filter({ has: page.locator(`a[href="${href}"]`) });
  for (const group of await groups.all()) {
    if (await group.getAttribute('open') === null) await group.locator(':scope > summary').click();
  }
}

// Grupo de una materia dentro del encabezado «Materias»: materia → unidades.
function subjectGroup(page: Page, name: string) {
  const subjectsEntry = page.locator('.sidebar .container-sidebar-entry').filter({
    has: page.getByRole('heading', { name: 'Materias', exact: true, includeHidden: true }),
  });
  return subjectsEntry.locator(':scope > .container-group-link > details').filter({
    has: page.locator(':scope > summary', { hasText: new RegExp(`^\\s*${name}\\s*$`) }),
  });
}

test('las seis unidades de BBDD solo contienen Teoría y Práctica', async ({ page }) => {
  for (let number = 1; number <= 6; number++) {
    const entries = readdirSync(`src/content/docs/bbdd-aplicadas/unidad-${number}`, { withFileTypes: true });
    expect(entries.every(entry => entry.isDirectory())).toBeTruthy();
    expect(entries.map(entry => entry.name).sort()).toEqual(['practica', 'teoria']);
  }
  await page.goto('/bbdd-aplicadas/index.html');
  const subject = subjectGroup(page, 'Bases de Datos Aplicadas');
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
  for (const [name, count] of [['Análisis Matemático I', 4], ['Diseño de Software', 6]] as const) {
    const subject = subjectGroup(page, name);
    const units = subject.locator(':scope > .container-group-link > details > summary').filter({ hasText: /^Unidad / });
    await expect(units).toHaveText(Array.from({ length: count }, (_, index) => `Unidad ${index + 1}`));
  }
});

test('Álgebra II tiene repaso, cuatro unidades con teoría y práctica, y simulacros', async ({ page }) => {
  await page.goto('/algebra-ii/index.html');
  const subject = subjectGroup(page, 'Álgebra y Geometría Analítica II');
  const groups = subject.locator(':scope > .container-group-link > details > summary');
  await expect(groups).toHaveText([
    'Repaso de Álgebra I',
    'Unidad 1 · Espacios vectoriales',
    'Unidad 2 · Transformaciones lineales',
    'Unidad 3 · Autovalores y autovectores',
    'Unidad 4 · Espacios con producto interno',
    'Integradores y simulacros',
  ]);
  for (let number = 1; number <= 4; number++) {
    const unit = subject.locator(':scope > .container-group-link > details').nth(number);
    await expect(unit.locator(':scope > .container-group-link > a')).toHaveCount(1);
    await expect(unit.locator(':scope > .container-group-link > details > summary')).toHaveText(['Teoría', 'Práctica']);
  }
});

test('el menú lateral lista todas las materias en orden alfabético, colapsadas salvo la actual', async ({ page }) => {
  await page.goto('/bbdd-aplicadas/index.html');
  await expect(page.locator('.sidebar .container-sidebar-entry > .entry-title')).toHaveText(['Materias']);
  const subjects = page.locator('.sidebar .container-sidebar-entry > .container-group-link > details');
  const names = (await subjects.locator(':scope > summary').allTextContents()).map(text => text.trim());
  expect(names).toEqual(['Álgebra y Geometría Analítica II', 'Análisis Matemático I', 'Bases de Datos Aplicadas', 'Diseño de Software']);
  expect(names).toEqual([...names].sort((a, b) => a.localeCompare(b, 'es', { sensitivity: 'base' })));
  const open = await subjects.evaluateAll(groups => groups.filter(group => (group as HTMLDetailsElement).open)
    .map(group => group.querySelector(':scope > summary')!.textContent!.trim()));
  expect(open).toEqual(['Bases de Datos Aplicadas']);
});

test('los títulos largos del menú no se superponen', async ({ page, isMobile }) => {
  test.skip(isMobile, 'El menú lateral fijo solo existe en escritorio.');
  await page.goto('/algebra-ii/como-estudiar/index.html');
  const summaries = await page.locator('.sidebar details[open] > summary').evaluateAll(nodes => nodes
    .filter(node => (node as HTMLElement).checkVisibility())
    .map(node => { const box = node.getBoundingClientRect(); const label = node.querySelector('.entry-link-inner')!.getBoundingClientRect(); return { top: box.top, bottom: box.bottom, labelBottom: label.bottom }; }));
  expect(summaries.length).toBeGreaterThan(0);
  for (const box of summaries) expect(box.labelBottom).toBeLessThanOrEqual(box.bottom + 0.5);
  const all = await page.locator('.sidebar .entry-group > summary, .sidebar a.entry-link').evaluateAll(nodes => nodes
    .filter(node => (node as HTMLElement).checkVisibility())
    .map(node => node.getBoundingClientRect()).map(box => [box.top, box.bottom])
    .sort((a, b) => a[0] - b[0]));
  for (let index = 1; index < all.length; index++) expect(all[index][0]).toBeGreaterThanOrEqual(all[index - 1][1] - 0.5);
});
