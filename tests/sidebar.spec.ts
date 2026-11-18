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

const bbddUnits = [
  'Conceptos básicos y SQL',
  'Relacionales: aspectos básicos',
  'Relacionales: aspectos avanzados',
  'No relacionales',
  'Protección de los datos',
  'Calidad en bases de datos',
];
const bbddTitles = [
  'Conceptos básicos',
  'Bases de datos relacionales: aspectos básicos',
  'Bases de datos relacionales: aspectos avanzados',
  'Bases de datos no relacionales',
  'Protección de los datos',
  'Calidad en bases de datos',
];

test('BBDD: presentación, cómo estudiar y seis unidades con ruta, teoría, práctica y repaso', async ({ page }) => {
  for (let number = 1; number <= 6; number++) {
    const entries = readdirSync(`src/content/docs/bbdd-aplicadas/unidad-${number}`, { withFileTypes: true });
    expect(entries.every(entry => entry.isDirectory())).toBeTruthy();
    expect(entries.map(entry => entry.name).sort()).toEqual(['practica', 'teoria']);
  }
  await page.goto('/bbdd-aplicadas/index.html');
  const subject = subjectGroup(page, 'Bases de Datos Aplicadas');
  await expect(subject.locator(':scope > .container-group-link > a')).toHaveText(['Presentación', 'Cómo estudiar']);
  const units = subject.locator(':scope > .container-group-link > details');
  await expect(units).toHaveCount(6);
  for (let index = 0; index < 6; index++) {
    const number = index + 1;
    const unit = units.nth(index);
    await expect(unit.locator(':scope > summary')).toHaveText(`Unidad ${number} · ${bbddUnits[index]}`);
    const links = unit.locator(':scope > .container-group-link > a');
    // Las unidades con resumen integrador y guía (4 a 6) los muestran al final, fuera de Teoría.
    await expect(links).toHaveText(number >= 4
      ? ['Presentación y ruta', 'Resumen integrador', number === 4 ? 'Guía para el parcial' : 'Guía de repaso']
      : ['Presentación y ruta']);
    await expect(links.first()).toHaveAttribute('href', `/bbdd-aplicadas/unidad-${number}/teoria/index.html`);
    await expect(unit.locator(':scope > .container-group-link > details > summary')).toHaveText(['Teoría', 'Práctica']);
    // La presentación no se repite dentro de Teoría.
    await expect(unit.locator(`details a[href="/bbdd-aplicadas/unidad-${number}/teoria/index.html"]`)).toHaveCount(0);
  }
  // Las páginas puente históricas no son lecciones del recorrido.
  for (const legacy of ['unidad-1/teoria/indice-cluster', 'unidad-2/practica/transacciones']) {
    await expect(subject.locator(`a[href="/bbdd-aplicadas/${legacy}/index.html"]`)).toHaveCount(0);
  }
  const hrefs = await subject.locator('a').evaluateAll(links => links.map(link => link.getAttribute('href')));
  expect(new Set(hrefs).size).toBe(hrefs.length);
  const labels = await page.locator('.sidebar summary').allTextContents();
  expect(labels.some(label => /^(?:unidad-\d+|teoria|practica|geogebra)$/.test(label.trim()))).toBeFalsy();
});

test('BBDD: la teoría de cada unidad sigue el orden de su ruta de aprendizaje', async ({ page }) => {
  for (let number = 1; number <= 6; number++) {
    await page.goto(`/bbdd-aplicadas/unidad-${number}/teoria/index.html`);
    // Enlaces de la sección «Ruta de aprendizaje», en orden de documento, hasta el h2 siguiente.
    const route = await page.locator('.sl-markdown-content').evaluate(content => {
      const paths: string[] = [];
      let inside = false;
      for (const node of content.querySelectorAll('h2, a[href]')) {
        if (node.tagName === 'H2') { inside = node.id === 'ruta-de-aprendizaje'; continue; }
        // Los enlaces a una sección (con ancla) pueden adelantar una parte de otra lección; la
        // posición de cada lección en la ruta la da su primer enlace a la página completa.
        const url = new URL(node.getAttribute('href')!, location.href);
        if (inside && !url.hash) paths.push(url.pathname);
      }
      return paths;
    });
    const subject = subjectGroup(page, 'Bases de Datos Aplicadas');
    const theory = subject.locator(':scope > .container-group-link > details').nth(number - 1)
      .locator(':scope > .container-group-link > details').first();
    const menu = await theory.locator('a').evaluateAll(links => links.map(link => link.getAttribute('href')));
    expect(menu.length).toBeGreaterThan(0);
    // Primera aparición de cada lección del menú en la ruta: deben venir en el mismo orden.
    const positions = menu.map(href => route.indexOf(href!));
    expect(positions.every(position => position >= 0), `Lecciones fuera de la ruta: ${menu.filter((_, i) => positions[i] < 0)}`).toBeTruthy();
    expect(positions).toEqual([...positions].sort((a, b) => a - b));
  }
});

test('BBDD: la portada lleva a Cómo estudiar y a la ruta de la Unidad 1', async ({ page }) => {
  await page.goto('/bbdd-aplicadas/index.html');
  await page.locator('.sl-markdown-content a[href="/bbdd-aplicadas/como-estudiar/index.html"]').first().click();
  await expect(page.locator('h1').first()).toHaveText('Cómo estudiar esta materia');
  for (const id of ['método-de-estudio', 'herramientas', 'evaluación', 'aprender-desde-cero', 'repasar-para-un-examen']) {
    await expect(page.locator(`[id="${id}"]`)).toHaveCount(1);
  }
  // «Siguiente» sigue el orden del menú: de Cómo estudiar a la presentación de la Unidad 1.
  await page.locator('.pagination-links a[rel="next"]').click();
  await expect(page).toHaveURL('/bbdd-aplicadas/unidad-1/teoria/index.html');
  await expect(page.locator('h1').first()).toHaveText('Unidad 1 — Conceptos básicos');
});

test('cada unidad de BBDD permite abrir su ruta y su práctica desde el menú', async ({ page, isMobile }) => {
  await page.goto('/');
  for (let number = 1; number <= 6; number++) {
    for (const [section, title] of [['teoria', `Unidad ${number} — ${bbddTitles[number - 1]}`], ['practica', `Unidad ${number} — Práctica`]]) {
      if (isMobile) await page.getByRole('button', { name: 'Menú de materias', exact: true }).click();
      // Start on the homepage to exercise the mobile drawer even on splash pages.
      if (!isMobile && number === 1 && section === 'teoria') await page.goto('/bbdd-aplicadas/index.html');
      const menu = page.locator(isMobile ? '#drawer nav[aria-label="Materias y unidades"]' : '.sidebar');
      const href = `/bbdd-aplicadas/unidad-${number}/${section}/index.html`;
      await openParents(menu, page, href);
      await menu.locator(`a[href="${href}"]`).click();
      await expect(page).toHaveURL(href);
      await expect(page.locator('h1').first()).toHaveText(title);
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
      await page.goto(`/bbdd-aplicadas/unidad-${number}/${suffix}?origen=legacy#ruta-de-aprendizaje`);
      await expect(page).toHaveURL(`/bbdd-aplicadas/unidad-${number}/teoria/index.html?origen=legacy#ruta-de-aprendizaje`);
      await expect(page.locator('#ruta-de-aprendizaje')).toBeVisible();
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
