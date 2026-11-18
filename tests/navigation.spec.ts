import { test, expect } from '@playwright/test';

test('portada por año y navegación contextual', async ({ page, isMobile }, testInfo) => {
  await page.goto('/');
  await page.screenshot({ path: testInfo.outputPath('portada.png'), fullPage: true, animations: 'disabled' });
  await testInfo.attach('Portada Lucode', { path: testInfo.outputPath('portada.png'), contentType: 'image/png' });
  for (const name of ['1er año','2do año','3er año']) await expect(page.getByRole('heading', { name, exact: true })).toBeVisible();
  await expect(page.locator('.sl-markdown-content a[href="/algebra-ii/index.html"]')).toBeVisible();
  await expect(page.getByText('Este sitio no es oficial', { exact: false })).toBeVisible();
  await page.locator('.sl-markdown-content a[href="/analisis-matematico-i/index.html"]').first().click();
  await expect(page).toHaveURL(/analisis-matematico-i\/index\.html$/);
  await page.locator('.sl-markdown-content a[href="/analisis-matematico-i/unidad-1/index.html"]').first().click();
  await expect(page).toHaveURL(/unidad-1\/index\.html$/);
  if (isMobile) {
    await page.getByRole('button', { name: 'Menú de materias', exact: true }).click();
    await expect(page.locator('#drawer')).toBeVisible();
    // Las materias del panel están colapsadas: se abre la materia y se elige su presentación.
    await page.locator('#drawer summary', { hasText: /^\s*Bases de Datos Aplicadas\s*$/ }).click();
    await page.locator('#drawer a[href="/bbdd-aplicadas/index.html"]').first().click();
    await expect(page).toHaveURL(/bbdd-aplicadas\/index\.html$/);
  }
});

test('fórmulas, diagramas y desborde móvil', async ({ page }) => {
  for (const route of ['/', '/analisis-matematico-i/unidad-1/practica/ejercicio-1/', '/bbdd-aplicadas/unidad-1/teoria/conceptos-basicos/', '/bbdd-aplicadas/como-estudiar/', '/bbdd-aplicadas/unidad-3/teoria/', '/bbdd-aplicadas/unidad-6/teoria/', '/diseno-de-software/unidad-3/teoria/']) {
    await page.goto(route);
    if (route.includes('ejercicio-1')) await expect(page.locator('.katex').first()).toBeVisible();
    if (route.includes('diseno-de-software')) await expect(page.locator('.mermaid svg').first()).toBeVisible({ timeout: 30000 });
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
  }
});

test('extractos de búsqueda con fórmulas en texto plano', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Buscar', exact: true }).click();
  await page.locator('.pagefind-ui__search-input').fill('inversa');
  await expect(page.locator('.pagefind-ui__result').first()).toBeVisible();
  const excerpts = (await page.locator('.pagefind-ui__result-excerpt').allInnerTexts()).join('\n');
  // KaTeX duplica cada fórmula (MathML, LaTeX y HTML): el índice solo debe tener una copia legible.
  expect(excerpts).not.toMatch(/\\(begin|frac|neq|left|right|mathbb)\b/);
  expect(excerpts).not.toMatch(/\^\{|_\{/);
});

test('búsqueda global', async ({ page }) => {
  for (const [term, subject] of [['derivada', 'analisis-matematico-i'], ['transacciones', 'bbdd-aplicadas'], ['patrones', 'diseno-de-software'], ['autovalores', 'algebra-ii']]) {
    await page.goto('/');
    await page.getByRole('button', { name: 'Buscar', exact: true }).click();
    const input = page.locator('.pagefind-ui__search-input');
    await input.fill(term);
    await expect(page.locator('.pagefind-ui__result').first()).toBeVisible();
    await expect(page.locator('.pagefind-ui__result-link').first()).toHaveAttribute('href', new RegExp(subject));
    await expect(page.locator('.pagefind-ui__result-link').first()).toHaveAttribute('href', /\/index\.html(?:#.*)?$/);
    await page.locator('.pagefind-ui__result-link').first().click();
    await expect(page.locator('h1').first()).not.toHaveText('404');
    await expect(page.locator('meta[name="generator"][content^="Starlight"]')).toHaveCount(1);
  }
});

test('redirecciones conservan fragmentos y consultas', async ({ page }) => {
  await page.goto('/diseno-de-software/diagramas.html?origen=legacy#uml');
  await expect(page).toHaveURL('/diseno-de-software/diagramas/index.html?origen=legacy#uml');
});

test('todos los diagramas Mermaid se renderizan', async ({ page }) => {
  test.setTimeout(180000);
  const { readFileSync, readdirSync } = await import('node:fs');
  const { join } = await import('node:path');
  const walk = (dir: string): string[] => readdirSync(dir, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(join(dir,e.name)) : [join(dir,e.name)]);
  const errors: string[] = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', msg => { if (msg.type() === 'error') console.log(page.url(), msg.text()); });
  for (const file of walk('dist').filter(f => f.endsWith('.html'))) {
    const count = (readFileSync(file,'utf8').match(/class="mermaid"/g) || []).length;
    if (!count) continue;
    await page.goto('/'+file.slice(5).replace(/index\.html$/, ''));
    // Mermaid renders sequentially; 31 diagrams can exceed 30s on shared CI runners.
    const renderTimeout = Math.max(30000, count * 3000);
    await expect(page.locator('.mermaid[data-processed="true"] svg'), file).toHaveCount(count, { timeout: renderTimeout });
    await expect.soft(page.getByText('Syntax error in text', { exact: false }), file).toHaveCount(0, { timeout: 500 });
  }
  expect(errors).toEqual([]);
});

test('Lucode conserva el aviso y permite alternar tema claro y oscuro', async ({ page }, testInfo) => {
  await page.goto('/analisis-matematico-i/unidad-1/practica/ejercicio-1/');
  await expect(page.locator('.disclaimer')).toBeVisible();
  await expect(page.locator('[data-slot="docs"]')).toBeVisible();
  const before = await page.locator('html').getAttribute('data-theme');
  await page.locator('starlight-theme-lucode-select button').click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', before === 'dark' ? 'light' : 'dark');
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-theme', before === 'dark' ? 'light' : 'dark');
  await expect(page.locator('.katex').first()).toBeVisible();
  await page.screenshot({ path: testInfo.outputPath('apunte-tema-alternativo.png'), animations: 'disabled' });
  await testInfo.attach('Apunte Lucode', { path: testInfo.outputPath('apunte-tema-alternativo.png'), contentType: 'image/png' });
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
});

test('Álgebra II: fórmulas, figuras, resoluciones plegadas y tema oscuro', async ({ page }) => {
  await page.goto('/algebra-ii/unidad-1/practica/nivel-inicial/');
  await expect(page.locator('.katex').first()).toBeVisible();
  const solution = page.locator('.sl-markdown-content details').first();
  await expect(solution.locator('summary')).toHaveText(/Resolución/);
  await expect(solution.locator('.katex').first()).toBeHidden();
  await solution.locator('summary').click();
  await expect(solution.locator('.katex').first()).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
  await page.goto('/algebra-ii/unidad-4/teoria/proyeccion-y-distancia/');
  const figure = page.locator('.math-figure svg').first();
  await expect(figure).toBeVisible();
  await expect(figure).toHaveAttribute('role', 'img');
  // Los trazos usan los tokens del tema: el color cambia al alternar claro y oscuro.
  const stroke = () => figure.locator('[class*="vec-"], [class*="line-"]').first().evaluate(e => getComputedStyle(e).stroke);
  const before = await stroke();
  await page.locator('starlight-theme-lucode-select button').click();
  await expect.poll(stroke).not.toBe(before);
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
});

test('el header tiene un menú por año con sus materias en orden alfabético', async ({ page, isMobile }) => {
  test.skip(isMobile, 'En móvil las materias se eligen desde el panel lateral.');
  await page.goto('/');
  const triggers = page.locator('.year-menu-trigger');
  await expect(triggers).toHaveText(['1er año', '2do año', '3er año']);
  await expect(page.locator('.nav-bar a')).toHaveText(['Inicio']);
  const third = page.getByRole('button', { name: '3er año', exact: true });
  await third.click();
  await expect(third).toHaveAttribute('aria-expanded', 'true');
  const panel = page.locator('#year-menu-3');
  await expect(panel).toBeVisible();
  await expect(panel.locator('a')).toHaveText(['Álgebra y Geometría Analítica II', 'Diseño de Software']);
  await page.keyboard.press('Escape');
  await expect(panel).toBeHidden();
  await expect(third).toHaveAttribute('aria-expanded', 'false');
  await third.click();
  await panel.getByRole('link', { name: 'Diseño de Software' }).click();
  await expect(page).toHaveURL('/diseno-de-software/index.html');
  await expect(page.getByRole('button', { name: '3er año', exact: true })).toHaveClass(/active/);
});

test('la columna de lectura es más ancha sin desbordar ni pisar el índice', async ({ page, isMobile }) => {
  test.skip(isMobile, 'En móvil la columna ocupa todo el ancho.');
  for (const [width, expected] of [[1440, 736], [1280, 664], [1024, 688]] as const) {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('/algebra-ii/unidad-1/teoria/subespacios/');
    const content = await page.locator('.sl-markdown-content').boundingBox();
    expect(Math.round(content!.width)).toBe(expected);
    const toc = page.locator('[data-slot="docs"] > .toc');
    if (await toc.isVisible()) expect(content!.x + content!.width).toBeLessThanOrEqual((await toc.boundingBox())!.x);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
  }
});
